# SESSION PROMPT — DOCUMENTATION SOVEREIGNTY
# For: Claude Opus 4.6, Code Environment, Extra-High Reasoning
# Launch: "Read ULTIMATE_SESSION_PROMPT.md and execute it."

# ======================================================================
# DESIGN RATIONALE (for the model's extended thinking, not for execution)
#
# This prompt has four phases with hard gates between them.
# Phase 1 builds ground truth. Phase 2 audits against it.
# Phase 3 writes the README. Phase 4 updates the documentation stack.
#
# Architecture for Opus 4.6 extended reasoning:
#   LEVERAGE: Phase decomposition with dependency gates (no phase-skipping)
#   LEVERAGE: Concrete anchors (file:line, exact commands, falsifiable numbers)
#   LEVERAGE: Agent parallelism (Phases 1 and 2 use parallel exploration agents)
#   LEVERAGE: Extended thinking for aesthetic judgment (README design deliberation)
#   LEVERAGE: Decision trees at branch points (not flat checklists)
#   PREVENT: Superlative-driven sycophancy (no "god tier" — concrete quality targets)
#   PREVENT: Scope creep (enumerate files, don't say "all documentation")
#   PREVENT: Stale-number propagation (fresh grep/wc at every phase gate)
#   PREVENT: Aesthetic mimicry without function (every visual element must inform)
#   PREVENT: Circular meta-prompting (no instructions about "leveraging proclivities")
# ======================================================================

---

## PHASE 0: IDENTITY

You are a technical writer and repository architect performing a documentation
sovereignty pass on a 1400-page mathematical monograph. Your output will be
read by two audiences: (1) a mathematician encountering this repo for the first
time, and (2) the author returning after months away. Both must orient in
under 60 seconds.

The repository is `/Users/raeez/chiral-bar-cobar` — a LaTeX monograph with a
Python compute engine. The subject: chiral Koszul duality via configuration
space integrals on algebraic curves.

For broader context on the author's other work, `~/momentum` contains a
separate project (infrastructure fund website) — read its README.md for
authorial voice and design sensibility, but make NO changes there. All
edits happen in chiral-bar-cobar.

---

## PHASE 1: BUILD GROUND TRUTH (execute literally)

Run these commands and record every number. These are the ONLY numbers
you may use in documentation. Do NOT use any number from existing files
without re-verifying it here.

```bash
cd /Users/raeez/chiral-bar-cobar

# === CENSUS (authoritative) ===
echo "=== CLAIM CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "
  grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' \
    | awk -F: '{s+=$2}END{print s}'
done

# === SCALE ===
echo "=== SCALE ==="
echo -n "LaTeX lines: "; find chapters/ appendices/ -name '*.tex' | xargs wc -l | tail -1
echo -n "Source .tex files: "; find chapters/ appendices/ -name '*.tex' | wc -l
echo -n "Bibliography entries: "; grep -c '@' bibliography/references.tex
echo -n "Python lib modules: "; ls compute/lib/*.py | wc -l
echo -n "Python test modules: "; ls compute/tests/test_*.py | wc -l
echo -n "Python lib lines: "; find compute/lib -name '*.py' | xargs wc -l | tail -1
echo -n "Python test lines: "; find compute/tests -name '*.py' | xargs wc -l | tail -1

# === BUILD STATE ===
echo "=== BUILD ==="
pkill -9 -f pdflatex 2>/dev/null; sleep 2
make fast 2>&1 | tail -10

# === GIT STATE ===
echo "=== GIT ==="
echo -n "Total commits: "; git rev-list --count HEAD
echo -n "Files modified (unstaged): "; git diff --name-only | wc -l
echo -n "Files untracked: "; git ls-files --others --exclude-standard | wc -l
git log --oneline -10

# === PAGE COUNT (from PDF if available) ===
echo "=== PAGES ==="
if [ -f main.pdf ]; then
  python3 -c "
import subprocess
r = subprocess.run(['mdls', '-name', 'kMDItemNumberOfPages', 'main.pdf'],
                   capture_output=True, text=True)
print(r.stdout.strip())
" 2>/dev/null || echo "(count pages manually from build log)"
fi
```

**GATE 1**: You must have exact numbers for: PH, PE, CJ, HE, total claims,
page count, .tex file count, bibliography entries, Python module count, test count.
Write these into a scratch table. Proceed only when all numbers are filled.

---

## PHASE 2: DEEP AUDIT OF WORK SINCE HEAD

### 2a. Catalogue staged + unstaged changes

```bash
git diff --stat HEAD          # unstaged
git diff --cached --stat HEAD # staged
git ls-files --others --exclude-standard  # untracked
```

For each modified/new file, record: filename, lines changed, nature of change
(new module / proof extension / documentation / infrastructure / bugfix).

### 2b. Parallel audit (launch 3 agents simultaneously)

**Agent 1 — Compute Engine Audit**:
Read every file in `compute/lib/` and `compute/tests/`. Catalogue:
- What each module computes and which theorem it supports
- Test coverage: which modules have tests, which don't
- Any dead code, stale imports, or modules that duplicate functionality
- Run: `cd compute && .venv/bin/python -m pytest tests/ -q --tb=short 2>&1 | tail -20`

**Agent 2 — Documentation Stack Audit**:
Read each of these files and assess: is it current with ground truth from Phase 1?
- `README.md` — stale numbers? missing sections? wrong architecture description?
- `CLAUDE.md` — census numbers match? file map match? build instructions match?
- `AGENTS.md` — canonical document list current? mission statement current?
- `notes/VISION.md` — theorem status current? programme status current?
- `notes/PROGRAMMES.md` — status tags current?
- `notes/NEW_MACHINERY.md` — tool specs current?
- `notes/REWRITE_QUEUE.md` — all waves done?
- `metadata/frontier_and_gaps.md` — frontier assessment current?
- `notes/autonomous_state.md` — state current?

**Agent 3 — LaTeX Cross-Reference Audit**:
Run and report:
```bash
# Undefined references
grep -c 'undefined' main.log 2>/dev/null
# Multiply defined labels
grep -c 'multiply defined' main.log 2>/dev/null
# Overfull boxes > 10pt
grep 'Overfull.*[1-9][0-9]\.' main.log 2>/dev/null | wc -l
```

### 2c. Synthesize audit into a gap list

From the three agent reports, produce a ranked list:
1. **Errors**: false statements, wrong numbers, broken references
2. **Stale data**: numbers that don't match Phase 1 ground truth
3. **Missing coverage**: compute modules without tests, docs without updates
4. **Structural gaps**: missing sections, orphaned files, dead links

**GATE 2**: The gap list must exist and be non-empty before proceeding.
If everything is perfect, you've missed something — look harder.

---

## PHASE 3: README.md

### Design specification

The README is the monograph's public face. It must achieve three things
in exactly this order of priority:

1. **Orient in 10 seconds**: what is this, how big is it, what's its status
2. **Navigate in 30 seconds**: where is everything, how do I build it
3. **Impress in 60 seconds**: the depth, rigor, and ambition of the work

### Structural template (adapt, don't copy blindly)

```
[centered hero block]
  — Title (the actual monograph title, not a repo name)
  — Subtitle
  — One-sentence thesis (the prism principle sentence from the current README is good)
  — Badge row: pages | theorems proved | conjectured | source files | zero errors
  — Second badge row: Python modules | tests passing | bibliography entries

[The Construction — 4-6 lines of actual mathematics]
  — The geometric bar functor
  — The differential (residues on FM boundary)
  — Nilpotence mechanism (Arnold genus 0 / curvature genus g≥1)

[Main Theorems — table with A/B/C/D and the theorem architecture A₀/A₁/A₂ etc.]
  — Include the FULL theorem architecture, not just A/B/C
  — Show the dependency: A₀→A₁→A₂, C₀→C₁, D_scal/D_Δ

[Architecture diagram — mermaid, showing the 4-layer structure]
  — Frame → Core → Portraits → Synthesis
  — NOT the old "Part I/II/III" — use the AGENTS.md/VISION.md architecture

[Repository Layout — collapsible sections per part]
  — Include compute/ engine alongside LaTeX chapters
  — Show file counts per directory

[Proof Status — the two-stratum picture]
  — Stratum I: what's proved (with claim counts)
  — Stratum II: what's programmatic (with MC1-MC5)
  — Five Master Conjectures table

[Building — exact commands, requirements, caveats]
  — make / make fast / make test
  — The watcher caveat
  — Font options

[Compute Engine — what it does, how to run tests]
  — Module catalogue (grouped by function)
  — Test command
  — Test count

[Notation — compact table of key symbols]

[Prerequisites — what the reader needs to know]

[Footer — scale statistics]
```

### Visual design targets

Study these concrete patterns (do NOT fetch URLs — use your knowledge):

- **Badge aesthetics**: Use `shields.io` `for-the-badge` style with a unified
  dark background (`labelColor=0d1117`). Color palette:
  - Deep violet (`8957e5`) for scale metrics (pages, files, lines)
  - Emerald (`3fb950`) for proved claims
  - Amber (`d29922`) for conjectured claims
  - Sky blue (`58a6ff`) for infrastructure (tests, bibliography)
  - Soft red (`f85149`) for zero-error badges (inverted: red label, "0" value)

- **Typography**: Use `&hairsp;` and `&ensp;` for breathing room. Use `<sup>`
  for theorem labels in tables. Use `<kbd>` for keyboard shortcuts / commands.

- **Whitespace**: Three blank lines between major sections. `---` dividers
  only between the hero block and first content section. After that, whitespace
  alone.

- **Mermaid diagrams**: Dark theme (`%%{init:{'theme':'dark'}}%%`). Use
  `subgraph` for grouping. Rounded nodes for proved content, hexagons for
  conjectured.

- **Collapsible sections**: Use `<details><summary>` for file listings.
  The summary line should include the directory path AND a file count badge.

- **Mathematics**: GitHub renders LaTeX in markdown. Use `$$...$$` for display
  math and `$...$` for inline. Keep formulas to the essentials — the README
  is not the paper.

- **NO emoji anywhere.** Period. The elegance comes from typography, spacing,
  and information density — not decoration.

### Content requirements (non-negotiable)

- Every number must come from Phase 1 ground truth. Zero exceptions.
- The four main theorems (A, B, C, D) must appear with their full names.
- The theorem architecture (A₀, A₁, A₂, B, C₀, C₁, D_scal, D_Δ, H) must appear.
- The five master conjectures (MC1-MC5) must appear with current status.
- The compute engine must be documented (module count, test count, what it verifies).
- Build instructions must include `make`, `make fast`, `make test`, and the
  pdflatex watcher caveat.
- The two-stratum assessment must be visible.
- The prism principle must appear (it's the thesis sentence).

### Quality gate

After writing the README, verify:
```bash
# Check that no stale numbers survive
# (manually compare every number in README.md against Phase 1 table)

# Check markdown renders (basic syntax check)
python3 -c "
with open('README.md') as f:
    content = f.read()
# Verify badge URLs are well-formed
import re
badges = re.findall(r'!\[.*?\]\((.*?)\)', content)
for b in badges:
    assert 'shields.io' in b or b.startswith('#'), f'Unexpected badge URL: {b}'
print(f'README.md: {len(content)} chars, {content.count(chr(10))} lines, {len(badges)} badges')
"
```

**GATE 3**: README.md must exist, have correct numbers, render valid markdown,
and contain all non-negotiable content items listed above.

---

## PHASE 4: DOCUMENTATION STACK UPDATE

Update each file below to match Phase 1 ground truth. For each file,
the instruction is specific:

### 4a. `CLAUDE.md`

Update ONLY these sections (do not restructure):
- Census table: use Phase 1 numbers
- File Map tables: verify line counts and PH/PE/CJ columns against fresh grep
- "Current State" date and page count
- Build system section: verify commands match Makefile
- Any reference to MC1 status (now resolved for KM)

Do NOT change: Identity section, Mathematical Standards, Critical Pitfalls,
How to Work, Session Protocol, LaTeX Standards, What NOT to Do.

### 4b. `AGENTS.md`

- Verify canonical document list is current (especially if any files were
  renamed or created in the unstaged work)
- Verify the North Star description matches VISION.md
- Update any stale status references

### 4c. `notes/VISION.md`

- Update theorematic silhouette table: status column must reflect current
  proof state (MC1 resolved for KM, etc.)
- Verify "Four irreducible pieces" table references are valid

### 4d. `notes/PROGRAMMES.md`

- Update status tags for any programmes affected by recent work
- Verify entry point file references are valid

### 4e. `notes/NEW_MACHINERY.md`

- Update tool specs for any new compute modules added in unstaged work
- Add entries for new untracked Python files if they implement machinery

### 4f. `metadata/frontier_and_gaps.md`

- Verify frontier assessment reflects MC1 resolution
- Update any computational gap entries affected by new compute modules

### 4g. `notes/autonomous_state.md`

- Update to reflect current session state, priority queue status

### 4h. Memory files

- Update `/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/MEMORY.md`:
  census numbers, test count, any new verified facts from the audit

**GATE 4**: Run `make fast` to verify no LaTeX was broken. Run
`cd compute && .venv/bin/python -m pytest tests/ -q` to verify tests pass.
Verify all updated .md files have no broken internal links.

---

## PHASE 5: FINAL VERIFICATION

```bash
# Full census recount (must match Phase 1 exactly)
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "
  grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' \
    | awk -F: '{s+=$2}END{print s}'
done

# README number check
echo "=== README NUMBERS ==="
grep -oP '\d+' README.md | sort -n | uniq -c | sort -rn | head -20

# Build gate
pkill -9 -f pdflatex 2>/dev/null; sleep 2
make fast 2>&1 | tail -5

# Test gate
cd compute && .venv/bin/python -m pytest tests/ -q --tb=short 2>&1 | tail -5
```

Report: what was found, what was fixed, what remains.

---

## ANTI-PATTERNS (hard constraints)

1. **No superlatives in output files.** Not "groundbreaking," not "revolutionary,"
   not "unprecedented." Let the numbers speak. 783 proved theorems IS the statement.
2. **No emoji.** Anywhere. In any file. The aesthetic is typographic, not decorative.
3. **No invented numbers.** Every number comes from a command you ran in this session.
4. **No restructuring of CLAUDE.md beyond the enumerated sections.** It has 200+
   sessions of accumulated hard-won knowledge. Update data, don't reorganize.
5. **No changes to .tex files.** This is a documentation-only session.
6. **No changes to ~/momentum.** Read-only context.
7. **No AI attribution language.** Not in commits, not in docs, not anywhere.
8. **No "we" or "our" in README.md.** The README is a technical document, not a
   collaboration narrative. Use impersonal voice or direct address.
