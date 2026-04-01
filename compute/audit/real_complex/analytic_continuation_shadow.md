# Analytic Continuation of the Shadow Tower to Complex Central Charge

## Date: 2026-04-01

## Summary

The shadow metric Q_L(c, t) for Virasoro is a **rational function** of c, holomorphic on C \ {0, -22/5}. The shadow tower coefficients S_r(c) are obtained by Taylor-expanding sqrt(Q_L(c,t)) and are themselves rational functions of c. We investigated the analytic continuation to complex c, with particular attention to c = 1/2 + i*gamma_n where gamma_n are imaginary parts of Riemann zeta zeros.

**Central negative result**: Nothing special happens at the Riemann zeta zeros. This is provable a priori: S_r(c) is rational in c, and rational functions cannot have resonances at transcendental points.

## 1. Shadow Tower at c = 1/2 + 14.134725i (First Zeta Zero)

All coefficients are finite and nonzero. The tower decays geometrically.

### Exact rational structure

From the convolution recursion for sqrt(Q_L(c,t)):

- S_2(c) = c/2 (linear in c)
- S_3(c) = 2 (constant, universal for Virasoro)
- S_4(c) = 10 / (c^2 (5c + 22)) (rational, poles at c = 0, -22/5)
- S_r(c) for r >= 5: rational functions of c of increasing degree

### Numerical values at c = 1/2 + i * 14.134725...

| r | Re(S_r) | Im(S_r) | |S_r| |
|---|---------|---------|------|
| 2 | +2.500e-01 | +7.067e+00 | 7.072e+00 |
| 3 | +2.000e+00 | +6.331e-18 | 2.000e+00 |
| 4 | -2.630e-04 | +6.144e-04 | 6.683e-04 |
| 5 | -2.052e-04 | -9.656e-05 | 2.268e-04 |
| 6 | +3.671e-05 | -7.133e-05 | 8.022e-05 |
| 7 | +2.547e-05 | +1.428e-05 | 2.920e-05 |
| 8 | -5.645e-06 | +9.270e-06 | 1.085e-05 |
| 9 | -3.423e-06 | -2.258e-06 | 4.101e-06 |
| 10 | +9.112e-07 | -1.278e-06 | 1.570e-06 |

**Branch points**: t+ = -0.0655 - 2.468i, t- = -0.0979 - 2.253i
**Growth rate**: rho = 0.44335 (convergent tower)
**Ratio test**: |S_{r+1}|/|S_r| converges to rho from below (0.339, 0.354, ..., 0.405 at r=18)

**Key observations**:
- S_3 = 2 exactly (to 18 decimal places). This is because S_3 = a_1/3 = q_1/(6*sqrt(q_0)) = 12c/(6c) = 2.
- S_r for r >= 4 are genuinely complex (nonzero imaginary parts).
- The magnitudes decay geometrically with ratio ~0.4, same as at any real c ~ 14.
- There is nothing special about this value of c. The tower is a smooth function of |c| at this point.

## 2. Smoothness on the Critical Line: No Resonances at Zeta Zeros

### Resonance check at first 3 zeta zeros

For each zeta zero gamma_n, we computed |S_r(1/2 + it)| for t in [gamma_n - 1, gamma_n + 1] at 21 sample points, for r = 4, 6, 8, 10.

**Result: ZERO local maxima at ANY zeta zero for ANY arity.**

| Zero | gamma_n | |S_4| at zero | Local max? | Range in neighborhood |
|------|---------|--------------|------------|----------------------|
| 1 | 14.1347 | 6.683e-04 | No | [5.483e-04, 8.257e-04] |
| 2 | 21.0220 | 2.095e-04 | No | [1.827e-04, 2.419e-04] |
| 3 | 25.0109 | 1.254e-04 | No | [1.116e-04, 1.415e-04] |

At every zeta zero, |S_r| lies in the interior of its local range, with no peak or special feature. The variation is monotonic (decreasing in t at large t).

### Growth rate rho(1/2 + it) vs t

| t | rho | Note |
|------|--------|------|
| 5.00 | 1.3168 | |
| 10.00 | 0.6360 | |
| 14.13 | 0.4435 | zeta zero |
| 14.50 | 0.4318 | |
| 20.00 | 0.3097 | |
| 21.02 | 0.2942 | zeta zero |
| 25.01 | 0.2462 | zeta zero |
| 30.00 | 0.2044 | |
| 32.94 | 0.1858 | zeta zero |
| 40.00 | 0.1525 | |
| 50.00 | 0.1216 | |

rho(1/2 + it) is monotonically decreasing in t, with no features at zeta zeros. Asymptotically, rho ~ C/|t| for large t (the branch points of Q_L move away from the origin as |c| grows).

### Theoretical explanation

S_r(c) is a **rational function** of c. The poles are at c = 0 (from kappa = c/2 in the denominator) and c = -22/5 (from S_4 = 10/(c(5c+22))). On the critical line c = 1/2 + it, the function t -> |S_r(1/2+it)| is real-analytic (smooth). A rational function of c evaluated on any line in C produces a rational function of the line parameter t, which is smooth and cannot have isolated peaks at transcendental points.

The Riemann zeta zeros gamma_n are transcendental (Hermite-Lindemann: if alpha is algebraic and nonzero, then e^{i*alpha} is transcendental; the functional equation of zeta forces the zeros to be transcendental). A rational function of t cannot distinguish these points from any other point on the real line.

## 3. Epstein Zeta at Complex c: Convergence Failure

### The obstruction

The Epstein zeta sum' Q(m,n)^{-s} requires Q(m,n) to have bounded argument away from pi for all (m,n) != (0,0). At complex c, Q(m,n) has complex coefficients and the argument sector is NOT bounded:

- At c = 10 (real): max|arg Q(m,n)| = 0.00 deg. Positive definite. Epstein converges.
- At c = 1/2 + 14.13i: max|arg Q(m,n)| = 180.0 deg. Q(-12,1) is nearly negative real.

**The theta function theta_Q(t) = sum exp(-pi*t*Q(m,n)) does NOT converge** at complex c when Re(Q(m,n)) can be negative. The standard Mellin-splitting method fails entirely.

### Q_L coefficients at c = 1/2 + 14.13i

q_0 = c^2 = -199.54 + 14.13i (nearly negative real!)
q_1 = 12c = 6.00 + 169.62i
q_2 = 35.93 - 0.03i (nearly real positive)

The problem is clear: q_0 ~ -200, so Q(m,0) = q_0 * m^2 ~ -200 m^2 is large and negative. The theta sum exp(-pi*t*Q(m,0)) = exp(+200*pi*t*m^2) DIVERGES.

### Conclusion on Epstein zeta at complex c

The Epstein zeta epsilon_{Q_L(c)}(s) is not defined for generic complex c. The lattice sum diverges because Q(m,n) takes values with argument near pi (nearly negative real), making exp(-pi*t*Q) exponentially growing. There is no analytic continuation of the Epstein zeta to complex c via the theta-function route.

Alternative approaches (e.g., defining Q^{-s} via a specific branch cut) might produce a convergent sum for Re(s) sufficiently large, but this would not have a functional equation, and the resulting object would not be an L-function in any standard sense.

## 4. Discriminant at Complex c

disc(Q_L(c)) = -320 c^2 / (5c + 22)

At c = 1/2 + 14.13i:
- disc = 222.47 - 826.37i (genuinely complex)
- |disc| = 855.79
- arg(disc) = -74.9 deg

For real c, disc is real and determines an imaginary quadratic field K = Q(sqrt(disc)). The Epstein zeta decomposes into the Dedekind zeta zeta_K(s) (for class number 1) or a sum over class group characters.

**For complex c, disc is complex, and this arithmetic framework dissolves entirely.** The "quadratic extension" Q(sqrt(disc)) embeds into C as a split extension (every quadratic extension of C is trivial). There is no number field, no class group, no Hecke L-functions, and no arithmetic content. The connection between the shadow metric and number theory is intrinsically a phenomenon of REAL central charge.

## 5. The Overdetermination Question

**Claim to test**: The functional equation Xi_Q(s) = Xi_Q(1-s), required for each fixed c, could constrain the zeros in the (c, s)-plane.

**Verdict: No.** Each fixed real c gives an independent Epstein zeta with its own independent functional equation. The zeros of eps_{Q(c)}(s) in s depend continuously on c and trace out curves in the (c, s)-plane, but these curves are controlled by the discriminant disc(c), which varies continuously and independently of the Riemann zeta.

At complex c, the framework breaks down entirely:
- The Epstein sum does not converge (argument sector violation)
- The theta function does not converge (negative-definite directions)
- The functional equation has no analogue (no Poisson summation for complex forms)

The (c, s) system is not overdetermined. Each real c produces one L-function with one functional equation. The system is exactly determined at each c, and the different c-values are independent.

## 6. What IS True (and What This Investigation Reveals)

### The shadow tower is algebraic

S_r(c) is a rational function of c for each r. The generating function H(c,t) = t^2 * sqrt(Q_L(c,t)) is algebraic in t (degree 2) for each c, and rational in c for each t. This is a manifestation of the finite-order nature of the convolution recursion for sqrt of a quadratic.

### The Epstein zeta connects to number theory only at real c

At real c with integer or rational discriminant, the Epstein zeta decomposes into Dedekind zeta functions of imaginary quadratic fields. This connection is broken at complex c because:
1. Complex discriminants do not define number fields
2. The Epstein sum itself fails to converge
3. There is no Poisson summation for complex-coefficient quadratic forms

### The separation theorem

The shadow tower (algebraic, rational in c) and the Riemann zeta function (transcendental, defined by the Euler product over primes) are separated by a categorical gap:

1. **Pole structure**: S_r(c) has poles at c = 0 and c = -22/5. The Riemann zeta has a pole at s = 1. These are different objects in different spaces.

2. **Analytic type**: S_r(c) is rational (meromorphic with finitely many poles). zeta(s) is meromorphic with infinitely many zeros. No rational function can have infinitely many zeros.

3. **Arithmetic content**: The Epstein zeta of Q_L connects to imaginary quadratic L-functions. The Riemann zeta is the L-function of the trivial character. These are different rows of the automorphic forms table.

4. **Critical line behavior**: On c = 1/2 + it, the shadow tower varies smoothly and monotonically (in modulus). On s = 1/2 + it, the Riemann zeta has infinitely many zeros. These are fundamentally different behaviors that cannot be mapped onto each other.

## Compute Artifacts

- Module: `compute/lib/shadow_tower_complex_c.py`
- Tests: `compute/tests/test_shadow_tower_complex_c.py` (55 tests, all passing)
- Key functions: `shadow_coefficients_complex`, `shadow_growth_rate_complex`, `investigate_at_zeta_zero`, `check_zeta_zero_resonances`, `full_investigation_report`
