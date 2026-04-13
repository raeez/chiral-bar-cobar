# S09_examples_mutual (571s)

- [HIGH] chapters/examples/landscape_census.tex:447 — PROBLEM: The canonical class-`L` caption writes `\Omega/(k{+}h^\vee)\,z`, which parses as `(\Omega/(k+h^\vee))z`, not the KZ form `\Omega/((k+h^\vee)z)`. That breaks the stated equivalence to `k\Omega_{\mathrm{tr}}/z`. FIX: replace the caption fragment with `\Omega/\bigl((k{+}h^\vee)z\bigr)` or `\frac{\Omega}{(k{+}h^\vee)z}`.

- [HIGH] chapters/examples/kac_moody.tex:2094 — PROBLEM: The same denominator drift reappears in the explicit `\widehat{\mathfrak{sl}}_2` seam computation; `r(z)=\Omega/(k+2)\,z` no longer matches the chapter’s own KZ normalization at 731-750. The same bad form repeats at 2263 and 2357. FIX: change all three occurrences to `r(z)=\frac{\Omega}{(k+2)z}` and `r_{ij}=\frac{\Omega}{(k+2)z_{ij}}`.

- [HIGH] chapters/examples/w_algebras.tex:127 — PROBLEM: The Vir/W-seam collapses the curvature element into scalars. The file says the curvature is “non-scalar” and then writes `m_0^{(T)} = c/2`, `m_0^{(W)} = c/3`; the same false scalarization recurs at 1548, 1557, 1901-1902, and 2780, contradicting the file’s own correction at 1165 and 1320 that `m_0` is not a scalar multiple of the vacuum. FIX: rename every scalar channel to coefficient notation, e.g. `\kappa_T = c/2`, `\kappa_W = c/3`, and reserve `m_0` for the actual degree-2 element; at 1548 specifically replace `m_0 = c/2` with `\kappa(\mathrm{Vir}_c)=c/2`, and if the element is needed add `m_0` is characterized by `[m_0,T]=(c/2)\mathbf{1}`.

- [MEDIUM] chapters/examples/w_algebras.tex:1261 — PROBLEM: The KM→Vir handoff introduces `c(k)=1-6(k+1)^2/(k+2)` without explicitly fencing it off from the affine Sugawara charge `3k/(k+2)` in chapters/examples/kac_moody.tex:432. The same level parameter `k` is reused, so the seam hides that two different central-charge functions are in play. FIX: append after 1264: `This \(c(k)\) is the Drinfeld--Sokolov reduced Virasoro central charge; it is not the affine Sugawara charge \(3k/(k+2)\) of the parent \(\widehat{\mathfrak{sl}}_2\).`

- [MEDIUM] chapters/examples/w_algebras.tex:1269 — PROBLEM: The critical-level sentence gives the affine critical point `k=-2`, but the explicit Virasoro pipeline later uses the uncurved condition `c=0` (`1548`, `1620-1622`) without stitching the two apart at the seam. That invites the false reading that the Virasoro uncurved point is the affine critical point. FIX: append after 1271 or 1622: `The affine critical point \(k=-2\) is distinct from the Virasoro uncurved locus \(c=0\); under \(c(k)=1-6(k+1)^2/(k+2)\), the latter occurs away from the critical affine level.`

- [LOW] chapters/examples/kac_moody.tex:19 — PROBLEM: The chapter opening hands off to Virasoro only by saying Jacobi no longer kills the tower; it does not state the actual seam invariant used later in the census and Virasoro chapter, namely `Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]` and class `M`. FIX: replace the last clause with `for the Virasoro algebra (Chapter~\ref{chap:w-algebra-koszul}), the quartic contact term \(Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]\) is generically nonzero and the quintic obstruction is forced, so the tower is class~M and does not terminate.`

## Summary
Checked: 3 | Findings: 6 | Verdict: FAIL


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
session id: 019d83c7-833e-7c71-b6c9-da2ba7452804
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


MISSION: SEAM AUDIT between kac_moody.tex and virasoro.tex.

KM→Vir examples. Check: (a) kappa formulas consistent, (b) r-matrix conventions consistent, (c) classification (L vs M) consistent, (d) central charge formulas match census

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers

thinking
**Planning a code/math audit**

I need to perform a code and math audit in the repository, following the AGENTS instructions. Before making any edits, I should read several documents, such as CLAUDE.md and the theorem registry. The user asked for an audit, not an edit, so I need to be careful about how I approach it. It seems like I may need to use deep-beilinson-audit and possibly multi-path-verify for formulas. I should begin by updating the user on my first steps.
codex
Scope is the `kac_moody.tex` ↔ `virasoro.tex` seam. I’m reading the constitutional surfaces and the two chapter files first, then I’ll run a hostile consistency pass on `\kappa`, `r(z)`, L/M classification, and central-charge formulas with exact line references only.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
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

 succeeded in 55ms:
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

 succeeded in 55ms:
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
 succeeded in 55ms:
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
**Evaluating skill usage**

I need to use my skill here and open the SKILL.md file for the deep-beilinson-audit. I’m considering using multi-path-verify, but it might not be necessary since the task is about auditing seams and verifying formulas. A minimal set of checks could include deep-beilinson-audit, while independent checks on specific formulas matter. I'll need to read the skill docs for better clarity. Let's dive into that!
codex
I’ve loaded the repo-wide audit constraints. Next I’m opening the `deep-beilinson-audit` workflow, and likely `multi-path-verify` for the formula checks, then I’ll inspect the two example chapters and the census surfaces around the seam.
exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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


thinking
**Inspecting target files**

I need to inspect the target files and any relevant dependencies, like landscape_census, and also identify transition points. It’s essential to locate the files and any relevant seam lines. I’ll be searching for kac_moody, virasoro, and kappa/r matrices, along with classifications and central charge. I'll inspect the exact files around all hits, using rg with line numbers. Plus, I'll look into formulas related to landscape_census. Let’s get started on that!
codex
The audit protocol is loaded. I’m locating every seam-relevant occurrence in `chapters/examples/kac_moody.tex`, `chapters/examples/virasoro.tex`, and the census so I can read the local transitions rather than sampling isolated lines.
exec
/bin/zsh -lc 'wc -l chapters/examples/kac_moody.tex chapters/examples/virasoro.tex chapters/connections/landscape_census.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa|r\\(z\\)|R-matrix|r-matrix|class L|class M|central charge|c/2|h\\"'^v|H_N|W_N|Virasoro|Kac|affine|trace-form|KZ" chapters/examples/kac_moody.tex chapters/examples/virasoro.tex chapters/connections/landscape_census.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
    6074 chapters/examples/kac_moody.tex
    6074 total
wc: chapters/examples/virasoro.tex: open: No such file or directory
wc: chapters/connections/landscape_census.tex: open: No such file or directory
 exited 2 in 51ms:
Total output lines: 577

chapters/examples/kac_moody.tex:1:\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
chapters/examples/kac_moody.tex:5:degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
chapters/examples/kac_moody.tex:12:cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
chapters/examples/kac_moody.tex:19:theory is simpler than gravity; for the Virasoro algebra
chapters/examples/kac_moody.tex:21:quartic Virasoro OPE, the tower does not terminate.
chapters/examples/kac_moody.tex:62: $\kappa(\widehat{\fg}_k)
chapters/examples/kac_moody.tex:64: $\kappa + \kappa' = 0$ (affine KM)
chapters/examples/kac_moody.tex:65: & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
chapters/examples/kac_moody.tex:77:\caption{Shadow archetype data for affine
chapters/examples/kac_moody.tex:78:Kac--Moody.}\label{tab:km-shadow-archetype}
chapters/examples/kac_moody.tex:85:$\kappa(\widehat{\fg}_k)$ &
chapters/examples/kac_moody.tex:88: $\kappa(x,[y,z])$ (Lie bracket) \\
chapters/examples/kac_moody.tex:90:$r$-matrix $r(z)$ & $\Omega/\bigl((k{+}h^\vee)\,z\bigr)$ (Casimir, KZ normalisation, Comp.~\ref{comp:sl2-collision-residue-kz}) \\
chapters/examples/kac_moody.tex:92: (sharing $\kappa$ with $\widehat{\fg}_{-k-2h^\vee}$) \\
chapters/examples/kac_moody.tex:93:Complementarity & $\kappa + \kappa' = 0$ (affine KM) \\
chapters/examples/kac_moody.tex:105:(Definition~\ref{def:modular-koszul-triple}) of the affine
chapters/examples/kac_moody.tex:106:Kac--Moody algebra at generic level $k \neq -h^\vee$ is
chapters/examples/kac_moody.tex:112:r(z) = \frac{\Omega}{(k{+}h^\vee)\,z}\,\Bigr),
codex
The initial search hit a path mismatch: `kac_moody.tex` exists where expected, but `virasoro.tex` and `landscape_census.tex` are elsewhere. I’m resolving the live paths before auditing to avoid reviewing the wrong surface.
exec
/bin/zsh -lc "rg --files | rg 'virasoro|landscape_census|census'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/census.json
virasoro_r_matrix.pdf
compute/lib/lattice_shadow_census.py
compute/lib/virasoro_bar_zhu.py
compute/lib/theorem_genus4_virasoro_engine.py
compute/lib/virasoro_shadow_extended.py
compute/lib/virasoro_shadow_all_arity.py
compute/lib/bar_cohomology_virasoro_explicit_engine.py
compute/lib/virasoro_ainfty.py
chapters/examples/landscape_census.tex
compute/tests/test_virasoro_bar.py
compute/tests/test_virasoro_shadow_tower.py
compute/tests/test_virasoro_ainfty_higher.py
compute/tests/test_virasoro_shadow_duality.py
compute/results/virasoro_bar_cohomology.jsonl
compute/scripts/virasoro_shadow_gf_analysis.py
compute/scripts/verify_virasoro_m4.py
compute/lib/virasoro_pbw_genus1.py
standalone/virasoro_r_matrix.pdf
standalone/cover_letter_virasoro_r_matrix.tex
exec
/bin/zsh -lc "rg -n \"Virasoro|W_2|c/2|class M|class L|H_N|kappa\\(Vir|r\\"'^Vir|r'"\\(z\\) = .*z\\"'^3|central charge" chapters/examples chapters/connections chapters/theory appendices' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 3660

appendices/general_relations.tex:28:Each entry represents a precise functor or natural transformation between categories. For instance, the correspondence ``Chiral multiplication $\leftrightarrow$ Residues at collision divisors'' is the content of Theorem~\ref{thm:residue-formula}, establishing that the multiplication map factors through the residue homomorphism. Similarly, ``Central extensions $\leftrightarrow$ Curved $A_\infty$ structures'' reflects Theorem~\ref{thm:heisenberg-bar}, showing how the failure of strict associativity due to central charges is precisely captured by the curvature term $m_0$.
appendices/general_relations.tex:60:$T(z)$ & $T(w)$ & $\frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w}$ \\
appendices/signs_and_shifts.tex:1614:\emph{Wrong.} ``The Sugawara central charge diverges at $k = -h^\vee$.''
appendices/signs_and_shifts.tex:1619:not merely in the central charge formula.
appendices/signs_and_shifts.tex:1635:\subsection{Pitfall 6: Virasoro self-duality point}
appendices/signs_and_shifts.tex:1637:\emph{Wrong.} ``The Virasoro algebra is self-dual at $c = 26$.''
appendices/homotopy_transfer.tex:717:algebras and the Virasoro algebra are chirally Koszul (all standard
appendices/computational_tables.tex:74:For the $W_3$ algebra with generators $\{L_n\}_{n \in \mathbb{Z}}$ (Virasoro) and $\{W_n\}_{n \in \mathbb{Z}}$ (weight-3 field):
appendices/computational_tables.tex:144:\subsection{Coefficient values for standard central charges}
appendices/combinatorial_frontier.tex:117:The zeroth column ($n=0$) is always~$1$: the augmentation $\cA \to \mathbb{C}$ contributes a one-dimensional class in bar degree zero. The first column ($n=1$) equals $\dim\overline{\cA}_{[1]}$, the dimension of the weight-$1$ augmentation ideal. For Kac--Moody algebras $\widehat{\mathfrak{g}}_k$, this is $\dim\mathfrak{g}$; for the Virasoro algebra, it is~$1$ (the single generator~$T$); for $\mathcal{W}_3$, it is~$2$ (generators $T$ and~$W$).
appendices/combinatorial_frontier.tex:119:\emph{The data is level-independent.} For every algebra in the table, the bar cohomology dimensions are independent of the level~$k$ (or central charge~$c$) at generic values. This is a deep consequence of the PBW spectral sequence structure: the $E_1$ page is a Lie algebra cohomology computation that depends only on the underlying finite-dimensional data $(\mathfrak{g}, \dim\mathfrak{g}, h^\vee)$, not on the level (this follows from the PBW spectral sequence: at generic level the $E_2$ page is level-independent, and concentration at $E_2$ gives the result; see Theorem~\ref{thm:master-pbw}). The level enters only through the curvature term $\omega_g$ at genus $g \geq 1$, which affects the genus expansion (Theorem~\ref{thm:genus-universality}) but not the bar cohomology dimensions themselves.
appendices/combinatorial_frontier.tex:232:Riordan numbers count several classical objects~\cite{BernhartRiordan}: Motzkin paths of length~$n$ that never touch the $x$-axis except at endpoints; non-crossing partitions of $\{1, \ldots, n\}$ without singleton blocks; and certain classes of restricted lattice paths. Their brief appearance in the old chiral bar-cohomology count motivates the \emph{conjectural} search for a combinatorial model of the $\widehat{\mathfrak{sl}}_2$ bar complex in terms of non-crossing structures, analogous to the Motzkin-path model for the Virasoro algebra (Theorem~\ref{thm:motzkin-path-model}). No such model has been constructed.
appendices/combinatorial_frontier.tex:238:The actual bar cohomology $\dim H^n = 2n+1$ grows only \emph{linearly}, far below the Riordan prediction: the Garland--Lepowsky concentration for semisimple~$\mathfrak{g}$ causes massive cancellation in the CE complex, collapsing the exponential chain-group dimensions to linear cohomology dimensions. The exponential growth-rate bound $3^n$ is far from saturated for $\widehat{\mathfrak{sl}}_2$; it IS saturated for the Virasoro and $\beta\gamma$ families (Remark~\ref{rem:garland-lepowsky-sl2}).
appendices/combinatorial_frontier.tex:240:\subsection{Motzkin numbers and their differences (Virasoro)}
appendices/combinatorial_frontier.tex:256:$\dim(\mathrm{Vir}_c^!)_n = M(n+1) - M(n)$ for all $n \geq 1$ (Theorem~\ref{thm:spectral-sequence-collapse}). The differences $M(n+1) - M(n)$ (OEIS~A002026) count $U$-initial Motzkin paths of length~$n+1$, i.e., Motzkin paths whose first step is an up step. This count has a direct representation-theoretic meaning: the bijection of Theorem~\ref{thm:motzkin-path-model} associates to each basis element of $H^n(\barBgeom(\mathrm{Vir}_c))$ a $U$-initial Motzkin path, with the three step types corresponding to the three singular terms in the Virasoro OPE $T(z)T(w)$.
appendices/combinatorial_frontier.tex:338:\item \emph{Virasoro at low degree.} The first few Virasoro bar cohomology dimensions $(1, 2, 5, 12, 30)$ begin with a Catalan-adjacent pattern: $C_1 = 1$, $C_2 = 2$, $C_3 = 5$. The agreement is not coincidental but breaks at $n = 4$ ($C_4 = 14 \neq 12$), reflecting the distinction between the full Catalan enumeration and the Motzkin-difference count.
appendices/combinatorial_frontier.tex:425:For $E_\infty$-chiral algebras (Kac--Moody, Virasoro), the bar generating function is algebraic of degree~$2$ over $\mathbb{Q}(x)$ (Corollary~\ref{cor:algebraicity-koszul}). The Yangian is $E_1$-chiral, not $E_\infty$, and the rationality of its bar GF may reflect the stronger algebraic constraints of the $E_1$ structure (full associativity of the chiral product, not just homotopy associativity).
appendices/combinatorial_frontier.tex:597:$\mathrm{Vir}_c$ & $c/2$ & $\mathrm{Vir}_{26-c}$ \quad ($\kappa + \kappa' = 13$) \\
codex
The Virasoro surface is not a single `chapters/examples/virasoro.tex` file. I’m resolving which chapter actually carries the seam by matching chapter titles and local KM→Vir transition language before I audit any “transition point.”
exec
/bin/zsh -lc "rg --files chapters/examples | rg 'vir|w_'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\chapter\\{|\\\\section\\{|transition|Kac--Moody|Virasoro|Heisenberg\" chapters/examples/*.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex
chapters/examples/logarithmic_w_algebras.tex
chapters/examples/w_algebras.tex
 succeeded in 51ms:
rg: regex parse error:
    (?:\chapter\{|\section\{|transition|Kac--Moody|Virasoro|Heisenberg)
       ^^
error: unrecognized escape sequence

thinking
**Searching for Virasoro content**

I'm considering whether there's content about Virasoro in the w-algebras or theory files. It might be tricky since the chapter name might not include "Virasoro" due to being in a deep folder. I think I should use a search command like `rg -n "chapter{.*Virasoro"` to locate it in chapters or examples. It feels like a good way to find what I need without digging through every file manually. Let's see how this goes!
exec
/bin/zsh -lc "rg -n 'chap:.*vir|label\\{chap:.*vir|Virasoro algebra' main.tex chapters/examples/*.tex chapters/theory/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\chapter\\{["'^}]*Virasoro|'"\\\\section\\{["'^}]*Virasoro|'"\\\\subsection\\{["'^}]*Virasoro'"' chapters/examples chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:310:This generates the Virasoro algebra with central charge:
chapters/examples/minimal_model_examples.tex:468:$\mathcal{L}_{r,s}$ of the Virasoro algebra at central charge
chapters/examples/minimal_model_examples.tex:545:The Ising model Virasoro algebra at $c = 1/2$ has the following
chapters/examples/minimal_model_examples.tex:573:Virasoro algebras: it arises from the subleading $T_{(1)}T = 2T$
chapters/examples/minimal_model_examples.tex:643:The Koszul dual of the Ising Virasoro algebra is
chapters/examples/minimal_model_examples.tex:648:$\kappa_{\mathrm{Vir}}+\kappa_{\mathrm{Vir}}' = 13$ for all Virasoro algebras;
chapters/examples/minimal_model_examples.tex:664:Virasoro algebra (Remark~\ref{rem:virasoro-complementarity-potential}).
chapters/examples/bar_complex_tables.tex:12:\noindent\emph{Exhaustive degree-by-degree bar complex computations for $\mathfrak{sl}_3$, $\mathcal{W}_3$, $E_8$, and the Virasoro algebra, complementing the Heisenberg calculations of Chapter~\ref{ch:heisenberg-frame}. Every structure constant, differential matrix, and chain-level verification that the preceding chapters deferred to ``explicit computation'' appears here.}
chapters/examples/bar_complex_tables.tex:249:\index{Virasoro algebra!bar complex}
chapters/examples/bar_complex_tables.tex:250:The Virasoro algebra has a single strong generator $T$ (conformal weight~$2$) with OPE:
chapters/examples/bar_complex_tables.tex:2634:\index{Virasoro algebra!bar complex!degree 3}
chapters/examples/bar_complex_tables.tex:3685:\index{Virasoro algebra!bar complex!degrees 4 and 5}
chapters/examples/bar_complex_tables.tex:3730:\index{Virasoro algebra!bar complex!degree 4}
chapters/examples/bar_complex_tables.tex:3824:\index{Virasoro algebra!bar complex!degree 5}
chapters/examples/bar_complex_tables.tex:3860:\index{Virasoro algebra!bar complex!dimension table}
chapters/examples/bar_complex_tables.tex:3910:\index{Virasoro algebra!bar cohomology}
chapters/examples/bar_complex_tables.tex:3912:For the Virasoro algebra $\mathrm{Vir}_c$ at any $c$, the PBW filtration
chapters/theory/computational_methods.tex:129:For the Virasoro algebra at central charge~$c$:
chapters/theory/computational_methods.tex:165:The value $\alpha = 2$ for the Virasoro algebra is not assumed.
chapters/theory/computational_methods.tex:301:For the Virasoro algebra:
 succeeded in 51ms:
appendices/branch_line_reductions.tex:429:\section{Virasoro positive-weight acyclicity and reduced spectral localization}
appendices/nonlinear_modular_shadows.tex:1269:\section{Mixed cubic--quartic families: Virasoro and principal \texorpdfstring{$\mathcal W_N$}{WN}}
appendices/nonlinear_modular_shadows.tex:1300:\subsection{Virasoro}
appendices/signs_and_shifts.tex:1635:\subsection{Pitfall 6: Virasoro self-duality point}
appendices/combinatorial_frontier.tex:240:\subsection{Motzkin numbers and their differences (Virasoro)}
appendices/combinatorial_frontier.tex:860:\subsection{Near-rationality of the Virasoro bar sequence}
appendices/ordered_associative_chiral_kd.tex:3078:\subsection{The Virasoro ordered bar complex and the gravitational Yangian}
chapters/theory/chiral_koszul_pairs.tex:4427:\subsection{Warm-up: Virasoro algebra}
chapters/theory/chiral_koszul_pairs.tex:5738:\subsection{Virasoro algebra: beyond the quadratic setting}
chapters/theory/chiral_modules.tex:3681:\subsection{Virasoro Verma modules under Koszul duality}
chapters/theory/nilpotent_completion.tex:355:\subsection{Example 1: Virasoro algebra}
chapters/theory/hochschild_cohomology.tex:94:\subsection{Virasoro Hochschild cohomology}
chapters/examples/bar_complex_tables.tex:246:\subsection{Virasoro bar complex through degree 3}
chapters/examples/bar_complex_tables.tex:2632:\section{Virasoro bar complex: degree 3}
chapters/examples/bar_complex_tables.tex:3683:\section{Virasoro bar complex through degree 5}
chapters/examples/w_algebras_deep.tex:3788:\subsection{Virasoro Gram matrix at weight~\texorpdfstring{$4$}{4} and the \texorpdfstring{$\mathcal{W}_4$}{W4} structure constant}
chapters/examples/free_fields.tex:4482:\section{Virasoro, strings, and moduli}\label{sec:virasoro-strings-moduli}
chapters/examples/free_fields.tex:4491:\subsection{Virasoro at critical central charge}
chapters/examples/free_fields.tex:4674:\subsection{String theory: Virasoro--BRST duality}
chapters/theory/ordered_associative_chiral_kd.tex:2913:\section{The Virasoro ordered bar complex and the gravitational Yangian}
Plan update
Auditing the live KM↔Vir seam using `chapters/examples/kac_moody.tex`, the Virasoro section inside `chapters/examples/w_algebras.tex`, and `chapters/examples/landscape_census.tex` as the canonical formula source.
  → Read seam-adjacent KM and Virasoro chapter regions for kappa, r-matrix, class, and central-charge claims
  • Cross-check each seam claim against the census and local transition language
  • Re-verify surviving inconsistencies and return exact file:line fixes only
codex
I’ve isolated the live Virasoro seam to `chapters/examples/w_algebras.tex`. Now I’m reading the exact ranges where KM hands off to Virasoro behavior and where the Virasoro section states the corresponding formulas.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1360,1575p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '717,780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1638,1778p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '5970,6012p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1360	Casimir eigenvalue
  1361	$\sum_{c,d} f^{ac}{}_d f^{bc}{}_d = 2h^\vee\,\delta^{ab}$
  1362	(cf.~\eqref{eq:d-squared-general}).
  1363	\end{definition}
  1364	
  1365	\begin{computation}[First-principles derivation of
  1366	$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$]
  1367	\label{comp:km-kappa-first-principles}
  1368	\index{modular characteristic!first-principles derivation}
  1369	\index{curvature!affine Kac--Moody!explicit residue}
  1370	
  1371	We derive the obstruction coefficient
  1372	$\kappa(\widehat{\fg}_k)$ by explicit residue computation
  1373	on the genus-$1$ bar complex, tracking the two OPE channels
  1374	separately.
  1375	
  1376	\emph{Step~1: Genus-$1$ bar differential.}
  1377	On the elliptic curve $E_\tau$, the degree-$1$ bar element
  1378	is $J^a(z_1) \boxtimes J^b(z_2) \cdot K^{(1)}_{12}$,
  1379	where $K^{(1)}(z|\tau) = \theta_1'(z|\tau)/\theta_1(z|\tau)$
 succeeded in 51ms:
   717	\index{r-matrix@$r$-matrix!Kac--Moody|textbf}
   718	\index{Kac--Moody algebra!collision-residue $r$-matrix}
   719	\index{CYBE!Kac--Moody}
   720	The bar complex propagator $d\log(z_1 - z_2)$ absorbs one pole
   721	order from the OPE (Proposition~\ref{prop:rmatrix-pole-landscape}).
   722	For the OPE
   723	$J^a(z)J^b(w) \sim k\,\kappa(a,b)/(z{-}w)^2 + f^{ab}{}_{c}J^c/(z{-}w)$,
   724	the collision residue extracts the zeroth product $a_{(0)}b = f^{ab}{}_{c}J^c$
   725	(the Lie bracket). The double-pole term
   726	$k\,\kappa(a,b)/(z{-}w)^2$ contributes the curvature~$m_0$, not the
   727	$r$-matrix (Computation~\ref{comp:sl2-collision-residue-kz},
   728	Step~2). Dualising the Lie-bracket residue via the
   729	level-shifted Killing form gives the Casimir $r$-matrix:
   730	\begin{equation}\label{eq:km-rmatrix}
   731	r^{\mathrm{KM}}_{\hat\fg_k}(z) = \frac{\Omega}{(k + h^\vee)\,z},
   732	\qquad
   733	\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b,
   734	\end{equation}
   735	which has a single simple pole, regardless of the rank of~$\fg$.
   736	The factor $(k + h^\vee)^{-1}$ reflects the level-shifted
 succeeded in 51ms:
     1	\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
     2	\label{chap:kac-moody}
     3	
     4	The Heisenberg algebra is abelian: its shadow tower terminates at
     5	degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
     6	The first nonabelian chiral algebra is
     7	$\widehat{\mathfrak{g}}_k$, and the question that
     8	governs this chapter is whether the Lie bracket destroys the
     9	finiteness of the obstruction tower or preserves it.
    10	%
    11	It preserves it. The Lie bracket of~$\fg$ appears as the
    12	cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
    13	degree~$3$; the Jacobi identity forces the quartic shadow to vanish;
    14	the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
    15	introduces noncommutativity but not infinite obstruction complexity:
    16	the structure constants of~$\fg$ produce exactly one new shadow
    17	beyond the Gaussian, and the Jacobi identity is the mechanism that
    18	kills the rest. This is the content of the assertion that gauge
    19	theory is simpler than gravity; for the Virasoro algebra
    20	(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
 succeeded in 52ms:
  1638	\toprule
  1639	$\fg$ & $\dim$ & $r$ & $h = h^\vee$ & $|\Delta_+|$
  1640	 & $\kappa(\widehat{\fg}_k)$ & $K$ & Class \\
  1641	\midrule
  1642	$E_6$ & $78$ & $6$ & $12$ & $36$
  1643	 & $13(k+12)/4$ & $156$ & L \\
  1644	$E_7$ & $133$ & $7$ & $18$ & $63$
  1645	 & $133(k+18)/36$ & $266$ & L \\
  1646	$E_8$ & $248$ & $8$ & $30$ & $120$
  1647	 & $62(k+30)/15$ & $496$ & L \\
  1648	\bottomrule
  1649	\end{tabular}
  1650	\end{center}
  1651	Here $K = c + c' = 2\dim\fg$ is the Koszul conductor.
  1652	Every entry satisfies $\kappa + \kappa' = 0$
  1653	(Proposition~\textup{\ref{prop:ff-channel-shear}}).
  1654	All three are class~L with shadow depth $r_{\max} = 3$:
  1655	the Jacobi identity kills the quartic obstruction
  1656	$S_4 = 0$ while the Lie bracket provides a nonzero
  1657	cubic shadow $\alpha \neq 0$
 succeeded in 52ms:
  5970	\end{remark}
  5971	
  5972	\begin{proposition}[Kappa anti-symmetry under Feigin--Frenkel involution]
  5973	\label{prop:kappa-anti-symmetry-ff}
  5974	\ClaimStatusProvedHere
  5975	\index{Feigin--Frenkel duality!kappa anti-symmetry}
  5976	\index{kappa@$\kappa$!Feigin--Frenkel anti-symmetry}
  5977	For any simple Lie algebra $\mathfrak{g}$ at non-critical level
  5978	$k \neq -h^\vee$:
  5979	\begin{equation}\label{eq:kappa-ff-antisymmetry}
  5980	 \kappa\bigl(\widehat{V}_k(\fg)\bigr)
  5981	 \;+\;
  5982	 \kappa\bigl(\widehat{V}_{-k-2h^\vee}(\fg)\bigr)
  5983	 \;=\; 0.
  5984	\end{equation}
  5985	The Verlinde level-rank swap
  5986	$\dim \mathcal{V}_1(\mathfrak{sl}_N, k)
  5987	= \dim \mathcal{V}_1(\mathfrak{sl}_k, N)$
  5988	holds at genus~$1$ if and only if $N = k$; for general $N \neq k$,
  5989	the swap requires $\mathfrak{gl}_N$ (including the

thinking
**Inspecting Virasoro ranges**

I'm considering how to inspect the relevant ranges for Virasoro. There are important aspects to look into, and I want to ensure I cover all necessary details effectively. Maybe I should focus on specific ranges and contexts where Virasoro applies. This feels like a crucial step, so let's make sure to gather accurate information! I'll dig into it further to clarify what I really need to look for here.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1234,1495p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5290,5375p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1543,1608p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2711,2765p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4720,4920p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3500,3668p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5290	Immediate from Theorems~\ref{thm:w-virasoro-quintic-forced}
  5291	and~\ref{thm:w-finite-termination}: the inductive mechanism
  5292	$\mathfrak{o}^{(r+1)} \ni
  5293	\{\mathfrak{C},\mathrm{Sh}_r\}_H \neq 0$
  5294	propagates non-vanishing to all degrees.
  5295	\end{proof}
  5296	
  5297	\subsection{Genus-$1$ Hessian correction for the Virasoro shadow}
  5298	\label{subsec:w-virasoro-genus1-hessian}
  5299	\index{genus loop operator!Virasoro computation}
  5300	\index{Hessian correction!genus-1 Virasoro}
  5301	
  5302	The infinite shadow obstruction tower carries information beyond the
  5303	$\hat{A}$-genus. The first concrete manifestation is the genus-$1$
  5304	Hessian correction obtained by applying the genus loop operator
  5305	$\Lambda_P$ (Definition~\ref{def:nms-genus-loop-operator}) to the
  5306	quartic shadow. We give the self-contained computation here;
  5307	the abstract framework is developed in
  5308	Appendix~\ref{sec:nms-genus-loop-operator}.
  5309	
 succeeded in 51ms:
  1234	\section{Explicit computation: Virasoro algebra}
  1235	
  1236	\subsection{Setup}
  1237	
  1238	The Virasoro algebra is the simplest W-algebra: $\mathcal{W}^k(\mathfrak{sl}_2, f_{\text{prin}})$ at central charge $c$.
  1239	
  1240	\begin{definition}[Virasoro algebra]
  1241	The Virasoro algebra has generators $L_n$ ($n \in \mathbb{Z}$) and central element $c$, with commutation relations:
  1242	\begin{equation}
  1243	[L_m, L_n] = (m-n) L_{m+n} + \frac{c}{12}(m^3 - m)\delta_{m+n,0}
  1244	\end{equation}
  1245	
  1246	As a vertex algebra, the generator is:
  1247	\begin{equation}
  1248	T(z) = \sum_{n \in \mathbb{Z}} L_n z^{-n-2}
  1249	\end{equation}
  1250	with OPE:
  1251	\begin{equation}
  1252	T(z)T(w) \sim \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w}
  1253	\end{equation}
 succeeded in 51ms:
  1543	\subsection{Genus-1 pipeline for the Virasoro algebra}
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
  1561	\subsubsection{Genus-1 bar complex}
  1562	
 succeeded in 51ms:
  2711	\index{Virasoro algebra!five-theorem verification}
  2712	The Virasoro algebra $\mathrm{Vir}_c = \mathcal{W}^k(\mathfrak{sl}_2)$
  2713	with $c = 1 - 6(k+1)^2/(k+2)$ verifies all five theorems:
  2714	
  2715	\begin{center}
  2716	\renewcommand{\arraystretch}{1.35}
  2717	\begin{tabular}{lp{10.0cm}}
  2718	\toprule
  2719	\textbf{Theorem} & \textbf{Virasoro specialization} \\
  2720	\midrule
  2721	\textbf{A} (Adjunction) &
  2722	 $\mathrm{Vir}_c^! \simeq \mathrm{Vir}_{26-c}$ via
  2723	 $k \mapsto -k - 4$ \textup{(}Theorem~\textup{\ref{thm:w-algebra-koszul-main}}\textup{)}.
  2724	 Involutive: $(26 - c)' = c$.
  2725	 Koszul self-dual at $c = 13$ (fixed point of $c \mapsto 26{-}c$);
  2726	 quadratic self-dual at $c = 0$
  2727	 \textup{(}Theorem~\textup{\ref{thm:virasoro-self-duality}}\textup{)}.
  2728	 \\
  2729	\textbf{B} (Inversion) &
  2730	 $\Omega(\bar{B}(\mathrm{Vir}_c)) \xrightarrow{\sim} \mathrm{Vir}_c$,
 succeeded in 50ms:
  3500	
  3501	
  3502	%% ================================================================
  3503	\section{Mixed cubic--quartic shadows: Virasoro and principal \texorpdfstring{$\mathcal{W}_N$}{WN}}
  3504	\label{sec:mixed-cubic-quartic-shadows}
  3505	\index{shadow calculus!mixed cubic--quartic}
  3506	\index{W-algebra@$\mathcal{W}$-algebra!mixed shadows}
  3507	
  3508	The three primitive archetypes (Gaussian (Heisenberg), Lie/tree
  3509	(affine $\widehat{\mathfrak{sl}}_2$), and contact/quartic ($\beta\gamma$))
  3510	do not exhaust the classification. Virasoro and principal
  3511	$\mathcal{W}_N$ are the first genuinely \emph{mixed} families: cubic
  3512	and quartic nonlinearities coexist inseparably already at the first
  3513	nontrivial level. This section computes their shadow calculus
  3514	explicitly. The theorems here are the $\mathcal{W}$-algebraic
  3515	counterparts of the abstract framework developed in
  3516	Appendix~\ref{sec:nms-mixed-families}; we include self-contained proofs
  3517	to keep the example chapters independently readable.
  3518	
  3519	On the arithmetic side
 succeeded in 53ms:
  4720	\emph{$\mathcal{W}_5$:} four channels $(T, W^{(3)}, W^{(4)}, W^{(5)})$ with kappa matrix $\operatorname{diag}(c/2, c/3, c/4, c/5)$ and total $\kappa = 77c/60$. Two parity lines ($W^{(3)}$ and $W^{(5)}$, both odd weight) have $\alpha = 0$; two non-parity lines ($T$ and $W^{(4)}$, both even weight) have $\alpha \neq 0$.
  4721	
  4722	\emph{$\mathbb{Z}_2$ parity rule:} for a generator $W^{(s)}$ of conformal weight $s$, the cubic shadow on the corresponding primary line vanishes if and only if $s$ is odd. This is the shadow-tower manifestation of the bosonic parity constraint: the OPE $W^{(s)}(z) W^{(s)}(w)$ has only even-order poles when $s$ is odd ($W^{(s)}$ is fermionic in the bar complex sense), so the extracted cubic $\alpha = W^{(s)}_{(2s-2)} W^{(s)} = 0$ vanishes. All data verified by \texttt{test\_higher\_w\_shadows.py} (112~tests); detailed shadow tables in \S\ref{sec:higher-w-shadow-data}.
  4723	\end{remark}
  4724	
  4725	\subsection{Tower construction for Virasoro}
  4726	\label{subsec:virasoro-tower-construction}
  4727	\index{shadow obstruction tower!Virasoro construction}
  4728	
  4729	We instantiate the tower construction template
  4730	(Construction~\ref{constr:tower-template}) for the Virasoro
  4731	algebra at generic central charge~$c$.
  4732	
  4733	\paragraph{Step~1: Degree~$2$.}
  4734	$\kappa(\mathrm{Vir}_c) = c/2$.
  4735	$\Theta_{\mathrm{Vir}}^{\leq 2} = (c/2)\,x^2$.
  4736	
  4737	\paragraph{Step~2: Degree~$3$, gravitational cubic.}
  4738	The simple-pole self-OPE $T_{(1)}T = 2T$ produces
  4739	$\ell_2^{\mathrm{tr}} \neq 0$, giving the gravitational cubic
exec
/bin/zsh -lc "rg -n '\\\\kappa\\(V_k|\\\\kappa\\(Vir|r\\"'^KM|r'"\\"'^Vir|Kac--Moody|Virasoro|class~L|class~M|central charge|26-c|c/2|Omega/'"\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z\\)|k\\\\Omega' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5:The complementarity sum $c + c' = 2d$ holds for every Kac--Moody
9:$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
21:$S_4 = 0$ singles out affine Kac--Moody (class~L), and $\Delta \neq 0$
22:forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
23:(class~M). The classification is not imposed but forced by the
33:and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
45:same-family partner datum, the central charge~$c(\cA)$, the
79: & $c/2$ & PH \\
87:\multicolumn{6}{|c|}{\textit{Affine Kac--Moody
119:\multicolumn{6}{|c|}{\textit{Affine Kac--Moody \textup{(}non-simply-laced, $h \neq h^\vee$\textup{)}}} \\
141: & $\mathrm{Vir}_{26-c}$\textsuperscript{$\ddagger$}
142: & $1 - \dfrac{6(k{+}1)^2}{k{+}2}$ & $26$ & $c/2$ & PH \\[4pt]
234: k\Omega_{\mathrm{tr}}/z\bigr), &
241: \mathrm{Vir}_{26-c},\;
320:$\mathrm{BP}_k = \mathcal{W}_3^{(2)}(k)$ (Bershadsky--Polyakov) & M & $\infty$ & mixed: $T$-line class~M ($r_{\max}^T = \infty$); $J$-line class~G ($r_{\max}^J = 2$) & Prop~\ref{prop:bp-tline-depth} \\
364:boundary at $m = 3$: $K_1$ is finite type ($A_2$, class~L),
365:$K_2$ is tame (affine $\widehat{A}_1$, class~M), and $K_m$ for
447:\multicolumn{6}{|c|}{\textit{Class L (Lie/tree): collision residue $r^{\mathrm{coll}}(z) = k\Omega_{\mathrm{tr}}/z = \Omega/(k{+}h^\vee)\,z$}} \\
451: & $k\Omega^{aa}/z$
463: & $(c/2)/z^3 + 2T/z$
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '40,180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '360,460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '200,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    40	\label{sec:master-table}
    41	\index{master table of invariants|textbf}
    42	
    43	Table~\ref{tab:master-invariants} records, for each Koszul chiral
    44	algebra~$\cA$ computed in this monograph, the Koszul dual or
    45	same-family partner datum, the central charge~$c(\cA)$, the
    46	level-independent sum $c(\cA) + c(\cA^!)$ under Koszul duality
    47	(Theorem~\ref{thm:central-charge-complementarity}), and the
    48	obstruction coefficient $\kappa(\cA)$ from the genus universality
    49	theorem $\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
    50	(Theorem~\ref{thm:genus-universality};
    51	; multi-weight requires $\delta F_g^{\mathrm{cross}}$,
    52	cf.~Theorem~\ref{thm:multi-weight-genus-expansion}).
    53	Throughout, $d = \dim\fg$, $r = \operatorname{rank}\fg$,
    54	$h^\vee$ is the dual Coxeter number, and $t = k + h^\vee$.
    55	
    56	\begin{table}[ht]
    57	\centering
    58	\caption{Computed invariants for Koszul chiral algebras}
    59	\label{tab:master-invariants}
 succeeded in 51ms:
   360	The shadow depth classification G/L/C/M applies to chirally Koszul
   361	algebras: those whose bar spectral sequence collapses at~$E_2$
   362	(Theorem~\ref{thm:koszul-equivalences-meta}). The Kronecker quiver
   363	$K_m$ (two vertices, $m$ parallel arrows) exhibits a sharp Koszul
   364	boundary at $m = 3$: $K_1$ is finite type ($A_2$, class~L),
   365	$K_2$ is tame (affine $\widehat{A}_1$, class~M), and $K_m$ for
   366	$m \geq 3$ is wild. In the wild regime, the symmetric Euler form
   367	has $\det = 4 - m^2 < 0$ (indefinite), the bar spectral sequence
   368	does not collapse at any finite page, and the signed Euler series
   369	$\prod_{n \geq 1}(1 - t^n)^{m+2}$ acquires negative coefficients
   370	starting at weight~$2$.
   371	
   372	These failures obstruct the construction of a shadow obstruction
   373	tower in the sense of Definition~\ref{def:shadow-depth-classification}:
   374	the MC element $\Theta_\cA$ does not exist in the formal deformation
   375	complex because the bar cohomology lacks concentration. The role of
   376	the shadow tower is taken by the Donaldson--Thomas invariants
   377	$\Omega(d_0, d_1)$ of the Kronecker quiver
   378	(Kontsevich--Soibelman~\cite{KS10}, Reineke~\cite{Re03}),
   379	which grow exponentially in $\max(d_0, d_1)$ for $m \geq 3$,
 succeeded in 51ms:
   200	$\operatorname{ek} = N{-}1$ for $\cW_N$.
   201	This is independent of shadow depth~$\kappa_d$
   202	(Theorem~\ref{thm:shadow-euler-independence}).
   203	\end{remark}
   204	
   205	\medskip
   206	
   207	\noindent\textbf{The shadow obstruction tower as organizing frame.}
   208	Every entry in Table~\ref{tab:master-invariants} is a projection of the
   209	universal MC element $\Theta_\cA \in \MC(\gAmod)$
   210	(Theorem~\ref{thm:mc2-bar-intrinsic}). The scalar $\kappa(\cA)$ is
   211	the degree-$2$ projection; the complementarity sum $c + c'$ is the
   212	ambient shadow at genus~$0$; the Koszul dual is obtained via
   213	Verdier duality on the bar coalgebra.
   214	The seed datum for each family is its modular Koszul triple
   215	$\mathfrak{T} = (\cA, \cA^!, r(z))$
   216	(Definition~\ref{def:modular-koszul-triple}):
   217	\begin{equation}\label{eq:census-triples}
   218	\begin{aligned}
   219	\mathfrak{T}_{\cH}
codex
The census confirms the canonical seam formulas: KM is class `L` with trace-form `kΩ_tr/z` equivalent to KZ `Ω/((k+h^\vee)z)`, and Virasoro is class `M` with `r(z)=(c/2)/z^3+2T/z` and `\kappa=c/2`. I’m now checking whether the chapter surfaces preserve those conventions consistently or silently switch objects.
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '630,745p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'c\\(k\\)|c \\+ c\\'|26-c|kappa\\(\\mathrm\\{Vir\\}_c\\)|class~M|class~L|r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}|r\\"'^'"\\{\\\\mathrm\\{KM\\}\\}|Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z\\)|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|c/2|5c\\+22|\\(UNIFORM-WEIGHT\\)|ALL-WEIGHT' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '460,485p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'For the Virasoro algebra|Virasoro.*Kac--Moody|Kac--Moody.*Virasoro|Unlike the Kac--Moody|critical level|Sugawara|DS reduction|class~L|class~M' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   630	\hline
   631	$\widehat{E}_7$ & $\tfrac{2527}{36}$ & $\tfrac{2527}{864}$ & $\tfrac{17689}{207360}$ & scalar \\
   632	\hline
   633	$\widehat{E}_8$ & $\tfrac{1922}{15}$ & $\tfrac{961}{180}$ & $\tfrac{6727}{43200}$ & scalar \\
   634	\hline
   635	\multicolumn{5}{|c|}{\textit{$\mathcal{W}$-Algebras}} \\
   636	\hline
   637	$\mathrm{Vir}_{c}$ & $c/2$ & $c/48$ & $7c/11520$ & scalar \\
   638	\hline
   639	$\mathcal{W}_{3,c}$ & $5c/6$ & $5c/144$ & $7c/6912$ & multi \\
   640	\hline
   641	\multicolumn{5}{|c|}{\textit{Lattice VOAs}} \\
   642	\hline
   643	$V_{D_4}$ & $4$ & $\tfrac{1}{6}$ & $\tfrac{7}{1440}$ & scalar \\
   644	\hline
   645	$V_{E_8}$ & $8$ & $\tfrac{1}{3}$ & $\tfrac{7}{720}$ & scalar \\
   646	\hline
   647	Leech $V_{\Lambda_{24}}$ & $24$ & $1$ & $\tfrac{7}{240}$ & scalar \\
   648	\hline
   649	\multicolumn{5}{|c|}{\textit{Exceptional}} \\
 succeeded in 51ms:
   460	\hline
   461	$\mathrm{Vir}_c$ ($TT$)
   462	 & $2$ & $\{4,2,1\}$ & $\{3,1\}$
   463	 & $(c/2)/z^3 + 2T/z$
   464	 & odd \\
   465	\hline
   466	$\cW_3$ ($TT$)
   467	 & $2$ & $\{4,2,1\}$ & $\{3,1\}$
   468	 & $(c/2)/z^3 + 2T/z$
   469	 & odd \\
   470	\hline
   471	$\cW_3$ ($TW$)
   472	 & $2,3$ & $\{2,1\}$ & $\{1\}$
   473	 & $3W/z$
   474	 & --- \\
   475	\hline
   476	$\cW_3$ ($WW$)
   477	 & $3$ & $\{6,4,3,2,1\}$ & $\{5,3,2,1\}$
   478	 & $(c/3)/z^5 + 2T/z^3 + \partial T/z^2 + \cdots$
   479	 & mixed \\
 exited 1 in 53ms:
zsh:1: unmatched '
 succeeded in 55ms:
chapters/examples/w_algebras.tex:105:DS reduction sends the Koszul pair
chapters/examples/w_algebras.tex:111:Principal DS reduction acts functorially on
chapters/examples/w_algebras.tex:285:(i)~DS reduction of the WZW model (geometric/physical);
chapters/examples/w_algebras.tex:311:\textup{[Regime: filtered-complete \textup{(}DS reduction from curved-central KM;
chapters/examples/w_algebras.tex:328:the critical level: if $k=-h^\vee$, then $k'=-k-2h^\vee=-h^\vee$.
chapters/examples/w_algebras.tex:504:The DS reduction $\mathcal{W}^k(\fg, e)$ for a general nilpotent
chapters/examples/w_algebras.tex:541:asserts that Koszul duality intertwines DS reduction with BV orbit duality.
chapters/examples/w_algebras.tex:575:% incomplete KRW formula that drops Sugawara terms; the correct
chapters/examples/w_algebras.tex:633:\begin{definition}[Classical DS reduction]\label{def:classical-ds}
chapters/examples/w_algebras.tex:656:The classical DS reduction is a \emph{Hamiltonian reduction}, and its
chapters/examples/w_algebras.tex:659:theorem in this chapter. Every algebraic statement about DS reduction
chapters/examples/w_algebras.tex:760:\begin{theorem}[Arakawa's geometric localization for DS reduction;
chapters/examples/w_algebras.tex:766:Let $M$ be a module in $\cO_k(\widehat{\fg})$ at non-critical level
chapters/examples/w_algebras.tex:767:$k \neq -h^\vee$ such that the DS reduction
chapters/examples/w_algebras.tex:779:\begin{remark}[DS reduction as geometric localization:
chapters/examples/w_algebras.tex:786:\emph{DS reduction is localization from $\fg^*$ to the Slodowy slice}.
chapters/examples/w_algebras.tex:793:This is the \emph{geometric localization principle} for DS reduction.
chapters/examples/w_algebras.tex:830:This is the \emph{Chriss--Ginzburg principle for DS reduction}:
chapters/examples/w_algebras.tex:855:\subsection{Quantum DS reduction via BRST}
chapters/examples/w_algebras.tex:857:\begin{definition}[Quantum DS reduction]\label{def:quantum-ds}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1588,1665p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1588	\begin{proof}
  1589	The $B$-cycle quasi-periodicity~\eqref{eq:B-cycle-quasi-periodicity}
  1590	shifts the propagator by $-2\pi i$. Applying $d^{(1)}$ twice to a
  1591	degree-2 element $T \otimes T \otimes \eta_{12}$, the self-contraction
  1592	loop involves:
  1593	
  1594	\emph{Step~1: OPE contraction.}
  1595	The Virasoro OPE has a quartic pole $T_{(3)}T = c/2$ and a double pole
  1596	$T_{(1)}T = 2T$. When the propagator completes a $B$-cycle, the
  1597	shift $-2\pi i$ interacts with the quartic pole to produce:
  1598	\begin{equation}
  1599	(d^{(1)})^2(T \otimes T \otimes K^{(1)}_{12})
  1600	= (-2\pi i) \cdot T_{(3)}T = (-2\pi i) \cdot \frac{c}{2}
  1601	\end{equation}
  1602	This is the direct analog of the Kac--Moody computation
  1603	(Theorem~\ref{thm:sl2-genus1-curvature}), with $T_{(3)}T = c/2$ playing
  1604	the role of the level + Casimir contribution $k + h^\vee$.
  1605	
  1606	\emph{Step~2: Identification with $\omega_1$.}
  1607	The $B$-cycle monodromy defect $(-2\pi i)$ determines a cohomology

thinking
**Examining potential issues**

I’m noticing a potential issue with line 1620, where it says the bar complex is uncurved at genus 1, which is odd since it’s uncurved at genus 0. Maybe there’s a misuse happening with the bar complex at genus 0 that I need to clarify. I should take a closer look at the search results for KM in w_algebras. It might be useful to check around lines 4390-4420 for clarification on classification shifts.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4384,4424p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4384	o^{(5)}(\mathcal{W}_3) \neq 0
  4385	\quad\text{in}\quad
  4386	H^2(F^5\gAmod/F^6\gAmod,\,d_2).
  4387	\end{equation}
  4388	In particular, the $\mathcal{W}_3$ shadow obstruction tower does not terminate at
  4389	degree~$4$, confirming that $\mathcal{W}_3$ belongs to shadow archetype
  4390	class~M \textup{(}$r_{\max} = \infty$\textup{)}.
  4391	\end{theorem}
  4392	
  4393	\begin{proof}
  4394	The $\mathcal{W}_3$ quintic obstruction is computed in
  4395	\S\ref{subsec:w-w3-quintic-obstruction} below: the quintic
  4396	contact terms arising from the weight-$5$ sector of the $T$--$W$
  4397	OPE are nonvanishing for generic~$c$. Since $o^{(5)}$ is polynomial
  4398	in the OPE structure constants (by the bar-intrinsic construction,
  4399	Theorem~\ref{thm:mc2-bar-intrinsic}), its generic nonvanishing
  4400	implies nonvanishing for all but finitely many values of~$c$.
  4401	\end{proof}
  4402	
  4403	\begin{remark}[$W$-line alternating vanishing and DS shadow depth increase]
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
     1	\chapter{W-algebra Koszul duals}\label{chap:w-algebra-koszul}
     2	\label{chap:w-algebras}
     3	
     4	The Virasoro algebra has infinite shadow depth. Every truncation
     5	$\Theta_{\mathrm{Vir}}^{\leq r}$ fails to close: the quintic
     6	obstruction $o^{(5)}_{\mathrm{Vir}} \neq 0$ propagates to every
     7	higher degree, and no finite projection of the MC element suffices to
     8	recover $D\Theta + \tfrac12[\Theta,\Theta] = 0$. What controls the
     9	tower?
    10	
    11	The $\mathcal{W}_N$ hierarchy answers by stratification. Each
    12	$\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
    13	arises from affine Kac--Moody algebras by Drinfeld--Sokolov reduction
    14	along the principal nilpotent, with OPEs involving composite fields
    15	and poles up to order~$2N$. The Virasoro algebra is the $N=2$ case;
    16	$\mathcal{W}_3$ adds a weight-$3$ primary; $\mathcal{W}_N$ at higher
    17	rank amplifies every feature. None of these is Koszul in any
    18	finite-depth sense: the depth classification
    19	(Theorem~\ref{thm:shadow-archetype-classification}) forces every
    20	principal $\mathcal{W}_N$ into class~$\mathsf{M}$, with
codex
I’m checking the `\widehat{\mathfrak{sl}}_2 \to \mathrm{Vir}` handoff next. That is the highest-risk place for a seam bug because the affine Sugawara central charge and the DS-reduced Virasoro central charge are different functions of the same level.
exec
/bin/zsh -lc "rg -n 'Sugawara central charge|DS reduction.*central charge|central charge.*Sugawara|c\\(k\\)|1 - 6\\(k\\+1\\)\\"'^2/'"\\(k\\+2\\)|k\\\\dim|k\\+h\\"'^'"\\\\vee' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '392,430p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '980,1025p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   980	\begin{equation}\label{eq:gko-coset}
   981	\mathrm{Com}\bigl(\widehat{\mathfrak{sl}}_{2,k+1},\;
   982	V_k(\mathfrak{sl}_2) \otimes V_1(\mathfrak{sl}_2)\bigr)
   983	\;\cong\; \mathrm{Vir}_{c(k)}
   984	\end{equation}
   985	where $c(k) = 1 - 6(k+1)^2/(k+2)$ is the Virasoro algebra at
   986	central charge equal to the DS reduction
   987	\textup{(}Goddard--Kent--Olive~\cite{GKO85}\textup{)}.
   988	\end{theorem}
   989	
   990	\begin{remark}[DS reduction as coset]\label{rem:ds-coset}
   991	\index{Drinfeld--Sokolov reduction!coset interpretation}
   992	Arakawa~\cite{Arakawa17} established:
   993	\begin{equation}\label{eq:ds-coset}
   994	\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})
   995	\;\cong\; H^0_{\mathrm{DS}}(V_k(\mathfrak{g}))
   996	\;\cong\; \mathrm{Com}(V',\, V_k(\mathfrak{g}) \otimes
   997	\mathcal{F})
   998	\end{equation}
   999	where $V' \hookrightarrow V_k(\mathfrak{g}) \otimes \mathcal{F}$ is the vertex algebra Whittaker reduction. In the bar-cobar framework, the bar complex of the ambient algebra restricts to the commutant, and the bar differential descends to the DS differential on the coset.
 succeeded in 53ms:
   392	Since $-\alpha_i$ are the screening momenta for level
   393	$k' = -k-2h^\vee$ by Feigin--Frenkel duality, the level shift arises
   394	from the BRST mechanism, not from the Heisenberg factor alone.
   395	
   396	\emph{Step~4: Curved $A_\infty$ identification.}
   397	For $k \neq -h^\vee$, the W-algebra has non-trivial curvature $m_0 \neq 0$ (Theorem~\ref{thm:w-bar-curvature}). The bar-cobar adjunction of Theorem~\ref{thm:e1-chiral-koszul-duality} gives a curved $A_\infty$ quasi-isomorphism:
   398	\[
   399	\Omega^{\mathrm{ch}}(\bar{B}(\mathcal{W}^k(\mathfrak{g}))) \xrightarrow{\;\sim\;} \mathcal{W}^{-k-2h^\vee}(\mathfrak{g})
   400	\]
   401	The curvature of the dual is $m_0' = (k' + h^\vee) \cdot C_2 = -(k + h^\vee) \cdot C_2 = -m_0$, where $C_2$ is the quadratic Casimir element. In particular, $m_0 = 0$ if and only if $m_0' = 0$, as expected.
   402	
   403	\emph{Step~5: Consistency checks.}
   404	\emph{(i) Involutivity.} $k'' = -(k') - 2h^\vee = -(-k-2h^\vee) - 2h^\vee = k$. \checkmark
   405	
   406	\emph{(ii) Critical level.} At $k = -h^\vee$: $k' = -(-h^\vee) - 2h^\vee = -h^\vee$. Both sides have vanishing curvature ($m_0 = 0$), and the involution fixes the level. The relevant critical consistency check is therefore the affine Feigin--Frenkel center
   407	$Z(\widehat{\mathfrak{g}}_{-h^\vee}) \cong \mathrm{Fun}(\mathrm{Op}_{\mathfrak{g}^\vee})$
   408	(Theorem~\ref{thm:ff-center}), not a separate manuscript-internal theorem that principal $\mathcal{W}$-centers are globally exchanged. \checkmark
   409	
   410	\emph{(iii) $\mathfrak{sl}_2$ reduction.} For $\mathfrak{g} = \mathfrak{sl}_2$ with $h^\vee = 2$: $\mathcal{W}^k(\mathfrak{sl}_2) = \mathrm{Vir}_{c(k)}$ with $c(k) = 1 - 6(k+1)^2/(k+2)$. The dual level $k' = -k-4$ gives $c(k') = 1 - 6(-k-3)^2/(-k-2) = 1 + 6(k+3)^2/(k+2)$. Then $c(k) + c(k') = 2 + 6[-(k+1)^2 + (k+3)^2]/(k+2) = 2 + 6 \cdot 4(k+2)/(k+2) = 2 + 24 = 26$. The Virasoro algebra at $c = 0$ is \emph{quadratic} self-dual ($\mathrm{Vir}_0^{!_{\mathrm{quad}}} \simeq \mathrm{Vir}_0$, Theorem~\ref{thm:virasoro-self-duality}); this is a property of the uncurved OPE at $c=0$, not of the FF level-shifting involution (which sends $c=0$ to $c=26$). \checkmark
   411	
 succeeded in 56ms:
chapters/examples/kac_moody.tex:159:$q = e^{\pi i/(k+h^\vee)}$
chapters/examples/kac_moody.tex:171:$\kappa = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$, while
chapters/examples/kac_moody.tex:423:T = \frac{1}{2(k+h^\vee)} \sum_a {:}J^a J^a{:}
chapters/examples/kac_moody.tex:430:The \emph{level} $k$ determines the central charge of the Virasoro algebra via the Sugawara construction:\index{Sugawara construction}
chapters/examples/kac_moody.tex:511:This is proved as Theorem~\ref{thm:universal-kac-moody-koszul} below: the bar complex of $\widehat{\mathfrak{g}}_k$ is computed via residues on FM compactifications (Step~1), the curvature $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is identified from the double-pole OPE (Step~2), the cobar OPE recovers the level $-k - 2h^\vee$ structure constants (Step~3), and the result is characterized by functorial uniqueness (Step~4).
chapters/examples/kac_moody.tex:521:m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a] = m_2(m_0, a) - m_2(a, m_0)
chapters/examples/kac_moody.tex:690:The simple pole comes from $\beta(z)$ contracting with $\gamma(w)^2$; the double pole from $\beta(z)\cdot(-2\partial\gamma(w)) = -2/(z-w)^2 = k/(z-w)^2$. At critical level $k = -h^\vee$, the Sugawara construction\index{Sugawara construction!undefined at critical level} $T = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a J^a{:}$ is \emph{undefined} (division by zero), not merely zero.
chapters/examples/kac_moody.tex:711:\item \emph{Central charge non-cancellation.} Unlike the $\beta\gamma$/$bc$ pair (Proposition~\ref{prop:betagamma-bc-koszul-detailed}), the central charges satisfy $c(k) + c(-k-4) = 2\dim(\mathfrak{sl}_2) = 6$ rather than zero: curvature prevents cancellation.
chapters/examples/kac_moody.tex:750:r^{\mathrm{KZ}}(z) = \frac{\Omega}{(k+h^\vee)\,z},
chapters/examples/kac_moody.tex:769:identification $k\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$.
chapters/examples/kac_moody.tex:966:The decomposition~\eqref{eq:bar-level-decomp} reflects the level-independence of bar chain groups (Lemma~\ref{lem:bar-dims-level-independent}): $d_{\mathrm{crit}}$ encodes $\mathfrak{g}$-structure constants, $\delta$ encodes the central extension, and $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is the degree-$0$ component of $(k + h^\vee)\delta$.
chapters/examples/kac_moody.tex:1278:($L_{\mathrm{Sug}} = \tfrac{1}{2(k+h^\vee)} \sum_a J^a J^a$,
chapters/examples/kac_moody.tex:1366:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$]
chapters/examples/kac_moody.tex:1553:The Sugawara central charge is
chapters/examples/kac_moody.tex:1554:$c = k\dim(\fg)/(k+h^\vee)$.
chapters/examples/kac_moody.tex:1556:$(k+h^\vee)^2 = kh^\vee$, i.e.,
chapters/examples/kac_moody.tex:1712:the central charge $c = k\dim\fg/(k + h^\vee)
chapters/examples/kac_moody.tex:1768:$r(z) = \Omega_\fg / ((k+h^\vee)z)$ (a single simple
chapters/examples/kac_moody.tex:1955:The curvature $m_0 = \frac{k+h^\vee}{2h^\vee}\kappa$ (identified in the proof of Theorem~\ref{thm:universal-kac-moody-koszul}) satisfies $m_1^2(a) = m_2(m_0, a) - m_2(a, m_0) = [m_0, a]$ for all $a \in \widehat{\mathfrak{g}}_k$, which is the curved $A_\infty$ relation replacing strict nilpotence $\dzero^2 = 0$.
chapters/examples/kac_moody.tex:1969:Z(\widehat{\mathfrak{g}}_k) = \sum_{g=0}^\infty \frac{1}{(k+h^\vee)^{2g-2}} Z_g

thinking
**Analyzing curvature properties**

I’m delving into the W-algebra curvature, which is proportional to k+2 and vanishes at k=-2. However, the Virasoro subalgebra curvature, represented as c/2, doesn’t vanish at that point, and c remains undefined. I’ve noted the distinction between these vanishings before. There seems to be a gap, specifically regarding the Virasoro section not mentioning that c=0 isn't the DS-critical point. I need to check for any internal inconsistencies related to central charge formulas and their alignment with conventions and user expectations.
exec
/bin/zsh -lc "rg -n '\\\\kappa\\(.*Vir|\\\\kappa\\(.*fg|c\\(k\\) = 1 - 6\\(k\\+1\\)\\"'^2/'"\\(k\\+2\\)|kappa\\s*=\\s*c/2|c \\+ c\\'|r\\(z\\) = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z\\)|r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}_c\\(z\\)|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'class~\\\\?\\"'$?L|class~'"\\\\?\\"'$?M|archetype|r_'"\\{\\\\max\\}|shadow depth' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: unmatched '
 succeeded in 51ms:
chapters/examples/kac_moody.tex:14:the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
chapters/examples/kac_moody.tex:77:\caption{Shadow archetype data for affine
chapters/examples/kac_moody.tex:78:Kac--Moody.}\label{tab:km-shadow-archetype}
chapters/examples/kac_moody.tex:84:Shadow depth $r_{\max}$ & $3$ \\
chapters/examples/kac_moody.tex:127:Affine Kac--Moody algebras occupy the Lie/tree archetype
chapters/examples/kac_moody.tex:128:($r_{\max} = 3$), between the Gaussian families
chapters/examples/kac_moody.tex:129:(Heisenberg, lattice, free fermion; $r_{\max} = 2$) and
chapters/examples/kac_moody.tex:130:the contact/quartic archetype of $\beta\gamma$
chapters/examples/kac_moody.tex:131:($r_{\max} = 4$). At generic level $k \neq -h^\vee$, the
chapters/examples/kac_moody.tex:143:corrections vanish at every genus, making Kac--Moody the archetype of
chapters/examples/kac_moody.tex:190:This is the Lie/tree secondary Borcherds archetype:
chapters/examples/kac_moody.tex:210:\index{genus-two shells!Lie/tree archetype}
chapters/examples/kac_moody.tex:213:the Lie/tree archetype sees two of the three shells:
chapters/examples/kac_moody.tex:262:Theorem~\ref{thm:km-strictification}: the archetype of
chapters/examples/kac_moody.tex:266:archetype, terminates at $r = 3$.
chapters/examples/kac_moody.tex:1622:\index{shadow archetype!exceptional types}
chapters/examples/kac_moody.tex:1654:All three are class~L with shadow depth $r_{\max} = 3$:
chapters/examples/kac_moody.tex:1658:(Theorem~\textup{\ref{thm:shadow-archetype-classification}}).
chapters/examples/kac_moody.tex:1666:The shadow class~L assignment follows from the general
chapters/examples/kac_moody.tex:1748:$1/(m_i + 1)$ contributions. Since all three are class~L
exec
/bin/zsh -lc "rg -n 'c/2|kappa = c/2|\\\\kappa\\s*=\\s*c/2|\\\\kappa\\(.*\\) = c/2|c\\(k\\) \\+ c\\(-k-4\\)|26-c|class~M|class~L|r\\(z\\)' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:90:$r$-matrix $r(z)$ & $\Omega/\bigl((k{+}h^\vee)\,z\bigr)$ (Casimir, KZ normalisation, Comp.~\ref{comp:sl2-collision-residue-kz}) \\
chapters/examples/kac_moody.tex:112:r(z) = \frac{\Omega}{(k{+}h^\vee)\,z}\,\Bigr),
chapters/examples/kac_moody.tex:711:\item \emph{Central charge non-cancellation.} Unlike the $\beta\gamma$/$bc$ pair (Proposition~\ref{prop:betagamma-bc-koszul-detailed}), the central charges satisfy $c(k) + c(-k-4) = 2\dim(\mathfrak{sl}_2) = 6$ rather than zero: curvature prevents cancellation.
chapters/examples/kac_moody.tex:740:The $r$-matrix $r(z) = \Omega/((k{+}h^\vee)\,z)$ satisfies the classical
chapters/examples/kac_moody.tex:770:%: r(z) lives on C_2(X), not over a point. The formal disk
chapters/examples/kac_moody.tex:1555:Setting $\kappa = c/2$ leads to
chapters/examples/kac_moody.tex:1560:$\kappa \neq c/2$ for all real~$k$.
chapters/examples/kac_moody.tex:1565:while $c/2$ is the modular characteristic
chapters/examples/kac_moody.tex:1654:All three are class~L with shadow depth $r_{\max} = 3$:
chapters/examples/kac_moody.tex:1666:The shadow class~L assignment follows from the general
chapters/examples/kac_moody.tex:1748:$1/(m_i + 1)$ contributions. Since all three are class~L
chapters/examples/kac_moody.tex:1768:$r(z) = \Omega_\fg / ((k+h^\vee)z)$ (a single simple
chapters/examples/kac_moody.tex:2071:$\mathcal{H}(T) = (\cA, \cA^!, C, r(z), \Theta_\cA,
chapters/examples/kac_moody.tex:2076:$r(z) = \Omega/((k{+}h^\vee)\,z)$ (the Casimir $r$-matrix, governing the KZ equation),
chapters/examples/kac_moody.tex:2094:yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
chapters/examples/kac_moody.tex:2315:(The KZ connection is the genus-$0$ shadow connection $\nabla^{\mathrm{hol}}_{0,n}$ of Theorem~\ref{thm:gz26-commuting-differentials}(iii); the classical-quantum bridge is Theorem~\ref{thm:kz-classical-quantum-bridge}.)
chapters/examples/kac_moody.tex:2328:r(z) = \frac{\Omega}{(k+2)\,z}
chapters/examples/kac_moody.tex:2351: $r(z) \in \mathfrak{sl}_2^{\otimes 2}[z^{-1}]$.
chapters/examples/kac_moody.tex:2357:$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no
chapters/examples/kac_moody.tex:3416:$r(z) = \Omega/\bigl((k{+}h^\vee)\,z\bigr)$ is well-defined and the
codex
The first nontrivial seam bug I’m testing now is notation drift inside `kac_moody.tex`: several `r(z)` displays appear as `\Omega/(k+2)\,z`, which is ambiguous and no longer visibly the same convention as the KZ form used elsewhere. I’m re-reading those local lines before I count them as findings.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2320,2362p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2068,2100p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2320	The entire chain is:
  2321	\[
  2322	\Theta_\cA
  2323	\;\xrightarrow{\text{restrict to }(g,n) = (0,2)}
  2324	\;\Theta_{0,2}
  2325	\;\xrightarrow{\operatorname{Res}^{\mathrm{coll}}}\;
  2326	f^{ab}{}_c\, J^c
  2327	\;\xrightarrow{\text{dualise}}\;
  2328	r(z) = \frac{\Omega}{(k+2)\,z}
  2329	\;\xrightarrow{\text{all }n}\;
  2330	\nabla^{\mathrm{KZ}}.
  2331	\]
  2332	\end{computation}
  2333	
  2334	\begin{remark}[Collision residue as Chriss--Ginzburg projection]
  2335	\label{rem:sl2-collision-chriss-ginzburg}
  2336	\index{Chriss--Ginzburg principle!collision residue}
  2337	The computation above exhibits the deepest instance of the
  2338	Chriss--Ginzburg principle
  2339	(\S\ref{subsec:chriss-ginzburg-derivation}):
 succeeded in 51ms:
  2068	\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
  2069	
  2070	In the holographic modular Koszul datum
  2071	$\mathcal{H}(T) = (\cA, \cA^!, C, r(z), \Theta_\cA,
  2072	\nabla^{\mathrm{hol}})$,
  2073	the Kac--Moody specialisation is:
  2074	$\cA = \widehat{\mathfrak{g}}_k$,
  2075	$\cA^! = \widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Feigin--Frenkel),
  2076	$r(z) = \Omega/((k{+}h^\vee)\,z)$ (the Casimir $r$-matrix, governing the KZ equation),
  2077	$\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$,
  2078	$\Theta_{\widehat{\mathfrak{g}}_k}^{\min}
  2079	= \kappa \cdot \eta \otimes \Lambda$
  2080	\textup{(}minimal scalar package for uniform-weight algebras\textup{)},
  2081	while the full universal class is Lie/tree with
  2082	$\mathfrak{C} \ne 0$, $o_4 = 0$.
  2083	\end{remark}
  2084	
  2085	\begin{computation}[Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$; \ClaimStatusProvedHere]
  2086	\label{comp:sl2-collision-residue-kz}
  2087	\index{collision residue!sl2 explicit@$\mathfrak{sl}_2$ explicit}
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '3408,3422p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3408	non-degenerate admissible level for $\widehat{\fg}$ with
  3409	$\gcd(p,q) = 1$ and $q \geq 3$. Then
  3410	\begin{equation}\label{eq:admissible-rank-h2}
  3411	\dim H^2\!\bigl(\barB(L_k(\fg))\bigr) \;=\; \mathrm{rk}(\fg).
  3412	\end{equation}
  3413	In particular the bar cohomology $H^2$ jumps from its generic value
  3414	\textup{(}attained on the open dense locus of non-admissible levels;
  3415	$k + h^\vee = p/q \neq 0$, so the affine $r$-matrix
  3416	$r(z) = \Omega/\bigl((k{+}h^\vee)\,z\bigr)$ is well-defined and the
  3417	generic Chevalley--Eilenberg count applies\textup{)} down to exactly
  3418	$\mathrm{rk}(\fg)$ at admissible levels with $q \geq 3$.
  3419	\end{conjecture}
  3420	
  3421	\begin{remark}[Mechanism and base case]
  3422	\label{rem:admissible-rank-obstruction-mechanism}

thinking
**Addressing notation inconsistencies**

I notice there’s a notation drift in lines 2094 and 2357, which seems ambiguous due to an inconsistency in the r-matrix convention. I’ll need to rewrite it as `r(z)=\Omega/((k+2)z)` or `\frac{\Omega}{(k+2)z}` since the user wants an exact fix. I also should check for similar ambiguous cases with the Virasoro r-matrix, like `c/2z^3` versus `(c/2)/z^3`. The equation in line 90 is mathematically equivalent; I’ll look for quartic `z^4` or `z^2` to verify.
exec
/bin/zsh -lc "rg -n 'z\\"'^4|z'"\\"'^2|r'"\\"'^'"\\{\\\\mathrm\\{Vir\\}.*z\\"'^3|r'"\\(z\\) = .*2T/z|c/2z\\"'^3|c/2'"\\)/z\\"'^3|c/2/z'"\\"'^3|Omega/'"\\(k\\+2\\)\\\\,z|Omega/\\(\\(k\\+2\\)\\\\,z\\)|Omega/\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z|Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z\\)' chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/landscape_census.tex:463: & $(c/2)/z^3 + 2T/z$
chapters/examples/landscape_census.tex:468: & $(c/2)/z^3 + 2T/z$
chapters/examples/landscape_census.tex:478: & $(c/3)/z^5 + 2T/z^3 + \partial T/z^2 + \cdots$
chapters/examples/w_algebras.tex:65:$r$-matrix $r(z)$ & $(c/2)/z^3 + 2T/z$ &
chapters/examples/w_algebras.tex:1474:r^{\mathrm{Vir}}_c(z) = \frac{c/2}{z^3} + \frac{2T}{z}.
chapters/examples/w_algebras.tex:1487:At $c = 0$: the cubic pole vanishes and $r(z) = 2T/z$.
chapters/examples/w_algebras.tex:1489:$r(z) = (13/2)/z^3 + 2T/z$.
chapters/examples/w_algebras.tex:1490:At $c = 26$: $r(z) = 13/z^3 + 2T/z$.
chapters/examples/w_algebras.tex:1504:$r^{\cW_3}_{TT}(z) = (c/2)/z^3 + 2T/z$.
chapters/examples/w_algebras.tex:1530:+ \frac{\partial T}{z^2}
chapters/examples/kac_moody.tex:1398:residue of $k(J^a,J^b)/z^2 \cdot (1/z + O(z))$ is zero
chapters/examples/kac_moody.tex:2094:yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
chapters/examples/kac_moody.tex:2263:Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
chapters/examples/kac_moody.tex:2357:$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no
chapters/examples/kac_moody.tex:2978:singularity $\{xy = z^2\} \subset \mathbb{A}^3$). The associated
chapters/examples/kac_moody.tex:3258:= (-i\tau)^{1/2}\, e^{\pi i m z^2/\tau}\,
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2256,2270p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2256	\eta_{12} \wedge \eta_{23}
  2257	\;+\;
  2258	\eta_{23} \wedge \eta_{31}
  2259	\;+\;
  2260	\eta_{31} \wedge \eta_{12}
  2261	\;=\; 0.
  2262	\end{equation}
  2263	Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
  2264	$z_{ij} = z_i - z_j$.
  2265	The CYBE
  2266	\begin{equation}\label{eq:sl2-cybe}
  2267	[r_{12}(z_{12}),\; r_{13}(z_{13})]
  2268	\;+\;
  2269	[r_{12}(z_{12}),\; r_{23}(z_{23})]
  2270	\;+\;



thinking
**Analyzing notation issues**

I'm looking at some potential notation issues in a specific file, using regex to find occurrences like `Omega/(k+2)\,z` and `Omega/(k+h^\vee)\,z`. There are specific line references like 2094, 2263, and 2357 that I can bundle together or format separately, depending on user preferences. 

The user requested every inconsistency, so I need to be precise. I might format my output as `chapters/examples/kac_moody.tex:2094,2263,2357` or provide separate findings for clarity.
thinking
**Identifying potential notation issues**

I think I'm okay with the notation, but I need to be precise. There's a possible seam bug: in `kac_moody.tex:1768`, it refers to `\Omega_\fg` in a different way than earlier lines (750-752) that define `\Omega`. I also noticed a gap in the Virasoro section from lines 2712-2745, where it states `obs_g` without the required `(UNIFORM-WEIGHT)` tag. The user specifically requested an audit and checks, so I'll focus on the consistency of kappa formulas, r-matrix conventions, and central charge formulas, as that's their main concern.
thinking
**Inspecting code context**

I’m considering a potential issue with the `w_algebras` line 128, specifically the notation `$m_0^{(T)} = c/2$ and $m_0^{(W)} = c/3$`. I think I need to check the context around lines 48-70 or 120-130 to fully understand this. There could also be an issue with object confusion, so I’ll look closely at the code in that range from 40-130 to clarify any misunderstandings.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '44,132p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    44	
    45	\begin{table}[ht]
    46	\centering
    47	\small
    48	\caption{Shadow archetype data for
    49	$\mathcal{W}$-algebras (Virasoro and
    50	$\mathcal{W}_3$).}\label{tab:w-shadow-archetype}
    51	\begin{tabular}{lll}
    52	\toprule
    53	\textbf{Invariant} & \textbf{Virasoro} & \textbf{$\mathcal{W}_3$} \\
    54	\midrule
    55	Class & M (mixed/infinite) & M (mixed/infinite) \\
    56	Shadow depth $r_{\max}$ & $\infty$ & $\infty$ \\
    57	$\kappa$ &
    58	 $c/2$ & $5c/6$ \\
    59	Cubic shadow $\mathfrak{C}$ &
    60	 Nonzero & Nonzero \\
    61	Quartic $Q^{\mathrm{contact}}$ &
    62	 $10/[c(5c{+}22)]$ &
    63	 Multi-channel \\

thinking
**Inspecting the Virasoro algebra**

I’m thinking about the central charge of the Virasoro algebra through the Sugawara construction and trying to figure out the formula's specifics. I wonder if there's a factor of 1/2 that I might be missing, so I’ll take a closer look around 429 to confirm. Let’s ensure I don’t overlook anything important. It's a bit tricky, but I’m on it!
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '423,438p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   423	T = \frac{1}{2(k+h^\vee)} \sum_a {:}J^a J^a{:}
   424	\end{equation}
   425	\end{theorem}
   426	
   427	\subsection{The level and its meaning}
   428	
   429	\begin{definition}[Level as central charge]
   430	The \emph{level} $k$ determines the central charge of the Virasoro algebra via the Sugawara construction:\index{Sugawara construction}
   431	\begin{equation}
   432	c(k, \mathfrak{g}) = \frac{k \cdot \dim(\mathfrak{g})}{k + h^\vee}
   433	\end{equation}
   434	where $h^\vee$ is the dual Coxeter number. For $\mathfrak{sl}_n$ one has $h^\vee = n$ (so $h^\vee(\mathfrak{sl}_2) = 2$, $h^\vee(\mathfrak{sl}_3) = 3$); in general $h^\vee = 1 + \sum_i a_i^\vee$ where $\theta = \sum_i a_i \alpha_i$ is the highest root and $a_i^\vee$ are the dual Kac labels, or equivalently $h^\vee = (\rho|\theta^\vee) + 1$ with $\theta^\vee = 2\theta/(\theta|\theta)$.
   435	\end{definition}
   436	
   437	\begin{remark}[Critical level]
   438	At $k = -h^\vee$ (the \emph{critical level}), the Sugawara construction is undefined: the denominator $k + h^\vee$ vanishes, so no Virasoro subalgebra is produced. The critical level is distinguished on three counts: the theory admits a commutative chiral algebra structure (the classical limit), the center $Z(\widehat{\mathfrak{g}}_{-h^\vee})$ becomes infinite-dimensional (Feigin--Frenkel), and the algebra governs self-dual Yang--Mills theory. For Koszul duality, the critical level is the fixed point of the Feigin--Frenkel involution $k \mapsto -k - 2h^\vee$: the curvature $m_0 \propto (k + h^\vee)$ vanishes, making the bar complex a genuine (uncurved) dg coalgebra and the Koszul dual algebra uncurved.


thinking
**Verifying notation consistency**

I need to check if `kac_moody.tex` and `w_algebras.tex` use the same notation for class labels, and I want to do this without focusing on font differences. It's important for clarity and consistency in whatever I'm working on, so I'll look through both files carefully to make sure that the class labels align properly. That could really help with understanding the content better!
thinking
**Inspecting mathematical notation**

I need to take a closer look at line 447, as TeX spacing might be affecting how the denominator appears. In math, `\Omega/(k{+}h^\vee)\,z` means `(\Omega/(k+h^\vee)) z`, which is different from `\Omega/((k+h^\vee)z)`. It looks wrong and ambiguous. There might be a seam inconsistency since a section in the KM chapter refers to census records equivalently but lacks proper parenthesis for clarity. I should check the census files and see if there's a need for a fix. Let's investigate line 447.
codex
The canonical census itself has an `r`-matrix formatting hazard in the class-`L` caption. If that denominator is not fully parenthesized, the seam is broken at the source, not just in the chapter prose. I’m verifying that line in context now.
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '444,452p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   444	 & $0$
   445	 & --- \\
   446	\hline
   447	\multicolumn{6}{|c|}{\textit{Class L (Lie/tree): collision residue $r^{\mathrm{coll}}(z) = k\Omega_{\mathrm{tr}}/z = \Omega/(k{+}h^\vee)\,z$}} \\
   448	\hline
   449	$\widehat{\fg}_k$ (diagonal $J^a J^a$)
   450	 & $1$ & $\{2\}$ & $\{1\}$
   451	 & $k\Omega^{aa}/z$
   452	 & IBR \\

thinking
**Inspecting repeated results**

I’m noticing that many search results show the same expression, `m_0^{(T)} = c/2`. It feels important to check contexts 1901 and 2780 to see if the same bug appears in those seam summary lines. These lines are crucial because they show up in the chapter synthesis and the verification of the five theorems. I really want to make sure everything is correct, so inspecting those contexts is my next step!
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1896,1915p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2774,2785p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1150,1172p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
  1909	Unlike the Virasoro algebra, which has a single generator $T$, giving a single
  1910	curvature channel $\kappa = c/2$. The $\mathcal{W}_3$ algebra has two
  1911	generators $T$ (weight~$2$) and $W$ (weight~$3$), producing two
  1912	independent vacuum leakages whose sum gives the total obstruction
  1913	coefficient $\kappa = c/2 + c/3 = 5c/6$. The cross-terms
  1914	$T \otimes W$ and $W \otimes T$ contribute no vacuum leakage
  1915	(the $TW$ OPE has at most a double pole), so the curvature is
 succeeded in 50ms:
  2774	\textbf{A} (Adjunction) &
  2775	 $(\mathcal{W}_3^k)^! \simeq \mathcal{W}_3^{-k-6}$
  2776	 via the Feigin--Frenkel involution
  2777	 \textup{(}Theorem~\textup{\ref{thm:w-algebra-koszul-main}}\textup{)}.
  2778	 Involutive: $(-k-6)' = k$.
  2779	 Koszul self-dual at $c = 50$ (fixed point of $c \mapsto 100{-}c$).
  2780	 Two curvature channels: $m_0^{(T)} = c/2$, $m_0^{(W)} = c/3$.
  2781	 \\
  2782	\textbf{B} (Inversion) &
  2783	 $\Omega(\bar{B}(\mathcal{W}_3^k)) \xrightarrow{\sim} \mathcal{W}_3^k$,
  2784	 genus-$0$ $E_2$-collapse at generic $k$
  2785	 \textup{(}Theorem~\textup{\ref{thm:w-koszul-precise}}\textup{)}.
 succeeded in 52ms:
  1150	
  1151	\begin{proof}[Computation for $\mathcal{W}_3$]
  1152	We detect the curvature by computing $m_1^2$ on a generator $T$. Here $m_1$ denotes the $A_\infty$ structure map (the bar differential using only $m_2$). Note that the \emph{full} bar complex differential $d_{\bar{B}}$ always satisfies $d_{\bar{B}}^2 = 0$; the failure of $m_1^2 = 0$ reveals the curvature $m_0$ via the curved $A_\infty$ relation $m_1^2(a) = m_2(m_0, a) - m_2(a, m_0) = [m_0, a]$ (see Appendix~\ref{app:koszul-reference}).
  1153	
  1154	\emph{Step~1.} Apply $m_1$ once:
  1155	\begin{equation}
  1156	m_1(T) = T \boxtimes T \otimes \eta_{12} + (\text{descendants})
  1157	\end{equation}
  1158	
  1159	\emph{Step~2.} Apply $m_1$ again. The OPE $T(z_1)T(z_2) = \frac{c/2}{(z_1-z_2)^4} + \frac{2T(z_2)}{(z_1-z_2)^2} + \frac{\partial T(z_2)}{z_1-z_2} + \cdots$ contributes through the Poincar\'e residue on the collision divisor.
  1160	
  1161	\emph{Step~3.} The fourth-order pole gives the leading contribution:
  1162	\begin{equation}
  1163	m_1^2(T) = \frac{c}{2} \cdot \mathbf{1} \neq 0 \quad \text{if } c \neq 0
  1164	\end{equation}
  1165	Since $m_1^2 \neq 0$, the $A_\infty$ structure is curved. The curvature element $m_0$ (determined implicitly by the curved $A_\infty$ relation $m_1^2(a) = [m_0, a]_{m_2}$) is a degree-2 element in the bar complex, \emph{not} a scalar multiple of the vacuum.
  1166	
  1167	\emph{Two distinct vanishing conditions.} The Virasoro subalgebra contribution $m_1^2(T) = \frac{c}{2} \cdot \mathbf{1}$ vanishes at $c = 0$. The full curvature of the $\mathcal{W}$-algebra bar complex (involving all generators, not just~$T$) is proportional to $(k + h^\vee)$ and vanishes at critical level $k = -h^\vee$, where the DS reduction degenerates and the $\mathcal{W}$-algebra is replaced by the Feigin--Frenkel center. These are different conditions: $c = 0$ and $k = -h^\vee$ do not coincide for $\mathcal{W}_N$ with $N \geq 3$.
  1168	
  1169	For $\mathcal{W}_3$ (Drinfeld--Sokolov reduction of $\widehat{\mathfrak{sl}}_3$ at level $k$), we have $c = 2 - \frac{24(k+2)^2}{k+3}$. (The $\mathcal{W}_3$ minimal models $\mathcal{W}_3(p,q)$ with $p > q \geq 3$ coprime have $c = 2(1 - 12(p-q)^2/(pq))$; for consecutive parameters $(p, p-1)$ this gives $c = 2 - 24/(p(p-1))$. These arise from the DS formula at specific rational values of $k$, not by the substitution $p = k+3$. The two parametrizations are related but distinct.)


thinking
**Considering severity of object confusion**

I think the severity might be HIGH because the wrong object is repeated, creating a seam inconsistency. Since the user is checking the kappa formulas for consistency, this confusion could be subtle but serious. I lean towards labeling it as HIGH since it directly undermines the statement of Virasoro curvature in relation to Kac-Moody. There might be gaps in `w_algebras.tex` concerning affine critical levels, but earlier lines distinguish them. I wonder if similar issues arise in `kac_moody.tex`.
thinking
**Evaluating curvature formulas**

I'm looking at the general W curvature formula, which is `m_0'=(k'+h^\vee) C_2`. I think there might be a conflict with the explicit formulas from Virasoro, so I’ll need to read more context to understand better. Let’s inspect the surrounding details from 360 to 405 to clarify the situation and see how these concepts might interact or fit together! It's always good to double-check those ranges.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '360,405p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   360	where $Q_{\mathrm{DS}}^{\mathrm{bar}}$ is the BRST differential
   361	induced on the bar complex by functoriality of~$\bar{B}$.
   362	Taking cohomology with respect to
   363	$Q_{\mathrm{DS}}^{\mathrm{bar}}$:
   364	The bar complexes of the constituent free fields are known: $\bar{B}(\mathcal{H}_k) \simeq \mathrm{coLie}^{\mathrm{ch}}(V^*)$ (the bar differential vanishes since the Heisenberg OPE has only a double pole; the coalgebra retains the level~$k$ through the pairing on~$V$, cf.\ Theorem~\ref{thm:heisenberg-koszul-dual-early}), and $\bar{B}(\mathcal{F}_{\beta\gamma})^\vee \simeq \mathcal{F}_{bc}$ (the bar coalgebra of $\beta\gamma$, dualized, is the $bc$ system, cf.\ Section~\ref{sec:betagamma-koszul-dual}).
   365	
   366	\emph{Step~3: BRST cohomology at the dual level.}
   367	The BRST differential $Q_{\mathrm{DS}}$ acts on the bar complex.
   368	
   369	The bar construction dualizes the coalgebra on the Heisenberg factor,
   370	so the screening momenta change sign:
   371	$\alpha_i \mapsto -\alpha_i$.
   372	This is the effect of the Koszul pairing
   373	$J \mapsto J^*$ on the level-dependent bilinear form.
   374	
   375	By Feigin--Frenkel duality~\cite{Feigin-Frenkel}, the negated momenta
   376	$-\alpha_i$ are precisely the screening momenta at the dual level
   377	$k' = -k - 2h^\vee$.
   378	
   379	Therefore:






thinking
**Investigating seam inconsistency**

I’m considering a potential seam inconsistency regarding `m0` on the W-side when using the affine formula compared to the Virasoro coefficient formula. I need to confirm if this is indeed the same object represented differently before the DS reduction. Line 401 mentions the W-side curvature, while later lines detail the Virasoro obstruction, which seems different. Since they both use `m_0`, I’m questioning whether this is a true inconsistency or simply different representations of the object.
thinking
**Identifying internal inconsistency**

I see that line 1320 describes `m_0` as a unique element whose commutators reproduce quartic pole data, which isn’t `C_2`. This definitely indicates an internal inconsistency. However, I wonder if this might be outside the user’s four checks. It's all about the handoff of the curvature object, and I need to clarify how `m_0` fits into this context. There might be a deeper insight to uncover here!
thinking
**Searching for specific lines**

I'm considering searching for `\Omega/(k+2)\,z` in other files since I have some results already, like 2094. I should look for the exact match of `m_0 = c/2`, as there are many results. I might find repeated lines in `w_algebras.tex` too. There's an inconsistency where it mentions non-scalar curvature but lists scalars. I'll note this, and it seems to involve referencing specific lines with a severity of HIGH for corrections needed.
thinking
**Evaluating object conflations**

I'm thinking about the guidelines that say object conflations are critical and should be marked as HIGH. To be safe, I’ll stick with marking it as HIGH. It seems like I should only use CRITICAL if I'm dealing with a theorem or proof that is actually false, but that’s not the case here. So, I'll keep it straightforward and mark it as HIGH for now.
thinking
**Analyzing central charge gap**

I'm focused on the potential gap between the DS and Sugawara central charge functions, making sure no nearby sentences cause confusion. I found relevant references around lines 1256-1266, but there's a valid gap based on absence of comparison with Sugawara c. I suggest inserting a specific sentence after line 1264 to clarify the distinction. This might mean a medium severity issue. I also think about a similar gap in verification at line 2712. If I clarify Sugawara once in that context, it could work.
thinking
**Identifying critical point gaps**

I believe I need to address another gap regarding critical point distinction, which might be tied to the central-charge gap. In the section `w_algebras.tex:1261-1271`, the introduction of `c(k)` and the critical level doesn’t clearly separate the DS-reduced Virasoro `c(k)` from the affine Sugawara `c_{\mathrm{Sug}}(k)` or the Virasoro uncurved point `c=0`. I propose adding sentences to clarify this after line 1264 and another after line 1271 to address any confusion. I could also cite additional lines for support.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1708,1724p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1708	Theorem~\ref{thm:quantum-complementarity-main} applied to
  1709	$\cA = \mathrm{Vir}_c$ with $\cA^! = \mathrm{Vir}_{26-c}$
  1710	(Example~\ref{ex:virasoro-koszul-dual}).
  1711	
  1712	\emph{Step~1: Obstruction from curvature.}
  1713	By Theorem~\ref{thm:vir-genus1-curvature},
  1714	$(d^{(1)})^2 = (c/2) \cdot \omega_1$. Since $T$ is the sole generator,
  1715	the invariant endomorphisms of the vacuum module reduce to scalars:
  1716	$\operatorname{End}(V_c)^{\mathrm{Vir}_c} = \mathbb{C}$.
  1717	Therefore $Q_1(\mathrm{Vir}_c) = \mathbb{C} \cdot (c/2) \subset
  1718	H^0(\overline{\mathcal{M}}_{1,1})$.
  1719	
  1720	\emph{Step~2: Dual obstruction coefficient.}
  1721	The dual $\mathrm{Vir}_{26-c}$ has curvature $(26-c)/2 = 13 - c/2$, so
  1722	its raw obstruction coefficient is $(13 - c/2) \in H^0(\overline{\mathcal{M}}_{1,1})$.
  1723	The Kodaira--Spencer map (Theorem~\ref{thm:kodaira-spencer-chiral-complete})
  1724	applies the Verdier involution $\sigma\colon H^0 \xrightarrow{\sim} H^2$,

thinking
**Verifying formulas and patterns**

I’m checking my progress because my verdict is a fail. I think I can count around three files, which is good. Before finalizing, I should confirm if line 447 and line 2094 indeed parse incorrectly, and it seems they do. I might quickly apply LaTeX or regex for pattern counting, even though it's not strictly necessary. I'm also searching for identical ambiguous formulas in landscape_census. I’ll run exact counts and check for specific occurrences of m_0.
exec
/bin/zsh -lc "rg -n 'm_0 = c/2|m_0\\"'^'"\\{\\(T\\)\\} = c/2|m_0\\"'^'"\\{\\(W\\)\\} = c/3|m_0\\"'^'"\\{\\(T\\)\\}|m_0\\"'^'"\\{\\(W\\)\\}' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
128:$m_0^{(T)} = c/2$ and $m_0^{(W)} = c/3$, one per generator.
1548:$m_0 = c/2$ from the quartic pole $T_{(3)}T = c/2$, giving a curved
1557:($m_0 = c/2$, reflecting the quartic pole). The $B$-cycle monodromy at
1854:\dfib^{\,2}(W) &= \frac{c}{2} \cdot m_0^{(W)} + (\text{corrections from } W \times W \text{ sixth-order pole})
1901:independent channels: $m_0^{(T)} = c/2$ (quartic pole of $TT$) and
1902:$m_0^{(W)} = c/3$ (sixth-order pole of $WW$); see
2780: Two curvature channels: $m_0^{(T)} = c/2$, $m_0^{(W)} = c/3$.

thinking
**Inspecting formula context**

I’m looking closely at line 1854, which uses `dfib^2(W) = c/2 · m_0^{(W)} + ...`. It seems like it could be problematic, so I need to inspect the context around lines 1848 to 1856. It might be another false formula, and I want to make sure I understand the surrounding text to clarify this issue. This careful examination will help reveal any underlying problems.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1848,1858p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1848	+ W \otimes W \otimes (\text{complicated 2-form}) + (\text{descendants})
  1849	\end{multline}
  1850	
  1851	\emph{Computing $\dfib^{\,2}$.}
  1852	\begin{align}
  1853	\dfib^{\,2}(T) &= \frac{c}{2} \cdot \mathbf{1} \quad \text{(proportional to curvature; vanishes iff $c = 0$)} \\
  1854	\dfib^{\,2}(W) &= \frac{c}{2} \cdot m_0^{(W)} + (\text{corrections from } W \times W \text{ sixth-order pole})
  1855	\end{align}
  1856	
  1857	The $W \times W$ contribution involves the sixth-order pole, which contributes additional curvature terms.
  1858	\end{computation}
codex
- [HIGH] chapters/examples/landscape_census.tex:447 — PROBLEM: The canonical class-`L` caption writes `\Omega/(k{+}h^\vee)\,z`, which parses as `(\Omega/(k+h^\vee))z`, not the KZ form `\Omega/((k+h^\vee)z)`. That breaks the stated equivalence to `k\Omega_{\mathrm{tr}}/z`. FIX: replace the caption fragment with `\Omega/\bigl((k{+}h^\vee)z\bigr)` or `\frac{\Omega}{(k{+}h^\vee)z}`.

- [HIGH] chapters/examples/kac_moody.tex:2094 — PROBLEM: The same denominator drift reappears in the explicit `\widehat{\mathfrak{sl}}_2` seam computation; `r(z)=\Omega/(k+2)\,z` no longer matches the chapter’s own KZ normalization at 731-750. The same bad form repeats at 2263 and 2357. FIX: change all three occurrences to `r(z)=\frac{\Omega}{(k+2)z}` and `r_{ij}=\frac{\Omega}{(k+2)z_{ij}}`.

- [HIGH] chapters/examples/w_algebras.tex:127 — PROBLEM: The Vir/W-seam collapses the curvature element into scalars. The file says the curvature is “non-scalar” and then writes `m_0^{(T)} = c/2`, `m_0^{(W)} = c/3`; the same false scalarization recurs at 1548, 1557, 1901-1902, and 2780, contradicting the file’s own correction at 1165 and 1320 that `m_0` is not a scalar multiple of the vacuum. FIX: rename every scalar channel to coefficient notation, e.g. `\kappa_T = c/2`, `\kappa_W = c/3`, and reserve `m_0` for the actual degree-2 element; at 1548 specifically replace `m_0 = c/2` with `\kappa(\mathrm{Vir}_c)=c/2`, and if the element is needed add `m_0` is characterized by `[m_0,T]=(c/2)\mathbf{1}`.

- [MEDIUM] chapters/examples/w_algebras.tex:1261 — PROBLEM: The KM→Vir handoff introduces `c(k)=1-6(k+1)^2/(k+2)` without explicitly fencing it off from the affine Sugawara charge `3k/(k+2)` in chapters/examples/kac_moody.tex:432. The same level parameter `k` is reused, so the seam hides that two different central-charge functions are in play. FIX: append after 1264: `This \(c(k)\) is the Drinfeld--Sokolov reduced Virasoro central charge; it is not the affine Sugawara charge \(3k/(k+2)\) of the parent \(\widehat{\mathfrak{sl}}_2\).`

- [MEDIUM] chapters/examples/w_algebras.tex:1269 — PROBLEM: The critical-level sentence gives the affine critical point `k=-2`, but the explicit Virasoro pipeline later uses the uncurved condition `c=0` (`1548`, `1620-1622`) without stitching the two apart at the seam. That invites the false reading that the Virasoro uncurved point is the affine critical point. FIX: append after 1271 or 1622: `The affine critical point \(k=-2\) is distinct from the Virasoro uncurved locus \(c=0\); under \(c(k)=1-6(k+1)^2/(k+2)\), the latter occurs away from the critical affine level.`

- [LOW] chapters/examples/kac_moody.tex:19 — PROBLEM: The chapter opening hands off to Virasoro only by saying Jacobi no longer kills the tower; it does not state the actual seam invariant used later in the census and Virasoro chapter, namely `Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]` and class `M`. FIX: replace the last clause with `for the Virasoro algebra (Chapter~\ref{chap:w-algebra-koszul}), the quartic contact term \(Q^{\mathrm{contact}}_{\mathrm{Vir}}=10/[c(5c+22)]\) is generically nonzero and the quintic obstruction is forced, so the tower is class~M and does not terminate.`

## Summary
Checked: 3 | Findings: 6 | Verdict: FAIL
tokens used
193,617
