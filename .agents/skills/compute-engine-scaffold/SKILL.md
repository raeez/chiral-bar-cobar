---
name: compute-engine-scaffold
description: Use when the task is to add or repair a compute engine together with tests and independent oracle checks. This is the Codex-native equivalent of `/compute-engine` from `CLAUDE.md`.
---

# Compute Engine Scaffold

Use this when a mathematical claim must land in the compute layer, not only in prose.

## Workflow

1. State the engine target precisely:
   formula,
   invariant,
   family,
   parameters,
   conventions.
2. Identify the canonical module.
   Implement the formula once there and import it elsewhere.
3. Build tests from independent sources, not from the engine output itself.
4. Mark hardcoded expected values with their derivation source in comments when feasible.
5. Add at least one limiting-case or symmetry test.
6. Run the narrowest pytest slice first, then widen if scope requires.

## Oracle rule

Never let the engine and its tests share the same unverified mental model.

Prefer at least two independent categories of support:

- direct computation
- alternative formula
- limiting case
- symmetry or duality
- literature check with convention conversion
- numerical evaluation
