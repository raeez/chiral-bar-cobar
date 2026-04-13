# F18_dangling_refs_v2 (1429s)

Full findings are in [vol2_chapters_unresolved_refs_report.md](/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md). The report is line-accurate and formatted exactly as requested: `[SEVERITY] file:line — PROBLEM: ... FIX: ...`.

I audited the full ref surface inside `~/chiral-bar-cobar-vol2/chapters/` and included `\ref`, `\eqref`, `\autoref`, `\cref`, `\Cref`, and `\pageref`, since they all hit the same label-resolution surface. The verified breakdown is:

- `232` same-file deleted anchors: the file still contains `% label removed: ...` but the prose still cites the dead label.
- `941` hidden imports from outside `chapters/`: mostly `main.tex` phantom labels and one appendix label.
- `132` missing `V1-*` aliases: the live Vol I label exists, but Vol II never created the bridge alias.
- `46` residual stale-name/orphan cases: wrong prefix, wrong local target, dead archived Vol I target, or a forward reference to a section/remark that does not exist.

## Summary
Checked: 7881 | Findings: 1351 | Verdict: FAIL


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
session id: 019d865c-d87b-7470-bf07-69e6f5167870
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


MISSION: FOUNDATION AUDIT of 

Same for Vol II. Find all \ref{} that don't resolve in ~/chiral-bar-cobar-vol2/chapters/.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Planning the audit process**

I'm focusing on the user's request for auditing unresolved references in the Vol II chapters. I'll need to inspect the repository and follow the AGENTS instructions closely. Reading files like CLAUDE.md and theorem_registry.md is essential. The user's specific request suggests we may use the deep-beilinson-audit skill. It looks like my focus is on identifying unresolved `\ref{}` without needing to fix them immediately. I'll ensure to gather findings with exact fixes as requested, but I might clarify this first.
thinking
**Clarifying audit instructions**

For this special user request, since they're asking for an audit, I need to focus on findings rather than making edits unless specifically requested. They want me to provide exact fixes for each finding, but typically, a review doesn't involve implementation. My focus will be on grounding my findings in the actual file contents and thoroughly auditing the surface. 

I'll inspect the Vol II chapters, possibly using tools like build, grep, or latexmk to gather unresolved `\ref{}` commands and ensure I identify them accurately along with their exact locations.
thinking
**Clarifying workspace permissions**

This task is an audit rather than an edit, but it's possible that I still need to provide substantial findings. Since the workspace-write includes only the current repository, I initially wondered if I could access Vol II since it might be outside. However, it appears I can read files in Vol II. The sandbox mode permits reading files, so I’ll confirm I can access those necessary documents. I might also consider using an explorer agent for further navigation.
codex
Using `deep-beilinson-audit` for a repository-grounded hostile audit, then `build-surface` only if I need build evidence to confirm unresolved references. First step is to read the required constitutional files in Vol I and the audit skill, then I’ll enumerate `\ref{}` targets and labels in Vol II `chapters/` and verify each unresolved hit against actual source lines.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2836 |
| Total tagged claims | 3665 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2836 |
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

 succeeded in 54ms:
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
**Planning the audit**

I need to audit unresolved references in volume 2 chapters. It would help if I read skill build-surface while gathering evidence. I think the next step is inspecting the volume 2 structure and getting a list of chapter files, labels, and references, maybe utilizing rg. Since this is a substantial task, I'll plan for it and include a longer plan with a scope lock. Commentary on the scope and initial results could be useful. I might consider using update_plan for this. Let's set the plan in motion!
codex
Scope lock: Vol II `~/chiral-bar-cobar-vol2/chapters/`, unresolved `\ref`/`\eqref`-style label targets inside that tree only. I’m building the target set from actual `\label{}` definitions and the reference set from actual `\ref{}` usages, then I’ll inspect every missing target in context, hunt for second-order alias/misnaming patterns, and only report findings that survive a line-by-line recheck.
Plan update
Hostile audit of unresolved reference targets in Vol II chapters, grounded in source lines only.
  → Enumerate all labels and reference commands in Vol II chapters
  • Identify unresolved targets and inspect each source location in context
  • Search for intended nearby labels or duplicate naming patterns to derive exact fixes
  • Re-verify surviving findings and produce line-accurate audit report



thinking
**Considering reference labels**

I need to enumerate labels and references, possibly using regular expressions. It looks like I could use multi-tool parallel processing. The user is asking for all \ref{} commands, so I should search for relevant commands like \ref, \eqref, and \Cref. To be cautious, I might focus on all label references. The user specifically mentioned unresolved \ref{}, which might also cover unresolved \eqref. I’m thinking I should audit any command that ends with "ref".
thinking
**Collecting reference data**

I need to gather all labels and ref commands from the chapters, focusing on \eqref and \ref since they might be unresolved. The user explicitly asked for \ref{}. I should check commands like `\Cref` and `\cref` if they're used. It might be handy to use a parsing script, possibly employing `rg -n` to search for patterns, but since simple shell commands might suffice, I’ll stick to those initially. I also need to inspect the /chiral-bar-cobar-vol2/chapters/ directory for any required data.
thinking
**Considering unresolved references**

I think I need to treat references to labels defined outside the chapters, like in frontmatter or appendices, as unresolved within this context. It seems that I should either define the labels within the chapters or adjust the references to point to existing labels. It’s essential to focus on what’s unresolved within the chapters themselves, even if the build might resolve labels from other sections. I need to ensure I’m aligning with the user's scope effectively.
exec
/bin/zsh -lc 'rg --files /Users/raeez/chiral-bar-cobar-vol2/chapters' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -o '\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -o '\\\\label\\{["'^}]+'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex
 succeeded in 52ms:
Total output lines: 7879

/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:4:\ref{thm:one-loop-koszul}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:4:\ref{thm:ds-koszul-obstruction}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:47:\ref{def:log-SC-algebra}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:47:\ref{thm:physics-bridge}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:95:\eqref{eq:KZ-action}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:135:\ref{def:log-SC-algebra}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:136:\eqref{eq:vir-propagator}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:136:\eqref{eq:vir-lambda-bracket}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:164:\eqref{eq:vir-lambda-bracket}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:174:\ref{def:log-SC-algebra}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:221:\ref{thm:resolvent-principle}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:222:\eqref{eq:resolvent-tree-formula}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:233:\ref{thm:tree-wheel-bridge}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:237:\ref{thm:one-loop-koszul}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:239:\ref{cor:koszul-resolvent}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:241:\ref{thm:ds-koszul-obstruction}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:264:\ref{def:shadow-depth-intersection}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:314:\ref{subsec:gravity-shadow-tower}
 succeeded in 51ms:
Total output lines: 4722

/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:2:\label{sec:examples_complete_conditional}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:18:\label{ex:nonabelian_CS_complete}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:31:\label{eq:su2-cs-action}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:52:\label{eq:su2-brst}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:64:\label{eq:su2-propagator}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:82:\label{prop:su2-lambda-bracket}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:86:\label{eq:su2-lambda}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:113:\label{prop:su2-m3}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:118:\label{eq:su2-m3}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:139:\label{eq:su2-m3-explicit}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:186:\label{prop:su2-truncation}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:244:\label{thm:su2-pva}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:269:\label{thm:su2-yangian}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:279:\label{eq:su2-rmatrix}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:322:\label{prop:su2-curvature}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:325:\label{eq:su2-curvature}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:348:\label{subsubsec:su2-verification}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:352:\label{prop:su2-hypotheses}



thinking
**Planning a systematic extraction**

I see that we have a huge output that needs robust extraction. I think using a Python script to gather labels and references makes sense. The goal is to list unresolved issues and identify their line numbers.

It could turn out that there are dozens or even hundreds of unresolved references. I feel like the user might expect a comprehensive report, so I need to ensure we cover everything thoroughly. I’ll focus on unresolved references and look for similarities in labels to find potential fixes systematically.
thinking
**Exploring label resolution options**

I’m thinking about how to compute the nearest existing labels. If I find a nearby label, I could propose fixes like "change to X" or "define label X at [file:line]." However, since the user wants an exact fix, I need to consider whether to rename a reference or add a missing label. 

I also need to inspect the context to choose the best option. For references outside chapters, there might be some intentional cross-volume labels that could complicate things. It seems like the user wants a clear resolution for missing definitions or unresolved references.
thinking
**Focusing on label sets**

I'm considering whether to build a label set specifically for chapters, focusing on unresolved references within those chapters. There could be hundreds of these to inspect, so I think generating a report will be essential. I might leave out references like `part:` since they likely belong in `main.tex` and fall outside the chapters' scope. 

For exact fixes, I could suggest moving the `\label{part:...}` into a chapter file or replacing the reference with hard text if that’s appropriate for the audit. The user also wants to find all unresolved references in Volume II, so I can keep track of those too.
codex
The raw surface is large, so I’m switching from grep output to a parser: actual `\label{}` set versus actual `\ref`-family targets inside Vol II `chapters/`. After that I’ll classify each miss as typo, stale rename, cross-volume leak, or non-chapter import, and only then I’ll write fixes.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, json
from collections import defaultdict
root='/Users/raeez/chiral-bar-cobar-vol2/chapters'
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
labels=defaultdict(list)
refs=[]
for dp, _, fns in os.walk(root):
    for fn in fns:
        if not fn.endswith('.tex'): continue
        path=os.path.join(dp, fn)
        with open(path,'r',encoding='utf-8') as f:
            for i,line in enumerate(f,1):
                for m in label_pat.finditer(line):
                    labels[m.group(1)].append((path,i,line.rstrip('\\n')))
                for m in ref_pat.finditer(line):
                    refs.append((path,i,m.group(1),m.group(2),line.rstrip('\\n')))
missing=[]
for r in refs:
    if r[3] not in labels:
        missing.append(r)
print('labels',len(labels))
print('refs',len(refs))
print('missing',len(missing))
# summary by prefix target
from collections import Counter
prefix=Counter(t.split(':',1)[0] if ':' in t else 'NO_PREFIX' for _,_,_,t,_ in missing)
for k,v in prefix.most_common(40):
    print(f'{k}\\t{v}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 157ms:
labels 4614
refs 7879
missing 1380
V1-thm	259
thm	151
V1-eq	138
part	131
eq	127
V1-prop	108
V1-def	69
V1-rem	52
V1-lem	42
V1-cor	41
def	35
V1-subsec	32
prop	30
sec	22
V1-constr	14
V1-sec	14
rem	11







thinking
**Considering missing references**

I’m dealing with 1380 missing references in the chapters-only label set. The task is to find all unresolved `\ref{}` calls in a specified directory. This is a hefty number of findings, and it might be best to group them, but the output contract specifies separate bullets for each finding. I'm wondering if there are duplicates that could help streamline the output. Each unresolved target may not need its own line; could I summarize them instead and create a report file for the user?
thinking
**Exploring report options**

I’m considering creating a local report file to document the findings, which would help since the final instructions suggest keeping the output under 50-70 lines, but including a link to the report is possible. The user wants all findings listed, so it might make sense to write a full report and summarize it in the final output with the link. I can create a Markdown report with all findings while ensuring my final answer contains the essential details. It seems practical to produce the report directly given the sheer number of findings.
thinking
**Considering output length and audit needs**

I’m thinking about producing the output directly, but with 1380 lines and potentially 100k tokens, it might overwhelm the user. The developer advises against overloading the response, but since the user wants a thorough audit, creating the file seems practical. I might consider using an explorer agent, but a manual script should suffice. I need to derive precise fixes by inspecting the missing references and intended labels, especially since many might be cross-volume references beginning with `V1-...`. I’ll need to locate corresponding labels in Volume I or their local equivalents.
thinking
**Searching for labels**

I think about searching the whole Volume II repository or all three volumes to find where the missing targets might exist. This would definitely help with classification. If a target exists outside the chapters or in Volume I, I could fix it by importing the file or renaming the reference to the local label. I wonder if many missing references might be due to labels lacking the `V1-` prefix. For those labels, an exact fix could involve adding a local alias immediately after the theorem.
thinking
**Resolving references in chapters**

To tackle the unresolved reference issue in chapters-only context, I could define a local alias. If it's genuinely cross-volume, I might need to convert the reference to literal text or properly externalize it. My first step would be to check if the exact target exists anywhere in Volume II outside the chapters. If it does, I wonder if I should move it into the chapters or add a duplicate label. I also need to search if similar targets exist in Volume I or if I find close matches in Volume II chapters.
thinking
**Fixing cross-volume references**

If a label exists only in Volume I, the precise fix would be to mention the cross-volume reference directly in the text without using `\ref`, or I could establish an external document link. The user is looking for an exact resolution here. Since there are many duplicates, perhaps I could automate the process to check for local base labels and recommend dropping the `V1-` prefix. For `part:*` labels, which are likely in `main.tex`, I might need to move them into the first chapter or create a stub in the chapters to ensure they're resolved correctly.
thinking
**Searching for fixes**

I think I need to search for targets in the full repository to find exact fixes. I could script to check if a local label exists. If it doesn’t, I should look outside chapters in volume 2, and also include volumes 1 and 3 in my search. I want to gather a unique count of the missing targets first. Then, I might write a script to search all the relevant .tex files across these volumes.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict, Counter
root='/Users/raeez/chiral-bar-cobar-vol2/chapters'
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
labels=set()
refs=[]
for dp,_,fns in os.walk(root):
    for fn in fns:
        if fn.endswith('.tex'):
            path=os.path.join(dp,fn)
            text=open(path,encoding='utf-8').read().splitlines()
            for i,line in enumerate(text,1):
                labels.update(m.group(1) for m in label_pat.finditer(line))
                refs.extend((path,i,m.group(1),m.group(2),line.strip()) for m in ref_pat.finditer(line))
missing=[r for r in refs if r[3] not in labels]
by_target=defaultdict(list)
for r in missing: by_target[r[3]].append(r)
print('missing uses',len(missing))
print('unique missing targets',len(by_target))
for target, items in sorted(by_target.items(), key=lambda kv:(-len(kv[1]), kv[0]))[:200]:
    print(f'{len(items):3d}\\t{target}\\t{items[0][0]}:{items[0][1]}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 193ms:
missing uses 1380
unique missing targets 773
 32	part:swiss-cheese	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex:126
 22	part:e1-core	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:157
 21	part:bbl-core	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1404
 21	part:examples	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:691
 16	V1-rem:sc-higher-genus	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:1937
 13	part:gravity	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2307
 12	V1-lem:degree-cutoff	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:802
 12	part:holography	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2272
 10	part:frontier	/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2103
  9	V1-thm:recursive-existence	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:816
  8	V1-eq:thqg-VII-genus-g-mc-eq	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_bootstrap.tex:458
  7	V1-prop:independent-sum-factorization	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1081
  7	V1-rem:virasoro-resonance-model	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:18
  7	V1-thm:collision-residue-twisting	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:420
  6	V1-thm:genus-universality	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:478
  6	V1-thm:lattice:curvature-braiding-orthogonal	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1907
  6	V1-thm:modular-characteristic	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:462
  6	V1-thm:thqg-IV-theta-duality	/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:362

thinking
**Examining reference issues in LaTeX**

I’m looking at how to handle a situation where a base target only exists in vol1. Either I should remove `V1-`, but only if the local reference is absent. I wonder if I could add an alias in vol2 for a duplicate theorem with a slightly different name. 

If the target starts with `part:` and exists in vol2, I should fix it by adding a local chapter label or using literal text. I might change `\ref{part:examples}` to `Part II`, though I need to check part numbering for accuracy. If there are no targets and similar labels in chapters, I could suggest renaming to fit. If the target is truly orphaned, I might have to find the intended label based on context. I’ll search the labels in main.tex and count classifications.
codex
I’ve confirmed this is not a handful of typos. There are `1380` unresolved chapter-local reference uses hitting `773` distinct missing targets, with four dominant failure modes already visible: Vol I leakage (`V1-*`), hidden imports from `main.tex` (`part:*`), stale local label renames, and genuinely orphaned targets.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict, Counter
roots={
 'v2_chapters':'/Users/raeez/chiral-bar-cobar-vol2/chapters',
 'v2_all':'/Users/raeez/chiral-bar-cobar-vol2',
 'v1_all':'/Users/raeez/chiral-bar-cobar',
 'v3_all':'/Users/raeez/calabi-yau-quantum-groups',
}
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
labels={k:defaultdict(list) for k in roots}
for name, root in roots.items():
    for dp,_,fns in os.walk(root):
        for fn in fns:
            if fn.endswith('.tex'):
                path=os.path.join(dp,fn)
                try:
                    with open(path,encoding='utf-8') as f:
                        for i,line in enumerate(f,1):
                            for m in label_pat.finditer(line):
                                labels[name][m.group(1)].append((path,i,line.strip()))
                except Exception:
                    pass
# missing targets from v2_chapters refs
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
refs=[]
for dp,_,fns in os.walk(roots['v2_chapters']):
    for fn in fns:
        if fn.endswith('.tex'):
            path=os.path.join(dp,fn)
            with open(path,encoding='utf-8') as f:
                for i,line in enumerate(f,1):
                    for m in ref_pat.finditer(line):
                        refs.append((path,i,m.group(1),m.group(2),line.strip()))
missing=sorted({r[3] for r in refs if r[3] not in labels['v2_chapters']})
# classify
cats=Counter()
for t in missing:
    if t in labels['v2_all'] and t not in labels['v2_chapters']:
        cats['vol2_nonchapter']=1+cats['vol2_nonchapter']
    elif t.startswith('V1-'):
        base=t[3:]
        if base in labels['v2_chapters']:
            cats['v1prefix_localbase']=1+cats['v1prefix_localbase']
        elif base in labels['v1_all']:
            cats['v1prefix_vol1only']=1+cats['v1prefix_vol1only']
        else:
            cats['v1prefix_orphan']=1+cats['v1prefix_orphan']
    elif t in labels['v1_all']:
        cats['vol1_plain']=1+cats['vol1_plain']
    elif t in labels['v3_all']:
        cats['vol3_plain']=1+cats['vol3_plain']
    else:
        cats['orphan_or_rename']=1+cats['orphan_or_rename']
print(cats)
# print examples per cat
for cat in cats:
    print('\\nCAT',cat)
    n=0
    for t in missing:
        cond=False
        if cat=='vol2_nonchapter': cond=(t in labels['v2_all'] and t not in labels['v2_chapters'])
        elif cat=='v1prefix_localbase': cond=(t.startswith('V1-') and t[3:] in labels['v2_chapters'])
        elif cat=='v1prefix_vol1only': cond=(t.startswith('V1-') and t[3:] not in labels['v2_chapters'] and t[3:] in labels['v1_all'])
        elif cat=='v1prefix_orphan': cond=(t.startswith('V1-') and t[3:] not in labels['v2_chapters'] and t[3:] not in labels['v1_all'])
        elif cat=='vol1_plain': cond=(t in labels['v1_all'])
        elif cat=='vol3_plain': cond=(t in labels['v3_all'])
        elif cat=='orphan_or_rename': cond=(t not in labels['v2_all'] and (not t.startswith('V1-') or (t[3:] not in labels['v1_all'] and t[3:] not in labels['v2_chapters'])) and t not in labels['v1_all'] and t not in labels['v3_all'])
        if cond:
            print(t)
            n+=1
            if n>=20: break
PY" in /Users/raeez/chiral-bar-cobar succeeded in 13.38s:
Counter({'vol2_nonchapter': 466, 'orphan_or_rename': 204, 'v1prefix_vol1only': 98, 'vol1_plain': 2, 'vol3_plain': 1})

CAT vol2_nonchapter
V1-chap:yangians
V1-comp:holographic-ss-vir
V1-comp:thqg-I-hs-fermion
V1-comp:thqg-I-hs-heisenberg
V1-comp:thqg-V-affine-yangian
V1-comp:thqg-V-quartic-graviton
V1-comp:vir-physical-cc
V1-conj:master-bv-brst
V1-conj:thqg-I-non-perturbative
V1-const:vol1-genus-spectral-sequence
V1-constr:clifford-spectral
V1-constr:nms-sewing-product
V1-constr:obstruction-recursion
V1-constr:thqg-III-verdier-involution
V1-constr:thqg-V-binary-extraction
V1-constr:thqg-VII-mc-recursion
V1-conv:higher-genus-differentials
exec
/bin/zsh -lc "rg -n '\\\\label\\{V1-chap:yangians\\}|\\\\label\\{part:swiss-cheese\\}|\\\\label\\{app:brace-signs\\}|\\\\label\\{chap:ordered-associative-chiral-kd\\}|\\\\label\\{thm:bar-cobar-isomorphism-main\\}' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:bar-cobar-isomorphism-main\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:408:\phantomsection\label{V1-chap:yangians}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:773:\phantomsection\label{thm:bar-cobar-isomorphism-main}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1210:\label{part:swiss-cheese}
/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2:\label{app:brace-signs}
exec
/bin/zsh -lc "rg -n '\\\\label\\{chap:ordered-associative-chiral-kd\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 115ms:
/Users/raeez/chiral-bar-cobar/compute/audit/theorem_a_b_tautology_verification.md:21:\label{thm:bar-cobar-isomorphism-main}
 exited 1 in 115ms:







thinking
**Generating a systematic report**

I’m considering using an explorer tool, but I think I can proceed without it. The plan is to create a full report file highlighting all the missing references and suggesting fixes. I need to be very systematic and thorough with each finding. The user mentions being harsh on any unresolved references or hidden imports in Vol II. It sounds like this will be a thorough review focusing mainly on those unresolved references and necessary imports. I might need a parser for this task.
thinking
**Creating a structured markdown report**

I’m considering creating a markdown report file either in the current repository or maybe in the /tmp directory. I need to examine each category to create fix templates. For instance, I'll look into the `vol2_nonchapter` category, which includes target labels existing in Vol II but not in `chapters/`. These references could indicate hidden imports. The fix might involve moving labels from `main.tex` or appendices into the appropriate chapter files, or possibly duplicating them in chapter files as needed.
thinking
**Determining exact fixes for references**

I’m thinking about whether the exact fix for the reference should be to change `\ref{app:brace-signs}` to `Appendix\\ref{app:brace-signs}` and include the appendices in the audit surface. However, that doesn't seem sufficient. Since the label exists outside of the chapters, the better fix might be to either move `appendices/brace-signs.tex` into the chapters or avoid referencing it from within the chapters. But I worry that this might be too broad of a solution.
thinking
**Fixing TeX labels**

It seems like the best way to address the hidden import issue is to add a mirror `\label` in the chapter where the referenced item is first introduced. I need to identify that chapter or section, but with `part:*`, it might be tricky. Could we use `\hypertarget`? However, I need to remember that duplicate labels cause warnings and might lead to ambiguous references, which isn’t ideal. 

I could consider setting category severity to HIGH and suggest moving the label definition to the first included chapter of that part, then deleting the phantom label from `main.tex`. This approach seems precise and avoids duplication. For `part:*`, if they’re defined in `main.tex`, they should also be moved to the introduction or the first chapter of that part. I’ll need to determine which chapter corresponds to each part and inspect `main.tex` around the relevant sections.
thinking
**Organizing part references**

It looks like there are about 131 references across several part labels, but only around 6 distinct part labels. I could report each usage of these or perhaps focus on each hidden import label along with all the usage lines. Since the user wants each finding, we might want to consider reporting per missing target instead, aggregating all usages together. This might provide a clearer picture of where everything stands without overwhelming details.
thinking
**Evaluating script usage and classifications**

I’m considering how to handle lines that don't resolve. It might make sense to create a report file that lists each instance. Instead of manually inspecting all 1,380 lines, I could use a script for initial findings and then spot-check to verify accuracy. Since the user wants this grounded in the actual file contents, I need to ensure the script verifies each finding and provides context for the fixes. I’ll also check examples from specific categories for validation.
codex
I’ve finished the first pass classification. Before I write the final findings, I’m spot-checking representative misses from each failure mode against the actual surrounding prose so the fixes are not generic guesses.
exec
/bin/zsh -lc "sed -n '1932,1944p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,170p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1398,1410p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,250p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
coalgebra element: it lives in $H^{2}(\overline{\cM}_g)$ via
the Hodge bundle, and its primitivity in $B_\Theta^{(g)}(\cA)$
is the statement that the
period-corrected differential
$\Dg{g}$ of Volume~I,
Remark~\ref{V1-rem:sc-higher-genus}\textup{(iii)}, is a
coderivation of~$\Delta$. The fibrewise differential
$\dfib$ is \emph{not} a coderivation
(Volume~I,
Remark~\ref{V1-rem:sc-higher-genus}\textup{(ii)}); only after
the Fay trisecant period correction does the curved
$E_1$ dg coalgebra structure persist, and only then does
the Hodge curvature class push forward to a primitive element
 succeeded in 51ms:
$\mathrm{av}\colon \mathfrak{g}^{E_1}_\cA \to
\mathfrak{g}^{\mathrm{mod}}_\cA$ is the
$\Sigma_n$-coinvariant projection (tensor coalgebra $T^c \to$
symmetric coalgebra $\Sym^c$). Volume~I's Theorems~A--D$+$H are the
invariants that survive this projection: the modular characteristic
$\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$, and the shadow
obstruction tower $(\Theta_\cA^{\le r})_{r \ge 2}$ at higher degrees.
Consequently, Part~\ref{part:e1-core} (ordered associative chiral Koszul duality,
dg-shifted factorization bridge, gravitational Yangian) is the
\emph{primary} layer of the theory; the remaining Parts describe the
modular/symmetric framework that is its $\mathrm{av}$-image.
See Volume~I, \S\textup{E$_1$ as primitive}
for the full statement.
\end{remark}

\begin{remark}[Dimensional reduction across the trilogy]
\label{rem:vol2-dimensional-reduction}
This volume operates at Level~2 of the dimensional reduction
hierarchy (Remark~\ref*{V1-rem:three-volume-dimensional-reduction}
of Volume~I): the 3d theory on $\C_z \times \R_t$, where the bar
 succeeded in 51ms:
 By Theorem~\textup{\ref{thm:bar-is-self-intersection}}\textup{(ii)},
 $\barB(\cA) \simeq \cO(\cL_\cA \times_{\Mvac}^h \cL_\cA)$:
 the bar complex is the structure sheaf of the derived
 self-intersection.
 Each tree~$\tau \in \mathrm{PRT}_k$ is a Feynman diagram
 with interaction vertices~$m_2$ and propagator lines~$h$;
 the sum over trees computes the structure constants of\/
 $\cO(\cL_\cA \times_{\Mvac} \cL_\cA)$.
\end{enumerate}
\end{theorem}

\begin{proof}
(i) is the Kadeishvili--Merkulov $\Ainf$ transfer theorem, applied
 succeeded in 51ms:
+ (-1)^{|a|}\,\bigl[m_2\!\bigl(a,m_2(b,c;\lambda_2);\lambda_1,\lambda_2\bigr)\bigr]
= -\bigl[Q\bigl(m_3(a,b,c)\bigr)\bigr] = 0.
\end{equation}

\emph{Caution}: This does \textbf{not} mean $m_2$ is associative in cohomology. Equation~\eqref{eq:n3_cohomology} states that the two $m_2 \circ m_2$ compositions differ by a $Q$-exact term (namely $m_3$). The associativity holds only as a cohomological identity, and the correction $m_3$ (which is $Q$-exact on cocycles but not zero at the chain level) must be tracked when decomposing into singular parts.

\medskip
\textbf{Step 3: Decomposition into singular and regular parts.}
The key to extracting the Jacobi identity is to analyze the \emph{singular} parts of the iterated $m_2$ compositions. Recall from \S\ref{subsec:reg-sing} that $m_2(a,b;\lambda) = m_2^{\mathrm{reg}}(a,b;\lambda) + m_2^{\mathrm{sing}}(a,b;\lambda)$, and the $\lambda$-bracket is $\{a_\lambda b\} = [m_2^{\mathrm{sing}}(a,b;\lambda)]$.

Consider the composition $m_2(m_2(a,b;\lambda_1),c;\lambda_1{+}\lambda_2,\lambda_2)$. Decomposing the inner $m_2(a,b;\lambda_1)$ into regular and singular parts:
exec
/bin/zsh -lc "rg -n '\\\\label\\{part:e1-core\\}|\\\\label\\{part:bbl-core\\}|\\\\label\\{part:examples\\}|\\\\label\\{part:gravity\\}|\\\\label\\{part:holography\\}|\\\\label\\{part:frontier\\}|\\\\label\\{part:swiss-cheese\\}' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{eq:n3_cohomology\\}|\\\\label\\{eq:n3-cohomology\\}|\\\\label\\{eq:.*n3.*cohomology.*\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{V1-rem:sc-higher-genus\\}|\\\\label\\{rem:sc-higher-genus\\}' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1210:\label{part:swiss-cheese}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1258:\label{part:e1-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1300:\label{part:bbl-core}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1325:\label{part:examples}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1370:\label{part:holography}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1403:\label{part:gravity}
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1427:\label{part:frontier}
 exited 1 in 53ms:

 succeeded in 72ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:572:\phantomsection\label{V1-rem:sc-higher-genus}%
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1468:\label{rem:sc-higher-genus}
exec
/bin/zsh -lc "rg -n '\\\\label\\{app:brace-signs\\}' /Users/raeez/chiral-bar-cobar-vol2/appendices /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/appendices/brace-signs.tex:2:\label{app:brace-signs}

thinking
**Fixing rg command issue**

I'm looking at a situation where the rg command exited with an error code of 1. This seems to be due to a missing eq label, specifically for eq:n3_cohomology. I need to find the exact solution, so it seems reasonable to search within the surrounding lines, particularly around line 230 to line 245, to see if I can identify that missing label or any other relevant details.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex | sed -n '228,242p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   228	
   229	\medskip
   230	\textbf{Step 2: Projection to cohomology.}
   231	Let $a,b,c$ be $Q$-closed representatives of classes in $H^\bullet(\A,Q)$. Then:
   232	\begin{itemize}
   233	\item Terms (II) vanish: $Qa = Qb = Qc = 0$.
   234	\item Term (I) is $Q$-exact: $Q\bigl(m_3(a,b,c)\bigr)$, so it vanishes in cohomology.
   235	\end{itemize}
   236	Therefore, in cohomology:
   237	\begin{equation}
   238	% label removed: eq:n3_cohomology
   239	\bigl[m_2\!\bigl(m_2(a,b;\lambda_1),c;\lambda_1{+}\lambda_2,\lambda_2\bigr)\bigr]
   240	+ (-1)^{|a|}\,\bigl[m_2\!\bigl(a,m_2(b,c;\lambda_2);\lambda_1,\lambda_2\bigr)\bigr]
   241	= -\bigl[Q\bigl(m_3(a,b,c)\bigr)\bigr] = 0.
   242	\end{equation}







thinking
**Determining label fixes**

It seems that the comment indicates a label has been removed, and the solution is clear: either restore the label or adjust the reference to a nearby one. There might be several cases of orphaned or renamed labels due to these removed ones. I think using comments could help identify these. I need to think about creating a pattern like "label removed" to find the exact fix by scanning for any related comments. That could be useful!
thinking
**Classifying missing labels**

I need to be more detailed in classifying missing targets. I believe I could parse through `main.tex` and the appendices to find exact labels that might be missing. For each distinct missing target, it might help to look for hidden imports, possibly relocating labels to their corresponding chapters. If a label is a phantom section alias in `main.tex`, I should consider moving it into the actual chapter file where the content is introduced. This would make those chapters more self-contained.
thinking
**Exploring label options**

I'm considering the best approach for handling label placements. Maybe I should move the label to the nearest relevant chapter file. However, this label represents a Volume I remark, not Volume II, since the existing label in Volume II just acts as a phantom alias for Volume I content. Moving it may not solve the mismatch if the content isn’t in Volume II chapters. I might need to create a local appendix section for "Cross-volume label aliases" to address the hidden imports, but it feels like a hack. The user is asking for an audit of weaknesses, which adds pressure!
thinking
**Identifying reference issues**

The problem here is that the chapters depend on invisible alias definitions in `main.tex` instead of relying on local or explicit external references. A possible fix could be to replace `\ref{V1-rem:sc-higher-genus}` with `Volume I, Remark\ref*{V1-rem:sc-higher-genus}` after loading support for external documents or even use the literal label text. But if `main.tex` already provides the alias, why is it an issue? The reference doesn't resolve within the `chapters/` folder, which indicates it’s a hidden import problem.
thinking
**Considering report generation**

I’m thinking about how to create a report for unresolved references. The idea of having one line per use is appealing, and while that could mean around 1380 lines, it might still fit in a 200k character file—totally manageable. I could generate the report in markdown format and save it to a writable repo as `reports/vol2_chapters_unresolved_refs_audit.md`. However, I’m also re-evaluating how to apply edits since the instructions emphasize using apply_patch for manual changes. Would bulk report creation with Python work here?
thinking
**Evaluating report options**

Generating a report with 773 or even 1380 lines using apply_patch seems huge, but it's possible. I could opt not to create a file, yet it might be simpler to generate a temporary file with Python and reference it in the final answer. Though, I'm hesitating because the instructions suggest avoiding Python for reading/writing files unless simpler methods like shell or apply_patch suffice. Since this report is generated, perhaps using Python is acceptable, but it still feels a bit risky to me.
thinking
**Evaluating LaTeX Label Fixes**

I’m digging into how to handle LaTeX labels in my main.tex file. If it's about prefixing with `part`, I’m thinking I could either move the label from main into the first chapter of that part or just replace the `\ref` with the actual part name. It might be simpler to keep the label in main and just replace `\ref` with `Part I` or `Part II`, but I’ll need to confirm the numbering to do that properly.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '1204,1435p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1204	\input{chapters/frame/preface}
  1205	
  1206	\input{chapters/theory/introduction}
  1207	
  1208	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1209	\part{The Open Primitive}
  1210	\label{part:swiss-cheese}
  1211	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  1212	
  1213	\noindent
  1214	The primitive datum of a three-dimensional holomorphic--topological
  1215	theory on $\C_z \times \R_t$ is not an algebra but a category: the
  1216	open/closed factorization dg-category~$\cC$ on a tangential log
  1217	curve $(X, D, \tau)$. Its objects are boundary conditions; its
  1218	morphisms are open-string states. A choice of vacuum
  1219	object~$b \in \cC$ produces an $A_\infty$-chiral algebra
  1220	$A_b = \End_\cC(b)$ as a \emph{chart}; the Morita class
  1221	of~$\cC$, not the quasi-isomorphism class of~$A_b$, is the
  1222	invariant. The governing operadic structure is the two-colored
  1223	Swiss-cheese operad~$\SCchtop$, with closed color~$\FM_k(\C)$


thinking
**Considering part references**

I need to fix references to parts by replacing them with their actual names. For instance, changing "Part\ref{part:e1-core}" to "Part II" seems best since the text already uses names. Since there are 6 parts starting after the preface, I can map them out: Part I for `part:swiss-cheese`, Part II for `part:e1-core`, and so on. However, if the numbering changes later, it could get tricky. Since the user only asked for an audit, a better fix might be to add labels within each chapter.
thinking
**Improving part references**

I'm suggesting that we replace the chapter-local `\ref{part:e1-core}` with the literal `Part II`, or we could move the part label into a chapter file. However, since hardcoding part references is not acceptable due to potential staleness, a better solution is needed. We can move `\label{part:e1-core}` to a chapter-local wrapper file, say `chapters/frame/part_e1_core_opener.tex`, which contains `\part{The $E_1$ Core}` and accompanying text. This way, references resolve correctly, and it aligns with protocol. The same approach applies to all part references.
exec
/bin/zsh -lc "rg -n '\\\\label\\{V1-thm:bar-cobar-isomorphism-main\\}' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/B01_thm_A_bridge.md:1848:/Users/raeez/chiral-bar-cobar-vol2/main.tex:928:\phantomsection\label{V1-thm:bar-cobar-isomorphism-main}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:928:\phantomsection\label{V1-thm:bar-cobar-isomorphism-main}%
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/S16_v1_to_v2_bridge.md:312:/Users/raeez/chiral-bar-cobar-vol2/main.tex:928:\phantomsection\label{V1-thm:bar-cobar-isomorphism-main}%
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/XV08_thm_status_xvol.md:330:/Users/raeez/chiral-bar-cobar-vol2/main.tex:928:\phantomsection\label{V1-thm:bar-cobar-isomorphism-main}%


thinking
**Considering appendix adjustments**

I’m considering whether to integrate appendices into the chapters or simply point to them. Since the user prefers a chapters-only format, maybe relocating the appendix file under chapters is best. Though, I could drop the reference instead. I should check for the count of `app:` labels — maybe there are only ten. I'll need to decide on an exact fix, perhaps by creating a new file or moving it, but it sounds like the user just wants a list. I'll also explore better heuristics for classification.
thinking
**Exploring label restoration**

I need to focus on restoring a label in the indicated environment or equation if found. I should search for closely related labels using methods like difflib or Levenshtein within the same file or prefix. For instance, I might compare `eq:Jacobi_assembled` with something like `eq:Jacobi_assembled_repaired`. Additionally, I could search the entire directory for the target, normalizing for hyphens, underscores, and case to find near-matches, possibly removing non-alphanumeric characters in the process.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap):ordered-associative-chiral-kd["'^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap):pva-descent["'^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'eq:Jacobi_assembled|eq:Jacobi_shifted|eq:n3_cohomology|eq:product-def|eq:m2-quantum-dz' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:37:\label{ch:ordered-associative-chiral-kd}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:38:\label{ch:ordered-associative-chiral-kd-extensions}
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex:69:\begin{equation}% label removed: eq:product-def
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex:79:The operation \eqref{eq:product-def} is independent of the choice of representatives of $[a]$ and $[b]$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex:87:where the sign $(-1)^{\degree{a}}$ on the third term is the standard Koszul sign from passing $m_1$ past $a$. This uses the fact that $Q = m_1$ commutes with the Laurent projection, since $Q$ acts on the field-algebra coefficients and does not involve the spectral parameter $\lambda$. Projecting to the regular part, we see that the change in $\Sym(m_2^{\mathrm{reg}}(a,b),m_2^{\mathrm{reg}}(b,a))$ is $Q$–exact. The same holds for $b\mapsto b+Qy$. Thus the class \eqref{eq:product-def} is independent of representatives.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex:95:Immediate from the graded symmetrization in \eqref{eq:product-def}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:188:% label removed: eq:Jacobi_shifted
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:238:% label removed: eq:n3_cohomology
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:244:\emph{Caution}: This does \textbf{not} mean $m_2$ is associative in cohomology. Equation~\eqref{eq:n3_cohomology} states that the two $m_2 \circ m_2$ compositions differ by a $Q$-exact term (namely $m_3$). The associativity holds only as a cohomological identity, and the correction $m_3$ (which is $Q$-exact on cocycles but not zero at the chain level) must be tracked when decomposing into singular parts.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:263:The Jacobi identity involves only sector (d). We therefore extract the \emph{doubly singular} part of~\eqref{eq:n3_cohomology}: singular in both the inner spectral parameter ($\lambda_1$ or $\lambda_2$) and the outer spectral parameter ($\lambda_1+\lambda_2$ or $\lambda_1$ respectively).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:267:The doubly-singular part of term (III) in~\eqref{eq:n3_cohomology} is:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:286:This involves $m_2$ applied to $\{a_{\lambda_1} b\}$ and $c$ at spectral parameter $\lambda_1 + \lambda_2$, which is $\{\{a_{\lambda_1} b\}_{\lambda_1+\lambda_2}\, c\}$, precisely the right-hand side of the Jacobi identity~\eqref{eq:Jacobi_shifted}, with the spectral substitution $\Lambda_{\{1,2\}} = \lambda_1 + \lambda_2$ producing the shifted parameter.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:290:The content of Step~4 is that the doubly-singular part of the $n=3$ identity~\eqref{eq:n3_cohomology} reads:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:319:confirming~\eqref{eq:n3_cohomology}. The chain-level operation $m_3(a,b,c)$ is a \emph{specific} homotopy witnessing the failure of strict associativity of $m_2$: it is the integral over the \emph{interior} of $\FM_3(\C)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:372:% label removed: eq:Jacobi_assembled
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:381:The identity~\eqref{eq:Jacobi_assembled} follows from Stokes' theorem on $\FM_3(\C)$ provided the codimension-2 corner contributions cancel. The codimension-2 strata of $\FM_3(\C)$ arise from pairwise intersections of the divisors $D_{\{1,2\}}$, $D_{\{1,3\}}$, $D_{\{2,3\}}$. The relevant corners are:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:394:Therefore all codimension-2 contributions vanish, and the Stokes identity receives contributions only from codimension-1 faces. This validates~\eqref{eq:Jacobi_assembled}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:398:Rearranging~\eqref{eq:Jacobi_assembled}:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:402:which is the Jacobi identity~\eqref{eq:Jacobi_shifted} for the $(-1)$-shifted PVA. The sign $(-1)^{(|a|+1)(|b|+1)}$ is the correct Koszul sign for a $(-1)$-shifted Lie bracket (the bracket has degree $-1$, so elements enter with shifted degree $|a|+1$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:414:The three terms in the Jacobi identity~\eqref{eq:Jacobi_shifted} correspond to the three codimension-1 boundary faces of $\FM_3(\C)$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:185:\begin{equation}% label removed: eq:m2-quantum-dz
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:280:The quantum correction~\eqref{eq:m2-quantum-dz} is the canonical
exec
/bin/zsh -lc "rg -n '\\\\label\\{(ch|chap|sec):["'^}]*pva[''^}]*descent[''^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:543:\label{sec:preface-pva-descent}

thinking
**Fixing chapter references**

I'm noticing there's no chapter label for "pva-descent." It seems I need to create a precise label. But maybe "chap:pva-descent" has been referenced somewhere already? I could resolve this by adding a label at the beginning of the "pva-descent-repaired" chapter or by changing the reference to "sec:preface-pva-descent." I think I need to gather a bit more context, so I'll inspect the use and potentially search for more information.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{chap:pva-descent\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2247:(PVA descent, Chapter~\ref{chap:pva-descent}). The bar complex

thinking
**Inspecting the label**

I need to inspect the label at the beginning of the pva-descent-repaired file. I’m not sure if I need to check the chapter environment or not, though. There might be some ambiguity there. I should open the file and start from there to see what's actually needed. It's important to clarify this before proceeding, so I don't miss anything relevant. Let’s get that sorted out first!
exec
/bin/zsh -lc "sed -n '1,24p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2238,2252p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\section{Cohomological descent to a shifted Poisson vertex algebra}
\label{sec:PVA_descent}
\label{sec:Ainfty-to-PVA}

The $A_\infty$ chiral algebra $(\cA, Q, \{m_k\})$ is a chain-level
object: the operations $m_k$ act on cochains, not on cohomology
classes. Passing to cohomology $H^\bullet(\cA, Q)$ strips away the
homotopical complexity (the higher operations $m_{k \geq 3}$
become $Q$-exact and vanish, Proposition~\ref{prop:m3_vanish})
and the surviving binary operation~$m_2$ descends to a
$(-1)$-shifted Poisson vertex algebra: a commutative product (from
the regular part of~$m_2$) and a skew-symmetric $\lambda$-bracket
(from the singular part) satisfying Jacobi and Leibniz. This
descent is the motivic projection of
Remark~\ref{rem:pva-depth-decomposition}: it retains the arithmetic
content of the bar complex while discarding its homotopy-theoretic
part.

Three points of the construction require emphasis.
 succeeded in 51ms:
where $P^! = (H^\bullet(\barB(P)))^\vee$ is the classical Koszul
dual PVA, $r^{\mathrm{cl}}(z)$ is the classical $r$-matrix, and
$\nabla^{\mathrm{cl}} = d - r^{\mathrm{cl}} \cdot d\log(z)$ is
the classical KZ connection.
\end{proposition}

\begin{proof}
Setting $\hbar = 0$ in the holographic modular Koszul datum:
the chiral algebra $\cA$ degenerates to the PVA $P = \gr(\cA)$
(PVA descent, Chapter~\ref{chap:pva-descent}). The bar complex
$\barB(\cA)$ degenerates to $\barB(P)$. The MC element
$\Theta_\cA$ degenerates to $\Theta^{\mathrm{cl}} = \Theta_P$,
and all projections degenerate accordingly.
\end{proof}



thinking
**Considering labeling issues**

I'm thinking that the script might need to output a message like, "FIX: add `\label{target}` to the theorem or equation being cited, since there's no matching label in Vol II chapters or other volumes." But that feels a bit speculative unless the context clarifies that it refers to something local. If nothing's found elsewhere, I could either add the label to the intended statement or rewrite the text to eliminate the `\ref`, since the exact fix isn't clear.
thinking
**Exploring automation options**

I’m thinking about how to inspect orphaned or renamed targets with automation and find nearest matches. It seems like there are a couple of options, but I want to compute the orphan targets using normalization. I’ll need to categorize them, looking at things like removed labels, prefix synonym matches, and normalized near match uniqueness. This approach could cover a lot of ground, so scripting some statistics sounds like a good plan!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, difflib
from collections import defaultdict, Counter
root='/Users/raeez/chiral-bar-cobar-vol2/chapters'
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
labels=defaultdict(list)
file_lines={}
refs=[]
for dp,_,fns in os.walk(root):
    for fn in fns:
        if fn.endswith('.tex'):
            path=os.path.join(dp,fn)
            lines=open(path,encoding='utf-8').read().splitlines()
            file_lines[path]=lines
            for i,line in enumerate(lines,1):
                for m in label_pat.finditer(line):
                    labels[m.group(1)].append((path,i))
                for m in ref_pat.finditer(line):
                    refs.append((path,i,m.group(2)))
missing=sorted(set(t for _,_,t in refs if t not in labels))
# external labels within vol2 all
all_labels=defaultdict(list)
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2'):
    for fn in fns:
        if fn.endswith('.tex'):
            path=os.path.join(dp,fn)
            for i,line in enumerate(open(path,encoding='utf-8'),1):
                for m in label_pat.finditer(line):
                    all_labels[m.group(1)].append((path,i))
# comments / normalized map
norm=lambda s: re.sub(r'["'^a-z0-9]+'"','',s.lower())
label_norm=defaultdict(list)
for lab, locs in labels.items():
    label_norm[norm(lab)].append(lab)
# prefix swap candidates
synonyms=[('chap:','ch:'),('ch:','chap:'),('rmk:','rem:'),('rem:','rmk:'),('sec:','subsec:'),('subsec:','sec:')]
counts=Counter()
examples=defaultdict(list)
for t in missing:
    found=False
    # label removed comment
    for path,lines in file_lines.items():
        txt='\\n'.join(lines)
        if f'label removed: {t}' in txt:
            counts['comment_removed']+=1
            examples['comment_removed'].append(t)
            found=True
            break
    if found: continue
    # exact outside chapters
    if t in all_labels:
        counts['vol2_outside']+=1
        examples['vol2_outside'].append(t)
        continue
    # prefix alias exact by V1-
    if ('V1-'+t) in all_labels:
        counts['v1_alias_for_plain']+=1
        examples['v1_alias_for_plain'].append(t)
        continue
    # prefix swap
    for a,b in synonyms:
        if t.startswith(a) and (b+t[len(a):]) in labels:
            counts['prefix_swap']+=1
            examples['prefix_swap'].append((t,b+t[len(a):]))
            found=True
            break
    if found: continue
    n=norm(t)
    cands=[lab for lab in label_norm[n] if lab"'!=t]
    if len(cands)==1:
        counts['"'normalized_exact']+=1
        examples['normalized_exact'].append((t,cands[0]))
        continue
    # fuzzy same prefix
    pref=t.split(':',1)[0] if ':' in t else ''
    pool=[lab for lab in labels if lab.split(':',1)[0]==pref]
    close=difflib.get_close_matches(t,pool,n=3,cutoff=0.82)
    if close:
        counts['fuzzy_same_prefix']+=1
        examples['fuzzy_same_prefix'].append((t,close[0]))
        continue
    counts['hard_orphan']+=1
    examples['hard_orphan'].append(t)
print(counts)
for cat in counts:
    print('\\n',cat)
    for x in examples[cat][:20]:
        print(x)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 9.74s:
Counter({'vol2_outside': 463, 'comment_removed': 185, 'hard_orphan': 121, 'prefix_swap': 1, 'fuzzy_same_prefix': 1})

 vol2_outside
V1-chap:yangians
V1-comp:holographic-ss-vir
V1-comp:thqg-I-hs-fermion
V1-comp:thqg-I-hs-heisenberg
V1-comp:thqg-V-affine-yangian
V1-comp:thqg-V-quartic-graviton
V1-comp:vir-physical-cc
V1-conj:master-bv-brst
V1-conj:thqg-I-non-perturbative
V1-const:vol1-genus-spectral-sequence
V1-constr:clifford-spectral
V1-constr:nms-sewing-product
V1-constr:obstruction-recursion
V1-constr:thqg-III-verdier-involution
V1-constr:thqg-V-binary-extraction
V1-constr:thqg-VII-mc-recursion
V1-conv:higher-genus-differentials
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict, Counter
# load labels all vols
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
def load(root):
    d=defaultdict(list)
    for dp,_,fns in os.walk(root):
        for fn in fns:
            if fn.endswith('.tex'):
                path=os.path.join(dp,fn)
                try:
                    for i,line in enumerate(open(path,encoding='utf-8'),1):
                        for m in label_pat.finditer(line):
                            d[m.group(1)].append((path,i))
                except Exception:
                    pass
    return d
v2ch=load('/Users/raeez/chiral-bar-cobar-vol2/chapters')
v2all=load('/Users/raeez/chiral-bar-cobar-vol2')
v1=load('/Users/raeez/chiral-bar-cobar')
# missing unique
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
missing=set()
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            path=os.path.join(dp,fn)
            for i,line in enumerate(open(path,encoding='utf-8'),1):
                for m in ref_pat.finditer(line):
                    t=m.group(2)
                    if t not in v2ch:
                        missing.add(t)
# isolate hard_orphans from prior logic simplified
hard=[]
for t in sorted(missing):
    if t in v2all: continue
    if any(f'label removed: {t}' in open(p,encoding='utf-8').read() for p in []):
        pass
# can't use previous exact. Instead classify V1-hard
for t in sorted(missing):
    if not t.startswith('V1-'): continue
    if t in v2all: continue
    base=t[3:]
    hit=''
    if base in v1: hit='base_in_v1'
    elif base in v2ch: hit='base_in_v2ch'
    elif ('V1-'+base) in v2all: hit='dbl'
    else: hit='none'
    hard.append((t,hit, v1.get(base,[])[:1], v2ch.get(base,[])[:1]))
from collections import Counter
c=Counter(x[1] for x in hard)
print(c)
for item in hard[:60]:
    print(item[0], item[1], item[2][:1], item[3][:1])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 11.30s:
Counter({'base_in_v1': 98})
V1-conj:bordered base_in_v1 [('/Users/raeez/chiral-bar-cobar/archive/source_tex/ordered_associative_chiral_koszul_duality.tex', 1306)] []
V1-conj:lattice-sewing base_in_v1 [('/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a074cd40/chapters/examples/lattice_foundations.tex', 120)] []
V1-const:vol1-modular-tangent-complex base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex', 11700)] []
V1-constr:bipartite-linfty-truncation base_in_v1 [('/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a074cd40/appendices/nonlinear_modular_shadows.tex', 2968)] []
V1-constr:platonic-package base_in_v1 [('/Users/raeez/chiral-bar-cobar/archive/raeeznotes/concordance.tex', 753)] []
V1-cor:anomaly-ratio base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex', 5863)] []
V1-cor:ds-theta-descent base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex', 2704)] []
V1-cor:envelope-universal-mc base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex', 28712)] []
V1-cor:hs-sewing-standard-landscape base_in_v1 [('/Users/raeez/chiral-bar-cobar/main.tex', 1559)] []
V1-cor:thqg-IV-shadow-depth base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_s_duality.tex', 693)] []
V1-cor:thqg-IV-twisted-tangent base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_s_duality.tex', 411)] []
V1-def:analytic-bar-coalgebra base_in_v1 [('/Users/raeez/chiral-bar-cobar/main.tex', 1713)] []
V1-def:analytic-koszul-pair base_in_v1 [('/Users/raeez/chiral-bar-cobar/main.tex', 1714)] []
V1-def:analytic-shadow base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex', 1622)] []
V1-def:coisson base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex', 79)] []
V1-def:eta-function base_in_v1 [('/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex', 381)] []
V1-def:hs-sewing base_in_v1 [('/Users/raeez/chiral-bar-cobar/main.tex', 1558)] []
V1-def:resonance-rank base_in_v1 [('/Users/raeez/chiral-bar-cobar/main.tex', 1746)] []
V1-def:sewing-envelope base_in_v1 [('/Users/raeez/chiral-bar-cobar/main.tex', 1747)] []
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '548,586p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
   548	\phantomsection\label{V1-prop:self-loop-vanishing}%
   549	\phantomsection\label{V1-prop:thqg-I-Fg-closed-form}%
   550	\phantomsection\label{V1-prop:thqg-I-graph-count}%
   551	\phantomsection\label{V1-prop:thqg-I-pants-hs}%
   552	\phantomsection\label{V1-prop:thqg-I-standard-hs}%
   553	\phantomsection\label{V1-prop:thqg-III-genus-1}%
   554	\phantomsection\label{V1-prop:thqg-III-involutivity}%
   555	\phantomsection\label{V1-prop:thqg-two-sources}%
   556	\phantomsection\label{V1-prop:thqg-V-rtt-from-sgybe}%
   557	\phantomsection\label{V1-prop:thqg-VI-kappa-action}%
   558	\phantomsection\label{V1-prop:thqg-VII-genus1}%
   559	\phantomsection\label{V1-prop:thqg-VII-genus2}%
   560	\phantomsection\label{V1-prop:thqg-VII-genus3}%
   561	\phantomsection\label{V1-prop:thqg-VII-genus4}%
   562	\phantomsection\label{V1-prop:vir-complementarity}%
   563	\phantomsection\label{V1-prop:virasoro-c26-selfdual}%
   564	\phantomsection\label{V1-rem:bcov-mc-dictionary}%
   565	\phantomsection\label{V1-rem:bv-bar-bridge}%
   566	\phantomsection\label{V1-rem:bv-bar-class-c-proof}%
   567	\phantomsection\label{V1-rem:conj-modular-resolved}%






thinking
**Analyzing citation fixes**

I need to consider that these hidden imports aren't just unresolved in chapters; they're phantom labels in the main file without a clear mathematical reference. The problem is that the chapter text relies on opaque aliases. The fix would be to replace instances of `\ref{V1-...}` with explicit citations to the correct Volume I label, using `xr-hyper`, or by restating the target theorem in Volume II with its own label. That seems like a more rigorous solution!
thinking
**Determining reference fixes**

I need to address specific findings for issues like `V1-rem:sc-higher-genus`. The problem arises because it’s unresolved in the chapters, as it depends on a phantom alias in `main.tex`. The fix involves deleting this hidden alias, loading `xr-hyper` for Volume I, and changing the reference to `\ref*{V1-rem:sc-higher-genus}` if the Volume I auxiliary is included. If not, I should restate it in Volume II with a proper label. I’m leaning towards the robust fix using `xr-hyper` external document for cross-volume references!
thinking
**Classifying report severity**

I need to clarify how to classify severity for a report. For CRITICAL issues, I’m thinking about dangling references with no targets or commented-out labels, as this can lead to unresolved builds. HIGH severity might apply to hidden imports outside chapters, which makes them non-self-contained. I’m considering MEDIUM for cross-volume references that should use the correct alias. Defining these categories feels important to set the right expectations for the user.
thinking
**Defining severity levels**

I’m thinking about simplifying to just CRITICAL, HIGH, and MEDIUM categories. To check if a full build resolves the issues, I may need to use build-surface, but the audit only covers chapters, so that might not help much. I should generate lines for all findings along with exact fixes. It could be useful to output this as a machine-generated report file, including per-use entries and the actual definition site in the fixes.
thinking
**Evaluating the document structure**

I need to fix the document by moving the `V1-*` alias block out of `main.tex` and putting it into a chapter-local file, like `chapters/frame/vol1_aliases.tex`. I'll then `\input` that before the first chapter. Alternatively, I could restate the remark in Volume II and replace the reference with a proper Volume II label. This approach is okay for a chapters-only audit, but it might not fully address the real source. The fix would be to move the alias definition from `main.tex:572` into the new file.
thinking
**Correcting citation issues**

I need to replace the citation with a live label on the current Volume I surface instead of referencing `archive/`. The problem is that the exact label might not exist, and I might need to inspect the context to make the right choice, which is tricky. Many hard orphans might be because the label only exists in archives or other areas. I may classify this as CRITICAL and consider rewriting the prose to remove that reference until the claim is reinstated.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, pathlib
pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')

def load_live(root):
    d={}
    # main.tex
    main=os.path.join(root,'main.tex')
    if os.path.exists(main):
        for i,line in enumerate(open(main,encoding='utf-8'),1):
            for m in pat.finditer(line):
                d.setdefault(m.group(1),[]).append((main,i))
    for sub in ['chapters','appendices']:
        base=os.path.join(root,sub)
        if os.path.isdir(base):
            for dp,_,fns in os.walk(base):
                for fn in fns:
                    if fn.endswith('.tex'):
                        path=os.path.join(dp,fn)
                        for i,line in enumerate(open(path,encoding='utf-8'),1):
                            for m in pat.finditer(line):
                                d.setdefault(m.group(1),[]).append((path,i))
    return d
v1=load_live('/Users/raeez/chiral-bar-cobar')
v2=load_live('/Users/raeez/chiral-bar-cobar-vol2')
# list hard V1 refs lacking live base/alias in v2
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
chlabels={}
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            p=os.path.join(dp,fn)
            for i,line in enumerate(open(p,encoding='utf-8'),1):
                for m in pat.finditer(line):
                    chlabels.setdefault(m.group(1),[]).append((p,i))
missing=sorted({m.group(2) for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters') for fn in fns if fn.endswith('.tex') for line in open(os.path.join(dp,fn),encoding='utf-8') for m in ref_pat.finditer(line)} - set(chlabels))
items=[]
for t in missing:
    if t.startswith('V1-') and t not in v2:
        base=t[3:]
        items.append((t, bool(base in v1), v1.get(base,[])[:3]))
print('missing V1 alias not in live v2', len(items))
print('base live in v1', sum(1 for _,b,_ in items if b))
print('base absent from live v1', sum(1 for _,b,_ in items if not b))
for t,b,locs in items[:80]:
    if not b:
        print('ABSENT',t)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 446ms:
missing V1 alias not in live v2 98
base live in v1 96
base absent from live v1 2
ABSENT V1-conj:lattice-sewing
ABSENT V1-constr:platonic-package
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, difflib
from collections import defaultdict, Counter
pat_label=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
pat_ref=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')

def load_paths(root, subs=None):
    d=defaultdict(list)
    files=[]
    if subs is None:
        for dp,_,fns in os.walk(root):
            for fn in fns:
                if fn.endswith('.tex'): files.append(os.path.join(dp,fn))
    else:
        for rel in subs:
            path=os.path.join(root,rel)
            if os.path.isfile(path): files.append(path)
            elif os.path.isdir(path):
                for dp,_,fns in os.walk(path):
                    for fn in fns:
                        if fn.endswith('.tex'): files.append(os.path.join(dp,fn))
    for path in files:
        try:
            for i,line in enumerate(open(path,encoding='utf-8'),1):
                for m in pat_label.finditer(line):
                    d[m.group(1)].append((path,i,line.strip()))
        except Exception:
            pass
    return d, files
v2ch, chfiles = load_paths('/Users/raeez/chiral-bar-cobar-vol2',['chapters'])
v2live, _ = load_paths('/Users/raeez/chiral-bar-cobar-vol2',['main.tex','chapters','appendices'])
v1live, _ = load_paths('/Users/raeez/chiral-bar-cobar',['main.tex','chapters','appendices'])
v3live, _ = load_paths('/Users/raeez/calabi-yau-quantum-groups',['main.tex','chapters','appendices'])
# load full text of chapters files for comment lookup
texts={p:open(p,encoding='utf-8').read() for p in chfiles}
missing_uses=[]
for path in chfiles:
    for i,line in enumerate(open(path,encoding='utf-8'),1):
        for m in pat_ref.finditer(line):
            target=m.group(2)
            if target not in v2ch:
                missing_uses.append((path,i,m.group(1),target,line.strip()))

def classify(target):
    if any(f'label removed: {target}' in txt for txt in texts.values()):
        return 'comment_removed'
    if target in v2live and target not in v2ch:
        return 'vol2_hidden_import'
    if target.startswith('V1-'):
        base=target[3:]
        if target in v2live:
            return 'vol2_hidden_import'  # alias in main/appendix
        if base in v1live:
            return 'missing_v1_alias'
        return 'dead_v1_reference'
    if ('V1-'+target) in v2live:
        return 'should_use_v1_alias'
    if target in v1live:
        return 'plain_v1_reference'
    if target in v3live:
        return 'plain_v3_reference'
    if target.startswith('chap:') and ('ch:'+target[5:]) in v2ch:
        return 'prefix_drift_chap_ch'
    # normalized/fuzzy omitted for stats only
    return 'local_orphan'

counter=Counter(classify(t) for _,_,_,t,_ in missing_uses)
print(counter)
for cat in counter:
    print('\\nCAT',cat)
    seen=[]
    for use in missing_uses:
        if classify(use[3])==cat and use[3] not in seen:
            print(use[3], '=>', use[0]+':'+str(use[1]))
            seen.append(use[3])
            if len(seen)>=20: break
PY" in /Users/raeez/chiral-bar-cobar succeeded in 19.70s:
Counter({'vol2_hidden_import': 941, 'comment_removed': 269, 'missing_v1_alias': 137, 'local_orphan': 23, 'dead_v1_reference': 4, 'plain_v1_reference': 2, 'prefix_drift_chap_ch': 2})

CAT local_orphan
sec:universal-bulk-proofs => /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:292
thm:spectral-ybe => /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex:215
rem:kunneth-geometric-insight => /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4963
def:modular-graph-coefficient-algebra => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:73
def:nms-quartic-resonance-class => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:602
thm:virasoro-koszul-dual => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1132
subsec:e1-five-theorems-all-genera => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1481
rem:bp-EN-level => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6388
def:shadow-depth-classes => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1577
thm:quintic-forced => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2032
sec:ym-spectral-gap => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2225
sec:bergman-fock => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2455
subsec:thqg-non-fredholm => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2644
subsec:thqg-genus2-fredholm => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2707
thm:virasoro-quartic-class => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:482
chap:pva-descent => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2247
thm:shifted-kz-connection => /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1293
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict
pat_label=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
pat_ref=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')

def load(root, subs):
    d=defaultdict(list)
    for rel in subs:
        path=os.path.join(root,rel)
        if os.path.isfile(path):
            files=[path]
        else:
            files=[]
            for dp,_,fns in os.walk(path):
                for fn in fns:
                    if fn.endswith('.tex'): files.append(os.path.join(dp,fn))
        for f in files:
            for i,line in enumerate(open(f,encoding='utf-8'),1):
                for m in pat_label.finditer(line): d[m.group(1)].append((f,i))
    return d
v2ch=load('/Users/raeez/chiral-bar-cobar-vol2',['chapters'])
v2live=load('/Users/raeez/chiral-bar-cobar-vol2',['main.tex','chapters','appendices'])
v1live=load('/Users/raeez/chiral-bar-cobar',['main.tex','chapters','appendices'])
v3live=load('/Users/raeez/calabi-yau-quantum-groups',['main.tex','chapters','appendices'])
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            f=os.path.join(dp,fn)
            text=open(f,encoding='utf-8').read()
            for i,line in enumerate(text.splitlines(),1):
                for m in pat_ref.finditer(line):
                    t=m.group(2)
                    if t in v2ch: continue
                    cat=None
                    if f'label removed: {t}' in text: cat='comment_removed'
                    elif t in v2live and t not in v2ch: cat='vol2_hidden_import'
                    elif t.startswith('V1-'):
                        base=t[3:]
                        if t in v2live: cat='vol2_hidden_import'
                        elif base in v1live: cat='missing_v1_alias'
                        else: cat='dead_v1_reference'
                    elif ('V1-'+t) in v2live: cat='should_use_v1_alias'
                    elif t in v1live: cat='plain_v1_reference'
                    elif t in v3live: cat='plain_v3_reference'
                    elif t.startswith('chap:') and ('ch:'+t[5:]) in v2ch: cat='prefix_drift_chap_ch'
                    else: cat='local_orphan'
                    if cat=='plain_v3_reference' or cat=='should_use_v1_alias':
                        print(cat, f'{f}:{i}', t)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 491ms:

codex
The bulk of the surface is now classified. The only places that still need manual judgment are a small residue of genuinely local or stale-name targets; I’m auditing those one by one so the final fixes are specific instead of boilerplate.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, difflib
from collections import defaultdict
# targets from previous pass
local_targets = [
'sec:universal-bulk-proofs','thm:spectral-ybe','rem:kunneth-geometric-insight','def:modular-graph-coefficient-algebra',
'def:nms-quartic-resonance-class','thm:virasoro-koszul-dual','subsec:e1-five-theorems-all-genera','rem:bp-EN-level',
'def:shadow-depth-classes','thm:quintic-forced','sec:ym-spectral-gap','sec:bergman-fock','subsec:thqg-non-fredholm',
'subsec:thqg-genus2-fredholm','thm:virasoro-quartic-class','chap:pva-descent','thm:shifted-kz-connection',
'thm:bar-superconnection','sec:log-ht-monodromy','prop:harrison-leading-vanishing','thm:ybe-implies-crossing',
'conj:w-transport-to-transpose','thm:virasoro-koszul-dual-frontier'
]
# Note: last 3 may not actually be in list; include if present for search breadth.
pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
labels=[]
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            p=os.path.join(dp,fn)
            for i,line in enumerate(open(p,encoding='utf-8'),1):
                for m in pat.finditer(line):
                    labels.append((m.group(1),p,i))
label_names=[x[0] for x in labels]
for target in local_targets:
    matches=difflib.get_close_matches(target,label_names,n=5,cutoff=0.5)
    print('\\nTARGET',target)
    for m in matches:
        loc=[x for x in labels if x[0]==m][0]
        print(' ',m, loc[1], loc[2])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 5.18s:

TARGET sec:universal-bulk-proofs
  thm:universal-bulk /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex 249
  subsec:universal-bulk-specializations /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex 12
  subsec:universal-bulk-specializations /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex 12
  subsec:chiral-RH-proof /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex 3948
  subsec:universal-property-twisting /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex 748

TARGET thm:spectral-ybe
  not:spectral /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex 76
  thm:spectral_R_YBE /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex 683
  rem:no-spectral-zeta /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex 3476
  thm:cbt-spectral-obstruction /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_core.tex 342
  chap:spectral-braiding /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex 8

TARGET rem:kunneth-geometric-insight
  rem:rosetta-geometric-steinberg /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex 1714
  rem:kunneth-genus-obstruction /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex 845
  rem:ds-chain-geometric-reading /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex 819
  rem:sn-eulerian-weight /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex 2545

thinking
**Checking orphan count**

I need to verify if the added last three items are accurate. It seems like the local_orphans count is showing 23, but that might include some not present in the search results. I wonder if I could script something to specifically list the local_orphan targets along with their use counts. It sounds like a good idea to get exact numbers and ensure everything adds up correctly! Let's figure out how to proceed with that.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict, Counter
pat_label=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
pat_ref=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')

def load(root, subs):
    d=defaultdict(list)
    files=[]
    for rel in subs:
        path=os.path.join(root,rel)
        if os.path.isfile(path): files.append(path)
        else:
            for dp,_,fns in os.walk(path):
                for fn in fns:
                    if fn.endswith('.tex'): files.append(os.path.join(dp,fn))
    for f in files:
        for i,line in enumerate(open(f,encoding='utf-8'),1):
            for m in pat_label.finditer(line): d[m.group(1)].append((f,i,line.strip()))
    return d, files
v2ch, chfiles=load('/Users/raeez/chiral-bar-cobar-vol2',['chapters'])
v2live,_=load('/Users/raeez/chiral-bar-cobar-vol2',['main.tex','chapters','appendices'])
v1live,_=load('/Users/raeez/chiral-bar-cobar',['main.tex','chapters','appendices'])
v3live,_=load('/Users/raeez/calabi-yau-quantum-groups',['main.tex','chapters','appendices'])
texts={p:open(p,encoding='utf-8').read() for p in chfiles}
def classify(path,target):
    if any(f'label removed: {target}' in txt for txt in texts.values()): return 'comment_removed'
    if target in v2live and target not in v2ch: return 'vol2_hidden_import'
    if target.startswith('V1-'):
        base=target[3:]
        if target in v2live: return 'vol2_hidden_import'
        elif base in v1live: return 'missing_v1_alias'
        else: return 'dead_v1_reference'
    if ('V1-'+target) in v2live: return 'should_use_v1_alias'
    if target in v1live: return 'plain_v1_reference'
    if target in v3live: return 'plain_v3_reference'
    if target.startswith('chap:') and ('ch:'+target[5:]) in v2ch: return 'prefix_drift_chap_ch'
    return 'local_orphan'
locs=defaultdict(list)
for p in chfiles:
    for i,line in enumerate(open(p,encoding='utf-8'),1):
        for m in pat_ref.finditer(line):
            t=m.group(2)
            if t not in v2ch and classify(p,t)=='local_orphan':
                locs[t].append((p,i,line.strip()))
for t,uses in sorted(locs.items(), key=lambda kv:(-len(kv[1]),kv[0])):
    print(len(uses), t, uses[0][0]+':'+str(uses[0][1]))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 6.31s:
1 ass:H1-H4 /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:57
1 chap:pva-descent /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2247
1 def:modular-graph-coefficient-algebra /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:73
1 def:nms-quartic-resonance-class /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:602
1 def:shadow-depth-classes /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1577
1 hyp:H1 /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:57
1 hyp:H3 /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:57
1 prop:harrison-leading-vanishing /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3276
1 rem:bp-EN-level /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6388
1 rem:kunneth-geometric-insight /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4963
1 sec:bergman-fock /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2455
1 sec:log-ht-monodromy /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:1613
1 sec:universal-bulk-proofs /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:292
1 sec:ym-spectral-gap /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2225
1 subsec:e1-five-theorems-all-genera /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1481
1 subsec:thqg-genus2-fredholm /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2707
1 subsec:thqg-non-fredholm /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2644
1 thm:bar-superconnection /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1295
1 thm:quintic-forced /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2032
1 thm:shifted-kz-connection /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1293
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex | sed -n '48,66p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(ass|assump|hyp):H1(-H4)?\\}|label removed: (ass|assump|hyp):H1(-H4)?|label removed: hyp:H3' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    48	
    49	\begin{remark}[Higher-Spin Gravity]
    50	When $\mathcal{V}$ is a W-algebra, the resulting 3D theory is a form of higher-spin gravity in the sense of Henneaux--Teitelboim and Vasiliev. The gauge symmetry extends diffeomorphisms to include higher-spin transformations.
    51	\end{remark}
    52	
    53	\subsubsection{BV Quantization and $A_\infty$ Operations}
    54	
    55	\begin{remark}[Analytic hypotheses for W-algebra examples]
    56	% label removed: rem:W-hypotheses
    57	All results in this section are conditional on Hypotheses~\ref{hyp:H1}--\ref{hyp:H3} and Assumption~\ref{ass:H1-H4}. Verification proceeds as follows.
    58	\emph{(H1)}: The BV data for the Khan--Zeng 3D HT Poisson sigma model is constructed explicitly; one-loop finiteness follows from the holomorphic structure by the arguments of \cite{GRW21,GGW21}.
    59	\emph{(H2)}: The propagator $K(t,z) = \Theta(t)/(2\pi z)$ is meromorphic in $z$ with a simple pole and has step-function (exponential) decay in $t$, satisfying the required regularity.
    60	\emph{(H3)}: The interaction vertices are polynomial in fields and derivatives, so the configuration-space integrals defining $m_k$ converge on $\FM_k(\C) \times \Conf_k(\R)$ by standard estimates; the AOS relations hold on logarithmic forms.
    61	\emph{(H4)}: Factorization compatibility follows from the general construction of \cite{CDG20,GKW25} for HT gauge theories with polynomial interactions.
    62	\end{remark}
    63	
    64	In the BV formalism, we introduce antifields $(\Phi^i)^* \sim \eta_i$ and ghosts $c^i \sim \epsilon_i$. The master action
    65	\[
    66	S_{\text{BV}} = S + \int (\Phi^i)^* Q c^i + \cdots
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex:19:% label removed: assump:H1-H4

thinking
**Exploring labels in pva-preview**

I’m curious about the interesting labels in the pva-preview. I think I need to search for specific elements, like H1 and H3 tags, to better understand them. There’s probably a lot to uncover regarding how these labels are utilized or represented. It feels like digging into some interesting details that could reveal more about their function or significance. Let’s see what insights I can find there!
exec
/bin/zsh -lc "rg -n 'label removed: hyp:H1|label removed: hyp:H3|\\\\label\\{hyp:H1\\}|\\\\label\\{hyp:H3\\}|\\\\label\\{ass:H1-H4\\}|\\\\label\\{assump:H1-H4\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
The remaining genuinely local misses are down to `23` one-off labels. Several are not external drift at all; they are internal stale names or deleted anchors inside the same file, so I’m reading each one in context and pinning it to the exact replacement label or exact point where the label has to be restored.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex | sed -n '208,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex | sed -n '286,296p'" in /Users/raeez/chiral-bar-cobar succeeded in 66ms:
   286	 which in any chart $\cC \simeq \Perf(A_b)$ is computed by
   287	 $\cC^\bullet_{\mathrm{ch}}(A_b, A_b)$.
   288	\end{enumerate}
   289	\end{theorem}
   290	
   291	The proof of each part is given in
   292	\S\ref{sec:universal-bulk-proofs}. The
   293	derived center is the \emph{bulk}, not the bar complex.
   294	The bar complex $\barB(A)$ classifies \emph{twisting morphisms}
   295	(universal couplings between $A$ and its Koszul dual~$A^!$,
   296	Volume~I, Theorem~A), while the derived center classifies
 succeeded in 66ms:
   208	\begin{proof}
   209	The correction $r_{\ell,\ell'}(z)$ is meromorphic in~$z$ by the
   210	one-loop exactness property of the perturbative 3d~HT theory
   211	(Theorem~\ref{thm:one-loop-koszul}). Associativity follows from
   212	the Yang--Baxter equation for the spectral $R$-matrix
   213	$R(z) = 1 + r(z)/z + \cdots$, which is proved by Stokes' theorem
   214	on $\FM_3(\C)$
   215	(Theorem~\ref{thm:spectral-ybe}).
   216	\end{proof}
   217	
   218	\begin{conjecture}[Global Weiss descent]
   219	\label{conj:weiss-descent}
   220	\index{Weiss descent!boundary factorization|textbf}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex | sed -n '4956,4970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '64,82p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    64	\index{Verdier duality!convolution algebra}
    65	
    66	\subsubsection{The graph-coefficient involution}
    67	
    68	\begin{definition}[Verdier duality on modular graph coefficients]
    69	% label removed: def:thqg-IV-verdier-modular
    70	\index{Verdier duality!modular graph coefficients}
    71	The modular graph coefficient algebra
    72	$\Gmod = \bigoplus_{g \geq 0} \Gmod_g$
    73	(Definition~\ref{def:modular-graph-coefficient-algebra})
    74	carries a canonical involution
    75	$\sigma_{\Gmod}\colon \Gmod \to \Gmod$
    76	induced by orientation reversal on stable curves:
    77	for a stable graph $\Gamma \in \Gmod_g$ with vertex genus assignment
    78	$\{g_v\}_{v \in V(\Gamma)}$, edge set $E(\Gamma)$, and leg set
    79	$L(\Gamma)$,
    80	\begin{equation}% label removed: eq:thqg-IV-graph-involution
    81	\sigma_{\Gmod}(\Gamma)
    82	\;:=\;
 succeeded in 51ms:
  4956	 quasi-isomorphism is on the \emph{source} cooperad, and
  4957	 $\Hom(-,V)$ for fixed~$V$ sends quasi-isomorphisms between
  4958	 levelwise finite-dimensional complexes to quasi-isomorphisms.
  4959	\end{itemize}
  4960	The K\"unneth decomposition of the bar complex into pure and mixed
  4961	sectors (Lemma~\ref{lem:operadic-kunneth}) provides geometric
  4962	insight into this argument but is not logically required;
  4963	see Remark~\ref{rem:kunneth-geometric-insight}.
  4964	
  4965	\medskip
  4966	\noindent\textbf{Step~7: Verification of parts (a)--(c).}
  4967	
  4968	\textit{Part~(a).}
  4969	Under the quasi-isomorphism $(\iota^*)^{-1}$, a
  4970	two-coloured tree $T$ in $\mathbf{B}(\cP)$ indexes an
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:modular-graph-coefficient-algebra\\}|\\\\label\\{def:thqg-IV-verdier-modular\\}|\\\\label\\{def:modular-graph["'^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 98ms:

exec
/bin/zsh -lc "rg -n 'label removed: def:modular-graph-coefficient-algebra|label removed: def:nms-quartic-resonance-class|label removed: def:shadow-depth-classes|label removed: thm:virasoro-koszul-dual|label removed: thm:virasoro-quartic-class|label removed: thm:quintic-forced|label removed: thm:shifted-kz-connection|label removed: thm:bar-superconnection|label removed: sec:ym-spectral-gap|label removed: sec:bergman-fock|label removed: subsec:thqg-non-fredholm|label removed: subsec:thqg-genus2-fredholm|label removed: sec:universal-bulk-proofs|label removed: rem:kunneth-geometric-insight|label removed: prop:harrison-leading-vanishing|label removed: chap:pva-descent|label removed: rem:bp-EN-level|label removed: subsec:e1-five-theorems-all-genera|label removed: thm:spectral-ybe' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Inspecting context**

I need to take a closer look at the context, possibly within the same file. There might be theorem or section headings present that don’t have labels. I could consider adding those labels for clarity. For example, there’s a section like sec:universal-bulk-proofs, and I wonder if there’s a corresponding area where the theorem is being proven. So, I should search for nearby headings to ensure everything is organized properly.
exec
/bin/zsh -lc "rg -n 'universal bulk|Kunneth|graph coefficient|quartic resonance|shadow depth|Virasoro.*Koszul dual|quartic class|Fredholm|Yang--Baxter|superconnection|shifted KZ|spectral gap|Bergman|five theorems.*all genera|bp.*EN-level' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 391

/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:119:the Yang--Baxter equation from $d^2=0$ via boundary-face analysis, the classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:120:Yang--Baxter equation as linearisation, and the affine ordered-bar
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1198:Yang--Baxter equation as $d^2=0$ on the degree-$3$ complex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1205:descent (Remark~\ref{rem:r-matrix-mc}); the Yang--Baxter equation is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1658:\item Yang--Baxter equation from $d^2=0$ via dual topological-combinatorial
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1660:\item Classical Yang--Baxter equation as linearisation
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2044:$R$-matrix satisfies the Yang--Baxter
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2079:and the bar differential as $d$. The Yang--Baxter equation
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2081:classical Yang--Baxter equation on~$r_0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2090:\begin{proposition}[Yang--Baxter from $d^2=0$ on degree~$3$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2093:\index{Yang--Baxter equation!from d squared zero@from $d^2=0$|textbf}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2096:Yang--Baxter equation:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2159:gives the Yang--Baxter equation: the two sides
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2164:\begin{corollary}[Classical Yang--Baxter equation;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2167:\index{Yang--Baxter equation!classical}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2171:Yang--Baxter equation:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2295:is the Casimir. The Yang--Baxter equation
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2397:is the Yang--Baxter
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:YBE\\}|\\\\label\\{thm:spectral_R_YBE\\}|\\\\label\\{thm:general-hs-sewing\\}|\\\\label\\{thm:heisenberg-higher-genus\\}|\\\\label\\{thm:level-rank\\}|\\\\label\\{rem:gz26-wn-comparison-conjectural\\}|\\\\label\\{rem:vol2-gz26-wn-comparison-conjectural\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/main.tex:1556: \phantomsection\label{thm:general-hs-sewing}% % genus_complete.tex
/Users/raeez/chiral-bar-cobar/main.tex:1831: \phantomsection\label{thm:level-rank}%
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1618:\begin{theorem}[Higher genus Heisenberg; \ClaimStatusProvedHere]\label{thm:heisenberg-higher-genus}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:69:\label{thm:YBE}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:683:\label{thm:spectral_R_YBE}
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:168:\label{rem:vol2-gz26-wn-comparison-conjectural}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:155:\label{thm:general-hs-sewing}
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1612:\label{rem:gz26-wn-comparison-conjectural}
exec
/bin/zsh -lc "rg -n '\\\\label\\{V1-thm:level-rank\\}|\\\\label\\{V1-rem:gz26-wn-comparison-conjectural\\}' /Users/raeez/chiral-bar-cobar-vol2/main.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '1618,1632p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex | sed -n '176,186p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1618	The complementarity $\kappa + \kappa' = K(\cA)$ then follows from
  1619	the computations of~\S\ref{V1-subsec:thqg-IV-complementarity-constant}.
  1620	
  1621	\emph{Facet~III.}
  1622	$K(\widehat{\fsl}_{N,k}) = 0$ is a special case of
  1623	Theorem~\ref{V1-thm:thqg-IV-km-K}. The level-rank duality
  1624	$\widehat{\fsl}_{N,k} \leftrightarrow \widehat{\fsl}_{k,N}$
  1625	(Theorem~\ref{thm:level-rank}) is a refinement for integer levels.
  1626	
  1627	\emph{Facet~IV.}
  1628	Summing over genera: the identity $\sigma(\Theta_\cA) = \Theta_{\cA^!}$
  1629	at the cohomological level gives
  1630	$H^*(\barB^{(g)}(\cA)) \oplus H^*(\barB^{(g)}(\cA^!))
  1631	\hookrightarrow H^*(\overline{\cM}_g, \cZ(\cA))$.
  1632	The Lagrangian decomposition follows from
 succeeded in 52ms:
   176	theorem~\ref{thm:vol2-seven-faces-master} carries Face~4 with the
   177	\emph{same} $\cW_N$ conjectural qualifier as Vol~I; the
   178	\texttt{ProvedHere} status of the master theorem refers to the
   179	existence and structural identification, not to the term-by-term
   180	operator match for $\cW_N$ (cf.\
   181	Vol~I, Remark~\ref{rem:gz26-wn-comparison-conjectural}).
   182	\end{remark}
   183	
   184	\section{Face 5: The dg-shifted Yangian}
   185	\label{sec:face-5-dg-shifted-yangian}
   186	
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '1832,1844p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2376,2386p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1832	
  1833	\begin{remark}[The six-fold package under duality]
  1834	% label removed: rem:thqg-IV-six-fold-duality
  1835	\index{platonic package!$S$-duality}
  1836	The modular Koszul datum $\Pi_X(L) = (\cF_X, \bar{B}_X, \Theta_L, \cL_L,
  1837	(V^{\mathrm{br}}, T^{\mathrm{br}}), R_4^{\mathrm{mod}})$
  1838	(Construction~\ref{V1-constr:platonic-package}) transforms under $\sigma$:
  1839	$\cF_X(L) \mapsto \cF_X(L^!)$,
  1840	$\bar{B}_X(L) \mapsto \bar{B}_X(L^!)$,
  1841	$\Theta_L \mapsto \Theta_{L^!}$,
  1842	$\cL_L \mapsto \cL_{L^!}$,
  1843	$(V^{\mathrm{br}}, T^{\mathrm{br}}) \mapsto ((V^!)^{\mathrm{br}}, (T^!)^{\mathrm{br}})$,
  1844	$R_4^{\mathrm{mod}}(L) \mapsto R_4^{\mathrm{mod}}(L^!)$.
 succeeded in 50ms:
  2376	% label removed: prob:thqg-X-lattice-sewing%
  2377	\index{lattice algebra!sewing envelope}%
  2378	Construct the sewing envelope of a lattice vertex algebra
  2379	$V_\Lambda$ explicitly as a completion of the Bergman Fock
  2380	space tensored with the lattice group algebra.
  2381	Conjecture~\textup{\ref{V1-conj:lattice-sewing}} predicts that
  2382	\begin{equation}% label removed: eq:thqg-X-lattice-sewing-conj
  2383	V_\Lambda^{\mathrm{sew}}
  2384	\;\cong\;
  2385	\operatorname{Sym} A^2(D)^{\otimes r}
  2386	\;\otimes\;
exec
/bin/zsh -lc "rg -n 'platonic-package|label removed: constr:platonic-package|label removed: V1-constr:platonic-package|Construction' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
1838:(Construction~\ref{V1-constr:platonic-package}) transforms under $\sigma$:
1986:The genus spectral sequence (Construction~\ref{V1-const:vol1-genus-spectral-sequence})

thinking
**Searching for data**

I realize that I don't have local access, so I'm considering searching in a file for something related to "modular Koszul datum." It seems like a construction might have been removed entirely, so I’m thinking that using a command-line tool like `rg` could help me locate any relevant information. I want to make sure I'm thorough and find all the connections or references in the file.
exec
/bin/zsh -lc "rg -n 'modular Koszul datum|Pi_X\\(L\\)|platonic' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1796:\begin{proposition}[Holographic modular Koszul datum under $S$-duality;
1799:\index{holographic modular Koszul datum!$S$-duality}
1800:The holographic modular Koszul datum
1835:\index{platonic package!$S$-duality}
1836:The modular Koszul datum $\Pi_X(L) = (\cF_X, \bar{B}_X, \Theta_L, \cL_L,
1838:(Construction~\ref{V1-constr:platonic-package}) transforms under $\sigma$:
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '1792,1808p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1792	\end{remark}
  1793	
  1794	\subsubsection{The holographic datum under $S$-duality}
  1795	
  1796	\begin{proposition}[Holographic modular Koszul datum under $S$-duality;
  1797	\ClaimStatusProvedHere]
  1798	% label removed: prop:thqg-IV-holographic-datum
  1799	\index{holographic modular Koszul datum!$S$-duality}
  1800	The holographic modular Koszul datum
  1801	$H(T) = (\cA, \cA^!, C, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$
  1802	transforms under the $S$-duality involution $\sigma$ as follows:
  1803	\begin{enumerate}[label=\textup{(\alph*)}]
  1804	\item $\cA \leftrightarrow \cA^!$ (boundary algebras exchange).
  1805	\item $C \mapsto C$ (the complementarity constant is preserved:
  1806	 $K(\cA) = K(\cA^!)$).
  1807	\item $r(z) \mapsto r^!(z) := \sigma(r(z))$ (the $r$-matrix
  1808	 transforms by the Verdier involution on the collision residue).
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2370,2394p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2370	\end{itemize}
  2371	\end{remark}
  2372	
  2373	\subsubsection{Open problems and the analytic frontier}
  2374	
  2375	\begin{openproblem}[Lattice sewing envelope]%
  2376	% label removed: prob:thqg-X-lattice-sewing%
  2377	\index{lattice algebra!sewing envelope}%
  2378	Construct the sewing envelope of a lattice vertex algebra
  2379	$V_\Lambda$ explicitly as a completion of the Bergman Fock
  2380	space tensored with the lattice group algebra.
  2381	Conjecture~\textup{\ref{V1-conj:lattice-sewing}} predicts that
  2382	\begin{equation}% label removed: eq:thqg-X-lattice-sewing-conj
  2383	V_\Lambda^{\mathrm{sew}}
  2384	\;\cong\;
  2385	\operatorname{Sym} A^2(D)^{\otimes r}
  2386	\;\otimes\;
  2387	\ell^2(\Lambda^*/\Lambda),
  2388	\end{equation}
  2389	where $r = \mathrm{rank}(\Lambda)$ and

thinking
**Fixing references and sections**

I’m considering fixing either the local label by changing the reference to `Open Problem\ref{prob:thqg-X-lattice-sewing}`, or possibly adding an alias if the conjecture in V1 is still intended, but V1 is currently absent. It seems better to focus on fixing the local open problem instead. I'll need to inspect section sec:universal-bulk-proofs and check if there's a subsection that proves some parts. Let’s search through the headings for clarity.
exec
/bin/zsh -lc "rg -n 'universal bulk|proof of each part|proofs' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
8:% coalgebraic projection; the derived center is the universal bulk;
217:\subsection{The universal bulk}
247:\begin{theorem}[The universal bulk;
250:\index{derived center!as universal bulk|textbf}
274: is the universal bulk algebra. On the Koszul locus, it is a
291:The proof of each part is given in
292:\S\ref{sec:universal-bulk-proofs}. The
350: & universal bulk \\
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex | sed -n '296,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   296	Volume~I, Theorem~A), while the derived center classifies
   297	\emph{bulk operators acting on the boundary}. These are different
   298	objects solving different problems.
   299	
   300	\subsection{The bar complex as coalgebraic projection}
   301	
   302	The bar construction of Volume~I enters the open/closed picture as
   303	a \emph{derived invariant} of the factorization category~$\cC$, not
   304	as the category itself.
   305	
   306	\begin{proposition}[Bar complex from the open sector;
   307	 \ClaimStatusProvedHere]
   308	\label{prop:bar-from-open}
   309	Let $\cC$ be an open/closed factorization dg-category with vacuum
   310	object~$b$ and boundary algebra $A_b = \End(b)$. The bar complex
   311	$\barB^{\mathrm{ch}}(A_b) = T^c(s^{-1}\bar{A}_b)$ records the
   312	twisting data of~$\cC$:
   313	\begin{enumerate}[label=\textup{(\roman*)}]
   314	\item The bar differential $d_{\barB}$ encodes how closed-sector
   315	 operations twist the open-sector composition (OPE residues

thinking
**Considering proof sections**

I’m noticing there’s no dedicated section for proofs, which could complicate things. The line about the proof being in a specific section is confusing since it doesn’t seem to exist. A possible fix might be to delete that line or add a label for any new proof subsection. It might be simpler to replace the sentence pointing to the theorem proof if it's immediately above. I need to check if that theorem is followed by its proof for clarity.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex | sed -n '247,289p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   247	\begin{theorem}[The universal bulk;
   248	 \ClaimStatusProvedHere]
   249	\label{thm:universal-bulk}
   250	\index{derived center!as universal bulk|textbf}
   251	\index{Swiss-cheese theorem!chiral|textbf}
   252	Let $(A, \{m_k\})$ be a curved $A_\infty$-chiral algebra.
   253	\begin{enumerate}[label=\textup{(\roman*)}]
   254	\item \emph{Brace dg algebra.} The complex
   255	 $(\cC^\bullet_{\mathrm{ch}}(A, A), \delta, \{-\}\{-,\ldots,-\})$
   256	 is a brace dg algebra: $\delta^2 = 0$ from $[m,m] = 0$, the
   257	 brace operations satisfy the higher pre-Lie identity, and the
   258	 Gerstenhaber bracket $[f,g] = f\{g\} - (-1)^{\|f\|\|g\|} g\{f\}$
   259	 descends to a Gerstenhaber algebra on cohomology.
   260	
   261	\item \emph{Swiss-cheese universality.}
   262	 The pair $\cU(A) := (\cC^\bullet_{\mathrm{ch}}(A, A),\; A)$
   263	 is the \emph{terminal} local chiral open/closed pair: for every
   264	 local open/closed pair $(\cB, A, \iota)$, there exists a unique
   265	 morphism $\Phi \colon \cB \to \cC^\bullet_{\mathrm{ch}}(A,A)$
   266	 intertwining the Swiss-cheese operations.

thinking
**Inspecting orphan contexts**

I need to look into local orphan contexts as well. Let me check the remaining ones. It seems there could be direct headings, but I might be missing some labels. I want to ensure that everything is correctly organized and functional. I'll go ahead and inspect these batches to see what’s going on. It’ll be interesting to figure this out and make any necessary adjustments!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '1572,1584p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '592,610p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   592	At degree~$4$:
   593	$\sigma(\mathfrak{Q}_\cA) = \mathfrak{Q}_{\cA^!}$.
   594	The clutching law is preserved:
   595	$\sigma(\xi^*_{\mathrm{sep}}\mathfrak{Q}_\cA)
   596	= \xi^*_{\mathrm{sep}}\mathfrak{Q}_{\cA^!}$.
   597	\end{proposition}
   598	
   599	\begin{proof}
   600	The quartic resonance class $\mathfrak{Q}_\cA$ is the genus-$0$,
   601	degree-$4$ component of $\Theta_\cA$ modulo gauge
   602	(Definition~\ref{def:nms-quartic-resonance-class}). By the $r = 4$
   603	case of Theorem~\ref{V1-thm:thqg-IV-shadow-duality},
   604	$\sigma(\Theta_\cA^{\leq 4}) = \Theta_{\cA^!}^{\leq 4}$.
   605	Extraction gives $\sigma(\mathfrak{Q}_\cA) = \mathfrak{Q}_{\cA^!}$.
   606	
   607	The clutching law involves pullback along the separating degeneration
   608	$\xi_{\mathrm{sep}}\colon
   609	\overline{\cM}_{g_1,n_1+1} \times \overline{\cM}_{g_2,n_2+1}
   610	\to \overline{\cM}_{g,n}$, which commutes with Verdier duality
 succeeded in 52ms:
  1572	% label removed: subsec:thqg-X-class-G
  1573	
  1574	The Heisenberg sewing theorem gives a Fredholm determinant
  1575	formula for the simplest possible chiral algebra, the free boson.
  1576	The shadow depth classification
  1577	(Definition~\ref{def:shadow-depth-classes}
  1578	in Appendix~\ref*{V1-app:nonlinear-modular-shadows})
  1579	organizes chiral algebras into four classes based on the
  1580	termination behavior of the shadow obstruction tower:
  1581	\begin{itemize}
  1582	\item Class~\textbf{G} (Gaussian): $r_{\max} = 2$.
  1583	 The shadow obstruction tower terminates at weight~$2$:
  1584	 $\Theta_\cA^{\min} = \eta\otimes\Gamma_\cA$.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '3268,3282p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '6380,6396p'" in /Users/raeez/chiral-bar-cobar succeeded in 108ms:
  3268	into territory where the current operadic machinery does not
  3269	yet reach.
  3270	\begin{enumerate}[label=\textup{(\roman*)}]
  3271	\item The $A_\infty$ formality question
  3272	 (Question~\ref{q:yangian-Ainfty}). A positive answer would
  3273	 reduce the filtered Yangian $Y_\hbar(\fg)$ to its associated
  3274	 graded as an $A_\infty$-algebra, collapsing the Harrison
  3275	 obstruction tower of
  3276	 Proposition~\ref{prop:harrison-leading-vanishing}. The
  3277	 evidence from Hochschild decomposition
  3278	 (Proposition~\ref{prop:HH-Ugt-decomposition}) is strong
  3279	 but not decisive: the relevant obstruction classes are
  3280	 spectral-parameter-dependent and mix the geometric and loop
  3281	 directions.
  3282	\item Construction of a ``Yangian vertex algebra'': a vertex
 succeeded in 100ms:
  6380	$\Ethree^{\mathrm{top}}$ on
  6381	$\Zder^{\mathrm{ch}}(\cW^k(\fg, f))$.
  6382	\end{proof}
  6383	
  6384	\begin{remark}[Why the non-principal obstructions are illusory
  6385	 for topologization]
  6386	\label{rem:non-principal-obstructions-illusory}
  6387	\index{Drinfeld--Sokolov reduction!non-principal!obstructions resolved}
  6388	Remark~\textup{\ref{rem:bp-EN-level}} listed two qualitative
  6389	differences between the principal and non-principal DS reductions:
  6390	\textup{(1)}~the DS-BRST complex at a non-principal nilpotent
  6391	is non-Koszul \textup{(}irregular constraint system\textup{)},
  6392	and \textup{(2)}~the residual Levi factor can be non-abelian.
  6393	Neither obstructs topologization, for the following reasons.
  6394	
  6395	\medskip\noindent
  6396	\textbf{Non-Koszulness.} The non-Koszulness of the DS complex

thinking
**Searching for labels**

I need to look for the actual label “rem:bp-EN-level.” Maybe there's an alias or some local variants related to virasoro and w3. I wonder if the intended label should actually be “rem:virasoro-EN-level.” I think it’s important to have the 3D gravity context in mind from our previous discussions. I’ll search for occurrences to clarify this further. It's a little complicated, but I’m determined to find the right information!
exec
/bin/zsh -lc "rg -n 'EN-level|non-principal DS|Bershadsky|Polyakov' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
391:\index{Bershadsky--Polyakov algebra!trichotomy}%
451:by the Bershadsky--Polyakov algebra
1042: Non-principal reductions (e.g.\ the Bershadsky--Polyakov algebra
3196: non-principal DS; $J$ survives \\
3204:The seventh row (the Bershadsky--Polyakov algebra) instantiates
3450:the Bershadsky--Polyakov algebra from $(\mathfrak{sl}_3,
3464:\index{Bershadsky--Polyakov algebra!coproduct resolution}
3466:primitive for the Bershadsky--Polyakov algebra
3495:non-principal DS reductions is sharp:
3501:\item \textbf{Non-principal} (Bershadsky--Polyakov and its
6224:\begin{theorem}[$\Ethree$-topological via non-principal DS reduction; \ClaimStatusProvedHere]
6226:\index{E3-topological algebra@$\Ethree$-topological algebra!non-principal DS|textbf}
6228:\index{Bershadsky--Polyakov algebra!E3-topological@$\Ethree$-topological}
6253:\item the Bershadsky--Polyakov algebra
6388:Remark~\textup{\ref{rem:bp-EN-level}} listed two qualitative
6389:differences between the principal and non-principal DS reductions:
6413:Bershadsky--Polyakov algebra\textup{)} affects the representation
6427:\begin{remark}[Specialisation to Bershadsky--Polyakov]
6429:\index{Bershadsky--Polyakov algebra!DS-transported antighost}
6550:including Virasoro, all $\cW_N$, and the Bershadsky--Polyakov
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '6424,6444p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6424	do not affect the BRST identity~\eqref{eq:T-DS-BRST-general}.
  6425	\end{remark}
  6426	
  6427	\begin{remark}[Specialisation to Bershadsky--Polyakov]
  6428	\label{rem:E3-DS-BP-specialisation}
  6429	\index{Bershadsky--Polyakov algebra!DS-transported antighost}
  6430	For $\fg = \mathfrak{sl}_3$, $f = f_{\min}$ with
  6431	$h_0 = h_1 = \mathrm{diag}(1, -1, 0)$,
  6432	$h^\vee = 3$, $x_0 = \tfrac{1}{2}h_1$, and
  6433	$(\kappa^{-1})^{h_1 h_j}$ from the $\mathfrak{sl}_3$
  6434	Killing form, the DS-transported antighost
  6435	\eqref{eq:G-prime-general} reduces to
  6436	\[
  6437	G'_{f_{\min}}(z) \;=\;
  6438	\frac{1}{2(k+3)}\sum_{a \in \mathfrak{sl}_3}
  6439	{:}J^a(z)\,\bar c_a(z){:}
  6440	\;-\; \tfrac{1}{2}\sum_j
  6441	(\kappa^{-1})^{h_1 h_j}\,\partial\bar c_{h_j}(z).
  6442	\]
  6443	The BRST identity

thinking
**Searching for reference clarification**

I'm thinking I should refer to `rem:E3-DS-BP-specialisation` instead of `rem:bp-EN-level`. I wonder if I only need to do that once. Should I change it to `rem:E3-DS-BP-specialisation`? But then I noticed line 6388 talks about two qualitative differences listed, possibly related to a previous discussion. It might be helpful to search the local text for that specific phrase to clarify this connection.
exec
/bin/zsh -lc "rg -n 'two qualitative differences|non-principal DS reductions|residual Levi factor|non-Koszul' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3495:non-principal DS reductions is sharp:
6389:differences between the principal and non-principal DS reductions:
6391:is non-Koszul \textup{(}irregular constraint system\textup{)},
6392:and \textup{(2)}~the residual Levi factor can be non-abelian.
6396:\textbf{Non-Koszulness.} The non-Koszulness of the DS complex
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '3488,3506p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3488	 coproduct is \emph{non-primitive}: the $\mathfrak{sl}_3$
  3489	 Casimir has a surviving Cartan component
  3490	 $H_1 \otimes H_1$ that projects to $J \otimes J$ under
  3491	 $p \otimes p$, giving a nonzero cross-term
  3492	 $\Delta_{z,1}(T) \ni (1/z)\, J \otimes J$.
  3493	\end{enumerate}
  3494	The dichotomy between principal and
  3495	non-principal DS reductions is sharp:
  3496	\begin{itemize}
  3497	\item \textbf{Principal} ($\mathrm{Vir}$, $\mathcal{W}_N$):
  3498	 \emph{all} fields are primitive, including composites,
  3499	 because no weight-$1$ generators survive the reduction:
  3500	 the ghost-number obstruction kills everything.
  3501	\item \textbf{Non-principal} (Bershadsky--Polyakov and its
  3502	 generalisations): free generators are primitive, but
  3503	 composites built from surviving weight-$1$ fields are
  3504	 non-primitive. The surviving weight-$1$ Casimir component
  3505	 provides exactly the cross-terms that escape the
  3506	 ghost-number filter.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '3456,3498p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3456	obstruction kills all cross-terms on free generators), but
  3457	\emph{composite}-primitivity can fail: fields built from
  3458	surviving weight-$1$ generators (e.g.\ the Sugawara stress
  3459	tensor) may acquire cross-terms from the split Casimir.
  3460	\end{remark}
  3461	
  3462	\begin{remark}[BP coproduct: resolved]
  3463	\label{rem:bp-coproduct-resolved}
  3464	\index{Bershadsky--Polyakov algebra!coproduct resolution}
  3465	The linear transferred coproduct $\Delta_{z,1}$ \emph{is}
  3466	primitive for the Bershadsky--Polyakov algebra
  3467	$\mathcal{W}(\mathfrak{sl}_3, f_{(2,1)})$ on all free
  3468	generators, but not on composites. The three free generators
  3469	behave as follows:
  3470	\begin{enumerate}
  3471	\item $G^+ = J^{E_{23}}$ and $G^- = J^{E_{31}}$ are
  3472	 fundamental affine generators. Because $E_{23}$ and
  3473	 $E_{31}$ are root vectors for simple roots of the
  3474	 $\mathfrak{sl}_2$-complement, the split Casimir
  3475	 $\Omega = \sum t^a \otimes t_a$ contributes no cross-term
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex | sed -n '1608,1618p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1608	The bar-cobar $R$-matrix satisfies the shift equations because:
  1609	\begin{enumerate}[label=\textup{(\roman*)}]
  1610	\item \textbf{Pentagon identity.}
  1611	  The pentagon identity for Virasoro conformal blocks is
  1612	  Theorem~\ref{thm:pentagon} (proved in
  1613	  Section~\ref{sec:log-ht-monodromy}).
  1614	
  1615	\item \textbf{Degenerate eigenvalue matching.}
  1616	  On the $(2,1)$-degenerate module, the bar-cobar braiding
  1617	  eigenvalues $\sigma_\pm = e^{\pm i\pi b\alpha_2}$ match the
  1618	  Ponsot--Teschner eigenvalues
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:pentagon\\}|pentagon identity' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1155:\begin{theorem}[Pentagon identity; \ClaimStatusProvedHere]\label{thm:pentagon}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '1288,1298p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1288	\renewcommand{\arraystretch}{1.3}
  1289	\begin{tabular}{lll}
  1290	\textbf{Level} & \textbf{Object} & \textbf{Governing theorem} \\
  1291	\hline
  1292	Strict & shifted KZ/FM connection $\nabla = d - \hbar\,r(z)\,dz/z$
  1293	 & Theorem~\ref{thm:shifted-kz-connection} \\
  1294	Derived & bar-valued superconnection, curvature $\Theta_{\mathrm{MC}}$
  1295	 & Theorem~\ref{thm:bar-superconnection} \\
  1296	Analytic & renormalized graph forms on $\mathfrak{C}_\Gamma(\mathbf{z})$
  1297	 & Theorem~\ref{thm:analytic-yb} \\
  1298	Reduced & log connection $\Rightarrow$ associator, braiding
exec
/bin/zsh -lc "rg -n '\\\\begin\\{theorem\\}|\\\\label\\{' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
40:\label{chap:log-ht-monodromy-standalone}
66:\begin{theorem}[Synthesis theorem; \ClaimStatusProvedHere]% label removed: thm:synthesis
190:\begin{theorem}[Flatness of the shifted KZ/FM connection; \ClaimStatusProvedHere]% label removed: thm:strict-flatness
348:\begin{theorem}[Master curvature formula; \ClaimStatusProvedHere]% label removed: thm:master-curvature
393:\begin{theorem}[Support hierarchy; \ClaimStatusProvedHere]% label removed: thm:support-hierarchy
472:\begin{theorem}[First obstruction theorem; \ClaimStatusProvedHere]% label removed: thm:first-obstruction
625:\begin{theorem}[Existence, logarithmicity, and residue factorization; \ClaimStatusProvedHere]% label removed: thm:log-bphz-existence
674:\begin{theorem}[Analytic curvature formula; \ClaimStatusProvedHere]% label removed: thm:analytic-curvature
693:\begin{theorem}[Compactified-Stokes flatness; \ClaimStatusProvedHere]% label removed: thm:analytic-flatness
720:\begin{theorem}[Binary residues and the analytic $A_\infty$ Yang-Baxter identity; \ClaimStatusProvedHere]% label removed: thm:analytic-yb
742:\begin{theorem}[Family version over semistable degenerations; \ClaimStatusProvedHere]% label removed: thm:family-version
770:\begin{theorem}[Quantum concentration from classical concentration; \ClaimStatusProvedHere]% label removed: thm:quantum-concentration
795:\begin{theorem}[Canonical $\h$-adic strong deformation retract; \ClaimStatusProvedHere]% label removed: thm:canonical-retract
867:\begin{theorem}[One-form rigidity; \ClaimStatusProvedHere]% label removed: thm:one-form-rigidity
960:\begin{theorem}[Pentagon identity; \ClaimStatusProvedHere]% label removed: thm:pentagon
973:\begin{theorem}[Hexagon identities; \ClaimStatusProvedHere]% label removed: thm:hexagon
990:\begin{theorem}[Local monodromy and pure braid representations; \ClaimStatusProvedHere]% label removed: thm:pure-braid
1085:\begin{theorem}[Unconditionality for resolved quasi-linear lines; \ClaimStatusProvedHere]% label removed: thm:unconditionality
1102:\begin{theorem}[Boundary factorization after reduction; \ClaimStatusProvedHere]% label removed: thm:reduced-boundary-factorization
1168:\begin{theorem}[Smashing localization commutes with factorization homology; \ClaimStatusProvedHere]% label removed: thm:smashing-localization

thinking
**Refining category definitions**

I’m working on refining the categories. I need to consider `samefile_removed`, which indicates that a missing reference target has `label removed: target` within the same file. Then, there's `otherfile_removed`, which means that a target comment was removed in a different file. This points to potential cross-file stale migration, and for fixes, I might need to restore the label from the definition file or update the reference to the new live label. I should count these cases too!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict, Counter
pat_label=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
pat_ref=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
root='/Users/raeez/chiral-bar-cobar-vol2/chapters'
texts={}
for dp,_,fns in os.walk(root):
    for fn in fns:
        if fn.endswith('.tex'):
            p=os.path.join(dp,fn)
            texts[p]=open(p,encoding='utf-8').read()
# labels in chapters/live v2
labels=set()
for p,txt in texts.items():
    labels.update(m.group(1) for m in pat_label.finditer(txt))
# classify comment_removed by samefile or otherfile
same=other=0
examples_same=[]; examples_other=[]
seen=set()
for p,txt in texts.items():
    for i,line in enumerate(txt.splitlines(),1):
        for m in pat_ref.finditer(line):
            t=m.group(2)
            if t in labels or (p,i,t) in seen: continue
            if f'label removed: {t}' in txt:
                same +=1
                if len(examples_same)<20: examples_same.append((p,i,t))
            elif any(f'label removed: {t}' in otxt for q,otxt in texts.items() if q"'!=p):
                other +=1
                if len(examples_other)<20: examples_other.append((p,i,t))
print('"'samefile',same,'otherfile',other)
print('same examples')
for x in examples_same: print(x)
print('other examples')
for x in examples_other: print(x)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 2.70s:
samefile 257 otherfile 5
same examples
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 45, 'sec:PVA_axioms_complete')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 45, 'sec:higher_vanish')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 147, 'eq:PVA1a')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 155, 'rmk:Laurent_vs_poly')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 162, 'eq:PVA1b')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 244, 'eq:n3_cohomology')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 263, 'eq:n3_cohomology')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 267, 'eq:n3_cohomology')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 286, 'eq:Jacobi_shifted')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 290, 'eq:n3_cohomology')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 319, 'eq:n3_cohomology')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 321, 'eq:Stokes_n3')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 334, 'eq:Stokes_n3')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 358, 'eq:Jacobi_pre_two_terms')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 358, 'eq:Jacobi_pre_two_terms')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 381, 'eq:Jacobi_assembled')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 394, 'eq:Jacobi_assembled')
('/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex', 398, 'eq:Jacobi_assembled')
exec
/bin/zsh -lc "rg -n 'label removed: thm:MacMahon-connection|label removed: def:resolved|label removed: thm:stasheff-n4' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '318,330p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex | sed -n '250,266p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:227:% label removed: thm:stasheff-n4
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:758:% label removed: thm:MacMahon-connection
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1025:\begin{definition}[Resolved degree-zero line system]% label removed: def:resolved-line
 succeeded in 51ms:
   318	\begin{proposition}[Spectral-to-categorical bridge; \ClaimStatusProvedHere]
   319	\label{prop:spectral-to-categorical}
   320	\index{braiding!spectral-to-categorical bridge|textbf}
   321	\index{R-matrix@$R$-matrix!spectral-to-categorical bridge}
   322	Let $A$ be a logarithmic $\SCchtop$-algebra whose tree-level line
   323	complex is resolved in degree~$0$
   324	\textup(Definition~\textup{\ref{def:resolved}}\textup).
   325	Let $L_1, L_2$ be objects of the reduced line category
   326	$\cC_{\mathrm{line}}^{\mathrm{red}}$, and let $\gamma_{12}$ be the
   327	half-circle exchange path in $\Conf_2(\CC)$ taking $z_1$ around~$z_2$
   328	counterclockwise through angle~$\pi$.  Then the categorical braiding
   329	\[
   330	\beta_{L_1,L_2} \colon L_1 \otimes L_2 \xrightarrow{\ \sim\ }
 succeeded in 52ms:
   250	 \sum_{n \ge 0} p(n)\, q^n,
   251	\]
   252	the generating function for integer partitions $p(n)$.
   253	
   254	The connection to the MacMahon function emerges from the full
   255	$W_\infty$ algebra (generators at spins $s \ge 2$ only, i.e.\
   256	$W_{1+\infty}$ modulo the $\mathrm{U}(1)$ current). The
   257	Theorem~\textup{\ref{thm:MacMahon-connection}} computation gives
   258	\[
   259	 P_{W_\infty}(q, 1)
   260	 \;=\;
   261	 \prod_{k \ge 2} \frac{1}{1 - q^k}.
   262	\]
   263	In the \emph{weight-refined} bar cohomology, the bigraded character
   264	(Theorem~\textup{\ref{thm:MacMahon-connection}}) satisfies
   265	\[
   266	 \sum_{p,n} \dim H^p_n(B(W_\infty))\, q^n t^p
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex | sed -n '348,356p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
   348	
   349	\medskip
   350	\noindent\textbf{Step 2: The degree-$4$ Stasheff relation on $(W,W,W,W)$.}
   351	
   352	On cohomology ($m_1 = 0$ on all inputs), the degree-$4$ Stasheff
   353	identity (Theorem~\ref{thm:stasheff-n4}) specialises to five
   354	tree-composition terms:
   355	\begin{align}
   356	\label{eq:stasheff-4-WWWW}

thinking
**Evaluating code adjustment**

I think I should change `def:resolved` to `def:resolved-line` for clarity. About `thm:stasheff-n4`, it could be a local theorem? I wonder if I might need to look into the removed label in the `thqg_fm_calculus_extensions`. I’m just exploring options here! Opening that up might help clarify things further. It feels good to be proactive about fixing any potential issues.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex | sed -n '220,236p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   220	\]
   221	where $V_{\mathrm{int}}$ encodes the interaction vertices
   222	connecting the four insertions (tree-level Feynman diagrams with
   223	external legs at $z_1, \ldots, z_4$).
   224	\end{construction}
   225	
   226	\begin{theorem}[Stasheff identity at $n = 4$; \ClaimStatusProvedHere]
   227	% label removed: thm:stasheff-n4
   228	For inputs $a, b, c, d \in \A$, the $n = 4$ Stasheff identity
   229	reads:
   230	\begin{align}
   231	0 &= m_1(m_4(a,b,c,d)) \notag \\
   232	&\quad + m_4(m_1(a),b,c,d)
   233	 + (-1)^{|a|}\, m_4(a,m_1(b),c,d) \notag \\
   234	&\quad + (-1)^{|a|+|b|}\, m_4(a,b,m_1(c),d)
   235	 + (-1)^{|a|+|b|+|c|}\, m_4(a,b,c,m_1(d)) \notag \\
   236	&\quad + m_2(m_3(a,b,c),d)


thinking
**Reviewing document details**

I need to make some adjustments in my document references. First, for “Chapter” in the file, it would be clearer to change `Chapter\ref{chap:pva-descent}` to `Section\ref{sec:PVA_descent}` since it’s a section. Then, I noticed that the definition around line 68 lacks a label. It might be best to add `\label{def:modular-graph-coefficient-algebra}` right after that definition. Since line 71 refers to the "modular graph coefficient algebra," adding the label makes sense for consistency.
thinking
**Checking definitions and labels**

I need to look into the definition of the quartic resonance class in the document related to gravitational duality. I noticed that there’s a subsection for degree 4 quartic resonance class under duality around line 602 that might not be labeled correctly. So, I should search through lines 587 to 602 to ensure that the definition is appropriately labeled. It’s essential for clarity and consistency, so I’ll dig deeper into this section!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '584,604p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   584	is preserved.
   585	\end{proof}
   586	
   587	\subsubsection{Degree~$4$: quartic resonance class under duality}
   588	
   589	\begin{proposition}[Quartic resonance duality; \ClaimStatusProvedHere]
   590	% label removed: prop:thqg-IV-quartic-duality
   591	\index{quartic resonance class!duality}
   592	At degree~$4$:
   593	$\sigma(\mathfrak{Q}_\cA) = \mathfrak{Q}_{\cA^!}$.
   594	The clutching law is preserved:
   595	$\sigma(\xi^*_{\mathrm{sep}}\mathfrak{Q}_\cA)
   596	= \xi^*_{\mathrm{sep}}\mathfrak{Q}_{\cA^!}$.
   597	\end{proposition}
   598	
   599	\begin{proof}
   600	The quartic resonance class $\mathfrak{Q}_\cA$ is the genus-$0$,
   601	degree-$4$ component of $\Theta_\cA$ modulo gauge
   602	(Definition~\ref{def:nms-quartic-resonance-class}). By the $r = 4$
   603	case of Theorem~\ref{V1-thm:thqg-IV-shadow-duality},
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex | sed -n '456,468p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   456	\end{tabular}
   457	\end{center}
   458	\end{definition}
   459	
   460	\begin{proposition}[Named shadows; \ClaimStatusProvedHere]
   461	% label removed: prop:thqg-named-shadows
   462	\index{modular characteristic!as shadow}
   463	\index{cubic shadow}
   464	\index{quartic resonance class}
   465	The first three layers of the shadow obstruction tower are:
   466	\begin{enumerate}[label=\textup{(\roman*)}]
   467	\item \textbf{Modular characteristic} ($r=2$):
   468	 $\kappa(\cA) := \Theta_\cA^{\le 2}|_{\text{scalar}}$, the
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex | sed -n '468,486p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   468	 $\kappa(\cA) := \Theta_\cA^{\le 2}|_{\text{scalar}}$, the
   469	 supertrace of the identity on weight-$1$ generators. This is
   470	 Theorem~D of Volume~I.
   471	\item \textbf{Cubic shadow} ($r=3$):
   472	 $\mathfrak{C}(\cA) := \Theta_\cA^{\le 3} - \Theta_\cA^{\le 2}$,
   473	 the tree-level $3$-point coupling. Vanishes for class~G algebras;
   474	 nontrivial for class~L and above.
   475	\item \textbf{Quartic resonance class} ($r=4$):
   476	 $\mathfrak{Q}(\cA) := [\Theta'^{\le 4}_\cA]$, the equivalence class
   477	 of the quartic correction modulo gauge equivalence. For class~G
   478	 and~L, $\mathfrak{Q}(\cA) = 0$. The first nontrivial quartic
   479	 class is $\mathfrak{Q}(\beta\gamma)$.
   480	 The Virasoro contact invariant is
   481	 $Q^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$
   482	 (Volume~I, Theorem~\ref{thm:virasoro-quartic-class}).
   483	\end{enumerate}
   484	All three are determined by $\Theta_\cA$.
   485	\end{proposition}
   486	

thinking
**Evaluating label corrections**

I’m considering whether to add `\label{def:nms-quartic-resonance-class}` to this proposition or alter the reference to `prop:thqg-named-shadows`, since the line indicates it’s a Definition. It’s really a proposition about named shadows. A more precise fix could be to change `Definition\ref{def:nms-quartic-resonance-class}` to `Proposition\ref{prop:thqg-named-shadows}\textup{(iii)}` and also restore `\label{prop:thqg-named-shadows}`. I might check if there's a similar need for `def:shadow-depth-classes`.
exec
/bin/zsh -lc "rg -n 'shadow depth classification|class~\\\\textbf\\{G\\}|Definition.*shadow depth|begin\\{definition\\}.*shadow depth' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1576:The shadow depth classification
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2864:The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex | sed -n '632,646p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   632	be in the image of $d_2$.
   633	Hence $[o_5] \ne 0 \in H^2(F^5/F^6, d_2)$.
   634	\end{proof}
   635	
   636	\subsubsection*{The four complexity classes for 3d gravity}
   637	
   638	\begin{definition}[Shadow depth class]
   639	\label{def:gravity-shadow-depth-class}
   640	\index{shadow depth!G/L/C/M classification}
   641	The \emph{shadow depth class} of a chiral algebra~$\cA$ is the
   642	algebraic invariant $r_{\max}(\cA)
   643	:= \min\{r \ge 2 \mid o_{r+1}(\cA) = 0\}$
   644	($r_{\max} = \infty$ if no such $r$ exists), classifying
   645	$\cA$ into one of four classes:
   646	\begin{center}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex | sed -n '1126,1138p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1126	
  1127	\emph{Derivation of $\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$.}
  1128	The Koszul dual central charge $c' = 26 - c$ follows from the bar
  1129	cohomology computation: $H^1(\barB(\mathrm{Vir}_c))$ is generated
  1130	by a single field $T'$ of conformal weight~$2$ with OPE
  1131	$T'(z)\,T'(w) \sim (26-c)/2\,(z-w)^{-4} + \cdots$
  1132	(Theorem~\ref{thm:virasoro-koszul-dual} in Vol~I\@).
  1133	Equivalently, the Virasoro algebra is obtained from
  1134	$\widehat{\fsl}_2$ by quantum Drinfeld--Sokolov reduction with
  1135	central charge formula
  1136	$c(k) = 13 - 6(k+2) - 6/(k+2)$.
  1137	The Feigin--Frenkel involution $k \mapsto k' = -k - 4$ gives
  1138	$k' + 2 = -(k+2)$, hence

thinking
**Searching for theorems**

I'm looking for theorems, specifically `thm:virasoro-koszul-dual`, but it seems like that might be missing in volume one. I wonder if `thm:w3-koszul-dual` is the only one present in volume two. So, maybe I should search through volume one more thoroughly to see if that label is actually there. It feels a bit like a treasure hunt with the theorems! Let's track this down.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:virasoro-koszul-dual\\}|Virasoro.*Koszul dual|Virasoro Koszul dual' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/logarithmic_w_algebras.tex:514:The Virasoro sector of the Koszul dual has central charge
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:725:The $\beta\gamma$ system combines a bosonic weight-$1$ field $\beta$ and a bosonic weight-$0$ field $\gamma$. Its bar complex shares the discriminant $\Delta(x) = (1-3x)(1+x)$ with $\widehat{\mathfrak{sl}}_2$ and the Virasoro algebra. The Koszul dual is the $bc$ ghost system (\S\ref{sec:fermion-boson-koszul}).
/Users/raeez/chiral-bar-cobar/chapters/examples/moonshine.tex:227:The Virasoro Koszul duality $\mathrm{Vir}_c^! \simeq
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:438:At $k = -h^\vee$ (the \emph{critical level}), the Sugawara construction is undefined: the denominator $k + h^\vee$ vanishes, so no Virasoro subalgebra is produced. The critical level is distinguished on three counts: the theory admits a commutative chiral algebra structure (the classical limit), the center $Z(\widehat{\mathfrak{g}}_{-h^\vee})$ becomes infinite-dimensional (Feigin--Frenkel), and the algebra governs self-dual Yang--Mills theory. For Koszul duality, the critical level is the fixed point of the Feigin--Frenkel involution $k \mapsto -k - 2h^\vee$: the curvature $m_0 \propto (k + h^\vee)$ vanishes, making the bar complex a genuine (uncurved) dg coalgebra and the Koszul dual algebra uncurved.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1419:\begin{proposition}[Virasoro Koszul dual at generic central charge;
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1422:\index{Virasoro algebra!Koszul dual at generic $c$|textbf}
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:660:Item~(i): the Virasoro Koszul duality is $c \mapsto 26 - c$
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1533:alone. The Virasoro algebra $\mathrm{Vir}_c$ is Koszul dual to
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1842:$c = 26$ & Virasoro Koszul duality + $\kappa_{\mathrm{tot}} = 0$
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_critical_string_dichotomy.tex:918:pole $T_{(3)}T = c/2$ in the Virasoro OPE. The Koszul dual is
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_critical_string_dichotomy.tex:924:\index{Virasoro!Koszul dual}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_s_duality.tex:909:The Virasoro shadow generating function $H(t,c)$ at central charge~$c$ and its Koszul dual $H(t, 26-c)$ at central charge~$26-c$ are related by the involution $c \mapsto 26-c$. At degree~$2$: $\kappa(c) + \kappa(26-c) = 13$ (constant). At degree~$4$: $\Delta(c) + \Delta(26-c) = 6960/[(5c+22)(152-5c)]$ (Proposition~\ref{prop:thqg-IV-quartic-duality}). At all degrees: the sigma-invariant $\Delta^{(r)} := S_r(c) + S_r(26-c)$ is level-independent (i.e., independent of $c$) if and only if $r \leq 3$. For $r \geq 4$, the sigma-invariant is a nontrivial rational function of~$c$ whose denominator contains $c^{r-4}(5c+22)^{\lfloor(r-4)/2\rfloor}$: the dynamical content begins at degree~$4$.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_perturbative_finiteness.tex:2217:At the Virasoro self-duality point $c = 13$ (where $\mathrm{Vir}_c^! \cong \mathrm{Vir}_{26-c} = \mathrm{Vir}_{13}$), the modular characteristic is $\kappa = 13/2$ and the shadow free energies are $F_g = (13/2)\lambda_g^{\mathrm{FP}}$. This is NOT the special central charge $c = 26$ where the bosonic string becomes critical; $c = 13$ is distinguished by the property that the Koszul dual is isomorphic to the original algebra. The free energies at $c = 13$:
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:963: the $n$-th graded piece of the Virasoro Koszul dual coalgebra.
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:4518:The non-quadratic case (Virasoro, $W_N$, Yangian) is handled uniformly via $I$-adic completion; the uncompleted statement $\bar{B}^{\mathrm{ch}}(\mathcal{A})^{\vee} \simeq \mathcal{A}^!$ (bar coalgebra dualizes to the Koszul dual algebra) holds only in the quadratic case, where $I$-adic and discrete topologies coincide.
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:77:\item Virasoro and $\mathcal{W}_{\infty}$ Koszul duals: explicit
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:726:\begin{example}[Virasoro Koszul dual]
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2568:For Virasoro: the Koszul dual is $\mathrm{Vir}_{26-c}$
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex:3681:\subsection{Virasoro Verma modules under Koszul duality}
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_modules.tex:3701:\index{Virasoro algebra!Verma module!Koszul duality}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex | sed -n '1418,1426p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1418	
  1419	\begin{proposition}[Virasoro Koszul dual at generic central charge;
  1420	\ClaimStatusProvedHere]
  1421	\label{prop:virasoro-generic-koszul-dual}
  1422	\index{Virasoro algebra!Koszul dual at generic $c$|textbf}
  1423	For all $c \in \mathbb{C}$,
  1424	\begin{equation}\label{eq:vir-koszul-dual-generic}
  1425	\mathrm{Vir}_c^! \;\simeq\; \mathrm{Vir}_{26-c}.
  1426	\end{equation}

thinking
**Fixing references and aliases**

I need to adjust the reference to `Proposition\ref{V1-prop:virasoro-generic-koszul-dual}` and add an alias in the chapter-local Vol I alias file. It makes me wonder if a local theorem or proposition exists as a reference; probably not, but I should check. The simplest solution seems to be changing `thm:virasoro-koszul-dual` to `V1-prop:virasoro-generic-koszul-dual` and updating the alias file. I’ll focus on the exact context within the document next!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1476,1486p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'five theorems|all genera|genus0|e1-theorems|e1-five-theorems' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1271:\label{sec:e1-five-theorems-genus0}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2192:degree~$n$ with all generators at weight~$1$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:3343:The affine family has all generators at weight~$1$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:3419:For $V_k(\fg)$ with $\dim\fg=d$, all generators have
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1215:% label removed: sec:e1-five-theorems-genus0
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1483:main theorems at all genera on the ordered bar-level surface.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1498:\item At all genera: the genus-refined ordered shadow truncations of
 succeeded in 52ms:
  1476	= 0$ is automatic from $D_{F\!\Ass}^2 = 0$
  1477	(Theorem~\ref*{V1-thm:fass-d-squared-zero}, Vol~I), by the bar-intrinsic
  1478	construction: $\Theta^{E_1} = D^{E_1}_\cA - d_0$ satisfies MC
  1479	because $(D^{E_1}_\cA)^2 = 0$. This is the $E_1$ analogue of
  1480	Theorem~\ref*{V1-thm:mc2-bar-intrinsic}.
  1481	See Remark~\ref*{V1-rem:conj-modular-resolved} (Vol~I) and
  1482	Vol~I's all-genera $E_1$-modular Koszul chapter for the full $E_1$ five
  1483	main theorems at all genera on the ordered bar-level surface.
  1484	\end{proof}
  1485	
  1486	\begin{construction}[$E_1$ shadow obstruction tower]

thinking
**Searching for references**

I see there’s no specific reference at line 1481, just a starred remark from V1. I'm wondering if "local_orphan" might not be an actual term. But wait—line 1481 doesn't align with subsec:e1-five-theorems-all-genera. I need to double-check and search for the exact context or source. It feels like I'm missing something, and I want to get this right! Let's clarify that reference.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{subsec:e1-five-theorems-all-genera\\}|\\\\eqref\\{subsec:e1-five-theorems-all-genera\\}|subsec:e1-five-theorems-all-genera' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2026,2038p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2448,2460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2218,2230p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2026	
  2027	For the Virasoro algebra at genus~$1$, the non-Fredholm
  2028	correction involves the quartic contact invariant
  2029	$\mathfrak{Q}_{\mathrm{Vir}} = 10/[c(5c+22)]$
  2030	and all higher obstruction classes $o_r$ for $r \geq 5$
  2031	(the quintic obstruction $o_5$ is forced to be nonzero
  2032	by Theorem~\ref{thm:quintic-forced}). The full partition
  2033	function $Z_1(\mathrm{Vir}_c;\,\tau)$ at genus~$1$ is:
  2034	\[
  2035	Z_1(\mathrm{Vir}_c;\,\tau)
  2036	= \dedeta(\tau)^{-(c-1)}
  2037	= q^{-(c-1)/24}\prod_{n=2}^{\infty}(1-q^n)^{-1},
  2038	\]
 succeeded in 51ms:
  2448	\begin{remark}[Evidence]
  2449	The FM$\times$Conf product decomposition of
  2450	$\Steinberg_\Lambda$ gives a direct-sum splitting indexed by
  2451	$\Lambda^*/\Lambda$. On each component the continuous part is
  2452	$\FM_k(\bC) \times \Conf_k^{<}(\bR)$ with the charge-zero
  2453	sublattice fibre; its BM homology is the $k$-th bar piece of
  2454	$\operatorname{Sym} A^2(D)^{\otimes r}$ by the Bergman--Fock
  2455	identification of~\S\ref{sec:bergman-fock}. Summing over
  2456	components produces the tensor factor
  2457	$\ell^2(\Lambda^*/\Lambda)$, and the $L^2$-completion follows
  2458	from the sewing-envelope topology
  2459	of~\eqref{V1-eq:thqg-X-lattice-sewing-conj}.
  2460	\end{remark}
 succeeded in 51ms:
  2218	(ii)~the bar Hodge theorem
  2219	$\ker(\Delta_B) = H^*(B(\cA))$
  2220	(harmonic forms represent bar cohomology);
  2221	(iii)~for chirally Koszul~$\cA$, bar cohomology concentrates on
  2222	the diagonal (weight $=$ bar degree), giving a positive spectral
  2223	gap off the diagonal. Compare the screening Hodge theorem
  2224	(Theorem~\ref{thm:screening-hodge-theorem} in
  2225	\S\ref{sec:ym-spectral-gap}) for the analogous statement in the
  2226	Yang--Mills setting.
  2227	\end{remark}
  2228	
  2229	\subsubsection{Coderived categories and genus $g \geq 1$}
  2230	
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2638,2712p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2638	\begin{remark}[Non-Fredholm corrections from strata at infinity]%
  2639	% label removed: rem:steinberg-non-fredholm%
  2640	\index{non-Fredholm correction!strata at infinity}%
  2641	\index{Siegel modular form}%
  2642	For class-L algebras, the non-Fredholm correction
  2643	$\delta Z_g$ of
  2644	\S\ref{subsec:thqg-non-fredholm} receives a Steinberg
  2645	interpretation: it is the contribution from the
  2646	\emph{non-compact strata} of~$\fSb$, the strata at
  2647	infinity in the FM compactification
  2648	$\overline{\mathrm{FM}}_k(\Sigma_g)$. The genus-$g$
  2649	Steinberg variety carries a natural fibration
  2650	\[
  2651	\fSb^{(g)} \;\longrightarrow\; \mathbb{H}_g
  2652	\]
  2653	over the Siegel upper half-space $\mathbb{H}_g$, where
  2654	the fibre over $\Omega \in \mathbb{H}_g$ is the Steinberg
  2655	variety of the sewing kernel
  2656	$\sewker_g(\Omega)$. The compact strata produce the
  2657	Fredholm determinant $Z_g^{\mathrm{G}}$; the non-compact
exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:ym-spectral-gap\\}|spectral gap' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_* /Users/raeez/chiral-bar-cobar-vol2/chapters/connections | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:1593:\begin{corollary}[Screening spectral gap criterion; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex:472:\begin{corollary}[Screening spectral gap criterion; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:68:\subsection{The instanton-completed Steinberg and spectral gap}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:95:\begin{conjecture}[Mass gap as spectral gap; \ClaimStatusConjectured]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:97:In finite dimensions, the Steinberg variety $Z$ for a reductive group $G$ has a spectral gap
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:98:in the Laplacian on $H_*^{\mathrm{BM}}(Z)$: this is the spectral gap between the trivial
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:101:\emph{the spectral gap of the Laplacian on $H_*^{\mathrm{BM}}(\Steinb_b^{\mathrm{inst}})$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:108:to the spectral gap criterion.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:118:the mass gap is expected to be the spectral gap of the Steinberg correspondence.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:119:In the finite-dimensional model, the spectral gap is a consequence of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:570:\begin{corollary}[Screening spectral gap criterion; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:9177:spectral gap.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dg_shifted_factorization_bridge.tex:1071:separating one factor into three ordered factors with spectral gaps
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:1593:\begin{corollary}[Screening spectral gap criterion; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex:472:\begin{corollary}[Screening spectral gap criterion; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:68:\subsection{The instanton-completed Steinberg and spectral gap}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:95:\begin{conjecture}[Mass gap as spectral gap; \ClaimStatusConjectured]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:97:In finite dimensions, the Steinberg variety $Z$ for a reductive group $G$ has a spectral gap
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:98:in the Laplacian on $H_*^{\mathrm{BM}}(Z)$: this is the spectral gap between the trivial
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:101:\emph{the spectral gap of the Laplacian on $H_*^{\mathrm{BM}}(\Steinb_b^{\mathrm{inst}})$
exec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*spectral-gap[''^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:69:\label{subsec:instanton-steinberg-spectral-gap}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:96:\label{conj:mass-gap-spectral-gap}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:571:\label{cor:screening-spectral-gap-criterion}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex:473:\label{cor:screening-spectral-gap-criterion}
exec
/bin/zsh -lc "rg -n 'Bergman--Fock|Bergman Fock|\\\\label\\{["'^}]*bergman[''^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2322:cofree coalgebra completion of the Bergman Fock space.
2349:\underbrace{\operatorname{Sym} A^2(D)}_{\text{Bergman Fock space}}
2379:$V_\Lambda$ explicitly as a completion of the Bergman Fock
2454:$\operatorname{Sym} A^2(D)^{\otimes r}$ by the Bergman--Fock
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex | sed -n '2320,2360p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2320	is $\anbar(\cH_\kappa^!) \cong
  2321	\overline{\operatorname{Sym} A^2(D)}^{\mathsf{co}}$, the
  2322	cofree coalgebra completion of the Bergman Fock space.
  2323	
  2324	The genus-$g$ complementarity decomposition
  2325	$Z_g(\cH_\kappa) + Z_g(\cH_\kappa^!)
  2326	= (\det\operatorname{Im}\Omega)^{-\kappa/2}
  2327	\cdot (\zetareg\Delta)^{-\kappa/2}
  2328	+ (\det\operatorname{Im}\Omega)^{\kappa/2}
  2329	\cdot (\zetareg\Delta)^{\kappa/2}$
  2330	is a direct Fredholm manifestation of Theorem~C
  2331	(complementarity): what $\cH_\kappa$ sees as the positive
  2332	curvature $+\kappa \cdot \omega_g$, its Koszul dual $\cH_\kappa^!$
  2333	sees as negative curvature $-\kappa \cdot \omega_g$.
  2334	\end{remark}
  2335	
  2336	\subsubsection{The platonic chain and the sewing hierarchy}
  2337	
  2338	\begin{remark}[The platonic chain for Fredholm partition functions]%
  2339	% label removed: rem:thqg-X-platonic-chain%
exec
/bin/zsh -lc "rg -n '"'^'"\\\\sub(section|subsection|subsubsection).*Non-Fredholm|"'^'"\\\\sub(section|subsection|subsubsection).*Genus-2 Fredholm|label removed: subsec:thqg-genus2-fredholm|label removed: subsec:thqg-non-fredholm' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1732:\subsection{Non-Fredholm corrections for classes L, C, M}

thinking
**Searching for theorem labels**

I need to look into genus 2 and see what I can find regarding labels around the theorem. It seems like I might not be in the right section, but I’ll explore this further. Maybe I can uncover more relevant information or perhaps identify specific terms associated with genus 2 theories. I’ll keep digging to ensure I'm not missing anything critical here. Let's see what I can find!
exec
/bin/zsh -lc "rg -n 'Genus-2 Fredholm|genus-2 Fredholm|"'^'"\\\\sub(section|subsection|subsubsection).*Genus 2|"'^'"\\\\sub(section|subsection|subsubsection).*Genus-2' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1106:\subsubsection{Genus 2: two handles and the Siegel modular form}
1108:\begin{theorem}[Genus-2 Fredholm determinant;
1216:\begin{computation}[Genus-2 Fredholm determinant: leading terms;
exec
/bin/zsh -lc "rg -n 'quintic.*forced|o_5|fifth-order obstruction|\\\\label\\{["'^}]*quintic[''^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2031:(the quintic obstruction $o_5$ is forced to be nonzero
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2032:by Theorem~\ref{thm:quintic-forced}). The full partition
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3826:$o_5 \ne 0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4703:and $o_5 \ne 0$ \textup{(degree~$5$, nonvanishing for generic~$c$)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4721:The shadow values $\mathfrak{C}$, $\mathfrak{Q}$, $o_5$ are
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:8243:$S^{(3)}$ & $S_5$ & $m_5$ via $o_5 \neq 0$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:261:$o_5$ & $o_5(c)$ & $o_5(26-c)$ & ---
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:520:\label{thm:gravity-quintic-obstruction}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:523:$o_5(\mathrm{Vir}_c) \in H^2(F^5\gAmod/F^6\gAmod, d_2)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:542:o_5
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:558:o_5(T^{\otimes 5};\,\lambda_1,\ldots,\lambda_4)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:578:To verify that $o_5$ is not a coboundary, we must show
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:579:$[o_5] \ne 0 \in H^2(F^5\gAmod/F^6\gAmod, d_2)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:625:It follows that $o_5$ represents a nonzero class in
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:628:term $-c^2\lambda^5$ in $o_5$ has $\lambda$-degree~$5$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:631:Since $o_5$ has nonzero projection to degree~$5$, it cannot
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:633:Hence $[o_5] \ne 0 \in H^2(F^5/F^6, d_2)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:719:is nonzero but $o_5 = 0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:774: for generic~$c$: its image is $[o_5]$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:785:obstruction $o_5$. By
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:virasoro-quartic-class\\}|quartic class.*Virasoro|Virasoro.*quartic class' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 92ms:
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/D02_scope_inflation.md:1552:PROOF: \begin{proof}[Proof of {\textup{(iii)}}] We compute $J^r(\mathrm{Vir}_c)$ for $r = 2, \ldots, 8$. \medskip\noindent\textbf{Degree $2$ ($J^2$).} The curvature is $\kappa(\mathrm{Vir}_c) = c/2$. The quadratic jet is one-dimensional: \[ J^2(\mathrm{Vir}_c) = \C \cdot \kappa, \qquad \kappa = c/2. \] \medskip\noindent\textbf{Degree $3$ ($J^3$).} The cubic shadow $\mathfrak{C}(\mathrm{Vir}_c)$ is gauge-trivial: $[\mathfrak{C}] = 0 \in H^1(F^3/F^4, d_2)$. This follows from $H^1(F^3/F^4, d_2) = 0$ for Virasoro, which holds because the relevant Chevalley--Eilenberg cohomology of the Virasoro Lie algebra vanishes at the correct degree. After gauge transformation, the cubic contribution is absorbed. Thus: \[ J^3(\mathrm{Vir}_c) = J^2(\mathrm{Vir}_c), \qquad \cA^{\mathrm{sh}}_{3,0} = 0 \;\text{(after gauge)}. \] \medskip\noindent\textbf{Degree $4$ ($J^4$).} The quartic contact shadow is nonzero: \[ \mathfrak{Q}^{\mathrm{contact}}_{\mathrm{Vir}} = \frac{10}{c(5c+22)}. \] This is the canonical quartic class, independent of the gauge choice for the cubic term (Vol~I, Theorem~\ref*{thm:cubic-gauge-triviality}). The quartic jet is two-dimensional: \[ J^4(\mathrm{Vir}_c) = \C \cdot \kappa \oplus \C \cdot \mathfrak{Q}^{\mathrm{contact}}, \qquad \dim J^4 = 2. \] \medskip\noindent\textbf{Degree $5$ ($J^5$).} The quintic obstruction class $o_5(\mathrm{Vir}_c)$ is nonzero. This is the fundamental distinction between class~C and class~M: the Virasoro algebra has a nonvanishing quintic shadow. The proof is by direct computation: the cyclic contraction \[ o_5 = \sum_{\Gamma \in \mathsf{Gr}_5^{\mathrm{tree}}} \frac{1}{|\Aut(\Gamma)|}\, \Phi^{\mathrm{Vir}}_\Gamma \] sums over binary trees with five leaves, and at least one term is nonzero because the Virasoro composite $:(L_{-2})^2 L:$ generates a nonvanishing degree-$5$ cyclic trace. Therefore: \[ \dim \cA^{\mathrm{sh}}_{5,0} \geq 1, \qquad o_5 \neq 0. \] \medskip\noindent\textbf{Degree $6$ ($J^6$).} The degree-$6$ shadow receives contributions from two sources: trees with six leaves decorated by $m_2$ and $m_3$, and the first planted-forest correction at degree $6$. The dimension is $\dim \cA^{\mathrm{sh}}_{6,0} \geq 1$. \medskip\noindent\textbf{Degree $7$ ($J^7$).} Similar analysis: $\dim \cA^{\mathrm{sh}}_{7,0} \geq 1$. The degree-$7$ shadow is the first level at which a genuinely new geometric stratum (the codimension-$5$ boundary of $\ov{\M}_{0,8}$) contributes. \medskip\noindent\textbf{Degree $8$ ($J^8$).} At degree $8$, the shadow has $\dim \cA^{\mathrm{sh}}_{8,0} \geq 2$: the quartic-quartic interaction $\mathfrak{Q} \cdot \mathfrak{Q}$ generates a new independent shadow class beyond the cascading contributions from lower degrees. The dimension table is: \[ \renewcommand{\arraystretch}{1.3} \begin{array}{c|c|c|c|c|c|c|c} r & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ \hline \dim \cA^{\mathrm{sh}}_{r,0}(\mathrm{Vir}_c) & 1 & 0 & 1 & 1 & 1 & 1 & \geq 2 \\ \dim J^r(\mathrm{Vir}_c) & 1 & 1 & 2 & 3 & 4 & 5 & \geq 7 \end{array} \] \end{proof} 
/Users/raeez/chiral-bar-cobar/compute/lib/platonic_blue_team.py:938:        This is the canonical quartic class for Virasoro, obtained by
exec
/bin/zsh -lc "rg -n 'quartic.*obstruction|quartic.*class|contact invariant|10/\\[c\\(5c\\+22\\)\\]|10/\\[c\\(5c\\+22\\)\\]' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex /Users/raeez/chiral-bar-cobar/chapters/connections /Users/raeez/chiral-bar-cobar/chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 305

/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:718:contact invariant $\mathfrak{Q}^{\mathrm{contact}}_{\beta\gamma}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:883:independent cyclic invariants (the contact invariant and a
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1399:The quartic contact invariant is the genus-$0$ projection of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1447:coefficient of the unique contact invariant
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1467:of the contact invariant (the number of dihedral equivalence
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1491:\to 0$, and the quartic correction vanishes; semiclassical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1984:The quartic contact invariant
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:2066:the quartic contact invariant $\mathfrak{Q} \ne 0$ contributes
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:2296:The quartic contact invariant $\mathfrak{Q} = 10/(c(5c+22))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:49:$S_4(A)$ is the quartic shadow obstruction (the first obstruction
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:205:Virasoro, with its quartic pole, lives in class $\mathbf{M}$: the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:231: of class~$\mathbf{C}$: the quartic contact invariant $m_4 \ne 0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:905:\subsubsection*{The quartic contact invariant and infinite depth}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:908:relation produces the quartic contact invariant from the Kac
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:918:The contact invariant is the \emph{normalised} version of
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:1616:contact invariant denominator $c(5c+22)$; higher levels
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3823:$\mathfrak{Q} = 10/[c(5c+22)]$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3843:$\mathfrak{Q}^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$

thinking
**Searching for specific terms**

I'm recognizing that my search might be too broad. It might be more effective to narrow it down to volume 2, especially if there's a local theorem related to it. I’m thinking of focusing on labels around the quartic contact invariant. Perhaps I should look for specific terms like `thm:gravity-quartic-obstruction` or `def:quartic-contact-invariant`. It seems I need to search for those exact labels to find what I'm looking for.
exec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*quartic[''^}]*'"\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1348:\label{thm:gravity-quartic-soft}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1478:\begin{equation}\label{eq:quartic-soft-ward}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:910:\begin{equation}\label{eq:gravity-quartic}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3840:\label{comp:gravity-quartic-correction}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:7920:\begin{equation}\label{eq:w3-quartic-decomposition}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex | sed -n '4920,4965p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4920	the collision divisors $D_S$, and there are finitely many such
  4921	divisors at each arity),
  4922	hence the filtration is bounded and exhaustive at each arity.
  4923	The spectral sequence
  4924	$E_1^{p,q} = H^{p+q}(\mathrm{gr}^p)
  4925	\Rightarrow H^{p+q}(\mathrm{tot})$
  4926	therefore converges (bounded filtration theorem;
  4927	Weibel~\cite{Wei94}, Theorem~5.5.1). By the spectral sequence
  4928	comparison theorem (loc.\ cit., Theorem~5.5.11),
  4929	a filtered map inducing a quasi-isomorphism
  4930	on the associated graded induces an isomorphism on all
  4931	subsequent pages, hence on the abutment.
  4932	Therefore $\iota^*$ is a quasi-isomorphism of dg~Lie algebras.
  4933	
  4934	\medskip
  4935	\noindent\textbf{Step~5: Colour-profile summary.}
  4936	Steps~3--4 establish the quasi-isomorphism $\iota^*$ on all
  4937	colour profiles at once, without decomposing into pure closed,
  4938	pure open, and mixed sectors. Three observations record how
  4939	the argument specialises to each sector.

thinking
**Checking remarks in text**

I see that I need to fix something related to remarks in the text. I’m thinking I should either add a proper remark or remove the sentence entirely. There's a possibility that a remark was omitted, and the exact fix might be to delete the forward reference at line 4963 since it doesn't seem to follow with a remark. 

I might need to check the lines below 4965, or even scan the next 30 lines for context.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex | sed -n '4963,4990p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4963	see Remark~\ref{rem:kunneth-geometric-insight}.
  4964	
  4965	\medskip
  4966	\noindent\textbf{Step~7: Verification of parts (a)--(c).}
  4967	
  4968	\textit{Part~(a).}
  4969	Under the quasi-isomorphism $(\iota^*)^{-1}$, a
  4970	two-coloured tree $T$ in $\mathbf{B}(\cP)$ indexes an
  4971	$L_\infty$ bracket $\ell_T$ on $\gSC_T$ via the convolution
  4972	pre-Lie product. The image under $\iota^*$ of this bracket is
  4973	the brace operation $\{-\}\{-,\ldots,-\}$ on
  4974	$C^\bullet_{\mathrm{ch,top}}(\cA,\cA)$: the Koszul resolution
  4975	$\iota$ maps bar elements (indexed by trees) to their
  4976	Koszul-dual images, and the convolution pre-Lie product on
  4977	$\Hom_\Sigma(\cP^{\text{\textexclamdown}}, \End_\cA)$ is the
  4978	brace product by the definition of braces from the cooperad
  4979	structure on $\cP^{\text{\textexclamdown}}$
  4980	(\cite{LV12}, \S10.1).
  4981	
  4982	\textit{Part~(b).}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '2928,2938p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2928	The obstruction therefore lives in
  2929	$\Har^3\bigl(U(\fg[t]),\, U(\fg[t])\bigr)$.
  2930	\end{proof}
  2931	
  2932	\begin{lemma}[Vanishing of the leading Harrison obstruction;
  2933	\ClaimStatusProvedHere]
  2934	\label{lem:harrison-leading-vanishing}
  2935	\index{Harrison cohomology!K\"unneth decomposition}
  2936	By the tensor decomposition
  2937	$U(\fg[t]) = U(\fg) \otimes \bC[t]$ and the K\"unneth
  2938	formula for Harrison cohomology of tensor products


thinking
**Evaluating theorem adjustments**

I need to change `prop:` to `lem:` in the reference, which is a good start. We’ve taken care of `sec:bergman-fock` and `sec:ym-spectral-gap` already. For `sec:universal-bulk-proofs`, I’m contemplating whether to remove a sentence or add a section. A critical fix would be to note that the proof doesn’t exist and add the appropriate label. The harsh but necessary fix would be to downgrade the theorem to a conjecture until the proof is found. It’s a tough choice!
thinking
**Reflecting on theorem classification**

I’m considering whether to classify the finding as CRITICAL. An immediate fix might be to change `\begin{theorem}[The universal bulk; \ClaimStatusProvedHere]` to `\begin{conjecture}[The universal bulk]`, or to add a proof. However, if there’s potential for a proof, downgrading seems more accurate. 

I might suggest replacing the sentence "The proof of each part is given in \S\ref{sec:universal-bulk-proofs}.” with “Proof omitted.” But this doesn’t fully address the unresolved refs. I’ll clarify that if no proof exists, the section should be explicitly stated in the report.
exec
/bin/zsh -lc "rg -n '\\\\(ref|eqref)\\{V1-conj:lattice-sewing\\}|\\\\(ref|eqref)\\{V1-constr:platonic-package\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1838:(Construction~\ref{V1-constr:platonic-package}) transforms under $\sigma$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2381:Conjecture~\textup{\ref{V1-conj:lattice-sewing}} predicts that
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2432:Conjecture~\textup{\ref{V1-conj:lattice-sewing}};
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2436:\textup{(}Conjecture~\textup{\ref{V1-conj:lattice-sewing})}.


thinking
**Considering LaTeX Solutions**

I'm thinking about a potential fix where I create `chapters/frame/main_aliases.tex` and move the `\phantomsection\label{target}` from the main file into it. Then, I would `\input` that file before `chapters/theory/introduction`. This should resolve the chapter-local issues. If the main label isn't a phantom section but a theorem label, moving just the label might misnumber it, but maybe that's okay. Creating a chapter-local alias file is likely sufficient since the user is focused on this specific resolution.
thinking
**Evaluating Alias File Placement**

I'm considering that if I move the alias file under the chapters without the proper counter context, it might lead to issues. It's really important to ensure that the context is accurate when making changes like this. I don't want to throw off the references or cause any confusion in the document. It seems I need to be careful about the placement to maintain clarity and correct numbering throughout.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/main.tex | sed -n '768,778p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   768	\phantomsection\label{sec:shadow-depth-classification}%
   769	\phantomsection\label{sec:w-algebras-explicit-appendix}%
   770	\phantomsection\label{subsec:holographic-modular-koszul-datum}%
   771	\phantomsection\label{subsec:spectral-ope-and-yangian}%
   772	\phantomsection\label{subsubsec:virasoro-complementarity-offset}%
   773	\phantomsection\label{thm:bar-cobar-isomorphism-main}%
   774	\phantomsection\label{thm:ch-core-helicity-chirality}%
   775	\phantomsection\label{thm:collision-residue-twisting}%
   776	\phantomsection\label{thm:convolution-d-squared-zero}%
   777	\phantomsection\label{thm:geometric-equals-operadic-bar}%
   778	\phantomsection\label{thm:gravity-mc-primitive-package}%
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import defaultdict, Counter
pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
# live labels with paths
v2live=defaultdict(list)
for rel in ['main.tex','chapters','appendices']:
    path=os.path.join('/Users/raeez/chiral-bar-cobar-vol2',rel)
    files=[]
    if os.path.isfile(path): files=[path]
    else:
        for dp,_,fns in os.walk(path):
            for fn in fns:
                if fn.endswith('.tex'): files.append(os.path.join(dp,fn))
    for f in files:
        for i,line in enumerate(open(f,encoding='utf-8'),1):
            for m in pat.finditer(line): v2live[m.group(1)].append((f,i,line.strip()))
# chapters labels
v2ch=set()
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            f=os.path.join(dp,fn)
            for line in open(f,encoding='utf-8'):
                for m in pat.finditer(line): v2ch.add(m.group(1))
# missing refs unique and subcategory hidden imports
pat_ref=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
missing=set()
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            f=os.path.join(dp,fn)
            for line in open(f,encoding='utf-8'):
                for m in pat_ref.finditer(line):
                    if m.group(2) not in v2ch: missing.add(m.group(2))
sub=Counter()
for t in missing:
    if t in v2live and t not in v2ch:
        loc=v2live[t][0][0]
        if t.startswith('part:'): sub['main_part']+=1
        elif '/appendices/' in loc: sub['appendix']+=1
        elif os.path.basename(loc)=='main.tex' and ('V1-'+t) in v2live: sub['main_plain_has_v1_alias']+=1
        elif os.path.basename(loc)=='main.tex' and t.startswith('V1-'): sub['main_v1_alias']+=1
        elif os.path.basename(loc)=='main.tex': sub['main_plain_only']+=1
        else: sub['other_nonchapter']+=1
print(sub)
for cat in sub:
    print('\\n',cat)
    n=0
    for t in sorted(missing):
        if not (t in v2live and t not in v2ch): continue
        loc=v2live[t][0][0]
        cond=False
        if cat=='main_part': cond=t.startswith('part:')
        elif cat=='appendix': cond='/appendices/' in loc
        elif cat=='main_plain_has_v1_alias': cond=os.path.basename(loc)=='main.tex' and ('V1-'+t) in v2live
        elif cat=='main_v1_alias': cond=os.path.basename(loc)=='main.tex' and t.startswith('V1-')
        elif cat=='main_plain_only': cond=os.path.basename(loc)=='main.tex' and not t.startswith('V1-') and ('V1-'+t) not in v2live
        elif cat=='other_nonchapter': cond=('/appendices/' not in loc and os.path.basename(loc)"'!='"'main.tex')
        if cond:
            print(t, loc, v2live[t][0][1])
            n+=1
            if n>=20: break
PY" in /Users/raeez/chiral-bar-cobar succeeded in 233ms:
Counter({'main_v1_alias': 367, 'main_plain_only': 61, 'main_plain_has_v1_alias': 28, 'main_part': 7, 'appendix': 1})

 main_v1_alias
V1-chap:yangians /Users/raeez/chiral-bar-cobar-vol2/main.tex 408
V1-comp:holographic-ss-vir /Users/raeez/chiral-bar-cobar-vol2/main.tex 409
V1-comp:thqg-I-hs-fermion /Users/raeez/chiral-bar-cobar-vol2/main.tex 410
V1-comp:thqg-I-hs-heisenberg /Users/raeez/chiral-bar-cobar-vol2/main.tex 411
V1-comp:thqg-V-affine-yangian /Users/raeez/chiral-bar-cobar-vol2/main.tex 412
V1-comp:thqg-V-quartic-graviton /Users/raeez/chiral-bar-cobar-vol2/main.tex 788
V1-comp:vir-physical-cc /Users/raeez/chiral-bar-cobar-vol2/main.tex 413
V1-conj:master-bv-brst /Users/raeez/chiral-bar-cobar-vol2/main.tex 414
V1-conj:thqg-I-non-perturbative /Users/raeez/chiral-bar-cobar-vol2/main.tex 792
V1-const:vol1-genus-spectral-sequence /Users/raeez/chiral-bar-cobar-vol2/main.tex 793
V1-constr:clifford-spectral /Users/raeez/chiral-bar-cobar-vol2/main.tex 417
V1-constr:nms-sewing-product /Users/raeez/chiral-bar-cobar-vol2/main.tex 419
V1-constr:obstruction-recursion /Users/raeez/chiral-bar-cobar-vol2/main.tex 794
V1-constr:thqg-III-verdier-involution /Users/raeez/chiral-bar-cobar-vol2/main.tex 795
V1-constr:thqg-V-binary-extraction /Users/raeez/chiral-bar-cobar-vol2/main.tex 796
V1-constr:thqg-VII-mc-recursion /Users/raeez/chiral-bar-cobar-vol2/main.tex 797
V1-conv:higher-genus-differentials /Users/raeez/chiral-bar-cobar-vol2/main.tex 798

thinking
**Inspecting theorem labels**

I'm looking at the need to restore a label in a theorem, which seems fine to me. Now, I should inspect the MacMahon theorem and confirm whether the label has been removed. I see there's something to check around 758, so I'll ensure I do that. It's important to verify this detail, as accuracy matters in the context of the theorem!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex | sed -n '750,764p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   750	results (Theorem~\ref{prop:WN-modular-vanishing} and Proposition~\ref{prop:WN-H1}).
   751	The modular operator is $(N-1)\partial$ at each finite stage; in the
   752	colimit it diverges in coefficient but remains zero modulo total derivatives
   753	at every finite truncation. The relevant $H^1$ stabilizes at dimension $1$
   754	because the central-charge parameter persists in the limit.
   755	\end{proof}
   756	
   757	\begin{theorem}[MacMahon connection; \ClaimStatusProvedHere]
   758	% label removed: thm:MacMahon-connection
   759	The bar cohomology of $W_\infty$ grows at the rate of three-dimensional
   760	partitions. Specifically, the graded character of $H^\bullet(B(W_\infty))$
   761	in the reduced-weight grading is
   762	\[
   763	\sum_{p \ge 0} \dim H^p_n(B(W_\infty))\, q^n t^p
   764	\;=\;
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:screening-hodge-theorem\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex:447:\label{thm:screening-hodge-theorem}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex:545:\label{thm:screening-hodge-theorem}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex | sed -n '430,450p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   430	The associated \emph{screening differential} on
   431	\[
   432	\mathcal K_{\mathrm{scr}}:=\mathcal H\otimes \Lambda^{\bullet}(\mathbb C^r)
   433	\]
   434	is
   435	\[
   436	\partial_{\mathrm{scr}}:=\sum_{i=1}^r \epsilon_i S_i,
   437	\qquad
   438	\partial_{\mathrm{scr}}^*:=\sum_{i=1}^r \iota_i S_i^*.
   439	\]
   440	Its \emph{screening Laplacian} is
   441	\[
   442	L_{\mathrm{scr}}:=\partial_{\mathrm{scr}}\partial_{\mathrm{scr}}^*+\partial_{\mathrm{scr}}^*\partial_{\mathrm{scr}}.
   443	\]
   444	\end{definition}
   445	
   446	\begin{theorem}[Screening Hodge theorem; \ClaimStatusProvedHere]
   447	\label{thm:screening-hodge-theorem}
   448	For a Hilbert-screening datum,
   449	\[
exec
/bin/zsh -lc "rg -n '"'^'"\\\\sub(section|subsection|subsubsection)' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_instanton_screening.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{subsec:e1-five-theorems-all-genera\\}')
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            p=os.path.join(dp,fn)
            for i,line in enumerate(open(p,encoding='utf-8'),1):
                if pat.search(line):
                    print(p,i,line.strip())
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "rg -n 'subsec:e1-five-theorems-all-genera' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:






thinking
**Evaluating classification issues**

I’m thinking that the earlier classification might have some issues due to strange line mapping. It could be the file using an incorrect target. I should trust the latest search results. I might need to recalculate the local orphan list with the current classification since it showed something odd. Maybe it’s due to a stale reference, or the file has changed. It’s probably best not to ignore it, and I should inspect missing unique classifications. I'll build a final report script that examines the actual missing uses.
thinking
**Considering manual overrides for targets**

I'm thinking that for tricky targets, it might be necessary to use a manual override dictionary with precise fixes. I feel good about having this option for categories that don't require manual intervention. This way, I can ensure accuracy and efficiency while managing different scenarios. I just want to make sure I'm using the best approach for each category and maintaining clarity throughout the process. Let's keep refining this!
thinking
**Correcting a reference**

I’m looking at a line with a theorem reference, which notes `(Theorem\ref{thm:screening-hodge-theorem} in \S\ref{sec:ym-spectral-gap})`. It seems I've realized that the text already includes the theorem reference. So, the simple fix would be to delete `in \S\ref{sec:ym-spectral-gap}`. It’s a relief to find a straightforward solution!
thinking
**Considering template adjustments**

I think I need a simpler template based on the target prefix, like `chap:`, `sec:`, or others. It might be more effective to move the label onto the actual heading in the chapter file. If the main file doesn’t have a clear label, it could just mention the main line without giving too much detail about the heading. I wonder if I should attach the label to the heading in the real file for clarity.
thinking
**Planning report generation**

I need to think through how the user asked for a file with specific line references, so maybe it can be per-use with the same target repeated. I could create a report with around 1380 lines generated from templates, which seems manageable. I might include a header summary programmatically. I’m considering creating a `markdown` file. Also, I might make a summary JSON for counts, though that may not be necessary. I should gather actual data for the report and consider using a Python script for generation. Spot-checking counts after this process will be important too.
codex
The hard cases are now pinned down. I have enough evidence to generate the full line-accurate report without hand-waving: `257` same-file deleted anchors, `941` hidden imports from outside `chapters/`, `137` missing Vol I aliases, and a small residue of stale-name/orphan targets with specific replacements.
Plan update
  ✓ Enumerate all labels and reference commands in Vol II chapters
  ✓ Identify unresolved targets and inspect each source location in context
  ✓ Search for intended nearby labels or duplicate naming patterns to derive exact fixes
  → Re-verify surviving findings and produce line-accurate audit report

thinking
**Generating a report**

I need to generate a report now. It sounds like I should write a script for this, and using Python seems like a good choice for creating the file. Since I’m not making manual edits, that might be okay. I should remember to include some commentary before the file write that says, "Before performing file edits of any kind, provide updates explaining what edits you are making." Keeping track of that commentary is essential!
codex
I’m writing the audit artifact into the workspace as a generated markdown report so the full `1380`-line surface is inspectable without truncation. The file will contain one finding per unresolved use, with the definition site and exact fix attached from the classification pass.





thinking
**Generating report file**

I need to generate a report file, and I could use Python for that. First, I should determine the output path, which might be something like `/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_audit_2025...`. I might need to create the directory if it doesn't exist, using either Python or a script with mkdir commands. I want the final report to include clickable links, possibly formatted in Markdown. I need to decide whether to use absolute or relative file paths in the report too.
thinking
**Crafting a script for label management**

I want to create a script that loads labels from various chapter versions and collects missing uses of actual line text. I’ll classify each use and include a manual overrides dictionary for mapping target labels to custom fixes and severity levels. For same-file removals, the severity is set to CRITICAL, with fixes defined as restoring labels at comment lines. For targets from other files, I’ll assign manual fixes and severity. I also need to determine how to handle missing aliases and decide on their severity levels, possibly defaulting to HIGH due to potential cross-volume issues.
thinking
**Adjusting label references**

I need to fix the reference for the `V1-` target and move the corresponding alias from the main file to the chapter-local `vol1_aliases`. I must check if the target is currently plain and if `V1-target` exists. The problem is that a plain label resolves only through the main stub while a namespaced Vol I alias already exists. To fix this, I’ll change the reference to `\ref{V1-target}` and relocate the `\phantomsection\label{V1-target}` into `chapters/frame/vol1_aliases.tex`. The severity for main plain-only situations will be set to HIGH.
thinking
**Organizing report findings**

I need to focus on the user’s request about referencing “7879 ref-family uses.” It might help to include direct text lines and define where information is found, which could involve paths and line numbers. For cases like the same file, I should note any definition comments. It’s important to ground claims in the content I’ve actually read. In the final report, I can summarize findings but also point to the full details in the report file for user inspection.
thinking
**Finalizing the report**

I think the final report could include a statement like, “Full report: [file]. Summary...” to cover the user's request effectively. It might also be beneficial to include 3-5 top sample findings directly in the final output. This way, the user gets a clear sense of the most important results while also knowing they can access the complete report for more details. Balancing the summary with key findings seems like a solid approach!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, json
from collections import defaultdict
from pathlib import Path

vol2 = '/Users/raeez/chiral-bar-cobar-vol2'
root = f'{vol2}/chapters'
v1 = '/Users/raeez/chiral-bar-cobar'
v3 = '/Users/raeez/calabi-yau-quantum-groups'
out = '/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md'

label_pat = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat = re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')

def load_labels(paths):
    labels = defaultdict(list)
    files = []
    for path in paths:
        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            for dp, _, fns in os.walk(path):
                for fn in fns:
                    if fn.endswith('.tex'):
                        files.append(os.path.join(dp, fn))
    for f in files:
        try:
            with open(f, encoding='utf-8') as fh:
                for i, line in enumerate(fh, 1):
                    for m in label_pat.finditer(line):
                        labels[m.group(1)].append((f, i, line.rstrip('\\n')))
        except Exception:
            pass
    return labels, sorted(files)

v2ch_labels, chapter_files = load_labels([root])
v2live_labels, _ = load_labels([f'{vol2}/main.tex', f'{vol2}/chapters', f'{vol2}/appendices'])
v1live_labels, _ = load_labels([f'{v1}/main.tex', f'{v1}/chapters', f'{v1}/appendices'])
v3live_labels, _ = load_labels([f'{v3}/main.tex', f'{v3}/chapters', f'{v3}/appendices'])

chapter_text = {f: Path(f).read_text(encoding='utf-8') for f in chapter_files}
chapter_lines = {f: txt.splitlines() for f, txt in chapter_text.items()}

# locate commented-out labels
removed_map = defaultdict(list)
for f, txt in chapter_text.items():
    for i, line in enumerate(txt.splitlines(), 1):
        m = re.search(r'label removed:\\s*(["'^'"\\s%]+)', line)
        if m:
            removed_map[m.group(1)].append((f, i, line.rstrip('\\n')))

manual = {
    'ass:H1-H4': {
        'severity': 'CRITICAL',
        'problem': 'The sentence cites "'`'"\\\\ref{ass:H1-H4}"'` but this W-algebra hypothesis package has no live assumption label anywhere in Vol II chapters; the only nearby surface is the local remark beginning here.'"',
        'fix': 'Add "'`'"\\\\label{ass:H1-H4}"'` to the remark at `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:55` and keep the current reference text only if you also label the individual hypotheses `(H1)`--`(H3)` in the same remark.'"'
    },
    'hyp:H1': {
        'severity': 'CRITICAL',
        'problem': 'The sentence cites "'`'"\\\\ref{hyp:H1}"'` but the `(H1)` item in this local W-algebra hypothesis remark is unlabelled.'"',
        'fix': 'Insert "'`'"\\\\label{hyp:H1}"'` immediately before the `(H1)` item at `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:58`.'"'
    },
    'hyp:H3': {
        'severity': 'CRITICAL',
        'problem': 'The sentence cites "'`'"\\\\ref{hyp:H3}"'` but the `(H3)` item in this local W-algebra hypothesis remark is unlabelled.'"',
        'fix': 'Insert "'`'"\\\\label{hyp:H3}"'` immediately before the `(H3)` item at `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:60`.'"'
    },
    'chap:pva-descent': {
        'severity': 'CRITICAL',
        'problem': 'This cites a non-existent chapter label "'`chap:pva-descent`; the only live target in Vol II chapters is the section label `sec:PVA_descent` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex:2`.'"',
        'fix': 'Change "'`Chapter~'"\\\\ref{chap:pva-descent}"'` to `Section~'"\\\\ref{sec:PVA_descent}"'` at this line.'"'
    },
    'def:modular-graph-coefficient-algebra': {
        'severity': 'CRITICAL',
        'problem': 'The proof cites "'`Definition~'"\\\\ref{def:modular-graph-coefficient-algebra}"'` but the definition introducing the modular graph coefficient algebra at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:68` has no label.'"',
        'fix': 'Add "'`'"\\\\label{def:modular-graph-coefficient-algebra}"'` to the definition beginning at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:68`.'"'
    },
    'def:nms-quartic-resonance-class': {
        'severity': 'CRITICAL',
        'problem': 'This cites a non-existent definition label for the quartic resonance class; the live Vol II surface that actually defines the object is the unlabelled proposition "'`Named shadows` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:460`.'"',
        'fix': 'Restore "'`'"\\\\label{prop:thqg-named-shadows}"'` on the proposition at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:460`, then change this citation to `Proposition~'"\\\\ref{prop:thqg-named-shadows}\\\\textup{(iii)}"'`.'"'
    },
    'def:shadow-depth-classes': {
        'severity': 'CRITICAL',
        'problem': 'The text cites "'`Definition~'"\\\\ref{def:shadow-depth-classes}"'` but the live Vol II label is `def:gravity-shadow-depth-class` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:638`.'"',
        'fix': 'Change this citation to "'`Definition~'"\\\\ref{def:gravity-shadow-depth-class}"'`.'"'
    },
    'prop:harrison-leading-vanishing': {
        'severity': 'CRITICAL',
        'problem': 'The cited result exists only as "'`'"\\\\label{lem:harrison-leading-vanishing}"'` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2932`; the proposition label in this sentence is stale.'"',
        'fix': 'Change "'`Proposition~'"\\\\ref{prop:harrison-leading-vanishing}"'` to `Lemma~'"\\\\ref{lem:harrison-leading-vanishing}"'`.'"'
    },
    'rem:bp-EN-level': {
        'severity': 'CRITICAL',
        'problem': 'This refers to a non-existent remark label; the live local remark carrying the cited Bershadsky--Polyakov/non-principal dichotomy is "'`rem:bp-coproduct-resolved` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3462`.'"',
        'fix': 'Change this citation to "'`Remark~'"\\\\ref{rem:bp-coproduct-resolved}"'`.'"'
    },
    'rem:kunneth-geometric-insight': {
        'severity': 'CRITICAL',
        'problem': 'This forward reference points to no remark anywhere in Vol II chapters; the argument immediately continues and no such remark follows.',
        'fix': 'Delete the clause "'`; see Remark~'"\\\\ref{rem:kunneth-geometric-insight}"'` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:4962-4963`.'"'
    },
    'sec:bergman-fock': {
        'severity': 'CRITICAL',
        'problem': 'The text cites "'`'"\\\\S\\\\ref{sec:bergman-fock}"'` but no section carries that label; the relevant local heading is the unlabelled subsubsection `The platonic chain and the sewing hierarchy` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2336`.'"',
        'fix': 'Add "'`'"\\\\label{sec:bergman-fock}"'` to the subsubsection at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2336`.'"'
    },
    'sec:log-ht-monodromy': {
        'severity': 'CRITICAL',
        'problem': 'This cites a non-existent section label; the live monodromy entry point is the chapter label "'`chap:log-ht-monodromy` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1`.'"',
        'fix': 'Change "'`Section~'"\\\\ref{sec:log-ht-monodromy}"'` to `Chapter~'"\\\\ref{chap:log-ht-monodromy}"'`.'"'
    },
    'sec:universal-bulk-proofs': {
        'severity': 'CRITICAL',
        'problem': 'The file promises a proof section "'`'"\\\\S\\\\ref{sec:universal-bulk-proofs}"'`, but no such section exists and the theorem above has no proof block.'"',
        'fix': 'Delete the sentence at "'`/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:291-293`; if the theorem is meant to stay `'"\\\\ClaimStatusProvedHere"'`, add a real proof section separately before restoring any cross-reference.'"'
    },
    'sec:ym-spectral-gap': {
        'severity': 'CRITICAL',
        'problem': 'The sentence adds a dead section reference after an already sufficient theorem citation; no "'`sec:ym-spectral-gap` label exists anywhere in Vol II chapters.'"',
        'fix': 'Delete "'`in '"\\\\S\\\\ref{sec:ym-spectral-gap}"'` from this sentence and leave `Theorem~'"\\\\ref{thm:screening-hodge-theorem}"'` as the only citation.'"'
    },
    'subsec:thqg-non-fredholm': {
        'severity': 'CRITICAL',
        'problem': 'This points to a missing subsection label for the non-Fredholm-correction discussion; the live heading is the unlabelled subsection "'`Non-Fredholm corrections for classes L, C, M` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1732`.'"',
        'fix': 'Add "'`'"\\\\label{subsec:thqg-non-fredholm}"'` to the subsection at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1732`.'"'
    },
    'subsec:thqg-genus2-fredholm': {
        'severity': 'CRITICAL',
        'problem': 'This points to a missing subsection label for the genus-2 Fredholm discussion; the live heading is the unlabelled subsubsection "'`Genus 2: two handles and the Siegel modular form` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1106`.'"',
        'fix': 'Add "'`'"\\\\label{subsec:thqg-genus2-fredholm}"'` to the subsubsection at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1106`.'"'
    },
    'thm:bar-superconnection': {
        'severity': 'CRITICAL',
        'problem': 'The table cites a theorem label that does not exist; the governing theorem for the bar-valued superconnection is the unlabelled "'`Master curvature formula` theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:348`.'"',
        'fix': 'Restore "'`'"\\\\label{thm:master-curvature}"'` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:348`, then change this citation to `Theorem~'"\\\\ref{thm:master-curvature}"'`.'"'
    },
    'thm:quintic-forced': {
        'severity': 'CRITICAL',
        'problem': 'This cites a non-existent theorem label; the live Vol II theorem proving the quintic obstruction is "'`thm:gravity-quintic-obstruction` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:520`.'"',
        'fix': 'Change this citation to "'`Theorem~'"\\\\ref{thm:gravity-quintic-obstruction}"'`.'"'
    },
    'thm:shifted-kz-connection': {
        'severity': 'CRITICAL',
        'problem': 'The table cites a theorem label that does not exist; the live theorem for the strict shifted KZ/FM connection is the unlabelled "'`Flatness of the shifted KZ/FM connection` theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:190`.'"',
        'fix': 'Restore "'`'"\\\\label{thm:strict-flatness}"'` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:190`, then change this citation to `Theorem~'"\\\\ref{thm:strict-flatness}"'`.'"'
    },
    'thm:spectral-ybe': {
        'severity': 'CRITICAL',
        'problem': 'This theorem label does not exist; the live Vol II Yang--Baxter theorem is "'`thm:YBE` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:68`.'"',
        'fix': 'Change this citation to "'`Theorem~'"\\\\ref{thm:YBE}"'`.'"'
    },
    'thm:virasoro-koszul-dual': {
        'severity': 'CRITICAL',
        'problem': 'This cites a non-existent Vol II theorem label for the Virasoro duality statement; the live Vol I statement is "'`prop:virasoro-generic-koszul-dual` at `/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1419`.'"',
        'fix': 'Change this citation to "'`Proposition~'"\\\\ref{V1-prop:virasoro-generic-koszul-dual}"'` and add `'"\\\\phantomsection\\\\label{V1-prop:virasoro-generic-koszul-dual}"'` to `chapters/frame/vol1_aliases.tex` in Vol II.'"'
    },
    'thm:virasoro-quartic-class': {
        'severity': 'CRITICAL',
        'problem': 'This cites a non-existent theorem label for the Virasoro quartic-contact formula; the live Vol II theorem is "'`thm:gravity-quartic-soft` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1348`.'"',
        'fix': 'Change this citation to "'`Theorem~'"\\\\ref{thm:gravity-quartic-soft}"'`.'"'
    },
    'thm:MacMahon-connection': {
        'severity': 'CRITICAL',
        'problem': 'These references target a theorem whose label was deleted in another Vol II file; the theorem surface is at "'`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757` with `% label removed: thm:MacMahon-connection`.'"',
        'fix': 'Restore "'`'"\\\\label{thm:MacMahon-connection}"'` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757`.'"'
    },
    'def:resolved': {
        'severity': 'CRITICAL',
        'problem': 'This stale label dropped the "'`-line` suffix; the live definition is `def:resolved-line` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1025`.'"',
        'fix': 'Change this citation to "'`Definition~'"\\\\ref{def:resolved-line}"'`.'"'
    },
    'thm:stasheff-n4': {
        'severity': 'CRITICAL',
        'problem': 'This reference points to a theorem whose label was deleted in another Vol II file; the theorem surface is at "'`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:226` with `% label removed: thm:stasheff-n4`.'"',
        'fix': 'Restore "'`'"\\\\label{thm:stasheff-n4}"'` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:226`.'"'
    },
    'V1-conj:lattice-sewing': {
        'severity': 'CRITICAL',
        'problem': 'This points to a dead Vol I alias with no live target in the current Vol I chapter tree; the actual local Vol II surface is the unlabelled open problem "'`Lattice sewing envelope` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2375`.'"',
        'fix': 'Restore "'`'"\\\\label{prob:thqg-X-lattice-sewing}"'` on the open problem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:2375`, then change this citation to `Open Problem~'"\\\\ref{prob:thqg-X-lattice-sewing}"'`.'"'
    },
    'V1-constr:platonic-package': {
        'severity': 'CRITICAL',
        'problem': 'This points to a dead Vol I construction alias; the live local Vol II replacement is the unlabelled proposition "'`Holographic modular Koszul datum under $S$-duality` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1796`.'"',
        'fix': 'Restore "'`'"\\\\label{prop:thqg-IV-holographic-datum}"'` on the proposition at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1796`, then change this citation to `Proposition~'"\\\\ref{prop:thqg-IV-holographic-datum}"'`.'"'
    },
    'thm:level-rank': {
        'severity': 'HIGH',
        'problem': 'This is a plain Vol I theorem reference with no Vol II alias; the live target exists only in Vol I "'`main.tex:1831` as `thm:level-rank`.'"',
        'fix': 'Change this citation to "'`Theorem~'"\\\\ref{V1-thm:level-rank}"'` and add `'"\\\\phantomsection\\\\label{V1-thm:level-rank}"'` to `chapters/frame/vol1_aliases.tex` in Vol II.'"'
    },
    'rem:gz26-wn-comparison-conjectural': {
        'severity': 'MEDIUM',
        'problem': 'This line points to the Vol I remark label even though the local Vol II file already defines "'`rem:vol2-gz26-wn-comparison-conjectural` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:168`.'"',
        'fix': 'Change this citation to "'`Remark~'"\\\\ref{rem:vol2-gz26-wn-comparison-conjectural}"'` and drop the `Vol~I,` prefix in the prose.'"'
    },
    'chap:ordered-associative-chiral-kd': {
        'severity': 'MEDIUM',
        'problem': 'The prefix is wrong: the live chapter label is "'`ch:ordered-associative-chiral-kd` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:37`.'"',
        'fix': 'Change this citation to "'`Chapter~'"\\\\ref{ch:ordered-associative-chiral-kd}"'`.'"'
    },
}

# utility

def target_def(labset, target):
    return labset.get(target, [])

def fmt_loc(loc):
    path, line, *_ = loc
    return f'{path}:{line}'

# collect references
refs = []
for f in chapter_files:
    for i, line in enumerate(chapter_lines[f], 1):
        for m in ref_pat.finditer(line):
            target = m.group(2)
            if target not in v2ch_labels:
                refs.append((f, i, m.group(1), target, line.rstrip('\\n')))

findings = []
for f, i, cmd, target, line in refs:
    use_loc = f'{f}:{i}'
    if target in manual:
        ent = manual[target]
        findings.append((ent['severity'], f, i, f'- [{ent[\"severity\"]}] {use_loc} — PROBLEM: {ent[\"problem\"]} FIX: {ent[\"fix\"]}'))
        continue

    same_removed = [loc for loc in removed_map.get(target, []) if loc[0] == f]
    other_removed = [loc for loc in removed_map.get(target, []) if loc[0] "'!= f]

    if same_removed:
        loc = same_removed[0]
        findings.append(('"'CRITICAL', f, i, f'- [CRITICAL] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: {target}` at `{fmt_loc(loc)}`, so the anchor was deleted and the prose was not updated. FIX: restore `'"\\\\label{{{target}}}"'` at `{fmt_loc(loc)}` and keep this reference unchanged.'"'))
        continue

    if target.startswith('part:') and target in v2live_labels and target not in v2ch_labels:
        loc = v2live_labels[target][0]
        slug = target.split(':',1)[1].replace('-', '_')
        findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` resolves only via `{fmt_loc(loc)}` in `main.tex`; the part label lives outside `chapters/`, so this chapter depends on a hidden structural import. FIX: extract the `'"\\\\part"'` block carrying `'"\\\\label{{{target}}}"'` from `{fmt_loc(loc)}` into `chapters/frame/part_{slug}.tex`, then `'"\\\\input"'` that file from `main.tex` so the label lives under `chapters/`.'"'))
        continue

    if target in v2live_labels and target not in v2ch_labels:
        loc = v2live_labels[target][0]
        path = loc[0]
        if '/appendices/' in path:
            findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` is a hidden appendix import; the only target is `{fmt_loc(loc)}` outside `chapters/`. FIX: move `{path}` under `chapters/appendices/` and keep `'"\\\\label{{{target}}}"'` there, then update `main.tex` to input the relocated file.'"'))
        elif os.path.basename(path) == 'main.tex' and target.startswith('V1-'):
            findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` resolves only through the naked alias `'"\\\\phantomsection\\\\label{{{target}}}"'` at `{fmt_loc(loc)}` in `main.tex`; the chapter tree itself has no local target. FIX: move `'"\\\\phantomsection\\\\label{{{target}}}"'` from `{fmt_loc(loc)}` into `chapters/frame/vol1_aliases.tex` and `'"\\\\input"'` that file before the first chapter.'"'))
        elif os.path.basename(path) == 'main.tex' and ('V1-'+target) in v2live_labels:
            alias_loc = v2live_labels['V1-'+target][0]
            findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` resolves only through a hidden `main.tex` alias at `{fmt_loc(loc)}`, even though the namespaced Vol I bridge label `V1-{target}` already exists at `{fmt_loc(alias_loc)}`. FIX: change this citation to `{cmd}{{V1-{target}}}` and move `'"\\\\phantomsection\\\\label{{V1-{target}}}"'` from `{fmt_loc(alias_loc)}` into `chapters/frame/vol1_aliases.tex`.'"'))
        else:
            findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` resolves only through `{fmt_loc(loc)}` in `main.tex`, not from any file under `chapters/`; this is a hidden import from the driver file. FIX: move `'"\\\\phantomsection\\\\label{{{target}}}"'` from `{fmt_loc(loc)}` into `chapters/frame/vol2_aliases.tex` and `'"\\\\input"'` that file before `chapters/theory/introduction.tex`.'"'))
        continue

    if target.startswith('V1-'):
        base = target[3:]
        if base in v1live_labels:
            base_loc = v1live_labels[base][0]
            findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` has no Vol II target at all, but the live Vol I source label `{base}` exists at `{fmt_loc(base_loc)}`. FIX: add `'"\\\\phantomsection\\\\label{{{target}}}"'` to `chapters/frame/vol1_aliases.tex`, sourced from `{fmt_loc(base_loc)}`, and `'"\\\\input"'` that alias file before the first chapter.'"'))
        else:
            findings.append(('CRITICAL', f, i, f'- [CRITICAL] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` has no target in Vol II chapters and no live base label `{base}` in the current Vol I source tree; this cross-volume citation points to dead surface. FIX: delete this `'"\\\\ref"'` and replace it with a local Vol II citation or restore a live Vol I label before reintroducing any cross-volume reference.'"'))
        continue

    if target in v1live_labels:
        base_loc = v1live_labels[target][0]
        findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` is a bare Vol I label with no Vol II alias; the only live target is `{fmt_loc(base_loc)}` in Volume I. FIX: change this citation to `{cmd}{{V1-{target}}}` and add `'"\\\\phantomsection\\\\label{{V1-{target}}}"'` to `chapters/frame/vol1_aliases.tex`.'"'))
        continue

    if target in v3live_labels:
        base_loc = v3live_labels[target][0]
        findings.append(('HIGH', f, i, f'- [HIGH] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` points outside Vol II chapters to a Vol III label at `{fmt_loc(base_loc)}` with no local alias. FIX: change this citation to a namespaced Vol III alias and add that alias under `chapters/frame/vol3_aliases.tex` before relying on `'"\\\\ref"'`.'"'))
        continue

    if other_removed:
        loc = other_removed[0]
        findings.append(('CRITICAL', f, i, f'- [CRITICAL] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` has no live target in `chapters/`; the only matching surface is a deleted label marker at `{fmt_loc(loc)}` in another Vol II file, so the citation is stale after a rename/removal. FIX: restore `'"\\\\label{{{target}}}"'` at `{fmt_loc(loc)}` or retarget this citation to the new live label before keeping the reference.'"'))
        continue

    if target.startswith('chap:') and ('ch:'+target[5:]) in v2ch_labels:
        ch_loc = v2ch_labels['ch:'+target[5:]][0]
        findings.append(('MEDIUM', f, i, f'- [MEDIUM] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` uses the wrong chapter-label prefix; the live label is `ch:{target[5:]}` at `{fmt_loc(ch_loc)}`. FIX: change this citation to `{cmd}{{ch:{target[5:]}}}`.'"'))
        continue

    findings.append(('CRITICAL', f, i, f'- [CRITICAL] {use_loc} — PROBLEM: "'`{cmd}{{{target}}}` has no target anywhere in the live Vol II chapters tree and no trustworthy external alias or replacement label was found in the live Vol I/II/III sources. FIX: remove this `'"\\\\ref"'` and replace it with a citation to a real labelled statement only after that label exists on the live surface.'"'))

# sort by severity then file/line
sev_order = {'CRITICAL':0,'HIGH':1,'MEDIUM':2,'LOW':3}
findings.sort(key=lambda x:(sev_order[x[0]], x[1], x[2], x[3]))

checked = 7879
findings_n = len(findings)

Path('/Users/raeez/chiral-bar-cobar/audit').mkdir(parents=True, exist_ok=True)
with open(out, 'w', encoding='utf-8') as fh:
    fh.write('# Vol II Chapters Unresolved Reference Audit\\n\\n')
    fh.write('Scope: "'`~/chiral-bar-cobar-vol2/chapters/` only.'"\\n\\n')
    fh.write(f'Checked "'`'"\\\\ref"'`-family uses: {checked}'"\\n\\n')
    for _, _, _, bullet in findings:
        fh.write(bullet + '\\n')
    fh.write('\\n## Summary\\n')
    fh.write(f'Checked: {checked} | Findings: {findings_n} | Verdict: FAIL\\n')
print(out)
print(findings_n)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 389ms:
/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md
1351

thinking
**Verifying report findings**

It looks like the report has 1351 findings instead of the expected 1380. I'm thinking some might be excluded due to duplicates or perhaps manual classification in some use lines. I should check the references, especially the ones in `\ref*`, against the earlier count of 7879. The 1351 count might be based on current references that only include commands, which is odd because we had 1380 earlier. I need to recompute the missing count to see what’s going on.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
labels=set()
refs=0
missing=0
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            p=os.path.join(dp,fn)
            txt=open(p,encoding='utf-8').read().splitlines()
            for line in txt:
                for m in label_pat.finditer(line): labels.add(m.group(1))
for dp,_,fns in os.walk('/Users/raeez/chiral-bar-cobar-vol2/chapters'):
    for fn in fns:
        if fn.endswith('.tex'):
            p=os.path.join(dp,fn)
            for line in open(p,encoding='utf-8'):
                for m in ref_pat.finditer(line):
                    refs+=1
                    if m.group(2) not in labels: missing+=1
print('refs',refs,'missing',missing)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 128ms:
refs 7881 missing 1351
codex
The generated report surfaced a smaller but still severe final count after re-running the parser on the live tree: `7881` `\ref`-family uses, `1351` unresolved within `chapters/`. I’m correcting the report header to match the verified final counts, then I’ll close with the path and verdict.

thinking
**Updating report counts**

I need to update the report counts, and I'm considering how to do that efficiently. Using Python's replace function seems like a quick way to get it done. It should allow me to modify the necessary data without too much hassle. I want to make sure everything lines up perfectly, as accuracy is key in my updates. I’m curious if there’s anything I should double-check after I replace the counts.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p=Path('/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md')
text=p.read_text(encoding='utf-8')
text=text.replace('Checked "'`'"\\\\ref"'`-family uses: 7879'"','Checked "'`'"\\\\ref"'`-family uses: 7881'"')
text=text.replace('Checked: 7879 | Findings: 1351 | Verdict: FAIL','Checked: 7881 | Findings: 1351 | Verdict: FAIL')
p.write_text(text, encoding='utf-8')
print('updated')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
updated

thinking
**Reviewing report details**

I think I should inspect the top lines and summary of the report. It seems essential to get a clear understanding of the main points and the overall findings. I want to make sure I'm catching any crucial details. I wonder if there are specific sections I should focus on, or if I can summarize them all at once. Let's take a closer look!
exec
/bin/zsh -lc "sed -n '1,18p' /Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Vol II Chapters Unresolved Reference Audit

Scope: `~/chiral-bar-cobar-vol2/chapters/` only.

Checked `\ref`-family uses: 7881

- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6388 — PROBLEM: This refers to a non-existent remark label; the live local remark carrying the cited Bershadsky--Polyakov/non-principal dichotomy is `rem:bp-coproduct-resolved` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3462`. FIX: Change this citation to `Remark~\ref{rem:bp-coproduct-resolved}`.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1285 — PROBLEM: `eqref{eq:log-ht-chain}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:log-ht-chain` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1268`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:log-ht-chain}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1268` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1306 — PROBLEM: `eqref{eq:log-ht-chain}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:log-ht-chain` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1268`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:log-ht-chain}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1268` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:257 — PROBLEM: These references target a theorem whose label was deleted in another Vol II file; the theorem surface is at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757` with `% label removed: thm:MacMahon-connection`. FIX: Restore `\label{thm:MacMahon-connection}` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757`.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:264 — PROBLEM: These references target a theorem whose label was deleted in another Vol II file; the theorem surface is at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757` with `% label removed: thm:MacMahon-connection`. FIX: Restore `\label{thm:MacMahon-connection}` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757`.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:410 — PROBLEM: These references target a theorem whose label was deleted in another Vol II file; the theorem surface is at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757` with `% label removed: thm:MacMahon-connection`. FIX: Restore `\label{thm:MacMahon-connection}` on the theorem at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_modular_pva_extensions.tex:757`.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:112 — PROBLEM: `eqref{eq:spinor-g1-action}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:spinor-g1-action` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:100`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:spinor-g1-action}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:100` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:265 — PROBLEM: `eqref{eq:spinor-g1-action}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:spinor-g1-action` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:100`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:spinor-g1-action}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:100` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:515 — PROBLEM: `eqref{eq:general-spinor-alpha}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:general-spinor-alpha` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:499`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:general-spinor-alpha}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:499` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:515 — PROBLEM: `eqref{eq:general-spinor-beta}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:general-spinor-beta` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:503`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:general-spinor-beta}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:503` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:552 — PROBLEM: `eqref{eq:general-spinor-alpha}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:general-spinor-alpha` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:499`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:general-spinor-alpha}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:499` and keep this reference unchanged.
- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:552 — PROBLEM: `eqref{eq:general-spinor-beta}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:general-spinor-beta` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:503`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:general-spinor-beta}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_anomaly_extensions.tex:503` and keep this reference unchanged.
exec
/bin/zsh -lc 'tail -n 5 /Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:809 — PROBLEM: `ref{V1-thm:cech-hca}` has no Vol II target at all, but the live Vol I source label `thm:cech-hca` exists at `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:5169`. FIX: add `\phantomsection\label{V1-thm:cech-hca}` to `chapters/frame/vol1_aliases.tex`, sourced from `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:5169`, and `\input` that alias file before the first chapter.
- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:830 — PROBLEM: `ref{V1-prop:two-element-strict}` has no Vol II target at all, but the live Vol I source label `prop:two-element-strict` exists at `/Users/raeez/chiral-bar-cobar/chapters/theory/quantum_corrections.tex:878`. FIX: add `\phantomsection\label{V1-prop:two-element-strict}` to `chapters/frame/vol1_aliases.tex`, sourced from `/Users/raeez/chiral-bar-cobar/chapters/theory/quantum_corrections.tex:878`, and `\input` that alias file before the first chapter.

## Summary
Checked: 7881 | Findings: 1351 | Verdict: FAIL
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os
from collections import Counter
# recompute categories matching report logic roughly
pat_label=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
pat_ref=re.compile(r'\\\\(ref|eqref|autoref|cref|Cref|pageref)\\{(["'^}]+)'"\\}')
vol2='/Users/raeez/chiral-bar-cobar-vol2'
v1='/Users/raeez/chiral-bar-cobar'
v3='/Users/raeez/calabi-yau-quantum-groups'

def load(paths):
    d={}
    files=[]
    for p in paths:
        if os.path.isfile(p): files.append(p)
        else:
            for dp,_,fns in os.walk(p):
                for fn in fns:
                    if fn.endswith('.tex'): files.append(os.path.join(dp,fn))
    out={}
    for f in files:
        for i,line in enumerate(open(f,encoding='utf-8'),1):
            for m in pat_label.finditer(line): out.setdefault(m.group(1),[]).append((f,i))
    return out, files
v2ch, chapter_files = load([f'{vol2}/chapters'])
v2live,_=load([f'{vol2}/main.tex',f'{vol2}/chapters',f'{vol2}/appendices'])
v1live,_=load([f'{v1}/main.tex',f'{v1}/chapters',f'{v1}/appendices'])
v3live,_=load([f'{v3}/main.tex',f'{v3}/chapters',f'{v3}/appendices'])
texts={f:open(f,encoding='utf-8').read() for f in chapter_files}
removed={}
for f,t in texts.items():
    for i,line in enumerate(t.splitlines(),1):
        m=re.search(r'label removed:\\s*(["'^'"\\s%]+)', line)
        if m: removed.setdefault(m.group(1),[]).append((f,i))
manual_keys={'ass:H1-H4','hyp:H1','hyp:H3','chap:pva-descent','def:modular-graph-coefficient-algebra','def:nms-quartic-resonance-class','def:shadow-depth-classes','prop:harrison-leading-vanishing','rem:bp-EN-level','rem:kunneth-geometric-insight','sec:bergman-fock','sec:log-ht-monodromy','sec:universal-bulk-proofs','sec:ym-spectral-gap','subsec:thqg-non-fredholm','subsec:thqg-genus2-fredholm','thm:bar-superconnection','thm:quintic-forced','thm:shifted-kz-connection','thm:spectral-ybe','thm:virasoro-koszul-dual','thm:virasoro-quartic-class','thm:MacMahon-connection','def:resolved','thm:stasheff-n4','V1-conj:lattice-sewing','V1-constr:platonic-package','thm:level-rank','rem:gz26-wn-comparison-conjectural','chap:ordered-associative-chiral-kd'}
cat=Counter(); sev=Counter()
for f in chapter_files:
    for i,line in enumerate(open(f,encoding='utf-8'),1):
        for m in pat_ref.finditer(line):
            t=m.group(2)
            if t in v2ch: continue
            if t in manual_keys:
                c='manual'; s='critical' if t not in {'thm:level-rank','rem:gz26-wn-comparison-conjectural','chap:ordered-associative-chiral-kd'} else ('high' if t=='thm:level-rank' else 'medium')
            elif t in removed and any(loc[0]==f for loc in removed[t]): c='samefile_removed'; s='critical'
            elif t.startswith('part:') and t in v2live and t not in v2ch: c='main_part'; s='high'
            elif t in v2live and t not in v2ch:
                loc=v2live[t][0][0]
                if '/appendices/' in loc: c='appendix_hidden'; s='high'
                elif os.path.basename(loc)=='main.tex' and t.startswith('V1-'): c='main_v1_alias'; s='high'
                elif os.path.basename(loc)=='main.tex' and ('V1-'+t) in v2live: c='main_plain_has_v1_alias'; s='high'
                elif os.path.basename(loc)=='main.tex': c='main_plain_only'; s='high'
                else: c='other_hidden'; s='high'
            elif t.startswith('V1-') and t[3:] in v1live: c='missing_v1_alias'; s='high'
            elif t.startswith('V1-'): c='dead_v1'; s='critical'
            elif t in v1live: c='plain_v1'; s='high'
            elif t in v3live: c='plain_v3'; s='high'
            elif t in removed: c='otherfile_removed'; s='critical'
            elif t.startswith('chap:') and ('ch:'+t[5:]) in v2ch: c='prefix_drift'; s='medium'
            else: c='hard_orphan'; s='critical'
            cat[c]+=1; sev[s]+=1
print('categories',cat)
print('severity',sev)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 402ms:
categories Counter({'main_v1_alias': 663, 'samefile_removed': 232, 'missing_v1_alias': 132, 'main_part': 131, 'main_plain_only': 77, 'main_plain_has_v1_alias': 64, 'manual': 29, 'hard_orphan': 10, 'plain_v1': 7, 'appendix_hidden': 6})
severity Counter({'high': 1081, 'critical': 270})




thinking
**Summarizing reference audit**

The user requested an audit for unresolved references in Volume II, similar to what they mentioned before. I need to find all `\ref{}` instances that don't resolve, which includes definitions and imports. Including `\eqref` seems acceptable since they mentioned "every missing definition." I should clarify that our report covers the entire reference family. It’s important to ensure the report file path is clickable. The final output shouldn’t be lengthy, but I’ll link to the full findings for reference.
thinking
**Breaking down unresolved references**

I conducted an audit of 7,881 reference-family usages in Volume II chapters and discovered 1,351 that remain unresolved. It's quite a significant number! I’ll need to break down the findings to provide clarity on which references are problematic. This data will help guide the user in resolving these issues. I want to ensure that the report is thorough and easy to understand, giving them a clear overview of the unresolved uses.
thinking
**Evaluating formatting commands**

I think I need to mention that I audited commands like `\ref`, `\eqref`, `\autoref`, `\cref`, `\Cref`, and `\pageref` because they all utilize the same label surface. The user pointed out that `\ref{}` behaves similarly, so that aligns well. However, I’m wondering if it’s essential to use the exact date for any of this—doesn’t seem necessary right now. Let's keep things straightforward!
thinking
**Reviewing document issues**

I need to check for missing aliases in Volume I—there are 132 of them. Also, I’ve got 46 local stale-name or orphan references to address. Maybe I should note one example of hard failures, but I don’t want to make the final document too lengthy. Keeping it concise, I think two paragraphs and one short bullet list will work well. That sounds like a good plan for now!
codex
Full findings are in [vol2_chapters_unresolved_refs_report.md](/Users/raeez/chiral-bar-cobar/audit/vol2_chapters_unresolved_refs_report.md). The report is line-accurate and formatted exactly as requested: `[SEVERITY] file:line — PROBLEM: ... FIX: ...`.

I audited the full ref surface inside `~/chiral-bar-cobar-vol2/chapters/` and included `\ref`, `\eqref`, `\autoref`, `\cref`, `\Cref`, and `\pageref`, since they all hit the same label-resolution surface. The verified breakdown is:

- `232` same-file deleted anchors: the file still contains `% label removed: ...` but the prose still cites the dead label.
- `941` hidden imports from outside `chapters/`: mostly `main.tex` phantom labels and one appendix label.
- `132` missing `V1-*` aliases: the live Vol I label exists, but Vol II never created the bridge alias.
- `46` residual stale-name/orphan cases: wrong prefix, wrong local target, dead archived Vol I target, or a forward reference to a section/remark that does not exist.

## Summary
Checked: 7881 | Findings: 1351 | Verdict: FAIL
tokens used
581,316
