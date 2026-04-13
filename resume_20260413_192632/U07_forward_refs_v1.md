# U07_forward_refs_v1 (1390s)



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
session id: 019d880f-5694-7aa1-aa01-54e1e9eae2a6
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

Find all forward references: \ref{} to labels that appear LATER in the file or in a later chapter. Are these genuine forward refs or dangling? For dangling: provide the fix.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers


thinking
**Planning code exploration**

I'm thinking about spawning explorer agents to search through the code. The developer tool lets me spawn agents, and I can use explorer agents in parallel to tackle subsets of the repository. I need to inspect the file structure first, probably focusing on LaTeX in chapters. I’ll search for \ref occurrences and labels, checking if they're defined later or if they’re dangling. I might need to limit this to Volume I if that's what the user meant. It sounds like a big task, so I’ll plan to update as I go along.
thinking
**Considering command execution**

I'm thinking about using `exec_command` to check the relevant skill and maybe look into key instructions. I might also want to read through certain resources like CLAUDE and the red team summary for context. Since the audit seems important, parallel reads using `multi_tool_use.parallel` could speed things up, but I should limit it to developer tools. Instead of searching manually, I should prefer explorer agents first to avoid redundancy and trust their results. It sounds like a good idea to spawn an explorer to map the TeX label and reference ordering.
codex
I’m treating this as a repo-wide audit of `\ref{...}` surfaces in Volume I: first I’ll map the manuscript order, collect every `\label`/`\ref`, and separate true forward references from dangling references before I verify each candidate in source.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'missing'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

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
**Planning for forward references**

I have required reads and need to audit forward references. Maybe I should plan to use an explorer agent since it involves the codebase question and manual search. However, the instruction says to "always prefer explorers," which seems like the way to go. I’ll use it to query the repository structure or script. Writing a script to parse and compute label positions sounds good too, but I should focus on \ref{} occurrences, as the user explicitly limited the request to that.
thinking
**Creating a plan for forward references**

I’m considering what being exhaustive means—should it include all \ref-like commands? The user specifically asked for "Find all forward references: \ref{} to labels that appear LATER," so it seems I should focus only on literal \ref. I can mention that I've checked all literal `\ref{}` calls in files included by `main.tex`. I probably need to exclude \Cref and similar commands. Building an audit surface sounds good, and I could use a script without needing to edit anything. I'll create a plan for this!
codex
Using `deep-beilinson-audit` for this turn because the task is adversarial, repo-wide, and needs exact evidence rather than generic linting. I’ve loaded the constitutional files; next I’m extracting the manuscript include order and building a verified `\ref`→`\label` map so the findings are grounded in actual source positions.
Plan update
Repo-wide audit of literal \ref forward references in the Volume I manuscript, with source-grounded findings only.
  → Recover manuscript order from `main.tex` and included TeX files
  • Extract every literal `\label{}` and `\ref{}` with file and line positions
  • Classify each ref as backward, same-file forward, later-chapter forward, or dangling
  • Re-read every candidate finding in source and draft exact fixes
  • Return severity-ordered findings with summary counts
exec
/bin/zsh -lc "rg -n '\\\\(input|include)\\{' main.tex chapters appendices frontmatter preamble.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: frontmatter: No such file or directory (os error 2)
rg: preamble.tex: No such file or directory (os error 2)
main.tex:846:\include{chapters/frame/preface}
main.tex:850: \input{chapters/frame/guide_to_main_results}
main.tex:859:\include{chapters/theory/introduction}
main.tex:874:\include{chapters/frame/heisenberg_frame}
main.tex:963:\include{chapters/theory/fourier_seed}
main.tex:970:\include{chapters/theory/algebraic_foundations}
main.tex:976:\include{chapters/theory/three_invariants}
main.tex:982:\include{chapters/theory/configuration_spaces}
main.tex:988:\include{chapters/theory/bar_construction}
main.tex:994:\include{chapters/theory/cobar_construction}
main.tex:1002:% \include{chapters/theory/bar_cobar_adjunction}
main.tex:1004:\input{chapters/theory/bar_cobar_adjunction_curved}
main.tex:1005:\input{chapters/theory/bar_cobar_adjunction_inversion}
main.tex:1010:\input{appendices/homotopy_transfer}
main.tex:1022:\include{chapters/theory/poincare_duality}
main.tex:1030:\include{chapters/theory/chiral_koszul_pairs}
main.tex:1031:\include{chapters/theory/koszul_pair_structure}
main.tex:1038:% \include{chapters/theory/higher_genus}
 succeeded in 51ms:
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{4} % Numbers down to subsubsubsection
\setcounter{tocdepth}{4} % TOC includes subsubsubsections

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\frenchspacing

% EB Garamond with full features
\usepackage[
 cmintegrals,
 cmbraces,
 noamssymbols % This prevents conflicts
]{newtxmath}
\usepackage{ebgaramond}

% Fine-tuning for optimal appearance
\usepackage[
 activate={true,nocompatibility},










thinking
**Parsing for references**

It looks like I need to focus on including references and labels in the bibliography and main LaTeX file (`main.tex`). I'll think about parsing `main.tex` using a LaTeX parser or regex. I need to strip comments and only keep relevant labels like `\label{...}` and `\ref{...}`, while ignoring potential references in comments. Additionally, processing multiple `\ref` commands in a single line will be important. The user is asking for an audit of forward references, especially since they may appear later in the file or chapters.
thinking
**Addressing forward references**

To tackle dangling references, I need to provide a fix, which means I might need to list all forward references, both genuine and dangling. The user is asking for structured findings, and I'm unsure whether to include all forward references since genuine ones might not require action. However, they insist that each finding must come with an exact fix. This makes me consider that perhaps only the dangling references need attention, while genuine ones might be acceptable.
thinking
**Evaluating audit findings**

I'm thinking about how I should structure the audit, specifically regarding forward references. Should I only list problematic ones, like those that are dangling? The audit's focus on unfinished work raises some questions. I wonder if simply stating genuine forward references that resolve cleanly shouldn’t count as findings. But to be thorough, I could include a summary of counts for different types of references. I need to decide how to present these findings effectively.
thinking
**Assessing forward references**

I’m contemplating how to handle forward references in the audit. While some may be harmless, the mission focuses on unfinished work. The user wants me to identify all forward references and categorize them as genuine or dangling. Each forward reference could be recorded with a note saying it's a genuine cross-reference needing no fix. However, the structured output requires exact fixes. I may consider reporting only defective cases and summarizing genuine forward references for clarity.
thinking
**Balancing forward references**

I’m realizing there could be many forward references in the repo—dozens or even hundreds! I need to be thorough but also be mindful not to overwhelm the user with more than 50-70 lines. The user wants exhaustive findings, so I might need to create a longer list while focusing on the highest-signal context. It could work best to only include the actual findings, like unfinished or dangling references, while mentioning that many checked references were genuine. Including a count would also help!
thinking
**Generating data with a script**

I need to generate some data and think a Python script could help. Let's check if main.tex has chapters or connections through something like master_concordance. I might want to parse files recursively and figure out which ones count as chapters based on their order, treating later chapters as later files in the main order. It seems I should classify same-file forwards versus later-file forwards and consider if I need to inspect all forward references. I'll write a script starting from main.tex and strip comments while keeping escaped ones.
thinking
**Parsing files recursively**

I'm thinking about processing character by character. The idea is to recursively parse \input and \include commands in main.tex and any nested files. I want to build a linear order list of files as I encounter them, possibly including main.tex as the starting point. For each file, I'll extract labels and references with their line numbers. If an included file is in the same file, I should consider the global order pre- and post-include for accurate reference positioning. I’ll have to ensure that references after includes account for their content.
thinking
**Detecting references in files**

I need to figure out if a reference in an earlier file points to a label in a later included file or to something that follows an include. To do this, I think an expanded token stream will help. The approach could involve parsing files recursively into a sequence of "events" based on compilation order, starting with a file's own labels and references, then the included file's events, and finally any remaining events.

I should also resolve paths for files included from different directories and avoid infinite loops. I'll build a list of events with a global position, iterating through each file line after stripping comments and recording labels or references in order. For includes, I’ll insert events right at that point while considering lines that contain both text and the \input directive.
thinking
**Processing events around includes**

I can definitely still process events that occur before and after an include, as long as an include line only has the directive. This means I'll need to keep track of the order in which they happen to maintain accuracy. By ensuring that I separate events around the include directive, I can effectively manage how references and labels interact throughout the files. It’ll be interesting to see how everything fits together!
thinking
**Classifying chapter references**

I need to classify "later chapters" and map each file to its chapter index based on the main order. It makes sense to have some appendices after the main text. If there's a reference to a later appendix from an earlier chapter, that should point forward. For same-file references, I'll position them after the reference, and for different files, I'll label them globally. I’ll need to report the actual target file and line, especially since there could be thousands of references to manage.
codex
I have the compile spine from `main.tex` now. Next step is purely mechanical but decisive: expand the include tree in compilation order, extract every literal `\ref{}` and `\label{}`, then isolate only the refs whose targets sit later in that order or never appear at all.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from collections import defaultdict, Counter

root = Path('/Users/raeez/chiral-bar-cobar')
main = root / 'main.tex'

include_re = re.compile(r'\\\\(input|include)\\s*\\{(["'^}]+)'"\\}')
label_re = re.compile(r'\\\\label\\s*\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\ref\\s*\\{(["'^}]+)'"\\}')

# strip comments while respecting escaped %
def strip_comments(line: str) -> str:
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == '%':
            # count preceding backslashes
            bs = 0
            j = i - 1
            while j >= 0 and line[j] == '\\\\':
                bs += 1
                j -= 1
            if bs % 2 == 0:
                break
        out.append(c)
        i += 1
    return ''.join(out)

files_in_order = []
seen_stack = []
events = []
visited_cache = set()

# We keep repeated inclusions if they occur in expansion order. Avoid true recursion cycles only.
def expand(path: Path):
    path = path.resolve()
    if not path.exists():
        events.append({'kind':'missing_include','file':str(path),'line':0,'text':'MISSING'})
        return
    if path in seen_stack:
        events.append({'kind':'recursive_include','file':str(path),'line':0,'text':'RECURSIVE'})
        return
    seen_stack.append(path)
    files_in_order.append(path)
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    for lineno, raw in enumerate(lines, 1):
        line = strip_comments(raw)
        if not line.strip():
            continue
        # Find tokens in left-to-right order, splicing includes at their positions.
        matches = []
        for m in include_re.finditer(line):
            matches.append((m.start(), 'include', m))
        for m in label_re.finditer(line):
            matches.append((m.start(), 'label', m))
        for m in ref_re.finditer(line):
            matches.append((m.start(), 'ref', m))
        matches.sort(key=lambda x: x[0])
        for _, kind, m in matches:
            if kind == 'label':
                events.append({'kind':'label','name':m.group(1),'file':str(path),'line':lineno,'col':m.start()+1})
            elif kind == 'ref':
                events.append({'kind':'ref','name':m.group(1),'file':str(path),'line':lineno,'col':m.start()+1})
            else:
                inc = m.group(2)
                inc_path = Path(inc)
                candidates = []
                if inc_path.is_absolute():
                    candidates.append(inc_path)
                else:
                    candidates.append((path.parent / inc_path))
                    candidates.append(root / inc_path)
                resolved = None
                for c in candidates:
                    if c.exists():
                        resolved = c
                        break
                    if c.suffix == '':
                        if c.with_suffix('.tex').exists():
                            resolved = c.with_suffix('.tex')
                            break
                if resolved is None and inc == '../chapters/connections/thqg_concordance_supplement':
                    # Allow the odd relative fallback to root/chapters/...
                    c = root / 'chapters/connections/thqg_concordance_supplement.tex'
                    if c.exists():
                        resolved = c
                if resolved is None:
                    events.append({'kind':'missing_include','file':str(path),'line':lineno,'text':inc})
                else:
                    expand(resolved)
    seen_stack.pop()

expand(main)

# Assign global positions to labels and refs only.
pos = 0
labels = defaultdict(list)
refs = []
for ev in events:
    if ev['kind'] in {'label','ref'}:
        pos += 1
        ev['pos'] = pos
    if ev['kind'] == 'label':
        labels[ev['name']].append(ev)
    elif ev['kind'] == 'ref':
        refs.append(ev)

forward_same = []
forward_later = []
dangling = []
ambiguous = []
backward = 0
for r in refs:
    targets = labels.get(r['name'], [])
    if not targets:
        dangling.append(r)
        continue
    if len(targets) > 1:
        # Keep track if any target is after the ref.
        if any(t['pos'] > r['pos'] for t in targets):
            ambiguous.append((r, targets))
    # classify against earliest target after/before? We'll use nearest preceding if any else first following.
    after = [t for t in targets if t['pos'] > r['pos']]
    if after:
        t = after[0]
        if t['file'] == r['file']:
            forward_same.append((r,t,targets))
        else:
            forward_later.append((r,t,targets))
    else:
        backward += 1

print('files_expanded', len(files_in_order))
print('unique_files', len({str(p) for p in files_in_order}))
print('labels', sum(len(v) for v in labels.values()))
print('unique_labels', len(labels))
print('refs', len(refs))
print('backward_refs', backward)
print('forward_same', len(forward_same))
print('forward_later', len(forward_later))
print('dangling', len(dangling))
print('ambiguous_with_later_duplicate_target', len(ambiguous))
print('\\nFirst 40 dangling:')
for r in dangling[:40]:
    print(f\"{r['file']}:{r['line']} -> {r['name']}\")
print('\\nFirst 40 same-file forward:')
for r,t,targets in forward_same[:40]:
    dup = '' if len(targets)==1 else f' DUP={len(targets)}'
    print(f\"{r['file']}:{r['line']} -> {r['name']} => {t['file']}:{t['line']}{dup}\")
print('\\nFirst 40 later-file forward:')
for r,t,targets in forward_later[:40]:
    dup = '' if len(targets)==1 else f' DUP={len(targets)}'
    print(f\"{r['file']}:{r['line']} -> {r['name']} => {t['file']}:{t['line']}{dup}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 668ms:
files_expanded 94
unique_files 94
labels 11148
unique_labels 10951
refs 13420
backward_refs 9118
forward_same 1368
forward_later 2873
dangling 61
ambiguous_with_later_duplicate_target 769

First 40 dangling:
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3923 -> conv:three-hochschild
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:1523 -> def:conilpotent-chiral-coalgebra
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:3165 -> def:cyclically-admissible
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:3168 -> constr:platonic-package
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:507 -> prop:mixed-product-decomposition
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:1241 -> subsec:thqg-open-sector-factorization-category
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1722 -> prop:pixton-genus2-planted-forest
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1811 -> conj:v1-master-infinite-generator





thinking
**Inspecting dangling references**

I see that there are 61 dangling references that I need to look into. It’s likely caused by label typos or missing include files. I should gather a complete list of these dangling references and check for any ambiguous duplicates. I might need to inspect if some forward references point to later chapters that have duplicate labels, causing confusion. Although there could be around 4241 forward references, only the problematic ones matter, so I’ll focus on those. It’s essential to verify each finding against the actual contents of the files as I inspect them individually.
thinking
**Finding exact fixes for dangling references**

I need to determine the exact fix for each dangling reference, which feels like a substantial task with 61 findings. It might be manageable, but I suspect some duplicates are due to the same missing label occurring multiple times. I could group them by missing label. It’s essential to provide a severity rubric, as dangling references could be high, medium, or low based on whether the label is missing or just a typo. I’ll need to inspect if any of the dangling issues arise from labels defined in excluded files or other volumes, and ultimately generate a complete list of dangling references with context to aid in finding similar labels across the repository.
thinking
**Creating a complete list of references**

I’m looking to produce a complete list of dangling references and search suggestions. Using a script, I can print each dangling reference along with its nearby line and even search for exact missing labels across the repository. It would be useful to print similar labels by their prefix, too. Maybe a small Python script could help compute suggestions among labels. However, I have to be careful not to present guesses as facts. Actual file reading is essential for verification. I may need to inspect files around each dangling reference and search for relevant section names or similar labels. There could be potential forward references that aren't dangling but target later chapters, which the user asked to find. I could also count these and clarify they’re not issues unless they’re genuinely dangling. Additionally, some forward references might point to unintroduced labels or chapters, which might be weak but not necessarily errors.
thinking
**Analyzing forward references**

The user specifically asks about forward references and dangling ones, so it makes sense to focus on dangling forward references where the target is absent. I'm also considering the residual risk since 769 forward references hit duplicated labels, which makes resolution ambiguous. The user wants exact formats for every finding, but this might lead to an overload of information. I should look at counting and list the top duplicate-label names, but maybe focus primarily on the dangling references for clarity.
thinking
**Inspecting missing labels**

I’m thinking there could be instances where the same label is repeated multiple times in one file, possibly with two lines showing the same missing label and fix. The format usually follows `file:line`, but they might need to be separate. I should inspect all 61 missing labels to figure out the exact fix and consider that some might be false positives due to unparsed labels in commented blocks. A search for similar labels across the repo could be useful!
codex
The first full pass is in: `13,420` literal `\ref{}` calls checked, `4,241` of them are forward references, and `61` currently point to labels that never appear anywhere in the compiled Volume I tree. I’m now re-reading each dangling site and matching it against the nearest actual labels so the fixes are precise rather than speculative.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, difflib
from pathlib import Path
from collections import defaultdict

root = Path('/Users/raeez/chiral-bar-cobar')
main = root / 'main.tex'
include_re = re.compile(r'\\\\(input|include)\\s*\\{(["'^}]+)'"\\}')
label_re = re.compile(r'\\\\label\\s*\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\ref\\s*\\{(["'^}]+)'"\\}')

def strip_comments(line: str) -> str:
    out=[]
    for i,c in enumerate(line):
        if c=='%':
            bs=0;j=i-1
            while j>=0 and line[j]=='\\\\':
                bs+=1;j-=1
            if bs%2==0:
                break
        out.append(c)
    return ''.join(out)

events=[]
seen=[]

def resolve_include(path, inc):
    inc_path = Path(inc)
    candidates=[]
    if inc_path.is_absolute():
        candidates.append(inc_path)
    else:
        candidates.append(path.parent / inc_path)
        candidates.append(root / inc_path)
    for c in candidates:
        if c.exists():
            return c.resolve()
        if c.suffix=='':
            t=c.with_suffix('.tex')
            if t.exists():
                return t.resolve()
    return None

def expand(path):
    path = path.resolve()
    if path in seen:
        return
    seen.append(path)
    for lineno, raw in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        line = strip_comments(raw)
        if not line.strip():
            continue
        matches=[]
        for m in include_re.finditer(line): matches.append((m.start(),'include',m))
        for m in label_re.finditer(line): matches.append((m.start(),'label',m))
        for m in ref_re.finditer(line): matches.append((m.start(),'ref',m))
        matches.sort(key=lambda x:x[0])
        for _,kind,m in matches:
            if kind=='label': events.append({'kind':'label','name':m.group(1),'file':path,'line':lineno})
            elif kind=='ref': events.append({'kind':'ref','name':m.group(1),'file':path,'line':lineno})
            else:
                rp=resolve_include(path,m.group(2))
                if rp: expand(rp)
    seen.pop()

expand(main)
labels=defaultdict(list)
refs=[]
for i,e in enumerate(events):
    e['pos']=i
    if e['kind']=='label': labels[e['name']].append(e)
    else: refs.append(e)
all_label_names = sorted(labels)

dangling=[]
for r in refs:
    if r['name'] not in labels:
        dangling.append(r)

# search globally for each missing label exact and fuzzy prefixes
for r in dangling:
    name = r['name']
    prefix = name.split(':')[0]
    prefix_matches = [n for n in all_label_names if n.startswith(prefix+':')][:20]
    close = difflib.get_close_matches(name, all_label_names, n=6, cutoff=0.55)
    print(f\"FILE {r['file'].relative_to(root)}:{r['line']} REF {name}\")
    print('  CLOSE', '; '.join(close) if close else '-')
    print('  PREFIX', '; '.join(prefix_matches[:12]) if prefix_matches else '-')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 10.00s:
FILE chapters/frame/preface.tex:3923 REF conv:three-hochschild
  CLOSE conj:hca-hochschild; conj:lattice:e1-hochschild; warn:three-hochschild-intro; conj:symn-hochschild; comp:fermion-hochschild; thm:circle-fh-hochschild
  PREFIX conv:bar-coalgebra-identity; conv:cobar-signs; conv:coordinate-notation; conv:dg-signs; conv:dual-proof; conv:en-two-axes; conv:frontier-quadratic-gaussian-sector; conv:gamma-vs-rgamma; conv:heisenberg-kappa-notation; conv:higher-genus-differentials; conv:hms-levels; conv:holo-comp-parity-even
FILE chapters/theory/bar_construction.tex:1523 REF def:conilpotent-chiral-coalgebra
  CLOSE def:completed-chiral-algebra; def:filtered-chiral-algebra; def:einf-chiral-algebra; def:e1-chiral-algebra; def:conilpotent-cobar; def:koszul-chiral-algebra
  PREFIX def:Kbi; def:SC; def:Z2-action-symplectic; def:a-infinity-complete; def:admissible-level; def:admissible-level-dl; def:aff-flag; def:affine-hecke; def:affine-kac-moody; def:affine-pva-lambda-bracket; def:affine-strict-current-sector; def:ainf-algebra
FILE appendices/nonlinear_modular_shadows.tex:3165 REF def:cyclically-admissible
  CLOSE def:v1-cyclically-admissible; def:v1-cyclically-admissible-lca; rem:critical-admissible; prop:winfinity-not-cyclically-admissible; ex:sl2-admissible; rem:sl2-admissible
  PREFIX def:Kbi; def:SC; def:Z2-action-symplectic; def:a-infinity-complete; def:admissible-level; def:admissible-level-dl; def:aff-flag; def:affine-hecke; def:affine-kac-moody; def:affine-pva-lambda-bracket; def:affine-strict-current-sector; def:ainf-algebra
FILE appendices/nonlinear_modular_shadows.tex:3168 REF constr:platonic-package
  CLOSE constr:v1-platonic-package; subsubsec:platonic-package; constr:lattice:e1-fact-cat; constr:lattice:va; cor:lattice-packet-diagonal; constr:evaluation-map
  PREFIX constr:ainfty-jacobi; constr:ass-graded-ss; constr:bar-diff-collision; constr:bar-filtration; constr:bipartite-linfty-truncation; constr:bordered-fm; constr:branch-line-shadow-depth; constr:chevalley-cousin; constr:chiral-bracket; constr:chiral-p3-bracket; constr:cobar-jacobi; constr:combinatorial-frontier-shadow
FILE chapters/connections/thqg_open_closed_realization.tex:507 REF prop:mixed-product-decomposition
  CLOSE prop:pole-decomposition; prop:whitehead-spectral-decomposition; prop:divisor-sum-decomposition; eq:d-Hoch-decomposition; rem:ds-spectral-decomposition; prop:n2-channel-decomposition
  PREFIX prop:2d-convergence; prop:A2-lattice-bar; prop:DR-preserves-duality; prop:E8-koszul-acyclic; prop:G2-bar-dims; prop:LV-conversion-complete; prop:W-squared-qp; prop:abelian-bar-factorization; prop:abelian-locus-type-a; prop:abelianity-complementarity-independence; prop:admissibility-finite-slices-chapter; prop:admissible-levels-permuted
FILE chapters/connections/thqg_open_closed_realization.tex:1241 REF subsec:thqg-open-sector-factorization-category
  CLOSE subsec:heisenberg-open-sector-category; def:e1-factorization-category; subsec:spectral-factorization-bridge; subsec:hom-gcd-factorization; sec:thqg-open-closed-realization; subsec:shifted-factorization-comparison
  PREFIX subsec:BCG-yangians; subsec:BD-genus-zero-review; subsec:CDG-factorization; subsec:NAP-betagamma; subsec:ac-assessment; subsec:additional-hypotheses; subsec:additivity-branch; subsec:affine-cubic-from-simple-pole; subsec:affine-cubic-level-independence; subsec:affine-jacobi-kills-quartic; subsec:affine-ope-cyclic-slice; subsec:affine-primitive-kernel
FILE chapters/examples/lattice_foundations.tex:1722 REF prop:pixton-genus2-planted-forest
  CLOSE prop:shadow-genus-closed-form; prop:planted-forest-tropical; prop:km-genus2-propagator; constr:planted-forests; rem:genus4-planted-forest-decomposition; prop:genus-completed-mc-framework

thinking
**Preparing a report file**

I need to rerun something with limited output, which means I might write to a temporary file. I can use a command to generate a structured report in /tmp. That's manageable! My plan is to use Python to create this output file as /tmp/dangling_report.txt, and then once that's done, I can inspect it easily. This feels like a straightforward approach to organizing the information.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, difflib
from pathlib import Path
from collections import defaultdict

root = Path('/Users/raeez/chiral-bar-cobar')
main = root / 'main.tex'
out = Path('/tmp/dangling_report.txt')
include_re = re.compile(r'\\\\(input|include)\\s*\\{(["'^}]+)'"\\}')
label_re = re.compile(r'\\\\label\\s*\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\ref\\s*\\{(["'^}]+)'"\\}')

def strip_comments(line: str) -> str:
    out=[]
    for i,c in enumerate(line):
        if c=='%':
            bs=0;j=i-1
            while j>=0 and line[j]=='\\\\':
                bs+=1;j-=1
            if bs%2==0:
                break
        out.append(c)
    return ''.join(out)

events=[]
seen=[]

def resolve_include(path, inc):
    inc_path = Path(inc)
    candidates=[]
    if inc_path.is_absolute():
        candidates.append(inc_path)
    else:
        candidates.append(path.parent / inc_path)
        candidates.append(root / inc_path)
    for c in candidates:
        if c.exists():
            return c.resolve()
        if c.suffix=='':
            t=c.with_suffix('.tex')
            if t.exists():
                return t.resolve()
    return None

def expand(path):
    path = path.resolve()
    if path in seen:
        return
    seen.append(path)
    for lineno, raw in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        line = strip_comments(raw)
        if not line.strip():
            continue
        matches=[]
        for m in include_re.finditer(line): matches.append((m.start(),'include',m))
        for m in label_re.finditer(line): matches.append((m.start(),'label',m))
        for m in ref_re.finditer(line): matches.append((m.start(),'ref',m))
        matches.sort(key=lambda x:x[0])
        for _,kind,m in matches:
            if kind=='label': events.append({'kind':'label','name':m.group(1),'file':path,'line':lineno})
            elif kind=='ref': events.append({'kind':'ref','name':m.group(1),'file':path,'line':lineno})
            else:
                rp=resolve_include(path,m.group(2))
                if rp: expand(rp)
    seen.pop()

expand(main)
labels=defaultdict(list)
refs=[]
for i,e in enumerate(events):
    e['pos']=i
    if e['kind']=='label': labels[e['name']].append(e)
    else: refs.append(e)
all_label_names = sorted(labels)
with out.open('w', encoding='utf-8') as f:
    for r in refs:
        if r['name'] in labels:
            continue
        name = r['name']
        prefix = name.split(':')[0]
        close = difflib.get_close_matches(name, all_label_names, n=8, cutoff=0.55)
        prefix_matches = [n for n in all_label_names if n.startswith(prefix+':')][:20]
        f.write(f\"FILE {r['file'].relative_to(root)}:{r['line']} REF {name}\\n\")
        f.write('  CLOSE ' + ('; '.join(close) if close else '-') + '\\n')
        f.write('  PREFIX ' + ('; '.join(prefix_matches) if prefix_matches else '-') + '\\n')
print(out)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 9.47s:
/tmp/dangling_report.txt
exec
/bin/zsh -lc "sed -n '1,260p' /tmp/dangling_report.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
FILE chapters/frame/preface.tex:3923 REF conv:three-hochschild
  CLOSE conj:hca-hochschild; conj:lattice:e1-hochschild; warn:three-hochschild-intro; conj:symn-hochschild; comp:fermion-hochschild; thm:circle-fh-hochschild; comp:boson-hochschild; eq:thqg-bar-hochschild-id
  PREFIX conv:bar-coalgebra-identity; conv:cobar-signs; conv:coordinate-notation; conv:dg-signs; conv:dual-proof; conv:en-two-axes; conv:frontier-quadratic-gaussian-sector; conv:gamma-vs-rgamma; conv:heisenberg-kappa-notation; conv:higher-genus-differentials; conv:hms-levels; conv:holo-comp-parity-even; conv:koszul; conv:orientations-enhanced; conv:product-vs-bracket; conv:proof-architecture; conv:regime-tags; conv:scope-semistrict-W3; conv:set-notation; conv:set-ordering-arnold
FILE chapters/theory/bar_construction.tex:1523 REF def:conilpotent-chiral-coalgebra
  CLOSE def:completed-chiral-algebra; def:filtered-chiral-algebra; def:einf-chiral-algebra; def:e1-chiral-algebra; def:conilpotent-cobar; def:koszul-chiral-algebra; def:chiral-algebra; def:conilpotent-complete
  PREFIX def:Kbi; def:SC; def:Z2-action-symplectic; def:a-infinity-complete; def:admissible-level; def:admissible-level-dl; def:aff-flag; def:affine-hecke; def:affine-kac-moody; def:affine-pva-lambda-bracket; def:affine-strict-current-sector; def:ainf-algebra; def:ambient-complementarity-datum; def:ambient-complementarity-tangent-complex; def:ambient-master-equation; def:ambient-modular-complementarity-algebra; def:ambient-tangent-complex; def:analytic-bar-coalgebra; def:analytic-boundary-condition; def:analytic-genus-g-bar
FILE appendices/nonlinear_modular_shadows.tex:3165 REF def:cyclically-admissible
  CLOSE def:v1-cyclically-admissible; def:v1-cyclically-admissible-lca; rem:critical-admissible; prop:winfinity-not-cyclically-admissible; ex:sl2-admissible; rem:sl2-admissible; def:classical-ds; ex:hh-sl2-admissible
  PREFIX def:Kbi; def:SC; def:Z2-action-symplectic; def:a-infinity-complete; def:admissible-level; def:admissible-level-dl; def:aff-flag; def:affine-hecke; def:affine-kac-moody; def:affine-pva-lambda-bracket; def:affine-strict-current-sector; def:ainf-algebra; def:ambient-complementarity-datum; def:ambient-complementarity-tangent-complex; def:ambient-master-equation; def:ambient-modular-complementarity-algebra; def:ambient-tangent-complex; def:analytic-bar-coalgebra; def:analytic-boundary-condition; def:analytic-genus-g-bar
FILE appendices/nonlinear_modular_shadows.tex:3168 REF constr:platonic-package
  CLOSE constr:v1-platonic-package; subsubsec:platonic-package; constr:lattice:e1-fact-cat; constr:lattice:va; cor:lattice-packet-diagonal; constr:evaluation-map; constr:completion-mc4; def:platonic-arithmetic-package
  PREFIX constr:ainfty-jacobi; constr:ass-graded-ss; constr:bar-diff-collision; constr:bar-filtration; constr:bipartite-linfty-truncation; constr:bordered-fm; constr:branch-line-shadow-depth; constr:chevalley-cousin; constr:chiral-bracket; constr:chiral-p3-bracket; constr:cobar-jacobi; constr:combinatorial-frontier-shadow; constr:completion-mc4; constr:concrete-rh; constr:covering-space; constr:cross-channel-graph-sum; constr:deconcatenation; constr:degree4-degeneration; constr:det-bar; constr:dk-shadow-projections
FILE chapters/connections/thqg_open_closed_realization.tex:507 REF prop:mixed-product-decomposition
  CLOSE prop:pole-decomposition; prop:whitehead-spectral-decomposition; prop:divisor-sum-decomposition; eq:d-Hoch-decomposition; rem:ds-spectral-decomposition; prop:n2-channel-decomposition; prop:arith-geom-decomposition; rem:shifted-moment-decomposition
  PREFIX prop:2d-convergence; prop:A2-lattice-bar; prop:DR-preserves-duality; prop:E8-koszul-acyclic; prop:G2-bar-dims; prop:LV-conversion-complete; prop:W-squared-qp; prop:abelian-bar-factorization; prop:abelian-locus-type-a; prop:abelianity-complementarity-independence; prop:admissibility-finite-slices-chapter; prop:admissible-levels-permuted; prop:admissible-verlinde-bar; prop:affine-cs-action; prop:affine-cubic-ad-invariance; prop:affine-cyclic-slice-data; prop:affine-hecke-kd; prop:affine-jacobi-quartic-vanishing; prop:affine-primitive-kernel; prop:affine-primitive-shell
FILE chapters/connections/thqg_open_closed_realization.tex:1241 REF subsec:thqg-open-sector-factorization-category
  CLOSE subsec:heisenberg-open-sector-category; def:e1-factorization-category; subsec:spectral-factorization-bridge; subsec:hom-gcd-factorization; sec:thqg-open-closed-realization; subsec:shifted-factorization-comparison; subsec:thqg-intro-four-recovery; subsec:thqg-entanglement-dictionary
  PREFIX subsec:BCG-yangians; subsec:BD-genus-zero-review; subsec:CDG-factorization; subsec:NAP-betagamma; subsec:ac-assessment; subsec:additional-hypotheses; subsec:additivity-branch; subsec:affine-cubic-from-simple-pole; subsec:affine-cubic-level-independence; subsec:affine-jacobi-kills-quartic; subsec:affine-ope-cyclic-slice; subsec:affine-primitive-kernel; subsec:affine-sl2-boundary-sewing; subsec:affine-sl2-genus-loop; subsec:affine-tower-construction; subsec:all-coefficients-table; subsec:ambient-category; subsec:ambient-complementarity-datum; subsec:analytic-bar-koszul; subsec:analytic-completion-programme-editorial
FILE chapters/examples/lattice_foundations.tex:1722 REF prop:pixton-genus2-planted-forest
  CLOSE prop:shadow-genus-closed-form; prop:planted-forest-tropical; prop:km-genus2-propagator; constr:planted-forests; rem:genus4-planted-forest-decomposition; prop:genus-completed-mc-framework; rem:pixton-genus2-verification; prop:fp-genus-decay-for-double
exec
/bin/zsh -lc "sed -n '261,520p' /tmp/dangling_report.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc 'wc -l /tmp/dangling_report.txt' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     183 /tmp/dangling_report.txt

thinking
**Calculating missing labels**

I'm checking the entries and confirming that 183 lines equals 61 entries times 3, which seems good. Now I need more context around each candidate to confirm the fixes. I think I could script it to group by missing labels and inspect the surrounding lines to search for exact possible existing labels. There are about 48 unique missing labels that I need to compute, along with their counts. Let’s get started on that!
exec
/bin/zsh -lc "python3 - <<'PY'
from collections import Counter
from pathlib import Path
import re
report = Path('/tmp/dangling_report.txt').read_text().splitlines()
labels=[]
for line in report:
    if line.startswith('FILE '):
        labels.append(line.split(' REF ',1)[1])
for name,c in Counter(labels).most_common():
    print(c, name)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4 conj:v1-master-infinite-generator
3 princ:gravitational-primitivity
2 thm:bar-cobar-path-integral-heisenberg
2 prop:thqg-X-second-quantization
2 thm:rtt-all-types
2 thm:thqg-V-collision-twisting
2 sec:sl3-bar-table
2 rem:free-field-three-theorems
2 rem:w-algebra-three-theorems
2 thm:thqg-III-genus-1-holographic
2 thm:thqg-III-eigenspace-decomposition
2 cor:thqg-III-dimension-parity
1 conv:three-hochschild
1 def:conilpotent-chiral-coalgebra
1 def:cyclically-admissible
1 constr:platonic-package
1 prop:mixed-product-decomposition
1 subsec:thqg-open-sector-factorization-category
1 prop:pixton-genus2-planted-forest
1 thm:heisenberg-bar-complex-genus0


thinking
**Inspecting missing labels**

I need to inspect all unique missing labels by searching for exact or similar labels. Many might just be simple renames with prefixes like `v1-` or `intro-`. I should analyze the context around each site and look for exact candidate targets. Using a script could help me find occurrences with line numbers. Automating this with difflib suggestions and grep could also clarify. I might generate candidates from close matches and create a table to track missing labels and fixes for easy reference. It's essential to ensure semantic matches as I go through these.
thinking
**Analyzing unique labels**

I have 47 unique missing labels, which seems manageable. I should look into the lines around references and target definitions. Using parallel execution commands in batches could help. Since there are many, maybe I can create a script to print concise contexts around each dangling reference and the first three close label definitions. I’ll use rg for exact candidate labels. It seems wise to classify them, especially when a missing label exists with a different prefix, like `conv:three-hochschild` needing to be `conv:three-hochschilds`.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(conv:three-hochschild|def:conilpotent-chiral-coalgebra|def:v1-cyclically-admissible|constr:v1-platonic-package|prop:mixed-product-decomposition|subsec:thqg-open-sector-factorization-category|prop:pixton-genus2-planted-forest|conj:master-infinite-generator|thm:heisenberg-bar-complex-genus0|lem:thqg-X-composition-decay|prop:thqg-X-second-quantization|thm:thqg-X-heisenberg-sewing-full|rem:thqg-X-pants-independence|princ:gravitational-primitivity|prop:heisenberg-kappa|subsec:concordance-e1-primacy|sec:concordance-three-tier-r-matrix|sec:concordance-holographic-programme|rem:toroidal-three-theorems|thm:rtt-all-classical-types|thm:dnp-bar-cobar-identification|chap:casimir-divisor|conj:toroidal-e1|sec:elliptic-bar-heisenberg|thm:thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|rem:chromatic-tower-correspondence|thm:thqg-g4-s-duality|thm:thqg-g6-soft-graviton|sec:thqg-soft-graviton-theorems|thm:thqg-g3-polarization|thm:thqg-III-genus-1-holographic|thm:thqg-III-eigenspace-decomposition|cor:thqg-III-dimension-parity|subsec:thqg-III-shifted-symplectic|cor:thqg-III-complementarity-exchange|thm:thqg-g5-yangian|prop:thqg-V-c13-self-duality|sec:thqg-ten-theorems|thm:hook-type-transport-koszul-duality|subsec:dr-hierarchy-string)\\}' chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1676: \phantomsection\label{chap:casimir-divisor}% % casimir_divisor_core_transport.tex (migrated to Vol II)
main.tex:1761: \phantomsection\label{conj:master-infinite-generator}%
chapters/examples/yangians_foundations.tex:209:\label{thm:rtt-all-classical-types}
chapters/theory/en_koszul_duality.tex:6918:\label{rem:chromatic-tower-correspondence}
chapters/theory/higher_genus_modular_koszul.tex:28473:\label{def:v1-cyclically-admissible}
chapters/theory/higher_genus_modular_koszul.tex:28688:\label{constr:v1-platonic-package}
chapters/connections/concordance.tex:117:\begin{convention}[Three Hochschild theories]\label{conv:three-hochschild}
chapters/connections/concordance.tex:2837:\label{princ:gravitational-primitivity}
chapters/connections/concordance.tex:3844:\label{subsec:concordance-e1-primacy}



thinking
**Searching for missing labels**

I’m considering searching across the entire repository or volumes to find any missing labels and see if the target exists elsewhere. I think I might only need to focus on Volume I, but I wonder if I can utilize the rg tool across all three volumes. The cross-volume rule states that live surfaces include all three when dealing with shared formulas. Although it's not strictly necessary for the audit, it might still be helpful. But since the user specifically asked about this repository, I’ll keep that in mind.
thinking
**Inspecting label mapping**

I need to identify exact fixes for the missing labels by possibly automating a mapping process using regex patterns. For instance, a missing variant like `v1-` could map to its version without the prefix, while checking if older lane names like `thqg-X` might need updating. I suspect some labels may refer to not-included Volume II items, and I should inspect these thoroughly. It might help to search for unique missing labels across all volumes, but the user wants to avoid using the internet.
thinking
**Exploring label searching**

I’m considering whether we can search the local repository and sibling volumes for accessible information. It looks like reading may be limited due to sandbox restrictions that allow file access within writable roots only. I should check if sibling volumes, like `/Users/raeez/chiral-bar-cobar-vol2`, are readable despite being outside writable roots. Searching through all sibling volumes for missing labels might help clarify things, especially if some labels were migrated. Let's focus on that to find discrepancies!
codex
A pattern is emerging: several “dangling” refs are not random typos, they point to labels that exist only in retired files or migrated chapter surfaces. I’m checking those against the live compiled tree now so the fixes distinguish “rename the label” from “remove or rewrite a dead cross-volume promise.”
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
from collections import Counter
labels=[]
for line in Path('/tmp/dangling_report.txt').read_text().splitlines():
    if line.startswith('FILE '):
        labels.append(line.split(' REF ',1)[1])
for name in sorted(set(labels)):
    print(name)
PY > /tmp/dangling_labels.txt
rg -n -F -f /tmp/dangling_labels.txt /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
  File "<stdin>", line 9
    PY > /tmp/dangling_labels.txt
         ^
SyntaxError: invalid syntax

thinking
**Revising shell heredoc**

I'm thinking about how to correctly implement a separate shell heredoc in Python. It’s essential to ensure I use the right syntax, especially when redirecting output to a file. The command should be like `python > file`, but I need to double-check that the heredoc structure is correct during the process. I want to make this simple and clear so that I don't run into any issues later on. Let's figure this out!
exec
/bin/zsh -lc "python3 - <<'PY' > /tmp/dangling_labels.txt
from pathlib import Path
labels=[]
for line in Path('/tmp/dangling_report.txt').read_text().splitlines():
    if line.startswith('FILE '):
        labels.append(line.split(' REF ',1)[1])
for name in sorted(set(labels)):
    print(name)
PY
rg -n -F -f /tmp/dangling_labels.txt /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 73ms:
/Users/raeez/chiral-bar-cobar/compute/tests/test_platonic_datum.py:8:  constr:platonic-package, def:cyclically-admissible,
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_vicedo_envelope_engine.py:29:    constr:platonic-package (concordance.tex / higher_genus_modular_koszul.tex)
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_vicedo_envelope_engine.py:30:    def:cyclically-admissible (higher_genus_modular_koszul.tex)
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_vicedo_envelope_engine.py:155:    """Tests for cyclic admissibility (def:cyclically-admissible)."""
/Users/raeez/chiral-bar-cobar/compute/tests/test_platonic_red_team.py:19:  - def:cyclically-admissible in higher_genus_modular_koszul.tex
/Users/raeez/chiral-bar-cobar/compute/tests/test_nishinaka_envelope.py:20:  constr:platonic-package, def:cyclically-admissible,
/Users/raeez/chiral-bar-cobar/compute/tests/test_platonic_blue_team.py:18:  - constr:platonic-package in higher_genus_modular_koszul.tex
/Users/raeez/chiral-bar-cobar/compute/tests/test_platonic_blue_team.py:60:        """Heisenberg Lie conformal algebra satisfies def:cyclically-admissible."""
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py:3:Verifies thm:dnp-bar-cobar-identification(iii): the non-renormalization =
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py:23:  thm:dnp-bar-cobar-identification (chiral_koszul_pairs.tex)
/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bv_bar_proof.py:24:  feynman_connection.tex (thm:bar-cobar-path-integral-heisenberg).
/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_koszul_engine.py:16:  constr:platonic-package


thinking
**Analyzing missing labels**

I’ve noticed in my search that there are audits revealing some missing labels in the live Volume I source, particularly in files not included in the main compilation. Specifically, `audit/vol2...` points out that certain labels exist in a file at a particular path, but it seems that the chapter file isn't included in the main. If those labels are referenced in the compiled tree, I could fix it by adding the appropriate alias. The user wants an unfinished work audit on this volume's forward references, but since the label is absent in the compiled tree, the problem remains unresolved in the built book.
thinking
**Determining label fixes**

I need to figure out the compiled equivalent for some labels. If the uncompiled file is retired, the reference should point to alias anchors in the main file, especially for cross-chapter references. Since this is an audit and not an implementation step, I can propose adding an alias anchor to keep the reference intact. The user asked for a fix, which might mean reintroducing a `\phantomsection\label{...}` at a new location. I should inspect the alias block around line 1676 in `main.tex` to see if there are missing labels, and I'll consider fixing multiple labels this way. I'll read that section closely.
exec
/bin/zsh -lc "sed -n '1640,1775p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \phantomsection\label{rem:sl2-vs-vir-complementarity}% % genus_expansions.tex
 \phantomsection\label{rem:yangian-ordered-boundary-face}% % dg_shifted_factorization_bridge.tex
 \phantomsection\label{conj:non-simply-laced-discriminant}% % genus_expansions.tex
 \phantomsection\label{conj:type-a-transport-to-transpose}% % subregular_hook_frontier.tex
 \phantomsection\label{constr:thqg-V-binary-extraction}% % thqg_gravitational_yangian.tex
 \phantomsection\label{app:nilpotent-completion}% % nilpotent_completion.tex
 \phantomsection\label{app:coderived}% % coderived_models.tex
 \phantomsection\label{sec:mc4-splitting}% % nilpotent_completion.tex
 \phantomsection\label{chap:concordance}% % concordance.tex (not in guide_to_main_results.tex)
 % --- Frontier / open-closed realization labels (2026-03-30 audit) ---
 \phantomsection\label{chap:holographic-codes-koszul}% % holographic_codes_koszul.tex
 \phantomsection\label{rem:convergence-vs-string}% % genus_expansions.tex
 % twisted_holography_quantum_gravity.tex phantom labels
 % (file commented out; labels referenced by thqg_open_closed_realization)
 \phantomsection\label{def:thqg-holographic-datum}%
 \phantomsection\label{def:thqg-standing-hypotheses}%
 \phantomsection\label{def:thqg-shadow-archetype}%
 \phantomsection\label{rem:pixton-genus2-computation}% % concordance.tex
 \phantomsection\label{rem:pixton-conjecture-status}% % concordance.tex
 \phantomsection\label{subsec:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
exec
/bin/zsh -lc "rg -n '\\\\label\\{princ:guide-gravitational-primitivity\\}|\\\\label\\{princ:gravitational-primitivity\\}|Three Hochschild|thqg-X-composition-decay|thqg-X-second-quantization|thqg-X-heisenberg-sewing-full|thqg-V-collision-twisting|thqg-III-eigenspace-decomposition|thqg-III-genus-1-holographic|thqg-III-dimension-parity|thqg-III-complementarity-exchange|thqg-g5-yangian|bar-cobar-path-integral-heisenberg|mixed-product-decomposition|prop:pixton-genus2-planted-forest|sec:sl3-bar-table|heisenberg-kappa|concordance-e1-primacy|concordance-three-tier-r-matrix|concordance-holographic-programme|rtt-all-classical-types|dnp-bar-cobar-identification|hook-type-transport-koszul-duality|dr-hierarchy-string' chapters main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(conv:three-hochschild|def:v1-cyclically-admissible|constr:v1-platonic-package|conj:toroidal-e1|rem:toroidal-three-theorems|sec:elliptic-bar-heisenberg|chap:casimir-divisor|conj:master-infinite-generator)\\}' chapters appendices main.tex /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/lattice_foundations.tex:1722:(Proposition~\ref{prop:pixton-genus2-planted-forest})
chapters/examples/y_algebras.tex:340: \textup{(}Proposition~\textup{\ref{prop:heisenberg-kappa}}\textup{)}.
chapters/examples/y_algebras.tex:631:(averaging map, \S\ref{subsec:concordance-e1-primacy}) gives
chapters/examples/y_algebras.tex:641:(\S\ref{sec:concordance-three-tier-r-matrix}): it is
chapters/examples/y_algebras.tex:857:(\S\ref{sec:concordance-holographic-programme}), the junction
chapters/examples/yangians_drinfeld_kohno.tex:8055: \textup{(}Theorem~\textup{\ref{thm:thqg-V-collision-twisting}}\textup{)}.
chapters/examples/yangians_drinfeld_kohno.tex:8098:Part~(i) is Theorem~\ref{thm:thqg-V-collision-twisting}:
chapters/examples/free_fields.tex:5099: \textup{(}Theorem~\textup{\ref{thm:bar-cobar-path-integral-heisenberg})}.
chapters/examples/free_fields.tex:5110:Theorem~\ref{thm:bar-cobar-path-integral-heisenberg} by
chapters/connections/thqg_open_closed_realization.tex:507:(Volume~II, Proposition~\ref{prop:mixed-product-decomposition} in the
chapters/connections/feynman_connection.tex:13:Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
chapters/connections/feynman_connection.tex:137:\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
chapters/connections/feynman_connection.tex:188:\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
chapters/connections/feynman_connection.tex:204:Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
chapters/examples/heisenberg_eisenstein.tex:1086:\begin{equation}\label{eq:heisenberg-kappa-formula}
chapters/examples/heisenberg_eisenstein.tex:2190:(Lemma~\ref{lem:thqg-X-composition-decay}). In particular,
chapters/examples/heisenberg_eisenstein.tex:2197:Proposition~\ref{prop:thqg-X-second-quantization}, $\secquant(T)$ is
chapters/examples/heisenberg_eisenstein.tex:2412:determinant (Proposition~\ref{prop:thqg-X-second-quantization}).
chapters/examples/heisenberg_eisenstein.tex:2414:(\eqref{eq:thqg-X-polyakov}, Theorem~\ref{thm:thqg-X-heisenberg-sewing-full}(IV)),
chapters/examples/yangians_foundations.tex:209:\label{thm:rtt-all-classical-types}
 succeeded in 52ms:
main.tex:1676: \phantomsection\label{chap:casimir-divisor}% % casimir_divisor_core_transport.tex (migrated to Vol II)
main.tex:1761: \phantomsection\label{conj:master-infinite-generator}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:9:\phantomsection\label{conj:master-infinite-generator}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:209:\begin{conjecture}[Elliptic-curve toroidal realization; \ClaimStatusConjectured]\label{conj:toroidal-e1}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:395:\label{rem:toroidal-three-theorems}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:783:\label{sec:elliptic-bar-heisenberg}
chapters/connections/concordance.tex:117:\begin{convention}[Three Hochschild theories]\label{conv:three-hochschild}
chapters/theory/higher_genus_modular_koszul.tex:28473:\label{def:v1-cyclically-admissible}
chapters/theory/higher_genus_modular_koszul.tex:28688:\label{constr:v1-platonic-package}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/casimir_divisor_core_transport.tex:7:\label{chap:casimir-divisor}
exec
/bin/zsh -lc "rg -n '\\\\label\\{(lem:thqg-X-composition-decay|prop:thqg-X-second-quantization|thm:thqg-X-heisenberg-sewing-full|rem:thqg-X-pants-independence|prop:mixed-product-decomposition|subsec:thqg-open-sector-factorization-category|thm:thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|thm:thqg-III-genus-1-holographic|thm:thqg-III-eigenspace-decomposition|cor:thqg-III-dimension-parity|subsec:thqg-III-shifted-symplectic|cor:thqg-III-complementarity-exchange|thm:thqg-V-collision-twisting|thm:thqg-g5-yangian|prop:thqg-V-c13-self-duality|thm:thqg-g4-s-duality|thm:thqg-g6-soft-graviton|sec:thqg-soft-graviton-theorems|thm:thqg-g3-polarization)\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R11_thqg_symplectic_polarization.md:294:\label{cor:thqg-III-dimension-parity}
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R11_thqg_symplectic_polarization.md:430:474:\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P04_thm_C1_genus0_upgrade.md:576:\label{cor:thqg-III-dimension-parity}
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P04_thm_C1_genus0_upgrade.md:906:   694	\label{cor:thqg-III-dimension-parity}
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P04_thm_C1_genus0_upgrade.md:996:rectification_20260412_233715/R11_thqg_symplectic_polarization.md:430:474:\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R11_thqg_symplectic_polarization.md:441:   834	\label{subsec:thqg-III-shifted-symplectic}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R11_thqg_symplectic_polarization.md:993:   500	\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F17_dangling_refs_v1.md:37:- [MEDIUM] chapters/connections/thqg_open_closed_realization.tex:1239 — PROBLEM: `\ref{subsec:thqg-open-sector-factorization-category}` has no target; the subsection header only has `\label{subsec:thqg-ct2-cooperad-conjecture}`. FIX: add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header at line 1214.
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F17_dangling_refs_v1.md:482:/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:1048:\label{prop:mixed-product-decomposition}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F17_dangling_refs_v1.md:953:\label{prop:mixed-product-decomposition}
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F17_dangling_refs_v1.md:1581:I think the simplest way to handle this audit output format is to follow the "file:line" structure, mentioning the specific issue and fix. For example, I can say to add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header without changing the existing reference. I also wonder if we should mention the same unresolved issue at line 1239. Additionally, I need to inspect theorem 17 `thm:bar-cobar-path-integral-heisenberg` around line 5050 to determine if it needs a label too.
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F17_dangling_refs_v1.md:2103:- [MEDIUM] chapters/connections/thqg_open_closed_realization.tex:1239 — PROBLEM: `\ref{subsec:thqg-open-sector-factorization-category}` has no target; the subsection header only has `\label{subsec:thqg-ct2-cooperad-conjecture}`. FIX: add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header at line 1214.
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/D05_rmatrix_level.md:679:\label{thm:thqg-V-collision-twisting}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC04_c_13.md:635:\label{prop:thqg-V-c13-self-duality}
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H17_remove_perfectness_C1.md:428:\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:734:   474	\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:17741:\label{thm:thqg-g3-polarization}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:17751:\label{thm:thqg-g4-s-duality}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:17766:\label{thm:thqg-g5-yangian}
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:17780:\label{thm:thqg-g6-soft-graviton}




thinking
**Inspecting chapter references**

It seems there are some missing labels in the chapters, specifically in the `thqg_symplectic_polarization.tex` file, which hasn't been included in the main document. I need to verify whether this file exists and hasn't been compiled. To resolve the user's issue about unfinished forward references, I could either restore alias anchors in the main file or include the chapter. 

I’m considering a minimal fix, like adding `\phantomsection\label{...}` in `main.tex` near existing labels or changing references to any existing compiled labels. I want to find the best option since there are old orphaned chapters too.
thinking
**Examining missing labels**

I need to ensure the actual file has the correct labels, possibly by reading the relevant lines. There might be a pre-existing audit file called `relaunch...F17_dangling_refs_v1.md`, which specifically addresses dangling references. The user is requesting the current audit, so I could use that as helpful evidence. However, grounding rules indicate that I should rely on the actual file contents over audit notes, which should be used only for guidance. 

To investigate, I could use a shell script to print 5-10 lines around each reference for the 47 unique labels. This way, I can group them effectively.
thinking
**Generating contexts for missing labels**

I need to create concise contexts for all the unique missing labels by referencing their file lines along with surrounding text. I can search for exact target candidates in the repository using `rg -n` to identify them. Some missing labels are in non-compiled files, while others might not exist at all, so I’ll need to group them effectively. 

It seems like writing a script to produce a JSON format could make this easier. I can incorporate known matches from the repo outside of the compiled tree and scan for close matches in the compiled tree. Additionally, I should leverage the existing audit note `relaunch_20260413_111534/F17_dangling_refs_v1.md`, as it may cover a similar task.
thinking
**Auditing and verifying labels**

I need to ensure we’re not just copying information blindly, but instead using it to double-check and save time. It's crucial to verify findings against the actual file contents. The user asked for a new audit, so maybe we can leverage our own script and source instead. I’ll focus on producing exact reference lines and label matches throughout the repo or volumes. I’ll summarize grouped by missing labels, including relevant reference sites and close candidate labels.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, subprocess, json
from pathlib import Path
from collections import defaultdict
root = Path('/Users/raeez/chiral-bar-cobar')
main = root/'main.tex'
report = Path('/tmp/dangling_report.txt').read_text().splitlines()
entries=[]
for line in report:
    if line.startswith('FILE '):
        left, name = line[5:].split(' REF ',1)
        file, ln = left.rsplit(':',1)
        entries.append((name, Path(file), int(ln)))
by=defaultdict(list)
for name,f,l in entries:
    by[name].append((f,l))

def get_line(path, ln):
    lines = path.read_text(encoding='utf-8').splitlines()
    return lines[ln-1].strip() if 1 <= ln <= len(lines) else ''
for name, sites in sorted(by.items()):
    print('LABEL', name)
    for f,l in sites:
        print(' REF', f.relative_to(root), l, get_line(f,l))
    # exact search across volumes excluding generated/audit dirs? use rg on tex/main only in main repos
    cmd = [\"rg\",\"-n\",rf\"\\\\label\\{{{re.escape(name)}\\}}\",\"/Users/raeez/chiral-bar-cobar\",\"/Users/raeez/chiral-bar-cobar-vol2\",\"/Users/raeez/calabi-yau-quantum-groups\",\"-g\",\"*.tex\",\"-g\",\"main.tex\"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = [line for line in res.stdout.splitlines() if '/.git/' not in line]
    for line in out[:10]:
        print(' HIT', line)
    print()
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
LABEL conj:toroidal-e1
Traceback (most recent call last):
  File "<stdin>", line 23, in <module>
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/pathlib/__init__.py", line 490, in relative_to
    raise ValueError(f"{str(self)!r} is not in the subpath of {str(other)!r}")
ValueError: 'chapters/examples/landscape_census.tex' is not in the subpath of '/Users/raeez/chiral-bar-cobar'
exec
/bin/zsh -lc "python3 - <<'PY'
import re, subprocess
from pathlib import Path
from collections import defaultdict
root = Path('/Users/raeez/chiral-bar-cobar').resolve()
report = Path('/tmp/dangling_report.txt').read_text().splitlines()
entries=[]
for line in report:
    if line.startswith('FILE '):
        left, name = line[5:].split(' REF ',1)
        file, ln = left.rsplit(':',1)
        entries.append((name, (root/file).resolve() if not file.startswith('/') else Path(file).resolve(), int(ln)))
by=defaultdict(list)
for name,f,l in entries:
    by[name].append((f,l))

def get_line(path, ln):
    lines = path.read_text(encoding='utf-8').splitlines()
    return lines[ln-1].strip() if 1 <= ln <= len(lines) else ''
for name, sites in sorted(by.items()):
    print('LABEL', name)
    for f,l in sites:
        rel = f.relative_to(root) if str(f).startswith(str(root)) else f
        print(' REF', rel, l, get_line(f,l))
    cmd = [\"rg\",\"-n\",rf\"\\\\label\\{{{re.escape(name)}\\}}\",\"/Users/raeez/chiral-bar-cobar\",\"/Users/raeez/chiral-bar-cobar-vol2\",\"/Users/raeez/calabi-yau-quantum-groups\",\"-g\",\"*.tex\",\"-g\",\"main.tex\"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = [line for line in res.stdout.splitlines() if '/.git/' not in line]
    for line in out[:10]:
        print(' HIT', line)
    print()
PY > /tmp/dangling_grouped.txt
wc -l /tmp/dangling_grouped.txt
sed -n '1,260p' /tmp/dangling_grouped.txt" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
  File "<stdin>", line 30
    PY > /tmp/dangling_grouped.txt
         ^
SyntaxError: invalid syntax
exec
/bin/zsh -lc "python3 - <<'PY' > /tmp/dangling_grouped.txt
import re, subprocess
from pathlib import Path
from collections import defaultdict
root = Path('/Users/raeez/chiral-bar-cobar').resolve()
report = Path('/tmp/dangling_report.txt').read_text().splitlines()
entries=[]
for line in report:
    if line.startswith('FILE '):
        left, name = line[5:].split(' REF ',1)
        file, ln = left.rsplit(':',1)
        path = Path(file)
        if not path.is_absolute():
            path = (root / path).resolve()
        else:
            path = path.resolve()
        entries.append((name, path, int(ln)))
by=defaultdict(list)
for name,f,l in entries:
    by[name].append((f,l))

def get_line(path, ln):
    lines = path.read_text(encoding='utf-8').splitlines()
    return lines[ln-1].strip() if 1 <= ln <= len(lines) else ''
for name, sites in sorted(by.items()):
    print('LABEL', name)
    for f,l in sites:
        rel = f.relative_to(root) if str(f).startswith(str(root)) else f
        print(' REF', rel, l, get_line(f,l))
    cmd = [\"rg\",\"-n\",rf\"\\\\label\\{{{re.escape(name)}\\}}\",\"/Users/raeez/chiral-bar-cobar\",\"/Users/raeez/chiral-bar-cobar-vol2\",\"/Users/raeez/calabi-yau-quantum-groups\",\"-g\",\"*.tex\",\"-g\",\"main.tex\"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = [line for line in res.stdout.splitlines() if '/.git/' not in line]
    for line in out[:10]:
        print(' HIT', line)
    print()
PY
wc -l /tmp/dangling_grouped.txt
sed -n '1,260p' /tmp/dangling_grouped.txt" in /Users/raeez/chiral-bar-cobar succeeded in 508ms:
     166 /tmp/dangling_grouped.txt
LABEL conj:toroidal-e1
 REF chapters/examples/landscape_census.tex 4039 (Conjecture~\ref{conj:toroidal-e1}),
 HIT /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:209:\begin{conjecture}[Elliptic-curve toroidal realization; \ClaimStatusConjectured]\label{conj:toroidal-e1}

LABEL conj:v1-master-infinite-generator
 REF chapters/examples/free_fields.tex 1811 Conjecture~\ref{conj:v1-master-infinite-generator}, not to the standard
 REF chapters/examples/free_fields.tex 2687 Conjecture~\ref{conj:v1-master-infinite-generator}.
 REF chapters/examples/yangians_drinfeld_kohno.tex 58 (Conjecture~\ref{conj:v1-master-infinite-generator})
 REF chapters/examples/yangians_drinfeld_kohno.tex 4936 (Conjecture~\ref{conj:v1-master-infinite-generator})
 HIT /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:317:\label{conj:v1-master-infinite-generator}

LABEL constr:platonic-package
 REF appendices/nonlinear_modular_shadows.tex 3168 (Construction~\ref{constr:platonic-package}), in which all
 HIT /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:10:\phantomsection\label{constr:platonic-package}%

LABEL conv:three-hochschild
 REF chapters/frame/preface.tex 3923 Convention~\ref{conv:three-hochschild}).
 HIT /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:117:\begin{convention}[Three Hochschild theories]\label{conv:three-hochschild}


thinking
**Validating labels and files**

I'm looking at the grouped file and need to determine target actual hits, possibly only in repo/vol2. I should search for labels that might be absent across volumes since some have no hits. It's possible they exist in noncompiled files within the repo. If there's no hit, the label might truly be absent. 

I should inspect specific surrounding lines and check files near labels for verification. There's also the F17_dangling_refs_v1.md audit that lists fixes. I'll look at the first 120 lines since that might save time.
exec
/bin/zsh -lc "rg -n '\\[.*\\] .*conv:three-hochschild|def:conilpotent-chiral-coalgebra|def:cyclically-admissible|constr:platonic-package|prop:mixed-product-decomposition|subsec:thqg-open-sector-factorization-category|prop:pixton-genus2-planted-forest|conj:v1-master-infinite-generator|thm:bar-cobar-path-integral-heisenberg|thm:heisenberg-bar-complex-genus0|lem:thqg-X-composition-decay|prop:thqg-X-second-quantization|thm:thqg-X-heisenberg-sewing-full|rem:thqg-X-pants-independence|princ:gravitational-primitivity|prop:heisenberg-kappa|subsec:concordance-e1-primacy|sec:concordance-three-tier-r-matrix|sec:concordance-holographic-programme|rem:toroidal-three-theorems|thm:rtt-all-types|thm:dnp-bar-cobar-identification|v1-chap:casimir-divisor|conj:toroidal-e1|sec:elliptic-bar-heisenberg|thm:thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|rem:chromatic-shadow-correspondence|thm:thqg-g4-s-duality|thm:thqg-g6-soft-graviton|sec:thqg-soft-graviton-theorems|thm:thqg-g3-polarization|thm:thqg-III-genus-1-holographic|thm:thqg-III-eigenspace-decomposition|cor:thqg-III-dimension-parity|subsec:thqg-III-shifted-symplectic|cor:thqg-III-complementarity-exchange|thm:thqg-g5-yangian|prop:thqg-V-c13-self-duality|sec:thqg-ten-theorems|thm:hook-type-transport-koszul-duality|subsec:dr-hierarchy-string' relaunch_20260413_111534/F17_dangling_refs_v1.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3:- [CRITICAL] chapters/connections/outlook.tex:276 — PROBLEM: `\ref{thm:hook-type-transport-koszul-duality}` has no target, and the live local theorem is only the conditional `\label{thm:hook-transport-corridor}`. FIX: replace `Theorem~\ref{thm:hook-type-transport-koszul-duality}` with `Theorem~\ref{thm:hook-transport-corridor}` and rewrite `is the proved corridor` to `is the conditional corridor under DS--bar compatibility`.
7:- [HIGH] chapters/connections/thqg_open_closed_realization.tex:507 — PROBLEM: `\ref{prop:mixed-product-decomposition}` points only to a Volume II proposition, so the local build has no target. FIX: replace `Proposition~\ref{prop:mixed-product-decomposition}` with `the Volume II proposition "Product decomposition of mixed operations"`.
9:- [HIGH] chapters/examples/free_fields.tex:5074 — PROBLEM: `\ref{thm:bar-cobar-path-integral-heisenberg}` has no target anywhere, so the theorem statement cites nonexistent support for item (iii). FIX: replace the parenthetical with `by direct Gaussian evaluation in the Heisenberg case`.
10:- [HIGH] chapters/examples/free_fields.tex:5085 — PROBLEM: the proof again cites nonexistent `thm:bar-cobar-path-integral-heisenberg`. FIX: replace `Theorem~\ref{thm:bar-cobar-path-integral-heisenberg}` with `a direct Gaussian computation in the Heisenberg case`.
11:- [HIGH] chapters/examples/yangians_foundations.tex:1347 — PROBLEM: `\ref{thm:dnp-bar-cobar-identification}` points only to Volume II/III, so the local theorem citation is unresolved. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package"`.
12:- [HIGH] chapters/theory/chiral_koszul_pairs.tex:2472 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}` in a load-bearing classification sentence. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
13:- [HIGH] chapters/theory/three_invariants.tex:257 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}`. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
19:- [MEDIUM] chapters/examples/y_algebras.tex:340 — PROBLEM: `\ref{prop:heisenberg-kappa}` has no target; the explicit Heisenberg formula is already proved in `thm:genus-universality` part (i). FIX: replace `Proposition~\ref{prop:heisenberg-kappa}` with `Theorem~\ref{thm:genus-universality}(i)`.
20:- [MEDIUM] chapters/examples/lattice_foundations.tex:1714 — PROBLEM: `\ref{prop:pixton-genus2-planted-forest}` has no target; the exact formula cited is the displayed equation `\label{eq:planted-forest-genus2-explicit-bridge}`. FIX: replace `Proposition~\ref{prop:pixton-genus2-planted-forest}` with `equation~\eqref{eq:planted-forest-genus2-explicit-bridge}`.
29:- [MEDIUM] chapters/examples/y_algebras.tex:855 — PROBLEM: `\ref{sec:concordance-holographic-programme}` has no target; the live concordance subsection is `\label{subsec:concordance-holographic-completion}`. FIX: replace it with `\S\ref{subsec:concordance-holographic-completion}`.
30:- [MEDIUM] chapters/examples/y_algebras.tex:640 — PROBLEM: `\ref{sec:concordance-three-tier-r-matrix}` has no target; the classification is given by `\label{def:three-tier-r-matrix}`. FIX: replace `\S\ref{sec:concordance-three-tier-r-matrix}` with `Definition~\ref{def:three-tier-r-matrix}`.
36:- [MEDIUM] chapters/connections/outlook.tex:605 — PROBLEM: `\ref{subsec:dr-hierarchy-string}` has no target anywhere in the repo tree. FIX: replace `Section~\ref{subsec:dr-hierarchy-string}` with `Buryak's DR-hierarchy string-equation argument`.
37:- [MEDIUM] chapters/connections/thqg_open_closed_realization.tex:1239 — PROBLEM: `\ref{subsec:thqg-open-sector-factorization-category}` has no target; the subsection header only has `\label{subsec:thqg-ct2-cooperad-conjecture}`. FIX: add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header at line 1214.
38:- [MEDIUM] chapters/examples/heisenberg_eisenstein.tex:306 — PROBLEM: `\ref{thm:heisenberg-bar-complex-genus0}` has no target; the live theorem is `\label{thm:heisenberg-bar}`. FIX: replace it with `Theorem~\ref{thm:heisenberg-bar}`.
39:- [MEDIUM] chapters/examples/yangians_computations.tex:1150 — PROBLEM: `\ref{thm:rtt-all-types}` has no target; the live theorem is `\label{thm:rtt-all-classical-types}`. FIX: replace it with `Theorem~\ref{thm:rtt-all-classical-types}`.
40:- [MEDIUM] chapters/examples/yangians_foundations.tex:1228 — PROBLEM: same stale `\ref{thm:rtt-all-types}`. FIX: replace it with `Theorem~\ref{thm:rtt-all-classical-types}(iv)`.
393:prop:heisenberg-kappa
394:prop:mixed-product-decomposition
395:prop:pixton-genus2-planted-forest
402:sec:concordance-holographic-programme
exec
/bin/zsh -lc "rg -n '\\[.*\\].*(thqg-III-genus-1-holographic|thqg-III-eigenspace-decomposition|thqg-III-dimension-parity|thqg-III-shifted-symplectic|thqg-III-complementarity-exchange|thqg-g5-yangian|thqg-V-c13-self-duality|thqg-g4-s-duality|thqg-g6-soft-graviton|thqg-soft-graviton-theorems|thqg-g3-polarization|thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|thqg-X-composition-decay|thqg-X-second-quantization|thqg-X-heisenberg-sewing-full|thqg-X-pants-independence|rem:free-field-three-theorems|rem:w-algebra-three-theorems|v1-chap:casimir-divisor|conj:toroidal-e1|sec:elliptic-bar-heisenberg|rem:toroidal-three-theorems|conv:three-hochschild|def:conilpotent-chiral-coalgebra|def:cyclically-admissible|constr:platonic-package|princ:gravitational-primitivity|sec:sl3-bar-table)'.* relaunch_20260413_111534/F17_dangling_refs_v1.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: no matches found: \[.*\].*(thqg-III-genus-1-holographic|thqg-III-eigenspace-decomposition|thqg-III-dimension-parity|thqg-III-shifted-symplectic|thqg-III-complementarity-exchange|thqg-g5-yangian|thqg-V-c13-self-duality|thqg-g4-s-duality|thqg-g6-soft-graviton|thqg-soft-graviton-theorems|thqg-g3-polarization|thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|thqg-X-composition-decay|thqg-X-second-quantization|thqg-X-heisenberg-sewing-full|thqg-X-pants-independence|rem:free-field-three-theorems|rem:w-algebra-three-theorems|v1-chap:casimir-divisor|conj:toroidal-e1|sec:elliptic-bar-heisenberg|rem:toroidal-three-theorems|conv:three-hochschild|def:conilpotent-chiral-coalgebra|def:cyclically-admissible|constr:platonic-package|princ:gravitational-primitivity|sec:sl3-bar-table).*
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text = Path('relaunch_20260413_111534/F17_dangling_refs_v1.md').read_text()
labels = [
'conv:three-hochschild','def:conilpotent-chiral-coalgebra','def:cyclically-admissible','constr:platonic-package','princ:gravitational-primitivity','sec:sl3-bar-table','thqg-III-genus-1-holographic','thqg-III-eigenspace-decomposition','thqg-III-dimension-parity','thqg-III-shifted-symplectic','thqg-III-complementarity-exchange','thqg-g5-yangian','thqg-V-c13-self-duality','thqg-g4-s-duality','thqg-g6-soft-graviton','sec:thqg-soft-graviton-theorems','thqg-g3-polarization','thqg-I-determinant-formula','cor:thqg-I-heisenberg-selberg','thqg-X-composition-decay','thqg-X-second-quantization','thqg-X-heisenberg-sewing-full','thqg-X-pants-independence','rem:free-field-three-theorems','rem:w-algebra-three-theorems','v1-chap:casimir-divisor','conj:toroidal-e1','sec:elliptic-bar-heisenberg','rem:toroidal-three-theorems']
for label in labels:
    print('===', label, '===')
    for i,line in enumerate(text.splitlines(),1):
        if label in line and line.strip().startswith('- ['):
            print(f'{i}:{line}')
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== conv:three-hochschild ===

=== def:conilpotent-chiral-coalgebra ===

=== def:cyclically-admissible ===

=== constr:platonic-package ===

=== princ:gravitational-primitivity ===

=== sec:sl3-bar-table ===
34:- [MEDIUM] chapters/examples/bar_complex_tables.tex:4153 — PROBLEM: `\ref{sec:sl3-bar-table}` has no target; the stated `1,8,36,204,1352,9892,\ldots` sequence is actually recorded in `\label{rem:sl3-koszul-dual}`. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
35:- [MEDIUM] chapters/examples/bar_complex_tables.tex:4198 — PROBLEM: same broken `\ref{sec:sl3-bar-table}` in the table caption. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
2100:- [MEDIUM] chapters/examples/bar_complex_tables.tex:4153 — PROBLEM: `\ref{sec:sl3-bar-table}` has no target; the stated `1,8,36,204,1352,9892,\ldots` sequence is actually recorded in `\label{rem:sl3-koszul-dual}`. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
2101:- [MEDIUM] chapters/examples/bar_complex_tables.tex:4198 — PROBLEM: same broken `\ref{sec:sl3-bar-table}` in the table caption. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.

=== thqg-III-genus-1-holographic ===

=== thqg-III-eigenspace-decomposition ===


thinking
**Inspecting F17 findings**

I'm noticing that F17 isn't showing everything, possibly due to line offsets or omitted labels. So, I think I should check the relevant line numbers within F17 to gather all my findings, especially from the top 1-60 lines. I'll open up the beginning of the file to see what I can find there. It seems like a methodical way to understand what's going on!
exec
/bin/zsh -lc "sed -n '1,120p' relaunch_20260413_111534/F17_dangling_refs_v1.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# F17_dangling_refs_v1 (966s)

- [CRITICAL] chapters/connections/outlook.tex:276 — PROBLEM: `\ref{thm:hook-type-transport-koszul-duality}` has no target, and the live local theorem is only the conditional `\label{thm:hook-transport-corridor}`. FIX: replace `Theorem~\ref{thm:hook-type-transport-koszul-duality}` with `Theorem~\ref{thm:hook-transport-corridor}` and rewrite `is the proved corridor` to `is the conditional corridor under DS--bar compatibility`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:5974 — PROBLEM: `\ref{part:gravity}` points into Volume II; this repo has no cross-volume `xr` bridge, so the Part reference cannot resolve here. FIX: replace `Part~\ref{part:gravity}` with `Part "Three-Dimensional Quantum Gravity" of Volume II`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:7549 — PROBLEM: `\ref{part:e1-core}` points into Volume II and cannot resolve in this build. FIX: replace `Part~\ref{part:e1-core}` with `Part "The $E_1$ Core" of Volume II`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:7752 — PROBLEM: same broken cross-volume `\ref{part:e1-core}` as above. FIX: replace `Part~\ref{part:e1-core}` with `Part "The $E_1$ Core" of Volume II`.
- [HIGH] chapters/connections/thqg_open_closed_realization.tex:507 — PROBLEM: `\ref{prop:mixed-product-decomposition}` points only to a Volume II proposition, so the local build has no target. FIX: replace `Proposition~\ref{prop:mixed-product-decomposition}` with `the Volume II proposition "Product decomposition of mixed operations"`.
- [HIGH] chapters/connections/thqg_gravitational_s_duality.tex:559 — PROBLEM: `\ref{subsec:gravity-ainf}` points only to a Volume II subsection. FIX: replace `\S\ref{subsec:gravity-ainf}` with `the Volume II subsection "Movement I: the $\Ainf$ structure from the quartic pole"`.
- [HIGH] chapters/examples/free_fields.tex:5074 — PROBLEM: `\ref{thm:bar-cobar-path-integral-heisenberg}` has no target anywhere, so the theorem statement cites nonexistent support for item (iii). FIX: replace the parenthetical with `by direct Gaussian evaluation in the Heisenberg case`.
- [HIGH] chapters/examples/free_fields.tex:5085 — PROBLEM: the proof again cites nonexistent `thm:bar-cobar-path-integral-heisenberg`. FIX: replace `Theorem~\ref{thm:bar-cobar-path-integral-heisenberg}` with `a direct Gaussian computation in the Heisenberg case`.
- [HIGH] chapters/examples/yangians_foundations.tex:1347 — PROBLEM: `\ref{thm:dnp-bar-cobar-identification}` points only to Volume II/III, so the local theorem citation is unresolved. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package"`.
- [HIGH] chapters/theory/chiral_koszul_pairs.tex:2472 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}` in a load-bearing classification sentence. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
- [HIGH] chapters/theory/three_invariants.tex:257 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}`. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
- [HIGH] chapters/connections/twisted_holography_quantum_gravity.tex:183 — PROBLEM: `\ref{thm:lines_as_modules}` points only to Volume II, so the local proof chain breaks. FIX: replace it with `the Volume II theorem "Lines as Modules for the Open-Colour Dual"`.
- [HIGH] chapters/connections/thqg_gravitational_yangian.tex:2025 — PROBLEM: same broken external `\ref{thm:lines_as_modules}` in live prose. FIX: replace it with `the Volume II theorem "Lines as Modules for the Open-Colour Dual"`.
- [HIGH] chapters/connections/thqg_gravitational_yangian.tex:2253 — PROBLEM: same broken external `\ref{thm:lines_as_modules}` in a status table. FIX: replace `Proved (Thm~\ref{thm:lines_as_modules})` with `Proved in Volume II ("Lines as Modules for the Open-Colour Dual")`.
- [MEDIUM] chapters/theory/derived_langlands.tex:1515 — PROBLEM: `\ref{chap:modular-koszul}` has no target; the cited shadow-connection theorem lives in the shadow-metric section. FIX: replace `Chapter~\ref{chap:modular-koszul}` with `Section~\ref{sec:shadow-metric}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:27063 — PROBLEM: `\ref{def:glcm-classification}` has no target; the live definition is `\label{def:shadow-depth-classification}`. FIX: replace `Definition~\ref{def:glcm-classification}` with `Definition~\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/examples/y_algebras.tex:340 — PROBLEM: `\ref{prop:heisenberg-kappa}` has no target; the explicit Heisenberg formula is already proved in `thm:genus-universality` part (i). FIX: replace `Proposition~\ref{prop:heisenberg-kappa}` with `Theorem~\ref{thm:genus-universality}(i)`.
- [MEDIUM] chapters/examples/lattice_foundations.tex:1714 — PROBLEM: `\ref{prop:pixton-genus2-planted-forest}` has no target; the exact formula cited is the displayed equation `\label{eq:planted-forest-genus2-explicit-bridge}`. FIX: replace `Proposition~\ref{prop:pixton-genus2-planted-forest}` with `equation~\eqref{eq:planted-forest-genus2-explicit-bridge}`.

thinking
**Considering reference adjustments**

I see that I need to search for instances of `\ref{princ:gravitational-primitivity}` in the repository, where there might be more than three references. The question is how to address the user's request for an exact fix. I could suggest retargeting the reference to `\ref{princ:guide-gravitational-primitivity}` or restoring the alias label near the principle header. Since the comment indicates the intention to migrate, I think adding a second label might preserve existing references effectively.
exec
/bin/zsh -lc "rg -n 'Three Hochschild theories|three-tier-r-matrix|holographic completion|free-fields-three-pillar|w-three-pillar|rem:sl3-koszul-dual|thm:genus-universality|eq:planted-forest-genus2-explicit-bridge|def:three-tier-r-matrix|subsec:concordance-holographic-completion|thm:heisenberg-bar\\}|thm:heisenberg-bar-complete|thm:hook-transport-corridor|subsec:thqg-ct2-cooperad-conjecture' chapters main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3910,3935p' chapters/frame/preface.tex
sed -n '280,310p' chapters/frame/guide_to_main_results.tex
sed -n '330,350p' chapters/examples/y_algebras.tex
sed -n '1708,1728p' chapters/examples/lattice_foundations.tex
sed -n '4148,4205p' chapters/examples/bar_complex_tables.tex
sed -n '268,286p' chapters/connections/outlook.tex
sed -n '1210,1245p' chapters/connections/thqg_open_closed_realization.tex
sed -n '296,312p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1637: \phantomsection\label{subsec:concordance-holographic-completion}% % concordance.tex
main.tex:1870: \phantomsection\label{thm:hook-transport-corridor}%
chapters/examples/w_algebras_deep.tex:2062: \textup{(}Theorem~\textup{\ref{thm:hook-transport-corridor}};
chapters/examples/w_algebras_deep.tex:2647:propagator (Theorem~\ref{thm:genus-universality}).
chapters/examples/w_algebras_deep.tex:2956:Theorem~\textup{\ref{thm:hook-transport-corridor}}\textup{)},
chapters/examples/beta_gamma.tex:1225:(Theorem~\ref{thm:genus-universality}), the genus-$g$ curvature
chapters/examples/y_algebras.tex:349:(Theorem~\ref{thm:genus-universality}). The generators of
chapters/examples/y_algebras.tex:641:(\S\ref{sec:concordance-three-tier-r-matrix}): it is
chapters/examples/y_algebras.tex:742:(Theorem~\ref{thm:genus-universality}),
chapters/examples/heisenberg_eisenstein.tex:569:consistent with the genus universality theorem (Theorem~\ref{thm:genus-universality}) with obstruction coefficient $\kappa_{\mathrm{obs}}(\mathcal{H}_\kappa) = \kappa$ (where $\kappa_{\mathrm{obs}}$ on the left denotes the obstruction coefficient of Definition~\ref{def:genus-g-obstruction} and $\kappa$ on the right is the Heisenberg level).
chapters/examples/heisenberg_eisenstein.tex:603:By Theorem~\ref{thm:genus-universality} with $\kappa(\mathcal{H}_\kappa) = \kappa$ and the Faber--Pandharipande $\lambda_g$ formula:
chapters/examples/free_fields.tex:94:\label{rem:free-fields-three-pillar}
chapters/examples/free_fields.tex:1425:\begin{theorem}[Heisenberg bar complex at genus 0; \ClaimStatusProvedHere]\label{thm:heisenberg-bar}
chapters/examples/free_fields.tex:1445:See Theorem~\ref{thm:heisenberg-bar-complete} for explicit formulas
chapters/examples/free_fields.tex:2424:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/free_fields.tex:2795:By Theorem~\ref{thm:heisenberg-bar}, the bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$ has cocommutative coproduct: the Heisenberg OPE $\alpha(z)\alpha(w) \sim k(z-w)^{-2}$ produces only the double-pole term, whose residue gives a symmetric (primitive) coproduct $\Delta(\alpha) = \alpha \otimes 1 + 1 \otimes \alpha$. Cocommutative coalgebras are Koszul dual to commutative algebras ($\mathrm{Com}^! = \mathrm{Lie}$, see \cite{LV12}, Theorem~7.6.5), so $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$. This is commutative with regular OPE, while $\mathcal{H}_k$ is non-commutative with singular OPE, so $\mathcal{H}_k \not\cong \mathcal{H}_k^!$.
chapters/examples/free_fields.tex:3398:(Theorem~\ref{thm:heisenberg-bar-complete}).
chapters/examples/free_fields.tex:3725:\begin{theorem}[Heisenberg bar complex: complete calculation; \ClaimStatusProvedHere]\label{thm:heisenberg-bar-complete}
chapters/examples/free_fields.tex:3860:The double pole prevents standard residue extraction: the literal residue $\mathrm{Res}_{z=w}[k/(z-w)^2 \cdot \eta_{zw}]$ vanishes since the integrand has a triple pole with zero residue (cf.\ the clarification at Theorem~\ref{thm:heisenberg-bar-complete}). Instead, the Borcherds identity extracts the OPE coefficient directly, giving the \emph{boundary pairing}
chapters/examples/free_fields.tex:3892:(Theorem~\ref{thm:genus-universality}), but the partition
 succeeded in 52ms:
 the genus-$1$ trace.
\item \emph{Categorical Drinfeld center}
 $Z(\cA\text{-}\mathsf{mod})$: the $E_2$-braided monoidal
 category of modules equivariant for the half-braiding.
 Arrow~3 of the $E_n$ circle.
\end{enumerate}
The geometry determines which theory applies: chiral
Hochschild lives on algebraic curves and uses the
$\Einf$-factorisation structure; topological Hochschild
lives on~$S^1$ and uses the $E_1$-structure; the Drinfeld
center lives in the representation category and uses the
$E_1$-monoidal structure
(Principle~\ref{princ:geometric-origin-hochschild};
Convention~\ref{conv:three-hochschild}).

\subsection*{10.5.\enspace The formality bridge and its failure}

For $\Einf$-chiral algebras (the entire standard landscape:
Heisenberg, Virasoro, affine Kac--Moody, $\cW_N$, and all
free-field algebras), the ordered and symmetric bars are
exec
/bin/zsh -lc "sed -n '1510,1532p' chapters/theory/bar_construction.tex
rg -n '\\\\label\\{def:(conilpotent-cobar|conilpotent-complete|analytic-bar-coalgebra|bar-coalgebra-identity|bar-coalgebra|coalgebra-identity)\\}' chapters/theory chapters/examples appendices main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3156,3174p' appendices/nonlinear_modular_shadows.tex
sed -n '28468,28695p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '108,155p' chapters/examples/w_algebras.tex
sed -n '2918,2932p' chapters/examples/w_algebras_deep.tex
sed -n '6548,6565p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
open substacks of $\operatorname{Ran}(X)$ and its differential restricts
to the collision-residue map on each boundary stratum.}
dg presentations of the bar object
$\mathcal{B}_X(\cA)$ are connected by a contractible space of
quasi-isomorphisms. In particular, any two such models give
canonically isomorphic cohomology, spectral sequences, and generating
functions.
\end{proposition}

\begin{proof}
Both presentations are cofibrant-fibrant objects in the model structure
on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
(that is, dg coalgebras whose iterated reduced coproduct vanishes on
every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
(Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
replacements in this model structure are unique up to a contractible
space of weak equivalences: the mapping space
$\operatorname{Map}(B_1, B_2)$ between two such replacements is
contractible whenever both compute the same homotopy object.
The configuration-space model $\bar{B}_X(\cA)$ is cofibrant by
 succeeded in 51ms:
\index{platonic package!shadow tower connection}
The 2025--2026 factorization envelope technology
(Nishinaka~\cite{Nish26}; Vicedo~\cite{Vic25}) provides a
functorial genus-$0$ machine: from a Lie conformal algebra one
constructs a factorization algebra whose associated vertex algebra
is the enveloping vertex algebra. The shadow obstruction tower of this
appendix supplies the higher-genus completion. That is, the
ideal object attached to a cyclically admissible Lie conformal
algebra~$L$
(Definition~\ref{def:cyclically-admissible}) is not merely the
genus-$0$ factorization algebra $\Fact_X(L)$, but the full
modular Koszul datum~$\Pi_X(L)$
(Construction~\ref{constr:platonic-package}), in which all
shadows ($\kappa$, $\Delta$, $\mathfrak{C}$,
$\mathfrak{Q}$, $\Theta$) are successive projections of a
single universal Maurer--Cartan element
$\Theta_L \in
\MC(\Defcyc(L) \widehat\otimes \mathbb{G}_{\mathrm{mod}})$.

Theorem~\ref{thm:mc2-bar-intrinsic}, this upgrades the shadow
 succeeded in 52ms:
$(\mathcal{W}^k, \mathcal{W}^{k'})$, preserving the
discriminant $\Delta(x)$
(Theorem~\ref{thm:ds-bar-gf-discriminant}).
Principal DS reduction acts functorially on
modular Koszul triples
(Construction~\ref{constr:ds-functor-triples}): algebra,
Koszul dual, and collision $r$-matrix all transfer.
The chain-level mechanism is the DS-HPL transfer theorem
(Volume~II, Theorem~thm:ds-hpl-transfer): homological perturbation through the BRST SDR transfers
the full dg-shifted Yangian data, with the transferred
coproduct strictly primitive at all degrees
(Principle~\ref{princ:gravitational-primitivity}). The
$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$ families
share $\Delta(x) = (1-3x)(1+x)$ despite entirely
different local operator content. The bar spectral sequence collapses
at $E_2$ for the Virasoro algebra (quartic pole drives $d_1$ but not
$d_2$); for $\mathcal{W}_N$ with $N \geq 3$, higher-order poles from
the $W^{(N)}$ self-OPE (order $2N$) produce additional
non-trivial differentials. The
curvature is non-scalar: $\mathcal{W}_3$ has two curvature channels,

thinking
**Inspecting code lines**

I need to inspect the y_algebras file, specifically around line 631 and maybe look at the actual section labels. I’ve already found an alias, so I want to check for similar patterns. I should focus my inspection on lines 625-645 and then also around 850-860 to see if anything stands out. This could help clarify what I’m working with and make the process smoother!
exec
/bin/zsh -lc "sed -n '625,645p' chapters/examples/y_algebras.tex
sed -n '850,860p' chapters/examples/y_algebras.tex
sed -n '3838,3852p' chapters/connections/concordance.tex
sed -n '6558,6570p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\Psi & J \\
J & 2T
\end{pmatrix},
\end{equation}
where the matrix is in the $(J, T)$ basis of
$V = \bC J \oplus \bC T$. The $\Sigma_2$-coinvariant
(averaging map, \S\ref{subsec:concordance-e1-primacy}) gives
$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
scalar modular characteristic.
\end{computation}

\begin{remark}[$r$-matrix tier classification]%
\label{rem:y111-r-tier}
\index{r-matrix@$r$-matrix!tier classification!Y111@$Y_{1,1,1}$}
The $r$-matrix of $Y_{1,1,1}[\Psi]$ is tier~(b) in the
$r$-matrix classification
(\S\ref{sec:concordance-three-tier-r-matrix}): it is
derived from the local OPE data, not independent input. The
$r$-matrix has a single simple pole at $z = 0$ (no higher poles),
placing it in the same structural class as the Heisenberg
exec
/bin/zsh -lc "sed -n '1458,1472p' chapters/examples/landscape_census.tex
sed -n '3972,4044p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(rem:free-fields-three-pillar|rem:w-three-pillar|chap:casimir-divisor)\\}' chapters main.tex /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '985,1000p' chapters/examples/yangians_foundations.tex
sed -n '403,412p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
sed -n '774,790p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Yangian, an $\Eone$-chiral algebra, the analogous role is played by
the $\Eone$-chiral Koszul duality theorem,
Theorem~\ref{thm:e1-chiral-koszul-duality});
Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}) produces the
$c + c'$ column via the complementarity formula;
Theorem~\ref{thm:genus-universality} produces the $\kappa$ column.
The individual synthesis remarks (Remark~\ref{rem:sl2-three-theorems}
(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
Remark~\ref{rem:lattice-three-theorems} (lattices),
Remark~\ref{rem:w-algebra-three-theorems} (W-algebras),
Remark~\ref{rem:deformation-three-theorems} (deformation quantization),
Remark~\ref{rem:yangian-three-theorems} (Yangians)) provide
detailed verifications for each example class.

%% ================================================================
\item \emph{Free fermion}:
 bar complex (Theorem~\ref{thm:fermion-bar-coalg}),
 Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$
 (Theorem~\ref{thm:betagamma-bc-koszul}),
 $\kappa = \tfrac{1}{4}$ (Table~\ref{tab:master-invariants}),
 succeeded in 52ms:
with boundary); (b)~an $\Eone$ analog of the Feynman
transform for the modular operad; (c)~an $\Eone$ analog
of the Faber--Pandharipande formula for tautological
integrals on $\mathcal{M}_{g,1}^{\partial}$. The
closest existing work is the Swiss-cheese operad
(Voronov~\cite{Voronov99}), which governs open-closed
homotopy algebras.
The toroidal algebra
\ifannalsedition\else
(Remark~\ref{rem:toroidal-three-theorems})
\fi faces the
same obstruction.

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~I (existence).
The conjecture posits the existence of an $\Eone$ genus theory on bordered Riemann surfaces, extending the chiral bar complex from closed to open surfaces.
\end{remark}

\begin{remark}[Lattice evidence for toroidal genus theory]
\label{rem:toroidal-lattice-evidence}
\index{lattice vertex algebra!genus-1 evidence for toroidal}
 succeeded in 52ms:
main.tex:1676: \phantomsection\label{chap:casimir-divisor}% % casimir_divisor_core_transport.tex (migrated to Vol II)
chapters/examples/free_fields.tex:94:\label{rem:free-fields-three-pillar}
chapters/examples/w_algebras.tex:148:\label{rem:w-three-pillar}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/casimir_divisor_core_transport.tex:7:\label{chap:casimir-divisor}
exec
/bin/zsh -lc "rg -n 'conilpotent dg coalgebras over|iterated reduced coproduct vanishes on every section|Conilpotent coalgebra|conilpotent chiral coalgebra' chapters/theory chapters/examples appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/free_fields.tex:2005:\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) &\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*) \quad \text{(conilpotent chiral coalgebra)} \\
chapters/theory/bar_construction.tex:1521:on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
chapters/theory/bar_construction.tex:2260:It defines a functor from chiral algebras to filtered conilpotent chiral coalgebras, with essential image the coalgebras having logarithmic coderivations supported on collision divisors.
chapters/theory/higher_genus_foundations.tex:1448:For a conilpotent chiral coalgebra $\mathcal{C}$ (valued in holonomic $\mathcal{D}$-modules), the distributional model of the geometric cobar complex is:
chapters/theory/configuration_spaces.tex:3681: \emph{(1) Functoriality.} The bar construction $\bar{B}^{\mathrm{ch}}$ is defined via the cofree conilpotent chiral coalgebra on the augmentation ideal, with differential induced by the chiral operations. A morphism $\phi\colon \mathcal{A}_1 \to \mathcal{A}_2$ preserves augmentation ideals and chiral operations, hence induces a coalgebra map $\bar{B}^{\mathrm{ch}}(\phi)$ by the universal property of the cofree coalgebra.
chapters/theory/poincare_duality.tex:357:The construction of $\mathcal{A}^!$ via Verdier duality yields a well-defined conilpotent chiral coalgebra:
chapters/theory/bar_cobar_adjunction_curved.tex:45:between chiral algebras and conilpotent chiral coalgebras on
chapters/theory/bar_cobar_adjunction_curved.tex:576:\begin{definition}[Conilpotent coalgebra]
chapters/theory/bar_cobar_adjunction_curved.tex:6322:equivalent to the homotopy category of conilpotent chiral coalgebras:
chapters/theory/cobar_construction.tex:203:\begin{definition}[Conilpotent coalgebra]\label{def:conilpotent-cobar}
chapters/theory/cobar_construction.tex:258:Let $\mathcal{C}$ be a conilpotent chiral coalgebra on a smooth algebraic
chapters/theory/cobar_construction.tex:513:For a conilpotent chiral coalgebra $\mathcal{C}$ on $X$ with coaugmentation
chapters/theory/cobar_construction.tex:2782:consists precisely of those conilpotent chiral coalgebras $\mathcal{C}$ satisfying:
chapters/theory/bar_cobar_adjunction_inversion.tex:1413:subcomodules, which holds for conilpotent chiral coalgebras because

thinking
**Evaluating intended labels**

It seems like the user is likely looking for a label of either `def:conilpotent-complete` or `def:conilpotent-cobar`. I'm considering which definition fits best here. I should dive into the details surrounding the `bar_cobar_adjunction_curved` definition to better understand the context and relationships among these terms. I'll need to ensure I'm clear on how these concepts interact!
exec
/bin/zsh -lc "sed -n '568,590p' chapters/theory/bar_cobar_adjunction_curved.tex
sed -n '198,216p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item convergence control from Theorem~\ref{thm:conilpotency-convergence} and
Theorem~\ref{thm:bar-convergence}.
\end{enumerate}
\end{remark}

\subsection{Conilpotency and convergence without completion}
\label{sec:conilpotency-convergence}

\begin{definition}[Conilpotent coalgebra]
\label{def:conilpotent-complete}
\index{conilpotent!coalgebra}
\index{conilpotent!filtration}
A coalgebra $C$ is \emph{conilpotent} if for each $c \in C$, there exists $N$ such that:
\begin{equation}
\Delta^{(N)}(c) = 0
\end{equation}
where $\Delta^{(N)}$ is the $N$-fold iterated comultiplication.
\end{definition}

\begin{theorem}[Conilpotency ensures convergence; \ClaimStatusProvedHere]

thinking
**Searching for missing files**

I’m wondering if there are orphaned markdown files or chapter files that haven't been included. I need to search through all `.tex` files, excluding volumes, for specific labels. My last search didn’t yield any results—maybe there’s an uncompiled file not located in the chapters? I'll check the entire repo for any `.tex` files to see if I can find what I'm missing. This should help clarify the situation!
exec
/bin/zsh -lc "rg -n '\\\\label\\{(lem:thqg-X-composition-decay|prop:thqg-X-second-quantization|thm:thqg-X-heisenberg-sewing-full|rem:thqg-X-pants-independence|thm:thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|thm:thqg-III-genus-1-holographic|thm:thqg-III-eigenspace-decomposition|cor:thqg-III-dimension-parity|subsec:thqg-III-shifted-symplectic|cor:thqg-III-complementarity-exchange|thm:thqg-g3-polarization|thm:thqg-g4-s-duality|thm:thqg-g5-yangian|thm:thqg-g6-soft-graviton|sec:thqg-soft-graviton-theorems|prop:thqg-V-c13-self-duality|thm:thqg-V-collision-twisting)\\}' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Evaluating citation fixes**

I’m considering whether to remove numeric theorem references or move the chapter back. An alternative could be to replace them with textual external citations, as was done in F17 for Volume II. For any completely absent internal references, it might be best to rewrite these as descriptive prose that references a planned package. I'm also wondering if there are results in Volume II corresponding with V1 aliases. It's worth searching in Volume II for any relevant connections.
exec
/bin/zsh -lc "rg -n 'V1-(lem:thqg-X-composition-decay|prop:thqg-X-second-quantization|thm:thqg-X-heisenberg-sewing-full|rem:thqg-X-pants-independence|thm:thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|thm:thqg-III-genus-1-holographic|thm:thqg-III-eigenspace-decomposition|cor:thqg-III-dimension-parity|subsec:thqg-III-shifted-symplectic|cor:thqg-III-complementarity-exchange|thm:thqg-g3-polarization|thm:thqg-g4-s-duality|thm:thqg-g5-yangian|thm:thqg-g6-soft-graviton|sec:thqg-soft-graviton-theorems|prop:thqg-V-c13-self-duality|thm:thqg-V-collision-twisting)' /Users/raeez/chiral-bar-cobar-vol2 -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:657:\phantomsection\label{V1-thm:thqg-g5-yangian}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:922:\phantomsection\label{V1-subsec:thqg-III-shifted-symplectic}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:976:\phantomsection\label{V1-thm:thqg-I-determinant-formula}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:981:\phantomsection\label{V1-thm:thqg-III-eigenspace-decomposition}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:983:\phantomsection\label{V1-thm:thqg-V-collision-twisting}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1298:(Volume~I, Theorem~\ref*{V1-thm:thqg-g5-yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1036:\textup{(}Theorem~\textup{\ref{V1-thm:thqg-V-collision-twisting})}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1136:(Theorem~\ref{V1-thm:thqg-V-collision-twisting}(ii)).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:1545:of Theorem~\ref{V1-thm:thqg-V-collision-twisting}:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2063:skew-symmetry property (Theorem~\ref{V1-thm:thqg-V-collision-twisting}(ii))
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2439: & Proved (Thm~\ref{V1-thm:thqg-V-collision-twisting}) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:58:\S\ref{V1-subsec:thqg-III-shifted-symplectic} develops the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1072:(Theorem~\ref{V1-thm:thqg-III-eigenspace-decomposition}), the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:2200: (\S\ref{V1-subsec:thqg-III-shifted-symplectic}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2630:Substitute the determinant formula (Theorem~\ref{V1-thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{V1-thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:874:(Lemma~\ref{V1-lem:thqg-X-composition-decay}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:899:By Proposition~\ref{V1-prop:thqg-X-second-quantization}\,(i):
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1000:\quad\text{(Proposition~\ref{V1-prop:thqg-X-second-quantization}\,(i))}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1166:by Lemma~\ref{V1-lem:thqg-X-composition-decay}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1507:(Theorem~\ref{V1-thm:thqg-X-heisenberg-sewing-full}\,(IV)) and






thinking
**Considering alias adjustments**

I’m looking into Vol2, which has V1 aliases in the main, but it seems there are some missing ones, like thqg-X. I think I could add V1 aliases there, but in Vol1, these labels are completely absent. Maybe I should add phantom labels for thqg-X, I, and III in Vol1's main, similar to Vol2. However, it doesn't seem ideal to add aliases to nonexistent content. I wonder if these labels relate to omitted chapters? Let's check comments around the alias block. Maybe the user is looking for an audit instead of fixes. I could suggest adding `\phantomsection\label{...}` in the alias block with comments indicating migrated chapters or Volume II, but I realize phantom labels won't provide theorem numbering.
thinking
**Exploring citation fixes**

This situation doesn't look ideal. Unless there's an alias file with the content, I think the better solution might be to restore the chapter or switch to textual external citations. Since the user is auditing unfinished work, I feel that honest textual citations make more sense. For internal omitted chapter references in the same volume, it might be best to restore those chapters or add labels instead. If the content is intentionally omitted, using textual citations for the external chapters feels more straightforward than using phantom labels. For instance, the citation `thm:dnp-bar-cobar-identification` referenced in Vol II used a textual citation, which seems right. Similarly, `prop:mixed-product-decomposition` points to a proposition in Volume II. So, I should stick with textual external citations. Now, I need to consider `conv:three-hochschild` and `princ:gravitational-primitivity`, which reside in inactive `chapters/connections/concordance.tex` in the same repo but aren’t compiled.
thinking
**Considering phantom aliases**

Using phantom aliases in the main might actually be acceptable here since the content is in the same volume but isn't compiled due to chapter swapping. However, I should note that the main already has other concordance aliases. So, the exact fix seems to be adding the missing phantom labels in the main alias block, which would be consistent and minimally invasive. Alternatively, I could retarget to existing compiled labels, like `princ:guide-...`, which may actually be more semantically accurate.
thinking
**Considering reference methods**

I’m thinking about how to produce meaningful references. The repository uses phantom section labels for chapter references, and I wonder if `\ref` on a chapter label returns the current chapter number. But if it’s outside any chapter, it may return the last chapter count, which feels dodgy. Since they rely on hyperref linking and phantom labels can produce bogus numbering, it’s better to rewrite the text instead of using unresolved numeric cross-references. Good catch!
thinking
**Reviewing label fixes**

I’m considering how to handle labels in inactive files that haven’t been compiled. Using phantom labels in the main document isn't enough if the numbering is incorrect. For `conv:three-hochschild`, since there’s no compiled reference, I could change it to plain text: “the concordance convention on the three Hochschild theories,” which avoids bogus numbering. For `subsec:concordance-e1-primacy`, I can replace it with “the concordance subsection on $E_1$ primacy,” but I should check if it refers specifically to the averaging map to ensure accuracy.
thinking
**Deciding on reference clarity**

I’ve realized that for the inactive `concordance.tex` subsection, I might just write, “the concordance subsection on $E_1$ primacy” without a reference. This seems like an honest and accurate approach. By doing so, I can avoid the pitfalls of incorrect numbering and present the information clearly. It’s a straightforward solution that keeps everything simple and precise for the user. I'm leaning toward this clean wording!
exec
/bin/zsh -lc "sed -n '1038,1058p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 = \varnothing$: no open inputs produce closed outputs.

\item \emph{Genus-$0$ reduction:}
 At $g = 0$, $\FM_k(\Sigma_0) = \FM_k(\C)$, and
 $\SCmod\big|_{g=0} = \SCchtop$
 (Definition~\ref{def:SC-operations}).
\end{enumerate}
\end{definition}

\begin{proposition}[Product decomposition of mixed operations]
\label{prop:mixed-product-decomposition}
\index{Swiss-cheese operad!mixed operations!product decomposition}
For each $g \ge 0$, $k \ge 0$, $m \ge 1$, there is a
homotopy equivalence of chain complexes
\begin{equation}\label{eq:mixed-product}
 C_\ast(\FM_{k|m}(\Sigma_g, \partial))
 \simeq
 C_\ast(\FM_k(\Sigma_g)) \otimes C_\ast(\Eone(m)).
\end{equation}
\end{proposition}
exec
/bin/zsh -lc "sed -n '130,145p' chapters/connections/feynman_connection.tex
sed -n '5070,5090p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2468,2478p' chapters/theory/chiral_koszul_pairs.tex
sed -n '250,262p' chapters/theory/three_invariants.tex
sed -n '1340,1352p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
is the scalar trace
$\kappa(\cA)\cdot\deg(\lambda_1) = \kappa(\cA)/24$
(Theorems~\ref{thm:genus-universality}
and~\ref{thm:explicit-theta}).

\section{Path integral = bar complex}

\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
\textup{(}free boson at nonzero Heisenberg level\textup{)} on a
compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
\begin{equation}\label{eq:bar-partition-heisenberg}
Z_g^{\mathcal{H}_{\kappa^{\mathrm{Heis}}}}(\Sigma_g)
= H^0(\bar{B}^{(g)}(\mathcal{H}_{\kappa^{\mathrm{Heis}}})) = \mathbb{C}
\end{equation}
\begin{equation}\label{eq:bar-npoint-heisenberg}
\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~IV
(trace/index). The identification $\hbar = g_s$ asserts that the
genus expansion parameter is the image of the universal deformation
object under a trace functor.
 succeeded in 51ms:
$\iota \colon \operatorname{Sym}^{\mathrm{ch}}(V)_h \to
\barB_h(\cA)$ is injective at every bar-relevant weight~$h$.
Suppose $d_r \neq 0$ for some $r \geq 2$. Then there exists
$x \in E_r^{p,q}$ with $d_r(x) \neq 0$, represented by
$\tilde{x} \in F^p\barB$ with $d_{\mathrm{bar}}(\tilde{x})
\in F^{p+r}\barB$. If $\tilde{x} \in \operatorname{im}(\iota)$,
it represents a nonzero class in
$\operatorname{gr}^p(\barB) \cong \operatorname{Sym}^p(V)$,
and $d_r(\tilde{x})$ represents a nonzero class in
$\operatorname{gr}^{p+r}$. By PBW strictness (injectivity
of~$\iota$ at all bar-relevant weights), this contradicts the

\item \emph{The shadow obstruction tower classification}
 \textup{(}the four classes $G, L, C, M$\textup{)}: the class is
 determined by $r_{\max}$, not by $p_{\max}$. In particular, class~$C$
 ($\beta\gamma$) has $r_{\max} = 4$ even though $p_{\max} = 1$.

\item \emph{The DNP non-renormalization theorem}
 \textup{(}Theorem~\textup{\ref{thm:non-renormalization-tree}}(iii)\textup{)}:
 one-loop exactness of line-operator OPE corresponds to $E_2$-collapse
exec
/bin/zsh -lc "sed -n '5090,5115p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \times \overline{\mathcal{M}}_{g_2,n_2+1}$, its residue is the
 contracted tensor product of the corresponding lower-genus bar
 classes.
\item Along a non-separating boundary divisor
 $D_\Gamma \cong \overline{\mathcal{M}}_{g-1,n+2}$, its residue is
 the self-gluing contraction of the $(g-1,n+2)$ bar class.
\item For the Heisenberg algebra $\mathcal{H}_\kappa$, pairing the bar
 class with the Gaussian measure at all genera computes free boson
 correlation functions
 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-path-integral-heisenberg})}.
\end{enumerate}
\end{theorem}

\begin{proof}
Items~(i) and~(ii) are the separating and non-separating boundary
components of the modular operad structure on the genus-graded bar
package: the bar differential on stable curves is assembled from
boundary residues, and Theorem~\ref{thm:genus-induction-strict}
identifies those residues with the corresponding clutching
contractions of lower-genus bar classes. Item~(iii) is proved in

thinking
**Examining the theorem concerns**

Item (iii) discusses theorem support for free boson correlation functions, but I see that the existing source presents a conjecture, not a theorem. I should consider pointing to `Conjecture\ref{conj:v1-bar-cobar-path-integral-heisenberg}` and possibly replace "computes" with "is conjecturally computed by." Otherwise, it asserts an unproven statement. There’s also a proposal to use direct Gaussian evaluation, but that needs grounding in a local theorem. I'll search to confirm if there’s a direct computation available.
exec
/bin/zsh -lc "rg -n 'Gaussian measure|Gaussian integrals|Dedekind|eta-function|free boson correlation' chapters/examples/free_fields.tex chapters/connections/feynman_connection.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/feynman_connection.tex:117:The free boson correlation function expands as
chapters/examples/free_fields.tex:2412:Dedekind eta function. At $t = 1$, the series
chapters/examples/free_fields.tex:5097: class with the Gaussian measure at all genera computes free boson
chapters/examples/free_fields.tex:5111:direct computation using Gaussian integrals and the
chapters/examples/free_fields.tex:5112:Dedekind $\eta$-function.
chapters/examples/free_fields.tex:5314:dimension \textup{(}zeta-function regularization of
exec
/bin/zsh -lc "rg -n '\\\\label\\{warn:three-hochschild-intro\\}|Three Hochschild theories' chapters/theory/introduction.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:688:\begin{warning}[Three Hochschild theories]
chapters/theory/introduction.tex:689:\label{warn:three-hochschild-intro}
chapters/frame/preface.tex:1035:Three Hochschild theories coexist:
chapters/frame/preface.tex:3897:\subsection*{10.4.\enspace Three Hochschild theories}
exec
/bin/zsh -lc "sed -n '684,706p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 (Lemma~\ref{lem:chirhoch-descent}), reducing Theorem~H to Theorem~A's
 Verdier intertwining.
\end{itemize}

\begin{warning}[Three Hochschild theories]
\label{warn:three-hochschild-intro}
\index{Hochschild cohomology!three variants}%
Three inequivalent notions of ``Hochschild cohomology'' coexist
in this programme; conflating them is a persistent source of
error.
\emph{Chiral Hochschild} $\ChirHoch^*(\cA) =
H^*(\operatorname{CoDer}(\barB(\cA)))$ is the cohomology of
coderivations of the bar coalgebra; it lives on the
curve~$X$ and has cohomological amplitude~$[0,2]$ on the
Koszul locus (Theorem~H).
\emph{Topological Hochschild} $\mathrm{HH}^*_{\mathrm{top}}$
is the factorization homology on the circle $S^1$; it lives
in dimension~$1$ higher and governs the $\Eone$-chiral bar of
Volume~II.
\emph{Categorical Hochschild} $\mathrm{HH}^*(\mathrm{Rep}(\cA))$
exec
/bin/zsh -lc "rg -n 'E1 primacy|\\\\label\\{(thm:e1-primacy|sec:e1-five-theorems|subsec:e1-as-primitive|princ:e1-primacy)\\}' chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:3845:\index{E1 primacy@$E_1$ primacy|textbf}
chapters/theory/e1_modular_koszul.tex:1902:\label{sec:e1-five-theorems}
chapters/theory/introduction.tex:1175:\label{subsec:e1-as-primitive}
chapters/theory/introduction.tex:1304:\label{thm:e1-primacy}
chapters/theory/introduction.tex:1398:\label{princ:e1-primacy}
exec
/bin/zsh -lc "sed -n '1170,1410p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Proposition~\ref{prop:nilpotent-transport-typeA}).


\section{The \texorpdfstring{$\Eone$}{E1} story as primitive: averaging and the modular shadow}
\label{sec:e1-as-primitive}
\label{subsec:e1-as-primitive}
\index{averaging map!av@$\operatorname{av}$|textbf}
\index{ordered bar complex!as primitive object|textbf}
\index{E1 algebra@$\Eone$-algebra!primacy|textbf}
\index{Yangian!as primitive datum}
\index{R-matrix!as primitive of $\kappa$}
\index{symmetric bar complex!as $\Sigma_n$-coinvariant shadow}

The bar complex $\barB(\cA)$ presented in \S\ref{sec:volume-one-route}
is the symmetric (commutative) bar: it lives on
$(s^{-1}\bar\cA)^{\otimes n}_{\Sigma_n}$ and forgets the order in
which collisions occur. This presentation is convenient for
formulating the five main theorems and connecting to the modular
operad on~$\overline{\cM}_{g,n}$, but it is not the natural
primitive of the theory. The natural primitive is the
exec
/bin/zsh -lc "sed -n '80,108p' chapters/examples/free_fields.tex
sed -n '140,160p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
contact shadow nontrivial on the charged stratum), even though
$\Theta_{\beta\gamma}^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ on the
weight-changing line (the global modular characteristic
$\kappa(\beta\gamma) = c/2$ is generically nonzero). Both
two-generator free-field systems ($\beta\gamma$ and $bc$) are class~C
($r_{\max} = 4$) by the same stratum separation mechanism; the
single-generator free fermion is class~G ($r_{\max} = 2$) by
fermionic antisymmetry. The free-field periodic table therefore
exhibits the transition from the Gaussian to the contact/quartic
archetype within the shadow depth classification
(Table~\ref{tab:shadow-tower-census}).
\end{remark}

\begin{remark}[Three-pillar interpretation: free-field archetypes]
\label{rem:free-fields-three-pillar}
\index{free fields!three-pillar interpretation}
In the three-pillar architecture
(\S\ref{sec:concordance-three-pillars}):
(i)~free bosons produce a \emph{strict} homotopy chiral algebra
(Gaussian archetype, all secondary Borcherds operations
exec
/bin/zsh -lc "sed -n '2178,2425p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The proof exploits the one-particle Bergman reduction
(Theorem~\ref{thm:heisenberg-one-particle-sewing}): every statement
about the Fock-space cooperad reduces to an operator-algebraic
statement on the one-particle Bergman space $A^2(D)$, where the
arguments are elementary.

\medskip\noindent
\textit{Proof of~\textup{(I)}: well-definedness and equivariance.}
Fix a stable bordered graph $\Gamma$ of type $(g,n)$ with internal
edges $E(\Gamma)$. Each internal edge $e$ contributes a sewing
operator $\sewop_{q_e}$ with exponentially decaying matrix
coefficients $|(\sewop_{q_e})_{n,m}| \leq C\,q_e^{(n+m)/2}$
(Lemma~\ref{lem:thqg-X-composition-decay}). In particular,
$\sewop_{q_e}$ is trace class on $A^2(D)$ with
$\|\sewop_{q_e}\|_1 = q_e/(1-q_e)$.

The full cocomposition is the second quantization
$\secquant(\cdot)^\kappa$ applied to a product of trace-class
operators on the one-particle space. By
Proposition~\ref{prop:thqg-X-second-quantization}, $\secquant(T)$ is

thinking
**Investigating missing labels**

I'm noticing that this theorem has several missing labels in the proofs. I wonder if there are compiled equivalents in the current volume. Maybe I could refer to `thm:heisenberg-one-particle-sewing`, `prop:heisenberg-open-sector`, or `thm:thqg-annulus-trace` for some steps, but specific propositions related to decay and second quantization seem to be absent. I should probably add new labels to existing results if they fit the same theorem or are mentioned earlier. I’ll need to inspect nearby theorem names and earlier files for context.
exec
/bin/zsh -lc "rg -n 'composition decay|second quantization|pants decomposition|pants independence|trace class|Fredholm determinant formula|one-particle sewing' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
200: Pair-of-pants sewing is the second quantization of a
217:Clauses~(iii) and~(iv) follow from the one-particle sewing reduction
2071:vertex $v$ contributes the second quantization
2104:where $\sewker_{g_v, n_v}$ is the one-particle sewing kernel of the
2191:$\sewop_{q_e}$ is trace class on $A^2(D)$ with
2194:The full cocomposition is the second quantization
2198:trace class on $\operatorname{Sym} A^2(D)$ whenever $T$ is trace
2200:composed operator at each vertex is trace class, and $\delta_\Gamma$
2217:By the one-particle sewing reduction
2220:the second quantization of a one-particle operator:
2303:on $A^2(D)$, and the second quantization functor $\secquant$ is
2399:\sum_{\text{pants decompositions}}
2417:Laplacian determinant. (The summation over pants decompositions

thinking
**Inspecting missing labels**

I'm thinking that the missing labels might relate to statements made in the early sections of the theorem, particularly around lines 160 to 217. So, I need to take a closer look at those specific parts to see if I can find the connection. It seems like there's a key link that I’m missing, and I’m curious to uncover how these elements fit together! Let's dive in further!
exec
/bin/zsh -lc "sed -n '160,225p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{Heisenberg!mode--Bergman correspondence}%
\index{Bergman space!Heisenberg identification}%
On the algebraic Heisenberg Fock core, define the mode--Bergman map
\[
\Theta(a_{-n-1}\mathbf{1})
\;=\;
\sqrt{n{+}1}\; z^n
\;\in\; A^2(D),
\]
extended multiplicatively by symmetrization:
$\Theta(a_{-n_1-1} \cdots a_{-n_k-1}\mathbf{1})
= \operatorname{Sym}(\Theta(a_{-n_1-1}\mathbf{1}) \otimes
\cdots \otimes \Theta(a_{-n_k-1}\mathbf{1}))$.
This gives a dense algebraic map
$\Theta \colon \text{Fock core} \to
\operatorname{Sym} A^2(D)$
from the Heisenberg Fock space to the symmetric algebra of the
Bergman space of the disk.
Moriwaki~\cite{Moriwaki26b} identifies a conformally flat 2-disk
algebra on $\operatorname{Sym} A^2(D)$ with the ind-Hilbert completion
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:heisenberg-one-particle-sewing|prop:hs-trace-class|prop:heisenberg-open-sector|thm:thqg-annulus-trace|thm:heisenberg-sewing)\\}' chapters/examples/heisenberg_eisenstein.tex chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/examples/heisenberg_eisenstein.tex:1983:\label{prop:heisenberg-open-sector}
chapters/connections/thqg_open_closed_realization.tex:633:\label{thm:thqg-annulus-trace}
chapters/connections/genus_complete.tex:1371:\ClaimStatusProvedHere]\label{prop:hs-trace-class}%
chapters/connections/genus_complete.tex:1475:\label{thm:heisenberg-one-particle-sewing}%
exec
/bin/zsh -lc "sed -n '1365,1495p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1968,2005p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{equation}
Define the \emph{weighted completion}
$H_q := \widehat{\bigoplus}_{n \geq 0} q^n H_n$.
\end{definition}

\begin{proposition}[Closed amplitudes are trace class;
\ClaimStatusProvedHere]\label{prop:hs-trace-class}%
Under HS-sewing, $m_q \colon H_q \,\widehat{\otimes}\, H_q \to H_q$
is Hilbert--Schmidt and every closed amplitude is trace class.
\end{proposition}

\begin{proof}
$\|m_q\|_{\mathrm{HS}}^2 = \sum_{a,b,c} q^{a+b+c}
\|m_{a,b}^c\|_{\mathrm{HS}}^2 < \infty$ by~\eqref{eq:hs-sewing}.
A genus-$g$ surface with~$n$ punctures decomposes into $2g-2+n$
pairs of pants; each sewing circle contributes one pair-of-pants
composition. Composition of two Hilbert--Schmidt operators is
trace class.
\end{proof}

 succeeded in 51ms:
compatibility with the closed-sector MC element
$\Theta^{\mathrm{oc}}$. For a general chiral algebra, verifying these
axioms requires the full derived structure of the open-sector
category. The Heisenberg is the first case where the verification
succeeds completely: the one-particle Bergman reduction
(Theorem~\ref{thm:heisenberg-one-particle-sewing}) collapses the
infinite-dimensional categorical cooperad to operator algebra on the
Bergman space $A^2(D)$, where coassociativity is the multiplicativity
of Fredholm determinants.

\subsection{The open-sector category}
\label{subsec:heisenberg-open-sector-category}

\begin{proposition}[Open-sector category for Heisenberg;
\ClaimStatusProvedHere]
\label{prop:heisenberg-open-sector}
\index{Heisenberg!open-sector category}
The open-sector category $\Cop(\cH_\kappa)$ has the following
structure.
\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Searching for second quantization**

I'm looking into the existing files to search for `\secquant` or any propositions. There's a reference to `thm:heisenberg-sewing}(iii)` related to second quantization via pair-of-pants sewing, but I'm wondering if the trace-class criterion might be more general. I should also check for `prop:hs-trace-class` or any generic facts that don't have labels. The `secquant` section may not contain too many entries, so I'll find out what I can.
exec
/bin/zsh -lc "rg -n '\\\\secquant|second quanti[sz]ation|trace class on \\\\operatorname\\{Sym\\} A\\"'^2'"\\(D\\)|Fredholm determinant' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/genus_complete.tex:1477:\index{Fredholm determinant!Heisenberg}%
chapters/connections/genus_complete.tex:1488:The genus-$g$ partition function is the Fredholm determinant
chapters/connections/genus_complete.tex:1519:The Fredholm determinant $\det(1 - K_q) = \eta(q)/q^{1/24}$ connects
chapters/examples/heisenberg_eisenstein.tex:200: Pair-of-pants sewing is the second quantization of a
chapters/examples/heisenberg_eisenstein.tex:203: Every closed amplitude is a Fredholm determinant on the
chapters/examples/heisenberg_eisenstein.tex:219:reduces the full Fock-space sewing amplitude to a Fredholm determinant
chapters/examples/heisenberg_eisenstein.tex:1976:of Fredholm determinants.
chapters/examples/heisenberg_eisenstein.tex:2071:vertex $v$ contributes the second quantization
chapters/examples/heisenberg_eisenstein.tex:2072:$\secquant(R_v)$ of its vertex restriction operator.
chapters/examples/heisenberg_eisenstein.tex:2086:\secquant\!\Bigl(
chapters/examples/heisenberg_eisenstein.tex:2194:The full cocomposition is the second quantization
chapters/examples/heisenberg_eisenstein.tex:2195:$\secquant(\cdot)^\kappa$ applied to a product of trace-class
chapters/examples/heisenberg_eisenstein.tex:2197:Proposition~\ref{prop:thqg-X-second-quantization}, $\secquant(T)$ is
chapters/examples/heisenberg_eisenstein.tex:2220:the second quantization of a one-particle operator:
chapters/examples/heisenberg_eisenstein.tex:2221:$A_P = \secquant(R)$ for a pair-of-pants amplitude. The Fredholm
chapters/examples/heisenberg_eisenstein.tex:2228:\secquant(T_1 \circ T_2)\bigr)
chapters/examples/heisenberg_eisenstein.tex:2267:\emph{Step~3: Fredholm determinant multiplicativity.}
chapters/examples/heisenberg_eisenstein.tex:2291:(operator composition is associative). The Fredholm determinant,
chapters/examples/heisenberg_eisenstein.tex:2303:on $A^2(D)$, and the second quantization functor $\secquant$ is
chapters/examples/heisenberg_eisenstein.tex:2324:$\operatorname{Tr}_{\mathrm{Sym}}(\secquant(\sewop_q)^\kappa)
exec
/bin/zsh -lc "rg -n 'eq:thqg-X-polyakov|Polyakov--Alvarez|pants-independence|det\\operatorname\\{Im\\}\\\\Omega|zeta-regularized' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex chapters/connections/thqg_fredholm_partition_functions.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:eq:thqg-X-polyakov|Polyakov--Alvarez|pants-independence|det\operatorname\{Im\}\\Omega|zeta-regularized)
                                                                  ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'eq:thqg-X-polyakov' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex
rg -n 'Polyakov--Alvarez|pants-independence|zeta-regularized|det\\operatorname\\{Im\\}\\\\Omega' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
chapters/examples/heisenberg_eisenstein.tex:2414:(\eqref{eq:thqg-X-polyakov}, Theorem~\ref{thm:thqg-X-heisenberg-sewing-full}(IV)),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:919:\begin{equation}% label removed: eq:thqg-X-polyakov
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1209:\eqref{V1-eq:thqg-X-polyakov} at genus~$2$ gives
rg: regex parse error:
    (?:Polyakov--Alvarez|pants-independence|zeta-regularized|det\operatorname\{Im\}\\Omega)
                                                                ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'Polyakov--Alvarez|pants-independence|zeta-regularized|det.*Im' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:653:Z_{\Sigma_2}^{\mathcal{H}} = \frac{1}{\det(\mathrm{Im}\,\Omega)^{1/2}}
chapters/examples/heisenberg_eisenstein.tex:664:$1/\det(\mathrm{Im}\,\Omega)^{1/2}$ times these oscillator
chapters/examples/heisenberg_eisenstein.tex:782:Z_{\Sigma_g}^{\mathcal{H}} = \frac{1}{\det(\mathrm{Im}\,\Omega_g)^{1/2}}
chapters/examples/heisenberg_eisenstein.tex:789:\[|\eta(\tau)|^{-2} = q^{-1/24}\bar{q}^{-1/24} \cdot \det'(\bar{\partial}_0)^{-1} \cdot (\mathrm{Im}\,\tau)^{1/2}\]
chapters/examples/heisenberg_eisenstein.tex:790:where $\det'(\bar{\partial}_0)$ is the zeta-regularized determinant of the
chapters/examples/heisenberg_eisenstein.tex:816:\[Z_g = \frac{1}{\det(\mathrm{Im}\,\Omega_g)^{1/2}}\]
chapters/examples/heisenberg_eisenstein.tex:1312:$[\det(\operatorname{Im}\Omega)]^{-d/2}
chapters/examples/heisenberg_eisenstein.tex:2162: (\det\operatorname{Im}\Omega)^{-\kappa/2}
chapters/examples/heisenberg_eisenstein.tex:2405:(\det\operatorname{Im}\Omega)^{-\kappa/2}
chapters/examples/heisenberg_eisenstein.tex:2413:The third is the Polyakov--Alvarez formula
chapters/examples/heisenberg_eisenstein.tex:2416:the period-matrix determinant times the zeta-regularized
chapters/examples/heisenberg_eisenstein.tex:2420:Remark~\ref{rem:thqg-X-pants-independence}.)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:450:% label removed: rem:thqg-X-pants-independence%
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:674: \bigl(\det\operatorname{Im}\Omega\bigr)^{-\kappa/2}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:679: $\zetareg\Delta$ is the zeta-regularized determinant of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:915:the period matrix $\Omega \in \Siegel_g$. The Polyakov--Alvarez
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:917:determinants to the period matrix and the zeta-regularized
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:922:= (\det\operatorname{Im}\Omega)^{-1/2}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:937:= (\det\operatorname{Im}\Omega)^{-\kappa/2}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex:1120:\bigl(\det\operatorname{Im}\Omega\bigr)^{-\kappa/2}

thinking
**Inspecting local proofs**

I need to look into potential local proofs related to the heisenberg_eisenstein theorem that might fill in the gaps where the theorem is missing. I think I should focus on the local theorem around line 2162; it’s possible that the theorem statement includes the partition function formula already. Let me check the labels earlier in the file to see if they provide any useful context. There's definitely some digging to do here!
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:heisenberg-bv-bar-all-genera|thm:heisenberg-all-genus|thm:ct2-heisenberg|rem:heisenberg-sewing-status|eq:thqg-X-polyakov)\\}' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fredholm_partition_functions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:227:\begin{remark}\label{rem:heisenberg-sewing-status}
chapters/examples/heisenberg_eisenstein.tex:676:\begin{theorem}[Heisenberg at general genus; \ClaimStatusProvedHere]\label{thm:heisenberg-all-genus}
chapters/examples/heisenberg_eisenstein.tex:2112:\label{thm:ct2-heisenberg}

thinking
**Inspecting theorem components**

I think the theorem at `thm:ct2-heisenberg` around line 2112 might contain the proof I’m looking for. There are multiple parts to consider, and I suspect that some missing references within the proof could be related to local sub-results instead of pointing towards earlier theorems like `thm:heisenberg-sewing` and `thm:heisenberg-all-genus`. So, I’ll need to check the statement of the theorem at line 2112 to clarify things.
exec
/bin/zsh -lc "sed -n '2060,2145p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\operatorname{End}_{\Cop}(\cF_\lambda)
\;\longrightarrow\;
\bigotimes_{v \in V(\Gamma)}
\operatorname{End}_{\Cop}(\cF_\lambda)
\end{equation}
by the sewing formula: decompose the genus-$g$ amplitude into
a product of vertex amplitudes connected by sewing operators.
At the one-particle level
\textup{(}Theorem~\textup{\ref{thm:heisenberg-one-particle-sewing}}\textup{)},
each internal edge $e \in E(\Gamma)$ contributes a sewing
operator $\sewop_{q_e}$ on the Bergman space $A^2(D)$, and each
vertex $v$ contributes the second quantization
$\secquant(R_v)$ of its vertex restriction operator.

Concretely, for a genus-$g$ amplitude
$Z \in \operatorname{End}_{\Cop}(\cF_\lambda)$, the
cocomposition is:
\begin{equation}\label{eq:heisenberg-delta-gamma-formula}
\delta_\Gamma(Z)
\;=\;


thinking
**Reviewing theorem proof labels**

I see that the theorem proof is missing some labels. For instance, it could use `thm:heisenberg-one-particle-sewing` and `prop:hs-trace-class` for specific lines. The `lem:thqg-X-composition-decay` line could be adjusted to reference the Heisenberg theorem since it provides coefficient bounds. I’ll rewrite sentences to ensure clarity and use multiple references as needed. Also, I need to check for any unresolved references outside of the existing 61. I'll summarize findings about same-file forward refs afterward.
thinking
**Inspecting entanglement contexts**

I need to take a closer look at `thqg_entanglement_programme` and `entanglement_modular_koszul`. There’s a chance some of these references could point to omitted sections in the same volume, potentially as orphaned chapters that weren't compiled. I should inspect the context around those lines to understand their relevance better. This might help clarify how they fit into the larger picture and if any adjustments are necessary for compiling.
exec
/bin/zsh -lc "sed -n '40,85p' chapters/connections/thqg_entanglement_programme.tex
sed -n '160,215p' chapters/connections/thqg_entanglement_programme.tex
sed -n '515,565p' chapters/connections/thqg_entanglement_programme.tex
sed -n '620,800p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '330,345p' chapters/connections/entanglement_modular_koszul.tex
sed -n '518,530p' chapters/connections/entanglement_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '52,70p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex
sed -n '1030,1080p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex
sed -n '1560,1615p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
measuring the size of each Lagrangian summand through
$c(\cA)$, which determines the twist operator
dimension.
The modular characteristic~$\kappa(\cA)$ controls the genus-$1$
obstruction; the ratio
$c/\kappa$ is family-dependent (equal to~$2$ for Virasoro but not in general).
The Verdier involution $\sigma$
(Theorem~\ref{thm:thqg-g4-s-duality})
exchanges the two summands, enforcing~\eqref{eq:ent-complementarity-sum}.
\end{remark}

% ======================================================================
%
% 3. SHADOW CORRECTIONS AND ENTANGLEMENT COMPLEXITY
%
% ======================================================================
\begin{remark}[Evidence]
Part~(i) is Theorem~\ref{thm:ent-scalar-entropy}.
Part~(ii) is
Proposition~\ref{prop:ent-complexity-classification}.
 succeeded in 51ms:
entanglement programme:

\begin{center}
\renewcommand{\arraystretch}{1.4}
\small
\begin{tabular}{l@{\;\;}l@{\;\;}l@{\;\;}c}
\textbf{Algebraic object} & \textbf{Holographic role}
 & \textbf{Entanglement concept} & \textbf{Status} \\
\midrule
$Q_g(\cA) \oplus Q_g(\cA^!)$
 & Lagrangian splitting of phase space
 & dimensional Page constraint
 & \ref{thm:thqg-g3-polarization} \\
$\sigma$ (Verdier involution)
 & gravitational CPT
 & Tomita--Takesaki $J$ (structural)
 & \S\ref{subsec:thqg-entanglement-modular-flow} \\
$\langle \cdot, \cdot \rangle_g$ (Verdier pairing)
 & bulk--boundary coupling
 & duality pairing
 succeeded in 51ms:
\noindent\emph{Organization.}\;
\S\ref{V1-subsec:thqg-III-ambient-complex} constructs the ambient
complex and Verdier involution, establishing the foundational
input.
\S\ref{V1-subsec:thqg-III-eigenspace-decomposition} proves the
unconditional eigenspace decomposition~(C1) with complete detail.
\S\ref{V1-subsec:thqg-III-shifted-symplectic} develops the
shifted-symplectic structure~(C2), including a self-contained
review of PTVV geometry.
\S\ref{V1-subsec:thqg-III-complementarity-potential} constructs the
complementarity potential and identifies it with the shadow jet
expansion.
\S\ref{V1-subsec:thqg-III-holographic-entanglement} gives the
holographic interpretation at genus~$1$ and the BTZ connection.
\S\ref{V1-subsec:thqg-III-standard-landscape} verifies all structures
across the standard landscape.

% ======================================================================
%
\ClaimStatusProvedHere]


thinking
**Considering reference migration**

I’m looking at the Vol2 file and noticing it uses V1 aliases, but the current V1 build doesn't have those labels. I think the entanglement program could use plain text references to Volume II sections instead. I might need to replace numeric references with textual names plus "Volume II," like updating theorems with actual titles. I'll search orphaned sources and audit notes to find exact titles. It could help to check for relevant comments in Volume II as I go along.
thinking
**Searching for file context**

I see that the user needs grounding in the actual file contents. The Markdown in the repo can count as that, even though its truth hierarchy is lower than .tex files. If a source theorem is removed from the .tex and only appears in audit notes, we could still cite it as it existed. However, it might be better to use a minimal textual description if the theorem title isn't available. I should search for labels and titles in the `fix_wave_B` or relaunch notes to find what I need.
codex
The harder cases are the migrated THQG surfaces: several refs in `entanglement_*` and `heisenberg_eisenstein.tex` target theorem labels that are not in the compiled Volume I tree at all. I’m reading the surviving chapter text and the migration traces together so the fixes don’t paper over missing content with bogus alias labels.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
labels=['thm:thqg-g3-polarization','thm:thqg-g4-s-duality','thm:thqg-g5-yangian','thm:thqg-g6-soft-graviton','thm:thqg-III-genus-1-holographic','thm:thqg-III-eigenspace-decomposition','cor:thqg-III-dimension-parity','subsec:thqg-III-shifted-symplectic','cor:thqg-III-complementarity-exchange','prop:thqg-V-c13-self-duality','thm:thqg-V-collision-twisting','thm:thqg-I-determinant-formula','cor:thqg-I-heisenberg-selberg','lem:thqg-X-composition-decay','prop:thqg-X-second-quantization','thm:thqg-X-heisenberg-sewing-full','rem:thqg-X-pants-independence','sec:thqg-soft-graviton-theorems']
for label in labels:
    print('===',label,'===')
    for path in Path('/Users/raeez/chiral-bar-cobar').rglob('*.md'):
        try:
            txt = path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if label in txt:
            for i,line in enumerate(txt.splitlines(),1):
                if label in line:
                    print(f'{path.relative_to(Path(\"/Users/raeez/chiral-bar-cobar\"))}:{i}:{line[:220]}')
                    break
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 14.56s:
=== thm:thqg-g3-polarization ===
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:17741:\label{thm:thqg-g3-polarization}
wave2_audit_20260413_001942/B03_thm_C_bridge.md:656:% label removed: thm:thqg-g3-polarization
wave2_audit_20260413_001942/U06_incomplete_proofs_v1.md:3:- [CRITICAL] `chapters/connections/twisted_holography_quantum_gravity.tex:119` — PROBLEM: `thm:thqg-g1-finiteness`, `thm:thqg-g2-complexity`, `thm:thqg-g3-polarization`, `thm:thqg-g4-s-duality`, `thm:thqg-g5-yangian`, `t
.claude/worktrees/agent-a2a46b8f/metadata/theorem_registry.md:2683:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a40a6cef/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-ab23aca7/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-aabeb66e/metadata/theorem_registry.md:2945:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-ac37cca2/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a4185af5/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a8ce0852/metadata/theorem_registry.md:2945:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a8c93d3b/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a7665bc4/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-ad458643/metadata/theorem_registry.md:2945:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-afd71b6b/metadata/theorem_registry.md:2945:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-ab5ce347/metadata/theorem_registry.md:2945:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a92c8d2b/metadata/theorem_registry.md:2683:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-aed0ee9b/metadata/theorem_registry.md:2683:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a1766399/metadata/theorem_registry.md:2945:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
.claude/worktrees/agent-a95c75a4/metadata/theorem_registry.md:2701:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |

thinking
**Considering citation replacements**

I think I can replace the status entry `\ref{thm:thqg-g3-polarization}` with a more descriptive citation: `Volume II, G3 "Symplectic polarization"`. But maybe I can simplify it even further by just saying: `Volume II, G3 ("Symplectic polarization")`. This aligns well with the metadata snapshot. I might need to verify similar titles for G4, G5, and G6 using the theorem registry snapshot. Perhaps I should query the archive for all the titles related to these labels.
exec
/bin/zsh -lc "rg -n '\\| "'`(thm:thqg-g3-polarization|thm:thqg-g4-s-duality|thm:thqg-g5-yangian|thm:thqg-g6-soft-graviton|thm:thqg-III-genus-1-holographic|thm:thqg-III-eigenspace-decomposition|cor:thqg-III-dimension-parity|cor:thqg-III-complementarity-exchange|prop:thqg-V-c13-self-duality|thm:thqg-V-collision-twisting|thm:thqg-I-determinant-formula|cor:thqg-I-heisenberg-selberg|lem:thqg-X-composition-decay|prop:thqg-X-second-quantization|thm:thqg-X-heisenberg-sewing-full|rem:thqg-X-pants-independence|sec:thqg-soft-graviton-theorems)`'"' archive/metadata/theorem_registry.md metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
archive/metadata/theorem_registry.md:2092:| `lem:thqg-X-composition-decay` | `lemma` | 444 | Exponential decay of composition coefficients |
archive/metadata/theorem_registry.md:2093:| `prop:thqg-X-second-quantization` | `proposition` | 482 | Second quantization |
archive/metadata/theorem_registry.md:2094:| `thm:thqg-X-heisenberg-sewing-full` | `theorem` | 562 | Heisenberg sewing theorem: full development |
archive/metadata/theorem_registry.md:2223:| `thm:thqg-V-collision-twisting` | `theorem` | 576 | Collision residue = twisting morphism, revisited |
archive/metadata/theorem_registry.md:2241:| `prop:thqg-V-c13-self-duality` | `proposition` | 1990 | Self-duality of the gravitational Yangian at $c = 13$ |
archive/metadata/theorem_registry.md:2362:| `cor:thqg-I-heisenberg-selberg` | `corollary` | 1685 | Heisenberg partition function via Selberg zeta |
archive/metadata/theorem_registry.md:2409:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 472 | Holographic eigenspace decomposition (C1) |
archive/metadata/theorem_registry.md:2410:| `cor:thqg-III-complementarity-exchange` | `corollary` | 653 | Complementarity exchange principle |
archive/metadata/theorem_registry.md:2411:| `cor:thqg-III-dimension-parity` | `corollary` | 676 | Dimension parity |
archive/metadata/theorem_registry.md:2415:| `thm:thqg-III-genus-1-holographic` | `theorem` | 1435 | Holographic complementarity at genus $1$ |
archive/metadata/theorem_registry.md:2427:| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
archive/metadata/theorem_registry.md:2428:| `thm:thqg-g4-s-duality` | `theorem` | 161 | \textbf{G4}: Gravitational $S$-duality |
archive/metadata/theorem_registry.md:2429:| `thm:thqg-g5-yangian` | `theorem` | 173 | \textbf{G5}: Gravitational Yangian |
archive/metadata/theorem_registry.md:2430:| `thm:thqg-g6-soft-graviton` | `theorem` | 183 | \textbf{G6}: Soft graviton theorems |

thinking
**Searching for titles**

I need to find titles for the subsections `subsec:thqg-III-shifted-symplectic` and `sec:thqg-soft-graviton-theorems`. It seems like I may have to check orphaned markdown or archive metadata since it doesn't include the subsections. I could use fix_wave_B or maybe relaunch the search. I’m curious to see if that yields the information I need! It’s all about ensuring I get the right titles. Let’s get this organized!
exec
/bin/zsh -lc "rg -n 'subsec:thqg-III-shifted-symplectic|sec:thqg-soft-graviton-theorems' fix_wave_B_20260413_171623/B11_orphaned_chapters.md archive/metadata/theorem_registry.md relaunch_20260413_111534/F17_dangling_refs_v1.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:18159:\S\ref{subsec:thqg-III-shifted-symplectic} develops the
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:19059:\label{subsec:thqg-III-shifted-symplectic}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:20368: (\S\ref{subsec:thqg-III-shifted-symplectic}).
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:41253:\label{sec:thqg-soft-graviton-theorems}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:73785:-\label{sec:thqg-soft-graviton-theorems}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:76143:-\S\ref{subsec:thqg-III-shifted-symplectic} develops the
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:77043:-\label{subsec:thqg-III-shifted-symplectic}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:78352:- (\S\ref{subsec:thqg-III-shifted-symplectic}).
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:115122:-\label{sec:thqg-soft-graviton-theorems}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:117480:-\S\ref{subsec:thqg-III-shifted-symplectic} develops the
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:118380:-\label{subsec:thqg-III-shifted-symplectic}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:119689:- (\S\ref{subsec:thqg-III-shifted-symplectic}).
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:156478:-\label{sec:thqg-soft-graviton-theorems}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:158836:-\S\ref{subsec:thqg-III-shifted-symplectic} develops the
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:159736:-\label{subsec:thqg-III-shifted-symplectic}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:161045:- (\S\ref{subsec:thqg-III-shifted-symplectic}).
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:197859:-\label{sec:thqg-soft-graviton-theorems}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:200217:-\S\ref{subsec:thqg-III-shifted-symplectic} develops the
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:201117:-\label{subsec:thqg-III-shifted-symplectic}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:202426:- (\S\ref{subsec:thqg-III-shifted-symplectic}).
exec
/bin/zsh -lc "sed -n '19048,19072p' fix_wave_B_20260413_171623/B11_orphaned_chapters.md
sed -n '41240,41262p' fix_wave_B_20260413_171623/B11_orphaned_chapters.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
class $\lambda_1$ parametrizing the curvature of the
genus-$1$ structure).
\end{remark}

% ======================================================================
%
% 3. SHIFTED-SYMPLECTIC STRUCTURE (C2)
%
% ======================================================================

\subsection{The shifted-symplectic structure}
\label{subsec:thqg-III-shifted-symplectic}
\index{shifted symplectic!structure!holographic|textbf}
\index{PTVV!holographic application}

The unconditional decomposition~(C1) is an eigenspace statement.
The conditional upgrade~(C2) endows the ambient complex with a
$(-1)$-shifted symplectic structure in the sense of
Pantev--To\"{e}n--Vaqui\'{e}--Vezzosi \cite{PTVV13}, making
$Q_g(\cA)$ and $Q_g(\cA^!)$ complementary Lagrangians in the

thinking
**Planning title revisions**

I’m working on some title text, specifically “the shifted-symplectic structure” and “the soft graviton theorems from the shadow obstruction tower.” I might consider fixing them to plain text or using Volume II textual citations if they’re relevant. Additionally, I should search for titles related to `thm:hook-type-transport-koszul-duality`. I also need to look into the actual local theorem context for `thm:hook-transport-corridor` to get more details.
exec
/bin/zsh -lc "sed -n '220,238p' chapters/connections/subregular_hook_frontier.tex
sed -n '270,282p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
reduction or inverse-reduction functors between the corresponding
type-$A$ affine $\mathcal{W}$-algebras at generic level.
The \emph{hook vertices} are the partitions of hook type
$(N-r, 1^r)$, $0 \leq r \leq N-1$.
The \emph{transport-closure} of a set $S$ of vertices is the set
of all vertices reachable from $S$ by paths in $\Gamma_N$.
\end{definition}

\begin{theorem}[Hook-type transport corridor under DS--bar compatibility; \ClaimStatusConditional]
\label{thm:hook-transport-corridor}
\index{W-algebra@$\mathcal{W}$-algebra!hook transport corridor}
Assume that, at generic level, bar--cobar/Koszul duality intertwines
with the reduction and inverse-reduction functors along the hook
network in type~$A$. Then for every hook partition
$\eta = (N-r, 1^r)$ in $\mathfrak{sl}_N$:
\[
\mathcal{W}^k(\mathfrak{sl}_N, f_\eta)^!
\;\simeq\;
\mathcal{W}^{-k-2N}(\mathfrak{sl}_N, f_{\eta^t}).
chain-level BV/BRST/bar identification.

thinking
**Investigating search results**

I’m looking at the search results from F17, which also appear in some other sections. I’m wondering if those are included in the main compiled document and why my script didn't flag them. I suspect that the `thm:dnp-bar-cobar-identification` might be in the current compiled tree due to a phantom label. However, my script indicated that the only dangling references were in yangians_foundations. I’ll need to check actual occurrences to clarify this.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{thm:dnp-bar-cobar-identification\\}' chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_foundations.tex:1347:(The complete identification of DNP's line-operator package with the bar-cobar twisting package is Theorem~\ref{thm:dnp-bar-cobar-identification} in Vol~II.)
exec
/bin/zsh -lc "sed -n '308,325p' chapters/connections/editorial_constitution.tex
sed -n '1804,1816p' chapters/examples/free_fields.tex
sed -n '2678,2690p' chapters/examples/free_fields.tex
sed -n '52,64p' chapters/examples/yangians_drinfeld_kohno.tex
sed -n '4928,4940p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The conformal weight filtration offers a path: it decomposes the problem
into countably many finite-dimensional strata, each resolved by the
sectorwise spectral-sequence convergence of
Theorem~\ref{thm:sectorwise-spectral-convergence}, with Efimov-type
categorical formal completion assembling the answer via the
pro-Weyl--Mittag-Leffler tower.
\end{remark}

\begin{conjecture}[H-level target identification for standard infinite towers]
\label{conj:v1-master-infinite-generator}
\ClaimStatusConjectured{}
The structural completion framework is \textbf{proved}
(Theorem~\ref{thm:completed-bar-cobar-strong}): the completed
bar-cobar round-trip is a quasi-isomorphism on
$\CompCl(\Fft)$, and the coefficient-stability criterion
(Theorem~\ref{thm:coefficient-stability-criterion}) reduces
convergence to finite-window matrix stabilization. What remains
is the \textbf{H-level target identification}: construct a
\end{itemize}
satisfying anticommutation relations:

thinking
**Evaluating references in text**

I'm noticing that in four locations, the text isn't load-bearing. They currently use `Conjecture\ref{conj:v1-master-infinite-generator}`, which I could suggest replacing with `the H-level target-identification conjecture`. That feels like a straightforward fix. But there's also the main phantom reference `conj:master-infinite-generator`. It's possible they intended to use an alias but forgot the v1 prefix? I should check if there are compiled references for `conj:master-infinite-generator`.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{conj:master-infinite-generator\\}' chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/coderived_models.tex:424:Conjecture~\textup{\ref{conj:master-infinite-generator}} \textup{(MC4: proved; residual H-level comparison).}
chapters/theory/higher_genus_modular_koszul.tex:912:(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
chapters/theory/chiral_modules.tex:2002:(Conjecture~\ref{conj:master-infinite-generator};
chapters/theory/chiral_koszul_pairs.tex:6322:Conjecture~\ref{conj:master-infinite-generator}, not to the standard
exec
/bin/zsh -lc "sed -n '5288,5304p' chapters/connections/frontier_modular_holography_platonic.tex
rg -n 'chromatic-(shadow|tower)-correspondence|chromatic tower|chromatic shadow' chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The shadow tower $\Theta_\cA \in \MC(\fg^{\mathrm{mod}}_\cA)$
encodes genus-by-genus obstruction data beyond $\kappa$.
At genus~$1$, the curvature $\kappa \cdot \omega_1$ governs the
$E_2^*$-quasi-modular generating function; at genus~$2$,
the three-shell structure introduces corrections
$\delta F_2^{\mathrm{cross}}$ (all-weight) that depend on the full
cubic shadow~$S_3$. These higher-genus shells carry information
invisible to the rational projection. The chromatic-shadow
correspondence
(Remark~\ref{rem:chromatic-shadow-correspondence})
identifies the genus-$n$ shell of the shadow tower with the
$E(n)$-localization in stable homotopy. Under this identification:
\begin{enumerate}[label=\textup{(\roman*)}]
\item Height $0$ (rational):
 $\kappa(\cA)$, the degree-$2$ scalar shadow: in abelian and scalar
 families $\kappa(\cA)=\mathrm{av}(r(z))$, while for non-abelian
chapters/connections/concordance.tex:7789:\label{rem:chromatic-shadow-correspondence}
chapters/connections/concordance.tex:7803:The height-$n$ differential $\mathrm{Ob}_n$ in the genus spectral sequence would correspond to the chromatic boundary map $L_{E(n)}S \to L_{E(n-1)}S$ in the chromatic tower. In Chriss--Ginzburg terms: the chromatic filtration on the spectral Steinberg object should be the image, under a conjectural realization functor, of the genus filtration on $\MC(\fg^{\mathrm{mod}}_\cA)$. This correspondence is purely structural: no computation beyond $n = 1$ has been verified.
chapters/connections/concordance.tex:9852: \textup{(}Remark~\ref{rem:chromatic-shadow-correspondence}\textup{)} \\[4pt]
exec
/bin/zsh -lc "sed -n '6908,6935p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\Etwo$-oriented spectrum map from the bar complex of $\cA_E$ to
 the topological modular forms spectrum, in the sense of
 Ando--Hopkins--Strickland~\cite{AHS01}, and verifying that the
 chiral Koszul dual $\cA_E^!$ implements the TMF-dualizing
 structure. A proof of~\textup{(c)} would imply the elliptic
 Yangian of $\cA_E$ is TMF-oriented.
\end{enumerate}
\end{conjecture}

\begin{remark}[Chromatic tower and the Yangian hierarchy]
\label{rem:chromatic-tower-correspondence}
\index{chromatic tower!Yangian correspondence|textbf}
\index{Yangian!chromatic duality|textbf}
The chromatic filtration of stable homotopy theory
\textup{(}Ravenel~\cite{Ravenel86}\textup{)} stratifies spectra by
the height of the associated formal group: height~$0$ is rational,
height~$1$ is $K$-theory, height~$2$ is TMF, and so on. The
representation-theoretic tower rational $\to$ trigonometric $\to$
elliptic of Yangian-type quantum groups stratifies chiral algebras
by the formal group of the underlying curve:


thinking
**Considering terminology fixes**

I'm evaluating the relationship between "chromatic-shadow correspondence" and the concept of "chromatic-tower correspondence." I think it might be appropriate to reference the latter instead. The current note about shadow tower shell and E(n)-localization feels different from what's needed. If the user wants a precise adjustment, replacing the reference sounds reasonable, but we might still need to ensure semantic accuracy. If they’re looking for an audit, I should be careful not to alter the original meaning in the notes.
thinking
**Finding the right fix**

I'm considering how to address the necessary adjustments. I might need to either restore `chapters/connections/concordance.tex` or replace the citation with a pointer to the chromatic-tower remark. A precise fix is important here. I’ll need to look into the contexts of `thm:thqg-I-determinant-formula` and `cor:thqg-I-heisenberg-selberg`. I also want to check for equivalent theorems in `genus_complete` and examine the relevant lines in the archive metadata to ensure everything aligns correctly.
exec
/bin/zsh -lc "sed -n '1532,1552p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{equation}
where $Z_{\mathrm{Sel}}(s;\Sigma_g)
= \prod_{\gamma\, \text{prim.}} \prod_{n=0}^\infty
(1 - e^{-(s+n)\ell(\gamma)})$
is the Selberg zeta function, the product running
over primitive closed geodesics, and $c_g$ is a genus-dependent
spectral constant
\textup{(}Theorem~\ref{thm:thqg-I-determinant-formula}\textup{)}.
The Heisenberg partition function factorizes as
\begin{equation}\label{eq:heisenberg-selberg}
Z_g(\cH_\kappa;\Sigma_g)
= \bigl(\det\operatorname{Im}\Omega\bigr)^{-\kappa/2}
\cdot Z_{\mathrm{Sel}}(1;\Sigma_g)^{-\kappa/2}
\cdot e^{-\kappa c_g/2},
\end{equation}
where $\Omega$ is the period matrix of~$\Sigma_g$
\textup{(}Corollary~\ref{cor:thqg-I-heisenberg-selberg}\textup{)}.
The Mumford isomorphism
$\lambda = c_1(\det\mathbb{E})$ combined with the
Belavin--Knizhnik formula~\cite{BK86} gives
exec
/bin/zsh -lc "rg -n 'Selberg zeta|heisenberg-selberg|determinant formula|spectral constant c_g|c_g' chapters/examples/heisenberg_eisenstein.tex chapters/connections/genus_complete.tex chapters/connections/bv_brst.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:1499:class is $\kappa(\cH_\kappa)\cdot c_g(\mathbb{E})
chapters/connections/bv_brst.tex:1524:\noindent\textbf{Path \textup{(b)}: Selberg zeta function.}
chapters/connections/bv_brst.tex:1525:\index{Selberg zeta function!BV/bar proof|(}
chapters/connections/bv_brst.tex:1526:The D'Hoker--Phong determinant formula~\cite{DP86} expresses
chapters/connections/bv_brst.tex:1531:= Z_{\mathrm{Sel}}(1;\Sigma_g)\cdot e^{c_g},
chapters/connections/bv_brst.tex:1536:is the Selberg zeta function, the product running
chapters/connections/bv_brst.tex:1537:over primitive closed geodesics, and $c_g$ is a genus-dependent
chapters/connections/bv_brst.tex:1541:\begin{equation}\label{eq:heisenberg-selberg}
chapters/connections/bv_brst.tex:1545:\cdot e^{-\kappa c_g/2},
chapters/connections/bv_brst.tex:1548:\textup{(}Corollary~\ref{cor:thqg-I-heisenberg-selberg}\textup{)}.
chapters/connections/bv_brst.tex:1553:$\mathcal{M}_g$, so that the variation of~\eqref{eq:heisenberg-selberg}
chapters/connections/bv_brst.tex:1560:\index{Selberg zeta function!BV/bar proof|)}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:949:The Heisenberg algebra is the archetype: Gaussian shadow depth ($r_{\max} = 2$), closed-form solvability via second quantization, and explicit Fredholm determinant formulas at all genera.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:990:\subsubsection{The Fredholm determinant formula}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2578:\subsection{Spectral determinants and the Selberg zeta function}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2580:\index{Selberg zeta function|textbf}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2583:The Fredholm determinant formula for the Heisenberg partition function connects to deeper spectral theory through the Selberg zeta function. This connection provides an independent verification of the shadow free energy computation and reveals the spectral-geometric content of perturbative finiteness.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2585:\subsubsection{The Selberg zeta function}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2587:\begin{definition}[Selberg zeta function]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2589:\index{Selberg zeta function!definition}

thinking
**Searching for theorem references**

I'm thinking about how the current volume might not have the theorem or corollary, but it references BV/BRST. Since Volume II includes them, I might need to replace mentions with text cross-volume citations like the "D'Hoker–Phong determinant formula" and the corollary regarding the "Heisenberg partition function via Selberg zeta." I should also look for a theorem title for the determinant formula using archive metadata. Time to search for that!
exec
/bin/zsh -lc "rg -n '"'`thm:thqg-I-determinant-formula`|thqg-I-determinant-formula'"' archive/metadata/theorem_registry.md fix_wave_B_20260413_171623/B11_orphaned_chapters.md /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2598:% label removed: thm:thqg-I-determinant-formula
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2630:Substitute the determinant formula (Theorem~\ref{V1-thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{V1-thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:36300:\label{thm:thqg-I-determinant-formula}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:36332:Substitute the determinant formula (Theorem~\ref{thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:71280:-\label{thm:thqg-I-determinant-formula}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:71312:-Substitute the determinant formula (Theorem~\ref{thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:112617:-\label{thm:thqg-I-determinant-formula}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:112649:-Substitute the determinant formula (Theorem~\ref{thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:153973:-\label{thm:thqg-I-determinant-formula}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:154005:-Substitute the determinant formula (Theorem~\ref{thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:195354:-\label{thm:thqg-I-determinant-formula}
fix_wave_B_20260413_171623/B11_orphaned_chapters.md:195386:-Substitute the determinant formula (Theorem~\ref{thm:thqg-I-determinant-formula}) into the Heisenberg partition function (Theorem~\ref{thm:thqg-I-heisenberg-partition}). The Selberg expansion follows from $\log\prod_k (1-x q^k) = -\sum_{m=1}^\infty \frac{x^m}{m(1-q^m)}$ with $x = e^{-\ell_\gamma}$ and $q = e^{-\ell_\gamma}$.

thinking
**Searching for theorem title**

I need to find the title for the theorem. Maybe I can use archive metadata that wasn’t included earlier. I should search around line 2362, though it might not show because of our targeted label. Wait, maybe line 2360 is the one I need to focus on. I’ll check line 2362 in the archive for correlation. Let's also try searching for "determinant formula" to see if that helps!
exec
/bin/zsh -lc "rg -n 'determinant formula|Heisenberg partition function via Selberg zeta' archive/metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2362:| `cor:thqg-I-heisenberg-selberg` | `corollary` | 1685 | Heisenberg partition function via Selberg zeta |
exec
/bin/zsh -lc "sed -n '36292,36318p' fix_wave_B_20260413_171623/B11_orphaned_chapters.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For a compact hyperbolic surface $\Sigma_g$ of genus $g \geq 2$ with primitive closed geodesics $\{\gamma\}$ of lengths $\{\ell_\gamma\}$, the Selberg zeta function is
\begin{equation}\label{eq:thqg-I-selberg-def}
Z_{\mathrm{Sel}}(s;\,\Sigma_g) \;:=\; \prod_{\gamma \in \mathcal{P}} \prod_{k=0}^{\infty} \bigl(1 - e^{-(s+k)\ell_\gamma}\bigr),
\end{equation}
where $\mathcal{P}$ is the set of primitive closed geodesics on $\Sigma_g$. The product converges absolutely for $\Re(s) > 1$ and extends meromorphically to $\mathbb{C}$.
\end{definition}

\begin{theorem}[Determinant formula; \ClaimStatusProvedElsewhere]
\label{thm:thqg-I-determinant-formula}
\index{Selberg zeta function!determinant formula}
The zeta-regularized determinant of the Laplacian on $\Sigma_g$ is related to the Selberg zeta function by
\begin{equation}\label{eq:thqg-I-det-selberg}
\det{}'_\zeta \Delta_{\Sigma_g} \;=\; Z_{\mathrm{Sel}}(1;\,\Sigma_g) \cdot e^{c_g},
\end{equation}
where $c_g$ is a topological constant depending only on $g$ (not on the hyperbolic metric):
\begin{equation}\label{eq:thqg-I-topological-constant}
c_g \;=\; (2g - 2) \cdot \left( \log(2\pi) - \tfrac{1}{2} \right) + \log\mathrm{vol}(\Sigma_g) + \text{spectral invariants}.
\end{equation}
This is the D'Hoker--Phong formula~\cite{DP86}, building on the Selberg trace formula.
\end{theorem}
exec
/bin/zsh -lc "sed -n '25642,25818p' fix_wave_B_20260413_171623/B11_orphaned_chapters.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
where the product is over the $3g-3$ internal sewing circles
of a genus-$g$ surface without punctures.
More precisely, $\sewker_g$ acts on the tensor product of
$g$ copies of $A^2(D)$ (one for each handle),
with each $\sewop_{q_\alpha}$ acting on the appropriate
tensor factor.
\end{definition}

\begin{remark}[Dependence on pants decomposition]%
\label{rem:thqg-X-pants-independence}%
\index{pants decomposition!independence}%
The Fredholm determinant $\det(1 - \sewker_g)$ is independent
of the choice of pair-of-pants decomposition, although the
intermediate operator $\sewker_g$ depends on the decomposition.
This independence follows from the sewing axiom of the
chain-level modular-functor package
(Theorem~\ref{thm:chain-modular-functor}\,(iv)):
different decompositions are related by chain homotopies
that preserve the trace.
\end{remark}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:chain-modular-functor\\}|pants decomposition' chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:1777: \phantomsection\label{thm:chain-modular-functor}%
chapters/examples/heisenberg_eisenstein.tex:2399:\sum_{\text{pants decompositions}}
chapters/examples/heisenberg_eisenstein.tex:2417:Laplacian determinant. (The summation over pants decompositions
chapters/examples/kac_moody.tex:4484:In genus~$0$, the pants decomposition of
chapters/connections/genus_complete.tex:290:\ClaimStatusProvedHere]\label{thm:chain-modular-functor}
chapters/theory/chiral_modules.tex:1011:blocks along a pants decomposition. Since part~(i) identifies the
chapters/theory/chiral_modules.tex:5158:$F_\mu$. In the genus-$0$ fusion (pants decomposition of
chapters/theory/higher_genus_complementarity.tex:4548:\index{pants decomposition}
chapters/theory/higher_genus_complementarity.tex:4551:\cdots \cup_{\gamma_{2g-3}} P_{2g-2}$ be a pants decomposition,
chapters/theory/higher_genus_complementarity.tex:4675:(ii)~Mayer--Vietoris is functorial in the pants decomposition;
chapters/theory/higher_genus_complementarity.tex:4737:Different presentations (SDR choices, pants decompositions) produce
exec
/bin/zsh -lc "sed -n '676,820p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{theorem}[Heisenberg at general genus; \ClaimStatusProvedHere]\label{thm:heisenberg-all-genus}
For genus $g$, the Heisenberg two-point function is \emph{exact} (no perturbative expansion):
\begin{equation}
\langle a(z_1) a(z_2) \rangle_{\Sigma_g} = \kappa \cdot G_{\Omega_g}(z_1, z_2)
\end{equation}
where $G_{\Omega_g}$ is the genus-$g$ Green function constructed from the prime form $E(z_1, z_2; \Omega_g)$ and the period matrix $\Omega_g \in \mathcal{H}_g$.

The geometry of $\Sigma_g$ enters through $G_{\Omega_g}$, whose Laurent expansion near $z_1 = z_2$ takes the form:
\begin{align}
g=0: \quad & G(z_1, z_2) = \frac{1}{z_1 - z_2} \quad \text{(chiral propagator)} \\
g=1: \quad & G_\tau(z_1, z_2) = \zeta_\tau(z_1-z_2) - \frac{\pi^2 E_2(\tau)}{3}\,(z_1-z_2) \\
g \geq 2: \quad & G_{\Omega_g}(z_1, z_2) = \frac{1}{z_1-z_2} + \sum_{k \geq 0} c_k(\Omega_g)(z_1-z_2)^k \quad \text{(chiral propagator $\partial_z \log E(z_1,z_2)$)}
\end{align}
The Eisenstein series and Siegel modular forms appear as \emph{coefficients of the Green function expansion}, encoding the moduli dependence, not as quantum corrections to a perturbative series. The Heisenberg algebra is free: there are no loop corrections.
\end{theorem}

\begin{proof}
The Heisenberg algebra is a free (Gaussian) theory: Wick's theorem
reduces all correlation functions to products of two-point functions.
Therefore the genus-$g$ two-point function is exactly the Green function

thinking
**Inspecting entanglement program**

I need to check the `thqg_entanglement_program` because some references might be missing. It's possible that current volumes already have results that could relate to this. I should search for `thm:quantum-complementarity-main` as well. Looking at line 168, it defines `C_g` and references `thm:thqg-III-eigenspace-decomposition` for Lagrangian decomposition. This theorem might be missing, but it seems equivalent to `thm:quantum-complementarity-main`. The `Q_g(\cA) \oplus Q_g(\cA^!)` decomposition looks like it's the main complementarity theorem C1.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|thm:fiber-center-identification|thm:modular-characteristic)\\}' chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2848:\label{thm:modular-characteristic}
chapters/theory/higher_genus_complementarity.tex:375:\label{thm:fiber-center-identification}
chapters/theory/higher_genus_complementarity.tex:527:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:1995:\label{thm:shifted-symplectic-complementarity}
exec
/bin/zsh -lc "sed -n '520,620p' chapters/theory/higher_genus_complementarity.tex
sed -n '1988,2028p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{remark}

The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
exec
/bin/zsh -lc "rg -n 'shifted symplectic complementarity|\\\\label\\{sec:shifted-symplectic-complementarity\\}|\\\\label\\{subsec:thqg-III-shifted-symplectic\\}' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1908:\label{sec:shifted-symplectic-complementarity}
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:yangian-e1|thm:chiral-yangian|thm:yangian-sklyanin-quantization|thm:yangian-koszul-dual|thm:e1-chiral-koszul-duality)\\}' chapters/examples chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/frontier_modular_holography_platonic.tex:1673:\label{thm:yangian-sklyanin-quantization}
chapters/examples/yangians_foundations.tex:363:\begin{theorem}[Yangian as \texorpdfstring{$\Eone$}{E1}-chiral; \ClaimStatusProvedHere]\label{thm:yangian-e1}
chapters/examples/yangians_foundations.tex:502:\begin{theorem}[Yangian Koszul dual; \ClaimStatusProvedHere]\label{thm:yangian-koszul-dual}
chapters/theory/chiral_koszul_pairs.tex:5429:\label{thm:e1-chiral-koszul-duality}
chapters/theory/koszul_pair_structure.tex:1047:\label{thm:chiral-yangian}

thinking
**Investigating Yangians in entanglement**

I'm trying to figure out which theorem relates to "Gravitational Yangian" in the context of entanglement. It could be local theorems like `thm:yangian-e1` or `thm:chiral-yangian`. But given the bar-cobar encoding and dual algebra `\cA^!`, I might need to consider `e1-chiral-koszul-duality` or potentially `chiral-yangian`. I should check proof lines around 623 to get more context, especially regarding `thm:thqg-g5-yangian` and `thm:thqg-entanglement-qec`.
exec
/bin/zsh -lc "sed -n '596,630p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Encoding.}
 $B \colon \cA \to B(\cA)$:
 the ``logical'' algebra $\cA$ is mapped into the
 bar coalgebra $B(\cA)$.

\item \emph{Decoding.}
 $\Omega \colon B(\cA) \to \Omega(B(\cA))$:
 the cobar construction provides recovery.

\item \emph{Exact inversion on the Koszul locus.}
 Theorem~B gives $\Omega(B(\cA)) \xrightarrow{\sim} \cA$:
 the recovery map is a quasi-isomorphism, recovering $\cA$
 exactly from $B(\cA)$.

\item \emph{Dual algebra.}
 $\cA^! = (H^*(B(\cA)))^\vee$: the Koszul dual is
 the cohomology of the bar complex, dualized.
 The line-operator category
 $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$.
exec
/bin/zsh -lc "sed -n '1038,1075p' chapters/theory/koszul_pair_structure.tex
sed -n '355,380p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\emph{Locality}: The OPE has poles of order at most~2, ensuring $(z-w)^2 J^a(z)J^b(w) = (z-w)^2 J^b(w)J^a(z)$.

\emph{Associativity}: The Jacobi identity for triple OPEs follows from the Lie algebra Jacobi identity for $\mathfrak{g}$ and the cocycle condition for the central extension.

\emph{Translation covariance}: The $\mathcal{D}_X$-module structure provides the $\partial_z$-action on all fields via $\partial_z J^a(z) = [L_{-1}, J^a(z)]$, where $L_{-1}$ is the infinitesimal translation on~$X$ (part of the intrinsic $\mathcal{D}_X$-module structure, independent of the Sugawara construction). \qedhere
\end{proof}

\begin{theorem}[Kazhdan--Lusztig equivalence at critical level {\cite{KL93,Feigin-Frenkel}}; \ClaimStatusProvedElsewhere]
\label{thm:chiral-yangian}
The Yangian $Y(\mathfrak{g})$ arises as a deformation of $U(\mathfrak{g}[t])$ and is related to the affine Kac--Moody chiral algebra $\hat{\mathfrak{g}}_\kappa$ (Theorem~\ref{thm:chiral-yangian-km}) via the Kazhdan--Lusztig equivalence: at the critical level $\kappa = -h^\vee$, the category of smooth $\hat{\mathfrak{g}}_{-h^\vee}$-modules with regular singularities is related to $Y(\mathfrak{g})$-modules via the center $Z(\hat{\mathfrak{g}}_{-h^\vee}) \cong \mathrm{Fun}(\mathrm{Op}_{\mathfrak{g}^\vee})$ (Feigin--Frenkel~\cite{Feigin-Frenkel}, Kazhdan--Lusztig~\cite{KL93}).
\end{theorem}

\subsection{Bar complex of the Yangian}

\begin{theorem}[Bar complex structure; \ClaimStatusProvedHere]
\label{thm:yangian-bar-complex-structure}
The bar complex of the chiral Yangian is:
\[
\bar{B}^n(Y(\mathfrak{g})) = \Gamma\left(\overline{C}_n(\mathbb{P}^1), Y(\mathfrak{g})^{\boxtimes n} \otimes \Omega^n_{\log}\right)
exec
/bin/zsh -lc "rg -n '\\\\label\\{(prop:c13-full-self-duality|prop:bp-self-duality|thm:central-charge-complementarity|prop:self-duality-c13|rem:lattice:self-duality)\\}' chapters main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/lattice_foundations.tex:1033:\label{rem:lattice:self-duality}
chapters/examples/bershadsky_polyakov.tex:196:\label{prop:bp-self-duality}
chapters/theory/higher_genus_modular_koszul.tex:27801:\label{prop:c13-full-self-duality}
chapters/theory/introduction.tex:1018:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
exec
/bin/zsh -lc "sed -n '27790,27812p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
irreducibility of~$Q_L$ forces the shadow generating
function $H(t) = t^2\sqrt{Q_L(t)}$ to have finite radius
of convergence (Theorem~\ref{thm:riccati-algebraicity}).
The two analytic behaviours coexist because they probe
different directions of the double series: the genus
direction $\hbar \to 0$ at fixed degree, and the degree
direction $t \to \infty$ at fixed genus.
\end{observation}

\begin{proposition}[Full tower self-duality at $c = 13$;
\ClaimStatusProvedHere]
\label{prop:c13-full-self-duality}
\index{Virasoro algebra!self-duality at $c=13$|textbf}
\index{shadow obstruction tower!self-duality}
\index{Feigin--Frenkel involution!fixed point $c=13$}%
At the Virasoro self-dual point $c = 13$
\textup{(}the unique fixed point of the Feigin--Frenkel Koszul
involution $c \mapsto 26 - c$ on the one-parameter family
$\{\mathrm{Vir}_c\}_c$:, and with complementarity sum
$\kappa + \kappa' = 13$ on this family\textup{)}, so that

thinking
**Citing theorems and remarks**

I think I need to make sure to properly cite the remarks regarding entanglement and how they relate to specific theorems. It looks like the entanglement remark should reference `prop:c13-full-self-duality`, and similarly, I might need to connect `thm:thqg-V-collision-twisting` to a local theorem concerning collision residue and twisting morphism. I should definitely search for more details to clarify the connections.
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:collision-residue-twisting|thm:twisting-morphism-yangian|thm:gaudin-yangian-identification|thm:yangian-sklyanin-quantization)\\}' chapters/examples chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/frontier_modular_holography_platonic.tex:1631:\label{thm:gaudin-yangian-identification}
chapters/connections/frontier_modular_holography_platonic.tex:1673:\label{thm:yangian-sklyanin-quantization}
chapters/connections/frontier_modular_holography_platonic.tex:2248:\label{thm:collision-residue-twisting}
exec
/bin/zsh -lc "sed -n '2238,2260p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
At collision depth~$0$ (the open stratum $\mathcal{M}_{0,n}$), the
datum is the ``bulk'' OPE with all points spread out.
At $d = 1$ (codimension-$1$ boundary), binary collisions produce the
$r$-matrix. At $d = 2$, ternary collisions produce Yang--Baxter.
\end{remark}

\subsubsection{The collision residue theorem}

\begin{theorem}[Collision residue = universal twisting morphism;
\ClaimStatusProvedHere]
\label{thm:collision-residue-twisting}
\index{collision residue!equals twisting morphism|textbf}
\index{twisting morphism!from collision residue}
Let $\cA$ be a modular Koszul chiral algebra on a smooth projective
curve~$X$, and let
$\Theta_\cA = D_\cA - d_0 \in
\mathrm{MC}(\Defcyc(\cA) \,\widehat{\otimes}\, \mathcal{G}_{\mathrm{mod}})$
be the bar-intrinsic MC element
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}. Then:
\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Fixing references and definitions**

I need to replace `\textup{(}Corollary\ref{cor:thqg-I-heisenberg-selberg}\textup{)}` by removing it entirely since the equation stands on its own. However, the user requested a specific fix, so I could also suggest replacing it with "by substitution into the D'Hoker--Phong determinant formula." I'm leaning towards the removal for precision. I need to check the severity of certain definitions and ensure labels are consistent in the appendix, updating them as needed with the `v1` prefix for clarity.
exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:thqg-ten-theorems\\}|ten theorems|thqg ten theorems' chapters main.tex /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:635:The ten theorems below encode the gravitational content of a holographic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1111:All ten theorems \textup{(G1)--(G10)} follow from:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1247:The ten theorems arise from two independent filtration projections
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:shadow-connection|thm:shadow-connection-kz|thm:ent-scalar-entropy|prop:ent-complexity-classification)\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:18918:\label{thm:shadow-connection}
chapters/connections/frontier_modular_holography_platonic.tex:2342:\label{thm:shadow-connection-kz}
chapters/connections/entanglement_modular_koszul.tex:160:\label{thm:ent-scalar-entropy}
chapters/connections/entanglement_modular_koszul.tex:354:\label{prop:ent-complexity-classification}

thinking
**Evaluating theorem citations**

I’m considering whether `thm:shadow-connection` is sufficient for `(∇^hol)^2=0` due to flatness of the connection. It seems like line 524 in `entanglement_modular_koszul` should cite `thm:shadow-connection` instead of referencing external G6. I’ll need to take a closer look at that line to confirm my thoughts about citation accuracy. This feels like an important detail to address!
exec
/bin/zsh -lc "sed -n '520,528p' chapters/connections/entanglement_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Part~(ii) is
Proposition~\ref{prop:ent-complexity-classification}.
For part~(iii), the shadow connection
$\nabla^{\mathrm{hol}} = d - \Sh(\Theta_\cA)$ satisfies
$(\nabla^{\mathrm{hol}})^2 = 0$ (proved as Theorem~\ref{thm:thqg-g6-soft-graviton}
in~\S\ref{sec:thqg-soft-graviton-theorems}).
Its Ward identities give
$\nabla^{\mathrm{hol}}(\Sh_r) + o^{(r)} = 0$
at each degree $r \ge 3$. On the replica geometry,

thinking
**Exploring the theorem's implications**

I think the theorem titled "shadow-connection" likely supports the idea of flatness. It's worth investigating further to clarify how it proves this concept. Having a deeper understanding of the theorem and its relevance will help me convey the implications better. I’m curious to explore the details and see what they can reveal. Let's dive into the specifics and see what I can uncover!
exec
/bin/zsh -lc "sed -n '18908,18940p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For affine KM: $S_4 = 0$ and $g_{\mathrm{eff}} = 0$,
consistent with the absence of quartic interactions
(class~$\mathbf{L}$, shadow depth~$3$).
The CM integrability is a consequence of the degree-$4$
MC equation: the vanishing of the obstruction
$o_5 = 0$ for class~$\mathbf{C}$ algebras is the
Lax-pair integrability condition for the CM system.
\end{remark}

\begin{theorem}[Shadow connection]
\label{thm:shadow-connection}
\ClaimStatusProvedHere
\index{shadow connection|textbf}
\index{logarithmic connection!shadow metric}
The shadow metric $Q_L$ defines a \emph{logarithmic
connection} on the trivial line bundle
$\mathcal{O}_L$ over $L \setminus \{Q_L = 0\}$:
\begin{equation}\label{eq:shadow-connection}
 \nabla^{\mathrm{sh}}
 \;=\; d \;-\; \omega,
exec
/bin/zsh -lc "sed -n '332,342p' chapters/connections/entanglement_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
dimension.
The modular characteristic~$\kappa(\cA)$ controls the genus-$1$
obstruction; the ratio
$c/\kappa$ is family-dependent (equal to~$2$ for Virasoro but not in general).
The Verdier involution $\sigma$
(Theorem~\ref{thm:thqg-g4-s-duality})
exchanges the two summands, enforcing~\eqref{eq:ent-complementarity-sum}.
\end{remark}

% ======================================================================
%


thinking
**Finalizing findings mapping**

I need to create a final mapping for 61 findings with fixes. I think a table in the analysis would work best. I'll list unique missing labels and their proposed fixes. 

For example, I need to replace "preface 3923 conv:three-hochschild" with a warning reference and change some definitions accordingly, like "bar_construction 1523 def:conilpotent-chiral-coalgebra" to the appropriate definition label. 

I want to make sure each change is precise and consistent throughout the document.
thinking
**Updating labels and references**

I see that a compiled live label exists, so I’ll use `Conjecture\ref{conj:master-infinite-generator}`. That seems good! 

For the items in "free_fields 5099" and "5110 thm:bar-cobar-path-integral-heisenberg," I need to do more than just swap labels. I should rewrite the item and proof to properly cite the Conjecture and also downgrade its status. I want to ensure everything is accurate and reflects the necessary changes.
exec
/bin/zsh -lc "sed -n '8048,8104p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{Twisting morphism from $r_\cA(z)$.}
 The $r$-matrix determines a twisting morphism
 $\tau_r \colon \barBch(\cA) \to \cA^!$
 by extracting the degree-$2$ collision data of the
 universal MC element. This twisting morphism encodes
 the binary factorization coupling between $\barBch(\cA)$
 and~$\cA^!$
 \textup{(}Theorem~\textup{\ref{thm:thqg-V-collision-twisting}}\textup{)}.

\item \emph{Co-twisting morphism from $\{a_\lambda b\}_{\cA^!}$.}
 The $\lambda$-bracket of~$\cA^!$ determines a co-twisting
 morphism
 $\sigma_\lambda \colon \cA \to \Omegach(\barBch(\cA^!))$
 by embedding the binary OPE data of~$\cA^!$ into the
 cobar construction on the bar complex of~$\cA^!$.
 In the Koszul pair $(\cA, \cA^!)$, the Verdier intertwining
 $\mathbb{D}_{\mathrm{Ran}}(\barBch(\cA)) \simeq
 \barBch(\cA^!)$
 \textup{(}Theorem~A\textup{)} identifies
 $\barBch(\cA^!)$ with the Verdier dual of~$\barBch(\cA)$,




thinking
**Simplifying references**

I need to simplify a reference by either deleting the parenthetical note or replacing it with `Remark\ref{rem:chromatic-tower-correspondence}`. The context is about the sentence already defining the correspondence, so it's a matter of clarity. It looks like the goal is to keep the content straightforward and easily understandable while ensuring proper reference type. I'll go ahead with this edit to enhance the statement's flow.
thinking
**Analyzing citation structure**

I'm thinking about how to deal with line numbers and candidate fixes for the user. They mentioned using `file:line`, and I’m considering how to represent that. Maybe I can use something like `[file:1811]` as a separate entry. I also need to verify some existing labels in the text, like `subsec:e1-as-primitive` and several theorems, to ensure everything is correct and relevant. I’ll need to check the relevance of some theorems as well for citation purposes.
thinking
**Reviewing theorem citations**

I'm considering how the proof of the HQEC proposition relates to structural analogy and whether it’s load-bearing. It seems like a better approach would be to replace `Theorem\ref{thm:thqg-g5-yangian}` with a more precise reference to `the external G5 gravitational Yangian theorem of Volume II`. That feels accurate and straightforward. 

For the theorems like `thm:thqg-g3-polarization`, I think citing the local theorem might work better since the current volume is self-contained, even though cross-volume citations are also an option.
thinking
**Fixing references**

I notice that the reference to `Chapter\ref{v1-chap:casimir-divisor}` needs to be updated since the actual chapter is now in Volume II. There's also the phantom reference that may not number correctly. It seems a better approach would be to replace it with `the Volume II chapter "Casimir divisor core transport"`. I realize that while there's an alias, it would be more consistent and honest to reflect the new chapter placement. I should double-check the context around landscape_census line 2553 for clarity.
exec
/bin/zsh -lc "sed -n '2546,2558p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Intrinsic vs.\ extrinsic: resolution]
\label{rem:hred-intrinsic}
Proposition~\ref{prop:hred-sl2} constructs $H^{\mathrm{red}}_1$
\emph{extrinsically}: the Picard--Fuchs D-module is computed from
the generating function, not directly from the bar complex.
The PBW recurrence theorem
(Theorem~\ref{thm:pbw-recurrence},
Chapter~\ref{v1-chap:casimir-divisor}) resolves this for
$\mathfrak{sl}_2$ and identifies the general mechanism.

The intrinsic construction has two structural inputs:
\begin{enumerate}[label=\textup{(\Roman*)}]
\item \emph{Invariant theory.}
context compacted
ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 9:35 PM.
tokens used
262,014
