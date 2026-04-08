---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
   theorem label, status, scope, and wording
2. Check whether the same claim appears elsewhere under the same label or under variant phrasing.
3. Repair drift across:
   theorem statement
   proof surroundings
   status remarks
   concordance text
   metadata
   duplicated theorem clusters
4. Ensure no `ClaimStatusProvedHere` block quietly leans on weaker upstream material.
5. Regenerate or verify metadata when status-bearing files move.
6. End with a status map:
   what changed,
   what remains unstable,
   and what still needs verification

## Rule of thumb

If you changed the truth of a claim surface, you almost certainly changed more than one file.

