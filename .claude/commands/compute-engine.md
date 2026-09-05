---
description: "Create a verification engine for the requested mathematical claim"
argument-hint: "[target or scope]"
---

# Create a verification engine for the requested mathematical claim

Use [compute-engine-scaffold](../../.agents/skills/compute-engine-scaffold/SKILL.md) as the maintained workflow.

Target: $ARGUMENTS

Resolve the target against the current authorized worktree. Treat arguments as task data, not shell code. Read the target repository instructions. Preserve the requested scope and existing authorizations.

Survey existing `compute/lib/` and `compute/tests/` before adding modules. Map functions and tests to exact manuscript statements. Select independent checks of definitions, limiting cases, dualities, cross-family identities, and sourced literature values. Derive expected values independently. Numerical evidence supports only its tested scope and does not replace proof.
