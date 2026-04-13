# S10_examples_to_wn (447s)

- [CRITICAL] chapters/examples/free_fields.tex:4522 — PROBLEM: The live Virasoro seam writes `d_{\mathrm{equiv}}^2 = (c - 26)\,\mu` with `\mu=\kappa_1`, but the same theorem block then identifies the coefficient as `\kappa(\mathrm{Vir}_c)-\kappa(\mathrm{Vir}_{26}) = c/2 - 13` at line 4546 and restates the obstruction as `(c/2 - 13)\,\kappa_1` at line 4609. Those coefficients are not equal. FIX: Replace `(c - 26)` by `(c/2 - 13)` at lines 4522 and 4546 so the theorem, proof, and remark all use the same Virasoro normalization `\kappa(\mathrm{Vir}_c)=c/2`; keep `\mu=\kappa_1`.

- [MEDIUM] chapters/examples/w_algebras.tex:2721 — PROBLEM: This section says it records “the five main theorems” (2702-2705), but slot `A` is not Theorem A from the concordance. Here `A` is used for Koszul-dual partner data `\mathrm{Vir}_c^!\simeq \mathrm{Vir}_{26-c}`; the same drift repeats at 2774 and 2830, while the concordance defines Theorem A as Bar-cobar adjunction at chapters/connections/concordance.tex:31. FIX: Rewrite 2702-2705 to say this section records the W-algebra theorem package, not the five theorem labels verbatim; relabel the `A` entries at 2721, 2774, and 2830 as `Koszul duality` instead of `A (Adjunction)`.

- [MEDIUM] chapters/examples/w_algebras.tex:3477 — PROBLEM: The seam collapses `c` and `\kappa`: `\kappa(\mathrm{Vir}_c)=c/2` is called “the central charge of the gravity theory” at 3478-3479, the curvature is said to be “weighted by the central charge” at 3485, and the sum `\kappa+\kappa'=13` is called “the total gravitational central charge” at 3493. But the same chapter separates these quantities via the anomaly-ratio formulas `\varrho=\kappa/c` and `\kappa(\mathcal W_N)=c(H_N-1)` at 2743 and 2836. FIX: Replace “central charge” by “modular characteristic” at 3478, 3485, and 3493; if you want the relation to `c`, add “for Virasoro, `\kappa=c/2`.”

- [LOW] chapters/examples/w_algebras.tex:2172 — PROBLEM: `thm:wn-obstruction` proves the right general formula, but the seam specialization `\mathcal W_2=\mathrm{Vir}` is only buried in the verification bullets at 2265-2266. The theorem statement itself never surfaces the `N=2` check that the chapter opening relies on. FIX: After line 2182 add: `For N=2, H_2=3/2, so \mathcal W_2=\mathrm{Vir}_c and \kappa(\mathcal W_2)=c/2, recovering Theorem~\ref{thm:vir-genus1-curvature}.`

- [LOW] chapters/connections/concordance.tex:9613 — PROBLEM: The constitutional formula surface writes `\kappa(\Walg_N)=c(H_N{-}1)` without defining `H_N`; the same naked shorthand reappears in chapters/examples/landscape_census.tex:1416. That leaves the exact harmonic-number convention implicit on the very seam where this repo repeatedly drifts between `H_N` and `H_{N-1}`. FIX: Expand both sites to `\kappa(\Walg_N)=c\sum_{j=2}^{N}1/j = c(H_N{-}1)`, with `H_N=\sum_{j=1}^{N}1/j`.

No `H_{N-1}` bug or `N=2` arithmetic failure survived re-verification; the surviving defects are coefficient normalization, theorem-surface sync, and explicitness gaps.

## Summary
Checked: 4 files | Findings: 5 | Verdict: FAIL


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
session id: 019d83c7-8317-7bf0-ba73-2cee32d9960e
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


MISSION: SEAM AUDIT between virasoro.tex and w_algebras.tex.

Vir→W_N. Check: (a) W_2=Vir specialization works, (b) kappa(W_N) at N=2 gives c/2, (c) harmonic number H_N convention consistent

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers
codex
Using `deep-beilinson-audit` and `multi-path-verify` for a seam audit focused on `virasoro.tex` ↔ `w_algebras.tex`. I’m starting by loading the required repo invariants, then I’ll read the two chapter surfaces and grep for the `W_2`, `\kappa(W_N)`, and harmonic-number transition points.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files | rg '("'^|/)(CLAUDE'"\\.md|concordance\\.tex|theorem_registry\\.md|red_team_summary\\.md|virasoro\\.tex|w_algebras\\.tex)"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/examples/w_algebras.tex
chapters/connections/concordance.tex
 succeeded in 54ms:
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


thinking
**Locating required files**

I need to read the necessary files and also find the target. I'll have to locate virasoro.tex as well, though I’m not sure if that’s the exact file name. It might be a good idea to search for it. I think I’ll use rg for this task, as it’s effective for searching through file contents. Let’s see what I can find!
codex
I have the audit workflow loaded. Next I’m reading the repo’s canonical formula/status surfaces plus the exact Virasoro and `W` chapter files, then I’ll pin the seam lines where `W_2`, `\kappa(W_N)`, and `H_N` are actually stated.
exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg 'virasoro.*\\.tex"'$|(''^|/)vir.*'"\\.tex"'$|w_algebras'"\\.tex"'$|landscape_census'"\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
chapters/examples/logarithmic_w_algebras.tex
chapters/examples/landscape_census.tex
chapters/examples/w_algebras.tex
standalone/virasoro_r_matrix.tex
standalone/cover_letter_virasoro_r_matrix.tex
codex
`virasoro.tex` does not exist under that name in this tree, so I’m locating the actual Virasoro chapter surface before I audit the seam. I’ll search the examples/theory tree for the chapter that carries the Virasoro formulas and the transition into `w_algebras.tex`.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\chapter\\{.*Virasoro|\\\\section\\{.*Virasoro|\\\\label\\{chap:.*vir|\\\\label\\{sec:.*vir|Virasoro algebra|Vir_c|kappa\\(Vir' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'W_2|W_N|H_N|H_\\{N\\}|H_\\{N-1\\}|kappa\\(W_N\\)|c/2|W_2=|W_2\\\\cong|W_2.*Vir|Vir.*W_2' chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters examples appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 522

standalone/computations.tex:794:coproduct. The Virasoro algebra has $\lambda^3$ (quartic pole),
standalone/N6_shadow_formality.tex:620:The Virasoro vertex algebra $\Vir_c$ has $\kappa(\Vir_c)=c/2$.
standalone/N6_shadow_formality.tex:622:$H^*(\barB(\Vir_c))$ satisfy
standalone/N6_shadow_formality.tex:636:$r_{\max}(\Vir_c)=\infty$: Virasoro is intrinsically
standalone/gaudin_from_collision.tex:387:\subsection{The Virasoro algebra: $k_{\max} = 3$}
standalone/gaudin_from_collision.tex:389:The Virasoro algebra has generators $T$ of weight $2$ with OPE
standalone/gaudin_from_collision.tex:416:The GZ Hamiltonians for the Virasoro algebra are $2$nd-order
standalone/ordered_chiral_homology.tex:7362:which generates an inner action of the Virasoro algebra at
standalone/ordered_chiral_homology.tex:8229:The Virasoro algebra $\mathrm{Vir}_c$ has a single generating
standalone/ordered_chiral_homology.tex:8241:% C2: kappa(Vir) = c/2. c=0 -> 0; c=13 -> 13/2 self-dual.
standalone/programme_summary_section1.tex:165:the failure that the Virasoro algebra measures.
standalone/programme_summary_section1.tex:588:\kappa(\Vir_c)
standalone/programme_summary_sections5_8.tex:47:$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
standalone/programme_summary_sections5_8.tex:437: $\Vir_c^! = \Vir_{26-c}$ (or
standalone/programme_summary_sections5_8.tex:455:The Virasoro Koszul duality $\Vir_c^! = \Vir_{26 - c}$
standalone/virasoro_r_matrix.tex:58:The spectral $R$-matrix of the Virasoro algebra on a primary state of
standalone/virasoro_r_matrix.tex:66:shadow coefficient $S_3(\Vir_c) = 2$ is independent of the central
standalone/virasoro_r_matrix.tex:99:For the Virasoro algebra $\Vir_c$, the $R$-matrix on a primary state
 exited 2 in 50ms:
Total output lines: 1928

rg: examples: No such file or directory (os error 2)
standalone/computations.tex:232:The total is $c/2304 + c/3456 = (3c + 2c)/6912 = 5c/6912 =
standalone/computations.tex:436:& $c/2304$ & $c/3456$ & $0$ & $5c/6912$ \\[2pt]
standalone/computations.tex:465:$\kappa_T = c/2$.
standalone/computations.tex:468:= \frac{2(20 - c/2)}{48}
standalone/computations.tex:554: $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$,
standalone/computations.tex:720:r^{\mathrm{Vir}}(z) = \frac{c/2}{z^3} + \frac{2T}{z}.
standalone/computations.tex:724:\item The \emph{leading coefficient} $c/2 = \kappa(\mathrm{Vir}_c)$
standalone/computations.tex:726: $F_g = (c/2) \int_{\overline{\mathcal{M}}_g} \lambda_g$ (uniform-weight) at all
standalone/computations.tex:729: transition at $h = c/24$.
standalone/computations.tex:753:$(c/2)/z^3 + 2T/z$ by homological perturbation through the
standalone/computations.tex:777: & $(c/2)/z^3 + 2T/z$ (cubic pole) \\[2pt]
standalone/computations.tex:783: & $c/2$ \\[2pt]
standalone/N6_shadow_formality.tex:422:$\kappa^{\Vir}=c/2$, $\kappa^{\Heis}=k$,
standalone/N6_shadow_formality.tex:424:$\kappa^{\cW_N}=c(H_N-1)$ with $H_N=\sum_{j=1}^N 1/j$. The
standalone/N6_shadow_formality.tex:425:coincidence $\kappa=c/2$ holds only for Virasoro, not universally;
standalone/N6_shadow_formality.tex:426:writing $\kappa=c/2$ for a non-Virasoro family is a standard
standalone/N6_shadow_formality.tex:620:The Virasoro vertex algebra $\Vir_c$ has $\kappa(\Vir_c)=c/2$.


thinking
**Investigating file references**

I need to figure out if the user is referring to the Vir section in `free_fields.tex` instead of `virasoro.tex`, which seems to be missing. My mission is to audit the seam between `virasoro.tex` and `w_algebras.tex`, particularly checking if the specialization W_2=Vir works. I should search for relevant chapters and determine if `free_fields.tex` contains the needed information. It's essential to identify transition points carefully, especially since the user mentioned a specific relationship between these files.
thinking
**Examining file structure**

I’m checking if `chapters/examples/free_fields.tex` has the Virasoro chapter and if `chapters/examples/w_algebras.tex` contains the W algebras. I also need to inspect the chapter order in `main.tex` to locate inclusions for both. Maybe there's a `virasoro.tex` in another volume, but the user specified to focus on the current repository. I should search using `rg` in the `chapters/examples` directory for specific labels and inspect the table of contents too. It’s crucial to read the relevant sections carefully for inconsistencies and provide exact fixes as needed.
codex
The “Virasoro” side is not a standalone `virasoro.tex` file here. I’m checking the live chapter graph to identify which file actually carries the Virasoro chapter/section that feeds into `chapters/examples/w_algebras.tex`, so the seam audit stays grounded in real source rather than the filename in the prompt.
exec
/bin/zsh -lc "rg -n 'w_algebras|free_fields|minimal_model_examples|genus_expansions' main.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '4480,4625p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1220,1268p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/holomorphic_topological.tex:12:% conj:agt-w-algebra defined in w_algebras_framework.tex
main.tex:1189:\include{chapters/examples/free_fields}
main.tex:1226:\include{chapters/examples/w_algebras}
main.tex:1228:% \include{chapters/examples/w_algebras_computations}
main.tex:1240:\input{chapters/examples/minimal_model_examples}
main.tex:1245:\input{chapters/examples/w_algebras_deep}
main.tex:1315:\input{chapters/examples/logarithmic_w_algebras}
main.tex:1320: \input{chapters/examples/genus_expansions}
main.tex:1537: \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
main.tex:1546: \phantomsection\label{subsec:genus2-complementarity-verification}% % genus_expansions.tex
main.tex:1550: \phantomsection\label{rem:sl2-vs-vir-complementarity}% % genus_expansions.tex
main.tex:1552: \phantomsection\label{conj:non-simply-laced-discriminant}% % genus_expansions.tex
main.tex:1561: \phantomsection\label{rem:convergence-vs-string}% % genus_expansions.tex
main.tex:1570: \phantomsection\label{thm:sl2-genus2-curvature}% % genus_expansions.tex
main.tex:1571: \phantomsection\label{thm:complementarity-root-datum}% % genus_expansions.tex
main.tex:1576: \phantomsection\label{ch:genus-expansions}% % genus_expansions.tex
 succeeded in 51ms:
  4480	
  4481	
  4482	\section{Virasoro, strings, and moduli}\label{sec:virasoro-strings-moduli}
  4483	
  4484	The Virasoro bar complex is analyzed at general central charge. On the
  4485	critical locus $c = 26$, the genus-$0$ equivariant anomaly vanishes,
  4486	giving the proved critical BRST/bar comparison on the total
  4487	matter+ghost string algebra. Stronger claims about full moduli-space
  4488	cohomology, physical amplitudes, or modular invariance require
  4489	additional input and are fenced below.
  4490	
  4491	\subsection{Virasoro at critical central charge}
  4492	
  4493	The free-field dualities above all involve algebras with a single OPE
  4494	pole order. The Virasoro algebra, with its double-pole Sugawara term,
  4495	is the first example where the bar complex exhibits genuine curvature.
  4496	 
  4497	\subsubsection{Setup}
  4498	 
  4499	\begin{definition}[Virasoro algebra]
 succeeded in 50ms:
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
 succeeded in 51ms:
  1220	\index{anomaly ratio!Polyakov formula}
  1221	The anomaly ratio $\varrho(\cA) := \kappa(\cA)/c(\cA)$ measures how much of the conformal anomaly survives from the Lie bracket's cyclic deformation. For the rank-$d$ Heisenberg algebra $\cH_1^{\oplus d}$ at level~$1$, $\varrho = d/d = 1$: the Polyakov formula $F_1 = c/24$ and the shadow formula $F_1 = \kappa/24$ coincide because $\kappa = c = d$. For all other standard families, $\varrho \neq 1$:
  1222	\begin{center}
  1223	\begin{tabular}{lccc}
  1224	Family & $c$ & $\kappa$ & $\varrho = \kappa/c$ \\ \hline
  1225	$\mathcal{H}_1^{\oplus d}$ \textup{($d$ bosons)} & $d$ & $d$ & $1$ \\
  1226	$\widehat{\mathfrak{sl}}_{2,k}$ & $3k/(k{+}2)$ & $3(k{+}2)/4$ & $(k{+}2)^2/(4k)$ \\
  1227	$\beta\gamma_{\lambda=1}$ & $2$ & $1$ & $1/2$ \\
  1228	$\mathrm{Vir}_c$ & $c$ & $c/2$ & $1/2$ \\
  1229	$\mathcal{W}_{3,c}$ & $c$ & $5c/6$ & $5/6$ \\
  1230	\end{tabular}
  1231	\end{center}
  1232	The ratio $\varrho(\mathrm{Vir}_c) = 1/2$ means that half the conformal anomaly is absorbed by the nonlinearity of the Virasoro OPE. For $\widehat{\mathfrak{sl}}_{2}$ at level~$k$, $\varrho = (k{+}2)^2/(4k) \sim k/4$ as $k \to \infty$ (linearly divergent) and also diverges at $k \to 0$. The genus-$g$ free energy $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ carries the modular
  1233	characteristic~$\kappa$, not the central charge~$c$; at genus~$1$,
  1234	$F_1 = \kappa/24$.
  1235	\end{remark}
  1236	
  1237	\begin{corollary}[Anomaly ratio and DS reduction; \ClaimStatusProvedHere]
  1238	\label{cor:anomaly-ratio-ds}
  1239	\index{anomaly ratio!DS reduction}

thinking
**Searching definitions**

I'm exploring the free_fields for relevant lines regarding kappa. I wonder if free_fields omits W_2 because it's specifically about Vir. I should think about comparing definitions or notations to get a clearer understanding. It's a bit tricky, and I need to ensure I'm interpreting everything correctly. By examining these distinctions, I might uncover more insights into their relationships and how they apply. Let’s see where this takes me!
codex
I’ve pinned the actual seam: `main.tex` goes from `chapters/examples/free_fields.tex` into `chapters/examples/w_algebras.tex`, and the Virasoro material lives in `free_fields.tex`, not a standalone `virasoro.tex`. I’m now reading the exact `\kappa(\mathcal W_N)` theorem block, the local `H_N` definitions, and the Virasoro specialization statements to see whether the chapter actually matches its own `N=2` claim.
exec
/bin/zsh -lc "rg -n 'kappa\\(|c/2|F_1|obs_1|genus-1|Virasoro' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'W_2|H_N|H_\\{N\\}|H_\\{N-1\\}|kappa\\(W_N\\)|kappa\\(\\\\mathcal\\{W\\}_N\\)|c \\* \\(H_N - 1\\)|c \\cdot \\(H_N - 1\\)' chapters/examples/landscape_census.tex chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:wn-obstruction|H_N|W_2|Virasoro specialization|kappa\\(\\\\mathcal\\{W\\}_N\\)|kappa = c \\\\cdot \\(H_N - 1\\)|\\\\mathcal W_N|\\\\mathcal\\{W\\}_N' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2148,2315p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
83:$\kappa(\beta\gamma) = c/2$ is generically nonzero). Both
152:the Virasoro algebra
174:Modular characteristic $\kappa(\mathcal{F}) = c/2 = 1/4$.
230: $\kappa(\mathcal{F}) = c/2 = 1/4$.
257:fermion of weight $h = 1/2$; standard from the Virasoro commutation
259:Then $\kappa = c/2 = 1/4$ by the universal formula
319:$\kappa(\mathcal{H}_k) = k$ is tunable
321:$\kappa(\mathcal{F}) = 1/4$ is fixed.
346:F_1(\mathcal{F}) &= \frac{1}{96},
364:with $\kappa(\mathcal{F}) = 1/4$
382:The explicit checks: $F_1 = (1/4)(1/24) = 1/96$;
396:= \frac{\kappa(\mathcal{F})}{\kappa(\mathcal{H}_k)}
478: $\kappa(\mathcal{F}^!) = -1/4$.
481: $\kappa(\mathcal{F}) + \kappa(\mathcal{F}^!) = 0$.
500:$\kappa(\mathcal{F}^!) = c'/2 = -1/4$.
506:$\kappa(\mathcal{H}_k) + \kappa(\mathcal{H}_k^!) = k + (-k) = 0$.
645:$\kappa(\mathcal{F}^!)$ & $-1/4$ \\
648:$F_1$ & $1/96$ \\
669:($\kappa = c/2$ in every case; see landscape census
686: $\kappa(\mathcal{F}^{\otimes d}) = d/4$\textup{)}.
 succeeded in 50ms:
11:The $\mathcal{W}_N$ hierarchy answers by stratification. Each
12:$\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
16:$\mathcal{W}_3$ adds a weight-$3$ primary; $\mathcal{W}_N$ at higher
20:principal $\mathcal{W}_N$ into class~$\mathsf{M}$, with
38:complementarity potential $S_{\mathcal{W}_N}$ is non-polynomial.
124:$d_2$); for $\mathcal{W}_N$ with $N \geq 3$, higher-order poles from
132:For principal $\mathcal{W}_N^k$ at generic level, the shadow
139:potential~$S_{\mathcal{W}_N}$ is non-polynomial.
142:identification $\Gamma_{\mathcal{W}_N}=\kappa(\mathcal{W}_N)\Lambda$
152:(i)~the \v{C}ech complex of $\mathcal{W}_N$ has secondary Borcherds
160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
164:$\mathcal{W}_N$ up to quasi-isomorphism; the contact Virasoro invariant
179:$\mathcal{W}_N$ is the first standard family exhibiting all three
200:inseparable for $\mathcal{W}_N$.
262:$\mathcal W_N$ family:
264:h_K(\mathcal W_2) \approx 0.567
276:$\mathcal W_N \subset \mathcal W_{N+1}$ (as
329:\item \emph{Virasoro specialization.} For $\mathfrak{g} = \mathfrak{sl}_2$ ($h^\vee = 2$), this gives $k' = -k-4$, and the central charges satisfy $c(k) + c(k') = 26$ exactly (by direct computation: $c(k') = 1 + 6(k+3)^2/(k+2)$, so $c(k)+c(k') = 2 + 24 = 26$), recovering the Virasoro level-shifting.
523:Nilpotent orbits are partially ordered by closure: $e = 0$ gives $\mathcal{W}^k(\fg, 0) = \widehat{\fg}_k$; $e = e_{\mathrm{prin}}$ gives $\mathcal{W}_N$ (generators of spins $d_i + 1$). For $\fg = \mathfrak{sl}_3$: $\widehat{\mathfrak{sl}}_{3,k} \supset \mathcal{W}^k(\mathfrak{sl}_3, f_{\min}) \supset \mathcal{W}_3$ (Computation~\ref{comp:sl3-ds-hierarchy}). The principal row is proved; the minimal/subregular and hook-type rows provide the leading non-principal audit corridor, with explicit local computations and a proved transport mechanism, but their full duality transport remains conditional or conjectural (Theorem~\ref{thm:hook-transport-corridor}, Conjecture~\ref{conj:bp-duality}, Conjecture~\ref{conj:type-a-transport-to-transpose}).
1167:\emph{Two distinct vanishing conditions.} The Virasoro subalgebra contribution $m_1^2(T) = \frac{c}{2} \cdot \mathbf{1}$ vanishes at $c = 0$. The full curvature of the $\mathcal{W}$-algebra bar complex (involving all generators, not just~$T$) is proportional to $(k + h^\vee)$ and vanishes at critical level $k = -h^\vee$, where the DS reduction degenerates and the $\mathcal{W}$-algebra is replaced by the Feigin--Frenkel center. These are different conditions: $c = 0$ and $k = -h^\vee$ do not coincide for $\mathcal{W}_N$ with $N \geq 3$.
 exited 2 in 52ms:
rg: regex parse error:
    (?:W_2|H_N|H_\{N\}|H_\{N-1\}|kappa\(W_N\)|kappa\(\\mathcal\{W\}_N\)|c \* \(H_N - 1\)|c \cdot \(H_N - 1\))
                                                                                           ^^
error: unrecognized escape sequence
 succeeded in 51ms:
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
  2163	\index{obstruction coefficient!general W_N@general $\mathcal{W}_N$}
  2164	
  2165	The Virasoro ($N = 2$) and $\mathcal{W}_3$ ($N = 3$) genus-1 pipelines
  2166	reveal a pattern in the obstruction coefficients: $\kappa = c/2$ and
  2167	$\kappa = c/2 + c/3 = 5c/6$ respectively, with each generator

thinking
**Inspecting theorem specifics**

I’m considering inspecting if the theorem `thm:w-algebra-koszul-main` with the special Virasoro specialization uses c + c' = 26. I’m wondering if there could be a mismatch with the free fields’ critical dimension, but probably not. I think there might be a subtle problem here. I should search for the W_2 specialization around line 2719 to get more clarity on this. It’ll help me understand what’s going on better.
codex
I have the main theorem block. Next I’m checking the chapter’s own summary tables and cross-references for second-order drift: places where `thm:wn-obstruction` may be stated correctly once and then weakened, overstated, or specialized inconsistently elsewhere in the same seam.
exec
/bin/zsh -lc "rg -n 'H_N|H_\\{N-1\\}|W_2|\\\\mathcal\\{W\\}_2|Virasoro specialization|c \\cdot \\(H_N - 1\\)|H_N - 1|sum_\\{j=1\\}\\"'^N 1/j'"' chapters/examples/landscape_census.tex chapters/connections/concordance.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2708,2850p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:vir-genus1-curvature|thm:w3-genus1-curvature|eq:B-cycle-quasi-periodicity|Theorem~\\\\ref\\{thm:genus-universality\\}|obs_1=\\\\kappa\\\\lambda_1|UNIFORM-WEIGHT|ALL-WEIGHT' chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:H_N|H_\{N-1\}|W_2|\\mathcal\{W\}_2|Virasoro specialization|c \cdot \(H_N - 1\)|H_N - 1|sum_\{j=1\}\^N 1/j)
                                                                    ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  2708	\begin{remark}[Five-theorem verification: Virasoro]
  2709	\label{rem:vir-five-theorems}
  2710	\index{main theorems!Virasoro verification}
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
 succeeded in 52ms:
chapters/examples/landscape_census.tex:34:theorem (Theorem~\ref{thm:genus-universality}), a pattern visible
chapters/examples/landscape_census.tex:50:(Theorem~\ref{thm:genus-universality};
chapters/examples/landscape_census.tex:661:(Theorem~\ref{thm:genus-universality}; );
chapters/examples/landscape_census.tex:1077:(see Theorem~\ref{thm:genus-universality}(ii)).
chapters/examples/landscape_census.tex:1195:The Faber--Pandharipande $\lambda_g$ formula (Theorem~\ref{thm:genus-universality}(iii))
chapters/examples/landscape_census.tex:1248:By Theorem~\ref{thm:genus-universality}(ii), the modular characteristic of $\mathcal{W}^k(\fg)$ is $\kappa = c \cdot \sum_{i=1}^r 1/(m_i+1)$. Since $\varrho = \kappa/c$, the ratio depends only on the exponents of~$\fg$, not on~$k$. The special values follow by direct substitution.
chapters/examples/landscape_census.tex:1258:where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
chapters/examples/landscape_census.tex:1262:Combine $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) with $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}(ii)).
chapters/examples/landscape_census.tex:1463:Theorem~\ref{thm:genus-universality} produces the $\kappa$ column.
chapters/examples/landscape_census.tex:3563:(Theorem~\ref{thm:genus-universality}), the genus-$g$ obstruction
chapters/examples/landscape_census.tex:3621:Theorem~\ref{thm:genus-universality}(iii).
chapters/examples/landscape_census.tex:3739:$\mathcal{W}_3$ (see Theorem~\ref{thm:genus-universality}(ii)
chapters/examples/landscape_census.tex:4004: (Theorem~\ref{thm:genus-universality}).
chapters/examples/free_fields.tex:2394:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/free_fields.tex:3859:(Theorem~\ref{thm:genus-universality}), but the partition
chapters/examples/free_fields.tex:4467:(Theorem~\ref{thm:genus-universality}), class~G
chapters/examples/free_fields.tex:4789:(iii)~Theorem~\ref{thm:genus-universality};
chapters/examples/w_algebras.tex:1577:\label{thm:vir-genus1-curvature}
chapters/examples/w_algebras.tex:1585:theorem (Theorem~\ref{thm:genus-universality}).
chapters/examples/w_algebras.tex:1589:The $B$-cycle quasi-periodicity~\eqref{eq:B-cycle-quasi-periodicity}

thinking
**Investigating Vir genus1 curvature**

I need to look into the Vir genus1 curvature theorem lines within w_algebras. Since the user asked about the relationship between Virasoro and w_algebras, it's possible that w_algebras includes the Virasoro genus1 theorem. I should read around thm:vir-genus1-curvature and w3-genus1-curvature. The connection might be internal to w_algebras rather than free_fields. I'll inspect around line 1577 and see what I find there.
codex
The Virasoro genus-1 theorem is also restated inside `w_algebras.tex`, so I’m checking both seams now: `free_fields.tex` → `w_algebras.tex`, and the internal Virasoro → `\mathcal W_N` transition within `w_algebras.tex` itself. That’s where second-order drift usually hides.
exec
/bin/zsh -lc "rg -n 'H_\\{N-1\\}|H_N|W_2|\\\\mathcal\\{W\\}_2|c \\cdot \\(H_N - 1\\)|sum_\\{j=1\\}\\"'^N 1/j|sum_'"\\{s=2\\}\\"'^N 1/s'"' chapters/examples/landscape_census.tex chapters/connections/concordance.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1558,1732p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'W_2|\\\\mathcal\\{W\\}_2|H_N|H_\\{N-1\\}|Virasoro|obstruction coefficient|kappa\\(\\\\mathcal\\{W\\}_N\\)' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1936,2015p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:H_\{N-1\}|H_N|W_2|\\mathcal\{W\}_2|c \cdot \(H_N - 1\)|sum_\{j=1\}\^N 1/j|sum_\{s=2\}\^N 1/s)
                                            ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  1558	genus~1 promotes this scalar curvature to a cohomology class on
  1559	$\overline{\mathcal{M}}_{1,1}$.
  1560	
  1561	\subsubsection{Genus-1 bar complex}
  1562	
  1563	The genus-1 bar complex is:
  1564	\begin{equation}\label{eq:vir-genus1-bar}
  1565	\barB^{(1),n}(\mathrm{Vir}_c) = \Gamma\bigl(\overline{C}_n(E_\tau),\;
  1566	 \omega_{E_\tau}^{\otimes 2n} \otimes \Omega^n_{\log}\bigr)
  1567	\end{equation}
  1568	where the exponent $2n$ reflects the conformal weight $h_T = 2$ of the
  1569	generator (each copy of $T$ contributes weight~$2$ to the tensor product).
  1570	The genus-1 propagator is~\eqref{eq:genus1-propagator}
  1571	and the differential is~\eqref{eq:genus1-diff}, with the OPE data of the
  1572	Virasoro algebra replacing that of $\widehat{\mathfrak{sl}}_2$.
  1573	
  1574	\subsubsection{Curvature theorem}
  1575	
  1576	\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere]
  1577	\label{thm:vir-genus1-curvature}
 succeeded in 50ms:
  1936	where the exponents $2n_T$ and $3n_W$ reflect the conformal weights
  1937	$h_T = 2$ and $h_W = 3$ of the respective generators.
  1938	
  1939	\subsubsection{Curvature theorem}
  1940	
  1941	\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3}; \ClaimStatusProvedHere]
  1942	\label{thm:w3-genus1-curvature}
  1943	The genus-1 differential satisfies:
  1944	\begin{equation}\label{eq:w3-genus1-dsquared}
  1945	(d^{(1)})^2 = \frac{5c}{6} \cdot \omega_1 \cdot \operatorname{id}
  1946	\end{equation}
  1947	where $\omega_1 \in H^2(\overline{\mathcal{M}}_{1,1})$ is the fundamental
  1948	class. Equivalently, the genus-1 obstruction coefficient is
  1949	$\kappa(\mathcal{W}_3^k) = 5c/6$, in agreement with the genus universality
  1950	theorem (Theorem~\ref{thm:genus-universality}).
  1951	\end{theorem}
  1952	
  1953	\begin{proof}
  1954	The $B$-cycle quasi-periodicity~\eqref{eq:B-cycle-quasi-periodicity}
  1955	shifts the propagator by $-2\pi i$. Applying $(d^{(1)})^2$ to the
 succeeded in 54ms:
9:$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
22:forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
48:obstruction coefficient $\kappa(\cA)$ from the genus universality
531:($h = 1$) gives $z^{-1}$; the Virasoro ($h = 2$) gives $z^{-3}$;
561:(Virasoro, $\cW_N$, $r_{\max} = \infty$), the degree-$3$ MC
726:The Virasoro discriminant complementarity is
730:$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
732:The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
735:sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
740:In the Virasoro row, the displayed partner $\mathrm{Vir}_{26-c}$ is
838:the full algebra, not the Virasoro subalgebra alone. For the
843:weight-$1$ contributions, and the Virasoro sector alone determines
1043: (Kac--Moody and Virasoro at all genera):
1047: proved unconditionally for Kac--Moody and Virasoro
1068: The Virasoro-based invariants ($c$, $\kappa$) are not defined.
1078:\textsuperscript{$\ddagger$}For the Virasoro row, the involution
1090:generator $T$ of weight~$2$ ($\dim V_1^\natural = 0$), so the Virasoro
1091:subalgebra determines~$\kappa$. The Koszul dual listed is the Virasoro-sector
1095:The complementarity sum $c + c' = 26$ is the Virasoro-sector value.
1232:The ratio $\varrho(\mathrm{Vir}_c) = 1/2$ means that half the conformal anomaly is absorbed by the nonlinearity of the Virasoro OPE. For $\widehat{\mathfrak{sl}}_{2}$ at level~$k$, $\varrho = (k{+}2)^2/(4k) \sim k/4$ as $k \to \infty$ (linearly divergent) and also diverges at $k \to 0$. The genus-$g$ free energy $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ carries the modular

thinking
**Inspecting landscape formulas**

I need to take a closer look at the lines in the landscape that pertain to the formulas. I think I should focus on the areas around lines 730 and 1416 specifically. The context of those lines is likely key to understanding how they relate to the formulas I'm looking at. I'll dive into those sections to ensure I fully grasp what's happening!
codex
I’ve isolated the live formula witnesses in `w_algebras.tex` and `landscape_census.tex`. Now I’m checking for two kinds of seam failures: a true contradiction, or a local proof/statement that only works because it silently changes what “Virasoro”, “\mathcal W_2”, or “H_N” means between sections.
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1408,1422p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '724,742p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '41,75p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2262,2303p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
  1419	
  1420	\emph{$\Eone$-Chiral Algebras (Nonlocal Vertex Algebras).}
  1421	\begin{enumerate}[label=(\roman*)]
  1422	\item Lattice algebras with non-symmetric cocycles: first strictly $\Eone$ examples;
 succeeded in 51ms:
   724	Both two-generator free-field systems share the same stratum separation
   725	mechanism and class~C shadow depth.
   726	The Virasoro discriminant complementarity is
   727	$\Delta(c) + \Delta(26{-}c) = 6960/[(5c{+}22)(152{-}5c)]$
   728	(Corollary~\ref{cor:discriminant-atlas}(ii)).
   729	The Koszul conductor for $\mathcal{W}_N$ is
   730	$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
   731	$K_2 = 26$, $K_3 = 100$, $K_4 = 246$, $K_5 = 488$.
   732	The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
   733	$c^* = 50$ for $\mathcal{W}_3$, $c^* = 123$ for $\mathcal{W}_4$.
   734	${}^\S$For the Monster module $V^\natural$: the complementarity
   735	sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
   736	($\kappa(V^\natural) = 12$, $\kappa(\mathrm{Vir}_2) = 1$; sum $= 13$),
   737	since $\dim V_1^\natural = 0$ forces $\kappa = c/2 = 12$
   738	.
   739	
   740	In the Virasoro row, the displayed partner $\mathrm{Vir}_{26-c}$ is
   741	the proved M/S-level same-family shadow used in the complementarity
   742	and semi-infinite calculations. The stronger H-level
 succeeded in 50ms:
  2262	
  2263	\emph{Verification.}
  2264	\begin{itemize}
  2265	\item $N = 2$: $\kappa = c \cdot (1/2) = c/2$. \checkmark
  2266	 (Theorem~\ref{thm:vir-genus1-curvature})
  2267	\item $N = 3$: $\kappa = c \cdot (1/2 + 1/3) = 5c/6$. \checkmark
  2268	 (Theorem~\ref{thm:w3-genus1-curvature})
  2269	\item $N = 4$: $\kappa = c \cdot (H_4 - 1) = 13c/12$.
  2270	 Three channels $(\kappa_2, \kappa_3, \kappa_4) = (c/2, c/3, c/4)$
  2271	 with $\kappa_2 + \kappa_3 + \kappa_4 = 13c/12$.
  2272	 Complementarity: $c + c' = 246$, $\kappa + \kappa' = 13 \cdot 246/12$.
  2273	\item $N = 5$: $\kappa = c \cdot (H_5 - 1) = 77c/60$.
  2274	 Four channels $(\kappa_2, \kappa_3, \kappa_4, \kappa_5) = (c/2, c/3, c/4, c/5)$
  2275	 with $\sum_j \kappa_j = 77c/60$.
  2276	 Complementarity: $c + c' = 488$, $\kappa + \kappa' = 77 \cdot 488/60$.
  2277	\item $N \to \infty$: $\kappa \sim c \cdot \ln N$, reflecting the
  2278	 logarithmic growth of the harmonic series. The obstruction
  2279	 grows without bound with the rank, consistent with the
  2280	 increasingly complex OPE structure of higher $\mathcal{W}$-algebras.
  2281	\end{itemize}
 succeeded in 51ms:
    41	Chapter~\ref{chap:kac-moody-koszul}.
    42	
    43	\index{W-algebra@$\mathcal{W}$-algebra!as modular Koszul family}
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

thinking
**Investigating theorem consistency**

I need to inspect the theorem around central-charge complementarity to ensure the formula is correct. It seems there could be an issue when N=2, but the formula gives c+c'=26, which checks out with my calculations. For N=3, it's 100, which seems fine. I should exhaustively search for inconsistencies or gaps. I'll check on free fields or w-algebras for H_N definitions to see if they're inconsistent or if there's an issue with the W_2 relation.
exec
/bin/zsh -lc "rg -n 'H_N' chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/examples/free_fields.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'W_2|\\\\mathcal\\{W\\}_2|\\\\cW_2|= \\\\mathrm\\{Vir\\}|= \\\\Vir|Virasoro is the .*N=2|N = 2.*Virasoro' chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/landscape_census.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'H_\\{N-1\\}|H_{N-1}' chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/examples/free_fields.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'c/2|5c/6|13/12|77c/60|1/2 \\+ 1/3 \\+ 1/4|1/2 \\+ 1/3' chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/concordance.tex:9613: $\kappa(\Walg_N) = c(H_N{-}1)$ \\
chapters/examples/landscape_census.tex:730:$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
chapters/examples/landscape_census.tex:1258:where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
chapters/examples/landscape_census.tex:1416:General $\mathcal{W}_N$: $\kappa = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2179:= c \cdot (H_N - 1)
chapters/examples/w_algebras.tex:2182:$H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number.
chapters/examples/w_algebras.tex:2237:= c \cdot (H_N - 1)
chapters/examples/w_algebras.tex:2246:(d^{(1)})^2 = c \cdot (H_N - 1) \cdot \omega_1 \cdot \operatorname{id}
chapters/examples/w_algebras.tex:2250:$\kappa = c \cdot (H_N - 1)$. This is consistent with the
chapters/examples/w_algebras.tex:2289:= (H_N - 1) \cdot (c + c')
chapters/examples/w_algebras.tex:2290:= (H_N - 1) \cdot 2(N{-}1)(2N^2{+}2N{+}1)
chapters/examples/w_algebras.tex:2298:Since $\kappa = c \cdot (H_N - 1)$ and $\kappa' = c' \cdot (H_N - 1)$:
chapters/examples/w_algebras.tex:2299:$\kappa + \kappa' = (H_N - 1)(c + c')$.
chapters/examples/w_algebras.tex:2345:For $\mathfrak{g} = \mathfrak{sl}_N$ (exponents $1, 2, \ldots, N-1$), $\varrho = H_N - 1$, recovering Theorem~\ref{thm:wn-obstruction}. The non-monotonicity in rank (e.g., $\varrho(E_8) < \varrho(E_6)$) reflects the spacing of the exponents: $E_8$ has large exponents ($29, 23, \ldots$) giving small $1/(m_i + 1)$ contributions. The isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) gives identical exponents and anomaly ratios; both have $h^\vee = 3$ (not $h = 4$), and the level shift $k' = -k - 2h^\vee = -k - 6$ uses the dual Coxeter number. Among the non-simply-laced types, $G_2$ has the lowest anomaly ratio ($2/3$) and $F_4$ the highest ($7/8$); both are less than $1$, so the associated $\mathcal{W}$-algebra shadow obstruction towers converge.
chapters/examples/w_algebras.tex:2624:$\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2626:$H_N = 1 + 1/2 + \cdots + 1/N$\textup{)}.
chapters/examples/w_algebras.tex:2836:\item $\kappa(\mathcal{W}_N^k) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2838: where $H_N = \sum_{j=1}^N 1/j$. At genus $1$: unconditional.
chapters/examples/w_algebras.tex:4474:$\kappa(\mathcal{W}_N^k) = c(\mathcal{W}_N^k) \cdot (H_N - 1)$,
 exited 2 in 51ms:
rg: regex parse error:
    (?:H_\{N-1\}|H_{N-1})
                    ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
chapters/examples/landscape_census.tex:1092:partner $\mathrm{Vir}_{26-c} = \mathrm{Vir}_2$;
chapters/connections/concordance.tex:10072: vanishing if and only if $N = 2$ (Virasoro: uniform-weight).
chapters/examples/free_fields.tex:4559:$\cA_{\mathrm{tot}} = \mathrm{Vir}_{26} \otimes bc$ is
chapters/examples/w_algebras.tex:264:h_K(\mathcal W_2) \approx 0.567
chapters/examples/w_algebras.tex:410:\emph{(iii) $\mathfrak{sl}_2$ reduction.} For $\mathfrak{g} = \mathfrak{sl}_2$ with $h^\vee = 2$: $\mathcal{W}^k(\mathfrak{sl}_2) = \mathrm{Vir}_{c(k)}$ with $c(k) = 1 - 6(k+1)^2/(k+2)$. The dual level $k' = -k-4$ gives $c(k') = 1 - 6(-k-3)^2/(-k-2) = 1 + 6(k+3)^2/(k+2)$. Then $c(k) + c(k') = 2 + 6[-(k+1)^2 + (k+3)^2]/(k+2) = 2 + 6 \cdot 4(k+2)/(k+2) = 2 + 24 = 26$. The Virasoro algebra at $c = 0$ is \emph{quadratic} self-dual ($\mathrm{Vir}_0^{!_{\mathrm{quad}}} \simeq \mathrm{Vir}_0$, Theorem~\ref{thm:virasoro-self-duality}); this is a property of the uncurved OPE at $c=0$, not of the FF level-shifting involution (which sends $c=0$ to $c=26$). \checkmark
chapters/examples/w_algebras.tex:1709:$\cA = \mathrm{Vir}_c$ with $\cA^! = \mathrm{Vir}_{26-c}$
chapters/examples/w_algebras.tex:2254:For $N = 2$ (Virasoro, uniform weight), the factorization
chapters/examples/w_algebras.tex:2704:the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
chapters/examples/w_algebras.tex:2912:For $\mathcal{W}^k(\mathfrak{sl}_2) = \mathrm{Vir}_{c(k)}$
chapters/examples/w_algebras.tex:3496:$\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$, the sum $\kappa + \kappa'$
chapters/examples/w_algebras.tex:6398:For $N = 2$ (Virasoro), the PVA has generator-degree~$1$ in the
 succeeded in 52ms:
chapters/examples/free_fields.tex:83:$\kappa(\beta\gamma) = c/2$ is generically nonzero). Both
chapters/examples/free_fields.tex:174:Modular characteristic $\kappa(\mathcal{F}) = c/2 = 1/4$.
chapters/examples/free_fields.tex:230: $\kappa(\mathcal{F}) = c/2 = 1/4$.
chapters/examples/free_fields.tex:259:Then $\kappa = c/2 = 1/4$ by the universal formula
chapters/examples/free_fields.tex:669:($\kappa = c/2$ in every case; see landscape census
chapters/examples/free_fields.tex:706:Modular characteristic $\kappa(\beta\gamma) = c/2 = 6\lambda^2 - 6\lambda + 1$,
chapters/examples/free_fields.tex:1137:at central charge $c = c_{\beta\gamma}(\lambda)$: $S_2 = \kappa = c/2$,
chapters/examples/free_fields.tex:1267:(using $\kappa = c/2$). The denominator $5c + 22 = 60\lambda^2 - 60\lambda + 32$
chapters/examples/free_fields.tex:2394:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/free_fields.tex:3871:\textbf{Modular characteristic} & $\kappa(\cF) = c/2 = 1/4$ \\
chapters/examples/free_fields.tex:3999:$\mathrm{Tr}_{H_{\alpha}}\bigl((-1)^{\beta F}\, q^{L_0 - c/24}\bigr)$,
chapters/examples/free_fields.tex:4121:theorem applied to $\kappa(\cF) = c/2 = 1/4$:
chapters/examples/free_fields.tex:4259:$T(z)T(w)$, which is $c/2$), while spin structures are
chapters/examples/free_fields.tex:4502:T(z)T(w) = \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} + \text{regular}
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/free_fields.tex:4609:$d_{\mathrm{equiv}}^2 = (c/2 - 13)\,\kappa_1$ obstructs the critical
chapters/examples/free_fields.tex:4928:\item \emph{Modular invariance.} The partition function $Z(\tau) = \operatorname{tr}_{\mathcal{H}} q^{L_0 - c/24}$ is invariant under $\mathrm{SL}_2(\mathbb{Z})$.
chapters/examples/free_fields.tex:4937:\emph{(1) Anomaly cancellation:} The integrand on $\overline{\mathcal{M}}_{g,n}$ involves $\det(\operatorname{Im} \Omega)^{-c/2}$; for the Belavin--Knizhnik anomaly to cancel, $c_{\mathrm{total}} = 0$. Hence $c_{\mathrm{matter}} = 26$ (bosonic, $c_{\mathrm{ghost}} = -26$) or $c_{\mathrm{matter}} = 15$ (super, $c_{\mathrm{ghost}} = -15$).
chapters/examples/free_fields.tex:5025:$m_0 = c/24N$.
chapters/examples/free_fields.tex:5090:$\det(\mathrm{Im}\,\Omega)^{-c/2}$.

thinking
**Evaluating theorem clarity**

I need to add a sentence after the equation or theorem remark to clarify: "For N=2, H_2=3/2, so \mathcal W_2=\mathrm{Vir}_c and \kappa(\mathcal W_2)=c/2." I want to make sure this information isn't lost in the proof verification. It could be a low-severity gap if the user wants more robust clarity. I’ll also check for any discrepancies in notation regarding Virasoro and other uses in the table. Let me inspect the relevant lines in `concordance.tex`.
codex
I found one actual coefficient mismatch already on the Virasoro side: the same obstruction is written once with `c-26` and elsewhere as `c/2-13` while the theorem itself identifies the class `\mu` with `\kappa_1`. I’m checking whether that is isolated or whether the same factor-of-2 drift contaminates the `\mathcal W_N` transition surfaces too.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '9606,9618p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'H_N - 1|sum_\\{j=1\\}\\"'^N 1/j|1/2 '"\\+ 1/3 \\+ 1/4|13c/12|77c/60|W_4|W_5' chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'c-26|c - 26|c/2 - 13|13 - c/2|kappa\\(\\\\mathrm\\{Vir\\}_c\\)|kappa\\(\\\\mathrm\\{Vir\\}_\\{26-c\\}\\)|W_2|\\\\mathcal\\{W\\}_2' chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/landscape_census.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/concordance.tex:5874: $1-\dfrac{c-26}{2}\,x$ & $1$ \\[6pt]
chapters/connections/concordance.tex:8739:$\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$
chapters/connections/concordance.tex:9612: $\kappa(\mathrm{Vir}_c) = c/2$,
chapters/examples/landscape_census.tex:33:and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
chapters/examples/free_fields.tex:4522:d_{\mathrm{equiv}}^2 = (c - 26)\,\mu,
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/free_fields.tex:4609:$d_{\mathrm{equiv}}^2 = (c/2 - 13)\,\kappa_1$ obstructs the critical
chapters/examples/w_algebras.tex:264:h_K(\mathcal W_2) \approx 0.567
chapters/examples/w_algebras.tex:1584:$\kappa(\mathrm{Vir}_c) = c/2$, in agreement with the genus universality
chapters/examples/w_algebras.tex:1721:The dual $\mathrm{Vir}_{26-c}$ has curvature $(26-c)/2 = 13 - c/2$, so
chapters/examples/w_algebras.tex:1722:its raw obstruction coefficient is $(13 - c/2) \in H^0(\overline{\mathcal{M}}_{1,1})$.
chapters/examples/w_algebras.tex:2704:the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
chapters/examples/w_algebras.tex:2743: $\kappa(\mathrm{Vir}_c) = c/2$, anomaly ratio $\varrho = 1/2$.
chapters/examples/w_algebras.tex:3477:\item $\kappa(\mathrm{Vir}_c) = c/2$
chapters/examples/w_algebras.tex:3489:\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c})
chapters/examples/w_algebras.tex:4734:$\kappa(\mathrm{Vir}_c) = c/2$.
 succeeded in 51ms:
  9606	 cubic coefficient $\alpha = S_3/\kappa$ universal per family:
  9607	 $\alpha = 0$ \textup{(}Heis\textup{)},
  9608	 $\alpha = 2$ \textup{(}Vir\textup{)},
  9609	 family-specific for $\Walg_N$ and affine KM \\
  9610	& $\kappa$ formula universality: $\kappa(\cH_k) = k$,
  9611	 $\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$,
  9612	 $\kappa(\mathrm{Vir}_c) = c/2$,
  9613	 $\kappa(\Walg_N) = c(H_N{-}1)$ \\
  9614	& $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for
  9615	 uniform-weight modular Koszul algebras at all genera
  9616	 \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
  9617	& Swiss-cheese theorem
  9618	 \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\
 succeeded in 50ms:
chapters/connections/concordance.tex:3113:$\delta_{\mathrm{mix}}$ for six families ($\cW_3$, $\cW_4$, $\cW_5$,
chapters/connections/concordance.tex:3115:$V(\mathfrak{sl}_2){+}V(\mathfrak{sl}_3)$); $\cW_4$ is never
chapters/examples/w_algebras.tex:268:h_K(\mathcal W_4) \approx 0.815
chapters/examples/w_algebras.tex:2179:= c \cdot (H_N - 1)
chapters/examples/w_algebras.tex:2182:$H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number.
chapters/examples/w_algebras.tex:2237:= c \cdot (H_N - 1)
chapters/examples/w_algebras.tex:2246:(d^{(1)})^2 = c \cdot (H_N - 1) \cdot \omega_1 \cdot \operatorname{id}
chapters/examples/w_algebras.tex:2250:$\kappa = c \cdot (H_N - 1)$. This is consistent with the
chapters/examples/w_algebras.tex:2269:\item $N = 4$: $\kappa = c \cdot (H_4 - 1) = 13c/12$.
chapters/examples/w_algebras.tex:2271: with $\kappa_2 + \kappa_3 + \kappa_4 = 13c/12$.
chapters/examples/w_algebras.tex:2273:\item $N = 5$: $\kappa = c \cdot (H_5 - 1) = 77c/60$.
chapters/examples/w_algebras.tex:2275: with $\sum_j \kappa_j = 77c/60$.
chapters/examples/w_algebras.tex:2289:= (H_N - 1) \cdot (c + c')
chapters/examples/w_algebras.tex:2290:= (H_N - 1) \cdot 2(N{-}1)(2N^2{+}2N{+}1)
chapters/examples/w_algebras.tex:2298:Since $\kappa = c \cdot (H_N - 1)$ and $\kappa' = c' \cdot (H_N - 1)$:
chapters/examples/w_algebras.tex:2299:$\kappa + \kappa' = (H_N - 1)(c + c')$.
chapters/examples/w_algebras.tex:2345:For $\mathfrak{g} = \mathfrak{sl}_N$ (exponents $1, 2, \ldots, N-1$), $\varrho = H_N - 1$, recovering Theorem~\ref{thm:wn-obstruction}. The non-monotonicity in rank (e.g., $\varrho(E_8) < \varrho(E_6)$) reflects the spacing of the exponents: $E_8$ has large exponents ($29, 23, \ldots$) giving small $1/(m_i + 1)$ contributions. The isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) gives identical exponents and anomaly ratios; both have $h^\vee = 3$ (not $h = 4$), and the level shift $k' = -k - 2h^\vee = -k - 6$ uses the dual Coxeter number. Among the non-simply-laced types, $G_2$ has the lowest anomaly ratio ($2/3$) and $F_4$ the highest ($7/8$); both are less than $1$, so the associated $\mathcal{W}$-algebra shadow obstruction towers converge.
chapters/examples/w_algebras.tex:2624:$\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2836:\item $\kappa(\mathcal{W}_N^k) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2838: where $H_N = \sum_{j=1}^N 1/j$. At genus $1$: unconditional.
codex
I’m checking whether the factor-of-two drift is already encoded in the concordance tables. If the constitution itself is mixed, that upgrades the severity; if not, it isolates the defect to the Virasoro chapter surface.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '400,420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5868,5878p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3470,3496p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2698,2708p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   412	The level-independence of $c(k) + c(k') = 26$ is an instance of the
   413	general pattern: for $\mathfrak{g} = \mathfrak{sl}_N$, the
   414	Freudenthal--de~Vries identity gives
   415	$c(\mathcal{W}^k) + c(\mathcal{W}^{k'})
   416	= 2(N{-}1)(2N^2{+}2N{+}1)$,
   417	independent of $k$.
   418	
   419	\end{proof}
 succeeded in 51ms:
  5868	\textbf{Family} & $\Delta_\cA(x)$ & rank \\
  5869	\hline
  5870	$\cH_k$ & $1-kx$ & $1$ \\[2pt]
  5871	$\widehat{\mathfrak{sl}}_2{}_k$ &
  5872	 $\dfrac{(1-kx)(1-(k{+}4)x)}{1-2x}$ & $2$ \\[6pt]
  5873	$\mathrm{Vir}_c$ &
  5874	 $1-\dfrac{c-26}{2}\,x$ & $1$ \\[6pt]
  5875	$\mathcal W_3{}_c$ &
  5876	 $\bigl(1-\dfrac{c-50}{2}\,x\bigr)
  5877	 \bigl(1-\bigl(\dfrac{c-50}{2}+\dfrac{48}{5c+22}\bigr)x\bigr)$
  5878	 & $2$ \\[6pt]
 succeeded in 51ms:
  3470	
  3471	\begin{remark}[Bar curvature and gravitational phase space]
  3472	\label{rem:bar-curvature-gravitational-symplectic}
  3473	\index{bar complex!gravitational symplectic form}
  3474	\index{moduli space!gravitational phase space}
  3475	Three identifications connect the bar complex to 3d gravity:
  3476	\begin{enumerate}[label=(\roman*)]
  3477	\item $\kappa(\mathrm{Vir}_c) = c/2$
  3478	 (Theorem~\ref{thm:modular-characteristic}) is the central charge
  3479	 of the gravity theory on $T^*\mathcal{T}_g$.
  3480	\item $\overline{\mathcal{M}}_g$ is the reduced phase space.
  3481	\item The curvature identity
  3482	 $d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$
  3483	 (Theorem~\ref{thm:genus1-universal-curvature}) says the bar
  3484	 differential fails to square to zero by the symplectic form,
  3485	 weighted by the central charge.
  3486	\end{enumerate}
  3487	The Koszul complementarity sum is
  3488	\[
  3489	\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c})
 succeeded in 52ms:
  2698	
  2699	\section{The five theorems for $\mathcal{W}$-algebras}
  2700	\label{sec:w-five-theorems}
  2701	
  2702	The five main theorems of Part~\ref{part:bar-complex} specialize to $\mathcal{W}$-algebras
  2703	through DS reduction from the affine Kac--Moody package. We record
  2704	the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
  2705	$\mathcal{W}_3$ in a verification table, then state the general
  2706	$\mathcal{W}_N$ pattern.
  2707	
  2708	\begin{remark}[Five-theorem verification: Virasoro]


thinking
**Inspecting theorems and values**

I need to check the theorem registry for the status of `thm:wn-obstruction`. It seems like it's probably been proven. I should also look for any seam mismatches, searching for `W_2` and noting that maybe `h_K(\mathcal W_2)` is approximately 0.567. It might be important to match those values with Vir. I think I might need to compute `h_K W_2`, which I suspect is around 0.
thinking
**Investigating Vir values**

I’m pondering whether the Vir value shows up elsewhere, and although I considered searching, it wasn’t part of the request. I think there might be an issue in the `landscape_census.tex` file, particularly at row or note indicating `Vir_{26-c} = Vir_2` at line 1092. I need to inspect those lines — it’s possible there’s something strange with c=2. So, I'll open up lines 1088 to 1094 to take a closer look.
codex
I’m sanity-checking the census bridge too. The seam can look locally consistent while the canonical census encodes a different specialization or partner convention, and that would still be a real failure surface.
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1086,1096p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'central charge of the gravity theory|weighted by the central charge|kappa\\(\\\\mathrm\\{Vir\\}_c\\) = c/2.*central charge|kappa\\(\\\\mathrm\\{Vir\\}_c\\).*weighted by the central charge' chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Adjunction\\)|Bar-cobar adjunction|Virasoro specialization.*Theorem A|five main theorems.*specialize|\\\\textbf\\{A\\} \\(Adjunction\\)' chapters/examples/w_algebras.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1086	The complementarity sum $c + c'$ is not defined in the
  1087	Feigin--Frenkel sense (no level shift); self-duality gives
  1088	$\kappa' = \kappa = 24$, so $\kappa + \kappa' = 48$.
  1089	\textsuperscript{$\S$}The Monster module $V^\natural$ has a single strong
  1090	generator $T$ of weight~$2$ ($\dim V_1^\natural = 0$), so the Virasoro
  1091	subalgebra determines~$\kappa$. The Koszul dual listed is the Virasoro-sector
  1092	partner $\mathrm{Vir}_{26-c} = \mathrm{Vir}_2$;
  1093	the full Koszul dual of $V^\natural$ as a VOA involves the
  1094	weight-$2$ Griess algebra and is not a standard-family object.
  1095	The complementarity sum $c + c' = 26$ is the Virasoro-sector value.
  1096	
 succeeded in 52ms:
chapters/examples/w_algebras.tex:3485: weighted by the central charge.
 succeeded in 52ms:
chapters/examples/w_algebras.tex:2702:The five main theorems of Part~\ref{part:bar-complex} specialize to $\mathcal{W}$-algebras
chapters/examples/w_algebras.tex:2721:\textbf{A} (Adjunction) &
chapters/examples/w_algebras.tex:2774:\textbf{A} (Adjunction) &
chapters/connections/concordance.tex:31:\textbf{A} & Bar-cobar adjunction


thinking
**Identifying inconsistencies in labeling**

I noticed there's a label issue in line 2721 calling it theorem A, which might confuse the user regarding the seam audit. This relates to the transition summary that verifies five theorems for Vir vs W3. Since it connects W_2 to W_N, it’s essential to clarify what theorem A refers to. The user's focus is on the seam between virasoro.tex and w_algebras.tex, which might not directly involve seams in w_algebras. I need to suggest a proper fix: possibly renaming or correcting the content of the row labeled incorrectly.
thinking
**Clarifying theorem inconsistencies**

In the concordance, I found Theorem A should represent the bar-cobar adjunction, but there's a mismatch since row A’s content discusses duality instead. To fix this, I think row A should clearly state `\barBch \dashv \Omegach` specialized to Vir/W3, or I could rename it to `A' (Koszul duality)`, since it's not one of the five main theorems. It might be better to replace row A’s content with the correct bar-cobar adjunction specialization and move any related details to row B. I need to verify if there's already a theorem about adjunction.
codex
I’ve now got three distinct classes of seam failures on the table: one real formula mismatch on the Virasoro side, one theorem-label drift in the W-algebra summary, and one local `\kappa`/central-charge conflation. I’m doing one more pass for hidden off-by-one drift (`H_{N-1}` or `{2,\dots,N+1}` style errors) before I lock the findings.
exec
/bin/zsh -lc "rg -n 'N\\+1|\\{2, \\.\\.\\., N\\+1\\}|2, 3, \\.\\.\\., N\\+1|H_\\{N-1\\}|H_N-1|H_N \\- 1|sum_\\{s=2\\}\\"'^N'"' chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/examples/free_fields.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/free_fields.tex:2674:\item \emph{W-algebras.} At critical level, the external quantum-Langlands picture relates $\mathcal{W}^{-h^\vee}(\mathfrak{g}, f)$ to a Langlands-dual $\mathcal{W}$-algebra, while the manuscript-internal proved statement is the critical fixed-point inversion package for the principal algebra. At general central charge: $\mathcal{W}_N^c \leftrightarrow \mathcal{W}_N^{c'}$ with $c + c' = 2(N-1)(2N^2+2N+1)$.
chapters/examples/landscape_census.tex:730:$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
chapters/examples/landscape_census.tex:1258:where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
chapters/examples/landscape_census.tex:1305:The \emph{Koszul conductor} $K = c(\cA) + c(\cA^!)$ (Theorem~\ref{thm:central-charge-complementarity}) admits a closed-form expression for the $\mathcal{W}_N$ series. Using the Drinfeld--Sokolov central charge $c(k) = (N-1)(1 - N(N+1)(k+N)^{-1}(k'+N)^{-1})$ and the Freudenthal--de Vries formula $c + c' = 2r + 4h^\vee d$ with $r = N-1$, $h^\vee = N$, $d = N^2-1$:
chapters/examples/landscape_census.tex:1309:The first values are: $K_2 = 26$, $K_3 = 100$, $K_4 = 246$, $K_5 = 488$. In general $K_N = 4N^3 - 2N - 2$ (equivalently $K_N = 2(N-1)(2N^2+2N+1)$).
chapters/examples/landscape_census.tex:1361:For non-simply-laced types, the dual Coxeter number $h^\vee$ governs the kappa formula and level-shifting duality $k \mapsto -k - 2h^\vee$. The Coxeter number $h$ appears in the Strange Formula $\lvert\rho\rvert^2 = dh/12$ and in the exponent sum $\sum m_i = rh/2$, but \emph{not} in the Feigin--Frenkel involution or the curvature formula. The low-rank isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) produces identical entries: both have $d = 10$, $h^\vee = 3$, and the same kappa formula. For $N \geq 3$, types $B_N$ and $C_N$ are genuinely distinct: they share $d = N(2N+1)$ and $h = 2N$, but $h^\vee(B_N) = 2N-1$ while $h^\vee(C_N) = N+1$, so their kappa formulas and level-shifting dualities diverge.
chapters/examples/landscape_census.tex:1416:General $\mathcal{W}_N$: $\kappa = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:276:$\mathcal W_N \subset \mathcal W_{N+1}$ (as
chapters/examples/w_algebras.tex:277:$\mathfrak{sl}_N \subset \mathfrak{sl}_{N+1}$) and the
chapters/examples/w_algebras.tex:2179:= c \cdot (H_N - 1)
chapters/examples/w_algebras.tex:2237:= c \cdot (H_N - 1)
chapters/examples/w_algebras.tex:2246:(d^{(1)})^2 = c \cdot (H_N - 1) \cdot \omega_1 \cdot \operatorname{id}
chapters/examples/w_algebras.tex:2250:$\kappa = c \cdot (H_N - 1)$. This is consistent with the
chapters/examples/w_algebras.tex:2289:= (H_N - 1) \cdot (c + c')
chapters/examples/w_algebras.tex:2290:= (H_N - 1) \cdot 2(N{-}1)(2N^2{+}2N{+}1)
chapters/examples/w_algebras.tex:2298:Since $\kappa = c \cdot (H_N - 1)$ and $\kappa' = c' \cdot (H_N - 1)$:
chapters/examples/w_algebras.tex:2299:$\kappa + \kappa' = (H_N - 1)(c + c')$.
chapters/examples/w_algebras.tex:2345:For $\mathfrak{g} = \mathfrak{sl}_N$ (exponents $1, 2, \ldots, N-1$), $\varrho = H_N - 1$, recovering Theorem~\ref{thm:wn-obstruction}. The non-monotonicity in rank (e.g., $\varrho(E_8) < \varrho(E_6)$) reflects the spacing of the exponents: $E_8$ has large exponents ($29, 23, \ldots$) giving small $1/(m_i + 1)$ contributions. The isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) gives identical exponents and anomaly ratios; both have $h^\vee = 3$ (not $h = 4$), and the level shift $k' = -k - 2h^\vee = -k - 6$ uses the dual Coxeter number. Among the non-simply-laced types, $G_2$ has the lowest anomaly ratio ($2/3$) and $F_4$ the highest ($7/8$); both are less than $1$, so the associated $\mathcal{W}$-algebra shadow obstruction towers converge.
chapters/examples/w_algebras.tex:2624:$\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2836:\item $\kappa(\mathcal{W}_N^k) = c \cdot (H_N - 1)$
exec
/bin/zsh -lc "rg -n 'weighted by the central charge|central charge of the gravity theory|modular characteristic|anomaly ratio' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3475,3486p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1207:\emph{(B) At General Level.} For $f = f_{\mathrm{prin}}$ and $k \neq -h^\vee$, the Koszul dual has the same modular characteristic as the W-algebra at the shifted level (Theorem~\ref{thm:w-algebra-koszul-main}):
2345:For $\mathfrak{g} = \mathfrak{sl}_N$ (exponents $1, 2, \ldots, N-1$), $\varrho = H_N - 1$, recovering Theorem~\ref{thm:wn-obstruction}. The non-monotonicity in rank (e.g., $\varrho(E_8) < \varrho(E_6)$) reflects the spacing of the exponents: $E_8$ has large exponents ($29, 23, \ldots$) giving small $1/(m_i + 1)$ contributions. The isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) gives identical exponents and anomaly ratios; both have $h^\vee = 3$ (not $h = 4$), and the level shift $k' = -k - 2h^\vee = -k - 6$ uses the dual Coxeter number. Among the non-simply-laced types, $G_2$ has the lowest anomaly ratio ($2/3$) and $F_4$ the highest ($7/8$); both are less than $1$, so the associated $\mathcal{W}$-algebra shadow obstruction towers converge.
2623:The modular characteristic is
2687:In the shadow obstruction tower: S-duality maps the modular characteristic
2743: $\kappa(\mathrm{Vir}_c) = c/2$, anomaly ratio $\varrho = 1/2$.
2799: anomaly ratio $\varrho(\mathfrak{sl}_3) = 1/2 + 1/3 = 5/6$
3485: weighted by the central charge.
7062:Here $\rho_{[3]} = 1/2 + 1/3 = 5/6$ is the principal anomaly ratio
7073:indicates that the anomaly ratio formulation does not apply to affine
7086:The anomaly ratio $\rho_{[2,1]}$ is computed from the generator
7149:where $\rho_\lambda$ is the anomaly ratio determined by the generator
7155:The anomaly ratio $\rho_\lambda = \sum_{\text{bos}} 1/h_i
7161:KRW formula. The modular characteristic $\kappa$ is defined as the
7163:identity $\kappa = \rho \cdot c$ at the level of the anomaly ratio
 succeeded in 52ms:
  3475	Three identifications connect the bar complex to 3d gravity:
  3476	\begin{enumerate}[label=(\roman*)]
  3477	\item $\kappa(\mathrm{Vir}_c) = c/2$
  3478	 (Theorem~\ref{thm:modular-characteristic}) is the central charge
  3479	 of the gravity theory on $T^*\mathcal{T}_g$.
  3480	\item $\overline{\mathcal{M}}_g$ is the reduced phase space.
  3481	\item The curvature identity
  3482	 $d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$
  3483	 (Theorem~\ref{thm:genus1-universal-curvature}) says the bar
  3484	 differential fails to square to zero by the symplectic form,
  3485	 weighted by the central charge.
  3486	\end{enumerate}
codex
I’m consolidating the genuine issues now. The off-by-one/harmonic-number checks came back clean: no `H_{N-1}` drift and the `N=2,3,4,5` arithmetic matches the stated `H_N` convention. What remains are the actual seam defects: a factor-of-two mismatch, a theorem-A mislabel, and a `\kappa`/`c` conflation.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '3487,3496p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'total gravitational central charge|central charge.*Koszul-dual pair|kappa \\+ kappa.+= 13' chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\textbf\\{A\\} \\(Adjunction\\)|Virasoro specialization|W_3 specialization|Bar-cobar adjunction' chapters/examples/w_algebras.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras.tex:3493:the total gravitational central charge of a Koszul-dual pair.
 succeeded in 51ms:
  3487	The Koszul complementarity sum is
  3488	\[
  3489	\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c})
  3490	= \frac{c}{2} + \frac{26-c}{2}
  3491	= 13,
  3492	\]
  3493	the total gravitational central charge of a Koszul-dual pair.
  3494	This is the Virasoro instance of Theorem~\textup{\ref{thm:modular-characteristic}}
  3495	\textup{(}Theorem~D\textup{)}: for a single-generator $\mathcal{W}$-algebra with
  3496	$\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$, the sum $\kappa + \kappa'$
 succeeded in 51ms:
chapters/examples/w_algebras.tex:329:\item \emph{Virasoro specialization.} For $\mathfrak{g} = \mathfrak{sl}_2$ ($h^\vee = 2$), this gives $k' = -k-4$, and the central charges satisfy $c(k) + c(k') = 26$ exactly (by direct computation: $c(k') = 1 + 6(k+3)^2/(k+2)$, so $c(k)+c(k') = 2 + 24 = 26$), recovering the Virasoro level-shifting.
chapters/examples/w_algebras.tex:2719:\textbf{Theorem} & \textbf{Virasoro specialization} \\
chapters/examples/w_algebras.tex:2721:\textbf{A} (Adjunction) &
chapters/examples/w_algebras.tex:2774:\textbf{A} (Adjunction) &
chapters/examples/w_algebras.tex:3385:In the Virasoro specialization ($N = 2$) of the 3d HT action, the
chapters/connections/concordance.tex:31:\textbf{A} & Bar-cobar adjunction





thinking
**Evaluating findings and formatting**

I’m working with 3 or 4 findings here. I need to verify there are no more seam-related issues. I’ll search for the mislabel in `theorem A` regarding lines 2774 and 2721. It might be tricky since the format expects a single line reference, but perhaps I can mention both.

Maybe I could say something like `chapters/examples/w_algebras.tex:2721` and note that the same drift appears at line 2774. I'll also check for a general pattern with theorem A in W_N. There's an interesting note about duality at line 2830!
thinking
**Clarifying theorem issues**

I’m realizing that the items should be enumerated, not labeled with letters. Item (A) states `(\mathcal{W}_N^k)^! \simeq ...`, which doesn't refer to the bar-cobar adjunction as it should. It seems this mismatch is part of the overall "five main theorems" pattern, affecting line 2830 as well. The entire section misuses theorem A for duality instead of the correct bar-cobar adjunction.

To fix this, I need to adjust sections 2721-2727, 2774-2780, and 2830, either by replacing item A or renaming them while introducing a new bullet for "Koszul dual partner." It's crucial for clarity.
thinking
**Specializing Theorem A**

It seems like the user is asking for a specific adjustment regarding Theorem A, which is about bar-cobar adjunction. To provide a concrete fix, I think I should propose replacing the line label `\textbf{A} (Adjunction)` with `\textbf{A} (Bar-cobar adjunction)`. However, this creates a count mismatch since the section is titled "five theorems." 

To resolve that, I can rewrite the entry to describe bar-cobar adjunction accurately. I might use something like: "the bar functor and cobar functor form an adjoint pair on the Virasoro/W-algebra bar complexes."
thinking
**Refining Theorem Details**

I’m thinking about the exact wording for the bar-cobar adjunction statement. It seems like I could say, "`$\barB^{\mathrm{ch}} \dashv \Omega^{\mathrm{ch}}$ on the curved-complete Virasoro sector; the dual partner is $\mathrm{Vir}_{26-c}$ via $k\mapsto-k-4`." But I don't want to add unnecessary details that aren't specified.

Since the user is asking for an audit, maybe I should state, "Replace the row with the actual bar-cobar adjunction statement from Concordance Theorem A" and adjust the dual partner formula to a preceding sentence. I think this should be precise enough. 

I can recommend: "FIX: Replace the row text with `$\barBch \dashv \Omegach$ on the Virasoro bar complex; the same adjunction underlies the curved-complete $\mathcal W_3$ sector," and move `$\mathrm{Vir}_c^! \simeq \mathrm{Vir}_{26-c}$` to a separate preliminary sentence. 

I still need to look at the free_fields coefficient mismatch. Let me check the exact lines for that!
thinking
**Clarifying anomaly coefficient**

I need to update the proof line explanation of the anomaly coefficient to say `(c/2 - 13) = \kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26})`. I think that change aligns better with the w_algebras seam and the theorem statement, making it a stronger seam fix. I wonder if there's any other evidence that supports using `c - 26`. I should search the repository specifically for `d_equiv^2 = (c - 26)` to verify this quickly.
codex
One last verification pass: I’m checking whether the `c-26` coefficient appears anywhere else on the live surface. If it only occurs in the Virasoro chapter and everything else uses the `\kappa=c/2` normalization, then the exact repair is local and clean.
exec
/bin/zsh -lc "rg -n 'd_\\{\\\\mathrm\\{equiv\\}\\}\\"'^2'"' chapters/examples/free_fields.tex chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd_\\{\\\\mathrm\\{equiv\\}\\}\\"'^2 = '"\\(c - 26\\)|c - 26\\)\\\\,mu|c/2 - 13|13 - c/2' chapters/examples/free_fields.tex chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:4522:d_{\mathrm{equiv}}^2 = (c - 26)\,\mu,
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/free_fields.tex:4609:$d_{\mathrm{equiv}}^2 = (c/2 - 13)\,\kappa_1$ obstructs the critical
 succeeded in 51ms:
chapters/examples/w_algebras.tex:1721:The dual $\mathrm{Vir}_{26-c}$ has curvature $(26-c)/2 = 13 - c/2$, so
chapters/examples/w_algebras.tex:1722:its raw obstruction coefficient is $(13 - c/2) \in H^0(\overline{\mathcal{M}}_{1,1})$.
chapters/examples/free_fields.tex:4522:d_{\mathrm{equiv}}^2 = (c - 26)\,\mu,
chapters/examples/free_fields.tex:4546:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/free_fields.tex:4609:$d_{\mathrm{equiv}}^2 = (c/2 - 13)\,\kappa_1$ obstructs the critical



thinking
**Clarifying reporting details**

I'm focusing on the local context and need to figure out the checked count (N). It could refer to the number of files reviewed, so I might go with `Checked: 4` which would include files like `free_fields.tex` and others. The format states `Checked: N | Findings: N | Verdict`, so perhaps I should say `Checked: 4 files | Findings: 4 | Verdict: FAIL`. I also want to consider mentioning the lack of a standalone `virasoro.tex`, though that might not qualify as a finding.
thinking
**Organizing findings and summary**

The user asked me to locate relevant files, and it's crucial that I recognize the actual Vir surface as `free_fields`. I plan to note this in the summary after the checked items. The output will mostly consist of findings followed by a summary, allowing a possible short note. I’ll apply the "MAXIMALLY HARSH adversarial auditor" approach for clarity, starting with findings organized by severity. For instance, I have four findings, with the first concerning a factor-of-two mismatch in `free_fields.tex`. I need to decide on the correct fix, likely focusing on a local normalization approach.
thinking
**Ensuring clarity on fixes**

I need to make sure that the exact fix I choose is completely unambiguous. It's important to have a clear understanding of what changes need to be made to avoid any confusion later on. Clarity will help facilitate accurate implementation, especially when dealing with technical details. I want to ensure that any modifications are well-defined so that everyone involved can follow along without misinterpretation. Okay, I'll focus on articulating that clearly!
codex
I don’t see an `H_{N-1}` bug. What I do see is weaker but still real seam debt: several canonical surfaces use `H_N-1` without restating `H_N=\sum_{j=1}^N 1/j`, which is exactly the convention that repeatedly drifts in this repo. I’m deciding whether to count those as low-severity seam gaps or keep only the hard contradictions.





thinking
**Clarifying theorem fixes**

I’m considering how to correct the labeling of theorem A. One option is to rewrite the A rows to indicate the bar-cobar adjunction specialization while moving the dual-partner formulas into a new heading for the Koszul duality package. 

There’s a simpler approach: changing the row labels from "A (Adjunction)" to "Koszul duality package" and adjusting item (A) to reflect that. But I wonder if that alters the claim about five main theorems. It's tricky!
thinking
**Refining text instructions**

I need to clarify the instructions for a label change. The user wants to replace `A (Adjunction)` with `Koszul duality package` and remove the claim that it’s Theorem A. I think I should provide a more precise fix. Instead of options, I’ll suggest: “FIX: Change the row/item label from `A (Adjunction)` to `Koszul duality package` at lines 2721, 2774, and 2830. The current row cannot stay in slot A.” That seems clearer!
thinking
**Determining the exact fix**

I'm settling on a minimal yet precise fix for the label change. I want to suggest: “Change the row/item label from `A (Adjunction)` to `K (Koszul duality)` at lines 2721, 2774, and 2830, and remove the sentence about the five main theorems at lines 2702-2705. I think I should replace it with a clear alternative, naming the W-algebra theorem package. This change seems to better align with the goals of the project without unnecessarily complicating things!
thinking
**Considering problem incorporation**

I'm thinking about incorporating my first finding into the problem statement regarding the live Virasoro predecessor surface. There's a reference to `free_fields.tex`, but since there's no standalone `virasoro.tex`, I'm not sure if it's necessary. I might mention it in a summary note after the line to provide clarity. I wonder how that would impact the overall flow of information, but I want to keep things concise.
thinking
**Reviewing file findings**

I'm looking at my findings: we checked four key files and got five findings, which seems good. The user wants every inconsistency noted precisely with file and line, along with a fix. I wonder if there could be more issues. One finding mentions `landscape_census.tex:730`, where `\varrho_N = H_N -1` is used without definition. Should I also consider a critical factor mismatch on the free_fields line at 4546? It feels like I need to verify these thoroughly.
codex
- [CRITICAL] chapters/examples/free_fields.tex:4522 — PROBLEM: The live Virasoro seam writes `d_{\mathrm{equiv}}^2 = (c - 26)\,\mu` with `\mu=\kappa_1`, but the same theorem block then identifies the coefficient as `\kappa(\mathrm{Vir}_c)-\kappa(\mathrm{Vir}_{26}) = c/2 - 13` at line 4546 and restates the obstruction as `(c/2 - 13)\,\kappa_1` at line 4609. Those coefficients are not equal. FIX: Replace `(c - 26)` by `(c/2 - 13)` at lines 4522 and 4546 so the theorem, proof, and remark all use the same Virasoro normalization `\kappa(\mathrm{Vir}_c)=c/2`; keep `\mu=\kappa_1`.

- [MEDIUM] chapters/examples/w_algebras.tex:2721 — PROBLEM: This section says it records “the five main theorems” (2702-2705), but slot `A` is not Theorem A from the concordance. Here `A` is used for Koszul-dual partner data `\mathrm{Vir}_c^!\simeq \mathrm{Vir}_{26-c}`; the same drift repeats at 2774 and 2830, while the concordance defines Theorem A as Bar-cobar adjunction at chapters/connections/concordance.tex:31. FIX: Rewrite 2702-2705 to say this section records the W-algebra theorem package, not the five theorem labels verbatim; relabel the `A` entries at 2721, 2774, and 2830 as `Koszul duality` instead of `A (Adjunction)`.

- [MEDIUM] chapters/examples/w_algebras.tex:3477 — PROBLEM: The seam collapses `c` and `\kappa`: `\kappa(\mathrm{Vir}_c)=c/2` is called “the central charge of the gravity theory” at 3478-3479, the curvature is said to be “weighted by the central charge” at 3485, and the sum `\kappa+\kappa'=13` is called “the total gravitational central charge” at 3493. But the same chapter separates these quantities via the anomaly-ratio formulas `\varrho=\kappa/c` and `\kappa(\mathcal W_N)=c(H_N-1)` at 2743 and 2836. FIX: Replace “central charge” by “modular characteristic” at 3478, 3485, and 3493; if you want the relation to `c`, add “for Virasoro, `\kappa=c/2`.”

- [LOW] chapters/examples/w_algebras.tex:2172 — PROBLEM: `thm:wn-obstruction` proves the right general formula, but the seam specialization `\mathcal W_2=\mathrm{Vir}` is only buried in the verification bullets at 2265-2266. The theorem statement itself never surfaces the `N=2` check that the chapter opening relies on. FIX: After line 2182 add: `For N=2, H_2=3/2, so \mathcal W_2=\mathrm{Vir}_c and \kappa(\mathcal W_2)=c/2, recovering Theorem~\ref{thm:vir-genus1-curvature}.`

- [LOW] chapters/connections/concordance.tex:9613 — PROBLEM: The constitutional formula surface writes `\kappa(\Walg_N)=c(H_N{-}1)` without defining `H_N`; the same naked shorthand reappears in chapters/examples/landscape_census.tex:1416. That leaves the exact harmonic-number convention implicit on the very seam where this repo repeatedly drifts between `H_N` and `H_{N-1}`. FIX: Expand both sites to `\kappa(\Walg_N)=c\sum_{j=2}^{N}1/j = c(H_N{-}1)`, with `H_N=\sum_{j=1}^{N}1/j`.

No `H_{N-1}` bug or `N=2` arithmetic failure survived re-verification; the surviving defects are coefficient normalization, theorem-surface sync, and explicitness gaps.

## Summary
Checked: 4 files | Findings: 5 | Verdict: FAIL
tokens used
158,926
