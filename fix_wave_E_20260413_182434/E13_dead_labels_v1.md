# E13_dead_labels_v1 (302s)

The literal `comm` pipeline in the prompt is wrong: it compares `\label{foo}` against `\ref{foo}`, so it marks every label as dead. I normalized label names first, then scanned live refs across Vol I/II/III for `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\hyperref[...]`, and related forms. No repo files were edited; for every finding the exact applied edit is `none`, per your instruction.

Results:
- Vol I chapter label instances scanned: `10510`
- Truly dead across live Vol I/II/III: `6156` instances
- Unique dead labels: `6124`
- Not dead, but only referenced from Vol II/III: `31`

Exhaustive reports:
- [dead_labels_report.txt](/tmp/dead_labels_report.txt)
- [dead_labels_report.tsv](/tmp/dead_labels_report.tsv)
- [cross_volume_exported_labels.txt](/tmp/cross_volume_exported_labels.txt)
- [dead_labels_summary.txt](/tmp/dead_labels_summary.txt)

Sample findings, in the requested format:
- PROBLEM at [arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:183): label `eq:scattering-matrix` has no live refs in Vol I/II/III. EXACT edit applied: none; reported only per instruction.
- PROBLEM at [arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:227): label `rem:lattice-specificity` has no live refs in Vol I/II/III. EXACT edit applied: none; reported only per instruction.
- PROBLEM at [arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:311): label `prop:divisor-sum-decomposition` has no live refs in Vol I/II/III. EXACT edit applied: none; reported only per instruction.


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
session id: 019d87c7-5771-7f73-8ab2-470662f4b828
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Find labels that are never referenced.
grep -roh '\\label{[^}]*}' chapters/ | sort > /tmp/labels.txt
grep -roh '\\ref{[^}]*}' chapters/ | sort > /tmp/refs.txt
comm -23 /tmp/labels.txt /tmp/refs.txt > /tmp/dead.txt
Report the dead labels. Do NOT delete them (they may be referenced from other volumes).
mcp startup: no servers

thinking
**Considering label reference search**

I should list the final answer with details about the problem at the specific file and line, and I need to apply the exact edits. Running grep commands might be necessary. I could use `multi_tool_use.parallel` to execute multiple commands at once, which could make things faster. I want to ensure I'm searching for dead labels, especially since the user's commands focus on `\ref{}`, so I should look for other reference macros too for a more thorough search.
codex
I’m checking the chapter label surface directly, then I’ll verify each apparent dead label against broader reference macros before reporting anything as unreferenced.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{["'^}]*'"\\}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\(ref|eqref|autoref|cref|Cref|vref|Vref|pageref)\\{["'^}]*'"\\}\" chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{[^}]*\})
       ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: regex parse error:
    (?:\(ref|eqref|autoref|cref|Cref|vref|Vref|pageref)\{[^}]*\})
                                                                ^
error: unopened group
exec
/bin/zsh -lc "grep -roh '\\\\label{["'^}]*}'"' chapters/ | sort > /tmp/labels.txt
grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sort > /tmp/refs.txt
comm -23 /tmp/labels.txt /tmp/refs.txt > /tmp/dead.txt
wc -l /tmp/dead.txt
sed -n '1,200p' /tmp/dead.txt" in /Users/raeez/chiral-bar-cobar succeeded in 224ms:
   10775 /tmp/dead.txt
\label{D1}
\label{D2}
\label{D3}
\label{D4}
\label{D5}
\label{D6}
\label{D:bar-htpy}
\label{D:bar}
\label{D:center-dg}
\label{D:center-htpy}
\label{D:deformation-htpy}
\label{D:discriminant-dg}
\label{D:discriminant-htpy}
\label{D:dual-htpy}
\label{D:dual}
\label{D:genus-tower}
\label{D:periodicity-dg}
\label{D:periodicity-htpy}
\label{MK:clutching-verdier}



thinking
**Debugging regex issues**

I'm trying to figure out how to recover from regex errors using `-F` for escaping. It feels like I need a more robust search approach. Should I consider using `grep` with Perl? Maybe `rg -N` would also work. I'm also thinking about how to compute candidate dead labels effectively; just finding labels without references feels too simplistic. The user asked for commands, so I need to report all dead labels without deleting any. I might have about 10,775 due to file:line duplicates, but I need to clarify the distinction between labels and references.
thinking
**Identifying command flaws**

I see that the command given is flawed, which I should definitely note. The problem seems to be a mismatch in the command itself when the user asked to "find labels that are never referenced." The command returns all labels because the forms differ. I think it’s important to mention and correct this in our process. The user wants to find dead labels without deleting anything, so I should focus on running the correct extraction and verification against references like `\cref` and `\eqref`.
thinking
**Determining unreferenced labels**

I need to identify labels that are never referenced within the chapters, and there could be quite a few. I might end up producing a long list with file:line details, potentially thousands if many labels are unreferenced. However, if I focus solely on `\ref` versus `\label`, the number might still be high but not as overwhelming. The user has requested a report on all dead labels, so I should generate a comprehensive report in `/tmp` that summarizes counts and includes some samples.
codex
The literal `comm` pipeline in the prompt is unsound: it compares `\\label{foo}` against `\\ref{foo}`, so it classifies every label as dead. I’m normalizing label names and checking broader reference macros before I report anything.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('chapters')
label_pat = re.compile(r'\\\\label\\{(["'^}]*)'"\\}')
ref_pat = re.compile(r'\\\\(?:ref|eqref|autoref|cref|Cref|vref|Vref|pageref)\\{(["'^}]*)'"\\}')
labels = []
refs = set()
for path in sorted(root.rglob('*.tex')):
    text = path.read_text(errors='ignore')
    for i, line in enumerate(text.splitlines(), 1):
        for m in label_pat.finditer(line):
            labels.append((m.group(1), str(path), i, line.strip()))
        for m in ref_pat.finditer(line):
            refs.add(m.group(1))
print('LABELS', len(labels))
print('UNIQUE_LABELS', len({n for n, *_ in labels}))
print('REFS', len(refs))
dead = [(n,p,i,l) for n,p,i,l in labels if n not in refs]
print('DEAD', len(dead))
for row in dead[:200]:
    print('\\t'.join(map(str,row)))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('chapters')
ref_pat = re.compile(r'\\\\(?:ref|eqref|autoref|cref|Cref|vref|Vref|pageref)\\{(["'^}]*)'"\\}')
macros = {}
for path in sorted(root.rglob('*.tex')):
    text = path.read_text(errors='ignore')
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r'\\\\([A-Za-z]+ref|[CV]?ref|eqref|autoref|cref|Cref|vref|Vref|pageref)\\{(["'^}]*)'"\\}', line):
            macros.setdefault(m.group(1), 0)
            macros[m.group(1)] += 1
for k in sorted(macros):
    print(f'{k}\\t{macros[k]}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 90ms:
LABELS 10510
UNIQUE_LABELS 10437
REFS 4497
DEAD 6227
eq:scattering-matrix	chapters/connections/arithmetic_shadows.tex	183	\begin{equation}\label{eq:scattering-matrix}
rem:lattice-specificity	chapters/connections/arithmetic_shadows.tex	227	\label{rem:lattice-specificity}
prop:divisor-sum-decomposition	chapters/connections/arithmetic_shadows.tex	311	\label{prop:divisor-sum-decomposition}
eq:log-det-sigma	chapters/connections/arithmetic_shadows.tex	313	\begin{equation}\label{eq:log-det-sigma}
prop:sewing-trace-formula	chapters/connections/arithmetic_shadows.tex	349	\label{prop:sewing-trace-formula}
eq:sewing-trace	chapters/connections/arithmetic_shadows.tex	354	\begin{equation}\label{eq:sewing-trace}
sec:four-identities	chapters/connections/arithmetic_shadows.tex	439	\section{Four identities}\label{sec:four-identities}
thm:narain-universality	chapters/connections/arithmetic_shadows.tex	444	\label{thm:narain-universality}
eq:narain-universality	chapters/connections/arithmetic_shadows.tex	448	\begin{equation}\label{eq:narain-universality}
eq:e8-epstein	chapters/connections/arithmetic_shadows.tex	478	\begin{equation}\label{eq:e8-epstein}
eq:z2-epstein	chapters/connections/arithmetic_shadows.tex	503	\begin{equation}\label{eq:z2-epstein}
eq:leech-hecke	chapters/connections/arithmetic_shadows.tex	528	\begin{equation}\label{eq:leech-hecke}
sec:charged-sector-resolution	chapters/connections/arithmetic_shadows.tex	604	\label{sec:charged-sector-resolution}
rem:discrimination-hierarchy	chapters/connections/arithmetic_shadows.tex	756	\label{rem:discrimination-hierarchy}
prop:shadow-arithmetic-factorization	chapters/connections/arithmetic_shadows.tex	779	\label{prop:shadow-arithmetic-factorization}
eq:shadow-arithmetic-factorization	chapters/connections/arithmetic_shadows.tex	785	\begin{equation}\label{eq:shadow-arithmetic-factorization}
 succeeded in 90ms:
eqref	1459
ref	14872



thinking
**Considering label references**

The output from Python shows only eqref and ref macros in the chapters, which is a good start. The user wants to ensure that if there are references to other volumes, they shouldn't delete any labels, but I should report dead labels within the chapters. I wonder if I should focus on finding labels that are never referenced in the repo, but still, leave them intact since they might be referenced elsewhere. Searching all three volumes could clarify which are local-only versus cross-volume. That seems like a more valuable audit!
thinking
**Searching for dead labels**

I need to search the full workspace for any dead labels that might be referenced in other volumes. There are 6,227 dead labels found within chapters relative to chapter references, which could make searching each one individually heavy. It seems beneficial to generate a report that includes the label, the file and line numbers, and whether they have local or external references. Since the sandbox allows reading generally, I think I might be able to access files across sibling repos, but I need to clarify the writable roots for certainty.
thinking
**Assessing reading permissions and skills**

It seems likely that reading might be allowed everywhere in the workspace, but I need to confirm that. The user hasn't mentioned any specific skills, but this task seems to align closely with label verification. I could consider using the multi-path-verify tool for checking the dead labels, and since the task matches the description for claim-surface-sync, that seems like the right option too. I'll need to announce the skill and open its SKILL.md. Cross-volume propagation might also be necessary due to references spanning across volumes.
codex
I’m using `claim-surface-sync` for the label audit and I’m checking whether any chapter-local dead labels are actually referenced from Vol II or Vol III before I classify them.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
paths = [Path('/Users/raeez/chiral-bar-cobar-vol2'), Path('/Users/raeez/calabi-yau-quantum-groups')]
label_refs = {}
pat = re.compile(r'\\\\(?:ref|eqref|autoref|cref|Cref|vref|Vref|pageref)\\{(["'^}]*)'"\\}')
for root in paths:
    count=0
    found=set()
    for path in root.rglob('*.tex'):
        try:
            text = path.read_text(errors='ignore')
        except Exception:
            continue
        for m in pat.finditer(text):
            found.add(m.group(1))
            count += 1
    print(root.name, count, len(found))
    sample = sorted(list(found))[:20]
    for s in sample:
        print(s)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 116ms:
chiral-bar-cobar-vol2 8619 2894
#1
V1-...
V1-chap:yangians
V1-comp:holographic-ss-vir
V1-comp:thqg-I-hs-fermion
V1-comp:thqg-I-hs-heisenberg
V1-comp:thqg-V-affine-yangian
V1-comp:thqg-V-quartic-graviton
V1-comp:vir-physical-cc
V1-conj:lattice-sewing
V1-conj:master-bv-brst
V1-conj:thqg-I-non-perturbative
V1-const:vol1-genus-spectral-sequence
V1-const:vol1-modular-tangent-complex
V1-constr:clifford-spectral
V1-constr:nms-sewing-product
V1-constr:obstruction-recursion
V1-constr:platonic-package
V1-constr:thqg-III-verdier-involution

thinking
**Figuring out loading needs**

I need to load the concordance and theorem registry since the skill suggests loading first. Even though I'm not editing anything, it feels right to follow the skill’s guidelines. Maybe I can skim through it? But, am I thinking about this correctly? If I'm just reporting dead labels, is loading really necessary? Still, it might be part of the instructions, so I should load it quickly.
codex
I’ve confirmed the skill’s protocol. Next I’m reconciling the dead-label candidates against the canonical claim/metadata surfaces so I don’t misreport labels that are intentionally exposed for cross-volume references.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
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




thinking
**Classifying references and labels**

I need to produce a report file, possibly in the /tmp directory. I have to correct dead labels across chapters and classify external references properly. The user specified they want to use chapters/, but there may be references in other areas like frontmatter, appendices, and metadata. If I only search chapters, I could end up with a lot of false positives. So, I should search all .tex files in the current repository to be thorough!
thinking
**Interpreting LaTeX labels**

I’m focusing on interpreting labels under chapters/ to find which ones aren’t referenced in Vol I/II/III. Since I can’t delete them, I’ll create a report file because the list might be extensive—possibly thousands. I need to carefully normalize references, especially with labels like `\ref{a,b}`. My regex might miss multiple labels if it captures everything as one label. I should also consider variants like `\hyperref[label]{text}` and check for macros. I want to use grep more broadly for this!
thinking
**Searching for LaTeX reference patterns**

I noticed that the previous script only identified `eqref` and `ref` among macros. To dig deeper, I need to search for patterns like `\\[A-Za-z]*ref\{` across all repositories. I should also look for variations like `\\hyperref[`, `\\Ref{`, `\\fullref`, `\\nameref`, and `\\cpageref`. This will help me audit all possible reference formats. It's important to be thorough to ensure I don’t miss anything crucial. Let's get started with this search!
codex
The first pass shows the main failure mode: chapter-local search alone overstates dead labels badly. I’m expanding the reference parser to catch comma lists and non-`\\ref` reference forms across Vol I/II/III before I freeze the report.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
roots = [Path('/Users/raeez/chiral-bar-cobar'), Path('/Users/raeez/chiral-bar-cobar-vol2'), Path('/Users/raeez/calabi-yau-quantum-groups')]
pat = re.compile(r'\\\\([A-Za-z]*ref[A-Za-z*]*)\\s*(?:\\[["'^'"\\]]*\\])?\\{')
counts = {}
for root in roots:
    for path in root.rglob('*.tex'):
        try:
            text = path.read_text(errors='ignore')
        except Exception:
            continue
        for m in pat.finditer(text):
            counts[m.group(1)] = counts.get(m.group(1), 0) + 1
for k in sorted(counts):
    print(f'{k}\\t{counts[k]}')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
roots = [Path('/Users/raeez/chiral-bar-cobar'), Path('/Users/raeez/chiral-bar-cobar-vol2'), Path('/Users/raeez/calabi-yau-quantum-groups')]
pat = re.compile(r'\\\\hyperref\\[(["'^'"\\]]+)\\]')
count = 0
labs = set()
for root in roots:
    for path in root.rglob('*.tex'):
        try:
            text = path.read_text(errors='ignore')
        except Exception:
            continue
        for m in pat.finditer(text):
            count += 1
            labs.add(m.group(1))
print('hyperref_count', count)
print('hyperref_labels', len(labs))
for s in sorted(list(labs))[:50]:
    print(s)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar')
# Find comma-separated refs in Vol I
pat = re.compile(r'\\\\(?:[A-Za-z]*ref[A-Za-z*]*)\\s*(?:\\[["'^'"\\]]*\\])?\\{(["'^}]*,[''^}]*)'"\\}')
seen = []
for path in root.rglob('*.tex'):
    try:
        text = path.read_text(errors='ignore')
    except Exception:
        continue
    for i,line in enumerate(text.splitlines(),1):
        if pat.search(line):
            seen.append((str(path), i, line.strip()))
print('comma_refs', len(seen))
for row in seen[:80]:
    print('\\t'.join(map(str,row)))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.16s:
hyperref_count 40
hyperref_labels 1
op:multi-generator-universality
 succeeded in 2.31s:
BDref	2
cref	77
eqref	79500
eqref*	5
hyperref	40
pageref	1
ref	791444
ref*	1563
 succeeded in 4.23s:
comma_refs 1
/Users/raeez/chiral-bar-cobar/archive/source_tex/celestial_boundary_master_note.tex	323	By \cref{lem:br-closed,lem:gauge-change-order-r}, $\Ob_r(b)$ is independent of the chosen $r$-normal form.

thinking
**Considering directory definitions**

I’m evaluating how to define labels only referenced in archives or old notes, which aren’t live references. I need to exclude any directories like `archive`, `backup`, and `superseded`. It sounds like I should search for all `.tex` files while skipping `archive`, and `.git`. Perhaps I can programmatically prune directories that aren't relevant, like `node_modules` or `venv`. My focus is really on live surfaces, so I’ll need to inspect the `BDref` in the current repo quickly.
codex
I found live reference forms beyond `\\ref`: `\\eqref`, `\\cref`, `\\ref*`, `\\eqref*`, `\\pageref`, `\\hyperref[...]`, and a custom `\\BDref`. I’m folding those into a live-surface scan and excluding archive-only noise.
exec
/bin/zsh -lc 'find /Users/raeez/chiral-bar-cobar-vol2 -maxdepth 2 -type d | sort' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\BDref|\\\\newcommand\\\\BDref|\\\\def\\\\BDref|\\\\DeclareRobustCommand\\\\BDref\" -g '*.tex' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'find /Users/raeez/calabi-yau-quantum-groups -maxdepth 2 -type d | sort' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'find /Users/raeez/chiral-bar-cobar -maxdepth 2 -type d | sort' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2
/Users/raeez/chiral-bar-cobar-vol2/.agents
/Users/raeez/chiral-bar-cobar-vol2/.agents/skills
/Users/raeez/chiral-bar-cobar-vol2/.build_logs
/Users/raeez/chiral-bar-cobar-vol2/.claude
/Users/raeez/chiral-bar-cobar-vol2/.claude/commands
/Users/raeez/chiral-bar-cobar-vol2/.claude/hooks
/Users/raeez/chiral-bar-cobar-vol2/.claude/specs
/Users/raeez/chiral-bar-cobar-vol2/.claude/worktrees
/Users/raeez/chiral-bar-cobar-vol2/.codex
/Users/raeez/chiral-bar-cobar-vol2/.codex/hooks
/Users/raeez/chiral-bar-cobar-vol2/.git
/Users/raeez/chiral-bar-cobar-vol2/.git/hooks
/Users/raeez/chiral-bar-cobar-vol2/.git/info
/Users/raeez/chiral-bar-cobar-vol2/.git/logs
/Users/raeez/chiral-bar-cobar-vol2/.git/objects
/Users/raeez/chiral-bar-cobar-vol2/.git/refs
/Users/raeez/chiral-bar-cobar-vol2/.pytest_cache
/Users/raeez/chiral-bar-cobar-vol2/.pytest_cache/v
/Users/raeez/chiral-bar-cobar-vol2/appendices
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups
/Users/raeez/calabi-yau-quantum-groups/.agents
/Users/raeez/calabi-yau-quantum-groups/.agents/skills
/Users/raeez/calabi-yau-quantum-groups/.build_logs
/Users/raeez/calabi-yau-quantum-groups/.claude
/Users/raeez/calabi-yau-quantum-groups/.claude/commands
/Users/raeez/calabi-yau-quantum-groups/.claude/hooks
/Users/raeez/calabi-yau-quantum-groups/.codex
/Users/raeez/calabi-yau-quantum-groups/.codex/hooks
/Users/raeez/calabi-yau-quantum-groups/.git
/Users/raeez/calabi-yau-quantum-groups/.git/hooks
/Users/raeez/calabi-yau-quantum-groups/.git/info
/Users/raeez/calabi-yau-quantum-groups/.git/logs
/Users/raeez/calabi-yau-quantum-groups/.git/objects
/Users/raeez/calabi-yau-quantum-groups/.git/refs
/Users/raeez/calabi-yau-quantum-groups/.pytest_cache
/Users/raeez/calabi-yau-quantum-groups/.pytest_cache/v
/Users/raeez/calabi-yau-quantum-groups/appendices
/Users/raeez/calabi-yau-quantum-groups/bibliography
/Users/raeez/calabi-yau-quantum-groups/chapters
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
/Users/raeez/chiral-bar-cobar/.agents
/Users/raeez/chiral-bar-cobar/.agents/skills
/Users/raeez/chiral-bar-cobar/.build_logs
/Users/raeez/chiral-bar-cobar/.claude
/Users/raeez/chiral-bar-cobar/.claude/commands
/Users/raeez/chiral-bar-cobar/.claude/hooks
/Users/raeez/chiral-bar-cobar/.claude/projects
/Users/raeez/chiral-bar-cobar/.claude/worktrees
/Users/raeez/chiral-bar-cobar/.codex
/Users/raeez/chiral-bar-cobar/.codex/hooks
/Users/raeez/chiral-bar-cobar/.git
/Users/raeez/chiral-bar-cobar/.git/hooks
/Users/raeez/chiral-bar-cobar/.git/info
/Users/raeez/chiral-bar-cobar/.git/logs
/Users/raeez/chiral-bar-cobar/.git/objects
/Users/raeez/chiral-bar-cobar/.git/refs
/Users/raeez/chiral-bar-cobar/.git/worktrees
/Users/raeez/chiral-bar-cobar/.pytest_cache
/Users/raeez/chiral-bar-cobar/.pytest_cache/v
exec
/bin/zsh -lc "rg -n '\\\\BDref|\\\\newcommand\\{\\\\BDref\\}|\\\\def\\\\BDref|\\\\DeclareRobustCommand\\{\\\\BDref\\}' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./main.tex:459:\newcommand{\BDref}[1]{\textup{[\cite{BD04}, #1]}}





thinking
**Building a robust script**

I'm realizing that I need to create a solid script that only searches live surfaces, excluding things like archive, audit, and temporary files. The focus should really be on live references in chapters, appendices, and possibly main files. I wonder if `standalone` should be included too since it might be used for certain builds. I'm also noting that I need to ensure to report any dead labels after checking across volumes. Let's settle on `chapters`, `appendices`, and `main.tex` for now.
thinking
**Counting labels in volumes**

I need to produce counts for labels defined in the `chapters/` of Volume I. This includes checking if they’re referenced anywhere in Volume I, including appendices and the main text. Additionally, I should see if they're referenced in the live surfaces of Volumes II and III. I might classify labels into two groups: those unreferenced across the live volumes and those that are chapter-local but referenced in other volumes. I should consider mentioning the cross-volume reference count as well. I think creating a report file like `/tmp/dead_labels_report.tsv` will help summarize everything clearly.
thinking
**Creating a dead labels report**

Since the user asked for a report on dead labels, outputting 6000 lines directly just won't work—it’s way too much! I think it’s better to create a report file that summarizes the counts instead. Maybe I can link to the report file in my final output. I want to include the top findings and a path to the complete report, ensuring I don’t make any edits along the way. I really need to focus on computing the exact dead labels, so let’s build a script for that!
thinking
**Exploring LaTeX Labels**

I'm considering using `\autoref` for live searches across several volumes with a regex pattern `[A-Za-z]*ref`. It's essential to split the comma contents since some macros have optional arguments. I need to check in specific directories like `chapters`, `appendices`, and `main.tex` to see if there are any duplicate labels. I suspect there might be around 73 duplicates, which could create problems for the user's commands regarding dead labels. I'll need to note these while remaining focused on the task.
thinking
**Planning the audit report**

I'm considering creating an adversarial audit focused on finding labels that aren't referenced. I may need to generate a file called `/tmp/vol1_dead_labels.tsv` with columns for label, file, line, local_refs, and external_refs. Since the user wants a specific format for findings, I'll document issues as "PROBLEM at file:line: label `x` has no live refs," stating that no edits are allowed. For better organization, maybe I can also create a report file `/tmp/dead_labels_report.txt` that summarizes all findings and counts, maintaining the requested format. I'll ensure the commands are accurately reported too.
codex
I have the live reference grammar pinned down. Now I’m generating a normalized report: Vol I chapter labels only, then live refs across Vol I/II/III, split into truly dead vs cross-volume-exported.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from collections import defaultdict, Counter

vols = {
    'vol1': Path('/Users/raeez/chiral-bar-cobar'),
    'vol2': Path('/Users/raeez/chiral-bar-cobar-vol2'),
    'vol3': Path('/Users/raeez/calabi-yau-quantum-groups'),
}

# Live surfaces only: top-level main.tex plus chapters/ and appendices/ trees.
def live_tex_files(root: Path):
    files = []
    main = root / 'main.tex'
    if main.exists():
        files.append(main)
    for sub in ('chapters', 'appendices'):
        d = root / sub
        if d.exists():
            files.extend(sorted(d.rglob('*.tex')))
    return files

label_pat = re.compile(r'\\\\label\\{(["'^}]*)'"\\}')
ref_cmd_pat = re.compile(r'\\\\(?P<cmd>ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|autoref\\*?|Autoref\\*?|vref\\*?|Vref\\*?|pageref\\*?|nameref\\*?|fullref\\*?|thmref\\*?)\\s*(?:\\[["'^'"\\]]*\\])?\\{(?P<body>["'^}]*)'"\\}')
hyperref_pat = re.compile(r'\\\\hyperref\\[(?P<label>["'^'"\\]]+)\\]')

# Collect chapter labels in Vol I.
labels = []
for path in sorted((vols['vol1'] / 'chapters').rglob('*.tex')):
    text = path.read_text(errors='ignore')
    for i, line in enumerate(text.splitlines(), 1):
        for m in label_pat.finditer(line):
            labels.append({
                'label': m.group(1).strip(),
                'file': str(path),
                'line': i,
                'text': line.strip(),
            })

refs_by_vol = {k: Counter() for k in vols}
locs_by_vol = {k: defaultdict(list) for k in vols}

for vol, root in vols.items():
    for path in live_tex_files(root):
        text = path.read_text(errors='ignore')
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            for m in ref_cmd_pat.finditer(line):
                body = m.group('body')
                for raw in body.split(','):
                    name = raw.strip()
                    if not name:
                        continue
                    refs_by_vol[vol][name] += 1
                    if len(locs_by_vol[vol][name]) < 5:
                        locs_by_vol[vol][name].append(f'{path}:{i}')
            for m in hyperref_pat.finditer(line):
                name = m.group('label').strip()
                if not name:
                    continue
                refs_by_vol[vol][name] += 1
                if len(locs_by_vol[vol][name]) < 5:
                    locs_by_vol[vol][name].append(f'{path}:{i}')

truly_dead = []
cross_only = []
vol1_live = []
for row in labels:
    name = row['label']
    c1 = refs_by_vol['vol1'][name]
    c2 = refs_by_vol['vol2'][name]
    c3 = refs_by_vol['vol3'][name]
    out = dict(row)
    out.update({'vol1_refs': c1, 'vol2_refs': c2, 'vol3_refs': c3})
    if c1 + c2 + c3 == 0:
        truly_dead.append(out)
    elif c1 == 0 and (c2 + c3) > 0:
        cross_only.append(out)
    elif c1 > 0:
        vol1_live.append(out)

# file summaries for truly dead
by_file = Counter(r['file'] for r in truly_dead)

report = Path('/tmp/dead_labels_report.txt')
tsv = Path('/tmp/dead_labels_report.tsv')
summary = Path('/tmp/dead_labels_summary.txt')
with report.open('w') as f:
    f.write('Dead chapter labels in Vol I with no live refs in Vol I/II/III.\\n')
    f.write('Reference forms counted: ref/ref*, eqref/eqref*, cref/Cref, autoref, vref/Vref, pageref, nameref, fullref, thmref, hyperref[label].\\n')
    f.write('Surfaces scanned: main.tex + chapters/ + appendices/ in each live volume; archive/out/audit trees excluded.\\n\\n')
    for r in truly_dead:
        f.write(f\"PROBLEM at {r['file']}:{r['line']}: label "'`{r['"'label']}"'` has no live refs in Vol I/II/III.'"\\n\")
        f.write('EXACT edit applied: none; reported only per instruction.\\n\\n')
with tsv.open('w') as f:
    f.write('label\\tfile\\tline\\tvol1_refs\\tvol2_refs\\tvol3_refs\\n')
    for r in truly_dead:
        f.write(f\"{r['label']}\\t{r['file']}\\t{r['line']}\\t{r['vol1_refs']}\\t{r['vol2_refs']}\\t{r['vol3_refs']}\\n\")
with summary.open('w') as f:
    f.write(f'Total Vol I chapter labels: {len(labels)}\\n')
    f.write(f'Truly dead across live Vol I/II/III: {len(truly_dead)}\\n')
    f.write(f'Cross-volume exported only (no Vol I live refs, but referenced in Vol II/III): {len(cross_only)}\\n')
    f.write(f'Referenced within live Vol I: {len(vol1_live)}\\n')
    f.write('\\nTop files by truly dead labels:\\n')
    for file, count in by_file.most_common(25):
        f.write(f'{count}\\t{file}\\n')
    f.write('\\nSample cross-volume-exported labels:\\n')
    for r in cross_only[:50]:
        refs = []
        if r['vol2_refs']:
            refs.append(f\"Vol II x{r['vol2_refs']}\")
        if r['vol3_refs']:
            refs.append(f\"Vol III x{r['vol3_refs']}\")
        f.write(f\"{r['label']}\\t{r['file']}:{r['line']}\\t{' ; '.join(refs)}\\n\")

print(summary.read_text())
print(f'REPORT={report}')
print(f'TSV={tsv}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 316ms:
Total Vol I chapter labels: 10510
Truly dead across live Vol I/II/III: 6156
Cross-volume exported only (no Vol I live refs, but referenced in Vol II/III): 31
Referenced within live Vol I: 4323

Top files by truly dead labels:
597	/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
298	/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex
248	/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
220	/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex
209	/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex
187	/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
173	/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
168	/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex
161	/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
140	/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
130	/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex
127	/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex
126	/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
123	/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex

thinking
**Planning data extraction**

I'm thinking about cross-checking counts using a shell pipeline. I want to extract label names from chapters and reference names from the three volumes, including chapters, appendices, and main.tex. Using Perl or rg with PCRE2 might work, but I'm also considering Python for its simplicity. I might need a quick approximation with Perl and `sort -u`. I could use `find ... | xargs perl -ne ...` or a Perl one-liner for efficiency. I'll aim for robust comma-splitting as well.
codex
I’ve got the normalized report. I’m doing one independent extraction pass with a separate shell/perl pipeline so the final count is not resting on a single parser.
exec
/bin/zsh -lc "perl -ne 'while(/\\\\label\\{(["'^}]*)'"\\}/g){print \""'$1'"\\n\"}' "'$(find chapters -type f -name '"'*.tex' | sort) | sort -u > /tmp/vol1_labels_norm.txt
perl -ne 'while(/\\\\(ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|autoref\\*?|Autoref\\*?|vref\\*?|Vref\\*?|pageref\\*?|nameref\\*?|fullref\\*?|thmref\\*?)\\s*(?:\\[["'^'"\\]]*\\])?\\{(["'^}]*)'"\\}/g){for "'$x (split(/,/, $2)){ $x =~ s/''^'"\\s+|\\s+"'$//g; print "$x'"\\n\" if length "'$x; }} while(/'"\\\\hyperref\\[(["'^'"\\]]+)\\]/g){print \""'$1'"\\n\"}' "'$(find /Users/raeez/chiral-bar-cobar -maxdepth 1 -name '"'main.tex' -o -path '/Users/raeez/chiral-bar-cobar/chapters/*.tex' -o -path '/Users/raeez/chiral-bar-cobar/chapters/*/*.tex' -o -path '/Users/raeez/chiral-bar-cobar/appendices/*.tex' -o -path '/Users/raeez/chiral-bar-cobar/appendices/*/*.tex' ; find /Users/raeez/chiral-bar-cobar-vol2 -maxdepth 1 -name 'main.tex' -o -path '/Users/raeez/chiral-bar-cobar-vol2/chapters/*.tex' -o -path '/Users/raeez/chiral-bar-cobar-vol2/chapters/*/*.tex' -o -path '/Users/raeez/chiral-bar-cobar-vol2/appendices/*.tex' -o -path '/Users/raeez/chiral-bar-cobar-vol2/appendices/*/*.tex' ; find /Users/raeez/calabi-yau-quantum-groups -maxdepth 1 -name 'main.tex' -o -path '/Users/raeez/calabi-yau-quantum-groups/chapters/*.tex' -o -path '/Users/raeez/calabi-yau-quantum-groups/chapters/*/*.tex' -o -path '/Users/raeez/calabi-yau-quantum-groups/appendices/*.tex' -o -path '/Users/raeez/calabi-yau-quantum-groups/appendices/*/*.tex') | sort -u > /tmp/live_refs_norm.txt
comm -23 /tmp/vol1_labels_norm.txt /tmp/live_refs_norm.txt | wc -l
sed -n '1,40p' /tmp/vol1_labels_norm.txt >/tmp/_ignore_check1
sed -n '1,40p' /tmp/live_refs_norm.txt >/tmp/_ignore_check2" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   10425
exec
/bin/zsh -lc "printf '%s
' /Users/raeez/chiral-bar-cobar/main.tex > /tmp/live_tex_files.txt
find /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices -type f -name '*.tex' | sort >> /tmp/live_tex_files.txt
printf '%s
' /Users/raeez/chiral-bar-cobar-vol2/main.tex >> /tmp/live_tex_files.txt
find /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/appendices -type f -name '*.tex' | sort >> /tmp/live_tex_files.txt
printf '%s
' /Users/raeez/calabi-yau-quantum-groups/main.tex >> /tmp/live_tex_files.txt
find /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/appendices -type f -name '*.tex' | sort >> /tmp/live_tex_files.txt
perl -ne 'while(/\\\\label\\{(["'^}]*)'"\\}/g){print \""'$1'"\\n\"}' "'$(find chapters -type f -name '"'*.tex' | sort) | sort -u > /tmp/vol1_labels_norm.txt
perl -ne 'while(/\\\\(ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|autoref\\*?|Autoref\\*?|vref\\*?|Vref\\*?|pageref\\*?|nameref\\*?|fullref\\*?|thmref\\*?)\\s*(?:\\[["'^'"\\]]*\\])?\\{(["'^}]*)'"\\}/g){for "'$x (split(/,/, $2)){ $x =~ s/''^'"\\s+|\\s+"'$//g; print "$x'"\\n\" if length "'$x; }} while(/'"\\\\hyperref\\[(["'^'"\\]]+)\\]/g){print \""'$1'"\\n\"}' "'$(cat /tmp/live_tex_files.txt) | sort -u > /tmp/live_refs_norm.txt
comm -23 /tmp/vol1_labels_norm.txt /tmp/live_refs_norm.txt | wc -l' in /Users/raeez/chiral-bar-cobar succeeded in 148ms:
    6124

thinking
**Computing duplicates in labels**

I need to check for duplicates among dead labels, possibly identifying around 32 extra duplicates across 29 labels. This is important because duplicate labels could mean one reference points to multiple locations, even though for dead labels, these duplicates might not be referenced. I should mention the adjacent issue, but generating a report with each duplicate finding might be necessary if the user requested a dead labels report. I also need to inspect cross-volume references to confirm labels aren’t dead.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
from collections import defaultdict, Counter

vols = {
    'vol1': Path('/Users/raeez/chiral-bar-cobar'),
    'vol2': Path('/Users/raeez/chiral-bar-cobar-vol2'),
    'vol3': Path('/Users/raeez/calabi-yau-quantum-groups'),
}

def live_tex_files(root: Path):
    files = []
    main = root / 'main.tex'
    if main.exists():
        files.append(main)
    for sub in ('chapters', 'appendices'):
        d = root / sub
        if d.exists():
            files.extend(sorted(d.rglob('*.tex')))
    return files

label_pat = re.compile(r'\\\\label\\{(["'^}]*)'"\\}')
ref_cmd_pat = re.compile(r'\\\\(?P<cmd>ref\\*?|eqref\\*?|cref\\*?|Cref\\*?|autoref\\*?|Autoref\\*?|vref\\*?|Vref\\*?|pageref\\*?|nameref\\*?|fullref\\*?|thmref\\*?)\\s*(?:\\[["'^'"\\]]*\\])?\\{(?P<body>["'^}]*)'"\\}')
hyperref_pat = re.compile(r'\\\\hyperref\\[(?P<label>["'^'"\\]]+)\\]')

labels = []
for path in sorted((vols['vol1'] / 'chapters').rglob('*.tex')):
    text = path.read_text(errors='ignore')
    for i, line in enumerate(text.splitlines(), 1):
        for m in label_pat.finditer(line):
            labels.append((m.group(1).strip(), str(path), i))

refs_by_vol = {k: Counter() for k in vols}
locs_by_vol = {k: defaultdict(list) for k in vols}
for vol, root in vols.items():
    for path in live_tex_files(root):
        text = path.read_text(errors='ignore')
        for i, line in enumerate(text.splitlines(), 1):
            for m in ref_cmd_pat.finditer(line):
                for raw in m.group('body').split(','):
                    name = raw.strip()
                    if name:
                        refs_by_vol[vol][name] += 1
                        if len(locs_by_vol[vol][name]) < 5:
                            locs_by_vol[vol][name].append(f'{path}:{i}')
            for m in hyperref_pat.finditer(line):
                name = m.group('label').strip()
                if name:
                    refs_by_vol[vol][name] += 1
                    if len(locs_by_vol[vol][name]) < 5:
                        locs_by_vol[vol][name].append(f'{path}:{i}')

cross = []
for name, path, line in labels:
    c1 = refs_by_vol['vol1'][name]
    c2 = refs_by_vol['vol2'][name]
    c3 = refs_by_vol['vol3'][name]
    if c1 == 0 and (c2 + c3) > 0:
        cross.append((name, path, line, c2, c3, '; '.join(locs_by_vol['vol2'][name]), '; '.join(locs_by_vol['vol3'][name])))

out = Path('/tmp/cross_volume_exported_labels.txt')
with out.open('w') as f:
    f.write('Vol I chapter labels with no live Vol I refs but live Vol II/III refs.\\n\\n')
    for name, path, line, c2, c3, l2, l3 in cross:
        f.write(f'{name}\\t{path}:{line}\\tVol II={c2}\\tVol III={c3}\\n')
        if l2:
            f.write(f'  Vol II refs: {l2}\\n')
        if l3:
            f.write(f'  Vol III refs: {l3}\\n')
        f.write('\\n')
print(f'cross_count={len(cross)}')
print(out)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 308ms:
cross_count=31
/tmp/cross_volume_exported_labels.txt


thinking
**Considering report details**

I’m thinking about creating a report on duplicates, but I’m not sure if it's necessary. I might also want to sample from the report or grab the top files. There's also a plan to produce a command that extracts all dead labels, but there are some specific instructions to follow regarding repository edits and pipeline comparisons. According to my findings, there are 6,156 dead label instances across multiple volumes, and I should provide full detailed reports. Maybe I’ll include some sample findings in the final report since they asked about the dead labels.
thinking
**Evaluating report details**

I’m considering the possibility of including the top files and noting the report path. Since there’s a huge list, it might help to mention some specific findings from the beginning. I think I could inspect the summary or the first few lines of the report, which could provide insight. Opening a full snippet might not be necessary, but it could be helpful to highlight the first 20 findings for clarity.
exec
/bin/zsh -lc "sed -n '1,40p' /tmp/dead_labels_report.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Dead chapter labels in Vol I with no live refs in Vol I/II/III.
Reference forms counted: ref/ref*, eqref/eqref*, cref/Cref, autoref, vref/Vref, pageref, nameref, fullref, thmref, hyperref[label].
Surfaces scanned: main.tex + chapters/ + appendices/ in each live volume; archive/out/audit trees excluded.

PROBLEM at /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:183: label `eq:scattering-matrix` has no live refs in Vol I/II/III.
EXACT edit applied: none; reported only per instruction.

PROBLEM at /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:227: label `rem:lattice-specificity` has no live refs in Vol I/II/III.
EXACT edit applied: none; reported only per instruction.

PROBLEM at /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:311: label `prop:divisor-sum-decomposition` has no live refs in Vol I/II/III.
EXACT edit applied: none; reported only per instruction.

PROBLEM at /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:313: label `eq:log-det-sigma` has no live refs in Vol I/II/III.
EXACT edit applied: none; reported only per instruction.

PROBLEM at /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:349: label `prop:sewing-trace-formula` has no live refs in Vol I/II/III.
EXACT edit applied: none; reported only per instruction.

PROBLEM at /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:354: label `eq:sewing-trace` has no live refs in Vol I/II/III.

thinking
**Crafting a concise report**

I think I can simplify my final output by keeping it concise, possibly in two paragraphs with some short bullet points. I want to make sure sections are well-defined, like **Result** and **Artifacts**. Too many lines might overwhelm, but I also want to ensure I include all necessary details in a clear manner. Striking the right balance between brevity and completeness is important!
codex
The literal `comm` pipeline in the prompt is wrong: it compares `\label{foo}` against `\ref{foo}`, so it marks every label as dead. I normalized label names first, then scanned live refs across Vol I/II/III for `\ref`, `\ref*`, `\eqref`, `\eqref*`, `\cref`, `\hyperref[...]`, and related forms. No repo files were edited; for every finding the exact applied edit is `none`, per your instruction.

Results:
- Vol I chapter label instances scanned: `10510`
- Truly dead across live Vol I/II/III: `6156` instances
- Unique dead labels: `6124`
- Not dead, but only referenced from Vol II/III: `31`

Exhaustive reports:
- [dead_labels_report.txt](/tmp/dead_labels_report.txt)
- [dead_labels_report.tsv](/tmp/dead_labels_report.tsv)
- [cross_volume_exported_labels.txt](/tmp/cross_volume_exported_labels.txt)
- [dead_labels_summary.txt](/tmp/dead_labels_summary.txt)

Sample findings, in the requested format:
- PROBLEM at [arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:183): label `eq:scattering-matrix` has no live refs in Vol I/II/III. EXACT edit applied: none; reported only per instruction.
- PROBLEM at [arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:227): label `rem:lattice-specificity` has no live refs in Vol I/II/III. EXACT edit applied: none; reported only per instruction.
- PROBLEM at [arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:311): label `prop:divisor-sum-decomposition` has no live refs in Vol I/II/III. EXACT edit applied: none; reported only per instruction.
tokens used
58,837
