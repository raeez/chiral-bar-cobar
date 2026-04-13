# F10_prerequisites_MC1_5 (1297s)

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:1937 — PROBLEM: Theorem `thm:pbw-propagation` assumes only hypotheses `(a)–(b)` of `thm:pbw-universal-semisimple` but concludes full `MK3`, even though `thm:pbw-universal-semisimple` explicitly says at 1741–1744 and 1808–1811 that `(a)–(b)` give only `E_3`-page enrichment death and leave later-page/extension analysis separate unless `(c)` is added. FIX: Either add hypothesis `(c)` to `thm:pbw-propagation`, or weaken its conclusion to “the enrichment dies by `E_3`, reducing `MK3` to later-page/extension analysis”; then rewrite every downstream sentence that calls `MK3` redundant under `(a)–(b)`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:1883 — PROBLEM: Proposition `prop:hook-pbw` proves `(a)–(b)` for all hook types and `(c)` only when `r \le N-3`, but its last sentence claims unconditionally that `MC1` implies `MK3` for the whole family. The boundary case `r=N-2` is not covered. FIX: Split the conclusion: for `r \le N-3`, cite `thm:pbw-universal-semisimple(c)` for full `MK3`; for `r=N-2`, state only the `E_3`-page enrichment-killing package and leave later pages/extensions open or separately proved.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2041 — PROBLEM: Remark `rem:pbw-propagation-scope` says affine Kac–Moody satisfies hypotheses `(a)–(b)`, but `thm:pbw-allgenera-km` at 1251–1253 explicitly says it does not use `thm:pbw-universal-semisimple` because the Sugawara stress tensor is composite, not a generator. The chapter is using two incompatible meanings of hypothesis `(b)`. FIX: Either remove affine Kac–Moody from this family list, or restate hypothesis `(b)` to require a unique weight-2 conformal field acting by `T_{(1)}=L_0` rather than a chosen generator; then reconcile `thm:pbw-allgenera-km` with that revised wording.
- [HIGH] chapters/connections/concordance.tex:4911 — PROBLEM: The concordance propagates the broken stronger version of PBW propagation, saying `MK3` follows from `MK1` for all positive-grading unique-weight-2 CFT-type algebras and citing `thm:pbw-propagation`. That summary inherits the target theorem’s overclaim. FIX: After repairing `thm:pbw-propagation`, rewrite this block to match the repaired statement: either add hypothesis `(c)` here as well, or downgrade the claim to `E_3`-page enrichment death plus a remaining later-page/extension step.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3336 — PROBLEM: Theorem `thm:universal-theta` states existence of a cyclic `L_\infty` algebra `\Defcyc(\cA)` and an MC element in `\Defcyc(\cA)\widehat{\otimes}R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`, but its proof only constructs `\Theta_\cA=D_\cA-d_0` on the bar-coderivation dg Lie side, never cites the theorem that constructs `\Defcyc(\cA)` (`thm:cyclic-linf-graph`), and then appeals to `thm:mc2-bar-intrinsic`, whose proved target is `\Defcyc(\cA)\widehat{\otimes}\Gmod` at 3555–3556, not the `R\Gamma` target written here. FIX: Add an explicit first step citing `thm:cyclic-linf-graph`; then either restate the theorem with target `\Defcyc(\cA)\widehat{\otimes}\Gmod` to match the proved construction, or insert a cited comparison/quasi-isomorphism `\Gmod \simeq R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` and transport `\Theta_\cA` across it.
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:3797 — PROBLEM: The scalar-trace part of `thm:mc2-bar-intrinsic` is circular. Its proof cites `thm:genus-universality`, but `thm:genus-universality` in `higher_genus_foundations.tex:5384–5407` derives its scalar lane from “the scalar part of the Maurer–Cartan element,” and `higher_genus_foundations.tex:791–800` explicitly imports `thm:mc2-bar-intrinsic` to define that MC element. The scalar clause is not independently established. FIX: Remove `thm:genus-universality` from the proof of `thm:mc2-bar-intrinsic` and prove the scalar trace directly from the bar-intrinsic differential, or demote part `(ii)` to a later corollary that depends on genus universality only after MC2 is already proved independently.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3819 — PROBLEM: The Verdier part of `thm:mc2-bar-intrinsic` is type-inconsistent. The proof first states `\mathbb D_{\Ran}\barB^{\mathrm{full}}_X(\cA)\simeq(\cA^!)_\infty` and explicitly calls the target a factorization algebra, then immediately says this sends the total bar coderivation `D_\cA` to `D_{\cA^!}`. That identifies a bar-coderivation on a coalgebra with the differential of a different object without a comparison theorem. FIX: Rewrite part `(iv)` in two steps: transport `D_\cA` to the differential on `(\cA^!)_\infty` under `MK:verdier`, then cite or prove a separate comparison identifying that transported differential with the bar-side `D_{\cA^!}`; if no such comparison is available, weaken the theorem to the transported Verdier statement and delete `\mathbb D(\Theta_\cA)=\Theta_{\cA^!}`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:7818 — PROBLEM: `thm:mc2-conditional-completion` says `prop:one-channel-verdier-criterion` “constructs the opposite one-channel Koszul line from the complementarity relation.” It does not. At 5500–5563 that proposition is only an equivalence criterion assuming the lines already exist. FIX: Replace the sentence beginning at 7817 with a conditional statement: Verdier compatibility follows once a `\sigma`-stable Verdier-nondegenerate plane `L_g \oplus L_g^!` is supplied; cite `prop:one-channel-verdier-criterion` only for that reduction. If construction from complementarity is intended, add a new proposition proving that construction and cite it instead.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:7965 — PROBLEM: Corollary `cor:scalar-saturation` claims the MC equation is automatic because `s^{-1}\eta` has odd degree and graded antisymmetry forces `l_n^{tr}(\eta,\ldots,\eta)=0` for `n\ge2`. That is false: repeated odd inputs do not vanish by graded antisymmetry in general. FIX: Delete lines 7965–7969. Keep only the one-dimensionality conclusion `\Theta^{\min}=\eta\otimes\Gamma_\cA`, and cite `thm:mc2-bar-intrinsic` or `thm:universal-theta` for actual MC existence instead of deriving it from parity.
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:9660 — PROBLEM: `thm:tautological-line-support` assumes only `MC2-1`, but Step 1 immediately uses the one-channel hypothesis `H^2(\Defcyc(\cA),l_1)\cong\mathbb C` via `cor:one-dim-obstruction`, which is not in the theorem statement. Step 2 then identifies `o_g` with `\mathrm{obs}_g` without a cited comparison theorem, and 9672–9676 equate a degree-2 form `\omega_g` with the top Chern class `\lambda_g` in all genera without a justified class-level bridge. FIX: Add the missing one-channel hypothesis explicitly to the theorem statement; replace “`\mathrm{obs}_g` and `o_g` are two names for the same geometric class” with a cited comparison proposition or downgrade the all-genera claim to genus 1 only; and remove the displayed form-level identification as a proof of `\lambda_g`, replacing it with a cited Hodge-class theorem or `thm:genus-universality` once the circularity is repaired.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:20537 — PROBLEM: `\ref{sec:landscape-census}` is undefined; the live label in `chapters/examples/landscape_census.tex` is `\label{ch:landscape-census}` at line 2. FIX: Change the reference to `Chapter~\ref{ch:landscape-census}` or add a real `sec:landscape-census` label to the cited section and use that label consistently.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:26919 — PROBLEM: `\ref{def:glcm-classification}` is undefined. The live local definition is `\label{def:shadow-depth-classification}` at line 16192. FIX: Replace `\ref{def:glcm-classification}` with `\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:32895 — PROBLEM: `\eqref{comp:sl2-kappa}` is undefined. The live formula is `\label{eq:sl2-kappa-decomp-genus2}` in `chapters/examples/genus_expansions.tex:987`. FIX: Replace `\eqref{comp:sl2-kappa}` with `\eqref{eq:sl2-kappa-decomp-genus2}`.
- [MEDIUM] main.tex:1686 — PROBLEM: Placeholder labels duplicate live theorem labels: `thm:master-theta` and `thm:master-pbw` are also defined at `chapters/connections/editorial_constitution.tex:194,220` and `chapters/connections/outlook.tex:663–664`. References from `higher_genus_modular_koszul.tex:3356` and `28884` therefore resolve against a non-unique label surface. FIX: Delete the duplicate placeholder labels in `main.tex` and `outlook.tex` or rename them to unique non-live aliases; keep the `editorial_constitution.tex` theorem labels as the single canonical definitions.
- [LOW] chapters/theory/higher_genus_modular_koszul.tex:3497 — PROBLEM: The proof of `prop:curvature-centrality-general` cites “Theorem `thm:genus-graded-koszul`, Step 4,” but the proof of `thm:genus-graded-koszul` at 344–352 has no Step 4. FIX: Delete that parenthetical or replace it with a valid pinpoint citation.

**MC1-MC5 DAG**
- `MC1 = thm:master-pbw` (`editorial_constitution.tex:193–215`) depends on `thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, and `thm:pbw-allgenera-principal-w`; `thm:pbw-universal-semisimple` is the shared helper for the Virasoro/finite-type `\mathcal W` lane. Dependency status: the family theorems exist, but the chapter’s stronger `(a)–(b) => MK3` propagation route is unsound as written. Circular chain seen: none.
- `MC2 = thm:master-theta` (`editorial_constitution.tex:218–237`) is routed through `thm:universal-theta` and `thm:mc2-bar-intrinsic`, with explicit dependencies on `thm:cyclic-linf-graph`, `prop:geometric-modular-operadic-mc`, `thm:genus-universality`, and `MK:verdier`. Dependency status: not satisfied as written; the scalar-trace leg is circular and the Verdier leg is type-mismatched. Circular chain seen: yes, `thm:mc2-bar-intrinsic -> thm:genus-universality ->` scalar-MC package using `thm:mc2-bar-intrinsic`.
- `MC3` is recorded in `concordance.tex:1850–1862` and `3278–3290` as depending on `thm:categorical-cg-all-types` and `cor:dk23-all-types`, with type-A strengthening through `thm:shifted-prefundamental-generation` and `thm:pro-weyl-recovery`. Dependency status: evaluation-generated core proved; DK-4/5 extension/completion beyond that core remains open. Circular chain seen: none in the read surface.
- `MC4` is recorded in `concordance.tex:1904–1926` and `editorial_constitution.tex:171–176,356–371` as depending on `thm:completed-bar-cobar-strong`, `lem:degree-cutoff`, `thm:mc-twisting-closure`, `thm:completed-twisting-representability`, and `thm:coefficient-stability-criterion`, with an explicit `MC1 -> MC4` edge via `thm:uniform-pbw-bridge` (`bar_cobar_adjunction_curved.tex:1977–2000`). Dependency status: the formal completion framework is proved; family-specific H-level target identification remains separate. Circular chain seen: none.
- `MC5` is recorded in `concordance.tex:1943–1959` and `3297–3305` as depending on `thm:general-hs-sewing`, `thm:algebraic-string-dictionary`, and `thm:bv-bar-coderived`, with the genuswise chain-level identification left at `conj:v1-master-bv-brst`. `editorial_constitution.tex:565–653` adds the downstream edge `(MC3 + realized MC4) -> standard-tower MC5 reduction`. Dependency status: analytic and coderived lanes are proved; the chain-level package is still open/conjectural. Circular chain seen: none, but the DAG is not closed because one edge is still conjectural.

## Summary
Checked: 13 | Findings: 15 | Verdict: FAIL


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
session id: 019d8648-99c5-74f0-9407-a9a94ad246cd
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_modular_koszul.tex

For MC1-MC5: trace the dependency DAG. Which theorems depend on which? Is each dependency satisfied? Are there circular chains? List the complete DAG.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Planning file audit**

I need to build or grep references and check for theorem dependency metadata. The request is for an exhaustive audit of one file, which means I'll have to verify every claim based on the actual content I read. I can use explorer subagents to search through the code and gather necessary skills. I might need to implement parallel file reads and use rg, ensuring I send out a commentary update before I start exploring.
codex
Auditing [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex) as a dependency-grounded hostile review. I’m reading the mandated repo-wide sources first, then I’ll trace MC1-MC5 through the actual labels, citations, and proof dependencies before I write any findings.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

thinking
**Exploring required skills**

I need to utilize my skills effectively. I’m thinking about checking SKILL.md for deep-beilinson-audit insights. I’m also considering what output format might be necessary, so I want to ensure I open the document to gather the right information. It’s important for me to process this with care to get everything I need to produce a useful result. Let's make sure I'm examining all the relevant details!
codex
Repo-wide invariants are loaded. Next I’m reading the audit skill and the target chapter’s local structure, then I’ll build the MC1-MC5 dependency graph from labels and proof blocks instead of relying on theorem folklore.
exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC1|MC2|MC3|MC4|MC5|\\\\label\\{|\\\\begin\\{theorem\\}|\\\\begin\\{proposition\\}|\\\\begin\\{lemma\\}|\\\\begin\\{conjecture\\}|\\\\ClaimStatus|\\\\ref\\{\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 exited 2 in 52ms:
rg: regex parse error:
    (?:MC1|MC2|MC3|MC4|MC5|\label\{|\begin\{theorem\}|\begin\{proposition\}|\begin\{lemma\}|\begin\{conjecture\}|\ClaimStatus|\ref\{)
                           ^^
error: unrecognized escape sequence

thinking
**Inspecting the file**

I need to inspect the file using `rg` with fixed strings or escaped. I probably need the whole file around labels MC1-MC5. Maybe I'll use `rg` for locating the labels or consider manual reading with `sed` for relevant parts. I need to audit the foundation chapter, which could be huge. I'll search for the MC1-MC5 labels and related claims, running `rg` focused on the string "MC1" with line numbers. Let's explore parallel commands for structure!
codex
I’ve confirmed the audit workflow. The next pass is purely structural: isolate every MC1-MC5 block, its status tag, and every explicit citation/ref inside each proof so the dependency DAG is evidence-based rather than reconstructed from memory.
exec
/bin/zsh -lc "rg -n -F 'MC2' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC1' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3356:This is Theorem~\ref{thm:master-theta} (MC2).
3501:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3527:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3530:\index{MC2!bar-intrinsic proof}
3531:\index{MC2!full generality}
3583:\begin{remark}[Scope of MC2 in this chapter]
3584:\index{MC2!coinvariant scope}
3585:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3854:\index{MC2!foundational dependency chain}
3907:\index{MC2!bar-intrinsic perspective}
3908:\index{MC2!two regimes}
3909:Theorem~\ref{thm:mc2-bar-intrinsic} resolves MC2: the universal
4070:\index{MC2!functoriality|textbf}
4661:\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
4671:MC2-1 resolved for KM by Theorem~\ref{thm:mc2-1-km}.
4743: of the MC2 package at Step~1.
4762: All MC2 Step-$1$--$3$ computations are verified for
4773: The MC2 kappa extraction is therefore \emph{universal across ranks},
4779: The MC2 pipeline is verified for
4938:The reduction above no longer records MC2 as a live open problem. It isolates
 succeeded in 51ms:
1883:In particular, \textup{MC1} implies \textup{MK3} unconditionally
exec
/bin/zsh -lc "rg -n -F 'MC3' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC4' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC5' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4957:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
28638: MC5 sewing
29384: & MC5 sewing
31842:\index{MC5!genus chain}
 succeeded in 53ms:
903:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
1922:stage; the completed MK3 statement is part of the MC4 package.
4957:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
 succeeded in 53ms:
4957:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
Plan update
Hostile audit focused on the target chapter and the MC1-MC5 dependency package. I’m separating structural dependency tracing from proof validation so findings are grounded in exact local blocks and imported hypotheses.
  ✓ Load repo-wide constitutional sources and audit workflow
  → Map MC1-MC5 labels, local theorem blocks, and explicit dependency references in higher_genus_modular_koszul.tex
  • Read cited proof blocks and imported dependencies to test status, hidden hypotheses, and circularity
  • Assemble exact findings with file:line, exact fixes, and a complete MC1-MC5 DAG

thinking
**Exploring target file**

I think I need to inspect the target file, focusing on the sections that revolve around main conjectures, particularly MC1 and MC2. I might want to examine later references as well. I suspect MC1 could be relevant to the theorem on master-scalar, so I’ll do a search. I might use a tool like rg to find "master" labels to help narrow down what I need. This feels like a solid plan!
exec
/bin/zsh -lc "rg -n '"'^'"\\\\(begin\\{theorem\\}|begin\\{proposition\\}|begin\\{lemma\\}|begin\\{conjecture\\}|label\\{|ClaimStatus)' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
236:\begin{proposition}[MCG-equivariance of the genus tower; \ClaimStatusProvedHere]
237:\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
324:\begin{theorem}[Genus-graded Koszul duality; \ClaimStatusProvedHere]
325:\label{thm:genus-graded-koszul}\label{thm:genus-graded-koszul-duality}\label{thm:extended-koszul}
355:\begin{lemma}[Genus-graded Koszul complex resolution; \ClaimStatusProvedHere]
356:\label{lem:genus-graded-koszul-resolution}
388:\label{rem:master-diagram-higher-genus}
416:\label{subsec:modular-koszul-definition}
665:\label{rem:extended-axiom-schema}
686:\begin{proposition}[Free-field examples are modular pre-Koszul; \ClaimStatusProvedHere]
687:\label{prop:standard-examples-modular-koszul}
728:\begin{proposition}[Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul; \ClaimStatusProvedHere]
729:\label{prop:conditional-modular-koszul}
770:\begin{theorem}[PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
771:\label{thm:pbw-allgenera-principal-w}
906:\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
907:\label{thm:pbw-genus1-km}
1220:\label{cor:unconditional-genus1-km}
1244:\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
1245:\label{thm:pbw-allgenera-km}
exec
/bin/zsh -lc "rg -n -F 'universal-theta' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'master-' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'master scalar' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
672:(Theorem~\ref{thm:universal-theta}).
2487:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2500: (Theorem~\ref{thm:universal-theta}):
2548:and~\ref{thm:universal-theta}).
2642:Theorem~\ref{thm:universal-theta}, made unconditional by
2661:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
3332:\label{thm:universal-theta}
3404:Theorem~\ref{thm:universal-theta} extends the canonical twisting
4663:The proof of Theorem~\ref{thm:universal-theta} assembles:
5197:Theorem~\ref{thm:universal-theta}. Then:
7796:In particular, Theorem~\ref{thm:universal-theta}
7854:Theorem~\textup{\ref{thm:universal-theta}} with the stated scalar
7891: $\Theta_{\cA}$ of Theorem~\ref{thm:universal-theta};
7904:modular-operadic clutching identities. Theorem~\ref{thm:universal-theta}
7914:$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
9722:Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
9790:(Theorem~\ref{thm:universal-theta}) is established
13953:(Theorem~\ref{thm:universal-theta}). By
 succeeded in 51ms:
106: (Proposition~\ref{prop:master-equation-from-mc}), the
388:\label{rem:master-diagram-higher-genus}
903:(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2664:See Table~\ref{tab:master-invariants}.
3356:This is Theorem~\ref{thm:master-theta} (MC2).
8266:Theorem~\ref{thm:master-commutative-square}).
8286: (Theorem~\ref{thm:master-commutative-square}), the
10167:\textup{(}Theorem~\textup{\ref{thm:quantum-master-equation})} is
12359:\label{prop:master-equation-from-mc}
12364:(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
12486:arguments (linearity in~$t$ and the master-equation recursion).
12975:(Theorem~\ref{thm:convolution-master-identification},
13318: \label{eq:primitive-master-equation}
13402:The primitive master equation~\eqref{eq:primitive-master-equation}
13437:master equation~\eqref{eq:primitive-master-equation}, projected to
13497:equation~\eqref{eq:primitive-master-equation}
13511:\label{def:reduced-branch-master-action}
13546:\label{eq:branch-master-action}
13567:\label{prop:branch-master-equation}
13581:equation~\eqref{eq:primitive-master-equation}: it is obtained by
 exited 1 in 52ms:


thinking
**Inspecting file sections**

I need to inspect the beginning of the file to understand the MC1 and possibly the master theorem definitions. I’m thinking of checking around lines 1-450, then some later sections. It seems better to focus on targeted reading instead of looking through everything. Using `sed -n` could help narrow it down. I might also want to utilize the theorem registry, but I’m cautious because the output could be large. Checking the first 500 lines and specific theorem sections sounds like a solid plan!
exec
/bin/zsh -lc "sed -n '650,2100p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,500p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2450,3410p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
ordered-factorization open problem.
\end{remark}

\begin{remark}[Logical structure]\label{rem:mk-axiom-relations}
The definition separates \emph{hypotheses} (MK1--MK3) from
\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
There is no circularity. The dg axioms MK1--MK3 present the homotopy axioms
\ref{MK:koszul-htpy}, \ref{MK:verdier-htpy},
and~\ref{MK:modular-htpy} of
Definition~\ref{def:modular-koszul-homotopy}. For simple Lie
symmetry, Lemma~\ref{lem:mk67-from-mc2} adds MK6--MK7 as theorematic
consequences without enlarging the antecedent axiom list.
\end{remark}

\begin{remark}[Extended consequences and remaining ordered extension problem]
\label{rem:extended-axiom-schema}
\index{modular Koszul chiral algebra!extended axioms}
Three further consequences:
\begin{enumerate}[label=\textup{(MK\arabic*)},start=6]
\item\label{MK:mc-control}
 succeeded in 51ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.

 succeeded in 50ms:
\begin{definition}[Scalar modular characteristic package]
\label{def:modular-characteristic-package}
\label{def:scalar-modular-package}
\index{modular characteristic package!scalar|textbf}
Let $\cA$ be a modular Koszul chiral algebra
(Definition~\ref{def:modular-koszul-chiral}). The
\emph{scalar modular characteristic package} of~$\cA$ consists of:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The \emph{obstruction invariant}
 $\kappa(\cA) \in \mathbb{C}$, the scalar controlling genus-$1$
 fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
 (Theorem~\ref{thm:genus-universality}).
\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
 of free energies determined by the bar complex at genus~$g$
 (Theorem~\ref{thm:universal-generating-function}).
\end{enumerate}
Both components are established. The Heisenberg specialization
appears in Chapter~\ref{ch:heisenberg-frame},
Definition~\ref{def:frame-modular-package}.


thinking
**Evaluating output truncation**

It looks like my output was truncated because it was too lengthy. I need to focus more on details about PBW propagation and the locality principle. I'll need the exact lines that have issues, so I may need to open line numbers later. I should check the MC2 section starting around line 3330 and then look into reduction or completion from line 4660 onwards. Using sed on those areas could be necessary.
codex
The file is heavily self-advertising as “proved here,” so the audit now shifts from surface claims to proof wiring. I’m reading the MC2 construction block, then the reduction/completion package that claims to collapse the gauntlet, because that is where circularity and hidden imports usually hide.
exec
/bin/zsh -lc "sed -n '3330,4090p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4610,5515p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
\label{thm:universal-theta}
\index{universal Maurer--Cartan class|textbf}
For every modular Koszul chiral algebra~$\cA$ on a smooth
projective curve~$X$ with non-degenerate invariant form,
there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
universal Maurer--Cartan class
\[
\Theta_{\cA} \in
\operatorname{MC}\!\bigl(
 \Defcyc(\cA) \;\widehat{\otimes}\;
 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
\bigr)
\]
such that:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the genus-$1$ component of its scalar trace is
 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
 the full scalar trace is
 succeeded in 52ms:

\begin{remark}[Two-channel decomposition of \texorpdfstring{$\Theta$}{Theta}]
\label{rem:theta-two-channel}
\index{universal Maurer--Cartan class!two-channel decomposition}
The scalar $\kappa$ decomposes into OPE channels
(Corollary~\ref{cor:km-cyclic-deformation}):
\[
\kappa(\widehat{\mathfrak{g}}_k)
\;=\;
\underbrace{\frac{\dim\mathfrak{g}\cdot k}{2h^\vee}}_{\text{double-pole}}
\;+\;
\underbrace{\frac{\dim\mathfrak{g}}{2}}_{\text{simple-pole}}.
\]
The curvature channel ($k$-dependent, $\propto C_2$) vanishes at
$k=-h^\vee$; the central extension channel persists.
The chain-level $\Theta$ carries both as separate coderivation
components.
\end{remark}

\begin{remark}[$\cW_3$ channel decomposition of $\kappa$]
exec
/bin/zsh -lc "sed -n '5500,7835p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7830,9755p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proposition}[One-channel Verdier/Koszul criterion;
\ClaimStatusProvedHere]\label{prop:one-channel-verdier-criterion}
\index{MC2!one-channel Verdier/Koszul criterion}
Let
\[
V_g \;:=\; H^*\!\bigl(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)\bigr)
\]
with Verdier pairing $\langle-,-\rangle_{\mathbb{D}}$ and involution
$\sigma$ as in Proposition~\ref{prop:lagrangian-eigenspaces}. Let
$L_g \subset Q_g(\cA)$ and $L_g^! \subset Q_g(\cA^!)$ be
one-dimensional lines.
Then the following are equivalent:
\begin{enumerate}[label=\textup{(\roman*)}]
\item there exists a $\sigma$-stable two-dimensional subspace
 $E_g \subset V_g$ such that
 \[
 E_g \;=\; L_g \oplus L_g^!
 \]
 and the restriction of $\langle-,-\rangle_{\mathbb{D}}$ to $E_g$ is
 non-degenerate;
 succeeded in 52ms:
For any Koszul chiral algebra $\cA$ on a smooth projective
curve~$X$ with non-degenerate invariant form and simple Lie
symmetry~$\mathfrak{g}$ on the proved uniform-weight lane, all
three hypotheses of
Theorem~\textup{\ref{thm:mc2-conditional-completion}} are satisfied:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{MC2-1}: $\Defcyc(\cA)$ is a complete cyclic
 $L_\infty$-algebra, by
 Theorem~\textup{\ref{thm:cyclic-linf-graph}} \textup{(}chiral
 graph complex construction, using the Fay trisecant identity of
 Proposition~\textup{\ref{prop:fay-trisecant}} and the Stokes
 regularity of
 Proposition~\textup{\ref{prop:stokes-regularity-FM}}\textup{)}.
\item \emph{MC2-2}: The completed tensor product
 $\Defcyc(\cA) \widehat{\otimes} \Gmod$ converges and carries
 modular-operadic clutching morphisms, by
 Proposition~\textup{\ref{prop:geometric-modular-operadic-mc}}.
\item \emph{MC2-3}: The genus-$g$ obstruction class lies on the
 tautological line, by
 Theorem~\textup{\ref{thm:tautological-line-support}}.

thinking
**Searching for theorem definitions**

I’m trying to gather more information regarding MC1, especially since the user asked specifically about MC1-MC5 in the context of a Directed Acyclic Graph (DAG). I’ll look for where MC1 and MC3-5 are defined, and I’m considering searching for “master-” to see if there are related master theorems in the document. It might be helpful to pinpoint specific lines and dependencies, so I’ll use a tool to search for “master” or “MC1.”
codex
MC2 is clear now: there are two competing proof stories in the same file, and they are not obviously aligned. I’m tracing MC1/MC3/MC4/MC5 next so the final DAG captures where the chapter genuinely proves something and where it only gestures to later chapters or conditional packages.
exec
/bin/zsh -lc "rg -n -F '(MC1' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC1' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC3' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
1883:In particular, \textup{MC1} implies \textup{MK3} unconditionally
 succeeded in 51ms:
4957:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
exec
/bin/zsh -lc "rg -n -F 'MC4' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC5' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
903:(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
1922:stage; the completed MK3 statement is part of the MC4 package.
4957:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
 succeeded in 52ms:
4957:Chapter~\ref{chap:concordance}: MC3, then MC4, then MC5; periodicity
28638: MC5 sewing
29384: & MC5 sewing
31842:\index{MC5!genus chain}

thinking
**Searching for theorem labels**

I see that I need to look for mentions of labels related to the MC1 theorem, which might also be referred to as master-pbw. I'll check the repository for instances of these labels, especially since the user is focused on auditing files and tracing the dependency DAG for MC1 to MC5. It's probably a good idea to look in the chapters for corresponding theorem labels as well, searching for terms like "master-" or "thm:master-pbw." Let's see what I can find!
exec
/bin/zsh -lc "rg -n 'label\\{thm:master-["'^}]+'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -F 'master-theta' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'master-pbw' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'master-' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
28884:By PBW concentration (Theorem~\ref{thm:master-pbw}),
 succeeded in 51ms:
106: (Proposition~\ref{prop:master-equation-from-mc}), the
388:\label{rem:master-diagram-higher-genus}
903:(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
2664:See Table~\ref{tab:master-invariants}.
3356:This is Theorem~\ref{thm:master-theta} (MC2).
8266:Theorem~\ref{thm:master-commutative-square}).
8286: (Theorem~\ref{thm:master-commutative-square}), the
10167:\textup{(}Theorem~\textup{\ref{thm:quantum-master-equation})} is
12359:\label{prop:master-equation-from-mc}
12364:(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
12486:arguments (linearity in~$t$ and the master-equation recursion).
12975:(Theorem~\ref{thm:convolution-master-identification},
13318: \label{eq:primitive-master-equation}
13402:The primitive master equation~\eqref{eq:primitive-master-equation}
13437:master equation~\eqref{eq:primitive-master-equation}, projected to
13497:equation~\eqref{eq:primitive-master-equation}
13511:\label{def:reduced-branch-master-action}
13546:\label{eq:branch-master-action}
13567:\label{prop:branch-master-equation}
13581:equation~\eqref{eq:primitive-master-equation}: it is obtained by
 succeeded in 51ms:
3356:This is Theorem~\ref{thm:master-theta} (MC2).

thinking
**Searching for definitions**

I’m considering that maybe the term “master-pbw” isn't defined in the file. It makes sense to search the entire repository for “master-pbw/theta” to see if I can find the references I need. I might also need to look into a dependency directed acyclic graph (DAG) across different volumes. Alright, searching the repo sounds like a practical first step to gather the necessary information!
exec
/bin/zsh -lc "rg -n -F 'thm:master-theta' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{thm:master-pbw\\}|label\\{thm:master-theta\\}|label\\{thm:master-["'^}]+'"' chapters main.tex appendices metadata | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:master-pbw' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1686: \phantomsection\label{thm:master-theta}%
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/editorial_constitution.tex:450:Theorem~\textup{\ref{thm:master-theta}}, and
chapters/connections/editorial_constitution.tex:488:Theorem~\ref{thm:master-theta} (originally conjectured, now resolved
chapters/connections/editorial_constitution.tex:549:Theorem~\ref{thm:master-theta} $\to$ Futures~3, 4;
chapters/connections/editorial_constitution.tex:594: Theorem~\ref{thm:master-theta}.
chapters/connections/editorial_constitution.tex:652:Theorem~\ref{thm:master-theta}, compatibly with truncation, Verdier
chapters/connections/editorial_constitution.tex:684: Theorem~\ref{thm:master-theta}.
chapters/connections/editorial_constitution.tex:800:MC2 & \textbf{Proved} (Thm~\ref{thm:master-theta})
chapters/connections/editorial_constitution.tex:1558: $\Theta_{\cA}$ (Theorem~\ref{thm:master-theta}).
chapters/connections/concordance.tex:5424:(Theorem~\ref{thm:master-theta}).
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/theory/higher_genus_modular_koszul.tex:3356:This is Theorem~\ref{thm:master-theta} (MC2).
chapters/theory/fourier_seed.tex:1038:(Theorem~\ref{thm:master-theta}).
 succeeded in 51ms:
main.tex:1686: \phantomsection\label{thm:master-theta}%
main.tex:1687: \phantomsection\label{thm:master-pbw}%
main.tex:1725: \phantomsection\label{thm:master-tower}%
chapters/examples/deformation_quantization.tex:607:\begin{theorem}[Master identity \cite{Kon03}; \ClaimStatusProvedElsewhere]\label{thm:master-identity-deformation}
chapters/examples/w_algebras_deep.tex:1424:\label{thm:master-commutative-square}
chapters/connections/master_concordance.tex:39:\label{thm:master-seven-face}
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/genus_complete.tex:235:\begin{theorem}[Master tower of extensions; \ClaimStatusProvedHere]\label{thm:master-tower}
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
 succeeded in 51ms:
appendices/combinatorial_frontier.tex:119:\emph{The data is level-independent.} For every algebra in the table, the bar cohomology dimensions are independent of the level~$k$ (or central charge~$c$) at generic values. This is a deep consequence of the PBW spectral sequence structure: the $E_1$ page is a Lie algebra cohomology computation that depends only on the underlying finite-dimensional data $(\mathfrak{g}, \dim\mathfrak{g}, h^\vee)$, not on the level (this follows from the PBW spectral sequence: at generic level the $E_2$ page is level-independent, and concentration at $E_2$ gives the result; see Theorem~\ref{thm:master-pbw}). The level enters only through the curvature term $\omega_g$ at genus $g \geq 1$, which affects the genus expansion (Theorem~\ref{thm:genus-universality}) but not the bar cohomology dimensions themselves.
main.tex:1687: \phantomsection\label{thm:master-pbw}%
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1152: \textup{(}Theorem~\textup{\ref{thm:master-pbw})},
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/theory/higher_genus_modular_koszul.tex:28884:By PBW concentration (Theorem~\ref{thm:master-pbw}),
chapters/theory/bar_cobar_adjunction_inversion.tex:3885:(Theorem~\ref{thm:master-pbw}). The Virasoro algebra has a
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:24:(Theorems~\ref{thm:master-pbw},
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:449:downstream of Theorem~\textup{\ref{thm:master-pbw}},
chapters/connections/editorial_constitution.tex:477:Theorem~\ref{thm:master-pbw} is the \emph{entry theorem}: together
chapters/connections/editorial_constitution.tex:548:Theorem~\ref{thm:master-pbw} $\to$ Future~2;
chapters/connections/editorial_constitution.tex:798:MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
exec
/bin/zsh -lc "rg -n 'MC[1-5]' chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex main.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,280p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/concordance.tex:1319:\item The one-slot obstruction constrains the MC3 categorical lift:
chapters/connections/concordance.tex:1353: status; the proved core (Theorems~A--D,\,H, MC2) is unaffected.
chapters/connections/concordance.tex:1358:is MC2 (proved by the bar-intrinsic construction,
chapters/connections/concordance.tex:1655:\item \emph{Zero risk}: Theorems~A--D,\,H, MC2 bar-intrinsic
chapters/connections/concordance.tex:1820:\item The MC3 categorical lift
chapters/connections/concordance.tex:1838:\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
chapters/connections/concordance.tex:1842: MC1 (PBW concentration) holds unconditionally for universal
chapters/connections/concordance.tex:1850:\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
chapters/connections/concordance.tex:1862:which is downstream of MC3. The
chapters/connections/concordance.tex:1883:\begin{construction}[MC3 status by Dynkin type]
chapters/connections/concordance.tex:1885:\index{MC3!status by type|textbf}
chapters/connections/concordance.tex:1886:\index{Dynkin type!MC3 status}
chapters/connections/concordance.tex:1887:\textbf{MC3 is proved for all simple types on the
chapters/connections/concordance.tex:1904:\item \emph{MC4}: The formal completion theory is \textbf{proved} by
chapters/connections/concordance.tex:1915: Splits into MC4$^+$ (positive towers) and MC4$^0$ (resonant).
chapters/connections/concordance.tex:1916: MC4$^+$ is \textbf{unconditionally solved} by weightwise
chapters/connections/concordance.tex:1920: completion to finite truncations. MC4$^0$ concerns algebras with
chapters/connections/concordance.tex:1924: PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1
chapters/connections/concordance.tex:1925: to MC4: uniform PBW degeneration plus quotient stabilization
chapters/connections/concordance.tex:1939: the MC4 completion radius is controlled by the same parameter
 succeeded in 51ms:
 & \textbf{Partially proved} (HS-sewing; genus-$0$ algebraic) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The historical five-master-conjecture package now consists of two
resolved load-bearing layers (the MC1 entry theorem and the MC2
universal $\Theta_\cA$ package) together with the fully resolved
MC3: \textbf{proved for all simple types} on the evaluation-generated
core. The all-types categorical prefundamental
Clebsch--Gordan closure and the DK comparison on the
evaluation-generated core are proved uniformly
\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
proves shifted-prefundamental generation and pro-Weyl recovery
\textup{(}Theorems~\ref{thm:shifted-prefundamental-generation},
\ref{thm:pro-weyl-recovery}\textup{)}. The residual DK-4/5
problem (extension and completion beyond evaluation modules;
Conjecture~\ref{conj:dk-compacts-completion}) is
exec
/bin/zsh -lc "sed -n '760,840p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5400,5460p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Proposition~\ref{prop:geometric-modular-operadic-mc} and
Theorem~\ref{thm:tautological-line-support}.
The non-scalar content is developed through the shadow
obstruction tower
(Definition~\ref{def:shadow-postnikov-tower}): finite-order
shadows through degree~$4$ are proved constructively, and the
all-degree convergence is guaranteed by the bar-intrinsic
construction (Theorem~\ref{thm:mc2-bar-intrinsic};
Theorem~\ref{thm:recursive-existence}).
One-channel line concentration is proved
for all algebras in algebraic families with rational OPE
coefficients (Theorem~\ref{thm:algebraic-family-rigidity}),
covering the entire standard Lie-theoretic landscape at
all non-critical levels including admissible ones.
The proof bypasses module-category semisimplicity via
Whitehead reduction to a finite-dimensional linear system
and algebraic semicontinuity of rank.

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~I
(existence of a homotopy object). At H-level: a filtered cyclic $L_\infty$
 succeeded in 51ms:
\item \emph{automatic Mittag--Leffler}: the surjective tower of
 finite quotients gives $\varprojlim^1 = 0$;
\item \emph{quasi-isomorphism}: the complete filtered comparison
 lemma passes finite-stage bar-cobar duality to the inverse limit.
\end{enumerate}
The completion closure $\CompCl(\Fft)$ carries a quasi-inverse
bar-cobar equivalence on the homotopy category
(Corollary~\ref{cor:completion-closure-equivalence}), stable under
MC~twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed
twisting representability
(Theorem~\ref{thm:completed-twisting-representability}). The
coefficient-stability criterion
(Theorem~\ref{thm:coefficient-stability-criterion}) reduces
verification to finite matrix stabilization, and the uniform PBW
bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1 to MC4.
The remaining example-specific task is H-level target identification
(coefficient stabilization on finite reduced-weight windows and
comparison with the named completion target).

The completion kinematics (the primitive cumulant quotient
exec
/bin/zsh -lc "rg -n -F 'thm:cyclic-linf-graph' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'def:cyclic-deformation-bar' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2545:by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
3786:(Theorem~\ref{thm:cyclic-linf-graph}), and the pronilpotent
4943:Theorem~\ref{thm:cyclic-linf-graph},
5412:Theorem~\ref{thm:cyclic-linf-graph}. The remaining MC2-3
7755: Theorem~\textup{\ref{thm:cyclic-linf-graph}} constructs the
7838: Theorem~\textup{\ref{thm:cyclic-linf-graph}} \textup{(}chiral
7862:Hypothesis~(i) is Theorem~\ref{thm:cyclic-linf-graph}, whose
 succeeded in 52ms:
447:(Definition~\ref{def:cyclic-deformation-bar}),
5192:Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
5707:Definition~\textup{\ref{def:cyclic-deformation-bar}} exist.
exec
/bin/zsh -lc "rg -n -F 'def:modular-koszul-chiral' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:genus-universality' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:recursive-existence' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
426:version; Definition~\ref{def:modular-koszul-chiral} gives the concrete
530:chosen model. Definition~\ref{def:modular-koszul-chiral} provides
535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
693:\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
796:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
924:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1270:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1453:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
1521:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
1604:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
1656:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
1939:Definition~\textup{\ref{def:modular-koszul-chiral})} and
2057:Definition~\ref{def:modular-koszul-chiral}
2455:(Definition~\ref{def:modular-koszul-chiral}). The
2636:Definition~\ref{def:modular-koszul-chiral} and
2692:(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
2926:(Definition~\ref{def:modular-koszul-chiral}) realized as the
3387:(Definition~\textup{\ref{def:modular-koszul-chiral}}); see
3818:Definition~\textup{\ref{def:modular-koszul-chiral}}
4078:Definition~\textup{\ref{def:modular-koszul-chiral})}, the
 succeeded in 51ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2461: (Theorem~\ref{thm:genus-universality}).
2568:(Theorem~\ref{thm:genus-universality}).
2756:Theorem~\ref{thm:genus-universality} identifies that trace with
2760:Theorem~\ref{thm:genus-universality}.
2761:Part~(i) is Theorem~\ref{thm:genus-universality} for
2769:Theorem~\ref{thm:genus-universality}(ii).
2833:Theorem~\ref{thm:genus-universality}; the second arrow is the
2840:Theorem~\ref{thm:genus-universality}); generating function via
3213:Theorem~\ref{thm:genus-universality}. The GUE free energy
3374:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3797:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3849:Theorem~\ref{thm:genus-universality}(ii)).
5415:(Theorem~\ref{thm:genus-universality},
7816:(Theorem~\ref{thm:genus-universality}).
7972:Theorem~\ref{thm:genus-universality} identifies the scalar trace
8120:Theorem~\ref{thm:genus-universality} identifies
8544:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
9624:Theorem~\textup{\ref{thm:genus-universality}}, then the full
9679:By Theorem~\ref{thm:genus-universality},
 succeeded in 51ms:
112: Theorem~\ref{thm:recursive-existence}:
2196: \textup{(Theorem~\ref{thm:recursive-existence})}.
3896:(Theorem~\ref{thm:recursive-existence}) then inherits
4028: (Theorem~\ref{thm:recursive-existence}).
4511:Theorem~\ref{thm:recursive-existence}).
9800:Theorem~\ref{thm:recursive-existence}).
11937:(Theorem~\ref{thm:recursive-existence}).
12663:\label{thm:recursive-existence}
12830:The logical structure of Theorem~\ref{thm:recursive-existence}
12892: \textup{(}Theorem~\textup{\ref{thm:recursive-existence})}
12927:(Theorem~\ref{thm:recursive-existence}).
13377:(Theorem~\ref{thm:recursive-existence}): for fixed $(g,n)$
14054: \textup{(}Theorem~\textup{\ref{thm:recursive-existence})}
14095:(iv)~Theorem~\ref{thm:recursive-existence} gives the
14606:element \textup{(}Theorem~\textup{\ref{thm:recursive-existence})}.
18988:(Theorem~\ref{thm:recursive-existence}): the inverse limit
21184:Theorem~\ref{thm:recursive-existence}
25189: \textup{(}Theorem~\textup{\ref{thm:recursive-existence}}\textup{)}.
25219:(ii)~By Theorem~\ref{thm:recursive-existence}, the obstruction at each stage is
27795:(Theorem~\textup{\ref{thm:recursive-existence}}).
exec
/bin/zsh -lc "sed -n '12640,12750p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{thm:cyclic-linf-graph\\}|label\\{def:cyclic-deformation-bar\\}|label\\{thm:genus-universality\\}|label\\{thm:recursive-existence\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,620p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{constr:obstruction-recursion}
Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
constructed through weight $N$. Its next obstruction is
\begin{equation}
\label{eq:next-obstruction}
\mathfrak{o}_{N+1}
:=
\Bigl(
D_{\cA}\Theta_{\cA}^{\leq N}
+ \tfrac12[\Theta_{\cA}^{\leq N},
\Theta_{\cA}^{\leq N}]
\Bigr)_{N+1}.
\end{equation}
If $[\mathfrak{o}_{N+1}] \in H^2(F^{N+1}/F^{N+2})$ vanishes,
choose a contracting homotopy $h$ and define
$\Theta_{\cA,N+1} := -h(\mathfrak{o}_{N+1})$.
Then $\Theta_{\cA}^{\leq N+1} := \Theta_{\cA}^{\leq N}
+ \Theta_{\cA,N+1}$ solves the Maurer--Cartan equation through
weight $N+1$.
\end{construction}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:12663:\label{thm:recursive-existence}
chapters/theory/chiral_hochschild_koszul.tex:1760:\label{def:cyclic-deformation-bar}
chapters/theory/chiral_hochschild_koszul.tex:2443:complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
chapters/theory/higher_genus_foundations.tex:5302:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
 succeeded in 51ms:
$Q_g(\cA^!) := H^*(\mathbf{Q}_g(\cA^!))$ recover the
deformation and obstruction spaces of
Theorem~\ref{thm:quantum-complementarity-main}.
\end{definition}

\begin{remark}[Model independence]\label{rem:model-independence}
Any two admissible dg presentations of the same factorization
object are connected by a contractible space of quasi-isomorphisms,
so the homotopy axioms \ref{MK:koszul-htpy}--\ref{MK:modular-htpy}
are invariants of the factorization algebra, not of a
chosen model. Definition~\ref{def:modular-koszul-chiral} provides
the dg model used throughout.
\end{remark}

\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
Let $X$ be a smooth projective curve over $\mathbb{C}$.
A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
the following data and satisfying the following axioms.
exec
/bin/zsh -lc "sed -n '11700,11880p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 with differential $d_0 = [D_0, -]$.
\item $E_1^{p,*} = H^*(\operatorname{gr}_F^p\, L_{\mathrm{mod}},
 d_0)$: tree-level cohomology at $p=0$, one-loop at $p=1$,
 genus-two shell data
 (Construction~\ref{const:vol1-genus-two-shells}) at $p=2$.
\item $d_1\colon E_1^{0,*}\to E_1^{1,*}$ is the genus-one
 obstruction $\operatorname{Ob}_1$
 (Construction~\ref{constr:obstruction-recursion});
 $d_r\colon E_r^{p,*}\to E_r^{p+r,*-r+1}$ encodes
 $\operatorname{Ob}_r$.
\item Completeness and pronilpotence of $F^1 L_{\mathrm{mod}}$ give
 $E_\infty^{p,q}\cong \operatorname{gr}_F^p\, H^{p+q}(L_{\mathrm{mod}})$.
\end{enumerate}
This is the spectral sequence of the Maurer--Cartan extension tower.
It is distinct from the PBW spectral sequence (which uses the
conformal-weight filtration within each fixed genus to compute bar
cohomology): the genus spectral sequence controls the
\emph{lift across genera}, and its differentials are the obstruction
maps.
\end{construction}

thinking
**Exploring Perl references**

I'm considering using Perl, and I might need to include some specific reference types like `eqref` and `cref`. I wonder if it would be better to search for `ref{` only or if I should expand my search to include `eqref`, `Cref`, and `autoref`. Maybe a good approach is to use a generic regular expression like `\\[A-Za-z]*ref\{` to capture all relevant variations. That seems like it could be effective!
codex
I’ve finished the first manual pass of the MC2 core. I’m now checking the chapter mechanically for missing labels and external dependency surfaces, because a lot of the prose claims “resolved” while quietly outsourcing key steps to other chapters.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
target=root/'chapters/theory/higher_genus_modular_koszul.tex'
text=target.read_text()
refs=[]
for m in re.finditer(r'\\\\(?:[A-Za-z]*ref|eqref)\\{(["'^}]+)'"\\}', text):
    refs.append(m.group(1))
labels=set()
for p in root.rglob('*.tex'):
    try:
        t=p.read_text()
    except Exception:
        continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', t):
        labels.add(m.group(1))
missing=sorted(set(refs)-labels)
for x in missing[:200]:
    print(x)
print('TOTAL_MISSING', len(missing))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, collections
p=pathlib.Path('chapters/theory/higher_genus_modular_koszul.tex')
text=p.read_text().splitlines()
refs=[]
for i,line in enumerate(text, start=1):
    for m in re.finditer(r'\\\\(?:[A-Za-z]*ref|eqref)\\{(["'^}]+)'"\\}', line):
        refs.append((m.group(1), i, line.strip()))
labels=collections.Counter()
for q in pathlib.Path('.').rglob('*.tex'):
    try: t=q.read_text()
    except: continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', t):
        labels[m.group(1)] += 1
# only duplicates referenced in target
seen=set()
for label, ln, line in refs:
    if labels[label] > 1 and label not in seen:
        seen.add(label)
        print(f'{label} {labels[label]}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, collections
p=pathlib.Path('chapters/theory/higher_genus_modular_koszul.tex')
text=p.read_text().splitlines()
refs=[]
for i,line in enumerate(text, start=1):
    for m in re.finditer(r'\\\\(?:[A-Za-z]*ref|eqref)\\{(["'^}]+)'"\\}', line):
        refs.append((m.group(1), i, line.strip()))
labels=collections.defaultdict(list)
for q in pathlib.Path('.').rglob('*.tex'):
    try: t=q.read_text().splitlines()
    except: continue
    for i,line in enumerate(t, start=1):
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', line):
            labels[m.group(1)].append((str(q),i))
for label, ln, line in refs:
    if label not in labels:
        print(f'{ln}: {label} :: {line[:160]}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.55s:
comp:sl2-kappa
def:glcm-classification
sec:landscape-census
thm:modular
TOTAL_MISSING 4
 succeeded in 1.53s:
def:modular-characteristic-package 52
thm:bar-modular-operad 50
thm:higher-genus-inversion 50
thm:mc2-bar-intrinsic 52
subsec:two-level-convention 52
def:shadow-algebra 53
def:modular-bar-hamiltonian 53
def:shadow-postnikov-tower 52
prop:master-equation-from-mc 52
thm:recursive-existence 54
thm:riccati-algebraicity 150
thm:single-line-dichotomy 150
thm:shadow-formality-identification 52
thm:quantum-complementarity-main 50
constr:dk-shadow-projections 50
prop:e1-shadow-r-matrix 50
thm:gz26-commuting-differentials 19
thm:gaudin-yangian-identification 19
prop:standard-examples-modular-koszul 52
thm:prism-higher-genus 50
 succeeded in 7.85s:
14778: thm:modular :: %% all genera, and the resolution of Conjecture~\ref{thm:modular}
20537: sec:landscape-census :: values appears in~\S\textup{\ref{sec:landscape-census}}.
26919: def:glcm-classification :: \textup{(}Definition~\textup{\ref{def:glcm-classification}}\textup{)}
32895: comp:sl2-kappa :: (equation~\eqref{comp:sl2-kappa}), the same value as at


thinking
**Analyzing unresolved references**

I’ve found four unresolved references which could use specific lines for clarity. Duplicate label references might be acceptable, though I wonder if all duplicates are just a result of clones across the repo. It seems a possible cause could be phantom sections in main.tex. I also need to check the provided label counts against the target file since some duplicates could impact reference stability. It sounds like I’ll need to pinpoint unresolved positions and check other related files for thoroughness.
thinking
**Examining the file's references**

The file refers to a significant line, 28884, which might be outside the audit scope. I notice that the MC1 DAG node in this chapter is not clearly defined, aside from `thm:pbw-propagation` and related theorems. I’ll need to consider the complete DAG, which includes `thm:master-pbw` from the editorial constitution, as its proof relies on three family theorems in this chapter. Since the user's focused on auditing this chapter, I’m thinking of including external nodes and their dependency edges. I’ll need to dig into those theorem proofs!
codex
I now have the first hard mechanical defects: the chapter contains four outright missing references. I’m validating whether those are isolated typos or whether they hide larger proof-routing failures in the MC package.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14768,14788p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '20528,20545p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 20528	The $\kappa$-conductor $\kappa(\cA) + \kappa(\cA^!)$ measures the
 20529	obstruction to extending complementarity
 20530	\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}
 20531	from genus~$0$ to higher genus without correction: the
 20532	cross-channel correction $\delta F_g^{\mathrm{cross}}$
 20533	\textup{(all-weight)} of
 20534	Theorem~\textup{\ref{thm:multi-generator-universality}} is
 20535	controlled by $\kappa + \kappa'$ and vanishes identically when
 20536	$\kappa + \kappa' = 0$. The full census of $\kappa$-conductor
 20537	values appears in~\S\textup{\ref{sec:landscape-census}}.
 20538	\end{proposition}
 20539	
 20540	\begin{proof}
 20541	Clause~(i): for affine Kac--Moody $V_k(\fg)$, the Feigin--Frenkel
 20542	involution $k \mapsto -(k + 2h^\vee)$ sends
 20543	$\kappa = \dim(\fg)(k + h^\vee)/(2h^\vee)$ to
 20544	$\kappa' = \dim(\fg)(-(k + 2h^\vee) + h^\vee)/(2h^\vee)
 20545	= -\kappa$, giving $\kappa + \kappa' = 0$.
 succeeded in 52ms:
 14768	$\{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ forces an
 14769	infinite tower
 14770	(Theorem~\ref{thm:w-virasoro-quintic-forced}).
 14771	All families satisfy HS-sewing
 14772	(Theorem~\ref{thm:general-hs-sewing});
 14773	analytic realization follows from
 14774	Corollary~\ref{cor:analytic-shadow-realization}.
 14775	\end{example}
 14776	
 14777	%% The $E_1$ shadow obstruction tower, the $E_1$ five main theorems at
 14778	%% all genera, and the resolution of Conjecture~\ref{thm:modular}
 14779	%% are now in Chapter~\ref{chap:e1-modular-koszul}
 14780	%% (Sections~\ref{sec:e1-shadow-tower}--\ref{sec:e1-five-theorems}).
 14781	
 14782	%% (removed: E₁ content now in Chapter~\ref{chap:e1-modular-koszul})
 14783	
 14784	
 14785	\subsection{Operadic complexity, formality, and shadow depth}
 14786	\label{subsec:operadic-complexity-shadow-depth}
 14787	
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '26910,26928p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '194,235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32886,32902p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 26910	\end{remark}
 26911	
 26912	\begin{conjecture}[Resurgent shadow classification]
 26913	\label{conj:resurgent-shadow-classification}
 26914	\ClaimStatusConjectured
 26915	\index{resurgence!shadow classification|textbf}%
 26916	\index{trans-series!G/L/C/M structure}%
 26917	\index{shadow invariants!non-perturbative}%
 26918	The G/L/C/M classification
 26919	\textup{(}Definition~\textup{\ref{def:glcm-classification}}\textup{)}
 26920	governs the non-perturbative structure of the genus expansion
 26921	$F(\hbar) = \sum_{g \geq 0} F_g(\cA)\,\hbar^{2g-2}$ as follows.
 26922	\begin{enumerate}[label=\textup{(\alph*)}]
 26923	\item \emph{Class~$\mathsf{G}$ \textup{(}Heisenberg\textup{)}.}\enspace
 26924	 The shadow discriminant vanishes: $\Delta(\cA) = 8\kappa(\cA)\,S_4(\cA) = 0$.
 26925	 The genus expansion terminates at finite order, so
 26926	 $F(\hbar)$ is a polynomial in~$\hbar$. No Borel singularities,
 26927	 no transseries sectors, no Stokes phenomena.
 26928	 The non-perturbative completion is exact.
 succeeded in 51ms:
 32886	\textup{(}cf.\ \S\ref{subsec:ell-degree2}\textup{)}.
 32887	\end{remark}
 32888	
 32889	\begin{remark}[The symmetric shadow at genus~$2$]
 32890	\label{rem:g2-shadow}
 32891	The averaging map $\av_2$ at degree~$2$ sends the
 32892	$12$-dimensional ordered de~Rham cohomology to
 32893	$\Sigma_2$-coinvariants. The scalar surviving $\av_2$ is
 32894	$\kappa = 3(k+2)/4$
 32895	(equation~\eqref{comp:sl2-kappa}), the same value as at
 32896	genus~$0$ and genus~$1$: the averaging map is a local
 32897	computation (residue extraction), independent of the global
 32898	topology.
 32899	The kernel $\ker(\av_2)$ at genus~$2$ is richer than at
 32900	genus~$1$: the four $B$-cycle monodromies contribute
 32901	independent antisymmetric classes that are invisible to the
 32902	symmetric theory.
 succeeded in 52ms:
   194	 finite-type interacting families]\label{thm:master-pbw}
   195	\ClaimStatusProvedHere{}
   196	The genus-$g$ PBW spectral sequence concentrates at all genera for the
   197	three standard finite-type interacting families treated in the proved
   198	core: affine Kac--Moody
   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
   200	Virasoro
   201	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}}\textup{)},
   202	and principal finite-type $\mathcal{W}$-algebras, including higher
   203	$\mathcal{W}_N$
   204	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}\textup{)}.
   205	
   206	\emph{This resolves MC1 for the standard finite-type interacting
   207	families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
   208	isolates the common unique-weight-$2$ $d_2$ mechanism behind the
   209	Virasoro and principal finite-type $\mathcal{W}$ arguments; for chiral
   210	algebras with semisimple Lie symmetry satisfying
   211	hypotheses~\textup{(a)--(c)}, the enrichment-killing is unconditional
   212	via Whitehead vanishing plus $L_0$ invertibility. The resolved status
   213	of MC1 for the named families rests on the family theorems above;

thinking
**Investigating editorial documents**

I’m thinking about diving into the editorial_constitution to look at theorem statuses and dependencies, particularly around line 218. I wonder if I really need all of that information, but it could help me derive a complete Directed Acyclic Graph (DAG) and understand the concordance better. I also need to check the MC3-5 status sections between lines 1838 and 1945, especially line 1943. Let's open those sections and see what I find!
exec
/bin/zsh -lc "sed -n '1830,1955p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3260,3305p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{tabular}{@{}llp{7.5cm}@{}}
\toprule
\textbf{Level} & \textbf{Formality input} & \textbf{Consequence} \\
\midrule
MC1 & PBW filtration & Genus-$0$ bar complex is formal:
 $E_2$-degeneration gives $H^*(\barB(\cA)) \cong$ quadratic dual
 (Theorem~\ref{thm:pbw-koszulness-criterion}).
 Holds unconditionally for universal algebras
 (Proposition~\ref{prop:pbw-universality}).
 For simple quotients $L_k(\fg)$ at admissible levels with
 denominator $q \geq 3$ and $\mathrm{rk}(\fg) \geq 2$,
 PBW concentration \emph{fails}: the Cartan subalgebra produces
 $\mathrm{rk}(\fg)$-dimensional bar cohomology in~$H^2$
 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}) \\
MC2 & $D^2 = 0$ & Bar-intrinsic MC element: $\Theta_\cA := D_\cA - d_0$
 is automatically MC because $D_\cA^2 = 0$
 (Theorem~\ref{thm:mc2-bar-intrinsic}).
 No homotopy correction needed \\
MC3 & Prefundamental CG & \textbf{Proved for all simple types on the evaluation-generated core}.
 All-types package~(i) is proved
 succeeded in 51ms:
\end{remark}

\begin{remark}[Three-pillar architecture and the MC open problems]
\label{rem:three-pillar-mc-unification}
\index{three-pillar architecture!MC open problems}
\index{MC open problems!three-pillar unification}
The three-pillar architecture determines the MC resolution strategy:
\begin{itemize}
\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
 element in the modular convolution $sL_\infty$-algebra; the
 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
 obstruction tower) are the constructive content.
 MC1 (PBW concentration) holds unconditionally for universal
 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
 (Proposition~\ref{prop:pbw-universality}). For simple quotients
 $L_k(\fg)$ at admissible levels, PBW concentration fails at
 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
 to $H^2(\barB)$
 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
exec
/bin/zsh -lc "sed -n '1935,1990p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \emph{Arithmetic connection}: the spectral curve of the shadow
 Higgs field
 (Theorem~\ref{thm:shadow-higgs-field}) has convergence
 radius $|c|/3$ in the degree variable;
 the MC4 completion radius is controlled by the same parameter
 $\lambda_{\mathrm{eff}} = -6/c$
 (Chapter~\ref{chap:arithmetic-shadows},
 Remark~\ref{rem:effective-coupling}).
\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
 Inductive genus
 determination, 2D convergence (no UV renormalization needed),
 analytic-algebraic comparison, and the general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
 plus subexponential sector growth implies convergence at all genera).
 Heisenberg sewing proved (Theorem~\ref{thm:heisenberg-sewing}:
 one-particle Bergman reduction, Fredholm determinant). At genus~$0$
 the algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1710,1865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1929,2050p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1710	\begin{theorem}[Universal PBW enrichment-killing for chiral
  1711	 algebras with conformal vector; \ClaimStatusProvedHere]
  1712	\label{thm:pbw-universal-semisimple}
  1713	\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
  1714	\index{PBW spectral sequence!universal semisimple enrichment-killing|textbf}
  1715	\index{modular Koszul chiral algebra!unique-weight-2 criterion|textbf}
  1716	\index{modular Koszul chiral algebra!semisimple enrichment-killing|textbf}
  1717	\textup{[Regime: curved-central
  1718	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1719	
  1720	Let $\cA$ be a chiral algebra defined by local OPE relations,
  1721	admitting a PBW filtration by conformal weight, and satisfying:
  1722	\begin{enumerate}[label=\textup{(\alph*)}]
  1723	\item the augmentation ideal $\bar{V}_\cA$ is
  1724	 positively graded: every homogeneous state has
  1725	 conformal weight $h \geq h_{\min} > 0$;
  1726	\item among all generators, exactly one has conformal
  1727	 weight~$2$, namely the stress tensor~$T$, with
  1728	 $T_{(1)} = L_0$.
  1729	\end{enumerate}
 succeeded in 52ms:
  1929	\begin{theorem}[PBW propagation: MK1 implies MK3;
  1930	 \ClaimStatusProvedHere]\label{thm:pbw-propagation}
  1931	\index{PBW spectral sequence!propagation theorem|textbf}
  1932	\index{MK3!follows from MK1|textbf}
  1933	\index{modular Koszul chiral algebra!MK3 redundancy|textbf}
  1934	\textup{[Regime: curved-central
  1935	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1936	
  1937	Let $\cA$ be a chiral algebra satisfying \textup{MK1}
  1938	\textup{(}genus-$0$ Koszulity,
  1939	Definition~\textup{\ref{def:modular-koszul-chiral})} and
  1940	hypotheses~\textup{(a)--(b)} of
  1941	Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
  1942	\textup{(}positive conformal grading with unique
  1943	weight-$2$ stress tensor\textup{)}.
  1944	Then axiom~\textup{MK3} holds: for every genus~$g \geq 1$,
  1945	\[
  1946	E_\infty(g) = E_\infty(0).
  1947	\]
  1948	In particular, axiom~\textup{MK3} is \emph{redundant} for the
exec
/bin/zsh -lc "sed -n '2428,2468p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3331,3395p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where the first factor parametrizes the relative positions of the
colliding points and the second parametrizes the remaining
configuration with $S$ collapsed to a single point~\cite[§3]{FM94}.
The residue of $\omega_\Gamma$ along $D_S$ localizes the
propagators within $S$: the edges internal to $S$ contribute the
graph amplitude of the subgraph $\Gamma|_S$, while the edges
connecting $S$ to the complement contribute the amplitude of the
quotient graph $\Gamma/S$ with $S$ collapsed to a single vertex
of valence $\sum_{a \in S} \mathrm{val}(a) - 2(|E_S|)$, where
$|E_S|$ counts edges internal to~$S$. The product of these two
amplitudes is exactly the graph amplitude of the collapsed graph,
as required.
\end{proof}

\begin{theorem}[Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph
complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
\index{cyclic $L_\infty$-algebra!from chiral graph complex}
Let $\cA$ be a Koszul chiral algebra on a smooth projective
curve~$X$ with non-degenerate invariant form
$\langle{-},{-}\rangle_{\cA}$.
 succeeded in 52ms:
  3331	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3332	\label{thm:universal-theta}
  3333	\index{universal Maurer--Cartan class|textbf}
  3334	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3335	projective curve~$X$ with non-degenerate invariant form,
  3336	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3337	universal Maurer--Cartan class
  3338	\[
  3339	\Theta_{\cA} \in
  3340	\operatorname{MC}\!\bigl(
  3341	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3342	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3343	\bigr)
  3344	\]
  3345	such that:
  3346	\begin{enumerate}[label=\textup{(\roman*)}]
  3347	\item the genus-$1$ component of its scalar trace is
  3348	 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
  3349	 the full scalar trace is
  3350	 $\operatorname{tr}(\Theta_{\cA})
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3810,3845p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '560,610p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   560	$\overline{C}_n(\Sigma_g)$
   561	(Theorem~\ref{thm:prism-higher-genus}).
   562	Each genus-$g$ piece carries a degree-$1$ \emph{fiberwise
   563	differential}~$\dfib$ with
   564	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
   565	(Convention~\ref{conv:higher-genus-differentials}).
   566	The completed total bar object
   567	$\bar{B}^{\mathrm{full}}_X(\cA) :=
   568	\prod_{g \geq 0} \hbar^g \bar{B}^{(g)}_X(\cA)$
   569	carries a strict total differential $\Dg{} \colon
   570	\bar{B}^{\mathrm{full}}_X(\cA) \to \bar{B}^{\mathrm{full}}_X(\cA)$
   571	with $\Dg{}^2 = 0$, whose reduction modulo $\hbar^{g+1}$ restricts
   572	to $\dfib$ at genus~$g$.
   573	
   574	\item\label{D:center-dg}
   575	A center local system $\mathcal{Z}_{\cA}$ on
   576	$\overline{\mathcal{M}}_{g,\bullet}$ whose fiber at a smooth
   577	curve~$\Sigma$ is the center $Z(\cA|_\Sigma)$.
   578	
   579	\item\label{D:discriminant-dg}
 succeeded in 51ms:
  3810	self-gluing differential $d_{\Gmod}$ gives non-separating
  3811	degenerations. Any MC element in
  3812	$\Defcyc(\cA) \widehat{\otimes} \Gmod$ automatically
  3813	satisfies the clutching factorization
  3814	(Proposition~\ref{prop:geometric-modular-operadic-mc}(c)).
  3815	
  3816	\emph{(iv) Verdier duality.}
  3817	Axiom~\textup{\ref{MK:verdier}} of
  3818	Definition~\textup{\ref{def:modular-koszul-chiral}}
  3819	gives an isomorphism of genus-completed complexes
  3820	$\mathbb{D}_{\Ran}\barB^{\mathrm{full}}_X(\cA)
  3821	\simeq (\cA^!)_\infty$
  3822	(factorization \emph{algebra}, not coalgebra),
  3823	functorial over~$\overline{\cM}_{g,n}$.
  3824	\textup{(}For the standard landscape, this axiom is
  3825	verified via Theorem~\textup{\ref{thm:verdier-bar-cobar}}
  3826	and the modular operad structure of the bar complex;
  3827	see Proposition~\textup{\ref{prop:standard-examples-modular-koszul}}.\textup{)}
  3828	As an isomorphism of complexes, it sends the total bar
  3829	coderivation $D_\cA$ to~$D_{\cA^!}$.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5145,5178p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9605,9698p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  9605	\end{remark}
  9606	
  9607	\begin{theorem}[Tautological line support from genus universality;
  9608	\ClaimStatusProvedHere]\label{thm:tautological-line-support}
  9609	\index{MC2!tautological line support}
  9610	Assume Hypothesis~\textup{\ref{mc2-hyp:cyclic}} \textup{(MC2-1)}: the
  9611	cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
  9612	$L_\infty$-algebra on bar coderivations, with the MC equation in
  9613	$\Defcyc(\cA)\widehat{\otimes}\Gmod$ modelling the nilpotence
  9614	condition $d_{\mathrm{bar}}^2 = 0$ of the genus-expanded bar
  9615	differential.
  9616	Then the genus-$1$ instance of
  9617	Hypothesis~\textup{\ref{mc2-hyp:tautological}} \textup{(MC2-3)}
  9618	holds:
  9619	\[
  9620	 o_1(\cA) \;=\; \kappa(\cA)\,\lambda_1
  9621	 \quad\text{in } W_1 .
  9622	\]
  9623	If, in addition, $\cA$ lies on the proved uniform-weight lane of
  9624	Theorem~\textup{\ref{thm:genus-universality}}, then the full
 succeeded in 52ms:
  5145	\]
  5146	by direct substitution of $\Phi(f)=\omega$. Collecting both sums
  5147	and using total antisymmetry of~$\omega$ to move arguments into
  5148	the standard position of the CE~formula yields
  5149	$\Phi(\delta f) = d_{\mathrm{CE}}\,\omega
  5150	= (d_{\mathrm{CE}}\circ\Phi)(f)$.
  5151	\end{proof}
  5152	
  5153	\begin{corollary}[One-dimensional obstruction space;
  5154	\ClaimStatusProvedHere]\label{cor:one-dim-obstruction}
  5155	In the setting of
  5156	Proposition~\textup{\ref{prop:genus-completed-mc-framework}},
  5157	if $H^2(L, l_1) \cong \mathbb{C}$, then the genus-$g$
  5158	obstruction is a single element of~$W_g$.
  5159	
  5160	For $\mathfrak{g}$ simple, the cyclic
  5161	CE~cohomology satisfies
  5162	$H^2_{\mathrm{cyc}}(\mathfrak{g}, \mathfrak{g})
  5163	\cong H^3(\mathfrak{g}) \cong \mathbb{C}$
  5164	by Proposition~\textup{\ref{prop:cyclic-ce-identification}}.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7742,7825p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
  7742	\begin{theorem}[MC2 completion under explicit hypotheses; \ClaimStatusProvedHere]
  7743	\label{thm:mc2-conditional-completion}
  7744	\index{MC2!completion under explicit hypotheses}
  7745	Let $\cA$ be a modular Koszul chiral algebra with simple Lie
  7746	symmetry~$\mathfrak{g}$. Assume:
  7747	\begin{enumerate}[label=\textup{(MC2-\arabic*)}]
  7748	\item\label{mc2-hyp:cyclic}
  7749	 The cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
  7750	 $L_\infty$-algebra on bar coderivations, with
  7751	 $H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g}) \cong \mathbb{C}$
  7752	 \textup{(}confirmed for all simple~$\mathfrak{g}$ by
  7753	 Corollary~\textup{\ref{cor:one-dim-obstruction}}\textup{)}.
  7754	 \textup{[}\emph{Resolved:}
  7755	 Theorem~\textup{\ref{thm:cyclic-linf-graph}} constructs the
  7756	 cyclic $L_\infty$ structure via the chiral graph complex.\textup{]}
  7757	\item\label{mc2-hyp:completion}
  7758	 The genus-completed tensor product
  7759	 $\Defcyc(\cA) \widehat{\otimes}
  7760	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$
  7761	 converges and carries modular-operadic clutching morphisms
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5500,5565p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  5500	\begin{proposition}[One-channel Verdier/Koszul criterion;
  5501	\ClaimStatusProvedHere]\label{prop:one-channel-verdier-criterion}
  5502	\index{MC2!one-channel Verdier/Koszul criterion}
  5503	Let
  5504	\[
  5505	V_g \;:=\; H^*\!\bigl(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)\bigr)
  5506	\]
  5507	with Verdier pairing $\langle-,-\rangle_{\mathbb{D}}$ and involution
  5508	$\sigma$ as in Proposition~\ref{prop:lagrangian-eigenspaces}. Let
  5509	$L_g \subset Q_g(\cA)$ and $L_g^! \subset Q_g(\cA^!)$ be
  5510	one-dimensional lines.
  5511	Then the following are equivalent:
  5512	\begin{enumerate}[label=\textup{(\roman*)}]
  5513	\item there exists a $\sigma$-stable two-dimensional subspace
  5514	 $E_g \subset V_g$ such that
  5515	 \[
  5516	 E_g \;=\; L_g \oplus L_g^!
  5517	 \]
  5518	 and the restriction of $\langle-,-\rangle_{\mathbb{D}}$ to $E_g$ is
  5519	 non-degenerate;

thinking
**Checking formula proof**

I suspect that this formula is explicitly forbidden, and possibly the corollary proof is not valid. I need to check the line numbers starting from 7928 onward. It sounds like there's something to inspect further here. I'll take a closer look at that part to clarify what's going on and confirm whether my assumption holds true. Let's see what I can find!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7920,7985p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7920	
  7921	\begin{corollary}[One-channel line concentration of the minimal MC
  7922	class;
  7923	\ClaimStatusProvedHere]
  7924	\label{cor:scalar-saturation}
  7925	\index{universal Maurer--Cartan class!scalar saturation}
  7926	\index{universal Maurer--Cartan class!scalar exactness}
  7927	For any Koszul chiral algebra~$\cA$ with simple Lie
  7928	symmetry~$\mathfrak{g}$ satisfying
  7929	$\dim H^2_{\mathrm{cyc}}(\cA,\cA) = 1$, the universal MC element
  7930	has minimal projection concentrated on a single cyclic line:
  7931	\[
  7932	\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}
  7933	\qquad
  7934	\text{for a unique }\Gamma_{\cA}\in\widehat{\Gmod}.
  7935	\]
  7936	On the proved uniform-weight lane one further has
  7937	\[
  7938	\Gamma_{\cA} = \kappa(\cA)\Lambda,
  7939	\qquad
exec
/bin/zsh -lc "rg -n -F '[m,[m,f]]' AGENTS.md CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
CLAUDE.md:365:- B47. `[m,[m,f]] = (1/2)[[m,m],f]` at even `||m||`. CORRECT: tautological at even; identity requires odd. AP138.
CLAUDE.md:553:AP138: Degenerate graded Jacobi. At even suspended degree ||m||=0, [[m,m],f]=0 is TAUTOLOGICAL. The identity [m,[m,f]]=½[[m,m],f] requires ||m|| ODD. Check parity before using Jacobi to relate ad_m^2 to [[m,m],-].
CLAUDE.md:830:AP138: Degenerate graded identity. At even suspended degree ||m||=0, the graded Jacobi identity gives [[m,m],f]=0 (tautological), NOT [m,[m,f]]=½[[m,m],f]. The "½ trick" requires ||m|| odd (where the graded antisymmetry gives [m,m]≠0). Before using Jacobi to relate ad_m^2 to [[m,m],-], CHECK the parity of ||m||. At even degree, the identity is vacuous.
AGENTS.md:278:B47. [m,[m,f]]=1/2[[m,m],f] at even ||m|| # tautological at even; identity requires odd



thinking
**Analyzing theorem complexities**

I see that the citation for MC2-3 references `Theoremref{thm:tautological-line-support}`, but the theorem overclaims and relies on a one-channel assumption. Since the current theorem involves a simple Lie and uniform-weight lane, maybe a one-dimensional assumption through the simple Lie could work, but that’s not sufficient. I might need to show contamination via a DAG. There's also this potential issue with `thm:pbw-propagation`, which asserts "MK1 implies MK3," but the proof seems problematic.
thinking
**Identifying potential issues**

I'm spotting a couple of potential problems in the text regarding `Hook-type W algebras`. For example, the MC1 theorem suggests implications that may not be valid due to the flaws in the `pbw-propagation` theorem. I also see unresolved references that need precise fixes, and I wonder about duplicate label counts across different documents. This could create confusion for references, especially if the same label is defined multiple times. If the labels are duplicated, LaTeX will resolve them unpredictably, which is a huge concern.
thinking
**Verifying label counts**

I’m thinking about whether escaped braces could be causing an issue. There’s also a chance that the regex is matching custom macros that have multiple labels, which is kind of strange. I want to check the specific label counts to figure this out. I’m considering using `rg` with a command like `rg -n '\\label{thm:master-pbw}' -g '*.tex'`, which should help pinpoint the problem. Let’s see what I find!
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:master-pbw\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1687: \phantomsection\label{thm:master-pbw}%
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:master-theta\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:universal-theta\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1686: \phantomsection\label{thm:master-theta}%
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3332:\label{thm:universal-theta}



thinking
**Identifying label duplication issues**

I think I've found a problem with duplicates — there are only three, but my earlier script might have issues counting references. The duplicate labels `thm:master-pbw` and `thm:master-theta` have multiple definitions, which could lead to confusion since the target file might pick the last loaded label. I wonder if main.tex and outlook's phantomsection labels are causing similar duplication. It's crucial to ensure definitions are unique or well-defined in the editorial_constitution.tex file. I'll need an exact fix for this issue.
thinking
**Investigating ambiguous references**

I need to check if the duplicates of `thm:master-theta` are causing any ambiguous references with MC2. The target file mentions this theorem at line 3356, which could lead to instability given the three definitions. That’s a good find! I’m also considering the potential inconsistency in the editorial_constitution regarding `\Theta^{≤2} ∈ MC...`. It's essential to inspect `main.tex`, particularly around the phantomsection labels. Duplicates can create confusion, so I plan to document exact lines and might reference other files as needed.
thinking
**Clarifying unresolved references**

I think there's a potential issue with the unresolved reference `thm:modular`, which is only in a comment line. But do comments count for unresolved references in the build? In TeX, comments are ignored, so they shouldn't affect the build process. The automated reference extractor noted line 14778, but since comments don't impact the build, this isn't a true unresolved reference. I need to ensure I remove any false positives to keep things clear for the user.
codex
Some of the missing-reference hits were harmless because they sit in commented-out lines. I’m filtering those out now and matching the live missing refs to nearby labels so the fixes are exact rather than speculative.
exec
/bin/zsh -lc "rg -n -F 'sl2-kappa' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/genus_expansions.tex:987:\begin{equation}\label{eq:sl2-kappa-decomp-genus2}
chapters/examples/genus_expansions.tex:1167:The decomposition~\eqref{eq:sl2-kappa-decomp-genus2} yields a
staging/for_ordered_assoc__w_infty_theorem.tex:75:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
staging/for_higher_genus__verlinde.tex:171:$\kappa = 3(k{+}2)/4$ (equation~\eqref{eq:sl2-kappa}),
staging/combined_for_higher_genus.tex:178:$\kappa = 3(k{+}2)/4$ (equation~\eqref{eq:sl2-kappa}),
staging/combined_for_higher_genus.tex:793:(equation~\eqref{comp:sl2-kappa}), the same value as at
staging/for_higher_genus__genus2.tex:582:(equation~\eqref{comp:sl2-kappa}), the same value as at
chapters/theory/higher_genus_modular_koszul.tex:32895:(equation~\eqref{comp:sl2-kappa}), the same value as at
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:936:$\kappa = 3(k + 2)/4$ (equation~\eqref{eq:sl2-kappa}).
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3544:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7558:\begin{equation}\label{eq:sl2-kappa}
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7623:The scalar $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa})
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8746:$\kappa = 3(k + 2)/4$ (equation~\eqref{eq:sl2-kappa}).
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8966:proportional to $\kappa(\cA)$ (equation~\eqref{eq:sl2-kappa}).
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9014:(equation~\eqref{eq:sl2-kappa}), the same value as at
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9200:$\kappa = 3(k{+}2)/4$ (equation~\eqref{eq:sl2-kappa}),
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9810:(equation~\eqref{comp:sl2-kappa}), the same value as at
chapters/theory/ordered_associative_chiral_kd.tex:8171:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
standalone/ordered_chiral_homology.tex:936:$\kappa = 3(k + 2)/4$ (equation~\eqref{eq:sl2-kappa}).
standalone/ordered_chiral_homology.tex:3544:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
exec
/bin/zsh -lc "rg -n -F 'glcm-classification' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'landscape-census' chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
target=root/'chapters/theory/higher_genus_modular_koszul.tex'
labels=set()
for p in root.rglob('*.tex'):
    try:t=p.read_text().splitlines()
    except: continue
    for line in t:
        m=re.search(r'\\\\label\\{(["'^}]+)'"\\}', line)
        if m: labels.add(m.group(1))
for i,line in enumerate(target.read_text().splitlines(), start=1):
    code=line.split('%',1)[0]
    for m in re.finditer(r'\\\\(?:[A-Za-z]*ref|eqref)\\{(["'^}]+)'"\\}', code):
        if m.group(1) not in labels:
            print(i, m.group(1), '::', code.strip())
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:26919:\textup{(}Definition~\textup{\ref{def:glcm-classification}}\textup{)}
 succeeded in 51ms:
chapters/examples/landscape_census.tex:2:\label{ch:landscape-census}
chapters/examples/landscape_census.tex:1102:\label{tab:koszulness-landscape-census}
chapters/connections/thqg_symplectic_polarization.tex:1764:\label{thm:thqg-III-landscape-census}
chapters/connections/thqg_symplectic_polarization.tex:1911:Theorem~\ref{thm:thqg-III-landscape-census} verifies the
chapters/connections/holomorphic_topological.tex:43: Chapter~\ref{ch:landscape-census}. The value depends on
chapters/connections/genus1_seven_faces.tex:1045:(Chapter~\ref{ch:landscape-census}), verify that the genus-$1$
chapters/connections/entanglement_modular_koszul.tex:568:\label{thm:ent-landscape-census}
chapters/theory/higher_genus_modular_koszul.tex:20537:values appears in~\S\textup{\ref{sec:landscape-census}}.
chapters/theory/higher_genus_modular_koszul.tex:20537:values appears in~\S\textup{\ref{sec:landscape-census}}.
chapters/theory/three_invariants.tex:234:\textup{(}Chapter~\textup{\ref{ch:landscape-census}}\textup{)}.
chapters/theory/e1_modular_koszul.tex:694:census~\S\textup{\ref{sec:landscape-census})}, all four
chapters/theory/ordered_associative_chiral_kd.tex:11053:\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
 succeeded in 6.11s:
2820 conv:proof-architecture :: Convention~\ref{conv:proof-architecture}]
20537 sec:landscape-census :: values appears in~\S\textup{\ref{sec:landscape-census}}.
26919 def:glcm-classification :: \textup{(}Definition~\textup{\ref{def:glcm-classification}}\textup{)}
32895 comp:sl2-kappa :: (equation~\eqref{comp:sl2-kappa}), the same value as at

thinking
**Investigating Missing Components**

I’m considering whether there’s something missing in the `conv:proof-architecture`. I think I should check line 2820 to see if it's active. Maybe there's a label that’s absent, which could indicate a problem. It makes sense to inspect that line and confirm if an actual label exists or if it’s just a labeling issue. This feels like a step that could clarify the situation! Let's explore this further.
exec
/bin/zsh -lc "rg -n -F 'proof-architecture' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2812,2828p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2820:Convention~\ref{conv:proof-architecture}]
chapters/theory/hochschild_cohomology.tex:285:Convention~\ref{conv:proof-architecture}]
chapters/theory/chiral_koszul_pairs.tex:3860:Convention~\ref{conv:proof-architecture}]
chapters/theory/introduction.tex:2551:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
chapters/theory/higher_genus_complementarity.tex:631:Convention~\ref{conv:proof-architecture}]
chapters/theory/higher_genus_complementarity.tex:4462:Convention~\ref{conv:proof-architecture}]
standalone/introduction_full_survey.tex:5297:\begin{convention}[Regime tags]\label{conv:regime-tags}\label{conv:proof-architecture}
 succeeded in 50ms:
  2812	the flat connection furnishes the bar-side comparison surface for
  2813	the KZ/Hitchin package on that
  2814	integrable affine lane; the factorization structure recovers the modular
  2815	functor (Theorem~\ref{thm:chain-modular-functor},
  2816	Conjecture~\ref{conj:categorical-modular-kd}).
  2817	\end{remark}
  2818	
  2819	\begin{remark}[Proof routing for Theorem~D;
  2820	Convention~\ref{conv:proof-architecture}]
  2821	\label{rem:theorem-d-model}
  2822	\index{modular characteristic theorem!model presentation}
  2823	\[
  2824	\Theta_\cA \text{ and its shadow tower}
  2825	\Longrightarrow
  2826	\mathrm{obs}_g=\kappa\cdot\lambda_g
  2827	\Longrightarrow
  2828	\sum_{g \ge 1} F_g x^{2g}

thinking
**Fixing missing references**

It looks like our script missed a reference for `conv:proof-architecture` since it only captures the first label per line due to regex limitations. That's a good catch! There are probably three missing references. I need to fix line 20537 to correctly reference `Chapter\ref{ch:landscape-census}` instead of `\S\ref{sec:landscape-census}` because chapter labels use "ch". Also, I need to find where `def:glcm-classification` is defined since there seems to be no label for it. I’ll look for `def:shadow-depth-classification` or a similar term.
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:["'^}]*classification[''^}]*'"\\}' chapters/theory/higher_genus_modular_koszul.tex chapters -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'G/L/C/M|shadow depth classification|class~\\\\mathsf\\{G\\}|GLCM' chapters/theory/higher_genus_modular_koszul.tex chapters -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:16192:\label{def:shadow-depth-classification}
chapters/theory/higher_genus_modular_koszul.tex:16192:\label{def:shadow-depth-classification}
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2325:genus-$0$ data. The shadow depth classification
chapters/theory/higher_genus_modular_koszul.tex:10931:%% The operadic complexity and shadow depth classification below
chapters/theory/higher_genus_modular_koszul.tex:11984:\index{shadow depth class!G/L/C/M}
chapters/theory/higher_genus_modular_koszul.tex:14815:%% FORCED DICHOTOMY: the G/L/C/M classification is not a taxonomy
chapters/theory/higher_genus_modular_koszul.tex:16396:\index{BPS particles!shadow depth classification}%
chapters/theory/higher_genus_modular_koszul.tex:16400:The shadow depth classification reflects this decomposition:
chapters/theory/higher_genus_modular_koszul.tex:16771:degree-$3$ projection of the shadow depth classification:
chapters/theory/higher_genus_modular_koszul.tex:16913:The shadow depth classification is a property of the algebra
chapters/theory/higher_genus_modular_koszul.tex:17346:Shadow depth is algebraic complexity; the G/L/C/M
chapters/theory/higher_genus_modular_koszul.tex:21980:\index{G/L/C/M classification!free-field scalar exactness}
chapters/theory/higher_genus_modular_koszul.tex:26916:\index{trans-series!G/L/C/M structure}%
chapters/theory/higher_genus_modular_koszul.tex:26918:The G/L/C/M classification
chapters/theory/higher_genus_modular_koszul.tex:27816:The G/L/C/M classification of
chapters/theory/higher_genus_modular_koszul.tex:28967:classification (G/L/C/M) and all shadow invariants
chapters/examples/y_algebras.tex:501:The shadow depth classification of $Y_{N_1,N_2,N_3}[\Psi]$
chapters/examples/logarithmic_w_algebras.tex:447:% Section 6: Shadow depth and the G/L/C/M classification
chapters/examples/logarithmic_w_algebras.tex:450:\section{Shadow depth and the G/L/C/M classification}
chapters/examples/free_fields.tex:89:archetype within the shadow depth classification
chapters/examples/toroidal_elliptic.tex:4417:shadow depth classification
chapters/examples/landscape_census.tex:18:four archetype classes G/L/C/M, just as electron configuration
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('.')
labels=set()
for p in root.rglob('*.tex'):
    try:t=p.read_text()
    except: continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', t):
        labels.add(m.group(1))
target=root/'chapters/theory/higher_genus_modular_koszul.tex'
for i,line in enumerate(target.read_text().splitlines(), start=1):
    code=line.split('%',1)[0]
    for m in re.finditer(r'\\\\(?:[A-Za-z]*ref|eqref)\\{(["'^}]+)'"\\}', code):
        if m.group(1) not in labels:
            print(i, m.group(1), '::', code.strip())
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.25s:
20537 sec:landscape-census :: values appears in~\S\textup{\ref{sec:landscape-census}}.
26919 def:glcm-classification :: \textup{(}Definition~\textup{\ref{def:glcm-classification}}\textup{)}
32895 comp:sl2-kappa :: (equation~\eqref{comp:sl2-kappa}), the same value as at

thinking
**Structuring findings and DAG**

I think I need to include high and medium findings, maybe even a separate section for clarity. So, I’ll likely list the findings and then include a summary afterward. It seems user specifically asks for the DAG, so I might add a section for it before the summary. I should keep it concise but still grounded in references and include a small DAG section that details nodes and dependencies. I need to think about circular chains as well.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1244,1458p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1499,1605p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1499	\begin{theorem}[PBW degeneration at all genera for Virasoro; \ClaimStatusProvedHere]
  1500	\label{thm:pbw-allgenera-virasoro}
  1501	\index{PBW spectral sequence!all-genera degeneration for Virasoro|textbf}
  1502	\index{Virasoro algebra!modular Koszulity|textbf}
  1503	\textup{[Regime: curved-central
  1504	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1505	
  1506	This theorem uses Theorem~\ref{thm:pbw-universal-semisimple} only to eliminate
  1507	the explicit genus-enrichment block. The absence of later differentials/extensions
  1508	is supplied by the family-specific argument below.
  1509	
  1510	For any genus~$g \geq 1$ and generic central charge~$c$, the PBW
  1511	spectral sequence for the genus-$g$ bar complex
  1512	$\bar{B}^{(g)}(\mathrm{Vir}_c)$ has concentrated
  1513	$E_\infty$ page:
  1514	\[
  1515	E_\infty^{p,q}\bigl(\bar{B}^{(g)}(\mathrm{Vir}_c)\bigr)
  1516	\;=\;
  1517	E_\infty^{p,q}\bigl(\bar{B}^{(0)}(\mathrm{Vir}_c)\bigr)
  1518	\quad \text{for all } g \geq 0.
 succeeded in 52ms:
  1244	\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
  1245	\label{thm:pbw-allgenera-km}
  1246	\index{PBW spectral sequence!all-genera degeneration|textbf}
  1247	\index{modular Koszul chiral algebra!unconditional all genera}
  1248	\textup{[Regime: curved-central
  1249	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1250	
  1251	This theorem does not use Theorem~\ref{thm:pbw-universal-semisimple}
  1252	\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
  1253	Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
  1254	mechanism, and the absence of later differentials/extensions is supplied by the
  1255	family-specific argument below.
  1256	
  1257	For any simple Lie algebra~$\fg$, any genus~$g \geq 1$, and
  1258	generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
  1259	for the genus-$g$ bar complex
  1260	$\bar{B}^{(g)}(\widehat{\fg}_k)$ has concentrated
  1261	$E_\infty$ page:
  1262	\[
  1263	E_\infty^{p,q}\bigl(\bar{B}^{(g)}(\widehat{\fg}_k)\bigr)

thinking
**Clarifying models**

I’m trying to think through how I might fix my previous approach by referencing actual minimal model decomposition, rather than relying on automatic Monte Carlo methods. It seems like noting a higher-level perspective could be beneficial here. Getting it right is essential, and I want to ensure I’m clear about the distinctions between these different methodologies to avoid any confusion.
exec
/bin/zsh -lc "sed -n '1919,1965p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'conj:v1-master-bv-brst' chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:bv-bar-coderived' chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex chapters -g '*.tex' | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Eventual constancy of the quotient structure tensors on every
$(m,q)$-window provides a compatible inverse system of multilinear
operations on all finite quotients. Passing to the inverse limit
defines continuous $\Ainf$-operations on~$\cA$. The $\Ainf$ identities
are polynomial on each quotient and pass to the limit entrywise.
Continuity of the completed bar differential follows because on each
weight quotient only finitely many degrees survive and all matrices are
stable. Theorem~\ref{thm:completed-bar-cobar-strong} then applies.
\end{proof}

\begin{theorem}[Completed twisting representability; \ClaimStatusProvedHere]
\label{thm:completed-twisting-representability}
\index{twisting morphism!completed|textbf}
For $\cA \in \CompCl(\Fft)$ and $C \in \Cstr$, define $\Twcts(C,\cA)$
to be the set of degree-$(-1)$ continuous twisting morphisms from~$C$
to~$\cA$. Then
\[
\operatorname{Hom}_{\mathrm{alg}}(\widehat\Omega^{\mathrm{ch}}C,\,\cA)
\;\cong\; \Twcts(C,\cA)
\;\cong\; \operatorname{Hom}_{\mathrm{coalg}}(C,\,
 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:50:(Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
chapters/connections/editorial_constitution.tex:468:Conjecture~\ref{conj:v1-master-bv-brst} is the \emph{identification}
chapters/connections/editorial_constitution.tex:544:Conjecture~\ref{conj:v1-master-bv-brst} is the
chapters/connections/editorial_constitution.tex:560:Conjecture~\ref{conj:v1-master-bv-brst} $\to$ Future~9.
chapters/connections/editorial_constitution.tex:1310:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)},
chapters/connections/editorial_constitution.tex:1350: Conjecture~\ref{conj:v1-master-bv-brst}.
chapters/connections/editorial_constitution.tex:1599: (Conjecture~\ref{conj:v1-master-bv-brst}),
chapters/connections/editorial_constitution.tex:1718:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/connections/editorial_constitution.tex:1856:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/connections/editorial_constitution.tex:1996:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/connections/editorial_constitution.tex:2056:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
chapters/connections/concordance.tex:701: class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:1958: conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
chapters/connections/concordance.tex:3305: (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
chapters/connections/concordance.tex:4671:genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:7631:\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
chapters/connections/concordance.tex:7791: (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
chapters/connections/concordance.tex:10109: (Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:11040: \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
 succeeded in 51ms:
chapters/connections/concordance.tex:697: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
chapters/connections/concordance.tex:1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/concordance.tex:3303: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:6961: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:7632: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9717: \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
chapters/connections/concordance.tex:10114: (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/concordance.tex:11042: Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
chapters/connections/concordance.tex:11163: (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
chapters/frame/preface_sections10_13_draft.tex:433:including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/frame/guide_to_main_results.tex:109: \ref{thm:bv-bar-coderived} \\[4pt]
chapters/connections/editorial_constitution.tex:441:\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
chapters/frame/preface.tex:4171:including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/theory/en_koszul_duality.tex:2708: (Theorem~\ref{thm:bv-bar-coderived}), and reconstruction
chapters/theory/en_koszul_duality.tex:3419:  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
chapters/theory/en_koszul_duality.tex:3438:  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
chapters/theory/en_koszul_duality.tex:3455:  (Theorem~\ref{thm:bv-bar-coderived}).
chapters/theory/ordered_associative_chiral_kd.tex:10057:  (Theorem~\ref{thm:bv-bar-coderived}).
chapters/theory/ordered_associative_chiral_kd.tex:10164:  and Theorem~\textup{\ref{thm:bv-bar-coderived}}: the
chapters/theory/ordered_associative_chiral_kd.tex:10194:(Theorem~\ref{thm:bv-bar-coderived}) to absorb the

thinking
**Searching for the theorem**

I need to find information on the uniform-pbw-bridge theorem. My previous attempt using `sed -n` didn’t yield results for 1919, but I actually had some output earlier. To clarify things, I should search for the relevant lines in "bar_cobar_adjunction_curved" that pertain to that year. Alright, let’s open it up and dig deeper!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1910,1945p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1910	
  1911	\begin{proof}
  1912	Fix $(m,q)$. The window $W_{m,q}(\cA_{\le N})$ involves finitely many
  1913	basis vectors. The bar differential on that finite-dimensional space is
  1914	given by a finite matrix whose entries are universal polynomial
  1915	expressions in finitely many OPE/$\Ainf$-coefficients. By hypothesis,
  1916	those coefficients stabilize for $N \gg 0$, so every matrix entry
  1917	stabilizes. This gives window-stability.
  1918	
  1919	Eventual constancy of the quotient structure tensors on every
  1920	$(m,q)$-window provides a compatible inverse system of multilinear
  1921	operations on all finite quotients. Passing to the inverse limit
  1922	defines continuous $\Ainf$-operations on~$\cA$. The $\Ainf$ identities
  1923	are polynomial on each quotient and pass to the limit entrywise.
  1924	Continuity of the completed bar differential follows because on each
  1925	weight quotient only finitely many degrees survive and all matrices are
  1926	stable. Theorem~\ref{thm:completed-bar-cobar-strong} then applies.
  1927	\end{proof}
  1928	
  1929	\begin{theorem}[Completed twisting representability; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "rg -n 'uniform PBW bridge|uniform-pbw-bridge' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1978:\label{thm:uniform-pbw-bridge}
2009:bridge (Theorem~\ref{thm:uniform-pbw-bridge}) give the correct
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1968,2015p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1968	= \sum_{k \ge 0} \mu_{n+k}(\alpha^{\otimes k},a_1,\dots,a_n).
  1969	\]
  1970	Since $\alpha \in F^1\cA$, each insertion raises filtration degree by at
  1971	least one. Modulo $F^{N+1}$, only $k \le N$ can contribute. So the
  1972	twist is quotientwise finite and continuous, preserves the strong
  1973	completion-tower axioms, and
  1974	Theorem~\ref{thm:completed-bar-cobar-strong} applies.
  1975	\end{proof}
  1976	
  1977	\begin{theorem}[Uniform PBW bridge from MC1 to MC4; \ClaimStatusProvedHere]
  1978	\label{thm:uniform-pbw-bridge}
  1979	\index{PBW!bridge to MC4}
  1980	Let $\cA = \varprojlim_N \cA_{\le N}$ be a strong completion tower, and
  1981	assume each finite stage carries a PBW filtration~$P$. Suppose:
  1982	\begin{enumerate}
  1983	\item for each quotient level~$q$, the associated-graded quotients
  1984	 $\operatorname{gr}_P(\cA_{\le N}/F^{q+1})$ stabilize for $N \gg 0$;
  1985	 and
  1986	\item for each~$q$, the bar spectral sequence of $\cA_{\le N}/F^{q+1}$
  1987	 degenerates at a page $E^{r(q)}$ independent of sufficiently
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '28628,28648p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29374,29392p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 28628	\begin{enumerate}[label=\textup{(\roman*)}]
 28629	\item \emph{Bar-cobar resolution}: defines
 28630	 $U^{\mathrm{mod}}_X(L) := \Omega(\barB^{\mathrm{ch}}(L) \otimes
 28631	 \mathsf{G}_{\mathrm{mod}})$. Reduces to
 28632	 Theorems~\textup{\ref{thm:bar-cobar-isomorphism-main}}
 28633	 and~\textup{\ref{thm:higher-genus-inversion}} at genus~$0$.
 28634	 Non-circular because $\barB^{\mathrm{ch}}(L)$ comes from $L$
 28635	 alone and $\mathsf{G}_{\mathrm{mod}}$ is combinatorial.
 28636	 Scope: Koszul algebras.
 28637	\item \emph{Genus tower}: constructs $U^{(g)}_X(L)$ inductively via
 28638	 MC5 sewing
 28639	 \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
 28640	 At genus~$0$, recovers the Nishinaka envelope~\cite{Nish26}.
 28641	 At genus~$1$, the correction is
 28642	 $\kappa \cdot \omega_1$. Fully constructive for shadow depth
 28643	 classes $\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$.
 28644	\item \emph{Kan extension}: the plain left Kan extension along
 28645	 $\mathrm{LCA} \hookrightarrow \mathrm{FactAlg}$ recovers the
 28646	 genus-$0$ envelope but is circular at higher genera: the
 28647	 colimit requires the very modular data that the envelope is
 succeeded in 50ms:
 29374	 & Modular characteristic $\kappa$
 29375	 \textup{(Thm~\ref{thm:modular-characteristic})} \\
 29376	Critical dimension $c = 26$
 29377	 & $\kappa(\cA^!) = 0$: vanishing of Koszul-dual
 29378	 curvature \\
 29379	Functional determinant
 29380	 $\det'{}_\zeta\Delta$
 29381	 & Fredholm determinant $\det(1 - K_\Theta)$
 29382	 \textup{(Prop.~\ref{prop:saddle-point-mc})} \\
 29383	Genus expansion
 29384	 & MC5 sewing
 29385	 \textup{(Thm~\ref{thm:general-hs-sewing})} \\
 29386	Ghost sector
 29387	 & Koszul dual $\cA^!$
 29388	 \textup{(Thm~\ref{thm:bar-cobar-inversion-qi})} \\
 29389	BPZ equations
 29390	 & Shadow connection
 29391	 $\nabla^{\mathrm{sh}}$
 29392	 \textup{(Thm~\ref{thm:shadow-connection})} \\
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31834,31850p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31834	(b)~the non-separating contraction $\hbar\Delta$ is the trace of the
 31835	cyclic pairing, which is computed by the same formula in both the
 31836	analytic (contour integration of~$G^g$) and algebraic (residue
 31837	extraction) settings.
 31838	\end{proof}
 31839	
 31840	\begin{remark}[The genus-$g$ chain]
 31841	\label{rem:mc5-analytic-chain}
 31842	\index{MC5!genus chain}
 31843	Three operations on the MC element $\Theta^{(g)}_\cA \in \gAmod$:
 31844	\emph{inductive extraction}
 31845	(Theorem~\ref{thm:inductive-genus-determination}),
 31846	\emph{convergent integral representation}
 31847	(Proposition~\ref{prop:2d-convergence},
 31848	Theorem~\ref{thm:analytic-algebraic-comparison}), and
 31849	\emph{analytic extension} to $\cA^{\mathrm{sew}}$ via
 31850	HS-sewing (Theorem~\ref{thm:general-hs-sewing}).

thinking
**Searching for proof gaps**

I'm thinking about limited mentions of MC5 internally. Are there other strong proof gaps? I want to search for suspicious dependencies referenced in the red_team summary, which says there are four proved claims with suspicious links in this file. Inspecting `suspicious_proved_claim_dependencies.csv` could help uncover non-proved dependencies. This might bring clarity, so I’ll start searching for that file to gather more details.
exec
/bin/zsh -lc "if [ -f suspicious_proved_claim_dependencies.csv ]; then rg -n 'higher_genus_modular_koszul\\.tex' suspicious_proved_claim_dependencies.csv; else rg -n 'higher_genus_modular_koszul\\.tex' master_claim_ledger_filtered.csv; fi" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: master_claim_ledger_filtered.csv: IO error for operation on master_claim_ledger_filtered.csv: No such file or directory (os error 2)
exec
/bin/zsh -lc "rg --files -g 'suspicious_proved_claim_dependencies.csv' -g 'master_claim_ledger_filtered.csv' -g 'label_status_conflicts.csv'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1871,1906p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1871	\begin{proposition}[Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses;
  1872	 \ClaimStatusProvedHere]
  1873	\label{prop:hook-pbw}
  1874	\index{W-algebra@$\mathcal{W}$-algebra!hook-type!PBW hypotheses|textbf}
  1875	\index{PBW spectral sequence!hook-type W-algebras|textbf}
  1876	For $N \geq 3$ and $1 \leq r \leq N-2$, the hook-type
  1877	$\mathcal{W}$-algebra
  1878	$\mathcal{W}^k(\mathfrak{sl}_N, f_{(N-r,\,1^r)})$ at generic level
  1879	satisfies hypotheses~\textup{(a)--(b)} of
  1880	Theorem~\textup{\ref{thm:pbw-universal-semisimple}}. When
  1881	$r \leq N-3$, the centralizer $\mathfrak{g}^f$ contains a
  1882	semisimple Levi factor, and hypothesis~\textup{(c)} holds as well.
  1883	In particular, \textup{MC1} implies \textup{MK3} unconditionally
  1884	for these algebras.
  1885	\end{proposition}
  1886	
  1887	\begin{proof}
  1888	The DS reduction $\mathcal{W}^k(\mathfrak{sl}_N, f_{(N-r,1^r)})$
  1889	has strong generators of three types: residual affine currents
  1890	$J^a$ at conformal weight~$1$, fermionic generators $G^\pm_i$ at
codex
The next check is the dangerous one: whether MC2 secretly uses Theorem `genus-universality`, while `genus-universality` itself leans back on the MC construction. If that happens, the “resolved” package is circular even if each individual lemma compiles.
exec
/bin/zsh -lc "rg -n -F 'thm:universal-theta' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5302,5425p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
  5302	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5303	\index{genus universality theorem|textbf}
  5304	\textup{[Regime: curved-central on the Koszul locus; all genera
  5305	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5306	
  5307	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5308	all have the \emph{same} conformal weight. There exists a
  5309	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5310	curvature, such that \begin{equation}\label{eq:genus-universality}
  5311	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5312	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5313	\quad \text{for all } g \geq 1,
  5314	\end{equation}
  5315	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  5316	\textup{(LOCAL)}
  5317	Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
  5318	For algebras with generators of \emph{several} conformal weights,
  5319	the genus-$1$ specialization is unconditional; the higher-genus
  5320	extension is conditional on the strong scalar ansatz of
  5321	Theorem~\ref{thm:multi-generator-universality}.
exec
/bin/zsh -lc "rg -n -F 'thm:mc2-bar-intrinsic' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'modular-characteristic' chapters/theory/higher_genus_foundations.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
792:(Theorem~\ref{thm:mc2-bar-intrinsic}) defines
819: \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
900:Level~(i) is Theorem~\ref{thm:mc2-bar-intrinsic}: $D_\cA^2=0$ holds
 succeeded in 51ms:
2154:characteristic (Theorem~\textup{\ref{thm:modular-characteristic}}).

thinking
**Investigating genus-universality**

Hmm, I'm considering the genus-universality and its relation to the MC2-bar-intrinsic, particularly looking at lines 792 and possibly earlier in the higher_genus_foundations.tex file. I think I should inspect the text around lines 780 to 900 to understand the context better. Searching for the relevant context of MC2-bar-intrinsic will definitely help clarify things and ensure I grasp all the important details. This sounds like an interesting exploration!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '780,910p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '880,910p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   780	+ \sum_{g_1+g_2=g}
   781	\tfrac{1}{2}[\Theta_\cA^{(g_1)}, \Theta_\cA^{(g_2)}]
   782	\;=\; 0,
   783	\]
   784	where $D^{(g)}_\cA := d_0 + \kappa(\cA)\,\omega_g$ is the corrected
   785	differential incorporating the genus-$g$ curvature. At $g = 0$,
   786	this is the tree-level MC equation. At $g = 1$, the correction
   787	$\kappa\,\omega_1$ is the Fay trisecant identity.
   788	\end{proposition}
   789	
   790	\begin{proof}
   791	The bar-intrinsic construction
   792	(Theorem~\ref{thm:mc2-bar-intrinsic}) defines
   793	$\Theta_\cA := D_\cA - d_0 \in \mathrm{MC}(\gAmod)$,
   794	satisfying $D_\cA\Theta_\cA +
   795	\tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ because $D_\cA^2 = 0$.
   796	The genus decomposition $\gAmod = \prod_{g \geq 0}
   797	\mathfrak{g}^{(g)}_\cA$ projects this single equation to genus~$g$,
   798	with the curvature $\kappa(\cA)\cdot\omega_g$ entering
   799	through the corrected differential $D^{(g)}_\cA$
 succeeded in 51ms:
   880	Level~\textup{(v)} \textup{(}$C_2$-cofinite\textup{)} implies
   881	\textup{(iv)}, \textup{(ii)}, and \textup{(i)}, but its
   882	relation to \textup{(iii)} \textup{(}Koszul\textup{)} is not
   883	one of containment: $C_2$-cofinite simple quotients
   884	$L_k(\fg)$ at admissible level satisfy~\textup{(v)} but may
   885	not satisfy~\textup{(iii)}, while Koszul universal algebras
   886	$V^k(\fg)$ at generic level satisfy~\textup{(iii)} but
   887	not~\textup{(v)}.
   888	Every chiral algebra satisfies~\textup{(i)}.
   889	Every positive-energy chiral algebra satisfies
   890	\textup{(i)}--\textup{(ii)}.
   891	The standard landscape \textup{(}Heisenberg, affine
   892	Kac--Moody at non-critical level, $\cW$-algebras at
   893	generic central charge, $\beta\gamma$ and $bc$
   894	systems\textup{)} satisfies levels
   895	\textup{(i)}--\textup{(iv)}; those that are also
   896	$C_2$-cofinite satisfy all five.
   897	\end{theorem}
   898	
   899	\begin{proof}



thinking
**Analyzing theorems and proofs**

I’ve noticed that the genus universality theorem references the MC2-bar-intrinsic in higher_genus_foundations, specifically starting at line 5302, while the proofs mention it around line 791. It seems there's a circular relationship across chapters: MC2 connects to genus-universality, which then circles back to MC2. I need to verify whether genus-universality itself cites the theorem MC2-bar-intrinsic in its proof. However, it appears there’s no direct citation in certain lines, prompting a further search for the related references in the foundation.
thinking
**Examining proof dependencies**

The proof lines 5384-5409 mention the "scalar part of the Maurer-Cartan element," but they don’t clarify its source, while the earlier proposition at lines 790-800 cites the mc2-bar-intrinsic to establish the genus-projected MC equation. This suggests an implicit dependency, meaning genus-universality isn’t independent of MC2. Theorems like `thm:universal-theta` and `thm:mc2-bar-intrinsic` rely on genus-universality to demonstrate scalar trace. I need to confirm if this forms a true circular reference, particularly within the scalar trace clause. So I’ll gather specific line numbers to resolve this.
thinking
**Exploring proof assumptions**

The proof line 5384 states that "on the scalar lane, the shadow obstruction tower is one-dimensional," referring to the scalar part of the Maurer-Cartan element. This implies a presupposition of the MC element. I'm wondering if this could be derived independently from its construction. It’s an intriguing point since determining the independence of this derivation could impact my understanding of the overall framework. I’ll have to explore this further to clarify these dependencies.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3790,3806p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3790	(Proposition~\ref{prop:geometric-modular-operadic-mc}(b)).
  3791	No conditional hypotheses are needed: the centrality of the
  3792	genus-$g$ curvature, required by the genus-induction procedure,
  3793	is automatic from the locality axiom
  3794	(Proposition~\ref{prop:curvature-centrality-general}).
  3795	
  3796	\emph{(ii) Scalar trace.}
  3797	Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
  3798	identity
  3799	$\operatorname{tr}(\Theta_\cA)_{g=1} = \kappa(\cA)\lambda_1$.
  3800	On the proved uniform-weight lane, the same theorem upgrades this to
  3801	\[
  3802	 \operatorname{tr}(\Theta_\cA)
  3803	 = \sum_{g \geq 1} \kappa(\cA)\lambda_g .
  3804	\]
  3805	
  3806	\emph{(iii) Clutching.}



thinking
**Evaluating the theorem's validity**

I need to find a direct fix since the genus-universality theorem relates to the observation `obs_g`, but `o_g` is a major obstruction. Without a proven identification theorem, the argument isn't valid. I should mention the missing one-channel hypothesis and the dimension mismatch. It's crucial to narrow this down to genus-1 and the one-channel sector. I'll need to be specific for the user, possibly splitting into two findings about the hypothesis and the identification issue. This is definitely complicated!
thinking
**Assessing theorems and findings**

I think I might need to focus on one critical finding regarding the theorem from 1929-2034 and highlight its importance for downstream applications in hook-PBW and scope remarks. It's looking promising! However, there’s a potential issue with the `universal-theta` theorem using a hidden external theorem, the `cyclic-linf-graph`, from another chapter. I also need to clarify the ambiguous existence of `Defcyc`. Keeping these concerns in mind will help organize the findings better!
thinking
**Identifying missing equations**

I’m spotting a potential issue with the reference to a missing equation labeled `eq:sl2-kappa-decomp-genus2` in the genus expansions. It seems like the actual label isn’t in the build, specifically in the standalone or ordered versions. The target file likely needs this genus 2 decomposition. I should check line 987 in the genus expansions to ensure the formula is accurate and confirm the exact fix needed by pointing to `eq:sl2-kappa-decomp-genus2`.
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '980,992p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1,15p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2320,2335p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   980	\mathrm{obs}_2(\widehat{\mathfrak{sl}}_{2,k})
   981	= \frac{3(k+2)}{4} \cdot \lambda_2
   982	\in H^4(\overline{\mathcal{M}}_2,\, Z(\widehat{\mathfrak{sl}}_{2,k}))
   983	\end{equation}
   984	where $\lambda_2 = c_2(\mathbb{E})$ is the second Chern class of the
   985	rank-$2$ Hodge bundle. The coefficient $3(k+2)/4 = \kappa(\widehat{\mathfrak{sl}}_{2,k})$
   986	decomposes as:
   987	\begin{equation}\label{eq:sl2-kappa-decomp-genus2}
   988	\underbrace{\frac{3(k+2)}{4}}_{\kappa}
   989	= \underbrace{\frac{3k}{4}}_{\textup{double-pole}}
   990	\;+\; \underbrace{\frac{3}{2}}_{\textup{Casimir}}
   991	\end{equation}
   992	The first summand $3k/4$ arises from the B-cycle monodromy of the
 succeeded in 52ms:
     1	\chapter*{Summary of Part IV}
     2	\label{ch:landscape-census}
     3	\addcontentsline{toc}{chapter}{Summary of Part IV}
     4	
     5	The complementarity sum $c + c' = 2d$ holds for every Kac--Moody
     6	algebra. The universal generating function $x/\sin x$ governs the
     7	$\hat{A}$-genus across all standard families. The spectral
     8	discriminant $\Delta(x) = 1 - 2x - 3x^2$ is shared by
     9	$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
    10	algebras with no apparent algebraic relation. These are the patterns
    11	that organize the landscape, and they are visible only in the census.
    12	
    13	Each chiral algebra in the standard landscape is determined, up to
    14	archetype, by a finite set of shadow invariants: the scalar
    15	$\kappa$, the cubic and quartic shadow coefficients $S_3$ and $S_4$,
 succeeded in 51ms:
  2320	Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
  2321	\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},
  2322	every algebraic invariant computed from the bar complex
  2323	(Koszulness, shadow depth, shadow metric, shadow
  2324	connection, CohFT, EO recursion) is determined by
  2325	genus-$0$ data. The shadow depth classification
  2326	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
  2327	(Definition~\ref{def:shadow-depth-classification})
  2328	is computed from $(\kappa, \alpha, S_4)$, which are
  2329	genus-$0$ OPE invariants. The genus-$2$ shell
  2330	activation pattern
  2331	(\S\ref{thm:genus2-shell-activation}) is a genus-$0$ invariant that \emph{manifests} at
  2332	genus~$2$.
  2333	
  2334	Any proposed genus-$g$ refinement of chiral
  2335	Koszulness at the level of bar cohomology collapses
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16188,16205p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16188	Step~$3$).
 16189	\end{proof}
 16190	
 16191	\begin{definition}[Shadow depth classification]
 16192	\label{def:shadow-depth-classification}
 16193	\ClaimStatusProvedHere
 16194	\index{shadow depth|textbf}
 16195	\index{shadow depth!classification}
 16196	\index{shadow obstruction tower!depth classification}
 16197	Let $\cA$ be a modular Koszul chiral algebra with
 16198	obstruction classes $o_r(\cA)$ from
 16199	Construction~\ref{constr:obstruction-recursion}.
 16200	Define the \emph{shadow depth}
 16201	$\kappa_d(\cA) := r_{\max}(\cA) =
 16202	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16203	(with the convention $\kappa_d = \infty$ if the tower
 16204	does not terminate).
 16205	The \emph{shadow depth class} of~$\cA$ is determined
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, collections
root=pathlib.Path('.')
# collect duplicate labels in included tex? all .tex for now
counts=collections.Counter()
for p in root.rglob('*.tex'):
    try:t=p.read_text()
    except: continue
    for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', t):
        counts[m.group(1)] += 1
dups={k:v for k,v in counts.items() if v>1}
target=root/'chapters/theory/higher_genus_modular_koszul.tex'
for i,line in enumerate(target.read_text().splitlines(), start=1):
    code=line.split('%',1)[0]
    for m in re.finditer(r'\\\\(?:[A-Za-z]*ref|eqref)\\{(["'^}]+)'"\\}', code):
        lab=m.group(1)
        if lab in dups:
            print(i, lab, dups[lab], '::', code.strip())
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.66s:
17 def:modular-characteristic-package 52 :: characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
26 thm:bar-modular-operad 50 :: (Theorem~\ref{thm:bar-modular-operad}).
32 thm:higher-genus-inversion 50 :: (Theorem~\ref{thm:higher-genus-inversion}).
43 thm:mc2-bar-intrinsic 52 :: unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
62 subsec:two-level-convention 52 :: (\S\ref{subsec:two-level-convention}). The weight filtration on
80 def:shadow-algebra 53 :: (Definition~\ref{def:shadow-algebra})
87 def:modular-bar-hamiltonian 53 :: (Definition~\ref{def:modular-bar-hamiltonian})
101 def:shadow-postnikov-tower 52 :: (Definition~\ref{def:shadow-postnikov-tower}).
106 prop:master-equation-from-mc 52 :: (Proposition~\ref{prop:master-equation-from-mc}), the
112 thm:recursive-existence 54 :: Theorem~\ref{thm:recursive-existence}:
126 thm:riccati-algebraicity 150 :: (Theorem~\ref{thm:riccati-algebraicity}). On any one-dimensional
132 thm:single-line-dichotomy 150 :: (Theorem~\ref{thm:single-line-dichotomy}):
150 thm:shadow-formality-identification 52 :: (Theorem~\ref{thm:shadow-formality-identification}). The
161 thm:quantum-complementarity-main 50 :: (Theorem~\ref{thm:quantum-complementarity-main}). For a Koszul pair
178 constr:dk-shadow-projections 50 :: (Construction~\ref{constr:dk-shadow-projections};
179 prop:e1-shadow-r-matrix 50 :: Proposition~\ref{prop:e1-shadow-r-matrix}) recovers the classical
184 thm:gz26-commuting-differentials 19 :: Theorem~\ref{thm:gz26-commuting-differentials}; the Gaudin
186 thm:gaudin-yangian-identification 19 :: Theorem~\ref{thm:gaudin-yangian-identification}.
199 prop:standard-examples-modular-koszul 52 :: Proposition~\ref{prop:standard-examples-modular-koszul} suffices.
205 thm:higher-genus-inversion 50 :: For each $g \geq 0$, the bar-cobar inversion of Theorem~\ref{thm:higher-genus-inversion}
context compacted
codex
Using `deep-beilinson-audit` on `higher_genus_modular_koszul.tex`. I have the main failure set and I’m re-checking exact line anchors plus the MC1–MC5 dependency DAG before I finalize.

thinking
**Exploring command execution**

I'm thinking about how to effectively use commentary, perhaps frequently. I want to inspect exact lines using exec_command in parallel, which could be useful. It seems like I should gather precise line ranges for my findings and the directed acyclic graph (DAG). Using multi_tool_use.parallel for multiple exec_command calls sounds like a solid plan. I might want to skip using apply_patch and focus on running rg/nl for targeted labels and references.
exec
/bin/zsh -lc 'rg -n "thm:pbw-universal-semisimple|thm:pbw-propagation|prop:hook-pbw|rem:pbw-propagation-scope|thm:pbw-allgenera-km|thm:universal-theta|thm:mc2-bar-intrinsic|thm:mc2-conditional-completion|cor:scalar-saturation|thm:tautological-line-support|cor:one-dim-obstruction|prop:one-channel-verdier-criterion|sec:landscape-census|def:glcm-classification|comp:sl2-kappa|def:shadow-depth-classification|eq:sl2-kappa-decomp-genus2|thm:genus-universality|thm:cyclic-linf-graph|thm:master-pbw|thm:master-theta" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/chiral_hochschild_koszul.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex chapters/examples/genus_expansions.tex chapters/examples/landscape_census.tex main.tex chapters/connections/outlook.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/outlook.tex:39: $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
chapters/connections/outlook.tex:40: and Remark~\ref{rem:pbw-propagation-scope}
chapters/connections/outlook.tex:55: \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
chapters/connections/outlook.tex:74:construction (Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
chapters/connections/outlook.tex:200:(Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/connections/outlook.tex:663:\phantomsection\label{thm:master-theta}
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
main.tex:953:(Theorem~\ref{thm:mc2-bar-intrinsic});
main.tex:1091:construction (Theorem~\ref{thm:mc2-bar-intrinsic}).
main.tex:1686: \phantomsection\label{thm:master-theta}%
main.tex:1687: \phantomsection\label{thm:master-pbw}%
chapters/connections/editorial_constitution.tex:21:(Theorem~\ref{thm:mc2-bar-intrinsic}:
chapters/connections/editorial_constitution.tex:24:(Theorems~\ref{thm:master-pbw},
chapters/connections/editorial_constitution.tex:25:\ref{thm:pbw-allgenera-km},
chapters/connections/editorial_constitution.tex:85:Theorems~\ref{thm:pbw-allgenera-km},
chapters/connections/editorial_constitution.tex:144: & \textbf{Proved} (bar-intrinsic, Thm~\ref{thm:mc2-bar-intrinsic}) \\
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:199:\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
chapters/connections/editorial_constitution.tex:207:families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
chapters/connections/editorial_constitution.tex:220:\label{thm:master-theta}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3331,3845p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7742,7975p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '188,238p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1710,2055p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '760,820p;5302,5415p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5153,5565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '2436,2475p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9607,9698p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3331	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3332	\label{thm:universal-theta}
  3333	\index{universal Maurer--Cartan class|textbf}
  3334	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3335	projective curve~$X$ with non-degenerate invariant form,
  3336	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3337	universal Maurer--Cartan class
  3338	\[
  3339	\Theta_{\cA} \in
  3340	\operatorname{MC}\!\bigl(
  3341	 \Defcyc(\cA) \;\widehat{\otimes}\;
  3342	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  3343	\bigr)
  3344	\]
  3345	such that:
  3346	\begin{enumerate}[label=\textup{(\roman*)}]
  3347	\item the genus-$1$ component of its scalar trace is
  3348	 $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
  3349	 the full scalar trace is
  3350	 $\operatorname{tr}(\Theta_{\cA})
 succeeded in 51ms:
  7742	\begin{theorem}[MC2 completion under explicit hypotheses; \ClaimStatusProvedHere]
  7743	\label{thm:mc2-conditional-completion}
  7744	\index{MC2!completion under explicit hypotheses}
  7745	Let $\cA$ be a modular Koszul chiral algebra with simple Lie
  7746	symmetry~$\mathfrak{g}$. Assume:
  7747	\begin{enumerate}[label=\textup{(MC2-\arabic*)}]
  7748	\item\label{mc2-hyp:cyclic}
  7749	 The cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
  7750	 $L_\infty$-algebra on bar coderivations, with
  7751	 $H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g}) \cong \mathbb{C}$
  7752	 \textup{(}confirmed for all simple~$\mathfrak{g}$ by
  7753	 Corollary~\textup{\ref{cor:one-dim-obstruction}}\textup{)}.
  7754	 \textup{[}\emph{Resolved:}
  7755	 Theorem~\textup{\ref{thm:cyclic-linf-graph}} constructs the
  7756	 cyclic $L_\infty$ structure via the chiral graph complex.\textup{]}
  7757	\item\label{mc2-hyp:completion}
  7758	 The genus-completed tensor product
  7759	 $\Defcyc(\cA) \widehat{\otimes}
  7760	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$
  7761	 converges and carries modular-operadic clutching morphisms
 succeeded in 52ms:
  2436	of valence $\sum_{a \in S} \mathrm{val}(a) - 2(|E_S|)$, where
  2437	$|E_S|$ counts edges internal to~$S$. The product of these two
  2438	amplitudes is exactly the graph amplitude of the collapsed graph,
  2439	as required.
  2440	\end{proof}
  2441	
  2442	\begin{theorem}[Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph
  2443	complex; \ClaimStatusProvedHere]\label{thm:cyclic-linf-graph}
  2444	\index{cyclic $L_\infty$-algebra!from chiral graph complex}
  2445	Let $\cA$ be a Koszul chiral algebra on a smooth projective
  2446	curve~$X$ with non-degenerate invariant form
  2447	$\langle{-},{-}\rangle_{\cA}$.
  2448	The two analytic inputs are now unconditional:
  2449	\begin{enumerate}[label=\textup{(H\arabic*)}]
  2450	\item\label{hyp:stokes-FM}
  2451	 \emph{Stokes regularity on FM compactifications}
  2452	 \textup{(}Proposition~\textup{\ref{prop:stokes-regularity-FM}}\textup{)}.
  2453	\item\label{hyp:fay-propagator}
  2454	 \emph{Fay trisecant identity for the Szeg\H{o} kernel}
  2455	 \textup{(}Proposition~\textup{\ref{prop:fay-trisecant}}\textup{)}.
 succeeded in 52ms:
   760	$(T^c(s^{-1}\bar\cA), \dfib')$ with
   761	$(\dfib')^2 - \dfib^{\,2} = \kappa(\cA) \cdot d\alpha$.
   762	The gauge transformation
   763	$\exp(\kappa(\cA) \cdot \alpha)$ provides a quasi-isomorphism
   764	but not an isomorphism of curved coalgebras: the cobar
   765	functors applied to the two models produce
   766	quasi-isomorphic but potentially non-isomorphic
   767	$A_\infty$ algebras (the difference is an exact deformation,
   768	invisible in cohomology but present at chain level).
   769	\end{proof}
   770	
   771	\begin{proposition}[Genus-$g$ MC element; \ClaimStatusProvedHere]
   772	\label{prop:genus-g-mc-element}
   773	\index{Maurer--Cartan!genus-g component@genus-$g$ component}
   774	\index{master MC element!genus decomposition}
   775	
   776	For each $g \geq 0$, the genus-$g$ component of the master MC
   777	element satisfies:
   778	\[
   779	D^{(g)}_\cA \;\Theta_\cA^{(g)}
 succeeded in 52ms:
  9607	\begin{theorem}[Tautological line support from genus universality;
  9608	\ClaimStatusProvedHere]\label{thm:tautological-line-support}
  9609	\index{MC2!tautological line support}
  9610	Assume Hypothesis~\textup{\ref{mc2-hyp:cyclic}} \textup{(MC2-1)}: the
  9611	cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
  9612	$L_\infty$-algebra on bar coderivations, with the MC equation in
  9613	$\Defcyc(\cA)\widehat{\otimes}\Gmod$ modelling the nilpotence
  9614	condition $d_{\mathrm{bar}}^2 = 0$ of the genus-expanded bar
  9615	differential.
  9616	Then the genus-$1$ instance of
  9617	Hypothesis~\textup{\ref{mc2-hyp:tautological}} \textup{(MC2-3)}
  9618	holds:
  9619	\[
  9620	 o_1(\cA) \;=\; \kappa(\cA)\,\lambda_1
  9621	 \quad\text{in } W_1 .
  9622	\]
  9623	If, in addition, $\cA$ lies on the proved uniform-weight lane of
  9624	Theorem~\textup{\ref{thm:genus-universality}}, then the full
  9625	all-genera statement holds:
  9626	\[
 succeeded in 52ms:
  5153	\begin{corollary}[One-dimensional obstruction space;
  5154	\ClaimStatusProvedHere]\label{cor:one-dim-obstruction}
  5155	In the setting of
  5156	Proposition~\textup{\ref{prop:genus-completed-mc-framework}},
  5157	if $H^2(L, l_1) \cong \mathbb{C}$, then the genus-$g$
  5158	obstruction is a single element of~$W_g$.
  5159	
  5160	For $\mathfrak{g}$ simple, the cyclic
  5161	CE~cohomology satisfies
  5162	$H^2_{\mathrm{cyc}}(\mathfrak{g}, \mathfrak{g})
  5163	\cong H^3(\mathfrak{g}) \cong \mathbb{C}$
  5164	by Proposition~\textup{\ref{prop:cyclic-ce-identification}}.
  5165	If $L = \Defcyc(\widehat{\mathfrak{g}}_k)$ with
  5166	$H^2(L, l_1) \cong H^2_{\mathrm{cyc}}(\mathfrak{g},
  5167	\mathfrak{g})$, then the genus tower is controlled by a
  5168	single sequence of tautological classes in
  5169	$R^*(\overline{\mathcal{M}}_g)$, consistent with the
  5170	universal scalar
  5171	$\kappa(\widehat{\mathfrak{g}}_k) \cdot \lambda_g$
  5172	of Theorem~D$_{\mathrm{scal}}$
 succeeded in 52ms:
   188	while the tree-level amplitude pairing requires the additional
   189	hypothesis isolated in
   190	Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
   191	orthogonal weak flank, not a link in this dependency chain.
   192	
   193	\begin{theorem}[Higher-genus PBW concentration for the standard
   194	 finite-type interacting families]\label{thm:master-pbw}
   195	\ClaimStatusProvedHere{}
   196	The genus-$g$ PBW spectral sequence concentrates at all genera for the
   197	three standard finite-type interacting families treated in the proved
   198	core: affine Kac--Moody
   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
   200	Virasoro
   201	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}}\textup{)},
   202	and principal finite-type $\mathcal{W}$-algebras, including higher
   203	$\mathcal{W}_N$
   204	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}\textup{)}.
   205	
   206	\emph{This resolves MC1 for the standard finite-type interacting
   207	families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
 succeeded in 52ms:
  1710	\begin{theorem}[Universal PBW enrichment-killing for chiral
  1711	 algebras with conformal vector; \ClaimStatusProvedHere]
  1712	\label{thm:pbw-universal-semisimple}
  1713	\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
  1714	\index{PBW spectral sequence!universal semisimple enrichment-killing|textbf}
  1715	\index{modular Koszul chiral algebra!unique-weight-2 criterion|textbf}
  1716	\index{modular Koszul chiral algebra!semisimple enrichment-killing|textbf}
  1717	\textup{[Regime: curved-central
  1718	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1719	
  1720	Let $\cA$ be a chiral algebra defined by local OPE relations,
  1721	admitting a PBW filtration by conformal weight, and satisfying:
  1722	\begin{enumerate}[label=\textup{(\alph*)}]
  1723	\item the augmentation ideal $\bar{V}_\cA$ is
  1724	 positively graded: every homogeneous state has
  1725	 conformal weight $h \geq h_{\min} > 0$;
  1726	\item among all generators, exactly one has conformal
  1727	 weight~$2$, namely the stress tensor~$T$, with
  1728	 $T_{(1)} = L_0$.
  1729	\end{enumerate}

thinking
**Inspecting relevant lines**

I should inspect lines around 1244-1253 for the KM remark and also check around the theorem related to genus-graded Koszul for the step count. It might be helpful to cite the exact lines that are relevant. I'm realizing that gathering specific details will enhance my understanding and provide better context. Let's double-check those lines to ensure everything is accurate!
codex
I’ve isolated the main theorem-level failures. I’m checking the local wording around the KM scope remark and one mis-citation so the final report uses exact, defensible line anchors only.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1244,1260p;320,360p;344,352p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1838,1988p;3264,3308p;4868,4934p;5278,5428p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   320	\end{proof}
   321	
   322	\subsection{Genus-graded Koszul property}
   323	
   324	\begin{theorem}[Genus-graded Koszul duality; \ClaimStatusProvedHere]
   325	\label{thm:genus-graded-koszul}\label{thm:genus-graded-koszul-duality}\label{thm:extended-koszul}
   326	\index{genus-graded Koszul duality}
   327	Let $(\mathcal{A}, \mathcal{A}^!)$ be a Koszul chiral pair at genus~0
   328	with central curvature at all genera (Remark~\ref{rem:voa-central-curvature}).
   329	Assume:
   330	\begin{enumerate}
   331	\item \emph{Modular Koszulity:} At each genus $g \geq 1$, the bar complex
   332	$\bar{B}^{(g)}(\mathcal{A})$ satisfies diagonal Ext vanishing:
   333	$\mathrm{Ext}^{i,j}_{\mathcal{A}^{(g)}}(\mathbb{k}, \mathbb{k}) = 0$ for $i \neq j$.
   334	\item \emph{Convergence:} The genus-graded bar complex
   335	$\bar{B}^{\mathrm{full}}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$
   336	converges in the $\hbar$-adic topology.
   337	\end{enumerate}
   338	Then $\mathcal{A}^! := \bigoplus_{g \geq 0} (\mathcal{A}^!)^{(g)}$
   339	is genus-graded Koszul, $(\mathcal{A}^!)^! \cong \mathcal{A}$ in
 succeeded in 52ms:
  1838	\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
  1839	 element in the modular convolution $sL_\infty$-algebra; the
  1840	 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
  1841	 obstruction tower) are the constructive content.
  1842	 MC1 (PBW concentration) holds unconditionally for universal
  1843	 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
  1844	 (Proposition~\ref{prop:pbw-universality}). For simple quotients
  1845	 $L_k(\fg)$ at admissible levels, PBW concentration fails at
  1846	 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
  1847	 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
  1848	 to $H^2(\barB)$
  1849	 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
  1850	\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
  1851	evaluation-generated core. The categorical CG decomposition is proved via
  1852	multiplicity-free $\ell$-weights
  1853	\textup{(}Theorem~\ref{thm:categorical-cg-all-types}\textup{)}, and
  1854	the DK comparison on the
  1855	evaluation-generated core is proved
  1856	\textup{(}Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
  1857	further proves shifted-prefundamental generation and pro-Weyl
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1,8p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '980,992p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '1680,1690p'; nl -ba chapters/connections/outlook.tex | sed -n '658,668p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   980	\mathrm{obs}_2(\widehat{\mathfrak{sl}}_{2,k})
   981	= \frac{3(k+2)}{4} \cdot \lambda_2
   982	\in H^4(\overline{\mathcal{M}}_2,\, Z(\widehat{\mathfrak{sl}}_{2,k}))
   983	\end{equation}
   984	where $\lambda_2 = c_2(\mathbb{E})$ is the second Chern class of the
   985	rank-$2$ Hodge bundle. The coefficient $3(k+2)/4 = \kappa(\widehat{\mathfrak{sl}}_{2,k})$
   986	decomposes as:
   987	\begin{equation}\label{eq:sl2-kappa-decomp-genus2}
   988	\underbrace{\frac{3(k+2)}{4}}_{\kappa}
   989	= \underbrace{\frac{3k}{4}}_{\textup{double-pole}}
   990	\;+\; \underbrace{\frac{3}{2}}_{\textup{Casimir}}
   991	\end{equation}
   992	The first summand $3k/4$ arises from the B-cycle monodromy of the
 succeeded in 52ms:
     1	\chapter*{Summary of Part IV}
     2	\label{ch:landscape-census}
     3	\addcontentsline{toc}{chapter}{Summary of Part IV}
     4	
     5	The complementarity sum $c + c' = 2d$ holds for every Kac--Moody
     6	algebra. The universal generating function $x/\sin x$ governs the
     7	$\hat{A}$-genus across all standard families. The spectral
     8	discriminant $\Delta(x) = 1 - 2x - 3x^2$ is shared by
 succeeded in 50ms:
  1680	 \phantomsection\label{rem:proof-roadmaps}%
  1681	 \phantomsection\label{rem:structural-gaps}%
  1682	 \phantomsection\label{rem:cat-o-generation-obstruction}%
  1683	 % --- Concordance theorems/conjectures ---
  1684	 \phantomsection\label{thm:universal-MC}%
  1685	 \phantomsection\label{thm:volume-one-concrete-modular-datum}%
  1686	 \phantomsection\label{thm:master-theta}%
  1687	 \phantomsection\label{thm:master-pbw}%
  1688	 \phantomsection\label{thm:discriminant-spectral}%
  1689	 \phantomsection\label{thm:lagrangian-complementarity}%
  1690	 \phantomsection\label{thm:anomaly-koszul}%
   658	
   659	% Concordance theorems/conjectures (full statements in editorial companion)
   660	\phantomsection\label{thm:family-index}
   661	\phantomsection\label{thm:universal-MC}
   662	\phantomsection\label{thm:volume-one-concrete-modular-datum}
   663	\phantomsection\label{thm:master-theta}
   664	\phantomsection\label{thm:master-pbw}
   665	\phantomsection\label{thm:discriminant-spectral}
   666	\phantomsection\label{thm:lagrangian-complementarity}
codex
The remaining pass is on the MC3–MC5 routing, so the dependency DAG I return is tied to named theorem surfaces rather than folklore summaries. I’m pulling the exact local lines where this chapter advertises those dependencies.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1970,2010p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC3|MC4|MC5|master-pbw|master-theta|completed-bar-cobar-strong|uniform-pbw-bridge|general-hs-sewing|bv-bar-coderived|algebraic-string-dictionary|conj:v1-master-bv-brst|categorical-cg-all-types|cor:dk23-all-types|shifted-prefundamental-generation|pro-weyl-recovery|completed-twisting-representability|coefficient-stability-criterion|mc-twisting-closure|lem:degree-cutoff" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4900,4955p;8380,8405p;28620,28645p;29375,29405p;31835,31855p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1970	Since $\alpha \in F^1\cA$, each insertion raises filtration degree by at
  1971	least one. Modulo $F^{N+1}$, only $k \le N$ can contribute. So the
  1972	twist is quotientwise finite and continuous, preserves the strong
  1973	completion-tower axioms, and
  1974	Theorem~\ref{thm:completed-bar-cobar-strong} applies.
  1975	\end{proof}
  1976	
  1977	\begin{theorem}[Uniform PBW bridge from MC1 to MC4; \ClaimStatusProvedHere]
  1978	\label{thm:uniform-pbw-bridge}
  1979	\index{PBW!bridge to MC4}
  1980	Let $\cA = \varprojlim_N \cA_{\le N}$ be a strong completion tower, and
  1981	assume each finite stage carries a PBW filtration~$P$. Suppose:
  1982	\begin{enumerate}
  1983	\item for each quotient level~$q$, the associated-graded quotients
  1984	 $\operatorname{gr}_P(\cA_{\le N}/F^{q+1})$ stabilize for $N \gg 0$;
  1985	 and
  1986	\item for each~$q$, the bar spectral sequence of $\cA_{\le N}/F^{q+1}$
  1987	 degenerates at a page $E^{r(q)}$ independent of sufficiently
  1988	 large~$N$.
  1989	\end{enumerate}
 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:24:(Theorems~\ref{thm:master-pbw},
chapters/connections/editorial_constitution.tex:50:(Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/editorial_constitution.tex:145:MC3 & $\Eone$-modular extension
chapters/connections/editorial_constitution.tex:147:MC4 & Infinite-generator convergence
chapters/connections/editorial_constitution.tex:149:MC5 & BV/BRST $=$ bar
chapters/connections/editorial_constitution.tex:159:MC3: \textbf{proved for all simple types} on the evaluation-generated
chapters/connections/editorial_constitution.tex:163:\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
chapters/connections/editorial_constitution.tex:164:Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
chapters/connections/editorial_constitution.tex:166:\textup{(}Theorems~\ref{thm:shifted-prefundamental-generation},
chapters/connections/editorial_constitution.tex:167:\ref{thm:pro-weyl-recovery}\textup{)}. The residual DK-4/5
chapters/connections/editorial_constitution.tex:170:downstream of MC3.
chapters/connections/editorial_constitution.tex:171:MC4 is proved: the strong completion-tower theorem
chapters/connections/editorial_constitution.tex:172:(Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
chapters/connections/editorial_constitution.tex:174:automatic continuity (Lemma~\ref{lem:degree-cutoff}), twisting
chapters/connections/editorial_constitution.tex:175:stability (Theorem~\ref{thm:mc-twisting-closure}), and a uniform PBW
chapters/connections/editorial_constitution.tex:176:bridge from MC1 (Theorem~\ref{thm:uniform-pbw-bridge}).
chapters/connections/editorial_constitution.tex:179:MC5 is not fully proved. What is proved at all genera is the analytic
chapters/connections/editorial_constitution.tex:181:\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
chapters/connections/editorial_constitution.tex:187:\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)},
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
 succeeded in 51ms:
  4900	 Hence they are the unique invariant vertices of the visible
  4901	 one-channel support graph under the induced projectivized
  4902	 automorphism action and therefore singleton orbits of the visible
  4903	 permutation group; across the concrete
  4904	 $\mathfrak{sl}_3,\mathfrak{sp}_4,\mathfrak{g}_2$ lanes, equivalently
  4905	 $m=1,2,3$, this visible orbit profile is the same canonical
  4906	 universal root-string orbit table, so the remaining visible
  4907	 combinatorics reduce first to direct identification against one fixed
  4908	 labeled table and then to reading that table off from one minimal
  4909	 invariant signature package, and finally to one universal signed
  4910	 seed-character law on the ordered one-channel seed triple, then
  4911	 further to one universal two-sign plus normalization-scalar law, and
  4912	 finally to one root-string parity sign plus normalization scalar,
  4913	 and then to one chart-normalized seed scalar.
  4914	
  4915	 For this genus-$1$-only ansatz and degree-$\le 3$ seed,
  4916	 obstruction support truncates at genus~$3$:
  4917	 $O_g=0$ for all $g\ge 4$ in the shifted
  4918	 $\mathfrak{sl}_2,\mathfrak{sl}_3,\mathfrak{sp}_4,\mathfrak{g}_2$ lanes.
  4919	 The combined normalization/scaling/root-signature/polynomial/CE/support






thinking
**Investigating theorems and DAGs**

I need to look into MC1 family theorems like principal W and Virasoro. The user asked for a complete DAG for MC1-MC5, so I might assemble one from editorial constitution and concordance lines. I should check for circular chains beyond MC2, wondering if circularity exists in PBW due to PBW-propagation. It seems MC5 might use MC1/MC2 and MC3/MC4, which is okay. I also noticed potential duplications in proof lines and inconsistencies around theorem 3527.
thinking
**Assessing findings and dependencies**

I realize that this might not be a theorem-level issue, even though the user wants an exhaust surface. I should examine theorems like PBW-Allgenera-Principal-W. Maybe this relates to eliminating enrichment and family-specific items on a later page. But I wonder if `thm:master-pbw` overstates its universal semisimple claim for MK3. 

The user wants precise file and line references for each finding, so I should ensure I focus on the target file while considering dependencies. It’s important to keep the audit centered there!
thinking
**Choosing file references**

I think it's best to prioritize references from the target file where the claims occur. We already have one finding related to circularity in higher_genus_foundations.tex, so I need to include both file lines. However, the output format only allows for one file:line. I could select the target theorem line where the issue arises and mention the dependency file lines in a section identified as PROBLEM. That should work well!
thinking
**Evaluating existence criteria**

I’m diving into the concepts here, considering if line support and scalar evaluation imply existence. It seems the mc2-reduction-principle lists obstruction locations rather than sufficiency for existence. The proof of theorem 7800-7823 suggests that existence depends on both conditions. However, if H^2 is one-dimensional, then obstruction might vanish if scalar evaluation aligns. But I need to be cautious—things aren’t so straightforward. I’ll continue examining the theorem and its assumptions carefully.
thinking
**Evaluating potential issues in labels**

I’m noticing a potential problem with duplicate labels, `thm:master-pbw` and `thm:master-theta`, which could lead to ambiguity in references since they might be pointing to the last instance built. This is pretty serious! I wonder if there are more missing references in the dependency DAG. I think I should run a search for undefined labels in the target by comparing refs to labels. I could use a shell script for that, perhaps to extract them and identify any mismatches. Let's focus on the target file and global labels across the repository.
thinking
**Considering shell usage**

The developer mentioned that I shouldn't use Python to read/write files when a simple shell suffices. I could use tools like `perl` or `awk`, but I'll go with shell commands and incorporate `rg` for unmatched refs. Ensuring no destructive actions is key here. I’m thinking that maybe I should use a commentary update first, though we've been sending updates frequently. Running just one command might be good for now.
codex
I’m doing one last consistency sweep for live undefined labels in the target file. If there are more than the three already isolated, they need to be in the report; if not, I’ll keep the list tight.
exec
/bin/zsh -lc 'labels=$(rg -o --no-filename '"'\\\\label\\{["'^}]+'"\\}' -g '*.tex' . | sed 's/\\\\label{//;s/}"'$//'"' | sort -u); refs="'$(rg -o --no-filename '"'\\\\(?:auto)?(?:eq)?ref\\{["'^}]+'"\\}' chapters/theory/higher_genus_modular_koszul.tex | sed -E 's/\\\\(?:auto)?(?:eq)?ref\\{//;s/}"'$//'"' | sort -u); comm -23 <(printf '%s
' \""'$refs") <(printf '"'%s
' \""'$labels")' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
sed: 1: "s/\\(?:auto)?(?:eq)?ref ...": RE error: repetition-operator operand invalid

codex
The first sweep command was malformed because BSD `sed` doesn’t accept that regex. I’m rerunning it with `perl` so the undefined-label check is actually reliable.
exec
/bin/zsh -lc 'labels=$(rg -o --no-filename '"'\\\\label\\{["'^}]+'"\\}' -g '*.tex' . | perl -pe 's/\\\\label\\{//; s/\\}"'$//'"' | sort -u); refs="'$(rg -o --no-filename '"'\\\\(?:auto)?(?:eq)?ref\\{["'^}]+'"\\}' chapters/theory/higher_genus_modular_koszul.tex | perl -pe 's/\\\\(?:auto)?(?:eq)?ref\\{//; s/\\}"'$//'"' | sort -u); comm -23 <(printf '%s
' \""'$refs") <(printf '"'%s
' \""'$labels")' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
comp:sl2-kappa
def:glcm-classification
sec:landscape-census
thm:modular

thinking
**Inspecting missing reference**

I find myself considering the missing reference `thm:modular` and realizing I need to inspect the relevant lines to see if they’re active or commented out. I’ve already noted that it was commented out at line 14778 from the summary, so I wonder if this output includes it. I need to locate that exact line to check everything properly. Let’s delve into that!
exec
/bin/zsh -lc "rg -n '\\\\(?:auto)?(?:eq)?ref\\{thm:modular\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
14778:%% all genera, and the resolution of Conjecture~\ref{thm:modular}




Reconnecting... 1/5 (stream disconnected before completion: Transport error: network error: error decoding response body)





thinking
**Analyzing theorem issues**

I noticed that the comment section is not live, which is good. There might be some references missing due to auto-references, but I think that could be alright. I'm also spotting a subtle issue with the theorem `thm:universal-theta`. While it uses `\lambda_g` on a proved uniform-weight lane, the statement says “full scalar trace is sum,” which isn't clearly tagged. Additionally, there's a potential problem with `prop:hook-pbw` regarding centralizers and action compatibility with PBW filtration. That might need clarification, but I’ll check the proof around lines 1901 to 1903 for context.
thinking
**Assessing theorem intricacies**

I'm considering a possible issue in `thm:mc2-bar-intrinsic`. Part (i) mentions the target `Defcyc(A)\hat{\otimes}\Gmod`, but line 3758 refers to `\dzero^2=0`, which might be fine. However, part (ii) still uses `thm:genus-universality`, but that's only genus-1 unconditional in the multi-weight scenario. 

Additionally, there seems to be a second-order failure in `chapters/connections/concordance.tex:4911-4925` due to `thm:pbw-propagation`. Should we explicitly document this finding since the user mentioned digging deeper? We also have some duplicate labels in `main.tex` and `outlook.tex`. Adding this to the findings might be worthwhile.
thinking
**Examining concordance claims**

There's a problem with the concordance claims stating that PBW propagation allows MK3 to follow from MK1 for all positive-grading unique-weight-2 algebras. This reliance on `thm:pbw-propagation` seems like an overclaim. I need to consider whether this assumption holds and if it introduces any inconsistencies in reasoning. It will be crucial to verify the foundation of this claim to ensure everything aligns properly within the framework of the algebraic structures I'm evaluating.
thinking
**Organizing Report Structure**

I’m thinking the report needs about 2 to 3 sections. I’ll structure it with **Findings** and **MC1-MC5 DAG**, then include a summary. I should keep it to flat bullets, avoiding any nesting. Each DAG bullet will show nodes and dependencies separated by semicolons, which aligns well with the need to mention circular yes/no references. 

I also need to ensure that line references are clickable, giving preference to the requested format for local files. Since the user wants strict format, I’ll compromise by using non-clickable but clear file references.
thinking
**Formulating Report Details**

I see that the developer prefers clickable links, but since the user wants a strict format, I’ll stick with plain file:line references. I should mention somewhere that I checked 13 files, maybe in the summary. Each DAG count could show "Checked: 13."

It's essential that I carefully draft my findings, avoiding unsupported adjectives. I’ll provide clear explanations of each problem referencing specific lines in the files, along with why they are contradictory. 

For example, “Theorem\ref{thm:pbw-propagation} assumes only hypotheses (a)–(b)...” will require detailed elaboration.
codex
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:1937 — PROBLEM: Theorem `thm:pbw-propagation` assumes only hypotheses `(a)–(b)` of `thm:pbw-universal-semisimple` but concludes full `MK3`, even though `thm:pbw-universal-semisimple` explicitly says at 1741–1744 and 1808–1811 that `(a)–(b)` give only `E_3`-page enrichment death and leave later-page/extension analysis separate unless `(c)` is added. FIX: Either add hypothesis `(c)` to `thm:pbw-propagation`, or weaken its conclusion to “the enrichment dies by `E_3`, reducing `MK3` to later-page/extension analysis”; then rewrite every downstream sentence that calls `MK3` redundant under `(a)–(b)`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:1883 — PROBLEM: Proposition `prop:hook-pbw` proves `(a)–(b)` for all hook types and `(c)` only when `r \le N-3`, but its last sentence claims unconditionally that `MC1` implies `MK3` for the whole family. The boundary case `r=N-2` is not covered. FIX: Split the conclusion: for `r \le N-3`, cite `thm:pbw-universal-semisimple(c)` for full `MK3`; for `r=N-2`, state only the `E_3`-page enrichment-killing package and leave later pages/extensions open or separately proved.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2041 — PROBLEM: Remark `rem:pbw-propagation-scope` says affine Kac–Moody satisfies hypotheses `(a)–(b)`, but `thm:pbw-allgenera-km` at 1251–1253 explicitly says it does not use `thm:pbw-universal-semisimple` because the Sugawara stress tensor is composite, not a generator. The chapter is using two incompatible meanings of hypothesis `(b)`. FIX: Either remove affine Kac–Moody from this family list, or restate hypothesis `(b)` to require a unique weight-2 conformal field acting by `T_{(1)}=L_0` rather than a chosen generator; then reconcile `thm:pbw-allgenera-km` with that revised wording.
- [HIGH] chapters/connections/concordance.tex:4911 — PROBLEM: The concordance propagates the broken stronger version of PBW propagation, saying `MK3` follows from `MK1` for all positive-grading unique-weight-2 CFT-type algebras and citing `thm:pbw-propagation`. That summary inherits the target theorem’s overclaim. FIX: After repairing `thm:pbw-propagation`, rewrite this block to match the repaired statement: either add hypothesis `(c)` here as well, or downgrade the claim to `E_3`-page enrichment death plus a remaining later-page/extension step.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3336 — PROBLEM: Theorem `thm:universal-theta` states existence of a cyclic `L_\infty` algebra `\Defcyc(\cA)` and an MC element in `\Defcyc(\cA)\widehat{\otimes}R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)`, but its proof only constructs `\Theta_\cA=D_\cA-d_0` on the bar-coderivation dg Lie side, never cites the theorem that constructs `\Defcyc(\cA)` (`thm:cyclic-linf-graph`), and then appeals to `thm:mc2-bar-intrinsic`, whose proved target is `\Defcyc(\cA)\widehat{\otimes}\Gmod` at 3555–3556, not the `R\Gamma` target written here. FIX: Add an explicit first step citing `thm:cyclic-linf-graph`; then either restate the theorem with target `\Defcyc(\cA)\widehat{\otimes}\Gmod` to match the proved construction, or insert a cited comparison/quasi-isomorphism `\Gmod \simeq R\Gamma(\overline{\mathcal M}_{g,\bullet},\mathbb Q)` and transport `\Theta_\cA` across it.
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:3797 — PROBLEM: The scalar-trace part of `thm:mc2-bar-intrinsic` is circular. Its proof cites `thm:genus-universality`, but `thm:genus-universality` in `higher_genus_foundations.tex:5384–5407` derives its scalar lane from “the scalar part of the Maurer–Cartan element,” and `higher_genus_foundations.tex:791–800` explicitly imports `thm:mc2-bar-intrinsic` to define that MC element. The scalar clause is not independently established. FIX: Remove `thm:genus-universality` from the proof of `thm:mc2-bar-intrinsic` and prove the scalar trace directly from the bar-intrinsic differential, or demote part `(ii)` to a later corollary that depends on genus universality only after MC2 is already proved independently.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:3819 — PROBLEM: The Verdier part of `thm:mc2-bar-intrinsic` is type-inconsistent. The proof first states `\mathbb D_{\Ran}\barB^{\mathrm{full}}_X(\cA)\simeq(\cA^!)_\infty` and explicitly calls the target a factorization algebra, then immediately says this sends the total bar coderivation `D_\cA` to `D_{\cA^!}`. That identifies a bar-coderivation on a coalgebra with the differential of a different object without a comparison theorem. FIX: Rewrite part `(iv)` in two steps: transport `D_\cA` to the differential on `(\cA^!)_\infty` under `MK:verdier`, then cite or prove a separate comparison identifying that transported differential with the bar-side `D_{\cA^!}`; if no such comparison is available, weaken the theorem to the transported Verdier statement and delete `\mathbb D(\Theta_\cA)=\Theta_{\cA^!}`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:7818 — PROBLEM: `thm:mc2-conditional-completion` says `prop:one-channel-verdier-criterion` “constructs the opposite one-channel Koszul line from the complementarity relation.” It does not. At 5500–5563 that proposition is only an equivalence criterion assuming the lines already exist. FIX: Replace the sentence beginning at 7817 with a conditional statement: Verdier compatibility follows once a `\sigma`-stable Verdier-nondegenerate plane `L_g \oplus L_g^!` is supplied; cite `prop:one-channel-verdier-criterion` only for that reduction. If construction from complementarity is intended, add a new proposition proving that construction and cite it instead.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:7965 — PROBLEM: Corollary `cor:scalar-saturation` claims the MC equation is automatic because `s^{-1}\eta` has odd degree and graded antisymmetry forces `l_n^{tr}(\eta,\ldots,\eta)=0` for `n\ge2`. That is false: repeated odd inputs do not vanish by graded antisymmetry in general. FIX: Delete lines 7965–7969. Keep only the one-dimensionality conclusion `\Theta^{\min}=\eta\otimes\Gamma_\cA`, and cite `thm:mc2-bar-intrinsic` or `thm:universal-theta` for actual MC existence instead of deriving it from parity.
- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:9660 — PROBLEM: `thm:tautological-line-support` assumes only `MC2-1`, but Step 1 immediately uses the one-channel hypothesis `H^2(\Defcyc(\cA),l_1)\cong\mathbb C` via `cor:one-dim-obstruction`, which is not in the theorem statement. Step 2 then identifies `o_g` with `\mathrm{obs}_g` without a cited comparison theorem, and 9672–9676 equate a degree-2 form `\omega_g` with the top Chern class `\lambda_g` in all genera without a justified class-level bridge. FIX: Add the missing one-channel hypothesis explicitly to the theorem statement; replace “`\mathrm{obs}_g` and `o_g` are two names for the same geometric class” with a cited comparison proposition or downgrade the all-genera claim to genus 1 only; and remove the displayed form-level identification as a proof of `\lambda_g`, replacing it with a cited Hodge-class theorem or `thm:genus-universality` once the circularity is repaired.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:20537 — PROBLEM: `\ref{sec:landscape-census}` is undefined; the live label in `chapters/examples/landscape_census.tex` is `\label{ch:landscape-census}` at line 2. FIX: Change the reference to `Chapter~\ref{ch:landscape-census}` or add a real `sec:landscape-census` label to the cited section and use that label consistently.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:26919 — PROBLEM: `\ref{def:glcm-classification}` is undefined. The live local definition is `\label{def:shadow-depth-classification}` at line 16192. FIX: Replace `\ref{def:glcm-classification}` with `\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:32895 — PROBLEM: `\eqref{comp:sl2-kappa}` is undefined. The live formula is `\label{eq:sl2-kappa-decomp-genus2}` in `chapters/examples/genus_expansions.tex:987`. FIX: Replace `\eqref{comp:sl2-kappa}` with `\eqref{eq:sl2-kappa-decomp-genus2}`.
- [MEDIUM] main.tex:1686 — PROBLEM: Placeholder labels duplicate live theorem labels: `thm:master-theta` and `thm:master-pbw` are also defined at `chapters/connections/editorial_constitution.tex:194,220` and `chapters/connections/outlook.tex:663–664`. References from `higher_genus_modular_koszul.tex:3356` and `28884` therefore resolve against a non-unique label surface. FIX: Delete the duplicate placeholder labels in `main.tex` and `outlook.tex` or rename them to unique non-live aliases; keep the `editorial_constitution.tex` theorem labels as the single canonical definitions.
- [LOW] chapters/theory/higher_genus_modular_koszul.tex:3497 — PROBLEM: The proof of `prop:curvature-centrality-general` cites “Theorem `thm:genus-graded-koszul`, Step 4,” but the proof of `thm:genus-graded-koszul` at 344–352 has no Step 4. FIX: Delete that parenthetical or replace it with a valid pinpoint citation.

**MC1-MC5 DAG**
- `MC1 = thm:master-pbw` (`editorial_constitution.tex:193–215`) depends on `thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, and `thm:pbw-allgenera-principal-w`; `thm:pbw-universal-semisimple` is the shared helper for the Virasoro/finite-type `\mathcal W` lane. Dependency status: the family theorems exist, but the chapter’s stronger `(a)–(b) => MK3` propagation route is unsound as written. Circular chain seen: none.
- `MC2 = thm:master-theta` (`editorial_constitution.tex:218–237`) is routed through `thm:universal-theta` and `thm:mc2-bar-intrinsic`, with explicit dependencies on `thm:cyclic-linf-graph`, `prop:geometric-modular-operadic-mc`, `thm:genus-universality`, and `MK:verdier`. Dependency status: not satisfied as written; the scalar-trace leg is circular and the Verdier leg is type-mismatched. Circular chain seen: yes, `thm:mc2-bar-intrinsic -> thm:genus-universality ->` scalar-MC package using `thm:mc2-bar-intrinsic`.
- `MC3` is recorded in `concordance.tex:1850–1862` and `3278–3290` as depending on `thm:categorical-cg-all-types` and `cor:dk23-all-types`, with type-A strengthening through `thm:shifted-prefundamental-generation` and `thm:pro-weyl-recovery`. Dependency status: evaluation-generated core proved; DK-4/5 extension/completion beyond that core remains open. Circular chain seen: none in the read surface.
- `MC4` is recorded in `concordance.tex:1904–1926` and `editorial_constitution.tex:171–176,356–371` as depending on `thm:completed-bar-cobar-strong`, `lem:degree-cutoff`, `thm:mc-twisting-closure`, `thm:completed-twisting-representability`, and `thm:coefficient-stability-criterion`, with an explicit `MC1 -> MC4` edge via `thm:uniform-pbw-bridge` (`bar_cobar_adjunction_curved.tex:1977–2000`). Dependency status: the formal completion framework is proved; family-specific H-level target identification remains separate. Circular chain seen: none.
- `MC5` is recorded in `concordance.tex:1943–1959` and `3297–3305` as depending on `thm:general-hs-sewing`, `thm:algebraic-string-dictionary`, and `thm:bv-bar-coderived`, with the genuswise chain-level identification left at `conj:v1-master-bv-brst`. `editorial_constitution.tex:565–653` adds the downstream edge `(MC3 + realized MC4) -> standard-tower MC5 reduction`. Dependency status: analytic and coderived lanes are proved; the chain-level package is still open/conjectural. Circular chain seen: none, but the DAG is not closed because one edge is still conjectural.

## Summary
Checked: 13 | Findings: 15 | Verdict: FAIL
tokens used
349,376
