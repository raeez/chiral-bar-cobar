# COMPUTE ENGINE AUDIT & METAMORPHOSIS
# For: Claude Opus 4.6, Code Environment, Extended High Reasoning
# Launch: "Read notes/COMPUTE_ENGINE_AUDIT_PROMPT.md and execute it."

# ======================================================================
# DESIGN RATIONALE
#
# This prompt is engineered for Opus 4.6's cognitive architecture in
# Claude Code with extended thinking. It exploits:
#
#   EXTENDED THINKING: Deep reasoning about mathematical architecture.
#     This prompt gives you large, well-defined problem spaces to think
#     through before acting. Phase 1 is pure understanding. Phase 2 is
#     pure design. Only Phase 3 touches code.
#
#   CODE ENVIRONMENT: Every claim verified by running code. The prompt
#     never asks you to assess code quality by reading alone — it asks
#     you to RUN the code and observe what happens.
#
#   AGENT DEPLOYMENT: Phase 1 uses parallel agents to map the engine
#     without consuming main context. The main context stays clean for
#     the design and build phases.
#
#   COMPOSITIONAL REASONING: The engine has 38 lib files that form a
#     dependency graph. The prompt asks you to understand the graph,
#     find the structural bottlenecks, and redesign from there.
#
# It defends against:
#
#   SYCOPHANCY: The frame is adversarial audit, not review. You are
#     looking for what is WRONG, what is DEAD, what is DUPLICATED.
#     924 passing tests does not mean the engine is good.
#
#   SCOPE CREEP: Four phases, each with concrete deliverables and exit
#     criteria. You do not advance to Phase N+1 until Phase N is done.
#     The deliverable for each phase is a specific artifact.
#
#   FORMULA HALLUCINATION: You are forbidden from writing mathematical
#     formulas without Python verification. This is structural, not
#     aspirational — the prompt forces the verification step.
#
#   RE-TREADING THE WRONG TREE: The bar_differential.py saga is
#     documented below. Do NOT attempt to fix it. Do NOT attempt to
#     compute bar cohomology via direct matrix methods for interacting
#     algebras. This is proved impossible.
#
#   PREMATURE REFACTORING: Phase 1 is understanding. Phase 2 is design
#     ON PAPER (in extended thinking). Only Phase 3 writes code. If you
#     refactor before understanding, you will break the 924 tests.
#
#   ANALYSIS PARALYSIS: Each phase has a time budget and a concrete
#     output. If you are stuck in Phase 1 for more than 40 tool calls,
#     write what you have and move on.
#
# ======================================================================

---

You are a research software engineer and mathematician auditing a
computational engine that supports a 1214-page research monograph on
chiral Koszul duality. The engine has 38 library modules, 27 test files,
55+ scripts, and 924 passing tests. It was built over 120+ sessions.

Your mission: understand the engine's true state, identify every
structural problem, design its ideal form, and execute the highest-impact
transformations. Think of this as a principal engineer doing a deep
technical review of a codebase they've inherited — except you also need
to understand the mathematics it implements.

---

## PHASE 0: ORIENT (5 minutes, literal execution)

```bash
cd /Users/raeez/chiral-bar-cobar/compute

# Test suite health
.venv/bin/python -m pytest tests/ -q 2>&1 | tail -5

# Engine size
echo "=== LIB ===" && wc -l lib/*.py | tail -1
echo "=== TESTS ===" && wc -l tests/*.py | tail -1
echo "=== SCRIPTS ===" && wc -l scripts/*.py | tail -1

# Dependency graph (imports between lib files)
echo "=== INTERNAL IMPORTS ==="
grep -rn "from \." lib/*.py | grep -v __pycache__ | sed 's/:.*//' | sort | uniq -c | sort -rn | head -20

# Dead code signals
echo "=== KNOWN BUGGY ==="
grep -l "WARNING\|BUGGY\|d.*!=.*0\|BROKEN\|DEPRECATED\|WRONG" lib/*.py scripts/*.py
```

Read ONLY:
1. `CLAUDE.md` — "Critical Pitfalls" and "Compute Engine" sections
2. The memory file at `/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/MEMORY.md` — "Compute Engine" and "Bar Differential" sections
3. The memory file at `/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/deep_audit_bar_computation.md`
4. The memory file at `/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/tensor_os_bar.md`

These four reads give you the ground truth about what works, what's broken,
and what's been tried. Do NOT skip them.

---

## PHASE 1: ADVERSARIAL AUDIT (30-40 tool calls)

**Deliverable**: A written diagnosis document (in your response, not a file)
with exactly these sections:

### 1A. THE DEAD AND THE BROKEN

Deploy 2 parallel agents:

**Agent 1 — Dead Code Hunter**:
```
RESEARCH ONLY — NO EDITS.
In /Users/raeez/chiral-bar-cobar/compute/:

1. Identify every lib/ file that is NEVER imported by any test file.
   Method: for each lib/X.py, grep for "from.*X import\|import.*X" in tests/*.py.
   List files with ZERO test imports.

2. Identify every script that is KNOWN BROKEN or produces incorrect results.
   Method: read the first 30 lines of each script (docstrings often say).
   Also check: any script that imports from bar_differential or bar_differential_v2.

3. Identify code duplication: files that implement the same mathematical
   object differently. Specifically check:
   - bar_differential.py vs bar_differential_v2.py vs chiral_bar_differential.py
   - w3_bar.py vs w3_bar_extended.py vs w3_bar_cohomology.py
   - yangian_bar.py vs yangian_bar_compute.py
   - chiral_bar.py vs chiral_ce.py
   - bar_gf_solver.py — what is this?
   For each pair, say: which is canonical? which is dead?

4. List every lib/ file that uses numpy (floating point) vs sympy (exact).
   Flag any lib/ file that does exact mathematics with floating-point arithmetic.

Return as structured lists.
```

**Agent 2 — Architectural Mapper**:
```
RESEARCH ONLY — NO EDITS.
In /Users/raeez/chiral-bar-cobar/compute/:

1. Build the import dependency graph of lib/*.py files.
   For each file, list what it imports from other lib/ files.
   Identify: root modules (imported by many, import few), leaf modules
   (import many, imported by few), and orphans (import/imported by nothing).

2. Identify the CORE ABSTRACTIONS:
   - What classes/types flow between modules? (OPEAlgebra, GradedVectorSpace, etc.)
   - Are there competing abstractions for the same concept?
   - Is there a unified "algebra" type that all specific algebras implement?

3. For each lib/ file, classify its computational status:
   - VERIFIED: produces results that appear in the manuscript's Master Table
     or verified_formulas.jsonl
   - STRUCTURAL: provides infrastructure (types, utilities) used by others
   - EXPLORATORY: computes things not in the manuscript
   - DEAD: broken, superseded, or never used

4. Check __init__.py: what does it export? What SHOULD it export?

Return as structured tables.
```

While agents run, do your own targeted investigation. Run these tests
and observe their structure:

```bash
cd /Users/raeez/chiral-bar-cobar/compute

# What do the "integration" tests actually test?
.venv/bin/python -m pytest tests/test_master_integration.py -v 2>&1 | head -40

# What does the cross-algebra comparison test?
.venv/bin/python -m pytest tests/test_cross_algebra.py -v 2>&1 | head -40

# The bar comparison — what's being compared?
.venv/bin/python -m pytest tests/test_bar_comparison.py -v 2>&1 | head -40

# Are there any tests that SHOULD fail but are marked xfail or skip?
grep -rn "xfail\|skip\|TODO\|FIXME\|BROKEN" tests/*.py | head -20
```

### 1B. THE MATHEMATICAL AUDIT

In your extended thinking, answer these questions:

1. **What can the engine actually compute from first principles?**
   Not "what values does it store in lookup tables" — what can it DERIVE?
   For each of the 11 algebras in the cross_algebra registry, classify:
   - Can it compute bar chain group dimensions? (Yes for all — this is just dim(g)^n)
   - Can it compute bar COHOMOLOGY dimensions? (Only for free fields where d_bracket=0)
   - Can it compute genus expansion coefficients? (Yes, from kappa formulas)
   - Can it verify Koszul duality relations? (Yes, from stored dual pairs)

2. **What is the engine's fundamental computational bottleneck?**
   The engine CANNOT compute bar cohomology for interacting algebras (sl2, sl3,
   Virasoro, W3) from first principles. It stores known values and verifies
   consistency. The "spectral sequence" module computes E2 pages but does not
   actually run a spectral sequence computation. Is this correct? Verify by
   reading spectral_sequence.py.

3. **What would it take to compute H^4(B-bar(sl3))?**
   This is the engine's frontier computation (Programme IX in PROGRAMMES.md).
   The chain group has dimension 8^4 * |OS^3(4)| = 4096 * 6 = 24576. The
   differential D_{4->3} maps into 8^3 * |OS^2(3)| = 512 * 3 = 1536
   dimensional space. Actually: is this right? The OS dimensions need
   verification. Run the OS algebra code to check.

```bash
cd /Users/raeez/chiral-bar-cobar/compute
.venv/bin/python -c "
from lib.os_algebra import os_dimension
for n in range(2, 7):
    for k in range(n):
        print(f'OS^{k}(C_{n}) = {os_dimension(n, k)}')
    print()
"
```

### 1C. THE ENGINEERING AUDIT

Look for these specific anti-patterns:

1. **Hardcoded values masquerading as computations**: Functions that return
   precomputed dictionaries rather than computing from OPE data. How many
   of the "bar cohomology dimension" functions are actually just lookup tables?

2. **Test tautologies**: Tests that assert `f(x) == f(x)` or that test the
   lookup table against itself. How many of the 924 tests verify mathematical
   properties (d^2=0, Jacobi, complementarity) vs how many just test
   "does this function return the expected constant"?

3. **Stranded infrastructure**: Code that builds toward a computation that
   was never completed. The os_algebra.py + chiral_bar_differential.py
   pipeline — does it end in a working computation, or does it dead-end?

4. **Convention inconsistencies**: Some files use numpy (floating point),
   others use sympy (exact). Some use 0-indexed generators, others 1-indexed.
   Some use "k" for level, others use "kappa". Map these inconsistencies.

**EXIT CRITERION**: You have a complete written diagnosis covering 1A, 1B, 1C.
You can articulate: (a) how many of the 38 lib files are dead/broken,
(b) what the engine can truly compute vs what it merely stores, (c) the
top 5 engineering problems, (d) the top 3 mathematical bottlenecks.

---

## PHASE 2: DESIGN (extended thinking, no code)

**Deliverable**: A written architecture document (in your response) with:

### 2A. THE IDEAL ENGINE

In your extended thinking, design the compute engine as it SHOULD exist.
Not what's achievable in one session — the platonic form. Consider:

**Layer 1: Core Algebra** (the type system)
- A unified `ChiralAlgebra` type that encapsulates: generators, OPE table,
  conformal weights, symmetry type (E_inf/E_1/P_inf), level parameter
- A `KoszulPair` type that links an algebra to its dual
- A `BarComplex` type that knows its chain groups, differential (when computable),
  and cohomology (when known, from any source: closed-form, spectral sequence, lookup)

**Layer 2: Computation** (what the engine derives)
- `bar_chain_groups`: dim(g)^n * OS dimensions — always computable
- `ce_cohomology`: Chevalley-Eilenberg — always computable (classical linear algebra)
- `genus_expansion`: from kappa formulas — always computable
- `spectral_sequence`: E1 page from PBW filtration — computable for KM algebras
- `bar_cohomology_free`: direct d^2=0 computation — computable for free fields
- `bar_cohomology_modular`: rank mod p for large matrices — NEW, computable for sl3
- `koszul_hilbert`: quadratic dual Hilbert series — computable from quadratic data

**Layer 3: Verification** (what the engine checks)
- `complementarity`: kappa(A) + kappa(A!) = 0 for KM
- `generating_function`: verify closed-form GF against computed values
- `discriminant`: verify shared discriminant across DS family
- `master_table`: cross-check all manuscript claims

**Layer 4: Frontier** (new capabilities from NEW_MACHINERY.md)
- `bar_admissible`: specialize bar complex to rational level (M2)
- `brst_comparison`: chain map B-bar -> C*_BRST (M6)
- `fusion_chain`: chain-level fusion product (M3)
- `sparse_rank`: large matrix rank over F_p (M9)

### 2B. THE TRIAGE

Classify every existing lib/ file into:
- **KEEP AS-IS**: Working, well-tested, used by manuscript. Do not touch.
- **REFACTOR**: Working but messy. Improve without changing behavior.
- **ABSORB**: Functionality should be merged into another module.
- **ARCHIVE**: Dead, broken, or superseded. Move to compute/archive/.
- **BUILD**: Does not exist yet but should.

### 2C. THE EXECUTION PLAN

Rank the top 10 actions by (IMPACT * FEASIBILITY / RISK):
- IMPACT: How much does this improve the engine's capabilities?
- FEASIBILITY: Can this be done in a single session?
- RISK: Could this break the 924 passing tests?

The top 3 should be executed in Phase 3. The rest go into a backlog.

**EXIT CRITERION**: You have a written architecture document with 2A, 2B, 2C.
The triage covers all 38 lib files. The execution plan has concrete actions.

---

## PHASE 3: BUILD (the rest of the session)

**Deliverable**: Working code changes with all tests passing.

Execute the top 3 actions from your Phase 2C plan. For each action:

1. **Announce**: State what you're doing and why (one sentence).
2. **Test first**: Run the relevant tests BEFORE making changes.
3. **Change**: Make the code change.
4. **Test after**: Run the relevant tests AFTER making changes.
5. **Full suite**: After all 3 actions, run the full test suite.

### RULES FOR PHASE 3

- **Do not break tests.** If a change causes test failures, revert it.
  The 924 passing tests are the engine's immune system. Do not suppress them.

- **Do not delete without archiving.** Dead code goes to compute/archive/,
  not /dev/null. Someone spent hours writing it; the history has value.

- **Do not add tests for broken code.** If bar_differential.py has d^2!=0,
  do not write a test that asserts d^2!=0. That's testing a bug.

- **Every new function gets a test.** If you add a computation, add a test
  that verifies a mathematical property (not just "returns the right constant").

- **Exact arithmetic only.** New computational code uses sympy/Fraction, not
  numpy/float. The engine computes mathematics, not approximations.

- **Use existing infrastructure.** OPEAlgebra, GradedVectorSpace, ChainComplex
  exist for a reason. Don't create parallel abstractions.

### CANDIDATE HIGH-IMPACT ACTIONS (from repository analysis)

These are pre-identified high-value targets. Your Phase 2 analysis may
surface better ones — use your judgment.

**A. Archive dead code** (~15 files):
Move bar_differential.py, bar_differential_v2.py, and all scripts that
import from them to compute/archive/. Move broken/superseded scripts to
compute/archive/scripts/. This reduces cognitive load without losing history.
RISK: Zero (archived files are still on disk). IMPACT: Clarity.

**B. Create compute/lib/__init__.py with proper exports**:
Currently empty. Should export the core types (OPEAlgebra, Generator,
GradedVectorSpace, ChainComplex) and the algebra constructors (heisenberg(),
sl2(), virasoro(), etc.). This makes `from compute.lib import *` actually
useful. RISK: Near-zero. IMPACT: Usability for all future work.

**C. Implement bar_cohomology_modular.py** (M9 from NEW_MACHINERY.md):
The most impactful new capability. Compute dim H^n(B-bar(sl3)) mod p
for small primes p. This requires:
1. Building the bar differential matrix over F_p (using existing OPE data
   from sl3_bar.py and OS algebra from os_algebra.py)
2. Computing matrix rank over F_p (numpy is fine here — it's arithmetic mod p)
3. Extracting cohomology dimensions
This would produce the FIRST NEW MATHEMATICAL RESULT from the engine:
H^4(B-bar(sl3)), which is currently unknown and would either confirm or
refute generating function conjectures.
RISK: Medium (new code, but isolated from existing tests).
IMPACT: Very high (new mathematical discovery).

**D. Unify the algebra registry**:
cross_algebra.py has an 11-algebra registry. bar_complex.py has a "known
bar dims" registry. koszul_pairs.py has a dual pairs registry.
genus_expansion.py has a kappa registry. These should be ONE registry
with ONE source of truth. Create compute/lib/registry.py.
RISK: Low (data unification, not logic change). IMPACT: Eliminates
inconsistency bugs, makes adding new algebras trivial.

**E. Build the "what can we compute" test**:
A single integration test that, for each algebra in the registry, calls
every computation the engine can perform and verifies consistency:
bar_chain_dims match formula, kappa values satisfy complementarity,
genus expansion matches universal formula, Koszul duals are correct, etc.
This is the engine's self-consistency check.
RISK: Zero (new test only). IMPACT: Catches future regressions.

---

## MATHEMATICAL GUARDRAILS

These facts are PROVED. If your code produces results contradicting them,
your code is wrong, not the facts.

| # | Invariant | Value |
|---|-----------|-------|
| 1 | dim B-bar^n(g_k) chain group | (dim g)^n * (n-1)! [after OS quotient] |
| 2 | H^n(B-bar(Heisenberg)) | p(n-2) for n >= 2, 1 for n = 1 |
| 3 | H^n(B-bar(sl2)) | Riordan R(n+3): 1, 3, 6, 15, 36, 91 |
| 4 | H^n(B-bar(Virasoro)) | Motzkin diffs M(n+1)-M(n): 1, 3, 8, 21, 55 |
| 5 | H^n(B-bar(bc)) | 2^n - n + 1 |
| 6 | H^n(B-bar(betagamma)) | A025565: 1, 2, 4, 10, 26, 70, 192 |
| 7 | Shared discriminant | Delta = 1 - 2x - 3x^2 = (1-3x)(1+x) for sl2/Vir/bg |
| 8 | kappa(sl2_k) | 3k/4 |
| 9 | kappa(Vir_c) | c/2 |
| 10 | Complementarity | kappa(A) + kappa(A!) = 0 for all KM |
| 11 | FF involution | k' = -k - 2h^vee |
| 12 | CE cohomology sl2 | (1+t^3) = {0:1, 3:1} |
| 13 | CE cohomology sl3 | (1+t^3)(1+t^5) |
| 14 | Bar differential bracket-only | d^2 != 0 (PROVED, all 2048 signs fail) |
| 15 | Full bar differential | d^2 = 0 (via Borcherds, not constructible as matrix) |
| 16 | OS^{n-1}(C_n) dimension | (n-1)! |

If you compute something that contradicts rows 1-13 or 16, stop and find your bug.
Row 14 is NOT a bug — it is a theorem. Do not try to fix it.
Row 15 means the full chiral bar differential satisfies d^2=0 but cannot be
built as an explicit matrix using only Lie bracket data.

---

## THE WRONG TREE (do NOT repeat this)

Over sessions 105-120, multiple attempts were made to compute bar cohomology
by building the bar differential as an explicit matrix. ALL FAILED:

- bar_differential.py: bracket-only d, tested all 2048 sign conventions, d^2!=0
- bar_differential_v2.py: different basis choice, same result
- chiral_bar_differential.py: includes OS algebra, same fundamental problem
- ~15 scripts in scripts/sl3_*, scripts/find_sign_convention.py, etc.

**Root cause**: The bracket-only differential (simple pole residue) does NOT
square to zero. This is PROVED (Pole Decomposition Theorem). The full chiral
bar differential includes curvature terms (double pole residue) that compensate.
But the curvature term maps to the VACUUM, which is quotiented out in the
reduced bar complex. So d^2=0 holds on the nose only for the FULL (unreduced)
bar complex or via the Borcherds identity argument (which is non-constructive
at the matrix level for interacting algebras).

**The correct computational approach** for interacting algebras is:
1. PBW spectral sequence (filter by conformal weight)
2. E1 page = CE cohomology with polynomial coefficients
3. At generic level, E1 = E2 collapse by Koszulness (PROVED)
4. Bar cohomology = Hilbert series of Koszul dual

This is implemented partially in spectral_sequence.py. Completing it is a
medium-term project (see NEW_MACHINERY.md M1, M9).

---

## CLOSE

After Phase 3, run:
```bash
cd /Users/raeez/chiral-bar-cobar/compute
.venv/bin/python -m pytest tests/ -q 2>&1 | tail -5
```

Then write a summary:
1. **Phase 1 findings**: How many dead files? What can the engine truly compute?
2. **Phase 2 design**: What is the ideal architecture? What are the top 10 actions?
3. **Phase 3 results**: What was built? Test count delta? Any new mathematical results?
4. **Backlog**: What should the next session tackle?

Update the memory file at `/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/MEMORY.md`
with any new findings about the compute engine's true state.

---

## THE MEASURE

The compute engine exists to serve one purpose: make the monograph's claims
VISIBLY TRUE to a skeptical referee. A referee reading "H^n(B-bar(sl2)) =
Riordan R(n+3)" wants to see either a proof or a computation. The engine
provides the computation.

But the engine's frontier — the computations it CANNOT yet do — is exactly
where the manuscript's most interesting claims live. H^4(B-bar(sl3)) is
unknown. The W3 generating function is conjectured from 4 data points.
The Yangian bar cohomology is conjectured. These are the computations
that would move the monograph from "framework" to "machine."

Your audit and design should be guided by this: what changes to the engine
would produce the most new mathematical knowledge? Not the cleanest code,
not the best abstractions, not the prettiest tests — the most new math.
Clean code is a means to that end, not an end in itself.
