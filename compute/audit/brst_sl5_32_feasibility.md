# BRST sl_5 (3,2) Feasibility Report

## Summary

The partition (3,2) of 5 is the first non-hook partition in type A and the
minimal test case for conj:ds-kd-arbitrary-nilpotent with non-abelian
nilradical.  The BRST spectral sequence computation is **FEASIBLE in sympy**,
decomposed by ghost number, through conformal weight 3 (sufficient to see
all 8 strong generators of the W-algebra).

## Orbit and Nilpotent Data

- **Partition**: (3,2) of 5.  **Transpose**: (2,2,1).
- **Weighted Dynkin diagram**: (0, 1, 1, 0).
- **Orbit dimension**: 16.  **Centralizer dimension**: dim(g^f) = 8.
- **Orbit class**: two_row_nonhook (the existing engine confirms this).
- **Is hook**: NO.  Hook-type transport (Fehily, CLNS) does NOT apply.

## Dynkin Grading on sl_5

The grading g = g_{-2} + g_{-1} + g_0 + g_1 + g_2 has:

| Grade | Dimension | Roots |
|-------|-----------|-------|
| -2    | 4         | e_{3,1}, e_{4,1}, e_{4,2}, e_{5,2} (negative of grade +2) |
| -1    | 4         | e_{3,1} etc. (negative of grade +1) |
|  0    | 4         | Cartan + e_{1,2}, e_{2,1}, e_{4,5}, e_{5,4} |
| +1    | 4         | e_{1,3}, e_{2,3}, e_{3,4}, e_{3,5} |
| +2    | 4         | e_{1,4}, e_{1,5}, e_{2,4}, e_{2,5} |

Total: dim(sl_5) = 24 = 4 + 4 + 4 + 4 + 4 + 4 (Cartan) = 24. Checks out
(4 + 4 + 8 + 4 + 4 = 24 with g_0 being 8-dim including Cartan; the table
above counts root spaces only, so g_0 has 4 root spaces + 4 Cartan = 8).

Corrected: g_0 = 8-dimensional (4 Cartan elements + 4 root spaces).
The full count: 4 + 4 + 8 + 4 + 4 = 24.

## n_+ Structure

- **dim(n_+) = 8**: 4 roots at grade 1, 4 roots at grade 2.
- **n_+ is NON-ABELIAN**.  The 4 nonzero commutators are:

```
[e_{1,3}, e_{3,4}] = e_{1,4}     (grade 1 + grade 1 = grade 2)
[e_{1,3}, e_{3,5}] = e_{1,5}
[e_{2,3}, e_{3,4}] = e_{2,4}
[e_{2,3}, e_{3,5}] = e_{2,5}
```

- **n_+ is 2-step nilpotent**: [n_+^1, n_+^1] = n_+^2, [n_+, n_+^2] = 0.
- This is the simplest possible non-abelian case: the BRST charge Q_gh
  is at most CUBIC in ghosts (one b, two c operators), with no higher
  ghost-number corrections.

## W-algebra Generators for W^k(sl_5, f_{(3,2)})

From the ad(h/2)-grading on g^f (8-dimensional centralizer):

| Conformal weight h | Parity   | Count | Description |
|--------------------|----------|-------|-------------|
| 1                  | bosonic  | 1     | Current J (from Cartan of g^f) |
| 3/2                | fermionic| 2     | From grade -1 of g^f |
| 2                  | bosonic  | 2     | Includes stress tensor T |
| 5/2                | fermionic| 2     | From grade -3 of g^f |
| 3                  | bosonic  | 1     | Highest-weight generator |

**Total: 4 bosonic + 4 fermionic = 8 strong generators.**

Central charge: c(3,2; k) = 2 - 108/(k+5) = 2(k - 49)/(k + 5).

## Ghost System

The BRST complex uses 8 bc ghost pairs:

| Grade | Pairs | b weight | c weight | b zero-mode? | c zero-mode? |
|-------|-------|----------|----------|--------------|--------------|
| 1     | 4     | 0        | 1        | YES (b_0)    | YES (c_0)    |
| 2     | 4     | -1       | 2        | NO           | YES (c_0, c_1) |

Ghost number ranges from -8 to +8 (17 sectors).

## BRST Charge Decomposition

Q_DS = Q_st + Q_gh where:

- **Q_st** (standard Koszul part): contracts n_+ generators against
  antighosts.  Present for all nilpotents.  Filtration degree 0.
- **Q_gh** (ghost-ghost part): 4 terms encoding [n_+^1, n_+^1] = n_+^2.
  Each term has the form f^{ij}_{pq,rs} c_pq c_rs b_ij (two grade-1
  ghosts times one grade-2 antighost).  Filtration degree
  1 + 1 - 2 = 0.

Both Q_st and Q_gh have Kazhdan filtration degree 0, so the leading
differential d_0 = Q_st + Q_gh is the FULL BRST differential on the
associated graded.

## Kazhdan Filtration

- **Number of layers**: 3 (grades 0, 1, 2).  Max grade = 2.
- **Key structural point**: since Q_st and Q_gh both have filtration
  degree 0, the spectral sequence question is whether H*(d_0) on
  gr_K(V_k(sl_5)) already gives the W-algebra at each conformal weight.
- For **abelian** n_+: Q_gh = 0, d_0 = Q_st is the Koszul differential,
  E_1 degeneration is automatic.
- For **non-abelian** n_+ (our case): d_0 = Q_st + Q_gh is a modified
  Koszul differential.  Whether its cohomology gives the W-algebra
  is the central question.

## Matrix Size Estimates

At each conformal weight Delta and ghost number p, the BRST differential
is a finite-dimensional matrix.  Conservative estimates at ghost number 0
(where the W-algebra lives):

| Weight Delta | dim (ghost# 0) | Feasibility |
|--------------|----------------|-------------|
| 0            | ~1             | trivial     |
| 1            | ~30-50         | trivial     |
| 2            | ~200-400       | easy        |
| 3            | ~1000-3000     | feasible    |

These are **sparse** matrices: Q_gh contributes only 4 terms.

**Verdict**: all matrices at ghost# 0 through weight 3 are well under
5000 x 5000.  This is NOT a monolithic >1000 x 1000 computation.  The
ghost-number decomposition (17 sectors) is the key simplification: the
total Fock space at weight 3 is ~50,000-dimensional, but each ghost-number
sector is ~3000 or less.

## Feasibility Assessment

**Is this a < 100 x 100 computation?**
At weights 0-1: YES.  Trivially feasible.

**Is this a > 1000 x 1000 computation?**
At weight 3 (needed to see the h=3 generator): the ghost# 0 sector
is ~1000-3000 dimensional.  This is at the boundary, but feasible
in sympy with rational arithmetic (sparse matrices, few hours).
Using numpy/scipy.sparse with floating-point would be instant.

**Overall verdict: FEASIBLE in sympy through weight 3.**
The computation decomposes into 17 independent ghost-number sectors,
each tractable.  Weight 0-2 is easy (< 400 x 400).  Weight 3 is the
hardest but still within sympy capacity for sparse rational matrices.

## Compute Engine Architecture

### Module: `compute/lib/brst_sl5_32_engine.py`

```
Phase 1: Fock space construction
  - Build sl_5 PBW basis at each weight Delta = 0..3
  - Build ghost Fock space basis at each (Delta, ghost#)
  - Tensor product: BRST complex at each (Delta, ghost#)

Phase 2: BRST differential
  - Implement Q_st: Koszul contraction (n_+ action on V_k tensored with ghosts)
  - Implement Q_gh: 4 structure-constant terms (c c b cubic ghost terms)
  - Assemble Q = Q_st + Q_gh as sparse matrix at each (Delta, p)

Phase 3: Cohomology
  - Compute ker(Q)/im(Q) at each (Delta, p) for generic k (symbolic)
  - Compare dim H^0(Q) at weights 0..3 against W-algebra character prediction:
      Weight 0: 1 (vacuum)
      Weight 1: 1 (J)
      Weight 3/2: 2 (fermions, in ghost# shifted sector)
      Weight 2: 3 (T + 2 bosonic generators)
      Weight 5/2: 2 (fermions)
      Weight 3: 2 (highest bosonic generator + descendant)

Phase 4: Spectral sequence check
  - If H*(Q) matches W-algebra character at all weights 0..3:
    STRONG EVIDENCE for E_1 degeneration (supports the conjecture)
  - If mismatch at any weight:
    E_1 degeneration FAILS (conjecture needs restriction or reformulation)
```

### Estimated Implementation Effort

- Phase 1: ~200 lines (PBW basis generation is standard; ghost Fock is
  exterior algebra with mode grading).
- Phase 2: ~150 lines (Q_st is a standard Chevalley-Eilenberg differential;
  Q_gh is 4 explicit terms).
- Phase 3: ~100 lines (kernel/image computation via sympy Matrix.nullspace).
- Phase 4: ~50 lines (character comparison).
- Tests: ~100 lines (verify against known abelian case (3,1,1) first,
  then run (3,2)).

**Total: ~600 lines of code, ~100 lines of tests.**

### Dependencies

- sympy (rational arithmetic, Matrix.nullspace)
- Existing engines: nonprincipal_ds_orbits.py, hook_type_w_duality.py
  (for orbit data and W-algebra generator predictions)
- Optional: scipy.sparse for weight-3 speedup

### Risk Factors

1. **Weight 3 may be slow** in pure sympy with symbolic k.  Mitigation:
   evaluate at 3-5 generic numerical values of k first, then confirm
   symbolically if the pattern is clear.
2. **Ghost-number conventions** must be consistent with the manuscript's
   BRST grading.  The existing sl_3 subregular engine (sl3_subregular_bar.py)
   provides a template.
3. **The computation does NOT by itself prove E_1 degeneration at all weights.**
   It verifies at weights 0-3 (where all generators appear).  A proof
   would require structural arguments (e.g., that the Kazhdan filtration
   spectral sequence is formal for 2-step nilpotent n_+).

## Comparison with Other Cases

| Nilpotent    | N  | dim(n_+) | Abelian? | BRST order | Status |
|--------------|----|----------|----------|------------|--------|
| Principal    | any| N(N-1)/2 | YES      | N-1        | PROVED |
| Subregular sl_3 | 3 | 2     | YES      | 1          | PROVED |
| Minimal sl_3 | 3 | 1        | YES      | 1          | PROVED |
| Hook (r,1^s) | any| rs      | YES      | 1          | PROVED |
| **(3,2) sl_5** | **5** | **8** | **NO** | **2** | **OPEN (this report)** |
| (2,2,1) sl_5 | 5  | 6        | YES      | 1          | Should follow from abelian case |

The (3,2) partition is genuinely the FIRST non-abelian test case in the
type-A corridor.  Its resolution (positive or negative) determines the
scope of conj:ds-kd-arbitrary-nilpotent.
