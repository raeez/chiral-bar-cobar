# Route C Arity-4 Attack: MC Overdetermination Fails for Virasoro

**Date**: 2026-04-01
**Target**: Route C (arithmetic_shadows.tex, subsec:route-c-development)
**Claims attacked**: prop:rigidity-threshold item (i), def:rigidity-defect applied to Virasoro
**Status tags audited**: thm:route-c-propagation (ClaimStatusProvedHere)
**Severity**: SERIOUS
**Error class**: B (formula/counting) + AP7 (scope inflation) + AP9 (same name, different object)

## Executive Summary

Route C claims that for Virasoro with m=1 spectral atom, the rigidity defect
delta(1,r) = r-3 is positive at r >= 4, making the shadow tower
overdetermined and forcing prime-locality. This is FALSE for three
independent, compounding reasons:

1. The Virasoro shadow tower does NOT have m=1 Stieltjes atoms.
   The spectral measure is continuous and signed (m = infinity).
2. The 1-atom model explicitly fails at S_4: it predicts S_4 = 9/c,
   but the actual value is S_4 = 10/(c(5c+22)).
3. The equation count r-1 is inflated: only 3 equations (from S_2, S_3, S_4)
   are independent; the rest are consequences of the MC recursion.

Route C remains logically valid as a conditional theorem but is inapplicable
to Virasoro. It applies correctly to lattice VOAs.

## The Claim Under Attack

**prop:rigidity-threshold** (line 4734, arithmetic_shadows.tex):

> (i) For Virasoro (m=1): delta(1,r) = r-3, so rigidity begins at r=4
>     (the quartic contact shadow Q_Vir^ct).

**def:rigidity-defect** (line 4720):

> For a spectral measure with m atoms, the MC recursion at arities 2,...,r
> gives (r-1) polynomial equations in 2m unknowns (m atoms + m weights).
> The rigidity defect is delta(m,r) := (r-1) - 2m.

**thm:route-c-propagation** (line 6113): Tagged ClaimStatusProvedHere.

## Problem 1: m != 1 for Virasoro (the spectral measure is continuous)

The Stieltjes representation (Theorem prop:shadow-spectral-measure) gives:

    G(t) = integral log(1 - lambda*t) d rho(lambda)
    S_r = -(1/r) integral lambda^r d rho(lambda)

The claim "m=1 for Virasoro" refers to the leading-order approximation:

    rho ~ delta(lambda + 6/c)  (a single atom at lambda_eff = -6/c)

But this is the LEADING-ORDER (large-r asymptotics) approximation only.
The exact shadow generating function is:

    H(t) = t^2 sqrt(Q_L(t))

where Q_L(t) = c^2 + 12ct + alpha(c)*t^2 with alpha(c) = (180c+872)/(5c+22).

### The discriminant proves m != 1

The discriminant of Q_L is:

    disc(Q_L) = (12c)^2 - 4*c^2*alpha(c) = -320*c^2/(5c+22)

This is NEGATIVE for all c > 0 (and indeed for all c > -22/5).

Consequence: sqrt(Q_L(t)) has branch points at COMPLEX values of t.
The Stieltjes measure rho is supported on a curve in the complex plane,
not at isolated real points. The number of atoms is m = infinity
(continuous signed measure).

### The manuscript itself proves this

prop:stieltjes-signed-universal (line 4990) proves that rho is a SIGNED
measure for all class-M theories with c > -22/5. The Hankel matrix of
moments has full rank at every size n >= 2, "confirming infinite support."

This directly contradicts the m=1 claim in prop:rigidity-threshold.

## Problem 2: The 1-atom model is explicitly inconsistent at S_4

If rho = c_1 delta(lambda_1) with a single real atom, then:

    S_2 = -(1/2) c_1 lambda_1^2
    S_3 = -(1/3) c_1 lambda_1^3

These determine:

    lambda_1 = 3*S_3/(2*S_2) = 3*2/(2*(c/2)) = 6/c
    c_1 = -2*S_2/lambda_1^2 = -c^3/36

The 1-atom model then PREDICTS:

    S_4^{predicted} = -(1/4) c_1 lambda_1^4 = 9/c

The ACTUAL Virasoro quartic contact invariant is:

    S_4^{actual} = 10/(c(5c+22))

### Numerical comparison

| c    | S_4^{predicted} | S_4^{actual} | Ratio    |
|------|----------------|--------------|----------|
| 0.5  | 18.000000      | 0.816327     | 22.0     |
| 1.0  | 9.000000       | 0.370370     | 24.3     |
| 6.0  | 1.500000       | 0.032051     | 46.8     |
| 13.0 | 0.692308       | 0.008842     | 78.3     |
| 26.0 | 0.346154       | 0.002530     | 136.8    |

The discrepancy GROWS as O(c), confirming that the 1-atom model is
structurally wrong, not merely inaccurate.

### Algebraic form of the discrepancy

    S_4^{predicted} - S_4^{actual} = (45c + 188)/(5c^2 + 22c)

This is a nontrivial rational function of c, never zero for c > 0.

## Problem 3: The MC recursion is incompatible with ANY finite-atom model

The MC recursion on the shadow tower has THREE independent inputs:
S_2 = kappa, S_3 = alpha, S_4 (quartic contact).

For r >= 5, S_r is DETERMINED by the recursion:

    S_r = -(1/(2r*kappa)) * SUM_{j+k=r+2, 3<=j<=k<r} f(j,k)*j*k*S_j*S_k

This is confirmed computationally: mc_recursion_rational and
sqrt_ql_rational agree exactly at every arity r >= 2 (verified to r=30
at 15 central charges in full_shadow_landscape.py).

The MC recursion and Newton's identities are DIFFERENT recursions. For
a finite-atom measure with m atoms, Newton's identity gives a LINEAR
recursion of depth m:

    p_r = e_1*p_{r-1} - e_2*p_{r-2} + ... + (-1)^{m-1}*e_m*p_{r-m}

The MC recursion involves ALL lower-arity S_j through the convolution
bracket structure.

**Verification at c=1 with 2 atoms**: From p_1=0, p_2=-1, p_3=-6,
Newton for 2 atoms determines e_1=6, e_2=1/2 and predicts p_4 = -35.5.
But the actual (MC-derived) p_4 = -40/27 = -1.48. The discrepancy
is a factor of 24. At higher arities, Newton and MC diverge exponentially.

This means the Virasoro shadow tower moments cannot be the moments
of ANY finite-atom measure, regardless of the number of atoms.
The "rigidity defect" delta(m,r) with finite m is conceptually
inapplicable to Virasoro.

### The equation-count interpretation

Route C counts (r-1) moment equations at arities 2,...,r against 2m
spectral unknowns. Since the MC recursion determines S_r for r >= 5
from (S_2, S_3, S_4), only 3 moment equations are truly independent.
But even these 3 conditions (from S_2, S_3, S_4) are INCONSISTENT
with any finite-atom model, so the equation count r-1 vs 2m is moot:
the system has no solution at any m.

## The AP9 Conflation (Same Name, Different Object)

Route C uses "m" to mean two different things:

**For lattice VOAs**: m = number of Hecke eigencomponents of the theta
function = dim S_{k/2} + 1 (cusp forms + Eisenstein). This is the number
of SPECTRAL ATOMS in the Stieltjes representation, because the
shadow-spectral correspondence (thm:shadow-spectral-correspondence)
identifies Stieltjes atoms with Hecke eigenvalues.

**For Virasoro**: m is implicitly set to 1, meaning "one character
component" or "one effective coupling lambda_eff = -6/c." But this
is NOT the number of Stieltjes atoms. The single character gives a
continuous spectral measure with infinitely many atoms.

The shadow-spectral correspondence DOES NOT HOLD for Virasoro:
- For lattices: Stieltjes atoms = Hecke eigenvalues (finite, real, discrete)
- For Virasoro: Stieltjes measure = continuous, complex, signed

## Impact Assessment

### prop:rigidity-threshold item (i)
**Verdict**: FALSE as stated. "m=1 for Virasoro" is incorrect in the
Stieltjes sense. Should either be removed or qualified to clarify that
"m=1" refers to the leading-order effective coupling, not the number
of Stieltjes atoms.

### thm:route-c-propagation
**Verdict**: LOGICALLY VALID as a conditional theorem (hypotheses (a)
and (b) are explicit). But INAPPLICABLE to Virasoro because:
- The proof uses the MC recursion S_r = -(1/(2r)) sum j*k*S_j*S_k*P,
  which is correct for r >= 5.
- The proof then claims "For r >= 4, the rigidity defect delta(m,r) > 0"
  (line 6165), which requires m=1. But m=1 is wrong.
- The proof is VALID for lattice VOAs where m is genuinely finite.

### Route C's characterization as "most promising" (line 6019)
**Verdict**: Misleading for non-lattice theories. Should be qualified:
"most promising for lattice VOAs; for non-lattice theories, the finite-atom
hypothesis fails and the mechanism is inapplicable."

## The MC Recursion at r=4: What Actually Happens

The MC recursion (from shadow_tower_ope_recursion.py) at r=4 gives:

    obs = (1/2)*3*3*S_3^2 = 9*alpha^2/2 = 18 (for alpha=2)
    S_4 = -obs/(2*4*kappa) = -18/(4c) = -9/(2c)

But the actual Virasoro S_4 = 10/(c(5c+22)).

This proves that the MC recursion DOES NOT extend to r=4: S_4 is not
determined by the nonlinear obstruction from (S_2, S_3) alone.
S_4 is genuinely independent initial data, encoding the quartic contact
coupling of the Virasoro OPE.

The code correctly treats S_4 as independent input (both
mc_recursion_rational and sqrt_ql_rational take S_4 as a parameter).

## Verification Script

```python
# Verify all claims in this document
from fractions import Fraction
from compute.lib.shadow_tower_ope_recursion import mc_recursion_rational, sqrt_ql_rational
from compute.lib.full_shadow_landscape import shadow_tower_coefficients

# 1. MC recursion starts at r=5, not r=4
kappa = Fraction(1, 2)
S3 = Fraction(2)
S4 = Fraction(10, 27)  # Virasoro at c=1

mc = mc_recursion_rational(kappa, S3, S4, 10)
ql = sqrt_ql_rational(kappa, S3, S4, 10)
for r in range(2, 11):
    assert mc[r] == ql[r], f"Mismatch at r={r}"
print("MC recursion = sqrt(Q_L) for all r=2..10: PASS")

# 2. 1-atom model fails at S_4
c_val = Fraction(1)
lam = Fraction(6)  # 6/c at c=1
c1 = -c_val**3 / 36
S4_predicted = -c1 * lam**4 / 4
S4_actual = Fraction(10, 27)
assert S4_predicted != S4_actual, "1-atom model should fail"
print(f"1-atom S_4 = {S4_predicted} != actual {S4_actual}: PASS")

# 3. MC recursion at r=4 gives wrong answer
obs = Fraction(1,2) * 9 * S3**2  # (1/2)*3*3*S3^2
S4_mc = -obs / (2 * 4 * kappa)
assert S4_mc != S4_actual, "MC recursion at r=4 should fail"
print(f"MC at r=4: S_4 = {S4_mc} != actual {S4_actual}: PASS")
```

## Recommended Fixes

1. **prop:rigidity-threshold item (i)**: Change "For Virasoro (m=1)" to
   "For lattice VOAs with a single cusp-form atom (m=1)" or qualify
   that m=1 is the leading-order effective-coupling approximation.

2. **thm:route-c-propagation**: Add a remark clarifying that the theorem
   applies to families with finite-atom Stieltjes measures (lattice VOAs),
   and that for class-M theories (Virasoro, W_N), the spectral measure
   is continuous and the overdetermination mechanism is inapplicable.

3. **Route C description** (line 6019): Qualify "most promising" with
   "for lattice VOAs" and add that alternative mechanisms are needed
   for non-lattice theories.

4. **def:rigidity-defect**: Add a remark noting that the equation count
   r-1 is inflated by MC-recursion-dependent equations; the true
   number of independent constraints from the shadow tower is 3
   (from S_2, S_3, S_4), since all S_r for r >= 5 are recursively
   determined.
