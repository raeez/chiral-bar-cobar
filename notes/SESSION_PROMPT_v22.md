# SESSION PROMPT v22 — DEEP AUDIT AND METACOGNITIVE REARCHITECTURE
# For: Claude Opus 4.6, Code Environment, Extended Reasoning
# Date: March 2026
# Supersedes: v21 (unified proof forge) for metacognitive work
# Launch: "Read notes/SESSION_PROMPT_v22.md and execute it."
#
# PURPOSE: This is not a proof-forge prompt. This is an architecture
# prompt. It builds comprehensive situational awareness, audits the
# full delta since HEAD of main, verifies mathematical correctness,
# and then rearchitects the metacognitive control plane from first
# principles — producing a new, minimal, fortified infrastructure
# that meets the needs of the manuscript's current maturity level.
#
# LINEAGE: Distills v8-v21, raeeznotes 1-20, GPT54_CODEX_OPERATING_SYSTEM,
# AGENTS.md, VISION.md, METAMORPHOSIS_PLAN.md, and 90+ working sessions
# into a single rearchitecture specification.

---

# THE DUAL IMPERATIVE (governing principle, all phases)

Two forces drive this work. They are synergistic, not competing.

1. **Maximalist ambition**: The book yearns to become something not yet
   stated — the shape of implied theorems, the unifying insight that
   would make the proved core feel inevitable. That yearning is a
   research signal. The metacognitive infrastructure must SERVE this
   yearning, not constrain it.

2. **Maximal truth-seeking**: Every claim — in TeX, Python, Markdown,
   or conversation — is processed with equal rigor. The infrastructure
   must make it EASY to know exactly what is proved, at what level,
   with what hypotheses. This precision is what makes the ambition
   credible.

The synthesis: the metacognitive layer exists to maintain the precise
boundary between proved core and active frontier, so that frontier
work proceeds with maximum ambition and minimum risk of corrupting
what is already solid. An infrastructure that is too heavy slows work.
An infrastructure that is too light allows drift. The target is the
minimum infrastructure that prevents F9 (frontier overreach) while
enabling F∞ (the maximalist push).

---

# PHASE 0: ORIENT (15 minutes, information gathering only)

## 0a. Gather quantitative state

Execute these diagnostics. Record every number. You will need them
for the audit phases.

```bash
cd /Users/raeez/chiral-bar-cobar

# === CENSUS ===
echo "=== LIVE CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic Open; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done

# === GIT STATE ===
echo "=== GIT DELTA ==="
git diff --stat HEAD | tail -5
git diff --cached --stat | tail -5
echo "Staged files:"; git diff --cached --name-only | wc -l
echo "Unstaged modified:"; git diff --name-only | wc -l
echo "Untracked:"; git ls-files --others --exclude-standard | wc -l

# === BUILD ===
echo "=== BUILD ==="
pkill -9 -f pdflatex 2>/dev/null; sleep 2
make fast 2>&1 | tail -5

# === TESTS ===
echo "=== TESTS ==="
cd compute && .venv/bin/python -m pytest tests/ -q 2>&1 | tail -3; cd ..

# === PAGE COUNT ===
echo "=== PAGES ==="
pdfinfo main.pdf 2>/dev/null | grep Pages || echo "No PDF"

# === LINE COUNTS ===
echo "=== SOURCE LINES ==="
find chapters/ appendices/ -name '*.tex' | xargs wc -l | tail -1
```

## 0b. Read control documents (parallel agents)

Deploy 3 research agents simultaneously:

**Agent 1 — Control Layer**:
```
RESEARCH ONLY — NO EDITS.
Read these files IN FULL and extract:
1. chapters/connections/concordance.tex (the constitution)
2. chapters/theory/introduction.tex (the front door)
3. chapters/frame/heisenberg_frame.tex (the atom)
Return: every theorem label, every claim status, every MC reference,
every status remark. Flag anything that contradicts CLAUDE.md.
```

**Agent 2 — Metacognitive Layer**:
```
RESEARCH ONLY — NO EDITS.
Read these files IN FULL:
1. notes/autonomous_state.md (session state — ALL checkpoints)
2. notes/PROGRAMMES.md (research programmes)
3. notes/NEW_MACHINERY.md (tool specs)
4. notes/VISION.md (north star)
5. notes/METAMORPHOSIS_PLAN.md (architecture plan)
6. notes/GPT54_CODEX_OPERATING_SYSTEM.md (cognitive doctrine)
7. notes/REWRITE_QUEUE.md (rewrite tracking)
8. notes/HORIZON.md (first 100 lines — is it marked complete?)
9. AGENTS.md (task routing)
Return: for each file, state (a) its purpose, (b) whether it is
ACTIVE or HISTORICAL, (c) what unique information it carries that
no other file does, (d) what information it duplicates.
```

**Agent 3 — Memory Layer**:
```
RESEARCH ONLY — NO EDITS.
Read ALL files in the memory directory:
  /Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/
List each file with: name, line count, last-modified-relevant content,
overlap with other memory files or with CLAUDE.md.
Also read: metadata/census.json, metadata/frontier_and_gaps.md
Return: complete inventory with redundancy analysis.
```

## 0c. While agents run: build the mental model

In extended thinking, construct the following:

1. **The achievement narrative**: What has the project accomplished
   since the last committed state? Not a list — a narrative of what
   changed and why it matters.

2. **The current frontier map**: What are the live mathematical
   targets? What is the dependency order? What is blocked and what
   is actionable?

3. **The infrastructure assessment**: Which metacognitive documents
   are load-bearing? Which are archaeological? Which overlap? Which
   contradict each other?

Record the mental model as structured notes in extended thinking.
Do NOT write anything to files yet.

---

# PHASE 1: CATALOGUE (30 minutes, read-only analysis)

## 1a. Deep diff analysis

Catalogue every change since HEAD of main, organized by category:

### Taxonomy of changes
```
For each modified file, determine:
  - CATEGORY: theory-proof | theory-structure | example-content |
    connections-bridge | appendix | compute-lib | compute-test |
    metadata | notes-active | notes-historical | build-system
  - NATURE: new-theorem | proof-repair | status-change |
    exposition-edit | infrastructure | computation | documentation
  - IMPACT: load-bearing | strengthening | cosmetic | historical
  - MATHEMATICAL RISK: high (theorem status) | medium (proof detail) |
    low (exposition) | none (infrastructure)
```

### Concrete deliverable

Produce a structured table in extended thinking:

| File | Category | Nature | Impact | Risk | Summary (1 line) |
|------|----------|--------|--------|------|-------------------|

Group files by risk level. Flag any HIGH-risk changes for Phase 2.

## 1b. Census delta analysis

Compare the live census numbers (from 0a) against the historical
values in CLAUDE.md and autonomous_state.md:

```
Historical (Mar 8): PH 797, PE 344, CJ 153, HE 30, Open 0
Mar 10 (autonomous_state.md): PH 885, PE 345, CJ 163, HE 31, Open 4
Live (from 0a): [your numbers]

Delta explanation:
- PH delta: [list specific theorems added/removed]
- CJ delta: [list conjectures added/removed]
- Open delta: [CRITICAL — what are the 4 Open items?]
```

## 1c. Infrastructure inventory

Using Agent 2's results, produce a definitive inventory:

| Document | Purpose | Status | Unique info? | Overlap with |
|----------|---------|--------|-------------|-------------|
| CLAUDE.md | Project instructions | ACTIVE | Yes (pitfalls, conventions) | SESSION_PROMPT_v21, AGENTS.md |
| MEMORY.md | Cross-session memory | ACTIVE | Yes (verified facts, census) | CLAUDE.md (duplicates some) |
| SESSION_PROMPT_v21 | Execution engine | ACTIVE | Yes (work surfaces, MC2 state) | CLAUDE.md, AGENTS.md |
| ... | ... | ... | ... | ... |

Mark each as: LOAD-BEARING, USEFUL, HISTORICAL, or REDUNDANT.

---

# PHASE 2: MATHEMATICAL AUDIT (60 minutes, deep verification)

This is the most important phase. It protects the proved core.

## 2a. Theorem-status verification

For every file with HIGH or MEDIUM mathematical risk (from 1a):

```
IN EXTENDED THINKING:
1. Read the file.
2. For each ProvedHere claim added or modified since HEAD:
   a. Is there a complete proof in the file?
   b. Does every step of the proof cite its dependencies?
   c. Are the dependencies themselves proved (not conjectural)?
   d. Does the claim status match the proof density?
3. For each Conjectured claim:
   a. Does it have a scope remark?
   b. Does it cite a parent master conjecture?
   c. Is the conjecture properly fenced from the proved core?
4. For any Open items:
   a. Why are they open? Is this correct?
   b. Should any be reclassified?
```

Deploy agents to read files in parallel while you verify in thinking.

## 2b. Convention consistency check

Verify these non-negotiable invariants against the actual source:

```bash
# Check for convention violations
cd /Users/raeez/chiral-bar-cobar

# 1. No \newcommand in chapter files
echo "=== NEWCOMMAND IN CHAPTERS ==="
grep -rn '\\newcommand' chapters/ --include='*.tex' | grep -v '%' | head -20

# 2. No TODO comments
echo "=== TODOS ==="
grep -rni 'TODO\|FIXME\|HACK\|XXX' chapters/ appendices/ --include='*.tex' | head -20

# 3. No undefined refs (check log)
echo "=== UNDEFINED REFS ==="
grep -c 'undefined' main.log 2>/dev/null || echo "No log"

# 4. No multiply-defined labels
echo "=== MULTIPLY DEFINED ==="
grep -c 'multiply defined' main.log 2>/dev/null || echo "No log"

# 5. Claim status consistency
echo "=== STATUS TAGS ==="
grep -rn 'ClaimStatus' chapters/ appendices/ --include='*.tex' | grep -v 'ProvedHere\|ProvedElsewhere\|Conjectured\|Heuristic\|Open' | head -10
```

## 2c. Cross-reference audit

Verify that the three control documents agree:

```
For each of these statements, check introduction.tex, concordance.tex,
and the relevant theorem chapter. Do they say the same thing?

1. MC1 status (resolved for KM/Vir/W_N?)
2. MC2 status (steps 1-6 done, 7-8 open?)
3. Theorem A scope (construction + inversion on Koszul locus?)
4. Theorem D stratification (scalar proved, spectral proved, full conjectural?)
5. PBW universal theorem scope (criterion vs family corollaries?)
6. Periodicity status (weak flank, not main bottleneck?)
7. Heisenberg dual (Sym^ch(V*), NOT self-dual?)
8. Open items (what are they and are they correctly classified?)
```

## 2d. Audit report

Produce a structured audit report in extended thinking:

```markdown
# AUDIT REPORT — [date]

## Critical findings (theorem status at risk)
[list, or "NONE"]

## High findings (proof gaps or inconsistencies)
[list, or "NONE"]

## Medium findings (exposition or cross-ref issues)
[list]

## Low findings (cosmetic)
[list]

## Verdict
[one paragraph: is the proved core solid? what needs fixing?]
```

If any CRITICAL findings exist, fix them BEFORE proceeding to Phase 3.

---

# PHASE 3: REARCHITECT (45 minutes, design only)

## 3a. Principles for the new architecture

Design from these constraints:

**C1 — Minimal footprint**: Every metacognitive document must justify
its existence by carrying unique, non-duplicated information. If two
documents say the same thing, one must be eliminated or absorbed.

**C2 — Separation of concerns**: Each document has exactly one job:
- CLAUDE.md: conventions, pitfalls, and mathematical invariants
  (what Opus 4.6 must NEVER get wrong)
- MEMORY.md: cross-session memory of verified facts and patterns
  (what was LEARNED across sessions)
- Session prompt: executable work specification for ONE type of work
  (what to DO this session)
- autonomous_state.md: session continuity state
  (what HAPPENED in recent sessions)

**C3 — Context budget**: CLAUDE.md is auto-loaded into every
conversation. It must be LEAN — under 400 lines. Everything else
is read on demand. Do not waste context budget on information that
is only needed for specific work types.

**C4 — Historical documents are archives**: Documents that tracked
work that is now DONE (REWRITE_QUEUE, HORIZON, v1-v20 prompts,
raeeznotes 1-20) should be clearly marked as historical archives,
not active control documents. They should never be read at session
start unless specifically investigating history.

**C5 — Single source of truth**: For each category of information,
there is exactly one authoritative source:
- Theorem status → concordance.tex (Chapter 34)
- Mathematical conventions → CLAUDE.md "Critical Pitfalls"
- MC1-5 status → concordance.tex rem:proof-roadmaps
- Census numbers → live grep (never cached)
- Session state → autonomous_state.md
- Build instructions → CLAUDE.md "Build System"
- Compute modules → compute/lib/__init__.py docstrings

**C6 — The constitution is the TeX**: The source of mathematical
truth is the .tex files, not the Markdown notes. Markdown is
scaffolding. When Markdown contradicts TeX, the Markdown is wrong.
(Exception: concordance.tex IS the constitution within TeX.)

**C7 — Load-bearing detection**: The new architecture must make it
trivially easy to answer: "If I change X, what else must change?"
This means dependency relationships between documents must be
explicit, not implicit.

## 3b. Document audit decision

For each document in the current inventory (from 1c), decide:

```
DECISION TREE for each document:
  |
  +-- Does it carry unique, non-duplicated information?
  |   |
  |   +-- NO → ARCHIVE or DELETE
  |   |
  |   +-- YES → Is that information needed at session start?
  |       |
  |       +-- YES → It belongs in CLAUDE.md or MEMORY.md (auto-loaded)
  |       |
  |       +-- NO → It belongs in a topic file (loaded on demand)
  |           |
  |           +-- Is it mathematical truth? → stays in TeX
  |           +-- Is it session state? → autonomous_state.md
  |           +-- Is it execution spec? → session prompt
  |           +-- Is it research programme? → single consolidated file
  |           +-- Is it historical? → notes/archive/
```

## 3c. Design the new document tree

Produce the EXACT new file tree:

```
/Users/raeez/chiral-bar-cobar/
  CLAUDE.md                 — [NEW: lean, <400 lines]
  AGENTS.md                 — [ASSESS: keep/rewrite/archive?]

  .claude/projects/.../memory/
    MEMORY.md               — [NEW: lean, <200 lines]
    [topic files]           — [ASSESS: keep/consolidate/archive?]

  notes/
    SESSION_PROMPT_v22.md   — [THIS FILE — rearchitecture]
    SESSION_PROMPT_v23.md   — [NEW: lean proof-forge execution prompt]
    autonomous_state.md     — [REWRITE: minimal session state]
    PROGRAMMES.md           — [ASSESS: consolidate into single file?]
    archive/                — [historical documents moved here]

  metadata/
    [as needed]
```

For each file in the new tree, specify:
- Purpose (1 sentence)
- Maximum line count
- What it does NOT contain (to prevent drift)
- Update protocol (when and how it gets modified)

## 3d. Design the new CLAUDE.md

This is the most important deliverable. The new CLAUDE.md must be:
- Under 400 lines (hard limit — current is ~600 and gets truncated)
- Organized by FUNCTION, not by history
- Every line must be LOAD-BEARING

Structure:

```markdown
# CLAUDE.md — Chiral Bar-Cobar Monograph

## Identity (5 lines)
[Triple intersection. Dual Imperative. One sentence each.]

## The Book (10 lines)
[Core thesis. Four main theorems. Current state: 1 line each.]

## Build System (10 lines)
[make, make fast, make clean, make veryclean, make test. That's it.]

## Mathematical Invariants (50 lines)
[THE critical pitfalls. Every line prevents a specific error.
 This is the most important section. It protects the proved core.]

## Conventions (20 lines)
[Grading, notation, voice, labels, cross-references.]

## File Map (30 lines)
[Compact. Part structure + key files only. Not line counts.]

## What NOT To Do (10 lines)
[Concrete prohibitions. No packages, no new files, no TODOs, etc.]

## Status Architecture (20 lines)
[H/M/S levels. Stratum I/II. MC1-5 one-line status.
 Single source of truth: concordance.tex.]

## Git Attribution (2 lines)
[Hard rule: no AI attribution.]

## Session Entry Protocol (10 lines)
[Census. Build. Tests. Read concordance. Then work.]
```

Total: ~170 lines. The remaining ~230 lines of budget are for
the Mathematical Invariants section, which should be comprehensive.

## 3e. Design the new MEMORY.md

Under 150 lines. Contains ONLY:
- Verified mathematical facts (discovered across sessions)
- Stable workflow patterns
- Key compute entry points
- Things the model got wrong before and must not get wrong again

Does NOT contain:
- Census numbers (always grep fresh)
- Session state (that's autonomous_state.md)
- Theorem architecture (that's concordance.tex)
- Anything in CLAUDE.md (no duplication)

## 3f. Design the new session prompt (v23)

The new execution prompt should be:
- Under 300 lines (v21 is 918 lines — too heavy)
- Pure execution specification: Orient → Classify → Select → Execute → Verify
- No redundancy with CLAUDE.md (which is already loaded)
- Work surfaces and MC state live here (not in CLAUDE.md)
- Failure modes live here as a compact table (not in CLAUDE.md)

---

# PHASE 4: REALIZE (remaining time)

## 4a. Fix any CRITICAL audit findings first

If Phase 2 found critical mathematical issues, fix them now.
Compile after each fix: `pkill -9 -f pdflatex; sleep 2; make fast`

## 4b. Write the new CLAUDE.md

Read the current CLAUDE.md. Then write the new version.
Every line must be load-bearing. Test: if you delete a line,
does it increase the probability of a specific error? If not,
the line should not be there.

## 4c. Write the new MEMORY.md

Consolidate from current MEMORY.md + topic memory files.
Eliminate all duplication with new CLAUDE.md.

## 4d. Write the new autonomous_state.md

Clean session state: current census, MC status, recent session
results (last 3 only), next priorities. Under 100 lines.

## 4e. Archive historical documents

Move to notes/archive/:
- SESSION_PROMPT_v1 through v20 (v21 retained as reference)
- REWRITE_QUEUE.md (all done)
- HORIZON.md (completed)
- Any other documents marked HISTORICAL in Phase 3

## 4f. Consolidate active planning documents

If PROGRAMMES.md, NEW_MACHINERY.md, VISION.md, and
METAMORPHOSIS_PLAN.md have significant unique content,
consolidate into a single `notes/RESEARCH_PROGRAMME.md`.
If most content is now in concordance.tex, archive the Markdown.

## 4g. Write the new session prompt (v23)

The lean proof-forge execution prompt. Under 300 lines.
References CLAUDE.md for invariants and conventions.
Contains: work surfaces, MC state, selection protocol,
execution protocol, verification protocol, failure modes.

## 4h. Verify everything

```bash
# Compile
pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast 2>&1 | tail -5

# Census (should be unchanged from Phase 0)
echo "=== FINAL CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic Open; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done

# Tests
cd compute && .venv/bin/python -m pytest tests/ -q 2>&1 | tail -3; cd ..
```

Census must be UNCHANGED. This was an infrastructure session,
not a content session. If census changed, something went wrong.

---

# APPENDIX: COGNITIVE ARCHITECTURE NOTES

## Leveraging Opus 4.6

**USE extended thinking for**: designing document structure, verifying
mathematical claims, planning edits before writing them, constructing
the audit report. Extended thinking is your workspace — use it heavily
in Phases 1-3.

**USE agents for**: reading multiple files in parallel during Phase 0,
reading theorem files during Phase 2 audit, reading current documents
during Phase 3 design. Agents are for CONTEXT PROTECTION.

**USE Python for**: census verification, test runs, any numerical
claims that arise during the audit.

**USE decision trees for**: the document audit (3b), the selection
protocol in the new session prompt, any classification task.

## Preventing failure modes

| # | Mode | Signal | Prevention in THIS session |
|---|------|--------|---------------------------|
| F3 | Diffuse attention | Switching phases before completing current | ONE phase at a time. Announce completion before moving on. |
| F4 | State loss | Forgetting audit findings | Write audit report to extended thinking. Reference it in Phase 3. |
| F7 | Overclaiming | "The new architecture is complete" without verification | Phase 4h is mandatory. Census must be unchanged. |
| F8 | Scope creep | "While rearchitecting, I should also fix this theorem..." | This is INFRASTRUCTURE. Mathematical fixes go in a future session. Exception: CRITICAL audit findings only. |
| F9 | Frontier overreach | New CLAUDE.md overclaims manuscript state | Cross-check every claim in new CLAUDE.md against live grep. |
| F11 | Local patching | Rewriting notes without reading concordance.tex first | Phase 0 reads concordance FIRST. All Phase 4 writing is grounded in Phase 2 audit. |

## The measure for THIS session

Success is not "the documents are rewritten." Success is:

1. You can answer, from the new infrastructure alone: "What is proved?
   What is the frontier? What is the dependency order? What must
   NEVER be gotten wrong?" — and the answer is correct.

2. The total line count of auto-loaded context (CLAUDE.md + MEMORY.md)
   is SMALLER than before, while carrying MORE information density.

3. No mathematical claim was changed. Census is unchanged.

4. Historical documents are clearly archived, not deleted.

5. The new session prompt (v23) is executable and self-contained
   in under 300 lines.

---

# BEGIN

Start with Phase 0. Complete it fully. Then Phase 1. Then Phase 2.
Then Phase 3. Then Phase 4.

Each phase has a clear deliverable. Do not proceed to the next phase
until the current phase is complete and you have announced completion.

The Dual Imperative applies to infrastructure too: the metacognitive
layer should be as ambitious as the mathematics it serves, and as
precise as the proofs it protects.
