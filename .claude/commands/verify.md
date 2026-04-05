---
description: "Multi-path verification of a formula or computational claim"
---

# Multi-Path Formula Verification

**Claim**: $ARGUMENTS

The Multi-Path Verification Mandate requires AT LEAST THREE independent verification paths for every numerical formula. These paths must be genuinely independent.

## Verification Path Taxonomy

Execute at least 3 of the following 8 methods:

### 1. Direct computation
Compute from the defining formula. Show all steps.

### 2. Alternative formula
Compute from an equivalent but structurally different expression.

### 3. Limiting case
Verify against known special cases: k=0, c=0, N=1, genus=0, etc.

### 4. Symmetry/duality
Verify via complementarity, level-rank duality, DS reduction, Feigin-Frenkel involution.

### 5. Cross-family consistency
Verify additivity, multiplicativity, or functoriality across families.

### 6. Literature comparison
Verify against published values with EXPLICIT source and convention check (AP38).

### 7. Dimensional/degree analysis
Verify correct weight, degree, conformal dimension, and units.

### 8. Numerical evaluation
Evaluate at specific parameter values and compare across methods.

## Protocol

1. **State the claim precisely** — what formula, in what convention, for what family
2. **Execute 3+ independent paths** — show work for each
3. **Compare results** — do all paths converge?
4. **If convergent**: report the verified value with confidence
5. **If divergent**: investigate the discrepancy. One path has an error. Find it.
6. **Write a test** in compute/tests/ encoding the multi-path verification
7. **Check AP38**: if comparing against literature, record source + convention
8. **Check AP49**: if cross-volume, verify convention compatibility

## Example

**Claim**: κ(Vir_c) = c/2

- **Path 1** (direct): From the Virasoro OPE T(z)T(w) ~ c/2/(z-w)^4 + ..., the bar propagator absorbs one pole (AP19): r(z) = (c/2)/z^3 + 2T/z. The leading coefficient is c/2.
- **Path 2** (limiting): At c=0 (trivial Virasoro): κ = 0. At c=26 (critical): κ = 13. These satisfy κ = c/2. ✓
- **Path 3** (complementarity): Vir_c^! = Vir_{26-c}. κ(Vir_c) + κ(Vir_{26-c}) = c/2 + (26-c)/2 = 13 (AP24). ✓
- **Path 4** (compute): `compute/tests/test_kappa_engine.py::test_kappa_virasoro` passes with κ = c/2.

**Result**: VERIFIED (4/4 paths converge).
