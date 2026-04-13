# F17_dangling_refs_v1 (978s)

- [CRITICAL] chapters/examples/free_fields.tex:5087 — PROBLEM: `thm:bar-cobar-path-integral-heisenberg` has no live label, and line 5098 repeats it inside the proof; the only live target is the conjecture `conj:bar-cobar-path-integral-heisenberg` in `chapters/connections/feynman_connection.tex`, so item `(iii)` of a `\ClaimStatusProvedHere` theorem is being justified by conjectural material. FIX: delete item `(iii)` from `thm:bar-string-integrand`, delete the sentence beginning `Item~(iii) is proved...` from the proof, and reintroduce the free-boson path-integral claim as a post-theorem `remark`/`evidence` paragraph citing `Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg}`.

- [HIGH] chapters/examples/heisenberg_eisenstein.tex:306 — PROBLEM: the proof cites dead `thm:heisenberg-bar-complex-genus0` and then uses `\S\ref{thm:frame-heisenberg-koszul-dual}`, i.e. a section symbol against a theorem label. FIX: replace `(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual})` with `(Theorem~\ref{thm:frame-heisenberg-koszul-dual})`.

- [MEDIUM] chapters/theory/derived_langlands.tex:1515 — PROBLEM: `chap:modular-koszul` is dead. The live enclosing chapter for `thm:shadow-connection` is `chap:higher-genus`. FIX: replace `Chapter~\ref{chap:modular-koszul}` with `Chapter~\ref{chap:higher-genus}`.

- [MEDIUM] chapters/examples/y_algebras.tex:340 — PROBLEM: `prop:heisenberg-kappa` is dead; the sentence is invoking the Heisenberg identity `\kappa(\mathcal H_\kappa)=\kappa`, whose live support is `thm:modular-characteristic` together with `conv:heisenberg-kappa-notation`. FIX: replace `Proposition~\ref{prop:heisenberg-kappa}` with `Theorem~\ref{thm:modular-characteristic} and Convention~\ref{conv:heisenberg-kappa-notation}`.

- [MEDIUM] chapters/examples/lattice_foundations.tex:1714 — PROBLEM: `prop:pixton-genus2-planted-forest` is dead; the explicit genus-2 planted-forest formula is live at `eq:planted-forest-genus2-explicit-bridge` inside `thm:pixton-mc-genus2`. FIX: replace `Proposition~\ref{prop:pixton-genus2-planted-forest}` with `equation~\eqref{eq:planted-forest-genus2-explicit-bridge}`.

- [MEDIUM] chapters/examples/landscape_census.tex:1465 — PROBLEM: `rem:free-field-three-theorems` is dead here and again at line 3978; the live synthesis remark is `rem:free-field-five-theorems`, and the current prose misstates the surface as “three-theorem”. FIX: replace both citations with `Remark~\ref{rem:free-field-five-theorems}` and change `three-theorem synthesis` to `five-theorem verification`.

- [MEDIUM] chapters/examples/landscape_census.tex:1467 — PROBLEM: `rem:w-algebra-three-theorems` is dead here and again at line 4016; the live W-algebra synthesis surface is `sec:w-five-theorems`, not a remark. FIX: replace both citations with `\S\ref{sec:w-five-theorems}` and change `three-theorem synthesis` to `five-theorem verification`.

- [MEDIUM] chapters/examples/y_algebras.tex:640 — PROBLEM: `sec:concordance-three-tier-r-matrix` is dead; the classification being cited lives at `def:three-tier-r-matrix`. FIX: replace `(\S\ref{sec:concordance-three-tier-r-matrix})` with `(Definition~\ref{def:three-tier-r-matrix})`.

- [MEDIUM] chapters/examples/y_algebras.tex:855 — PROBLEM: `sec:concordance-holographic-programme` is dead; the sentence points to the definition of the holographic modular Koszul datum, whose live label is `def:holographic-modular-koszul-datum`. FIX: replace `(\S\ref{sec:concordance-holographic-programme})` with `(Definition~\ref{def:holographic-modular-koszul-datum})`.

- [MEDIUM] chapters/examples/bar_complex_tables.tex:4153 — PROBLEM: `sec:sl3-bar-table` is dead here and again in the caption at line 4198; the live `\widehat{\mathfrak{sl}}_3` cohomology discussion is `sec:sl3-spectral-sequence`. FIX: replace both occurrences with `\S\ref{sec:sl3-spectral-sequence}`; at line 4153 also change `Section ... satisfy` to `Section ... satisfies`.

- [MEDIUM] chapters/connections/outlook.tex:276 — PROBLEM: `thm:hook-type-transport-koszul-duality` is dead; the live result is `thm:hook-transport-corridor`. FIX: replace the citation with `Theorem~\ref{thm:hook-transport-corridor}`.

- [MEDIUM] chapters/examples/yangians_foundations.tex:1228 — PROBLEM: `thm:rtt-all-types` is dead here and again in `chapters/examples/yangians_computations.tex:1150`; the live theorem is `thm:rtt-all-classical-types`. FIX: replace both citations with `Theorem~\ref{thm:rtt-all-classical-types}` and keep `(iv)` on the foundations line.

- [LOW] chapters/theory/higher_genus_modular_koszul.tex:15142 — PROBLEM: the commented line still contains dead `\ref{thm:modular}`. It will not break TeX, but it does poison grep-based audits and future relabeling. FIX: delete `\ref{thm:modular}` from the comment or rewrite the comment without any label reference.

## Summary
Checked: 18 | Findings: 13 | Verdict: FAIL


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
session id: 019d878a-6557-7983-a0bc-23b1d9e2782f
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


MISSION: FOUNDATION AUDIT of chapters/

Find all \ref{} that don't resolve. Run: grep -roh '\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Planning a foundation audit**

I need to respond to the user's request for a foundation audit of chapters and unresolved references. While it seems I might act as a coding agent in the repository, I should follow specific instructions from AGENTS. It’s not clear if any edits are needed, but I might still need to read through some files. Regardless, I’ll likely utilize the deep-beilinson-audit skill for the audit. I might also use explorer agents for assistance with codebase questions, and possibly grep commands for further searches.
thinking
**Focusing on unresolved references**

I need to ensure I’m providing exactly what the user wants regarding findings, specifically looking for every unresolved reference within the chapters directory. The task is to conduct a foundation audit, making findings based on file and line numbers. They suggested using grep commands, and I should only focus on unresolved refs at this point. However, I could also look for related issues nearby. After my initial findings, I’ll dig deeper into any second-order failures that might arise. Ultimately, my priority is addressing the unresolved references as directed.
thinking
**Verifying reference labels**

I need to check if any labels are defined in other directories, like prefaces or appendices, but the user specifically wants to focus on unresolved references within the chapters. My task is to find all instances of \ref{} that don’t resolve, and I’ll run commands strictly limited to chapters. Since every unresolved reference is a finding, I might not count those resolved outside the chapters, even if the final build could recognize them. I’ll prioritize the user's mission and stick to the chapters as the baseline.
codex
Using `deep-beilinson-audit` for this turn because the task is an adversarial audit of manuscript foundations. I’m starting with the exact unresolved-reference surface in `chapters/`, then I’ll verify each hit against actual file contents and inspect nearby context for second-order failures before reporting only grounded findings.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

codex
I’ve loaded the audit workflow and am now grounding it against the repo’s live constitutional surface plus the raw `chapters/` ref/label inventory. Next I’ll inspect each unresolved hit in context rather than trusting the set difference blindly.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 53ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
exec
/bin/zsh -lc "grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sort -u > /tmp/refs.txt && grep -roh '\\\\label{["'^}]*}'"' chapters/ | sort -u > /tmp/labels.txt && comm -23 /tmp/refs.txt /tmp/labels.txt" in /Users/raeez/chiral-bar-cobar succeeded in 263ms:
\ref{D1}
\ref{D2}
\ref{D3}
\ref{D4}
\ref{D5}
\ref{D6}
\ref{D:genus-tower}
\ref{MK:koszul-htpy}
\ref{MK:koszul}
\ref{MK:modular-htpy}
\ref{MK:modular}
\ref{MK:verdier-htpy}
\ref{MK:verdier}
\ref{alg:NAP-koszul}
\ref{app:arnold-relations}
\ref{app:branch-line-reductions}
\ref{app:coderived-models}
\ref{app:coderived}
\ref{app:combinatorial-frontier}
\ref{app:curved-ainfty-formulas}



thinking
**Investigating unresolved references**

I want to focus on checking for unresolved references in the user’s document. To be thorough, I should compare against all labels in the repository to ensure that missing references in chapters aren’t actually in appendices. The user is looking for truly unresolved references at compile time. So, I should inspect both chapter-local references and the full repo label list. Although the user provided a flawed command, my goal is to conduct an audit while perhaps suggesting improvements.
thinking
**Auditing references and definitions**

I need to focus on auditing the chapters for unresolved references while possibly noting any command bugs that lead to false positives. They asked for findings in the manuscript rather than a fix for the command itself. I could capture reference names using regex, but I should remind myself to stick with unresolved references since that's their main concern. I also need to keep an eye on missing definitions, hidden imports, and unjustified steps, but they might not want a completely exhaustive search. I'll look for nearby unresolved references that could be due to stale names.
thinking
**Counting unresolved references**

I need to determine the actual count of unresolved references. To do this, I'll run corrected normalized commands for the chapters only and also check the full repository labels to verify any unresolved references during compilation. Using the shell should help with executing these commands. By comparing the results, I can ensure accuracy in identifying all unresolved references. This approach should provide the clarity I need to help the user effectively.
codex
The raw `comm` command the task specified is not trustworthy as written: it compares literal `\ref{...}` strings to literal `\label{...}` strings, so it marks every reference as “unresolved.” I’m normalizing the keys now and then re-checking against actual source locations so the findings don’t contain false positives.
exec
/bin/zsh -lc "rg -o --no-filename '\\\\ref\\{["'^}]+'"\\}' chapters | sed 's/"'^'"\\\\ref{//; s/}"'$//'"' | sort -u > /tmp/refs_norm.txt
rg -o --no-filename '\\\\label\\{["'^}]+'"\\}' chapters | sed 's/"'^'"\\\\label{//; s/}"'$//'"' | sort -u > /tmp/labels_norm_chapters.txt
comm -23 /tmp/refs_norm.txt /tmp/labels_norm_chapters.txt" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
app:arnold-relations
app:branch-line-reductions
app:coderived-models
app:combinatorial-frontier
app:curved-ainfty-formulas
app:homotopy-transfer
app:koszul-reference
app:nonlinear-modular-shadows
app:sign-conventions
app:signs
app:theta
app:w3-jacobi-full
chap:modular-koszul
comp:bp-shadow-tower
conj:nms-graph-completed-master-element
conj:nms-nonlinear-phase-standard
conj:nms-rank2-isomonodromic
conj:superstring-degeneration
conj:w3-bar-gf
conj:yangian-ordered-center
exec
/bin/zsh -lc "rg -o --no-filename '\\\\label\\{["'^}]+'"\\}' . | sed 's/"'^'"\\\\label{//; s/}"'$//'"' | sort -u > /tmp/labels_norm_all.txt
comm -23 /tmp/refs_norm.txt /tmp/labels_norm_all.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chap:modular-koszul
prop:heisenberg-kappa
prop:pixton-genus2-planted-forest
rem:cubic-source-caveat
rem:free-field-three-theorems
rem:thqg-I-spectral-finiteness
rem:w-algebra-three-theorems
sec:completion-programme-overview
sec:concordance-holographic-programme
sec:concordance-three-tier-r-matrix
sec:sl3-bar-table
thm:bar-cobar-path-integral-heisenberg
thm:heisenberg-bar-complex-genus0
thm:hook-type-transport-koszul-duality
thm:modular
thm:rtt-all-types
codex
I’ve narrowed the true unresolved-reference surface to 16 labels after checking against all labels in the repo, not just `chapters/`. The next pass is source-level: every surviving label gets traced to its exact occurrences, nearby prose, and the most defensible replacement target before I write any finding.
exec
/bin/zsh -lc 'for k in chap:modular-koszul prop:heisenberg-kappa prop:pixton-genus2-planted-forest rem:cubic-source-caveat rem:free-field-three-theorems rem:thqg-I-spectral-finiteness rem:w-algebra-three-theorems sec:completion-programme-overview sec:concordance-holographic-programme sec:concordance-three-tier-r-matrix sec:sl3-bar-table thm:bar-cobar-path-integral-heisenberg thm:heisenberg-bar-complex-genus0 thm:hook-type-transport-koszul-duality thm:modular thm:rtt-all-types; do echo "=== $k ==="; rg -n "'"\\\\\\\\ref\\{"'$k'"\\}\" chapters; done" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
chapters/examples/yangians_foundations.tex:1228:Theorem~\textup{\ref{thm:rtt-all-types}(iv)} likewise operates
chapters/examples/yangians_computations.tex:1150:(Theorem~\ref{thm:rtt-all-types}): the $R$-matrix for

thinking
**Inspecting candidate labels**

I need to check the nearby context and find candidate labels. I can use a tool like `rg` to look for similar label names across the repository. It seems like for every 16, okay, it might make sense. I’ll create a mapping for the candidate label searches using `rg` for label names that contain specific keywords. Additionally, I should examine the line contexts, and maybe I could script something to run each label search across the entire repository for any similar or renamed labels.
exec
/bin/zsh -lc "for pat in 'modular-koszul' 'heisenberg-kappa' 'pixton-genus2' 'cubic-source' 'free-field-three' 'thqg-I-spectral-finiteness' 'w-algebra-three' 'completion-programme-overview' 'concordance-holographic-programme' 'concordance-three-tier-r-matrix' 'sl3-bar-table' 'bar-cobar-path-integral-heisenberg' 'heisenberg-bar-complex-genus0' 'hook-type-transport-koszul-duality' 'thm:modular' 'rtt-all-types'; do echo \"=== "'$pat ==="; rg -n "$pat" .; done' in /Users/raeez/chiral-bar-cobar succeeded in 477ms:
=== free-field-three ===
./chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
./chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).
./audit_campaign_20260412_231034/F08_c_bc.md:521: (Remark~\ref{rem:free-field-three-theorems}).
./relaunch_20260413_111534/F17_dangling_refs_v1.md:23:- [MEDIUM] chapters/examples/landscape_census.tex:1465 — PROBLEM: `\ref{rem:free-field-three-theorems}` has no target; the actual free-field synthesis remark is `\label{rem:free-fields-three-pillar}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
./relaunch_20260413_111534/F17_dangling_refs_v1.md:24:- [MEDIUM] chapters/examples/landscape_census.tex:3978 — PROBLEM: same broken `\ref{rem:free-field-three-theorems}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
./relaunch_20260413_111534/F17_dangling_refs_v1.md:398:rem:free-field-three-theorems
./relaunch_20260413_111534/F17_dangling_refs_v1.md:428:=== rem:free-field-three-theorems ===
./relaunch_20260413_111534/F17_dangling_refs_v1.md:429:chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
./relaunch_20260413_111534/F17_dangling_refs_v1.md:430:chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).
./relaunch_20260413_111534/F17_dangling_refs_v1.md:490:=== rem:free-field-three-theorems ===
./relaunch_20260413_111534/F17_dangling_refs_v1.md:1175:I realize that using `\S` is semantically incorrect, which is great because it helps fix the prefix drift. I should look for other labels that might have the wrong prefixes too. For instance, there’s `sec:landscape-census` versus `ch:landscape-census`. The fix here would be to replace `sec:` with `ch:`, or better yet, cite it as `Chapter\ref{ch:landscape-census}`. I also need to systematically map other labels, like checking if `rem:free-field-three-theorems` corresponds to `rem:free-fields-three-pillar`.
./relaunch_20260413_111534/F17_dangling_refs_v1.md:2021:  rg -n -F '\\ref{rem:free-field-three-theorems}' chapters
./relaunch_20260413_111534/F17_dangling_refs_v1.md:2067:I'm thinking about how to structure my findings. I could use backticks around labels and replacements, like `FIX: replace \`Remark\ref{rem:free-field-three-theorems}\` with \`Remark\ref{rem:free-fields-three-pillar}\``. It seems I also need to include the path and line, ensuring I follow the output contract that specifies using relative paths rather than labels. I should mention that I checked 38, possibly stating: `Checked: 38 | Findings: 38 | Verdict: FAIL`. Let's keep one bullet per finding and ensure to start with bullets since the user wanted findings only. I’ll organize them correctly!
./relaunch_20260413_111534/F17_dangling_refs_v1.md:2089:- [MEDIUM] chapters/examples/landscape_census.tex:1465 — PROBLEM: `\ref{rem:free-field-three-theorems}` has no target; the actual free-field synthesis remark is `\label{rem:free-fields-three-pillar}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
./relaunch_20260413_111534/F17_dangling_refs_v1.md:2090:- [MEDIUM] chapters/examples/landscape_census.tex:3978 — PROBLEM: same broken `\ref{rem:free-field-three-theorems}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
./audit_campaign_20260412_231034/F09_c_bg.md:412: (Remark~\ref{rem:free-field-three-theorems}).
./audit_campaign_20260412_231034/F18_complementarity.md:643:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
./fix_wave_A_20260413_112727/A12_fix_broken_refs_v1_rest.md:442:1 chapters/examples/landscape_census.tex:1465 rem:free-field-three-theorems None nearby
./fix_wave_A_20260413_112727/A12_fix_broken_refs_v1_rest.md:443:2 chapters/examples/landscape_census.tex:3978 rem:free-field-three-theorems None nearby

thinking
**Searching label definitions**

I'm thinking I should search for definitions of these unresolved labels. It might be easier to use a command like `rg -n "\\\\label\\{.*(something)" chapters appendices`. I can handle each label separately, which seems manageable. Maybe I could even set up a small shell loop to process the results efficiently. This way, I can work through each one methodically. Let’s give it a try and see what we uncover!
exec
/bin/zsh -lc "printf '=== chap:modular-koszul ===\\n'; sed -n '1500,1525p' chapters/theory/derived_langlands.tex; rg -n '\\\\label\\{chap:.*modular.*koszul|\\\\label\\{ch:.*modular.*koszul' chapters appendices main.tex
printf '\\n=== prop:heisenberg-kappa ===\\n'; sed -n '330,350p' chapters/examples/y_algebras.tex; rg -n 'heisenberg-kappa|kappa-notation|\\\\label\\{prop:.*heisenberg.*kappa' chapters appendices main.tex
printf '\\n=== prop:pixton-genus2-planted-forest ===\\n'; sed -n '1702,1722p' chapters/examples/lattice_foundations.tex; rg -n 'pixton.*planted|planted.*forest|\\\\label\\{prop:.*pixton' chapters appendices main.tex
printf '\\n=== rem:cubic-source-caveat ===\\n'; sed -n '1830,1850p' chapters/connections/thqg_holographic_reconstruction.tex; rg -n 'cubic-source-caveat|\\\\label\\{rem:.*cubic.*source' chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
=== chap:modular-koszul ===
correspondence~\cite{BD04,FG06}, the bar complex at integral level
occupies a specific position: it is the vertex-algebraic avatar of the
de~Rham side, with the bar differential encoding the flat connection
on the critical-level Hecke eigensheaf, while the Koszul dual
$V_{k^\vee}(\fg^\vee)$ occupies the Betti side.
\end{remark}


\begin{remark}[Shadow connection, opers, and the Hitchin WKB]
\label{rem:shadow-hitchin-wkb}
\index{shadow connection!Hitchin WKB}
\index{oper!indicial roots from shadow data}
\index{WKB approximation!from shadow connection}
The shadow connection
$\nabla^{\mathrm{sh}} = d - Q_L'/(2Q_L)\,dt$
(Chapter~\ref{chap:modular-koszul},
Theorem~\ref{thm:shadow-connection})
specializes to the Knizhnik--Zamolodchikov connection for
affine Kac--Moody algebras and to the BPZ connection for

thinking
**Evaluating labels and conventions**

I need to find the right label for "heisenberg-kappa." It might be more suitable as "conv:heisenberg-kappa-notation" or something related to a theorem. The Heisenberg formula states that the current contributes κ = k, but there's no proposition label present. Since the user is looking for an exact fix, I could suggest replacing it with "Convention\ref{conv:heisenberg-kappa-notation}." I need to check the convention details around line 2168 to make sure it aligns with the modular characteristic.
exec
/bin/zsh -lc "printf '=== conv:heisenberg-kappa-notation context ===\\n'; sed -n '2158,2178p' chapters/theory/higher_genus_foundations.tex
printf '\\n=== possible kappa theorem context ===\\n'; sed -n '2838,2875p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n=== more unresolved set 2 ===\\n'; sed -n '1455,1475p' chapters/examples/landscape_census.tex
sed -n '3968,4025p' chapters/examples/landscape_census.tex
rg -n 'free-field-three-theorems|w-algebra-three-theorems|three-theorems' chapters appendices main.tex
printf '\\n=== rem:thqg-I-spectral-finiteness ===\\n'; sed -n '2092,2112p' chapters/connections/thqg_perturbative_finiteness.tex
rg -n 'spectral-finiteness|thqg-I-spectral' chapters appendices main.tex
printf '\\n=== sec:completion-programme-overview ===\\n'; sed -n '2037,2055p' chapters/connections/thqg_preface_supplement.tex
rg -n '\\\\label\\{sec:.*completion.*programme.*overview|\\\\label\\{sec:.*completion.*program.*overview' chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
=== conv:heisenberg-kappa-notation context ===
of the Yangian \textup{(}Drinfeld~\cite{Drinfeld85}\textup{)}.
The MC equation $d\alpha + \frac{1}{2}[\alpha, \alpha] = 0$
reduces to the classical Yang--Baxter equation
$[r_{12}, r_{13}] + [r_{12}, r_{23}] + [r_{13}, r_{23}] = 0$
for~$r$.
\end{proposition}

\subsubsection{Example: Heisenberg deformation}

\begin{convention}[Heisenberg level notation]
\label{conv:heisenberg-kappa-notation}
We write $\mathcal{H}_\kappa$ for the Heisenberg vertex algebra at
level~$\kappa$, using the same letter as the modular characteristic
to emphasize the identity $\kappa(\mathcal{H}_\kappa) = \kappa$: for
the Heisenberg algebra, the level parameter coincides with the modular
characteristic (Theorem~\textup{\ref{thm:modular-characteristic}}).
\end{convention}

\begin{proposition}[Deforming Heisenberg; \ClaimStatusProvedHere]

thinking
**Troubleshooting output issues**

I’m looking at the rg command that ended with code 1, which could mean there was no match found. It seems like I might need to rerun it for completion labels. The output cuts off at line 2055, so that could indicate a missing section. I’ll need to search for relevant section labels to ensure I don’t miss anything important. Let’s see how I can gather the extra output needed!
codex
I have enough to see the pattern: these are not random missing labels, they are stale names after relabeling, hidden-driver aliases that were never materialized, and one outright bad audit command. I’m now matching each stale name to the live target or proving that no live target exists, so every fix is executable rather than speculative.
exec
/bin/zsh -lc "printf '=== sec:concordance-holographic-programme ===\\n'; sed -n '846,864p' chapters/examples/y_algebras.tex; rg -n 'concordance-holographic-programme|holographic programme|holographic program' chapters/connections/concordance.tex chapters appendices main.tex
printf '\\n=== sec:concordance-three-tier-r-matrix ===\\n'; sed -n '632,648p' chapters/examples/y_algebras.tex; rg -n 'three-tier-r-matrix|three tier r-matrix|r-matrix conventions' chapters/connections/concordance.tex chapters appendices main.tex
printf '\\n=== sec:sl3-bar-table ===\\n'; sed -n '4146,4205p' chapters/examples/bar_complex_tables.tex; rg -n '\\\\label\\{sec:sl3-bar-table\\}|sl3-bar-table|SL_3 bar table|sl3 bar table' chapters/examples/bar_complex_tables.tex chapters appendices main.tex
printf '\\n=== thm:bar-cobar-path-integral-heisenberg ===\\n'; sed -n '5078,5106p' chapters/examples/free_fields.tex; rg -n 'bar-cobar-path-integral-heisenberg|path-integral-heisenberg|path integral.*Heisenberg' chapters appendices main.tex
printf '\\n=== thm:heisenberg-bar-complex-genus0 ===\\n'; sed -n '296,316p' chapters/examples/heisenberg_eisenstein.tex; rg -n 'heisenberg-bar-complex-genus0|heisenberg.*genus0|heisenberg.*bar.*genus' chapters appendices main.tex
printf '\\n=== thm:hook-type-transport-koszul-duality ===\\n'; sed -n '268,284p' chapters/connections/outlook.tex; rg -n 'hook-type-transport-koszul-duality|hook.*transport.*koszul.*duality|transport.*hook.*duality' chapters appendices main.tex
printf '\\n=== thm:modular ===\\n'; sed -n '15132,15150p' chapters/theory/higher_genus_modular_koszul.tex; rg -n '\\\\label\\{thm:modular\\}|Conjecture~\\\\ref\\{thm:modular\\}|Theorem~\\\\ref\\{thm:modular\\}|modular\\}' chapters/theory/higher_genus_modular_koszul.tex chapters appendices main.tex
printf '\\n=== thm:rtt-all-types ===\\n'; sed -n '1142,1160p' chapters/examples/yangians_computations.tex; sed -n '1218,1236p' chapters/examples/yangians_foundations.tex; rg -n 'rtt-all-types|rtt-all-classical-types|RTT presentation and MC3 for all' chapters appendices main.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== sec:concordance-holographic-programme ===
common line $\bC$ in the $4$d $\cN = 4$ holomorphic-topological
theory~\cite{gaiotto-rapchak}. The three gauge groups
$\mathrm{GL}(N_i)$ live on the three half-spaces; the coupling
$\Psi = -\varepsilon_2/\varepsilon_1$ is the ratio of
$\Omega$-background parameters. The $Y$-algebra is the algebra
of local operators supported on the junction line~$\bC$.

In the holomorphic modular Koszul datum
$\cH(T) = (A, A^!, \mathfrak{C}, r(z), \Theta_A, \nabla^{\mathrm{hol}})$
(\S\ref{sec:concordance-holographic-programme}), the junction
origin provides:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $A = Y_{N_1,N_2,N_3}[\Psi]$,
 $A^! = Y_{N_1,N_2,N_3}[-\Psi]$: the boundary and its
 Koszul dual;
\item $r(z)$: the collision residue
 (Computation~\ref{comp:y111-collision-residue}), encoding the
 OPE singularities along the junction line;
\item $\Theta_A$: the universal MC element, with
exec
/bin/zsh -lc "printf '=== free-field / w-algebra three-theorem candidates ===\\n'; rg -n 'three-theorem|three theorems|synthesis' chapters/examples/free_fields.tex chapters/examples/w_algebras.tex
printf '\\n=== free_fields relevant context ===\\n'; sed -n '4300,4385p' chapters/examples/free_fields.tex
printf '\\n=== w_algebras relevant context ===\\n'; sed -n '6600,6685p' chapters/examples/w_algebras.tex
printf '\\n=== thqg-I spectral finiteness candidate context ===\\n'; sed -n '1998,2025p' chapters/connections/thqg_perturbative_finiteness.tex
printf '\\n=== concordance holographic programme nearby headings ===\\n'; sed -n '6650,6715p' chapters/connections/concordance.tex
printf '\\n=== concordance three-tier r-matrix nearby headings ===\\n'; sed -n '1810,1875p' chapters/theory/introduction.tex
printf '\\n=== completion programme label search ===\\n'; rg -n 'completion programme|completion program|analytic completion|completion package|completion overview' chapters/connections/thqg_preface_supplement.tex chapters/connections/*.tex chapters/theory/*.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== free-field / w-algebra three-theorem candidates ===

=== free_fields relevant context ===
give $\vartheta[\delta](0|\Omega) = 0$ (the odd theta
constants vanish at $z = 0$). The GSO-summed genus-$2$
partition function is
\[
Z_2^{\mathrm{GSO}}(\cF)
= \frac{1}{2^4}\sum_{\delta\,\mathrm{even}}
 \vartheta[\delta](0|\Omega)^2,
\]
where the sum runs over the $10$ even characteristics.
This expression is a Siegel modular form of weight $1/2$
for a subgroup of $\mathrm{Sp}_4(\mathbb{Z})$, in
contrast to the Heisenberg genus-$2$ partition function
$Z_2(\cH_\kappa) = (\det \mathrm{Im}\,\Omega)^{-1/2}$
\textup{(}Computation~\textup{\ref{comp:partition-genus-two})},
which transforms under the full $\mathrm{Sp}_4(\mathbb{Z})$.
\end{remark}


thinking
**Inspecting analytic completion labels**

I need to take a closer look at the concordance around the analytic completion section to check if there’s a missing label. It seems like `sec:completion-programme-overview` was possibly meant to refer to `\subsection{The analytic completion programme}`, but it might not be labeled correctly. I'll read around entry 5257 to confirm if the label exists. It's important to clarify this for accuracy!
exec
/bin/zsh -lc "printf '=== concordance analytic completion section ===\\n'; sed -n '5248,5270p' chapters/connections/concordance.tex
printf '\\n=== free_fields maybe missing remark later? ===\\n'; rg -n 'free field.*three|three theorems in action|free-field' chapters/examples/free_fields.tex
printf '\\n=== w_algebras maybe missing remark later? ===\\n'; rg -n 'w-algebra.*three|three theorems in action|three theorems' chapters/examples/w_algebras.tex
printf '\\n=== sec:completion-programme-overview similar labels ===\\n'; rg -n '\\\\label\\{sec:.*completion|\\\\label\\{subsec:.*completion' chapters/connections/concordance.tex chapters/connections/genus_complete.tex chapters/connections/thqg_introduction_supplement_body.tex chapters/connections/editorial_constitution.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== concordance analytic completion section ===
finite-stage chiral Koszul duality to an equivalence between the
completion closure of admissible chiral $A_\infty$-algebras on curves
and the homotopy theory of complete pronilpotent modular cumulant
coalgebras, with genus-$0$ truncation $=$ completed bar/cobar,
ordered-boundary truncation $=$ dg-shifted Yangian jet tower, and
universal deformation theory $=$ graph MC
class~$\Theta_\cA$.
\end{conjecture}

\subsection{The analytic completion programme}
\label{subsec:analytic-completion-programme}
\index{analytic completion!programme}

The proved algebraic engine operates in the world of formal
factorization algebras, cochain complexes, and dg categories. A
genuine local-to-global field theory also requires analytic sewing
(convergent partition functions, Hilbert-space completions, and
positivity). Recent work of
Moriwaki~\cite{Moriwaki26a, Moriwaki26b} constructs conformally flat

thinking
**Searching for algebra remarks**

I think there might be a missing label in the remark regarding free-field and w-algebra, specifically the three-theorems. I should search for something like `rem:free-field-five-theorems`, as that could be what’s intended. I’ll look around that remark and also check for any equivalent in w-algebra. Maybe I’ll find an analogous remark like `rem:w-five-theorems` in my search. Time to dig into this!
exec
/bin/zsh -lc "printf '=== free-field five-theorems context ===\\n'; sed -n '5428,5450p' chapters/examples/free_fields.tex
printf '\\n=== w-algebras theorem synthesis search ===\\n'; rg -n 'five projections|five main theorems|three theorems|Theta_\\\\cA|synthesis' chapters/examples/w_algebras.tex
printf '\\n=== w-algebras relevant end-context ===\\n'; sed -n '7080,7165p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
=== free-field five-theorems context ===

\subsection{Comparison of free-field examples}

Geometric complexity correlates inversely with algebraic simplicity: the free fermion (one generator) vanishes above degree~$1$; the $\beta\gamma$ system grows as $2 \cdot 3^{n-1}$; the Heisenberg gains a central charge class; the Virasoro connects to $\overline{\mathcal{M}}_{0,n}$; W-algebras link to flag varieties.

\begin{remark}[Five projections of $\Theta_\cA$: free-field archetypes]
\label{rem:free-field-five-theorems}
\index{main theorems!free field verification}
\index{Chriss--Ginzburg structure principle!free fields}
Each free-field archetype verifies all five main theorems as projections
of the universal MC element
$\Theta_\cA \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}). The verification tables below
organize the proved data per family; the shadow archetype column
refers to the classification of
Table~\ref{tab:shadow-tower-census}.
\end{remark}

\subsubsection{Heisenberg: five-theorem verification}

thinking
**Investigating relevant sections**

I’m not seeing anything obvious in the w_algebras, so I think I should search around section 2702 for possible relevant details. It might be a good idea to inspect the text in the range of 2690 to 2725. I wonder if something important is more hidden there. Getting all the context will help in understanding things better. Let’s see what we can find in that section!
exec
/bin/zsh -lc "sed -n '2688,2722p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa \mapsto \kappa^!$, the quartic contact class
$Q^{\mathrm{contact}} \mapsto Q^{\mathrm{contact},!}$,
and the shadow metric $Q_L \mapsto Q_{L^!}$, with the
complementarity structure of Theorem~D controlling the
duality at every degree. The entire Koszul pair
$(\mathcal{W}^k(\mathfrak{g}),
\mathcal{W}^{k^\vee}({}^L\mathfrak{g}))$ is
a shadow-level realization of gauge-theoretic S-duality.
\end{remark}


\section{The five theorems for $\mathcal{W}$-algebras}
\label{sec:w-five-theorems}

The five main theorems of Part~\ref{part:bar-complex} specialize to $\mathcal{W}$-algebras
through DS reduction from the affine Kac--Moody package. We record
the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
$\mathcal{W}_3$ in a verification table, then state the general
$\mathcal{W}_N$ pattern.

exec
/bin/zsh -lc "sed -n '3968,4023p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Locating the computations]\label{rem:cross-ref-guide}
Each row of the Master Table~\textup{\ref{tab:master-invariants}} is
computed in the following locations.
\begin{enumerate}
\item \emph{Free fermion}:
 bar complex (Theorem~\ref{thm:fermion-bar-coalg}),
 Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$
 (Theorem~\ref{thm:betagamma-bc-koszul}),
 $\kappa = \tfrac{1}{4}$ (Table~\ref{tab:master-invariants}),
 three-theorem synthesis
 (Remark~\ref{rem:free-field-three-theorems}).
\item \emph{$bc$--$\beta\gamma$}:
 bar complex (Theorem~\ref{thm:betagamma-bar-complex}),
 Koszul duality
 (Proposition~\ref{prop:bc-betagamma-orthogonality},
 Theorem~\ref{thm:betagamma-bc-koszul}),
 central charge (Theorem~\ref{thm:betagamma-bc-koszul}),
 detailed computation (\S\ref{sec:betagamma-koszul-dual}).
\item \emph{Heisenberg}:
 bar complex (Theorem~\ref{thm:heisenberg-bar}),

thinking
**Updating references and definitions**

I should fix the reference to `sec:w-five-theorems` and change the wording to "five-theorem verification." First, I’ll check if `sec:w-five-theorems` exists. The reference for `sec:concordance-three-tier-r-matrix` should probably be `def:three-tier-r-matrix` in the introduction because it’s not a section. In the y_algebras line, it says it’s derived from a definition, so I need to adjust it from section to definition. I may also look for a relevant subsection in concordance.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(sec|subsec|def|rem|thm):.*(holographic|datum|holomorphic-modular)' chapters/examples/y_algebras.tex chapters/connections/concordance.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/thqg_holographic_reconstruction.tex chapters/theory/introduction.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_holographic_reconstruction.tex:5:\label{sec:thqg-holographic-reconstruction}
chapters/connections/thqg_holographic_reconstruction.tex:359:\label{def:shadow-depth-holographic}
chapters/connections/thqg_holographic_reconstruction.tex:1557:\label{rem:operadic-complexity-holographic}
chapters/connections/thqg_holographic_reconstruction.tex:1731:\label{subsec:holographic-synthesis}
chapters/connections/thqg_holographic_reconstruction.tex:1736:\label{thm:holographic-reconstruction}
main.tex:1577: \phantomsection\label{def:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
main.tex:1581: \phantomsection\label{subsec:concordance-holographic-completion}% % concordance.tex
main.tex:1598: \phantomsection\label{def:thqg-holographic-datum}%
main.tex:1603: \phantomsection\label{subsec:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
main.tex:1605: \phantomsection\label{thm:complementarity-root-datum}% % genus_expansions.tex
main.tex:1691: \phantomsection\label{thm:volume-one-concrete-modular-datum}%
main.tex:1747: \phantomsection\label{def:genus1-modular-datum}%
main.tex:1854: \phantomsection\label{def:relative-holographic-deformation}%
chapters/connections/frontier_modular_holography_platonic.tex:103:\label{subsec:frontier-protected-holographic-transform}
chapters/connections/frontier_modular_holography_platonic.tex:106:\label{def:frontier-protected-holographic-transform}
chapters/connections/frontier_modular_holography_platonic.tex:1122:\label{subsec:holographic-modular-koszul-datum}
chapters/connections/frontier_modular_holography_platonic.tex:1147:\label{def:holographic-modular-koszul-datum}
chapters/connections/frontier_modular_holography_platonic.tex:1238:\label{rem:holographic-cumulant-comparison}
chapters/connections/frontier_modular_holography_platonic.tex:3996:\label{subsec:relative-holographic-deformation}%
chapters/connections/frontier_modular_holography_platonic.tex:4001:\label{def:holographic-forgetful}%
exec
/bin/zsh -lc "sed -n '848,862p' chapters/examples/y_algebras.tex
sed -n '1138,1160p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathrm{GL}(N_i)$ live on the three half-spaces; the coupling
$\Psi = -\varepsilon_2/\varepsilon_1$ is the ratio of
$\Omega$-background parameters. The $Y$-algebra is the algebra
of local operators supported on the junction line~$\bC$.

In the holomorphic modular Koszul datum
$\cH(T) = (A, A^!, \mathfrak{C}, r(z), \Theta_A, \nabla^{\mathrm{hol}})$
(\S\ref{sec:concordance-holographic-programme}), the junction
origin provides:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item $A = Y_{N_1,N_2,N_3}[\Psi]$,
 $A^! = Y_{N_1,N_2,N_3}[-\Psi]$: the boundary and its
 Koszul dual;
\item $r(z)$: the collision residue
 (Computation~\ref{comp:y111-collision-residue}), encoding the
literature (Costello--Dimofte--Gaiotto~\cite{CDG20},
Dimofte--Niu--Py~\cite{DNP25}, Gaiotto--Zeng~\cite{GZ26},
Khan--Zeng~\cite{KhanZeng25}, and
Latyntsev~\cite{Latyntsev23}) identifies the six components of the
holographic datum below. The content of the present subsection is that
exec
/bin/zsh -lc "sed -n '2028,2065p' chapters/connections/thqg_preface_supplement.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Perturbative finiteness
 & Theorem~\ref{thm:general-hs-sewing}
 & HS-sewing for standard landscape \\[2pt]
$G/L/C/M$ classes
 & \S\ref{subsec:shadow-postnikov-tower-intro}
 & shadow depth classification \\[2pt]
$S$-duality
 & Theorem C
 & complementarity / Lagrangian \\[2pt]
Gravitational Yangian
 & Chapter~\ref{chap:yangians}
 & Arnold $\Rightarrow$ CYBE \\[2pt]
Soft theorems
 & \S\ref{def:modular-shadow-connection}
 & shadow connection Ward identities \\[2pt]
Modular bootstrap
 & \S\ref{sec:genus-spectral-sequence}
 & genus spectral sequence \\[2pt]
Critical-string dichotomy
 & \S\ref{sec:completion-programme-overview}

thinking
**Searching for critical concepts**

I need to find the section that covers critical-string dichotomy or transgression algebra. I’ll think about the best search terms to use for this. It’s really important to ensure that I’m pinpointing the right concepts so that I can provide accurate information. I wonder if there are key phrases or definitions that will help narrow down the search effectively. Alright, let’s get started on locating this information!
exec
/bin/zsh -lc "rg -n 'transgression algebra|critical-string dichotomy|completion programme overview|analytic completion programme|completion kinematics programme' chapters/connections/concordance.tex chapters/connections/thqg_preface_supplement.tex chapters/connections/editorial_constitution.tex chapters/connections/genus_complete.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_gravitational_s_duality.tex:2579:$\cA^{\mathrm{sew}}$ (via the analytic completion programme of
chapters/connections/thqg_entanglement_programme.tex:652:and the analytic completion programme.
chapters/connections/thqg_preface_supplement.tex:1773:\subsection*{The critical-string dichotomy}
chapters/connections/thqg_preface_supplement.tex:1776:\subsubsection*{The transgression algebra}
chapters/connections/thqg_preface_supplement.tex:1788:The \emph{transgression algebra} of $\mathrm{Vir}_c$ at genus~$g$
chapters/connections/thqg_preface_supplement.tex:1798:the transgression algebra degenerates to the exterior extension
chapters/connections/thqg_preface_supplement.tex:1801:transgression algebra is a genuine Clifford extension.
chapters/connections/thqg_preface_supplement.tex:1803:The critical-string dichotomy:
chapters/connections/thqg_preface_supplement.tex:1812: transgression algebra is a Clifford extension with
chapters/connections/thqg_preface_supplement.tex:1818:the transgression algebra (which is strict at $c=0$, the Koszul
chapters/connections/thqg_preface_supplement.tex:1885:\cA_{\mathrm{defect}})$, and the transgression algebra acquires
chapters/connections/thqg_preface_supplement.tex:1901:algebra. The critical-string dichotomy extends: at $c=26$ the
chapters/connections/thqg_preface_supplement.tex:2048: & transgression algebra
chapters/connections/thqg_critical_string_dichotomy.tex:8:\index{transgression algebra|textbf}
chapters/connections/thqg_critical_string_dichotomy.tex:27:the transgression algebra $B_\Theta$ is the universal solution to the
chapters/connections/thqg_critical_string_dichotomy.tex:48:\subsection{The transgression algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:50:\index{transgression algebra!construction|textbf}
chapters/connections/thqg_critical_string_dichotomy.tex:83:\index{transgression algebra!definition|textbf}
chapters/connections/thqg_critical_string_dichotomy.tex:93:\emph{curvature}). The \emph{transgression algebra} of the pair
chapters/connections/thqg_critical_string_dichotomy.tex:127:\index{transgression algebra!kills curvature}

thinking
**Investigating critical-string dichotomy**

I think the critical-string dichotomy is likely a local subsection within the same file, although it might be unlabeled. It seems that the reference line 2047 should connect to chapter or file `chap:thqg-critical-string-dichotomy`. I'll take a moment to search for that label and confirm its placement. It's important to get the correct reference to ensure clarity in the discussion of this topic!
exec
/bin/zsh -lc "rg -n '\\\\label\\{.*critical-string.*dichotomy|\\\\label\\{chap:.*critical.*string|\\\\label\\{sec:.*critical.*string|\\\\label\\{subsec:.*transgression|\\\\label\\{.*transgression.*algebra' chapters/connections/thqg_critical_string_dichotomy.tex chapters/connections/*.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_critical_string_dichotomy.tex:5:\label{sec:thqg-critical-string-dichotomy}
chapters/connections/thqg_critical_string_dichotomy.tex:49:\label{subsec:transgression-algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:82:\label{def:transgression-algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:1040:\label{thm:critical-string-dichotomy}
chapters/connections/thqg_introduction_supplement_body.tex:1493:\label{subsec:thqg-intro-ahat-transgression}
chapters/connections/thqg_critical_string_dichotomy.tex:5:\label{sec:thqg-critical-string-dichotomy}
chapters/connections/thqg_critical_string_dichotomy.tex:49:\label{subsec:transgression-algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:82:\label{def:transgression-algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:1040:\label{thm:critical-string-dichotomy}
exec
/bin/zsh -lc "rg -n '\\\\label\\{.*sl3.*(bar|table)|sl3.*degree|sl3.*bar' chapters/examples/bar_complex_tables.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
176:\begin{computation}[\texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential]\label{comp:sl3-bar}
568:\label{sec:sl3-degree3-details}
570:\index{sl3-hat@$\widehat{\mathfrak{sl}}_3$!degree-3 bar complex}
573:Computation~\ref{comp:sl3-bar}. The full degree-3
577:\label{comp:sl3-degree3-complete}
578:\index{bar complex!sl3@$\mathfrak{sl}_3$!degree 3}
676:Using the degree-2 differential from Computation~\ref{comp:sl3-bar}:
735:Computation~\ref{comp:sl3-degree3-complete} confirms that these
750:bar complex]\label{comp:sl3-dim-table}
932:and~\ref{comp:sl3-chiral-bracket-os}) becomes unwieldy beyond degree~$4$.
965: Computation~\ref{comp:sl3-degree3-complete}, where Serre relations
1393:(Computation~\ref{comp:sl3-degree3-complete}). The bar element is:
4153:Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
4198:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
4519:(Computation~\ref{comp:sl3-bar})
4531:(Computation~\ref{comp:sl3-bar}).
4555:(Computation~\ref{comp:sl3-bar}):
exec
/bin/zsh -lc "sed -n '740,770p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The Feigin--Frenkel theorem (Theorem~\ref{thm:critical-level-structure})
identifies $Z(\widehat{\mathfrak{sl}}_{3,-3})$ with a polynomial algebra
in two generators (degrees $2$ and $3$, corresponding to the fundamental
invariants of the Langlands dual $\mathfrak{sl}_3^\vee$). The degree-2
generator corresponds to the Casimir class in $H^2(\bar{B})$; the
degree-3 class arising from the Serre relations corresponds to the
cubic invariant.
\end{proof}

\begin{computation}[Dimension table for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3}
bar complex]\label{comp:sl3-dim-table}
\index{bar complex!dimension table!sl3@$\mathfrak{sl}_3$}
The dimensions of the bar complex components $\bar{B}^n = \mathfrak{sl}_3^{\otimes n}
\otimes \Omega^{n-1}(\overline{\mathrm{Conf}}_n)$ through degree~5:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{c|ccc|c}
$n$ & $\dim(\mathfrak{sl}_3^{\otimes n})$ &
$\dim \Omega^{n-1}(\overline{\mathrm{Conf}}_n)$ &
$\dim \bar{B}^n$ & Generating relations \\

thinking
**Searching cohomology dimensions**

I’m wondering if the series of numbers `[1,8,36,204,1352,...]` could represent cohomology dimensions. It’s possible, but I want to check further. I think it’s essential to search specifically for those numbers to see what connections I can find. I'll dig into the properties or theories that might relate to them, ensuring I gather any relevant information that could clarify their significance. That might be a fruitful path to explore!
exec
/bin/zsh -lc "rg -n '\\[1, 8, 36, 204, 1352|1, 8, 36, 204, 1352|1352' chapters/examples/bar_complex_tables.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:1011:The bar cohomology dimensions $H^n = [1, 8, 36, 204, 1352, \ldots]$
chapters/examples/bar_complex_tables.tex:1094:conjectured bar cohomology sequence $1, 8, 36, 204, 1352, 9892, \ldots$
chapters/examples/bar_complex_tables.tex:1102:and a non-trivial consistency check on $H^4 = 1352$.
chapters/examples/bar_complex_tables.tex:1123:$H^n = [1, 8, 36, 204, 1352, \ldots]$.
chapters/examples/bar_complex_tables.tex:1195:$H^n = [1, 8, 36, 204, 1352, \ldots]$. The actual chiral bar
chapters/examples/bar_complex_tables.tex:4152:$[1, 8, 36, 204, 1352, 9892, \ldots]$ of
chapters/examples/bar_complex_tables.tex:4193:$[1, 8, 36, 204, 1352, \ldots]$ &
chapters/examples/bar_complex_tables.tex:1011:The bar cohomology dimensions $H^n = [1, 8, 36, 204, 1352, \ldots]$
chapters/examples/bar_complex_tables.tex:1094:conjectured bar cohomology sequence $1, 8, 36, 204, 1352, 9892, \ldots$
chapters/examples/bar_complex_tables.tex:1102:and a non-trivial consistency check on $H^4 = 1352$.
chapters/examples/bar_complex_tables.tex:1123:$H^n = [1, 8, 36, 204, 1352, \ldots]$.
chapters/examples/bar_complex_tables.tex:1195:$H^n = [1, 8, 36, 204, 1352, \ldots]$. The actual chiral bar
chapters/examples/bar_complex_tables.tex:4152:$[1, 8, 36, 204, 1352, 9892, \ldots]$ of
chapters/examples/bar_complex_tables.tex:4193:$[1, 8, 36, 204, 1352, \ldots]$ &
chapters/examples/landscape_census.tex:1918: & 8 & 36 & 204 & 1352$^\dagger$ & 9892$^\dagger$ & 76084$^\dagger$ & 598592$^\dagger$ & 4755444$^\dagger$ & $8^n$ \\
chapters/examples/landscape_census.tex:2615: $\dim H^4 = 1352$, $\dim H^5 = 9892$, $\dim H^6 = 76084$,
chapters/examples/landscape_census.tex:2634:\emph{Scope.} Independent verification requires computing $\dim H^4(\barBgeom(\widehat{\mathfrak{sl}}_{3,k}))$ directly from the chiral bar differential. The value $1352$ would confirm the recurrence~\eqref{eq:sl3-bar-recurrence} and the rationality of the GF, while any other value would rule out this rational form.
chapters/examples/landscape_census.tex:2636:The degree-$4$ chain group has dimension $\dim \bar{B}^4 = (\dim\mathfrak{sl}_3)^4 \cdot 3! = 24576$, and the chiral bracket differential $d\colon \bar{B}^4 \to \bar{B}^3$ maps into the $1024$-dimensional space $\bar{B}^3$. The bracket differential at degree~$4 \to 3$ has been verified computationally to be \emph{surjective} (rank~$1024$; Computation~\ref{comp:sl3-modular-rank}). The independent verification of $\dim H^4 = 1352$ therefore reduces to computing $\dim\ker(d^{4 \to 3}) - \dim\operatorname{im}(d^{5 \to 4})$, where the first term equals $24576 - 1024 = 23552$ (by surjectivity) and the second requires the rank of the degree-$5$ differential on the $786432$-dimensional chain group $\bar{B}^5 = 8^5 \cdot 4! = 786432$. This rank computation is feasible via modular arithmetic over $\mathbb{F}_p$ for suitable primes~$p$.
chapters/theory/computational_methods.tex:776:$\AffKM{sl}_3$ & $8,36,204,\mathbf{1352}$
chapters/theory/computational_methods.tex:1033:$H^4(\barBch(\AffKM{sl}_3)) = 1352$. Conjectured.

thinking
**Checking candidate labels**

I think I need to examine the area around 1011 for a potential candidate label. It might make sense to also check around 1000 for a section label. So, I’ll focus on inspecting the range from 1000 to 1020 to see if anything stands out. It seems like organizing these labels might help clarify things as I move forward. Let’s see what I can find in that section!
exec
/bin/zsh -lc "sed -n '1000,1025p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The resolution is that the PBW spectral sequence of
Theorem~\ref{thm:pbw-koszulness-criterion} proves acyclicity
of the \emph{Koszul complex} $K = \barB(A) \otimes_\tau A$,
not the bar complex $\barB(A)$ itself. The $E_1^{p,0}$ terms
are invariants in the symmetric algebra filtration of the
Koszul complex, and the convergence
$E_\infty \Rightarrow H^*(K)$ gives the Koszul criterion
$H^*(K) = \Bbbk$ (acyclicity), not the bar cohomology
$H^*(\barB(A))$ directly.

The bar cohomology dimensions $H^n = [1, 8, 36, 204, 1352, \ldots]$
are instead computed from the Koszul acyclicity via the Hilbert
series inversion $H_A(t) \cdot H_{A^!}(-t) = 1$, using the
Koszul dual Hilbert series
$H_{A^!}(t) = \sum_n \dim(A^!)_n \, t^n$.
The direct spectral sequence approach to $H^*(\barB(A))$
requires the \emph{Chevalley--Eilenberg cohomology of the
loop algebra} $H^*(\mathfrak{g}^-; \Bbbk)$, computed in
\texttt{ce\_cohomology\_loop.py}:
exec
/bin/zsh -lc "sed -n '1086,1130p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Koszul dual dimensions from bar cohomology]
\label{rem:sl3-koszul-dual}
\index{Koszul dual!sl3@$\mathfrak{sl}_3$}

Formal series inversion $H_A(t) \cdot H_{A^!}(-t) = 1$
(which is equivalent to Koszulness when it holds; here applied as a
consistency device to conjectured data) applied to the
conjectured bar cohomology sequence $1, 8, 36, 204, 1352, 9892, \ldots$
yields putative Koszul dual dimensions
$(A^!)_n = 1, 8, 28, 140, 392, \ldots$.
The ``chiral excess'' $(A^!)_n - \dim \Lambda^n(\mathfrak{g}^*)$ is
$0, 0, 0, 84, 322, \ldots$, measuring the departure of the chiral
Koszul dual from the classical exterior algebra. Positivity of the
Koszul dual dimensions through degree~$7$ (verified computationally)
is a necessary condition for the conjectured generating function
and a non-trivial consistency check on $H^4 = 1352$.

The excess~$84$ at degree~$3$ also appears as the gap between the
chiral bar cohomology and the closest quadratic approximation
exec
/bin/zsh -lc "sed -n '1188,1210p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(vacuum module dimensions $1, 8, 44, 192, \ldots$).
At weight~$2$: $\chi_2 = -44 + 64 = 20$, consistent.
At weight~$3$: $\chi_3 = -192 + 704 - 1024 = -512$, requiring
$H^3_3 \geq 512 > 204 = H^3$. \emph{Inconsistent}.

\medskip
Neither model reproduces the bar cohomology
$H^n = [1, 8, 36, 204, 1352, \ldots]$. The actual chiral bar
complex involves the full Borcherds product (including higher
residues), and its chain structure differs from both naive
models. This is a \emph{chain-level} manifestation of the
$R^{(1)}$ barrier: the curvature corrections modify not only the
differential but the effective chain space itself.
\end{remark}


\section{\texorpdfstring{Non-simply-laced example:
$\widehat{\mathfrak{so}}_5$ (type $B_2$)}{Non-simply-laced example:
so-5 (type B-2)}}
\label{sec:B2-details}

thinking
**Determining label placement**

I think I might not have a good candidate for adding the missing label `\label{sec:sl3-bar-table}`. I need to identify the best location to place it. The phrase "Section\ref{sec:sl3-bar-table} satisfies a quadratic recursion" and the caption refer to the earlier SL3 analysis, but adding the label to `\begin{computation}[Dimension table...]` might not fit. It seems better to put it in a subsection or section focused on SL3 discussions. I'll look around the start of earlier sections for the best fit.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\(section|subsection|subsubsection)\\{' chapters/examples/bar_complex_tables.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
14:\section{Heisenberg computations}
17:\subsection{Bar complex: degrees 3 and 4}
90:\subsection{Twisting morphism verification}
139:\section{Kac--Moody computations}
203:\subsection{Acyclicity verification}
243:\section{$\mathcal{W}$-algebra computations}
246:\subsection{Virasoro bar complex through degree 3}
405:\subsection{\texorpdfstring{$\mathcal{W}_3$ bar complex: degree-2 computation}{W-3 bar complex: degree-2 computation}}
567:\section{\texorpdfstring{$\widehat{\mathfrak{sl}}_3$ bar complex: degree-3 Serre relations}{sl-3 bar complex: degree-3 Serre relations}}
794:\subsection{Weight-decomposed modular rank}
925:\subsection{\texorpdfstring{$\widehat{\mathfrak{sl}}_3$ bar cohomology: spectral sequence approach}{sl-3 bar cohomology: spectral sequence approach}}
1204:\section{\texorpdfstring{Non-simply-laced example:
1221:\subsection{Root system and structure constants}
1283:\subsection{Bar differential}
1478:\section{Geometric-algebraic bar comparison}
1494:\subsection{Setup: two bar complexes}
1581:\subsection{Degree 3: Arnold relations and the Jacobi identity}
1647:\subsection{\texorpdfstring{Explicit matrices for $\mathfrak{sl}_2$}{Explicit matrices for sl2}}
2010:\section{\texorpdfstring{BGG resolution of $\widehat{\mathfrak{sl}}_2$ via bar
2031:\subsection{Setup and weight decomposition}
exec
/bin/zsh -lc "sed -n '920,950p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
with entries determined by the $\mathfrak{sl}_3$ structure constants
and the OS residue map combinatorics.
\end{computation}


\subsection{\texorpdfstring{$\widehat{\mathfrak{sl}}_3$ bar cohomology: spectral sequence approach}{sl-3 bar cohomology: spectral sequence approach}}
\label{sec:sl3-spectral-sequence}
\index{sl3-hat@$\widehat{\mathfrak{sl}}_3$!spectral sequence}
\index{PBW spectral sequence!sl3@$\mathfrak{sl}_3$}

The direct computation of bar cohomology via matrix ranks
(Computations~\ref{comp:sl3-modular-rank}
and~\ref{comp:sl3-chiral-bracket-os}) becomes unwieldy beyond degree~$4$.
The PBW spectral sequence of Theorem~\ref{thm:pbw-koszulness-criterion}
provides a more systematic approach.

\begin{proposition}[PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3};
\ClaimStatusProvedHere]
\label{prop:sl3-pbw-ss}
The PBW filtration on the bar complex of $\widehat{\mathfrak{sl}}_{3,k}$ at

thinking
**Considering code adjustments**

I think the best fix might be to change `sec:sl3-bar-table` to `sec:sl3-spectral-sequence` since that subsection is the one discussing the bar cohomology sequence. However, line 4152 mentions dimensions that satisfy a quadratic recursion, which I might need to look at later in this subsection. It seems like I should search within `sec:sl3-spectral-sequence` for references to recursion to get a better understanding.
exec
/bin/zsh -lc "rg -n 'quadratic recursion|characteristic polynomial|sqrt\\{13\\}|sl3-bar-recurrence' chapters/examples/bar_complex_tables.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4153:Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
4154:characteristic polynomial whose discriminant involves $\sqrt{13}$:
4155:the dominant singularity sits at $x_* = (-3 + \sqrt{13})/2$,
4156:giving asymptotic growth $((3 + \sqrt{13})/2)^n \approx (3.303)^n$.
4194:$((3{+}\sqrt{13})/2)^n$ &
4198:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
4214:$1 - 3x - x^2$, and the dominant root $(3 + \sqrt{13})/2$ strictly

thinking
**Considering proof status**

I’m realizing there’s a larger issue here: it seems the theorem is treating a conjecture as a theorem in the proof, which isn’t just an unresolved reference, it's inflating proof status. Since the user specifically asked about every unjustified step, I need to look into that. I’ll also need to read the surrounding lines to understand the theorem’s context and claim status, particularly around the 5050. There’s a lot to unpack here!
exec
/bin/zsh -lc "sed -n '5048,5108p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where $G$ is the bulk-to-boundary propagator and
$\Phi_{\mathrm{grav}}$ is the graviton field. This is
conjecturally modeled using the curved Koszul pairing with
$m_0 = c/24N$.
\end{example}

\begin{remark}[Scope]
Theorem~\ref{thm:genus-deformation-exact} is proved; the residual conjecture is
$\hbar = g_s = 1/N$, which requires AdS/CFT.

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~IV
(trace/index). The identification $\hbar = g_s$ asserts that the
genus expansion parameter is the image of the universal deformation
object under a trace functor.
\end{remark}


\subsection{String amplitudes via bar complex}

\begin{theorem}[Bar classes on moduli and boundary factorization;

thinking
**Evaluating theorem adjustments**

I need to address item iii in the theorem since it’s justified by an unresolved theorem, and I’m thinking of downgrading it. Since item iii isn’t proved here, I might consider splitting it into a remark or simply replacing the theorem with a proposition that only includes items i and ii. The user asks for an exact fix, so maybe I should propose moving item iii to a remark after the proof, citing relevant conjectures. Let's check `feynman_connection.tex` for those conjectures.
exec
/bin/zsh -lc "sed -n '130,170p' chapters/connections/feynman_connection.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is the scalar trace
$\kappa(\cA)\cdot\deg(\lambda_1) = \kappa(\cA)/24$
(Theorems~\ref{thm:genus-universality}
and~\ref{thm:explicit-theta}).

\section{Path integral = bar complex}

\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
\textup{(}free boson at nonzero Heisenberg level\textup{)} on a
compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
\begin{equation}\label{eq:bar-partition-heisenberg}
Z_g^{\mathcal{H}_{\kappa^{\mathrm{Heis}}}}(\Sigma_g)
= H^0(\bar{B}^{(g)}(\mathcal{H}_{\kappa^{\mathrm{Heis}}})) = \mathbb{C}
\end{equation}
\begin{equation}\label{eq:bar-npoint-heisenberg}
\langle \alpha(z_1) \cdots \alpha(z_n) \rangle_{\Sigma_g}
= H^n(\bar{B}^{(g)}(\mathcal{H}_{\kappa^{\mathrm{Heis}}}))
/ H^0(\bar{B}^{(g)}(\mathcal{H}_{\kappa^{\mathrm{Heis}}}))
\end{equation}

thinking
**Classifying theorem severity**

I'm trying to clarify the situation regarding the conjecture and theorem status. It looks like item iii is unsupported, which I believe should be classified as CRITICAL or HIGH severity. But wait, the user asked only for the unresolved reference. This unresolved reference highlights a proof-after-conjecture step that might not be justified. Additionally, there's confusion about the theorem label for the Heisenberg bar complex. I need to look into the context related to it, especially concerning genus-0 and the symmetric algebra. Let's search for the correct label names.
exec
/bin/zsh -lc "rg -n 'frame-heisenberg-bar|heisenberg-bar-complex-genus0|Heisenberg bar complex at genus|symmetric chiral algebra on the dual space' chapters/frame/heisenberg_frame.tex chapters/examples/heisenberg_eisenstein.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:49:The Heisenberg bar complex at genus~$0$
chapters/examples/heisenberg_eisenstein.tex:296:is the symmetric chiral algebra on the dual space, with
chapters/examples/heisenberg_eisenstein.tex:305:is the symmetric chiral algebra on the dual space
chapters/examples/heisenberg_eisenstein.tex:306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
chapters/frame/heisenberg_frame.tex:883:\begin{theorem}[Heisenberg bar complex at genus~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
chapters/frame/heisenberg_frame.tex:884:\label{thm:frame-heisenberg-bar}
chapters/frame/heisenberg_frame.tex:886:\begin{equation}\label{eq:frame-heisenberg-bar-cohomology}
chapters/frame/heisenberg_frame.tex:1042:Theorem~\ref{thm:frame-heisenberg-bar} (concentrated in
chapters/frame/heisenberg_frame.tex:1235:bar concentration (Theorem~\ref{thm:frame-heisenberg-bar}).
chapters/frame/heisenberg_frame.tex:1292:(Theorem~\ref{thm:frame-heisenberg-bar}); the cobar functor
chapters/frame/heisenberg_frame.tex:2208:(Theorem~\ref{thm:frame-heisenberg-bar}); the degree-$r$ piece of
chapters/frame/heisenberg_frame.tex:2306:(Theorem~\ref{thm:frame-heisenberg-bar}); the double-pole
chapters/examples/heisenberg_eisenstein.tex:49:The Heisenberg bar complex at genus~$0$
chapters/examples/heisenberg_eisenstein.tex:296:is the symmetric chiral algebra on the dual space, with
chapters/examples/heisenberg_eisenstein.tex:305:is the symmetric chiral algebra on the dual space
chapters/examples/heisenberg_eisenstein.tex:306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
chapters/examples/free_fields.tex:1423:\begin{theorem}[Heisenberg bar complex at genus 0; \ClaimStatusProvedHere]\label{thm:heisenberg-bar}
chapters/frame/heisenberg_frame.tex:883:\begin{theorem}[Heisenberg bar complex at genus~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
chapters/frame/heisenberg_frame.tex:884:\label{thm:frame-heisenberg-bar}
chapters/frame/heisenberg_frame.tex:886:\begin{equation}\label{eq:frame-heisenberg-bar-cohomology}
exec
/bin/zsh -lc "sed -n '1418,1445p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
level-inverted Heisenberg.
 
\subsubsection{Bar complex computation}
\label{sec:heisenberg-bar-complex}
 
\begin{theorem}[Heisenberg bar complex at genus 0; \ClaimStatusProvedHere]\label{thm:heisenberg-bar}
For $\mathcal{H}_k$ on $\mathbb{P}^1$:
\[
H^n(\bar{B}_{\text{geom}}(\mathcal{H}_k)) =
\begin{cases}
\mathbb{C} & n = 0 \\
0 & n = 1 \\
\mathbb{C} \cdot c_k & n = 2 \\
0 & n > 2
\end{cases}
\]
where $c_k$ is the central charge class. For genus $g \geq 1$, additional classes arise from $H^1(\Sigma_g)$; see Theorem~\ref{thm:heisenberg-higher-genus}.
\end{theorem}
 
\begin{proof}
codex
I’m seeing a second layer beyond simple dangling labels: some stale refs are attached to wrong epistemic status or wrong object type. The free-field “theorem” cites a conjecture as if proved, and the Heisenberg file is using `\S` against a theorem label, which means the local proof surface is already drifting, not just the cross-reference table.
exec
/bin/zsh -lc "sed -n '286,312p' chapters/examples/heisenberg_eisenstein.tex
printf '\\n=== frame heisenberg koszul dual label context ===\\n'; sed -n '1176,1198p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Heisenberg algebra!complementarity}

\begin{proposition}[Heisenberg complementarity; \ClaimStatusProvedHere]
\label{prop:heisenberg-complementarity}
The Heisenberg algebra and its Koszul dual satisfy exact
complementarity:
\begin{equation}\label{eq:heisenberg-complementarity}
\text{(free-field type~I):}\qquad \kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) \;=\; 0 \qquad \text{(not the Virasoro $13$).}
\end{equation}
The dual algebra $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$
is the symmetric chiral algebra on the dual space, with
curvature $m_0 = -\kappa \cdot \omega_1$. At level
$\kappa = 0$ the bar complex is uncurved; at $\kappa \neq 0$ both
$\cH_\kappa$ and $\cH_\kappa^!$ are curved, with opposite
curvatures.
\end{proposition}

\begin{proof}
The Koszul dual $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$
is the symmetric chiral algebra on the dual space

thinking
**Repairing theorem references**

I need to fix the reference from `\S\ref` to `Theorem\ref{thm:frame-heisenberg-koszul-dual}`. The initial reference to `thm:heisenberg-bar-complex-genus0` seems unnecessary since the proof of the duality is already in `frame-heisenberg-koszul-dual`. The sentence about the Koszul dual emphasizes that it's established by `thm:frame-heisenberg-koszul-dual`, so I'll replace the citation with just that theorem. Additionally, I'll add a period after the next sentence for proper punctuation.
exec
/bin/zsh -lc "rg -n 'hook-transport-corridor|hook-type-transport-koszul-duality|type-a-transport-to-transpose|hook.*corridor|transport.*transpose' chapters/examples/w_algebras.tex chapters/connections/outlook.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/outlook.tex:276: (Theorem~\ref{thm:hook-type-transport-koszul-duality}).
chapters/examples/w_algebras.tex:488:(Theorem~\ref{thm:hook-transport-corridor}). The remaining open
chapters/examples/w_algebras.tex:523:Nilpotent orbits are partially ordered by closure: $e = 0$ gives $\mathcal{W}^k(\fg, 0) = \widehat{\fg}_k$; $e = e_{\mathrm{prin}}$ gives $\mathcal{W}_N$ (generators of spins $d_i + 1$). For $\fg = \mathfrak{sl}_3$: $\widehat{\mathfrak{sl}}_{3,k} \supset \mathcal{W}^k(\mathfrak{sl}_3, f_{\min}) \supset \mathcal{W}_3$ (Computation~\ref{comp:sl3-ds-hierarchy}). The principal row is proved; the minimal/subregular and hook-type rows provide the leading non-principal audit corridor, with explicit local computations and a proved transport mechanism, but their full duality transport remains conditional or conjectural (Theorem~\ref{thm:hook-transport-corridor}, Conjecture~\ref{conj:bp-duality}, Conjecture~\ref{conj:type-a-transport-to-transpose}).
chapters/examples/w_algebras.tex:602:network. Accordingly the hook corridor is kept conditional
chapters/examples/w_algebras.tex:603:(Theorem~\ref{thm:hook-transport-corridor}), and the
chapters/examples/w_algebras.tex:612:(Conjecture~\ref{conj:type-a-transport-to-transpose}).
chapters/examples/w_algebras.tex:7172:\label{rem:hook-transport-corridor-shadow}
chapters/examples/w_algebras.tex:7173:\index{hook-type W-algebra@hook-type $\mathcal{W}$-algebra!transport corridor}
chapters/examples/w_algebras.tex:7174:\index{transport-to-transpose conjecture}
chapters/examples/w_algebras.tex:7178:(at $m = N-2$). The transport-to-transpose conjecture
chapters/examples/w_algebras.tex:7179:(Conjecture~\ref{conj:type-a-transport-to-transpose})
chapters/examples/w_algebras.tex:7192:The hook-type corridor is the first genuine proved non-principal
chapters/examples/w_algebras_deep.tex:1120:hook/minimal corridor under audit \\
chapters/examples/w_algebras_deep.tex:2061: \textup{(}Theorem~\textup{\ref{thm:hook-transport-corridor}};
chapters/examples/w_algebras_deep.tex:2955:Theorem~\textup{\ref{thm:hook-transport-corridor}}\textup{)},
chapters/examples/w_algebras_deep.tex:3330:(Conjecture~\ref{conj:type-a-transport-to-transpose}) gives
chapters/examples/bershadsky_polyakov.tex:484:\section{The hook-type corridor}\label{sec:bp-hook}
chapters/examples/bershadsky_polyakov.tex:495:\index{hook-type corridor}
chapters/examples/yangians_drinfeld_kohno.tex:6538:conjecture. In the hook-type corridor
chapters/examples/yangians_drinfeld_kohno.tex:6539:\textup{(}Theorem~\ref{thm:hook-transport-corridor}\textup{)},
exec
/bin/zsh -lc "rg -n 'kappa\\(\\\\mathcal\\{H\\}|Heisenberg.*formula|Heisenberg.*modular characteristic|Heisenberg level notation|kappa\\(\\mathcal\\{H' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:kappa\(\\mathcal\{H\}|Heisenberg.*formula|Heisenberg.*modular characteristic|Heisenberg level notation|kappa\(\mathcal\{H)
                                                                                                                     ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'Heisenberg level notation' chapters -g '*.tex'
rg -n -F 'kappa(\\mathcal{H}' chapters -g '*.tex'
rg -n -F 'Heisenberg formula' chapters -g '*.tex'
rg -n -F 'modular characteristic (not the level' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2167:\begin{convention}[Heisenberg level notation]
chapters/examples/heisenberg_eisenstein.tex:603:By Theorem~\ref{thm:genus-universality} with $\kappa(\mathcal{H}_\kappa) = \kappa$ and the Faber--Pandharipande $\lambda_g$ formula:
chapters/examples/heisenberg_eisenstein.tex:1087:\boxed{\;\kappa(\mathcal{H}_\kappa^{\oplus d})
chapters/examples/heisenberg_eisenstein.tex:1094:At $\kappa = 1$: $\kappa(\mathcal{H}_1^{\oplus d}) = d = c$.
chapters/examples/heisenberg_eisenstein.tex:1097:$\kappa(\mathcal{H}_\kappa^{\oplus d_1}
chapters/examples/heisenberg_eisenstein.tex:1100:= \kappa(\mathcal{H}_\kappa^{\oplus d_1})
chapters/examples/heisenberg_eisenstein.tex:1101:+ \kappa(\mathcal{H}_\kappa^{\oplus d_2})$,
chapters/examples/heisenberg_eisenstein.tex:1119:$\kappa(\mathcal{H}_\kappa^{\oplus d}) = d\kappa$
chapters/examples/heisenberg_eisenstein.tex:1348:$\kappa(\mathcal{H})$ and Bernoulli numbers. This section explains
chapters/examples/heisenberg_eisenstein.tex:1366:$\Theta_{\mathcal{H}}^{\leq 2} = \kappa(\mathcal{H})$.
chapters/examples/heisenberg_eisenstein.tex:1528:= \kappa(\mathcal{H})$ for all $r \geq 2$,
chapters/examples/heisenberg_eisenstein.tex:1791:\sum_{g \ge 0} \hbar^g\,\kappa(\mathcal{H}_\kappa)\,\lambda_g
chapters/examples/free_fields.tex:319:$\kappa(\mathcal{H}_k) = k$ is tunable
chapters/examples/free_fields.tex:396:= \frac{\kappa(\mathcal{F})}{\kappa(\mathcal{H}_k)}
chapters/examples/free_fields.tex:506:$\kappa(\mathcal{H}_k) + \kappa(\mathcal{H}_k^!) = k + (-k) = 0$.
chapters/examples/free_fields.tex:2420:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$, with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/kac_moody.tex:1550:$\kappa(\mathcal{H}_k^{\oplus d}) = dk$
chapters/examples/genus_expansions.tex:121:$\kappa(\mathcal{H}_\kappa) = d\kappa$
chapters/examples/genus_expansions.tex:245:\kappa(\mathcal{H}_1^{\otimes d}) = d$
chapters/examples/genus_expansions.tex:627:For the Heisenberg algebra, complementarity was the identity $\kappa(\mathcal{H}_k) + \kappa(\mathcal{H}_k^!) = 0$ (\S\ref{sec:frame-complementarity}). The mechanism is the same here ($\kappa + \kappa' = 0$ for all affine Kac--Moody), but the dual level $k' = -k - 2h^\vee$ now involves the dual Coxeter number.
exec
/bin/zsh -lc "rg -n 'delta_\\{\\\\mathrm\\{pf\\}\\}\\"'^'"\\{\\(2,0\\)\\}|pixton.*genus2|planted-forest correction.*48|10 S_3 - \\\\kappa|eq:planted-forest-genus2' chapters/theory/higher_genus_modular_koszul.tex chapters/examples/lattice_foundations.tex chapters/connections/concordance.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:1713:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/examples/lattice_foundations.tex:1714:(Proposition~\ref{prop:pixton-genus2-planted-forest})
chapters/connections/concordance.tex:2144: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$;
chapters/connections/concordance.tex:2145: for Virasoro $\delta_{\mathrm{pf}}^{(2,0)} = -(c-40)/48$.
chapters/connections/concordance.tex:4282:\label{rem:pixton-genus2-computation}
chapters/connections/concordance.tex:4286:$\delta_{\mathrm{pf}}^{(2,0)}$ receives contributions from
chapters/connections/concordance.tex:4294:\begin{equation}\label{eq:planted-forest-genus2-polynomial}
chapters/connections/concordance.tex:4295:\delta_{\mathrm{pf}}^{(2,0)}
chapters/connections/concordance.tex:4368:\delta_{\mathrm{pf}}^{(2,0)}(\cW_3)
chapters/theory/higher_genus_modular_koszul.tex:3464:the three planted-forest graphs contribute~$\delta_{\mathrm{pf}}^{(2,0)}
chapters/theory/higher_genus_modular_koszul.tex:3525:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:3532:$\delta_{\mathrm{pf}}^{(2,0)}$), and the shadow visibility genus
chapters/theory/higher_genus_modular_koszul.tex:18351:$\delta_{\mathrm{pf}}^{(2,0)}
chapters/theory/higher_genus_modular_koszul.tex:18407:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$,
chapters/theory/higher_genus_modular_koszul.tex:20441:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$:
chapters/theory/higher_genus_modular_koszul.tex:20442:for Virasoro, $\delta_{\mathrm{pf}}^{(2,0)} = -(c{-}40)/48$,
chapters/theory/higher_genus_modular_koszul.tex:24933:\cdot [\delta_{\mathrm{pf}}^{(2,0)}]
chapters/theory/higher_genus_modular_koszul.tex:24963:$\delta_{\mathrm{pf}}^{(2,0)} = \alpha(10\alpha{-}\kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:25057: {total $= -\delta_{\mathrm{pf}}^{(2,0)}$};
chapters/theory/higher_genus_modular_koszul.tex:25128:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10\,S_3 - \kappa)/48$,
exec
/bin/zsh -lc "sed -n '26540,26575p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n=== concordance remark context ===\\n'; sed -n '4278,4302p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(dumbbell-type graphs), the $\hbar\Delta$ term corresponds to
\emph{non-separating} self-sewing (lollipop-type graphs), and
$d_{\mathrm{pf}}$ collects the planted-forest corrections from
iterated boundary strata of codimension~$\geq 2$.

\begin{theorem}[Pixton--MC bridge at genus~$2$; \ClaimStatusProvedHere]
\label{thm:pixton-mc-genus2}
\index{Pixton ideal!genus-2 MC bridge|textbf}
\index{genus-2 amplitude!MC decomposition}
Let $\cA$ be a chirally Koszul algebra with shadow data
$(\kappa, S_3, S_4)$. The MC equation at $(g,n)=(2,0)$
determines the genus-$2$ free energy as
\begin{equation}\label{eq:F2-mc-decomposition}
F_2(\cA)
\;=\;
\kappa \cdot \lambda_2^{\mathrm{FP}}
\;+\;
\delta_{\mathrm{pf}}^{(2,0)}(\cA),
\qquad
\lambda_2^{\mathrm{FP}}
exec
/bin/zsh -lc "sed -n '1096,1115p' chapters/connections/thqg_holographic_reconstruction.tex
sed -n '1648,1665p' chapters/connections/thqg_soft_graviton_theorems.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
by induction.

Therefore $o_{r+1} \neq 0$ for all $r \geq 2$, and
$r_{\max}(\mathrm{Vir}_c) = \infty$.
\end{proof}

\begin{remark}[The cubic vertex as permanent source]
\label{rem:cubic-permanent-source}
\index{Virasoro algebra!cubic as permanent source}
The essential mechanism is that the cubic vertex
$\mathfrak{C} = 2x^3$ acts as a \emph{permanent source}
in the shadow obstruction tower: its bracket with any nonzero shadow
produces a nonzero obstruction at the next level. This
is specific to the mixed archetype, where both
$\mathfrak{C} \neq 0$ and $\mathfrak{Q}^{\mathrm{ct}}
\neq 0$ coexist. In the Lie/tree archetype (Kac--Moody),
$\mathfrak{C} \neq 0$ but $\mathfrak{Q}^{\mathrm{ct}} = 0$,
so the quartic bracket $\{\mathfrak{C}, \mathfrak{C}\}_H$
is $d_2$-exact (by Jacobi) and no quintic is generated.
In the contact archetype ($\beta\gamma$),
exec
/bin/zsh -lc "sed -n '1828,1846p' chapters/connections/thqg_holographic_reconstruction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathfrak{Q}^{\mathrm{ct}}\,x^4$.
Reconstruction terminates at step~$3$ (the cubic is
gauge-trivial).
\end{example}

\begin{example}[Virasoro reconstruction]
\label{ex:virasoro-reconstruction}
\index{Virasoro algebra!holographic reconstruction}
Input: $\kappa = c/2$, $\mathfrak{C} = 2x^3$,
$Q^{\mathrm{ct}} = 10/(c(5c+22))$, and the recursive
formula $S_{r+1} = -6r/(c(r+1))\,S_r$
\textup{(}cubic-source approximation; exact for
$r \leq 5$, see
Remark~\textup{\ref{rem:cubic-source-caveat}}\textup{)}.
Output:
$\Theta_{\mathrm{Vir}_c} = \sum_{r=2}^\infty S_r\,x^r$,
with $S_r$ given by
Proposition~\ref{prop:virasoro-shadow-coefficients}.
At $c = 26$:

thinking
**Searching for coefficients**

I’m trying to find precise remarks on Virasoro shadow coefficients for the case where r is less than or equal to 5. I keep thinking that it’s crucial to get the details right. I should look up "r ≤ 5" specifically to find the relevant information and context around it. Let’s see what I can discover about that! It feels a bit complex but I’m eager to sort through it.
exec
/bin/zsh -lc "rg -n 'r \\\\leq 5|r <= 5|exact for.*5|cubic-source approximation' chapters/connections/thqg_holographic_reconstruction.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_holographic_reconstruction.tex:1320:cubic-source approximation;
chapters/connections/thqg_holographic_reconstruction.tex:1346:For $r \leq 5$ this agrees with the exact shadow
chapters/connections/thqg_holographic_reconstruction.tex:1399:cubic-source approximation,
chapters/connections/thqg_holographic_reconstruction.tex:1448:degree~$10$, cubic-source approximation;
chapters/connections/thqg_holographic_reconstruction.tex:1456:For $r \leq 5$, these are the exact shadow coefficients.
chapters/connections/thqg_holographic_reconstruction.tex:1839:\textup{(}cubic-source approximation; exact for
chapters/connections/thqg_holographic_reconstruction.tex:1840:$r \leq 5$, see
chapters/connections/thqg_holographic_reconstruction.tex:1872:\item For $r \geq 5$, the cubic-source approximation
chapters/connections/thqg_holographic_reconstruction.tex:2098:\textup{(}the cubic-source approximation, exact for
chapters/connections/thqg_holographic_reconstruction.tex:2099:$r \leq 5$\textup{)} makes the infinite tower
chapters/examples/genus_expansions.tex:1432:Cross-channels contribute to the bar differential but not to the obstruction class (B-cycle integrals of exact forms vanish). For $\mathfrak{sl}_3$: $\varrho = 1/2 + 1/3 = 5/6$.
chapters/connections/thqg_holographic_reconstruction.tex:1320:cubic-source approximation;
chapters/connections/thqg_holographic_reconstruction.tex:1346:For $r \leq 5$ this agrees with the exact shadow
chapters/connections/thqg_holographic_reconstruction.tex:1399:cubic-source approximation,
chapters/connections/thqg_holographic_reconstruction.tex:1448:degree~$10$, cubic-source approximation;
chapters/connections/thqg_holographic_reconstruction.tex:1456:For $r \leq 5$, these are the exact shadow coefficients.
chapters/connections/thqg_holographic_reconstruction.tex:1839:\textup{(}cubic-source approximation; exact for
chapters/connections/thqg_holographic_reconstruction.tex:1840:$r \leq 5$, see
chapters/connections/thqg_holographic_reconstruction.tex:1872:\item For $r \geq 5$, the cubic-source approximation
chapters/connections/thqg_holographic_reconstruction.tex:2098:\textup{(}the cubic-source approximation, exact for
exec
/bin/zsh -lc "sed -n '1312,1462p' chapters/connections/thqg_holographic_reconstruction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Virasoro algebra!shadow coefficients!recursive structure}

The recursive formula~\eqref{eq:shadow-recursive-formula}
determines the shadow coefficients $S_r$ for all
$r \geq 5$. We record the first several values and
exhibit the closed-form solution.

\begin{proposition}[Virasoro shadow coefficients,
cubic-source approximation;
\ClaimStatusProvedHere]
\label{prop:virasoro-shadow-coefficients}
\index{shadow coefficients!Virasoro}
The primary-line shadow coefficients
$\mathrm{Sh}_r(\mathrm{Vir}_c) = S_r\,x^r$
have the following dominant contribution from
the cubic source term in the shadow master equation.
The cubic-source recursion gives
\begin{equation}\label{eq:virasoro-shadow-recursion}
S_{r+1}^{\mathrm{cub}} = -\frac{6r}{c(r+1)}\,S_r^{\mathrm{cub}},
\qquad r \geq 5,
exec
/bin/zsh -lc "sed -n '1508,1522p' chapters/theory/derived_langlands.tex
rg -n '\\\\label\\{chap:.*(modular|genus|langlands)' chapters/theory/*.tex chapters/connections/*.tex chapters/examples/*.tex chapters/frame/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Shadow connection, opers, and the Hitchin WKB]
\label{rem:shadow-hitchin-wkb}
\index{shadow connection!Hitchin WKB}
\index{oper!indicial roots from shadow data}
\index{WKB approximation!from shadow connection}
The shadow connection
$\nabla^{\mathrm{sh}} = d - Q_L'/(2Q_L)\,dt$
(Chapter~\ref{chap:modular-koszul},
Theorem~\ref{thm:shadow-connection})
specializes to the Knizhnik--Zamolodchikov connection for
affine Kac--Moody algebras and to the BPZ connection for
Virasoro. At the critical level $k = -h^\vee$
(equivalently, $\kappa(\widehat{\fg}_{-h^\vee}) = 0$): the shadow connection becomes
regular, the shadow metric degenerates to $Q_L(t) = 9\alpha^2
t^2$, and the space of flat sections consists of polynomial
chapters/theory/e1_modular_koszul.tex:10:\label{chap:e1-modular-koszul}
chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
chapters/theory/higher_genus_foundations.tex:2:\label{chap:higher-genus}
chapters/connections/semistrict_modular_higher_spin_w3.tex:6:\label{chap:semistrict-modular-W3}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:shadow-connection\\}' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:18909:\label{thm:shadow-connection}
exec
/bin/zsh -lc "sed -n '1,20p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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


thinking
**Exploring file structure**

I'm finding it interesting that this file is labeled as a section instead of a chapter. Maybe it's included within a chapter? It seems like the `chap:modular-koszul` label is missing since this file isn’t set as a chapter. I'm wondering if there is a hidden label in `main.tex` or if it’s wrapped in a chapter. I think it would be worth searching for phantom labels in `main.tex` to clarify!
exec
/bin/zsh -lc "rg -n 'chap:modular-koszul|higher_genus_modular_koszul' main.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:23295:%: from higher_genus_modular_koszul.tex:2888; lambda=0 -> 1, lambda=1/2 -> -1/2 verified
chapters/theory/derived_langlands.tex:1515:(Chapter~\ref{chap:modular-koszul},
chapters/theory/higher_genus.tex:6:\input{chapters/theory/higher_genus_modular_koszul}

thinking
**Reviewing chapter references**

I'm thinking that the `chap:higher-genus` chapter might include the `higher_genus_modular_koszul` section. I should probably fix the reference to `Chapter\ref{chap:higher-genus}`. The `thm:shadow-connection` theorem is within that section found in the `higher_genus.tex` file. So it looks like I need to inspect the contents of `chapters/theory/higher_genus.tex` to ensure everything aligns properly. Let's double-check that!
exec
/bin/zsh -lc "sed -n '1,20p' chapters/theory/higher_genus.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% Dispatcher: higher_genus.tex
% Split into three semantic units for maintainability.
% The compiled PDF is byte-for-byte identical.
\input{chapters/theory/higher_genus_foundations}
\input{chapters/theory/higher_genus_complementarity}
\input{chapters/theory/higher_genus_modular_koszul}

thinking
**Counting unresolved references**

I'm thinking that I need to compile a full list of 16 unresolved references, along with each file and line number for the exact fixes. Some labels might show up multiple times in the same file, so I need to consider whether to count each occurrence or just unique unresolved references. Since the user mentioned that every unresolved reference is a finding with a fix, it seems like each occurrence is important. I might need to run a script to count these occurrences accurately.
exec
/bin/zsh -lc "sed -n '1078,1094p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
m_0^{(ij)} &= \kappa\delta^{ij}\cdot\omega_1,
\label{eq:rank-d-curvature}
\\
m_0 &= \sum_{i=1}^d m_0^{(ii)}
= d\kappa\cdot\omega_1.
\end{align}
The obstruction coefficient is the scalar
prefactor:
\begin{equation}\label{eq:heisenberg-kappa-formula}
\boxed{\;\kappa(\mathcal{H}_\kappa^{\oplus d})
= d\kappa.\;}
\end{equation}

\emph{Step~5: Consistency checks.}
\begin{enumerate}[label=(\roman*)]
\item \emph{Central charge comparison.}
At $\kappa = 1$: $\kappa(\mathcal{H}_1^{\oplus d}) = d = c$.


thinking
**Calculating unresolved references**

I'm looking into how we can compute references in chapters that aren’t explicitly labeled but exist in main.tex or other non-chapter paths. I think I calculated 16 unresolved references? Wait, if I consider chapters-only minus all labels, that results in 16 unresolved. The difference here seems to be about labels that are resolved outside of chapters, mainly in appendices and maybe in main.tex, where there are over 100 such labels.
thinking
**Identifying hidden imports**

I'm thinking about how appendices are part of the main book structure. I should identify labels defined only in the main.tex file or those outside the `chapters/`. The user's audit surface focuses on `chapters/`, so references outside of that could be considered hidden imports. However, references to appendices might be legitimate. I need to compute chapter references that resolve only in main.tex while considering labels in appendices too. I'll search for those labeled references next.
codex
I’ve finished the true dangling-label pass. One extra adversarial check is still worth doing before I report: labels that resolve only because `main.tex` injects a phantom alias are hidden imports, and they survive a naive unresolved-ref audit while still leaving the chapter tree non-self-contained.
exec
/bin/zsh -lc "rg -o --no-filename '\\\\label\\{["'^}]+'"\\}' main.tex | sed 's/"'^'"\\\\label{//; s/}"'$//'"' | sort -u > /tmp/labels_main.txt
comm -23 /tmp/refs_norm.txt /tmp/labels_norm_chapters.txt > /tmp/not_in_chapters.txt
comm -12 /tmp/not_in_chapters.txt /tmp/labels_main.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
app:coderived-models
app:combinatorial-frontier
app:w3-jacobi-full
conj:w3-bar-gf
cor:clean-replacement
def:quartic-log-contact-class
ex:tower-four-archetypes
part:bar-complex
part:characteristic-datum
part:physics-bridges
part:standard-landscape
princ:modular-trace
prop:quartic-contact-vanishes-BL
sec:conventions
thm:complementarity
thm:kappa-kac-moody
thm:level-rank
thm:vol2-annulus-trace



thinking
**Evaluating chapter references**

I’m looking at some references in chapters that are only resolved by labels in main.tex. I need to find those occurrences and see if they’re hidden imports. Some could be legitimate part labels, and while referencing parts might be okay, unlike hidden ones, chapters compiled without main would fail. There are 19 labels to check, but I’m wondering if the user means phantom labels in main.tex as hidden imports. It could make the final findings long. Do I really need to inspect all occurrences?
thinking
**Analyzing hidden imports**

The user is asking for every hidden import, which might turn out to be more than just the unresolved references. I think I need to include hidden imports from main.tex that aren't defined in the chapters. Should I include appendix labels too? Maybe not since they are explicit and not hidden. I should identify if labels are only in main.tex or also in the appendices since some might appear in both. I need to verify unique locations in main.tex, so I’ll need to search and inspect each label.
thinking
**Identifying labels in main.tex**

There may be quite a few labels, but I think they’re manageable. Some could be legitimate part labels, like part:bar-complex in main.tex, which is fine. However, others might be phantom aliases for appendix sections. I really need to determine if they’re exclusive to main.tex. I can use a command like `rg -n -F '\label{label}' .` to identify these labels and generate counts to organize the data properly.
exec
/bin/zsh -lc 'for k in app:coderived-models app:combinatorial-frontier app:w3-jacobi-full conj:w3-bar-gf cor:clean-replacement def:quartic-log-contact-class ex:tower-four-archetypes part:bar-complex part:characteristic-datum part:physics-bridges part:standard-landscape princ:modular-trace prop:quartic-contact-vanishes-BL sec:conventions thm:complementarity thm:kappa-kac-moody thm:level-rank thm:vol2-annulus-trace; do echo "=== $k ==="; rg -n -F "'"\\\\label{"'$k}" .; done' in /Users/raeez/chiral-bar-cobar succeeded in 631ms:
./main.tex:1821: \phantomsection\label{app:combinatorial-frontier}%
=== app:w3-jacobi-full ===
./appendices/computational_tables.tex:135:\label{app:w3-jacobi-full}
./main.tex:1822: \phantomsection\label{app:w3-jacobi-full}%
./wave2_audit_20260413_001942/U08_empty_sections.md:283:./.claude/worktrees/agent-a001fc1b/appendices/computational_tables.tex	133	section	\section{\texorpdfstring{$W_3$ algebra coefficients}{W-3 algebra coefficients}}	2	\label{app:w3-coefficients} || \label{app:w3-jacobi-full}
./wave2_audit_20260413_001942/U08_empty_sections.md:369:appendices/computational_tables.tex	133	section	\section{\texorpdfstring{$W_3$ algebra coefficients}{W-3 algebra coefficients}}	2	\label{app:w3-coefficients} || \label{app:w3-jacobi-full}
./wave2_audit_20260413_001942/U08_empty_sections.md:760:appendices/computational_tables.tex	133	section	\section{\texorpdfstring{$W_3$ algebra coefficients}{W-3 algebra coefficients}}	2	\label{app:w3-coefficients} || \label{app:w3-jacobi-full}	subsection	137	\subsection{\texorpdfstring{Composite field $\Lambda$ formula}{Composite field formula}}
=== conj:w3-bar-gf ===
./main.tex:1796: \phantomsection\label{conj:w3-bar-gf}%
./appendices/combinatorial_frontier.tex:469:\begin{conjecture}[\texorpdfstring{$\mathcal{W}_3$}{W3} bar cohomology generating function; \ClaimStatusConjectured]\label{conj:w3-bar-gf}
=== cor:clean-replacement ===
./main.tex:1843: \phantomsection\label{cor:clean-replacement}%
./wave2_audit_20260413_001942/C17_concordance.md:1961:  1837	 \phantomsection\label{cor:clean-replacement}%
=== def:quartic-log-contact-class ===
./main.tex:1860: \phantomsection\label{def:quartic-log-contact-class}% % Vol II ht_bulk_boundary_line_core.tex
=== ex:tower-four-archetypes ===
./main.tex:1839: \phantomsection\label{ex:tower-four-archetypes}%
=== part:bar-complex ===
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:768:main.tex:895:\label{part:bar-complex}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:309:/Users/raeez/chiral-bar-cobar/main.tex:895:\label{part:bar-complex}

thinking
**Evaluating phantom labels**

I'm noticing plenty of phantom labels in main.tex. Including all of them might overwhelm the findings, especially since the user wants to focus on unresolved references in the mission chapters. However, they mentioned wanting every hidden import too. I see at least 19 labels referenced in chapters that are only defined in main.tex. I wonder if I should report their occurrences; maybe that’s too many, though. I think I should compute their occurrences to file lines. Let’s go for it!
exec
/bin/zsh -lc "for k in app:coderived-models app:combinatorial-frontier app:w3-jacobi-full conj:w3-bar-gf cor:clean-replacement def:quartic-log-contact-class ex:tower-four-archetypes part:bar-complex part:characteristic-datum part:physics-bridges part:standard-landscape princ:modular-trace prop:quartic-contact-vanishes-BL sec:conventions thm:complementarity thm:kappa-kac-moody thm:level-rank thm:vol2-annulus-trace; do rg -n \"\\\\\\\\ref\\{"'$k'"\\}\" chapters || true; done" in /Users/raeez/chiral-bar-cobar succeeded in 69ms:
chapters/connections/thqg_symplectic_polarization.tex:1967:(Theorem~\ref{thm:kappa-kac-moody}).
chapters/connections/thqg_gravitational_s_duality.tex:1995:(Theorem~\ref{thm:level-rank}) is a refinement for integer levels.
chapters/connections/concordance.tex:4014:(Theorem~\ref{thm:vol2-annulus-trace}), and (iii)~the closed-sector


thinking
**Evaluating hidden imports**

There seems to be a multitude of hidden imports, and while some part labels are legitimate, including every hidden import is a massive task. The user might be looking for a more adversarial audit, but I think focusing only on the phantomsection labels from main.tex is the way to go. That's about ten labels defined with `\phantomsection`. I should also ignore any that exist in the appendices since they aren’t hidden.
thinking
**Considering phantom labels**

I see that `app:coderived-models` is the only phantom label, while the others like `cor:clean-replacement`, `def:quartic-log-contact-class`, and others are also phantom labels. I need to check if `conj:w3-bar-gf` has an appendix definition because that would mean it’s not hidden. Now, I could compute occurrences and suggest fixes, but that might increase the number of findings. The user mentioned wanting to cover all missing definitions and hidden imports, so including some is probably a good idea. That could bring the total findings to about 31.
exec
/bin/zsh -lc "rg -n '\\\\label\\{app:coderived\\}|\\\\label\\{app:coderived-models\\}|coderived models' appendices chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1590: \phantomsection\label{app:coderived}% % coderived_models.tex
main.tex:1607: \phantomsection\label{app:coderived-models}% % planned appendix
chapters/theory/coderived_models.tex:3:\label{app:coderived}

thinking
**Inspecting and correcting refs**

I need to replace `app:coderived-models` references with `app:coderived`. I'll inspect the occurrences in the line contexts, possibly checking an appendix too. This seems straightforward.

For the `cor:clean-replacement`, it looks like it's just a phantom label. I’ll need to search for a similar live label in volume II. Comments in the main.tex file could guide me, so I should inspect that section around the label line or search for occurrences there.
exec
/bin/zsh -lc "sed -n '1838,1845p' main.tex
rg -n 'clean replacement|clean-replacement' chapters /Users/raeez/chiral-bar-cobar-vol2 -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \phantomsection\label{thm:kappa-kac-moody}%
 \phantomsection\label{ex:tower-four-archetypes}%
 % --- Cross-volume Vol II labels ---
 \phantomsection\label{def:swiss-cheese-W-resolution}%
 \phantomsection\label{thm:branch-bv}%
 \phantomsection\label{cor:clean-replacement}%
 \phantomsection\label{conj:rmatrix}% % Vol II log_ht_monodromy_frontier.tex
 \phantomsection\label{cor:holographic-dictionary}% % Vol II log_ht_monodromy_core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex:516:\label{cor:clean-replacement}
chapters/theory/e1_modular_koszul.tex:2624:operad \textup{(}Volume~II, \S\ref{cor:clean-replacement}\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:49:Semidirect slogan replacement & ProvedHere & Cor.~\ref{cor:clean-replacement} \\





thinking
**Considering technical fixes**

I need to address the user's request about the reference issue in their LaTeX file. The fix involves removing `\phantomsection\label{cor:clean-replacement}` from main.tex and either creating an alias file or replacing the cross-volume reference with plain text. It seems the user isn’t necessarily looking for a patch but rather a clear fix suggestion. Maybe focusing specifically on unresolved references could be more effective, especially with the inclusion of hidden imports as mentioned.
thinking
**Exploring hidden imports**

I’m reflecting on the idea of including cross-volume hidden imports from the current chapters. To do this effectively, I need to pinpoint exact lines, which could be manageable if I focus on the ones identified through the main.tex diff and their occurrences. However, this will likely increase the length of the document. It’s crucial to inspect each unique hidden-import target and analyze its occurrence count, but determining the exact fix might be a bit challenging.
thinking
**Clarifying user request**

The user is asking for a precise fix related to unresolved references. The goal is to identify all unresolved references, as every one of them is a valid finding. Hidden imports are also noted as important. To keep things manageable, I should report unresolved references along with a few status or hidden import failures. However, there's a balance between being complete and manageable, especially since the user mentioned needing a foundation audit of chapters. I need to see if I can include those hidden imports without complicating things too much.
thinking
**Defining checked references**

I think we can consider the checked surface as all the `\ref{}` citations in the chapters along with any labels from the main.tex aliases. I need to count how many checked occurrences there are. Some hidden import categories might not be relevant since they aren't aliased. Since part labels in main.tex don't function as standalone chapters, they might be treated differently in our audit. I should focus on how to summarize the checked references accurately while considering potential fixes for labels. We can possibly group multiple line references together for clearer findings.
thinking
**Grouping unresolved labels**

I can format the unresolved labels in a way that shows them grouped by file and line numbers, like `chapters/theory/higher_genus_foundations.tex:293; 407; 831`. This helps condense the information while still being clear. The user mentioned that every unresolved reference counts as a finding, so it might make sense to group similar missing labels across different line references if they're addressing the same issue. However, I need to keep to a structured format, possibly using semicolons for clarity while managing the line count. I should keep the total under 70 lines.
exec
/bin/zsh -lc "sed -n '2616,2628p' chapters/theory/e1_modular_koszul.tex
sed -n '508,522p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 vertex, so every open graph thickens to a surface
 \textup{(}Theorem~\textup{\ref{thm:cyclicity-ribbon}}\textup{)}.
\end{enumerate}
The open input is a cyclic $A_\infty$-object
$(O, m_\bullet, \tau)$\textup; the closed input is
the modular datum $\Theta_\cA$.
The tree part recovers the Boardman--Vogt resolution
$W(\mathrm{SC}^{\mathrm{ch,top}})$ of the Swiss-cheese
operad \textup{(}Volume~II, \S\ref{cor:clean-replacement}\textup{)}.
\end{definition}

\begin{remark}[The correct holographic language]%
\label{rem:correct-holographic-language}%
operation spaces, combined with the factor-by-factor recognition
(CG17 for~$\C$, AF15 for~$\R$) and the K\"unneth isomorphism for
mixed operations, closes the assembly.
\qedhere
\end{proof}

\begin{corollary}[Clean replacement of the semidirect slogan;

thinking
**Evaluating hidden imports**

I could mention that there are 10 additional hidden-import references resolved only by `main.tex` aliases, and each finding is part of a structured contract. I need to focus on the unresolved/core items first. It's important to see how widely `thm:complementarity` is used. While considering local labels like `thm:quantum-complementarity-main`, I find it might be safer to stick to unresolved items since this will keep things less complex and aligned with what the user asked for.
exec
/bin/zsh -lc "sed -n '5724,5736p' chapters/theory/higher_genus_foundations.tex
sed -n '1598,1608p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:propagator-weight-universality}%
\index{propagator weight universality|textbf}%
\index{bar complex!propagator weight}%
\index{prime form!weight of d log}%
The bar complex propagator is $d\log E(z,w)$, where $E(z,w)$
is the prime form on a Riemann surface. The prime form is a
section of $K^{-1/2} \boxtimes K^{-1/2}$
(cf.\ the critical pitfall in~\S\ref{sec:conventions}),
so $d\log E = dE/E$ has weight~$1$ in both variables,
\emph{regardless} of the conformal weight of the fields being sewed.

This observation has two consequences:
\begin{enumerate}[label=\textup{(\roman*)}]
 \phantomsection\label{cor:hs-sewing-standard-landscape}% % genus_complete.tex
 \phantomsection\label{thm:ds-bar-gf-discriminant}% % landscape_census.tex
 \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
 % thm:family-index now defined in guide_to_main_results.tex
 \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
 % --- 18 additional phantom stubs (2026-03-29 audit) ---
 \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
exec
/bin/zsh -lc "rg -n 'sec:conventions' main.tex chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1639: \phantomsection\label{sec:conventions}% % higher_genus_foundations.tex forward ref
chapters/theory/higher_genus_foundations.tex:5731:(cf.\ the critical pitfall in~\S\ref{sec:conventions}),

thinking
**Searching for conventions**

I’m considering whether there’s a specific section in higher_genus_foundations or another source that discusses conventions. It would be helpful to dig into labels that are similar to find relevant information. I want to make sure I’m covering all bases, so looking into various sources should help clarify things. Let’s see what I can uncover! It’s always good to explore these things thoroughly.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(sec|subsec|conv):.*convention' chapters/theory/higher_genus_foundations.tex chapters/theory/*.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_construction.tex:634:\subsection{Sign conventions}\label{sec:sign-conventions}
chapters/theory/higher_genus_modular_koszul.tex:10824:\label{subsec:two-level-convention}
exec
/bin/zsh -lc "wc -l /tmp/refs_norm.txt /tmp/labels_norm_all.txt /tmp/not_in_chapters.txt
printf 'unresolved_occurrences='; for k in chap:modular-koszul prop:heisenberg-kappa prop:pixton-genus2-planted-forest rem:cubic-source-caveat rem:free-field-three-theorems rem:thqg-I-spectral-finiteness rem:w-algebra-three-theorems sec:completion-programme-overview sec:concordance-holographic-programme sec:concordance-three-tier-r-matrix sec:sl3-bar-table thm:bar-cobar-path-integral-heisenberg thm:heisenberg-bar-complex-genus0 thm:hook-type-transport-koszul-duality thm:modular thm:rtt-all-types; do rg -n \"\\\\\\\\ref\\{"'$k'"\\}\" chapters | wc -l | tr -d '\\n'; printf '+'; done; echo" in /Users/raeez/chiral-bar-cobar succeeded in 328ms:
       1+       1+       1+       0+       2+       0+       2+       0+       1+       1+       2+       2+       1+       1+       1+       2+

thinking
**Debugging regex issues**

I’m noticing some zeros popping up, possibly due to how `rg` interprets regex. It seems like I might have made an error with braces or hyphens. Well, if it didn’t work, it’s not a huge deal. I’ll manually count and have found 21 so far. Now, it’s time to compute all unresolved occurrences using a line-matching method with a command: `while read k; do rg -n "\\ref{$k}" chapters; done`. Let’s see if that clears things up!
exec
/bin/zsh -lc "python - <<'PY'
labels = '''chap:modular-koszul
prop:heisenberg-kappa
prop:pixton-genus2-planted-forest
rem:cubic-source-caveat
rem:free-field-three-theorems
rem:thqg-I-spectral-finiteness
rem:w-algebra-three-theorems
sec:completion-programme-overview
sec:concordance-holographic-programme
sec:concordance-three-tier-r-matrix
sec:sl3-bar-table
thm:bar-cobar-path-integral-heisenberg
thm:heisenberg-bar-complex-genus0
thm:hook-type-transport-koszul-duality
thm:modular
thm:rtt-all-types'''.splitlines()
import subprocess, shlex
count=0
for k in labels:
    out = subprocess.run(['rg','-n',fr'\\\\ref\\{{{k}\\}}','chapters'],capture_output=True,text=True).stdout.strip().splitlines()
    count += len([x for x in out if x])
print(count)
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python3 - <<'PY'
labels = '''chap:modular-koszul
prop:heisenberg-kappa
prop:pixton-genus2-planted-forest
rem:cubic-source-caveat
rem:free-field-three-theorems
rem:thqg-I-spectral-finiteness
rem:w-algebra-three-theorems
sec:completion-programme-overview
sec:concordance-holographic-programme
sec:concordance-three-tier-r-matrix
sec:sl3-bar-table
thm:bar-cobar-path-integral-heisenberg
thm:heisenberg-bar-complex-genus0
thm:hook-type-transport-koszul-duality
thm:modular
thm:rtt-all-types'''.splitlines()
import subprocess
count=0
for k in labels:
    out = subprocess.run(['rg','-n',fr'\\\\ref\\{{{k}\\}}','chapters'],capture_output=True,text=True).stdout.strip().splitlines()
    count += len([x for x in out if x])
print(count)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 240ms:
18
exec
/bin/zsh -lc 'for k in chap:modular-koszul prop:heisenberg-kappa prop:pixton-genus2-planted-forest rem:cubic-source-caveat rem:free-field-three-theorems rem:thqg-I-spectral-finiteness rem:w-algebra-three-theorems sec:completion-programme-overview sec:concordance-holographic-programme sec:concordance-three-tier-r-matrix sec:sl3-bar-table thm:bar-cobar-path-integral-heisenberg thm:heisenberg-bar-complex-genus0 thm:hook-type-transport-koszul-duality thm:modular thm:rtt-all-types; do echo "=== $k"; rg -n "'"\\\\\\\\ref\\{"'$k'"\\}\" chapters || true; done" in /Users/raeez/chiral-bar-cobar succeeded in 83ms:
chapters/examples/heisenberg_eisenstein.tex:306:(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual});
=== thm:hook-type-transport-koszul-duality
chapters/connections/outlook.tex:276: (Theorem~\ref{thm:hook-type-transport-koszul-duality}).
=== thm:modular
chapters/theory/higher_genus_modular_koszul.tex:15142:%% all genera, and the resolution of Conjecture~\ref{thm:modular}
=== thm:rtt-all-types
chapters/examples/yangians_foundations.tex:1228:Theorem~\textup{\ref{thm:rtt-all-types}(iv)} likewise operates
chapters/examples/yangians_computations.tex:1150:(Theorem~\ref{thm:rtt-all-types}): the $R$-matrix for
exec
/bin/zsh -lc "rg -n -F '\\ref{rem:cubic-source-caveat}' chapters
rg -n -F '\\ref{rem:thqg-I-spectral-finiteness}' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Exploring hidden imports**

I’m considering whether to reference `e1_modular_koszul` alongside `cor:clean-replacement` from volume II through the main phantom. Including both as hidden import findings might be valuable. However, there could be more unresolved findings to address. I wonder how many alias-only references exist in the chapters after excluding certain labels. I’ll need to compute occurrences defined only by phantom sections in main.tex, which could lead to around 12 occurrences to manage. I should run this once for accuracy.
exec
/bin/zsh -lc 'for k in app:coderived-models cor:clean-replacement def:quartic-log-contact-class ex:tower-four-archetypes princ:modular-trace prop:quartic-contact-vanishes-BL sec:conventions thm:complementarity thm:kappa-kac-moody thm:level-rank thm:vol2-annulus-trace; do echo "=== $k ==="; rg -n -F "'"\\\\ref{"'$k}" chapters; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
=== app:coderived-models ===
chapters/theory/higher_genus_foundations.tex:293:see Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:407: $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:831: \textup{(}Appendix~\textup{\ref{app:coderived-models})}.
=== cor:clean-replacement ===
chapters/theory/e1_modular_koszul.tex:2624:operad \textup{(}Volume~II, \S\ref{cor:clean-replacement}\textup{)}.
=== def:quartic-log-contact-class ===
chapters/connections/concordance.tex:4022:Definition~\ref{def:quartic-log-contact-class} (Volume~II) defines
=== ex:tower-four-archetypes ===
=== princ:modular-trace ===
chapters/connections/concordance.tex:4009:Principle~\ref{princ:modular-trace} (Volume~II) organizes the modular
=== prop:quartic-contact-vanishes-BL ===
chapters/connections/concordance.tex:4026:Proposition~\ref{prop:quartic-contact-vanishes-BL} proves
=== sec:conventions ===
chapters/theory/higher_genus_foundations.tex:5731:(cf.\ the critical pitfall in~\S\ref{sec:conventions}),
=== thm:complementarity ===
chapters/examples/y_algebras.tex:486:Theorem~\ref{thm:complementarity} for $\cW$-algebras.
chapters/examples/yangians_drinfeld_kohno.tex:7585:\textup{(}Theorem~\textup{\ref{thm:complementarity})} has dimension
chapters/examples/yangians_drinfeld_kohno.tex:7627:genus-$g$ surface (Theorem~\ref{thm:complementarity}). For
chapters/examples/moonshine.tex:38: & Thm~\ref{thm:complementarity} \\
exec
/bin/zsh -lc "rg -n 'kappa-kac-moody|level-rank|tower-four-archetypes' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:616:$\lambda \mapsto 1 - \lambda$ (level-rank), which is
chapters/examples/w_algebras_deep.tex:860:(the level-rank involution; distinct from the Feigin--Frenkel
chapters/examples/kac_moody.tex:2647:level-rank duality for $\mathfrak{sl}_2$ conformal blocks
chapters/examples/kac_moody.tex:5918:\label{sec:level-rank-bar-cobar}
chapters/examples/kac_moody.tex:5919:\index{level-rank duality!as bar-cobar equivalence}
chapters/examples/kac_moody.tex:5920:\index{Koszul duality!level-rank}
chapters/examples/kac_moody.tex:5923:interpretation is that \emph{level-rank duality}, the classical
chapters/examples/kac_moody.tex:5929:\label{prop:level-rank-boundary-voa}
chapters/examples/kac_moody.tex:5930:\index{level-rank duality!boundary VOA isomorphism}
chapters/examples/kac_moody.tex:5937:\begin{equation}\label{eq:level-rank-voa-iso}
chapters/examples/kac_moody.tex:5945:\label{cor:level-rank-bar-intertwining}
chapters/examples/kac_moody.tex:5946:\index{bar complex!level-rank intertwining}
chapters/examples/kac_moody.tex:5948:\eqref{eq:level-rank-voa-iso} lifts to an equivalence of dg
chapters/examples/kac_moody.tex:5950:\begin{equation}\label{eq:level-rank-bar-equiv}
chapters/examples/kac_moody.tex:5957:level-rank duality \emph{is} the bar-cobar adjunction
chapters/examples/kac_moody.tex:5963:\label{rem:level-rank-feigin-frenkel}
chapters/examples/kac_moody.tex:5964:\index{Feigin--Frenkel duality!and level-rank}
chapters/examples/kac_moody.tex:5985:The Verlinde level-rank swap
chapters/examples/kac_moody.tex:6029:\begin{conjecture}[Complementarity as the level-rank pairing;
chapters/examples/kac_moody.tex:6031:\label{conj:level-rank-complementarity}
exec
/bin/zsh -lc "rg -n 'ordered-modular-MC|associative modular Maurer|modular Maurer|resolution of Conjecture' chapters/theory/e1_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/ordered_associative_chiral_kd.tex:10276:\subsection{Associative modular Maurer--Cartan theory}
chapters/theory/ordered_associative_chiral_kd.tex:10282:\begin{theorem}[Associative modular Maurer--Cartan class;
chapters/theory/higher_genus_modular_koszul.tex:3570:\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
chapters/theory/higher_genus_modular_koszul.tex:15142:%% all genera, and the resolution of Conjecture~\ref{thm:modular}
chapters/theory/higher_genus_modular_koszul.tex:28685: is the universal modular Maurer--Cartan class

thinking
**Addressing severity distribution**

I'm considering how to mention the severity distribution of issues: one critical, one high, and the rest medium or low. Maybe there could be one or two high-priority items, like the Heisenberg proof. The others might be medium, while I’ll comment on the low ones. I also need to include exact fixes, like for `rem:cubic-source-caveat`, replacing it with `Proposition\ref{prop:virasoro-shadow-coefficients}` and deleting the "Remark" wording. I think I should document that too!
codex
I’ve mapped every stale label to a live target or, where no live target exists, to the minimal truthful rewrite. I’m doing one last existence check on those replacement labels now so the final list doesn’t contain “fixes” that are themselves dead.
exec
/bin/zsh -lc 'for k in chap:higher-genus conv:heisenberg-kappa-notation thm:pixton-mc-genus2 prop:virasoro-shadow-coefficients rem:free-field-five-theorems rem:thqg-I-spectral-geometric sec:w-five-theorems subsec:transgression-algebra def:holographic-modular-koszul-datum def:three-tier-r-matrix sec:sl3-spectral-sequence conj:bar-cobar-path-integral-heisenberg thm:frame-heisenberg-koszul-dual thm:hook-transport-corridor thm:rtt-all-classical-types; do echo "=== $k ==="; rg -n -F "'"\\\\label{"'$k}" chapters appendices /Users/raeez/chiral-bar-cobar-vol2/chapters || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
chapters/connections/subregular_hook_frontier.tex:229:\label{thm:hook-transport-corridor}
=== thm:rtt-all-classical-types ===
chapters/examples/yangians_foundations.tex:209:\label{thm:rtt-all-classical-types}
exec
/bin/zsh -lc "rg -n 'virasoro-shadow-coefficients|thqg-I-spectral-geometric|subsec:transgression-algebra' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'label\\{prop:vir' chapters/connections/thqg_holographic_reconstruction.tex
rg -n 'label\\{rem:thqg-I' chapters/connections/thqg_perturbative_finiteness.tex
rg -n 'label\\{subsec:transgression' chapters/connections/thqg_critical_string_dichotomy.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: chapters/connections/thqg_holographic_reconstruction.tex: IO error for operation on chapters/connections/thqg_holographic_reconstruction.tex: No such file or directory (os error 2)
rg: chapters/connections/thqg_perturbative_finiteness.tex: IO error for operation on chapters/connections/thqg_perturbative_finiteness.tex: No such file or directory (os error 2)
rg: chapters/connections/thqg_critical_string_dichotomy.tex: IO error for operation on chapters/connections/thqg_critical_string_dichotomy.tex: No such file or directory (os error 2)

thinking
**Identifying file paths**

I'm considering if those files might be under the current repository. I remember reading them from chapters/connections, but I'm wondering if the path has any uppercase letters. It feels like I need to double-check and list the files to clarify this. Taking a moment to ensure I gather the right paths is probably a smart move, so I’ll proceed with that!
exec
/bin/zsh -lc "ls chapters/connections | rg 'thqg_holographic|thqg_perturbative|thqg_critical'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Checking file locations**

I'm wondering if these files might actually be in Volume II. Earlier, it seemed like we read from the current repository, possibly using a symlink. I think I should list the contents of the 'chapters/connections' directory and look at the first few items to clarify this. So, I'll run the command to check what’s there. Let's see if I can find the right files!
exec
/bin/zsh -lc "ls chapters/connections | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
arithmetic_shadows.tex
bv_brst.tex
concordance.tex
editorial_constitution.tex
entanglement_modular_koszul.tex
feynman_connection.tex
feynman_diagrams.tex
frontier_modular_holography_platonic.tex
genus1_seven_faces.tex
genus_complete.tex
holographic_codes_koszul.tex
holographic_datum_master.tex
master_concordance.tex
outlook.tex
poincare_computations.tex
semistrict_modular_higher_spin_w3.tex
subregular_hook_frontier.tex
thqg_entanglement_programme.tex
thqg_introduction_supplement.tex
thqg_introduction_supplement_body.tex
exec
/bin/zsh -lc 'pwd
ls chapters/connections | wc -l' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
      21
exec
/bin/zsh -lc "rg -n 'cubic-source-caveat|thqg-I-spectral-finiteness|completion-programme-overview' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n 'rem:free-field-three-theorems|thqg_holographic_reconstruction|thqg_preface_supplement|thqg_perturbative_finiteness' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).
codex
The surface shifted while I was verifying it: several earlier hits were not reproducible in the live `chapters/` tree anymore. I’m regenerating the unresolved-reference set from scratch right now and dropping anything I can’t re-read locally, so the final report only contains current, reproducible findings.
exec
/bin/zsh -lc 'for k in $(comm -23 /tmp/refs_norm_now.txt /tmp/labels_norm_all_now.txt); do echo "=== $k ==="; rg -n -F "'"\\\\ref{"'$k}" chapters; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
comm: /tmp/labels_norm_all_now.txt: No such file or directory
exec
/bin/zsh -lc "rg -o --no-filename '\\\\ref\\{["'^}]+'"\\}' chapters | sed 's/"'^'"\\\\ref{//; s/}"'$//'"' | sort -u > /tmp/refs_norm_now.txt
rg -o --no-filename '\\\\label\\{["'^}]+'"\\}' . | sed 's/"'^'"\\\\label{//; s/}"'$//'"' | sort -u > /tmp/labels_norm_all_now.txt
comm -23 /tmp/refs_norm_now.txt /tmp/labels_norm_all_now.txt" in /Users/raeez/chiral-bar-cobar succeeded in 144ms:
chap:modular-koszul
prop:heisenberg-kappa
prop:pixton-genus2-planted-forest
rem:free-field-three-theorems
rem:w-algebra-three-theorems
sec:concordance-holographic-programme
sec:concordance-three-tier-r-matrix
sec:sl3-bar-table
thm:bar-cobar-path-integral-heisenberg
thm:heisenberg-bar-complex-genus0
thm:hook-type-transport-koszul-duality
thm:modular
thm:rtt-all-types

thinking
**Resolving parallel call issues**

I’m noticing a race issue with my parallel calls, so I need to rerun the second one. This leaves me with 13 unresolved unique labels, which is good! I’ll drop the ones related to thqg, so the final report won’t include them. Now, I just need to get the occurrences sorted out for clarity. Let's get things organized correctly!
exec
/bin/zsh -lc 'for k in $(cat /tmp/refs_norm_now.txt | comm -23 - /tmp/labels_norm_all_now.txt); do echo "=== $k ==="; rg -n -F "'"\\\\ref{"'$k}" chapters; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== chap:modular-koszul ===
chapters/theory/derived_langlands.tex:1515:(Chapter~\ref{chap:modular-koszul},
=== prop:heisenberg-kappa ===
chapters/examples/y_algebras.tex:340: \textup{(}Proposition~\textup{\ref{prop:heisenberg-kappa}}\textup{)}.
=== prop:pixton-genus2-planted-forest ===
chapters/examples/lattice_foundations.tex:1714:(Proposition~\ref{prop:pixton-genus2-planted-forest})
=== rem:free-field-three-theorems ===
chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).
=== rem:w-algebra-three-theorems ===
chapters/examples/landscape_census.tex:1467:Remark~\ref{rem:w-algebra-three-theorems} (W-algebras),
chapters/examples/landscape_census.tex:4016: (Remark~\ref{rem:w-algebra-three-theorems}).
=== sec:concordance-holographic-programme ===
chapters/examples/y_algebras.tex:855:(\S\ref{sec:concordance-holographic-programme}), the junction
=== sec:concordance-three-tier-r-matrix ===
chapters/examples/y_algebras.tex:640:(\S\ref{sec:concordance-three-tier-r-matrix}): it is
=== sec:sl3-bar-table ===
chapters/examples/bar_complex_tables.tex:4153:Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
chapters/examples/bar_complex_tables.tex:4198:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
=== thm:bar-cobar-path-integral-heisenberg ===






thinking
**Verifying candidate labels**

I need to verify the candidate replacement labels, especially for the proposition. I’ve already checked most, but I need to find the actual label for `prop:virasoro-shadow-coefficients`, and it seems the necessary file may be absent. I’ve noted that since certain items were dropped, I don't need to worry about them. I should confirm the existence of other theorems within the current repository, particularly checking various theorems' actual conjecture labels.
thinking
**Reviewing context and unresolved references**

I need to gather context from `lattice_foundations 1714`, as well as `chapters/examples/landscape_census.tex` at lines 1465 and 4016. I'll also check `chapters/connections/outlook.tex:276` and `chapters/theory/higher_genus_modular_koszul.tex:15142`. Additionally, it might be worth including a second-order issue related to the free fields theorem, mentioning the conjecture. That seems to align with what the user is asking. Lastly, the unresolved section on `y_algebras` could relate to `frontier_modular_holography_platonic.tex`, which I should verify is in the current repository.
thinking
**Summarizing findings and adjustments**

I've checked and found 18 items with 13 key findings. I might need to consider mentioning a shell command bug, as the user may expect precise compliance. However, the naive command could falsely return all references. I could briefly add a candidate fix for `chap:modular-koszul`, suggesting replacing it with `Chapter\ref{chap:higher-genus}`. There are other propositions and remarks to address, like improving `prop:heisenberg-kappa` and `rem:free-field-three-theorems` too.
thinking
**Updating references**

I need to replace both references in the text with `\S\ref{sec:w-five-theorems}` and change `three-theorem synthesis` to `five-theorem verification`. It might also be worth checking lines 4016 and 3978 to see if they need the same update. That sounds good! I could consider whether separating these changes is necessary, but one bullet point should suffice. It feels great to clarify these details!
thinking
**Considering documentation issues**

I realize that the label won't affect TeX directly, but it does complicate grep-based audits and planning for future relabeling. To resolve this, I should either delete `\ref{thm:modular}` from the comment or completely rewrite the comment without mentioning any label reference. It’s important to keep things clear and organized to avoid confusion later on!
thinking
**Clarifying unresolved references**

I’m considering how to address the issue of unresolved references. My thought is to summarize by stating: “Checked 18 current unresolved-ref occurrences after normalizing \ref/\label keys.” I think clarity is essential here. I might state findings as “Findings: 13 | Verdict: FAIL.” I need to mention that the live source is only `conj:bar-cobar-path-integral-heisenberg`. I wonder if including other label locations adds unnecessary length, but grounding might be beneficial. I’ll aim to keep things concise in the final lines.
codex
- [CRITICAL] chapters/examples/free_fields.tex:5087 — PROBLEM: `thm:bar-cobar-path-integral-heisenberg` has no live label, and line 5098 repeats it inside the proof; the only live target is the conjecture `conj:bar-cobar-path-integral-heisenberg` in `chapters/connections/feynman_connection.tex`, so item `(iii)` of a `\ClaimStatusProvedHere` theorem is being justified by conjectural material. FIX: delete item `(iii)` from `thm:bar-string-integrand`, delete the sentence beginning `Item~(iii) is proved...` from the proof, and reintroduce the free-boson path-integral claim as a post-theorem `remark`/`evidence` paragraph citing `Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg}`.

- [HIGH] chapters/examples/heisenberg_eisenstein.tex:306 — PROBLEM: the proof cites dead `thm:heisenberg-bar-complex-genus0` and then uses `\S\ref{thm:frame-heisenberg-koszul-dual}`, i.e. a section symbol against a theorem label. FIX: replace `(Theorem~\ref{thm:heisenberg-bar-complex-genus0}, \S\ref{thm:frame-heisenberg-koszul-dual})` with `(Theorem~\ref{thm:frame-heisenberg-koszul-dual})`.

- [MEDIUM] chapters/theory/derived_langlands.tex:1515 — PROBLEM: `chap:modular-koszul` is dead. The live enclosing chapter for `thm:shadow-connection` is `chap:higher-genus`. FIX: replace `Chapter~\ref{chap:modular-koszul}` with `Chapter~\ref{chap:higher-genus}`.

- [MEDIUM] chapters/examples/y_algebras.tex:340 — PROBLEM: `prop:heisenberg-kappa` is dead; the sentence is invoking the Heisenberg identity `\kappa(\mathcal H_\kappa)=\kappa`, whose live support is `thm:modular-characteristic` together with `conv:heisenberg-kappa-notation`. FIX: replace `Proposition~\ref{prop:heisenberg-kappa}` with `Theorem~\ref{thm:modular-characteristic} and Convention~\ref{conv:heisenberg-kappa-notation}`.

- [MEDIUM] chapters/examples/lattice_foundations.tex:1714 — PROBLEM: `prop:pixton-genus2-planted-forest` is dead; the explicit genus-2 planted-forest formula is live at `eq:planted-forest-genus2-explicit-bridge` inside `thm:pixton-mc-genus2`. FIX: replace `Proposition~\ref{prop:pixton-genus2-planted-forest}` with `equation~\eqref{eq:planted-forest-genus2-explicit-bridge}`.

- [MEDIUM] chapters/examples/landscape_census.tex:1465 — PROBLEM: `rem:free-field-three-theorems` is dead here and again at line 3978; the live synthesis remark is `rem:free-field-five-theorems`, and the current prose misstates the surface as “three-theorem”. FIX: replace both citations with `Remark~\ref{rem:free-field-five-theorems}` and change `three-theorem synthesis` to `five-theorem verification`.

- [MEDIUM] chapters/examples/landscape_census.tex:1467 — PROBLEM: `rem:w-algebra-three-theorems` is dead here and again at line 4016; the live W-algebra synthesis surface is `sec:w-five-theorems`, not a remark. FIX: replace both citations with `\S\ref{sec:w-five-theorems}` and change `three-theorem synthesis` to `five-theorem verification`.

- [MEDIUM] chapters/examples/y_algebras.tex:640 — PROBLEM: `sec:concordance-three-tier-r-matrix` is dead; the classification being cited lives at `def:three-tier-r-matrix`. FIX: replace `(\S\ref{sec:concordance-three-tier-r-matrix})` with `(Definition~\ref{def:three-tier-r-matrix})`.

- [MEDIUM] chapters/examples/y_algebras.tex:855 — PROBLEM: `sec:concordance-holographic-programme` is dead; the sentence points to the definition of the holographic modular Koszul datum, whose live label is `def:holographic-modular-koszul-datum`. FIX: replace `(\S\ref{sec:concordance-holographic-programme})` with `(Definition~\ref{def:holographic-modular-koszul-datum})`.

- [MEDIUM] chapters/examples/bar_complex_tables.tex:4153 — PROBLEM: `sec:sl3-bar-table` is dead here and again in the caption at line 4198; the live `\widehat{\mathfrak{sl}}_3` cohomology discussion is `sec:sl3-spectral-sequence`. FIX: replace both occurrences with `\S\ref{sec:sl3-spectral-sequence}`; at line 4153 also change `Section ... satisfy` to `Section ... satisfies`.

- [MEDIUM] chapters/connections/outlook.tex:276 — PROBLEM: `thm:hook-type-transport-koszul-duality` is dead; the live result is `thm:hook-transport-corridor`. FIX: replace the citation with `Theorem~\ref{thm:hook-transport-corridor}`.

- [MEDIUM] chapters/examples/yangians_foundations.tex:1228 — PROBLEM: `thm:rtt-all-types` is dead here and again in `chapters/examples/yangians_computations.tex:1150`; the live theorem is `thm:rtt-all-classical-types`. FIX: replace both citations with `Theorem~\ref{thm:rtt-all-classical-types}` and keep `(iv)` on the foundations line.

- [LOW] chapters/theory/higher_genus_modular_koszul.tex:15142 — PROBLEM: the commented line still contains dead `\ref{thm:modular}`. It will not break TeX, but it does poison grep-based audits and future relabeling. FIX: delete `\ref{thm:modular}` from the comment or rewrite the comment without any label reference.

## Summary
Checked: 18 | Findings: 13 | Verdict: FAIL
tokens used
547,034
