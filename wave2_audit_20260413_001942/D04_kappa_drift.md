# D04_kappa_drift (656s)

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1426](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1426) — PROBLEM: `\kappa` is treated as a central basis vector and cohomology generator: `Z(\mathcal H_\kappa)=\mathbb C\cdot\mathbf1\oplus\mathbb C\cdot\kappa`, `\rho(\kappa)`, `Q_1(\mathcal H_\kappa)=\mathbb C\cdot\kappa`. That collapses a scalar level/modular characteristic into an algebra element. FIX: introduce a new genus-1 class symbol, e.g. `z_{\mathrm{cen}}`, and rewrite this lane as `Q_1(\mathcal H_\kappa)=\mathbb C\cdot z_{\mathrm{cen}}`, `\rho(z_{\mathrm{cen}})(\alpha)=\lambda_1\cup\alpha`; keep the coefficient separate as `\kappa(\mathcal H_\kappa)=\kappa`. Apply the same replacement at lines 1427-1435, 1727-1729, 2505-2513, 2538-2544, and 2791.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:2322](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:2322) — PROBLEM: the Heisenberg section says “The central charge `\kappa` now appears in”, reidentifying the Heisenberg level/modular characteristic as a central charge. FIX: change the sentence to `The Heisenberg level, equivalently the modular characteristic \kappa(\mathcal H_\kappa)=\kappa, now appears in:`; if central charge is needed, write it separately as `c(\mathcal H)=1`.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:3816](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:3816) — PROBLEM: in the genus-1 Heisenberg example, `\kappa` is again called “the central charge”. FIX: rewrite line 3816 as `where \kappa=\kappa(\mathcal H_\kappa)` is the Heisenberg level/modular characteristic, and `[1]^{(1)}` is the genus-1 identity element`; also change line 3790 to `For the Heisenberg vertex algebra \mathcal H_\kappa at level \kappa`.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:4901](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4901) — PROBLEM: the file reuses bare `\kappa` for the Casimir element `\sum_a J^a\otimes J_a`, colliding with the chapter’s obstruction-coefficient `\kappa`. FIX: replace the Casimir symbol by `\Omega` in this subsection: `m_0=\frac{k+h^\vee}{2h^\vee}\Omega`, `\Omega=\sum_a J^a\otimes J_a`, and update downstream mentions accordingly.

- [HIGH] [chapters/examples/kac_moody.tex:521](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:521) — PROBLEM: `kac_moody.tex` defines `m_0=((k+h^\vee)/(2h^\vee))\kappa` with `\kappa` the Casimir element, despite the manuscript’s own rule that the Casimir should be `\Omega` to avoid confusion with the modular characteristic. FIX: replace the Casimir symbol by `\Omega` at lines 511, 521-523, 966, 1180-1182, and 1955; reserve `\kappa(\widehat{\mathfrak g}_k)` for the scalar modular characteristic.

- [HIGH] [chapters/examples/w_algebras_deep.tex:1642](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:1642) — PROBLEM: `\kappa` is used for the `\mathfrak{sl}_3` Casimir element inside a chapter that already uses `\kappa` for the modular characteristic of `\mathcal W_3` and `\mathcal W_N`. FIX: rename the Lie-theoretic tensor to `\Omega_{\mathfrak{sl}_3}` and rewrite the paragraph as `the Casimir element \Omega_{\mathfrak{sl}_3} ... maps \Omega_{\mathfrak{sl}_3}\cdot (k+3)/6 \mapsto (k+3)`.

- [HIGH] [chapters/theory/cobar_construction.tex:2519](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2519) — PROBLEM: the universal central-extension relation calls bare `\kappa` “the central charge”. In this repo `\kappa` is the modular characteristic, not a generic central-extension parameter. FIX: change the coefficient in line 2517 to a new symbol, e.g. `t_{\mathrm{cen}}`, and rewrite lines 2519-2522 and 2527-2528 as `t_{\mathrm{cen}}`/`\omega_{\mathrm{cen}}`, not `\kappa`.

- [HIGH] [chapters/theory/cobar_construction.tex:2544](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2544) — PROBLEM: `\kappa(V_k(\mathfrak g))=\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)` is said to recover the Sugawara central charge. It does not; the Sugawara central charge is `c(V_k(\mathfrak g))=k\dim(\mathfrak g)/(k+h^\vee)`. FIX: replace `recovering the Sugawara central charge` with `distinct from the Sugawara central charge`, and append the explicit central-charge formula.

- [HIGH] [chapters/examples/deformation_quantization.tex:457](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:457) — PROBLEM: Example 1 defines bare `\kappa` as a propagator integral deformation parameter, while the same file later uses canonical family-valued `\kappa(\widehat{\fg}_k)`. That makes bare `\kappa` denote two different invariants in one chapter. FIX: rename the local parameter throughout Example 1 to `t_{\mathrm{dq}}`: `a(z)a^*(w)\sim t_{\mathrm{dq}}/(z-w)`, `t_{\mathrm{dq}}=\hbar\int_{\overline C_2(X)}\eta_{12}`, and add `t_{\mathrm{dq}}` is not the modular characteristic `\kappa(\cA)`.

- [HIGH] [chapters/examples/deformation_quantization.tex:554](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:554) — PROBLEM: `\kappa(\tau)=\kappa_0E_2(\tau)` makes `\kappa` into a `\tau`-dependent quasi-modular function, conflicting with the manuscript’s use of `\kappa(\cA)` as a fixed invariant of the algebra. FIX: replace this by a new symbol such as `A_{\mathrm{ell}}(\tau)=A_0E_2(\tau)` and state explicitly that the quasi-modular dependence belongs to the genus-1 propagator coefficient, not to `\kappa(\cA)`.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:3137](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3137) — PROBLEM: the file calls `\kappa(V_k(\fg))` a “total holographic central charge”, collapsing `\kappa` and `c`. The repo elsewhere explicitly distinguishes them. FIX: replace `central charge` by `modular characteristic` or `obstruction coefficient` here, and make the same wording change at lines 11928 and 11984; if a central charge is intended, write the separate Sugawara `c(V_k(\fg))`.

- [MEDIUM] [chapters/theory/quantum_chiral_algebras.tex:202](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:202) — PROBLEM: Vol III uses bare `\kappa` for an invariant pairing `\frakg\otimes\frakg\to\C`, violating the volume’s own kappa-discipline and colliding with the modular-characteristic notation. FIX: rename the pairing to `B_{\frak g}` or `(-,-)_{\frak g}` at lines 202, 204, and 209.

- [MEDIUM] [chapters/theory/higher_genus_foundations.tex:5858](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5858) — PROBLEM: the corollary is titled and stated as `\kappa`-periodicity, but the displayed formula is affine-linear: `\kappa(k+n)=\kappa(k)+n\,d/(2h^\vee)`. That is not periodic. FIX: rename the heading and first sentence to `Affine-linear level-shift formula for \kappa` / `\kappa shifts affinely under integral level translation`; keep the formula itself.

- [MEDIUM] [chapters/examples/landscape_census.tex:1416](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:1416) — PROBLEM: the canonical `\mathcal W_N` formula uses `H_N-1` without defining `H_N` in the same sentence, on the exact seam where this repo repeatedly drifts between `H_N-1` and `H_{N-1}`. FIX: rewrite the line as `General \mathcal W_N: \kappa(\mathcal W_N)=c\sum_{j=2}^{N}1/j = c(H_N-1),\; H_N=\sum_{j=1}^{N}1/j.`

- [LOW] [chapters/theory/quantum_chiral_algebras.tex:460](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:460) — PROBLEM: `The \kappa-spectrum check` reintroduces bare `\kappa` even though the actual quantities are `\kappa_{\mathrm{ch}}` and `\kappa_{\mathrm{BKM}}`. FIX: change the phrase to `the $(\kappa_{\mathrm{ch}},\kappa_{\mathrm{BKM}})$-spectrum check` or `the modular-characteristic spectrum check`.

## Summary
Checked: 5973 | Findings: 15 | Verdict: FAIL


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
session id: 019d8418-b5fe-72d1-8578-b6fa9b9eafac
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

Find EVERY instance of \kappa in chapters/theory/ and chapters/examples/. For each: (a) is the family specified? (b) is the formula correct? (c) is it consistent with landscape_census.tex? Focus on instances where bare kappa could mean different things.

Search ALL three volumes:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding: exact file:line, PROBLEM, and EXACT FIX.
mcp startup: no servers



thinking
**Determining audit parameters**

I need to work as a coding agent in the repository. The user has requested an adversarial audit, but it seems they don't want me to make edits, just to review. They want me to find instances of a specific symbol across all three volumes. I think I can read the necessary directories, but I’ll need to double-check what the workspace allows. While it’s focused on auditing, I might still need to familiarize myself with some pertinent files.
thinking
**Planning the audit for \kappa**

I need to search for every instance of \kappa across the theory and examples chapters in all three volumes. The instructions are clear: I should find all occurrences in the specified paths. It sounds like it’s important to capture every instance of \kappa, particularly those that are ambiguous. This could result in a significant number of results, so I need to prepare for a thorough inspection of possibly hundreds of instances. Using an explorer subagent might be a good approach to facilitate the search.
thinking
**Planning to use explorer**

I think using the explorer could be a good way to handle the search since it’s faster and more authoritative. However, I need to ensure we actually read the file contents as part of the process. The explorer can search and summarize, but grounding my findings is crucial. I should consider using shell commands like `rg` for efficient searching. It seems I’ll need to provide commentary updates at regular intervals as I work on this. I should also mention my areas of expertise while doing so.
codex
Audit surface is all `\kappa` occurrences across the three volume chapter trees, with emphasis on bare or ambiguous uses against the canonical census. I’m starting by reading the minimal constitutional files and then doing a repository-wide grep so the findings are grounded in live source, not repo folklore.


thinking
**Planning exploration tools**

I think I should spawn an explorer agent to search through the codebase. I need specific file lines and direct quotes, so I'll start with the explorer for an initial scan and then manually verify with the shell. The instructions suggest asking explorers first, which makes sense. It would be good to have one explorer per volume since tasks can be parallelized. I’m curious if the explorer can read outside the workspace, but that might depend on access. Let's get started on this!
thinking
**Auditing steps**

Since we're auditing, I'll focus on using deep-beilinson-audit and possibly multi-path-verify to check for formula correctness. I definitely need to read their SKILL.md for more context. It seems like claim-surface-sync might not be necessary since we aren’t editing the status. I think it's best to read just enough to gather the essential information needed for the audit without going overboard. Let's go ahead with this plan!
codex
Using `deep-beilinson-audit` for the adversarial sweep and `multi-path-verify` for the formula checks. Next step is to load the audit workflow and the canonical formula surface, then fan out the grep across the three volumes.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

I need to audit all occurrences of "kappa." I might consider using an explorer or shell for this task. Formulating a clear plan seems essential since the user wants exhaustive and exact line references. I should probably run rg to gather all occurrences with line numbers from across the volumes. Also, I might need to directly compare data with landscape_census.tex and read the relevant lines within the repo chapters or connections. So, let’s start searching!
codex
The audit protocol is loaded. I’m locating the canonical `\kappa` census and building the full occurrence list across all three volumes before classifying anything, because the main failure mode here is drift plus local redefinitions.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.out'"' '\\\\kappa' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 7021

chapters/examples/deformation_quantization.tex:19: curvature $\kappa(\cA) \cdot \omega_g$, and the quantized algebra is
chapters/examples/deformation_quantization.tex:35:governed by~$\kappa(\cA)$.
chapters/examples/deformation_quantization.tex:451:\[a(z) a^*(w) \sim \frac{\kappa}{z-w}\]
chapters/examples/deformation_quantization.tex:453:The level $\kappa$ is the first quantum correction, measuring the failure of commutativity.
chapters/examples/deformation_quantization.tex:457:\[\kappa = \hbar \int_{\overline{C}_2(X)} \eta_{12}\]
chapters/examples/deformation_quantization.tex:459:For $X = \mathbb{C}$: $\kappa = \hbar$ (the propagator integral evaluates to $1$)
chapters/examples/deformation_quantization.tex:461:For $X = E$ (elliptic curve): The deformation quantization on $E$ exists but the level $\kappa$ depends on the choice of propagator (Green's function on $E$). The Euler characteristic $\chi(E) = 0$ constrains the anomaly but does not force $\kappa = 0$; rather, the star product on $E$ is governed by the elliptic propagator $\partial_z G(z,w)$.
chapters/examples/deformation_quantization.tex:554:\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
chapters/examples/deformation_quantization.tex:1053:For the Heisenberg algebra $\mathcal{H}_\kappa$ with Coisson
chapters/examples/deformation_quantization.tex:1055:$\{a_\lambda b\}_{\mathrm{cl}} = \kappa$ (a constant Poisson
chapters/examples/deformation_quantization.tex:1060:\frac{\hbar \kappa}{2}
chapters/examples/deformation_quantization.tex:1069:\emph{Order $\hbar^1$:} $a \star_1 b = \frac{\kappa}{2}
chapters/examples/deformation_quantization.tex:1071:(\partial^{(n)} b) = \frac{\kappa}{2} a_{(0)}b$ (the
chapters/examples/deformation_quantization.tex:1076:a \star_2 b &= \frac{\kappa^2}{8}
chapters/examples/deformation_quantization.tex:1079:&= \frac{\kappa^2}{8} a_{(0)(0)}b
chapters/examples/deformation_quantization.tex:1082:$a \star_2 a = \frac{\kappa^2}{8} \cdot 0 = 0$ (the iterated
chapters/examples/deformation_quantization.tex:1092:a \star b = \normord{ab} + \frac{\hbar\kappa}{2} a_{(0)}b
chapters/examples/deformation_quantization.tex:1099:$\mathcal{H}_\kappa$: the bar complex has no higher $A_\infty$
exec
/bin/zsh -lc "rg -n --hidden 'landscape_census\\.tex|\\\\chapter\\{.*landscape|\\\\section\\{.*landscape|kappa\\(V_k|kappa\\(Vir|kappa\\(H_k|kappa\\(W_N' . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 331ms:
./AGENTS.md:157:Verify against these AND `landscape_census.tex` before writing. NEVER write kappa from memory (AP1).
./AGENTS.md:161:kappa(H_k) = k                                       # Heisenberg; k=0→0, k=1→1
./AGENTS.md:162:kappa(Vir_c) = c/2                                    # Virasoro ONLY; c=0→0, c=13→13/2
./AGENTS.md:163:kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)                 # Affine KM; k=0→dim(g)/2 (NOT 0), k=-h^v→0
./AGENTS.md:164:kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^N 1/j      # W_N; N=2: H_2-1=1/2 so kappa=c/2=Vir
./AGENTS.md:224:B7.  kappa(W_N) = c*H_{N-1}            # MUST be c*(H_N - 1)
./AGENTS.md:319:Before ANY kappa: (a) identify family, (b) open landscape_census.tex and copy formula, (c) paste with AP1 comment, (d) evaluate at two boundary values.
./AGENTS.md:378:source: [landscape_census.tex:LINE / compute/...]
./AGENTS.md:385:census: landscape_census.tex:LINE = [_]  match? [Y/N]
./AGENTS.md:648:7. Never guess a formula: compute or cite landscape_census.tex (AP1)
./audit_campaign_20260412_230832/F14_averaging.md:64:7. Also check landscape_census.tex for the canonical source
./audit_campaign_20260412_230832/F12_MC_equation.md:64:7. Also check landscape_census.tex for the canonical source
./audit_campaign_20260412_230832/BC03_c_zero.md:54:Find ALL formulas involving central charge c. At c=0: kappa(Vir)→0, kappa(Heis at k=0)→0. Check: does the theory degenerate gracefully?
./audit_campaign_20260412_230832/F20_WN_weights.md:64:7. Also check landscape_census.tex for the canonical source
./audit_campaign_20260412_230832/AP03_wrong_WN_kappa.md:52:MISSION: Sweep for AP136/B7: kappa(W_N) = c*H_{N-1} across all three volumes.
./audit_campaign_20260412_230832/F01_kappa_KM.md:54:CANONICAL: kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
./audit_campaign_20260412_230832/F01_kappa_KM.md:64:7. Also check landscape_census.tex for the canonical source
./audit_campaign_20260412_230832/F04_kappa_WN.md:54:CANONICAL: kappa(W_N) = c*(H_N - 1)
./audit_campaign_20260412_230832/F04_kappa_WN.md:64:7. Also check landscape_census.tex for the canonical source
./audit_campaign_20260412_230832/F19_arnold_KZ.md:64:7. Also check landscape_census.tex for the canonical source




thinking
**Organizing search tasks**

I need to conduct a thorough search for every instance of \kappa in the specified chapters, both in theory and examples. The user's mission asks if the family is specified, if the formula is correct, and its consistency with landscape_census.tex. I should focus on chapters from both volumes and make sure I understand the specifics, especially since the structure appears complex with many connections. Let's carefully parse their request to ensure we're auditing the right sections.
thinking
**Searching for \kappa instances**

I should focus on the theory and examples subdirectories within each volume's chapters while considering all chapter files across the three volumes to ensure thoroughness. However, I need to zero in on findings that are actually problematic rather than just listing safe occurrences. It's essential to identify every instance of \kappa, check them, and only report the problematic ones. I might also want to compute the total number checked and gather specific line numbers along with potential fixes for clarity.
thinking
**Planning review automation**

I need to actually review file contents around specific lines. Given the scale of the task, it makes sense to automate the extraction and use heuristics, then manually verify the candidate findings. Since we're in a network-restricted environment, I could utilize tools like rg and scripts in shell, such as awk or perl, to help streamline the process. There's no need to make edits at this stage, just focus on extraction and verification.
thinking
**Exploring data processing tools**

I’m weighing whether to use shell commands or Python scripts for analysis. The guidelines suggest using shell for simpler tasks, but Python can handle more complex data processing. I feel like employing shell with tools like `rg` might be sufficient for searching directly through data files, especially to find specific lines in `landscape_census.tex`. I should also check for canonical formulas, particularly around kappa values in the specified volumes. Let's take a closer look!
codex
The raw grep is too wide to trust directly. I’m reducing it to a candidate set: explicit formulas, bare scalar uses, and Vol III notation collisions, then I’ll verify each candidate in file context against the census rather than pattern-matching line fragments.
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1180,1275p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa\\s*\\(|\\\\kappa\\s*=|\\\\kappa_[A-Za-z]|\\\\kappa\\"'^|bare kappa|'"\\\\kappa\\b' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1398,1435p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '2120,2175p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1398	genus and semi-infinite calculations; the stronger H-level
  1399	infinite-generator realization is delegated to the exact
  1400	$W_\infty$ MC4 package of filtered H-level targets, residue identities,
  1401	and finite detection on $\mathcal{I}_N$, whose first live
  1402	higher-spin stages are already reduced on the theorem surface to the
  1403	stage-$3$ fifteen-coefficient packet and the stage-$4$
  1404	exact six-entry identity packet on~$\mathcal{I}_4$, organized as three
  1405	local OPE blocks and splitting into four higher-spin channels together
  1406	with two Virasoro-target channels whose principal values are fixed and
  1407	whose residue-side contraction requires the normalized two-point/Ward
  1408	package of Corollary~\ref{cor:winfty-stage4-residue-four-channel}. The
  1409	first next reduced stage is the explicit eleven-entry packet
  1410	$\mathcal{J}_5^{\mathrm{red}}$ of
  1411	Corollary~\ref{cor:winfty-ds-stage5-reduced-packet}.
  1412	Complete genus-$1$ pipelines for $\mathrm{Vir}_c$
  1413	(\S\ref{sec:virasoro-genus-one-pipeline}, $c + c' = 26$, $\kappa = c/2$)
  1414	and $\mathcal{W}_3^k$
  1415	(\S\ref{sec:w3-genus-one-pipeline}, $c + c' = 100$, $\kappa = 5c/6$).
  1416	General $\mathcal{W}_N$: $\kappa = c \cdot (H_N - 1)$
  1417	(Theorem~\ref{thm:wn-obstruction}).
 succeeded in 52ms:
15:$\kappa$, the cubic and quartic shadow coefficients $S_3$ and $S_4$,
16:and the critical discriminant $\Delta = 8\kappa S_4$. The
24:structure of the MC element $\Theta_\cA$: once $\kappa$ and $S_4$
32:The scalar modular characteristic $\kappa(\widehat{\fg}_k) = td/2h^\vee$
33:and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
48:obstruction coefficient $\kappa(\cA)$ from the genus universality
49:theorem $\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
68: & $\boldsymbol{\kappa(\cA)}$ & \textbf{Status} \\
83:Heisenberg $\mathcal{H}_\kappa$
85: & $1$ & ---\textsuperscript{$\dagger$} & $\kappa$ & PH \\
201:This is independent of shadow depth~$\kappa_d$
210:(Theorem~\ref{thm:mc2-bar-intrinsic}). The scalar $\kappa(\cA)$ is
220: &= \bigl(\cH_\kappa,\;
222: \kappa/z\bigr), &
274:Heisenberg $\mathcal{H}_\kappa$ & G & 2 & --- & \S\ref{ch:heisenberg-frame} \\
278:Niemeier $V_\Lambda$ (all 24; $\kappa = 24$) & G & 2 & ---; blind to root system & Thm~\ref{thm:lattice:niemeier-shadow-universality} \\
316:Monster $V^\natural$ ($c = 24$, $\kappa = 12$) & M & $\infty$ & Griess algebra at weight~$2$; $\Delta \neq 0$ & Rem~\ref{rem:lattice:monster-shadow} \\
586:\caption{Free energies $F_1 = \kappa/24$ and $F_2 = 7\kappa/5760$ for $21$ standard families}
594: & $\boldsymbol{\kappa}$
595: & $\boldsymbol{F_1 = \kappa/24}$
 succeeded in 52ms:
  1180	 conformal weight $h = 2$, which is in the bar-relevant range
  1181	 $h \geq 2$. PBW fails; status is open. More generally, for
  1182	 admissible levels $k = p/q - 2$, the first null vector appears at
  1183	 $h = (p{-}1)q$, which is in the bar-relevant range whenever
  1184	 $(p{-}1)q \geq 2$.
  1185	\item \emph{Critical level does not break Koszulness.}
  1186	 The universal algebra $V_{-h^\vee}(\fg)$ at the critical level
  1187	 is uncurved ($\kappa = 0$) but remains Koszul by PBW universality.
  1188	 Critical level breaks the Sugawara construction, not free strong
  1189	 generation.
  1190	\end{enumerate}
  1191	\end{remark}
  1192	
  1193	\begin{remark}[Genus-\texorpdfstring{$1$}{1} free energy and the conformal anomaly]\label{rem:genus-1-verification}
  1194	\index{free energy!genus one}
  1195	The Faber--Pandharipande $\lambda_g$ formula (Theorem~\ref{thm:genus-universality}(iii))
  1196	gives the genus-$g$ free energy
  1197	$F_g(\cA) = \kappa(\cA) \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$ .
  1198	At $g = 1$, $|B_2| = 1/6$, yielding
  1199	\[
 succeeded in 51ms:
  2120	Then $P_{\widehat{\mathfrak{g}}}$ and $P_{\mathcal{W}}$ are algebraic
  2121	functions sharing the same discriminant.
  2122	
  2123	Explicitly, for $\mathfrak{g} = \mathfrak{sl}_2$,
  2124	the Virasoro and $\beta\gamma$ generating functions are:
  2125	\begin{align}
  2126	P_{\mathrm{Vir}}(x)
  2127	 &= \frac{4x}{(1 - x + \sqrt{1 - 2x - 3x^2})^2},
  2128	 \label{eq:gf-vir-motzkin} \\
  2129	P_{\beta\gamma}(x)
  2130	 &= \sqrt{\frac{1+x}{1-3x}}
  2131	 = \frac{1+x}{\sqrt{1-2x-3x^2}}.
  2132	 \label{eq:gf-betagamma}
  2133	\end{align}
  2134	
  2135	Both are algebraic functions of the discriminant
  2136	$\Delta(x) = 1 - 2x - 3x^2 = (1-3x)(1+x)$.
  2137	The $\widehat{\mathfrak{sl}}_2$ generating function is
  2138	\emph{rational} (Remark~\ref{rem:garland-lepowsky-sl2}):
  2139	\begin{equation}\label{eq:gf-sl2-rational}

thinking
**Defining the auditing scope**

I'm thinking I need to gather all occurrences of instances in the theory and examples sections across multiple volumes and list them with counts. It makes sense to focus on any ambiguous or problematic examples for the report. I want to clarify the exact scope, so maybe we can limit our search to only the theory and examples subdirectories. Since the user specifically asked for these areas, we can exclude other connections, simplifying our task. I'll proceed to count occurrences by file.
exec
/bin/zsh -lc "rg -l '\\\\kappa' chapters/theory chapters/examples | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -l '\\\\kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples 2>/dev/null | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -l '\\\\kappa' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples 2>/dev/null | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples 2>/dev/null | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/bar_complex_tables.tex
chapters/examples/bershadsky_polyakov.tex
chapters/examples/beta_gamma.tex
chapters/examples/deformation_quantization.tex
chapters/examples/deformation_quantization_examples.tex
chapters/examples/free_fields.tex
chapters/examples/genus_expansions.tex
chapters/examples/heisenberg_eisenstein.tex
chapters/examples/kac_moody.tex
chapters/examples/landscape_census.tex
chapters/examples/lattice_foundations.tex
chapters/examples/level1_bridge.tex
chapters/examples/logarithmic_w_algebras.tex
chapters/examples/minimal_model_examples.tex
chapters/examples/moonshine.tex
chapters/examples/n2_superconformal.tex
chapters/examples/symmetric_orbifolds.tex
chapters/examples/toroidal_elliptic.tex
chapters/examples/w3_composite_fields.tex
chapters/examples/w3_holographic_datum.tex
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex
 succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex
 succeeded in 52ms:
    5973


thinking
**Considering audit file usage**

I’m thinking about potentially using existing audit files, but the user wants us to stay grounded in the actual file contents we read. It’s important to verify what those contents are. Given the scale of the task, I’ll need a systematic scan using heuristics alongside manual verification of the candidate files. Balancing between existing materials and actual content is key here!
thinking
**Considering agent usage**

I’m thinking that since it's already manual, it might be okay. But, should I create explorer agents for reviewing candidates for Vol II and Vol III? The user didn't explicitly ask for parallel or delegated work, and the deep-beilinson-audit skill suggests using subagents only if requested. So, it sounds like I shouldn’t use subagents after all. I'll need to update the plan tool for substantial work, so I should create a concise plan.
Plan update
Audit is large, so I’m reducing the 5,973 `\kappa` hits to verified issue classes and then re-reading each candidate in context before reporting.
  ✓ Build canonical comparison surface from `chapters/examples/landscape_census.tex` and the repo constitution
  → Enumerate `\kappa` occurrences in Vol I/II/III theory+examples and bucket them by formula, bare scalar use, and Vol III subscript discipline
  • Re-read each candidate in file context, eliminate false positives, and prepare exact line-specific fixes

thinking
**Inspecting candidate distribution**

I need to check the candidate distribution, possibly by looking at the file counts. It seems like using a tool like “rg count” could be helpful for this. I want to ensure that I'm accurately assessing the distribution, as that might provide insights into what's happening with the candidates. This method should make it simpler to gather and analyze the necessary data. I'll get started on that check now!
exec
/bin/zsh -lc "rg -c '\\\\kappa' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples 2>/dev/null | sort -t: -k2,2nr | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -c '\\\\kappa' chapters/theory chapters/examples | sort -t: -k2,2nr | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -c '\\\\kappa' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples 2>/dev/null | sort -t: -k2,2nr | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:127
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:123
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:95
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:87
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:71
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:30
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:15
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:13
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:12
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:9
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:7
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:6
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex:5
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:2
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:2
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex:1
 succeeded in 53ms:
chapters/theory/higher_genus_modular_koszul.tex:1117
chapters/theory/higher_genus_foundations.tex:326
chapters/examples/genus_expansions.tex:311
chapters/examples/kac_moody.tex:267
chapters/examples/toroidal_elliptic.tex:232
chapters/theory/higher_genus_complementarity.tex:216
chapters/examples/heisenberg_eisenstein.tex:214
chapters/examples/free_fields.tex:159
chapters/examples/w_algebras_deep.tex:141
chapters/examples/w_algebras.tex:124
chapters/theory/chiral_hochschild_koszul.tex:122
chapters/theory/bar_cobar_adjunction_inversion.tex:118
chapters/examples/landscape_census.tex:108
chapters/theory/introduction.tex:87
chapters/examples/lattice_foundations.tex:66
chapters/theory/computational_methods.tex:65
chapters/theory/ordered_associative_chiral_kd.tex:64
chapters/examples/y_algebras.tex:63
chapters/examples/bar_complex_tables.tex:62
chapters/theory/introduction.tex.bak:62
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:255
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:107
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:75
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:41
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:29
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:29
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:27
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:26
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:21
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:17
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:11
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex:10
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:10
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:9
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:8
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:8
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex:6
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:5
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:4
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex:1

thinking
**Exploring unique candidate lines**

I'm considering using a script to generate unique candidate lines for all volumes. I might categorize them into a few groups, like: lines with `\kappa =`, bare `\kappa` without subscripts in Vol III, and generic statements using `\kappa`. 

I should also check for missing definitions in W_N formulas and generic equations like `F_g = \kappa \cdot \lambda_g`. It’s essential to verify any findings manually and examine Vol III guidelines, especially in relation to `\kappa`. I'll search for bare uses in examples or theory.
codex
I’ve narrowed the main risk classes: bare scalar `\kappa`, family-specific formulas written without family tags, and Vol III notation that may violate the subscript discipline. I’m now reading those files in context, because the false-positive rate is high unless I can see the local definition paragraph.
exec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z])'"\\\\kappa(?"'![_''^(A-Za-z])'"' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'In this section.*\\\\kappa|we write .*\\\\kappa|denote .*\\\\kappa|let .*\\\\kappa|\\\\kappa_\\{ch\\}|\\\\kappa_\\{cat\\}|\\\\kappa_\\{BKM\\}|\\\\kappa_\\{fiber\\}' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nP '\\\\kappa\\s*=|=\\s*\\\\kappa|\\\\kappa\\s*\\+' /Users/raeez/chiral-bar-cobar/chapters/theory /Users/raeez/chiral-bar-cobar/chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:202:Let $\frakg$ be a finite-dimensional Lie algebra equipped with an invariant pairing $\kappa \colon \frakg \otimes \frakg \to \C$. Holomorphic Chern--Simons theory with gauge algebra $\frakg$ on a complex manifold $M$ has action
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:204: S_{\mathrm{hCS}}(A) \;=\; \frac{1}{2} \int_M \Omega \wedge \kappa\!\left(A \wedge \dbar A + \tfrac{2}{3} A \wedge A \wedge A\right),
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:209: the boundary on $\Sigma$ produces the affine Kac--Moody vertex algebra $V_k(\frakg)$ at level $k$ determined by $\kappa$. This is an $E_\infty$-chiral algebra on $\Sigma$ (in the Beilinson--Drinfeld sense) with $\Eone$-ordered refinement via the Vol~II Swiss-cheese structure.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:460:This is the most speculative conjecture in the chapter: it requires (a) the 6d algebraic framework for $K3 \times E$, (b) CY-A$_3$, (c) the identification of the BKM root datum with the K3 Mukai lattice. The $\kappa$-spectrum check is $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$.
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5016:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{ch}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:366:Let $A_0 = \cH_{24}$ be the rank-$0$ Heisenberg chiral algebra with $\kappa_{\mathrm{fiber}}(A_0) = 24$, and let $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$. Then:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:234:Let $\cC$ be a smooth proper CY-$d$ category ($d = 2$ or $d = 3$) satisfying the hypotheses of Theorem~CY-A$_d$ (Chapter~\ref{ch:cy-to-chiral}), and let $A_\cC = \Phi(\cC)$ be its image under the CY-to-chiral functor. There exists a parameter $q \in \C^*$ (determined by $\kappa_{\mathrm{ch}}(A_\cC)$) and a Hopf algebra in a braided category, $C(\cC, q)$, such that there is an equivalence of modular tensor categories
 succeeded in 51ms:
Total output lines: 1774

/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:239: \kappa_{\mathrm{ch}}(A_{K3 \times K3}) = \kappa_{\mathrm{ch}}(V_{\Lambda_{K3}}) + \kappa_{\mathrm{ch}}(V_{\Lambda_{K3}}) = 24 + 24 = 48,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:240: $\Delta_{\mathrm{ns}}(\Tr_A) = \kappa_{\mathrm{cat}} \cdot \lambda_1$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:562:$\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ extracts the scalar
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:575:trace $\mathrm{tr}_{\cZ}(\sigma) = \kappa_{\mathrm{cat}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:8:This chapter replaces the wrong identification by the right one. The CY trace, properly refined to negative cyclic homology $\HC^-_d(\cC)$, determines $\kappa_{\mathrm{ch}}(A_\cC)$ through the CY-to-chiral functor $\Phi$. The resulting equality $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is a statement about the CY Euler characteristic of the category, which in general differs from the topological Euler characteristic of the underlying manifold. The genus-$g$ obstruction tower $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ then encodes the higher-genus CY invariants on the uniform-weight lane, with the multi-weight cross-channel correction $\delta F_g^{\mathrm{cross}}$ from Vol~I appearing at $g \geq 2$ for families with fields of distinct conformal weights.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:28: \item The genus-$g$ obstruction satisfies $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ on the uniform-weight lane; unconditionally at genus~$1$ for all families (Vol~I, Theorem~D); at genus $g \geq 2$ for multi-weight algebras, the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (Vol~I, op:multi-generator-universality, resolved negatively; $\delta F_2(\mathcal{W}_3) = (c{+}204)/(16c) > 0$);
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:66:Each entry is computed independently. For $E$: the quantum chiral algebra is the Heisenberg $H_1$ with $\kappa_{\mathrm{ch}} = 1$ (the level), while $\chi_{\mathrm{top}}(E) = 0$. For $K3$: the quantum chiral algebra is the $\cN = 4$ SCA with $\kappa_{\mathrm{ch}} = 2 = \dim_\C(K3)$, while $\chi_{\mathrm{top}}/24 = 1$. For $K3 \times E$: $\chi_{\mathrm{top}}(K3 \times E) = \chi(K3) \cdot \chi(E) = 24 \cdot 0 = 0$; the chiral de Rham complex has $\kappa_{\mathrm{ch}} = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$ (proved by additivity); the BKM automorphic weight is the distinct quantity $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$ (see the $\kappa_{\mathrm{ch}}$-spectrum, Example~\ref{ex:kappa-spectrum-k3xe}). For the conifold: the resolved conifold has $\chi_{\mathrm{top}} = 2$ (the total space of $\cO(-1) \oplus \cO(-1) \to \bP^1$ deformation retracts onto the zero section $\bP^1$, so $\chi_{\mathrm{top}} = \chi(\bP^1) = 2$), giving $\chi_{\mathrm{top}}/24 = 1/12$, while $\kappa_{\mathrm{ch}} = 1$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:88:The discrepancy $5 \neq 2$ reflects the fact that the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ for $K3 \times E$ is \emph{not} the tensor product of the $K3$ and $E$ chiral algebras. The weight $5 = \dim(\Sp_4)/2$ is determined by the Borcherds product structure, not by a product decomposition. By contrast, the chiral de Rham modular characteristic $\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$ \emph{is} additive (Proposition~\ref{prop:kappa-k3}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:255:differential satisfies $d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:326: $d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:360:$d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$ is the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:476:$F_g = \kappa_{\mathrm{cat}} \cdot \lambda_g^{FP}$ (UNIFORM-WEIGHT);
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:492:At degree $2$: $\mathrm{av}(\cR(z)) = \kappa_{\mathrm{cat}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:571:$\mathrm{av}(\cR^{-1}) = \kappa_{\mathrm{cat}}(\cA^!_{E_2})$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:23:This averaging is \emph{lossy}: $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ forgets the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:122:is a morphism of cochain complexes and sends the $E_1$ structure to the $E_\infty$ structure. It is lossy: the kernel contains the $R$-matrix data of the holomorphic factor, and on degree two $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:198: ($\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$) \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:257: $\mathrm{av}(R(z))|_{z=0} = \kappa_{\mathrm{ch}} \cdot \mathrm{id}$.

thinking
**Verifying candidate lines**

I'm looking at some candidate lines that include formulas, and I need to verify certain suspicious ones manually. My focus will be on the kappa lines from theory or examples. I think using heuristics might help detect actual problems.

I noticed that deformation_quantization.tex introduces `\kappa` as the integral of a propagator, which raises some questions. Is it consistent with the census? The ambiguity around "level \kappa" could be a concern, so I’ll inspect the context. I’ll also flag it as MEDIUM/HIGH depending on any confusion found in lines 451-461 and 554.
exec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '430,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '540,562p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '1048,1160p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   430	\subsection{Configuration spaces as deformation parameters}
   431	
   432	The space of quantizations is:
   433	\[\mathcal{Q}(\mathcal{A}_{\text{cl}}) = \text{MC}(\bar{B}^1(\mathcal{A}_{\text{cl}}))/\text{gauge}\]
   434	
   435	Geometrically:
   436	\[\mathcal{Q}(\mathcal{A}_{\text{cl}}) \cong \prod_{n=2}^\infty H^0(\overline{C}_n^{\text{ch}}(X), \Omega^{\dim C_n}_{\text{closed}})/\text{exact}\]
   437	
   438	Each configuration space $\overline{C}_n^{\text{ch}}(X)$ contributes deformation parameters at order $\hbar^n$.
   439	
   440	\section{Examples: quantizing concrete chiral algebras}
   441	
   442	\subsection{Example 1: Heisenberg algebra}
   443	
   444	\subsubsection{Classical structure}
   445	
   446	\[\{a(z), a^*(w)\} = \frac{1}{z-w} \quad \text{(coisson/PVA $\lambda$-bracket)}\]
   447	
   448	\subsubsection{Quantization}
   449	
 succeeded in 52ms:
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
   559	At genus $g$, quantization involves integration over the Siegel upper half-space $\mathbb{H}_g$ parametrizing period matrices:
 succeeded in 51ms:
  1048	\begin{computation}[Heisenberg chiral star product through \texorpdfstring{$\hbar^3$}{3}]
  1049	\label{comp:heisenberg-star-product}
  1050	\index{Heisenberg algebra!star product}
  1051	\index{deformation quantization!Heisenberg}
  1052	
  1053	For the Heisenberg algebra $\mathcal{H}_\kappa$ with Coisson
  1054	(classical) structure given by the $\lambda$-bracket
  1055	$\{a_\lambda b\}_{\mathrm{cl}} = \kappa$ (a constant Poisson
  1056	structure on the jet space), the chiral star product is the
  1057	\emph{Moyal product}:
  1058	\begin{equation}\label{eq:heisenberg-moyal}
  1059	a \star_\hbar b = \mu \circ \exp\left(
  1060	\frac{\hbar \kappa}{2}
  1061	\sum_{n \geq 0} (-\partial_w)^n \otimes \partial_z^{(n)}
  1062	\right)(a \otimes b)
  1063	\end{equation}
  1064	where $\mu$ is the normally-ordered product.
  1065	
  1066	\emph{Order $\hbar^0$:} $a \star_0 b = \normord{ab}$
  1067	(normal ordering).


thinking
**Evaluating file issues**

This file seems to have several meanings for "kappa," like Heisenberg level and modular form, making it ambiguous. I should suggest renaming the local deformation parameter to `\hbar_{\mathrm{eff}}` or `k_{\mathrm{Heis}}`, and replacing the genus-one modular formula. But I want to be careful not to over-claim. The line with `\kappa(\tau)` likely has inaccuracies, as the modular characteristic should be constant. I need to check other files too, especially `higher_genus_foundations.tex`, for more uses of "kappa."
thinking
**Investigating kappa issues**

I might be facing issues with the theorem stating a single-generator family where `\kappa` serves as the scalar obstruction coefficient. To clarify, I'll need to examine the context around specific lines that raise suspicion. There might be about 10-20 significant findings regarding `\kappa`, especially in multi-family contexts or missing definitions in W_N formulas. Checking the `wave2_audit` for `kappa` mentions could help too. I should search for occurrences like "where \kappa =" to see if any definitions are missing.
exec
/bin/zsh -lc "rg -n 'where .*\\\\kappa|write .*\\\\kappa|let .*\\\\kappa|denote .*\\\\kappa|set .*\\\\kappa|with .*\\\\kappa' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5326,5366p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4788,4814p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5848,5865p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
317:When we write ``$\dfib^{\,2} = \kappa\cdot\omega_g$'' in this chapter, the
782:where $D^{(g)}_\cA := d_0 + \kappa(\cA)\,\omega_g$ is the corrected
796:with the curvature $\kappa(\cA)\cdot\omega_g$ entering
1861:For a chiral algebra $\cA$ with scalar curvature $\kappa(\cA)$, the
2146:We write $\mathcal{H}_\kappa$ for the Heisenberg vertex algebra at
3816:where $\kappa$ is the central charge and $[1]^{(1)}$ is the genus-1 identity element.
4137:Let $\cA$ be a Koszul chiral algebra with modular characteristic $\kappa(\cA)$
4482:The $d_2$ differential maps $E_2^{p,q} \to E_2^{p+2,q-1}$ and is identified with the Kodaira--Spencer map $\kappa: T_{\mathcal{M}_g} \to R^1\pi_* T_{\Sigma_g/\mathcal{M}_g}$, which measures how the complex structure of~$\Sigma_g$ deforms as we move in moduli space. At genus~1, this is the classical identification of the Kodaira--Spencer class with $\partial/\partial\tau$, and $d_2$ acts by differentiating with respect to $\tau$ (modulo the quasi-modular correction from~$E_2$).
4901:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element. This curvature arises
4999:where $\kappa(\mathcal{W}_3^k) = c/2 + c/3 = 5c/6$.
5253:(where $\kappa_k$ are the Miller--Morita--Mumford classes),
5739:with $\kappa = \sum_i \kappa_{h_i}$.
5818:with per-channel propagator $P_s = 1/\kappa_s$.
5858:For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
5921:By Theorem~\ref{thm:genus-universality}(ii), $\kappa(\mathcal{W}_N^k) = c \cdot \varrho(\mathfrak{sl}_N)$ where $\varrho(\mathfrak{sl}_N) = \sum_{s=2}^N 1/s = H_N - 1$. Under the Feigin--Frenkel involution $k \mapsto k' = -k - 2N$, $c \mapsto c' = K_N - c$, so $\kappa' = (K_N - c)(H_N - 1)$ and $\kappa + \kappa' = K_N(H_N - 1)$.
6142:where $\mathrm{obs}_{g,n}=\kappa\cdot\lambda_g\cdot
6159:\item \emph{Compatible with Koszul duality}: for Kac--Moody algebras, $\kappa(\cA^!) = -\kappa(\cA)$, so the Koszul involution acts as negation on the image.
6164:Additivity is Corollary~\ref{cor:kappa-additivity}. The unit $\mathbf{1}$ (trivial algebra) has $\kappa(\mathbf{1}) = 0$. Surjectivity follows from $\kappa(\mathcal{H}_q) = q$ for $q \in \mathbb{Q}$. Non-injectivity: the Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{g}}_{-h^\vee})$ is a non-trivial Koszul algebra with $\kappa = 0$. Part (iii) is Theorem~\ref{thm:genus-universality}(ii).
6173:at the full subcategory of algebras with $\kappa = 0$. Objects of $\mathrm{KCA}^{\mathrm{unc}}$ are equivalence classes of Koszul chiral algebras modulo critical-level algebras: $\cA \sim \mathcal{B}$ if $\cA \otimes \mathcal{C} \simeq \mathcal{B} \otimes \mathcal{C}'$ for some $\mathcal{C}, \mathcal{C}'$ with $\kappa = 0$. By Theorem~\ref{thm:koszul-k0}, the obstruction coefficient $\kappa$ is a complete invariant on $K_0(\mathrm{KCA}^{\mathrm{unc}})$.
6858:These coincide with the values $\kappa(\cA)$ computed by direct
 succeeded in 53ms:
  4788	\subsection{Example 1: Heisenberg algebra, level shift obstruction}
  4789	\label{subsec:heisenberg-obstruction}
  4790	
  4791	\begin{theorem}[Heisenberg obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:heisenberg-obs}
  4792	For the Heisenberg vertex algebra $\mathcal{H}_\kappa$ at level $\kappa$, the 
  4793	genus-$g$ obstruction is :
  4794	\begin{equation}
  4795	\text{obs}_g^{\mathcal{H}} = \kappa \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g, \mathbb{C})
  4796	\qquad \end{equation}
  4797	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle \textup{(LOCAL)}.
  4798	
  4799	Explicitly:
  4800	\begin{itemize}
  4801	\item $g=1$: $\text{obs}_1 = \kappa \cdot \lambda_1$ \textup{(g=1 only; all-weight at g=1 is unconditional)} where $\lambda_1 = c_1(\mathbb{E}) \in H^2(\overline{\mathcal{M}}_{1,1})$
  4802	\item $g=2$: $\text{obs}_2 = \kappa \cdot \lambda_2 = \kappa \cdot c_2(\mathbb{E})$ \item $g \geq 3$: $\text{obs}_g = \kappa \cdot \lambda_g$ \end{itemize}
  4803	\end{theorem}
  4804	
  4805	\begin{proof}
  4806	
  4807	\emph{Step 1: Heisenberg structure.}
 succeeded in 53ms:
  5326	$\widehat{\mathfrak{g}}_{-k-2h^\vee}$: $\kappa(\mathcal{A}^!) = -\kappa(\mathcal{A})$.
  5327	For $\mathcal{W}$-algebras $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ obtained by Drinfeld--Sokolov
  5328	reduction: $\kappa(\mathcal{A}^!) = \varrho(\mathfrak{g})\, K - \kappa(\mathcal{A})$, where
  5329	$K = c(\mathcal{A}) + c(\mathcal{A}^!)$ is the complementarity constant
  5330	(Remark~\ref{rem:vir-vs-km-complementarity}) and
  5331	$\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i + 1}$ is the exponent sum
  5332	($m_1, \ldots, m_r$ the exponents of~$\mathfrak{g}$; for $\mathcal{W}_N = \mathcal{W}(\mathfrak{sl}_N)$,
  5333	$\varrho = H_N - 1 = \sum_{s=2}^{N} 1/s$).
  5334	In particular, $\kappa + \kappa' = 0$ for affine Kac--Moody algebras
  5335	(by the Feigin--Frenkel involution
  5336	$k \mapsto -k - 2h^\vee$, which gives
  5337	$\kappa' = -\kappa$; note that the $\varrho$-formula
  5338	applies to $\mathcal{W}$-algebras, not to affine Kac--Moody
  5339	algebras directly),
  5340	$\kappa + \kappa' = 13$ for the Virasoro algebra
  5341	($\varrho = 1/2$, $K = 26$),
  5342	and $\kappa + \kappa' = 250/3$ for $\mathcal{W}_3$
  5343	($\varrho = 5/6$, $K = 100$).
  5344	The obstruction coefficient $\kappa = 0$ if and only if $\mathcal{A}$ is at critical level;
  5345	for Kac--Moody the dual is then also critical, but for $\mathcal{W}$-algebras
 succeeded in 53ms:
  5848	For Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ (before DS reduction), $\kappa/c = (k+h^\vee)^2/(2h^\vee k)$, which depends on the level. The level-independence of $\kappa/c$ is specific to $\mathcal{W}$-algebras and reflects the DS reduction.
  5849	\end{corollary}
  5850	
  5851	\begin{proof}
  5852	From Theorem~\ref{thm:genus-universality}(ii): $\kappa = c \cdot \varrho(\mathfrak{g})$. Since $\varrho$ depends only on the exponents of $\mathfrak{g}$, it is independent of $k$.
  5853	\end{proof}
  5854	
  5855	\begin{corollary}[\texorpdfstring{$\kappa$}{kappa}-periodicity under level shift; \ClaimStatusProvedHere]
  5856	\label{cor:kappa-periodicity}
  5857	\index{obstruction coefficient!periodicity}
  5858	For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
  5859	\end{corollary}
  5860	
  5861	\begin{proof}
  5862	For KM: $\kappa = (k+h^\vee)d/(2h^\vee)$, which is linear in $k$ with slope $d/(2h^\vee)$. Level shift $k \to k+n$ adds $nd/(2h^\vee)$.
  5863	\end{proof}
  5864	
  5865	\begin{remark}[Universality principle]\label{rem:lambda-universality}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '308,326p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3808,3822p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   308	\[
   309	 \Dtot = \sum_{g\ge 0} \hbar^{2g-2}\,\Dg{g}, \qquad
   310	 \Dtot^{\,2} = 0.
   311	\]
   312	
   313	\noindent
   314	\textbf{Warning.}
   315	The obstruction class $\mathrm{obs}_g$ (Definition~\ref{def:genus-g-obstruction})
   316	measures the failure of $\dfib^{\,2} = 0$, \emph{not} of $\Dg{g}^{\,2} = 0$.
   317	When we write ``$\dfib^{\,2} = \kappa\cdot\omega_g$'' in this chapter, the
   318	differential is always $\dfib$; when we write ``$\Dg{g}^{\,2} = 0$,'' the
   319	differential is always $\Dg{g}$. Earlier chapters that use unadorned
   320	$d$ for the genus-$0$ bar differential are using $\dzero$.
   321	\end{convention}
   322	
   323	\begin{remark}[Curvature as infinitesimal monodromy: the chiral Riemann--Hilbert correspondence]
   324	\label{rem:curvature-riemann-hilbert}
   325	\index{Riemann--Hilbert correspondence!chiral|textbf}
   326	\index{curvature!as infinitesimal monodromy}
 succeeded in 52ms:
  3808	&\quad + \int_{E_\tau} J(z_1) \otimes J(z_2) \cdot d_{\mathrm{dR}}\eta_{12}^{(1)}
  3809	\end{align}
  3810	
  3811	Using the quantum-corrected Arnold relation
  3812	$d_{\mathrm{dR}}\eta_{12}^{(1)} = 2\pi i \omega_\tau$:
  3813	\begin{equation}
  3814	d^{(1)}[\text{Tr}^{(1)}(J \otimes J)] = \kappa \cdot [1]^{(1)}
  3815	\end{equation}
  3816	where $\kappa$ is the central charge and $[1]^{(1)}$ is the genus-1 identity element.
  3817	
  3818	This is the \emph{central extension} $[J, J] = \kappa \cdot c$ emerging from genus-1 quantum geometry.
  3819	\end{example}
  3820	
  3821	% ================================================================
  3822	% NEW COMPREHENSIVE SECTION: GENUS 1-3 COMPLETE TREATMENT

thinking
**Inspecting context for central charge**

I see that line 3816 refers to kappa as the central charge, but I'm wondering if it's more related to Heisenberg levels instead. I need to look closer at the context around that line. If J is the Heisenberg current, it might suggest a definite error, so it’s worth checking surrounding lines, particularly around line 3788, to get clarity. Let's dive deeper into that section to figure this out!
codex
I’ve found one real overloading bug already: `higher_genus_foundations.tex` uses bare `\kappa` chapter-wide for obstruction/curvature, then later reuses the same symbol to mean a central charge. I’m checking whether that is isolated or part of a wider local notation collapse before I write the findings.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3778,3819p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'central charge and .*\\\\kappa|\\\\kappa is the central charge|central extension .*\\\\kappa' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3778	\emph{Exhaustiveness.} The components $d^{(0)}, d^{(1)}, \ldots$ exhaust the full differential because the boundary of $\overline{C}_n(\Sigma_g) \subset \overline{\mathcal{M}}_{g,n}$ is the union of collision divisors (giving $d^{(0)}$) and moduli boundary strata (contributing to $d^{(k)}$ for $k \ge 1$). The identity $\Dg{g}^{\,2} = 0$ decomposes into relations
  3779	\[
  3780	\sum_{a+b=r} d^{(a)} \circ d^{(b)} = 0
  3781	\]
  3782	for each Leray degree $r$, encoding consistency across the correction tower.
  3783	\end{proof}
  3784	
  3785	\subsection{Explicit genus 1 example: central extensions}
  3786	
  3787	\begin{example}[Heisenberg central extension from genus 1]
  3788	\label{ex:heisenberg-genus-1}
  3789	\index{central extension!higher genus}
  3790	For the Heisenberg vertex algebra $\mathcal{H}$ with current $J(z) = \sum_{n \in \mathbb{Z}} a_n z^{-n-1}$:
  3791	
  3792	\emph{Genus 0.} At genus $0$, the bar differential gives:
  3793	\begin{equation}
  3794	d^{(0)}[J \otimes J] = [J, J]_{g=0} = 0
  3795	\end{equation}
  3796	There is no central extension at genus zero.
  3797	
 succeeded in 52ms:
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/theory/higher_genus_foundations.tex:4034:\emph{Geometric interpretation.} The quasi-periodic shift $-2\pi i\,(dz_i - dz_j)$ under $z_i \to z_i + \tau$ is the obstruction to $\eta_{ij}^{(1)}$ descending to a well-defined form on $C_n(E_\tau)$. This shift defines the central extension at genus~1 and is the source of the curvature element $\kappa$ in the bar complex.
chapters/theory/cobar_construction.tex:2522:The resulting central extension is universal because any 2-cocycle $\omega: \mathcal{A} \otimes \mathcal{A} \to \mathbb{C}$ that defines a central extension of~$\mathcal{A}$ factors through the genus-1 trace pairing. Indeed, the Hochschild 2-cocycle condition requires $\omega$ to be $\mathcal{A}$-bilinear and invariant, which forces $\omega = c \cdot \mathrm{Tr}$ for some constant~$c$. The genus-1 construction produces exactly this with $c = \kappa$.
chapters/theory/cobar_construction.tex:2527:The central extension cocycle $\omega_\kappa = \kappa \cdot
chapters/theory/higher_genus_complementarity.tex:2544:\emph{Interpretation}: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (the central extension appears as an obstruction) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$ (the first Chern class appears as a deformation).
exec
/bin/zsh -lc "rg -nP '\\\\kappa\\s*=\\s*c/2|\\\\kappa\\s*=\\s*\\\\frac\\{c\\}\\{2\\}|\\\\kappa\\s*=\\s*c \\* \\(H_N - 1\\)|\\\\kappa\\s*=\\s*\\\\varrho|\\\\kappa\\s*=\\s*\\(k\\s*\\+\\s*h\\"'^'"\\\\vee\\)' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'H_\\{N-1\\}|H_N - 1|H_N\\)|H_N =' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1669: so $\kappa = c/2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1711:For $N = 2$: $\kappa = c/2$; for $N = 3$: $\kappa = 5c/6$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3856: since $\kappa = c/2$ for both algebra and dual\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4161:$\kappa = c/2$ (Proposition~\ref{prop:benchmark-modular-data}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:710:For Virasoro ($\alpha = 2$, $\kappa = c/2$),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2312:involution $c \mapsto 26 - c$, the curvature $\kappa = c/2$, and the
chapters/examples/w_algebras_deep.tex:1568:$\kappa = \varrho(\fg) \cdot c$ inherits this algebraic identity.
chapters/examples/y_algebras.tex:318:channel. The formula $\kappa = c/2$ applies only when the
chapters/examples/y_algebras.tex:370:formula $\kappa = c/2$ requires the Virasoro sector to be the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3559:weight~$2$, with curvature $\kappa = c/2$ and
chapters/examples/logarithmic_w_algebras.tex:205:obstruction, and $\kappa = c/2$. The weight-$(2p{-}1)$ generators
chapters/examples/logarithmic_w_algebras.tex:235:$\kappa = c/2 = -1$ applies.
chapters/examples/beta_gamma.tex:2037:(The global modular characteristic $\kappa = c/2 = 6\lambda^2 - 6\lambda + 1$
chapters/examples/lattice_foundations.tex:5046:$p$ & $c$ & Model & $\kappa = c/2$ & $\rho$ \\
chapters/examples/lattice_foundations.tex:5063:shadow at this value of~$c$: $\kappa = c/2$, $\alpha = 2$,
chapters/examples/free_fields.tex:259:Then $\kappa = c/2 = 1/4$ by the universal formula
chapters/examples/free_fields.tex:669:($\kappa = c/2$ in every case; see landscape census
chapters/examples/free_fields.tex:1137:at central charge $c = c_{\beta\gamma}(\lambda)$: $S_2 = \kappa = c/2$,
chapters/examples/free_fields.tex:1267:(using $\kappa = c/2$). The denominator $5c + 22 = 60\lambda^2 - 60\lambda + 32$
chapters/examples/free_fields.tex:5245:coefficient $\kappa = (k+h^\vee)\dim(\fg)/(2h^\vee)$ for
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2715: $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:3047:\kappa(\cW_N) \;=\; c \cdot (H_N - 1),
chapters/theory/higher_genus_modular_koszul.tex:3051:where $H_N$ is the $N$-th harmonic number (not $H_{N-1}$; see
chapters/theory/higher_genus_modular_koszul.tex:3054:$c \cdot (H_N - 1)$ is its Brown--Henneaux coefficient at
chapters/theory/higher_genus_modular_koszul.tex:3055:spin content $\{2, 3, \ldots, N\}$, and the factor $H_N - 1$
chapters/theory/higher_genus_modular_koszul.tex:3056:is the anomaly ratio $\varrho(\mathfrak{sl}_N) = H_N - 1$ of
chapters/theory/higher_genus_modular_koszul.tex:4522:$c\!\cdot\!(H_N - 1)$ &
chapters/theory/higher_genus_modular_koszul.tex:4535:Here $H_N = \sum_{j=1}^N 1/j$ is the harmonic number,
chapters/theory/higher_genus_modular_koszul.tex:4627:$\cW_N$ in general, $\kappa = c \cdot (H_N - 1)$ where
chapters/theory/higher_genus_modular_koszul.tex:4628:$H_N = \sum_{j=1}^{N} 1/j$ is the harmonic number, and the
chapters/theory/higher_genus_modular_koszul.tex:20859:= c\,(H_N - 1)$.}
chapters/theory/higher_genus_modular_koszul.tex:20862:\sum_{j=2}^{N} c/j = c\,(H_N - 1)$, where
chapters/theory/higher_genus_modular_koszul.tex:20863:$H_N = 1 + \frac{1}{2} + \dotsb + \frac{1}{N}$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:633:$K_N/c^*_N = 2(H_N - 1)$ equals~$1$ only at $N = 2$ (where
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:840:Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:856:\;=\; (H_N - 1)\,\alpha_N,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:858:where $H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:860:$K_N/c_N^* = 2(H_N - 1)$ equals~$1$ if and only if $N = 2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:867:$\kappa(\mathcal{W}_{N,c}) = c\,(H_N - 1)$, where $H_N - 1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:872:$\kappa(\mathcal{W}_{N,\alpha_N - c}) = (\alpha_N - c)(H_N - 1)$.

thinking
**Investigating Kappa Definitions**

I’m thinking about how findings can show ambiguity even if the formula is technically correct. If we find a bare `\kappa`, it could mean different things. I need to fix this by replacing `\kappa` with something more specific. The goal is to sweep through the issues thoroughly. I want to check for lines featuring bare `\kappa` in files without clear definitions nearby. It’s crucial to search for the local definition, especially in `w_algebras.tex`, to clarify earlier uses.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2148,2162p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '120,145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/logarithmic_w_algebras.tex | sed -n '192,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '240,270p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2148	$\mathcal{W}_3^k$ & $100$ & $250/3$ & $c = 50$ \\
  2149	\bottomrule
  2150	\end{tabular}
  2151	\end{center}
  2152	For KM, $\kappa$ is linear in~$k$ (sum vanishes); for $\mathcal{W}$-algebras, $\kappa$ is nonlinear (via DS), producing a nonzero sum.
  2153	\end{remark}
  2154	
  2155	\begin{remark}[Convention: \texorpdfstring{$\kappa$}{kappa} vs.\ \texorpdfstring{$\kappa_g$}{kappa\_g}]\label{rem:kappa-convention-disambiguation}
  2156	Throughout this chapter, $\kappa$ (without subscript) denotes the \emph{obstruction coefficient} of the genus-1 bar complex: the scalar in the formula $\mathrm{obs}_1 = \kappa \cdot \lambda_1$, where $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class. This is a number depending on the chiral algebra (e.g., $\kappa = c/2$ for Virasoro, $\kappa = 5c/6$ for $\mathcal{W}_3$).
  2157	
  2158	This should not be confused with the \emph{Mumford--Miller--Morita kappa class} $\kappa_g = \pi_*(\psi^{g+1}) \in H^{2g}(\overline{\mathcal{M}}_g)$, which is a tautological class on the moduli space of curves (cf.\ Chapter~\ref{chap:higher-genus}). The level of the affine algebra is denoted~$k$, not~$\kappa$.
  2159	\end{remark}
  2160	
  2161	\subsection{\texorpdfstring{General $\mathcal{W}_N$: obstruction coefficient formula}{General WN: obstruction coefficient formula}}
  2162	\label{sec:wn-obstruction}
 succeeded in 51ms:
   192	 \kappa(\cW(p)) \;=\; \frac{c(\cW(p))}{2}
   193	 \;=\; \frac{1}{2} - \frac{3(p-1)^2}{p}.
   194	\end{equation}
   195	\end{proposition}
   196	
   197	\begin{proof}
   198	Three verification paths.
   199	
   200	\emph{Path~1 (generator analysis).}
   201	The algebra $\cW(p)$ has $\dim V_1 = 0$: there are no weight-$1$
   202	currents ($T$ has weight~$2$; the triplet $W^a$ has weight
   203	$2p - 1 \geq 3$). By the criterion , when $\dim V_1 = 0$
   204	the Virasoro subalgebra alone determines the genus-$1$ bar
   205	obstruction, and $\kappa = c/2$. The weight-$(2p{-}1)$ generators
   206	$W^a$ enter the bar differential at degree $\geq 2$ (they source
   207	the shadow coefficients $S_3, S_4, \ldots$) but do not affect the
   208	scalar genus-$1$ curvature, which arises from the degree-$0$
   209	vacuum diagram with no external insertions.
   210	
   211	\emph{Path~2 (lattice parent).}
 succeeded in 51ms:
   120	$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$ families
   121	share $\Delta(x) = (1-3x)(1+x)$ despite entirely
   122	different local operator content. The bar spectral sequence collapses
   123	at $E_2$ for the Virasoro algebra (quartic pole drives $d_1$ but not
   124	$d_2$); for $\mathcal{W}_N$ with $N \geq 3$, higher-order poles from
   125	the $W^{(N)}$ self-OPE (order $2N$) produce additional
   126	non-trivial differentials. The
   127	curvature is non-scalar: $\mathcal{W}_3$ has two curvature channels,
   128	$m_0^{(T)} = c/2$ and $m_0^{(W)} = c/3$, one per generator.
   129	
   130	\begin{remark}[Shadow obstruction tower for
   131	$\mathcal{W}$-algebras]\label{rem:w-master-mc}
   132	For principal $\mathcal{W}_N^k$ at generic level, the shadow
   133	obstruction tower has a distinguished one-dimensional cyclic
   134	level direction, with
   135	$\kappa = \varrho(\mathfrak{g}) \cdot c$ where
   136	$\varrho(\mathfrak{g}) = \sum_i 1/(m_i + 1)$.
   137	The transferred higher operations $\ell_n^{\mathrm{tr}}$ are all
   138	nonzero (unlike Heisenberg) and the complementarity
   139	potential~$S_{\mathcal{W}_N}$ is non-polynomial.
 succeeded in 52ms:
   240	\item\label{item:fermion-discriminant}
   241	 Critical discriminant:
   242	 $\Delta(\mathcal{F}) = 8\kappa S_4 = 0$.
   243	\item\label{item:fermion-class}
   244	 Shadow class: G \textup{(}Gaussian\textup{)}, $r_{\max} = 2$.
   245	\item\label{item:fermion-tower}
   246	 Tower termination:
   247	 $\Theta_{\mathcal{F}}^{\leq r}
   248	 = \Theta_{\mathcal{F}}^{\leq 2}
   249	 = \tfrac{1}{4} \cdot \eta \otimes \Lambda$
   250	 for all $r \geq 2$.
   251	\end{enumerate}
   252	\end{proposition}
   253	
   254	\begin{proof}
   255	\eqref{item:fermion-kappa}:
   256	The free fermion has central charge $c = 1/2$ (a single real
   257	fermion of weight $h = 1/2$; standard from the Virasoro commutation
   258	relations).
   259	Then $\kappa = c/2 = 1/4$ by the universal formula

thinking
**Analyzing notation issues**

It seems like `logarithmic_w_algebras.tex` is fine within the proof while the family is fixed. However, `free_fields.tex` appears to be specific to theorems. I must identify any ambiguous uses in multi-family contexts or where family identification is incorrect. There’s a remark in `w_algebras.tex` at line 135 that comes before the definition at 2155, but the principal family W_N is fixed, which is okay. I should look for occurrences of `\kappa` used ambiguously in the same file, especially regarding "central charge" and the Casimir element. Candidate files like `higher_genus_foundations.tex` at lines 3816 and 4901 are relevant since they use the same symbol, indicating a serious notation issue, especially around line 4901.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4888,4912p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'where \\\\kappa = .*Casimir|\\\\kappa = .*Casimir|invariant pairing \\\\kappa|Killing form \\\\kappa|central charge.*\\\\kappa|\\\\kappa is the central charge' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4888	At the critical level $k = -h^\vee$, the obstruction vanishes for all $g$, consistent with
  4889	$d^2 = 0$ on the bar complex (Proposition~\ref{prop:km-bar-curvature}(i)).
  4890	\end{theorem}
  4891	
  4892	\begin{proof}
  4893	
  4894	\emph{Step 1: Genus-zero curvature.}
  4895	
  4896	By Proposition~\ref{prop:km-bar-curvature}, the bar complex
  4897	of $\widehat{\mathfrak{g}}_k$ has curvature:
  4898	\begin{equation}\label{eq:km-curvature-recall}
  4899	m_0 = \frac{k + h^\vee}{2h^\vee} \cdot \kappa
  4900	\end{equation}
  4901	where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element. This curvature arises
  4902	because squaring the bar differential on degree-2 elements produces:
  4903	\[d^2(J^a \boxtimes J^b \cdot \eta_{12}) = (k + h^\vee) \cdot
  4904	\bigl(\text{adjoint Casimir contribution}\bigr)\]
  4905	The factor $h^\vee$ comes from the contraction
  4906	$\sum_c f^{ac}{}_d f^{bc}{}_e = 2h^\vee \cdot (J^a, J^b)$
  4907	(the Casimir eigenvalue on the adjoint representation in the normalization where
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1856:The modular characteristic $\kappa_{\mathrm{ch}}$ of a CY$_3$ chiral algebra is determined by the CY category, not by the Virasoro central charge alone. This section establishes the key distinction between $\chi_{\mathrm{top}}/24$ and $\kappa_{\mathrm{ch}}$.
chapters/examples/symmetric_orbifolds.tex:466:the Brown--Henneaux central charge $c = 6N$ via $\kappa = c/3$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:173:On the $\cW$-algebra side, the principal $\cW$-algebra of $\mathfrak{sl}_2$ is the Virasoro vertex algebra at central charge $c(k) = 1 - 6(k+1)^2/(k+2)$ via the Drinfeld--Sokolov formula. The level $k_{A_1}$ distinguished by the Vol~III Kazhdan--Lusztig boundary of the semiclassical locus is the unique level for which the Virasoro output matches the modular characteristic $\kappa_{\mathrm{ch}} = \mu = 1$. Substituting $\kappa_{\mathrm{ch}}^{\mathrm{Vir}} = c/2$ (the Virasoro entry of the Vol~I kappa table) and $\kappa_{\mathrm{ch}} = 1$ forces $c = 2$ on the nominal Vir side; the semiclassical limit on the LG side is instead the free-fermion normalization $c = 1/2$, whose Vir-kappa is $1/4$ and whose two Clifford states account for the factor of two in Example~\ref{ex:mf-quadratic}. The two normalizations differ by a factor attributable to the Clifford stabilization, and Conjecture~\ref{conj:ade-w-algebra} for $A_1$ asserts their equality up to this normalization: the Vol~III chiral algebra is the free fermion at $c = 1/2$, i.e.\ the Ising chiral algebra in its free-fermion presentation, with two Clifford states matching the two-dimensional endomorphism algebra of Example~\ref{ex:mf-quadratic}.
chapters/theory/higher_genus_modular_koszul.tex:3137:the total holographic central charge~$\kappa(V_k(\fg))$.
chapters/theory/higher_genus_modular_koszul.tex:11984:central charge $S_2 = \kappa(\cA)$ already captures the entire
chapters/theory/higher_genus_modular_koszul.tex:29022:characteristic, \emph{not} the central charge: $\kappa/(6\pi)
chapters/examples/w_algebras.tex:7039:ratio and central charge via $\kappa = \rho_\lambda \cdot c$.
chapters/examples/free_fields.tex:1137:at central charge $c = c_{\beta\gamma}(\lambda)$: $S_2 = \kappa = c/2$,
chapters/examples/free_fields.tex:2875:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
chapters/examples/genus_expansions.tex:441:The Feigin--Frenkel involution $k \mapsto k' = -k - 2h^\vee = -k-4$ acts on the central charge as $c \mapsto c' = 6 - c$, and on the obstruction coefficient as $\kappa \mapsto -\kappa$.
chapters/examples/genus_expansions.tex:2011:For $\mathcal{W}_3^k(\mathfrak{sl}_3)$ with central charge $c(k) = 2 - 24(k+2)^2/(k+3)$, the obstruction coefficient is $\kappa = 5c/6$ (Table~\ref{tab:master-invariants}). The genus-$g$ free energy:
chapters/examples/genus_expansions.tex:2034:The negative free energies reflect the negative central charge at $k = 1$. At the dual level $k' = -7$: $c' = 152$, $\kappa' = 380/3$, and $F_g' = -F_g + \frac{250}{3} \cdot \lambda_g^{\mathrm{FP}}$.
chapters/examples/kac_moody.tex:523:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
chapters/examples/kac_moody.tex:1182:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element.
chapters/theory/bar_cobar_adjunction_curved.tex:253:\item The critical gravitational coupling is the fixed point of the duality involution on the scalar lane. When the scalar complementarity constant is written as $\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!) = K_\kappa(\mathcal{A})$, the fixed point is $\kappa_{\mathrm{crit}} = K_\kappa(\mathcal{A})/2$. This constant is family-specific. For affine Kac--Moody, Heisenberg, and free-field families one has $K_\kappa = 0$, so $\kappa_{\mathrm{crit}} = 0$. For Virasoro one has $K_\kappa = 13$, so $\kappa_{\mathrm{crit}} = 13/2$, equivalently $c = 13$. For the Bershadsky--Polyakov family the manuscript uses $\kappa(\mathcal{B}^k) = c/6$ together with the central-charge conductor $c(\mathcal{B}^k) + c((\mathcal{B}^k)^!) = 196$; hence the self-dual central charge is $c = 98$, and the induced scalar critical coupling is $\kappa_{\mathrm{crit}} = 49/3$.
chapters/theory/bar_cobar_adjunction_curved.tex:5930:and curvature $\mu_0 \propto \mathbf{1}$ from the central charge (the proportionality constant depends on the $A_\infty$ model; the modular characteristic is $\kappa(\mathrm{Vir}_c) = c/2$). Since $\mathbf{1}$ is central, $\mu_0 \in Z(\mathrm{Vir}_c)$.
chapters/theory/coderived_models.tex:908:central charge, where the curvature~$\kappa(\cA)$ is nonzero
chapters/theory/higher_genus_foundations.tex:2322:The central charge $\kappa$ now appears in:
chapters/theory/higher_genus_foundations.tex:4901:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element. This curvature arises
chapters/theory/higher_genus_foundations.tex:5858:For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.

thinking
**Inspecting notation collisions**

I'm noticing more notation collisions in my search results. The central charge \(\kappa\) seems suspicious as it appears in the file `higher_genus_foundations.tex`. I need to inspect `kac_moody.tex`, which uses \(\kappa\) as both a Casimir element and modular characteristic. I need to figure out if there's a local notation collision here. Additionally, `cobar_construction.tex` has a potentially misleading statement regarding the Sugawara central charge. I'll verify the context and check if \(\kappa\) indeed equals \(c/6\) as stated.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2314,2328p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2314	
  2315	\subsection{The Heisenberg algebra at genus 2}
  2316	
  2317	\subsubsection{\texorpdfstring{Operators on $\Sigma_2$}{Operators on -2}}
  2318	
  2319	The Heisenberg operators $a(z), a^*(z)$ on $\Sigma_2$ satisfy:
  2320	\[\langle a(z_1) a^*(z_2) \rangle_{\Sigma_2} = G_{\Sigma_2}(z_1, z_2) + \kappa \cdot (\text{contact terms})\]
  2321	
  2322	The central charge $\kappa$ now appears in:
  2323	\begin{itemize}
  2324	\item Genus 0 correction: in $(z_1 - z_2)^{-2}$ pole
  2325	\item Genus 1 correction: in trace around $S^1$ cycles
  2326	\item \emph{Genus 2 correction}: in double-trace contributions (NEW!)
  2327	\end{itemize}
  2328	
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '512,530p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1174,1188p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2538,2550p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1428,1440p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1174	m_1^2(J^a \boxtimes J^b \cdot \eta_{12}) = (k + h^\vee) \cdot \bigl(\text{adjoint Casimir contribution}\bigr)
  1175	\end{equation}
  1176	The factor $h^\vee$ arises from the adjoint representation: by Lemma~\ref{lem:killing-structure-constants}, $\sum_{c,d} f^{ac}{}_d f^{bc}{}_d = 2h^\vee \cdot \delta^{ab}$, which gives $\sum_{c,d,e} f^{ac}{}_d f^{bc}{}_e (J^d, J^e) = 2h^\vee \cdot (J^a, J^b)$. (For $\mathfrak{sl}_2$ with $h^\vee = 2$, this was verified explicitly in Theorem~\ref{thm:sl2-koszul-dual}: $m_1^2(e \boxtimes f \cdot \eta_{12}) = (k+2) \cdot \partial h$.)
  1177	
  1178	Therefore $m_1^2 = 0$ if and only if $k = -h^\vee$ (critical level); the bar differential $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$. For $k \neq -h^\vee$, the bar complex is a curved $A_\infty$-coalgebra with curvature:
  1179	\begin{equation}
  1180	m_0 = \frac{k + h^\vee}{2h^\vee} \cdot \kappa \in \bar{B}^0
  1181	\end{equation}
  1182	where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element.
  1183	
  1184	\emph{Step~3: Cobar computation and level shift.}
  1185	Apply the cobar functor $\Omega$ to $\bar{B}(\widehat{\mathfrak{g}}_k)$. The cobar construction dualizes the coalgebra: generators of $\Omega(\bar{B})$ are the linear duals $(J^a)^* = J^{a,*}$ of the bar generators, and the cobar differential $d_\Omega$ is determined by dualizing the bar differential~\eqref{eq:bar-diff-general}.
  1186	
  1187	Dualizing the double-pole contribution: the term $k \cdot (J^a, J^b) \cdot |0\rangle$ in the bar differential dualizes to a double-pole term in the cobar OPE. Concretely, the cobar OPE between dual generators is:
  1188	\begin{equation}\label{eq:cobar-ope}
 succeeded in 53ms:
   512	\end{proof}
   513	
   514	\begin{remark}[Central charge sum]\label{rem:km-central-charge-sum}
   515	The central charges satisfy $c(\widehat{\mathfrak{g}}_k) + c(\widehat{\mathfrak{g}}_{-k-2h^\vee}) = 2\dim\mathfrak{g}$, independent of $k$ (Theorem~\ref{thm:central-charge-complementarity}).
   516	\end{remark}
   517	
   518	\begin{definition}[Curved Koszul complex]\label{def:curved-koszul-km}
   519	For $k \neq -h^\vee$, the $A_\infty$ structure has curvature:
   520	\begin{equation}
   521	m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a] = m_2(m_0, a) - m_2(a, m_0)
   522	\end{equation}
   523	where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
   524	\end{definition}
   525	
   526	\subsection{The Wakimoto perspective}
   527	
   528	\begin{definition}[Wakimoto module]\label{def:wakimoto}
   529	\index{Wakimoto representation|textbf}
   530	The Wakimoto module $\mathcal{M}_{\mathrm{Wak}}$ at critical level is the free field algebra
 succeeded in 50ms:
  2538	\subsection{Comparison with physical literature}
  2539	
  2540	Our construction recovers known results from physics:
  2541	
  2542	\begin{itemize}
  2543	%: from landscape_census.tex; k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical)
  2544	\item \emph{Kac--Moody algebras:} For the affine vertex algebra $V_k(\mathfrak{g})$ at level~$k$, the modular characteristic is $\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k + h^{\vee})/(2h^{\vee})$, recovering the Sugawara central charge. The Heisenberg algebra is a separate family with $\kappa(\mathcal{H}_k) = k$ (Census~C1); it is \emph{not} a specialization of the Kac--Moody formula (the abelian limit $\dim(\mathfrak{g}) = 1$ does not admit a dual Coxeter number).
  2545	
  2546	\item \emph{Virasoro central charge:} For the Virasoro vertex algebra, the central
  2547	charge $c$ appears as $\operatorname{Tr}(L_m \otimes L_n)$ with $m+n = 0$
  2548	
  2549	\item \emph{$W$-algebras:} For $W$-algebras (following Arakawa), higher-weight
  2550	central charges appear at genus 1 in traces of higher-weight operators
 succeeded in 51ms:
  1428	self-dual under the Koszul pairing), so the general argument specialises to the
  1429	scalar commutation $[\mathbb{D}, \rho(\kappa)] = 0$. The action of $\kappa$ on
  1430	$H^*(\overline{\mathcal{M}}_{1,1})$ is:
  1431	\begin{equation}
  1432	\rho(\kappa)(\alpha) = \lambda_1 \cup \alpha
  1433	\end{equation}
  1434	where $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle.
  1435	This is computed via the Gauss--Manin connection: the central charge $\kappa$ pairs with
  1436	the KS class $\partial/\partial\tau$ to give $\lambda_1$ (Mumford isomorphism).
  1437	\end{proof}
  1438	
  1439	\emph{Step 8: Verdier involution and eigenspace decomposition.}
  1440	

thinking
**Investigating notation issues**

I'm noticing notation collisions and potentially misleading claims in some documents. I need to search for more instances, creating a list of lines that mention phrases like "central charge κ" or "Casimir κ." I already have some examples. 

For instance, there’s a problem in "higher_genus_foundations.tex" where κ is misused for Heisenberg when it should be level `k`. Other lines in the same document also overload κ, which needs attention. Plus, I should check context in "higher_genus_complementarity.tex" to clarify how κ is being used.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1418,1438p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'central charge \\\\kappa|\\\\kappa is the central charge|where \\\\kappa = .*Casimir|the central charge \\\\kappa|central extension.*\\\\kappa' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1418	\begin{equation}
  1419	\sigma \circ \nabla_{\kappa(v)}^z = -\nabla_{\kappa(v)}^z \circ \sigma
  1420	\end{equation}
  1421	which is the anti-commutativity~\eqref{eq:verdier-ks-anticommute} with $\mathbb{D}$
  1422	replaced by the full involution $\sigma$. This holds for \emph{all} Koszul chiral
  1423	pairs, not just those with one-dimensional center.
  1424	
  1425	\emph{Verification for Heisenberg.} For $\mathcal{H}_\kappa$ with center
  1426	$Z(\mathcal{H}_\kappa) = \mathbb{C} \cdot \mathbf{1} \oplus \mathbb{C} \cdot \kappa$,
  1427	the transpose $\kappa_Z$ is the identity on $\mathbb{C} \cdot \kappa$ (the level is
  1428	self-dual under the Koszul pairing), so the general argument specialises to the
  1429	scalar commutation $[\mathbb{D}, \rho(\kappa)] = 0$. The action of $\kappa$ on
  1430	$H^*(\overline{\mathcal{M}}_{1,1})$ is:
  1431	\begin{equation}
  1432	\rho(\kappa)(\alpha) = \lambda_1 \cup \alpha
  1433	\end{equation}
  1434	where $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle.
  1435	This is computed via the Gauss--Manin connection: the central charge $\kappa$ pairs with
  1436	the KS class $\partial/\partial\tau$ to give $\lambda_1$ (Mumford isomorphism).
  1437	\end{proof}
 succeeded in 51ms:
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/kac_moody.tex:966:The decomposition~\eqref{eq:bar-level-decomp} reflects the level-independence of bar chain groups (Lemma~\ref{lem:bar-dims-level-independent}): $d_{\mathrm{crit}}$ encodes $\mathfrak{g}$-structure constants, $\delta$ encodes the central extension, and $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is the degree-$0$ component of $(k + h^\vee)\delta$.
chapters/theory/higher_genus_foundations.tex:3818:This is the \emph{central extension} $[J, J] = \kappa \cdot c$ emerging from genus-1 quantum geometry.
chapters/theory/higher_genus_foundations.tex:4034:\emph{Geometric interpretation.} The quasi-periodic shift $-2\pi i\,(dz_i - dz_j)$ under $z_i \to z_i + \tau$ is the obstruction to $\eta_{ij}^{(1)}$ descending to a well-defined form on $C_n(E_\tau)$. This shift defines the central extension at genus~1 and is the source of the curvature element $\kappa$ in the bar complex.
chapters/theory/higher_genus_complementarity.tex:1728:(central extension, eigenvalue $+1$) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C}
chapters/theory/higher_genus_complementarity.tex:2544:\emph{Interpretation}: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (the central extension appears as an obstruction) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$ (the first Chern class appears as a deformation).
chapters/theory/cobar_construction.tex:2522:The resulting central extension is universal because any 2-cocycle $\omega: \mathcal{A} \otimes \mathcal{A} \to \mathbb{C}$ that defines a central extension of~$\mathcal{A}$ factors through the genus-1 trace pairing. Indeed, the Hochschild 2-cocycle condition requires $\omega$ to be $\mathcal{A}$-bilinear and invariant, which forces $\omega = c \cdot \mathrm{Tr}$ for some constant~$c$. The genus-1 construction produces exactly this with $c = \kappa$.
chapters/theory/cobar_construction.tex:2527:The central extension cocycle $\omega_\kappa = \kappa \cdot

thinking
**Inspecting higher-genus complementarity**

I’m noticing that the `higher_genus_complementarity` snippet feels a bit off with `Z(H_kappa) = C·1 ⊕ C·\kappa` — using κ as a central element seems unusual. Maybe it should be `c` or a level class instead. I think I should look deeper into the context to figure out if there are multiple issues at play. It might help to explore around references 1424, 1720, and 2540 for more clarity!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1718,1732p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2538,2548p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1424,1436p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '958,970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2518,2529p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2538	$Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (which pairs with $H^0 = \mathbb{C}$), 
  2539	we have:
  2540	\begin{equation}
  2541	Q_1(\mathcal{H}_\kappa^!) = (\mathbb{C}\lambda)^\vee = \mathbb{C} \cdot \lambda^\vee
  2542	\end{equation}
  2543	
  2544	\emph{Interpretation}: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (the central extension appears as an obstruction) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$ (the first Chern class appears as a deformation).
  2545	
  2546	Together they span:
  2547	\begin{equation}
  2548	Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \oplus \mathbb{C} 
 succeeded in 50ms:
  1718	\emph{Verification at small genera.}
  1719	
  1720	\emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
  1721	$\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
  1722	giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
  1723	$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
  1724	Theorem~\ref{thm:quantum-complementarity-main}.
  1725	
  1726	\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
  1727	For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
  1728	(central extension, eigenvalue $+1$) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C}
  1729	\cdot \lambda$ (curvature, eigenvalue $-1$). Dimension check: $1 + 1 = 2$.
  1730	
  1731	\emph{Genus $2$}: $\dim H^*(\overline{\mathcal{M}}_2) = 8$
  1732	(Poincar\'e polynomial $1 + 3t^2 + 3t^4 + t^6$).
 succeeded in 50ms:
  1424	
  1425	\emph{Verification for Heisenberg.} For $\mathcal{H}_\kappa$ with center
  1426	$Z(\mathcal{H}_\kappa) = \mathbb{C} \cdot \mathbf{1} \oplus \mathbb{C} \cdot \kappa$,
  1427	the transpose $\kappa_Z$ is the identity on $\mathbb{C} \cdot \kappa$ (the level is
  1428	self-dual under the Koszul pairing), so the general argument specialises to the
  1429	scalar commutation $[\mathbb{D}, \rho(\kappa)] = 0$. The action of $\kappa$ on
  1430	$H^*(\overline{\mathcal{M}}_{1,1})$ is:
  1431	\begin{equation}
  1432	\rho(\kappa)(\alpha) = \lambda_1 \cup \alpha
  1433	\end{equation}
  1434	where $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle.
  1435	This is computed via the Gauss--Manin connection: the central charge $\kappa$ pairs with
  1436	the KS class $\partial/\partial\tau$ to give $\lambda_1$ (Mumford isomorphism).
 succeeded in 51ms:
   958	Standard spectral sequence theory for a bicomplex
   959	\cite[Ch.~5]{Weibel94}. The convergence follows from
   960	the finite-dimensionality of $\bar{B}^n$ (Lemma~\ref{lem:bar-dims-level-independent}).
   961	\end{proof}
   962	
   963	\begin{remark}[Interpretation of the bicomplex]
   964	\label{rem:bicomplex-interpretation}
   965	\index{bar complex!bicomplex!interpretation}
   966	The decomposition~\eqref{eq:bar-level-decomp} reflects the level-independence of bar chain groups (Lemma~\ref{lem:bar-dims-level-independent}): $d_{\mathrm{crit}}$ encodes $\mathfrak{g}$-structure constants, $\delta$ encodes the central extension, and $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is the degree-$0$ component of $(k + h^\vee)\delta$.
   967	\begin{enumerate}[label=\textup{(\roman*)}]
   968	\item At $k = -h^\vee$: $\delta$ vanishes and the bar complex is uncurved with differential $d_{\mathrm{crit}}$.
   969	\item For generic $k \neq -h^\vee$: the critical-first spectral sequence relates bar cohomology at generic and critical levels.
   970	\item At admissible $k = -h^\vee + p/q$: rationality of $(k + h^\vee)$ may create resonance phenomena.
 succeeded in 51ms:
  2518	\]
  2519	where $\mathbf{K}$ is the central element and $\kappa$ is the central charge. This is the relation defining the universal central extension $\widehat{\mathcal{A}}$.
  2520	
  2521	\emph{Step 4: Universality.}
  2522	The resulting central extension is universal because any 2-cocycle $\omega: \mathcal{A} \otimes \mathcal{A} \to \mathbb{C}$ that defines a central extension of~$\mathcal{A}$ factors through the genus-1 trace pairing. Indeed, the Hochschild 2-cocycle condition requires $\omega$ to be $\mathcal{A}$-bilinear and invariant, which forces $\omega = c \cdot \mathrm{Tr}$ for some constant~$c$. The genus-1 construction produces exactly this with $c = \kappa$.
  2523	\end{proof}
  2524	
  2525	\begin{remark}[Central extension as genus-\texorpdfstring{$1$}{1} component of \texorpdfstring{$\Theta$}{Theta}]
  2526	\label{rem:central-ext-theta1}
  2527	The central extension cocycle $\omega_\kappa = \kappa \cdot
  2528	\mathrm{Tr}$ is exactly the genus-$1$ component $\theta_1$ of
  2529	the universal MC class (Theorem~\ref{thm:explicit-theta}):
codex
The next pass is checking “same symbol, different object” failures. Those are more dangerous than a stray missing subscript, because they silently turn one proven invariant into a central charge, a Casimir, or an arbitrary deformation parameter in the middle of a proof.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2508,2524p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2508	\int_{E_\tau} a \otimes b \cdot 2\pi i\, \omega_\tau = 2\pi i \cdot \mathrm{Tr}(a \otimes b)
  2509	\]
  2510	where $\mathrm{Tr}(a \otimes b) = \oint a(z)b(z)\, dz$ is the trace pairing on $\mathcal{A}$.
  2511	
  2512	\emph{Step 3: Cobar complex computation.}
  2513	The cobar $\Omega C_\bullet^{(1)}$ has generators dual to $C_1^{(1)}$ and differential encoded by the structure maps of the coalgebra $C_\bullet^{(1)}$. The zeroth cohomology $H^0(\Omega C_\bullet^{(1)})$ is the algebra generated by the dual generators modulo the relations imposed by~$d_\Omega$.
  2514	
  2515	The genus-1 contribution to $d_\Omega$ produces the central extension relation: for generators $J^a$ of~$\mathcal{A}$,
  2516	\[
  2517	[J^a, J^b]_{\widehat{\mathcal{A}}} = [J^a, J^b]_{\mathcal{A}} + \kappa \cdot \mathrm{Tr}(J^a \otimes J^b) \cdot \mathbf{K}
  2518	\]
  2519	where $\mathbf{K}$ is the central element and $\kappa$ is the central charge. This is the relation defining the universal central extension $\widehat{\mathcal{A}}$.
  2520	
  2521	\emph{Step 4: Universality.}
  2522	The resulting central extension is universal because any 2-cocycle $\omega: \mathcal{A} \otimes \mathcal{A} \to \mathbb{C}$ that defines a central extension of~$\mathcal{A}$ factors through the genus-1 trace pairing. Indeed, the Hochschild 2-cocycle condition requires $\omega$ to be $\mathcal{A}$-bilinear and invariant, which forces $\omega = c \cdot \mathrm{Tr}$ for some constant~$c$. The genus-1 construction produces exactly this with $c = \kappa$.
  2523	\end{proof}
  2524	
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex | sed -n '196,212p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'invariant pairing \\\\kappa|equipped with an invariant pairing \\\\kappa|where \\\\kappa is the central charge|central charge \\\\kappa|Casimir element|\\\\kappa = \\\\sum_a J\\"'^a '"\\\\otimes J_a|level \\\\kappa depends|Let \\\\"'$A_0 = '"\\\\cH_\\{24\\}.*\\\\kappa_\\{BKM\\}' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   196	\label{sec:qca-from-qg}
   197	
   198	The Costello programme constructs quantum chiral algebras from holomorphic Chern--Simons theory on complex manifolds of varying dimension. The dimensional hierarchy of the ambient space determines the $\En$ level of the resulting chiral algebra: the observables of holomorphic Chern--Simons on $\C^n$ carry $E_n$-factorization structure, and the holomorphic refinement reduces this to $E_k$-chiral structure upon projection to $\C^k$. Three regimes matter for CY quantum groups.
   199	
   200	\begin{construction}[Holomorphic Chern--Simons hierarchy]
   201	\label{constr:hol-cs-hierarchy}
   202	Let $\frakg$ be a finite-dimensional Lie algebra equipped with an invariant pairing $\kappa \colon \frakg \otimes \frakg \to \C$. Holomorphic Chern--Simons theory with gauge algebra $\frakg$ on a complex manifold $M$ has action
   203	\[
   204	 S_{\mathrm{hCS}}(A) \;=\; \frac{1}{2} \int_M \Omega \wedge \kappa\!\left(A \wedge \dbar A + \tfrac{2}{3} A \wedge A \wedge A\right),
   205	\]
   206	where $A \in \Omega^{0,1}(M; \frakg)$ is a $(0,1)$-connection and $\Omega$ is a holomorphic volume form on $M$ (when $M$ is Calabi--Yau) or a partial volume form (when $M$ is a product). The three regimes:
   207	\begin{enumerate}[label=\textup{(\roman*)}]
   208	 \item \emph{3d holomorphic CS on $\Sigma \times \R$} (Costello~2007, Costello--Gwilliam~2021):
   209	 the boundary on $\Sigma$ produces the affine Kac--Moody vertex algebra $V_k(\frakg)$ at level $k$ determined by $\kappa$. This is an $E_\infty$-chiral algebra on $\Sigma$ (in the Beilinson--Drinfeld sense) with $\Eone$-ordered refinement via the Vol~II Swiss-cheese structure.
   210	
   211	 \item \emph{5d holomorphic CS on $\C^2 \times \R$} (Costello~2013, ``Supersymmetric gauge theory and the Yangian''):
   212	 the Omega-background parameters $(h_1, h_2)$ on $\C^2$ with $h_1 + h_2 + h_3 = 0$ produce the affine Yangian $Y(\widehat{\fgl}_1)$ for $\frakg = \fgl_1$, or more generally $Y(\widehat{\frakg})$ for semisimple $\frakg$. The observables on $\C^2$ carry $\Etwo$-chiral factorization structure; projection to a curve $C \subset \C^2$ gives $\Eone$-chiral structure. The positive half $Y^+(\widehat{\fgl}_1)$ is the CoHA (which is associative, not chiral: AP-CY7). The full Yangian is recovered by the Drinfeld double.
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:820: where $\Omega_\fg$ is the Casimir element and
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1450: where $\Omega_{\mathfrak{gl}_K}$ is the Casimir element.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3296:and the null vector relation $:ff: = 0$. The Casimir element
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4595:Casimir element of $\widehat{\mathfrak{gl}}_1$ acting on
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:704: where $\Omega$ is the Casimir element and $k$ is the affine level; at $k = 0$ the $r$-matrix vanishes identically;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:285: where $\Omega$ is the Casimir element and $k$ is the affine level; at $k = 0$ the $r$-matrix vanishes identically;
chapters/examples/w_algebras_deep.tex:1642:the Casimir element $\kappa$ of $\mathfrak{sl}_3$ in the adjoint
chapters/theory/higher_genus_modular_koszul.tex:1359:higher-weight analogs (Casimir elements in
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1821: $\Omega = \sum_a J^a \otimes J^a$ is the Casimir element, the
chapters/examples/w_algebras.tex:401:The curvature of the dual is $m_0' = (k' + h^\vee) \cdot C_2 = -(k + h^\vee) \cdot C_2 = -m_0$, where $C_2$ is the quadratic Casimir element. In particular, $m_0 = 0$ if and only if $m_0' = 0$, as expected.
chapters/theory/en_koszul_duality.tex:4928:on $\Conf_n(X)$, where $\Omega_{ij}$ is the Casimir element
chapters/examples/kac_moody.tex:114:where $\Omega = \sum_a J^a \otimes J_a$ is the Casimir element, and the
chapters/examples/kac_moody.tex:523:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
chapters/examples/kac_moody.tex:651:where $\kappa$ is the Casimir element.
chapters/examples/kac_moody.tex:1182:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element.
chapters/examples/kac_moody.tex:1274:Casimir element $C_{\mathrm{adj}} = 2h^\vee \cdot \mathrm{id}$
chapters/examples/kac_moody.tex:1486:a multiple of the Casimir element
chapters/examples/kac_moody.tex:1770:the Casimir element
chapters/examples/kac_moody.tex:2211:residue gives the rational $r$-matrix. The Casimir element of
chapters/theory/derived_langlands.tex:447:Casimir element~$C$ acts on~$V$ by the nonzero scalar

thinking
**Clarifying notation conflicts**

I noticed that `cobar_construction.tex` says to use Ω instead of κ for Casimir to avoid confusion, but both `kac_moody.tex` and `higher_genus_foundations` still use κ. This seems to strengthen some findings, so I need to take a closer look at `kac_moody.tex`. It's possible that local usage is causing a conflict, especially since that file also uses modular characteristic formulas. I should check the chapter-level conventions and focus on the context around the start and line 651.
codex
I found a stronger seam: one core theory file already states the house rule “write `\Omega` rather than `\kappa` for the Casimir to avoid confusion,” while other example/theory files still use `\kappa` for the Casimir element. That gives a concrete canonical fix for the collisions I’m verifying now.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2152,2162p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '1638,1645p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa\\s*=\\s*\\\\sum_a J\\"'^a '"\\\\otimes J_a|where \\\\kappa is the Casimir element|the Casimir element \\\\kappa' chapters/examples/kac_moody.tex chapters/theory/higher_genus_foundations.tex chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1638	m_0^{\mathcal{W}_3} = \frac{c}{2}|0\rangle
  1639	= \frac{2 - 24(k+2)^2/(k+3)}{2}|0\rangle
  1640	\]
  1641	The relationship between $(k+3)\kappa/6$ and $c/2$ is:
  1642	the Casimir element $\kappa$ of $\mathfrak{sl}_3$ in the adjoint
  1643	representation has eigenvalue $2h^\vee = 6$, and the DS projection
  1644	maps $\kappa \cdot (k+3)/6 \mapsto (k+3)$. The Sugawara denominator
  1645	$2(k+h^\vee) = 2(k+3)$ then converts this to $c = 8k/(k+3)$,
 succeeded in 53ms:
  2152	\label{prop:km-bar-curvature}
  2153	\index{curvature!affine bar complex}
  2154	For the affine Kac--Moody chiral algebra $\widehat{\mathfrak{g}}_k$ at level $k$, the bar complex $\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)$ has curvature
  2155	\begin{equation}\label{eq:km-curvature-part1}
  2156	m_0 = \frac{k + h^\vee}{2h^\vee} \cdot \Omega
  2157	\end{equation}
  2158	where $h^\vee$ is the dual Coxeter number and $\Omega = \sum_a J^a \otimes J_a$ is the Casimir element (we write $\Omega$ rather than $\kappa$ for the Casimir to avoid confusion with the modular characteristic $\kappa(\cA)$). In particular:
  2159	\begin{enumerate}[label=\textup{(\roman*)}]
  2160	\item $m_1^2 = 0$ \textup{(}i.e., $d^2 = 0$ on the internal differential\textup{)} if and only if $k = -h^\vee$ \textup{(}critical level\textup{)};
  2161	\item The total bar differential $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$, regardless of the level.
  2162	\end{enumerate}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:4901:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element. This curvature arises
chapters/examples/kac_moody.tex:523:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
chapters/examples/kac_moody.tex:1182:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element.

thinking
**Searching for kappa usage**

I'm exploring whether the file w_algebras_deep uses κ as a Casimir element and if it also employs it as a modular characteristic. It seems likely it does. I need to inspect volume III for issues related to `kappa` specifically. My earlier search found some information, but I want to run a more thorough search for occurrences in the text. I'll use a regex pattern like `\bkappa\b` to catch instances that may not have approved subscripts, even if they could be within TeX comments.
exec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z])'"\\\\kappa(?"'![_''^(A-Za-z])'"' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z])'"\\\\kappa(?"'![_''^(A-Za-z])'"' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:202:Let $\frakg$ be a finite-dimensional Lie algebra equipped with an invariant pairing $\kappa \colon \frakg \otimes \frakg \to \C$. Holomorphic Chern--Simons theory with gauge algebra $\frakg$ on a complex manifold $M$ has action
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:204: S_{\mathrm{hCS}}(A) \;=\; \frac{1}{2} \int_M \Omega \wedge \kappa\!\left(A \wedge \dbar A + \tfrac{2}{3} A \wedge A \wedge A\right),
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:209: the boundary on $\Sigma$ produces the affine Kac--Moody vertex algebra $V_k(\frakg)$ at level $k$ determined by $\kappa$. This is an $E_\infty$-chiral algebra on $\Sigma$ (in the Beilinson--Drinfeld sense) with $\Eone$-ordered refinement via the Vol~II Swiss-cheese structure.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:460:This is the most speculative conjecture in the chapter: it requires (a) the 6d algebraic framework for $K3 \times E$, (b) CY-A$_3$, (c) the identification of the BKM root datum with the K3 Mukai lattice. The $\kappa$-spectrum check is $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$.
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:840:Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:900:$F_1 = \kappa \cdot \lambda_1^{\mathrm{FP}}$ holds
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:904:scalar formula $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1237:$\kappa + \kappa^! = 0$. For $\mathcal{W}_N$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1242:$\kappa + \kappa^! = 0$. For $\mathcal{W}_N$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1254:$\kappa + \kappa^! = 13 \ne 0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:212:equivalence $B_\kappa \dashv \Omega_\kappa$ on the Koszul locus
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:698:\textbf{Algebra} & \textbf{Class} & $d_{\mathrm{alg}}$ & $\kappa$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:701:Heisenberg $\cH_k$ & G & $0$ & $k$ & Yes ($\kappa = k$) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:703: Yes ($\kappa \neq 0$ for $k \neq -h^\vee$) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:715:terminates at~$\kappa$. Affine Kac--Moody is
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:875:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:884:\textup{(}$\kappa$, $S_3$, $Q^{\mathrm{contact}}$, \ldots\textup{)}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1064:obstruction tower $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1108:$\dfib^{\,2} = \kappa \cdot \omega_g$\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1361:At genus~$0$ the bar differential is a coderivation of the bar coalgebra, and $d^2$ is determined by its cogenerator projection. At genus~$g \geq 1$ the fiberwise differential $\dfib$ with $\dfib^{\,2} = \kappa \cdot \omega_g \neq 0$ is \emph{not} a coderivation (the cross terms at interior splittings produce a factor-$2$ discrepancy; see Remark~\ref{rem:bar-ordered-primacy} of Vol~I). The cogenerator projection nevertheless computes the \emph{obstruction class}: $\dfib^{\,2}$ is determined by the cogenerator projection to the degree-$1$ component $s^{-1}\cA$. This cogenerator extracts a double residue:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:1400: $\dfib^{\,2} = \kappa \cdot \omega_g$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2629: \kappa \cdot \omega_g)$ belongs to the coderived category.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2659:curved ($\dfib^{\,2} = \kappa \cdot \omega_g$), and cobar
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:2794:$(\barB^{(g)}_{\mathrm{geom}}, \dfib^{\,2} = \kappa \cdot




thinking
**Searching for findings**

I need to explore other files for similar unexpanded instances of H_N. There are many possibilities, but if H_N isn't defined nearby, they could qualify as findings. However, the task is to find every instance, so I should consider what constitutes a finding: any use of `\kappa` without a specified family or with incorrect formulas. If it’s mentioned in a context specifying a family, it doesn’t count. I’ll look for paragraphs mentioning multiple families or generic statements. Finding an efficient method for this search could save time.
thinking
**Planning findings automation**

Automating this process seems tough, but I could leverage existing file conventions and candidate lines. The user wants about 10-15 findings for a deep audit, although the instruction to "Find EVERY instance..." pushes for completeness. I'll track the total checked hits and findings count while ensuring no obvious categories are overlooked. I should mention that I checked 5973 lines and found X issues. The user requested a pass/fail verdict, so I need to focus on findings first. There are likely problematic lines to inspect, such as in `deformation_quantization.tex` and `kac_moody.tex`, where certain usages of kappa seem ambiguous or contrary to canon. I might format findings per line, grouping them if necessary.
thinking
**Formatting findings accurately**

I can include one finding referencing the first line and note its repetition at line 1182, but the format requires singular file:line references. It might be better to separate the findings. I could state the issue in the format file:523 — PROBLEM: ... and then mention that it's repeated at 1182. However, I need to ensure that the user receives an exact file:line reference for each finding, so I'll stick with the requested format for clarity.
thinking
**Evaluating findings and formatting**

The user wants exact line references for each finding. I could start with the first line at 523 as the problem, mentioning that the same substitution applies to lines 651, 966, and 1182. However, this might not satisfy the user fully. 

If they want precise file:line details for each finding, listing them can be essential. I'll focus on identifying unique problematic lines, which might be around 12-15, making it manageable. I'll search within `kac_moody.tex` for occurrences of bare kappa as Casimir using exact methods.
exec
/bin/zsh -lc "rg -n '\\\\kappa = \\\\sum_a J\\"'^a '"\\\\otimes J_a|where \\\\kappa is the Casimir element|m_0 = .*\\\\kappa' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa = \\\\sum_a J\\"'^a '"\\\\otimes J_a|where \\\\kappa is the Casimir element|central charge \\\\kappa|Casimir element \\\\kappa|\\\\mathbb\\{C\\} \\\\cdot \\\\kappa|\\\\rho\\(\\\\kappa\\)|level \\\\kappa depends|\\\\kappa\\(\\\\tau\\)' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/cobar_construction.tex chapters/examples/deformation_quantization.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
511:This is proved as Theorem~\ref{thm:universal-kac-moody-koszul} below: the bar complex of $\widehat{\mathfrak{g}}_k$ is computed via residues on FM compactifications (Step~1), the curvature $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is identified from the double-pole OPE (Step~2), the cobar OPE recovers the level $-k - 2h^\vee$ structure constants (Step~3), and the result is characterized by functorial uniqueness (Step~4).
521:m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a] = m_2(m_0, a) - m_2(a, m_0)
523:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
820:This is Theorem~\ref{thm:universal-kac-moody-koszul} applied to $\mathfrak{g} = \mathfrak{sl}_3$ with $h^\vee = 3$. The explicit bar complex computation through degree~3 (Computation~\ref{comp:sl3-bar-dimensions}) is consistent: the bar differential on $\bar{B}^1$ extracts the OPE data with the double-pole coefficient $k$, and Verdier duality on the bar coalgebra produces the Koszul dual generators with double-pole coefficient $-k - 2 \cdot 3 = -k-6$. The curvature at non-critical levels satisfies $m_0 = \frac{k+3}{6}\cdot\kappa_{\mathfrak{sl}_3}$, vanishing precisely at $k = -3$.
966:The decomposition~\eqref{eq:bar-level-decomp} reflects the level-independence of bar chain groups (Lemma~\ref{lem:bar-dims-level-independent}): $d_{\mathrm{crit}}$ encodes $\mathfrak{g}$-structure constants, $\delta$ encodes the central extension, and $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is the degree-$0$ component of $(k + h^\vee)\delta$.
1180:m_0 = \frac{k + h^\vee}{2h^\vee} \cdot \kappa \in \bar{B}^0
1182:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element.
1955:The curvature $m_0 = \frac{k+h^\vee}{2h^\vee}\kappa$ (identified in the proof of Theorem~\ref{thm:universal-kac-moody-koszul}) satisfies $m_1^2(a) = m_2(m_0, a) - m_2(a, m_0) = [m_0, a]$ for all $a \in \widehat{\mathfrak{g}}_k$, which is the curved $A_\infty$ relation replacing strict nilpotence $\dzero^2 = 0$.
 succeeded in 51ms:
chapters/examples/deformation_quantization.tex:554:\[\kappa(\tau) = \kappa_0 E_2(\tau)\]
chapters/theory/higher_genus_complementarity.tex:1426:$Z(\mathcal{H}_\kappa) = \mathbb{C} \cdot \mathbf{1} \oplus \mathbb{C} \cdot \kappa$,
chapters/theory/higher_genus_complementarity.tex:1427:the transpose $\kappa_Z$ is the identity on $\mathbb{C} \cdot \kappa$ (the level is
chapters/theory/higher_genus_complementarity.tex:1429:scalar commutation $[\mathbb{D}, \rho(\kappa)] = 0$. The action of $\kappa$ on
chapters/theory/higher_genus_complementarity.tex:1432:\rho(\kappa)(\alpha) = \lambda_1 \cup \alpha
chapters/theory/higher_genus_complementarity.tex:1727:For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
chapters/theory/higher_genus_complementarity.tex:2505:where $\omega_1 \in H^2(\overline{\mathcal{M}}_{1,1})$ is the fundamental class (the $B$-cycle monodromy of the propagator, valued in $\mathbb{C} \cdot \kappa$).
chapters/theory/higher_genus_complementarity.tex:2513:d^{(1)}_{\mathrm{total}}) = \mathbb{C} \cdot \kappa
chapters/theory/higher_genus_complementarity.tex:2538:$Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (which pairs with $H^0 = \mathbb{C}$), 
chapters/theory/higher_genus_complementarity.tex:2544:\emph{Interpretation}: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (the central extension appears as an obstruction) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$ (the first Chern class appears as a deformation).
chapters/theory/higher_genus_complementarity.tex:2791:d^{(1)}_{\mathrm{total}}) = \mathbb{C} \cdot \kappa$.
chapters/theory/higher_genus_foundations.tex:4901:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element. This curvature arises



thinking
**Considering findings in file**

I'm looking at a file that combines local and global kappa, which seems good. I noticed a potential finding in `quantum_chiral_algebras.tex:209`, where it mentions "level k determined by κ." It looks like κ is an invariant pairing, and that sounds significant to the context. I should consider how this relates to my overall research and explore its implications further.
thinking
**Identifying mathematical errors**

I’m analyzing a theorem related to complementarity, and I think there's a significant issue here. There's a critical error in stating `Z(H_κ) = C·1 ⊕ C·κ`, as a scalar isn't a central element of the algebra. This could undermine the proof due to a faulty step concerning center decomposition. I might need to suggest a specific fix: `Z(H_\kappa)= \mathbb C\cdot 1`, as the obstruction class exists in a different mathematical space.
thinking
**Revising mathematical notation**

I need to rewrite `Q_1(H_\kappa)=\mathbb C\cdot z_{\mathrm{cen}}`, clarifying that `z_{\mathrm{cen}}` is the genus-1 central-extension class with the coefficient being the scalar level `\kappa(H_\kappa)=\kappa`. It’s essential to base my corrections on specific references, especially around lines 1727, etc., where `Q1(H_kappa)=C·κ` and the dual case `Q1(H^!)=C·λ` are mentioned. The fix involves replacing `C·κ` with `C·z_{\mathrm{cen}}` in several lines, ensuring clarity about what `z_{\mathrm{cen}}` denotes. There’s also a potential high-severity error regarding "κ is the central charge" in a higher genus example.
exec
/bin/zsh -lc "rg -n 'recovering the Sugawara central charge|Sugawara central charge|central charge.*\\\\kappa\\(|\\\\kappa\\(V_k\\(\\\\mathfrak\\{g\\}\\)\\).*central charge' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'periodicity under level shift|periodic under level shift|\\\\kappa\\-periodicity|kappa-periodicity' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1692:The Sugawara central charge of $V_k(\mathfrak{sl}_3)$ is
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2564:\item The Sugawara central charge is
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:934:$c = k\dim(\fg)/(k + h^\vee)$ (the Sugawara central charge).
chapters/examples/bar_complex_tables.tex:4576:The Sugawara central charge transforms as
chapters/theory/higher_genus_modular_koszul.tex:2992:Sugawara central charge of the boundary WZW model; it is also
chapters/theory/higher_genus_modular_koszul.tex:3137:the total holographic central charge~$\kappa(V_k(\fg))$.
chapters/theory/higher_genus_modular_koszul.tex:11984:central charge $S_2 = \kappa(\cA)$ already captures the entire
chapters/examples/free_fields.tex:2875:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
chapters/theory/introduction.tex.bak:1009:\emph{Part~(a).}  The Sugawara central charge is
chapters/examples/kac_moody.tex:1553:The Sugawara central charge is
chapters/theory/introduction.tex:1048:\emph{Part~(a).} The Sugawara central charge is
chapters/theory/higher_genus_foundations.tex:5858:For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
chapters/theory/derived_langlands.tex:966:The related Sugawara central charge $c = k\dim(\fg)/(k+h^\vee)$
chapters/theory/bar_cobar_adjunction_curved.tex:5930:and curvature $\mu_0 \propto \mathbf{1}$ from the central charge (the proportionality constant depends on the $A_\infty$ model; the modular characteristic is $\kappa(\mathrm{Vir}_c) = c/2$). Since $\mathbf{1}$ is central, $\mu_0 \in Z(\mathrm{Vir}_c)$.
chapters/theory/coderived_models.tex:908:central charge, where the curvature~$\kappa(\cA)$ is nonzero
chapters/theory/cobar_construction.tex:2544:\item \emph{Kac--Moody algebras:} For the affine vertex algebra $V_k(\mathfrak{g})$ at level~$k$, the modular characteristic is $\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k + h^{\vee})/(2h^{\vee})$, recovering the Sugawara central charge. The Heisenberg algebra is a separate family with $\kappa(\mathcal{H}_k) = k$ (Census~C1); it is \emph{not} a specialization of the Kac--Moody formula (the abelian limit $\dim(\mathfrak{g}) = 1$ does not admit a dual Coxeter number).
 succeeded in 50ms:
chapters/theory/higher_genus_foundations.tex:5855:\begin{corollary}[\texorpdfstring{$\kappa$}{kappa}-periodicity under level shift; \ClaimStatusProvedHere]
chapters/theory/higher_genus_foundations.tex:5856:\label{cor:kappa-periodicity}
chapters/theory/higher_genus_foundations.tex:5858:For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.

thinking
**Inspecting findings**

I found references to total holographic central charge and another central charge, but I’m not sure if they’re accurate. I need to inspect these closely to verify their validity. It sounds like I should check the context around these terms to make sure I understand what they mean and how they relate to the findings. So, let's dig deeper into the specifics and clarify what’s actually going on!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3128,3140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11976,11988p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3128	\emph{bare} boundary coupling: it is the level-dependent piece
  3129	seen directly by the $r$-matrix, and at $k = 0$ it vanishes,
  3130	consistent with the AP\textup{126} mandate that a level-stripped
  3131	$r$-matrix $k\,\Omega/z$ must vanish at zero level. The second
  3132	summand $\tfrac{1}{2}\dim(\fg)$ is the \emph{holographic anomaly
  3133	shift} from Sugawara normal-ordering: it is the bulk one-loop
  3134	renormalization of the stress tensor, independent of level, and
  3135	it records the quantum correction that promotes the classical
  3136	Chern--Simons action to its quantum counterpart. The sum is
  3137	the total holographic central charge~$\kappa(V_k(\fg))$.
  3138	At $k = 0$ the bare piece vanishes and only the anomaly shift
  3139	survives: $\kappa = \dim(\fg)/2$ is the residual holographic
  3140	central charge of the free-field limit, not zero. At
 succeeded in 51ms:
 11976	$\mathbf{C}$ & $4$ & $S_2, S_3, S_4$ & $\beta\gamma$ &
 11977	 quartic contact term \\
 11978	$\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
 11979	 $\cW_N$ & full correction tower \\
 11980	\bottomrule
 11981	\end{tabular}
 11982	\end{center}
 11983	Class~$\mathbf{G}$ is the Brown--Henneaux regime: the leading
 11984	central charge $S_2 = \kappa(\cA)$ already captures the entire
 11985	boundary-bulk map, and no higher-degree vertices contribute.
 11986	Class~$\mathbf{L}$ admits a single quantum correction at degree~$3$,
 11987	killed at degree~$\geq 4$ by the Jacobi identity of the affine
 11988	bracket. Class~$\mathbf{C}$ admits a further quartic

thinking
**Clarifying central charge findings**

I'm reviewing some lines that mention central charge language related to kappa. There's a potential problem with the identification — `κ(V_k(g))` refers to a modular characteristic, not a central charge. There are also some discrepancies in the labels, like calling it total holographic central charge and a possibly incorrect statement on line 11984 regarding `central charge S_2 = κ(A)`. I need to search for these phrases to confirm if they appear consistently across files.
codex
I found a second object-collapse class beyond the Casimir issue: some theory prose explicitly calls `\kappa` a “central charge.” That is not a harmless synonym in this repo; the census treats `\kappa` and `c` as different invariants except in special families. I’m checking the live lines where that wording appears.
exec
/bin/zsh -lc "rg -n 'central charge["'^'"\\n]*\\\\kappa\\(|central charge["'^'"\\n]*\\\\kappa|holographic central charge~\\\\kappa|S_2 = \\\\kappa|\\\\kappa\\(.*\\) is the central charge' chapters/theory chapters/examples /Users/raeez/chiral-bar-cobar-vol2/chapters/theory /Users/raeez/chiral-bar-cobar-vol2/chapters/examples /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1408,1418p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:173:On the $\cW$-algebra side, the principal $\cW$-algebra of $\mathfrak{sl}_2$ is the Virasoro vertex algebra at central charge $c(k) = 1 - 6(k+1)^2/(k+2)$ via the Drinfeld--Sokolov formula. The level $k_{A_1}$ distinguished by the Vol~III Kazhdan--Lusztig boundary of the semiclassical locus is the unique level for which the Virasoro output matches the modular characteristic $\kappa_{\mathrm{ch}} = \mu = 1$. Substituting $\kappa_{\mathrm{ch}}^{\mathrm{Vir}} = c/2$ (the Virasoro entry of the Vol~I kappa table) and $\kappa_{\mathrm{ch}} = 1$ forces $c = 2$ on the nominal Vir side; the semiclassical limit on the LG side is instead the free-fermion normalization $c = 1/2$, whose Vir-kappa is $1/4$ and whose two Clifford states account for the factor of two in Example~\ref{ex:mf-quadratic}. The two normalizations differ by a factor attributable to the Clifford stabilization, and Conjecture~\ref{conj:ade-w-algebra} for $A_1$ asserts their equality up to this normalization: the Vol~III chiral algebra is the free fermion at $c = 1/2$, i.e.\ the Ising chiral algebra in its free-fermion presentation, with two Clifford states matching the two-dimensional endomorphism algebra of Example~\ref{ex:mf-quadratic}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1399:  S_2 = \kappa_{\mathrm{fiber}} = 24, \quad
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1856:The modular characteristic $\kappa_{\mathrm{ch}}$ of a CY$_3$ chiral algebra is determined by the CY category, not by the Virasoro central charge alone. This section establishes the key distinction between $\chi_{\mathrm{top}}/24$ and $\kappa_{\mathrm{ch}}$.
chapters/examples/symmetric_orbifolds.tex:466:the Brown--Henneaux central charge $c = 6N$ via $\kappa = c/3$
chapters/theory/higher_genus_modular_koszul.tex:3137:the total holographic central charge~$\kappa(V_k(\fg))$.
chapters/theory/higher_genus_modular_koszul.tex:11928:\item $S_2 = \kappa(\cA)$ is the leading holographic central
chapters/theory/higher_genus_modular_koszul.tex:11984:central charge $S_2 = \kappa(\cA)$ already captures the entire
chapters/theory/higher_genus_modular_koszul.tex:17371:$S_2 = \kappa$, $S_3 = \alpha$, $S_4$.
chapters/theory/higher_genus_modular_koszul.tex:19980:all conform to the pattern. At $r = 2$: $S_2 = \kappa
chapters/theory/higher_genus_modular_koszul.tex:26912: $\{S_2 = \kappa(\cA),\, S_3,\, \ldots,\, S_{r_{\max}}\}$.
chapters/theory/higher_genus_modular_koszul.tex:29022:characteristic, \emph{not} the central charge: $\kappa/(6\pi)
chapters/theory/coderived_models.tex:908:central charge, where the curvature~$\kappa(\cA)$ is nonzero
chapters/examples/free_fields.tex:311:quadratic; only $S_2 = \kappa = 1/4$ contributes. The shadow
chapters/examples/free_fields.tex:1137:at central charge $c = c_{\beta\gamma}(\lambda)$: $S_2 = \kappa = c/2$,
chapters/examples/free_fields.tex:1185:$S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
chapters/examples/free_fields.tex:2875:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
chapters/theory/introduction.tex:773:\index{holographic central charge|see{$\kappa$}}%
chapters/examples/genus_expansions.tex:441:The Feigin--Frenkel involution $k \mapsto k' = -k - 2h^\vee = -k-4$ acts on the central charge as $c \mapsto c' = 6 - c$, and on the obstruction coefficient as $\kappa \mapsto -\kappa$.
chapters/examples/genus_expansions.tex:2011:For $\mathcal{W}_3^k(\mathfrak{sl}_3)$ with central charge $c(k) = 2 - 24(k+2)^2/(k+3)$, the obstruction coefficient is $\kappa = 5c/6$ (Table~\ref{tab:master-invariants}). The genus-$g$ free energy:
chapters/examples/genus_expansions.tex:2034:The negative free energies reflect the negative central charge at $k = 1$. At the dual level $k' = -7$: $c' = 152$, $\kappa' = 380/3$, and $F_g' = -F_g + \frac{250}{3} \cdot \lambda_g^{\mathrm{FP}}$.
 succeeded in 53ms:
  1408	package of Corollary~\ref{cor:winfty-stage4-residue-four-channel}. The
  1409	first next reduced stage is the explicit eleven-entry packet
  1410	$\mathcal{J}_5^{\mathrm{red}}$ of
  1411	Corollary~\ref{cor:winfty-ds-stage5-reduced-packet}.
  1412	Complete genus-$1$ pipelines for $\mathrm{Vir}_c$
  1413	(\S\ref{sec:virasoro-genus-one-pipeline}, $c + c' = 26$, $\kappa = c/2$)
  1414	and $\mathcal{W}_3^k$
  1415	(\S\ref{sec:w3-genus-one-pipeline}, $c + c' = 100$, $\kappa = 5c/6$).
  1416	General $\mathcal{W}_N$: $\kappa = c \cdot (H_N - 1)$
  1417	(Theorem~\ref{thm:wn-obstruction}).
  1418	\end{enumerate}

thinking
**Reviewing search results**

I've got more candidate lines in my search results, but they don't seem to show concrete findings. I’m thinking it might be worth looking closely at `symmetric_orbifolds.tex:466`, especially since κ = c/3 seems a bit off. I should examine the context around this to see if I can uncover anything more meaningful. Let's dig into that!
exec
/bin/zsh -lc "nl -ba chapters/examples/symmetric_orbifolds.tex | sed -n '458,470p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   458	of $1/g_s^2$.
   459	\end{remark}
   460	
   461	For $X = T^4$ or $K3$, Costello--Paquette
   462	\cite{CP2020} identify the large-$N$ boundary
   463	chiral algebra with the free symmetric orbifold, and the
   464	bulk Kodaira--Spencer theory with the holographic dual.
   465	The modular characteristic $\kappa = 2N$ (for $K3$) matches
   466	the Brown--Henneaux central charge $c = 6N$ via $\kappa = c/3$
   467	(the anomaly ratio for $K3$ is $\varrho = 1/3$, not $1/2$,
   468	because $K3$ has both Virasoro and affine currents).
   469	
   470	

thinking
**Looking into family-specific details**

I think it might be okay to consider some family-specific aspects for K3, though I'm not sure if it’s necessary to include them in the census. I should take a look at `higher_genus_modular_koszul.tex` for the actual line if I’m looking into the \kappa central charge because major canonical theory might be important. The user asks for an exact fix, so I'll inspect the context around line 11928 as well.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11924,11930p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29018,29024p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 11924	= \cA^{\mathrm{sh}}_{r,0}$ is the order-$r$ correction to this
 11925	reconstruction, and the depth class of~$\cA$ is the truncation
 11926	order of the correction series.
 11927	\begin{itemize}
 11928	\item $S_2 = \kappa(\cA)$ is the leading holographic central
 11929	 charge: the classical response of the bulk to a boundary
 11930	 perturbation, measured by the cylinder two-point function.
 succeeded in 51ms:
 29018	modular graph class\textup{)} against the conformal
 29019	deformation~$\sigma$.
 29020	
 29021	\item The coefficient $\kappa/(6\pi)$ involves the modular
 29022	characteristic, \emph{not} the central charge: $\kappa/(6\pi)
 29023	\neq c/(6\pi)$ in general. The classical Polyakov coefficient
 29024	$1/(6\pi)$ for a single scalar field arises only for the




thinking
**Investigating notation issues**

I need to check `deformation_quantization.tex` at line 451 to clarify the Heisenberg algebra notation. Using κ as Heisenberg level isn't wrong since the modular characteristic is the same, but line 457 introduces it differently with a propagator integral and line 554 complicates it with a τ-dependent κ. I think the focus needs to shift to lines 457 and 554 instead. At line 457, κ is defined as an integral parameter, and later as a canonical characteristic—causing potential confusion with notation.
thinking
**Renaming parameters for clarity**

I need to rename the local parameter to `t_{\mathrm{dq}}` consistently throughout Example 1, such as in `a(z)a^*(w) ∼ t_{\mathrm{dq}}/(z-w)` and `t_{\mathrm{dq}} = \hbar\int_{\overline C_2(X)}\eta_{12}`. I also want to add a sentence clarifying that `t_{\mathrm{dq}}` is not the modular characteristic κ(ℵ). 

There's a tau-dependent issue at line 554, where κ(τ) conflicts with κ(ℵ) as a fixed algebra invariant. I should replace it with `t_{\mathrm{ell}}(τ)` and clarify that the quasi-modular dependence resides in the genus-1 propagator coefficient. Additionally, there appears to be a similar problem at `quantum_chiral_algebras.tex:202-209`.
thinking
**Analyzing code context**

I need to check line 2791 for context since it appears to have repeated class instances. I don't think I need to inspect beyond that. If I mention repeated lines, I’ll want to confirm it, but the previous search output seems adequate.

I notice a potential collision in the file at line 2519 where it uses `\kappa` as a central charge, but line 2158 uses Ω instead of κ, which suggests possible misidentification. Other assorted lines have varying potentials for issues, ranging from high to low.
thinking
**Inspecting candidate formulations**

I’m considering another candidate here: `kac_moody.tex:1555 Setting \kappa = c/2 leads to...` This seems like it could represent a correct reductio if it implies that stating a wrong formula results in a contradiction. I need to take a closer look at this to verify how it fits into my reasoning. There’s a lot to unpack here, and I want to make sure I'm getting this right!
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1548,1560p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1548	$\kappa_{\mathrm{dp}} = k\cdot\dim(\fg)$ (with no $h^\vee$
  1549	normalization needed), recovering
  1550	$\kappa(\mathcal{H}_k^{\oplus d}) = dk$
  1551	(Computation~\ref{comp:rank-d-heisenberg-genus1}).
  1552	\item \emph{Sugawara comparison.}
  1553	The Sugawara central charge is
  1554	$c = k\dim(\fg)/(k+h^\vee)$.
  1555	Setting $\kappa = c/2$ leads to
  1556	$(k+h^\vee)^2 = kh^\vee$, i.e.,
  1557	$k^2 + kh^\vee + (h^\vee)^2 = 0$,
  1558	which has no real solutions (discriminant
  1559	$-3(h^\vee)^2 < 0$). Hence
  1560	$\kappa \neq c/2$ for all real~$k$.


thinking
**Addressing findings in the document**

I’m considering the identification of repeated findings at line 3137 or 11928, settling on 3137 for now. The problem here is the 'total holographic central charge' term. I think I should fix it by replacing 'central charge' with 'modular characteristic' or 'holographic obstruction coefficient.' If it's meant to be 'central charge,' I might need the Sugawara term 'c(V_k(g))'. Do we also need to check 11928? It's uncertain, but maybe I should mention similar adjustments at 11928 and 11984.
thinking
**Considering document indexing**

I need to think about whether the term "holographic central charge" should be included in the index at introduction.tex on line 773. I’m wondering if it’s necessary, but maybe I should just leave it out for now. It feels like I might be overthinking it, so perhaps I should just decide to leave it as is. Keeping the document simple could be better!
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex | sed -n '454,462p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   454	\begin{enumerate}[label=\textup{(\roman*)}]
   455	 \item The defect algebra $A^!_{K3 \times E}$ on $E$ is a deformation of the Koszul dual of the BKM vertex algebra $V_{\mathfrak{g}_{\Delta_5}}$, with deformation controlled by the K3 complex structure moduli.
   456	 \item The Wilson lines wrapping $E$ are indexed by Mukai vectors $v \in H^*(K3, \Z)$; the fusion of Wilson lines is controlled by the Mukai pairing.
   457	 \item The coproduct on $A^!_{K3 \times E}$ is the chiral coproduct of Vol~I (test-scaffolded for spin-$2$ in the latest commit), specialized to the $K3 \times E$ root datum.
   458	 \item The $\Etwo$-braided representation category of the chiral quantum group is the Verlinde category of the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ (Proposition~\ref{prop:mtc-k3}, Chapter~\ref{ch:e2-chiral}).
   459	\end{enumerate}
   460	This is the most speculative conjecture in the chapter: it requires (a) the 6d algebraic framework for $K3 \times E$, (b) CY-A$_3$, (c) the identification of the BKM root datum with the K3 Mukai lattice. The $\kappa$-spectrum check is $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$.
   461	\end{conjecture}
   462	
codex
- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1426](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1426) — PROBLEM: `\kappa` is treated as a central basis vector and cohomology generator: `Z(\mathcal H_\kappa)=\mathbb C\cdot\mathbf1\oplus\mathbb C\cdot\kappa`, `\rho(\kappa)`, `Q_1(\mathcal H_\kappa)=\mathbb C\cdot\kappa`. That collapses a scalar level/modular characteristic into an algebra element. FIX: introduce a new genus-1 class symbol, e.g. `z_{\mathrm{cen}}`, and rewrite this lane as `Q_1(\mathcal H_\kappa)=\mathbb C\cdot z_{\mathrm{cen}}`, `\rho(z_{\mathrm{cen}})(\alpha)=\lambda_1\cup\alpha`; keep the coefficient separate as `\kappa(\mathcal H_\kappa)=\kappa`. Apply the same replacement at lines 1427-1435, 1727-1729, 2505-2513, 2538-2544, and 2791.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:2322](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:2322) — PROBLEM: the Heisenberg section says “The central charge `\kappa` now appears in”, reidentifying the Heisenberg level/modular characteristic as a central charge. FIX: change the sentence to `The Heisenberg level, equivalently the modular characteristic \kappa(\mathcal H_\kappa)=\kappa, now appears in:`; if central charge is needed, write it separately as `c(\mathcal H)=1`.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:3816](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:3816) — PROBLEM: in the genus-1 Heisenberg example, `\kappa` is again called “the central charge”. FIX: rewrite line 3816 as `where \kappa=\kappa(\mathcal H_\kappa)` is the Heisenberg level/modular characteristic, and `[1]^{(1)}` is the genus-1 identity element`; also change line 3790 to `For the Heisenberg vertex algebra \mathcal H_\kappa at level \kappa`.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:4901](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4901) — PROBLEM: the file reuses bare `\kappa` for the Casimir element `\sum_a J^a\otimes J_a`, colliding with the chapter’s obstruction-coefficient `\kappa`. FIX: replace the Casimir symbol by `\Omega` in this subsection: `m_0=\frac{k+h^\vee}{2h^\vee}\Omega`, `\Omega=\sum_a J^a\otimes J_a`, and update downstream mentions accordingly.

- [HIGH] [chapters/examples/kac_moody.tex:521](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:521) — PROBLEM: `kac_moody.tex` defines `m_0=((k+h^\vee)/(2h^\vee))\kappa` with `\kappa` the Casimir element, despite the manuscript’s own rule that the Casimir should be `\Omega` to avoid confusion with the modular characteristic. FIX: replace the Casimir symbol by `\Omega` at lines 511, 521-523, 966, 1180-1182, and 1955; reserve `\kappa(\widehat{\mathfrak g}_k)` for the scalar modular characteristic.

- [HIGH] [chapters/examples/w_algebras_deep.tex:1642](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:1642) — PROBLEM: `\kappa` is used for the `\mathfrak{sl}_3` Casimir element inside a chapter that already uses `\kappa` for the modular characteristic of `\mathcal W_3` and `\mathcal W_N`. FIX: rename the Lie-theoretic tensor to `\Omega_{\mathfrak{sl}_3}` and rewrite the paragraph as `the Casimir element \Omega_{\mathfrak{sl}_3} ... maps \Omega_{\mathfrak{sl}_3}\cdot (k+3)/6 \mapsto (k+3)`.

- [HIGH] [chapters/theory/cobar_construction.tex:2519](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2519) — PROBLEM: the universal central-extension relation calls bare `\kappa` “the central charge”. In this repo `\kappa` is the modular characteristic, not a generic central-extension parameter. FIX: change the coefficient in line 2517 to a new symbol, e.g. `t_{\mathrm{cen}}`, and rewrite lines 2519-2522 and 2527-2528 as `t_{\mathrm{cen}}`/`\omega_{\mathrm{cen}}`, not `\kappa`.

- [HIGH] [chapters/theory/cobar_construction.tex:2544](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2544) — PROBLEM: `\kappa(V_k(\mathfrak g))=\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)` is said to recover the Sugawara central charge. It does not; the Sugawara central charge is `c(V_k(\mathfrak g))=k\dim(\mathfrak g)/(k+h^\vee)`. FIX: replace `recovering the Sugawara central charge` with `distinct from the Sugawara central charge`, and append the explicit central-charge formula.

- [HIGH] [chapters/examples/deformation_quantization.tex:457](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:457) — PROBLEM: Example 1 defines bare `\kappa` as a propagator integral deformation parameter, while the same file later uses canonical family-valued `\kappa(\widehat{\fg}_k)`. That makes bare `\kappa` denote two different invariants in one chapter. FIX: rename the local parameter throughout Example 1 to `t_{\mathrm{dq}}`: `a(z)a^*(w)\sim t_{\mathrm{dq}}/(z-w)`, `t_{\mathrm{dq}}=\hbar\int_{\overline C_2(X)}\eta_{12}`, and add `t_{\mathrm{dq}}` is not the modular characteristic `\kappa(\cA)`.

- [HIGH] [chapters/examples/deformation_quantization.tex:554](/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:554) — PROBLEM: `\kappa(\tau)=\kappa_0E_2(\tau)` makes `\kappa` into a `\tau`-dependent quasi-modular function, conflicting with the manuscript’s use of `\kappa(\cA)` as a fixed invariant of the algebra. FIX: replace this by a new symbol such as `A_{\mathrm{ell}}(\tau)=A_0E_2(\tau)` and state explicitly that the quasi-modular dependence belongs to the genus-1 propagator coefficient, not to `\kappa(\cA)`.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:3137](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3137) — PROBLEM: the file calls `\kappa(V_k(\fg))` a “total holographic central charge”, collapsing `\kappa` and `c`. The repo elsewhere explicitly distinguishes them. FIX: replace `central charge` by `modular characteristic` or `obstruction coefficient` here, and make the same wording change at lines 11928 and 11984; if a central charge is intended, write the separate Sugawara `c(V_k(\fg))`.

- [MEDIUM] [chapters/theory/quantum_chiral_algebras.tex:202](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:202) — PROBLEM: Vol III uses bare `\kappa` for an invariant pairing `\frakg\otimes\frakg\to\C`, violating the volume’s own kappa-discipline and colliding with the modular-characteristic notation. FIX: rename the pairing to `B_{\frak g}` or `(-,-)_{\frak g}` at lines 202, 204, and 209.

- [MEDIUM] [chapters/theory/higher_genus_foundations.tex:5858](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5858) — PROBLEM: the corollary is titled and stated as `\kappa`-periodicity, but the displayed formula is affine-linear: `\kappa(k+n)=\kappa(k)+n\,d/(2h^\vee)`. That is not periodic. FIX: rename the heading and first sentence to `Affine-linear level-shift formula for \kappa` / `\kappa shifts affinely under integral level translation`; keep the formula itself.

- [MEDIUM] [chapters/examples/landscape_census.tex:1416](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:1416) — PROBLEM: the canonical `\mathcal W_N` formula uses `H_N-1` without defining `H_N` in the same sentence, on the exact seam where this repo repeatedly drifts between `H_N-1` and `H_{N-1}`. FIX: rewrite the line as `General \mathcal W_N: \kappa(\mathcal W_N)=c\sum_{j=2}^{N}1/j = c(H_N-1),\; H_N=\sum_{j=1}^{N}1/j.`

- [LOW] [chapters/theory/quantum_chiral_algebras.tex:460](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:460) — PROBLEM: `The \kappa-spectrum check` reintroduces bare `\kappa` even though the actual quantities are `\kappa_{\mathrm{ch}}` and `\kappa_{\mathrm{BKM}}`. FIX: change the phrase to `the $(\kappa_{\mathrm{ch}},\kappa_{\mathrm{BKM}})$-spectrum check` or `the modular-characteristic spectrum check`.

## Summary
Checked: 5973 | Findings: 15 | Verdict: FAIL
tokens used
195,682
