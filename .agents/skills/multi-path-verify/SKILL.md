---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

## Use at least three independent paths when feasible

Choose from:

- direct computation from the definition
- an alternative but equivalent formula
- limiting or special cases
- symmetry, duality, or complementarity
- cross-family consistency
- literature comparison with explicit convention checks
- degree, weight, or dimensional analysis
- numerical evaluation at concrete parameter values

## Verification rules

- Paths must be genuinely independent, not cosmetic rewrites of the same computation.
- If the paths diverge, do not average them. Diagnose the discrepancy.
- If the claim survives, report the verified statement with its exact scope.
- If it fails, replace it with the strongest narrower statement that actually survives.

## Repository follow-through

When the verified claim is represented in the compute layer, add or update a targeted test when feasible.

When the verified claim affects manuscript status, sync the theorem surface rather than fixing only one sentence.

