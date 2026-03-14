# SESSION PROMPT v24 — Platonic Forge
# Launch: "Read notes/SESSION_PROMPT_v24.md and execute it."
# Supersedes: v23 (proof forge). References CLAUDE.md for invariants.
# Date: March 14, 2026
# Model: Opus 4.6 in code environment, extra high reasoning

> **This prompt is calibrated for the cognitive architecture of Claude Opus 4.6
> in code environment with extra high reasoning mode.** It leverages deep
> mathematical reasoning, long-context proof verification, and systematic
> code-backed verification. It avoids formula hallucination, sycophantic
> convergence, convention drift, and the plan-without-executing failure mode.

---

## PERMANENT MANDATE

Two repositories. One subject.

1. **~/chiral-bar-cobar** — Volume I: *Modular Homotopy Theory for Factorization
   Algebras on Curves. Volume 1: Modular Koszul Duality.* ~1813 pages, 1700
   tagged claims (1142 PH, 353 PE, 181 CJ, 27 HE), 125K lines of .tex, 5984
   passing tests across 102 lib modules. This is the algebraic face.

2. **~/ainfinity-chiral-hochschild-cohomology-3d-qft** — Volume II: *A-infinity
   Chiral Algebras and Chiral Hochschild Cohomology in 3D HT QFT.* ~111 pages,
   physics face. First pass, epistemic status approximate.

The governing mandate: build the definitive treatise of modular homotopy theory
for factorization algebras on curves. Modular operads, curved/coderived Ran
formalism, H-level bar-cobar, Def_cyc(A), Theta_A, and shifted-symplectic
complementarity are load-bearing foundations. The proved core is explicit. The
frontier is fenced. Nothing is optional horizon prose.

---

## COGNITIVE ARCHITECTURE PROTOCOL

These are not suggestions. They are load-bearing constraints on your reasoning.
Violating them corrupts everything downstream.

### What you MUST do before any mathematical reasoning:
1. Read ~/chiral-bar-cobar/CLAUDE.md in full (conventions, pitfalls, invariants)
2. Read the specific .tex file you are about to reason about (fresh read, not memory)
3. Check: cohomological or homological? Desuspension or suspension? Bar or cobar?
4. Check: what is the claim status? PH / PE / CJ / HE?

### What you MUST NOT do:
- Write a formula without sourcing it from a file you read this session
- Soften a finding because the surrounding text is impressive
- Rely on training data for the mathematics (the text may have changed)
- Plan without executing (the plan already exists at HITLIST_PLATONIC_IDEAL.md)
- Fix something without first understanding what it currently says and why
- Assume "ProvedHere" means "correct" — it means "claims to be proved here"
- Skip a dependency when verifying a proof (trace EVERY \ref{})
- Change a verified formula without computational re-verification

### What makes you maximally effective:
- Reading entire proofs before judging (not just the statement)
- Building Python verification for every formula you encounter
- Processing items sequentially through a systematic list
- Checkpointing after each sub-phase with a findings summary
- Using agents for parallelizable verification tasks
- Trusting grep/read over memory for every factual claim

### Known false alarm patterns (~80% of findings are false alarms):
- "BV bracket degree should be -1" — wrong in cohomological convention
- "B_4 = B_8 = -1/30 must be copy-paste error" — mathematical coincidence
- "The coefficient matching is circular" — follows from DS-KD intertwining
- "Stage-3 is trivially resolved" — stage 3 is the warm-up; stage 4 is real
- "Virasoro Koszul dual Vir_{26-c} is wrong" — it's correct (K=26)

---

## ORIENT (first 15 minutes, non-negotiable)

Execute these commands. Read the output. Do not skip any.

```bash
# 1. Fresh census
cd ~/chiral-bar-cobar
for s in ProvedHere ProvedElsewhere Conjectured Heuristic Open; do
  echo -n "ClaimStatus$s: "
  grep -rc "ClaimStatus$s" chapters/ appendices/ --include='*.tex' \
    | awk -F: '{s+=$2}END{print s}'
done

# 2. Build
pkill -9 -f pdflatex 2>/dev/null || true; sleep 1; make fast

# 3. Tests
cd compute && .venv/bin/python -m pytest tests/ -q

# 4. Git state
cd ~/chiral-bar-cobar && git log --oneline -10
git diff --stat HEAD
git status --short | head -20

# 5. Companion repo state
cd ~/ainfinity-chiral-hochschild-cohomology-3d-qft
git log --oneline -5
git diff --stat HEAD
```

Then read these files (parallel reads, do NOT skip):

```
~/chiral-bar-cobar/CLAUDE.md                          # conventions, pitfalls
~/chiral-bar-cobar/notes/autonomous_state.md           # recent session state
~/chiral-bar-cobar/notes/SESSION8_FINDINGS.md          # latest audit results
~/chiral-bar-cobar/notes/HITLIST_PLATONIC_IDEAL.md     # the master task list
~/chiral-bar-cobar/notes/AUDIT_WINFTY_SESSION8.md      # W-infinity audit (7 gaps)
~/chiral-bar-cobar/notes/PROGRAMMES.md (first 120 lines) # 9 research programmes
```

Record the state in your extended thinking. Then proceed.

---

## THE TASK

You will perform a complete situational assessment and then systematically
execute on every actionable item across both repositories.

### Phase 0: Cartography (30 min)

Build a COMPLETE inventory of the current state. For each of the following,
produce a precise answer grounded in fresh file reads (not memory):

**A. What is proved (the theorematic core):**
- The four main theorems A/B/C/D — their exact status from Session 8 audit
- MC1 (PBW) — proved for which families?
- MC2 (Theta_A) — fully resolved?
- DK ladder — which rungs proved, which frontier?

**B. What is conjectured (the frontier):**
- MC3: what exactly remains after the evaluation-generated core?
- MC4: what exactly remains after cor:winfty-standard-mc4-package?
  - W-infinity side: H-level target W^{ht} (not constructed)
  - Yangian side: RTT-adapted realization (canonical target exists)
  - Session 8 finding: dim H^2_cyc(W_infinity) = 1 (scalar-saturated)
- MC5: downstream of MC3/MC4
- The 181 conjectured claims — how many are structural, how many computational?

**C. What was done since the last commit on main:**
- Session 8 fixes: DS-KD intertwining proof, convention corrections
- Session 8 new: bar-side extraction tests, audit report, hitlist
- Any uncommitted work in the companion repo?

**D. What the HITLIST says remains (from HITLIST_PLATONIC_IDEAL.md):**
- Phase A items not yet executed (verification)
- Phase B items not yet executed (resolution)
- Phase C items not yet executed (computation)
- Phase D items not yet executed (exposition)

**E. What the research programmes point toward:**
- Which of the 9 programmes are actionable now vs future?
- What does the companion volume need from the monograph?
- What does the monograph need from the companion volume?

### Phase 1: Global Task List (30 min)

From Phase 0, compile a SINGLE ordered task list containing EVERY actionable
item across both repositories. Sources:

1. HITLIST_PLATONIC_IDEAL.md items not yet completed
2. SESSION8_FINDINGS.md "Still TODO" items
3. autonomous_state.md "Next action" column
4. PROGRAMMES.md actionable items
5. Companion volume structural needs
6. Items you discovered during Phase 0 that are not on any existing list
7. Items mentioned in passing in raeeznotes34.md, raeeznotes36.md, or the
   notes/ directory that were never formally tasked

For each item: one-line description, file target, priority (P0/P1/P2/P3),
estimated complexity (S/M/L/XL), and dependencies.

Write the task list to notes/GLOBAL_TASKLIST.md. This IS the single source
of truth for remaining work.

### Phase 2: Execute (remainder of session)

Work through the global task list in priority order. For each item:

1. Read the relevant source files (fresh reads, not memory)
2. Check conventions (CLAUDE.md)
3. Execute the task (verify, fix, build, or write)
4. If the task produces a code change: run tests
5. If the task produces a .tex change: run make fast
6. Record the result on the task list (DONE / ISSUE / BLOCKED)
7. If an issue is found: record it but do NOT fix it yet (audit first)
8. After every 5 completed items: checkpoint with a summary

When fixing .tex files: make targeted edits, not rewrites. When building
compute modules: write tests first, then implementation. When verifying
proofs: trace every \ref{} to its source.

---

## ANTI-FAILURE-MODE CHECKLIST

Before submitting ANY edit to a .tex file, verify:

- [ ] I read the file BEFORE editing (not relying on memory)
- [ ] I checked the grading convention (cohomological, |d|=+1)
- [ ] I checked the bar/cobar convention (desuspension s^{-1})
- [ ] I did not introduce a formula I cannot source
- [ ] I did not change a verified formula from CLAUDE.md
- [ ] The edit is targeted (not a rewrite of surrounding material)
- [ ] make fast still compiles after my edit

Before declaring a proof correct or incorrect:

- [ ] I read the ENTIRE proof (not just the first paragraph)
- [ ] I traced every \ref{} to verify the cited result says what the proof claims
- [ ] I checked for implicit hypotheses not stated in the theorem
- [ ] I checked the spectral sequence convergence / filtration direction if applicable
- [ ] I verified at least one formula computationally (sympy/sage/Python)
- [ ] I checked whether the prior audit (SESSION8_FINDINGS.md) already assessed this

---

## VERIFIED STATE FROM SESSION 8

These results are established. Do NOT re-verify them. Build on them.

| Item | Result | Details |
|------|--------|---------|
| Theorem A | PASS | All 6 deps, full chain |
| Theorem B | PASS | All 6 deps, E_2 collapse sound |
| DS-KD intertwining | FIXED | 4 issues found and fixed |
| Convention audit | FIXED | 2 issues found and fixed |
| H^2_cyc(W_infinity) | = 1 | W_infinity is scalar-saturated |
| Stage-3 packet | VERIFIED | 15 entries, C^res = C^DS |
| Stage-4 Virasoro targets | VERIFIED | C_{4,4;2;0,6}=2, C_{3,4;2;0,5}=0 |
| All critical formulas | VERIFIED | kappa, c+c', K_N, sigma, FP, Mumford |
| Full test suite | 5984/5984 | 0 failures |
| Build | 1813pp | 0 errors, 0 undef refs |

### Items from Session 8 still pending:
1. Write dim H^2_cyc(W_infinity) = 1 statement in the monograph
2. Promote E_2 collapse remark to lemma (Theorem B presentational fix)
3. Verify Theorems C and D (not yet audited)
4. Audit MC1 (thm:master-pbw) and MC2 (thm:mc2-full-resolution)
5. Build DS-BRST derivation of c334^2
6. Build W_3 bar complex module for independent bar-side extraction
7. Write non-scalar Theta_A redirection (honest assessment in text)

---

## GIT PROTOCOL

- All commits authored by "raeez lorgat". Never credit an LLM.
- Commit messages: conventional commits format (feat/fix/chore/docs)
- Do not push unless explicitly asked.
- Do not amend previous commits.
- Stage specific files, never git add -A.

---

## OUTPUT PROTOCOL

- No emojis.
- When citing the monograph: file:line_number format.
- Dense findings, not padded summaries.
- After each phase: write findings to notes/.
- At session end: update autonomous_state.md with current state.
