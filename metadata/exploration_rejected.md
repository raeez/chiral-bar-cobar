# Exploration Engine — Rejected Candidates

Session 96, Mar 5 2026. Full run of EXPLORATION_ENGINE.md (Phases 0-5).

## Rejection Categories

### Exact Duplicates (removed before filtering)

1. **Multiplicative genus from bar-cobar**
   - Source: Domain Agent D1 (Algebraic)
   - Duplicate of: HORIZON B9
   - Statement: Every Koszul chiral algebra determines a multiplicative genus via κ·((x/2)/sin(x/2)−1)
   - Reason: Already recorded as B9 in Session 95

2. **Complementarity sum as root datum invariant**
   - Source: Domain Agent D3 (Geometric-Topological)
   - Duplicate of: HORIZON A8 + B7
   - Statement: κ+κ' depends only on root datum, not level
   - Reason: Already recorded as A8 (sl_N case) and B7 (general formula) in Session 95

### Anti-Pattern Flags (demoted or cautioned, NOT removed)

3. **Conformal block rank complementarity at admissible levels**
   - Source: Domain Agent D2 (Module-Representation)
   - Anti-Pattern #13: "Admissible level k = -h∨+p/q: FF dual k' fails p/q > 0"
   - Action: Restricted statement to GENERIC levels only (admitted as B13 with caution)
   - Note: At admissible levels, the dual level k' = -k-2h∨ = h∨-p/q may itself be admissible with different p'/q'. The module categories at k and k' can be very different (one rational, one not). The complementarity claimed requires k generic.

4. **Ext ↔ Tor exchange (original Level A claim)**
   - Source: Domain Agent D2 (Module-Representation)
   - Issue: Originally claimed as Level A. Demoted to Level B because curved case requires Positselski's framework (non-trivial lift to chiral setting).
   - Action: Admitted as B11 with explicit uncurved/curved distinction

5. **Module tensor product duality (original Level A claim)**
   - Source: Domain Agent D2 (Module-Representation)
   - Issue: Originally claimed as Level A strict monoidal. Demoted to Level B because bar construction is likely only lax monoidal on fusion products.
   - Action: Admitted as B12 with lax/strict caveat

## Anti-Pattern Checklist (applied to all 18 candidates)

| # | Anti-Pattern | Candidates Flagged |
|---|-------------|-------------------|
| 1 | H self-dual | None |
| 2 | Bar-cobar QI ≠ derived equiv | B11 (noted) |
| 3 | Bosonization ≠ Koszul | None |
| 4 | bc has 2 generators | None |
| 5 | Coisson ≠ P∞-chiral | None |
| 6 | Sugawara undefined at critical | None |
| 7 | κ doesn't determine algebra | None |
| 8 | F_g ≠ Z_g | None |
| 9 | FM ≠ X^n\Δ | None |
| 10 | Periodicity not preserved in general | None (already in B2) |
| 11 | P^n ≠ S^{2n} | None |
| 12 | Prime form K^{-1/2} | None |
| 13 | Admissible dual fails | B13 (restricted to generic) |
| 14 | λ_g² = 0 open for g≥3 | C8 (acknowledged as open) |
| 15 | WRT needs quantum groups | None |
| 16 | AGT needs 4d input | None |
