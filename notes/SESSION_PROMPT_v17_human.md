# Session v17 — Futures Gap Closure (Human-Readable)

## What this session does

The v15 session fixed the proof architecture (circularity, false citations, contradictions). The v16 session propagated notation and status fixes across all 55 files. This session closes the gap between **what the manuscript advertises** and **what it actually proves**.

raeeznotes4.md identified 9 "advertised futures" — things the manuscript promises or implies it will deliver. A systematic gap analysis found 46 specific places where those promises don't match reality. The gaps fall into three categories:

| Tier | Count | What it means | This session |
|------|-------|---------------|--------------|
| T1 | 7 | Text claims more than proofs deliver | Fix all 7 |
| T2 | 8 | Conjecture closable with existing machinery | Attempt top 4 |
| T3 | 31 | Correctly conjectural, needs new math/physics | Verify, don't touch |

## Phase A: Say what you mean (text-only, no new math)

Seven places where the prose overclaims:

| # | What's wrong | Where | Fix |
|---|-------------|-------|-----|
| A1 | Residual "H^1(M_g) controls genus corrections" | intro, concordance | Replace with H^1(Sigma_g) or three-level diagram |
| A2 | Status table says "proved" without qualifiers | concordance §34.9-10 | Add "on Koszul locus" for B_mod, "on evaluation locus" for DK |
| A3 | "Unified periodicity" framed as near-term | deformation, concordance | Reframe as "partial, family-dependent profile" |
| A4 | Theta_A implied to be established | intro, concordance | Add "conjectural" / "programme target" |
| A5 | A_mod claimed without functorial/operadic distinction | concordance | Add one sentence: "functorial (proved); operadic (unstated)" |
| A6 | Index theorem framed as aspirational | intro | Change "we expect" to "we prove" — it IS proved |
| A7 | Proved core conflated with full modular homotopy theory | intro | Add Stratum I/II qualifier |

All seven are grep-read-edit cycles. No mathematics changes. Census stays the same.

## Phase B: Close the closable gaps (real math, prioritized)

Four conjectures where the existing machinery should suffice for a complete proof:

| Priority | Gap | Conjecture | Approach | Impact |
|----------|-----|-----------|----------|--------|
| B1 | WZW modular periodicity | conj:modular-periodicity | WZW characters are theta/eta ratios — same proof as minimal models | Strengthens Future 7 |
| B2 | Sharp geometric period | conj:geometric-periodicity | Mumford relation 12*lambda = kappa_1 + delta | Strengthens Future 7 |
| B3 | AGT scope narrowing | conj:agt-bar-cobar | 2D side already proved; narrow to 4D-2D bridge only | Cleans Future 9 |
| B4 | Higher-genus anomaly | conj:anomaly-physical | May already follow from Theorem D (kappa+kappa'=0 at all genera) | Cleans Future 9 |

**Rule**: Only upgrade with a complete proof. A half-proof is worse than a clean conjecture.

Four more T2 items exist (KS operator, sl_3 discriminant, Yangian cat O) but are either blocked or require substantial new work. Deferred.

## Phase C: Verify the conjectural stays conjectural

31 T3 gaps across Futures 2-9 are correctly identified as open research problems. Quick sweep to confirm:
- Each has a scope remark
- None is accidentally tagged ProvedHere
- The Stratum I/II separation in concordance covers them all

## What stays the same

- All four main theorems (A, B, C, D) — untouched
- All 757 ProvedHere claims — untouched
- Proof architecture from v15 — untouched
- Notation from v16 — untouched
- Bibliography — untouched (unless B1/B2 need a new citation)

## Expected outcomes

| Metric | Before | After (if B1-B4 all succeed) |
|--------|--------|------------------------------|
| PH | 757 | ~760 |
| CJ | 118 | ~114 |
| Overclaims in prose | 7 identified | 0 |
| T3 conjectures with scope remarks | most | all |
