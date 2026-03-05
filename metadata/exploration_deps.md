# Exploration Engine — Dependency Graph

Session 96, Mar 5 2026. Dependencies for all HORIZON items (46 total).

## Notation
- `→` means "is prerequisite for"
- `←` means "depends on"
- Items marked DONE are completed and available as inputs

## Full Graph

```
                    PROVED THEOREMS (manuscript)
                    ============================
    thm:bar-cobar-isomorphism-main ─────────────────────┐
    thm:higher-genus-inversion ─────────────────────────┤
    thm:quantum-complementarity-main ───────────────────┤
    thm:genus-universality ─────────────────────────────┤
    thm:prism-higher-genus ─────────────────────────────┤
    thm:e1-module-koszul-duality ───────────────────────┤
    thm:kodaira-spencer-chiral-complete ────────────────┤
    thm:virasoro-hochschild ────────────────────────────┤
    thm:w-algebra-hochschild ───────────────────────────┤
    thm:connes-exact-sequence ──────────────────────────┤
    cor:ds-bar-level-shift (A10 DONE) ──────────────────┤
    thm:universal-generating-function (A4 DONE) ────────┤
    cor:kappa-additivity (A5 DONE) ─────────────────────┤
    thm:bernoulli-universality (B6 DONE) ───────────────┤
                                                        │
                                                        ▼
                          ┌─────────────────────────────────┐
                          │     LEVEL A (independent)       │
                          └─────────────────────────────────┘

    A2  ← Master Table data (no theorem deps)
    A8  ← thm:central-charge-complementarity ──→ B7
    A9  ← DS computation for general g
    A11 ← thm:km-bar-computation (independent)
    A12 ← A2 (sl₃ subgoal) + Master Table sl₃ data
    A13 ← Master Table H data (independent)
    A14 ← thm:prism-higher-genus + GeK98
    A15 ← thm:connes-exact-sequence + Master Table

                          ┌─────────────────────────────────┐
                          │     LEVEL B (framework + ext)    │
                          └─────────────────────────────────┘

    B1  ← Positselski PDF verification
    B2  ← mixed-type Koszul pair example
    B3  ← Verlinde asymptotic comparison (Witten volume)
    B4  ← tautological ring computation
    B5  ← affine wall-crossing (hardest B item)
    B7  ← A8
    B8  ← A1 DONE
    B9  ← A4 DONE ──→ C5
    B10 ← admissible rep theory (PE: Arakawa)
    B11 ← thm:e1-module-koszul-duality (uncurved: easy; curved: B1)
    B12 ← B11 + fusion product structure
    B13 ← thm:verlinde-bar + analytic continuation of Verlinde
    B14 ← A10 DONE + B11
    B15 ← configuration_spaces.tex log FM
    B16 ← A13 + chirCom/chirLie duality
    B17 ← DNP25 comparison (FRONTIER reference)
    B18 ← prop:zhu-koszul-compatibility

                          ┌─────────────────────────────────┐
                          │     LEVEL C (open problems)      │
                          └─────────────────────────────────┘

    C1  ← independent (GL program)
    C2  ← independent (KL program)
    C3  ← independent (higher-dim)
    C4  ← A4 DONE + B1
    C5  ← B9 + A8
    C6  ← B4 + E₃ page computation
    C7  ← A14 + B11
    C8  ← independent (algebraic geometry)

                          ┌─────────────────────────────────┐
                          │     LEVEL D (speculative)        │
                          └─────────────────────────────────┘

    D1-D5 ← independent programs (multi-year)
```

## Critical Paths (shortest path to high-value targets)

1. **A11 + A13 + A14** → 3 remarks/corollaries, no dependencies, < 3 pages total
2. **A12** ← needs sl₃ bar dims (currently missing deg 4-5 in Master Table)
3. **B16** ← A13 (partition identity) → explicit Lie chiral coalgebra computation
4. **B11** → B12, B14, C7 (3 downstream items depend on module Ext/Tor)
5. **B17** ← DNP25 (must read FRONTIER paper in detail)
6. **C8** ← independent AG computation; if proved, closes conj:obstruction-nilpotent-higher

## Actionable Clusters

**Cluster 1: Immediate write (no research needed)**
A11, A13, A14 — formal observations from existing theorems

**Cluster 2: Computation (existing framework)**
A12, A15, B16 — substitute into proved formulas

**Cluster 3: Module theory (needs B11 first)**
B11 → B12 → B14 → C7

**Cluster 4: Frontier integration (needs external papers)**
B17 (DNP25), B13 (Verlinde analytic continuation)

**Cluster 5: Algebraic geometry (independent)**
C8 (λ_g² = 0), C6 (tautological classes)
