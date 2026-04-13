# C09_higher_genus_complementarity (513s)

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1393](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1393) — PROBLEM: the formula still contains the literal placeholder `(\text{---})^!`, so the Verdier--Koszul involution is not actually written. FIX: replace the sentence with `Let $\sigma := ((-)^!)^{-1}\circ \mathbb{D}$ be the Verdier--Koszul involution (Lemma~\ref{lem:verdier-involution-moduli}).`

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:2103](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2103) — PROBLEM: `thm:ss-genus-stratification` restates the spectral-sequence theorem already proved earlier as `thm:ss-quantum`, creating duplicate theorem/proof surfaces for the same claim. FIX: delete lines `2103–2141` and replace them with a short remark: `The geometric origin of Theorem~\ref{thm:ss-quantum} is the genus stratification of the universal configuration family over $\overline{\mathcal{M}}_g$.`

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:3883](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3883) — PROBLEM: `lem:DR-verdier-compat` duplicates `prop:DR-preserves-duality` and even flips the shift sign (`[-d]` earlier, `[+\dim X]` here). FIX: delete lines `3883–3908` and replace them with `By Proposition~\ref{prop:DR-preserves-duality}, $\mathrm{DR}(\mathbb{D}_X\mathcal{M}) \simeq \mathrm{DR}(\mathcal{M})^\vee[-\dim X]$.`

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:4136](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4136) — PROBLEM: running prose still contains the editorial note `op:multi-generator-universality resolved negatively`. FIX: replace the full sentence tail with `for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.`

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:2196](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2196) — PROBLEM: the scope remark refers to a conjecture as a “corollary” and downgrades it to `\ClaimStatusHeuristic{}`. FIX: replace `This corollary is labeled \ClaimStatusHeuristic{} because` with `This conjecture is labeled \ClaimStatusConjectured{} because`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:2454](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2454) — PROBLEM: the scope remark under a conjecture again uses `\ClaimStatusHeuristic{}` instead of matching the conjectural surface. FIX: replace `Labeled \ClaimStatusHeuristic{} because:` with `Labeled \ClaimStatusConjectured{} because:`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:3333](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3333) — PROBLEM: the regime note uses bare `\kappa`, leaving the family unspecified. FIX: replace `curvature $\kappa$ is a central scalar` with `curvature $\kappa(\cA)$ is a central scalar`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:3389](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3389) — PROBLEM: the comparison table writes `\dfib^{\,2} = \kappa\cdot\omega_g` with bare `\kappa`. FIX: replace it with `\dfib^{\,2} = \kappa(\cA)\cdot\omega_g`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:3491](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3491) — PROBLEM: the Arakelov-twisting sentence again uses bare `\kappa`. FIX: replace `with curvature~$\kappa \cdot \omega_g$` with `with curvature~$\kappa(\cA)\cdot \omega_g$`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:5141](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5141) — PROBLEM: the hierarchy paragraph switches to bare invariants (`\kappa`, `\Delta`) and stays ambiguous through lines `5146`, `5151`, and `5161`. FIX: rewrite the cluster as `$\kappa(\cA) \to \Delta_{\cA} \to \mathfrak{C}_{\cA} \to \mathfrak{Q}_{\cA} \to \Theta_{\cA}$`, `d_{\mathrm{fib}}^2 = \kappa(\cA)\cdot\omega_g`, and `t_g^{(1)}` determined by `\kappa(\cA)` alone.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:5751](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5751) — PROBLEM: the sentence is grammatically broken (`is proved , is controlled`) and uses bare `\kappa`. FIX: replace the clause with `where the uniform-weight identity $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$ is proved, it is controlled by the same data.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:122](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:122) — PROBLEM: the “Physical and mathematical motivation” subsection opens with stacked remarks and no orienting sentence. FIX: insert after the heading: `Four viewpoints force Theorem~C: the anomaly/deformation split, the Kodaira--Spencer action on tautological classes, the involutive algebraic structure of Koszul duality, and the first explicit genus-$1$ test case.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:184](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:184) — PROBLEM: the text jumps from motivation straight into formal definitions without a bridge. FIX: insert before the definition: `These motivations converge on one construction: the ambient complex and its two homotopy eigenspaces.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2743](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2743) — PROBLEM: `one expects` is hedge language in a mathematical remark. FIX: replace `one expects` with `the Verlinde formula predicts`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2552](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2552) — PROBLEM: `We can verify this directly` promises a computation the example does not actually carry out. FIX: replace the sentence with `A direct cobar computation is omitted here; this example identifies $\mathbb{C}\cdot\lambda$ via complementarity.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2752](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2752) — PROBLEM: `We conclude with a practical algorithm` is AP109 signpost prose. FIX: replace it with `The complementarity identities above yield a practical algorithm for computing $Q_g(\mathcal{A})$ and checking complementarity in examples.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:3031](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3031) — PROBLEM: `We review` is a weak section opener. FIX: replace it with `The higher-genus descent argument uses only a specific genus-zero Beilinson--Drinfeld package, so this subsection isolates exactly the genus-zero input that must survive after adding moduli.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:4310](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4310) — PROBLEM: `We now show` is a pure signpost instead of a necessity transition. FIX: replace lines `4310–4313` with `This induction is the chain-level shadow of a single H-level statement: factorization homology descent. The subsection below makes that passage explicit.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:4799](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4799) — PROBLEM: `We now make each entry in the table explicit` is filler transition language. FIX: replace it with `The next examples realize the table entry by entry: Heisenberg is quadratic, affine is cubic, $\beta\gamma$ is quartic on the contact slice, and Virasoro is non-polynomial.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:4927](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4927) — PROBLEM: `We now prove` is another AP109 signpost. FIX: replace it with `The direct definition above still needs a geometric source: the next theorem identifies the potential as the generating function of a Lagrangian in a shifted cotangent chart.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2928](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2928) — PROBLEM: the table uses forbidden `---` as a placeholder in the Heisenberg row. FIX: replace `---` with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2930](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2930) — PROBLEM: the free-fermion row uses two forbidden `---` placeholders. FIX: replace both with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2932](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2932) — PROBLEM: the lattice row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2936](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2936) — PROBLEM: the `\beta\gamma` row uses two forbidden `---` placeholders. FIX: replace both with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2941](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2941) — PROBLEM: the `\widehat{\mathfrak{sl}}_2` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2943](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2943) — PROBLEM: the `\widehat{\mathfrak{sl}}_3` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2945](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2945) — PROBLEM: the `\widehat{G}_2` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2947](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2947) — PROBLEM: the `\widehat{E}_8` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2417](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2417) — PROBLEM: missing punctuation leaves `\lambda_g$ At $k=-h^\vee$` as a broken sentence. FIX: change it to `\lambda_g$. At $k = -h^\vee$, ...` or `\lambda_g$; at $k = -h^\vee$, ...`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:5366](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5366) — PROBLEM: there is a stray space before the semicolon, and the clause is padded by vague prose. FIX: replace `via the shift by $d_g$ ; the two sides of the holographic decomposition see genuinely different spectral data.` with `via the shift by $d_g$; the two sides of the holographic decomposition carry distinct spectral data.`

## Summary
Checked: 6105 | Findings: 30 | Verdict: FAIL


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
session id: 019d83fd-f588-7870-896c-72fe1b7f1f46
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/theory/higher_genus_complementarity.tex

Read the entire file. Audit for:

1. **AI slop vocabulary** (AP29): moreover, additionally, notably, crucially, remarkably,
   interestingly, furthermore, delve, leverage, tapestry, cornerstone, "it is worth noting".
   FIX: rewrite each occurrence without the slop word.

2. **Em dashes** (---  or U+2014): FORBIDDEN.
   FIX: replace with colon, semicolon, or separate sentence.

3. **Markdown in LaTeX** (AP121): backtick numerals, **bold**, _italic_.
   FIX: use $...$, \textbf, \emph.

4. **Chapter opening quality**: Does the chapter open with the PROBLEM (CG deficiency opening)?
   Or does it open with "In this chapter we..." (AP106/AP109)?
   FIX: rewrite the opening to state the deficiency/problem first.

5. **Passive voice hedging** in mathematical statements: "it can be shown", "one might expect",
   "it seems reasonable". If the math is clear, STATE it. If not, mark conjecture.
   FIX: active voice or explicit conjecture.

6. **Notation consistency**: Are macros used consistently? Any bare \kappa without family?
   Any bare \Omega/z without level k? Any undefined macros?
   FIX: add family superscript, level prefix, or macro definition.

7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
   FIX: delete dead code or resolve TODOs.

8. **Redundancy**: Same theorem stated in multiple places with different wording.
   FIX: state once, cite elsewhere.

9. **Transition quality**: Does each section force the next? Or do transitions use
   "We now turn to..." signpost language (AP109)?
   FIX: mathematical necessity transitions.

10. **Typography**: double spaces, inconsistent spacing around operators, broken LaTeX
    environments, mismatched braces.
    FIX: fix each instance.

Report EVERY finding with exact line number and exact fix.
mcp startup: no servers

thinking
**Evaluating explorer usage**

I’m thinking about the instruction "Always prefer explorers first," which suggests I should ask them about the file structure. I need to ensure minimal compliance and consider using the explorer to read the target file and any supporting files to pinpoint exact lines or issues. But the user specifically asked for findings with actual line numbers. I wonder if I can trust the explorer’s output fully—how necessary it is to verify claims with what I've read directly. Maybe I could also check the line count manually if needed, while still adhering to instructions not to re-read or search covered code.
codex
Auditing [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex) end to end for the ten requested surfaces. I’m loading the required repo guidance first, then I’ll read the full target file with line numbers and verify each candidate finding against the actual text before I report it.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 exited 1 in 50ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
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
**Planning file tasks**

I need to read the archive for a fallback. I think I should also use a skill and announce that I'm opening the deep-beilinson-audit skill. I might have to build-surface too since I’m uncertain about the audit being only deep-beil. I'll check the skill and possibly find the file line count to read the entire file. Might need to use rg for occurrences. Using the explorer could help spot issues in this codebase context. Let's move forward and update the comments!
codex
I’ve loaded the repo-wide guardrails and confirmed the theorem registry points to this chapter as a dense claim surface. Next I’m reading the audit skill and the full target file with numbered lines, plus a targeted grep sweep for the banned patterns so the review is grounded and exhaustive rather than impressionistic.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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

collab spawn_agent(call_JCwdFAHf0OdpjUGNKUM1fHK6, prompt="Read the entire file chapters/theory/higher_genus_complementarity.tex and identify cosmetic/aesthetic audit findings str…")
spawn_agent(call_JCwdFAHf0OdpjUGNKUM1fHK6, prompt="Read the entire file chapters/theory/higher_genus_complementarity.tex and identify cosmetic/aesthetic audit findings str…") pending init:
  agent: 019d83fe-635b-75d3-b026-042b1c6b3ad0
mcp startup: no servers
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
    6105 chapters/theory/higher_genus_complementarity.tex
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
bibliography
bp_self_duality.pdf
chapters
chiral_chern_weil.pdf
exec
/bin/zsh -lc "sed -n '1,200p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
codex
The file is 6,105 lines, so I’m reading it in numbered chunks and cross-checking with targeted pattern sweeps. I’ll keep the review on the ten requested surfaces only, and I’ll discard any candidate issue that doesn’t survive a second pass against the actual lines.
exec
/bin/zsh -lc "sed -n '200,400p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}\colon
\mathbf{C}_g \to \mathbf{C}_g), \qquad
\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id}\colon
\mathbf{C}_g \to \mathbf{C}_g).
\end{equation}
The \emph{cohomological shadows} (S-level) are defined by:
\begin{align}\label{eq:shadow-spaces}
Q_g(\cA) &:= H^*(\mathbf{Q}_g(\cA))
= \ker(\sigma - \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))),\\
Q_g(\cA^!) &:= H^*(\mathbf{Q}_g(\cA^!))
= \ker(\sigma + \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))).
\end{align}
\end{definition}

\begin{remark}[H/M/S layers; Convention~\ref{conv:hms-levels}]
The homotopy fibers~\eqref{eq:complementarity-fiber} are the
H-level objects; the bar complexes
$(\bar{B}^{(g)}(\cA), \Dg{g})$ are M-level models; the kernel
decomposition~\eqref{eq:shadow-spaces} is the S-level shadow.
The involution-splitting lemma
Plan update
Audit higher_genus_complementarity.tex for the requested cosmetic/aesthetic surfaces, grounded in direct file reads and verified with targeted pattern searches.
  → Read the entire target file in numbered chunks and note candidate issues by line
  • Run targeted pattern searches for banned vocabulary, em dashes, Markdown artifacts, hedging, TODO/dead-code markers, spacing, and notation red flags
  • Re-verify each candidate finding against the local text and draft exact fixes with severity and line references
exec
/bin/zsh -lc "sed -n '400,800p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\[
E_1^{p,q} = H^q\bigl(\operatorname{gr}_p
C^{(g)}_X(\cA)\big|_\Sigma\bigr)
\]
has $E_1^{p,q} = 0$ for $q \neq 0$ by Step~2
(the associated graded sees only the
genus-$0$ collision differential, which is Koszul-acyclic).
Therefore all differentials $d_r$ with $r \geq 2$ vanish
(their target lies in a row $q' \leq -1$, which is zero),
and $d_1$ acts within the $q = 0$ row, so
$E_\infty^{p,q} = E_2^{p,q}$. In particular,
$H^q(C^{(g)}_X(\cA)\!\mid_\Sigma) = 0$ for $q \neq 0$:
the full fiber complex (including the curvature terms) has
cohomology concentrated in bar-differential degree~$0$.
The surviving $H^0$ is the graded coalgebra
$\bigoplus_p E_\infty^{p,0} \cong \bigoplus_p (\cA^!)_p$,
which is identified with the Koszul dual coalgebra and
hence with the center $\mathcal{Z}_{\cA}\!\mid_\Sigma$
by the genus-$0$ center-bar identification
(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
exec
/bin/zsh -lc "sed -n '800,1200p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{proof}
Three conditions must be verified.

\emph{(1) Finite cohomological dimension of the base.}
The Deligne--Mumford--Knudsen stack
$\overline{\mathcal{M}}_g$ is a smooth proper
Deligne--Mumford stack of dimension $3g - 3$. For any
constructible sheaf $\mathcal{F}$ on
$\overline{\mathcal{M}}_g$,
$H^i(\overline{\mathcal{M}}_g, \mathcal{F}) = 0$ for
$i > 2(3g-3) = 6g - 6$
(Artin vanishing for proper DM stacks,
\cite[\S4.1]{Olsson16}).

\emph{(2) Constructibility of the fiber sheaves.}
The fiber cohomology sheaf
$\mathcal{H}^q_{\mathrm{fiber}}(\cA)$ on
$\overline{\mathcal{M}}_g$ is constructible with respect to
the stratification by topological type of stable curve.
On the smooth locus $\mathcal{M}_g$, it is a local system
exec
/bin/zsh -lc "sed -n '1200,1600p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$(E_1)_{\mathcal{A}^!}$, up to the appropriate sign.

\emph{Higher pages}: By induction, if $(E_r)_{\mathcal{A}} \cong ((E_r)_{\mathcal{A}^!})^\vee$, 
then taking cohomology with respect to $d_r$ preserves this duality:
\begin{equation}
(E_{r+1})_{\mathcal{A}} = H(E_r, d_r)_{\mathcal{A}} \cong (H(E_r, d_r)_{\mathcal{A}^!})^\vee 
= ((E_{r+1})_{\mathcal{A}^!})^\vee
\end{equation}

\emph{$E_\infty$ page}: Taking the limit $r \to \infty$:
\begin{equation}
(E_\infty^{p,q,g})_{\mathcal{A}} \cong ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee
\end{equation}

But $E_\infty^{*,*,g} = \text{gr}^g H^*$ by definition, so:
\begin{equation}
\text{gr}^g H^{p+q}(\bar{B}(\mathcal{A})) \cong (\text{gr}^g H^{p+d-q}(\bar{B}(
\mathcal{A}^!)))^\vee
\end{equation}
\end{proof}
exec
/bin/zsh -lc "sed -n '1600,2000p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
= -\beta
\]
where the sign $-1$ arises because the $j_! \to j_*$ natural
transformation, composed with the Koszul identification
$(\mathcal{A}^!)^! \simeq \mathcal{A}$, picks up the sign from
the anti-commutativity~\eqref{eq:verdier-ks-anticommute}.
Therefore elements from $\bar{B}^{(g)}(\mathcal{A}^!)$ have
eigenvalue $-1$ and contribute to~$V^-$.

The geometric content of the eigenspace decomposition
is the $j_*/j_!$ dichotomy.
Bar cochains of~$\mathcal{A}$ on the FM compactification
$\overline{C}_n(X)$ are sections of
$j_*j^*\mathcal{A}^{\boxtimes n}$: they \emph{extend across the
boundary} with logarithmic poles (the $j_*$-extension, which
permits growth along boundary divisors).
Cobar cochains of~$\mathcal{A}$ (equivalently, bar cochains
of~$\mathcal{A}^!$) are sections of
$j_!j^*(\mathcal{A}^!)^{\boxtimes n}$: they have \emph{compact
support} away from the boundary (the $j_!$-extension, which
exec
/bin/zsh -lc "sed -n '2000,2400p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
statement exists. Because~$\chi_g$ intertwines the involutions and the
pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
ambient homotopy eigenspaces
$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
Lagrangians. Pulling that structure back along~$\chi_g$ shows that
$L_g^+$ and~$L_g^-$ are isotropic. Since
$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
they are maximal isotropic, hence Lagrangian. Passing to cohomology
gives $H^*(L_g^+) = Q_g(\cA)$ and
$H^*(L_g^-) = Q_g(\cA^!)$.
\end{proof}

\begin{remark}[Genus-wise strictification]
\label{rem:genuswise-strictification}
\index{strictification!genus-wise}
The dg~Lie algebra $L_g = \barB^{(g)}(\cA)[1]$ appearing in
Theorem~\ref{thm:shifted-symplectic-complementarity} is a genus-$g$
strict chart inside the modular deformation package of
\S\ref{subsec:modular-deformation-complex}. More precisely, after
exec
/bin/zsh -lc "sed -n '2400,2800p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
complementarity formula takes the uncurved form:
\begin{equation}\label{eq:critical-complementarity}
Q_g(\widehat{\mathfrak{g}}_{-h^\vee})
\;\oplus\;
Q_g(\mathrm{CE}^{\mathrm{ch}}(\mathfrak{g}))
\;=\;
H^*\!\bigl(\overline{\mathcal{M}}_g,\,
\mathrm{Fun}(\mathrm{Op}_{\mathfrak{g}^\vee}(D))\bigr)
\end{equation}
where $\mathrm{Fun}(\mathrm{Op}_{\mathfrak{g}^\vee}(D))$ is the
Feigin--Frenkel center (Remark~\ref{rem:feigin-frenkel-center}; \cite{Feigin-Frenkel}).
\end{corollary}

\begin{proof}
From Table~\ref{tab:obstruction-summary}, the genus-$g$ obstruction for
$\widehat{\mathfrak{g}}_k$ is
$\mathrm{obs}_g = \frac{(k+h^\vee)\dim(\mathfrak{g})}{2h^\vee}\,
\lambda_g$ At $k = -h^\vee$, the coefficient $k + h^\vee$ vanishes. The
complementarity formula
(Theorem~\ref{thm:quantum-complementarity-main}) with
exec
/bin/zsh -lc "sed -n '2800,3200p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
The complementarity theorem is the mathematical foundation for the
complementarity of Type A and Type B topological strings, the
exchange of quantum corrections under mirror symmetry, and the
modular constraints on genus expansions.
\end{remark}

\subsection{The complementarity landscape}
\label{subsec:complementarity-landscape}
\index{complementarity!landscape|textbf}
\index{Koszul conductor|textbf}
\index{anomaly ratio|textbf}

The complementarity sum $\kappa(\cA) + \kappa(\cA^!)$ is a
level-independent invariant for every standard family
(Theorem~\ref{thm:complementarity-root-datum}). We collect the
full data here.

\begin{proposition}[Complementarity landscape; \ClaimStatusProvedHere]
\label{prop:complementarity-landscape}
\index{complementarity!landscape}
exec
/bin/zsh -lc "rg -n 'TODO|FIXME|XXX|"'^[[:space:]]*%|'"\\\\kappa(["'^_[:alpha:]]|$)|'"\\\\Omega/z|\\\\Omega\\\\,d\\\\log z|  +' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '---|—|\\*\\*|_[A-Za-z0-9]|"'`'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover| additionally|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|worth mentioning|it should be noted|it is important to note|we now turn to|we now|one might expect|it can be shown|it seems reasonable|seems to|appears to|perhaps|arguably' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: unrecognized flag ---|—|\*\*|_[A-Za-z0-9]|`
 succeeded in 52ms:
11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
15:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
29:splitting reduces to $\kappa(\cA) + \kappa(\cA^!) = K$: the modular
155:For $\mathcal{H}_\kappa$ at genus~$1$
157:characteristic $\kappa(\mathcal{H}_\kappa) = \kappa$):
159:$Q_1(\mathcal{H}_\kappa)=\mathbb{C}\cdot\kappa$ (central extension),
160:$Q_1(\mathcal{H}_\kappa^!)=\mathbb{C}\cdot\lambda$ (curved structure),
317:curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes
390:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes (it lies
448:$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
449:while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
559:The only curvature input is the scalar $\kappa(\cA)$,
897:Q_1(\mathcal{H}_\kappa) = \text{span}\{\kappa \cdot \lambda_1\} \cong \mathbb{C}
899:Here $\kappa$ is the level parameter and $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class;
900:the obstruction class $\kappa \cdot \lambda_1$ is a genus-$1$ quantum correction
980:For $\mathcal{H}_\kappa$ the current $J(z)$ is not central
981:($J(z)\,J(w) \sim \kappa/(z-w)^2$), while the vacuum~$\mathbf{1}$
982:and the level parameter~$\kappa$ are central (regular OPE with all
983:fields), so $H^0 = Z(\mathcal{H}_\kappa) =
984:\mathbb{C}\cdot\mathbf{1} \oplus \mathbb{C}\cdot\kappa$.
 succeeded in 52ms:
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
 succeeded in 51ms:
4310:We now show that this induction is the chain-level shadow of a
4799:We now make each entry in the table explicit.
4927:We now prove that the complementarity potential arises from shifted
exec
/bin/zsh -lc "sed -n '3200,3600p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
is fully faithful and pseudo-tensor, fiberwise over $\mathcal{M}_g$.
\end{lemma}

\begin{proof}
The embedding is defined fiberwise: for each $[\Sigma_g] \in \mathcal{M}_g$, we have:
\[\Delta^{(S)}|_{[\Sigma_g]}: M(\Sigma_g) \hookrightarrow M(\Sigma_g^S)\]
which is the BD embedding for the specific curve $\Sigma_g$.

\emph{Full faithfulness.} For $\mathcal{F}, \mathcal{G} \in M(\mathcal{C}_g/\mathcal{M}_g)$:
\begin{align*}
\Hom(\Delta^{(S)}_* \mathcal{F}, \Delta^{(S)}_* \mathcal{G}) 
&= \int_{[\Sigma_g] \in \mathcal{M}_g} \Hom_{\Sigma_g}(\Delta^{(S)}_* \mathcal{F}|_{[\Sigma_g]}, \Delta^{(S)}_* \mathcal{G}|_{[\Sigma_g]}) \\
&\simeq \int_{[\Sigma_g] \in \mathcal{M}_g} \Hom_{\Sigma_g}(\mathcal{F}|_{[\Sigma_g]}, \mathcal{G}|_{[\Sigma_g]}) && \text{(BD, fiberwise)} \\
&= \Hom(\mathcal{F}, \mathcal{G})
\end{align*}
The second isomorphism uses BD's full faithfulness on each fiber.

\emph{Pseudo-tensor.} The tensor structure $\otimes_{ch}$ on $M(\mathcal{C}_g/\mathcal{M}_g)$ is defined fiberwise, so preservation follows from BD fiberwise. \qedhere
\end{proof}

exec
/bin/zsh -lc "sed -n '3600,4000p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

By Lemmas \ref{lem:boundary-compatible}, \ref{lem:quantum-preserves-acyclicity}, and 
\ref{lem:graded-acyclic}, the Chevalley--Cousin complex $C(\mathcal{A})$ over 
$\mathcal{M}_{g,n}$ is acyclic for all $g \geq 0$.

Therefore, the descent from $R(X)$ to $X$ extends to all genera with quantum corrections.
\end{proof}

\begin{remark}[Physical interpretation]\label{rem:physical-higher-genus-descent}
The theorem states that configuration space integrals computing correlation functions on $\Sigma_g$ remain well-defined at all genera, provided the quantum corrections (central charges, anomalies) parametrized by $H^*(\overline{\mathcal{M}}_g)$ are included.
\end{remark}

\section[Verdier duality and Ayala-Francis compatibility]{Verdier duality and Ayala--Francis compatibility}
\label{sec:verdier-ayala-francis}

\subsection{Three levels of duality}
\label{subsec:three-dualities}

\begin{definition}[Three duality structures]\label{def:three-dualities}
We work with three dualities simultaneously.

exec
/bin/zsh -lc "sed -n '4000,4400p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
= \left(\int_X \mathcal{A}^!\right) \otimes \left(\int_X \mathcal{A}^!\right)\]

which is the Ayala--Francis coalgebra structure.
\end{proof}

\emph{Step 5: Full Compatibility}

\begin{lemma}[Diagram commutes; \ClaimStatusProvedHere]\label{lem:diagram-commutes-AF}
The diagram in the theorem statement commutes up to natural isomorphism.
\end{lemma}

\begin{proof}[Proof of Lemma]
By Lemmas \ref{lem:DR-verdier-compat}, \ref{lem:ran-duality-AF}, \ref{lem:bar-as-fact-hom-AF}, and 
\ref{lem:coalgebra-verdier-AF}, we have:
\[\text{DR}(\mathbb{D}(\mathcal{A})) \simeq \text{DR}(\mathcal{A})^* 
\simeq \text{AF-dual}(\text{DR}(\mathcal{A}))\]

The naturality in $\mathcal{A}$ ensures this is a natural isomorphism of functors.
\end{proof}


thinking
**Evaluating command issues**

I need to fix the broken regex command later and continue reading the rest of the file. I noticed some false positives while using kappa grep due to class issues. The user asked for a cosmetic audit of the file, which could involve addressing bare kappa formula problems. I'll also look for long comment blocks, particularly those over ten lines. It seems like the first line brings up a problem, which doesn't seem promising for our findings, so I'll evaluate that further.
thinking
**Planning regex pattern search**

I’m thinking about how to approach this pattern search using `rg -n -- '---|—|\\*\\*|`. I have to be careful with my quoting. For backticks, I can use single quotes around the regex. When it comes to patterns starting with a hyphen, using `--` should work. I’d like to read the file in 500-line chunks, focusing on chunks 421-840 first and continuing through the entire file. I don’t need every line for the final audit, but I will read in 420-line segments until the end, maybe processing four chunks in parallel.
exec
/bin/zsh -lc 'rg -n "notably|crucially|importantly|furthermore|clearly" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "Notably|crucially|importantly|clearly" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

codex
The opening is already problem-first rather than “In this chapter we…”, so I’m not manufacturing a chapter-opening finding. The live candidates so far are structural signpost phrases, some likely dead comment blocks, and a few notation lines that need context before I treat them as real violations.
exec
/bin/zsh -lc "rg -n -- '---|—' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '421,840p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '841,1260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "—" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '\\*\\*|"'`|_[A-Za-z]'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1393:Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution
2928: & $k$ & $-k$ & $0$ & --- & $k = 0$ \\
2930: & $1/4$ & $-1/4$ & $0$ & --- & --- \\
2932: & $r$ & $-r$ & $0$ & $2r$ & --- \\
2936: & $0$ & --- & --- \\[4pt]
2941: & $3(k{+}2)/4$ & $-3(k{+}2)/4$ & $0$ & $6$ & --- \\
2943: & $4(k{+}3)/3$ & $-4(k{+}3)/3$ & $0$ & $16$ & --- \\
2945: & $7(k{+}4)/4$ & $-7(k{+}4)/4$ & $0$ & $28$ & --- \\
2947: & $62(k{+}30)/15$ & $-62(k{+}30)/15$ & $0$ & $496$ & --- \\[4pt]
 succeeded in 53ms:
   421	\emph{Step~4: Base change.}
   422	Apply cohomology and base change to the family
   423	$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$.
   424	The fiber-level concentration from Step~3 gives
   425	$R^q\pi_{g*}\bar{B}^{(g)}(\cA) = 0$ for $q \neq 0$.
   426	Perfectness of $R\pi_{g*}\bar{B}^{(g)}(\cA)$
   427	(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
   428	uniformly over $\overline{\mathcal{M}}_g$.
   429	The surviving $R^0\pi_{g*}$ is identified with
   430	$\mathcal{Z}_{\cA}$ by the fiber-level identification
   431	from Step~3, which holds uniformly over the base.
   432	\end{proof}
   433	
   434	\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
   435	\index{Theorem C!decomposition}
   436	Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
   437	identification, this theorem) produces the ambient complex;
   438	$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
   439	gives the Verdier eigenspace decomposition and its Lagrangian
   440	splitting; $\mathrm{C}_2$
 succeeded in 53ms:
   841	graded pieces
   842	(Grothendieck~\cite[\S II.4.17]{Tohoku}). The $d_r$
   843	differential shifts the genus grading by~$r$ and the
   844	complementary degree by~$-r+1$. Since $E_r^{p,q,g} = 0$
   845	for $p > 6g - 6$ by (1) and for $g < 0$ by (3), every
   846	$d_r$ with $r > 6g - 6 + 1 = 6g - 5$ has either zero source
   847	or zero target. For fixed total degree, $r \le 3g - 2$
   848	suffices: the genus spectral sequence stabilizes
   849	at $E_{3g-2}$.
   850	\end{proof}
   851	
   852	\emph{Step 3: Quantum corrections are $E_\infty$ contributions.}
   853	
   854	\begin{lemma}[Quantum corrections as spectral sequence limit; \ClaimStatusProvedHere]
   855	\label{lem:quantum-from-ss}
   856	The genus-$g$ quantum correction space is:
   857	\begin{equation}
   858	Q_g(\mathcal{A}) = E_\infty^{*,*,g} = \bigoplus_{p+q=*} \text{gr}^g H^{p+q}(
   859	\bar{B}(\mathcal{A}))
   860	\end{equation}
 exited 1 in 50ms:

 succeeded in 50ms:
Total output lines: 873

7:compactifications $\overline{C}_n(X)$ and the Arnold forms
8:$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
13:operations $m_n$ for $n \geq 3$ that determine whether the shadow
15:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
17:$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
20: H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
22: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
59: H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
61: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
63:where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
64:$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
66: identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
78: complex $\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g,
80: $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
82: \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
83: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
84: rank, with $\mathbf{Q}_g(\cA) \simeq
85: \mathbf{Q}_g(\cA^!)^\vee[-(3g{-}3)]$.
exec
/bin/zsh -lc 'rg -n "---" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: unrecognized flag ---
exec
/bin/zsh -lc 'rg -n "`" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
zsh:1: unmatched "

exec
/bin/zsh -lc "rg -n '"'`'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
347:(EGA~III, Th\'eor\`eme~7.7.5)
3711:Both sides compute a form of ``dual'' of $\text{DR}(\mathcal{M})$; we must show they give the same result.
4023:Without this compatibility, we could not be sure that the ``dual coalgebra'' we construct
4024:geometrically is the same as the ``Koszul dual'' in the abstract algebraic sense.
4083:(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
4172:$D_\Gamma$. The passage from ``quasi-isomorphism on each~$D_\Gamma$''
4173:to ``quasi-isomorphism on all of~$\partial\overline{\mathcal{M}}_g$''
4775:survives), complementarity is ``fake,'' a linear splitting.
exec
/bin/zsh -lc "rg -n \"\\\\kappa\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:\kappa)
       ^^
error: unrecognized escape sequence
thinking
**Analyzing markdown issues**

I’m facing challenges with the markdown rg and its false positives, particularly due to TeX subscripts. I realize I might need to limit my focus—perhaps targeting backticks and `**`. Also, the em dash lines include placeholders like `---`, which the user deems forbidden. I need to figure out if these placeholders count as forbidden and whether to replace them with something else. I should probably keep reading beyond what I've covered so far because this file is extensive. Let’s continue to explore it in larger chunks for efficiency!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1261,1680p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '\\*\\*|"'`'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1681,2100p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|worth mentioning|it should be noted|it is important to note|one might expect|it can be shown|it seems reasonable|seems reasonable|we now turn to|we now|arguably|perhaps|appears to|seems to' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1261	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1262	
  1263	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
  1264	$g \geq 1$, and let $\pi: \mathcal{C}_g
  1265	\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
  1266	\begin{equation}
  1267	\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
  1268	\end{equation}
  1269	constructed from the Gauss--Manin connection on the chiral homology sheaf.
  1270	
  1271	This action interacts with Verdier duality via anti-commutativity: let
  1272	$\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim} H^*(\bar{B}^{(g)}(
  1273	\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
  1274	Then for every $z \in Z(\mathcal{A})$ and $v \in T_{[\Sigma_g]}\overline{\mathcal{M}}_g$:
  1275	\begin{equation}\label{eq:verdier-ks-anticommute}
  1276	\mathbb{D} \circ \nabla_{\kappa(v)}^z = -\nabla_{\kappa(v)}^z \circ \mathbb{D}
  1277	\end{equation}
  1278	where $\kappa(v)$ is the Kodaira--Spencer class associated to $v$ and $\nabla^z$
  1279	denotes the action of $z$ via the Gauss--Manin connection.
  1280	\end{theorem}
 succeeded in 51ms:
347:(EGA~III, Th\'eor\`eme~7.7.5)
3711:Both sides compute a form of ``dual'' of $\text{DR}(\mathcal{M})$; we must show they give the same result.
4023:Without this compatibility, we could not be sure that the ``dual coalgebra'' we construct
4024:geometrically is the same as the ``Koszul dual'' in the abstract algebraic sense.
4083:(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
4172:$D_\Gamma$. The passage from ``quasi-isomorphism on each~$D_\Gamma$''
4173:to ``quasi-isomorphism on all of~$\partial\overline{\mathcal{M}}_g$''
4775:survives), complementarity is ``fake,'' a linear splitting.
 succeeded in 51ms:
  1681	Q_g(\mathcal{A}) \cap Q_g(\mathcal{A}^!) = 0
  1682	\end{equation}
  1683	\end{lemma}
  1684	
  1685	\begin{proof}[Proof of Lemma~\ref{lem:trivial-intersection-complete}]
  1686	By Lemma~\ref{lem:eigenspace-decomposition-complete}, $Q_g(\mathcal{A}) = V^+$ and
  1687	$Q_g(\mathcal{A}^!) = V^-$ are the $+1$ and $-1$ eigenspaces of the involution
  1688	$\sigma$. Since $+1 \neq -1$ (we work over $\mathbb{C}$, characteristic $\neq 2$),
  1689	eigenspaces for distinct eigenvalues of any linear operator intersect trivially:
  1690	\[
  1691	V^+ \cap V^- = 0. \qedhere
  1692	\]
  1693	\end{proof}
  1694	
  1695	\emph{Step 10: Exhaustion (sum equals total cohomology).}
  1696	
  1697	\begin{lemma}[Exhaustion property; \ClaimStatusProvedHere]
  1698	\label{lem:exhaustion-complete}
  1699	The quantum correction spaces exhaust the moduli space cohomology:
  1700	\begin{equation}
 succeeded in 52ms:
4310:We now show that this induction is the chain-level shadow of a
4799:We now make each entry in the table explicit.
4927:We now prove that the complementarity potential arises from shifted
exec
/bin/zsh -lc "rg -n \"\\\\kappa\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\kappa)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '\\\\kappa' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
15:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
29:splitting reduces to $\kappa(\cA) + \kappa(\cA^!) = K$: the modular
155:For $\mathcal{H}_\kappa$ at genus~$1$
157:characteristic $\kappa(\mathcal{H}_\kappa) = \kappa$):
159:$Q_1(\mathcal{H}_\kappa)=\mathbb{C}\cdot\kappa$ (central extension),
160:$Q_1(\mathcal{H}_\kappa^!)=\mathbb{C}\cdot\lambda$ (curved structure),
317:curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes
390:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes (it lies
448:$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
449:while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
559:The only curvature input is the scalar $\kappa(\cA)$,
897:Q_1(\mathcal{H}_\kappa) = \text{span}\{\kappa \cdot \lambda_1\} \cong \mathbb{C}
899:Here $\kappa$ is the level parameter and $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class;
900:the obstruction class $\kappa \cdot \lambda_1$ is a genus-$1$ quantum correction
980:For $\mathcal{H}_\kappa$ the current $J(z)$ is not central
981:($J(z)\,J(w) \sim \kappa/(z-w)^2$), while the vacuum~$\mathbf{1}$
982:and the level parameter~$\kappa$ are central (regular OPE with all
983:fields), so $H^0 = Z(\mathcal{H}_\kappa) =
984:\mathbb{C}\cdot\mathbf{1} \oplus \mathbb{C}\cdot\kappa$.
exec
/bin/zsh -lc "rg -n '\\\\Omega/z' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n TODO chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n "obvious" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n "clearly" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

codex
A real defect surfaced: line 1393 contains a literal placeholder inside a formula, not a stylistic choice. I’m continuing through the rest of the file now so I can separate one-off damage from repeated patterns and avoid under-reporting second-order issues.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2101,2520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'HIGHER GENUS QUASI-ISOMORPHISM|KOSZUL DUALITY ACROSS GENERA|AMBIENT COMPLEMENTARITY AND THE LAGRANGIAN UPGRADE|Absorbed from' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2521,2940p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '((\\\\text\\{---\\})\\"'^!|'"\\(\\(-\\)\\"'^!'"\\)|Verdier--Koszul involution)' chapters/theory/higher_genus_complementarity.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
4033:% HIGHER GENUS QUASI-ISOMORPHISM
4516:% KOSZUL DUALITY ACROSS GENERA
4517:% (Absorbed from koszul_across_genera.tex)
4522:% AMBIENT COMPLEMENTARITY AND THE LAGRANGIAN UPGRADE
 succeeded in 53ms:
  2101	\end{remark}
  2102	
  2103	\begin{theorem}[Spectral sequence as genus stratification; \ClaimStatusProvedHere]\label{thm:ss-genus-stratification}
  2104	\textup{[Regime: curved-central; all genera
  2105	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  2106	
  2107	The spectral sequence of the bar complex admits a natural genus grading:
  2108	\[E_1^{p,q,g} = H^q\left(\bar{B}^p_g(\mathcal{A})\right)\]
  2109	where $\bar{B}^p_g$ denotes contributions from genus-$g$ configuration spaces, converging to:
  2110	\[E_\infty^{*,*} = \bigoplus_{g \geq 0} H^*_{\text{chiral}}(\mathcal{A}, \Sigma_g)\]
  2111	
  2112	The genus filtration refines the topological complexity and corresponds to loop order 
  2113	in quantum field theory.
  2114	\end{theorem}
  2115	
  2116	\begin{proof}[Geometric origin]
  2117	The genus stratification arises from the moduli space $\overline{\mathcal{M}}_{g,n}$ of 
  2118	stable curves. For smooth curve $X$ of genus $g$:
  2119	
  2120	\emph{Step 1:} The configuration space $\overline{C}_n(X)$ fibers over $X$. Taking $X$ 
 succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:1393:Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution
chapters/theory/higher_genus_complementarity.tex:1393:Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution
 succeeded in 52ms:
  2521	\end{equation}
  2522	where $V^*$ is the linear dual of the generating space~$V$, the curvature
  2523	$m_0 = -\kappa \cdot c$ encodes the obstruction, and
  2524	$\kappa(\mathcal{H}_\kappa^!) = -\kappa$
  2525	(since $h^\vee = 0$ for the Heisenberg).
  2526	Note: $\mathcal{H}_\kappa^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)
  2527	\neq \mathcal{H}_{-\kappa}$; the Koszul dual is generated by~$V^*$,
  2528	not by~$V$ at level~$-\kappa$
  2529	\textup{(}Remark~\textup{\ref{rem:km-complementarity-vs-feigin-frenkel})}.
  2530	
  2531	By the complementarity theorem:
  2532	\begin{equation}
  2533	Q_1(\mathcal{H}_\kappa^!) = \left(H^*(\overline{\mathcal{M}}_{1,1}, Z(\mathcal{H}_\kappa)) 
  2534	/ Q_1(\mathcal{H}_\kappa)\right)^\vee
  2535	\end{equation}
  2536	
  2537	Since $H^*(\overline{\mathcal{M}}_{1,1}) = \mathbb{C} \oplus \mathbb{C}\lambda$ and 
  2538	$Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (which pairs with $H^0 = \mathbb{C}$), 
  2539	we have:
  2540	\begin{equation}
exec
/bin/zsh -lc "rg -n '\\*\\*' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2941,3360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3361,3780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'TODO|FIXME|XXX|op:|resolved negatively|"'^%|% [A-Z]'"' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
95:(Proposition~\ref{prop:standard-examples-modular-koszul}).
577:(Proposition~\ref{prop:model-independence}) lifts to H-level.
595:(PTVV~\cite{PTVV13}; Proposition~\ref{prop:ptvv-lagrangian}).
1787:(Proposition~\ref{prop:model-independence}) ensures the
1800:Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
1804:\label{prop:lagrangian-eigenspaces}
1889:Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
1891:Proposition~\ref{prop:ptvv-lagrangian} upgrades the Verdier side to a
1944: Proposition~\ref{prop:modular-deformation-truncation}) of the
2030:\label{prop:ptvv-lagrangian}
2055:(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
2072: Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
2091:Proposition~\ref{prop:ptvv-lagrangian});
2364:Proposition~\ref{prop:virasoro-generic-koszul-dual}).
2818:\label{prop:complementarity-landscape}
2891:$c(k) + c(k') = 2\dim(\fg)$ is Proposition~\ref{prop:sl2-complementarity-all-genera}.
2910:(Proposition~\ref{prop:complementarity-landscape});
3083:\begin{proposition}[Factorization over moduli; \ClaimStatusProvedHere]\label{prop:factorization-over-moduli}
3237:\begin{proposition}[Gluing formula at nodes; \ClaimStatusProvedHere]\label{prop:gluing-at-nodes}
3660:\begin{proposition}[DR preserves duality structures; \ClaimStatusProvedHere]\label{prop:DR-preserves-duality}
 succeeded in 52ms:
  2941	 & $3(k{+}2)/4$ & $-3(k{+}2)/4$ & $0$ & $6$ & --- \\
  2942	$\widehat{\mathfrak{sl}}_3$
  2943	 & $4(k{+}3)/3$ & $-4(k{+}3)/3$ & $0$ & $16$ & --- \\
  2944	$\widehat{G}_2$
  2945	 & $7(k{+}4)/4$ & $-7(k{+}4)/4$ & $0$ & $28$ & --- \\
  2946	$\widehat{E}_8$
  2947	 & $62(k{+}30)/15$ & $-62(k{+}30)/15$ & $0$ & $496$ & --- \\[4pt]
  2948	\midrule
  2949	\multicolumn{6}{@{}l}{\textit{$\cW_N$-algebras:
  2950	 $\kappa + \kappa^! = \varrho_N K_N \neq 0$
  2951	}} \\[2pt]
  2952	$\mathrm{Vir}_c$ ($= \cW_2$)
  2953	 & $c/2$ & $(26{-}c)/2$
  2954	 & $13$ & $26$ & $13$ \\
  2955	$\cW_3$
  2956	 & $5c/6$ & $5(100{-}c)/6$
  2957	 & $250/3$ & $100$ & $50$ \\
  2958	$\cW_4$
  2959	 & $13c/12$ & $13(246{-}c)/12$
  2960	 & $533/2$ & $246$ & $123$ \\
 succeeded in 52ms:
  3361	\]
  3362	For $\dzero \circ d_k = 0$: after integrating $z_i$ over $\gamma_k$, the result is a form on a configuration space with one fewer variable. The collision singularity $(z_i - z_j)^{-1}$ is replaced by $\oint_{\gamma_k} (z_i - z_j)^{-1} dz_i$, which is either $0$ (if $z_j \notin \gamma_k$) or $2\pi i$ (if $z_j \in \gamma_k$), in both cases producing a regular function of $z_j$ with no residue to extract. For $d_k \circ \dzero = 0$: extracting the residue $\operatorname{Res}_{D_{ij}}$ at $z_i = z_j$ eliminates the variable $z_i$ (replacing it by the OPE coefficient at $z_j$); the subsequent period integral $\oint_{\gamma_k} dz_i$ has nothing to act on, since $z_i$ no longer appears.
  3363	
  3364	\emph{Pole-order separation.} The full OPE contains higher-order poles $(z_i - z_j)^{-m}$ for $m \geq 2$, but these contribute to the correction operators $d_k$ with $k \geq 2$ in the expansion $\Dg{g} = \dzero + \sum_k t_k d_k$, not to $\dzero$ or $d_1$. The relation $\dzero d_k + d_k \dzero = 0$ established above involves only the residue operator $\dzero$ and the period integral $d_k$; the simple-pole analysis suffices because $\dzero$ extracts first-order residues by definition (Definition~\ref{def:bar-differential-complete}).
  3365	
  3366	\emph{Step 4: Quantum terms vanish; the Fay trisecant identity
  3367	is the higher-genus Borcherds identity.}
  3368	
  3369	Three propagators control the bar differential at genus~$g$,
  3370	producing three chain-level models with different algebraic types
  3371	(Convention~\ref{conv:higher-genus-differentials}):
  3372	\begin{center}
  3373	\small
  3374	\begin{tabular}{lllll}
  3375	\textbf{Model} & \textbf{Propagator} & \textbf{Arnold 3-form} & \textbf{Differential} & \textbf{Category} \\[2pt]
  3376	Classical &
  3377	 $(z_i - z_j)^{-1}\,dz_i$ &
  3378	 $\mathcal{A}_3^{(0)} = 0$ &
  3379	 $\dzero^2 = 0$ &
  3380	 derived \\[2pt]
collab wait(call_mUTPBXpoUGXR9xDnqp0jdFUc)
  receivers: 019d83fe-635b-75d3-b026-042b1c6b3ad0
exec
/bin/zsh -lc 'rg -n "genuinely" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1643:carry genuinely different deformation-theoretic content.
5133:and the complementarity potential is genuinely non-polynomial; its
5205:anomaly itself is an invariant: it is the first genuinely nonlinear
5366:; the two sides of the holographic decomposition see genuinely
5693:The first genuinely nonlinear holographic anomaly is the quadratic
exec
/bin/zsh -lc 'rg -n "basically" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

wait(call_mUTPBXpoUGXR9xDnqp0jdFUc) timed out:
exec
/bin/zsh -lc "sed -n '1620,1675p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
forces vanishing along boundary divisors).
The Verdier involution exchanges $j_*$ and $j_!$
(Lemma~\ref{lem:verdier-extension-exchange}), hence exchanges
$\mathcal{A}$-contributions and $\mathcal{A}^!$-contributions.
The identification of the $+1$-eigenspace with
$Q_g(\mathcal{A})$ and the $-1$-eigenspace with
$Q_g(\mathcal{A}^!)$ then follows from the Verdier intertwining
$\mathbb{D}_{\mathrm{Ran}}\, \bar{B}(\mathcal{A}) \simeq
\cA^!_\infty$ (Theorem~\ref{thm:verdier-bar-cobar}):
at the level of centers,
$\sigma(\mathcal{Z}(\mathcal{A})) = \mathcal{Z}(\mathcal{A}^!)$,
so $\sigma$ acts as $+1$ on $j_*$-extended classes from~$\mathcal{A}$
and as $-1$ on $j_!$-extended classes from~$\mathcal{A}^!$.

More precisely, the anti-commutativity
\eqref{eq:verdier-ks-anticommute} ensures that the Kodaira--Spencer
deformation maps $V^+$ to $V^-$ and vice versa. If $\alpha \in V^+$,
then
\begin{equation}
\sigma(\nabla_{\kappa(v)}^z \alpha) = -\nabla_{\kappa(v)}^z (\sigma \alpha) =
exec
/bin/zsh -lc "sed -n '5110,5160p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{itemize}
\item Gaussian: all $\ell_n^{\mathrm{tr}} = 0$ for $n \geq 2$
(Heisenberg);
\item Lie/tree: $\ell_2^{\mathrm{tr}} \neq 0$,
$\ell_n^{\mathrm{tr}} = 0$ for $n \geq 3$ (affine);
\item Contact/quartic: $\ell_2^{\mathrm{tr}} = 0$,
$\ell_3^{\mathrm{tr}} \neq 0$ ($\beta\gamma$);
\item Mixed: $\ell_2^{\mathrm{tr}} \neq 0$ \emph{and}
$\ell_3^{\mathrm{tr}} \neq 0$ (Virasoro, $\mathcal{W}_N$).
\end{itemize}
The shadow obstruction tower is the homotopy structure made visible.
\end{remark}

\begin{remark}[The three archetypes from the Lagrangian perspective]
\label{rem:three-archetypes-lagrangian}
The fake-complementarity criterion reframes the archetype trichotomy
(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
The Heisenberg is exactly fake: $S_{\mathcal{H}}$ is quadratic.
Affine $\widehat{\mathfrak{sl}}_2$ is cubic at leading order:
$S_{\mathrm{aff}} = \tfrac12 H + \tfrac16\kappa(a,[a,a])$,
exec
/bin/zsh -lc "sed -n '5185,5225p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
shifted-symplectic phase space in the sense of
Proposition~\ref{prop:ptvv-lagrangian}, with a
$(-(3g{-}3))$-shifted symplectic form.
The two complementary branches $\mathbf{Q}_g(\cA)$ and
$\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces of this phase space,
and the passage from one to the other is Fourier transform.
Quantizing the linearized phase space produces a Heisenberg algebra,
a Fock representation, a Weyl algebra, and a Fourier kernel that
intertwines creation with annihilation. This is the content of the
linear holographic calculus.

When one goes beyond the linear theory (when two Riemann surfaces
are sewn together and the intermediate phase space is integrated
out), the composition of holographic maps ceases to be strictly
multiplicative. It picks up a determinant factor, a square-root
correction $\det(1 - C_1 B_2)^{-1/2}$ that measures the failure of
naive composition. This determinant anomaly satisfies a $2$-cocycle
law and defines a central extension of the sewing semigroup: the
metaplectic extension. A choice of metaplectic splitting
trivializes the cocycle and restores strict composition, but the
codex
The mid-file surfaces are getting clearer. There are several non-mathematical editorial scars: placeholder dashes used as table values, an unresolved `op:... resolved negatively` note left in running prose, and inherited section-header comment blocks that look like merge debris rather than durable source.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4201,4620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'We now |we now |We now|turn to|we turn to|This completes|We conclude with|We review|We show|we show|we prove' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3781,4200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1043:This completes Step~I: the genus filtration, the associated spectral
1244:This completes Step~II: Verdier duality on configuration spaces
1743:This completes Step~III. Combining Steps~7--10, we have shown:
1760:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
2752:We conclude with a practical algorithm for computing $Q_g(\mathcal{A})$ and verifying 
3031:We review the Beilinson--Drinfeld construction at genus zero, identifying what generalizes.
3561:This completes the extension of BD's Chevalley--Cousin acyclicity to all genera. The key new ingredients were:
3644:We show these three dualities are compatible via the de Rham functor.
3707:For any $\mathcal{D}$-module $\mathcal{M}$ on $\mathrm{Conf}_n(X)$, we prove:
3774:Now we show that DR makes the two dualities compatible.
4310:We now show that this induction is the chain-level shadow of a
4799:We now make each entry in the table explicit.
4927:We now prove that the complementarity potential arises from shifted
 succeeded in 52ms:
  4201	left to the separate coderived-model formalism
  4202	\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
  4203	and is intentionally not folded into
  4204	Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
  4205	Proposition~\ref{prop:coderived-adequacy}(a) remains.
  4206	\end{remark}
  4207	
  4208	\begin{remark}[Geometric substrate (Volume~II)]
  4209	\label{rem:theorem-b-lagrangian}
  4210	\index{Lagrangian self-intersection!Theorem B}
  4211	Volume~II interprets Koszul inversion as the reconstruction
  4212	of a Lagrangian from its clean self-intersection: the derived
  4213	self-intersection groupoid
  4214	$\mathfrak{S} = \mathcal{L} \times_{\mathcal{M}} \mathcal{L}$
  4215	is \'etale precisely on the Koszul locus, and an \'etale groupoid
  4216	determines its base up to equivalence.
  4217	\end{remark}
  4218	
  4219	\begin{remark}[Structural explanation: the Getzler--Kapranov involution]
  4220	\label{rem:inversion-from-ft-squared}
 succeeded in 51ms:
  3781	& \mathbb{D}_X(\mathcal{M}_n) \arrow[d, "\text{DR}"] \\
  3782	\int_{\text{Conf}_n(X)} \mathcal{A} \arrow[r, "\text{AF-dual}"] 
  3783	& \mathbb{D}_{\text{top}}\left(\int_{-\text{Conf}_n(X)} \bar{B}(\mathcal{A})\right)
  3784	\end{tikzcd}
  3785	\]
  3786	\end{proposition}
  3787	
  3788	\begin{proof}[Proof of Proposition]
  3789	\emph{Step 1: Apply DR to Verdier dual (left-then-down).}
  3790	
  3791	From Lemma~\ref{lem:verdier-dual-chiral}:
  3792	\[\mathbb{D}_X(\mathcal{M}_n) \simeq (\mathcal{A}^\vee)^{\boxtimes n} \otimes \Omega^{2n-k}_c\]
  3793	
  3794	Applying DR:
  3795	\begin{align*}
  3796	\text{DR}(\mathbb{D}_X(\mathcal{M}_n)) 
  3797	&= R\Gamma(\text{Conf}_n(X), \Omega^\bullet \otimes_{\mathcal{D}} ((\mathcal{A}^\vee)^{\boxtimes n} \otimes \Omega^{2n-k}_c)) \\
  3798	&\simeq R\Gamma_c(\text{Conf}_n(X), \mathcal{A}^\vee)^{\boxtimes n} && \text{(Poincaré duality)} \\
  3799	&\simeq \left(R\Gamma(\text{Conf}_n(X), \mathcal{A})^{\boxtimes n}\right)^\vee && \text{(linear duality)}
  3800	\end{align*}
collab wait(call_JAg0rVBiRTXuaHhpUWV3nIge)
  receivers: 019d83fe-635b-75d3-b026-042b1c6b3ad0
exec
/bin/zsh -lc "sed -n '5340,5385p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 \C, & g \text{ odd}, \\[4pt]
 \Det\!\bigl(V_g(\cA)\bigr)^{\otimes 2}, & g \text{ even}.
 \end{cases}
 \end{equation}
\end{enumerate}
\end{corollary}

\begin{proof}
The transposition
$\mathbf{Q}_g(\cA^!) \simeq V_g(\cA)^\vee[-d_g]$ gives (i) on
cohomology. Self-holography forces palindromicity.
Evaluating at $u = -1$ and using the parity of $d_g = 3g - 3$
(odd when $g$ is even) gives (iii). For (iv), duality gives
$\Det(V^\vee) \cong \Det(V)^{-1}$, and a shift by $[-d_g]$
inverts the determinant line iff $d_g$ is odd. The direct-sum
formula then yields~\eqref{eq:holo-comp-det-parity}.
\end{proof}

\begin{remark}[The palindromic constraint on standard families]
\label{rem:holo-comp-palindromic-examples}
exec
/bin/zsh -lc "sed -n '5670,5720p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\Det(R\pi_* \mathcal{Z}(\cA))$. The metaplectic $2$-cocycle is
therefore the sewing obstruction of the half-determinant: it
measures the failure of $\Det^{1/2}$ to be multiplicative under
gluing of Riemann surfaces.
\end{remark}

\subsection{The first nonlinear holographic anomaly}
\label{subsec:holo-comp-first-nonlinear-anomaly}

\begin{corollary}[First nonlinear holographic anomaly;
\ClaimStatusProvedHere]
\label{cor:holo-comp-first-nonlinear-anomaly}
\index{nonlinear anomaly!first holographic|textbf}
Let $G_1$, $G_2$ be composable Gaussian triples. The trace-log
expansion of the anomaly is
\begin{equation}\label{eq:holo-comp-trace-log-anomaly}
\log \alpha_g(C_1, B_2)
=
\frac{1}{2}\operatorname{Tr}(C_1 B_2)
+ \frac{1}{4}\operatorname{Tr}\!\bigl((C_1 B_2)^2\bigr)
wait(call_JAg0rVBiRTXuaHhpUWV3nIge) timed out:
exec
/bin/zsh -lc 'rg -n "barB" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
75: $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect
108:$\barB(\cA)$ carries a proper $\mathrm{CY}_1$ structure
1894:$L_g = \barB^{(g)}(\cA)[1]$ would require the additional BV package of
1918: $\barB^{\mathrm{ch}}(\cA)$
1925: \barB^{\mathrm{ch}}(\cA)
1927: \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
1929: \barB^{\mathrm{ch}}(\cA^!)[1]
1935: The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
1962:The BV bracket $\{-,-\}_{\mathrm{BV}}$ on $\barB^{\mathrm{ch}}(\cA)$
1969:$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
1972:$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
1978:Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
1981:$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
1983:$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
1984:(\barB^{(g)}(\cA))^\vee[1]$.
2016:The dg~Lie algebra $L_g = \barB^{(g)}(\cA)[1]$ appearing in
2097:$L_g = \barB^{(g)}(\cA)[1]$. In each proved incarnation,
2744:$\dim H^0(\barB^{(1)}(\widehat{\mathfrak{sl}}_{2,k}), \Dg{1})
4227:$\barB = \mathrm{FT}(\cA)$ and
4228:$\Omega(\barB) = \mathrm{FT}(\mathrm{FT}(\cA)) \simeq \cA$

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '130,210p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   130	this split algebraic content: what $\mathcal{A}$ sees as obstruction,
   131	$\mathcal{A}^!$ sees as deformation. The conformal
   132	anomaly of matter is the ghost-number violation of ghosts.
   133	\end{remark}
   134	
   135	\begin{remark}[Kodaira--Spencer action on tautological classes]
   136	The center $Z(\cA)$ acts on $H^*(\overline{\mathcal{M}}_g)$
   137	($\lambda$-classes, $\psi$-classes, boundary classes) via the
   138	Kodaira--Spencer map
   139	$\rho\colon Z(\cA)\to\mathrm{End}(H^*(\overline{\mathcal{M}}_g))$,
   140	and the eigenspace decomposition gives
   141	$H^*(\overline{\mathcal{M}}_g,Z(\cA))
   142	=Q_g(\cA)\oplus Q_g(\cA^!)$.
   143	\end{remark}
   144	
   145	\begin{remark}[Algebraic structure]
   146	The involution $\cA \mapsto \cA^!$ with $(\cA^!)^! \simeq \cA$
   147	forces any functorial invariant to decompose:
   148	$F(\cA) \oplus F(\cA^!) = \text{universal}$. The complementarity
   149	theorem identifies $H^*(\overline{\mathcal{M}}_g, Z(\cA))$ as the
exec
/bin/zsh -lc 'rg -n "seem(s|ed|ing)?" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "appear(s|ed|ing)" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2016:The dg~Lie algebra $L_g = \barB^{(g)}(\cA)[1]$ appearing in
2177: Example: The level $\kappa$ in Heisenberg $\mathcal{H}_\kappa$ appears as central
2178:extension, while in the Koszul dual $\mathrm{CE}(\mathfrak{h}_{-\kappa})$ (curved commutative algebra) it appears as curvature $\mu_0 = -\kappa \cdot \omega
2544:\emph{Interpretation}: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (the central extension appears as an obstruction) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$ (the first Chern class appears as a deformation).
2623:The \emph{Koszul} dual $\widehat{\mathfrak{g}}_{-h^\vee}^! = \mathrm{CE}^{\mathrm{ch}}(\mathfrak{g}_{-h^\vee})$ appearing in complementarity must not be confused with the $\mathcal{W}$-algebra $\mathcal{W}(\mathfrak{g})$ that appears in the Feigin--Frenkel theorem. The $\mathcal{W}$-algebra is obtained from $\widehat{\mathfrak{g}}_{-h^\vee}$ via quantum Drinfeld--Sokolov reduction (a non-trivial functor), not via bar-cobar duality. The two dualities are related (the DS reduction functor intertwines them; see Theorem~\ref{thm:ds-complementarity-tower-main}), but they are logically distinct.
3362:For $\dzero \circ d_k = 0$: after integrating $z_i$ over $\gamma_k$, the result is a form on a configuration space with one fewer variable. The collision singularity $(z_i - z_j)^{-1}$ is replaced by $\oint_{\gamma_k} (z_i - z_j)^{-1} dz_i$, which is either $0$ (if $z_j \notin \gamma_k$) or $2\pi i$ (if $z_j \in \gamma_k$), in both cases producing a regular function of $z_j$ with no residue to extract. For $d_k \circ \dzero = 0$: extracting the residue $\operatorname{Res}_{D_{ij}}$ at $z_i = z_j$ eliminates the variable $z_i$ (replacing it by the OPE coefficient at $z_j$); the subsequent period integral $\oint_{\gamma_k} dz_i$ has nothing to act on, since $z_i$ no longer appears.
thinking
**Continuing findings process**

I need to keep working on the sections from 4621 to 6105. There are many more findings to explore! The user is looking for every detail, so I need to be exhaustive and targeted. I might focus primarily on the requested surfaces instead of worrying too much about mathematical correctness. But I should ensure the line numbers are exact and consider whether I need to read every line with the same detail. Alright, let's keep going with the chunks!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4621,5040p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4621	\Bigr).
  4622	\end{equation}
  4623	A tangent vector in $T_{\mathrm{comp}}(\cA)$ is a first-order
  4624	deformation of $\cA$, a first-order deformation of $\cA^!$, and a
  4625	first-order deformation of the universal kernel, constrained by the
  4626	linearized Maurer--Cartan equation.
  4627	\end{definition}
  4628	
  4629	\begin{theorem}[Ambient complementarity in tangent form]
  4630	\label{thm:ambient-complementarity-tangent}
  4631	\ClaimStatusProvedHere
  4632	Assume an ambient complementarity datum exists for $\cA$. Then:
  4633	\begin{enumerate}[label=\textup{(\roman*)}]
  4634	\item the complex $T_{\mathrm{comp}}(\cA)$ carries a canonical
  4635	nondegenerate pairing of degree $-1$;
  4636	\item the one-sided tangent complexes
  4637	\[
  4638	T_{\cA} := \operatorname{fib}(\nabla_{\cA} \colon L_{\cA} \to K_{\cA}),
  4639	\qquad
  4640	T_{\cA^!} := \operatorname{fib}(\nabla_{\cA^!} \colon L_{\cA^!} \to K_{\cA})
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5041,5460p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5041	\begin{proof}
  5042	In the cotangent normal form one Lagrangian is the zero section and
  5043	the other is the graph of $dS_{\cA}$. Their derived intersection
  5044	is the derived zero locus of $dS_{\cA}$, which is the derived
  5045	critical locus of $S_{\cA}$.
  5046	\end{proof}
  5047	
  5048	\begin{proposition}[Criterion for fake complementarity]
  5049	\label{prop:fake-complementarity-criterion}
  5050	\ClaimStatusProvedHere
  5051	In the cotangent chart centered at $\mathcal{M}_{\cA}$, the
  5052	following are equivalent:
  5053	\begin{enumerate}[label=\textup{(\roman*)}]
  5054	\item the dual Lagrangian $\mathcal{M}_{\cA^!}$ is linear;
  5055	\item the complementarity potential $S_{\cA}$ is quadratic;
  5056	\item the derived critical locus $\operatorname{Crit}(S_{\cA})$
  5057	is controlled entirely by its Hessian complex, with no higher
  5058	nonlinear operations.
  5059	\end{enumerate}
  5060	The first obstruction to fake complementarity is the first nonzero
exec
/bin/zsh -lc "rg -n 'placeholder|---|op:|resolved negatively|\\texttt\\{|TODO|FIXME|XXX|\\\\qedhere|This subsection|This section|The following theorem records|The following table|practical algorithm|We review' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
95:(Proposition~\ref{prop:standard-examples-modular-koszul}).
577:(Proposition~\ref{prop:model-independence}) lifts to H-level.
595:(PTVV~\cite{PTVV13}; Proposition~\ref{prop:ptvv-lagrangian}).
1393:Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution
1691:V^+ \cap V^- = 0. \qedhere
1760:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
1787:(Proposition~\ref{prop:model-independence}) ensures the
1800:Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
1804:\label{prop:lagrangian-eigenspaces}
1889:Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
1891:Proposition~\ref{prop:ptvv-lagrangian} upgrades the Verdier side to a
1895:Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
1944: Proposition~\ref{prop:modular-deformation-truncation}) of the
2030:\label{prop:ptvv-lagrangian}
2055:(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
2072: Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
2091:Proposition~\ref{prop:ptvv-lagrangian});
2364:Proposition~\ref{prop:virasoro-generic-koszul-dual}).
2752:We conclude with a practical algorithm for computing $Q_g(\mathcal{A})$ and verifying 
2818:\label{prop:complementarity-landscape}
collab wait(call_dMfEboJZXySQjulc1oQ8BR19)
  receivers: 019d83fe-635b-75d3-b026-042b1c6b3ad0
exec
/bin/zsh -lc 'rg -n "might" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n "should" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2025:should be read conditionally as one coordinate chart on a single modular formal
wait(call_dMfEboJZXySQjulc1oQ8BR19) timed out:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5461,5880p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5881,6105p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5461	\item The generator relations are
  5462	 $w \star_{g,\hbar} v = wv + \hbar\, w(v)$,
  5463	 while $v \star v' = vv'$ and $w \star w' = ww'$.
  5464	\item The linear Fourier kernels compose exactly:
  5465	 $\langle \mathbf{K}_{12}^{\mathrm{lin}},
  5466	 \mathbf{K}_{23}^{\mathrm{lin}}\rangle_{(2)}
  5467	 = \mathbf{K}_{13}^{\mathrm{lin}}$.
  5468	\end{enumerate}
  5469	\end{theorem}
  5470	
  5471	\begin{proof}
  5472	Associativity: pairwise contraction operators commute, so both
  5473	parenthesizations of a triple product equal
  5474	$\mu_{123} \circ \exp(\hbar(\Gamma_{12} + \Gamma_{13} +
  5475	\Gamma_{23}))$. PBW: each Wick contraction lowers symmetric degree
  5476	by $2$. The generator relations follow because the only nontrivial
  5477	contraction pairs a left $W$-generator with a right $V$-generator.
  5478	The linear sewing law is the $B = C = 0$ specialization of the
  5479	Gaussian composition theorem below.
  5480	\end{proof}
 succeeded in 53ms:
  5881	$\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'})
  5882	= \mathrm{const}$
  5883	(Proposition~\ref{prop:ds-package-functoriality}(iv))
  5884	has a purely \emph{algebraic} origin in the Feigin--Frenkel
  5885	involution.
  5886	
  5887	The central charge of $\mathcal{W}_N^k = \mathcal{W}^k(\fg,
  5888	f_{\mathrm{prin}})$ is
  5889	(Theorem~\ref{thm:wn-obstruction})
  5890	\begin{equation}\label{eq:wn-central-charge-complement}
  5891	c(t) \;=\; (N{-}1)\Bigl[1 -
  5892	\frac{N(N{+}1)(t{-}1)^2}{t}\Bigr],
  5893	\qquad t = k + h^\vee,
  5894	\end{equation}
  5895	and Feigin--Frenkel duality sends $t \mapsto -t$. Since
  5896	$c(t) + c(-t)$ eliminates the odd powers of~$t$:
  5897	\[
  5898	c(t) + c(-t) \;=\; 2(N{-}1)(2N^2{+}2N{+}1),
  5899	\]
  5900	the curvature sum
exec
/bin/zsh -lc "rg -n '  +|\\t' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

collab wait(call_CMZjNcMwYTFN709Y1bDuU2Eh)
  receivers: 019d83fe-635b-75d3-b026-042b1c6b3ad0
codex
- **AI Slop** – `chapters/theory/higher_genus_complementarity.tex#L1643`: the sentence “The two eigenspaces therefore carry *genuinely* different deformation-theoretic content” leans on the informal filler word “genuinely,” which recurs at `#L5133`, `#L5205`, `#L5366`, and `#L5693`. Replace the adjective with precise mathematical language, e.g., “carry distinct deformation-theoretic content” (line 1643), “the complementarity potential is manifestly non‑polynomial” (line 5133), “the anomaly itself is the first nonlinear holographic correction” (line 5205), “the two sides … see distinct spectral data” (line 5366), and “the first nonlinear holographic anomaly” (line 5693).

- **Section framing** – `chapters/theory/higher_genus_complementarity.tex#L124-L162`: the new “Physical and mathematical motivation” subsection opens immediately with a stack of `\begin{remark}` blocks, so the reader is plunged into examples without any connective overview. Add a short lead-in (e.g., “The following remarks spell out the physical intuition, Kodaira–Spencer action, and algebraic structure that feed into Theorem C.”) before the first `remark` to ground the subsection heading.

- **Logical transition into definitions** – `chapters/theory/higher_genus_complementarity.tex#L184-L205`: after the motivational remarks there is no bridging sentence before jumping into the formal definition of the ambient and shadow complexes. Insert a sentence such as “We now fix the ambient/shadow notation needed to state Theorem C precisely” so the reader understands how the preceding motivation feeds into the upcoming construction.

Next: rephrase the highlighted phrases and add the two short lead‑in/transition sentences so the prose feels more intentional.
wait(call_CMZjNcMwYTFN709Y1bDuU2Eh) 1 agents complete:
  019d83fe-635b-75d3-b026-042b1c6b3ad0 completed: "- **AI Slop** – `chapters/theory/higher_genus_complementarity.tex#L1643`: the sentence “The two eigenspaces therefore ca…"






thinking
**Considering search findings**

The explorer returned a few findings, but there are still many more to explore. I might need to use different searches for banned words, as "genuinely" isn’t on the user’s list, yet it could be seen as sloppiness. The user specifically asked for listed terms, so maybe we shouldn’t include it. I’ll need to focus on the requested surfaces and exact defects, and check line numbers for specific issues. It’s important to stay grounded in final findings!
thinking
**Searching for macro issues**

I need to consider searching for undefined macros, but it’s tricky. Using LaTeX compile might be an option, although it seems more cosmetic. I could run a targeted grep or compile the specific file to check for undefined macros. Perhaps using `texfot` is excessive. I should be cautious about markdown elements—only the table caption line uses backticks and isn’t actual markdown. The user wants every finding with exact line numbers and fixes, which I need to keep in mind!
thinking
**Grouping table row findings**

I’m thinking about how to handle reporting identical table rows. Should I report each line individually, or cluster contiguous lines with the same issue? The request for "every finding" suggests I document each instance, but perhaps I could group ranges instead. The final contract specifies singular file:line, so I might use a representative line for each bullet but mention contiguous lines. It seems I’ll need separate lines for each `---` occurrence, or I could reference specific table line numbers as needed.
thinking
**Evaluating transition language**

The user asked whether each section forces the next or if transitions use phrases like "We now turn to..." from AP109. I think it’s important to identify mathematical necessity transitions, including phrases like "We conclude" or "We review." However, not every phrase is problematic, like "This completes." I need to focus on obvious signposts that may disrupt flow. It seems there are specific phrases I should look out for, so I might compile a list of slop words too.
thinking
**Considering findings and variables**

I’m thinking about whether the final document should mention that there are no findings related to the listed AP29 words, but it seems the contract should only include actual findings. In the summary, I can note that I checked 6105 lines. To simplify, I might not include sections with zero findings. Also, I need to clarify the use of the \kappa variable, as search results show it in many contexts without family ties. I should determine if this poses an issue.
thinking
**Evaluating chapter quality**

I think the user wants the opening of the chapter to have good quality. The file begins with `\section{The complementarity theorem}`, which technically suggests it's a section rather than a chapter. I need to consider how to make a section feel like a strong chapter opener. Hmm, I'll think about incorporating engaging elements that can create a smooth transition from section to the overall theme of the chapter. Let's explore this idea more!
codex
The file is fully read now. I’m doing a verification sweep for hedging and notation ambiguity so I don’t overstate cosmetic problems that are actually locally scoped, and I’m matching each surviving issue to an exact rewrite rather than a generic style complaint.
exec
/bin/zsh -lc "rg -n -i 'one expects|it may|may be|could be|would be|appears|seems|reasonable|arguably|perhaps|likely|should be read|think of|one sees|we can verify|we prove|we review|we conclude|we now' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa(?"'!'"\\()' -P chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\Omega/z|\\\\Omega\\\\,d\\\\log z|\\\\Omega/z|\\\\Omega\\\\/z' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import re
from pathlib import Path
text = Path('chapters/theory/higher_genus_complementarity.tex').read_text()
patterns = ['moreover','additionally','notably','crucially','remarkably','interestingly','furthermore','delve','leverage','tapestry','cornerstone','it is worth noting']
for p in patterns:
    for m in re.finditer(re.escape(p), text, flags=re.I):
        line = text.count('\\n', 0, m.start()) + 1
        print(f'{line}:{m.group(0)}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1344:We prove the anti-commutativity~\eqref{eq:verdier-ks-anticommute} in full generality
2025:should be read conditionally as one coordinate chart on a single modular formal
2177: Example: The level $\kappa$ in Heisenberg $\mathcal{H}_\kappa$ appears as central
2178:extension, while in the Koszul dual $\mathrm{CE}(\mathfrak{h}_{-\kappa})$ (curved commutative algebra) it appears as curvature $\mu_0 = -\kappa \cdot \omega
2544:\emph{Interpretation}: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ (the central extension appears as an obstruction) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$ (the first Chern class appears as a deformation).
2552:\emph{Verification}: We can verify this directly by computing the cobar complex of
2623:The \emph{Koszul} dual $\widehat{\mathfrak{g}}_{-h^\vee}^! = \mathrm{CE}^{\mathrm{ch}}(\mathfrak{g}_{-h^\vee})$ appearing in complementarity must not be confused with the $\mathcal{W}$-algebra $\mathcal{W}(\mathfrak{g})$ that appears in the Feigin--Frenkel theorem. The $\mathcal{W}$-algebra is obtained from $\widehat{\mathfrak{g}}_{-h^\vee}$ via quantum Drinfeld--Sokolov reduction (a non-trivial functor), not via bar-cobar duality. The two dualities are related (the DS reduction functor intertwines them; see Theorem~\ref{thm:ds-complementarity-tower-main}), but they are logically distinct.
2743:formula (equation~\eqref{eq:verlinde-general}), one expects
2752:We conclude with a practical algorithm for computing $Q_g(\mathcal{A})$ and verifying 
3031:We review the Beilinson--Drinfeld construction at genus zero, identifying what generalizes.
3362:For $\dzero \circ d_k = 0$: after integrating $z_i$ over $\gamma_k$, the result is a form on a configuration space with one fewer variable. The collision singularity $(z_i - z_j)^{-1}$ is replaced by $\oint_{\gamma_k} (z_i - z_j)^{-1} dz_i$, which is either $0$ (if $z_j \notin \gamma_k$) or $2\pi i$ (if $z_j \in \gamma_k$), in both cases producing a regular function of $z_j$ with no residue to extract. For $d_k \circ \dzero = 0$: extracting the residue $\operatorname{Res}_{D_{ij}}$ at $z_i = z_j$ eliminates the variable $z_i$ (replacing it by the OPE coefficient at $z_j$); the subsequent period integral $\oint_{\gamma_k} dz_i$ has nothing to act on, since $z_i$ no longer appears.
3558:We prove acyclicity by induction on the Cousin filtration, now accounting for quantum corrections, incorporating Lemmas \ref{lem:relative-diagonal}, \ref{lem:boundary-compatible}, \ref{lem:quantum-preserves-acyclicity}.
3707:For any $\mathcal{D}$-module $\mathcal{M}$ on $\mathrm{Conf}_n(X)$, we prove:
4310:We now show that this induction is the chain-level shadow of a
4799:We now make each entry in the table explicit.
4927:We now prove that the complementarity potential arises from shifted
5182:The physical picture is clean. Think of the genus-$g$ ambient complex
 succeeded in 52ms:
11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
155:For $\mathcal{H}_\kappa$ at genus~$1$
157:characteristic $\kappa(\mathcal{H}_\kappa) = \kappa$):
159:$Q_1(\mathcal{H}_\kappa)=\mathbb{C}\cdot\kappa$ (central extension),
160:$Q_1(\mathcal{H}_\kappa^!)=\mathbb{C}\cdot\lambda$ (curved structure),
897:Q_1(\mathcal{H}_\kappa) = \text{span}\{\kappa \cdot \lambda_1\} \cong \mathbb{C}
899:Here $\kappa$ is the level parameter and $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class;
900:the obstruction class $\kappa \cdot \lambda_1$ is a genus-$1$ quantum correction
980:For $\mathcal{H}_\kappa$ the current $J(z)$ is not central
981:($J(z)\,J(w) \sim \kappa/(z-w)^2$), while the vacuum~$\mathbf{1}$
982:and the level parameter~$\kappa$ are central (regular OPE with all
983:fields), so $H^0 = Z(\mathcal{H}_\kappa) =
984:\mathbb{C}\cdot\mathbf{1} \oplus \mathbb{C}\cdot\kappa$.
1291:\kappa: T_{\overline{\mathcal{M}}_g} \to R^1\pi_* T_{\mathcal{C}_g/\overline{\mathcal{M}}_g}
1381:map $\kappa_Z: Z(\mathcal{A}) \to Z(\mathcal{A}^!)$ such that:
1384:\mathbb{D} \circ \rho(z) = \rho(\kappa_Z(z)) \circ \mathbb{D}
1389:$\langle \rho(z)\omega, \omega' \rangle_{\mathrm{Verdier}} = \langle \omega, \rho(\kappa_Z(z))\omega' \rangle_{\mathrm{Verdier}}$
1395:$(\mathcal{A}^!)^! \simeq \mathcal{A}$ sends $\kappa_Z(z) \in Z(\mathcal{A}^!)$ back to
1396:$z \in Z(\mathcal{A})$ (since $\kappa_Z$ composed with $\kappa_Z'$ is the identity by
1409:&= \rho(\kappa_Z(z)) \circ \mathbb{D} \circ \mathcal{L}_{\tilde{v}}
 exited 127 in 52ms:
zsh:1: command not found: python
 exited 1 in 53ms:





thinking
**Evaluating code comments**

I'm wondering if certain sections are considered dead code or just style noise. The user mentions dead code in commented-out sections longer than 10 lines, but this one has only 3 lines. So, maybe they don't fit that criteria, but they could still be aesthetic noise. Lines 4515-4523 are only 8 lines, so also not over 10. I think I should focus on line 4136, as it clearly indicates unresolved issues, which I might categorize as dead code to fix or rewrite. I will take care not to over-report.
thinking
**Considering cosmetic audits**

I see there's an environment or status mismatch here. The user asked for an aesthetic or cosmetic audit, rather than focusing on theorem status. However, I wonder if this could still be categorized as dead code or an inconsistency. Since it's part of the file's content, should I include it? It doesn't really align with the requested areas, but it's a live inconsistency in the prose that might still deserve attention. I'll need to think this through!
thinking
**Considering cosmetic audit details**

The user wants a cosmetic and aesthetic audit of the file, so I should focus on aspects like dead code, redundancy, and typography. The status mismatch they mentioned doesn't fit in the audit list, unless I consider it typography, which doesn’t seem right. However, there are prose flaws I can highlight. For instance, there's an inconsistency where "This corollary" should read "conjecture" at line 2195-2196. Those kinds of copy-edit errors are definitely worth including in my notes.
thinking
**Analyzing remarks for audit**

I see that the remark should clarify that it’s not proved by saying, "This conjecture is labeled \ClaimStatusConjectured." It's definitely a cosmetic fix, but I wonder if it's within the user's scope since they want every weakness analyzed. Since the entire file is read, I might need to include it as it highlights a weakness. Although the user didn’t specifically ask for this, it aligns with their goal. I'll also check for any other instances of "This corollary" to catch all relevant inconsistencies.
exec
/bin/zsh -lc "rg -n 'This corollary|Labeled \\\\ClaimStatusHeuristic|ClaimStatusHeuristic' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'genuinely|clean\\.|Think of|practical algorithm|we review|We review|We conclude|We now|resolved negatively|is proved ,' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'``|'"''|\\bconfig\\. space\\b|\\bH-level\\b|\\bM-level\\b|\\bS-level\\b' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2196:This corollary is labeled \ClaimStatusHeuristic{} because a complete proof requires:
2454:Labeled \ClaimStatusHeuristic{} because: (a)~A/B-model Koszul pair
 succeeded in 50ms:
1643:carry genuinely different deformation-theoretic content.
2752:We conclude with a practical algorithm for computing $Q_g(\mathcal{A})$ and verifying 
3031:We review the Beilinson--Drinfeld construction at genus zero, identifying what generalizes.
4136:The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
4310:We now show that this induction is the chain-level shadow of a
4799:We now make each entry in the table explicit.
4927:We now prove that the complementarity potential arises from shifted
5133:and the complementarity potential is genuinely non-polynomial; its
5182:The physical picture is clean. Think of the genus-$g$ ambient complex
5205:anomaly itself is an invariant: it is the first genuinely nonlinear
5366:; the two sides of the holographic decomposition see genuinely
5693:The first genuinely nonlinear holographic anomaly is the quadratic
5751:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ is proved , is controlled by the same data.
 succeeded in 53ms:
Total output lines: 6105

1:\section{The complementarity theorem}
2:\label{sec:complementarity-theorem}
3:
4:Classical Koszul duality over a point is a discrete correspondence:
5:$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
6:Already at genus~$0$ on a curve, the Fulton--MacPherson
7:compactifications $\overline{C}_n(X)$ and the Arnold forms
8:$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
9:that has no counterpart over a point: the collision residues that
10:define the bar differential, the averaging map
11:$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
12:characteristic from the spectral $r$-matrix, and the higher
13:operations $m_n$ for $n \geq 3$ that determine whether the shadow
14:tower terminates. At genus~$g \geq 1$, the fiberwise curvature
15:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
16:algebras to interact through the moduli
17:$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
18:decomposes into two complementary halves via Verdier duality:
exec
/bin/zsh -lc "rg -n 'Verdier--Koszul involution|\\(\\(-\\)\\"'^!'"\\)|\\(\\(\\-\\)\\"'^!'"\\)|\\(\\text\\{---\\}\\)\\"'^!'"' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1388,1398p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For $\omega \in \bar{B}^{(g)}(\mathcal{A})$ and $\omega' \in \bar{B}^{(g)}(\mathcal{A}^!)$:
$\langle \rho(z)\omega, \omega' \rangle_{\mathrm{Verdier}} = \langle \omega, \rho(\kappa_Z(z))\omega' \rangle_{\mathrm{Verdier}}$
by the $Z(\mathcal{A})$-linearity of the Koszul pairing.

\emph{Ingredient 3: The involution absorbs the transpose.}
Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution
(Lemma~\ref{lem:verdier-involution-moduli}). The Koszul identification
$(\mathcal{A}^!)^! \simeq \mathcal{A}$ sends $\kappa_Z(z) \in Z(\mathcal{A}^!)$ back to
$z \in Z(\mathcal{A})$ (since $\kappa_Z$ composed with $\kappa_Z'$ is the identity by
Koszul involutivity). Therefore:
\begin{equation}
 succeeded in 53ms:
chapters/theory/higher_genus_complementarity.tex:1393:Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution






thinking
**Noting down issues**

I’m thinking it might be better to clearly point out each line with an exact fix. For instance, on line 2928, I've identified a problem: the table uses `---` as a placeholder in the `$K=c+c'$` column. This isn't just visually ambiguous, but it also goes against the rule of forbidden em-dash syntax. I really want to make sure everything is clear and understandable, so documenting these issues properly can help in addressing them more effectively.
thinking
**Evaluating redundancy in theorems**

It seems I'm seeing the same content presented with different wording here. I need to double-check. Both Theorem 706 and Theorem 2103 describe the genus spectral sequence of a bar complex. This looks like redundancy, which isn't ideal since it can lead to confusion or unnecessary repetition. I should clarify these points to ensure clear understanding.
thinking
**Considering theorem adjustments**

I see that theorem 2103 duplicates earlier theorem 706. I could resolve this by referencing theorem ss-quantum in a remark, or I could delete the duplicate and insert a new remark. Since the user specifically asked for an exact fix rather than an edit, I'll keep that in mind while addressing the issue. It seems like there's a straightforward way to correct this, which is good!
thinking
**Fixing punctuation issues**

I'm looking at some specific fixes for style and punctuation. There's an issue with the phrase that states, "We can verify this directly by computing," which I think should be replaced with, "A direct cobar computation is omitted here; the example identifies $\mathbb C\cdot\lambda$ via complementarity."

I noticed there are missing punctuation marks, which is certainly important for typography. For example, there's a fragment that could be fixed to read more clearly. I'll also address a leading semicolon in another line to improve clarity.
thinking
**Planning a fix**

I need to make an exact fix in the document. Specifically, I want to delete the duplicate theorem or proof block from 2103 to 2141. I’ll replace it with a remark that introduces the geometric origin of a specific theorem. I think the code should look like `\begin{remark}[Geometric origin of Theorem\ref{thm:ss-quantum}] ... \end{remark}`. It seems straightforward, but I want to ensure I get the formatting right.
thinking
**Considering style changes**

I’m thinking about whether to delete the leading space for clarity and possibly improve the overall style. Maybe using a comma would make it clearer too. So, I guess I’ll suggest replacing `\`$d_g$ ;\`` with `\`$d_g$; \``. It feels like a small change, but it could enhance readability! Let’s see how this adjustment goes!
codex
- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1393](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1393) — PROBLEM: the formula still contains the literal placeholder `(\text{---})^!`, so the Verdier--Koszul involution is not actually written. FIX: replace the sentence with `Let $\sigma := ((-)^!)^{-1}\circ \mathbb{D}$ be the Verdier--Koszul involution (Lemma~\ref{lem:verdier-involution-moduli}).`

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:2103](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2103) — PROBLEM: `thm:ss-genus-stratification` restates the spectral-sequence theorem already proved earlier as `thm:ss-quantum`, creating duplicate theorem/proof surfaces for the same claim. FIX: delete lines `2103–2141` and replace them with a short remark: `The geometric origin of Theorem~\ref{thm:ss-quantum} is the genus stratification of the universal configuration family over $\overline{\mathcal{M}}_g$.`

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:3883](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3883) — PROBLEM: `lem:DR-verdier-compat` duplicates `prop:DR-preserves-duality` and even flips the shift sign (`[-d]` earlier, `[+\dim X]` here). FIX: delete lines `3883–3908` and replace them with `By Proposition~\ref{prop:DR-preserves-duality}, $\mathrm{DR}(\mathbb{D}_X\mathcal{M}) \simeq \mathrm{DR}(\mathcal{M})^\vee[-\dim X]$.`

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:4136](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4136) — PROBLEM: running prose still contains the editorial note `op:multi-generator-universality resolved negatively`. FIX: replace the full sentence tail with `for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.`

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:2196](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2196) — PROBLEM: the scope remark refers to a conjecture as a “corollary” and downgrades it to `\ClaimStatusHeuristic{}`. FIX: replace `This corollary is labeled \ClaimStatusHeuristic{} because` with `This conjecture is labeled \ClaimStatusConjectured{} because`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:2454](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2454) — PROBLEM: the scope remark under a conjecture again uses `\ClaimStatusHeuristic{}` instead of matching the conjectural surface. FIX: replace `Labeled \ClaimStatusHeuristic{} because:` with `Labeled \ClaimStatusConjectured{} because:`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:3333](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3333) — PROBLEM: the regime note uses bare `\kappa`, leaving the family unspecified. FIX: replace `curvature $\kappa$ is a central scalar` with `curvature $\kappa(\cA)$ is a central scalar`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:3389](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3389) — PROBLEM: the comparison table writes `\dfib^{\,2} = \kappa\cdot\omega_g` with bare `\kappa`. FIX: replace it with `\dfib^{\,2} = \kappa(\cA)\cdot\omega_g`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:3491](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3491) — PROBLEM: the Arakelov-twisting sentence again uses bare `\kappa`. FIX: replace `with curvature~$\kappa \cdot \omega_g$` with `with curvature~$\kappa(\cA)\cdot \omega_g$`.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:5141](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5141) — PROBLEM: the hierarchy paragraph switches to bare invariants (`\kappa`, `\Delta`) and stays ambiguous through lines `5146`, `5151`, and `5161`. FIX: rewrite the cluster as `$\kappa(\cA) \to \Delta_{\cA} \to \mathfrak{C}_{\cA} \to \mathfrak{Q}_{\cA} \to \Theta_{\cA}$`, `d_{\mathrm{fib}}^2 = \kappa(\cA)\cdot\omega_g`, and `t_g^{(1)}` determined by `\kappa(\cA)` alone.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:5751](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5751) — PROBLEM: the sentence is grammatically broken (`is proved , is controlled`) and uses bare `\kappa`. FIX: replace the clause with `where the uniform-weight identity $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$ is proved, it is controlled by the same data.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:122](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:122) — PROBLEM: the “Physical and mathematical motivation” subsection opens with stacked remarks and no orienting sentence. FIX: insert after the heading: `Four viewpoints force Theorem~C: the anomaly/deformation split, the Kodaira--Spencer action on tautological classes, the involutive algebraic structure of Koszul duality, and the first explicit genus-$1$ test case.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:184](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:184) — PROBLEM: the text jumps from motivation straight into formal definitions without a bridge. FIX: insert before the definition: `These motivations converge on one construction: the ambient complex and its two homotopy eigenspaces.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2743](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2743) — PROBLEM: `one expects` is hedge language in a mathematical remark. FIX: replace `one expects` with `the Verlinde formula predicts`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2552](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2552) — PROBLEM: `We can verify this directly` promises a computation the example does not actually carry out. FIX: replace the sentence with `A direct cobar computation is omitted here; this example identifies $\mathbb{C}\cdot\lambda$ via complementarity.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2752](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2752) — PROBLEM: `We conclude with a practical algorithm` is AP109 signpost prose. FIX: replace it with `The complementarity identities above yield a practical algorithm for computing $Q_g(\mathcal{A})$ and checking complementarity in examples.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:3031](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3031) — PROBLEM: `We review` is a weak section opener. FIX: replace it with `The higher-genus descent argument uses only a specific genus-zero Beilinson--Drinfeld package, so this subsection isolates exactly the genus-zero input that must survive after adding moduli.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:4310](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4310) — PROBLEM: `We now show` is a pure signpost instead of a necessity transition. FIX: replace lines `4310–4313` with `This induction is the chain-level shadow of a single H-level statement: factorization homology descent. The subsection below makes that passage explicit.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:4799](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4799) — PROBLEM: `We now make each entry in the table explicit` is filler transition language. FIX: replace it with `The next examples realize the table entry by entry: Heisenberg is quadratic, affine is cubic, $\beta\gamma$ is quartic on the contact slice, and Virasoro is non-polynomial.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:4927](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4927) — PROBLEM: `We now prove` is another AP109 signpost. FIX: replace it with `The direct definition above still needs a geometric source: the next theorem identifies the potential as the generating function of a Lagrangian in a shifted cotangent chart.`

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2928](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2928) — PROBLEM: the table uses forbidden `---` as a placeholder in the Heisenberg row. FIX: replace `---` with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2930](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2930) — PROBLEM: the free-fermion row uses two forbidden `---` placeholders. FIX: replace both with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2932](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2932) — PROBLEM: the lattice row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2936](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2936) — PROBLEM: the `\beta\gamma` row uses two forbidden `---` placeholders. FIX: replace both with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2941](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2941) — PROBLEM: the `\widehat{\mathfrak{sl}}_2` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2943](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2943) — PROBLEM: the `\widehat{\mathfrak{sl}}_3` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2945](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2945) — PROBLEM: the `\widehat{G}_2` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2947](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2947) — PROBLEM: the `\widehat{E}_8` row uses forbidden `---` in the `c_*` column. FIX: replace it with `\text{n/a}`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:2417](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2417) — PROBLEM: missing punctuation leaves `\lambda_g$ At $k=-h^\vee$` as a broken sentence. FIX: change it to `\lambda_g$. At $k = -h^\vee$, ...` or `\lambda_g$; at $k = -h^\vee$, ...`.

- [LOW] [chapters/theory/higher_genus_complementarity.tex:5366](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5366) — PROBLEM: there is a stray space before the semicolon, and the clause is padded by vague prose. FIX: replace `via the shift by $d_g$ ; the two sides of the holographic decomposition see genuinely different spectral data.` with `via the shift by $d_g$; the two sides of the holographic decomposition carry distinct spectral data.`

## Summary
Checked: 6105 | Findings: 30 | Verdict: FAIL
tokens used
239,793
