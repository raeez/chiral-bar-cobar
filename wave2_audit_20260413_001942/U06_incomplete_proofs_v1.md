# U06_incomplete_proofs_v1 (851s)

- [CRITICAL] `chapters/connections/twisted_holography_quantum_gravity.tex:119` — PROBLEM: `thm:thqg-g1-finiteness`, `thm:thqg-g2-complexity`, `thm:thqg-g3-polarization`, `thm:thqg-g4-s-duality`, `thm:thqg-g5-yangian`, `thm:thqg-g6-soft-graviton`, `thm:thqg-g7-bootstrap`, `thm:thqg-g8-reconstruction`, `thm:thqg-g9-critical-string`, `thm:thqg-g10-fredholm`, `thm:thqg-g14-error-correction`, `thm:thqg-g15-page`, and `thm:thqg-dependency` at lines `119/130/149/159/174/188/213/230/247/270/323/336/360` are all tagged `\ClaimStatusProvedHere`, and each is followed by another claim rather than a proof block. FIX: retag this whole “sixteen results” ladder `\ClaimStatusProvedElsewhere` with theorem-by-theorem citations, or insert a separate `proof` environment under each theorem; do not keep them as `ProvedHere` summaries.
- [CRITICAL] `chapters/frame/heisenberg_frame.tex:1183` — PROBLEM: `thm:frame-heisenberg-koszul-dual`, `thm:genus1-heisenberg`, `thm:frame-genus1-curvature`, and `thm:frame-genus2-curvature` at lines `1183/1407/1429/1577` are `\ClaimStatusProvedHere` without proof environments; the genus-1 curvature lane even begins “The proof is the direct computation” in prose instead of opening `\begin{proof}`. FIX: wrap each argument in an actual proof block, or retag each theorem `\ClaimStatusProvedElsewhere` and cite the detailed theorem already referenced in prose.
- [CRITICAL] `chapters/examples/w3_holographic_datum.tex:603` — PROBLEM: `thm:w3hol-Q-T`, `thm:w3hol-Q-W`, and `thm:w3hol-discriminants` at lines `603/616/627` are consecutive `ProvedHere` theorems with no proof blocks before the next section. FIX: add a proof after each theorem, or collapse the three formulas into one theorem with one proof; until then, remove `ProvedHere`.
- [CRITICAL] `chapters/theory/computational_methods.tex:598` — PROBLEM: `thm:comp-ds-consistency`, `thm:comp-zhu-c-dependence`, and `thm:comp-three-way-bar` at lines `598/708/788` are `ProvedHere` theorems followed only by narrative prose. FIX: insert proof blocks that state the finite computation, the exact search space, and the oracle/engine used, or retag them as computed observations instead of `ProvedHere` theorems.
- [CRITICAL] `chapters/frame/guide_to_main_results.tex:240` — PROBLEM: `thm:guide-family-index` is a `ProvedHere` theorem in the guide chapter with no local proof block. FIX: change it to `\ClaimStatusProvedElsewhere` and cite the proving theorem(s), or add a local proof; guide-level summaries cannot remain `ProvedHere` unsupported.
- [CRITICAL] `chapters/connections/holographic_datum_master.tex:151` — PROBLEM: `thm:seven-faces-master` is `ProvedHere`, but the file immediately says the proof is “distributed” across later sections instead of giving a proof block. FIX: insert a real proof block that assembles the seven identifications, or retag the theorem `\ClaimStatusProvedElsewhere` and leave the distributed discussion as exposition.
- [CRITICAL] `chapters/connections/outlook.tex:247` — PROBLEM: `thm:operadic-complexity` is a bare `ProvedHere` theorem with no proof block before the next section. FIX: downgrade it to `\ClaimStatusProvedElsewhere` with a citation to the proving theorem, or add a proof here.
- [CRITICAL] `chapters/connections/editorial_constitution.tex:193` — PROBLEM: `thm:master-pbw` is tagged `ProvedHere`, but the file moves straight into another theorem and remarks; no proof block is attached. FIX: convert this master-summary theorem to `\ClaimStatusProvedElsewhere` with exact pointers to the family theorems it summarizes, or write a local proof that assembles them.
- [CRITICAL] `chapters/connections/concordance.tex:4069` — PROBLEM: `thm:pixton-from-shadows` and `thm:lagrangian-complementarity` at lines `4069/4962` are `ProvedHere` theorems without proof blocks; `thm:pixton-from-shadows` is followed by a remark titled “Proof of Theorem...” instead of a `proof` environment. FIX: convert those remarks into actual `proof` blocks, or retag both theorems `\ClaimStatusProvedElsewhere` with exact references.
- [CRITICAL] `chapters/connections/arithmetic_shadows.tex:12592` — PROBLEM: `thm:prime-locality-obstructions` is a multi-obstruction theorem tagged `\ClaimStatusProvedHere where indicated`, but the file goes straight into the next subsection with no proof block. FIX: split the five items into separately tagged proved/open propositions with proofs, or keep the theorem and add an item-by-item proof/status block; the current mixed-status theorem cannot remain unproved.
- [CRITICAL] `chapters/connections/thqg_gravitational_complexity.tex:1075` — PROBLEM: `thm:thqg-vanishing-mechanisms` and `thm:thqg-grav-landscape` at lines `1075/1359` are `ProvedHere` theorems with no proof blocks before the next claim. FIX: add proof environments or retag them as `ProvedElsewhere` summaries with exact citations.
- [CRITICAL] `chapters/connections/thqg_introduction_supplement_body.tex:856` — PROBLEM: `thm:thqg-intro-operadic-complexity` is `ProvedHere` and receives no proof block. FIX: make it `\ClaimStatusProvedElsewhere` with the proving reference, or add a proof here.
- [CRITICAL] `chapters/examples/free_fields.tex:987` — PROBLEM: `thm:betagamma-bar-complex` and `thm:w-algebra-ainfty` at lines `987/5345` both lack local proofs; the latter explicitly says “See Chapter~... for the full construction and proof,” which flatly contradicts `\ClaimStatusProvedHere`. FIX: give `thm:betagamma-bar-complex` an actual low-degree proof, and retag `thm:w-algebra-ainfty` `\ClaimStatusProvedElsewhere` unless you inline the proof here.
- [CRITICAL] `chapters/connections/casimir_divisor_core_transport.tex:742` — PROBLEM: `thm:pbw-recurrence` is `ProvedHere` and no proof block appears before the next theorem. FIX: add the recurrence proof here, or retag it `\ClaimStatusProvedElsewhere` with the exact proving citation.
- [HIGH] `appendices/koszul_reference.tex:268` — PROBLEM: `thm:essential-image-koszul` is a five-condition iff theorem marked `ProvedHere`, but the only proof block starts at line `300` and is explicitly “Proof outline.” FIX: replace the outline with a full two-direction proof, or downgrade the theorem to a weaker status until that proof exists.
- [HIGH] `chapters/connections/master_concordance.tex:35` — PROBLEM: `thm:master-seven-face` is partly `ProvedHere`, yet the attached block at line `91` is explicitly a “Proof sketch” that only describes the chain of identifications. FIX: split the theorem into proved-here and proved-elsewhere components with exact proofs/citations, or turn the sketch into a remark and remove the composite `ProvedHere` status.
- [HIGH] `chapters/theory/introduction.tex:1313` — PROBLEM: `thm:e1-primacy` is a four-part theorem tagged `ProvedHere`, but the attached block at line `1355` is explicitly a “Proof sketch.” FIX: retag the introduction theorem `\ClaimStatusProvedElsewhere` and turn the sketch into a roadmap remark, or supply a full proof block that actually proves parts `(i)`–`(iv)`.
- [HIGH] `chapters/theory/configuration_spaces.tex:4518` — PROBLEM: `thm:normal-crossings-verified` states the normal-crossings property for general `\overline{C}_n(X)`, but the only proof at line `4527` is “Verification for n=3.” FIX: either restrict the theorem statement to `\overline{C}_3(\mathbb C)` or replace the verification with a general nested-blowup normal-crossings proof.
- [HIGH] `chapters/connections/casimir_divisor_core_transport.tex:872` — PROBLEM: `thm:growth-mode-factorization` has four clauses, but the proof at line `905` is only “Verification for \(\mathfrak{sl}_2\)” and checks the factorization/DS divisibility, not the theorem’s growth-rate and cancellation clauses. FIX: either shrink the theorem to the explicitly verified `\mathfrak{sl}_2` factorization statement, or add arguments for clauses `(iii)` and `(iv)` and keep the full theorem.
- [HIGH] `appendices/nonlinear_modular_shadows.tex:177` — PROBLEM: `thm:nms-mc-principle` is a foundational equivalence theorem tagged `ProvedHere`, but the attached block at line `197` is explicitly a “Proof sketch.” FIX: expand it into a full equivalence proof constructing the MC element and the inverse algebra structure, or downgrade the claim surface until that proof exists.
- [MEDIUM] `chapters/examples/yangians_computations.tex:4770` — PROBLEM: `thm:yangian-H2-reduction` is tagged `ProvedHere`, but its proof at line `4786` is explicitly a “Proof sketch.” FIX: replace the sketch with a full spectral-sequence argument spelling out the filtration, the `E_1` page, and the no-differential claim, or weaken the status tag.

Literal trailing `...` / `TO BE COMPLETED` proof endings found: `0`. The surviving failures are missing proof blocks and incomplete proof surfaces, not placeholder line endings.

## Summary
Checked: 3973 | Findings: 21 | Verdict: FAIL


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
session id: 019d840a-fa35-7693-aee7-56aeb38f795b
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


MISSION: UNFINISHED WORK AUDIT.

Find all \begin{proof} that end with '...' or 'TO BE COMPLETED' or are <5 lines for a complex theorem. Also find ProvedHere tags without a following proof block.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers


thinking
**Planning codebase inspection**

I need to announce the skills I'm using and why. First, I'll open the skill file in commentary mode. I should inspect the repo using `rg`, but it seems I need a comprehensive approach since the network is restricted. I might consider using explorer agents instead, as they’re faster and more reliable for codebase questions. I'll spawn multiple explorer agents to search for specific patterns, including proof endings and blocks. Frequent commentary updates are also important, so I should map out my steps clearly.
thinking
**Preparing audit findings**

I need to prepare findings based on the user's request for a "MISSION: UNFINISHED WORK AUDIT." They specifically don't want any code changes, just a review-style audit. My findings must be ordered by severity and include file and line numbers. It's essential that I provide exact fixes rather than just diagnoses. I might specify what proof is unfinished and provide precise wording, such as "Replace trailing '...' with a complete proof establishing X via Y and cite Lemma Z." I’ll infer details from the context to be accurate.
codex
Using `deep-beilinson-audit` for an adversarial audit of unfinished proof surfaces. I’m first locating every proof block and theorem-status tag that matches the failure modes you named, then I’ll verify each hit in-file before reporting findings.
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


thinking
**Evaluating file loading**

I need to load the required files, and I’m thinking about using parallel processing with exec_command through multi_tool_use.parallel. Should I provide an update in commentary before I dive deeper? It seems like I've already done that. Now, I should focus on reading only the minimal necessary data, using parallel commands, maybe with tools like sed to handle specific sections. That way, I can keep everything organized and efficient!
codex
I’ve loaded the audit workflow. Next I’m grounding the search against the repo’s live status surfaces so the unfinished-proof findings don’t drift from the concordance or registry.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 50ms:
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
**Planning an audit for unfinished work**

I need to audit unfinished work by finding proofs that end with specific phrases like "TO BE COMPLETED" or "ProvedHere" tags that don't have the follow-up proof block. It seems I'll have to check all .tex files in the repo, including appendices, and gather actual file contents with line references for each finding. Automating the extraction seems necessary, perhaps using shell commands and a parser, but I need to verify findings to avoid false positives. Using Python for analysis could be justified for more complex parsing.
thinking
**Developing an audit method**

The instructions say I shouldn’t use Python for editing when shell commands could work, but I think Python might be okay for analysis. I’ll consider using Perl or Awk as alternatives, but also exec_command with here-doc for Python may be useful. I need to stick to direct tools without spawning agents since the user didn't request that. My audit method will involve enumerating .tex files, searching for `\begin{proof}` blocks with specific phrases, and defining what qualifies as a complex theorem based on context.
thinking
**Clarifying the audit for complex theorems**

The user specified less than five lines for a complex theorem, so I need to read the actual file contents rather than rely on assumptions. For each flagged short proof, I’ll read the theorem's statement to determine if it's truly complex. This requires careful judgment to identify obvious complex theorems, such as major theorems or those with multi-line statements. I’ll inspect all proofs under five lines in the theorem environment and plan to verify these findings thoroughly.
codex
The raw search is going to overfire, so I’m building it in two passes: machine enumeration first, then manual verification of every candidate against the surrounding theorem/proof block. That avoids false positives from short routine lemmas or comments inside proofs.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\begin\\{proof\\}|TO BE COMPLETED|\\.\\.\\.' chapters appendices frontmatter main.tex metadata -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'ClaimStatusProvedHere' chapters appendices frontmatter -S" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
Total output lines: 2778

rg: frontmatter: No such file or directory (os error 2)
main.tex:241:% Without explicit theH... definitions, many sibling counters reset to
main.tex:295:% Evidence environment: used after conjectures in place of \begin{proof}.
main.tex:304:% Without these, hyperref emits "bookmark level for unknown ... defaults to 0"
appendices/signs_and_shifts.tex:54:\begin{proof}
appendices/signs_and_shifts.tex:182:\begin{proof}
appendices/signs_and_shifts.tex:282:\begin{proof}
appendices/signs_and_shifts.tex:1060:\begin{proof}[Verification]
appendices/homotopy_transfer.tex:36:\begin{proof}
appendices/homotopy_transfer.tex:84:\begin{proof}
appendices/homotopy_transfer.tex:156:\begin{proof}
appendices/homotopy_transfer.tex:471:\begin{proof}
appendices/homotopy_transfer.tex:506:\begin{proof}
appendices/homotopy_transfer.tex:544:\begin{proof}
appendices/homotopy_transfer.tex:655:\begin{proof}
appendices/homotopy_transfer.tex:761:\begin{proof}
appendices/arnold_relations.tex:39:\begin{proof}[Proof of Theorem~\ref{thm:arnold-relations-appendix}]
appendices/arnold_relations.tex:77:\begin{proof}
 exited 2 in 50ms:
Total output lines: 3049

rg: frontmatter: No such file or directory (os error 2)
appendices/homotopy_transfer.tex:16:\ClaimStatusProvedHere
appendices/homotopy_transfer.tex:145:\begin{lemma}[Existence of SDR; \ClaimStatusProvedHere]
appendices/homotopy_transfer.tex:454:\begin{theorem}[Chiral homotopy transfer; \ClaimStatusProvedHere]
appendices/homotopy_transfer.tex:523:\ClaimStatusProvedHere]
appendices/homotopy_transfer.tex:617:\ClaimStatusProvedHere]
appendices/homotopy_transfer.tex:733:\ClaimStatusProvedHere]
chapters/examples/deformation_quantization.tex:134:\begin{theorem}[Coisson quantization at genus \texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]\label{thm:chiral-quantization}
chapters/examples/deformation_quantization.tex:186:\begin{theorem}[Chiral Kontsevich formula; \ClaimStatusProvedHere]
chapters/examples/deformation_quantization.tex:418:\begin{proposition}[MC \texorpdfstring{$\Leftrightarrow$}{iff} star product; \ClaimStatusProvedHere]
chapters/examples/deformation_quantization.tex:536:\begin{theorem}[Genus expansion; \ClaimStatusProvedHere]\label{thm:deformation-genus-expansion}
chapters/examples/deformation_quantization.tex:1363:\ClaimStatusProvedHere
chapters/examples/deformation_quantization.tex:1737:\ClaimStatusProvedHere
chapters/examples/deformation_quantization.tex:1824:\begin{theorem}[Boundary-linear LG theorem; \ClaimStatusProvedHere]
appendices/branch_line_reductions.tex:174:\begin{proposition}[The scalar shadow is an abelian MC element; \ClaimStatusProvedHere]
appendices/branch_line_reductions.tex:233:\begin{theorem}[Spectral cumulant hierarchy; \ClaimStatusProvedHere]
appendices/branch_line_reductions.tex:315:\begin{theorem}[First obstruction is traceless and quadratic; \ClaimStatusProvedHere]
appendices/branch_line_reductions.tex:388:\begin{corollary}[Vanishing criterion for filtered lifts; \ClaimStatusProvedHere]







thinking
**Developing proof parser**

I need a robust Python script to scan .tex files and identify proof blocks that are either short or end without actual proof, particularly looking for certain patterns. I think I'll output this to a temporary file. It seems wise to gather all proof blocks with fewer than five non-blank lines after the theorem environment for inspection. I may also want to find blocks ending with ellipses or “TO BE COMPLETED” tags, according to the user’s request.
thinking
**Identifying proof structures**

I need to ensure that the last meaningful line in my proof blocks ends with specific strings before `\end{proof}`. I'll also look for comments like "TO BE COMPLETED" within those proofs. It's essential to locate the exact file and line number for these entries. Additionally, I'm examining claims with "ProvedHere" tags that lack corresponding proof blocks, particularly after theorem environments. I wonder if definitions should be excluded, but it seems the user wants to focus on proof-bearing environments like theorems and propositions for completeness.
thinking
**Focusing on proof requirements**

I need to clarify that the theorem registry counts remarks or computations as "ProvedHere," but the user is looking specifically for unfinished proofs. So, I should focus on proof-required environments like theorems, propositions, lemmas, and corollaries. The user's request also involves finding any "ProvedHere" tags that lack a corresponding proof block. This means I need to track all relevant environments that should typically include proofs and ensure that my analysis is grounded in the actual file contents.
thinking
**Evaluating theorem registry for proofs**

I'm thinking about how the user wants unfinished work, possibly missing proof blocks related to theorem-like claims. I need to decide the scope carefully—maybe looking into theorem registry metadata, as it tracks ProvedHere blocks. It sounds like parsing .tex files might be easier. I’ll write a Python script using regex to identify claims, checking for `ProvedHere` status between specific lines. I could get all .tex files from chapters and appendices and analyze line by line.
thinking
**Refining proof detection strategy**

I'm thinking that tags often appear in the optional argument line or the one right before a statement ends. I can check if the environment body has `ClaimStatusProvedHere` before the first blank line. It seems easier to just see if `ClaimStatusProvedHere` is anywhere within the environment before its end. 

Next, I need to identify proof blocks after `\end{env}`, searching for the first non-comment, non-blank line that follows. If there’s no proof block before the next theorem-like environment, that might indicate something is missing. I might allow for up to 20 lines until the next claim section; I’ll have to verify any flagged cases manually. For the proof blocks, I should identify the beginning and end, counting lines that are non-blank and non-commented.
thinking
**Identifying meaningful lines in proofs**

I need to determine if the last meaningful line contains specific markers like `...`, `TO BE COMPLETED`, or `TODO` since the user has emphasized those. I should also capture the line number of this last line, along with the preceding claim environment type, label, or title. This way, I can better understand the context and locate what needs attention. Keeping track of all these details will help me serve the user's needs effectively!
thinking
**Planning proof inspection**

I'm thinking about outputting CSV-like candidates including proof blocks with end patterns and short proof blocks under five content lines. I'll need to manually check flagged items, which might not be too many. 

End patterns could be few, while short proofs may be more numerous. For complexity, I'll focus on theorems that are short, possibly narrowing down to dozens. 

Using some heuristics like checking theorem statement spans or equation presence could help. I could script to list all theorems with proofs shorter than five lines and then inspect them manually.
codex
I’ve got the broad hit list; now I’m shrinking it to the actual defect surface with a parser. The next pass will only emit verified candidates: proof blocks, their preceding claim environment, proof length, and whether a `ProvedHere` claim never reaches a proof before the next structural boundary.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, json
from pathlib import Path
root = Path('.')
tex_files = sorted([p for base in ['chapters','appendices'] for p in (root/base).rglob('*.tex')])
claim_envs = {'theorem','proposition','lemma','corollary','maintheorem','computation','verification','calculation','remark','definition','construction','example'}
proof_begin_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[["'^'"\\]]*\\])?')
proof_end_re = re.compile(r'\\\\end\\{proof\\}')
claim_begin_re = re.compile(r'\\\\begin\\{(' + '|'.join(sorted(claim_envs)) + r')\\}(?:\\[["'^'"\\]]*)?')
claim_end_re_tpl = r'\\\\end\\{%s\\}'
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
status_re = re.compile(r'\\\\ClaimStatusProvedHere')
section_re = re.compile(r'\\\\(part|chapter|section|subsection|subsubsection)\\*?\\b')
comment_re = re.compile(r'(?<"'!'"\\\\)%.*"'$'"')

def strip_comments(s):
    return comment_re.sub('', s)

results = {'proof_end_bad': [], 'short_theorem_proofs': [], 'provedhere_no_proof': []}

for path in tex_files:
    lines = path.read_text().splitlines()
    # collect proof blocks and claim envs
    claims = []
    proofs = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = claim_begin_re.search(line)
        if m:
            env = m.group(1)
            start = i+1
            end_pat = re.compile(claim_end_re_tpl % re.escape(env))
            j = i
            status_lines = []
            labels = []
            while j < len(lines):
                s = strip_comments(lines[j])
                if status_re.search(s):
                    status_lines.append(j+1)
                labels += label_re.findall(s)
                if end_pat.search(s):
                    break
                j += 1
            title = None
            # crude title extraction from begin line optional arg through same line
            opt = None
            if '[' in line and ']' in line:
                opt = line.split('[',1)[1].rsplit(']',1)[0]
            elif '[' in line:
                # gather until closing ] or end env
                acc = line.split('[',1)[1]
                k = i+1
                while k <= j:
                    acc += '\\n' + lines[k]
                    if ']' in lines[k]:
                        acc = acc.split(']',1)[0]
                        break
                    k += 1
                opt = acc
            if opt:
                title = ' '.join(opt.replace('\\n',' ').split())
            claims.append({'env':env,'start':start,'end':j+1,'status_lines':status_lines,'labels':labels,'title':title})
            i = j+1
            continue
        m = proof_begin_re.search(line)
        if m:
            start = i+1
            j = i+1
            while j < len(lines):
                if proof_end_re.search(strip_comments(lines[j])):
                    break
                j += 1
            body_lines = []
            for k in range(i+1, min(j, len(lines))):
                s = strip_comments(lines[k]).rstrip()
                if s.strip():
                    body_lines.append((k+1, s))
            last = body_lines[-1] if body_lines else (start, '')
            proofs.append({'start':start,'end':min(j+1,len(lines)),'body_count':len(body_lines),'body_lines':body_lines,'last_line':last[0],'last_text':last[1].strip()})
            i = j+1
            continue
        i += 1
    # map claims to following proof block before next structural boundary/claim env
    for idx, claim in enumerate(claims):
        # bad proof endings
        pass
    for proof in proofs:
        last = proof['last_text']
        if last.endswith('...') or 'TO BE COMPLETED' in last:
            # find preceding claim
            prev = None
            for claim in claims:
                if claim['end'] < proof['start']:
                    prev = claim
                else:
                    break
            results['proof_end_bad'].append({
                'file': str(path), 'proof_start': proof['start'], 'proof_end': proof['end'],
                'last_line': proof['last_line'], 'last_text': last,
                'prev_env': prev['env'] if prev else None,
                'prev_start': prev['start'] if prev else None,
                'prev_label': prev['labels'][0] if prev and prev['labels'] else None,
                'prev_title': prev['title'] if prev else None,
                'body_count': proof['body_count'],
            })
    # short theorem proofs
    theorem_like = {'theorem','maintheorem'}
    for proof in proofs:
        prev = None
        for claim in claims:
            if claim['end'] < proof['start']:
                prev = claim
            else:
                break
        if prev and prev['env'] in theorem_like and proof['start'] - prev['end'] <= 6 and proof['body_count'] < 5:
            # compute theorem body size and lines
            theorem_lines = []
            for k in range(prev['start']-1, prev['end']):
                s = strip_comments(lines[k]).rstrip()
                if s.strip() and not claim_begin_re.search(s) and not re.search(claim_end_re_tpl % re.escape(prev['env']), s):
                    theorem_lines.append((k+1, s))
            results['short_theorem_proofs'].append({
                'file': str(path), 'theorem_start': prev['start'], 'theorem_end': prev['end'],
                'label': prev['labels'][0] if prev['labels'] else None, 'title': prev['title'],
                'proof_start': proof['start'], 'proof_end': proof['end'], 'proof_body_count': proof['body_count'],
                'theorem_nonblank_count': len(theorem_lines),
            })
    # provedhere without following proof for proof-bearing envs
    proof_bearing = {'theorem','proposition','lemma','corollary','maintheorem'}
    claim_starts = [c['start'] for c in claims]
    for idx, claim in enumerate(claims):
        if claim['env'] not in proof_bearing or not claim['status_lines']:
            continue
        # search from claim end+1 until next proof or next claim/section boundary
        next_claim_start = claims[idx+1]['start'] if idx+1 < len(claims) else len(lines)+1
        limit = next_claim_start-1
        proof_found = None
        boundary_line = None
        for k in range(claim['end'], min(limit, len(lines))):
            s = strip_comments(lines[k])
            if proof_begin_re.search(s):
                proof_found = k+1
                break
            if section_re.search(s):
                boundary_line = k+1
                limit = k+1
                break
        if proof_found is None:
            results['provedhere_no_proof'].append({
                'file': str(path), 'env': claim['env'], 'start': claim['start'], 'end': claim['end'],
                'label': claim['labels'][0] if claim['labels'] else None, 'title': claim['title'],
                'status_line': claim['status_lines'][0], 'next_claim_start': next_claim_start,
                'boundary_line': boundary_line,
            })

# sort results
for k in results:
    results[k] = sorted(results[k], key=lambda x:(x['file'], x.get('start',x.get('theorem_start',x.get('proof_start',0)))))
print(json.dumps({k: {'count': len(v), 'items': v[:200]} for k,v in results.items()}, indent=2))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 263ms:
{
  "proof_end_bad": {
    "count": 0,
    "items": []
  },
  "short_theorem_proofs": {
    "count": 103,
    "items": [
      {
        "file": "appendices/arnold_relations.tex",
        "theorem_start": 91,
        "theorem_end": 96,
        "label": "thm:bar-d-squared-arnold",
        "title": "Bar differential squares to zero; \\ClaimStatusProvedHere",
        "proof_start": 98,
        "proof_end": 100,
        "proof_body_count": 1,
        "theorem_nonblank_count": 4
      },
      {

thinking
**Inspecting JSON results**

I need to look into the truncated JSON and maybe save full results as files in a temporary workspace to inspect later. I think rerunning the script to write detailed TSV/JSON files in that directory is a good idea. I'll need to manually review counts of categories, especially making sure there are no bad proof endings. But I should also search for the string "TO BE COMPLETED" separately, just to be thorough. Let's execute that search now.
codex
The parser found no proof blocks whose last meaningful line literally ends with `...` or contains `TO BE COMPLETED`, but I’m checking the raw strings separately so that a formatting quirk inside the proof body doesn’t slip through.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'TO BE COMPLETED' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\.\\.\\.' chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/thqg_gravitational_s_duality.tex:1906:$c(k) = 2(1 - 12/(k+3)) = 50$ gives $k + 3 = -12/24 = -1/2$... but
 exited 1 in 53ms:




thinking
**Balancing proof verification**

It looks like I need to verify around 103 short theorem proofs and check for numerous candidates. Manual verification is necessary since there could be false positives, and I’ll need exact fixes for each finding. The user wants an exhaustive report, but I have to balance that with the developer's guidance to keep it under 50-70 lines. I might group findings in a structured bullet list, aiming for around 30-40 verified findings without overwhelming the user.
thinking
**Reviewing theorem proofs**

I need to keep my findings within 70 lines, ideally flagging around 20 actual findings. I should inspect candidates closely, as many short proofs may simply reference earlier theorems. The user specifically asks for explanations under five lines for complex theorems, so I can’t assume every short proof qualifies. I should generate full data, filter by certain criteria, and check each candidate in context for potential false positives. I'll pay special attention to those without immediate proof blocks.
thinking
**Identifying proof structures**

I’m considering that proofs might come later in a section, formatted with something like `\begin{proof}[Proof of Theorem X]` after supporting lemmas. The user wants ProvedHere tags without an immediate proof block following the theorem. So, if there’s no proof right after, that’s a finding. I need to note these, but I should also provide exact fixes. Even if proofs are deferred, I must flag them to meet the user’s specifications. It feels a bit tricky!
codex
I’m now checking the second-order failure mode: `ProvedHere` theorems that technically have a proof block, but only as a sketch or one-line pointer. Those survive naïve grep and are exactly the kind of status inflation you asked me to kill.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, json
from pathlib import Path
tex_files = sorted([p for base in ['chapters','appendices'] for p in Path(base).rglob('*.tex')])
claim_envs = {'theorem','proposition','lemma','corollary','maintheorem'}
proof_begin_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
proof_end_re = re.compile(r'\\\\end\\{proof\\}')
claim_begin_re = re.compile(r'\\\\begin\\{(' + '|'.join(sorted(claim_envs)) + r')\\}(?:\\[(["'^'"\\]]*))?')
comment_re = re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
status_re = re.compile(r'\\\\ClaimStatusProvedHere')

def strip_comments(s):
    return comment_re.sub('', s)

items=[]
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]
    proofs=[]
    i=0
    while i<len(lines):
        s=strip_comments(lines[i])
        m=claim_begin_re.search(s)
        if m:
            env=m.group(1); opt=m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i
            label=None; status=False
            while j<len(lines):
                t=strip_comments(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if end_re.search(t): break
                j+=1
            claims.append({'env':env,'start':i+1,'end':j+1,'opt':opt,'label':label,'status':status})
            i=j+1; continue
        m=proof_begin_re.search(s)
        if m:
            opt=m.group(1) or ''
            j=i+1
            body=[]
            while j<len(lines):
                t=strip_comments(lines[j]).rstrip()
                if proof_end_re.search(t): break
                if t.strip(): body.append((j+1,t.strip()))
                j+=1
            proofs.append({'start':i+1,'end':j+1,'opt':opt,'body_count':len(body),'body':body})
            i=j+1; continue
        i+=1
    # associate nearby proof to preceding claim
    for p in proofs:
        prev=None
        for c in claims:
            if c['end']<p['start']:
                prev=c
            else:
                break
        if prev and prev['status'] and prev['env']=='theorem' and p['start']-prev['end']<=6:
            if re.search(r'sketch|outline|references?|verification', p['opt'], re.I) or p['body_count']<5:
                items.append({'file':str(path),'label':prev['label'],'theorem_start':prev['start'],'proof_start':p['start'],'proof_opt':p['opt'],'proof_body_count':p['body_count'],'title':prev['opt']})
print(json.dumps(items[:200], indent=2))
print('COUNT', len(items))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 243ms:
[
  {
    "file": "appendices/arnold_relations.tex",
    "label": "thm:bar-d-squared-arnold",
    "theorem_start": 91,
    "proof_start": 98,
    "proof_opt": "",
    "proof_body_count": 1,
    "title": "Bar differential squares to zero; \\ClaimStatusProvedHere"
  },
  {
    "file": "appendices/koszul_reference.tex",
    "label": "thm:essential-image-koszul",
    "theorem_start": 268,
    "proof_start": 300,
    "proof_opt": "Proof outline",
    "proof_body_count": 20,
    "title": "Essential image of Koszul duality; \\ClaimStatusProvedHere"
  },
  {







thinking
**Evaluating findings strategy**

I see there are many findings to consider. I might need to inspect the raw context for the severe ones and think about outputting the top representatives. The user wants everything, but generating all 103 could be overwhelming. Perhaps I can compress categories by file clusters? 

Alternatively, I might treat clusters of adjacent theorems as single findings while ensuring I report every actual finding. It's important to find a balance between completeness and the line limits.
thinking
**Deciding on findings report**

I need to think this through. The user wants an exhaustive report, so maybe I should produce around 30 high-confidence findings and mention additional candidates. I wonder if saving a full audit log to a file and referencing it makes sense, but they want the final output formatted a certain way. 

Maybe I should create a concise list while noting that a fuller machine-generated candidate list exists. I need to inspect candidates further, especially since some findings might come from appendices not included in the main document.
thinking
**Identifying missing proof counts**

I’m considering using the theorem registry to scan for missing proof counts, and I suspect there could be more than 100. It seems like I need to validate everything thoroughly by grounding claims in the actual file contents. 

Using `sed` might help read through contexts for each candidate, but that's a lot of data to sift through. Maybe I can automate this by outputting surrounding lines. If tool output is truncated, I could write a script to extract contexts and save them for inspection.
thinking
**Refining search criteria**

I think I need to use a more precise criterion to narrow the findings. For short proofs, maybe I should only consider theorem statements with a non-blank count of 10 or more, or proof bodies of 2 or fewer to focus on serious cases. I might also want to categorize based on complex theorems using those counts. It seems I should manually review various candidates and adjust labels for better detection and measurement as I go along.
thinking
**Improving proof detection**

I noticed that the proof began at line 144, while the theorem started at line 134 and the next claim started at 140. Originally, I thought our search led to false positives, as the theorem is followed by a label. But that next claim at 140 might be due to a remark or something similar. There seem to be many no-proof candidates that could be false positives because they include proof-like comments. I’m thinking we need a better algorithm for detection that allows for these intricacies.
thinking
**Analyzing proof structure**

I’m noticing that if another claim starts before the proof, it might create a missing immediate proof by style. Since the user asked about the proof block, I’m wondering if I might still be missing something. The theorem could be proved after lemmas, like in the case of `thm:chiral-quantization`, where a proof block appears at line 144. But why does the next claim start at 140? It could be that the claim parser misidentified the proof as a claim or something else. It's quite confusing!
thinking
**Inspecting theorem claims**

I'm wondering if there's a parsing issue with the environment since the current claim doesn't seem to have an equation. Could the next claim starting at 140 actually be a proposition? I need to take a closer look. Maybe the theorem ends at 139, with the proof starting at 144. I'm curious why the next claim starts at 140. There might be another theorem beginning at that point, so I'll inspect further.
codex
Some of the first-pass “no proof” hits are likely false positives from deferred proofs or an intervening remark. I’m re-running that pass with label-aware matching so I only keep claims that truly never get a proof block, not ones whose proof is merely delayed.
exec
/bin/zsh -lc "sed -n '128,150p' chapters/examples/deformation_quantization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

The OPE of a chiral algebra is precisely a star product:
\[a(z) \cdot b(w) = \sum_{k=0}^\infty \frac{(a *_k b)(w)}{(z-w)^k}\]

This has the same structure as Kontsevich's formula: the classical term is $a(z)b(w)$ (commutative product), the first quantum correction is $\frac{\{a, b\}(w)}{z-w}$ (Poisson bracket), and the higher quantum corrections are $\frac{(a *_k b)(w)}{(z-w)^k}$.

\begin{theorem}[Coisson quantization at genus \texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]\label{thm:chiral-quantization}
Every coisson algebra on a smooth curve $X$ of genus~$0$ admits a deformation
quantization to a vertex algebra ($\Einf$-chiral algebra), canonical up to
gauge equivalence (gauge equivalence in $\Convinf$, Convention~\ref{rem:two-level-convention}).
\end{theorem}

\begin{remark}[Higher genus extension]\label{rem:chiral-quantization-higher-genus}
The higher-genus extension is conjectural (\ClaimStatusConjectured): it requires controlling the global obstructions in $H^2$ of the chiral Hochschild complex on $\overline{\mathcal{M}}_{g,n}$. This remains open.
\end{remark}

\begin{proof}[Proof of Theorem~\ref{thm:chiral-quantization}]
The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).

For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.


thinking
**Refining proof detection logic**

I’m working on how to improve the detection of proof blocks related to claims, especially with ProvedHere tags. The user asked for a solution that identifies claims without following proof blocks. I need to check boundaries between sections and remarks for context. If a theorem intervenes before the proof, that might change the results. The logic needs clarity, especially focusing on whether there's a proof block after the claim but before another section boundary.
thinking
**Refining proof association logic**

I’m considering how to handle proof blocks and their relationship to claims. If a proof's optional argument mentions the claim label specifically, that’s a good indicator. If another claim comes before the proof but references the original label, that’s also acceptable. I want to check for proofs that start after a claim but lack explicit labels. It might be useful to implement searches for proof blocks tied to labels within the same file and use theorem_registry metadata to assist with mapping.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, json
from pathlib import Path
tex_files = sorted([p for base in ['chapters','appendices'] for p in Path(base).rglob('*.tex')])
claim_envs = {'theorem','proposition','lemma','corollary','maintheorem'}
claim_re = re.compile(r'\\\\begin\\{('+'|'.join(sorted(claim_envs))+r')\\}(?:\\[(["'^'"\\]]*))?')
proof_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
comment_re = re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
status_re = re.compile(r'\\\\ClaimStatusProvedHere')
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
section_re = re.compile(r'\\\\(part|chapter|section|subsection|subsubsection)\\*?\\b')

def sc(s): return comment_re.sub('', s)
items=[]
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]; proofs=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        m=claim_re.search(s)
        if m:
            env=m.group(1); title=m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if end_re.search(t): break
                j+=1
            claims.append({'env':env,'title':title,'start':i+1,'end':j+1,'label':label,'status':status})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            opt=m.group(1) or ''
            proofs.append({'start':i+1,'opt':opt})
        i+=1
    section_lines=[idx+1 for idx,l in enumerate(lines) if section_re.search(sc(l))]
    for idx,c in enumerate(claims):
        if not(c['status'] and c['env'] in claim_envs):
            continue
        # end of search window: next section boundary after claim end
        window_end=len(lines)+1
        for sl in section_lines:
            if sl>c['end']:
                window_end=sl
                break
        next_claim_start=claims[idx+1]['start'] if idx+1<len(claims) else len(lines)+1
        local_proofs=[p for p in proofs if c['end']<p['start']<window_end]
        # immediate proof before next claim
        immediate = any(p['start'] < next_claim_start for p in local_proofs)
        # later explicit proof reference by label
        explicit = False
        if c['label']:
            explicit = any(c['label'] in p['opt'] for p in local_proofs)
        if not immediate and not explicit:
            items.append({'file':str(path),'label':c['label'],'env':c['env'],'start':c['start'],'end':c['end'],'title':c['title'],'window_end':window_end,'next_claim_start':next_claim_start,'proofs_in_window':local_proofs[:5]})
print('COUNT',len(items))
print(json.dumps(items[:200], indent=2))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 393ms:
COUNT 131
[
  {
    "file": "appendices/arnold_relations.tex",
    "label": "cor:bar-d-squared-zero-arnold",
    "env": "corollary",
    "start": 164,
    "end": 171,
    "title": "Bar differential squares to zero; \\ClaimStatusProvedHere",
    "window_end": 173,
    "next_claim_start": 180,
    "proofs_in_window": []
  },
  {
    "file": "appendices/branch_line_reductions.tex",
    "label": "cor:mu2-centered-at-13",
    "env": "corollary",
    "start": 561,
    "end": 571,
    "title": "The genus-\\(2\\) one-line coefficient is centered at \\texorpdfstring{$13$}{13}; \\ClaimStatusProvedHere",


thinking
**Assessing proof claims**

I'm realizing there are still many false positives when it comes to proof identification in this context. Maybe I shouldn't report unless there’s absolutely no proof in the current window, which could help reduce the count. I’m thinking I need to distinguish between genuinely missing proof blocks and corollaries that don't need separate proof because they're directly derived from previous theorems. There’s an issue with ProvedHere tags lacking accompanying proofs, even when they seem obvious. It seems focusing on clear missing proof blocks is the more defensible approach.
thinking
**Inspecting candidate clusters**

I need to take a closer look at the contexts of the strongest candidate clusters, particularly in `appendices/nonlinear_modular_shadows.tex`, where there are numerous short proofs. Many of these one-line proofs might just state something like "This is immediate from the previous theorem." I’m considering what to do: either fully expand these proofs or possibly downgrade their status to corollaries. I think it might be best to inspect a sample first, perhaps using sed around specific lines.
codex
The biggest concentration is an appendix with a whole run of `ProvedHere` theorems discharged by one-line proofs. I’m reading that cluster now because if it’s real, it’s a systematic status-inflation defect rather than isolated sloppiness.
exec
/bin/zsh -lc "sed -n '520,670p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\nabla_{\cA}-\nabla_{\cA^!}:
L_{\cA}\oplus L_{\cA^!}\longrightarrow K_{\cA}
\Bigr).
\end{equation}
A tangent vector in $T_{\mathrm{comp}}(\cA)$ is therefore a first-order deformation of $\cA$, a first-order deformation of $\cA^!$, and a first-order deformation of the universal kernel, constrained by the linearized Maurer--Cartan equation.
\end{definition}

\begin{theorem}[Ambient complementarity in tangent form; \ClaimStatusProvedHere]
\label{thm:nms-ambient-complementarity-tangent}
Assume an ambient complementarity datum exists for $\cA$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the complex $T_{\mathrm{comp}}(\cA)$ carries a canonical nondegenerate pairing of degree $-1$;
\item the one-sided tangent complexes
\[
T_{\cA}:=\mathrm{fib}(\nabla_{\cA}:L_{\cA}\to K_{\cA}),
\qquad
T_{\cA^!}:=\mathrm{fib}(\nabla_{\cA^!}:L_{\cA^!}\to K_{\cA})
\]
are isotropic inside $T_{\mathrm{comp}}(\cA)$;
\item if the pairing on $L_{\cA}\oplus K_{\cA}\oplus L_{\cA^!}$ is perfect and bar--cobar duality identifies the normal complex of one side with the shifted dual tangent complex of the other, then $T_{\cA}$ and $T_{\cA^!}$ are complementary Lagrangians in $T_{\mathrm{comp}}(\cA)$.

thinking
**Evaluating theorem structure**

I'm trying to determine if there's an issue with a theorem that lacks a direct proof or summary. Maybe I should only focus on the main theorem without including corollaries or propositions in the next section. I'll need to take a closer look at these. It might be a good idea to list the theorems that don't have proofs and use a script to filter out just the main theorems without their proofs for clarity.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, json
from pathlib import Path
tex_files = sorted([p for base in ['chapters','appendices'] for p in Path(base).rglob('*.tex')])
claim_re = re.compile(r'\\\\begin\\{(theorem|maintheorem)\\}(?:\\[(["'^'"\\]]*))?')
proof_re = re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
comment_re = re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
status_re = re.compile(r'\\\\ClaimStatusProvedHere')
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
section_re = re.compile(r'\\\\(part|chapter|section|subsection|subsubsection)\\*?\\b')

def sc(s): return comment_re.sub('', s)
items=[]
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]; proofs=[]; sections=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        if section_re.search(s): sections.append(i+1)
        m=claim_re.search(s)
        if m:
            env=m.group(1); title=m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if end_re.search(t): break
                j+=1
            claims.append({'env':env,'title':title,'start':i+1,'end':j+1,'label':label,'status':status})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            proofs.append({'start':i+1,'opt':m.group(1) or ''})
        i+=1
    for idx,c in enumerate(claims):
        if not c['status']: continue
        window_end = next((sl for sl in sections if sl>c['end']), len(lines)+1)
        proofs_in_window=[p for p in proofs if c['end']<p['start']<window_end]
        if not proofs_in_window:
            items.append({'file':str(path),'start':c['start'],'end':c['end'],'label':c['label'],'title':c['title'],'window_end':window_end})
print('COUNT',len(items))
for item in items[:200]:
    print(f\"{item['file']}:{item['start']}:{item['label']}:{item['title']}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 252ms:
COUNT 44
appendices/ordered_associative_chiral_kd.tex:5200:thm:yangian-quantum-group:Yangian--quantum group deformation for the affine lineage
chapters/connections/arithmetic_shadows.tex:196:thm:shadow-spectral-correspondence:Shadow--spectral correspondence
chapters/connections/arithmetic_shadows.tex:1402:thm:bg-vir-coincidence:$\beta\gamma$--Virasoro rate coincidence
chapters/connections/arithmetic_shadows.tex:1592:thm:refined-shadow-spectral:Refined shadow--spectral correspondence
chapters/connections/arithmetic_shadows.tex:12592:thm:prime-locality-obstructions:Precise obstructions to prime-locality;
chapters/connections/arithmetic_shadows.tex:12795:thm:riccati-determinacy-assessment:Riccati determinacy; \ClaimStatusProvedHere
chapters/connections/casimir_divisor_core_transport.tex:742:thm:pbw-recurrence:PBW recurrence theorem for
chapters/connections/concordance.tex:4069:thm:pixton-from-shadows:Pixton ideal from shadow obstruction tower; \ClaimStatusProvedHere
chapters/connections/concordance.tex:4962:thm:lagrangian-complementarity:Lagrangian complementarity;
chapters/connections/holographic_datum_master.tex:151:thm:seven-faces-master:Seven-face master theorem; \ClaimStatusProvedHere
chapters/connections/outlook.tex:247:thm:operadic-complexity:Operadic complexity; \ClaimStatusProvedHere
chapters/connections/thqg_fredholm_partition_functions.tex:563:thm:thqg-X-heisenberg-sewing-full:Heisenberg sewing theorem: full development;
chapters/connections/thqg_gravitational_complexity.tex:1075:thm:thqg-vanishing-mechanisms:Classification of vanishing mechanisms
chapters/connections/thqg_gravitational_complexity.tex:1359:thm:thqg-grav-landscape:Gravitational complexity census
chapters/connections/thqg_gravitational_complexity.tex:1407:thm:thqg-g2-main:Shadow-depth classification; result (G2)
chapters/connections/thqg_holographic_reconstruction.tex:894:thm:virasoro-rmax-infinity:$r_{\max}(\mathrm{Vir}_c) = \infty$; \ClaimStatusProvedHere
chapters/connections/thqg_introduction_supplement_body.tex:856:thm:thqg-intro-operadic-complexity:Operadic complexity; \ClaimStatusProvedHere;
chapters/connections/twisted_holography_quantum_gravity.tex:119:thm:thqg-g1-finiteness:\textbf{G1}: Perturbative finiteness
chapters/connections/twisted_holography_quantum_gravity.tex:130:thm:thqg-g2-complexity:\textbf{G2}: Shadow-depth classification





thinking
**Determining proof block fix**

For the missing proof block, I think the exact fix could be to insert `\begin{proof}` right after `\end{theorem}`. Alternatively, I might suggest downgrading the status to `\ClaimStatusProvedElsewhere`, but I need to provide a specific reference to the theorem proving it. It's tricky to pinpoint the most significant issues based on file contents. Maybe I can specify to replace `\ClaimStatusProvedHere` with a note about the proving chapter once the full proof block is added.
thinking
**Focusing on proof block status**

If there’s no proof block, I see that the exact fix could be to downgrade the status or add a complete proof since the local defect is unfinished. The simplest immediate fix would be to downgrade the status. If I want to keep `ProvedHere`, I should insert a proof block. Since the user is looking for an exact fix, I can recommend changing `\ClaimStatusProvedHere` to either `\ClaimStatusProvedElsewhere` or `\ClaimStatusConjectured` until a full proof is provided.
thinking
**Evaluating audit status changes**

For an audit, it seems best to downgrade the status if proof is incomplete. This is clear and actionable. We could propose changes like replacing `\ClaimStatusProvedHere` with `\ClaimStatusProvedElsewhere` if the proof references external results. But it’s not always obvious! If proof is from a “References” section, then updating to `\ClaimStatusProvedElsewhere` makes sense. It might also be good to retag the theorem as `\ClaimStatusConjectured` if the argument is only a sketch. A minimal safe fix could be `\ClaimStatusConditional`.
thinking
**Clarifying proof requirements**

Since the user is looking for an exact fix, I think the best approach is to suggest expanding the proof into a full version that explicitly proves clauses (i)-(iii). This should include constructing the pairing, verifying isotropy, and checking maximality. Until that full proof is written, I recommend removing `\ClaimStatusProvedHere`. This gives clear and substantive steps to follow, ensuring the user knows exactly what to do next. That feels clear and actionable!
thinking
**Exploring theorem inclusion**

I think it’s possible to focus on including the main theorem and just a few significant propositions in the introduction. I need to examine the contexts for any sketches, outlines, or references that would be helpful for verification. It seems useful to use searching tools to find relevant terms like “Proof sketch,” “Proof outline,” or “Proof references” in the files. Let’s compile a list of these items for review!
codex
I’m focusing the report on the defects that are unquestionably unfinished from the source itself: `Proof sketch/outline/references` under `ProvedHere`, multi-clause theorems with one-line proofs, and `ProvedHere` theorems that never receive any proof block in their local section. That keeps the findings hard, not speculative.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\begin\\{proof\\}\\[(Proof sketch|Proof outline|Proof references|References|Sketch|Verification)' chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:2894:\begin{proof}[Verification]
appendices/nonlinear_modular_shadows.tex:197:\begin{proof}[Proof sketch]
chapters/examples/beta_gamma.tex:1678:\begin{proof}[Proof sketch]
appendices/signs_and_shifts.tex:1060:\begin{proof}[Verification]
appendices/koszul_reference.tex:300:\begin{proof}[Proof outline]
chapters/examples/heisenberg_eisenstein.tex:208:\begin{proof}[Proof references]
chapters/examples/heisenberg_eisenstein.tex:842:\begin{proof}[Verification]
chapters/examples/free_fields.tex:808:\begin{proof}[Sketch]
chapters/examples/free_fields.tex:840:\begin{proof}[Verification of Koszul pair conditions]
chapters/examples/free_fields.tex:3925:\begin{proof}[References]
chapters/examples/free_fields.tex:4320:\begin{proof}[References]
chapters/examples/free_fields.tex:4374:\begin{proof}[References]
chapters/examples/yangians_computations.tex:4357:\begin{proof}[Proof sketch]
chapters/examples/yangians_computations.tex:4786:\begin{proof}[Proof sketch]
chapters/examples/w3_composite_fields.tex:293:\begin{proof}[Verification]
chapters/connections/thqg_gravitational_yangian.tex:1756:\begin{proof}[Verification of the CYBE]
chapters/connections/master_concordance.tex:91:\begin{proof}[Proof sketch]
chapters/connections/casimir_divisor_core_transport.tex:905:\begin{proof}[Verification for \(\mathfrak{sl}_2\)]
chapters/connections/genus_complete.tex:1341:\begin{proof}[Proof sketch]
chapters/connections/thqg_introduction_supplement_body.tex:437:\begin{proof}[Proof sketch]

thinking
**Compiling claim info**

I need to focus only on those claims where the status is "ProvedHere." I've already got some scripts prepared for this. Now, I want to create a compact list that includes the necessary claim information. It’s important to ensure that I'm filtering correctly to get just the relevant data for clarity and efficiency. Let’s keep it organized!
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=sorted([p for b in ['chapters','appendices'] for p in Path(b).rglob('*.tex')])
claim_envs={'theorem','proposition','lemma','corollary','maintheorem'}
claim_re=re.compile(r'\\\\begin\\{('+'|'.join(sorted(claim_envs))+r')\\}(?:\\[(["'^'"\\]]*))?')
proof_re=re.compile(r'\\\\begin\\{proof\\}\\[(["'^'"\\]]*(?:Proof sketch|Proof outline|Proof references|References|Sketch|Verification)["'^'"\\]]*)\\]')
comment_re=re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
status_re=re.compile(r'\\\\ClaimStatusProvedHere')

def sc(s): return comment_re.sub('', s)
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        m=claim_re.search(s)
        if m:
            env,title=m.group(1),m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if end_re.search(t): break
                j+=1
            claims.append({'env':env,'start':i+1,'end':j+1,'title':title,'label':label,'status':status})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            prev=None
            for c in claims:
                if c['end']<i+1:
                    prev=c
                else:
                    break
            if prev and prev['status']:
                print(f\"{path}:{i+1}:{prev['env']}:{prev['label']}:{m.group(1)}\")
        i+=1
PY" in /Users/raeez/chiral-bar-cobar succeeded in 213ms:
appendices/koszul_reference.tex:300:theorem:thm:essential-image-koszul:Proof outline
appendices/nonlinear_modular_shadows.tex:197:theorem:thm:nms-mc-principle:Proof sketch
appendices/signs_and_shifts.tex:1060:proposition:prop:LV-conversion-complete:Verification
chapters/connections/casimir_divisor_core_transport.tex:905:theorem:thm:growth-mode-factorization:Verification for \(\mathfrak{sl}_2\)
chapters/connections/genus_complete.tex:1341:proposition:prop:sewing-universal-property:Proof sketch
chapters/connections/master_concordance.tex:91:theorem:thm:master-seven-face:Proof sketch
chapters/connections/thqg_gravitational_yangian.tex:1756:proposition:prop:thqg-V-rtt-from-sgybe:Verification of the CYBE
chapters/examples/free_fields.tex:840:theorem:thm:single-fermion-boson-duality:Verification of Koszul pair conditions
chapters/examples/heisenberg_eisenstein.tex:208:theorem:thm:heisenberg-sewing:Proof references
chapters/examples/heisenberg_eisenstein.tex:842:theorem:thm:dmvv-agreement:Verification
chapters/examples/w3_composite_fields.tex:293:theorem:thm:arakawa-verification-complete:Verification
chapters/examples/w_algebras_deep.tex:2894:corollary:cor:ds-theta-descent:Verification
chapters/examples/yangians_computations.tex:4786:theorem:thm:yangian-H2-reduction:Proof sketch
chapters/theory/chiral_modules.tex:330:proposition:prop:module-koszul-equivalence:Verification
chapters/theory/configuration_spaces.tex:4527:theorem:thm:normal-crossings-verified:Verification for $n=3$
chapters/theory/introduction.tex:1355:theorem:thm:e1-primacy:Proof sketch

thinking
**Inspecting theorem contexts**

I need to check these contexts for possible verification on a specific case regarding a general theorem, as there seems to be a clear defect. I wonder if the theorem titles or contents are complex, so I'll inspect a subset of them. It feels like there could be quite a few, but I think it should be manageable if I concentrate on around 16 relevant ones. Let's see how this goes!
codex
I’ve isolated 16 status-heavy sketch/reference/verification proofs. I’m reading them directly now; these are usually the cleanest unfinished-work defects because the file itself tells you the proof is not complete.
exec
/bin/zsh -lc "sed -n '260,325p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '870,925p' chapters/connections/casimir_divisor_core_transport.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '160,215p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '70,110p' chapters/connections/master_concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
factorization.

\begin{theorem}[Growth-mode factorization for
 \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat};
 \ClaimStatusProvedHere]
\label{thm:growth-mode-factorization}
\index{growth-mode factorization}
The spectral discriminant of \(\widehat{\mathfrak{sl}}_2\) factors as
\begin{equation}\label{eq:growth-mode-factor}
\Delta_{\widehat{\mathfrak{sl}}_2}(x)
=(1-3x)(1+x)
=(1-(\dim\mathfrak{sl}_2)\,x)\cdot
\Delta^{\mathrm{DS}}_{\mathfrak{sl}_2}(x),
\end{equation}
where:
\begin{enumerate}[label=\textup{(\roman*)}]
\item
\(\Delta^{\mathrm{DS}}_{\mathfrak{sl}_2}(x)=1+x\) has degree~\(1\).
\item
\(\Delta^{\mathrm{DS}}_{\mathfrak{sl}_2}\) divides
 succeeded in 51ms:
 generating the Sklyanin Poisson bracket on the space of
 $\cA^{!}$-line-operator configurations; the Yangian quantizes
 this classical Poisson structure \textup{(Semenov-Tian-Shansky
 1983)}.
 \item \emph{Gaudin Hamiltonian generator}\/: $r(z)$ is the
 generating function of the Gaudin Hamiltonians
 $H_i^{\mathrm{Gaudin}}=\sum_{j\neq i}k\,\Omega_{ij}/(z_i-z_j)$
 and their higher-collision generalizations
 \textup{(Feigin--Frenkel--Reshetikhin 1994)}.
\end{enumerate}
The identifications $\mathrm{F1}\Leftrightarrow\mathrm{F4}$ and
$\mathrm{F1}\Leftrightarrow\mathrm{F7}$ are proved in this monograph;
the identifications $\mathrm{F1}\Leftrightarrow\mathrm{F2}$ and
$\mathrm{F1}\Leftrightarrow\mathrm{F3}$ are proved in Volume~II and
in Khan--Zeng's companion paper; the identification
$\mathrm{F5}\Leftrightarrow\mathrm{F6}$ is Drinfeld's and
Semenov-Tian-Shansky's classical result; the three-parameter
normalization identifying $\hbar$ with the reciprocal of the level
shift $(k+h^{\vee})$ is proved here.
\end{theorem}
 succeeded in 52ms:
$L_\infty$ structure whose higher brackets $\ell_k$ ($k \geq 3$)
arise from the Feynman transform of the modular operad
$\{C_\bullet(\overline{\cM}_{g,n})\}$ via $A_\infty$/$L_\infty$
homotopy transfer \cite[\S10.3]{LV12}. The dg~Lie bracket $[-,-]$
is the binary truncation. The Maurer--Cartan equation
\eqref{eq:nms-mc-equation} is the strict shadow of the full $L_\infty$
MC equation $\sum_{n \geq 1} \frac{1}{n!}\ell_n(\Theta,\ldots,\Theta) = 0$;
for the coderivation model these coincide (this is
the MC moduli identification invoked in
Definition~\ref{def:nms-modular-convolution-lie}).
The full $L_\infty$ MC equation admits \emph{gauge equivalences} (homotopies between MC elements):
two MC elements related by $L_\infty$ gauge transform give
quasi-isomorphic bar complexes. This is the homotopy-theoretic reason
that bar-cobar inversion (Theorem~B) is well-defined up to
quasi-isomorphism.
\end{remark}

\begin{theorem}[Algebra structure $=$ Maurer--Cartan element; \ClaimStatusProvedHere]
\label{thm:nms-mc-principle}%
\index{Maurer--Cartan element!modular}%
 succeeded in 53ms:
\end{question}

\begin{remark}\label{rem:why-essential-image-matters}
The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
\end{remark}

\subsection{Main characterization theorem}

\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
A chiral coalgebra $\widehat{\mathcal{C}}$ is (isomorphic to) the Koszul dual 
$\mathcal{A}^!$ of some chiral algebra $\mathcal{A}$ if and only if:

\begin{enumerate}
\item \emph{Conilpotency.} $\widehat{\mathcal{C}}$ is conilpotent: every element of $\ker(\epsilon)$ is annihilated by a sufficiently high iterate of the reduced coproduct $\bar{\Delta}$:
 \[\ker(\epsilon) = \bigcup_{n \geq 0} \ker(\bar{\Delta}^{(n)})\]
 
\item \emph{Connected.} The counit is surjective onto the ground field:
 \[\epsilon: \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}\]
 
\item \emph{Geometric representability.} $\widehat{\mathcal{C}}$ admits a presentation as sections of a $\mathcal{D}_X$-module coalgebra on the Ran space of~$X$; equivalently, there exists a factorization coalgebra~$\mathcal{F}$ such that $\widehat{\mathcal{C}} \simeq \Gamma(\mathrm{Ran}(X),\, \mathcal{F})$, compatible with the operadic structure of the Fulton--MacPherson compactification
exec
/bin/zsh -lc "sed -n '1310,1385p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4750,4805p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '180,235p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,855p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
contains the matrix-valued meromorphic function; the $\Einf$ side
contains its $\Sigma_n$-symmetrized scalar.

\begin{theorem}[$\Eone$ primacy; \ClaimStatusProvedHere]
\label{thm:e1-primacy}
\index{primacy thesis!E1@$\Eone$|textbf}
\index{averaging map!information loss}
\index{Reynolds operator!as averaging map}
Let\/ $\cA$ be a cyclic chiral algebra on\/~$X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Surjectivity.)}
 The averaging map
 $\operatorname{av}\colon {\gAmod}^{\Eone}
 \twoheadrightarrow \gAmod$
 \textup{(}\eqref{eq:intro-averaging}\textup{)}
 is a surjective dg~Lie morphism.
\item \textup{(MC projection.)}
 $\operatorname{av}$ sends
 $\Theta_\cA^{\Eone} \mapsto \Theta_\cA$
 \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
 succeeded in 53ms:
of the affine Heisenberg vertex algebra. This suggests that the
sewing envelope (\S\ref{sec:analytic-completion}) of the algebraic
Heisenberg VOA is exactly $\operatorname{Sym} A^2(D)$, making
the Heisenberg the first model in which the entire analytic
completion programme is explicit.
\end{remark}

\begin{theorem}[Heisenberg sewing theorem;
\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
\index{Heisenberg!sewing theorem}%
Under the mode--Bergman correspondence~$\Theta$
\textup{(}Remark~\textup{\ref{rem:heisenberg-mode-bergman}}\textup{)}:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(\ClaimStatusProvedElsewhere, Moriwaki~\cite{Moriwaki26b})}
 The sewing envelope of the algebraic Heisenberg VOA is exactly
 $\operatorname{Sym} A^2(D)$.
\item \textup{(\ClaimStatusProvedHere)}
 The completed bar differential is the closure of the Gaussian
 collision operator on Bergman tensors.
\item \textup{(\ClaimStatusProvedHere)}
 succeeded in 53ms:
\label{def:yangian-exact-support-dg-lie}
\index{exact-support deformation!dg Lie algebra}
Fix a pairwise MC background~$\rho$. Define
\begin{equation}
 \fg_{\mathrm{ex}}(\rho)
 :=
 \prod_{|I| \ge 3} L_I\langle I\rangle,
\end{equation}
with differential $\delta_\rho$ and bracket $[-,-]_{\mathrm{ex}}$
given by full-support projection of the twisted differential and
bracket. Then $(\fg_{\mathrm{ex}}(\rho), \delta_\rho,
[-,-]_{\mathrm{ex}})$ is a complete dg Lie algebra, and $x \in
\fg_{\mathrm{ex}}(\rho)^1$ is Maurer--Cartan if and only if
$\cA_I(x) := R_I + \widetilde{x}_I$ is Maurer--Cartan on every
ordered set~$I$.
\end{definition}

The decisive reduction theorem places the first obstruction squarely
in the three-leg sector.

 succeeded in 51ms:
Cross-check against the $bc$ shadow engines in
\texttt{compute/tests/} (the full family of $bc$-shadow tests all
evaluate a weight-independent shadow depth of $4$).
\end{proof}


\subsection{\texorpdfstring{Free fermion $\leftrightarrow$ free boson: single-generator Koszul duality}{Free fermion--free boson: single-generator Koszul duality}}

\begin{theorem}[Single-generator fermion-boson duality; \ClaimStatusProvedHere]\label{thm:single-fermion-boson-duality}
The free fermion $\mathcal{F} = \Lambda^{\mathrm{ch}}(\psi)$ (one fermionic generator) and the free boson $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$ (one bosonic generator) form a Koszul pair:
\[\mathcal{F}^! \cong \mathrm{Sym}^{\mathrm{ch}}(\gamma), \qquad
 (\mathrm{Sym}^{\mathrm{ch}}(\gamma))^! \cong \mathcal{F}.\]
This is the chiral incarnation of the operadic duality $\mathrm{Lie}^! = \mathrm{Com}$
in a single generator.
\end{theorem}

\begin{remark}
This single-generator duality should not be confused with the \emph{two-generator} duality $(\beta\gamma)^! \cong bc$ of Theorem~\ref{thm:betagamma-bc-koszul}. Here both sides have $\dim V = 1$; in the $\beta\gamma$--$bc$ duality, both sides have $\dim V = 2$.
\end{remark}


thinking
**Evaluating proof completeness**

I need to check if the proof covers all necessary points. It seems to address factorization and DS invariance, but it doesn’t tackle items (iii)-(iv), which seems strong. I’m wondering about the `yangian-H2-reduction` proof sketch — could it actually be complete enough? It presents a spectral sequence argument in four lines. But since it’s labeled as a "proof sketch," it feels unfinished. I should also inspect the introduction of the `thm:e1-primacy` proof sketch, which seems lengthy but lacks closure. Let's see if there’s a continuation.
exec
/bin/zsh -lc "sed -n '1385,1425p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
{\gAmod}^{\Eone}$ with $\operatorname{av} \circ s = \id$.
Such a section would lift the commutative MC element
$\Theta_\cA$ to an ordered element in the image of~$s$;
but the pentagon constraint on $\ker(\operatorname{av})$
forces the degree-$3$ component of any lift to involve
$\Phi_{\mathrm{KZ}}$, which does not lie in the image
of any linear section.
\end{proof}

\begin{remark}[Categorical $E_1$ primacy]
\label{rem:categorical-e1-primacy}
Theorem~\ref{thm:e1-primacy} is a dg Lie statement. The categorical
analogue (that the braided monoidal category $\mathcal{C}_{\mathrm{line}}$
of line operators is the primitive categorical datum, with modular tensor
categories derived via the Drinfeld center
$Z(\mathcal{C}_{\mathrm{line}})$) amounts to DK-5
(Conjecture~\ref{conj:dk5-restricted}). The proved content (MC3 on the
evaluation-generated core for all simple types,
Theorem~\ref{thm:categorical-cg-all-types}) establishes the base case.
The full categorical $\Eone$ primacy theorem $=$ DK-5.
codex
The sketch/outline hits are real. I’m checking the “no proof block at all” surfaces next, starting with core theory files rather than frontier prose, because a missing proof in the theory lane is more damaging than a summary theorem in a connection chapter.
exec
/bin/zsh -lc "sed -n '600,730p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1088,1128p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '238,290p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1388,1450p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The Laurent expansion near $z = 0$ is:
\begin{equation}\label{eq:frame-green-laurent}
G_\tau(z) = \frac{1}{z}
- \frac{\pi^2 E_2(\tau)}{3}\, z + O(z^3).
\end{equation}
At genus~$0$, only the pole $1/z$ survives. The $E_2$-term
is the first appearance of modular forms in the bar complex.

\subsection{The genus-1 two-point function}

The Heisenberg two-point function on $E_\tau$ is
\begin{equation}\label{eq:frame-genus1-2pt}
\langle \alpha(z_1)\, \alpha(z_2) \rangle_{E_\tau}
= k \cdot G_\tau(z_1 - z_2).
\end{equation}

The genus-$1$ partition function is computed by the following theorem.

\begin{theorem}[Genus-1 Heisenberg partition function; \ClaimStatusProvedHere]\label{thm:genus1-heisenberg}
 succeeded in 53ms:
at $n = 2$, explicit computation gives a $5$-dimensional
space with weights $\{-2, -1, 0, 1, 2\}$, each of
multiplicity one ($= V_2$);
at $n = 3$, a $7$-dimensional space with weights
$\{-3, \ldots, 3\}$ ($= V_3$).
The full conjecture at all~$n$ would follow from an
identification of $H^n$ with the Kostant harmonic
space~$\mathcal{H}^n$ in the nilpotent radical,
restricted to the loop grading at total weight
$n(n{+}1)/2$.
\end{remark}

\section{\texorpdfstring{General $\widehat{\mathfrak{g}}$: functorial construction}{General g: functorial construction}}

\subsection{Abstract setting}

\begin{theorem}[Universal Koszul duality for affine Kac--Moody; \ClaimStatusProvedHere]\label{thm:universal-kac-moody-koszul}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

 succeeded in 53ms:
the linear order.
\end{proposition}

\begin{proof}
This follows from the associativity of operadic composition
in $\End^{\mathrm{ch}}_A$. See the detailed proof given
below in \S\ref{subsubsec:proof-brace-identity}.
\end{proof}

\begin{theorem}[Brace dg algebra; \ClaimStatusProvedHere]
\label{thm:brace-dg-algebra}
\index{brace algebra!dg structure}
Let $(A, \{m_k\})$ be a curved $\Ainf$-chiral algebra.
Then the triple
$\bigl(C^\bullet_{\mathrm{ch}}(A, A),\, \delta,\,
\{-\}\{-, \ldots, -\}\bigr)$
is a \emph{brace dg algebra}: the brace operations
satisfy the following four identities.

\begin{enumerate}[label=\textup{(B\arabic*)}]
 succeeded in 53ms:
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
\[
F_g(\cA)
codex
The core-theory “no proof” defects are real. One example is a theorem that is followed by prose and subsubsections proving components, but never actually enters a `proof` environment. That still violates the status discipline you asked me to audit.
exec
/bin/zsh -lc "sed -n '590,735p' chapters/theory/computational_methods.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '880,930p' chapters/examples/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '590,660p' chapters/examples/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '130,190p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
construction appears at the $E_2$ page.

\emph{Miura composition.} The free-field realization
$\cW_N \hookrightarrow \cH^{\otimes(N-1)}$ embeds the
$W$-algebra into $N - 1$ Gaussian towers. The quadratic
Sugawara creates quartic cross-correlators from these Gaussian
inputs.

\begin{theorem}[DS transfer consistency]
\label{thm:comp-ds-consistency}
\ClaimStatusProvedHere
For $N = 2, 3, 4, 5$ and levels $k = 1, 2, 3, 5, 10$,
the DS-transferred shadow coefficients $S_r(\cW_N)$ for
$r = 2, \ldots, 20$ agree exactly across all three
methods.
\end{theorem}

These are three descriptions of a single algebraic fact: the
Sugawara construction is a degree-$2$ map on shadow space, and
degree-$2$ maps create branch points from smooth curves.
 succeeded in 51ms:

 succeeded in 52ms:
where the diagonal flow on the joint primary slice agrees with a
single-channel flow.
\end{corollary}

\section{The shadow connection}
\label{sec:w3hol-shadow-connection}

The shadow connection $\nabla^{\mathrm{hol}}$ on the primary slice
of $\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}$ decomposes into a
$T$-line piece and a $W$-line piece. Each piece is a logarithmic
connection of the corresponding shadow metric
(Theorem~\ref{thm:shadow-connection}).

\begin{theorem}[Shadow metric on the \texorpdfstring{$T$}{T}-line; \ClaimStatusProvedHere]
\label{thm:w3hol-Q-T}
On the $T$-line (the primary slice generated by the stress-energy
tensor) the shadow metric of $\Walg_3$ is
\begin{equation}\label{eq:w3hol-Q-T}
Q_T(t) \;=\; c^2 + 12 c\, t +
\frac{180 c + 872}{5c + 22}\, t^2.
 succeeded in 51ms:
\Theta_\cA\bigm|_{\partial\overline{\mathcal{M}}_{0,2}^{\mathrm{coll}}}.
\end{equation}
The notation $r_\cA(z)$ records the residual spectral parameter that
survives the collision: when two marked points~$z_1, z_2$ approach
each other, the bar propagator $\eta(z_1,z_2) = d\log(z_1 - z_2)$
acquires a residue along the diagonal, leaving a one-parameter
family $r_\cA(z) \in \mathrm{End}_\cA(2)[\![z^{-1}]\!]$ indexed by
the relative coordinate $z = z_1 - z_2$.

The existence of $r_\cA(z)$ follows from the bar-intrinsic
construction. $\Theta_\cA$ exists by
Theorem~\ref{thm:mc2-bar-intrinsic}: the universal MC element is
$D_\cA - d_0$, and its restriction to any boundary stratum is
well-defined because $D_\cA$ is a graded morphism on the modular
cyclic complex. Uniqueness up to gauge equivalence is the content
of generic cyclic rigidity
(Theorem~\ref{thm:cyclic-rigidity-generic}): the cyclic deformation
complex has one-dimensional second cohomology in degree~$2$ on the
generic locus. The collision residue is
therefore a canonical invariant of~$\cA$.
codex
The connection chapters have a repeated pattern: a theorem is stated with `\ClaimStatusProvedHere`, then the file says “the proof is distributed across later sections” or gives no proof at all. That’s not a proof block; I’m verifying whether this is a whole theorem ladder or just isolated cases.
exec
/bin/zsh -lc "sed -n '100,380p' chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{definition}[Gravitational phase space]
\label{def:thqg-gravitational-phase-space}
The \emph{gravitational phase space} at genus $g$ is the ambient complex
$\mathbf{C}_g(\cA)$ equipped with the shifted-symplectic Lagrangian splitting
\begin{equation}\label{eq:thqg-lagrangian-splitting}
\mathbf{C}_g(\cA) \;\simeq\; \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
\end{equation}
from the complementarity theorem (Theorem~\ref{thm:quantum-complementarity-main})
and its proved Verdier/ambient shifted-symplectic upgrades
\textup{(}Proposition~\ref{prop:ptvv-lagrangian},
Theorem~\ref{thm:ambient-complementarity-fmp}\textup{)}.
The summands $\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$ are the bulk and defect
sectors. The Verdier involution $\sigma$ interchanges them.
\end{definition}

\section{The sixteen results}
\label{sec:thqg-ten-theorems}

\begin{theorem}[\textbf{G1}: Perturbative finiteness]\ClaimStatusProvedHere







thinking
**Evaluating theorem reports**

This file contains numerous theorems without any proofs, making it a bit chaotic overall. Since it's labeled "ProvedHere," I could report it, but the user specifically requested an audit of unfinished work. The severity seems high because the summaries might be mis-tagged. I might need to check related files to see if proofs are just missing. I’m considering generating a final list of all findings, separating them by severity and mentioning counts properly.
thinking
**Assessing line counts for findings**

I think managing the 44 lines is possible if each one is concise. With a summary, I could get approximately 46 lines total, which fits within the 50-70 line range. I could combine 44 no-proof findings with maybe 10 sketches or short proofs for a total of 54 findings. However, I need to verify that each no-proof candidate truly has no associated proof before proceeding. While I can trust the script output, I should be cautious about unverified claims.
thinking
**Standardizing proof reports**

Some proofs are distributed in later sections, which means they still lack a following proof block. I think I can report all 44 no-proof theorem findings directly from the script. For a precise solution, I could standardize the response by suggesting, "Insert a proof block here or downgrade to `\ClaimStatusProvedElsewhere` with an exact forward reference." Since the current `ProvedHere` is unsupported locally, this standardized fix might meet the user's request. The same approach could apply to sketches and short proofs, making sure they're consistent.
thinking
**Auditing the script**

I'm considering whether to include all 44 items from the script since some are duplicated and in appendices. The user asked for an audit of the current repo, and both files are in there. I think they should be included since each surface is defective. I also need to think about including items in the twisted holography quantum gravity cluster. 

I noticed the proof starts in a subsection, but our no-proof algorithm didn't find it, so I’m wondering if the user wants the following proof block included.
thinking
**Refining proof detection**

I need to refine the no-proof detection process. It seems like we shouldn't count a section as having no proof if there's no claim before the proof—just a subsection heading. In this case, the theorem does have a proof, so I need to filter out these false positives. I should also frame the Heisenberg theorem with prose without a proof block or subsection. I’m thinking maybe I should adjust the detection to allow for a subsection heading between the theorem and proof, searching until the next claim environment.
thinking
**Clarifying proof detection**

The user's question revolves around the "ProvedHere" tags and whether they require a following proof block. I need to consider if the theorem is flagged based on its proof environment. The user's specific request is about having no following proof block. I should be cautious about overlooking the actual proof blocks present. To improve my script, I must focus on identifying claims that lack proof blocks entirely, not just those that might fall under section boundaries. This way, I’ll accurately locate the next proof-bearing claim.
thinking
**Improving theorem claim detection**

I need to compute theorem-like claims that lack a proof before the next proof-bearing claim, while ignoring section boundaries. I’m concerned that this could lead to overcounting if proofs are distributed after later claims. The user specifically requested instances without a following proof block, so if claims come in between without a proof, they might still be counted. I’ll focus on starting detection from the next claim only. This approach should yield more accurate results with fewer false positives.
codex
The earlier “no proof” pass was too aggressive around subsection breaks. I’m re-running it with the stricter rule that only matters for your audit: no proof block before the next proof-bearing claim. That keeps distributed proofs out but still catches unsupported `ProvedHere` surfaces.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=sorted([p for b in ['chapters','appendices'] for p in Path(b).rglob('*.tex')])
claim_re=re.compile(r'\\\\begin\\{(theorem|maintheorem|proposition|lemma|corollary)\\}(?:\\[(["'^'"\\]]*))?')
proof_re=re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
comment_re=re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
status_re=re.compile(r'\\\\ClaimStatusProvedHere')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')

def sc(s): return comment_re.sub('', s)
items=[]
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]; proofs=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        m=claim_re.search(s)
        if m:
            env,title=m.group(1),m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if end_re.search(t): break
                j+=1
            claims.append({'env':env,'title':title,'start':i+1,'end':j+1,'label':label,'status':status})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            proofs.append({'start':i+1,'opt':m.group(1) or ''})
        i+=1
    for idx,c in enumerate(claims):
        if not(c['status'] and c['env'] in {'theorem','maintheorem'}):
            continue
        next_claim=claims[idx+1]['start'] if idx+1<len(claims) else len(lines)+1
        proofs_before_next=[p for p in proofs if c['end']<p['start']<next_claim]
        if not proofs_before_next:
            items.append((str(path),c['start'],c['label'],c['title']))
print('COUNT',len(items))
for item in items:
    print(':'.join(str(x) for x in item))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 233ms:
COUNT 50
appendices/ordered_associative_chiral_kd.tex:5200:thm:yangian-quantum-group:Yangian--quantum group deformation for the affine lineage
chapters/connections/arithmetic_shadows.tex:196:thm:shadow-spectral-correspondence:Shadow--spectral correspondence
chapters/connections/arithmetic_shadows.tex:1402:thm:bg-vir-coincidence:$\beta\gamma$--Virasoro rate coincidence
chapters/connections/arithmetic_shadows.tex:1592:thm:refined-shadow-spectral:Refined shadow--spectral correspondence
chapters/connections/arithmetic_shadows.tex:12592:thm:prime-locality-obstructions:Precise obstructions to prime-locality;
chapters/connections/arithmetic_shadows.tex:12795:thm:riccati-determinacy-assessment:Riccati determinacy; \ClaimStatusProvedHere
chapters/connections/casimir_divisor_core_transport.tex:742:thm:pbw-recurrence:PBW recurrence theorem for
chapters/connections/concordance.tex:4069:thm:pixton-from-shadows:Pixton ideal from shadow obstruction tower; \ClaimStatusProvedHere
chapters/connections/concordance.tex:4962:thm:lagrangian-complementarity:Lagrangian complementarity;
chapters/connections/editorial_constitution.tex:193:thm:master-pbw:Higher-genus PBW concentration for the standard
chapters/connections/editorial_constitution.tex:218:thm:master-theta:Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and
chapters/connections/editorial_constitution.tex:1623:thm:en-koszul-duality-conc:\texorpdfstring{$\mathsf{E}_n$}{En} Koszul duality via configuration
chapters/connections/holographic_datum_master.tex:151:thm:seven-faces-master:Seven-face master theorem; \ClaimStatusProvedHere
chapters/connections/outlook.tex:247:thm:operadic-complexity:Operadic complexity; \ClaimStatusProvedHere
chapters/connections/thqg_gravitational_complexity.tex:878:thm:thqg-genus1-hessian:Genus-$1$ Hessian correction
chapters/connections/thqg_gravitational_complexity.tex:1075:thm:thqg-vanishing-mechanisms:Classification of vanishing mechanisms
chapters/connections/thqg_gravitational_complexity.tex:1359:thm:thqg-grav-landscape:Gravitational complexity census
chapters/connections/thqg_gravitational_complexity.tex:1407:thm:thqg-g2-main:Shadow-depth classification; result (G2)
chapters/connections/thqg_introduction_supplement_body.tex:856:thm:thqg-intro-operadic-complexity:Operadic complexity; \ClaimStatusProvedHere;
exec
/bin/zsh -lc "sed -n '980,1010p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\noindent\emph{Graded symmetry.}
The sign formula in (3) encodes the Koszul sign rule for the fermion system: swapping $\psi_i$ and $\psi_j$ in the tensor product introduces a sign $(-1)^{|\psi_i||\psi_j|}$. Since each fermion has odd degree, this produces $(-1)^1 = -1$ for each transposition, so reversing all $n$ factors gives $(-1)^{n(n-1)/2}$, matching the stated formula.
\end{proof}


\subsection{\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex computation}

\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex; \ClaimStatusProvedHere]\label{thm:betagamma-bar-complex}
The chiral bar complex of the $\beta\gamma$ system has:
\begin{align}
\dim(\bar{B}^1) &= 2, \\
\dim(\bar{B}^2) &= 6
\end{align}
with generators corresponding to ordered monomials of $\beta, \gamma$ (and their descendants under the conformal weight grading) placed on the configuration space with logarithmic forms.

The degrees $n \leq 2$ are verified below.
\end{theorem}

\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank; \ClaimStatusProvedHere]\label{thm:betagamma-bar-dim}
For all $n \geq 1$, $\operatorname{rank}(\bar{B}^n_{\mathrm{geom}}(\beta\gamma)) = 2 \cdot 3^{n-1}$,



thinking
**Evaluating theorem proof status**

I’m looking at an interesting theorem, `thm:betagamma-bar-complex`, which lacks proof prior to the next theorem. I wonder if the following theorem, which discusses ranks, can support it. It seems that part of the statement claiming "degrees n<=2 are verified" is present, but there’s no complete proof; this feels unfinished. I think it might be worth reporting on the no-proof cases, perhaps limiting it to 50 lines for clarity. Some examples might require further inspection to determine their proof status.
thinking
**Organizing theorem proof analysis**

I think I can fit everything within the line limits if I keep things concise while including proof sketches and outlines of short complex proofs. Some no-proof theorems do have sketches later, so I should separate these categories. I might count around 11 theorem-level proofs, determining which are unfinished. I could report on about 61 findings in total, combining the no-proof cases and high findings. It might be good to mention any proofs that end with "..." or "TO BE COMPLETED," stating that there are none among my findings. Additionally, I should include really strong proof examples beyond just sketches.
thinking
**Identifying theorem proofs**

I’m considering reporting a few notable cases like `w3_holographic_datum`, which has no proof and isn't short. Other examples might include `semistrict_modular_higher_spin_w3` and `genus_complete`, among others. However, since the user specifically asked for short complex theorem proofs, I should focus on theorems with proofs shorter than 5 lines and significant non-blank statements (let's say 12 or more). I think I could script an output to gather around 20 of these findings.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=sorted([p for b in ['chapters','appendices'] for p in Path(b).rglob('*.tex')])
claim_re=re.compile(r'\\\\begin\\{(theorem|maintheorem)\\}(?:\\[(["'^'"\\]]*))?')
proof_re=re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
comment_re=re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
status_re=re.compile(r'\\\\ClaimStatusProvedHere')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')

def sc(s): return comment_re.sub('', s)
items=[]
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]; proofs=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        m=claim_re.search(s)
        if m:
            env,title=m.group(1),m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False
            body=[]
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if j>i and t.strip() and not end_re.search(t):
                    body.append((j+1,t.strip()))
                if end_re.search(t): break
                j+=1
            claims.append({'start':i+1,'end':j+1,'title':title,'label':label,'status':status,'body_count':len(body)})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            opt=m.group(1) or ''
            j=i+1; body=[]
            while j<len(lines):
                t=sc(lines[j])
                if re.search(r'\\\\end\\{proof\\}',t): break
                if t.strip(): body.append((j+1,t.strip()))
                j+=1
            proofs.append({'start':i+1,'end':j+1,'opt':opt,'body_count':len(body)})
            i=j+1; continue
        i+=1
    for p in proofs:
        prev=None
        for c in claims:
            if c['end']<p['start']:
                prev=c
            else:
                break
        if prev and prev['status'] and p['start']-prev['end']<=8 and p['body_count']<5 and prev['body_count']>=10:
            items.append((str(path),prev['start'],prev['label'],prev['title'],p['start'],p['body_count']))
print('COUNT',len(items))
for item in items:
    print(':'.join(str(x) for x in item))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 202ms:
COUNT 57
appendices/nonlinear_modular_shadows.tex:527:thm:nms-ambient-complementarity-tangent:Ambient complementarity in tangent form; \ClaimStatusProvedHere:543:3
appendices/nonlinear_modular_shadows.tex:581:thm:nms-cotangent-normal-form:Shifted cotangent normal form; \ClaimStatusProvedHere:608:1
appendices/nonlinear_modular_shadows.tex:771:thm:nms-shadow-master-equations:Quartic shadow master equations; \ClaimStatusProvedHere:797:1
appendices/nonlinear_modular_shadows.tex:953:thm:nms-heisenberg-exact-linearity:Heisenberg exact linearity; \ClaimStatusProvedHere:969:1
appendices/nonlinear_modular_shadows.tex:1142:thm:nms-betagamma-quartic-birth:\texorpdfstring{$\beta\gamma$}{betagamma} quartic birth; \ClaimStatusProvedHere:1162:1
appendices/nonlinear_modular_shadows.tex:1207:thm:nms-archetype-trichotomy:Primitive nonlinear archetype trichotomy; \ClaimStatusProvedHere:1228:4
appendices/nonlinear_modular_shadows.tex:1798:thm:nms-boundary-filtration-quartic-envelope:Boundary filtration of the quartic envelope; \ClaimStatusProvedHere:1818:1
appendices/nonlinear_modular_shadows.tex:2152:thm:nms-quintic-frame-families:Quintic shadow for the three frame families; \ClaimStatusProvedHere:2167:1
appendices/nonlinear_modular_shadows.tex:2171:thm:nms-virasoro-quintic-forced:The Virasoro quintic is forced; \ClaimStatusProvedHere:2186:1
appendices/nonlinear_modular_shadows.tex:2451:thm:nms-unified-summary:Ambient complementarity and nonlinear modular shadows; \ClaimStatusProvedHere:2489:1
chapters/connections/arithmetic_shadows.tex:443:thm:narain-universality:Narain universality:465:4
chapters/connections/arithmetic_shadows.tex:2082:thm:shadow-resonance-locus:\ClaimStatusProvedHere:2096:3
chapters/connections/casimir_divisor_core_transport.tex:1062:thm:common-core-exact-sequences:Common-core exact sequences:1080:3
chapters/connections/dg_shifted_factorization_bridge.tex:480:thm:abelian-strictification:Abelian strictification theorem:493:4
chapters/connections/dg_shifted_factorization_bridge.tex:614:thm:cartan-diagonal-defect-exact:Cartan-diagonal shift defect is exact:641:1
chapters/connections/genus_complete.tex:235:thm:master-tower:Master tower of extensions; \ClaimStatusProvedHere:252:1
chapters/connections/semistrict_modular_higher_spin_w3.tex:657:thm:main-semistrict-modular-higher-spin-package-chapter:Main Theorem: the classical $W_3$ sector defines a semistrict modular higher-spin package \ClaimStatusProvedHere:688:1
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:983:thm:fortified-frontier-package:Fortified frontier package \ClaimStatusProvedHere:1013:3
chapters/connections/thqg_critical_string_dichotomy.tex:1274:thm:vir-self-duality-c13:Virasoro self-duality at $c = 13$;:1304:3




thinking
**Evaluating findings report**

Fifty-seven seems like a lot of findings. While not all may be unfinished, some proofs could be concise and more straightforward. I’m thinking of filtering based on title complexity or proof validation. The user asked for a full return of findings, but sharing highlights may be better. Maybe I could create a report file with all findings listed and provide key points in the final answer. I should definitely consider how best to present this information clearly.
thinking
**Considering report generation**

The instructions mention not to tell the user to copy or save, but linking to a file is permitted. I could create an audit report file since that's not explicitly prohibited. Even though editing is restricted, generating a report isn’t the same issue. I might use a redirect to create the report under `/tmp`. I need to check how to write the report without conflicting with editing guidelines, but summarizing remains crucial for the final answer.
thinking
**Organizing response findings**

The user wants a final response with findings, which complicates things. Instead of presenting everything, I could organize the findings in sections categorized by type. It seems reasonable to focus on unfinished proofs rather than all the trivial theorems. I might consider listing clear unfinished elements such as proof sketches or missing blocks while avoiding trailing ellipses. This could bring the total to around 50. Still, I need to mention that many short proofs were screened and a smaller complex set remains since the user requested those too.
thinking
**Organizing proof findings**

I’m focusing on reporting the top 10 high-confidence proof findings. Keeping it manageable is key! I might include a brief summary of the methodology, such as checking N proof environments and M theorem surfaces. I think no extra explanations are necessary before the findings, but they could come after the summary. I should also gather exact counts for total proofs, maybe computed from a script to get the total proof blocks and theorem claims scanned.
codex
I’ve now got the hard set. There are zero literal `...`/`TO BE COMPLETED` proof endings; the real unfinished-work surface is status inflation: missing proof blocks, proof sketches sold as `ProvedHere`, and a smaller subset of genuinely complex theorems discharged in 1–4 lines.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=sorted([p for b in ['chapters','appendices'] for p in Path(b).rglob('*.tex')])
proofs=0
provedhere_theorems=0
provedhere_theorem_like=0
comment_re=re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
claim_re=re.compile(r'\\\\begin\\{(theorem|maintheorem|proposition|lemma|corollary)\\}')
status_re=re.compile(r'\\\\ClaimStatusProvedHere')
for path in tex_files:
    lines=path.read_text().splitlines()
    i=0
    while i < len(lines):
        s=comment_re.sub('', lines[i])
        if '\\\\begin{proof}' in s:
            proofs += 1
        m=claim_re.search(s)
        if m:
            env=m.group(1)
            end='\\\\end{%s}'%env
            j=i
            status=False
            while j < len(lines):
                t=comment_re.sub('', lines[j])
                if status_re.search(t): status=True
                if end in t: break
                j += 1
            if status:
                provedhere_theorem_like += 1
                if env in {'theorem','maintheorem'}:
                    provedhere_theorems += 1
            i=j
        i += 1
print('proofs',proofs)
print('provedhere_theorems',provedhere_theorems)
print('provedhere_theorem_like',provedhere_theorem_like)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 170ms:
proofs 2770
provedhere_theorems 1203
provedhere_theorem_like 2694
exec
/bin/zsh -lc "sed -n '4490,4545p' chapters/theory/configuration_spaces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{example}[Transition for \texorpdfstring{$D_{12}$}{D12} and \texorpdfstring{$D_{23}$}{D23} in \texorpdfstring{$\overline{C}_3(\mathbb{C})$}{C-bar-3(C)}]\label{ex:transition-d12-d23}
Charts $U_{12}$ (near $D_{12}$) and $U_{23}$ (near $D_{23}$) overlap in the region where
all three points are close but not yet colliding.

\emph{Chart $U_{12}$:} $(u_{12}, \epsilon_{12}, \theta_{12}, z_3)$
\[z_1 = u_{12} + \frac{\epsilon_{12}}{2} e^{i\theta_{12}}, \quad
z_2 = u_{12} - \frac{\epsilon_{12}}{2} e^{i\theta_{12}}, \quad z_3 = z_3\]

\emph{Chart $U_{23}$:} $(u_{23}, \epsilon_{23}, \theta_{23}, z_1)$
\[z_2 = u_{23} + \frac{\epsilon_{23}}{2} e^{i\theta_{23}}, \quad
z_3 = u_{23} - \frac{\epsilon_{23}}{2} e^{i\theta_{23}}, \quad z_1 = z_1\]

\emph{Transition functions.}
To express $U_{23}$ coordinates in terms of $U_{12}$:
\begin{align}
u_{23} &= \frac{z_2 + z_3}{2} = \frac{(u_{12} - \frac{\epsilon_{12}}{2}e^{i\theta_{12}}) + z_3}{2}\\
\epsilon_{23} &= |z_2 - z_3| = \left| u_{12} - \frac{\epsilon_{12}}{2}e^{i\theta_{12}} - z_3 \right|\\
\theta_{23} &= \arg(z_2 - z_3) = \arg\left(u_{12} - \frac{\epsilon_{12}}{2}e^{i\theta_{12}} - z_3\right)
\end{align}


thinking
**Structuring findings efficiently**

I'm considering if I can combine multiple findings into one line instead of having separate lines for each. The structured contract wants singular file and line references, but maybe I can group them as comma-separated values after the file path? For example, I could structure it as `chapters/connections/twisted_holography_quantum_gravity.tex:119,130,149...`. This might help reduce the count while still covering everything. Grouping similar failure modes in the same file seems reasonable too.
codex
I’m collapsing repeated defects into file-local clusters where the same failure pattern repeats line after line. That still keeps the audit exhaustive, but it avoids turning the answer into a 100-line dump of the same sentence.
exec
/bin/zsh -lc "sed -n '4498,4588p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5188,5268p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '190,255p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4058,4105p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
(Definition~\ref{def:chiral-ce-complex}) equipped with
the chiral $\Pthree$ bracket
(Construction~\ref{constr:chiral-p3-bracket}) and the
$\cD$-module structure from the factorisation algebra
on~$X$. It carries a $(k+h^\vee)$-adic filtration
$F^\bullet \CE^{\mathrm{ch}}_k(\fg)$ defined by:
\begin{equation}\label{eq:hbar-filtration}
  F^p \CE^{\mathrm{ch}}_k(\fg)
  \;=\;
  (k+h^\vee)^p \cdot \CE^{\mathrm{ch}}_k(\fg).
\end{equation}
\end{definition}

\begin{theorem}[Structure of the chiral $\Ethree$-algebra]
\label{thm:chiral-e3-structure}
\ClaimStatusProvedHere
Let $\fg$ be a simple Lie algebra.
The chiral $\Ethree$-algebra
$\CE^{\mathrm{ch}}_k(\fg)$ satisfies:
\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 51ms:
$q^H$ operators. The one-loop collapse for the affine lineage ensures
that the bar-complex monodromy on $\mathrm{Conf}_n(E_\tau)$ equals the
KZB monodromy, and the identification follows.
\end{proof}

\subsection{The genus-$1$ deformation: from Yangian to quantum group}
\label{sec:yangian-to-quantum}

The passage from genus~$0$ to genus~$1$ can be summarised as a
deformation of the Yangian $Y_\hbar(\mathfrak{g})$ to the
quantum group $U_q(\mathfrak{g})$.

\begin{theorem}[Yangian--quantum group deformation for the affine lineage]
\ClaimStatusProvedHere
\label{thm:yangian-quantum-group}
\index{Yangian!genus-1 deformation to quantum group|textbf}
\index{quantum group!from Yangian|textbf}
Let $\mathfrak{g}$ be a simple Lie algebra and $k \in \mathbb{C}
\setminus \{-h^\vee\}$ generic.
\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 51ms:
which is the genus-$2$ projection of the full MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$, and projects to a relation in
$R^*(\overline{\mathcal{M}}_2)$.
For class-G algebras (Heisenberg), only the iterated-loop shell
survives, and the projected relation is the genus-$2$ Mumford
relation $\lambda_2^2 = 0$. For class-M algebras (Virasoro),
all three shells contribute, and the planted-forest shell
$\Theta^{(2)}_{\mathrm{pf}}$ produces the first non-Mumford
tautological relation; this should be compared with the
Faber--Zagier relation in $R^2(\overline{\mathcal{M}}_2)$.
\end{remark}

\begin{theorem}[Pixton ideal from shadow obstruction tower; \ClaimStatusProvedHere]
\label{thm:pixton-from-shadows}% NOTE: retains conj: prefix for backward compatibility; claim is ProvedHere
\index{Pixton relations!generation theorem|textbf}
For any chirally Koszul algebra~$\cA$ whose genus-$0$ shadow data
defines a \emph{semisimple} Frobenius algebra on~$V$, the
MC-descended tautological relations
$\{\operatorname{taut}_{g,n}([\Theta_\cA]_{g,n})
: g \geq 0,\, n \geq 0\}$
together with the Mumford relations generate the Pixton ideal
 succeeded in 53ms:
constrains the spectral coefficients. The question is
whether these constraints are strong enough to reach the
zeros. The answer, for lattice algebras, is that
the shadow depth counts exactly the critical lines of the
constrained Epstein zeta:

\begin{theorem}[Shadow--spectral correspondence]
\label{thm:shadow-spectral-correspondence}
\ClaimStatusProvedHere
Let $V_\Lambda$ be an even lattice vertex algebra of rank~$r$ with
theta function $\Theta_\Lambda\in M_{r/2}(\Gamma)$. Write
$\Theta_\Lambda = c_E\, E_{r/2} + \sum_j c_j f_j$ for the
decomposition into the Eisenstein series~$E_{r/2}$ and Hecke
eigenforms $f_j\in S_{r/2}(\Gamma)$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The constrained Epstein zeta factors as
\begin{equation}\label{eq:epstein-factorization}
 \varepsilon^r_s(V_\Lambda)
 = 2^{-s}\Bigl(
 c_E\,C_E(s)\,\zeta(s)\,\zeta(s-\tfrac{r}{2}+1)
codex
I’m not going to report the `editorial_constitution`/cross-file clusters unless the local source really leaves the theorem hanging. Those files often defer proofs in unusual ways, and I don’t want false positives in an audit like this.
exec
/bin/zsh -lc "sed -n '180,235p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
HS-sewing package
\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
$+$ subexponential sector growth implies HS-sewing convergence;
Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
identification is still conjectural; at genus~$0$ the algebraic
BRST/bar comparison is proved
\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)},
while the tree-level amplitude pairing requires the additional
hypothesis isolated in
Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
orthogonal weak flank, not a link in this dependency chain.

\begin{theorem}[Higher-genus PBW concentration for the standard
 finite-type interacting families]\label{thm:master-pbw}
\ClaimStatusProvedHere{}
The genus-$g$ PBW spectral sequence concentrates at all genera for the
three standard finite-type interacting families treated in the proved
core: affine Kac--Moody
\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
exec
/bin/zsh -lc "sed -n '235,320p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
the all-degree limit~$\Theta_\cA = \varprojlim \Theta_\cA^{\leq r}$
is proved (Theorem~\ref{thm:mc2-bar-intrinsic};
Theorem~\ref{thm:recursive-existence}).

\emph{Resolved intrinsically by
Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}.
The older comparison route of
Theorem~\textup{\ref{thm:mc2-full-resolution}} now supplies the
all-genera scalar package only on the proved uniform-weight lane.
The \texttt{conj:} label prefix is retained for cross-reference
compatibility.
See Definition~\textup{\ref{def:full-modular-package}}.}
\end{theorem}

\begin{conjecture}[Staged factorization-categorical DK/KL extension]
\label{conj:master-dk-kl}
\ClaimStatusConjectured{}
The proved generated-core DK comparison surface
\textup{(}traditionally packaged as DK-2/3\textup{)} on the
evaluation-generated core

thinking
**Inspecting theorems and proofs**

I'm analyzing some theorems that have internal references and commentary but lack proof blocks, which I could report as a cluster. The `twisted_holography_quantum_gravity` theorem ladder seems similar. I also need to look into the `en_koszul_duality` theorem, ensuring no proof block comes before the next claim. Perhaps it's like the chiral_center_theorem, where there's a theorem followed by a lemma used in its proof. I should inspect further lines after the lemma for later proof references. Let's dig deeper!
exec
/bin/zsh -lc "sed -n '4588,4720p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
genus-$0$ collision residue\textup{)} satisfy
\begin{equation}\label{eq:bv-p3-commute}
  [\Delta, \{a,-\}^{\mathrm{ch}}] = 0
  \quad \text{for all } a \in \CE^{\mathrm{ch}}(\fg_k).
\end{equation}
\end{lemma}

\begin{proof}
The abstract $\Ethree$-algebra structure on the derived
chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$
is provided by Proposition~\ref{prop:e3-structure}(ii)
via the Higher Deligne Conjecture applied to the
$\Etwo$-coalgebra $\BarSig(V_k(\fg))$.
This abstract $\Ethree$ structure includes, in particular,
an abstract BV operator $\Delta_{\mathrm{HDC}}$
(from the framed $\Etwo$ structure) and an abstract
$\Pthree$ bracket $\{-,-\}_{\mathrm{HDC}}$
(the degree-$(-2)$ Lie bracket from the $S^2$ fundamental
class of $\Conf_2(\RR^3)/\RR^+$). These satisfy all
$\Ethree$ compatibility conditions, including

thinking
**Evaluating theorem proofs**

I’m realizing that our no-proof algorithm may flag false positives because it’s not accounting for claims that may be lemmas appearing before actual proof blocks. The user wasn’t asking for a following proof block, so I wonder if having later proof is still acceptable. We should find actual no-proof surfaces where there isn’t a relevant proof block nearby, and I’ll need to compute this at the theorem level to ensure accuracy. Let’s get started on that.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=sorted([p for b in ['chapters','appendices'] for p in Path(b).rglob('*.tex')])
claim_re=re.compile(r'\\\\begin\\{(theorem|maintheorem)\\}(?:\\[(["'^'"\\]]*))?')
proof_re=re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
comment_re=re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
status_re=re.compile(r'\\\\ClaimStatusProvedHere')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
section_re=re.compile(r'\\\\(chapter|section|subsection|subsubsection)\\*?\\b')

def sc(s): return comment_re.sub('', s)
items=[]
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]; proofs=[]; sections=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        if section_re.search(s): sections.append(i+1)
        m=claim_re.search(s)
        if m:
            env,title=m.group(1),m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if end_re.search(t): break
                j+=1
            claims.append({'start':i+1,'end':j+1,'label':label,'title':title,'status':status})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            proofs.append({'start':i+1,'opt':m.group(1) or ''})
        i+=1
    for idx,c in enumerate(claims):
        if not c['status'] or not c['label']: continue
        next_claim = claims[idx+1]['start'] if idx+1<len(claims) else len(lines)+1
        immediate = any(c['end'] < p['start'] < next_claim for p in proofs)
        if immediate:
            continue
        # allow explicit later proof of theorem label before next section
        next_section = next((sl for sl in sections if sl > c['end']), len(lines)+1)
        explicit_later = any(c['label'] in p['opt'] and c['end'] < p['start'] < next_section+200 for p in proofs)
        if not explicit_later:
            items.append((str(path),c['start'],c['label'],c['title']))
print('COUNT',len(items))
for item in items:
    print(':'.join(str(x) for x in item))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 215ms:
COUNT 36
chapters/connections/arithmetic_shadows.tex:12592:thm:prime-locality-obstructions:Precise obstructions to prime-locality;
chapters/connections/casimir_divisor_core_transport.tex:742:thm:pbw-recurrence:PBW recurrence theorem for
chapters/connections/concordance.tex:4069:thm:pixton-from-shadows:Pixton ideal from shadow obstruction tower; \ClaimStatusProvedHere
chapters/connections/concordance.tex:4962:thm:lagrangian-complementarity:Lagrangian complementarity;
chapters/connections/editorial_constitution.tex:193:thm:master-pbw:Higher-genus PBW concentration for the standard
chapters/connections/holographic_datum_master.tex:151:thm:seven-faces-master:Seven-face master theorem; \ClaimStatusProvedHere
chapters/connections/outlook.tex:247:thm:operadic-complexity:Operadic complexity; \ClaimStatusProvedHere
chapters/connections/thqg_gravitational_complexity.tex:1075:thm:thqg-vanishing-mechanisms:Classification of vanishing mechanisms
chapters/connections/thqg_gravitational_complexity.tex:1359:thm:thqg-grav-landscape:Gravitational complexity census
chapters/connections/thqg_introduction_supplement_body.tex:856:thm:thqg-intro-operadic-complexity:Operadic complexity; \ClaimStatusProvedHere;
chapters/connections/twisted_holography_quantum_gravity.tex:119:thm:thqg-g1-finiteness:\textbf{G1}: Perturbative finiteness
chapters/connections/twisted_holography_quantum_gravity.tex:130:thm:thqg-g2-complexity:\textbf{G2}: Shadow-depth classification
chapters/connections/twisted_holography_quantum_gravity.tex:149:thm:thqg-g3-polarization:\textbf{G3}: Symplectic polarization
chapters/connections/twisted_holography_quantum_gravity.tex:159:thm:thqg-g4-s-duality:\textbf{G4}: Gravitational $S$-duality
chapters/connections/twisted_holography_quantum_gravity.tex:174:thm:thqg-g5-yangian:\textbf{G5}: Gravitational Yangian
chapters/connections/twisted_holography_quantum_gravity.tex:188:thm:thqg-g6-soft-graviton:\textbf{G6}: Soft graviton theorems
chapters/connections/twisted_holography_quantum_gravity.tex:213:thm:thqg-g7-bootstrap:\textbf{G7}: Modular bootstrap
chapters/connections/twisted_holography_quantum_gravity.tex:230:thm:thqg-g8-reconstruction:\textbf{G8}: Holographic reconstruction
chapters/connections/twisted_holography_quantum_gravity.tex:247:thm:thqg-g9-critical-string:\textbf{G9}: Critical string dichotomy





thinking
**Analyzing theorem clusters**

I’ve got 36 theorem no-proof surfaces to inspect. It seems I need to group these into clusters for clearer understanding. For instance, `twisted_holography_quantum_gravity.tex` has 13 surfaces, while `frame/heisenberg_frame.tex` actually lists 4, not the 5 I thought. There are a few others I need to verify too, like `free_fields.tex` and `holographic_datum_master.tex`. All in all, I think I counted correctly. This should be manageable as 14 cluster findings. Great!
thinking
**Outlining theorem clusters**

I'm trying to sketch out 8 clusters related to theorem surfaces. For example, the `appendices/koszul_reference.tex` presents an essential image Koszul proof outline, while `appendices/nonlinear_modular_shadows.tex` offers an NMS-MC principle proof sketch. I’m also looking at various proofs and sketches in chapters, like `concordance.tex` for the master seven-face theorem. One point to note is that I have references in `heisenberg_eisenstein.tex`, but no local proof block. So that might be a concern!
thinking
**Evaluating proof references**

I'm considering the user's request regarding unfinished work, specifically referencing that "Proof references" could be acceptable if they're precise. The theorem mentions ProvedHere, which cites other theorems, possibly making it acceptable as a proof sketch. The mission asks for proofs under five lines, not just sketches. However, the subtlety in the sketch might still be important. I see four major proofs, and some might suit the user’s needs even if they seem incomplete, like `H2 reduction` and `nms-mc-principle`.
thinking
**Reviewing theorem proofs**

I’m analyzing a theorem that’s specific to sl2, and its proof seems to cover certain items only partially. It might be better to label this as a short proof issue instead of a verification. The `configuration_spaces` verification for n=3 could be strong and should definitely be included. I also notice that both `casimir_divisor` and the `thm:master-seven-face` proof might require summary sketches. I’ll consider including several items as high importance due to their structure and content. Plus, there's a cluster of short complex theorems to inspect as well.
thinking
**Planning theorem generation**

I'm considering how to generate grouped theorems based on specific criteria: surfaces with a theorem body count of at least 10 and fewer than 5 proofs. I want to focus on instances where there are multiple occurrences. The next step is to count lines by file using a script. This approach seems efficient, and I think it will help in organizing the data effectively for analysis.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from collections import defaultdict
tex_files=sorted([p for b in ['chapters','appendices'] for p in Path(b).rglob('*.tex')])
claim_re=re.compile(r'\\\\begin\\{(theorem|maintheorem)\\}(?:\\[(["'^'"\\]]*))?')
proof_re=re.compile(r'\\\\begin\\{proof\\}(?:\\[(["'^'"\\]]*)\\])?')
comment_re=re.compile(r'(?<"'!'"\\\\)%.*"'$'"')
status_re=re.compile(r'\\\\ClaimStatusProvedHere')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')

def sc(s): return comment_re.sub('', s)
byfile=defaultdict(list)
for path in tex_files:
    lines=path.read_text().splitlines()
    claims=[]; proofs=[]
    i=0
    while i<len(lines):
        s=sc(lines[i])
        m=claim_re.search(s)
        if m:
            env,title=m.group(1),m.group(2) or ''
            end_re=re.compile(r'\\\\end\\{%s\\}'%re.escape(env))
            j=i; label=None; status=False; body=[]
            while j<len(lines):
                t=sc(lines[j])
                if status_re.search(t): status=True
                lm=label_re.search(t)
                if lm and not label: label=lm.group(1)
                if j>i and t.strip() and not end_re.search(t): body.append(t.strip())
                if end_re.search(t): break
                j+=1
            claims.append({'start':i+1,'end':j+1,'label':label,'status':status,'body_count':len(body),'title':title})
            i=j+1; continue
        m=proof_re.search(s)
        if m:
            j=i+1; body=[]
            while j<len(lines):
                t=sc(lines[j])
                if '\\\\end{proof}' in t: break
                if t.strip(): body.append(t.strip())
                j+=1
            proofs.append({'start':i+1,'body_count':len(body)})
            i=j+1; continue
        i+=1
    for p in proofs:
        prev=None
        for c in claims:
            if c['end']<p['start']: prev=c
            else: break
        if prev and prev['status'] and p['start']-prev['end']<=8 and p['body_count']<5 and prev['body_count']>=10:
            byfile[str(path)].append((prev['start'],prev['label'],p['start'],p['body_count']))
for file, items in sorted(byfile.items(), key=lambda kv:(-len(kv[1]), kv[0])):
    if len(items)>=2:
        print(file, len(items), items)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 193ms:
appendices/nonlinear_modular_shadows.tex 10 [(527, 'thm:nms-ambient-complementarity-tangent', 543, 3), (581, 'thm:nms-cotangent-normal-form', 608, 1), (771, 'thm:nms-shadow-master-equations', 797, 1), (953, 'thm:nms-heisenberg-exact-linearity', 969, 1), (1142, 'thm:nms-betagamma-quartic-birth', 1162, 1), (1207, 'thm:nms-archetype-trichotomy', 1228, 4), (1798, 'thm:nms-boundary-filtration-quartic-envelope', 1818, 1), (2152, 'thm:nms-quintic-frame-families', 2167, 1), (2171, 'thm:nms-virasoro-quintic-forced', 2186, 1), (2451, 'thm:nms-unified-summary', 2489, 1)]
chapters/theory/higher_genus_modular_koszul.tex 7 [(3268, 'thm:spectral-characteristic', 3285, 1), (26010, 'thm:tr-shadow-free-energies', 26026, 3), (26050, 'thm:genus4-stable-graph-census', 26073, 3), (26079, 'thm:genus4-free-energy', 26094, 3), (26149, 'thm:bar-macmahon', 26162, 4), (26189, 'thm:shadow-dt-curve-counting', 26203, 3), (33606, 'thm:common-sheet-law', 33619, 1)]
chapters/theory/cobar_construction.tex 3 [(1094, 'thm:fermion-boson-koszul', 1114, 1), (1857, 'thm:cobar-free', 1870, 2), (2624, 'thm:universal-extension-tower', 2642, 1)]
chapters/theory/koszul_pair_structure.tex 3 [(269, 'thm:chiral-hochschild-complex', 282, 1), (1023, 'thm:chiral-yangian-km', 1036, 4), (2069, 'thm:ordered-HH-coHH-cohomology', 2088, 3)]
chapters/connections/arithmetic_shadows.tex 2 [(443, 'thm:narain-universality', 465, 4), (2082, 'thm:shadow-resonance-locus', 2096, 3)]
chapters/connections/dg_shifted_factorization_bridge.tex 2 [(480, 'thm:abelian-strictification', 493, 4), (614, 'thm:cartan-diagonal-defect-exact', 641, 1)]
chapters/connections/thqg_entanglement_programme.tex 2 [(655, 'thm:thqg-entanglement-wedge', 682, 1), (697, 'thm:thqg-page-constraint', 734, 4)]
chapters/connections/thqg_gravitational_complexity.tex 2 [(831, 'thm:thqg-virasoro-potential', 847, 2), (1115, 'thm:thqg-independent-sum', 1131, 4)]
chapters/examples/genus_expansions.tex 2 [(1913, 'thm:universal-generating-function', 1926, 1), (3087, 'thm:complementarity-root-datum', 3107, 2)]
chapters/examples/kac_moody.tex 2 [(1934, 'thm:kac-moody-ainfty', 1950, 3), (2026, 'thm:closed-form-ope', 2039, 1)]
chapters/theory/bar_cobar_adjunction_curved.tex 2 [(6781, 'thm:mixed-boundary-sseq', 6799, 4), (7017, 'thm:casimir-quadric-rigidity', 7040, 4)]
chapters/theory/higher_genus_foundations.tex 2 [(2562, 'thm:bar-cobar-isomorphism-main-equations', 2626, 3), (6148, 'thm:koszul-k0', 6163, 1)]

thinking
**Considering cluster usage**

I'm thinking about how to approach no-proof clusters. Maybe I should consider using the first line of each cluster and then mention all lines in the text. It seems like that could create clarity and help in organizing the information better. I wonder if this method would give a proper overview of the content or if there might be a better way to do it. Let's see how this unfolds!
exec
/bin/zsh -lc "sed -n '5338,5394p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
The Wakimoto module decomposes as a tensor product $\mathcal{M}_{\mathrm{Wak}} = \bigotimes_{\alpha \in \Delta_+} (\beta\gamma)_\alpha \otimes \mathcal{H}_{\mathfrak{h}}$ of free-field archetypes whose bar complexes are computed in~\S\S\ref{sec:bar-complexes-free-fields}--\ref{sec:heisenberg-bar-complex-sec2}. The Drinfeld--Sokolov BRST charge $Q_{\mathrm{DS}}$ commutes with the bar differential ($Q^2 = 0$), so a spectral sequence with $E_1 = H^*(\bar{B}(\mathcal{M}_{\mathrm{Wak}}), d_{\bar{B}})$ and $d_1 = Q_{\mathrm{DS}}$ converges to $H^*(\bar{B}(\mathcal{W}^{-h^\vee}(\mathfrak{g})))$; see Chapter~\ref{chap:w-algebras} for the complete argument.
\end{proof}

\begin{proposition}[Graphical interpretation; \ClaimStatusProvedHere]\label{prop:wakimoto-graph}
The Wakimoto bar complex admits a description via decorated graphs in which vertices carry Wakimoto generators, edges carry log-form propagators $\eta_{ij} = d\log(z_i - z_j)$, and the differential implements Wick contraction (Feynman rule interpretation). See Chapter~\ref{chap:w-algebras} for the complete graphical calculus.
\end{proposition}

\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
\label{thm:w-algebra-ainfty}
\index{W-algebra!$A_\infty$ structure}
The W-algebra $\mathcal{W}^k(\mathfrak{g})$ carries an $A_\infty$
structure $\{m_n\}_{n \geq 1}$ with $m_1 = 0$, $m_2$ the OPE bracket, $m_3$ from triple collisions on $\overline{C}_3(X)$, and higher $m_k$ from $k$-fold collisions via the propagator calculus. The $A_\infty$ relations hold by $d_{\bar{B}}^2 = 0$. See Chapter~\ref{chap:w-algebras} for the full construction and proof via homotopy transfer.
\end{theorem}

\begin{conjecture}[W-algebra \texorpdfstring{$A_\infty$}{A-infinity} and quantum
cohomology; \ClaimStatusConjectured]
\label{conj:w-algebra-quantum-cohomology}
The $A_\infty$ operations of
Theorem~\ref{thm:w-algebra-ainfty} encode the quantum
cohomology of the flag variety: $m_k$ corresponds to

thinking
**Assessing theorem proofs**

This theorem mentions seeing Chapter w-algebras for its proof, which indicates that it should be "Proved Elsewhere" rather than here. It's a good observation. The `free_fields` betagamma bar complex states that it's verified below, but the next theorem's proof might still be sufficient on its own? I think I should take a closer look at this before making a final judgment. There's definitely more to explore here!
codex
I’m reading the `free_fields` misses because they’re a good example of two different failure modes: one theorem promises “verified below” and never gets its own proof, and another cites a proof in another chapter while still carrying `ProvedHere`.
exec
/bin/zsh -lc "sed -n '996,1038p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\end{theorem}

\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank; \ClaimStatusProvedHere]\label{thm:betagamma-bar-dim}
For all $n \geq 1$, $\operatorname{rank}(\bar{B}^n_{\mathrm{geom}}(\beta\gamma)) = 2 \cdot 3^{n-1}$,
where the rank counts the number of independent generator-type sectors in the
geometric bar complex.
\end{theorem}

\begin{proof}
We prove by induction on~$n$.

\emph{Base cases.} The cases $n = 1, 2, 3$ are verified explicitly in the
complete bar complex computation (Theorem~\ref{thm:betagamma-bar-cohomology},
Chapter~\ref{chap:beta-gamma}):
$\operatorname{rank}(\bar{B}^1) = 2$ ($\beta$- and $\gamma$-sectors),
$\operatorname{rank}(\bar{B}^2) = 6$ ($2^2 = 4$ pure tensor types $+$ $2$
derivative types $V_{\partial\beta}, V_{\partial\gamma}$),
$\operatorname{rank}(\bar{B}^3) = 18$ ($2^3 = 8$ pure tensor $+$ $10$ derivative).

\emph{Type decomposition.} The geometric bar complex at bar degree~$n$

thinking
**Inspecting the code**

I’m thinking maybe we need to check the `arithmetc_shadows` at line 12592 since it's showing a no-proof error. I wonder what’s causing that. Should I focus on that specific line to see if there are underlying issues? It could be a good idea to inspect the code around that area to figure out what’s going wrong, ensuring we get to the root of the problem effectively. Let's narrow it down!
exec
/bin/zsh -lc "sed -n '12584,12695p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 constants, the Hecke defect at the shadow coefficient level
 vanishes identically
 \textup{(}Proposition~\textup{\ref{prop:hecke-defect-families}}\textup{)}.
\end{enumerate}
\end{proposition}

\subsection{Where prime-locality fails or is open}

\begin{theorem}[Precise obstructions to prime-locality;
\ClaimStatusProvedHere{} where indicated]%
\label{thm:prime-locality-obstructions}%
\index{prime-locality!precise obstructions|textbf}
The following five obstructions interact and collectively
characterize the difficulty of extending prime-locality
beyond the proved cases:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Lack of $\bZ$-form \textup{(}non-lattice\textup{):}}
 For a lattice VOA, the partition function is built from a theta
 function $\Theta_\Lambda = \sum_{\lambda\in\Lambda} q^{|\lambda|^2/2}$,
 which has integral Fourier coefficients

thinking
**Evaluating theorem classification**

I'm looking at this theorem that's marked "Proved Here where indicated," but it doesn't have a proof. This might be acceptable since it's summarizing statuses instead of requiring a proof. I’m considering converting it to a theorem with proof for clarity, point-by-point, or perhaps making it a remark or status table. I also think about creating a no-proof cluster for key results and maybe labeling it as "Proved Elsewhere." Let's inspect further to clarify.
exec
/bin/zsh -lc "sed -n '238,258p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
(Theorem~\ref{thm:single-line-dichotomy}) proves that on any
one-dimensional primary slice, $r_{\max} \in \{2, 3, \infty\}$;
the contact class $\mathbf{C}$ ($r_{\max} = 4$) escapes via stratum
separation in $\Defcyc^{\mathrm{mod}}$.

\subsection{Operadic complexity theorem}
\label{subsec:concordance-operadic-complexity}
\index{operadic complexity|textbf}

\begin{theorem}[Operadic complexity; \ClaimStatusProvedHere]
\label{thm:operadic-complexity}
For a chirally Koszul algebra~$\cA$,
$r_{\max}(\cA) = A_\infty\text{-depth} = L_\infty\text{-formality level}$.
\end{theorem}

% ======================================================================

\section{Open frontiers}
\label{sec:modular-koszul-programme}
\index{open frontiers|textbf}



thinking
**Summarizing proof findings**

I could say, "Checked: 3973 proof surfaces | Findings: 31 | Verdict: FAIL." But the structure requires just one number, so using "3973" could work. A final summary could be "Checked: 3973 | Findings: 31 | Verdict: FAIL." I need to clarify if there are zero literal proof endings which could be included as a note. Perhaps adding a line before the summary could help, but the user is asking for structured information, so it should stay organized.
thinking
**Considering inclusion of clusters**

I’m thinking I should include the `appendices/nonlinear_modular_shadows` cluster as MEDIUM, but it feels a bit repetitive since it’s still an appendix. Also, I’m considering the `higher_genus_modular_koszul` cluster as MEDIUM too because it’s central to the core theory. There are 7 complex theorems with 1-4 line proofs, which seems pretty critical and maybe more important than some connection chapters. Hm, I’ll need to evaluate this further!
thinking
**Verifying a theorem**

I want to inspect one example to verify a theorem, particularly this one related to spectral characteristics. It feels essential to dig deeper into this to ensure accuracy. I’m considering what aspects I should focus on while reviewing this example so that I can comprehend its implications effectively. It’s interesting how verification can reveal nuances in these concepts! Let’s see what this inspection reveals!
exec
/bin/zsh -lc "sed -n '3248,3290p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Chekhov--Eynard--Orantin topological recursion on the spectral
curve $y^2 = Q_L(t)$
(Theorem~\ref{thm:riccati-algebraicity}). The
\emph{planted-forest} graphs (at least one genus-$0$ vertex of
valence~$\geq 3$) live on codimension-$\geq 2$ strata that
the CEO residue formula does not reach; their sum is
$\delta_{\mathrm{pf}}^{(g,0)}$. At genus~$1$, no planted-forest
graphs exist, so $\delta_{\mathrm{pf}}^{(1,0)} = 0$ and
$F_1 = F_1^{\mathrm{CEO}} = \kappa/24$. At genus~$2$,
$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$
(Remark~\ref{rem:planted-forest-correction-explicit}).
The identity is verified by nine independent paths in
\texttt{compute/lib/theorem\_shadow\_tr\_pf\_engine.py},
including Heisenberg specialization ($\delta_{\mathrm{pf}} = 0$
implies $F_g^{\mathrm{CEO}} = F_g^{\mathrm{shadow}}$),
$\cW_3$ $\mathbb{Z}_2$-parity ($S_3 = 0$ kills
$\delta_{\mathrm{pf}}^{(2,0)}$), and the shadow visibility genus
(Corollary~\ref{cor:shadow-visibility-genus}).
\end{remark}



thinking
**Reflecting on proof requirements**

I see the user asked for proofs of complex theorems that are under five lines, and while this one has a one-line proof citing another theorem, it's still a bit complex. I’m weighing whether this is acceptable since it references an exact theorem. It might not be considered unfinished, but given the user's interest in unfinished work, I realize I may need to focus on short proofs that aren't just concise references. This changes the task significantly.
thinking
**Assessing proof quality**

I'm considering the `higher_genus_modular_koszul` spectral characteristic, which cites another theorem, so it might not need further examination. Many one-line proofs in appendices reference earlier theorems, which could be adequate as well. I think I'll focus on short proofs that don't fully address all parts or are just vague statements. I’ll also look at the proof quality in the `appendices/nonlinear_modular_shadows` cluster. The user requested an audit, but findings may be limited. I need to identify genuinely insufficient short proofs, like the `casimir_divisor_core_transport` verification.
exec
/bin/zsh -lc "sed -n '228,256p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
% ==========================================
% UNIVERSAL TOWER AND SPECTRAL SEQUENCES
% ==========================================

\subsection{The universal genus tower}\label{subsec:universal-tower}
\index{genus tower}

\begin{theorem}[Master tower of extensions; \ClaimStatusProvedHere]\label{thm:master-tower}
There exists a system of restriction maps connecting bar complexes across genera:
\[\cdots \xrightarrow{\rho_{g+1,g}} \bar{B}^{(g+1)}(\mathcal{A}) \xrightarrow{\rho_{g,g-1}} \bar{B}^{(g)}(\mathcal{A}) \xrightarrow{\rho_{g-1,g-2}} \cdots \xrightarrow{\rho_{1,0}} \bar{B}^{(0)}(\mathcal{A})\]

The connecting maps are induced by the boundary divisors of $\overline{\mathcal{M}}_g$:
\begin{itemize}
\item \emph{Nonseparating degeneration.} $\rho_{\text{nonsep}}: \bar{B}^{(g)}(\mathcal{A}) \to \mathrm{Tr}_{\mathcal{A}}(\bar{B}^{(g-1)}(\mathcal{A}))$, where $\mathrm{Tr}_{\mathcal{A}}$ denotes the self-sewing (trace over $\mathcal{A}$), given by $\alpha \mapsto \text{Res}_{D_{\text{nonsep}}}[\alpha]$.
\item \emph{Separating degeneration.} $\rho_{\text{sep}}: \bar{B}^{(g)}(\mathcal{A}) \to \bigoplus_{g_1+g_2=g} \bar{B}^{(g_1)}(\mathcal{A}) \otimes \bar{B}^{(g_2)}(\mathcal{A})$, given by $\alpha \mapsto \text{Res}_{D_{\text{sep}}}[\alpha]$.
\end{itemize}
The tower reflects the modular operad structure of the boundary stratification of $\overline{\mathcal{M}}_g$.

The total complex with string coupling $g_s$:
\[\bar{B}^{\text{total}}(\mathcal{A}) = \widehat{\bigoplus}_{g=0}^\infty g_s^{2g-2} \bar{B}^{(g)}(\mathcal{A})\]
codex
The short-proof category is where I’m being strictest. I’m only keeping cases where the proof text itself is visibly incomplete: a sketch/outline, a verification of only one special case, or a proof that leaves stated clauses untouched. Concise cross-reference proofs by themselves are not enough for me to call something unfinished.
exec
/bin/zsh -lc "sed -n '28,100p' chapters/connections/master_concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$\Theta_{\cA}$ admits seven distinct but equivalent presentations.
Each presentation arises in a different mathematical tradition, uses
different language, and is verified by different compute engines.
The master identification asserts that the seven presentations pick
out the same underlying element of $\cA^{!}\otimes\cA^{!}[\![z^{-1}]\!]$
for every chirally Koszul algebra $\cA$ in the standard landscape.

\begin{theorem}[Seven-face identification;
\ClaimStatusProvedHere\ for faces $1$--$4$, $7$;
\ClaimStatusProvedElsewhere\ for faces $5$--$6$ on Drinfeld $1985$
and Semenov-Tian-Shansky $1983$]
\label{thm:master-seven-face}
Let $\cA$ be a chirally Koszul chiral algebra in the standard
landscape, and let
$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cA})$
be the collision residue of its universal Maurer--Cartan element.
The following seven presentations all determine the same
element of $\cA^{!}\otimes\cA^{!}[\![z^{-1}]\!]$:
\begin{enumerate}[label=\textup{\textbf{(F\arabic*)}}]
 \item \emph{Twisting morphism}\/: $r(z)$ is the genus-zero binary













thinking
**Evaluating proof findings**

I’m analyzing some proof sketches and theorems that are partly proved elsewhere. I need to inspect the `theory/computational_methods` cluster, which contains summary theorems without proofs. I think I should report on that cluster since it seems relevant. Additionally, I’ll check around lines 708 and 788 to confirm no proofs exist. I’m contemplating how to create final findings using 14 critical no-proof clusters and a couple of short proof inadequacies connected with configuration spaces and the Casimir divisor.
thinking
**Identifying proof clusters**

I need to identify more proof clusters. The `appendices/koszul_reference` might outline several points, while verification for `configuration_spaces` only covers n=3 for general n. Checking `casimir_divisor_core_transport` reflects on sl2, leaving some theorem items uncovered. I noticed that the proof sketch for `theory/introduction thm:e1-primacy` may not be complete. It's critical to mention that we found no proof endings with ellipses or "TO BE COMPLETED." 

I'll categorize my findings into clusters: aiming for 20 total findings with potential distributions among critical, high, and medium clusters.
thinking
**Ensuring problem and fix clarity**

I need to ensure that I clearly identify the `PROBLEM` and the corresponding `FIX`. It’s important that these two are exactly matched; otherwise, I can see myself getting confused. Also, it might be a good idea to consider a severity order for the problems to prioritize which ones need addressing first. This way, I can tackle the most critical issues effectively. It's always better to have a structured approach!
thinking
**Evaluating proof options**

I’m looking at the theorem cluster in the frame file and considering my options. I could either insert proof blocks or retag to “ProvedElsewhere” with references to detailed theorems since this chapter might serve as a summary. It seems like adding proof blocks after each theorem could help, but I could also consider downgrading if that’s necessary. However, to be safe, I think the best approach is to retag and cite where proof exists.
thinking
**Considering status tag changes**

I realize that if the proof is located elsewhere, the smart move would be to change the status tag to "ProvedElsewhere." That feels like a solid resolution. For each finding, I think it might be best to remove "\ClaimStatusProvedHere," which keeps things safe for now. If a proof is provided later, I can restore the theorem by adding it back. However, the user is specifically asking for an exact fix, so I'll focus on that.
thinking
**Refining the master_concordance**

I'm considering the theorem for `master_concordance`, which already has mixed statuses. I think I should split it into separate proved-here propositions for faces 1-4 and 7, while creating a proved-elsewhere proposition for faces 5-6. After that, I'll replace the sketch with an actual proof chain or retag the theorem as `ProvedElsewhere`. But I'm wondering if that might be too much—it's a lot to take in!
thinking
**Clarifying repair actions**

I'm considering how to provide local repair actions based on the truth state of the repository. The user specified no guesses, meaning I can only share what the source shows. For instance, with `twisted_holography_quantum_gravity`, since this section is a results list lacking proof blocks, the honest fix would be to stop referring to them as `ProvedHere`. It's all about being clear and truthful about the status!
thinking
**Evaluating proof structure**

I need to consider how to summarize results from computational methods with no proof. I might retag these as `ProvedElsewhere` if the compute engines provide actual proof. It seems better to add proof blocks that explicitly cite the verification engines used. 

The user is asking for a direct fix, so I could suggest "Insert proof blocks referencing the relevant tables and state the finite search space." I’ll craft a structured output with about 20 concise bullet points while possibly including a mention of the lack of proof at the beginning.
thinking
**Summarizing key references**

I've got a list of important references to summarize, including some potentially critical entries. Numbers seven through ten are as follows: 7 for outlook at line 247, 8 concerning editorial constitution at line 193, 9 for concordance between lines 4069 and 4962, and 10 highlighting arithmetic shadows at line 12592. These seem to be pivotal points that should be featured in the final output. Now, let’s put these references together neatly!
thinking
**Considering summary details**

I could mention clarity when summarizing residual omitted information. Maybe it's better to replace something less important, like `nms-mc-principle` or `yangians_H2`. The unfinished proof sketch might be clearer. I think the `nms-mc-principle` is a foundational theorem suitable for the appendix—definitely worth including. As for `yangian_H2`, it feels like an optional addition. If I can keep within a line limit, maybe including 21 findings is manageable and effective.
thinking
**Summarizing proof findings**

I'm working on a proof sketch for a theorem and want to summarize my findings. Should I mention categories and counts in the summary? It's essential to ensure clear grounding for each bullet, like labeling proof blocks properly. I need to address the risk of being too brief since the user wants an exhaustive approach. Counting individual surfaces represented gives me 43, with various clusters covering many aspects, and I’ll make sure to clarify labels for bullets.
thinking
**Formulating proof summary**

In my summary, I think I should mention that there are zero literal ending placeholders, although I wonder if it's necessary to note that many short proofs were filtered as valid cross-references. A concise opening line could say, "Literal trailing '...' / 'TO BE COMPLETED' proof endings: 0." Then I'll present my findings. While the user asked for findings only, setting severity levels can add value. I need to provide compact bullets for each cluster to be clear and effective.
thinking
**Considering bullet formatting**

I’m planning to create a flat bullet list. It seems like one of the bullets might be too long due to many labels in the twisted_holography cluster. It could still fit, but it looks like the final count might reach over 70 lines with 21 bullets plus a summary of around 24 lines. Each bullet is lengthy, but that’s okay. I also need to make sure to use `PROBLEM` and `FIX` in exact uppercase.
codex
- [CRITICAL] `chapters/connections/twisted_holography_quantum_gravity.tex:119` — PROBLEM: `thm:thqg-g1-finiteness`, `thm:thqg-g2-complexity`, `thm:thqg-g3-polarization`, `thm:thqg-g4-s-duality`, `thm:thqg-g5-yangian`, `thm:thqg-g6-soft-graviton`, `thm:thqg-g7-bootstrap`, `thm:thqg-g8-reconstruction`, `thm:thqg-g9-critical-string`, `thm:thqg-g10-fredholm`, `thm:thqg-g14-error-correction`, `thm:thqg-g15-page`, and `thm:thqg-dependency` at lines `119/130/149/159/174/188/213/230/247/270/323/336/360` are all tagged `\ClaimStatusProvedHere`, and each is followed by another claim rather than a proof block. FIX: retag this whole “sixteen results” ladder `\ClaimStatusProvedElsewhere` with theorem-by-theorem citations, or insert a separate `proof` environment under each theorem; do not keep them as `ProvedHere` summaries.
- [CRITICAL] `chapters/frame/heisenberg_frame.tex:1183` — PROBLEM: `thm:frame-heisenberg-koszul-dual`, `thm:genus1-heisenberg`, `thm:frame-genus1-curvature`, and `thm:frame-genus2-curvature` at lines `1183/1407/1429/1577` are `\ClaimStatusProvedHere` without proof environments; the genus-1 curvature lane even begins “The proof is the direct computation” in prose instead of opening `\begin{proof}`. FIX: wrap each argument in an actual proof block, or retag each theorem `\ClaimStatusProvedElsewhere` and cite the detailed theorem already referenced in prose.
- [CRITICAL] `chapters/examples/w3_holographic_datum.tex:603` — PROBLEM: `thm:w3hol-Q-T`, `thm:w3hol-Q-W`, and `thm:w3hol-discriminants` at lines `603/616/627` are consecutive `ProvedHere` theorems with no proof blocks before the next section. FIX: add a proof after each theorem, or collapse the three formulas into one theorem with one proof; until then, remove `ProvedHere`.
- [CRITICAL] `chapters/theory/computational_methods.tex:598` — PROBLEM: `thm:comp-ds-consistency`, `thm:comp-zhu-c-dependence`, and `thm:comp-three-way-bar` at lines `598/708/788` are `ProvedHere` theorems followed only by narrative prose. FIX: insert proof blocks that state the finite computation, the exact search space, and the oracle/engine used, or retag them as computed observations instead of `ProvedHere` theorems.
- [CRITICAL] `chapters/frame/guide_to_main_results.tex:240` — PROBLEM: `thm:guide-family-index` is a `ProvedHere` theorem in the guide chapter with no local proof block. FIX: change it to `\ClaimStatusProvedElsewhere` and cite the proving theorem(s), or add a local proof; guide-level summaries cannot remain `ProvedHere` unsupported.
- [CRITICAL] `chapters/connections/holographic_datum_master.tex:151` — PROBLEM: `thm:seven-faces-master` is `ProvedHere`, but the file immediately says the proof is “distributed” across later sections instead of giving a proof block. FIX: insert a real proof block that assembles the seven identifications, or retag the theorem `\ClaimStatusProvedElsewhere` and leave the distributed discussion as exposition.
- [CRITICAL] `chapters/connections/outlook.tex:247` — PROBLEM: `thm:operadic-complexity` is a bare `ProvedHere` theorem with no proof block before the next section. FIX: downgrade it to `\ClaimStatusProvedElsewhere` with a citation to the proving theorem, or add a proof here.
- [CRITICAL] `chapters/connections/editorial_constitution.tex:193` — PROBLEM: `thm:master-pbw` is tagged `ProvedHere`, but the file moves straight into another theorem and remarks; no proof block is attached. FIX: convert this master-summary theorem to `\ClaimStatusProvedElsewhere` with exact pointers to the family theorems it summarizes, or write a local proof that assembles them.
- [CRITICAL] `chapters/connections/concordance.tex:4069` — PROBLEM: `thm:pixton-from-shadows` and `thm:lagrangian-complementarity` at lines `4069/4962` are `ProvedHere` theorems without proof blocks; `thm:pixton-from-shadows` is followed by a remark titled “Proof of Theorem...” instead of a `proof` environment. FIX: convert those remarks into actual `proof` blocks, or retag both theorems `\ClaimStatusProvedElsewhere` with exact references.
- [CRITICAL] `chapters/connections/arithmetic_shadows.tex:12592` — PROBLEM: `thm:prime-locality-obstructions` is a multi-obstruction theorem tagged `\ClaimStatusProvedHere where indicated`, but the file goes straight into the next subsection with no proof block. FIX: split the five items into separately tagged proved/open propositions with proofs, or keep the theorem and add an item-by-item proof/status block; the current mixed-status theorem cannot remain unproved.
- [CRITICAL] `chapters/connections/thqg_gravitational_complexity.tex:1075` — PROBLEM: `thm:thqg-vanishing-mechanisms` and `thm:thqg-grav-landscape` at lines `1075/1359` are `ProvedHere` theorems with no proof blocks before the next claim. FIX: add proof environments or retag them as `ProvedElsewhere` summaries with exact citations.
- [CRITICAL] `chapters/connections/thqg_introduction_supplement_body.tex:856` — PROBLEM: `thm:thqg-intro-operadic-complexity` is `ProvedHere` and receives no proof block. FIX: make it `\ClaimStatusProvedElsewhere` with the proving reference, or add a proof here.
- [CRITICAL] `chapters/examples/free_fields.tex:987` — PROBLEM: `thm:betagamma-bar-complex` and `thm:w-algebra-ainfty` at lines `987/5345` both lack local proofs; the latter explicitly says “See Chapter~... for the full construction and proof,” which flatly contradicts `\ClaimStatusProvedHere`. FIX: give `thm:betagamma-bar-complex` an actual low-degree proof, and retag `thm:w-algebra-ainfty` `\ClaimStatusProvedElsewhere` unless you inline the proof here.
- [CRITICAL] `chapters/connections/casimir_divisor_core_transport.tex:742` — PROBLEM: `thm:pbw-recurrence` is `ProvedHere` and no proof block appears before the next theorem. FIX: add the recurrence proof here, or retag it `\ClaimStatusProvedElsewhere` with the exact proving citation.
- [HIGH] `appendices/koszul_reference.tex:268` — PROBLEM: `thm:essential-image-koszul` is a five-condition iff theorem marked `ProvedHere`, but the only proof block starts at line `300` and is explicitly “Proof outline.” FIX: replace the outline with a full two-direction proof, or downgrade the theorem to a weaker status until that proof exists.
- [HIGH] `chapters/connections/master_concordance.tex:35` — PROBLEM: `thm:master-seven-face` is partly `ProvedHere`, yet the attached block at line `91` is explicitly a “Proof sketch” that only describes the chain of identifications. FIX: split the theorem into proved-here and proved-elsewhere components with exact proofs/citations, or turn the sketch into a remark and remove the composite `ProvedHere` status.
- [HIGH] `chapters/theory/introduction.tex:1313` — PROBLEM: `thm:e1-primacy` is a four-part theorem tagged `ProvedHere`, but the attached block at line `1355` is explicitly a “Proof sketch.” FIX: retag the introduction theorem `\ClaimStatusProvedElsewhere` and turn the sketch into a roadmap remark, or supply a full proof block that actually proves parts `(i)`–`(iv)`.
- [HIGH] `chapters/theory/configuration_spaces.tex:4518` — PROBLEM: `thm:normal-crossings-verified` states the normal-crossings property for general `\overline{C}_n(X)`, but the only proof at line `4527` is “Verification for n=3.” FIX: either restrict the theorem statement to `\overline{C}_3(\mathbb C)` or replace the verification with a general nested-blowup normal-crossings proof.
- [HIGH] `chapters/connections/casimir_divisor_core_transport.tex:872` — PROBLEM: `thm:growth-mode-factorization` has four clauses, but the proof at line `905` is only “Verification for \(\mathfrak{sl}_2\)” and checks the factorization/DS divisibility, not the theorem’s growth-rate and cancellation clauses. FIX: either shrink the theorem to the explicitly verified `\mathfrak{sl}_2` factorization statement, or add arguments for clauses `(iii)` and `(iv)` and keep the full theorem.
- [HIGH] `appendices/nonlinear_modular_shadows.tex:177` — PROBLEM: `thm:nms-mc-principle` is a foundational equivalence theorem tagged `ProvedHere`, but the attached block at line `197` is explicitly a “Proof sketch.” FIX: expand it into a full equivalence proof constructing the MC element and the inverse algebra structure, or downgrade the claim surface until that proof exists.
- [MEDIUM] `chapters/examples/yangians_computations.tex:4770` — PROBLEM: `thm:yangian-H2-reduction` is tagged `ProvedHere`, but its proof at line `4786` is explicitly a “Proof sketch.” FIX: replace the sketch with a full spectral-sequence argument spelling out the filtration, the `E_1` page, and the no-differential claim, or weaken the status tag.

Literal trailing `...` / `TO BE COMPLETED` proof endings found: `0`. The surviving failures are missing proof blocks and incomplete proof surfaces, not placeholder line endings.

## Summary
Checked: 3973 | Findings: 21 | Verdict: FAIL
tokens used
325,579
