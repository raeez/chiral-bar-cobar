---
description: "Deep Beilinson audit — adversarial falsification of a target"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Deep Beilinson Audit

**Target**: $ARGUMENTS

"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." — Beilinson

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

Every claim is false until independently verified. This audit deploys the Six Hostile Examiners.

## PROTOCOL

### Step 1: Scope

Determine audit scope from $ARGUMENTS:
- **A file path** → audit that file page by page
- **"vol1"/"vol2"/"vol3"** → launch parallel audit agents per chapter
- **A theorem label** → audit the theorem + all its dependencies in the DAG
- **"compute"** → audit compute layer for AP10 violations
- **"cross-volume"** → audit formula consistency across all three volumes

### Step 2: Deploy the Six Hostile Examiners

For each page/chunk of the target:

- **Beilinson** (falsification-first): Is every "proved" claim actually proved? Circular dependencies? Honest scope?
- **Witten** (mathematical physics): Does the math reproduce known physics? Are physical claims rigorous or heuristic?
- **Costello** (factorization algebras): Is the categorical framework correct? Ran space constructions well-defined?
- **Gaiotto** (vertex algebras/W-algebras): Are kappa formulas correct? Koszul duals correctly identified? Shadow computations match VOA literature?
- **Drinfeld** (Yangians/quantum groups): Yangian structures correctly defined? DK bridge correctly stated?
- **Kontsevich** (operads/formality): Operadic framework correct? Formality claims properly proved? Terminology precise?

### Step 3: For Each Claim

1. **Recompute** every formula from first principles (AP1, AP3)
2. **Check proof logic** — hypotheses match? (AP4, AP7)
3. **Verify conventions** against signs_and_shifts.tex
4. **Check scope** against ALL edge cases (AP7, AP18)
5. **Cross-check** against compute/tests/ and compute/lib/
6. **Cross-check** against published literature
7. **Propagation check** (AP5) — grep all three volumes for variants

### Step 4: Classify Findings

For each finding:
- **Severity**: CRITICAL / SERIOUS / MODERATE / MINOR
- **Class**: A (logical/circular) / B (formula) / C (structural) / D (status) / E (editorial)
- **Exact location**: file:line
- **Exact claim**: what is stated
- **Exact issue**: what is wrong
- **Proposed fix**: the correction (independently verified)

### Step 5: Fix and Propagate

1. Apply fixes in dependency order
2. After EVERY fix, grep ALL THREE volumes for variants (AP5)
3. Build after every 3 fixes
4. Run tests after all fixes: `make test`

### Step 6: Report

- Total claims audited
- Findings by severity and class
- Fixes applied
- RECTIFICATION-FLAGs remaining
- Build status
- Test status

### Parallel Audit (for volume-level targets)

Launch RED/BLUE/GREEN agents in parallel:

```
Agent(description="RED audit", run_in_background=true,
  prompt="DEEP FALSIFICATION AUDIT: recompute every formula, check every proof...")

Agent(description="BLUE audit", run_in_background=true,
  prompt="CONSISTENCY AUDIT: cross-reference integrity, status tags, AP5...")

Agent(description="GREEN audit", run_in_background=true,
  prompt="COMPLETENESS AUDIT: missing proofs, dangling references, gaps...")
```

Merge findings, deduplicate, fix, re-audit until CONVERGED.
