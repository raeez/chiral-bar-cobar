# Adversarial Attack on Prime-Locality: Ising Model M(4,3), c = 1/2

## Summary

Explicit computation of the Ising partition function Z_Ising at the coefficient level, testing whether the Dirichlet coefficients are multiplicative. This is a direct verification of `prop:rational-cft-multiplicativity-failure` in `arithmetic_shadows.tex`.

**Verdict**: The manuscript's claim of 14 coprime failures is **CORRECT** under the manuscript's convention, but the description "with m, n <= 20" is **MISLEADING** -- it should say "with mn <= 20" (product bound, not individual bound). With individual m, n <= 20, there are 104+ failures (Convention A) or 98+ failures (Convention B).

**Critical finding**: The equation `|eta(tau)|^2 Z(tau) = sum_{n >= 0} a_n q^n` in the manuscript is **strictly incorrect** because `|eta|^2 Z` does not have integer Fourier exponents. The spin channel theta_{2,1} has exponents in Z + 1/16, so |theta_{2,1}|^2 has exponents in Z + 1/8. The "Dirichlet coefficients" used in the manuscript are a **flattened** quantity that strips the fractional q-power offset from each channel.

## Setup

The Ising model M(4,3) has c = 1/2, three primaries:
- (1,1): h = 0 (identity)
- (2,1): h = 1/16 (spin field sigma)
- (1,2): h = 1/2 (energy operator epsilon)

Partition function: Z = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2.

Using the Rocha-Caridi formula, eta * chi_{r,s} = theta_{r,s} where theta is a theta-like function with explicit integer coefficients. All computations are exact (integer arithmetic, no floating point).

## Two Conventions

### Convention A (manuscript, existing code)

For each primary, compute |theta_i|^2 at integer levels above the channel's ground state, then sum across all channels. This is equivalent to aligning all channels at q^0 and summing.

```
a_0 = 3, a_1 = -2, a_2 = -3, a_3 = -2, a_4 = 0, a_5 = 2,
a_6 = 1, a_7 = 4, a_8 = 1, a_9 = -2, a_10 = 0, a_11 = 2,
a_12 = -3, a_13 = 2, a_14 = -1, a_15 = 0, a_16 = -2, a_17 = 0,
a_18 = -2, a_19 = -4, a_20 = -3, a_21 = 2, a_22 = 1, a_23 = 0,
a_24 = 4, a_25 = -2, a_26 = 5, a_27 = 2, a_28 = 3, a_29 = 0,
a_30 = 0
```

### Convention B (exact)

The exact integer-exponent part of |eta|^2 Z (identity + energy channels only):

```
a_0 = 1, a_1 = -1, a_2 = 1, a_3 = -2, a_4 = -2, a_5 = 1,
a_6 = 0, a_7 = 3, a_8 = 2, a_9 = 0, a_10 = -2, a_11 = 0,
a_12 = -1, a_13 = 2, a_14 = -2, a_15 = 1, a_16 = 0, a_17 = -2,
a_18 = 2, a_19 = -2, a_20 = -4, a_21 = 0, a_22 = 1, a_23 = 0,
a_24 = 2, a_25 = 2, a_26 = 1, a_27 = 0, a_28 = 2, a_29 = 0,
a_30 = 0
```

The spin channel contributes at q^{k + 1/8} for k in Z:
```
k=0: 1, k=2: -2, k=4: -1, k=6: 2, k=8: 1, k=10: 2, k=12: -2, ...
```

**Conventions differ**. a_0 = 3 (Convention A) vs a_0 = 1 (Convention B). The discrepancy is because Convention A adds the spin channel's leading coefficient (1) and the energy channel's leading coefficient (1) to the identity's (1), even though these live at different q-powers.

## Multiplicativity Test Results

### Convention A, product bound mn <= 20 (manuscript claim)

**14 ordered coprime failures** (manuscript says "14 coprime failures with m, n <= 20"):

| m | n | a_{mn} | a_m * a_n | defect |
|---|---|--------|-----------|--------|
| 2 | 3 | 1 | 6 | -5 |
| 2 | 5 | 0 | -6 | 6 |
| 2 | 7 | -1 | -12 | 11 |
| 2 | 9 | -2 | 6 | -8 |
| 3 | 2 | 1 | 6 | -5 |
| 3 | 4 | -3 | 0 | -3 |
| 3 | 5 | 0 | -4 | 4 |
| 4 | 3 | -3 | 0 | -3 |
| 4 | 5 | -3 | 0 | -3 |
| 5 | 2 | 0 | -6 | 6 |
| 5 | 3 | 0 | -4 | 4 |
| 5 | 4 | -3 | 0 | -3 |
| 7 | 2 | -1 | -12 | 11 |
| 9 | 2 | -2 | 6 | -8 |

**VERIFIED**: 14 failures, matching the manuscript claim.

**CLARIFICATION NEEDED**: The manuscript says "m, n <= 20" but the test range is mn <= 20. These are very different: with individual m, n <= 20, there are 104 unordered failures under Convention A.

### Convention A, individual bound m, n <= 30

104 unordered coprime failures.

### Convention B, individual bound m, n <= 30

98 unordered coprime failures.

## Per-Channel Analysis

**All three channels individually fail multiplicativity**:
- Identity channel |theta_{1,1}|^2: 34 failures (m, n <= 15)
- Spin channel |theta_{2,1}|^2: 42 failures (in Q = q^{1/8} variable, m, n <= 15*8)
- Energy channel |theta_{1,2}|^2: 34 failures (m, n <= 15)

This rules out any per-channel rescue of multiplicativity.

## Hecke Recursion Analysis

For a weight-k Hecke eigenform: a_{p^2} = a_p^2 - chi(p) * p^{k-1} * a_1.
The defects d(p) = a_{p^2} - a_p^2 are:

| p | a_p | a_{p^2} | a_p^2 | defect |
|---|-----|---------|-------|--------|
| 2 | -3 | 0 | 9 | -9 |
| 3 | -2 | -2 | 4 | -6 |
| 5 | 2 | -2 | 4 | -6 |
| 7 | 4 | 0 | 16 | -16 |
| 11 | 2 | -2 | 4 | -6 |
| 13 | 2 | 0 | 4 | -4 |

The defects do NOT follow any p^{k-1} growth pattern: |d(2)| = 9, |d(3)| = 6, |d(5)| = 6, |d(7)| = 16, |d(11)| = 6, |d(13)| = 4. This oscillation confirms the flattened partition function is NOT a Hecke eigenform for any weight.

## Q(sqrt(5)) Arithmetic Analysis

The shadow tower at c = 1/2 has:
- kappa = 1/4
- S_4 = 40/49
- Delta = 8 * kappa * S_4 = 80/49
- sqrt(Delta) = 4*sqrt(5)/7

So Q(sqrt(5)) enters the shadow tower via sqrt(Delta). However:

**FINDING: Q(sqrt(5)) does NOT predict multiplicativity failures.**

The failure primes are {2, 3, 5, 7, 11, 13, 17, 19, 23, 29} -- ALL primes up to the test bound. Their splitting in Q(sqrt(5)):

| Prime | Splitting in Q(sqrt(5)) |
|-------|------------------------|
| 2 | inert |
| 3 | inert |
| 5 | ramified |
| 7 | inert |
| 11 | split |
| 13 | inert |
| 17 | inert |
| 19 | split |
| 23 | inert |
| 29 | split |

Failure counts: split=3, inert=6, ramified=1.
Baseline counts (all primes <= 29): split=3, inert=6, ramified=1.

The distributions are **identical** -- zero enrichment. This makes sense: multiplicativity fails at ALL coprime pairs, regardless of arithmetic properties. The Q(sqrt(5)) number field controls the growth rate of the shadow tower (rho ~ 12.5), not the multiplicativity of the partition function.

## Shadow Metric Discriminant

The user's prompt asks about Q(sqrt(5)). In fact, TWO number fields appear:

1. **Q(sqrt(5))** via sqrt(Delta) = sqrt(80/49) = 4*sqrt(5)/7. This controls the shadow growth rate. It is the magnitude of the branch points of the shadow generating function H(t) = t^2 * sqrt(Q(t)).

2. **Q(sqrt(-10))** via disc(Q) = -160/49. This is the discriminant of the shadow metric Q(t) = c^2 + 12ct + alpha*t^2. The roots of Q(t) are in Q(sqrt(-10)), not Q(sqrt(5)).

The shadow radius is rho = sqrt((180c+872)/((5c+22)*c^2)) = 12.53 at c = 1/2. This is >> 1, confirming the shadow tower diverges (c < c* ~ 6.12).

## Modified Dirichlet Series

**Is there a modified series that IS multiplicative?**

Tested modifications:
1. Normalize by a_1: still fails.
2. Per-channel extraction: all channels fail individually.
3. Hecke recursion: no consistent weight.

**Conclusion**: No simple algebraic modification of the flattened Dirichlet series yields a multiplicative sequence. The structural obstruction is that the partition function is a QUADRATIC FORM on VVMF components, and no individual component is a Hecke eigenform.

The manuscript correctly identifies (in the Level 2 analysis of `prop:shadow-arithmetic-trichotomy`) that multiplicativity is recovered at the SHADOW level: the arity-2 shadow projection Sh_2^{(1)} is proportional to kappa * E_2*(tau), whose Fourier coefficients sigma_1(n) are multiplicative. The shadow level extracts the modular geometry of M-bar_{1,r}, bypassing the per-channel theta function arithmetic.

## Files

- **Module**: `compute/lib/ising_prime_locality.py`
- **Tests**: `compute/tests/test_ising_prime_locality.py` (62 tests, all pass)
- **Audit**: this file

## Manuscript Corrections Recommended

1. **MINOR**: `prop:rational-cft-multiplicativity-failure` proof says "14 coprime failures with m, n <= 20." Should specify: "14 ordered coprime failures with product mn <= 20." With individual m, n <= 20, there are 104+ failures.

2. **MODERATE**: The equation "|eta(tau)|^2 Z(tau) = sum_{n >= 0} a_n q^n" is strictly incorrect for minimal models with non-integer conformal weights (i.e., ALL non-trivial unitary minimal models). The spin channel contributes at q^{h_sigma} = q^{1/8} exponents. The "Dirichlet coefficients" are actually a flattened quantity. This should be noted or the notation should indicate the flattening.

3. **INFORMATIONAL**: Q(sqrt(5)) does NOT predict multiplicativity failures. The connection between the shadow tower's number field and partition function arithmetic is through the SHADOW LEVEL (where multiplicativity is recovered), not through the full partition function (where it fails universally).
