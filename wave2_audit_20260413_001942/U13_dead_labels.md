# U13_dead_labels (838s)

- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` relocation stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: delete the entire `\phantomsection\label{...}` lines; the stubs themselves are no longer needed.
- [HIGH] main.tex:1622 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `ch:ym-higher-body-couplings` (1622), `app:typeA-baxter-rees-theta` (1624), `subsec:cy-research-programmes` (1630), `sec:concordance-e1-modular-theory` (1655), `sec:concordance-structural-upgrades` (1656), `subsec:concordance-koszulness-meta-theorem` (1659), `princ:shadow-depth-escalator` (1660), `princ:physics-is-homotopy-type` (1662), `subsec:concordance-shadow-depth-classes` (1663), `subsec:concordance-further-characterizations` (1664), `subsec:concordance-bifunctor-obstruction` (1665), `subsec:concordance-koszulness-xref` (1666), `subsec:concordance-computational-diagnostics` (1667), `subsec:analytic-completion-programme-editorial` (1670), `sec:concordance-arithmetic-sewing` (1671), `constr:prime-side-li` (1753), `sec:genus-all-master` (1775), `subsec:sewing-gram-matrix` (1781), `def:swiss-cheese-W-resolution` (1835), `thm:branch-bv` (1836), `rem:affine-half-space-bv` (1840), `conj:relative-quartic-computation` (1847), `def:relative-holographic-deformation` (1848), `constr:vol2-oc-mc-element` (1857), `thm:vol2-oc-mc-equation` (1858), `conj:globalization` (1859), `conj:boundary-line-generation` (1860), `conj:khan-zeng-comparison` (1861). FIX: delete the entire stub lines.

The exhaustive grouped report, in your requested `[SEVERITY] file:line — PROBLEM: ... FIX: ...` format, is at [vol1_dead_label_audit.md](/tmp/vol1_dead_label_audit.md). The raw per-label inventory is at [vol1_dead_labels_raw.tsv](/tmp/vol1_dead_labels_raw.tsv).

Method: I scanned live Vol I `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex`, stripped TeX comments, and counted incoming refs across Vol I/II/III `.tex` sources via `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\Cref`, `\pageref`, and `\hyperref[...]`. I did not edit source.

## Summary
Checked: 129 | Findings: 446 | Verdict: FAIL


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
session id: 019d8418-b5fe-7542-bc54-937ed1690476
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

Find all \label{} that are never \ref{}'d anywhere. These are dead labels. For each: is the labeled object still needed? If not, flag for removal.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers



thinking
**Auditing repository labels**

I need to conduct a thorough audit of the repository for labels that aren't referenced anywhere. It's crucial to ground every claim in the contents of the files I've read. I should likely use tools extensively and start with the AGENTS required for the initial reads before making any substantial edits, since this is strictly an audit. The user requests an adversarial audit, so employing deep-beilinson-audit and possibly claim-surface-sync makes sense. I might need to keep the commentary updated with frequent progress reports.
thinking
**Examining skill files for audit**

I need to examine skill files and possibly use parallel tools to read multiple files at once. It's likely I'd update my plan since the task is substantial. I'll send commentary updates before diving into the work and ensure that I read the required files ahead of any substantive edits—though it's just an audit, not editing. I should also consider if I need to read files like CLAUDE/concordance/registry/red_team_summary. My goal is to be exhaustive in searching for dead labels across the repository while keeping the scope manageable.
thinking
**Clarifying label checks across volumes**

The user has requested an audit of a 4500-page manuscript, but I'm currently only looking at Volume I. However, the AGENTS cross-volume rule states that when tasks involve shared formulas, definitions, or other referenced elements, I should consider all three volumes. Since the user specifically asked about dead labels, I need to check for any references across other volumes. They want me to find all instances of \label{} that are never referenced by \ref{} anywhere, even if that means looking across the entire set of volumes.
codex
Using `deep-beilinson-audit` for an adversarial label-surface audit, with `claim-surface-sync` logic where cross-file references matter. I’m first reading the skill instructions and then I’ll compute the actual dead-label set from source rather than eyeballing it.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files -g 'CLAUDE.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g 'raeeznotes/raeeznotes100/red_team_summary.md' -g 'archive/raeeznotes/raeeznotes100/red_team_summary.md'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
 succeeded in 53ms:
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
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/concordance.tex

thinking
**Locating required files**

I need to read the required files, but it looks like the red_team's archive path might not be found. That's a bit concerning! Maybe I should check the specific location and ensure everything is where it should be. I'll plan to locate it carefully. I think using a parallel approach could help streamline this process and avoid delays. Let's see if I can uncover the right path!
codex
I have the audit protocol loaded. Next I’m reading the repo’s live constitutional surfaces and then I’ll derive the dead-label inventory from the `.tex` sources, including cross-volume checks so I don’t misclassify externally referenced labels as dead.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else rg --files | rg 'red_team_summary\\.md"'$'"'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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




thinking
**Auditing dead labels**

I need to perform an audit for dead labels, which involves gathering exact file contents. I should compute a list of all labels and references, looking for those marked with “never \ref{}'d anywhere.” The references can come from various commands like \Cref, \autoref, or \pageref. To avoid false positives, I must inspect how labels are used throughout the repository, potentially including cross-volume references. It looks like I’ll be covering all labels in the repo, including those from other volumes.
thinking
**Determining label references**

I’m considering whether labels referenced only in generated aux files should count towards dead labels. I need to focus on the actual file contents that are read. Running grep across relevant files seems okay, which allows me to avoid reading each file manually. However, the grounding rule states that I should read the lines of each finding file. There could be many dead labels—potentially hundreds—but I need to balance exhaustiveness with not overwhelming the user, ideally keeping responses under 70 lines.
thinking
**Creating a report for findings**

I’m thinking about creating a report file that lists all the dead labels exhaustively and summarizes the findings. The task specifies formatting the results as bullet points, and I’ll likely need to include this exhaustive list, even if it turns out to be lengthy. If there are only a few dozen, I can present all the information. However, if the numbers reach the hundreds, I might provide a link to the report and summarize instead. I’ll focus on direct requests first and avoid unnecessary edits unless asked.
thinking
**Deciding on agent use**

I'm considering whether we should move forward with spawning agents. It seems like avoiding subagents may be the best approach. I'll need to use update_plan, as this feels like a substantial change. My next steps include doing some commentary on the plan, and then I should proceed with the update_plan to ensure everything aligns correctly. It's all about being thorough!
codex
Scope lock: Vol I dead-label audit, with cross-volume reference checks against Vol II and Vol III so I do not falsely call a shared label dead.

Plan:
1. Enumerate every `\label{...}` in Vol I `.tex` sources.
2. Enumerate every live reference macro occurrence across Vol I/II/III `.tex` sources and build the used-label set.
3. Compute Vol I labels with zero incoming references.
4. Re-read each candidate in context and classify whether the labeled object is still structurally needed or should be removed.
5. Re-verify the final list against source lines before reporting.
Plan update
Auditing all dead LaTeX labels in Vol I, with cross-volume reference checks to avoid false positives.
  → Enumerate Vol I label definitions and cross-volume reference uses
  • Inspect each unreferenced label in source context and determine removal/retention fix
  • Re-verify final findings and produce exhaustive report

thinking
**Searching for macro definitions**

I'm trying to compute the labels and references, so I need to know which macros are used. I think we should search for reference macros, like \ref, \eqref, \autoref, and others. There are also potential ones like \thmref, \chapref, and \secref. It looks like it could be involving cleveref, so I want to make sure to check for all definitions of these macros in the preamble. I'll need to use some regex patterns as I search for custom references.
codex
I’m deriving the live reference vocabulary now. If the manuscript uses custom wrappers like `\thmref` or `\secref`, a naive `\\ref{}` grep would misclassify active labels as dead.
exec
/bin/zsh -lc "rg -n --no-heading '\\\\label\\{' chapters appendices frontmatter main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading '\\\\(newcommand|DeclareRobustCommand|NewDocumentCommand|providecommand)\\\\\\\\?[A-Za-z@]*ref' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading '\\\\(ref|eqref|autoref|cref|Cref|vref|Vref|pageref|nameref|thmref|lemref|propref|corref|defref|chapref|secref|appref|partref|fullref|hyperref)\\b' ." in /Users/raeez/chiral-bar-cobar exited 2 in 63ms:
Total output lines: 11417

rg: frontmatter: No such file or directory (os error 2)
main.tex:895:\label{part:bar-complex}
main.tex:1073:\label{part:characteristic-datum}
main.tex:1164:\label{part:standard-landscape}
main.tex:1368:\label{part:physics-bridges}
main.tex:1450:\label{part:seven-faces}
main.tex:1483:\label{part:v1-frontier}
main.tex:1556: \phantomsection\label{thm:general-hs-sewing}% % genus_complete.tex
main.tex:1557: \phantomsection\label{subsec:hs-sewing}% % genus_complete.tex
main.tex:1558: \phantomsection\label{def:hs-sewing}% % genus_complete.tex
main.tex:1559: \phantomsection\label{cor:hs-sewing-standard-landscape}% % genus_complete.tex
main.tex:1560: \phantomsection\label{thm:ds-bar-gf-discriminant}% % landscape_census.tex
main.tex:1561: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
main.tex:1563: \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
main.tex:1565: \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
main.tex:1566: \phantomsection\label{thm:heisenberg-one-particle-sewing}% % genus_complete.tex (8 refs)
main.tex:1567: \phantomsection\label{thm:resonance-filtered-bar-cobar}% % nilpotent_completion.tex (3 refs)
main.tex:1568: \phantomsection\label{thm:frontier-protected-bulk-antiinvolution}% % frontier_modular_holography_platonic.tex
 exited 1 in 113ms:

 succeeded in 115ms:
ex:2232:(Proposition~\ref{prop:fact-dmod-props}(iv)).
./standalone/ordered_chiral_homology.tex:2307:(see Example~\ref{ex:yangian} for the Yangian
./standalone/ordered_chiral_homology.tex:2329:explicitly in \S\ref{sec:examples}) times the Hodge class
./standalone/ordered_chiral_homology.tex:2355:  The curvature~\eqref{eq:fib-curvature} appears in the
./standalone/ordered_chiral_homology.tex:2556:Proposition~\ref{prop:lossy-descent},
./standalone/ordered_chiral_homology.tex:2585:  & \textup{(}Definition~\textup{\ref{def:e1-chiral-rmatrix}}\textup{)} \\
./standalone/ordered_chiral_homology.tex:2588:  & \textup{(}Definition~\textup{\ref{def:ainf-chiral-endo}}\textup{)} \\
./standalone/ordered_chiral_homology.tex:2591:  & \textup{(}Definition~\textup{\ref{def:chiral-coproduct}}\textup{)}
./standalone/ordered_chiral_homology.tex:2611:triangle~\eqref{eq:equiv-triangle}.
./standalone/ordered_chiral_homology.tex:2623:of~\eqref{eq:assoc-embed}.
./standalone/ordered_chiral_homology.tex:2636:(equation~\eqref{eq:stasheff-chiral}) follows from Stokes'
./standalone/ordered_chiral_homology.tex:2655:is the hexagon axiom~\eqref{eq:hexagon}: the two
./standalone/ordered_chiral_homology.tex:2663:is equivalent to the QYBE~\eqref{eq:qybe} for $S(z)$.
./standalone/ordered_chiral_homology.tex:2665:$S$-locality~\eqref{eq:s-locality-sec8} ensures that the
./standalone/ordered_chiral_homology.tex:2666:integrals~\eqref{eq:mk-from-ope} converge: the factor
./standalone/ordered_chiral_homology.tex:2699:identities~\eqref{eq:stasheff-chiral}, so the $\Ainf$
./standalone/ordered_chiral_homology.tex:2742:Definition~\ref{def:chiral-coproduct}(i).
./standalone/ordered_chiral_homology.tex:2744:The OPE compatibility~\eqref{eq:ope-compat} follows from
./standalone/ordered_chiral_homology.tex:2752:(Definition~\ref{def:chiral-coproduct}(iii)) holds because
./standalone/ordered_chiral_homology.tex:2767:Definition~\ref{def:chiral-coproduct}, the vertex







thinking
**Evaluating file handling options**

I'm thinking about how to handle extensive outputs more systematically. I need to compute dead labels, but I can't use Python for reading/writing files. Instead, simple shell commands or apply_patch are recommended. I might use Python for data analysis but will prioritize simpler methods like Perl and Awk. I also need to audit active manuscript files while excluding backups (.bak, *.fix). I'll focus on .tex files and those under chapters, appendices, or standalone papers related to the user's large manuscript.
thinking
**Assessing label audit scope**

I’m thinking about whether to focus only on active files in main.tex, but inactive or standalone files might have labels not part of the manuscript. My mission is to audit and find all labels that are never referenced; these would be dead labels. It seems I should consider all relevant .tex files in the repository, excluding backups. However, if a label is defined in a standalone draft and referenced nowhere, it’s likely still dead. I need to clarify the scope of the audit to the user.
thinking
**Clarifying label audit details**

Since the user asked for every \label{} that's never referenced anywhere, I should consider all .tex files in the repository, excluding backups. It's important to exclude backup artifacts like .bak and .backup files, as they don't represent manuscript surfaces and would just create unnecessary noise. I need to establish a solid rationale for this approach. I can generate a candidate list using `rg --files -g '*.tex'` while omitting any files with .bak or those in the archive directory.
thinking
**Evaluating label instances**

I need to compute defined label instances and check if the label name appears in any reference macros. I shouldn't count the self-definition as a reference. If there are duplicated labels, any incoming reference will count the label's use without identifying which definition it refers to. Since the user is asking about exact dead labels, perhaps each instance of a label name that is never referenced should be considered dead. However, I must decide whether to exclude or note duplicates.
thinking
**Evaluating label relevance**

I need to assess whether labeled objects are still necessary. If not, I should flag them for removal. I’ll read the context around each label to determine if they are still relevant, as many could just be section labels for navigation without cross-references. Some might be anchors for hyperlinks or future migration. For `main.tex`, many `\phantomsection\label{...}` stubs exist to preserve references. I’ll check those lines to decide if they’re essential or candidates for removal.
thinking
**Deciding on label removal**

I need to determine if a theorem requires a label. If it's isolated and not referenced, I can remove just the `\label{...}` and keep the theorem. My usual fix would be to delete the label but keep the object. For structural elements like chapters, labels might be used for TOC or hyperlinks. If they’re unreferenced, only the label should go. For equations, I should remove the `\label{}` but keep the equation itself. I'll inspect the context to see if sections are placeholders and decide if they should be removed too.
thinking
**Assessing label and object relevance**

If the object is a phantomsection stub, the whole line should be removed since it's unnecessary. For empty placeholders, I need to inspect if the object is needed. It might be useful to compute a candidate list programmatically and group by file, but I have to read through each of those lines, which could be a lot. I should estimate how many might be involved. I'll consider using Perl to extract labels and references and possibly write a shell script for this task.
codex
I’ve confirmed the repo has a lot of migration stubs and wrapper labels in `main.tex`, so I’m separating “dead compatibility stub” from “live theorem/section object with unnecessary label.” That distinction matters for the exact fix.
exec
/bin/zsh -lc "rg -o --no-filename '\\\\hyperref\\s*\\[' main.tex chapters appendices standalone papers | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -o --no-filename '\\\\[A-Za-z@]+ref\\s*\\{' main.tex chapters appendices standalone papers | sed 's/[[:space:]]*{"'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -o --no-filename '\\\\(crefrange|Crefrange|cpagerefrange|Cpagerefrange)\\s*\\{' main.tex chapters appendices standalone papers | sed 's/[[:space:]]*{"'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   2 \hyperref[
 succeeded in 53ms:

 succeeded in 53ms:
2085 \eqref
   3 \svy@oldref

thinking
**Revising regex patterns**

I’m thinking about the regex that only captured `eqref`. It seems like the `\ref` macros often have text before them, which might be the issue. The pattern should ideally capture `\ref` too, but maybe backslashes in rg are affecting this. I’ve realized that `rg -o` with the regex `\\[A-Za-z@]+ref\s*\{` only matches `\eqref{` because the `+` requires at least one character before `ref`. I’ll switch to using `*` instead and rerun the command.
exec
/bin/zsh -lc "rg -o --no-filename '\\\\[A-Za-z@]*ref\\s*\\[' main.tex chapters appendices standalone papers | sed 's/[[:space:]]*\\["'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -o --no-filename '\\\\[A-Za-z@]*ref\\s*\\{' main.tex chapters appendices standalone papers | sed 's/[[:space:]]*{"'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   2 \hyperref
 succeeded in 52ms:
18261 \ref
2085 \eqref
   3 \svy@oldref
exec
/bin/zsh -lc "rg -o --no-filename '\\\\[A-Za-z@]*ref\\s*\\{' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | sed 's/[[:space:]]*{"'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -o --no-filename '\\\\[A-Za-z@]*ref\\s*\\[' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | sed 's/[[:space:]]*\\["'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
7978 \ref
1487 \eqref
  22 \cref
   2 \BDref
   1 \pageref
 succeeded in 53ms:


thinking
**Inspecting cross-volume references**

I need to look into how \cref and \BDref are used for cross-volume referencing. It seems like I should inspect \BDref specifically. Maybe I can find definitions in Volume 2, Section III. Also, if labels from Volume I are referenced in Volumes II or III via these commands, they should be counted too. I wonder if I need to search in this repository as well, although I’m guessing I might not find anything there. So, I’ll need to check BDref, possibly looking for custom macro wrapping with \ref.
codex
Vol II/III introduce extra reference macros, so I’m expanding the used-label parser there. Otherwise I’d produce false positives on labels kept alive only by cross-volume references.
exec
/bin/zsh -lc "rg -n --no-heading '\\\\BDref\\s*\\{' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading '\\\\(newcommand|DeclareRobustCommand|NewDocumentCommand|providecommand)\\{\\\\BDref\\}' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading '\\\\cref\\s*\\{' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:252:\providecommand{\BDref}[1]{\textup{[\cite{BD04}, #1]}}
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:405:The distinction is as follows (see \BDref{§2.3, §3.2}):
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:435:Chirality requires: (1) the twist preserves a holomorphic structure on the Coulomb branch \cite{Gai19}; (2) $T(z)$ survives the twist with vanishing anomalies; (3) the factorization algebra extends to a $\mathcal{D}$-module on $\mathrm{Ran}(X)$ (automatic for chiral algebras by \BDref{Chapter 3}, requires verification for twisted gauge theories).
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:695:Let $Q$ be a cocycle parametrized by $(b,C,D,E)$ as in \cref{prop:W3cocycles}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:744:This is the content of \cref{thm:H1W3}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:791:computation of \cref{thm:H1W3} shows that in the relevant sector this torsor is one-dimensional
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:865:result of \cref{cor:unique-lift} into an actual one-loop quantization theorem.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:408:compatibilities with the one-edge expansions, the proof of \cref{thm:modular-bar} goes
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:727:Apply \cref{prop:D0D1} and the argument of the proposition from \S3.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:802:To prove that $d_1\Theta_0$ is closed, use \cref{prop:D0D1}. Since $D_0^2=0$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:851:The same computation as in \cref{thm:Ob1} shows that $R_g$ is closed. The vanishing
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:913:Under the hypotheses of \cref{thm:conditional-tree}, if all obstruction classes vanish,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1066:Apply \cref{lem:BV} to the identity $[P_\Pi,P_\Pi]=0$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1076:shadow of the genus-one forcing term $d_1\Theta_0$ in \cref{thm:Ob1}. In particular, if
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1865:Let $Q$ be a cocycle parametrized by $(b,C,D,E)$ as in \cref{prop:W3cocycles}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1914:This is the content of \cref{thm:H1W3}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:1961:computation of \cref{thm:H1W3} shows that in the relevant sector this torsor is one-dimensional
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:2035:result of \cref{cor:unique-lift} into an actual one-loop quantization theorem.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:547:compatibilities with the one-edge expansions, the proof of \cref{thm:modular-bar} goes
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1415:Apply \cref{prop:D0D1} and the argument of the proposition from \S3.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1536:To prove that $d_1\Theta_0$ is closed, use \cref{prop:D0D1}. Since $D_0^2=0$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1585:The same computation as in \cref{thm:Ob1} shows that $R_g$ is closed. The vanishing
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1647:Under the hypotheses of \cref{thm:conditional-tree}, if all obstruction classes vanish,



thinking
**Auditing Manuscript Structure**

I’m considering using active build files from `main.tex`, which includes chapter inputs and phantom stubs. The user is asking for a manuscript audit, likely focusing on the active build. I think it makes sense to audit only the sources, chapters, and appendices that are included in `main.tex`, as dead labels from standalone documents shouldn't affect the 4500-page manuscript. I need to ensure a comprehensive audit while focusing solely on the active build files mentioned.
thinking
**Considering Cross-References**

I’m thinking of using all `.tex` files in Vol II/III since live cross-references might occur anywhere, and that seems just fine. For definitions in the current repo, I could include labels from `main.tex`, phantom stubs, and the `chapters` and `appendices`. That sounds good! Now, I need to compute the labels defined in this scope to ensure everything connects properly. It's all about being thorough, I guess!
thinking
**Organizing references**

I’m focusing on scoping the main.tex file along with all the chapter and appendix files. That seems good. It looks like I’ll also need to account for cross-volume references in Vol II and Vol III. I think it’d be smart to include the repository’s main, chapters, and appendices as reference sources too. Overall, we can process these along with the volumes, and we don’t need any standalone papers for this task.
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my %defs; my %def_instances; my %refs;
for my "'$file (@def_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
    my "'$label = $1;
    my $pos = $-[0];
    my $line = 1 + substr($text,0,$pos) =~ tr/'"\\n//;
    push @{"'$defs{$label}}, "$file:$line";
  }
}
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref|eqref|cref|Cref|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    my "'$arg = $1;
    for my $label (split /'"\\s*,\\s*/, "'$arg) {
      next unless length $label;
      $refs{$label}++;
    }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) {
    my "'$label = $1;
    $refs{$label}++ if length $label;
  }
}
my @dead;
for my $label (sort keys %defs) {
  next if $refs{$label};
  for my $loc (@{$defs{$label}}) {
    print "$label'"\\t"'$loc'"\\n\";
  }
}
' > /tmp/vol1_dead_labels_raw.tsv
wc -l /tmp/vol1_dead_labels_raw.tsv
sed -n '1,120p' /tmp/vol1_dead_labels_raw.tsv" in /Users/raeez/chiral-bar-cobar succeeded in 664ms:
    7737 /tmp/vol1_dead_labels_raw.tsv
D:bar	chapters/theory/higher_genus_modular_koszul.tex:543
D:bar-htpy	chapters/theory/higher_genus_modular_koszul.tex:436
D:center-dg	chapters/theory/higher_genus_modular_koszul.tex:574
D:center-htpy	chapters/theory/higher_genus_modular_koszul.tex:453
D:deformation-htpy	chapters/theory/higher_genus_modular_koszul.tex:444
D:discriminant-dg	chapters/theory/higher_genus_modular_koszul.tex:579
D:discriminant-htpy	chapters/theory/higher_genus_modular_koszul.tex:459
D:dual	chapters/theory/higher_genus_modular_koszul.tex:549
D:dual-htpy	chapters/theory/higher_genus_modular_koszul.tex:441
D:periodicity-dg	chapters/theory/higher_genus_modular_koszul.tex:584
D:periodicity-htpy	chapters/theory/higher_genus_modular_koszul.tex:464
MK:clutching-verdier	chapters/theory/higher_genus_modular_koszul.tex:673
MK:complementarity	chapters/theory/higher_genus_modular_koszul.tex:633
MK:complementarity-htpy	chapters/theory/higher_genus_modular_koszul.tex:504
MK:e1-face	chapters/theory/higher_genus_modular_koszul.tex:677
MK:inversion	chapters/theory/higher_genus_modular_koszul.tex:625
MK:inversion-htpy	chapters/theory/higher_genus_modular_koszul.tex:498
MK:mc-control	chapters/theory/higher_genus_modular_koszul.tex:669
SA:completion	chapters/theory/introduction.tex:2595



thinking
**Considering report on findings**

I could create a report summarizing all my findings, but the task specifies returning them as bullets. I need to check if the count makes sense because there are 3,615 tagged claims and many equations that aren't referenced later. It seems there could be thousands. I think I should find all labels defined that aren't referenced anywhere, assess if they’re still needed, and flag them for removal if not. But going through all 7,737 manually seems impossible! Automation could be helpful, but the user wants no guesses or inferences.
thinking
**Refining approach for label detection**

I’m considering if I could read file contents for each label, but it seems I need to refine my scope drastically. The task might not cover the entire repository but could focus on unfinished work. Maybe I should look at migration stubs in `main.tex`? However, the user mentioned every label. I think I need to use existing tools or scripts for detecting dead labels. I should search the repository for any existing scripts and utilize them effectively!
thinking
**Searching for unused labels**

I should consider if there's a script to help me find unused labels. It seems like I could use something like "rg unused label" to search for them efficiently. I’ll look into this further to gather the necessary tools or commands. Finding a script would make the process much smoother, and I'm curious about how to implement this effectively. Let's see if I can dig up a solution soon!
codex
The raw dead-label set on the active Vol I tree is very large, so I’m checking whether the repo already has a manuscript-specific detector or ignore policy before I classify thousands of false-actionable equation anchors one by one.
exec
/bin/zsh -lc "rg -n --no-heading 'unused label|dead label|unreferenced label|unused labels|unreferenced labels|label audit|dead-label' scripts compute metadata chapters appendices main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'label\\{' compute/tests scripts metadata | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading 'orphan|dangling|unused|unreferenced' compute scripts metadata ." in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
scripts/adversarial_wave2.py:240:7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
scripts/adversarial_wave2.py:275:    ("U13_dead_labels", VOL1, "Find all \\label{} that are never \\ref{}'d anywhere. These are dead labels. For each: is the labeled object still needed? If not, flag for removal."),
compute/audit/latex_pitfall_blacklist_wave12.md:19:- MINOR: hygiene (prose slop, spacing, unused labels, orphan cites). Warn only.
compute/audit/latex_pitfall_blacklist_wave12.md:375:- Failure mode: dead label; ships with the PDF but no cross-reference reaches it.
 succeeded in 65ms:
scripts/generate_metadata.py:264:            if primary_label in local_line and "\\label{" in local_line:
scripts/generate_metadata.py:287:    """Extract all \\label{} occurrences from a file."""
scripts/adversarial_campaign.py:220:    ("AP09_label_prefix", "AP125: label prefix mismatch", r"grep -n 'begin{conjecture}' chapters/ | while read line; do file=$(echo $line | cut -d: -f1); num=$(echo $line | cut -d: -f2); grep -A5 \"^\" $file | head -6 | grep 'label{thm:'; done 2>/dev/null | head -20", "conj env needs conj: prefix"),
scripts/adversarial_campaign.py:226:    ("AP15_duplicate_labels", "AP124: duplicate labels across volumes", r"grep -roh '\\label{[^}]*}' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30", "Labels must be unique across volumes"),
scripts/adversarial_campaign.py:266:    ("XV09_label_unique_xvol", "Label uniqueness", "labels", "Are there any duplicate \\label{} across all 3 repos? Run: grep -roh '\\\\label{[^}]*}' across all volumes, find duplicates."),
scripts/export_vol1_xrefs.py:5:extracts every \\newlabel{...}{...} and \\new@label@record{...}{...} entry,
compute/tests/test_ap5_cross_volume_checker.py:292:        r"A theorem: \label{thm:shared-label} done.",
compute/tests/test_ap5_cross_volume_checker.py:297:        r"Another theorem: \label{thm:shared-label} done.",
compute/tests/test_ap5_cross_volume_checker.py:312:        r"\label{thm:vol1-only}",
compute/tests/test_ap5_cross_volume_checker.py:317:        r"\label{thm:vol2-only}",
scripts/generate_theorem_dependency_index.py:107:                    if f"\\label{{{label}}}" in local_line:
scripts/adversarial_wave2.py:169:    ("F17_dangling_refs_v1", "chapters/", "Find all \\ref{} that don't resolve. Run: grep -roh '\\\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix."),
scripts/adversarial_wave2.py:275:    ("U13_dead_labels", VOL1, "Find all \\label{} that are never \\ref{}'d anywhere. These are dead labels. For each: is the labeled object still needed? If not, flag for removal."),
scripts/adversarial_wave2.py:348:    ("B17_label_collisions", "Find duplicate labels across all three volumes. grep -roh '\\\\label{[^}]*}' from all three repos, sort, find duplicates. Each duplicate is a finding."),
compute/tests/test_beilinson_auditor.py:124:                "\\label{thm:upstream}\n"
compute/tests/test_beilinson_auditor.py:128:                "\\label{thm:main}\n"
compute/tests/test_beilinson_auditor.py:153:                "\\label{conj:X}\n"
compute/tests/test_beilinson_auditor.py:175:                "\\label{thm:A}\n"
compute/tests/test_beilinson_auditor.py:179:                "\\label{thm:B}\n"
compute/tests/test_beilinson_auditor.py:209:                "\\label{thm:outer}\n"
 succeeded in 90ms:
compute/lib/pixton_genus3_engine.py:443:    """Recursive helper (unused, see result_box_hack)."""
./compute/lib/pixton_genus3_engine.py:443:    """Recursive helper (unused, see result_box_hack)."""
./compute/lib/bc_voronoi_shadow_engine.py:1126:    The parameter 'a' is unused (kept for API compatibility); the check
compute/lib/bc_voronoi_shadow_engine.py:1126:    The parameter 'a' is unused (kept for API compatibility); the check
./scripts/bar_cohomology_table.py:208:    H = [0, 8, 36]  # H[0] unused, H[1]=8, H[2]=36
./compute/lib/sewing_shadow_intertwining.py:347:    b = [0.0] * (q_max + 1)  # b[0] unused
./scripts/adversarial_wave2.py:169:    ("F17_dangling_refs_v1", "chapters/", "Find all \\ref{} that don't resolve. Run: grep -roh '\\\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix."),
./scripts/adversarial_wave2.py:170:    ("F18_dangling_refs_v2", "", "Same for Vol II. Find all \\ref{} that don't resolve in ~/chiral-bar-cobar-vol2/chapters/.", ),
./scripts/adversarial_wave2.py:171:    ("F19_dangling_refs_v3", "", "Same for Vol III. Find all \\ref{} that don't resolve in ~/calabi-yau-quantum-groups/chapters/."),
./scripts/adversarial_wave2.py:240:7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
./scripts/adversarial_wave2.py:269:    ("U07_forward_refs_v1", VOL1, "Find all forward references: \\ref{} to labels that appear LATER in the file or in a later chapter. Are these genuine forward refs or dangling? For dangling: provide the fix."),
./scripts/adversarial_wave2.py:276:    ("U14_orphaned_chapters", VOL1, "Check main.tex for \\input{} commands. Are all chapter files \\input'd? Are there .tex files in chapters/ NOT in the \\input graph? These are orphaned."),
./compute/lib/bar_comparison_engine.py:1463:    log_coeffs = [Fraction(0)] * (max_n + 1)  # index 0 unused
./compute/lib/mc_newton_spectral.py:195:    c_val : unused (kept for API compatibility)
./compute/lib/mc_newton_spectral.py:236:    c_val : unused (kept for API compatibility)
compute/lib/sewing_shadow_intertwining.py:347:    b = [0.0] * (q_max + 1)  # b[0] unused
./compute/lib/koszul_epstein_rankin_selberg.py:242:        Shadow data (unused at genus 1; included for genus-2 extension).
./compute/lib/dt_invariants_bar.py:133:    log_coeffs = [Rational(0)] * (N + 1)  # log_coeffs[0] unused
compute/lib/koszul_epstein_rankin_selberg.py:242:        Shadow data (unused at genus 1; included for genus-2 extension).
compute/lib/bar_comparison_engine.py:1463:    log_coeffs = [Fraction(0)] * (max_n + 1)  # index 0 unused











thinking
**Evaluating grouping strategies**

I’m thinking about how one finding can cover a cluster of labels, allowing me to group them by file. I need to focus on naming exact labels and line numbers for the fix. It’s essential to gather an exhaustive list, but I believe we’re looking at dozens or hundreds of labels, not thousands. 

For any unused labels in a file, I could consolidate them into a single bullet point with a fix. I'll need to determine the best grouping strategy too, maybe by object type and the nature of the fix.
thinking
**Considering grouping options**

I’m contemplating whether to continue grouping by type. For instance, I could look at unused chapter labels, theorem remark labels, and equation labels where the object is still needed but the label isn’t. The fix would be to delete those `\label` commands only.

However, grouping by object type per file could lead to a few hundred bullets, but I think that might be acceptable. I’ll need to calculate the count, especially since there are 7,737 labels across about 100 files. Grouping by file could reduce it to around 100 bullets, which seems more manageable.
thinking
**Considering report creation**

I'm thinking about creating a report file that could include full enumerations as the user requested them to return findings. Maybe I can provide high-level clusters in the final output and say the detailed machine-checked list is in a file, like `[dead_labels_audit.md]`. I wonder if I should create this file in the `/tmp` directory instead of editing the repo, since the user wants exhaustive details. I'll figure out the best way to provide a summary while linking to the full report.
thinking
**Generating an exhaustive report**

I'm considering whether to create an exhaustive markdown report in `/tmp` or at the repo root with a name like `dead_label_audit_...md`. Since I want to avoid modifying the repo, using `/tmp` seems safer. My final output can mention that the "full exhaustive report" is at `[dead_label_audit.md](/tmp/...)`, while ensuring it doesn't exceed 50-70 lines. I think I should summarize key findings, include path details, and categorize the dead labels by severity, likely setting most to LOW. I’ll make sure my report is both thorough and accurate.
thinking
**Assessing severity of dead labels**

I'm evaluating the seriousness of various dead labels in the project. For instance, `main.tex` contains dead `\phantomsection` stubs, which are likely HIGH or MEDIUM risk since they can mislead cross-volume sync due to being unfinished remnants. Duplicate dead labels and unused theorem-label aliases could be MEDIUM if they cause confusion. Unused chapter, section, or equation labels might be LOW. Dead labels on cross-volume compatibility shims could be HIGH since they indicate unfinished work. I’m thinking about creating a report that sorts findings by severity.
thinking
**Evaluating label compatibility**

I could see that the dead compatibility stubs in main.tex could be rated as HIGH due to migration surfaces. Meanwhile, chapter-opening and claim-surface labels that are never used might be considered MEDIUM, while LOW includes equation/section/example label debt. 

I need to check if labeled objects are still necessary. If they aren't, I can flag them for removal. I might need to programmatically inspect file context to confirm whether some sections are needed or empty placeholders. It seems daunting to do this manually for so many labels!
thinking
**Inferring label context**

I might be able to infer from the file type and label location whether the object is within an actual environment—assuming it’s not a phantomsection. The rules state that I shouldn’t present inferences as facts, so I’ll need to do a proper read. 

I could read a bit of context around each label to see if it's attached to elements like `\chapter`, `\section`, or `\begin{theorem}`. Automating this would be great! I can create a script to extract snippets around labels and classify them based on nearby macros. That feels like a solid plan!
thinking
**Determining object types**

I'm breaking down how to determine the kind of object associated with labels. 

If I see a line with `\phantomsection\label{`, it’s a stub, and I can remove the entire line if there are no references. If the preceding line has something like `\chapter{`, `\section{`, or `\subsection{`, that means the object is still needed, and I would just remove the label. Environment labels, including `\begin{theorem}` or `\begin{remark}`, also indicate that the object is needed. I should automate the extraction of lines to help organize and cluster them by type. That feels like an efficient method!
thinking
**Verifying label classification**

I’m thinking about how to approach sorting and verifying labels. Using exact lines and line numbers could help avoid any ambiguity. It seems essential to group labels by file and object type since there might be mixed types. Automated classification sounds like a solid approach, especially when identifying previously flagged labels. However, even with automation, I should ensure accuracy in the final report by relying on context counts instead of manual inspections. It feels a bit overwhelming, but I've got this!
thinking
**Considering report generation**

I’m exploring options for generating a report. The user wants something exhaustive, which makes me think about outputting a machine-checked cluster report with exact lines. I should include a method note and verify each bullet against the source. Presenting top findings in the final report might just lead to a longer document, so instead, maybe I can summarize counts and then point to the full report. However, I grapple with user expectations; it’s tricky but worth considering the best way to scope it down.
thinking
**Exploring automation for reports**

I'm considering how to automate the identification of "object still needed" accurately. For phantom section stubs, I should remove the object, but for others, just the label. This approach could allow for an exhaustive grouped report. I think it’s crucial to compute counts by file and type, so inspecting the distribution should help. Using a script to classify and count sounds like a solid plan to ensure efficiency and accuracy in the report.
codex
I’m switching from per-label prose to a machine-checked cluster report, because the active Vol I build has thousands of unreferenced labels. Each cluster will still cite exact labels and lines, but I need the grouping to keep the output actionable rather than unusable.
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my %refs;
for my "'$file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref|eqref|cref|Cref|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
my %count;
for my $file (@def_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = '"'phantom-stub'; }
      elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = '"'sectioning'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = '"'claimlike'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\\\\\\\?\\s*"'$/) { $kind = '"'displaymath'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = '"'float'; }
      elsif ("'$ctx =~ /'"\\\\item\\b/s) { "'$kind = '"'item'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = '"'list'; }
      "'$count{"$file'"\\t"'$kind"}++;
    }
  }
}
for my $k (sort { $count{$b} <=> $count{$a} || $a cmp $b } keys %count) {
  print "$count{$k}'"\\t"'$k'"\\n\";
}
' | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Bareword "phantom" not allowed while "strict subs" in use at -e line 24.
Bareword "other" not allowed while "strict subs" in use at -e line 23.
Bareword "sectioning" not allowed while "strict subs" in use at -e line 24.
Bareword "claimlike" not allowed while "strict subs" in use at -e line 24.
Bareword "displaymath" not allowed while "strict subs" in use at -e line 24.
Bareword "float" not allowed while "strict subs" in use at -e line 24.
Bareword "item" not allowed while "strict subs" in use at -e line 24.
Bareword "list" not allowed while "strict subs" in use at -e line 24.
Bareword "stub" not allowed while "strict subs" in use at -e line 24.
Execution of -e aborted due to compilation errors.
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my %refs;
for my "'$file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref|eqref|cref|Cref|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
my %count;
for my $file (@def_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = "other";
      if ($lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = "phantom-stub"; }
      elsif ($ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = "sectioning"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = "claimlike"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = "displaymath"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = "float"; }
      elsif ($ctx =~ /'"\\\\item\\b/s) { "'$kind = "item"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = "list"; }
      $count{"$file'"\\t"'$kind"}++;
    }
  }
}
for my $k (sort { $count{$b} <=> $count{$a} || $a cmp $b } keys %count) {
  print "$count{$k}'"\\t"'$k'"\\n\";
}
' | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
269	chapters/theory/higher_genus_modular_koszul.tex	claimlike
244	chapters/theory/higher_genus_modular_koszul.tex	displaymath
140	chapters/connections/arithmetic_shadows.tex	claimlike
106	chapters/theory/higher_genus_foundations.tex	claimlike
102	chapters/connections/thqg_perturbative_finiteness.tex	claimlike
101	chapters/theory/ordered_associative_chiral_kd.tex	claimlike
97	chapters/connections/frontier_modular_holography_platonic.tex	displaymath
97	chapters/examples/w_algebras.tex	claimlike
91	chapters/examples/free_fields.tex	claimlike
91	chapters/theory/bar_cobar_adjunction_inversion.tex	claimlike
90	chapters/connections/arithmetic_shadows.tex	displaymath
81	chapters/examples/genus_expansions.tex	claimlike
79	chapters/examples/w_algebras.tex	displaymath
76	chapters/connections/thqg_perturbative_finiteness.tex	displaymath
75	chapters/frame/heisenberg_frame.tex	displaymath
75	chapters/theory/higher_genus_complementarity.tex	claimlike
74	chapters/examples/kac_moody.tex	claimlike
72	chapters/examples/toroidal_elliptic.tex	claimlike
72	chapters/theory/configuration_spaces.tex	claimlike
71	chapters/theory/chiral_hochschild_koszul.tex	claimlike





thinking
**Analyzing report generation**

I see that there are many file kinds, maybe around 250 groups. It seems manageable if combined into a single file, but I’ll need to do some manual verification for classification. Perhaps I could script this and sample some files. I think it would be efficient to generate an exhaustive markdown report automatically. I need to check cross-references for precise counts and adjust classifications for certain labels. I’m wondering if some objects are still necessary, especially when they might just be placeholders. Reading the context will be essential for accuracy.
thinking
**Enhancing automated classification**

I see that automated classification uses actual lines, so I could include context snippets in the report for better grounding. It seems I should only claim that the label is attached to a claim-like environment. If a statement remains, I’ll just remove the label, which seems precise. If a claim is a placeholder or duplicate, that needs separate review. For phantom stubs, I can say the object should be removed. I’ll also need to read contexts for better understanding and ensure I'm basing the report on solid evidence, like label occurrences in theorems. Plus, I’ll determine severity categories.
thinking
**Evaluating assignment categories**

I’m considering how to assign severity categories for various groups in `main.tex`. I could use `[HIGH]` for phantom-stub groups, which include dead compatibility anchors or migrated chapter stubs in the active root file. For labels attached to different environments like theorems or claims, `[MEDIUM]` might fit because they can expand the claim surface and increase risk. I think `[LOW]` could work for sectioning and other anchors. I'm also pondering if there's any `[CRITICAL]` level — maybe there aren’t any claim-like items in the `main.tex` stub.
thinking
**Considering report formatting**

I’m thinking about whether I can use multiline within each bullet point if it’s a report file. It seems like I can format bullet points and list labels after a colon. I might need to maintain a flat list, which is manageable. I’m also considering creating a report in /tmp, including a summary table with counts and maybe the top 100 items. It’s important to decide if I should include duplicate labels in the main file, so I’ll cross-reference. If both labels are dead and have no references, they could be listed separately.
thinking
**Verifying reference extraction**

I need to check if the reference extraction for active file names is catching all instances of `\Cref`, `\autoref`, etc., in the current repository. My previous search focused only on `\ref`, `\eqref`, and `hyperref`, but I wonder if there might be `\cref` in cross volumes that need inclusion. I might also need to compute counts for checked files and labels, potentially summarizing with details like the number of files, labels, and dead references. Let’s get to it!
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my (%refs,%defs,%groups); my "'$def_count=0; my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref|eqref|cref|Cref|pageref)\\s*\\{(["'^}]+)'"\\}/g) { for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; } }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
for my $file (@def_files) {
  $files{$file}=1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1; $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = "other";
      if ($lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = "phantom-stub"; }
      elsif ($ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = "sectioning"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = "claimlike"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = "displaymath"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = "float"; }
      elsif ($ctx =~ /'"\\\\item\\b/s) { "'$kind = "item"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = "list"; }
      $defs{$label}++;
      $groups{"$file'"\\t"'$kind"}++;
    }
  }
}
my $dead_count = 0; $dead_count += $_ for values %groups;
my $group_count = scalar keys %groups;
my $file_count = scalar keys %files;
print "files=$file_count'"\\nlabels="'$def_count'"\\ndead="'$dead_count'"\\ngroups="'$group_count'"\\n\";
'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
files=114
labels=12786
dead=7737
groups=401



thinking
**Evaluating label removal**

I'm thinking about how to classify labels attached to prose and macros. It seems we should focus on whether the labeled object is still needed. If not, I should flag it for removal, and it looks like I can delete the `\label{...}` tokens directly. This approach is precise, although I need to verify some clusters manually, especially in files like `main.tex` and the introduction, while considering the overall context to avoid false positives from comments or macros.
thinking
**Checking label usage**

I need to see if any label names appear in `\input`, but it seems they don't. Next, I should check if labels are used in `\nameref` or `\autoref`, but the search returned nothing. That's fine. I want to identify labels defined multiple times: if a label is duplicated and unreferenced, I’ll list both; if it's referenced, I won't. Also, unreferenced duplicates need to be removed. I might create a TSV or markdown file for counts, potentially generating around 401 bullet points.
thinking
**Designing the report markdown**

I'm working on the report for the Dead Label Audit. I need to scan `main.tex`, as well as chapter and appendix files, looking for instances of `\label{}` to identify dead labels—those with no incoming references. So far, I've checked 114 files, identified 12,786 labels, and found 7,737 dead labels. I'll need to categorize the findings into high and medium priority sections, detailing specific problems and proposed fixes for removing those dead labels effectively.
codex
The grouped report is nearly ready. I’m spot-checking the nontrivial classes now: dead `main.tex` migration anchors, dead claim labels on actual theorem surfaces, and a few low-severity section/equation clusters to make sure the automatic kinding matches the source.
exec
/bin/zsh -lc "sed -n '2560,2650p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1550,1668p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,620p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3028,3052p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
which the categorical $\exp/\log$ correspondence
(Remark~\ref{rem:nilpotence-periodicity}) holds at all genera:
bar and cobar are mutually inverse on the Koszul locus,
and curvature is controlled by a universal scalar~$\kappa(\cA)$.
All four main theorems hold for modular Koszul algebras.
Definition~\ref{def:modular-koszul-homotopy} gives the homotopy-native
version; Definition~\ref{def:modular-koszul-chiral} gives the concrete
dg model.

\begin{definition}[Modular Koszul object: homotopy form]\label{def:modular-koszul-homotopy}
\index{modular Koszul chiral algebra!homotopy form}
Let $X$ be a smooth projective curve over~$\mathbb{C}$.
A \emph{modular Koszul object} on~$X$ is an augmented factorization algebra
$\cA \in \operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))$
equipped with:
\begin{enumerate}[label=\textup{(D\arabic*$_\infty$)}]
\item\label{D:bar-htpy}
A bar object
$\mathbf{B}_X(\cA) \in \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$
in the homotopy category of factorization coalgebras.
 succeeded in 52ms:
\begin{enumerate}
\item \textbf{Quadratic.} $\dzero^2 = 0$;
 Theorems~A--D hold without qualification.
 Heisenberg, free fermions, lattice VOAs.
\item \textbf{Curved-central.}
 $\dfib^{\,2} = \kappa \cdot \omega_g$; $\Dg{g}^{\,2} = 0$.
 $\widehat{\mathfrak{g}}_k$ at non-critical level, Virasoro
 with $c \neq 0$.
\item \textbf{Filtered-complete.} Complete filtration with
 $\operatorname{gr}^F \cA$ quadratic Koszul.
 $\mathcal{W}$-algebras via DS reduction, deformation
 quantizations.
\item \textbf{Programmatic.} Stratum~II
 (Remark~\ref{rem:two-strata}); stated as conjectures.
 Derived DK, $\mathbb{E}_n$ for $n \geq 2$.
\end{enumerate}
The four regimes correspond to increasing monodromy of the
categorical logarithm: single-valued, scalar curvature, filtered
convergence, full structure.
\end{convention}
 succeeded in 52ms:
% genus_complete) that are referenced from annals-included chapters.
% Without these stubs the annals PDF shows "??" at every cross-reference.
% In archive mode the real labels take precedence (these are skipped).
% ======================================================================
\ifannalsedition
 % --- High-frequency labels from archive-only chapters ---
 \phantomsection\label{thm:general-hs-sewing}% % genus_complete.tex
 \phantomsection\label{subsec:hs-sewing}% % genus_complete.tex
 \phantomsection\label{def:hs-sewing}% % genus_complete.tex
 \phantomsection\label{cor:hs-sewing-standard-landscape}% % genus_complete.tex
 \phantomsection\label{thm:ds-bar-gf-discriminant}% % landscape_census.tex
 \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
 % thm:family-index now defined in guide_to_main_results.tex
 \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
 % --- 18 additional phantom stubs (2026-03-29 audit) ---
 \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
 \phantomsection\label{thm:heisenberg-one-particle-sewing}% % genus_complete.tex (8 refs)
 \phantomsection\label{thm:resonance-filtered-bar-cobar}% % nilpotent_completion.tex (3 refs)
 \phantomsection\label{thm:frontier-protected-bulk-antiinvolution}% % frontier_modular_holography_platonic.tex
 \phantomsection\label{thm:stabilized-completion-positive}% % nilpotent_completion.tex
 succeeded in 52ms:
\subsection{Bifunctor obstruction}
\label{subsec:concordance-bifunctor-obstruction}
\index{Robert-Nicoud--Wierstra!bifunctor obstruction}
\index{Koszul property!bifunctor obstruction}

The RNW no-bifunctor obstruction \cite{RNW19}
(\S\ref{sec:concordance-three-pillars}, identification
theorem~7) is structural: $\operatorname{hom}_\alpha(
\mathcal{C},\mathcal{A})$ extends to $\infty$-morphisms in
either slot separately but not both. Koszulness does not kill
it; Koszulness makes it irrelevant by factoring all
constructions one slot at a time
(Theorem~\ref{thm:quillen-equivalence-chiral}). This is why
the MC3 strategy
(Theorem~\ref{thm:mc3-type-a-resolution}) succeeds.
\label{rem:concordance-bifunctor-koszul}


%% ------------------------------------------------------------------
\subsection{Computational diagnostics}

thinking
**Exploring LaTeX labels**

I think I should note that there are 7,737 dead labels across the active Volume I build, grouped into 401 findings. Hmm, I wonder if some labels are referenced only by `\ref*`. I might need to search for macros like `\ref*{`. LaTeX uses `\ref*` with hyperref, and it seems my regex misses `\ref*{}`. I’ll definitely need to follow up with a search to address this!
exec
/bin/zsh -lc "rg -n --no-heading '\\\\labelcref\\s*\\{|\\\\namecref\\s*\\{|\\\\lcnamecref\\s*\\{|\\\\cpageref\\s*\\{' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -o --no-filename '\\\\(?:ref|eqref|cref|Cref|pageref)\\*\\s*\\{' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | sed 's/[[:space:]]*{"'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
 625 \ref*
   5 \eqref*

thinking
**Correcting references**

I realize I need to include starred references, which is a great catch! I should check if the dead count decreases. I’ll need to re-run with `\ref*` and `\eqref*`. Are there any other starred references I could use, like `\cref*`? I think using `*` in my search pattern could help me find all of them. So, I'll get started on searching for unique patterns!
codex
There are starred cross-reference macros in the corpus. I’m rerunning the dead-label computation with `\ref*` and `\eqref*` included so the final list does not overreport.
exec
/bin/zsh -lc "rg -o --no-filename '\\\\[A-Za-z@]*ref\\*?\\s*\\{' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | sed 's/[[:space:]]*{"'$//'"' | sort | uniq -c | sort -nr" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
24615 \ref
3214 \eqref
 625 \ref*
  22 \cref
   5 \eqref*
   2 \BDref
   1 \pageref

thinking
**Recomputing references and counts**

I need to include certain references, like ref* and eqref*, but maybe not cref*. That's great! I'll have to recompute the counts and groups based on item priority. Maybe I should consider BDref without labeling it. It seems like a good idea! I also want to search for `\autoref` to see if I need it or not. Lastly, I feel I might slightly lower the dead count as I recalculate.
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my (%refs,%groups); my "'$def_count=0; my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
for my $file (@def_files) {
  $files{$file}=1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1; $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = "other";
      if ($lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = "phantom-stub"; }
      elsif ($lines[$i] =~ /'"\\\\item\\s*\\\\label/) { "'$kind = "item"; }
      elsif ($ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = "sectioning"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = "displaymath"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = "float"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = "claimlike"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = "list"; }
      $groups{"$file'"\\t"'$kind"}++;
    }
  }
}
my $dead_count = 0; $dead_count += $_ for values %groups;
print "files=".(scalar keys %files)."'"\\nlabels="'$def_count'"\\ndead="'$dead_count'"\\ngroups=\".(scalar keys %groups).\"\\n\";
'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
files=114
labels=12786
dead=7729
groups=401

thinking
**Evaluating report generation**

I'm thinking about the project and realizing I might need to star more macros. I'm not finding `\Cref*`, which is a bit tricky. It might make sense to use `\eqref` with line breaks since my file regex will handle that well. I also need to generate a grouped markdown report, which should include precise lists and possibly fix text per group. Using Perl might help me produce that efficiently. Additionally, I want to compute severity counts based on classifications like high, medium, and low.
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my (%refs,%sev_labels,%sev_groups);
for my "'$file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!"; local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) { for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; } }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
for my $file (@def_files) {
  open my $fh, q{<}, $file or die "$file: $!"; my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label=$1; next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = "other";
      if ($lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = "phantom-stub"; }
      elsif ($lines[$i] =~ /'"\\\\item\\s*\\\\label/) { "'$kind = "item"; }
      elsif ($ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = "sectioning"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = "displaymath"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = "float"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = "claimlike"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = "list"; }
      my $sev = $kind eq q{phantom-stub} ? q{HIGH} : $kind eq q{claimlike} ? q{MEDIUM} : q{LOW};
      $sev_labels{$sev}++;
      $sev_groups{$sev}{"$file'"\\t"'$kind"}++;
    }
  }
}
for my $sev (qw(HIGH MEDIUM LOW)) {
  my $groups = $sev_groups{$sev} ? scalar keys %{$sev_groups{$sev}} : 0;
  my $labels = $sev_labels{$sev} // 0;
  print "$sev groups=$groups labels=$labels'"\\n\";
}
'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
HIGH groups=2 labels=37
MEDIUM groups=104 labels=3620
LOW groups=295 labels=4072

thinking
**Considering file groups**

I'm thinking about these two high groups—there's the main.tex and possibly another phantom-stub in the file. I need to figure out what the second group is. This is a bit confusing, so I’m just trying to clarify. I'll look for details about the groups and see what I can find. Connecting the dots here might lead to a better understanding of the structure. Let’s see what I uncover!
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my %refs;
for my "'$file (@ref_files) { open my $fh, q{<}, $file or die "$file: $!"; local $/; my $text = <$fh>; close $fh; while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) { for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; } } while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; } }
my %groups;
for my $file (@def_files) { open my $fh, q{<}, $file or die "$file: $!"; my @lines = <$fh>; close $fh; for (my $i=0; $i<=$#lines; $i++) { while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) { my "'$label=$1; next if $refs{$label}; if ($lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { push @{"'$groups{$file}}, "$label:$i"; } } } }
for my $file (sort keys %groups) { print "$file'"\\t\".(scalar @{"'$groups{$file}})."'"\\n\"; }
'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/introduction.tex	2
main.tex	35
exec
/bin/zsh -lc "rg -n '\\\\phantomsection\\\\label\\{' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2494:\phantomsection\label{def:modular-homotopy-theory-intro}%
2495:\phantomsection\label{eq:all-degree-master-eq-intro}%
2496:\phantomsection\label{eq:arnold-seed}%
2497:\phantomsection\label{eq:bar-graded-object-intro}%
2498:\phantomsection\label{eq:the-seed}%
2499:\phantomsection\label{eq:universal-MC}%
2500:\phantomsection\label{prop:modular-homotopy-classification}%
2501:\phantomsection\label{prop:shadow-massey-identification}%
2502:\phantomsection\label{rem:categorical-logarithm-paradigm}%
2503:\phantomsection\label{sec:flat-connection-intro}%
2504:\phantomsection\label{sec:modular-char-spectral-disc-intro}%
2505:\phantomsection\label{sec:primitive-kernel-intro}%
2506:\phantomsection\label{sec:the-seed}%
2507:\phantomsection\label{subsec:shadow-postnikov-tower-intro}%
2508:\phantomsection\label{thm:modular-koszul-duality-main}%
exec
/bin/zsh -lc "sed -n '2488,2512p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

% ================================================================
% Stub labels for external cross-references from body chapters.
% These labels were defined in material that has been relocated
% from this introduction to the relevant body chapters.
% ================================================================
\phantomsection\label{def:modular-homotopy-theory-intro}%
\phantomsection\label{eq:all-degree-master-eq-intro}%
\phantomsection\label{eq:arnold-seed}%
\phantomsection\label{eq:bar-graded-object-intro}%
\phantomsection\label{eq:the-seed}%
\phantomsection\label{eq:universal-MC}%
\phantomsection\label{prop:modular-homotopy-classification}%
\phantomsection\label{prop:shadow-massey-identification}%
\phantomsection\label{rem:categorical-logarithm-paradigm}%
\phantomsection\label{sec:flat-connection-intro}%
\phantomsection\label{sec:modular-char-spectral-disc-intro}%
\phantomsection\label{sec:primitive-kernel-intro}%
\phantomsection\label{sec:the-seed}%
\phantomsection\label{subsec:shadow-postnikov-tower-intro}%





thinking
**Analyzing classification needs**

I need to determine which two items are dead. There's a potential issue with the stubs count in main.tex, which lists 35 instead of 41. I should inspect the claim-like group for `chapters/theory/higher_genus_modular_koszul.tex`, as the automated classification might require some adjustments. I could generate a report file using a script, possibly in Perl, although Python might be easier. I want to carefully design a script that sorts by severity and organizes the output properly.
thinking
**Structuring stub issues**

I'm considering how to separate main.tex and the introduction for high phantom stubs. It might help to subdivide by file and type, while also keeping track of counts. For instance, I could list issues like this:

- [HIGH] main.tex:1561 — PROBLEM: dead `\phantomsection` stubs lacking incoming references. FIX: delete these lines entirely.

For the introduction, I could note:
- [HIGH] chapters/theory/introduction.tex:2496 — PROBLEM: dead relocation stubs with no incoming refs. FIX: also delete those lines.

I need to ensure I identify actual dead labels and formulate a clear fix for medium claim-like groups as well.
thinking
**Considering user satisfaction**

I'm wondering if this will truly satisfy the user. Should I suggest deleting labels or adding references instead? It's possible that the exact fix should be to delete the labels since they are considered dead. I think focusing on removing what’s unnecessary might streamline things for the user. I want to clarify what the best approach is to ensure they get the resolution they need. Let me refine that thought and explore the options further!
thinking
**Refining object categories**

I’m thinking about how to refine object categories further. For instance, with raw-label-lines, I could consider removing those that only consist of `\label{...}`. Inline labels might be computed and just listed as “delete the listed `\label{...}` commands.” 

I'm also pondering file-kind groups for labels, which could be sizable, but compressing labels might help. Perhaps I could even create clickable links for files within the repository, so users can navigate more easily!
thinking
**Considering report generation**

I think generating 401 bullets with links might be a bit complex. In the final answer, I could just link to the report file instead. It might be useful to use a markdown file in the /tmp directory, and it could also be helpful to generate TSV as well. 

Maybe I could do both the report and raw CSV to cover all bases. I’ll plan to use Perl for this process since it’s versatile!
exec
/bin/zsh -lc "perl -e '
use strict; use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my (%refs,%groups); my "'$def_count=0; my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
for my $file (@def_files) {
  $files{$file}=1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1; $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = "other";
      if ($lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = "phantom-stub"; }
      elsif ($lines[$i] =~ /'"\\\\item\\s*\\\\label/) { "'$kind = "item"; }
      elsif ($ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = "sectioning"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = "displaymath"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = "float"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = "claimlike"; }
      elsif ($ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = "list"; }
      my $sev = $kind eq q{phantom-stub} ? q{HIGH} : $kind eq q{claimlike} ? q{MEDIUM} : q{LOW};
      my $key = join("'"\\t\", "'$sev, $file, $kind);
      push @{$groups{$key}}, { label => $label, line => $i+1 };
    }
  }
}
my $dead_count = 0; $dead_count += scalar(@$_) for values %groups;
my $group_count = scalar keys %groups;
my $report = q{/tmp/vol1_dead_label_audit.md};
open my $out, q{>}, $report or die "$report: $!";
print {$out} "# Vol I Dead Label Audit'"\\n\\n\";
print {"'$out} "Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `'"\\\\ref"'`, `'"\\\\ref*"'`, `'"\\\\eqref"'`, `'"\\\\eqref*"'`, `'"\\\\cref"'`, `'"\\\\Cref"'`, `'"\\\\pageref"'`, and `'"\\\\hyperref[...]"'`.'"\\n\\n\";
print {"'$out} "Checked: ".(scalar keys %files)." files | Labels: $def_count | Dead labels: $dead_count | Grouped findings: $group_count'"\\n\\n\";
for my "'$sev (qw(HIGH MEDIUM LOW)) {
  print {$out} "## $sev'"\\n\";
  my @keys = grep { /"'^$sev'"\\t/ } keys %groups;
  @keys = sort {
    my ("'$sa,$fa,$ka)=split /'"\\t/,"'$a,3; my ($sb,$fb,$kb)=split /'"\\t/,"'$b,3;
    my $mina = (sort { $a <=> $b } map { $_->{line} } @{$groups{$a}})[0];
    my $minb = (sort { $a <=> $b } map { $_->{line} } @{$groups{$b}})[0];
    $fa cmp $fb || $mina <=> $minb || $ka cmp $kb;
  } @keys;
  for my $key (@keys) {
    my ($sev2,$file,$kind) = split /'"\\t/,"'$key,3;
    my @items = sort { $a->{line} <=> $b->{line} || $a->{label} cmp $b->{label} } @{$groups{$key}};
    my $first_line = $items[0]{line};
    my @tokens = map { sprintf('"'"'`%s` (%d)'"', "'$_->{label}, $_->{line}) } @items;
    my $labels = join('"', ', @tokens);
    my ("'$problem,$fix);
    if ($kind eq q{phantom-stub}) {
      $problem = "dead `'"\\\\phantomsection\\\\label{...}"'` compatibility stubs with zero incoming refs across Vol I/II/III: $labels.";
      $fix = "Delete the entire `'"\\\\phantomsection\\\\label{...}"'` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.";
    } elsif ($kind eq q{claimlike}) {
      $problem = "dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: $labels.";
      $fix = "Keep the surrounding mathematical content, but delete the listed `'"\\\\label{...}"'` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.";
    } elsif ($kind eq q{sectioning}) {
      $problem = "dead section/chapter/part labels with zero incoming refs: $labels.";
      $fix = "Keep the sectioning structure, but delete the listed `'"\\\\label{...}"'` commands. Reintroduce a label only when an actual cross-reference exists.";
    } elsif ($kind eq q{displaymath}) {
      $problem = "dead display-math labels with zero incoming refs: $labels.";
      $fix = "Keep the displayed formulae, but delete the listed `'"\\\\label{...}"'` commands. If a formula needs to be cited later, add the label back when the citation is added.";
    } elsif ($kind eq q{float}) {
      $problem = "dead table/figure labels with zero incoming refs: $labels.";
      $fix = "Keep the float content, but delete the listed `'"\\\\label{...}"'` commands unless you add a real reference to the float.";
    } elsif ($kind eq q{item}) {
      $problem = "dead enumerated-item labels with zero incoming refs: $labels.";
      $fix = "Keep the list items, but delete the listed `'"\\\\label{...}"'` commands. If an item must be cited, add the reference at the call site and restore only that label.";
    } elsif ($kind eq q{list}) {
      $problem = "dead list-level labels with zero incoming refs: $labels.";
      $fix = "Keep the list structure, but delete the listed `'"\\\\label{...}"'` commands.";
    } else {
      $problem = "dead labels with zero incoming refs: $labels.";
      $fix = "Delete the listed `'"\\\\label{...}"'` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.";
    }
    print {$out} "- [$sev2] $file:$first_line — PROBLEM: $problem FIX: $fix'"\\n\";
  }
  print {"'$out} "'"\\n\";
}
print {"'$out} "## Summary'"\\nChecked: \".(scalar keys %files).\" | Findings: "'$group_count | Verdict: FAIL'"\\n\";
close "'$out;
print "$report'"\\n\";
'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
zsh:fg:1: no job control in this shell.
zsh:1: no matches found: (%d), $_->{label}, $_->{line}) } @items;\n    my $labels = join(,

thinking
**Evaluating shell quoting**

I'm running into a shell quoting issue related to using braces and zsh glob expansion. I wonder if using `cat <<'PERL'` might make things easier. I could utilize `exec_command` with the command formatted as a heredoc. I’m thinking about trying `perl <<'PERL'...PERL`. It seems like a practical approach to solve this problem, so let’s go ahead and implement that!
exec
/bin/zsh -lc "perl <<'PERL'
use strict;
use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my (%refs,%groups);
my "'$def_count = 0;
my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/;
  my $text = <$fh>;
  close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) {
      $refs{$label}++ if length $label;
    }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) {
    "'$refs{$1}++ if length $1;
  }
}
for my $file (@def_files) {
  $files{$file} = 1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>;
  close $fh;
  for (my $i = 0; $i <= $#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1;
      $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) {
        "'$kind = '"'phantom-stub';
      } elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) {
        "'$kind = '"'item';
      } elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) {
        "'$kind = '"'sectioning';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) {
        $kind = '"'displaymath';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) {
        "'$kind = '"'float';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) {
        "'$kind = '"'claimlike';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) {
        "'$kind = '"'list';
      }
      my "'$sev = $kind eq '"'phantom-stub' ? 'HIGH' : "'$kind eq '"'claimlike' ? 'MEDIUM' : 'LOW';
      my "'$key = join("'"\\t\", "'$sev, $file, $kind);
      push @{$groups{$key}}, { label => $label, line => $i + 1 };
    }
  }
}
my $dead_count = 0;
$dead_count += scalar(@$_) for values %groups;
my $group_count = scalar keys %groups;
my $report = '"'/tmp/vol1_dead_label_audit.md';
open my "'$out, q{>}, $report or die "$report: $!";
print {$out} "# Vol I Dead Label Audit'"\\n\\n\";
print {"'$out} "Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `'"\\\\ref"'`, `'"\\\\ref*"'`, `'"\\\\eqref"'`, `'"\\\\eqref*"'`, `'"\\\\cref"'`, `'"\\\\Cref"'`, `'"\\\\pageref"'`, and `'"\\\\hyperref[...]"'`.'"\\n\\n\";
print {"'$out} "Checked: ".(scalar keys %files)." files | Labels: $def_count | Dead labels: $dead_count | Grouped findings: $group_count'"\\n\\n\";
for my "'$sev (qw(HIGH MEDIUM LOW)) {
  print {$out} "## $sev'"\\n\";
  my @keys = grep { /"'^$sev'"\\t/ } keys %groups;
  @keys = sort {
    my ("'$sa,$fa,$ka) = split /'"\\t/, "'$a, 3;
    my ($sb,$fb,$kb) = split /'"\\t/, "'$b, 3;
    my ($mina) = sort { $a <=> $b } map { $_->{line} } @{$groups{$a}};
    my ($minb) = sort { $a <=> $b } map { $_->{line} } @{$groups{$b}};
    $fa cmp $fb || $mina <=> $minb || $ka cmp $kb;
  } @keys;
  for my $key (@keys) {
    my ($sev2, $file, $kind) = split /'"\\t/, "'$key, 3;
    my @items = sort { $a->{line} <=> $b->{line} || $a->{label} cmp $b->{label} } @{$groups{$key}};
    my $first_line = $items[0]{line};
    my @tokens = map { sprintf('"'"'`%s` (%d)'"', "'$_->{label}, $_->{line}) } @items;
    my $labels = join('"', ', @tokens);
    my ("'$problem, $fix);
    if ($kind eq '"'phantom-stub') {
      "'$problem = "dead `'"\\\\phantomsection\\\\label{...}"'` compatibility stubs with zero incoming refs across Vol I/II/III: $labels.";
      $fix = "Delete the entire `'"\\\\phantomsection\\\\label{...}"'` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.";
    } elsif ($kind eq '"'claimlike') {
      "'$problem = "dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: $labels.";
      $fix = "Keep the surrounding mathematical content, but delete the listed `'"\\\\label{...}"'` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.";
    } elsif ($kind eq '"'sectioning') {
      "'$problem = "dead section/chapter/part labels with zero incoming refs: $labels.";
      $fix = "Keep the sectioning structure, but delete the listed `'"\\\\label{...}"'` commands. Reintroduce a label only when an actual cross-reference exists.";
    } elsif ($kind eq '"'displaymath') {
      "'$problem = "dead display-math labels with zero incoming refs: $labels.";
      $fix = "Keep the displayed formulae, but delete the listed `'"\\\\label{...}"'` commands. If a formula needs to be cited later, add the label back when the citation is added.";
    } elsif ($kind eq '"'float') {
      "'$problem = "dead table/figure labels with zero incoming refs: $labels.";
      $fix = "Keep the float content, but delete the listed `'"\\\\label{...}"'` commands unless you add a real reference to the float.";
    } elsif ($kind eq '"'item') {
      "'$problem = "dead enumerated-item labels with zero incoming refs: $labels.";
      $fix = "Keep the list items, but delete the listed `'"\\\\label{...}"'` commands. If an item must be cited, add the reference at the call site and restore only that label.";
    } elsif ($kind eq '"'list') {
      "'$problem = "dead list-level labels with zero incoming refs: $labels.";
      $fix = "Keep the list structure, but delete the listed `'"\\\\label{...}"'` commands.";
    } else {
      $problem = "dead labels with zero incoming refs: $labels.";
      $fix = "Delete the listed `'"\\\\label{...}"'` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.";
    }
    print {$out} "- [$sev2] $file:$first_line — PROBLEM: $problem FIX: $fix'"\\n\";
  }
  print {"'$out} "'"\\n\";
}
print {"'$out} "## Summary'"\\nChecked: \".(scalar keys %files).\" | Findings: "'$group_count | Verdict: FAIL'"\\n\";
close "'$out;
print "$report'"\\n\";
PERL" in /Users/raeez/chiral-bar-cobar succeeded in 83ms:
/tmp/vol1_dead_label_audit.md

thinking
**Inspecting report formatting**

I need to check the top of the report and see if there are any formatting issues that stand out. It’s really important to have everything looking neat and organized, especially if anyone else is going to look at it. I wonder if there are specific elements that are frequently overlooked. I’ll take my time to make sure I catch anything that seems off — I want to get this right to help improve clarity!
exec
/bin/zsh -lc "sed -n '1,40p' /tmp/vol1_dead_label_audit.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 40

# Vol I Dead Label Audit

Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\Cref`, `\pageref`, and `\hyperref[...]`.

Checked: 114 files | Labels: 12786 | Dead labels: 7729 | Grouped findings: 401

## HIGH
- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.
- [HIGH] main.tex:1597 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `subsec:frontier-protected-holographic-transform` (1597), `chap:dg-shifted-factorization` (1617), `ch:ym-higher-body-couplings` (1622), `app:typeA-baxter-rees-theta` (1624), `subsec:cy-research-programmes` (1630), `sec:concordance-e1-modular-theory` (1655), `sec:concordance-structural-upgrades` (1656), `subsec:concordance-koszulness-meta-theorem` (1659), `princ:shadow-depth-escalator` (1660), `princ:physics-is-homotopy-type` (1662), `subsec:concordance-shadow-depth-classes` (1663), `subsec:concordance-further-characterizations` (1664), `subsec:concordance-bifunctor-obstruction` (1665), `subsec:concordance-koszulness-xref` (1666), `subsec:concordance-computational-diagnostics` (1667), `subsec:analytic-completion-programme-editorial` (1670), `sec:concordance-arithmetic-sewing` (1671), `thm:higher-genus-diff` (1721), `def:euler-koszul-defect` (1739), `def:surface-moment-matrix` (1750), `def:w-algebra-cft` (1752), `constr:prime-side-li` (1753), `sec:genus-all-master` (1775), `subsec:sewing-gram-matrix` (1781), `def:infty-operad` (1817), `def:swiss-cheese-W-resolution` (1835), `thm:branch-bv` (1836), `rem:affine-half-space-bv` (1840), `conj:relative-quartic-computation` (1847), `def:relative-holographic-deformation` (1848), `constr:vol2-oc-mc-element` (1857), `thm:vol2-oc-mc-equation` (1858), `conj:globalization` (1859), `conj:boundary-line-generation` (1860), `conj:khan-zeng-comparison` (1861). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.

## MEDIUM
- [MEDIUM] chapters/connections/arithmetic_shadows.tex:227 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:lattice-specificity` (227), `prop:divisor-sum-decomposition` (311), `prop:sewing-trace-formula` (349), `thm:narain-universality` (444), `rem:discrimination-hierarchy` (756), `prop:shadow-arithmetic-factorization` (779), `rem:genus2-theta-niemeier` (832), `rem:mc-complete-niemeier` (882), `rem:shadow-spectral-CG` (984), `prop:hecke-all-orders` (1021), `prop:period-shadow-dictionary` (1072), `rem:depth-non-unimodular` (1137), `comp:period-shadow-vz` (1155), `comp:period-shadow-ve8` (1173), `comp:period-shadow-leech` (1195), `comp:period-shadow-rank24-comparison` (1247), `comp:period-shadow-rank2` (1266), `thm:spectral-decomposition-principle` (1290), `rem:homotopy-becomes-arithmetic` (1330), `def:cusp-growth-rate` (1366), `prop:growth-rate-dictionary` (1377), `thm:bg-vir-coincidence` (1403), `cor:rigorous-infinite-depth` (1546), `prop:bg-primary-counting` (1580), `rem:ising-arithmetic-paradox` (1651), `rem:non-unimodular` (1719), `def:arithmetic-depth-filtration` (1757), `rem:depth-decomposition-universality` (1880), `rem:vnatural-class-m` (1938), `thm:shadow-sullivan` (1973), `rem:shadow-metric-gram` (2103), `rem:stieltjes-discriminant` (2197), `rem:transcendence-asymmetry` (2329), `rem:mc-motivic-identity` (2346), `rem:shadow-tower-dm-z` (2386), `prop:resurgent-orthogonality` (2491), `prop:gevrey-zero-degree` (2564), `rem:resurgent-anomaly-cancellation` (2599), `prop:padic-convergence` (2622), `rem:kummer-kubota-leopoldt` (2648), `rem:ferrero-washington-failure` (2693), `thm:drinfeld-associator-bar-transport` (2833), `rem:zagier-dimension-shadow` (2904), `rem:shadow-mzv-observational` (2927), `thm:partition-modular-classification` (3018), `rem:l-functions-koszul-pairs` (3121), `prop:hecke-eigenvalue-extraction` (3152), `prop:moment-matrix-negativity` (3242), `rem:shadow-p-adic-locality` (3264), `prop:calogero-shadow-dictionary` (3298), `rem:tau-shadow-kw` (3379), `rem:shadow-eisenstein-numerical-check` (3631), `rem:langlands-gl2-eisenstein` (3694), `rem:shadow-s1-quantum-volume-evidence` (3749), `rem:cs-bernoulli` (3889), `thm:nonabelian-hodge` (3920), `rem:depth-hodge` (4095), `rem:nahc-upgrade` (4140), `rem:ode-im-shadow-identification` (4273), `rem:wn-galois-evidence` (4590), `rem:eisenstein-deformation` (4611), `rem:bps-self-referential` (4699), `thm:general-bps` (4719), `rem:dt-pt-wall-crossing` (4760), `ex:heisenberg-intertwining` (4910), `rem:specialised-shadow-field-invariants` (5390), `prop:koszul-field-criterion` (5441), `ex:koszul-field-1-25` (5500), `ex:koszul-field-13` (5507), `prop:two-fixed-points` (5516), `rem:koszul-epstein-constraints` (5638), `prop:heisenberg-koszul-epstein` (5683), `comp:virasoro-c1-koszul-epstein` (5735), `rem:davenport-heilbronn-koszul-epstein` (5799), `rem:virasoro-character-vector` (5898), `rem:vvmf-rankin-selberg` (5899), `def:potential-side-transform` (5934), `def:gram-side-transform` (5952), `def:genuine-residue-moment-matrix` (6150), `def:compatibility-ratios` (6174), `rem:li-numerical-values-arith` (6497), `rem:sewing-lift-two-line` (6589), `rem:euler-product-from-independent-sum` (6629), `rem:propagator-variance-euler` (6711), `rem:virasoro-first-miura-defect` (6838), `def:residue-divisor` (6990), `rem:clutching-defect-meaning` (7032), `rem:clutching-vs-quartic-closure` (7087), `def:local-compatibility-discrepancy` (7114), `def:beilinson-functional` (7139), `rem:beilinson-closure-hierarchy` (7168), `rem:zeta-proxy-failure` (7204), `rem:decisive-computation` (7264), `rem:quartic-meeting-point` (7334), `rem:arithmetic-end-state` (7367), `rem:mc-rigidity-diagnosis` (7704), `rem:operadic-transfer` (7729), `def:shadow-bracket-form` (7758), `thm:petersson-identification` (7778), `rem:route-c-finite-atoms` (7936), `conj:modular-spectral-rigidity-sharp` (7952), `prop:lattice-ramanujan-rigidity` (7999), `ex:leech-rigidity` (8023), `rem:naive-prime-locality-obstruction` (8259), `prop:shadow-arithmetic-trichotomy` (8292), `rem:mgf-relation` (8613), `rem:universal-ramanujan` (8962), `rem:prime-locality-known` (9046), `prop:mc-constraint-counting` (9249), `rem:route-c-hypotheses` (9390), `rem:theta-bridge-resolution` (9631), `rem:two-chiralities` (9838), `rem:kronecker-limit` (9855), `rem:algebra-representation-gap` (9970), `rem:holomorphic-arithmetic-blindness` (10113), `rem:three-new-gaps` (10319), `rem:honest-comparison` (10362), `def:scattering-coupling` (10468), `rem:factorization-scope` (10547), `rem:hecke-defect-leading` (10769), `rem:hecke-defect-two-levels` (10908), `conj:conditional-ramanujan` (11005), `rem:langlands-interface` (11152), `def:arithmetic-packet-module` (11194), `rem:packet-reformulation` (11415), `rem:arithmetic-comparison-sharpening` (11488), `ex:packet-heisenberg` (11686), `ex:packet-rank1-lattice` (11749), `ex:packet-virasoro` (11783), `ex:packet-w3` (11857), `rem:genus2-definitive-scope` (12261), `rem:leech-all-sk` (12316), `prop:prime-locality-proved-cases` (12553), `thm:prime-locality-obstructions` (12594), `rem:route-c-success` (12702), `rem:route-c-gap` (12726), `thm:riccati-determinacy-assessment` (12796), `prop:shadow-not-selberg` (12839), `rem:shadow-riemann-independence` (12900), `rem:prime-locality-definitive` (12937). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] chapters/connections/bv_brst.tex:57 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:brst-anomaly-gkw` (57), `rem:modular-qme-bv` (103), `rem:sft-bar-identification` (155), `def:bv-data-chiral` (169), `def:bv-laplacian` (248), `rem:qme-bar-cobar` (269), `rem:genus0-amplitude-bar` (293), `rem:genus1-bv` (320), `rem:anomaly-curvature-bv` (326), `def:brst-operator` (336), `thm:brst-physical-states` (355), `conj:bar-topological-brst` (429), `rem:brst-nilpotence-periodicity` (475), `rem:bv-convergence` (611), `comp:superstring-ghost-koszul` (765), `rem:brst-bar-higher-genus` (854), `def:semi-infinite-cohomology` (874), `rem:semi-infinite-vs-brst` (900), `rem:string-brst-special-case` (1013), `rem:master-table-brst` (1117), `cor:virasoro-semi-infinite` (1169), `rem:w-semi-infinite-conditional` (1248), `def:bv-algebra-complete` (1279), `rem:bv-shifted-symplectic` (1385), `rem:heisenberg-bv-bar-scope` (1624), `rem:bv-bar-coderived-higher-genus` (1951), `rem:bv-bar-coderived-why` (1973), `comp:burns-koszul-datum` (2056), `conj:non-cy-local-surfaces` (2137), `rem:non-cy-scope` (2174), `conj:wzw-brst-bar-all-genera` (2292), `rem:wzw-brst-bar-generic-level` (2306). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] chapters/connections/casimir_divisor_core_transport.tex:350 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `thm:primary-jordan-filtration` (350), `prop:no-projector` (467), `lem:generic-separator` (588), `cor:finite-scalar-probes` (665), `rem:intrinsic-resolution` (969), `prop:transport-factors-through-common-core` (1088), `prop:sl3-w3-defect` (1203), `prop:explicit-sl3-projectors` (1244), `conj:geometric-divisor-core-lift` (1360), `conj:jordan-lift` (1400), `conj:geometric-common-core-factorization` (1416), `conj:geometric-ds-common-core` (1427). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] chapters/connections/concordance.tex:435 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:oper-langlands-concordance` (435), `rem:tau-protagonist` (449), `prop:glz-special-case` (512), `rem:concordance-rx-kx` (593), `rem:feigin-frenkel-comparison` (625), `rem:cg-comparison` (665), `def:envelope-shadow-complexity` (799), `rem:envelope-shadow-complexity-standard` (913), `rem:from-examples-to-machine` (934), `rem:envelope-shadow-frontier` (948), `rem:concordance-platonic-adjunction` (1034), `rem:envelope-execution-programme` (1047), `rem:concordance-synthesis` (1108), `rem:ms-complementary` (1163), `rem:ms-genus0-agreement` (1177), `rem:three-pillars` (1218), `rem:preprint-dependency-table` (1392), `rem:three-pillar-mc-unification` (1833), `prop:top-down-architecture` (2332), `thm:operadic-complexity-concordance` (2518), `princ:shadow-depth-escalator` (2762), `princ:physics-is-homotopy-type` (2814), `rem:transport-closure-diagnostics` (3498), `rem:pixton-from-mc` (4040), `prop:vol2-bar-cobar-bridge` (4546), `conj:vol2-hochschild-bridge` (4555), `prop:vol2-dk-ybe-bridge` (4570), `prop:vol2-w-algebra-bridge` (4578), `prop:vol2-relative-holographic-bridge` (4601), `prop:vol2-ribbon-thooft-bridge` (4622), `rem:concordance-pva-bridge` (4665), `rem:lagrangian-conj-scope` (4986), `rem:universal-MC-scope` (5283), `rem:discriminant-spectral-scope` (5758), `rem:family-index-punchline` (6142), `rem:concordance-scalar-free-energ…5369 tokens truncated…), `prop:g9-clifford-deformation` (2029), `prop:g9-trace-formula` (2104), `cor:g9-partition-trace` (2128), `rem:g9-partition-u0` (2143), `rem:g9-open-questions` (2164). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] chapters/connections/thqg_entanglement_programme.tex:101 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:thqg-two-entanglements` (101), `rem:thqg-capacity-bounds-entanglement` (214), `rem:thqg-annulus-as-partial-trace` (272), `def:thqg-qes-approximant` (306), `rem:thqg-mc-as-extremization` (356), `rem:thqg-shadow-on-replica` (462), `rem:thqg-kms-from-complementarity` (555), `rem:thqg-hqec-analogy` (626), `rem:thqg-page-transition` (742), `rem:thqg-page-constructive` (761), `conj:thqg-g11-target` (796), `conj:thqg-g12-target` (820), `conj:thqg-g13-target` (839), `conj:thqg-g14-target` (856), `conj:thqg-g15-target` (872), `conj:thqg-g16-target` (891), `rem:thqg-g11-g16-dependencies` (906), `rem:thqg-convergent-advantage` (942). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] chapters/connections/thqg_fredholm_partition_functions.tex:103 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `def:thqg-X-bergman-space` (103), `rem:thqg-X-bergman-conformal` (129), `def:thqg-X-bergman-collar` (141), `lem:thqg-X-bergman-projection` (159), `def:thqg-X-sewing-envelope-review` (177), `prop:thqg-X-sewing-filtration` (195), `rem:thqg-X-tensor-sewing` (284), `def:thqg-X-sewing-operator` (305), `rem:functional-det-fredholm-bridge` (847), `prop:polyakov-alvarez-shadow-specialization` (869), `rem:uv-finiteness-compactness` (911), `thm:thqg-X-genus-1-fredholm` (948), `rem:thqg-X-genus-1-modular` (1033), `comp:thqg-X-genus-1-series` (1051), `rem:thqg-X-trace-vs-fredholm` (1079), `thm:thqg-X-genus-2-fredholm` (1096), `comp:thqg-X-genus-2-series` (1204), `thm:thqg-X-genus-3-fredholm` (1231), `rem:thqg-X-schottky` (1331), `thm:thqg-X-general-genus-fredholm` (1351), `prop:thqg-X-free-energy-ahat` (1425), `thm:thqg-X-class-G-fredholm` (1501), `ex:thqg-X-lattice-fredholm` (1548), `rem:thqg-X-lattice-curvature-braiding` (1579), `prop:thqg-X-rank-additivity` (1594), `def:thqg-X-non-fredholm-correction` (1641), `thm:thqg-X-feynman-expansion` (1661), `prop:thqg-X-class-L-feynman` (1724), `ex:thqg-X-affine-genus-2` (1774), `prop:thqg-X-class-C-quartic` (1818), `rem:thqg-X-class-M-corrections` (1862), `prop:thqg-X-virasoro-decomposition` (1902), `rem:thqg-X-resurgent` (1950), `def:thqg-X-analytic-bar-review` (1978), `prop:thqg-X-analytic-bar-bounded` (1999), `prop:thqg-X-analytic-coproduct` (2027), `rem:thqg-X-coderived-review` (2058), `def:thqg-X-coderived-shadow-pf` (2087), `prop:thqg-X-coderived-fredholm-G` (2107), `rem:thqg-X-analytic-koszul` (2133), `rem:thqg-X-platonic-chain` (2163), `rem:thqg-X-fredholm-summary` (2268), `def:cohft-vertex-factor` (2358), `rem:operad-vertex-factors` (2460), `thm:gravitational-complementarity-genus-expansion` (2496), `prop:virasoro-F2-full` (2611), `prop:cohft-complementarity` (2662), `rem:quantum-bh-entropy` (2715), `rem:discriminant-instanton-duality` (2764). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] chapters/connections/thqg_gravitational_complexity.tex:103 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:thqg-first-four` (103), `def:thqg-gravitational-complexity` (141), `thm:thqg-complexity-controls-bulk` (174), `prop:thqg-depth-qi-invariant` (216), `thm:thqg-grav-content` (374), `thm:thqg-gaussian-termination` (431), `cor:thqg-gaussian-potential` (451), `ex:thqg-gaussian-data` (465), `thm:thqg-lie-termination` (499), `ex:thqg-lie-data` (527), `thm:thqg-contact-termination` (564), `prop:thqg-cubic-gauge` (598), `def:thqg-comp-potential` (822), `thm:thqg-virasoro-potential` (832), `ex:thqg-four-potentials` (853), `thm:thqg-genus1-hessian` (879), `cor:thqg-virasoro-genus1` (895), `rem:thqg-rho1-normalisation` (922), `thm:thqg-genus2-diagnostic` (939), `thm:thqg-obstruction-table` (1002), `thm:thqg-vanishing-mechanisms` (1076), `thm:thqg-independent-sum` (1116), `prop:thqg-depth-koszulness-independent` (1148), `prop:thqg-duality-preserves-complexity` (1186), `cor:thqg-duality-table` (1199), `def:thqg-tropical-depth` (1230), `prop:thqg-tropical-profiles` (1237), `thm:thqg-holographic-type` (1274), `prop:thqg-wn-stabilization` (1331), `thm:thqg-grav-landscape` (1360), `thm:thqg-g2-main` (1408), `prop:thqg-complexity-functor` (1456), `rem:thqg-ds-complexity` (1505), `prop:thqg-coefficient-asymptotics` (1531), `rem:thqg-singular-loci` (1573), `prop:thqg-generic-constancy` (1600), `ex:thqg-virasoro-class-jumps` (1620), `ex:thqg-affine-class-jumps` (1634), `thm:thqg-mc-euler-lagrange` (1655), `rem:thqg-four-gravity-theories` (1686), `thm:thqg-holographic-ss` (1753), `prop:thqg-collapse-criteria` (1787), `prop:thqg-e1-virasoro` (1844), `prop:thqg-collapse-L` (1891), `prop:thqg-collapse-C` (1915), `prop:thqg-curve-independence` (1960), `comp:thqg-sextic` (1988). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
exec
/bin/zsh -lc 'tail -n 5 /tmp/vol1_dead_label_audit.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^- '"\\[(HIGH|MEDIUM|LOW)\\]' /tmp/vol1_dead_label_audit.md | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
- [LOW] chapters/theory/three_invariants.tex:77 — PROBLEM: dead display-math labels with zero incoming refs: `eq:p-max-def` (77), `eq:k-max-def` (107), `eq:r-max-def` (146). FIX: Keep the displayed formulae, but delete the listed `\label{...}` commands. If a formula needs to be cited later, add the label back when the citation is added.
- [LOW] chapters/theory/three_invariants.tex:265 — PROBLEM: dead labels with zero incoming refs: `warn:ap59-three-invariants` (265). FIX: Delete the listed `\label{...}` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.

## Summary
Checked: 114 | Findings: 401 | Verdict: FAIL
 succeeded in 52ms:
Total output lines: 20

8:- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.
9:- [HIGH] main.tex:1597 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `subsec:frontier-protected-holographic-transform` (1597), `chap:dg-shifted-factorization` (1617), `ch:ym-higher-body-couplings` (1622), `app:typeA-baxter-rees-theta` (1624), `subsec:cy-research-programmes` (1630), `sec:concordance-e1-modular-theory` (1655), `sec:concordance-structural-upgrades` (1656), `subsec:concordance-koszulness-meta-theorem` (1659), `princ:shadow-depth-escalator` (1660), `princ:physics-is-homotopy-type` (1662), `subsec:concordance-shadow-depth-classes` (1663), `subsec:concordance-further-characterizations` (1664), `subsec:concordance-bifunctor-obstruction` (1665), `subsec:concordance-koszulness-xref` (1666), `subsec:concordance-computational-diagnostics` (1667), `subsec:analytic-completion-programme-editorial` (1670), `sec:concordance-arithmetic-sewing` (1671), `thm:higher-genus-diff` (1721), `def:euler-koszul-defect` (1739), `def:surface-moment-matrix` (1750), `def:w-algebra-cft` (1752), `constr:prime-side-li` (1753), `sec:genus-all-master` (1775), `subsec:sewing-gram-matrix` (1781), `def:infty-operad` (1817), `def:swiss-cheese-W-resolution` (1835), `thm:branch-bv` (1836), `rem:affine-half-space-bv` (1840), `conj:relative-quartic-computation` (1847), `def:relative-holographic-deformation` (1848), `constr:vol2-oc-mc-element` (1857), `thm:vol2-oc-mc-equation` (1858), `conj:globalization` (1859), `conj:boundary-line-generation` (1860), `conj:khan-zeng-comparison` (1861). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.
12:- [MEDIUM] chapters/connections/arithmetic_shadows.tex:227 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:lattice-specificity` (227), `prop:divisor-sum-decomposition` (311), `prop:sewing-trace-formula` (349), `thm:narain-universality` (444), `rem:discrimination-hierarchy` (756), `prop:shadow-arithmetic-factorization` (779), `rem:genus2-theta-niemeier` (832), `rem:mc-complete-niemeier` (882), `rem:shadow-spectral-CG` (984), `prop:hecke-all-orders` (1021), `prop:period-shadow-dictionary` (1072), `rem:depth-non-unimodular` (1137), `comp:period-shadow-vz` (1155), `comp:period-shadow-ve8` (1173), `comp:period-shadow-leech` (1195), `comp:period-shadow-rank24-comparison` (1247), `comp:period-shadow-rank2` (1266), `thm:spectral-decomposition-principle` (1290), `rem:homotopy-becomes-arithmetic` (1330), `def:cusp-growth-rate` (1366), `prop:growth-rate-dictionary` (1377), `thm:bg-vir-coincidence` (1403), `cor:rigorous-infinite-depth` (1546), `prop:bg-primary-counting` (1580), `rem:ising-arithmetic-paradox` (1651), `rem:non-unimodular` (1719), `def:arithmetic-depth-filtration` (1757), `rem:depth-decomposition-universality` (1880), `rem:vnatural-class-m` (1938), `thm:shadow-sullivan` (1973), `rem:shadow-metric-gram` (2103), `rem:stieltjes-discriminant` (2197), `rem:transcendence-asymmetry` (2329), `rem:mc-motivic-identity` (2346), `rem:shadow-tower-dm-z` (2386), `prop:resurgent-orthogonality` (2491), `prop:gevrey-zero-degree` (2564), `rem:resurgent-anomaly-cancellation` (2599), `prop:padic-convergence` (2622), `rem:kummer-kubota-leopoldt` (2648), `rem:ferrero-washington-failure` (2693), `thm:drinfeld-associator-bar-transport` (2833), `rem:zagier-dimension-shadow` (2904), `rem:shadow-mzv-observational` (2927), `thm:partition-modular-classification` (3018), `rem:l-functions-koszul-pairs` (3121), `prop:hecke-eigenvalue-extraction` (3152), `prop:moment-matrix-negativity` (3242), `rem:shadow-p-adic-locality` (3264), `prop:calogero-shadow-dictionary` (3298), `rem:tau-shadow-kw` (3379), `rem:shadow-eisenstein-numerical-check` (3631), `rem:langlands-gl2-eisenstein` (3694), `rem:shadow-s1-quantum-volume-evidence` (3749), `rem:cs-bernoulli` (3889), `thm:nonabelian-hodge` (3920), `rem:depth-hodge` (4095), `rem:nahc-upgrade` (4140), `rem:ode-im-shadow-identification` (4273), `rem:wn-galois-evidence` (4590), `rem:eisenstein-deformation` (4611), `rem:bps-self-referential` (4699), `thm:general-bps` (4719), `rem:dt-pt-wall-crossing` (4760), `ex:heisenberg-intertwining` (4910), `rem:specialised-shadow-field-invariants` (5390), `prop:koszul-field-criterion` (5441), `ex:koszul-field-1-25` (5500), `ex:koszul-field-13` (5507), `prop:two-fixed-points` (5516), `rem:koszul-epstein-constraints` (5638), `prop:heisenberg-koszul-epstein` (5683), `comp:virasoro-c1-koszul-epstein` (5735), `rem:davenport-heilbronn-koszul-epstein` (5799), `rem:virasoro-character-vector` (5898), `rem:vvmf-rankin-selberg` (5899), `def:potential-side-transform` (5934), `def:gram-side-transform` (5952), `def:genuine-residue-moment-matrix` (6150), `def:compatibility-ratios` (6174), `rem:li-numerical-values-arith` (6497), `rem:sewing-lift-two-line` (6589), `rem:euler-product-from-independent-sum` (6629), `rem:propagator-variance-euler` (6711), `rem:virasoro-first-miura-defect` (6838), `def:residue-divisor` (6990), `rem:clutching-defect-meaning` (7032), `rem:clutching-vs-quartic-closure` (7087), `def:local-compatibility-discrepancy` (7114), `def:beilinson-functional` (7139), `rem:beilinson-closure-hierarchy` (7168), `rem:zeta-proxy-failure` (7204), `rem:decisive-computation` (7264), `rem:quartic-meeting-point` (7334), `rem:arithmetic-end-state` (7367), `rem:mc-rigidity-diagnosis` (7704), `rem:operadic-transfer` (7729), `def:shadow-bracket-form` (7758), `thm:petersson-identification` (7778), `rem:route-c-finite-atoms` (7936), `conj:modular-spectral-rigidity-sharp` (7952), `prop:lattice-ramanujan-rigidity` (7999), `ex:leech-rigidity` (8023), `rem:naive-prime-locality-obstruction` (8259), `prop:shadow-arithmetic-trichotomy` (8292), `rem:mgf-relation` (8613), `rem:universal-ramanujan` (8962), `rem:prime-locality-known` (9046), `prop:mc-constraint-counting` (9249), `rem:route-c-hypotheses` (9390), `rem:theta-bridge-resolution` (9631), `rem:two-chiralities` (9838), `rem:kronecker-limit` (9855), `rem:algebra-representation-gap` (9970), `rem:holomorphic-arithmetic-blindness` (10113), `rem:three-new-gaps` (10319), `rem:honest-comparison` (10362), `def:scattering-coupling` (10468), `rem:factorization-scope` (10547), `rem:hecke-defect-leading` (10769), `rem:hecke-defect-two-levels` (10908), `conj:conditional-ramanujan` (11005), `rem:langlands-interface` (11152), `def:arithmetic-packet-module` (11194), `rem:packet-reformulation` (11415), `rem:arithmetic-comparison-sharpening` (11488), `ex:packet-heisenberg` (11686), `ex:packet-rank1-lattice` (11749), `ex:packet-virasoro` (11783), `ex:packet-w3` (11857), `rem:genus2-definitive-scope` (12261), `rem:leech-all-sk` (12316), `prop:prime-locality-proved-cases` (12553), `thm:prime-locality-obstructions` (12594), `rem:route-c-success` (12702), `rem:route-c-gap` (12726), `thm:riccati-determinacy-assessment` (12796), `prop:shadow-not-selberg` (12839), `rem:shadow-riemann-independence` (12900), `rem:prime-locality-definitive` (12937). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
13:- [MEDIUM] chapters/connections/bv_brst.tex:57 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:brst-anomaly-gkw` (57), `rem:modular-qme-bv` (103), `rem:sft-bar-identification` (155), `def:bv-data-chir…2838 tokens truncated…`def:relative-holographic-deformation` (4017), `cor:holographic-deformation-cohomology` (4076), `def:holographic-obstruction-tower` (4089), `def:relative-quartic-obstruction` (4125), `conj:relative-quartic-computation` (4148), `rem:frontier-obstruction-anatomy` (4192), `rem:frontier-sft-vertices` (4260), `rem:frontier-tachyon` (4356), `rem:frontier-positive-geometry-bar` (4371), `prop:frontier-celestial-ope` (4456), `prop:frontier-sw-shadow` (4530), `prop:frontier-cs-shadow` (4597), `rem:agt-factorization-homology` (4656), `thm:frontier-twisted-holography` (4706), `prop:phantom-m5-koszul-dual` (5060), `rem:frontier-holographic-datum-table` (5141), `comp:burns-space-holographic-datum` (5194), `rem:kappa-hodge-to-witten-genus` (5265), `rem:shadow-tower-tqft-taylor` (5330). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
22:- [MEDIUM] chapters/connections/genus1_seven_faces.tex:136 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `def:g1sf-collision-residue` (136), `rem:g1sf-dichotomy` (218), `rem:g1sf-kzb-shadow` (426), `rem:g1sf-higher-rank` (550), `rem:g1sf-hitchin` (633), `rem:g1sf-c1-vanishing` (740), `rem:g1sf-genuinely-new` (791), `rem:g1sf-class-gc` (807), `rem:g1sf-class-m-scope` (918), `thm:g1sf-degeneration` (950), `thm:g1sf-b-cycle-monodromy` (1093), `rem:g1sf-b-cycle-face-0` (1130), `rem:g1sf-class-m-no-qg` (1145), `conj:g1sf-higher-genus` (1180). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
23:- [MEDIUM] chapters/connections/genus_complete.tex:159 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `thm:higher-genus-diff` (159), `conj:holographic-bar-cobar` (702), `prop:bulk-from-boundary` (767), `rem:mc-defect-couplings` (782), `def:holographic-state-spaces` (800), `def:holographic-partition-function` (817), `def:descendant-hol-amplitudes` (859), `rem:finite-data-genus` (881), `def:modular-chern-weil-transform` (902), `rem:k-theoretic-hierarchy` (954), `ex:chern-weil-heisenberg` (992), `ex:chern-weil-virasoro` (1020), `rem:entropy-genus-independent` (1055), `def:complementarity-legendrian` (1084), `conj:front-discriminant-resonance` (1100), `def:nonlinear-regular-locus` (1112), `def:complementarity-stokes-groupoid` (1130), `def:phase-index` (1143), `rem:phase-index-families` (1155), `rem:stokes-r-matrix` (1184), `thm:full-modular-invariant-hierarchy` (1212), `rem:beyond-ahat-genus` (1266), `rem:hs-sewing-completed` (1441), `cor:hs-implies-gram` (1456), `rem:heisenberg-bc-connection` (1518), `prop:analytic-conilpotency` (1552), `def:shadow-partition-function` (1638), `conj:analytic-center-invariance` (1654), `rem:analytic-execution-order` (1734), `def:euler-koszul-defect` (1950), `thm:euler-koszul-criterion` (1971), `comp:euler-koszul-defect-table` (2008), `prop:zeta-zeros-defect-derivative` (2100), `thm:li-closed-form` (2138), `rem:li-numerical-two-theories` (2206), `def:surface-moment-matrix` (2280), `def:surface-moment-matrix` (2281), `thm:surface-moment-positivity` (2298), `cor:virasoro-gram-ratio` (2321), `thm:sewing-rkhs` (2356), `def:platonic-arithmetic-package` (2565), `rem:sewing-hecke-collapse` (2786). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
24:- [MEDIUM] chapters/connections/holographic_codes_koszul.tex:70 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:hc-two-codes` (70), `rem:hc-adh-comparison` (201), `rem:hc-unitary-physical-qec` (286), `conj:hc-physical-qec` (314), `rem:hc-non-koszul-failure` (424), `rem:hc-universal-parameters` (674), `thm:hc-census` (713), `rem:hc-gravitational-code-complexity` (756). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
25:- [MEDIUM] chapters/connections/holographic_datum_master.tex:769 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:hdm-master-scope` (769), `rem:hdm-u-a-recoverability-scope` (837), `rem:hdm-heisenberg-verification` (859), `rem:hdm-four-consistency-conditions` (902), `thm:hdm-hbar-three-identification` (964), `thm:hdm-higher-gaudin` (1025), `rem:hdm-higher-gaudin-trichotomy` (1072), `rem:hdm-why-seven` (1140), `rem:hdm-methodological-hierarchy` (1159). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
26:- [MEDIUM] chapters/connections/holomorphic_topological.tex:87 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:ht-cg-dictionary` (87), `prop:ht-bar-genus-zero` (118), `thm:ht-mc-all-genera` (150), `cor:ht-shadow-archetype` (187), `prop:ht-five-shadow-synthesis` (245), `prop:ht-four-recovery` (287), `rem:ht-s-duality-proved` (368), `rem:ht-four-dualities-comparison` (382), `ex:ht-n4-sym` (461), `ex:ht-n2-hyper` (476), `ex:ht-n1` (492), `rem:boundary-voa-shadow-depth-classification` (507), `rem:ht-twistor-genus-level` (629), `rem:ht-twistor-three-regimes` (682), `rem:beta-function-kappa-distinction` (734), `rem:ht-celestial-obstruction-convolution` (823), `rem:costello-four-layers` (955), `rem:costello-comparison-table` (1022), `rem:burns-f2-verification` (1187), `rem:gaiotto-programme-comparison` (1222), `rem:costello-bcov` (1385). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
27:- [MEDIUM] chapters/connections/kontsevich_integral.tex:37 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `def:vassiliev-invariant` (37), `def:chord-diagram` (50), `thm:kontsevich-invariant` (61), `def:weight-system` (82), `rem:imaginary-part` (244), `rem:bar-quasi-triangular` (378), `rem:cs-scope` (511). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
28:- [MEDIUM] chapters/connections/master_concordance.tex:113 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:master-seven-not-six` (113), `rem:master-seven-face-architecture` (486). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
29:- [MEDIUM] chapters/connections/outlook.tex:103 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:three-pillars` (103), `conj:celestial-cross-conjecture-vol1` (318), `rem:koszul-swampland-evidence` (429). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
exec
/bin/zsh -lc "perl <<'PERL' > /tmp/vol1_dead_labels_raw.tsv
use strict;
use warnings;
my @def_files = (\"main.tex\", glob(\"chapters/**/*.tex\"), glob(\"appendices/**/*.tex\"));
my @ref_files = (@def_files, glob(\"/Users/raeez/chiral-bar-cobar-vol2/**/*.tex\"), glob(\"/Users/raeez/calabi-yau-quantum-groups/**/*.tex\"));
my %refs;
for my "'$file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/;
  my $text = <$fh>;
  close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) {
      $refs{$label}++ if length $label;
    }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) {
    "'$refs{$1}++ if length $1;
  }
}
print "severity'"\\tkind\\tfile\\tline\\tlabel\\n\";
for my "'$file (@def_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>;
  close $fh;
  for (my $i = 0; $i <= $#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) {
        "'$kind = '"'phantom-stub';
      } elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) {
        "'$kind = '"'item';
      } elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) {
        "'$kind = '"'sectioning';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) {
        $kind = '"'displaymath';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) {
        "'$kind = '"'float';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) {
        "'$kind = '"'claimlike';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) {
        "'$kind = '"'list';
      }
      my "'$sev = $kind eq '"'phantom-stub' ? 'HIGH' : "'$kind eq '"'claimlike' ? 'MEDIUM' : 'LOW';
      print join(\"\\t\", "'$sev, $kind, $file, $i+1, $label), "'"\\n\";
    }
  }
}
PERL
wc -l /tmp/vol1_dead_labels_raw.tsv
sed -n '1,10p' /tmp/vol1_dead_labels_raw.tsv" in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
    7730 /tmp/vol1_dead_labels_raw.tsv
severity	kind	file	line	label
HIGH	phantom-stub	main.tex	1597	subsec:frontier-protected-holographic-transform
HIGH	phantom-stub	main.tex	1617	chap:dg-shifted-factorization
HIGH	phantom-stub	main.tex	1622	ch:ym-higher-body-couplings
HIGH	phantom-stub	main.tex	1624	app:typeA-baxter-rees-theta
HIGH	phantom-stub	main.tex	1630	subsec:cy-research-programmes
HIGH	phantom-stub	main.tex	1655	sec:concordance-e1-modular-theory
HIGH	phantom-stub	main.tex	1656	sec:concordance-structural-upgrades
HIGH	phantom-stub	main.tex	1659	subsec:concordance-koszulness-meta-theorem
HIGH	phantom-stub	main.tex	1660	princ:shadow-depth-escalator

thinking
**Updating plan status**

I need to update the plan step statuses, but first, it’s crucial to verify some labels that may be unreferenced. I could spot-check one from the main document and one from concordance using regex across the repository. We’ve already reviewed the context. It might show no hits besides definitions. While manual verification could help, it’s possible the script has adequately computed it. I should also search for high severity clusters and orphan labels, just to be thorough.
codex
The report is built. I’m doing a final falsification pass on representative labels from each severity tier so the machine-generated list isn’t sneaking in a false positive through an unhandled macro.
exec
/bin/zsh -lc "rg -n -F 'subsec:frontier-protected-holographic-transform' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'sec:the-seed' chapters/theory/introduction.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'rem:concordance-bifunctor-koszul' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'D:bar-htpy' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/introduction.tex:2506:\phantomsection\label{sec:the-seed}%
chapters/theory/introduction.tex:2506:\phantomsection\label{sec:the-seed}%
 succeeded in 53ms:
main.tex:1597: \phantomsection\label{subsec:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
appendices/nonlinear_modular_shadows.tex:1022:\S\ref{subsec:frontier-protected-holographic-transform}.
chapters/connections/frontier_modular_holography_platonic.tex:103:\label{subsec:frontier-protected-holographic-transform}
 succeeded in 50ms:
chapters/connections/concordance.tex:3043:\label{rem:concordance-bifunctor-koszul}
 succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:436:\item\label{D:bar-htpy}

thinking
**Evaluating Perl globbing behavior**

I'm considering how Perl's glob function works with the pattern `glob('appendices/**/*.tex')`. It might not recurse as I expected. It seems like it could only match one level, depending on shell expansion. If it's looking for `appendices/**/*.tex`, it would miss top-level files like `appendices/nonlinear_modular_shadows.tex`. I'll need to modify this to include `appendices/*.tex` as well. This is crucial because certain file counts and references in the appendices won't be accurate otherwise. I need to reassess my approach.
codex
I found a real bug in the first pass: Perl globbing missed top-level `appendices/*.tex`, which created false positives. I’m rebuilding the file list with `rg --files` now and regenerating the audit from that corrected surface.
exec
/bin/zsh -lc "rg --files main.tex chapters appendices -g '*.tex' | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex
chapters/examples/deformation_quantization.tex
chapters/examples/w_algebras_deep.tex
chapters/examples/symmetric_orbifolds.tex
chapters/examples/lattice_foundations.tex
chapters/examples/beta_gamma.tex
chapters/examples/yangians.tex
chapters/examples/y_algebras.tex
chapters/examples/logarithmic_w_algebras.tex
chapters/examples/w3_holographic_datum.tex
chapters/examples/heisenberg_eisenstein.tex
chapters/examples/free_fields.tex
chapters/examples/yangians_foundations.tex
chapters/examples/kac_moody.tex
chapters/examples/toroidal_elliptic.tex
chapters/examples/bershadsky_polyakov.tex
chapters/examples/bar_complex_tables.tex
chapters/examples/minimal_model_fusion.tex
chapters/examples/landscape_census.tex
chapters/examples/w3_composite_fields.tex
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/main.tex
/Users/raeez/chiral-bar-cobar-vol2/main.tex
/Users/raeez/calabi-yau-quantum-groups/appendices/conventions.tex
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex

thinking
**Rebuilding report structure**

I need to rebuild using the RG file lists, considering current repo appendices at the top-level and maybe some standalone files too. Since we’re actively building, it’s important. I should include the top-level `appendices/conventions.tex` from Volume III references. I’ll regenerate the report properly, ensuring we address false positives that may come from omitted appendices in the definitions and references. I'll verify that the previous false positives disappear by rerunning counts using the updated file list with Perl.
exec
/bin/zsh -lc "perl <<'PERL'
use strict;
use warnings;
sub file_list {
  my (@paths) = @_;
  my "'$cmd = '"'rg --files ' . join(' ', map { quotemeta("'$_) } @paths) . q{ -g '"'*.tex'};
  my @files = split /\\n/, qx{"'$cmd};
  return grep { length } @files;
}
my @def_files = file_list('"'main.tex','chapters','appendices');
my @ref_files = (@def_files, file_list('/Users/raeez/chiral-bar-cobar-vol2','/Users/raeez/calabi-yau-quantum-groups'));
my (%refs,%groups);
my "'$def_count = 0;
my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/; my $text = <$fh>; close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
for my $file (@def_files) {
  $files{$file}=1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>; close $fh;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label=$1; $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = '"'phantom-stub'; }
      elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) { "'$kind = '"'item'; }
      elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = '"'sectioning'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = '"'displaymath'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = '"'float'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = '"'claimlike'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = '"'list'; }
      "'$groups{"$file'"\\t"'$kind"}++;
    }
  }
}
my $dead_count=0; $dead_count += $_ for values %groups;
print "files=".(scalar keys %files)."'"\\nlabels="'$def_count'"\\ndead="'$dead_count'"\\ngroups=\".(scalar keys %groups).\"\\n\";
PERL" in /Users/raeez/chiral-bar-cobar succeeded in 92ms:
files=129
labels=13795
dead=8259
groups=446

thinking
**Regenerating report**

I noticed that the counts increased because I included appendix labels, which also led to a rise in the dead count. That's fine; I just need to regenerate the report using the correct file list this time. I want to make sure any false positives have been resolved. So, let’s rerun the generation process and check everything again to make it right! It's all about accuracy!
exec
/bin/zsh -lc "perl <<'PERL'
use strict;
use warnings;
sub file_list {
  my (@paths) = @_;
  my "'$cmd = '"'rg --files ' . join(' ', map { quotemeta("'$_) } @paths) . q{ -g '"'*.tex'};
  my @files = split /\\n/, qx{"'$cmd};
  return grep { length } @files;
}
my @def_files = file_list('"'main.tex','chapters','appendices');
my @ref_files = (@def_files, file_list('/Users/raeez/chiral-bar-cobar-vol2','/Users/raeez/calabi-yau-quantum-groups'));
my (%refs,%groups);
my "'$def_count = 0;
my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/;
  my $text = <$fh>;
  close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) {
      $refs{$label}++ if length $label;
    }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) {
    "'$refs{$1}++ if length $1;
  }
}
for my $file (@def_files) {
  $files{$file} = 1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = <$fh>;
  close $fh;
  for (my $i = 0; $i <= $#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1;
      $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) {
        "'$kind = '"'phantom-stub';
      } elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) {
        "'$kind = '"'item';
      } elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) {
        "'$kind = '"'sectioning';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) {
        $kind = '"'displaymath';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) {
        "'$kind = '"'float';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) {
        "'$kind = '"'claimlike';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) {
        "'$kind = '"'list';
      }
      my "'$sev = $kind eq '"'phantom-stub' ? 'HIGH' : "'$kind eq '"'claimlike' ? 'MEDIUM' : 'LOW';
      my "'$key = join("'"\\t\", "'$sev, $file, $kind);
      push @{$groups{$key}}, { label => $label, line => $i + 1 };
    }
  }
}
my $dead_count = 0;
$dead_count += scalar(@$_) for values %groups;
my $group_count = scalar keys %groups;
my $report = '"'/tmp/vol1_dead_label_audit.md';
open my "'$out, q{>}, $report or die "$report: $!";
print {$out} "# Vol I Dead Label Audit'"\\n\\n\";
print {"'$out} "Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `'"\\\\ref"'`, `'"\\\\ref*"'`, `'"\\\\eqref"'`, `'"\\\\eqref*"'`, `'"\\\\cref"'`, `'"\\\\Cref"'`, `'"\\\\pageref"'`, and `'"\\\\hyperref[...]"'`.'"\\n\\n\";
print {"'$out} "Checked: ".(scalar keys %files)." files | Labels: $def_count | Dead labels: $dead_count | Grouped findings: $group_count'"\\n\\n\";
for my "'$sev (qw(HIGH MEDIUM LOW)) {
  print {$out} "## $sev'"\\n\";
  my @keys = grep { /"'^$sev'"\\t/ } keys %groups;
  @keys = sort {
    my ("'$sa,$fa,$ka) = split /'"\\t/, "'$a, 3;
    my ($sb,$fb,$kb) = split /'"\\t/, "'$b, 3;
    my ($mina) = sort { $a <=> $b } map { $_->{line} } @{$groups{$a}};
    my ($minb) = sort { $a <=> $b } map { $_->{line} } @{$groups{$b}};
    $fa cmp $fb || $mina <=> $minb || $ka cmp $kb;
  } @keys;
  for my $key (@keys) {
    my ($sev2, $file, $kind) = split /'"\\t/, "'$key, 3;
    my @items = sort { $a->{line} <=> $b->{line} || $a->{label} cmp $b->{label} } @{$groups{$key}};
    my $first_line = $items[0]{line};
    my @tokens = map { sprintf('"'"'`%s` (%d)'"', "'$_->{label}, $_->{line}) } @items;
    my $labels = join('"', ', @tokens);
    my ("'$problem, $fix);
    if ($kind eq '"'phantom-stub') {
      "'$problem = "dead `'"\\\\phantomsection\\\\label{...}"'` compatibility stubs with zero incoming refs across Vol I/II/III: $labels.";
      $fix = "Delete the entire `'"\\\\phantomsection\\\\label{...}"'` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.";
    } elsif ($kind eq '"'claimlike') {
      "'$problem = "dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: $labels.";
      $fix = "Keep the surrounding mathematical content, but delete the listed `'"\\\\label{...}"'` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.";
    } elsif ($kind eq '"'sectioning') {
      "'$problem = "dead section/chapter/part labels with zero incoming refs: $labels.";
      $fix = "Keep the sectioning structure, but delete the listed `'"\\\\label{...}"'` commands. Reintroduce a label only when an actual cross-reference exists.";
    } elsif ($kind eq '"'displaymath') {
      "'$problem = "dead display-math labels with zero incoming refs: $labels.";
      $fix = "Keep the displayed formulae, but delete the listed `'"\\\\label{...}"'` commands. If a formula needs to be cited later, add the label back when the citation is added.";
    } elsif ($kind eq '"'float') {
      "'$problem = "dead table/figure labels with zero incoming refs: $labels.";
      $fix = "Keep the float content, but delete the listed `'"\\\\label{...}"'` commands unless you add a real reference to the float.";
    } elsif ($kind eq '"'item') {
      "'$problem = "dead enumerated-item labels with zero incoming refs: $labels.";
      $fix = "Keep the list items, but delete the listed `'"\\\\label{...}"'` commands. If an item must be cited, add the reference at the call site and restore only that label.";
    } elsif ($kind eq '"'list') {
      "'$problem = "dead list-level labels with zero incoming refs: $labels.";
      $fix = "Keep the list structure, but delete the listed `'"\\\\label{...}"'` commands.";
    } else {
      $problem = "dead labels with zero incoming refs: $labels.";
      $fix = "Delete the listed `'"\\\\label{...}"'` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.";
    }
    print {$out} "- [$sev2] $file:$first_line — PROBLEM: $problem FIX: $fix'"\\n\";
  }
  print {"'$out} "'"\\n\";
}
print {"'$out} "## Summary'"\\nChecked: \".(scalar keys %files).\" | Findings: "'$group_count | Verdict: FAIL'"\\n\";
close "'$out;
my $raw = '"'/tmp/vol1_dead_labels_raw.tsv';
open my "'$rawfh, q{>}, $raw or die "$raw: $!";
print {$rawfh} "severity'"\\tkind\\tfile\\tline\\tlabel\\n\";
for my "'$key (sort keys %groups) {
  my ($sev2,$file,$kind)=split /'"\\t/,"'$key,3;
  my @items = sort { $a->{line} <=> $b->{line} || $a->{label} cmp $b->{label} } @{$groups{$key}};
  for my $it (@items) {
    print {$rawfh} join("'"\\t\", "'$sev2, $kind, $file, $it->{line}, $it->{label}), "'"\\n\";
  }
}
close "'$rawfh;
print "$report'"\\n"'$raw'"\\n\";
PERL" in /Users/raeez/chiral-bar-cobar succeeded in 109ms:
/tmp/vol1_dead_label_audit.md
/tmp/vol1_dead_labels_raw.tsv
exec
/bin/zsh -lc "sed -n '1,20p' /tmp/vol1_dead_label_audit.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'tail -n 5 /tmp/vol1_dead_label_audit.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'subsec:frontier-protected-holographic-transform|sec:the-seed|rem:concordance-bifunctor-koszul|D:bar-htpy' /tmp/vol1_dead_label_audit.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
# Vol I Dead Label Audit

Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\Cref`, `\pageref`, and `\hyperref[...]`.

Checked: 129 files | Labels: 13795 | Dead labels: 8259 | Grouped findings: 446

## HIGH
- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.
- [HIGH] main.tex:1622 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `ch:ym-higher-body-couplings` (1622), `app:typeA-baxter-rees-theta` (1624), `subsec:cy-research-programmes` (1630), `sec:concordance-e1-modular-theory` (1655), `sec:concordance-structural-upgrades` (1656), `subsec:concordance-koszulness-meta-theorem` (1659), `princ:shadow-depth-escalator` (1660), `princ:physics-is-homotopy-type` (1662), `subsec:concordance-shadow-depth-classes` (1663), `subsec:concordance-further-characterizations` (1664), `subsec:concordance-bifunctor-obstruction` (1665), `subsec:concordance-koszulness-xref` (1666), `subsec:concordance-computational-diagnostics` (1667), `subsec:analytic-completion-programme-editorial` (1670), `sec:concordance-arithmetic-sewing` (1671), `constr:prime-side-li` (1753), `sec:genus-all-master` (1775), `subsec:sewing-gram-matrix` (1781), `def:swiss-cheese-W-resolution` (1835), `thm:branch-bv` (1836), `rem:affine-half-space-bv` (1840), `conj:relative-quartic-computation` (1847), `def:relative-holographic-deformation` (1848), `constr:vol2-oc-mc-element` (1857), `thm:vol2-oc-mc-equation` (1858), `conj:globalization` (1859), `conj:boundary-line-generation` (1860), `conj:khan-zeng-comparison` (1861). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.

## MEDIUM
- [MEDIUM] appendices/_sl2_yangian_insert.tex:133 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:ordered-vs-symmetric-sl2` (133), `cor:hilbert-sl2` (456), `prop:eval-tensor-sl2` (502), `rem:closed-vs-open-sl2` (597), `rem:e-inf-e1-sl2` (612), `rem:sl2-formality` (633). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/arnold_relations.tex:73 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `prop:operadic-equivalence-arnold` (73), `thm:bar-d-squared-arnold` (92), `def:orlik-solomon-arnold` (113), `lem:OS-cohomology-arnold` (125), `rem:nine-term-detailed-arnold` (155), `cor:dres-squared-global` (501), `rem:nine-term-global` (521). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/branch_line_reductions.tex:147 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `def:scalar-mc-skeleton` (147), `prop:scalar-mc-skeleton` (175), `rem:scalar-skeleton-not-replacement` (196), `def:spectral-cumulants` (214), `thm:spectral-cumulant-hierarchy` (234), `rem:connected-cycle-interpretation` (283), `def:trace-compatible-filtered-dglie` (301), `rem:filtered-lift-use-after-mc2` (421), `def:effective-positive-weight-functor` (438), `cor:vir-localization-reduced-spectral` (493), `rem:reduced-line-shared-sheet` (509), `cor:mu2-centered-at-13` (562), `def:branch-line-primitive-quotients` (660), `def:hodge-depth` (677), `cor:vir-genus-two-vanishing` (845), `cor:first-primitive-genus-three` (857), `thm:pure-branch-primitive-coefficient` (905), `rem:rose-coefficients-all-genera` (938), `rem:genus-three-basis-notation` (984), `cor:genus-three-primitive-top-hodge` (1037), `rem:what-genus-three-remembers` (1092), `cor:shared-sheet-universal-coefficients` (1109), `ex:heisenberg-scalar-only-frame` (1151), `conj:spectral-shadow-principle` (1184), `rem:logarithm-canonical` (1202), `rem:blr-structural-picture` (1244). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/combinatorial_frontier.tex:116 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:reading-frontier-table` (116), `rem:partition-mc3-bridge` (156), `rem:complementary-vs-koszul-dual` (604), `rem:ce-vs-chiral` (843), `conj:virasoro-pade-periodic` (941). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/dual_methodology.tex:9 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `conv:dual-proof` (9), `rem:dual-proofs` (14), `thm:abstract-rh` (92), `thm:geometric-infty-operads` (158), `cor:derived-koszul` (192). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/homotopy_transfer.tex:15 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `prop:htt-rectification` (15), `ex:trees-m4` (230), `prop:transfer-signs` (259), `thm:minimal-model-existence` (284), `cor:formality` (296), `ex:minimal-derham` (306), `thm:htt-operadic` (339), `prop:linf-relations` (380), `comp:l4-formula` (391), `thm:linf-minimal-unique` (404), `ex:transfer-sym-coalg` (433), `ex:km-minimal` (486), `rem:koszulness-formality-htt` (590), `rem:feynman-htt` (686), `rem:higher-genus-htt` (794), `rem:renormalization-htt` (836). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/koszul_reference.tex:17 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `thm:extended-koszul-appendix` (17), `thm:genus-graded-koszul-duality-appendix` (73), `lem:genus-graded-koszul-resolution-appendix` (117), `thm:genus-graded-mc-appendix` (138), `rem:why-essential-image-matters` (262), `lem:connectedness-augmentation` (359), `cor:geom-implies-koszul` (420), `thm:completion-characterization` (589), `rem:non-uniqueness-strict` (637). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/nonlinear_modular_shadows.tex:35 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:shadow-period-correction` (35), `rem:nms-prefundamental-cg` (74), `rem:shadow-termination-novelty` (289), `prop:nms-five-component` (335), `thm:nms-shadow-tower-mc` (395), `cor:nms-all-families-universal` (435), `rem:nms-chriss-ginzburg` (448), `def:nms-ambient-datum` (480), `def:nms-ambient-tangent-complex` (513), `thm:nms-ambient-complementarity-tangent` (528), `thm:nms-ambient-complementarity-fmp` (552), `rem:nms-stronger-than-additive` (566), `def:nms-degree-shadows` (693), `rem:nms-hcq-as-degree-shadows` (706), `def:nms-shadow-graph-complex` (849), `rem:nms-tree-vs-obstruction` (882), `def:nms-primary-composite-envelope` (903), `prop:nms-quartic-closure-envelope` (924), `cor:nms-heisenberg-gaussian-boundary` (974), `rem:nms-class-g-not-over-a-point` (986), `rem:nms-heisenberg-derived-center` (1011), `def:nms-affine-sector` (1029), `cor:nms-affine-boundary-tree` (1062), `conj:nms-critical-mc` (1103), `rem:nms-critical-purely-nonlinear` (1116), `rem:nms-affine-derived-center` (1121), `def:nms-betagamma-slice` (1138), `cor:nms-betagamma-boundary-law` (1191), `rem:nms-uniform-linearity` (1249), `rem:nms-betagamma-derived-center` (1254), `def:nms-virasoro-envelope` (1304), `rem:quartic-theta-significance` (1394), `rem:nms-virasoro-derived-center` (1431), `def:nms-w3-envelope` (1460), `thm:nms-w3-mixed-shadow-normal-form` (1472), `def:nms-w3-primary-resonance` (1502), `rem:nms-visible-vs-full-resonance` (1526), `def:nms-principal-wn-envelope` (1590), `def:nms-generic-parameter-locus` (1661), `def:nms-contact-quartic-bundle` (1666), `rem:nms-tautological-lines` (1685), `prop:nms-basis-independence-specialization` (1747), `rem:nms-why-characteristic-class` (1760), `def:nms-cubic-tree-bundle` (1768), `rem:nms-tree-class-interpretation` (1794), `rem:nms-log-fm-clutching` (1863), `cor:nms-family-boundary-behavior` (1910), `rem:nms-why-quartic-resonance-is-new` (1942), `def:nms-nonlinear-characteristic-package` (1950), `prop:nms-functoriality-duality-quartic` (1979), `rem:nms-characteristic-hierarchy` (1988), `rem:nms-frontier-reset` (2047), `thm:nms-quintic-frame-families` (2153), `rem:nms-virasoro-infinite-tower` (2208), `cor:nms-quintic-separating-boundary` (2232), `prop:nms-genus-loop-properties` (2278), `rem:nms-beyond-ahat` (2335), `rem:nms-modular-invariant-ratio` (2396), `def:nms-full-modular-shadow-characteristic` (2406), `rem:nms-invariant-hierarchy-summary` (2432), `thm:nms-unified-summary` (2452), `rem:nms-what-remains` (2494), `def:nms-modular-feynman-transform` (2507), `rem:nms-feynman-three-requirements` (2538), `def:nms-complementarity-legendrian` (2568), `rem:nms-legendrian-three-virtues` (2580), `rem:nms-phase-wall-crossing` (2748), `def:nms-nonlinear-branch-stack` (2756), `rem:nms-conceptual-outcome` (2772), `def:nms-polarized-modular-graph-algebra` (2795), `thm:nms-bipartite-complementarity` (2821), `conj:nms-polarized-universal-class` (2829), `def:nms-resonance-wall-locus` (2844), `def:nms-resonance-scattering-diagram` (2853), `def:nms-complementarity-schober` (2874), `rem:nms-schober-vs-scattering` (2884), `def:nms-modular-wavefunction` (2892), `rem:nms-wavefunction-normal-forms` (2909), `conj:nms-quartic-lift` (2948), `rem:quartic-lift-evidence` (2953), `conj:nms-resonance-wall-crossing` (2989), `conj:nms-quantization-theorem` (2994), `rem:nms-implementation-path` (2999), `rem:nms-bridge-consumption` (3079), `rem:nms-extended-hierarchy` (3135), `rem:nms-factorization-envelope-programme` (3154), `rem:nms-mc4-finite-linear-algebra` (3465), `def:nms-kappa-matrix` (3513), `ex:nms-w3-multivariable-shadow` (3584), `rem:propagator-variance-mixing` (3632), `rem:nms-w4-two-propagator` (3724), `rem:ds-depth-monotonicity-failure` (3805), `rem:ds-ghost-shadow-consistency` (3891), `rem:ope-closedness-necessary` (4019), `rem:nms-discriminant-instability` (4179), `def:nms-mc-moduli-curve` (4213), `thm:nms-mc-moduli-curve-structure` (4236), `thm:nms-hadamard-mc-potential` (4299), `cor:nms-mc-solution-counting` (4346), `rem:nms-trivial-isomonodromy` (4363). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/notation_index.tex:415 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `def:koszul-operad-index` (415), `def:twisting-morphism-index` (444). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
 succeeded in 53ms:
- [LOW] chapters/theory/three_invariants.tex:77 — PROBLEM: dead display-math labels with zero incoming refs: `eq:p-max-def` (77), `eq:k-max-def` (107), `eq:r-max-def` (146). FIX: Keep the displayed formulae, but delete the listed `\label{...}` commands. If a formula needs to be cited later, add the label back when the citation is added.
- [LOW] chapters/theory/three_invariants.tex:265 — PROBLEM: dead labels with zero incoming refs: `warn:ap59-three-invariants` (265). FIX: Delete the listed `\label{...}` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.

## Summary
Checked: 129 | Findings: 446 | Verdict: FAIL
 succeeded in 53ms:
8:- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.
176:- [LOW] chapters/connections/concordance.tex:1676 — PROBLEM: dead labels with zero incoming refs: `sum:three-pillars-chain-level` (1676), `constr:mc3-difficulty-gradient-concordance` (1884), `rem:concordance-bifunctor-koszul` (3043), `eq:bernoulli-a-hat` (6120), `item:concordance-classical-sewing-zeta` (8673), `item:concordance-entanglement-annulus` (8710), `item:concordance-cyclotomic-chart` (8753), `item:concordance-cyclotomic-admissible` (8871), `item:concordance-cyclotomic-km` (8899), `item:concordance-cyclotomic-virasoro` (8939), `item:concordance-cyclotomic-zhu` (9004), `item:concordance-periodic-cdg` (9076), `item:concordance-modular-globalisation` (9197), `item:concordance-discard-criteria` (9224), `constr:shadow-epstein-functor` (9913). FIX: Delete the listed `\label{...}` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.
429:- [LOW] chapters/theory/higher_genus_modular_koszul.tex:436 — PROBLEM: dead enumerated-item labels with zero incoming refs: `D:bar-htpy` (436), `D:dual-htpy` (441), `D:deformation-htpy` (444), `D:center-htpy` (453), `D:discriminant-htpy` (459), `D:periodicity-htpy` (464), `MK:inversion-htpy` (498), `MK:complementarity-htpy` (504), `D:bar` (543), `D:dual` (549), `D:center-dg` (574), `D:discriminant-dg` (579), `D:periodicity-dg` (584), `MK:inversion` (625), `MK:complementarity` (633), `MK:mc-control` (669), `MK:clutching-verdier` (673), `MK:e1-face` (677). FIX: Keep the list items, but delete the listed `\label{...}` commands. If an item must be cited, add the reference at the call site and restore only that label.

thinking
**Verifying main label status**

Alright, I need to check if the high main label is actually dead. I’m thinking about searching a couple of places, specifically looking for `ch:ym-higher-body-couplings` across the repository. This will help me confirm its status. It’s important to get this verification done accurately! I'm curious to see what I find and how it all connects. Let’s get started on this!
exec
/bin/zsh -lc "rg -n -F 'D:bar-htpy' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'rem:concordance-bifunctor-koszul' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'ch:ym-higher-body-couplings' main.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'sec:modular-char-spectral-disc-intro' chapters/theory/introduction.tex chapters appendices /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:3043:\label{rem:concordance-bifunctor-koszul}
 succeeded in 53ms:
chapters/theory/higher_genus_modular_koszul.tex:436:\item\label{D:bar-htpy}
 succeeded in 53ms:
main.tex:1622: \phantomsection\label{ch:ym-higher-body-couplings}% % ym_higher_body_couplings.tex (migrated to Vol II)
chapters/connections/ym_higher_body_couplings.tex:2:\label{ch:ym-higher-body-couplings}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex:2:\label{ch:ym-higher-body-couplings}
 succeeded in 51ms:
chapters/theory/introduction.tex:2504:\phantomsection\label{sec:modular-char-spectral-disc-intro}%
chapters/theory/introduction.tex:2504:\phantomsection\label{sec:modular-char-spectral-disc-intro}%

thinking
**Calculating label groups**

It seems like I've confirmed the true dead labels, which is great! Now, I need to count the high groups or labels after updating the file list. I'll get started on that computation to ensure I have accurate counts. This step is crucial for moving forward effectively and making sure everything aligns correctly. Let's see what the numbers say!
exec
/bin/zsh -lc "perl <<'PERL'
use strict;
use warnings;
sub file_list {
  my (@paths) = @_;
  my "'$cmd = '"'rg --files ' . join(' ', map { quotemeta("'$_) } @paths) . q{ -g '"'*.tex'};
  my @files = split /\\n/, qx{"'$cmd};
  return grep { length } @files;
}
my @def_files = file_list('"'main.tex','chapters','appendices');
my @ref_files = (@def_files, file_list('/Users/raeez/chiral-bar-cobar-vol2','/Users/raeez/calabi-yau-quantum-groups'));
my (%refs,%sev_labels,%sev_groups);
for my "'$file (@ref_files) { open my $fh, q{<}, $file or die "$file: $!"; local $/; my $text=<$fh>; close $fh; while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) { for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; } } while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; } }
for my $file (@def_files) { open my $fh, q{<}, $file or die "$file: $!"; my @lines = <$fh>; close $fh; for (my $i=0; $i<=$#lines; $i++) { while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) { my "'$label=$1; next if $refs{$label}; my $ctx=join q{}, map { $lines[$_] // q{} } grep { $_>=0 && $_<=$#lines } ($i-2,$i-1,$i,$i+1); my $kind='"'other'; if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind='"'phantom-stub'; } elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) { "'$kind='"'item'; } elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind='"'sectioning'; } elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind='"'displaymath'; } elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind='"'float'; } elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind='"'claimlike'; } elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind='"'list'; } my "'$sev = $kind eq '"'phantom-stub' ? 'HIGH' : "'$kind eq '"'claimlike' ? 'MEDIUM' : 'LOW'; "'$sev_labels{$sev}++; $sev_groups{$sev}{"$file'"\\t"'$kind"}++; } } }
for my $sev (qw(HIGH MEDIUM LOW)) { my $groups = $sev_groups{$sev} ? scalar keys %{$sev_groups{$sev}} : 0; my $labels = $sev_labels{$sev} // 0; print "$sev groups=$groups labels=$labels'"\\n\"; }
PERL" in /Users/raeez/chiral-bar-cobar succeeded in 140ms:
HIGH groups=2 labels=30
MEDIUM groups=116 labels=3861
LOW groups=328 labels=4368


thinking
**Considering comment handling**

I'm thinking about how to handle multiline comments when looking for labels and references. So, should I ignore commented labels too? I think that's likely yes. However, we don’t have commented-out labels in our file list, so I need to strip comments to avoid getting false positives. The user wants to find all active `\label{}` that aren’t referenced anywhere, so I should probably ignore comments. I'll implement a way to strip comments carefully while respecting escaped characters.
thinking
**Updating parser for comments**

I’m working on improving the parser by stripping comments before scanning references and labels, as this might affect counts. I need to decide if I should include `%` in URLs, even though it's unlikely in TeX. The plan is to implement a line-wise preprocessing function to handle this correctly. I also have to ensure that labels in comments are ignored and that escaped `%` signs are managed properly. I’ll need to recompute counts after these changes!
codex
I’m closing one more accuracy gap: the first parser counted reference macros inside comments. I’m stripping TeX comments and regenerating once more so commented-out `\ref{...}` lines don’t keep dead labels artificially alive.
exec
/bin/zsh -lc "perl <<'PERL'
use strict;
use warnings;
sub file_list {
  my (@paths) = @_;
  my "'$cmd = '"'rg --files ' . join(' ', map { quotemeta("'$_) } @paths) . q{ -g '"'*.tex'};
  my @files = split /\\n/, qx{"'$cmd};
  return grep { length } @files;
}
sub strip_comments {
  my ($text) = @_;
  my @out;
  for my $line (split /'"\\n/, "'$text, -1) {
    $line =~ s/(?<!'"\\\\)%.*"'$//;
    push @out, $line;
  }
  return join("'"\\n\", @out);
}
my @def_files = file_list('main.tex','chapters','appendices');
my @ref_files = (@def_files, file_list('/Users/raeez/chiral-bar-cobar-vol2','/Users/raeez/calabi-yau-quantum-groups'));
my (%refs,%groups);
my "'$def_count = 0;
my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/;
  my $text = strip_comments(<$fh>);
  close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) { $refs{$label}++ if length $label; }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) { "'$refs{$1}++ if length $1; }
}
for my $file (@def_files) {
  $files{$file}=1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @raw = <$fh>; close $fh;
  my @lines = map { my $x=$_; $x =~ s/(?<!'"\\\\)%.*"'$//; $x } @raw;
  for (my $i=0; $i<=$#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label=$1; $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) { "'$kind = '"'phantom-stub'; }
      elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) { "'$kind = '"'item'; }
      elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) { "'$kind = '"'sectioning'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) { $kind = '"'displaymath'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) { "'$kind = '"'float'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) { "'$kind = '"'claimlike'; }
      elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) { "'$kind = '"'list'; }
      "'$groups{"$file'"\\t"'$kind"}++;
    }
  }
}
my $dead_count=0; $dead_count += $_ for values %groups;
print "files=".(scalar keys %files)."'"\\nlabels="'$def_count'"\\ndead="'$dead_count'"\\ngroups=\".(scalar keys %groups).\"\\n\";
PERL" in /Users/raeez/chiral-bar-cobar succeeded in 251ms:
files=129
labels=13794
dead=8265
groups=446

thinking
**Regenerating report**

I noticed that the counts have changed slightly, so it looks like I need to regenerate the final report. I’ll strip out any comments to ensure it’s clean and clear, focusing on the essential data. It's important to ensure everything is accurate before I present it. I want to get this right because clarity matters in a final report! Alright, let's get started on regenerating that report.
exec
/bin/zsh -lc "perl <<'PERL'
use strict;
use warnings;
sub file_list {
  my (@paths) = @_;
  my "'$cmd = '"'rg --files ' . join(' ', map { quotemeta("'$_) } @paths) . q{ -g '"'*.tex'};
  my @files = split /\\n/, qx{"'$cmd};
  return grep { length } @files;
}
sub strip_comments {
  my ($text) = @_;
  my @out;
  for my $line (split /'"\\n/, "'$text, -1) {
    $line =~ s/(?<!'"\\\\)%.*"'$//;
    push @out, $line;
  }
  return join("'"\\n\", @out);
}
my @def_files = file_list('main.tex','chapters','appendices');
my @ref_files = (@def_files, file_list('/Users/raeez/chiral-bar-cobar-vol2','/Users/raeez/calabi-yau-quantum-groups'));
my (%refs,%groups);
my "'$def_count = 0;
my %files;
for my $file (@ref_files) {
  open my $fh, q{<}, $file or die "$file: $!";
  local $/;
  my $text = strip_comments(<$fh>);
  close $fh;
  while ($text =~ /'"\\\\(?:ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|pageref)\\s*\\{(["'^}]+)'"\\}/g) {
    for my "'$label (split /'"\\s*,\\s*/, "'$1) {
      $refs{$label}++ if length $label;
    }
  }
  while ($text =~ /'"\\\\hyperref\\s*\\[(["'^'"\\]]+)\\]/g) {
    "'$refs{$1}++ if length $1;
  }
}
for my $file (@def_files) {
  $files{$file} = 1;
  open my $fh, q{<}, $file or die "$file: $!";
  my @lines = map { my $x = $_; $x =~ s/(?<!'"\\\\)%.*"'$//; $x } <$fh>;
  close $fh;
  for (my $i = 0; $i <= $#lines; $i++) {
    while ($lines[$i] =~ /'"\\\\label\\s*\\{(["'^}]+)'"\\}/g) {
      my "'$label = $1;
      $def_count++;
      next if $refs{$label};
      my $ctx = join q{}, map { $lines[$_] // q{} } grep { $_ >= 0 && $_ <= $#lines } ($i-2,$i-1,$i,$i+1);
      my $kind = '"'other';
      if ("'$lines[$i] =~ /'"\\\\phantomsection\\s*\\\\label/) {
        "'$kind = '"'phantom-stub';
      } elsif ("'$lines[$i] =~ /'"\\\\item\\s*\\\\label/) {
        "'$kind = '"'item';
      } elsif ("'$ctx =~ /'"\\\\(?:part|chapter|section|subsection|subsubsection)\\*?\\{/s) {
        "'$kind = '"'sectioning';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:equation|align|gather|multline|eqnarray|tikzcd|displaymath)\\}/s || "'$lines[$i] =~ /'"\\\\label\\{["'^}]+'"\\}\\s*\\\\\\\\?\\s*"'$/) {
        $kind = '"'displaymath';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:table|tabular|longtable|figure)\\}/s || "'$ctx =~ /'"\\\\caption\\{/s) {
        "'$kind = '"'float';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:theorem|proposition|lemma|corollary|remark|definition|example|computation|verification|conjecture|principle|convention|maintheorem|calculation)\\}/s) {
        "'$kind = '"'claimlike';
      } elsif ("'$ctx =~ /'"\\\\begin\\{(?:enumerate|itemize|description)\\}/s) {
        "'$kind = '"'list';
      }
      my "'$sev = $kind eq '"'phantom-stub' ? 'HIGH' : "'$kind eq '"'claimlike' ? 'MEDIUM' : 'LOW';
      my "'$key = join("'"\\t\", "'$sev, $file, $kind);
      push @{$groups{$key}}, { label => $label, line => $i + 1 };
    }
  }
}
my $dead_count = 0;
$dead_count += scalar(@$_) for values %groups;
my $group_count = scalar keys %groups;
my $report = '"'/tmp/vol1_dead_label_audit.md';
open my "'$out, q{>}, $report or die "$report: $!";
print {$out} "# Vol I Dead Label Audit'"\\n\\n\";
print {"'$out} "Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `'"\\\\ref"'`, `'"\\\\ref*"'`, `'"\\\\eqref"'`, `'"\\\\eqref*"'`, `'"\\\\cref"'`, `'"\\\\Cref"'`, `'"\\\\pageref"'`, and `'"\\\\hyperref[...]"'`. TeX comments were stripped before scanning.'"\\n\\n\";
print {"'$out} "Checked: ".(scalar keys %files)." files | Labels: $def_count | Dead labels: $dead_count | Grouped findings: $group_count'"\\n\\n\";
for my "'$sev (qw(HIGH MEDIUM LOW)) {
  print {$out} "## $sev'"\\n\";
  my @keys = grep { /"'^$sev'"\\t/ } keys %groups;
  @keys = sort {
    my ("'$sa,$fa,$ka) = split /'"\\t/, "'$a, 3;
    my ($sb,$fb,$kb) = split /'"\\t/, "'$b, 3;
    my ($mina) = sort { $a <=> $b } map { $_->{line} } @{$groups{$a}};
    my ($minb) = sort { $a <=> $b } map { $_->{line} } @{$groups{$b}};
    $fa cmp $fb || $mina <=> $minb || $ka cmp $kb;
  } @keys;
  for my $key (@keys) {
    my ($sev2, $file, $kind) = split /'"\\t/, "'$key, 3;
    my @items = sort { $a->{line} <=> $b->{line} || $a->{label} cmp $b->{label} } @{$groups{$key}};
    my $first_line = $items[0]{line};
    my @tokens = map { sprintf('"'"'`%s` (%d)'"', "'$_->{label}, $_->{line}) } @items;
    my $labels = join('"', ', @tokens);
    my ("'$problem, $fix);
    if ($kind eq '"'phantom-stub') {
      "'$problem = "dead `'"\\\\phantomsection\\\\label{...}"'` compatibility stubs with zero incoming refs across Vol I/II/III: $labels.";
      $fix = "Delete the entire `'"\\\\phantomsection\\\\label{...}"'` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.";
    } elsif ($kind eq '"'claimlike') {
      "'$problem = "dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: $labels.";
      $fix = "Keep the surrounding mathematical content, but delete the listed `'"\\\\label{...}"'` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.";
    } elsif ($kind eq '"'sectioning') {
      "'$problem = "dead section/chapter/part labels with zero incoming refs: $labels.";
      $fix = "Keep the sectioning structure, but delete the listed `'"\\\\label{...}"'` commands. Reintroduce a label only when an actual cross-reference exists.";
    } elsif ($kind eq '"'displaymath') {
      "'$problem = "dead display-math labels with zero incoming refs: $labels.";
      $fix = "Keep the displayed formulae, but delete the listed `'"\\\\label{...}"'` commands. If a formula needs to be cited later, add the label back when the citation is added.";
    } elsif ($kind eq '"'float') {
      "'$problem = "dead table/figure labels with zero incoming refs: $labels.";
      $fix = "Keep the float content, but delete the listed `'"\\\\label{...}"'` commands unless you add a real reference to the float.";
    } elsif ($kind eq '"'item') {
      "'$problem = "dead enumerated-item labels with zero incoming refs: $labels.";
      $fix = "Keep the list items, but delete the listed `'"\\\\label{...}"'` commands. If an item must be cited, add the reference at the call site and restore only that label.";
    } elsif ($kind eq '"'list') {
      "'$problem = "dead list-level labels with zero incoming refs: $labels.";
      $fix = "Keep the list structure, but delete the listed `'"\\\\label{...}"'` commands.";
    } else {
      $problem = "dead labels with zero incoming refs: $labels.";
      $fix = "Delete the listed `'"\\\\label{...}"'` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.";
    }
    print {$out} "- [$sev2] $file:$first_line — PROBLEM: $problem FIX: $fix'"\\n\";
  }
  print {"'$out} "'"\\n\";
}
print {"'$out} "## Summary'"\\nChecked: \".(scalar keys %files).\" | Findings: "'$group_count | Verdict: FAIL'"\\n\";
close "'$out;
my $raw = '"'/tmp/vol1_dead_labels_raw.tsv';
open my "'$rawfh, q{>}, $raw or die "$raw: $!";
print {$rawfh} "severity'"\\tkind\\tfile\\tline\\tlabel\\n\";
for my "'$key (sort keys %groups) {
  my ($sev2,$file,$kind)=split /'"\\t/,"'$key,3;
  my @items = sort { $a->{line} <=> $b->{line} || $a->{label} cmp $b->{label} } @{$groups{$key}};
  for my $it (@items) {
    print {$rawfh} join("'"\\t\", "'$sev2, $kind, $file, $it->{line}, $it->{label}), "'"\\n\";
  }
}
close "'$rawfh;
print "$report'"\\n"'$raw'"\\n\";
PERL" in /Users/raeez/chiral-bar-cobar succeeded in 284ms:
/tmp/vol1_dead_label_audit.md
/tmp/vol1_dead_labels_raw.tsv

thinking
**Verifying report details**

I think I need to check the report and summarize it accurately. There are likely a few key points that I should highlight to ensure the information is clear and concise. I want to make sure I'm thorough in my review. Let’s double-check any details that might need clarification, so I can provide the best possible summary for the user. Doing this right is important! All right, let’s get started on that.
exec
/bin/zsh -lc 'wc -l /tmp/vol1_dead_labels_raw.tsv' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'tail -n 5 /tmp/vol1_dead_label_audit.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,15p' /tmp/vol1_dead_label_audit.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    8266 /tmp/vol1_dead_labels_raw.tsv
 succeeded in 53ms:
- [LOW] chapters/theory/three_invariants.tex:77 — PROBLEM: dead display-math labels with zero incoming refs: `eq:p-max-def` (77), `eq:k-max-def` (107), `eq:r-max-def` (146). FIX: Keep the displayed formulae, but delete the listed `\label{...}` commands. If a formula needs to be cited later, add the label back when the citation is added.
- [LOW] chapters/theory/three_invariants.tex:265 — PROBLEM: dead labels with zero incoming refs: `warn:ap59-three-invariants` (265). FIX: Delete the listed `\label{...}` commands. Where a label sits alone on its own line, remove that whole line; where it is inline, remove only the dead label token.

## Summary
Checked: 129 | Findings: 446 | Verdict: FAIL
 succeeded in 52ms:
# Vol I Dead Label Audit

Scope: `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex` in Vol I. Incoming references checked across those files plus all `.tex` sources in Vol II and Vol III. Counted as live refs: `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\Cref`, `\pageref`, and `\hyperref[...]`. TeX comments were stripped before scanning.

Checked: 129 files | Labels: 13794 | Dead labels: 8265 | Grouped findings: 446

## HIGH
- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.
- [HIGH] main.tex:1622 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `ch:ym-higher-body-couplings` (1622), `app:typeA-baxter-rees-theta` (1624), `subsec:cy-research-programmes` (1630), `sec:concordance-e1-modular-theory` (1655), `sec:concordance-structural-upgrades` (1656), `subsec:concordance-koszulness-meta-theorem` (1659), `princ:shadow-depth-escalator` (1660), `princ:physics-is-homotopy-type` (1662), `subsec:concordance-shadow-depth-classes` (1663), `subsec:concordance-further-characterizations` (1664), `subsec:concordance-bifunctor-obstruction` (1665), `subsec:concordance-koszulness-xref` (1666), `subsec:concordance-computational-diagnostics` (1667), `subsec:analytic-completion-programme-editorial` (1670), `sec:concordance-arithmetic-sewing` (1671), `constr:prime-side-li` (1753), `sec:genus-all-master` (1775), `subsec:sewing-gram-matrix` (1781), `def:swiss-cheese-W-resolution` (1835), `thm:branch-bv` (1836), `rem:affine-half-space-bv` (1840), `conj:relative-quartic-computation` (1847), `def:relative-holographic-deformation` (1848), `constr:vol2-oc-mc-element` (1857), `thm:vol2-oc-mc-equation` (1858), `conj:globalization` (1859), `conj:boundary-line-generation` (1860), `conj:khan-zeng-comparison` (1861). FIX: Delete the entire `\phantomsection\label{...}` lines for these stubs; the stubs themselves are the labeled objects, and no live source references them.

## MEDIUM
- [MEDIUM] appendices/_sl2_yangian_insert.tex:133 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:ordered-vs-symmetric-sl2` (133), `cor:hilbert-sl2` (456), `prop:eval-tensor-sl2` (502), `rem:closed-vs-open-sl2` (597), `rem:e-inf-e1-sl2` (612), `rem:sl2-formality` (633). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/arnold_relations.tex:73 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `prop:operadic-equivalence-arnold` (73), `thm:bar-d-squared-arnold` (92), `def:orlik-solomon-arnold` (113), `lem:OS-cohomology-arnold` (125), `rem:nine-term-detailed-arnold` (155), `cor:dres-squared-global` (501), `rem:nine-term-global` (521). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/branch_line_reductions.tex:147 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `def:scalar-mc-skeleton` (147), `prop:scalar-mc-skeleton` (175), `rem:scalar-skeleton-not-replacement` (196), `def:spectral-cumulants` (214), `thm:spectral-cumulant-hierarchy` (234), `rem:connected-cycle-interpretation` (283), `def:trace-compatible-filtered-dglie` (301), `rem:filtered-lift-use-after-mc2` (421), `def:effective-positive-weight-functor` (438), `cor:vir-localization-reduced-spectral` (493), `rem:reduced-line-shared-sheet` (509), `cor:mu2-centered-at-13` (562), `def:branch-line-primitive-quotients` (660), `def:hodge-depth` (677), `cor:vir-genus-two-vanishing` (845), `cor:first-primitive-genus-three` (857), `thm:pure-branch-primitive-coefficient` (905), `rem:rose-coefficients-all-genera` (938), `rem:genus-three-basis-notation` (984), `cor:genus-three-primitive-top-hodge` (1037), `rem:what-genus-three-remembers` (1092), `cor:shared-sheet-universal-coefficients` (1109), `ex:heisenberg-scalar-only-frame` (1151), `conj:spectral-shadow-principle` (1184), `rem:logarithm-canonical` (1202), `rem:blr-structural-picture` (1244). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
- [MEDIUM] appendices/combinatorial_frontier.tex:116 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:reading-frontier-table` (116), `rem:partition-mc3-bridge` (156), `rem:complementary-vs-koszul-dual` (604), `rem:ce-vs-chiral` (843), `conj:virasoro-pade-periodic` (941). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.



thinking
**Summarizing findings on labels**

I could use the file related to the dead label audit. I scanned 129 Volume I files, cross-checked incoming references across Volumes I, II, and III after cleaning them up. I found 13,794 labels total, with 8,265 being dead, categorized into 446 findings. Notably, there are two high stub clusters and a mix of claim-like clusters. I might highlight the highest-severity clusters but will include an exhaustive report path too. I hope that meets the request!
thinking
**Finalizing report reference**

It seems like the exhaustive report file already has the format needed. I can definitely state, "The exhaustive report is here; the top high-severity findings are below." This way, I link everything together clearly for the user. It's a good approach since it directs the user to the necessary details without repeating too much. I hope that provides the clarity and completeness needed for their request!
thinking
**Considering report limitations**

I need to address how to respond about the remaining 444 findings in the linked report, as the user may want every detail. However, that's not feasible. The report uses the exact requested format, so I'll ensure it remains accessible. I could mention that no edits were made, but maybe that’s not necessary. I should also consider updating the plan for completion. It's definitely a balancing act here!
Plan update
Rebuilt the dead-label audit with corrected file discovery, cross-volume ref parsing, starred refs, and TeX comment stripping; generated exhaustive grouped and raw reports under /tmp.
  ✓ Enumerate Vol I label definitions and cross-volume reference uses
  ✓ Inspect each unreferenced label in source context and determine removal/retention fix
  ✓ Re-verify final findings and produce exhaustive report
codex
- [HIGH] chapters/theory/introduction.tex:2504 — PROBLEM: dead `\phantomsection\label{...}` relocation stubs with zero incoming refs across Vol I/II/III: `sec:modular-char-spectral-disc-intro` (2504), `sec:the-seed` (2506). FIX: delete the entire `\phantomsection\label{...}` lines; the stubs themselves are no longer needed.
- [HIGH] main.tex:1622 — PROBLEM: dead `\phantomsection\label{...}` compatibility stubs with zero incoming refs across Vol I/II/III: `ch:ym-higher-body-couplings` (1622), `app:typeA-baxter-rees-theta` (1624), `subsec:cy-research-programmes` (1630), `sec:concordance-e1-modular-theory` (1655), `sec:concordance-structural-upgrades` (1656), `subsec:concordance-koszulness-meta-theorem` (1659), `princ:shadow-depth-escalator` (1660), `princ:physics-is-homotopy-type` (1662), `subsec:concordance-shadow-depth-classes` (1663), `subsec:concordance-further-characterizations` (1664), `subsec:concordance-bifunctor-obstruction` (1665), `subsec:concordance-koszulness-xref` (1666), `subsec:concordance-computational-diagnostics` (1667), `subsec:analytic-completion-programme-editorial` (1670), `sec:concordance-arithmetic-sewing` (1671), `constr:prime-side-li` (1753), `sec:genus-all-master` (1775), `subsec:sewing-gram-matrix` (1781), `def:swiss-cheese-W-resolution` (1835), `thm:branch-bv` (1836), `rem:affine-half-space-bv` (1840), `conj:relative-quartic-computation` (1847), `def:relative-holographic-deformation` (1848), `constr:vol2-oc-mc-element` (1857), `thm:vol2-oc-mc-equation` (1858), `conj:globalization` (1859), `conj:boundary-line-generation` (1860), `conj:khan-zeng-comparison` (1861). FIX: delete the entire stub lines.

The exhaustive grouped report, in your requested `[SEVERITY] file:line — PROBLEM: ... FIX: ...` format, is at [vol1_dead_label_audit.md](/tmp/vol1_dead_label_audit.md). The raw per-label inventory is at [vol1_dead_labels_raw.tsv](/tmp/vol1_dead_labels_raw.tsv).

Method: I scanned live Vol I `main.tex`, `chapters/**/*.tex`, and `appendices/**/*.tex`, stripped TeX comments, and counted incoming refs across Vol I/II/III `.tex` sources via `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\Cref`, `\pageref`, and `\hyperref[...]`. I did not edit source.

## Summary
Checked: 129 | Findings: 446 | Verdict: FAIL
tokens used
164,380
