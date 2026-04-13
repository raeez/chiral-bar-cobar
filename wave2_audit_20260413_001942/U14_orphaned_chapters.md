# U14_orphaned_chapters (696s)

- [CRITICAL] `main.tex:1554` — PROBLEM: the `\ifannalsedition` block seeds phantom labels for omitted chapter files (`concordance.tex`, `editorial_constitution.tex`, `twisted_holography_quantum_gravity.tex`, multiple migrated Vol II/III files), so cross-references can succeed while the real chapter is absent. FIX: after resolving each orphan below, delete the corresponding phantom labels from `main.tex`; keep phantoms only for intentionally non-chapter targets.

- [HIGH] `chapters/connections/outlook.tex:2` — PROBLEM: `outlook.tex` says the full concordance lives in `standalone/editorial.tex`, but that file does not exist. FIX: create `standalone/editorial.tex` and move the concordance/editorial companion behind that entry point, or delete the claim from `outlook.tex`.

- [HIGH] `chapters/connections/concordance.tex:1` — PROBLEM: 11,309-line constitutional chapter is orphaned; `main.tex:1505-1507` still says `master_concordance` is placed after `concordance.tex`, but there is no active `\input{chapters/connections/concordance}` anywhere. FIX: move this file out of `chapters/` into the standalone companion promised by `outlook.tex:2`, and remove the stale concordance comments/phantoms from `main.tex`.

- [HIGH] `chapters/connections/thqg_concordance_supplement.tex:1` — PROBLEM: orphaned supplement; its only parent is the orphan `chapters/connections/concordance.tex:6620`. FIX: move it with `concordance.tex` into the standalone editorial companion and stop treating it as a chapter-surface file.

- [HIGH] `chapters/connections/editorial_constitution.tex:1` — PROBLEM: orphaned chapter; `outlook.tex:2` says `outlook` replaces `editorial_constitution` in the monograph proper, yet `main.tex:1561` and `1673` still plant labels for it. FIX: move it out of `chapters/` into the standalone editorial companion and delete the stale phantom labels in `main.tex`.

- [HIGH] `chapters/connections/twisted_holography_quantum_gravity.tex:5` — PROBLEM: the THQG master chapter is dead because its only root include is commented out at `main.tex:1493`, while `main.tex:1590-1594` fakes some of its labels. FIX: restore `\input{chapters/connections/twisted_holography_quantum_gravity}` at `main.tex:1493` and remove the THQG phantom-label block.

- [HIGH] `chapters/connections/thqg_perturbative_finiteness.tex:1` — PROBLEM: orphaned section file; its only parent is the unreachable THQG master at `twisted_holography_quantum_gravity.tex:495`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_gravitational_complexity.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:496`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_symplectic_polarization.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:497`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_gravitational_s_duality.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:498`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_gravitational_yangian.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:499`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_soft_graviton_theorems.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:500`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_modular_bootstrap.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:501`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_holographic_reconstruction.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:502`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_critical_string_dichotomy.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:503`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_fredholm_partition_functions.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:504`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_preface_supplement.tex:2` — PROBLEM: the file says it should be “Inserted near the end of the preface chapter via `\input`,” but no such input exists anywhere in the live graph. FIX: add `\input{chapters/connections/thqg_preface_supplement}` near the end of `chapters/frame/preface.tex`.

- [MEDIUM] `chapters/connections/holomorphic_topological.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1397` comments out its only include and marks it “migrated to Vol II Part V.” FIX: remove it from Vol I’s `chapters/` tree and keep only the Vol II copy; also drop its `main.tex` phantom labels at `1607, 1609-1611`.

- [MEDIUM] `chapters/connections/kontsevich_integral.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1398` marks it “migrated to Vol II Part III.” FIX: remove it from Vol I’s `chapters/` tree and delete its `main.tex` phantom labels at `1608, 1612, 1613, 1620`.

- [MEDIUM] `chapters/connections/physical_origins.tex:1` — PROBLEM: orphaned 19-line stub; both the file (`lines 5-9`) and `main.tex:1399` say its content was absorbed into Vol II. FIX: delete this stub from `chapters/connections/`.

- [MEDIUM] `chapters/connections/ym_boundary_theory.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1402` marks it “Migrated to Vol II.” FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1621`.

- [MEDIUM] `chapters/connections/ym_higher_body_couplings.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1403` marks it “Migrated to Vol II.” FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1622`.

- [MEDIUM] `chapters/connections/ym_instanton_screening.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1404` marks it “Migrated to Vol II.” FIX: remove it from Vol I’s `chapters/` tree and delete its phantom labels at `main.tex:1623,1626`.

- [MEDIUM] `chapters/connections/casimir_divisor_core_transport.tex:4` — PROBLEM: orphaned migrated chapter; `main.tex:1409` says it moved to Vol II Part II, and line 4 promises a `casimir_divisor_core_transport_standalone.tex` wrapper that is not present in the repo. FIX: remove this file from Vol I’s `chapters/` tree and delete the false standalone-wrapper claim if the wrapper is not restored in the destination.

- [MEDIUM] `chapters/connections/typeA_baxter_rees_theta.tex:1` — PROBLEM: orphaned migrated appendix-chapter; `main.tex:1410` says it moved to Vol II Part II. FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1624`.

- [MEDIUM] `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:3` — PROBLEM: orphaned migrated chapter; `main.tex:1411` says it moved to Vol II Part II. FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1625`.

- [MEDIUM] `chapters/connections/dg_shifted_factorization_bridge.tex:1` — PROBLEM: orphaned removed chapter; `main.tex:1412` says it was “removed; content in Vol II Part II,” yet `main.tex:1579,1617-1619` still seeds labels for it. FIX: delete this file from Vol I’s `chapters/` tree and remove the stale phantom labels.

- [MEDIUM] `chapters/examples/toroidal_elliptic.tex:5` — PROBLEM: orphaned migrated chapter; `main.tex:1347` says it was “Moved to Vol III,” but Vol I still keeps the full 4,694-line file and a large phantom-label block at `main.tex:1628-1652`. FIX: remove the file from Vol I’s `chapters/examples/` tree and delete the toroidal/Vol III phantom-label block.

- [LOW] `chapters/frame/preface_section1_draft.tex:1` — PROBLEM: orphaned draft; the file says “To be integrated into preface.tex,” but `chapters/frame/preface.tex` already contains Section 1 starting at line `118`. FIX: archive or delete this draft.

- [LOW] `chapters/frame/preface_section1_v2.tex:1` — PROBLEM: orphaned alternate draft of the same live section; `chapters/frame/preface.tex` already carries the same Section 1 lane, including matching later headings at `625` and `739`. FIX: archive or delete this superseded v2 file.

- [LOW] `chapters/frame/preface_sections2_4_draft.tex:1` — PROBLEM: orphaned draft; `preface.tex` already contains Sections 2, 3, and 4 at lines `858`, `1274`, and `1737`. FIX: archive or delete this draft.

- [LOW] `chapters/frame/preface_sections5_9_draft.tex:1` — PROBLEM: orphaned draft; `preface.tex` already contains Sections 5, 6, 7, 8, and 9 at lines `2161`, `2435`, `2742`, `3147`, and `3279`. FIX: archive or delete this draft.

- [LOW] `chapters/frame/preface_sections10_13_draft.tex:1` — PROBLEM: orphaned draft; `preface.tex` already contains Section 10 and the matching closing headings at `3522`, `3731`, `3928`, `4010`, `4100`, `4216`, `4271`, and `4313`. FIX: archive or delete this draft.

## Summary
Checked: 113 | Findings: 33 | Verdict: FAIL


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
session id: 019d8418-b5fe-75d3-aa35-2eec3b47e2de
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

Check main.tex for \input{} commands. Are all chapter files \input'd? Are there .tex files in chapters/ NOT in the \input graph? These are orphaned.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers



thinking
**Planning repository audit**

I need to address the user's request for an audit of a specific repository regarding unfinished work, focusing on the inputs in main.tex and checking all chapter files. It seems like there are orphaned .tex files in the chapters. This requires a thorough inspection according to guidelines, and I’ll likely rely on the skill of deep-beilinson-audit. I'll check AGENTS’ instructions and review relevant files before taking any next steps, starting with an update to the user acknowledging the task ahead.
thinking
**Planning unfinished work audit**

The request is centered on auditing unfinished work involving the main.tex input graph and identifying orphaned .tex files. It seems I may not need to read large files as we're not making mathematical edits. I'll probably utilize the explorer agent for codebase questions since the instructions stress its use over manual searches. This is a codebase audit, so it makes sense to parallelize efforts with the explorer and shell commands for thorough inspection of main.tex and related files.
thinking
**Utilizing explorer and shell**

The explorer can search for files quickly, but I should remember that the results depend on the actual contents. It seems we can read files directly too. I'll consider using the explorer for broader codebase questions like listing all chapter .tex files that aren't included in main.tex. I’m thinking we could do both: map the graph with the explorer and verify details using shell commands. I should also use parallel execution of developer tools while avoiding internet browsing.
codex
Using `deep-beilinson-audit` for this turn because you asked for an adversarial audit. I’m starting by reading the live include graph from `main.tex` and enumerating every `chapters/**/*.tex` file so I can verify which chapter surfaces are actually reachable and which are orphaned.
Plan update
  → Inspect `main.tex` include graph and collect all `\input` targets
  • Enumerate `.tex` files under `chapters/` and compare against reachable inputs
  • Verify each orphan candidate against actual file contents and produce exact findings with fixes

thinking
**Considering file reading options**

I need to read the skill file, and I'm wondering whether to use exec_command or cat, or maybe even sed. I think exec_command is the right choice to read the first lines of SKILL.md and maybe main.tex. Should I consider listing files as well? I could use multi_tool_use.parallel to run exec_command multiple times. But perhaps it's better to use the explorer agent to map the include graph and run shell commands myself. Let's try that!
codex
I’m pulling the audit workflow instructions from the local skill and, in parallel, a codebase explorer to compute the `main.tex` include graph against `chapters/**/*.tex`. After that I’ll verify every orphan candidate directly in the files before I report it.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

collab spawn_agent(call_cg5yEaAoE1Msi4T77Xk3ZHN9, prompt="<task>Audit the TeX include graph rooted at main.tex in /Users/raeez/chiral-bar-cobar. Identify every `.tex` file under …")
mcp startup: no servers
spawn_agent(call_cg5yEaAoE1Msi4T77Xk3ZHN9, prompt="<task>Audit the TeX include graph rooted at main.tex in /Users/raeez/chiral-bar-cobar. Identify every `.tex` file under …") pending init:
  agent: 019d8419-1820-7d82-89c4-2fbd5df38a7a
Plan update
Determine included chapter files from main.tex and then find reachable vs orphan chapter .tex files.
  → Map include graph by parsing main.tex and every included chapter file under chapters/ for \input/\include statements.
  • List all chapter .tex files under chapters/ and mark those found reachable through the graph, recording parent include paths.
  • Identify remaining chapter .tex files as orphans and verify they do not appear in graph chains.
codex
The skill is loaded. I’m reading `main.tex` and the `chapters/` tree directly now; the goal is to prove reachability from actual `\input` chains, not just grep for filenames.
exec
/bin/zsh -lc "sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 51ms:
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
chapters/examples/yangians_drinfeld_kohno.tex

codex
I have the file inventory. Next I’m extracting the actual `\input`/`\include` edges so the audit is about reachability, not just file presence.
exec
/bin/zsh -lc "sed -n '260,520p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(input|include)\\{' main.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\let\theHtechnique\theHtheorem

\let\theHapplications\theHtheorem
\let\theHframework\theHtheorem
\let\theHmaintheorem\theHtheorem
\let\theHconstruction\theHtheorem
\let\theHperspective\theHtheorem
\let\theHconclusion\theHtheorem
\let\theHquestion\theHtheorem
\let\theHsummary\theHtheorem
\let\theHprocedure\theHtheorem
\let\theHinterpretation\theHtheorem

\let\theHhistorical\theHtheorem
\let\theHcontext\theHtheorem
\let\theHattribution\theHtheorem
\let\theHreading\theHtheorem
\let\theHapplication\theHtheorem
\let\theHprinciple\theHtheorem
\let\theHmotivation\theHtheorem
 succeeded in 51ms:
main.tex:841:\include{chapters/frame/preface}
main.tex:845: \input{chapters/frame/guide_to_main_results}
main.tex:854:\include{chapters/theory/introduction}
main.tex:869:\include{chapters/frame/heisenberg_frame}
main.tex:882:% \input{platonic_introduction_volume_I} % archived; content absorbed into introduction.tex
main.tex:958:\include{chapters/theory/fourier_seed}
main.tex:965:\include{chapters/theory/algebraic_foundations}
main.tex:971:\include{chapters/theory/three_invariants}
main.tex:977:\include{chapters/theory/configuration_spaces}
main.tex:983:\include{chapters/theory/bar_construction}
main.tex:989:\include{chapters/theory/cobar_construction}
main.tex:996:\include{chapters/theory/bar_cobar_adjunction}
main.tex:1000:\input{appendices/homotopy_transfer}
main.tex:1006:% \input{chapters/theory/bar_cobar_quasi_isomorphism}
main.tex:1012:\include{chapters/theory/poincare_duality}
main.tex:1020:\include{chapters/theory/chiral_koszul_pairs}
main.tex:1021:\include{chapters/theory/koszul_pair_structure}
main.tex:1027:\include{chapters/theory/higher_genus}
main.tex:1029:% \include{chapters/theory/higher_genus_full}
main.tex:1034:% \input{chapters/theory/higher_genus_quasi_isomorphism}
thinking
**Planning recursive LaTeX include graph parsing**

I'm outlining a Python script to recursively parse LaTeX `\input` and `\include` commands from the main file, building a graph of included `.tex` files under `chapters/`. I'll handle comment stripping carefully and resolve relative paths for includes. My goal is to find all reachable chapter files from `main.tex` and identify orphan files with clear evidence, presenting inclusion chains for all reachable files.
exec
/bin/zsh -lc "python - <<'PY'
import os, re, json
root = os.getcwd()
main = os.path.join(root, 'main.tex')
print('main', main)
include_pat = re.compile(r'\\\\(input|include)\\s*\\{(["'^}]+)'"\\}')

def strip_comments(line):
    res = []
    i = 0
    while i < len(line):
        if line[i] == '%':
            if i > 0 and line[i-1] == '\\\\':
                res.append('%')
                i += 1
                continue
            break
        res.append(line[i])
        i += 1
    return ''.join(res)

def resolve(current, target):
    if not target.endswith('.tex'):
        target = target + '.tex'
    return os.path.normpath(os.path.join(os.path.dirname(current), target))

from collections import deque
queue = deque()
queue.append(main)
parent = {}
visited = set([main])
include_children = {}

while queue:
    curr = queue.popleft()
    include_children[curr] = []
    try:
        data = open(curr, encoding='utf-8').read().splitlines()
    except FileNotFoundError:
        continue
    for line in data:
        line = strip_comments(line)
        for m in include_pat.finditer(line):
            tgt = m.group(2).strip()
            if not tgt:
                continue
            resolved = resolve(curr, tgt)
            include_children[curr].append(resolved)
            if resolved not in visited:
                visited.add(resolved)
                parent[resolved] = curr
                queue.append(resolved)

print('visited_count', len(visited))
# list tex files under chapters
chapters = []
for dirpath, dirnames, filenames in os.walk(os.path.join(root, 'chapters')):
    for fn in filenames:
        if fn.endswith('.tex'):
            chapters.append(os.path.normpath(os.path.join(dirpath, fn)))
chapters.sort()
print('chapter_count', len(chapters))
# gather reachable under chapters
from collections import defaultdict
reachable = []
for c in chapters:
    if c in visited:
        # build chain
        chain = []
        curr = c
        while curr:
            chain.append(curr)
            curr = parent.get(curr)
        reachable.append((c, list(reversed(chain))))
reachable.sort()
orphans = [c for c in chapters if c not in visited]
print(json.dumps({
    'reachable': [(c, chain) for c, chain in reachable],
    'orphans': orphans
}, indent=2))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python


exec
/bin/zsh -lc "python3 - <<'PY'
import os, re, json
root = os.getcwd()
main = os.path.join(root, 'main.tex')
print('main', main)
include_pat = re.compile(r'\\\\(input|include)\\s*\\{(["'^}]+)'"\\}')

def strip_comments(line):
    res = []
    i = 0
    while i < len(line):
        if line[i] == '%':
            if i > 0 and line[i-1] == '\\\\':
                res.append('%')
                i += 1
                continue
            break
        res.append(line[i])
        i += 1
    return ''.join(res)

def resolve(current, target):
    if not target.endswith('.tex'):
        target = target + '.tex'
    return os.path.normpath(os.path.join(os.path.dirname(current), target))

from collections import deque
queue = deque()
queue.append(main)
parent = {}
visited = set([main])
include_children = {}

while queue:
    curr = queue.popleft()
    include_children[curr] = []
    try:
        with open(curr, encoding='utf-8') as f:
            data = f.read().splitlines()
    except FileNotFoundError:
        continue
    for line in data:
        line = strip_comments(line)
        for m in include_pat.finditer(line):
            tgt = m.group(2).strip()
            if not tgt:
                continue
            resolved = resolve(curr, tgt)
            include_children[curr].append(resolved)
            if resolved not in visited:
                visited.add(resolved)
                parent[resolved] = curr
                queue.append(resolved)

print('visited_count', len(visited))
chapters = []
chapters_root = os.path.join(root, 'chapters')
for dirpath, dirnames, filenames in os.walk(chapters_root):
    for fn in filenames:
        if fn.endswith('.tex'):
            chapters.append(os.path.normpath(os.path.join(dirpath, fn)))
chapters.sort()
print('chapter_count', len(chapters))
reachable = []
for c in chapters:
    if c in visited:
        chain = []
        curr = c
        while curr:
            chain.append(curr)
            curr = parent.get(curr)
        reachable.append((c, list(reversed(chain))))
reachable.sort()
orphans = [c for c in chapters if c not in visited]
print(json.dumps({
    'reachable': [(c, chain) for c, chain in reachable],
    'orphans': orphans
}, indent=2))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 355ms:
main /Users/raeez/chiral-bar-cobar/main.tex
visited_count 96
chapter_count 113
{
  "reachable": [
    [
      "/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex",
      [
        "/Users/raeez/chiral-bar-cobar/main.tex",
        "/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex"
      ]
    ],
    [
      "/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex",
      [
        "/Users/raeez/chiral-bar-cobar/main.tex",
        "/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex"
      ]
    ],
    [


thinking
**Considering reachability computation**

I’m trying to compute reachability and I might write a script for it. I need to check if there are inputs within comments since my regex includes commented lines, but I only want active edges. I’ll need to parse TeX lines to remove comments and consider inputs that may just include file names without the .tex extension. I think using a shell script or a one-off Python script could work well. I'll focus on auditing only .tex files under chapters, avoiding appendices.
thinking
**Identifying orphan files and references**

I need to figure out line references for orphan files, probably starting with line 1 of each orphan file. The problem is that these files aren't included anywhere. I might also want to reference lines in main.tex where content has been omitted, specifically the commented lines. Formatting should focus on one file:line reference, such as orphan file line 1 or a specific line in main.tex that shows the omission. This helps demonstrate that the orphan file has content but no inclusion and indicates that it’s not reachable from main.tex.
thinking
**Determining fixes for orphan files**

I think using file:1 can indicate the existence of an orphan file. I need to suggest an exact fix, like adding `\input{...}` in `main.tex` if the content belongs to Volume I, or maybe moving it to an archive or another volume and leaving a comment about the migration. Since the user wants specific fixes and not just diagnoses, I’ll need to inspect the content of each orphan file carefully to categorize them as drafts, stubs, or supplements. This could involve many files—possibly dozens!
thinking
**Computing orphan list**

I need to calculate the exact orphan list first. I think it makes sense to run a script while ignoring comments and traversing the includes. Using Python would probably be the best choice for this task since it's efficient for handling such computations. I need to focus on ensuring the script runs smoothly and produces the correct results. Getting that orphan list right is crucial!
codex
I have the raw edge list, but it includes commented-out `\input`s. I’m now computing the active graph by stripping TeX comments first so the orphan list is defensible.
Plan update
  ✓ Map include graph by parsing main.tex and every included chapter file under chapters/ for \input/\include statements.
  ✓ List all chapter .tex files under chapters/ and mark those found reachable through the graph, recording parent include paths.
  ✓ Identify remaining chapter .tex files as orphans and verify they do not appear in graph chains.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
root = Path('/Users/raeez/chiral-bar-cobar')
include_re = re.compile(r'\\\\(?:input|include)\\{(["'^}]+)'"\\}')

def strip_comments(line: str) -> str:
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == '%':
            # escaped percent does not start comment
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

files = [root/'main.tex'] + sorted((root/'chapters').rglob('*.tex'))
edges = {}
for f in files:
    text = f.read_text(errors='ignore').splitlines()
    refs = []
    for lineno, line in enumerate(text, 1):
        s = strip_comments(line)
        for m in include_re.finditer(s):
            target = m.group(1).strip()
            if not target:
                continue
            p = (root/target)
            if p.suffix "'!= '"'.tex':
                p = p.with_suffix('.tex')
            refs.append((lineno, p.resolve().relative_to(root.resolve()).as_posix()))
    edges[f.resolve().relative_to(root.resolve()).as_posix()] = refs

reachable = set()
parent = {}
stack = ['main.tex']
while stack:
    cur = stack.pop()
    if cur in reachable:
        continue
    reachable.add(cur)
    for lineno, tgt in edges.get(cur, []):
        if tgt not in parent:
            parent[tgt] = (cur, lineno)
        if (root/tgt).exists():
            stack.append(tgt)

chapters = sorted(p.resolve().relative_to(root.resolve()).as_posix() for p in (root/'chapters').rglob('*.tex'))
orphan = [p for p in chapters if p not in reachable]
print('REACHABLE_CHAPTERS', len([p for p in chapters if p in reachable]))
print('ORPHANS', len(orphan))
for p in orphan:
    print(p)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 588ms:
REACHABLE_CHAPTERS 82
ORPHANS 31
chapters/connections/casimir_divisor_core_transport.tex
chapters/connections/concordance.tex
chapters/connections/dg_shifted_factorization_bridge.tex
chapters/connections/editorial_constitution.tex
chapters/connections/holomorphic_topological.tex
chapters/connections/kontsevich_integral.tex
chapters/connections/physical_origins.tex
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex
chapters/connections/thqg_concordance_supplement.tex
chapters/connections/thqg_critical_string_dichotomy.tex
chapters/connections/thqg_fredholm_partition_functions.tex
chapters/connections/thqg_gravitational_complexity.tex
chapters/connections/thqg_gravitational_s_duality.tex
chapters/connections/thqg_gravitational_yangian.tex
chapters/connections/thqg_holographic_reconstruction.tex
chapters/connections/thqg_modular_bootstrap.tex
chapters/connections/thqg_perturbative_finiteness.tex
chapters/connections/thqg_preface_supplement.tex


thinking
**Preparing detailed inclusion lists**

I’m organizing reachable and orphan chapter files into two clear flat lists with inclusion paths and verification evidence, carefully verifying counts and references so the final message explains the file inclusion status and methodology based on BFS parsing from `main.tex`.

exec
/bin/zsh -lc "python3 - <<'PY'
import os, re
root = os.getcwd()
main = os.path.join(root, 'main.tex')
include_pat = re.compile(r'\\\\(input|include)\\s*\\{(["'^}]+)'"\\}')

def strip_comments(line):
    res = []
    i = 0
    while i < len(line):
        if line[i] == '%':
            if i > 0 and line[i-1] == '\\\\':
                res.append('%')
                i += 1
                continue
            break
        res.append(line[i])
        i += 1
    return ''.join(res)

def resolve(current, target):
    if not target.endswith('.tex'):
        target = target + '.tex'
    return os.path.normpath(os.path.join(os.path.dirname(current), target))

from collections import deque
queue = deque([main])
parent = {}
visited = {main}
while queue:
    curr = queue.popleft()
    try:
        with open(curr, encoding='utf-8') as f:
            data = f.read().splitlines()
    except FileNotFoundError:
        continue
    for line in data:
        line = strip_comments(line)
        for m in include_pat.finditer(line):
            tgt = m.group(2).strip()
            if not tgt:
                continue
            resolved = resolve(curr, tgt)
            if resolved not in visited:
                visited.add(resolved)
                parent[resolved] = curr
                queue.append(resolved)

chapters = []
chapters_root = os.path.join(root, 'chapters')
for dirpath, dirnames, filenames in os.walk(chapters_root):
    for fn in filenames:
        if fn.endswith('.tex'):
            chapters.append(os.path.normpath(os.path.join(dirpath, fn)))
chapters.sort()
reachable = []
for c in chapters:
    if c in visited:
        chain = []
        curr = c
        while curr:
            chain.append(curr)
            curr = parent.get(curr)
        reachable.append((c, list(reversed(chain))))
orphan = [c for c in chapters if c not in visited]
print('reachable_count', len(reachable))
print('orphans_count', len(orphan))
for path, chain in reachable:
    rel_chain = [os.path.relpath(p, root) for p in chain]
    print(path, '->'.join(rel_chain))
print('ORPHANS:')
for path in orphan:
    print(path)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 342ms:
reachable_count 71
orphans_count 42
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex main.tex->chapters/connections/arithmetic_shadows.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex main.tex->chapters/connections/bv_brst.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex main.tex->chapters/connections/entanglement_modular_koszul.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_connection.tex main.tex->chapters/connections/feynman_connection.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/feynman_diagrams.tex main.tex->chapters/connections/feynman_diagrams.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex main.tex->chapters/connections/frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex main.tex->chapters/connections/genus1_seven_faces.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex main.tex->chapters/connections/genus_complete.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_codes_koszul.tex main.tex->chapters/connections/holographic_codes_koszul.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex main.tex->chapters/connections/holographic_datum_master.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex main.tex->chapters/connections/master_concordance.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/outlook.tex main.tex->chapters/connections/outlook.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/poincare_computations.tex main.tex->chapters/connections/poincare_computations.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/semistrict_modular_higher_spin_w3.tex main.tex->chapters/connections/semistrict_modular_higher_spin_w3.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex main.tex->chapters/connections/subregular_hook_frontier.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_entanglement_programme.tex main.tex->chapters/connections/thqg_entanglement_programme.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex main.tex->chapters/connections/thqg_open_closed_realization.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex main.tex->chapters/examples/bar_complex_tables.tex
thinking
**Analyzing orphan files**

I'm thinking about finding orphan `.tex` files along with any commented-out includes in the main.tex. I need to determine the exact fix and the severity of the issue. Maybe I should group some findings, like orphans by their parent aggregator? However, the output contract specifies using a bullet list. I could potentially list each orphan file or cluster them by the main issue. It might be necessary to inspect each orphan file for reference details as well.
thinking
**Inspecting orphan files**

I'm considering looking at the head of the files, as comments might indicate they've been moved to Vol II or archived. I also need to check if any orphan files are referenced in comments within main.tex or elsewhere. I could use a script to find active parents and the comments. Inspecting the first 40 lines of each orphan could help, and I might use shell commands to manage large groups. Additionally, searching for file names in the repository could uncover important comments.
codex
The graph has 31 unreachable chapter files. I’m classifying each one now from its own contents and from any commented-out include sites, so the fixes can be exact instead of generic.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
root = Path('/Users/raeez/chiral-bar-cobar')
orphans = [
'chapters/connections/casimir_divisor_core_transport.tex',
'chapters/connections/concordance.tex',
'chapters/connections/dg_shifted_factorization_bridge.tex',
'chapters/connections/editorial_constitution.tex',
'chapters/connections/holomorphic_topological.tex',
'chapters/connections/kontsevich_integral.tex',
'chapters/connections/physical_origins.tex',
'chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex',
'chapters/connections/thqg_concordance_supplement.tex',
'chapters/connections/thqg_critical_string_dichotomy.tex',
'chapters/connections/thqg_fredholm_partition_functions.tex',
'chapters/connections/thqg_gravitational_complexity.tex',
'chapters/connections/thqg_gravitational_s_duality.tex',
'chapters/connections/thqg_gravitational_yangian.tex',
'chapters/connections/thqg_holographic_reconstruction.tex',
'chapters/connections/thqg_modular_bootstrap.tex',
'chapters/connections/thqg_perturbative_finiteness.tex',
'chapters/connections/thqg_preface_supplement.tex',
'chapters/connections/thqg_soft_graviton_theorems.tex',
'chapters/connections/thqg_symplectic_polarization.tex',
'chapters/connections/twisted_holography_quantum_gravity.tex',
'chapters/connections/typeA_baxter_rees_theta.tex',
'chapters/connections/ym_boundary_theory.tex',
'chapters/connections/ym_higher_body_couplings.tex',
'chapters/connections/ym_instanton_screening.tex',
'chapters/examples/toroidal_elliptic.tex',
'chapters/frame/preface_section1_draft.tex',
'chapters/frame/preface_section1_v2.tex',
'chapters/frame/preface_sections10_13_draft.tex',
'chapters/frame/preface_sections2_4_draft.tex',
'chapters/frame/preface_sections5_9_draft.tex',
]

def first_nonempty(path):
    for i, line in enumerate(path.read_text(errors='ignore').splitlines(), 1):
        if line.strip():
            return i, line[:160]
    return 1, ''

all_tex = list(root.rglob('*.tex'))
for rel in orphans:
    path = root / rel
    line, first = first_nonempty(path)
    refs = []
    for tex in all_tex:
        text = tex.read_text(errors='ignore').splitlines()
        for i, ln in enumerate(text, 1):
            if rel[:-4] in ln or Path(rel).name in ln:
                refs.append(f\"{tex.relative_to(root)}:{i}:{ln.strip()[:180]}\")
    print('FILE', rel)
    print('FIRST', f'{line}:{first}')
    print('LINES', sum(1 for _ in path.open(errors='ignore')))
    print('REFS', len(refs))
    for r in refs[:10]:
        print(' ', r)
    if len(refs) > 10:
        print(' ', '...')
    print('---')
PY" in /Users/raeez/chiral-bar-cobarcodex
Reachable:
- `chapters/connections/arithmetic_shadows.tex`: `main.tex → chapters/connections/arithmetic_shadows.tex`
- `chapters/connections/bv_brst.tex`: `main.tex → chapters/connections/bv_brst.tex`
- `chapters/connections/entanglement_modular_koszul.tex`: `main.tex → chapters/connections/entanglement_modular_koszul.tex`
- `chapters/connections/feynman_connection.tex`: `main.tex → chapters/connections/feynman_connection.tex`
- `chapters/connections/feynman_diagrams.tex`: `main.tex → chapters/connections/feynman_diagrams.tex`
- `chapters/connections/frontier_modular_holography_platonic.tex`: `main.tex → chapters/connections/frontier_modular_holography_platonic.tex`
- `chapters/connections/genus1_seven_faces.tex`: `main.tex → chapters/connections/genus1_seven_faces.tex`
- `chapters/connections/genus_complete.tex`: `main.tex → chapters/connections/genus_complete.tex`
- `chapters/connections/holographic_codes_koszul.tex`: `main.tex → chapters/connections/holographic_codes_koszul.tex`
- `chapters/connections/holographic_datum_master.tex`: `main.tex → chapters/connections/holographic_datum_master.tex`
- `chapters/connections/master_concordance.tex`: `main.tex → chapters/connections/master_concordance.tex`
- `chapters/connections/outlook.tex`: `main.tex → chapters/connections/outlook.tex`
- `chapters/connections/poincare_computations.tex`: `main.tex → chapters/connections/poincare_computations.tex`
- `chapters/connections/semistrict_modular_higher_spin_w3.tex`: `main.tex → chapters/connections/semistrict_modular_higher_spin_w3.tex`
- `chapters/connections/subregular_hook_frontier.tex`: `main.tex → chapters/connections/subregular_hook_frontier.tex`
- `chapters/connections/thqg_entanglement_programme.tex`: `main.tex → chapters/connections/thqg_entanglement_programme.tex`
- `chapters/connections/thqg_open_closed_realization.tex`: `main.tex → chapters/connections/thqg_open_closed_realization.tex`
- `chapters/examples/bar_complex_tables.tex`: `main.tex → chapters/examples/bar_complex_tables.tex`
- `chapters/examples/bershadsky_polyakov.tex`: `main.tex → chapters/examples/bershadsky_polyakov.tex`
- `chapters/examples/beta_gamma.tex`: `main.tex → chapters/examples/beta_gamma.tex`
- `chapters/examples/deformation_quantization.tex`: `main.tex → chapters/examples/deformation_quantization.tex`
- `chapters/examples/deformation_quantization_examples.tex`: `main.tex → chapters/examples/deformation_quantization_examples.tex`
- `chapters/examples/free_fields.tex`: `main.tex → chapters/examples/free_fields.tex`
- `chapters/examples/genus_expansions.tex`: `main.tex → chapters/examples/genus_expansions.tex`
- `chapters/examples/heisenberg_eisenstein.tex`: `main.tex → chapters/examples/heisenberg_eisenstein.tex`
- `chapters/examples/kac_moody.tex`: `main.tex → chapters/examples/kac_moody.tex`
- `chapters/examples/landscape_census.tex`: `main.tex → chapters/examples/landscape_census.tex`
- `chapters/examples/lattice_foundations.tex`: `main.tex → chapters/examples/lattice_foundations.tex`
- `chapters/examples/level1_bridge.tex`: `main.tex → chapters/examples/level1_bridge.tex`
- `chapters/examples/logarithmic_w_algebras.tex`: `main.tex → chapters/examples/logarithmic_w_algebras.tex`
- `chapters/examples/minimal_model_examples.tex`: `main.tex → chapters/examples/minimal_model_examples.tex`
- `chapters/examples/minimal_model_fusion.tex`: `main.tex → chapters/examples/minimal_model_fusion.tex`
- `chapters/examples/moonshine.tex`: `main.tex → chapters/examples/moonshine.tex`
- `chapters/examples/n2_superconformal.tex`: `main.tex → chapters/examples/n2_superconformal.tex`
- `chapters/examples/symmetric_orbifolds.tex`: `main.tex → chapters/examples/symmetric_orbifolds.tex`
- `chapters/examples/w3_composite_fields.tex`: `main.tex → chapters/examples/w3_composite_fields.tex`
- `chapters/examples/w3_holographic_datum.tex`: `main.tex → chapters/examples/w3_holographic_datum.tex`
- `chapters/examples/w_algebras.tex`: `main.tex → chapters/examples/w_algebras.tex`
- `chapters/examples/w_algebras_deep.tex`: `main.tex → chapters/examples/w_algebras_deep.tex`
- `chapters/examples/y_algebras.tex`: `main.tex → chapters/examples/y_algebras.tex`
- `chapters/examples/yangians.tex`: `main.tex → chapters/examples/yangians.tex`
- `chapters/frame/guide_to_main_results.tex`: `main.tex → chapters/frame/guide_to_main_results.tex`
- `chapters/frame/heisenberg_frame.tex`: `main.tex → chapters/frame/heisenberg_frame.tex`
- `chapters/frame/preface.tex`: `main.tex → chapters/frame/preface.tex`
- `chapters/theory/algebraic_foundations.tex`: `main.tex → chapters/theory/algebraic_foundations.tex`
- `chapters/theory/bar_cobar_adjunction.tex`: `main.tex → chapters/theory/bar_cobar_adjunction.tex`
- `chapters/theory/bar_construction.tex`: `main.tex → chapters/theory/bar_construction.tex`
- `chapters/theory/chiral_hochschild_koszul.tex`: `main.tex → chapters/theory/chiral_hochschild_koszul.tex`
- `chapters/theory/chiral_koszul_pairs.tex`: `main.tex → chapters/theory/chiral_koszul_pairs.tex`
- `chapters/theory/chiral_modules.tex`: `main.tex → chapters/theory/chiral_modules.tex`
- `chapters/theory/cobar_construction.tex`: `main.tex → chapters/theory/cobar_construction.tex`
- `chapters/theory/coderived_models.tex`: `main.tex → chapters/theory/coderived_models.tex`
- `chapters/theory/computational_methods.tex`: `main.tex → chapters/theory/computational_methods.tex`
- `chapters/theory/configuration_spaces.tex`: `main.tex → chapters/theory/configuration_spaces.tex`
- `chapters/theory/derived_langlands.tex`: `main.tex → chapters/theory/derived_langlands.tex`
- `chapters/theory/e1_modular_koszul.tex`: `main.tex → chapters/theory/e1_modular_koszul.tex`
- `chapters/theory/en_koszul_duality.tex`: `main.tex → chapters/theory/en_koszul_duality.tex`
- `chapters/theory/existence_criteria.tex`: `main.tex → chapters/theory/existence_criteria.tex`
- `chapters/theory/filtered_curved.tex`: `main.tex → chapters/theory/filtered_curved.tex`
- `chapters/theory/fourier_seed.tex`: `main.tex → chapters/theory/fourier_seed.tex`
- `chapters/theory/higher_genus.tex`: `main.tex → chapters/theory/higher_genus.tex`
- `chapters/theory/hochschild_cohomology.tex`: `main.tex → chapters/theory/hochschild_cohomology.tex`
- `chapters/theory/introduction.tex`: `main.tex → chapters/theory/introduction.tex`
- `chapters/theory/koszul_pair_structure.tex`: `main.tex → chapters/theory/koszul_pair_structure.tex`
- `chapters/theory/nilpotent_completion.tex`: `main.tex → chapters/theory/nilpotent_completion.tex`
- `chapters/theory/ordered_associative_chiral_kd.tex`: `main.tex → chapters/theory/ordered_associative_chiral_kd.tex`
- `chapters/theory/poincare_duality.tex`: `main.tex → chapters/theory/poincare_duality.tex`
- `chapters/theory/poincare_duality_quantum.tex`: `main.tex → chapters/theory/poincare_duality_quantum.tex`
- `chapters/theory/quantum_corrections.tex`: `main.tex → chapters/theory/quantum_corrections.tex`
- `chapters/theory/spectral_sequences.tex`: `main.tex → chapters/theory/spectral_sequences.tex`
- `chapters/theory/three_invariants.tex`: `main.tex → chapters/theory/three_invariants.tex`

Orphans (no `\input`/`\include` path from `main.tex` or any recursively included file in `main.tex`’s graph):
- `chapters/connections/casimir_divisor_core_transport.tex`
- `chapters/connections/concordance.tex`
- `chapters/connections/dg_shifted_factorization_bridge.tex`
- `chapters/connections/editorial_constitution.tex`
- `chapters/connections/holomorphic_topological.tex`
- `chapters/connections/kontsevich_integral.tex`
- `chapters/connections/physical_origins.tex`
- `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex`
- `chapters/connections/thqg_concordance_supplement.tex`
- `chapters/connections/thqg_critical_string_dichotomy.tex`
- `chapters/connections/thqg_fredholm_partition_functions.tex`
- `chapters/connections/thqg_gravitational_complexity.tex`
- `chapters/connections/thqg_gravitational_s_duality.tex`
- `chapters/connections/thqg_gravitational_yangian.tex`
- `chapters/connections/thqg_holographic_reconstruction.tex`
- `chapters/connections/thqg_introduction_supplement.tex`
- `chapters/connections/thqg_introduction_supplement_body.tex`
- `chapters/connections/thqg_modular_bootstrap.tex`
- `chapters/connections/thqg_perturbative_finiteness.tex`
- `chapters/connections/thqg_preface_supplement.tex`
- `chapters/connections/thqg_soft_graviton_theorems.tex`
- `chapters/connections/thqg_symplectic_polarization.tex`
- `chapters/connections/twisted_holography_quantum_gravity.tex`
- `chapters/connections/typeA_baxter_rees_theta.tex`
- `chapters/connections/ym_boundary_theory.tex`
- `chapters/connections/ym_higher_body_couplings.tex`
- `chapters/connections/ym_instanton_screening.tex`
- `chapters/examples/toroidal_elliptic.tex`
- `chapters/examples/yangians_computations.tex`
- `chapters/examples/yangians_drinfeld_kohno.tex`
- `chapters/examples/yangians_foundations.tex`
- `chapters/frame/preface_section1_draft.tex`
- `chapters/frame/preface_section1_v2.tex`
- `chapters/frame/preface_sections10_13_draft.tex`
- `chapters/frame/preface_sections2_4_draft.tex`
- `chapters/frame/preface_sections5_9_draft.tex`
- `chapters/theory/bar_cobar_adjunction_curved.tex`
- `chapters/theory/bar_cobar_adjunction_inversion.tex`
- `chapters/theory/chiral_center_theorem.tex`
- `chapters/theory/higher_genus_complementarity.tex`
- `chapters/theory/higher_genus_foundations.tex`
- `chapters/theory/higher_genus_modular_koszul.tex`

Verification: parsed `main.tex` and every file reachable from it, stripping `%` comments and looking for literal `\input`/`\include` tokens, so each reachable entry has an inclusion edge from `main.tex` (no intermediate files appeared) and every orphan lacks a parent edge in that graph.

Next step: decide whether orphaned chapter files should be reintegrated into `main.tex` via appropriate includes or archived/merged elsewhere.

thinking
**Considering script efficiency**

I'm thinking about creating a more efficient script to print metadata. It might also be helpful to consider using `rg` for separate tasks later on. I wonder if breaking it up might make it easier to manage and optimize. It's always nice to streamline processes, so let me figure out how to do that effectively. I’m looking forward to implementing these improvements!
codex
The first classification pass was too heavy because it scanned every TeX file against every orphan. I’m switching to a lighter pass: file headers first, then targeted reference checks only where needed.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar')
orphans = [
'chapters/connections/casimir_divisor_core_transport.tex',
'chapters/connections/concordance.tex',
'chapters/connections/dg_shifted_factorization_bridge.tex',
'chapters/connections/editorial_constitution.tex',
'chapters/connections/holomorphic_topological.tex',
'chapters/connections/kontsevich_integral.tex',
'chapters/connections/physical_origins.tex',
'chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex',
'chapters/connections/thqg_concordance_supplement.tex',
'chapters/connections/thqg_critical_string_dichotomy.tex',
'chapters/connections/thqg_fredholm_partition_functions.tex',
'chapters/connections/thqg_gravitational_complexity.tex',
'chapters/connections/thqg_gravitational_s_duality.tex',
'chapters/connections/thqg_gravitational_yangian.tex',
'chapters/connections/thqg_holographic_reconstruction.tex',
'chapters/connections/thqg_modular_bootstrap.tex',
'chapters/connections/thqg_perturbative_finiteness.tex',
'chapters/connections/thqg_preface_supplement.tex',
'chapters/connections/thqg_soft_graviton_theorems.tex',
'chapters/connections/thqg_symplectic_polarization.tex',
'chapters/connections/twisted_holography_quantum_gravity.tex',
'chapters/connections/typeA_baxter_rees_theta.tex',
'chapters/connections/ym_boundary_theory.tex',
'chapters/connections/ym_higher_body_couplings.tex',
'chapters/connections/ym_instanton_screening.tex',
'chapters/examples/toroidal_elliptic.tex',
'chapters/frame/preface_section1_draft.tex',
'chapters/frame/preface_section1_v2.tex',
'chapters/frame/preface_sections10_13_draft.tex',
'chapters/frame/preface_sections2_4_draft.tex',
'chapters/frame/preface_sections5_9_draft.tex',
]
for rel in orphans:
    path = root / rel
    lines = path.read_text(errors='ignore').splitlines()
    print(f'FILE {rel}')
    print(f'COUNT {len(lines)}')
    shown = 0
    for i, line in enumerate(lines, 1):
        if line.strip():
            print(f'{i}:{line[:200]}')
            shown += 1
        if shown == 8:
            break
    print('---')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE chapters/connections/casimir_divisor_core_transport.tex
COUNT 1512
2:% Body fragment for repository integration.
3:% Assumes standard AMS theorem environments and basic macros.
4:% A standalone wrapper is provided in casimir_divisor_core_transport_standalone.tex.
6:\chapter{Casimir Recurrence Modules, Divisor Cores, and Intrinsic Spectral Transport}
7:\label{chap:casimir-divisor}
9:\section{The first-principles problem}
11:The spectral discriminant
12:\[
---
FILE chapters/connections/concordance.tex
COUNT 11309
1:\chapter{Concordance with primary literature}
2:\label{chap:concordance}
4:\index{concordance|textbf}
6:This chapter is the constitution of the monograph. When chapters
7:disagree, this chapter governs. It records the five main theorems
8:with their precise status and locates every result against the
9:prior literature: what is proved, what is conditional, what

thinking
**Computing parent references**

I’m thinking I need to start by computing parent references from the active graph while excluding self-mentions. I should create a script that outputs active inbound edges and any relevant comments from the main. It seems like I'll need to utilize the parsed active edges I've already gathered. I want to make sure to analyze all references and the specific comments along with their line text. I’ll aim to script this robustly!
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
root = Path('/Users/raeez/chiral-bar-cobar')
orphans = [
'chapters/connections/casimir_divisor_core_transport.tex',
'chapters/connections/concordance.tex',
'chapters/connections/dg_shifted_factorization_bridge.tex',
'chapters/connections/editorial_constitution.tex',
'chapters/connections/holomorphic_topological.tex',
'chapters/connections/kontsevich_integral.tex',
'chapters/connections/physical_origins.tex',
'chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex',
'chapters/connections/thqg_concordance_supplement.tex',
'chapters/connections/thqg_critical_string_dichotomy.tex',
'chapters/connections/thqg_fredholm_partition_functions.tex',
'chapters/connections/thqg_gravitational_complexity.tex',
'chapters/connections/thqg_gravitational_s_duality.tex',
'chapters/connections/thqg_gravitational_yangian.tex',
'chapters/connections/thqg_holographic_reconstruction.tex',
'chapters/connections/thqg_modular_bootstrap.tex',
'chapters/connections/thqg_perturbative_finiteness.tex',
'chapters/connections/thqg_preface_supplement.tex',
'chapters/connections/thqg_soft_graviton_theorems.tex',
'chapters/connections/thqg_symplectic_polarization.tex',
'chapters/connections/twisted_holography_quantum_gravity.tex',
'chapters/connections/typeA_baxter_rees_theta.tex',
'chapters/connections/ym_boundary_theory.tex',
'chapters/connections/ym_higher_body_couplings.tex',
'chapters/connections/ym_instanton_screening.tex',
'chapters/examples/toroidal_elliptic.tex',
'chapters/frame/preface_section1_draft.tex',
'chapters/frame/preface_section1_v2.tex',
'chapters/frame/preface_sections10_13_draft.tex',
'chapters/frame/preface_sections2_4_draft.tex',
'chapters/frame/preface_sections5_9_draft.tex',
]
include_re = re.compile(r'\\\\(?:input|include)\\{(["'^}]+)'"\\}')

def strip_comments(line: str):
    out=[]
    i=0
    while i < len(line):
        c=line[i]
        if c=='%':
            bs=0
            j=i-1
            while j>=0 and line[j]=='\\\\':
                bs+=1
                j-=1
            if bs%2==0:
                break
        out.append(c)
        i+=1
    return ''.join(out)

tex_files = sorted(root.rglob('*.tex'))
active_inbound={rel:[] for rel in orphans}
all_mentions={rel:[] for rel in orphans}
for tex in tex_files:
    reltex = tex.relative_to(root).as_posix()
    lines = tex.read_text(errors='ignore').splitlines()
    for i, line in enumerate(lines,1):
        clean=strip_comments(line)
        for m in include_re.finditer(clean):
            tgt = m.group(1).strip()
            if not tgt:
                continue
            if not tgt.endswith('.tex'):
                tgt += '.tex'
            if tgt in active_inbound:
                active_inbound[tgt].append((reltex,i,line.strip()))
        for rel in orphans:
            short = rel[:-4]
            if short in line or Path(rel).name in line:
                all_mentions[rel].append((reltex,i,line.strip()))

for rel in orphans:
    print('FILE', rel)
    print('ACTIVE', len(active_inbound[rel]))
    for r in active_inbound[rel][:5]:
        print(' ',f'{r[0]}:{r[1]}:{r[2][:160]}')
    print('MENTIONS', len(all_mentions[rel]))
    for r in all_mentions[rel][:8]:
        print(' ',f'{r[0]}:{r[1]}:{r[2][:160]}')
    print('---')
PY" in /Users/raeez/chiral-bar-cobar
thinking
**Considering scanning speed**

I'm wondering if the scanning process is still running. With the nested loops at 31 lines, it might be okay, but I could see it becoming slower. I think it might make sense to wait a bit longer to see how it progresses. It’s important to ensure everything is running smoothly without unnecessary delays, right? I guess I'll keep an eye on it!

thinking
**Considering code comments**

I notice that the master branch has a commented-out input at 1493, but it lacks a migration note, which stands out compared to the neighboring comments. This makes me think it was likely intended but remains unfinished. It’s interesting how even small details like this can hint at the developer's intentions. I wonder if other parts of the code also show similar signs of being in progress.
exec
/bin/zsh -lc "sed -n '1486,1498p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Parts~\ref{part:bar-complex}--\ref{part:seven-faces} develop the proved core, its standard computations, its
bridges to adjacent programmes, and the centrepiece collision-residue
identification. Part~\ref{part:v1-frontier} enters the frontier: modular holography,
higher-spin geometry, entanglement, and the open problems toward which
the engine points.

\input{chapters/connections/frontier_modular_holography_platonic}
% \input{chapters/connections/twisted_holography_quantum_gravity}
% thqg_open_closed_realization promoted to Part II (The Characteristic Datum)
\input{chapters/connections/entanglement_modular_koszul}
\input{chapters/connections/thqg_entanglement_programme}
\input{chapters/connections/holographic_codes_koszul}
\input{chapters/connections/semistrict_modular_higher_spin_w3}

thinking
**Inspecting commentary context**

It seems the comment I received just mentions "open_closed promoted," which feels a bit vague. The master left a comment without any rationale, which makes me wonder if it's incomplete. I should check the preface for any references to a supplement related to this, or if something is missing. I’ll need to do a little bit of searching to clarify things!
exec
/bin/zsh -lc "rg -n 'thqg_preface_supplement|twisted holography|quantum gravity programme' chapters/frame/preface.tex chapters/frame/heisenberg_frame.tex main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Evaluating unfinished work**

I'm considering how to handle unfinished work for the audit. Marking items as "orphan" with fixes like "archive/remove" seems reasonable. Since a whole chapter is excluded from the main work and has no call site, I might move it to an archive. For files with migration notes, moving them to Vol II/III is the fix. For drafts, I should either integrate them into `preface.tex` or delete them if they're outdated. I also need to look for possible duplicates in `preface.tex`. Verification is key.
codex
I’ve confirmed the first obvious pattern: several orphan files announce in their own headers that they are drafts, supplements, or section fragments. I’m checking the live preface/frontier chapters next to determine whether each one is missing integration or is just dead ballast that should be archived.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\providecommand{\cZ}{\mathcal{Z}}
\providecommand{\cA}{\mathcal{A}}
\providecommand{\barB}{\overline{B}}
\providecommand{\gAmod}{\mathfrak{g}_{\cA}^{\mathrm{mod}}}
\providecommand{\MC}{\text{MC}}
\providecommand{\cM}{\mathcal{M}}
\providecommand{\cC}{\mathcal{C}}
\providecommand{\cO}{\mathcal{O}}
\providecommand{\cP}{\mathcal{P}}
\providecommand{\Eone}{E_1}
\providecommand{\Convinf}{\mathrm{Conv}_\infty}
\providecommand{\Convstr}{\mathrm{Conv}_{\mathrm{str}}}
\providecommand{\orline}[1]{\mathrm{or}(#1)}
\providecommand{\fg}{\mathfrak{g}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}

\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\label{ch:preface}
\markboth{Preface}{Preface}
 succeeded in 50ms:
\section{Modular holography on the proved core: reconstruction, transposition, quantization, and metaplectic anomaly}
\label{sec:frontier-modular-holography-platonic}
\index{holography!modular proved core|textbf}
\index{modular homotopy theory!holography|textbf}
\index{metaplectic correction!holographic kernel|textbf}
\index{determinant anomaly!holographic sewing|textbf}

The proved modular Koszul core supplies the holographic package:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the bar--cobar transform and its Verdier intertwining
 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}},
 Theorem~\textup{\ref{thm:higher-genus-inversion}}\textup{)},
\item the genus-$g$ ambient complex
 $\mathbf C_g(\cA)=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\cA))$
 together with the Verdier involution $\sigma$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)},
\item the complementary-Lagrangian decomposition
 $\mathbf C_g(\cA)\simeq \mathbf Q_g(\cA)\oplus \mathbf Q_g(\cA^!)$
 \textup{(}Lemma~\textup{\ref{lem:involution-splitting}},
 Theorem~\textup{\ref{thm:quantum-complementarity-main}},
 succeeded in 51ms:
\chapter{The Gaussian Archetype}\label{ch:heisenberg-frame}

One generator. One relation.
\[
J(z)\,J(w) \;\sim\; \frac{k}{(z-w)^2}.
\]
If bar-cobar duality fails for this OPE, it fails everywhere.
The Heisenberg vertex algebra $\mathcal{H}_k$ is the simplest
chiral algebra: a single current $J$ of conformal weight~$1$,
a level $k \in \mathbb{C}$, a double pole, nothing else. It is
the abelian Kac--Moody algebra at level~$k$; equivalently, the
boundary algebra of abelian Chern--Simons theory on $\Sigma \times
\mathbb{R}_+$. Every construction in this monograph is already
present, in closed form, in the residues of this single OPE.
The programme must be tested here first.

Extract the double-pole coefficient at a collision $z_i \to z_j$
inside the Fulton--MacPherson compactification
$\overline{C}_n(X)$: the result is $k$ times the logarithmic
form $\eta_{ij} = d\log(z_i - z_j)$. Three points suffice.

thinking
**Checking for duplicate content**

I need to determine if the draft files contain duplicate preface content. It seems likely since preface.tex already has sections labeled 1 and so on. I think I'll search using exact section titles to confirm. Using a tool like rg might be helpful for this search, as it can efficiently look through the files. I really want to make sure everything is in order!
exec
/bin/zsh -lc "rg -n '"'^'"\\\\section\\*\\{|"'^'"\\\\noindent\\\\textbf\\{|The ordered bar construction on algebraic curves|The open/closed world \\(Volume~II\\)|The bar construction on algebraic curves' chapters/frame/preface.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_section1_v2.tex chapters/frame/preface_sections2_4_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/frame/preface_sections10_13_draft.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/frame/preface_sections10_13_draft.tex:7:\noindent\textbf{The open/closed world (Volume~II).}
chapters/frame/preface_sections10_13_draft.tex:195:\noindent\textbf{Modular PVA quantization.}
chapters/frame/preface_sections10_13_draft.tex:277:\noindent\textbf{Holographic modular Koszul duality.}
chapters/frame/preface_sections10_13_draft.tex:367:\noindent\textbf{Completion and the frontier.}
chapters/frame/preface_sections10_13_draft.tex:478:\noindent\textbf{The boxed machine.}
chapters/frame/preface_sections10_13_draft.tex:533:\noindent\textbf{The computational infrastructure.}
chapters/frame/preface_sections10_13_draft.tex:569:\noindent\textbf{The single open problem.}
chapters/frame/preface_sections5_9_draft.tex:19:\section*{5.\quad The modular tangent complex and Chern--Weil theory}
chapters/frame/preface_sections5_9_draft.tex:29:\noindent\textbf{The scalar curvature $\kappa(\cA)$.}\enspace
chapters/frame/preface_sections5_9_draft.tex:76:\noindent\textbf{The spectral discriminant $\Delta_\cA(x)$.}\enspace
chapters/frame/preface_sections5_9_draft.tex:110:\noindent\textbf{The quartic shadow
chapters/frame/preface_sections5_9_draft.tex:261:\section*{6.\quad The shadow obstruction tower}
chapters/frame/preface_sections5_9_draft.tex:450:\noindent\textbf{Shadow growth rate.}\enspace
chapters/frame/preface_sections5_9_draft.tex:510:\section*{7.\quad The standard landscape}
chapters/frame/preface_sections5_9_draft.tex:595:\noindent\textbf{Heisenberg} (class G).
chapters/frame/preface_sections5_9_draft.tex:606:\noindent\textbf{Affine Kac--Moody} (class L).
chapters/frame/preface_sections5_9_draft.tex:622:\noindent\textbf{Virasoro} (class M).
chapters/frame/preface_sections5_9_draft.tex:635:\noindent\textbf{$\mathcal W_3$} (class M).
chapters/frame/preface_sections5_9_draft.tex:656:\noindent\textbf{$\beta\gamma$ system} (class C).
chapters/frame/preface_sections5_9_draft.tex:668:\noindent\textbf{Lattice vertex algebras} (class G).



thinking
**Organizing draft files**

I'm seeing that the draft files have some duplicate content in preface.tex, so I should fix that by archiving or deleting the drafts. I need to check the line ranges for duplicates. Similarly, for the toroidal_elliptic, a comment indicates it's been moved to Vol III, so I'll archive or move it too. I should search for the actual comment line. It seems easier to cite `main.tex:1347` rather than an orphan file to keep things clean. I'll consider how to structure citations for any orphan entries that aren’t mentioned in the main file.
thinking
**Addressing orphan files**

I noticed an issue in main.tex at line 1347. The input for `toroidal_elliptic` is commented out, leaving it as a 4694-line orphan even though the comment states it was moved to Vol III. My plan is to remove the stale Vol I file from `chapters/examples/` and archive it correctly under Vol III. However, I should check if `concordance.tex` is meant to stay out of the main file, as AGENTS references it as essential. I need to investigate if `master_concordance.tex` is the version meant for main or if `concordance.tex` is intentionally excluded.
thinking
**Inspecting master concordance**

I need to take a closer look at the top of the master_concordance.tex file. I wonder what specific details I'm looking for there and how they might impact the overall project. I’ll approach this step by step, making sure I understand the context and purpose of each part. Hopefully, this will allow me to clarify anything that seems unclear or out of place. Let’s see what I find!
exec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/master_concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\chapter{Master concordance: the seven-face programme across three volumes}
\label{ch:master-concordance}

\begin{abstract}
The collision residue of the universal Maurer--Cartan element admits
seven distinct but equivalent presentations. The cross-volume
dictionary records the identification
\[
 r(z) \;=\; \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cA})
 \;\in\; \cA^{!}\otimes\cA^{!}\,[\![z^{-1}]\!].
\]
Each face appears in all three volumes, specialized to the
appropriate setting: chiral algebras on curves (Vol~I), 3d
holomorphic-topological QFT (Vol~II), and Calabi--Yau quantum groups
(Vol~III). The trilingual dictionary below records the chapter and
section coordinates of each face in each volume, together with the
paper of origin and the pointwise status of each face as proved, cited,
or conjectured. The seven faces comprise a single mathematical object
presented in seven dialects; the master theorem of this chapter states
their mutual identification, and the tables that follow localize the
exec
/bin/zsh -lc "sed -n '1504,1513p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

% Master concordance: the trilingual dictionary connecting the seven-face
% programme across all three volumes. Placed after the constitution
% (concordance.tex) and after outlook.tex so that it serves as the final
% navigation index of Vol~I, pointing to the corresponding chapters in
% Vol~II (3d HT QFT) and Vol~III (Calabi--Yau quantum groups).
\input{chapters/connections/master_concordance}
\fi

% ======================================================================


thinking
**Clarifying section files**

I'm looking at the child files designated as section files, which seem to contain comments stating, "Section file for Chapter: Twisted Holography and Quantum Gravity." This suggests that they’re organized by chapter and potentially hold relevant content or notes related to that specific topic. I want to make sure I understand their purpose so I can help appropriately! If there’s more context needed, feel free to provide it!
thinking
**Considering findings structure**

I’m thinking about organizing findings per cluster root with related child lists. This might meet the request for exhaustive surfacing, but it’s tricky because the user wants findings for every individual file. The main cluster root could serve as a finding, but I might need additional findings for each second-order failure. However, that could get noisy. It seems better to document one finding for the root and separate findings for orphan section files, like those with "thqg_preface_supplement." I need to accurately count the files and findings—should be around 100 total chapter .tex files, but I should confirm with an inventory count, which I think is 113.
codex
I’ve confirmed a second-order failure: some orphans are not isolated files, they are whole dead subgraphs. `concordance.tex` drops its own supplement, and `twisted_holography_quantum_gravity.tex` strands ten section files behind a commented-out root include in `main.tex`.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar')
print(sum(1 for _ in (root/'chapters').rglob('*.tex')))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
113

thinking
**Calculating line counts**

I'm thinking about the total line counts for the chapters. I've got chapter 113 and it’s reachable for 82 and orphaned for 31. I wonder if it’s necessary to find the total line counts for the unreachable chapters. Maybe I can compute that, but then again, do I really need to? I’m weighing my options about whether this task is essential or if I can move on to something else.
exec
/bin/zsh -lc "rg -n 'casimir_divisor_core_transport|dg_shifted_factorization_bridge|shifted_rtt_duality_orthogonal_coideals|editorial_constitution|ym_boundary_theory|ym_higher_body_couplings|ym_instanton_screening|toroidal_elliptic|preface_section1_draft|preface_section1_v2|preface_sections10_13_draft|preface_sections2_4_draft|preface_sections5_9_draft|thqg_preface_supplement|twisted_holography_quantum_gravity|concordance.tex|thqg_concordance_supplement' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./main.tex:1347: % \input{chapters/examples/toroidal_elliptic} % Moved to Vol III
./main.tex:1402: % \input{chapters/connections/ym_boundary_theory} % Migrated to Vol II
./main.tex:1403: % \input{chapters/connections/ym_higher_body_couplings} % Migrated to Vol II
./main.tex:1404: % \input{chapters/connections/ym_instanton_screening} % Migrated to Vol II
./main.tex:1409: % \input{chapters/connections/casimir_divisor_core_transport} % migrated to Vol II Part II
./main.tex:1411: % \input{chapters/connections/shifted_rtt_duality_orthogonal_coideals} % migrated to Vol II Part II
./main.tex:1412: % \input{chapters/connections/dg_shifted_factorization_bridge} % removed; content in Vol II Part II
./main.tex:1493:% \input{chapters/connections/twisted_holography_quantum_gravity}
./main.tex:1507:% (concordance.tex) and after outlook.tex so that it serves as the final
./main.tex:1561: \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
./main.tex:1563: \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
./main.tex:1575: \phantomsection\label{subsec:concordance-holographic-completion}% % concordance.tex
./main.tex:1579: \phantomsection\label{rem:yangian-ordered-boundary-face}% % dg_shifted_factorization_bridge.tex
./main.tex:1586: \phantomsection\label{chap:concordance}% % concordance.tex (not in guide_to_main_results.tex)
./main.tex:1590: % twisted_holography_quantum_gravity.tex phantom labels
./main.tex:1595: \phantomsection\label{rem:pixton-genus2-computation}% % concordance.tex
./main.tex:1596: \phantomsection\label{rem:pixton-conjecture-status}% % concordance.tex
./main.tex:1614: \phantomsection\label{chap:casimir-divisor}% % casimir_divisor_core_transport.tex (migrated to Vol II)
./main.tex:1615: \phantomsection\label{thm:pbw-recurrence}% % casimir_divisor_core_transport.tex (migrated to Vol II)
./main.tex:1616: \phantomsection\label{thm:growth-mode-factorization}% % casimir_divisor_core_transport.tex (migrated to Vol II)

thinking
**Analyzing file changes**

I've got some clues from `outlook.tex`. It mentions replacing concordance and editorial_constitution in the current frontier build. So it seems those were intentionally replaced by outlook, but they're still under chapters. I should consider whether to archive or delete them. I need to take a closer look at the top of `outlook.tex` for more insights. That should help clarify the necessary steps!
exec
/bin/zsh -lc "sed -n '1,80p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
% ======================================================================
% OUTLOOK — Replaces concordance + editorial_constitution in the
% monograph proper. Contains the mathematical architecture (three
% pillars, three rings, five main theorems) and key definitions
% referenced from theory chapters. The full concordance with
% literature comparisons, conjecture stratification, and research
% programmes is available as a standalone companion document
% (standalone/editorial.tex).
% ======================================================================

\chapter{Outlook}
\label{chap:outlook}

\index{concordance|textbf}

\section{The five main theorems}
\label{sec:outlook-five-theorems}

The algebraic engine rests on five theorems, all proved:


thinking
**Inspecting for issues**

I need to assess whether there's a subtle issue with phantom labels. It seems like an audit is necessary, especially focused on the section from lines 1550 to 1675. I should investigate this block closely to identify any inconsistencies or problems. Checking these lines will hopefully clarify if there are issues that need addressing. Let's explore the details in that specific range!
codex
I’ve reached the subtle layer now. `main.tex` is not just omitting chapter files; it also injects phantom labels for several omitted chapters, which can hide the omission because cross-references still resolve. I’m verifying that block before I write findings.
exec
/bin/zsh -lc "sed -n '1552,1678p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
 \phantomsection\label{thm:euler-koszul-tier-classification}% % genus_complete.tex
 \phantomsection\label{def:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex





thinking
**Inspecting documents for clarity**

I need to highlight that phantom labels in the annals can obscure missing items, which could be critical. I should check for any orphan files in specific documents and see if there are replacements or superseded drafts. I might look for comments in `outlook` or `preface` to inform my decisions. Archiving or deleting drafts might be necessary, and I should compute counts to summarize findings effectively, with the user expecting a specific number of findings.
thinking
**Defining findings and severity**

I’ve been thinking about how to set the number of findings to report. I might consider using each orphan file as an individual finding, which would give me 31 findings total. That approach could be lengthy but manageable, perhaps around 50-70 lines including a concise summary. I'll need to ensure each reference is clear and concise while categorizing them by severity. For example, I could highlight critical issues like phantom labels masking orphan chapters as one finding.
thinking
**Listing findings individually**

I’m considering whether to list findings individually without clustering them. If I do that, I could include both the root comments and associated child orphans. This approach might make it easier to categorize their severity as high or medium individually instead. It seems like a more precise method to ensure that each finding gets the attention it deserves. I’ll need to weigh the clarity of this method against the potential length of the report.
thinking
**Fixing document structure**

I need to fix the structure of my document. It looks like I have a choice: either restore the old `\input{chapters/connections/concordance}` before `master_concordance` or move `concordance.tex` to either `standalone` or `archive`. There's also the stale comments in `main.tex` to remove. The same goes for `editorial_constitution.tex` since it's replaced by `outlook.tex`. I also need to archive `thqg_concordance_supplement` if I move `concordance.tex`. Lastly, I should check about `thqg_preface_supplement`.
thinking
**Inspecting supplement and structure**

It seems the THQG chapter might intentionally be dropped since its root version is commented out. I think the best fix is to archive the supplement along with the THQG materials. If the chapter is excluded, then the preface supplement should also go. The file header suggests it was intended for insertion, but the current book format doesn’t include THQG. I should check if the `preface` already includes the open/closed world and completion/frontier sections, as that might render the supplement outdated. Let’s look at the first few lines of the supplement for clarity.
exec
/bin/zsh -lc "sed -n '1,80p' chapters/connections/thqg_preface_supplement.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
% Preface supplement: Twisted Holography and Quantum Gravity programme.
% Inserted near the end of the preface chapter via \input.

\bigskip
\begin{center}
\rule{0.6\textwidth}{0.4pt}
\end{center}
\bigskip

\section*{IV.\quad Twisted holography and quantum gravity}

\noindent
The twelve sections above construct the universal Maurer--Cartan
element~$\Theta_\cA$ and its projections for every standard
chiral algebra. This final section asks what these constructions
say about gravity.

A three-dimensional holomorphic-topological (HT) field theory~$T$
on $\R_+\times\C$ is a functor from the bordism category of
surfaces with complex structure and intervals with orientation to



thinking
**Exploring document issues**

I’m considering citing main files 1589 and 1590, thinking it might help clarify nuances. I need to look into `twisted_holography_quantum_gravity.tex` to check its status. It seems there are issues with phantom labels and unreachable sections that need to be fixed. I might organize findings based on the necessary fixes, either by restoring missing components or by moving out entire clusters. Listing orphan files with suggested fixes could help streamline the process.
thinking
**Identifying document connections**

I'm noticing a specific problem in the chapters/connections directory with `twisted_holography_quantum_gravity.tex`. The master chapter at line 505 is unreachable because the only root in `main.tex` at line 1493 is commented out. This means that all ten section files it attempts to input are essentially dead. I should figure out how to fix this issue to restore access to these sections, as they’re currently cut off from the main document.
thinking
**Clarifying file structure fixes**

I see that since `outlook.tex:1` mentions replacing the concordance in the main monograph, the ideal fix is to move the concordance out of chapters and into standalone. But I wonder why the main comment refers to placing it after the constitution; that seems outdated now. Maybe the fix is to simply archive or move the concordance instead of including it. I might need to check if `standalone/editorial.tex` actually exists to clarify this.
exec
/bin/zsh -lc "rg --files standalone -g 'editorial*.tex' -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
standalone/computations.tex
standalone/N6_shadow_formality.tex
standalone/gaudin_from_collision.tex
standalone/ordered_chiral_homology.tex
standalone/programme_summary_section1.tex
standalone/programme_summary_sections5_8.tex
standalone/virasoro_r_matrix.tex
standalone/N4_mc4_completion.tex
standalone/riccati.tex
standalone/cover_letter_garland_lepowsky.tex
standalone/programme_summary_sections9_14.tex
standalone/cover_letter_virasoro_r_matrix.tex
standalone/garland_lepowsky.tex
standalone/genus1_seven_faces.tex
standalone/survey_modular_koszul_duality_v2.tex
standalone/N2_mc3_all_types.tex
standalone/cover_letter_shadow_towers.tex
standalone/w3_holographic_datum.tex
standalone/bp_self_duality.tex
standalone/introduction_full_survey.tex
exec
/bin/zsh -lc "rg --files -g '*casimir_divisor_core_transport*' -g '*dg_shifted_factorization_bridge*' -g '*shifted_rtt_duality_orthogonal_coideals*' -g '*ym_boundary_theory*' -g '*ym_higher_body_couplings*' -g '*ym_instanton_screening*' -g '*toroidal_elliptic*'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/toroidal_elliptic.tex
chapters/connections/ym_instanton_screening.tex
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex
rectification_20260412_233715/R16_toroidal_elliptic_v3.md
chapters/connections/dg_shifted_factorization_bridge.tex
chapters/connections/ym_boundary_theory.tex
rectification_20260412_233715/R15_toroidal_elliptic_v1.md
chapters/connections/casimir_divisor_core_transport.tex
chapters/connections/ym_higher_body_couplings.tex
exec
/bin/zsh -lc "rg --files -g '*standalone*.tex' | rg 'casimir|shifted|ym_|toroidal|concordance|editorial|thqg'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg --files | rg 'casimir_divisor_core_transport_standalone|editorial|concordance'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
wave2_audit_20260413_001942/S13_concordance_to_body.md
wave2_audit_20260413_001942/C17_concordance.md
chapters/connections/master_concordance.tex
chapters/connections/concordance.tex
chapters/connections/thqg_concordance_supplement.tex
chapters/connections/editorial_constitution.tex
rectification_20260412_233715/R14_concordance.md
compute/lib/theorem_concordance_rectification_engine.py
compute/tests/test_theorem_concordance_rectification_engine.py

thinking
**Identifying wrapper issues**

I'm noticing that there's no wrapper for the file `casimir_divisor_core_transport.tex`, which makes the header claiming a standalone wrapper seem misleading or even completely missing. That could be a subtle issue to highlight. I wonder if other orphan files claim to have wrappers too. It might be helpful to perform a search for "standalone wrapper" in those orphan files. Let's investigate further to clarify this!
exec
/bin/zsh -lc "rg -n 'standalone wrapper|To be integrated|Inserted near the end|migrated to|Moved to|absorbed into|replaces' chapters/connections chapters/frame chapters/examples chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface_sections10_13_draft.tex:397:The multiplicity-free $\ell$-weight property (Chari--Moura) replaces the
chapters/connections/physical_origins.tex:5:This chapter has been absorbed into Volume~II\@. The physical
chapters/frame/preface_sections2_4_draft.tex:2:% To be integrated into preface.tex
chapters/frame/preface_sections2_4_draft.tex:416:the operadic bar construction, replaces trees by stable graphs:
chapters/frame/preface_sections2_4_draft.tex:1215:\noindent\textbf{Corollary} (MC replaces the sum over topologies).
chapters/connections/thqg_gravitational_yangian.tex:1126:Using $z_{31} = -z_{13}$ (the sign is absorbed into the skew-symmetry
chapters/examples/w_algebras_deep.tex:2151:replaces the deconfined phase (finitely many shadow degrees, simple
chapters/frame/preface.tex:1329:the operadic bar construction, replaces trees by stable graphs:
chapters/frame/preface.tex:2147:\noindent\textbf{Corollary} (MC replaces the sum over topologies).
chapters/frame/preface.tex:3224: Heisenberg one-particle reduction replaces spectral-zeta
chapters/frame/preface.tex:4135:The multiplicity-free $\ell$-weight property (Chari--Moura) replaces the
chapters/examples/lattice_foundations.tex:194:is absorbed into the grading; the exponential weight damping
chapters/examples/lattice_foundations.tex:2939:The dual form $-q \equiv 2 \pmod{3}$ replaces $q(\alpha_i,\alpha_j) = 1$
chapters/examples/lattice_foundations.tex:4231:(Theorem~\ref{thm:lattice:factorization-koszul}(ii)) replaces
chapters/examples/lattice_foundations.tex:4274:finiteness (Remark~\ref{rem:lattice:sectorwise-finiteness}) replaces
chapters/examples/lattice_foundations.tex:4752:poles. The genus-$1$ propagator on $E_\tau$ replaces
chapters/frame/heisenberg_frame.tex:169: coupling both pole orders, replaces the Jacobi identity. The PBW
chapters/frame/heisenberg_frame.tex:3638:\eqref{eq:cs-hinge-degree-n-amplitude} replaces the pair of
chapters/frame/heisenberg_frame.tex:4449:ordered: $\overline{C}_n^{\mathrm{ord}}(X)$ replaces
chapters/theory/higher_genus_modular_koszul.tex:27:Fiberwise curvature is absorbed into the genus expansion; the price is

thinking
**Inspecting editorial references**

I need to see if the term `editorial_constitution` is referenced or if it has been replaced. I’ll search for this string, focusing on the main phantom or outlook sections. That seems like a good starting point. Additionally, it will be helpful to inspect the main lines from 1397 to 1412, particularly looking at those commented-out migrated chapters. This could provide clarity on what changes have been made.
exec
/bin/zsh -lc "sed -n '1395,1413p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\ifannalsedition\else
 % --- Archive-only: physics-facing bridges and frontier connections ---
 % \input{chapters/connections/holomorphic_topological} % migrated to Vol II Part V
 % \input{chapters/connections/kontsevich_integral} % migrated to Vol II Part III
 % \input{chapters/connections/physical_origins} % 19-line stub; content absorbed into Vol II
 \input{chapters/connections/genus_complete}
 % Yang--Mills boundary theory — migrated to Vol II Part V
 % \input{chapters/connections/ym_boundary_theory} % Migrated to Vol II
 % \input{chapters/connections/ym_higher_body_couplings} % Migrated to Vol II
 % \input{chapters/connections/ym_instanton_screening} % Migrated to Vol II
 % Derived structures and geometric Langlands
 \input{chapters/theory/derived_langlands}
 % --- Promoted from appendices: substantial bridge chapters ---
 % spectral_sequences and existence_criteria moved to Appendices (EXEC-17)
 % \input{chapters/connections/casimir_divisor_core_transport} % migrated to Vol II Part II
 % \input{chapters/connections/typeA_baxter_rees_theta} % migrated to Vol II Part II
 % \input{chapters/connections/shifted_rtt_duality_orthogonal_coideals} % migrated to Vol II Part II
 % \input{chapters/connections/dg_shifted_factorization_bridge} % removed; content in Vol II Part II
\fi
exec
/bin/zsh -lc "rg --files | rg '"'^casimir_divisor_core_transport_standalone'"\\.tex"'$|/casimir_divisor_core_transport_standalone'"\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Checking orphan files**

I think I need to look for orphan files that could mention nonexistent wrappers, but I’m not so sure if that will yield anything. It might help to use results from an explorer agent, but that’s still pending. There could be something there eventually, so it’s worth investigating further. I just want to make sure I’m thorough in this search. Let’s check and see what I can find!
collab wait(call_q6xObvkt7nDanWSE9l0TJAmP)
  receivers: 019d8419-1820-7d82-89c4-2fbd5df38a7a
wait(call_q6xObvkt7nDanWSE9l0TJAmP) 1 agents complete:
  019d8419-1820-7d82-89c4-2fbd5df38a7a completed: "Reachable:
- `chapters/connections/arithmetic_shadows.tex`: `main.tex → chapters/connections/arithmetic_shadows.tex`
- `…"
collab close_agent(call_we68q57R3YpFaTn2cCnoBILc)
  receiver: 019d8419-1820-7d82-89c4-2fbd5df38a7a
close_agent(call_we68q57R3YpFaTn2cCnoBILc) completed: "Reachable:
- `chapters/connections/arithmetic_shadows.tex`: `main.tex → chapters/connections/arithmetic_shadows.tex`
- `…":
  receiver: 019d8419-1820-7d82-89c4-2fbd5df38a7a

thinking
**Verifying orphan files**

I’m considering if there are orphans among the included subfiles, although my script indicated there shouldn’t be. I need to check if `yg_foundations` and other files are reachable by `yangians.tex`. I could mention that I checked 113 findings, which included 31 or 33. Perhaps not all orphans are unfinished, as some may be archived. I’ll do one more verification of our orphan list with active inbound edges using an efficient script on our parsed graph.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
root = Path('/Users/raeez/chiral-bar-cobar')
orphans = [
'chapters/connections/casimir_divisor_core_transport.tex',
'chapters/connections/concordance.tex',
'chapters/connections/dg_shifted_factorization_bridge.tex',
'chapters/connections/editorial_constitution.tex',
'chapters/connections/holomorphic_topological.tex',
'chapters/connections/kontsevich_integral.tex',
'chapters/connections/physical_origins.tex',
'chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex',
'chapters/connections/thqg_concordance_supplement.tex',
'chapters/connections/thqg_critical_string_dichotomy.tex',
'chapters/connections/thqg_fredholm_partition_functions.tex',
'chapters/connections/thqg_gravitational_complexity.tex',
'chapters/connections/thqg_gravitational_s_duality.tex',
'chapters/connections/thqg_gravitational_yangian.tex',
'chapters/connections/thqg_holographic_reconstruction.tex',
'chapters/connections/thqg_modular_bootstrap.tex',
'chapters/connections/thqg_perturbative_finiteness.tex',
'chapters/connections/thqg_preface_supplement.tex',
'chapters/connections/thqg_soft_graviton_theorems.tex',
'chapters/connections/thqg_symplectic_polarization.tex',
'chapters/connections/twisted_holography_quantum_gravity.tex',
'chapters/connections/typeA_baxter_rees_theta.tex',
'chapters/connections/ym_boundary_theory.tex',
'chapters/connections/ym_higher_body_couplings.tex',
'chapters/connections/ym_instanton_screening.tex',
'chapters/examples/toroidal_elliptic.tex',
'chapters/frame/preface_section1_draft.tex',
'chapters/frame/preface_section1_v2.tex',
'chapters/frame/preface_sections10_13_draft.tex',
'chapters/frame/preface_sections2_4_draft.tex',
'chapters/frame/preface_sections5_9_draft.tex',
]
include_re = re.compile(r'\\\\(?:input|include)\\{(["'^}]+)'"\\}')

def strip_comments(line: str):
    out=[]
    i=0
    while i < len(line):
        c=line[i]
        if c=='%':
            bs=0
            j=i-1
            while j>=0 and line[j]=='\\\\':
                bs+=1
                j-=1
            if bs%2==0:
                break
        out.append(c)
        i+=1
    return ''.join(out)

inbound = {o: [] for o in orphans}
for tex in [root/'main.tex'] + list((root/'chapters').rglob('*.tex')):
    rel = tex.relative_to(root).as_posix()
    for i, line in enumerate(tex.read_text(errors='ignore').splitlines(),1):
        s = strip_comments(line)
        for m in include_re.finditer(s):
            target = m.group(1).strip()
            if not target.endswith('.tex'):
                target += '.tex'
            if target in inbound:
                inbound[target].append((rel,i))
for o, parents in inbound.items():
    if parents:
        print(o)
        for p in parents:
            print(' ',p[0],p[1])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 580ms:
chapters/connections/thqg_concordance_supplement.tex
  chapters/connections/concordance.tex 6620
chapters/connections/thqg_critical_string_dichotomy.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 503
chapters/connections/thqg_fredholm_partition_functions.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 504
chapters/connections/thqg_gravitational_complexity.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 496
chapters/connections/thqg_gravitational_s_duality.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 498
chapters/connections/thqg_gravitational_yangian.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 499
chapters/connections/thqg_holographic_reconstruction.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 502
chapters/connections/thqg_modular_bootstrap.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 501
chapters/connections/thqg_perturbative_finiteness.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 495
chapters/connections/thqg_soft_graviton_theorems.tex
  chapters/connections/twisted_holography_quantum_gravity.tex 500
exec
/bin/zsh -lc "rg -n 'preface_section1_draft|preface_section1_v2|preface_sections10_13_draft|preface_sections2_4_draft|preface_sections5_9_draft' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./chapters/frame/preface_sections2_4_draft.tex:1:% preface_sections2_4_draft.tex — Sections 2-4 of the Restored Preface
./chapters/frame/preface_sections5_9_draft.tex:1:% preface_sections5_9_draft.tex — Sections 5-9 of the Restored Preface
./chapters/frame/preface_section1_draft.tex:1:% preface_section1_draft.tex — Section 1 of the Restored Preface
./chapters/frame/preface_section1_v2.tex:1:% preface_section1_v2.tex — Section 1 of the Preface (v2)
exec
/bin/zsh -lc "rg -n 'thqg_preface_supplement|Twisted Holography and Quantum Gravity programme|Twisted holography and quantum gravity' -g '*.tex' main.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/thqg_preface_supplement.tex:1:% Preface supplement: Twisted Holography and Quantum Gravity programme.
chapters/connections/thqg_preface_supplement.tex:10:\section*{IV.\quad Twisted holography and quantum gravity}
chapters/connections/thqg_concordance_supplement.tex:4:\section{Twisted holography and quantum gravity programme}
chapters/connections/concordance.tex:6618:% Twisted holography and quantum gravity programme: sixteen gravitational

thinking
**Searching for replacements**

I need to verify that the terms `concordance` and `editorial_constitution` have been properly replaced with `outlook` and check if there's a missing standalone item. It's important to ensure everything aligns correctly. I wonder if there's a specific way to approach this search that will make it easier for me to find what I need. I’ll make sure to document any findings clearly! Let’s see what I can uncover.
exec
/bin/zsh -lc 'test -f standalone/editorial.tex; echo $?' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Replaces concordance \\+ editorial_constitution|standalone/editorial\\.tex' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\input\\{chapters/connections/concordance\\}|\\\\input\\{chapters/connections/editorial_constitution\\}' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1
 exited 1 in 52ms:

 succeeded in 53ms:
2:% OUTLOOK — Replaces concordance + editorial_constitution in the
8:% (standalone/editorial.tex).


thinking
**Reporting editorial issues**

I think I can report a missing standalone editorial, which seems significant, potentially with medium to high severity. I need to verify the comment in `main.tex`, which implies that the concordance should be included. I'll also check if phantom labels refer to the orphan `holomorphic_topological`. It might be helpful to report a global finding here. If a chapter is migrated or archived, I should ensure to delete its phantom labels and redirect references. Lastly, I need to verify if `physical_origins.tex` is only a stub with 19 lines.
thinking
**Checking orphan content**

I need to fix the remove stub, which sounds good. Maybe I should also compute the total lines of orphan content to get a better understanding. It might be helpful to highlight this as dead surface size since it could be quite significant. Counting those lines could reveal a huge amount. I think summarizing the total lines would provide useful insight into the extent of the orphan content we’re dealing with.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar')
orphans = [
'chapters/connections/casimir_divisor_core_transport.tex',
'chapters/connections/concordance.tex',
'chapters/connections/dg_shifted_factorization_bridge.tex',
'chapters/connections/editorial_constitution.tex',
'chapters/connections/holomorphic_topological.tex',
'chapters/connections/kontsevich_integral.tex',
'chapters/connections/physical_origins.tex',
'chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex',
'chapters/connections/thqg_concordance_supplement.tex',
'chapters/connections/thqg_critical_string_dichotomy.tex',
'chapters/connections/thqg_fredholm_partition_functions.tex',
'chapters/connections/thqg_gravitational_complexity.tex',
'chapters/connections/thqg_gravitational_s_duality.tex',
'chapters/connections/thqg_gravitational_yangian.tex',
'chapters/connections/thqg_holographic_reconstruction.tex',
'chapters/connections/thqg_modular_bootstrap.tex',
'chapters/connections/thqg_perturbative_finiteness.tex',
'chapters/connections/thqg_preface_supplement.tex',
'chapters/connections/thqg_soft_graviton_theorems.tex',
'chapters/connections/thqg_symplectic_polarization.tex',
'chapters/connections/twisted_holography_quantum_gravity.tex',
'chapters/connections/typeA_baxter_rees_theta.tex',
'chapters/connections/ym_boundary_theory.tex',
'chapters/connections/ym_higher_body_couplings.tex',
'chapters/connections/ym_instanton_screening.tex',
'chapters/examples/toroidal_elliptic.tex',
'chapters/frame/preface_section1_draft.tex',
'chapters/frame/preface_section1_v2.tex',
'chapters/frame/preface_sections10_13_draft.tex',
'chapters/frame/preface_sections2_4_draft.tex',
'chapters/frame/preface_sections5_9_draft.tex',
]
print(sum(len((root/p).read_text(errors='ignore').splitlines()) for p in orphans))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
59069








thinking
**Evaluating response structure**

I’m considering how to structure my answer. It looks like I should use a straightforward orphan list along with identifying problems and their fixes. I want to mention any subtle meta findings about phantom labels, as they’re relevant. But I shouldn’t go too far off track. Since they wanted these second-order subtle issues, I’ll add around two meta findings. I also need to decide on how to map the severity.
thinking
**Evaluating file details**

I just calculated the sum of 3+12+10+1+5, which equals 31. That feels good! I should mention that the `concordance.tex` header includes `\input{thqg_concordance_supplement}` at line 6620. It might be worth addressing `thqg_preface_supplement` separately since it’s not in the master. The header says it’s inserted near the end of the preface, but there’s no input for it, making this an orphaned file.
thinking
**Considering user's needs**

I wonder if the user is looking for an audit rather than a code change. An exact fix could still be enlightening, even if it's not applied. For instance, I could suggest adding `\input{chapters/connections/concordance}` before `\input{chapters/connections/master_concordance}` in `main.tex`. However, if `outlook.tex` states that it replaces concordance, it creates an inconsistency that I need to consider. Let's clarify this!
thinking
**Evaluating unfinished work**

I’m thinking about how to address the unfinished work, particularly regarding whether to include the concordance. It seems the better fix might be to remove it from the chapters and create standalone/editorial.tex. Given the current build suggests the book doesn’t intend to include it, I should just relocate orphan concordance.tex out of chapters and update comments instead. As for the missing standalone claim, I can either create the standalone version or stop claiming it altogether.
thinking
**Structuring fixes for orphans**

I’m thinking about how to move concordance.tex out of chapters/ and into the standalone wrapper at standalone/editorial.tex, creating that wrapper if needed. I’ll also delete the stale comments and labels in main.tex. For the thqg_concordance_supplement.tex, I’ll apply the same move. It makes sense to do line moves or possibly group them for clarity. I could also include line references in main for the migrated comments, ensuring each orphan file follows a clear pattern. Having one bullet per orphan file helps keep things organized.
thinking
**Estimating categories**

I'm thinking about how to categorize the current issues. For the critical matters, I'll note them as "CRITICAL meta 1." Then, it seems that a high-priority category should include the orphan cluster that contains active contradictions. This approach will help me stay organized and focused as I tackle each section. I'll make sure to clearly identify these categories to address the issues effectively. Keeping them distinct will guide my next steps better!
thinking
**Ensuring accuracy in references**

I'm thinking about how to make the fix stronger, which is a good step. I also noticed that the `outlook` is missing a standalone editorial. I need to ensure that my line references are accurate. Should I be looking at `main.tex:1554` or possibly 1555? It's important to get this right so everything aligns properly and the overall structure remains solid! Let's double-check those references for clarity.
thinking
**Refining command usage**

I’m trying to figure out how to use the command to get specific line numbers from my file. The first attempt with `sed -n '1552,1678p'` didn’t show the line numbers, so I’ll switch to `nl -ba main.tex | sed -n '1552,1678p'` instead. I should also check around line 1505 for a comment and gather specific includes this way. Gathering the information accurately is important!
codex
I’m at the final verification pass now: exact line numbers for the masking issues in `main.tex`, then I’ll emit the orphan list with fixes only.
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1488,1512p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba main.tex | sed -n '1552,1678p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/outlook.tex | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1488	identification. Part~\ref{part:v1-frontier} enters the frontier: modular holography,
  1489	higher-spin geometry, entanglement, and the open problems toward which
  1490	the engine points.
  1491	
  1492	\input{chapters/connections/frontier_modular_holography_platonic}
  1493	% \input{chapters/connections/twisted_holography_quantum_gravity}
  1494	% thqg_open_closed_realization promoted to Part II (The Characteristic Datum)
  1495	\input{chapters/connections/entanglement_modular_koszul}
  1496	\input{chapters/connections/thqg_entanglement_programme}
  1497	\input{chapters/connections/holographic_codes_koszul}
  1498	\input{chapters/connections/semistrict_modular_higher_spin_w3}
  1499	% --- Promoted from appendices: substantial frontier chapters ---
  1500	\input{chapters/theory/nilpotent_completion}
  1501	\input{chapters/theory/coderived_models}
  1502	\input{chapters/connections/subregular_hook_frontier}
  1503	\input{chapters/connections/outlook}
  1504	
  1505	% Master concordance: the trilingual dictionary connecting the seven-face
  1506	% programme across all three volumes. Placed after the constitution
  1507	% (concordance.tex) and after outlook.tex so that it serves as the final
 succeeded in 51ms:
  1552	% In archive mode the real labels take precedence (these are skipped).
  1553	% ======================================================================
  1554	\ifannalsedition
  1555	 % --- High-frequency labels from archive-only chapters ---
  1556	 \phantomsection\label{thm:general-hs-sewing}% % genus_complete.tex
  1557	 \phantomsection\label{subsec:hs-sewing}% % genus_complete.tex
  1558	 \phantomsection\label{def:hs-sewing}% % genus_complete.tex
  1559	 \phantomsection\label{cor:hs-sewing-standard-landscape}% % genus_complete.tex
  1560	 \phantomsection\label{thm:ds-bar-gf-discriminant}% % landscape_census.tex
  1561	 \phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex
  1562	 % thm:family-index now defined in guide_to_main_results.tex
  1563	 \phantomsection\label{sec:concordance-three-pillars}% % concordance.tex (not in guide_to_main_results.tex)
  1564	 % --- 18 additional phantom stubs (2026-03-29 audit) ---
  1565	 \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
  1566	 \phantomsection\label{thm:heisenberg-one-particle-sewing}% % genus_complete.tex (8 refs)
  1567	 \phantomsection\label{thm:resonance-filtered-bar-cobar}% % nilpotent_completion.tex (3 refs)
  1568	 \phantomsection\label{thm:frontier-protected-bulk-antiinvolution}% % frontier_modular_holography_platonic.tex
  1569	 \phantomsection\label{thm:stabilized-completion-positive}% % nilpotent_completion.tex
  1570	 \phantomsection\label{thm:euler-koszul-tier-classification}% % genus_complete.tex
  1571	 \phantomsection\label{def:frontier-protected-holographic-transform}% % frontier_modular_holography_platonic.tex
 succeeded in 51ms:
     1	% ======================================================================
     2	% OUTLOOK — Replaces concordance + editorial_constitution in the
     3	% monograph proper. Contains the mathematical architecture (three
     4	% pillars, three rings, five main theorems) and key definitions
     5	% referenced from theory chapters. The full concordance with
     6	% literature comparisons, conjecture stratification, and research
     7	% programmes is available as a standalone companion document
     8	% (standalone/editorial.tex).
     9	% ======================================================================
    10	
    11	\chapter{Outlook}
    12	\label{chap:outlook}










thinking
**Clarifying file details**

I should avoid mentioning unsupported claims as facts and ground everything in what I read from actual file contents. For instance, I can state that “main.tex:1402 comments out its only include and marks it 'Migrated to Vol II'” as solid fact. Recommendations can be made based on observations. Regarding file paths, I think using repo-relative paths is fine based on what the user requested. Let’s also ensure I check specific lines in `chapters/examples/toroidal_elliptic.tex` for accurate header and movement details.
thinking
**Finalizing output format**

I need to make sure I'm using semicolons instead of em dashes and avoid nested bullets. I'll go for a flat list with about 33 bullets. It seems helpful to mention my checks on the 113 chapter `.tex` files and how the active graph is rooted at `main.tex`, with comments stripped before parsing, too. I wonder if I could also add a brief summary and mention that I parsed `main.tex` recursively, leading to findings on reachable and orphaned items. But I should ensure there's no room for guesses or inferences.
thinking
**Formatting bullet points**

I'm thinking we can keep each bullet point concise, ideally at one or two lines. With long file names, wrapping might be necessary. I’ll aim for 25-35 words per bullet for clarity.

So, for the 33 bullets, if they're around one line each, that could total roughly 33 lines, maybe even wrapping under 70 lines in rendering. I could focus on shortening repeated phrases about child fixes too.

I wonder about using code formatting around paths and inputs, but it might clutter things. The requested format doesn’t specify backticks, so I think it’s okay to leave them out.
thinking
**Considering chapter fixes**

I’m thinking about how to fix the issue by possibly replacing phantom labels for cut chapters with clear forward references to the active chapter. I wonder if it might also be effective to just delete those references entirely. This might make things clearer. Still, I think even one concise bullet point could be enough to address the matter. It feels like there’s a lot of complexity here, but clarity should be the goal!
thinking
**Drafting structure for fixes**

I'm creating a wrapper and need to double-check the counts, including 33 bullets. It seems good to use severity labels like `[CRITICAL]`, `[HIGH]`, `[MEDIUM]`, and `[LOW]`. I want to group `thqg` child sections under HIGH and focus on fixing repeated issues. So, I’ll make the final draft concise and precise without an intro and mention "orphans" in the problem. Each fix should be exact, stating clearly what to do for each file migration.
thinking
**Deciding on exact fixes**

I think it makes sense to choose deletion because the main comments indicate that certain files are already migrated. So, I’ll say: “FIX: remove this file from Vol I's chapters tree and keep the Vol II/III copy as the only active source; drop its phantom labels from main.tex.” I also need to delete the `dg_shifted_factorization_bridge` from Vol I and clear its labels. Similarly, for `physical_origins`, I’ll delete the stub from Vol I and direct references to Vol II. 

For the THQG cluster, I might consider restoring specific sections while dealing with phantom labels.
thinking
**Considering chapter fixes**

I’m noticing that phantom labels were added instead of deleting references, which might suggest it was an unfinished inclusion rather than a deliberate removal. So, it seems the best exact fix would be to restore the actual chapters instead of leaving those phantom labels. Since the user asked for a review of unfinished work, this feels more aligned with that focus than an archive approach. I’ll need to ensure I’m addressing the unfinished aspects effectively.
thinking
**Organizing project files**

I need to create a standalone wrapper for a project. For the THQG cluster, I’ll restore the master input and remove any phantom files, then add a preface supplement input. For the migrated Volume II/III files, I have to delete or archive them from the Volume I chapters and also eliminate any phantoms there. As for the preface drafts, I'll archive or delete those since the live preface has already integrated that content.
thinking
**Considering document structure**

I need to decide whether to create a `standalone/editorial.tex` that inputs certain chapter files or delete a claim from `outlook.tex`. Creating the wrapper seems best since it aligns with user comments and keeps orphan files intact. The concordance/editorial bullets can suggest moving them into this standalone wrapper instead of keeping them in the chapter graph. This way, they're still recognized, though not in the main graph. The goal remains to have a current repo structure, which might allow for a live compilation path for these orphans.
thinking
**Clarifying orphan status**

So, I need to consider that even if I create a `standalone/editorial.tex`, the files within `chapters/` won't be included in the `main.tex` graph. According to the user's definition, they would be considered orphaned since they're not part of the input graph. This is an important distinction to make because the user's goal seems to focus on ensuring all relevant files are recognized in the compilation process. Keeping them linked somehow would be beneficial.
 succeeded in 9m 46s:
FILE chapters/connections/casimir_divisor_core_transport.tex
FIRST 2:% Body fragment for repository integration.
LINES 1512
REFS 40
  main.tex:1409:% \input{chapters/connections/casimir_divisor_core_transport} % migrated to Vol II Part II
  main.tex:1614:\phantomsection\label{chap:casimir-divisor}% % casimir_divisor_core_transport.tex (migrated to Vol II)
  main.tex:1615:\phantomsection\label{thm:pbw-recurrence}% % casimir_divisor_core_transport.tex (migrated to Vol II)
  main.tex:1616:\phantomsection\label{thm:growth-mode-factorization}% % casimir_divisor_core_transport.tex (migrated to Vol II)
  .claude/worktrees/agent-a074cd40/main.tex:1346:\input{chapters/connections/casimir_divisor_core_transport}
  .claude/worktrees/agent-ab4d244b/main.tex:1346:\input{chapters/connections/casimir_divisor_core_transport}
  .claude/worktrees/agent-a7a899b6/main.tex:1275:\input{chapters/connections/casimir_divisor_core_transport}
  .claude/worktrees/agent-ad4860d3/main.tex:1346:\input{chapters/connections/casimir_divisor_core_transport}
  .claude/worktrees/agent-abc99e5a/main.tex:1275:\input{chapters/connections/casimir_divisor_core_transport}
  .claude/worktrees/agent-ab0fb328/main.tex:1275:\input{chapters/connections/casimir_divisor_core_transport}
  ...
---
FILE chapters/connections/concordance.tex
FIRST 1:\chapter{Concordance with primary literature}
LINES 11309
REFS 603
codex
- [CRITICAL] `main.tex:1554` — PROBLEM: the `\ifannalsedition` block seeds phantom labels for omitted chapter files (`concordance.tex`, `editorial_constitution.tex`, `twisted_holography_quantum_gravity.tex`, multiple migrated Vol II/III files), so cross-references can succeed while the real chapter is absent. FIX: after resolving each orphan below, delete the corresponding phantom labels from `main.tex`; keep phantoms only for intentionally non-chapter targets.

- [HIGH] `chapters/connections/outlook.tex:2` — PROBLEM: `outlook.tex` says the full concordance lives in `standalone/editorial.tex`, but that file does not exist. FIX: create `standalone/editorial.tex` and move the concordance/editorial companion behind that entry point, or delete the claim from `outlook.tex`.

- [HIGH] `chapters/connections/concordance.tex:1` — PROBLEM: 11,309-line constitutional chapter is orphaned; `main.tex:1505-1507` still says `master_concordance` is placed after `concordance.tex`, but there is no active `\input{chapters/connections/concordance}` anywhere. FIX: move this file out of `chapters/` into the standalone companion promised by `outlook.tex:2`, and remove the stale concordance comments/phantoms from `main.tex`.

- [HIGH] `chapters/connections/thqg_concordance_supplement.tex:1` — PROBLEM: orphaned supplement; its only parent is the orphan `chapters/connections/concordance.tex:6620`. FIX: move it with `concordance.tex` into the standalone editorial companion and stop treating it as a chapter-surface file.

- [HIGH] `chapters/connections/editorial_constitution.tex:1` — PROBLEM: orphaned chapter; `outlook.tex:2` says `outlook` replaces `editorial_constitution` in the monograph proper, yet `main.tex:1561` and `1673` still plant labels for it. FIX: move it out of `chapters/` into the standalone editorial companion and delete the stale phantom labels in `main.tex`.

- [HIGH] `chapters/connections/twisted_holography_quantum_gravity.tex:5` — PROBLEM: the THQG master chapter is dead because its only root include is commented out at `main.tex:1493`, while `main.tex:1590-1594` fakes some of its labels. FIX: restore `\input{chapters/connections/twisted_holography_quantum_gravity}` at `main.tex:1493` and remove the THQG phantom-label block.

- [HIGH] `chapters/connections/thqg_perturbative_finiteness.tex:1` — PROBLEM: orphaned section file; its only parent is the unreachable THQG master at `twisted_holography_quantum_gravity.tex:495`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_gravitational_complexity.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:496`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_symplectic_polarization.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:497`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_gravitational_s_duality.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:498`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_gravitational_yangian.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:499`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_soft_graviton_theorems.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:500`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_modular_bootstrap.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:501`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_holographic_reconstruction.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:502`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_critical_string_dichotomy.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:503`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_fredholm_partition_functions.tex:1` — PROBLEM: orphaned section file; its only parent is `twisted_holography_quantum_gravity.tex:504`. FIX: restore the root THQG `\input` at `main.tex:1493`.

- [HIGH] `chapters/connections/thqg_preface_supplement.tex:2` — PROBLEM: the file says it should be “Inserted near the end of the preface chapter via `\input`,” but no such input exists anywhere in the live graph. FIX: add `\input{chapters/connections/thqg_preface_supplement}` near the end of `chapters/frame/preface.tex`.

- [MEDIUM] `chapters/connections/holomorphic_topological.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1397` comments out its only include and marks it “migrated to Vol II Part V.” FIX: remove it from Vol I’s `chapters/` tree and keep only the Vol II copy; also drop its `main.tex` phantom labels at `1607, 1609-1611`.

- [MEDIUM] `chapters/connections/kontsevich_integral.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1398` marks it “migrated to Vol II Part III.” FIX: remove it from Vol I’s `chapters/` tree and delete its `main.tex` phantom labels at `1608, 1612, 1613, 1620`.

- [MEDIUM] `chapters/connections/physical_origins.tex:1` — PROBLEM: orphaned 19-line stub; both the file (`lines 5-9`) and `main.tex:1399` say its content was absorbed into Vol II. FIX: delete this stub from `chapters/connections/`.

- [MEDIUM] `chapters/connections/ym_boundary_theory.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1402` marks it “Migrated to Vol II.” FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1621`.

- [MEDIUM] `chapters/connections/ym_higher_body_couplings.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1403` marks it “Migrated to Vol II.” FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1622`.

- [MEDIUM] `chapters/connections/ym_instanton_screening.tex:1` — PROBLEM: orphaned migrated chapter; `main.tex:1404` marks it “Migrated to Vol II.” FIX: remove it from Vol I’s `chapters/` tree and delete its phantom labels at `main.tex:1623,1626`.

- [MEDIUM] `chapters/connections/casimir_divisor_core_transport.tex:4` — PROBLEM: orphaned migrated chapter; `main.tex:1409` says it moved to Vol II Part II, and line 4 promises a `casimir_divisor_core_transport_standalone.tex` wrapper that is not present in the repo. FIX: remove this file from Vol I’s `chapters/` tree and delete the false standalone-wrapper claim if the wrapper is not restored in the destination.

- [MEDIUM] `chapters/connections/typeA_baxter_rees_theta.tex:1` — PROBLEM: orphaned migrated appendix-chapter; `main.tex:1410` says it moved to Vol II Part II. FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1624`.

- [MEDIUM] `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:3` — PROBLEM: orphaned migrated chapter; `main.tex:1411` says it moved to Vol II Part II. FIX: remove it from Vol I’s `chapters/` tree and delete its phantom label at `main.tex:1625`.

- [MEDIUM] `chapters/connections/dg_shifted_factorization_bridge.tex:1` — PROBLEM: orphaned removed chapter; `main.tex:1412` says it was “removed; content in Vol II Part II,” yet `main.tex:1579,1617-1619` still seeds labels for it. FIX: delete this file from Vol I’s `chapters/` tree and remove the stale phantom labels.

- [MEDIUM] `chapters/examples/toroidal_elliptic.tex:5` — PROBLEM: orphaned migrated chapter; `main.tex:1347` says it was “Moved to Vol III,” but Vol I still keeps the full 4,694-line file and a large phantom-label block at `main.tex:1628-1652`. FIX: remove the file from Vol I’s `chapters/examples/` tree and delete the toroidal/Vol III phantom-label block.

- [LOW] `chapters/frame/preface_section1_draft.tex:1` — PROBLEM: orphaned draft; the file says “To be integrated into preface.tex,” but `chapters/frame/preface.tex` already contains Section 1 starting at line `118`. FIX: archive or delete this draft.

- [LOW] `chapters/frame/preface_section1_v2.tex:1` — PROBLEM: orphaned alternate draft of the same live section; `chapters/frame/preface.tex` already carries the same Section 1 lane, including matching later headings at `625` and `739`. FIX: archive or delete this superseded v2 file.

- [LOW] `chapters/frame/preface_sections2_4_draft.tex:1` — PROBLEM: orphaned draft; `preface.tex` already contains Sections 2, 3, and 4 at lines `858`, `1274`, and `1737`. FIX: archive or delete this draft.

- [LOW] `chapters/frame/preface_sections5_9_draft.tex:1` — PROBLEM: orphaned draft; `preface.tex` already contains Sections 5, 6, 7, 8, and 9 at lines `2161`, `2435`, `2742`, `3147`, and `3279`. FIX: archive or delete this draft.

- [LOW] `chapters/frame/preface_sections10_13_draft.tex:1` — PROBLEM: orphaned draft; `preface.tex` already contains Section 10 and the matching closing headings at `3522`, `3731`, `3928`, `4010`, `4100`, `4216`, `4271`, and `4313`. FIX: archive or delete this draft.

## Summary
Checked: 113 | Findings: 33 | Verdict: FAIL
tokens used
107,141
