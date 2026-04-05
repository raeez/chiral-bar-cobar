---
description: "Cross-volume AP5 propagation check for a formula or pattern"
---

# Cross-Volume Propagation Check (AP5)

**Pattern**: $ARGUMENTS

After EVERY correction, grep for all variant forms across ALL THREE volumes. This prevents the #1 systematic failure mode: fixing a formula in one file while the same formula appears wrong in 10+ other files.

## Protocol

1. **Grep all three volumes** for the pattern:
```bash
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar/appendices/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar-vol2/chapters/ ~/chiral-bar-cobar-vol2/appendices/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/calabi-yau-quantum-groups/chapters/ ~/calabi-yau-quantum-groups/notes/ 2>/dev/null
```

2. **Also check variant forms** — the same formula may be written differently:
   - LaTeX macros vs expanded form
   - Different variable names
   - Different normalization conventions (AP49: OPE modes in Vol I, λ-brackets in Vol II)

3. **Check compute layer** for hardcoded values:
```bash
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar/compute/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar-vol2/compute/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/calabi-yau-quantum-groups/compute/ 2>/dev/null
```

4. **Check CLAUDE.md and concordance** for stale descriptions:
```bash
grep -n "$ARGUMENTS" ~/chiral-bar-cobar/CLAUDE.md ~/chiral-bar-cobar-vol2/CLAUDE.md ~/calabi-yau-quantum-groups/CLAUDE.md 2>/dev/null
grep -n "$ARGUMENTS" ~/chiral-bar-cobar/chapters/connections/concordance.tex 2>/dev/null
```

5. **Report** all occurrences with file:line, classify as CONSISTENT or DIVERGENT.
6. **Fix** all divergent instances in the same session.
