# SESSION PROMPT v10 — Depth Engine
# For: Claude Opus 4.6, Code Environment, Extra-High Reasoning Mode
# Date: March 2026
# Supersedes: v1-v9, all specialized prompts
# Launch: "Read notes/SESSION_PROMPT_v10.md and execute it."

# ======================================================================
# WHY v10 EXISTS
#
# v1-v9 all shared a fatal pattern:
#   Orient (15-20%) -> Audit fixes (40-60%) -> CRASH before math depth
#
# Over ~130 sessions, the audit backlog has been reduced from 234 to 12.
# The mathematical depth work — the thing that actually improves the
# book — has NEVER been reached. Not once.
#
# v10 inverts the architecture:
#   - Orientation: 2 min (read pre-verified state, not re-audit)
#   - Warmup fixes: 0-30 min (optional, pre-specified to the line)
#   - Mathematical depth: 80% of session (pre-scored, pre-specified)
#
# Opus 4.6 design:
#   LEVERAGE: Extended thinking for sustained mathematical derivation
#   LEVERAGE: Python verification as structural proof-checking
#   LEVERAGE: Pre-specified insertion points (no searching = no waste)
#   LEVERAGE: Single target announced in first 5 tool calls
#   PREVENT: Orientation overhead (ground_truth file replaces re-auditing)
#   PREVENT: Audit gravity (fix_queue is bounded and optional)
#   PREVENT: Target diffusion (pre-scored targets, pick highest, commit)
#   PREVENT: State loss (checkpoint at tool calls 50, 100)
#   PREVENT: Hallucination (Python template for every formula)
#   PREVENT: Sycophantic convergence (adversarial self-check protocol)
# ======================================================================

---

## 0. ORIENT (2 minutes — this replaces re-auditing)

```bash
cd /Users/raeez/chiral-bar-cobar

# Verify ground truth hasn't drifted (3 numbers, 30 seconds)
echo -n "PH: "; grep -rc '\\ClaimStatusProvedHere' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
echo -n "Tests: "; cd compute && .venv/bin/python -m pytest tests/ -q 2>&1 | tail -1; cd ..
make fast 2>&1 | tail -1
```

Expected: PH ~695, 1187 passed, Output written on main.pdf.
If ANY of these fail: stop, diagnose, do not proceed.

Read ONE file: `memory/ground_truth_mar2026.md` (45 lines).
You now know everything. Do not read CLAUDE.md, PROGRAMMES.md, HORIZON.md,
autonomous_state.md, or any other planning document. The ground truth file
is the single source of truth.

---

## 1. CHOOSE (1 minute — in extended thinking, not tool calls)

Two paths. Pick one. Announce it. Never switch.

### Path A: WARMUP + DEPTH (recommended for fresh sessions)
1. Do quick fixes F1-F7 from `memory/fix_queue.md` (30 min)
2. Then execute highest-scoring depth target from `memory/depth_targets.md`

### Path B: DEPTH ONLY (recommended when fix queue is done)
1. Execute highest-scoring depth target directly

Read `memory/depth_targets.md`. The targets are pre-scored:
- **D1** (Phi on Verma, score 100) — if module theory is the goal
- **D3** (BRST=bar, score 64) — if physics connection is the goal
- **D4** (Discriminant spectral, score 60) — if computational discovery is the goal

Announce: "Path [A/B], target D[N]: [one-line description]"

---

## 2. WARMUP FIXES (if Path A — 30 min max, then STOP fixing)

Read `memory/fix_queue.md`. Execute F1-F7 (quick wins only).
Each fix is specified to the exact line. Do not investigate. Do not explore.
Read the file, make the edit, move on.

After all quick fixes: `make fast 2>&1 | tail -3`
If clean: proceed to depth. If not: fix compilation only, then proceed.

**HARD RULE**: Do not touch F8-F12. Do not discover new fixes. Do not audit.
The warmup is BOUNDED. When the 30-minute timer (or F7) is done, switch to depth.

---

## 3. GATHER (10 min — agents read, you plan)

Deploy up to 2 agents. Each reads specific files and returns structured data.

```
RESEARCH ONLY — NO EDITS.
Read: [specific files from depth_targets.md]
Extract:
  1. Exact theorem statements I need as input (quote the LaTeX)
  2. Label names for cross-references
  3. Insertion point: file:line for the new content
  4. Convention warnings (signs, gradings, notation)
Return as: label | statement | file:line
Flag anything contradicting memory/ground_truth_mar2026.md pitfalls.
```

While agents run: in extended thinking, write the MATHEMATICAL STATEMENT
you intend to prove. Not LaTeX. Not prose. The mathematical content:
- Hypotheses (quote exact conditions from cited theorems)
- Construction (what functor/map/computation you will perform)
- Conclusion (what the output is, identified as a named object)

If you cannot write this statement: you are not ready. Read more.

---

## 4. DERIVE (40-60 min — this is where the session lives or dies)

### Extended thinking protocol
Work in extended thinking FIRST. Do NOT write LaTeX yet.
The derivation has three mandatory stages:

**Stage 1: Hypothesis verification**
For every theorem you cite in the proof chain:
- State its hypotheses (quote exact wording from manuscript)
- Verify each hypothesis holds in your specific case
- If ANY hypothesis fails: stop, find alternative, or document obstruction

**Stage 2: Step-by-step derivation**
- Every formula DERIVED, not recalled
- Track signs EXPLICITLY (never "up to sign")
- Track gradings EXPLICITLY (cohomological degree, conformal weight, bar degree)
- If you write a number: compute it. If you cite a formula: verify it.

**Stage 3: Self-adversarial check**
Before writing ANY LaTeX, ask:
- "What would a referee specializing in [operads/vertex algebras/config spaces] attack?"
- "Which step would I be embarrassed about if pressed for details?"
- "Is there a simpler case I can verify first (sl2, degree 1)?"

### Python verification (mandatory for every new formula)
```python
from fractions import Fraction
# [computation matching depth_targets.md template]
# EVERY intermediate step as a variable
# EVERY final answer with an assert
assert result == expected, f"MISMATCH: {result} vs {expected}"
print(f"VERIFIED: {result}")
```

### Dimensional consistency (before ANY formula)
- Conformal weight balances both sides
- Cohomological degree correct
- Bar degree correct
- Number of terms matches combinatorial prediction

---

## 5. WRITE (15-20 min — only after derivation is COMPLETE and verified)

1. Read target file at insertion point (±50 lines)
2. Write using manuscript conventions:
   - `\ClaimStatusProvedHere` on every new theorem/proposition
   - `\label{thm:xxx}` / `\label{comp:xxx}` / `\label{prop:xxx}`
   - Cross-reference via `\ref{}` to every theorem in the derivation chain
   - Voice: impersonal ("we construct", "one verifies")
   - Index entries: `\index{keyword|textbf}` for new definitions
3. `make fast` after EACH insertion (max 2 edits between compiles)
4. Fix any compilation issues before the next edit

### LaTeX non-negotiables
- NO `\newcommand` in chapter files
- Use existing macros: `\chirAss`, `\chirCom`, `\chirLie`, `\Eone`, `\Einf`, `\Pinf`, `\B`, `\cA`
- Label scheme: `def:`, `thm:`, `prop:`, `lem:`, `cor:`, `comp:`, `rem:`, `conj:`
- Cross-reference with `\ref{}` and `\eqref{}`, never hardcoded numbers

---

## 6. CLOSE (5 min)

```bash
make fast 2>&1 | tail -5
echo -n "PH: "; grep -rc '\\ClaimStatusProvedHere' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
cd compute && .venv/bin/python -m pytest tests/ -q 2>&1 | tail -1; cd ..
```

Update ONLY these files:
1. `memory/ground_truth_mar2026.md` — update census if changed
2. `memory/fix_queue.md` — mark completed items
3. `memory/depth_targets.md` — mark completed targets, add notes on obstructions
4. `notes/autonomous_state.md` — session summary (5 lines max)

Do NOT update: CLAUDE.md (sync separately), PROGRAMMES.md, HORIZON.md,
SESSION_PROMPT_v10.md, or any other planning document. State lives in memory/.

---

## 7. MATHEMATICAL INVARIANTS (violating any = stop and recheck)

| # | Fact | Trap |
|---|------|------|
| 1 | Com! = Lie (NOT coLie) | Koszul dual coalgebra = SUB of cofree |
| 2 | H! = Sym^ch(V*) (NOT self-dual) | F! = betagamma (NOT Heisenberg) |
| 3 | FF involution: k <-> -k-2h^v | NOT -k-h^v |
| 4 | Cohomological grading: \|d\| = +1 | Bar uses desuspension s^{-1} |
| 5 | Curved: m1^2(a) = [m0, a] | MINUS sign in commutator |
| 6 | P-inf-chiral != Coisson | Different quantization levels |
| 7 | d_bracket^2 != 0 | Use PBW SS, not matrix rank |
| 8 | sl2: h^v=2, rho=1, dim=3 | Weyl-Kac: k -> -k-4 (not -k-2) |

---

## 8. CONTEXT BUDGET

| Phase | Tool calls | Context % |
|-------|-----------|-----------|
| Orient | 3-5 | 5% |
| Choose | 0 (thinking) | 0% |
| Warmup | 10-20 | 10-15% |
| Gather | 5-10 | 10% |
| Derive | 10-20 | 40-50% |
| Write | 10-15 | 20-25% |
| Close | 3-5 | 5% |

### Compression survival
At tool call 50: write checkpoint to `notes/autonomous_state.md`:
```
Target: [D-number and description]
Progress: [what's derived, what remains]
Insertion point: [file:line]
Next: [what to write]
```

At tool call 100: repeat checkpoint.

### If blocked
If the derivation hits a wall after 30 minutes of extended thinking:
1. Write the OBSTRUCTION precisely (what step fails, what's missing)
2. Add it to `memory/depth_targets.md` under the target's "Risk" section
3. Switch to next-highest-scoring target (this is the ONLY allowed target switch)
4. If second target also blocks: do warmup fixes and close session cleanly

---

## 9. THE MEASURE

A session succeeds if it produces ONE of:
- A new `\ClaimStatusProvedHere` theorem with complete proof and Python verification
- A new computation (`comp:` label) with explicit values matching predictions
- A conjecture upgrade: CJ -> PH with full derivation chain

A session fails if it produces only:
- Audit fixes (these are maintenance, not advancement)
- Planning documents (these are overhead, not output)
- Partial derivations without LaTeX in the manuscript

The book has 695 proved theorems and 1310 pages. It does not need more volume.
It needs DEPTH: one computation that shows the machine works on modules.
One chain map that connects algebra to physics. One spectral interpretation
that explains why the discriminant is universal.

That is what this session is for.
