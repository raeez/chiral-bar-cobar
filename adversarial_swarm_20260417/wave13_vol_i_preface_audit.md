# Wave 13 — Vol I preface.tex + main.tex residual-drift audit (2026-04-17)

## Scope
Audit of `chapters/frame/preface.tex` (5136 lines) and `main.tex` (2234 lines) for drift surviving Waves 1-13 heals.

## Findings

### CLEAN (already healed in prior waves)

1. **Theorem D scope discipline** (preface §Theorem~D, lines 1630-1652): genus-1 unconditional every family; g∈{1,2} on-the-nose; g≥3 socle-only via Graber-Vakil; on-the-nose lift conditional on Faber's λ_g-conjecture. Matches Wave-1 heal. The word "AP225 resolved" does NOT appear (correctly absent).
2. **Theorem A modular-family CONDITIONAL** (lines 1558-1565): explicitly conditional on Francis-Gaitsgory six-functor base-change (GR17 Ch. III §10) + Mok25 log factorization-gluing. Not overclaimed as "PROVED". Matches Wave-3 heal.
3. **"quadrichotomy"** used throughout (lines 110, 175, 1737); **no "quaternitomy"** occurrences in either file. AP235 clean.
4. **No "genuinely disjoint" overclaim** for PTVV alternatives in preface.
5. **No "strict chain-level class L topologization"** / no "FF replaces JKL26 unconditional".
6. **No Drinfeld-double-verified-Heis claim**; candidate Drinfeld double stated as structural target (line 778).
7. **Fingerprint φ(A) uses p_max, r_max** correctly defined (max OPE-pole order, shadow-tower depth). No "κ-isospectral via p_max" overclaim appears (not in scope of these two files).
8. **No Monster fingerprint instantiation** `(2,2,χ,196884,coset)` in preface/main — only the generic 5-slot schema.
9. **UNIFORM-WEIGHT tag** carried on all standalone Theorem-D statements (lines 148, 805, 1382, 1440, 1636, 3370, 3487, 3750, 4910). AP32 clean for full statements.
10. **Theorem C** stated without T1..T9 decomposition labels; no downgraded-inscription leakage.
11. **AP234 κ+κ^!=ϱ·K** correctly scoped on line 86 (`ϱ_A family-specific`) and values enumerated per family 1620-1627.

### HEAL APPLIED

**Drift #1 (AP32 synopsis gap):** preface.tex line 89 stated `$\mathrm{obs}_g=\kappa\lambda_g$ (Theorem~D)` in the seven-theorem synopsis without scope tag. HEALED by appending `\textup{(UNIFORM-WEIGHT)}`. The fuller theorem statement (lines 1630-1652) already carried the tag; synopsis now matches.

## Verdict
Preface and main.tex abstract are post-Wave-13 platonic-clean on the eleven drift-pattern triggers enumerated in the audit brief. One minor AP32 synopsis-tag gap healed surgically (line 89). No further edits required.

## Files touched
- `chapters/frame/preface.tex` line 89 (AP32 tag insertion).

## Cross-volume propagation (AP5)
No formula-change performed; tag-only insertion on Vol-I-local synopsis. No propagation required.

## Build/commit
No commit performed (budget discipline + user did not request commit).
