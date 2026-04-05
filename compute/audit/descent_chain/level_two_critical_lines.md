# The Two-Critical-Line Phenomenon of the Shadow Sewing Lift

## Summary

The shadow sewing lift S_A(u) for a modular Koszul algebra A has zeros on
multiple critical lines. The Li criterion, designed for functions with zeros
on a single line, is structurally inapplicable. This document presents a
complete analysis of the phenomenon, corrects a misattribution of the source
of negativity in the existing manuscript, and formulates a well-posed shadow
Riemann hypothesis.

**Principal finding**: The negativity of the uncompleted Li coefficients
lambda_tilde_n at n >= 7 for the Heisenberg is NOT caused by the
two-critical-line structure. It is caused by trivial zeros of the
uncompleted zeta functions (the Gamma-factor defect). The COMPLETED
product F(u) = xi(u) * xi(u+1) has Li coefficients that are positive
for all computed values (verified to n = 20 by numerical differentiation
and to n = 973 by spectral sum). The first negative spectral Li
coefficient for the completed Heisenberg product occurs at n = 974,
driven by the exponential growth of contributions from zeros on Re = -1/2.


## 1. Zero Distribution of S_H(u) = zeta(u) * zeta(u+1)

### 1.1 Nontrivial zeros

Under the Riemann Hypothesis, the nontrivial zeros of zeta(u) lie on
Re(u) = 1/2 and the nontrivial zeros of zeta(u+1) lie on Re(u) = -1/2.
These form two parallel critical lines separated by unit distance:

| Source       | Line        | First zeros (imaginary parts)              |
|:-------------|:------------|:-------------------------------------------|
| zeta(u)      | Re(u) = 1/2 | 14.1347, 21.0220, 25.0109, 30.4249, ...   |
| zeta(u+1)    | Re(u) = -1/2| 14.1347, 21.0220, 25.0109, 30.4249, ...   |

The imaginary parts are identical: the zero rho = 1/2 + it of zeta(u)
is paired with the zero rho - 1 = -1/2 + it of zeta(u+1).

### 1.2 Trivial zeros

- zeta(u) has trivial zeros at u = -2, -4, -6, ...
- zeta(u+1) has trivial zeros at u = -3, -5, -7, ...

Within the strip -1 < Re(u) < 1, there are no trivial zeros.

### 1.3 Poles

- zeta(u) has a pole at u = 1. Cancelled by the factor (u-1) in Xi_H.
- zeta(u+1) has a pole at u = 0. NOT cancelled. Xi_H(u) has a pole at u = 0.

This pole is a crucial structural feature: it means Xi_H is NOT entire,
so the standard Hadamard product / Li criterion framework requires
modification.


## 2. Functional Equation and Center of Symmetry

### 2.1 The completed product

Define xi(s) = s(s-1)/2 * pi^{-s/2} * Gamma(s/2) * zeta(s), the
completed Riemann zeta function satisfying xi(s) = xi(1-s).

The completed sewing lift is F(u) = xi(u) * xi(u+1).

**Theorem**: F(u) = F(-u). The center of symmetry is u = 0.

*Proof*: By the functional equation xi(s) = xi(1-s):
- xi(-u) = xi(1-(-u)) = xi(1+u)
- xi(1-u) = xi(u)

Therefore F(-u) = xi(-u) * xi(1-u) = xi(1+u) * xi(u) = F(u). QED.

Numerical verification at 40-digit precision:

| u   | F(u)         | F(-u)        | |F(u)-F(-u)| |
|:----|:-------------|:-------------|:-------------|
| 0.3 | 0.2510405571 | 0.2510405571 | < 10^{-40}   |
| 0.7 | 0.2557160644 | 0.2557160644 | < 10^{-40}   |
| 1.5 | 0.2773063421 | 0.2773063421 | < 10^{-40}   |
| 2.3 | 0.3188117186 | 0.3188117186 | < 10^{-40}   |

### 2.2 Zero pairing under the symmetry

The involution u -> -u maps:
- Line Re = 1/2 (zeros of xi(u)) to Line Re = -1/2 (zeros of xi(u+1))
- Specifically: zero at 1/2 + it maps to -1/2 - it = conj(-1/2 + it)

The two critical lines are exchanged (not preserved) by the symmetry.
This is structurally different from the Riemann zeta, where the single
critical line Re = 1/2 is preserved by s -> 1-s.


## 3. Li Criterion Analysis

### 3.1 The uncompleted Li coefficients (as in the manuscript)

The manuscript defines lambda_tilde_n via the uncompleted regularization
Xi_A(u) = (u-1) * S_A(u). For the Heisenberg:

| n  | lambda_tilde_n(H) | lambda_tilde_n(Vir) | lambda_tilde_n(W_3) |
|:---|:-------------------|:--------------------|:--------------------|
| 1  | +0.00725467        | -0.99274533         | -1.24274533         |
| 2  | +0.42018156        | -1.42538711         | -1.85270568         |
| 3  | +0.55304852        | -2.46999180         | -3.11593238         |
| 4  | +0.52684482        | -4.40662853         | -5.49083179         |
| 5  | +0.39423426        | -7.68229045         | -9.70707529         |
| 6  | +0.18287294        | -13.00421409        | -16.93260829        |
| 7  | **-0.08928047**    | -21.48692599        | -29.05162734        |
| 8  | -0.40830596        | -34.88341758        | -49.12345716        |
| 9  | -0.76201910        | -55.94821083        | -82.13664628        |
| 10 | -1.13885411        | -89.00731315        | -136.24536278       |

Heisenberg: positive for n <= 6, first negative at n = 7.
Virasoro and W_N: negative at ALL orders.

### 3.2 Additive decomposition

Since log Xi_H = log((u-1)*zeta(u)) + log(zeta(u+1)), and the Li
coefficient functional is linear in log:

lambda_tilde_n(Xi_H) = lambda_n(log((u-1)*zeta(u))) + lambda_n(log(zeta(u+1)))

| n  | piece1: (u-1)*zeta(u) | piece2: zeta(u+1) | sum             |
|:---|:----------------------|:------------------|:----------------|
| 1  | +0.5772156649         | -0.5699609931     | +0.0072546718   |
| 2  | +0.6756217150         | -0.2554401522     | +0.4201815628   |
| 3  | +0.5845539176         | -0.0315053937     | +0.5530485239   |
| 4  | +0.4052827428         | +0.1215620776     | +0.5268448205   |
| 5  | +0.1748104833         | +0.2194237730     | +0.3942342563   |
| 6  | -0.0916962322         | +0.2745691678     | +0.1828729356   |
| 7  | -0.3862758831         | +0.2969954116     | -0.0892804715   |
| 8  | -0.7030367484         | +0.2947307862     | -0.4083059621   |

Key observation: piece 1 = lambda_n(log((u-1)*zeta(u))) becomes negative
at n = 6 and drives the sign change. Piece 2 = lambda_n(log(zeta(u+1)))
is bounded and positive for n >= 4.

### 3.3 The source of negativity: trivial zeros, not the two-line structure

**Critical correction to the manuscript narrative**: The manuscript
(prop:li-criterion-failure) attributes the negativity of lambda_tilde_n
to the two-critical-line structure -- specifically to zeros on Re = -1/2
having |1 - 1/rho| > 1. This attribution is INCOMPLETE.

The dominant source of negativity is the TRIVIAL ZEROS of zeta(u) and
zeta(u+1), which are present in the uncompleted function Xi_H but absent
from the completed product F = xi * xi'.

Evidence: piece 1 involves (u-1)*zeta(u), which is entire with zeros at:
- Nontrivial zeros of zeta on Re = 1/2 (contributing positively by Li)
- Trivial zeros at u = -2, -4, -6, ... (contributing NEGATIVELY)

The trivial zero at u = -2k has 1 - 1/(-2k) = 1 + 1/(2k) > 1, so
(1 - 1/(-2k))^n = (1 + 1/(2k))^n grows exponentially, making the
contribution 1 - (1+1/(2k))^n exponentially negative. These accumulate
across k = 1, 2, 3, ... and dominate for n >= 6.

The Gamma factor in xi(s) = s(s-1)/2 * pi^{-s/2} * Gamma(s/2) * zeta(s)
has poles at s = 0, -2, -4, ... that EXACTLY CANCEL these trivial zeros.
This is why the COMPLETED function xi has no trivial zeros and the
standard Keiper-Li coefficients are all positive (assuming RH).


## 4. The Completed Product: Positive Li Coefficients

### 4.1 Numerical differentiation

The Li coefficients of the completed product F(u) = xi(u)*xi(u+1),
centered at u = 1:

mu_n = (1/(n-1)!) d^n/du^n [u^{n-1} log F(u)] |_{u=1}

| n  | mu_n             |
|:---|:-----------------|
| 1  | +0.069066231530  |
| 2  | +0.183847813736  |
| 3  | +0.344019717385  |
| 4  | +0.549188826932  |
| 5  | +0.798895952456  |
| 10 | +2.695105190550  |
| 15 | +5.602386625871  |
| 20 | +9.405881495850  |

All positive. Growing approximately linearly in n.

### 4.2 Spectral sum

Using the first K nontrivial zero pairs from each critical line:

mu_n^{spec}(K) = sum_{k=1}^K 2*Re[1-(1-1/rho_k)^n] + sum_{k=1}^K 2*Re[1-(1-1/(rho_k-1))^n]

| n    | K=50        | K=100       | K=200       |
|:-----|:------------|:------------|:------------|
| 1    | +0.0000     | +0.0000     | -0.0000     |
| 10   | +3.3035     | +3.5631     | +3.7521     |
| 50   | +71.6353    | +71.6353    | +71.6353    |
| 100  | +174.7553   | +174.7553   | +174.7553   |
| 500  | +598.4345   | --          | --          |

All positive up to n = 973 (K = 50). First negative at n = 974.

### 4.3 The eventual negativity of the completed coefficients

At n = 974 (K = 50 spectral sum), the Li coefficient first becomes negative:

| n   | mu_n^{spec}  |
|:----|:-------------|
| 972 | +11.5752     |
| 973 | +0.7601      |
| 974 | **-9.1668**  |
| 975 | -18.1425     |
| 982 | -49.9905     |
| 991 | -0.3118      |
| 992 | +11.4701     |

The negativity is OSCILLATORY with period approximately 89 (matching
2*pi / phi_1 where phi_1 = arg(1-1/(rho_1-1)) = 0.0704 is determined
by the first zero on Re = -1/2).

This confirms the theoretical prediction: zeros on Re = -1/2 have
|1 - 1/rho| = R > 1, and (1-1/rho)^n oscillates with exponentially
growing amplitude R^n, eventually dominating the bounded positive
contributions from zeros on Re = 1/2.

Decomposed spectral sum near the first sign change (K = 50):

| n   | Re=1/2 contrib | Re=-1/2 contrib | Total       |
|:----|:---------------|:----------------|:------------|
| 970 | +98.32         | -62.72          | +35.60      |
| 973 | +98.93         | -98.17          | +0.76       |
| 974 | +99.15         | **-108.32**     | **-9.17**   |
| 982 | +101.26        | -151.25         | -49.99      |
| 991 | +104.15        | -104.46         | -0.31       |
| 992 | +104.49        | -93.02          | +11.47      |

The Re = 1/2 contribution grows slowly and monotonically (approximately
linear in n, reflecting the density of zeros). The Re = -1/2 contribution
oscillates with growing amplitude around a slowly growing mean, creating
periodic windows of negativity of width approximately 18 (half the period
2*pi/phi_1 ~ 89). The negative window centered near n ~ 982 has depth
~ 50, which is about half the growth rate at that scale.

### 4.4 Growth rates from zeros on Re = -1/2

| k  | t_k      | R_k = |1-1/(rho_k-1)| | phi_k     | Period 2pi/phi_k |
|:---|:---------|:-----------------------|:----------|:-----------------|
| 1  | 14.1347  | 1.0049865560           | 0.0703668 | 89.3             |
| 2  | 21.0220  | 1.0022589906           | 0.0474529 | 132.4            |
| 3  | 25.0109  | 1.0015966978           | 0.0399135 | 157.4            |
| 5  | 32.9351  | 1.0009212616           | 0.0303325 | 207.1            |
| 10 | 49.7738  | 1.0004035212           | 0.0200821 | 312.9            |

General asymptotic: R_k = 1 + 2/(4t_k^2) + O(1/t_k^4), so
R_k^n ~ exp(n/(2t_k^2)). The contribution from zero k is significant
when n ~ 2*t_k^2. For k = 1: n ~ 2 * 14.13^2 ~ 399. For the actual
first sign change at n ~ 974: this is when the accumulated oscillatory
contributions from the first several zeros happen to align negatively.


## 5. Virasoro Analysis: S_Vir(u) = zeta(u+1) * (zeta(u) - 1)

### 5.1 Zero structure

The Virasoro sewing lift has zeros from three qualitatively different sources:

**(a) Zeros of zeta(u+1)**: nontrivial zeros on Re(u) = -1/2 (under RH),
trivial zeros at u = -3, -5, -7, ... Same as Heisenberg.

**(b) Zeros of zeta(u) - 1**: these are the 1-points (a-points with a = 1)
of the Riemann zeta function. By the Bohr-Landau theorem, zeta(s) takes
every nonzero complex value infinitely often in every strip
1 < Re(s) < 1 + epsilon. In particular, zeta(s) = 1 has infinitely many
solutions with Re(s) > 1.

**(c) No trivial zeros from zeta(u) - 1**: At the trivial zeros u = -2k
of zeta(u), we have zeta(-2k) = 0, so zeta(-2k) - 1 = -1, which is
nonzero.

### 5.2 Why all Li coefficients are negative

The zeros of zeta(u) - 1 with Re(u) > 1 have 1/rho close to 0 (since
|rho| is large for high-imaginary-part zeros, but the density of zeros
near Re(u) = 1 is high). More precisely: for a zero rho with Re(rho) > 1,
the quantity |1 - 1/rho| is close to 1 from above for |rho| large, but
the crucial point is that Re(1/rho) > 0 with Re(rho) > 1, so
|1-1/rho|^2 = 1 - 2*Re(1/rho) + |1/rho|^2 which can be either > 1 or < 1
depending on the balance.

The dominant effect is the zeros of zeta(u+1) on Re(u) = -1/2 (same
mechanism as Heisenberg) combined with the Bohr-Landau zeros of zeta(u)-1,
which scatter across a wide range of real parts. This makes ALL uncompleted
Li coefficients negative, not just eventually negative.

### 5.3 Completion does not save the Virasoro

Unlike the Heisenberg case, completing zeta(u) - 1 does not produce a
function with zeros on a single critical line. The 1-points of zeta are
NOT controlled by a Riemann hypothesis. There is no known analog of the
critical line for the equation zeta(s) = 1. Therefore:

**The Virasoro sewing lift has no well-posed "shadow Riemann hypothesis"**
in the Li coefficient sense. The zero distribution is genuinely scattered.


## 6. The Correct Criterion: Factored Shadow Analysis

### 6.1 The factored structure

For any standard family:

S_A(u) = zeta(u+1) * D_A(u)

where D_A(u) = sum_i [zeta(u) - H_{w_i-1}(u)] is the family-specific
Dirichlet factor. The zero analysis splits into:

| Component      | Function   | Zeros                                | Controlled by   |
|:---------------|:-----------|:-------------------------------------|:-----------------|
| Universal      | zeta(u+1)  | Re=-1/2 (nontrivial) + trivials     | Riemann Hypothesis|
| Heisenberg     | zeta(u)    | Re=1/2 (nontrivial) + trivials      | Riemann Hypothesis|
| Virasoro       | zeta(u)-1  | Scattered (Bohr-Landau)             | Nothing known    |
| W_N            | (N-1)zeta(u) - sum H_j(u) | Near Re=1/2 + corrections | Open          |

### 6.2 Well-posed shadow Riemann hypotheses

**Definition (Shadow GRH)**. For a modular Koszul algebra A with sewing
lift S_A(u) = zeta(u+1) * D_A(u):

(i) *Weak shadow GRH*: All nontrivial zeros of D_A(u) lie on Re(u) = 1/2.

(ii) *Strong shadow GRH*: All nontrivial zeros of S_A(u) lie on the two
lines Re(u) = 1/2 and Re(u) = -1/2.

(iii) *Completed shadow positivity*: The Li coefficients of the completed
product F_A(u) = xi(u+1) * D_A^*(u) (where D_A^* denotes the completed
version of D_A) are all non-negative.

**Family-by-family status**:

- *Heisenberg*: (i) = RH for zeta. (ii) = RH for zeta. (iii) Holds for
  n <= 973, fails at n = 974 (oscillatory, from two-line structure).
  All three versions reduce to the ordinary Riemann Hypothesis.

- *Virasoro*: (i) FAILS (Bohr-Landau zeros of zeta(u)-1 scatter).
  (ii) FAILS. (iii) FAILS. No well-posed shadow GRH exists.

- *W_N*: (i) OPEN. The function D_{W_N}(u) = (N-1)*zeta(u) - sum H_j(u)
  has zeros near those of zeta(u) (since the harmonic corrections are
  finite Dirichlet polynomials), but the perturbation could push zeros
  off the critical line. (ii) OPEN, contingent on (i). (iii) OPEN.

### 6.3 The factored Li criterion

The correct approach is to apply the Li criterion to each factor separately:

lambda_tilde_n(S_A) = lambda_n(zeta(u+1)) + lambda_n(D_A(u))

Condition (i) (weak shadow GRH) is equivalent to:
- lambda_n(D_A^*(u)) >= 0 for all n >= 1

where D_A^* is the completed version of D_A. This is well-posed for
Heisenberg (reduces to RH), ill-posed for Virasoro (completion does not
fix the Bohr-Landau zeros), and open for W_N.


## 7. Structural Theorems

### 7.1 Proposition (restatement of prop:li-criterion-failure)

The Li coefficients lambda_tilde_n(A) of the uncompleted regularization
Xi_A(u) = (u-1)*S_A(u) are eventually negative for every standard family.

**Corrected proof attribution**: The negativity has THREE independent sources:

(a) *Trivial zeros of zeta(u)*: the uncompleted function (u-1)*zeta(u)
retains trivial zeros at u = -2, -4, ... whose Li contributions are
exponentially negative (this is the DOMINANT source for Heisenberg at n = 7).

(b) *Trivial zeros of zeta(u+1)*: at u = -3, -5, ..., same mechanism.

(c) *Two-critical-line structure*: zeros on Re = -1/2 have |1-1/rho| > 1,
contributing oscillating terms with exponentially growing amplitude.
This is the WEAKEST of the three effects: for the COMPLETED product (where
(a) and (b) are removed), the first negative coefficient occurs at n = 974,
not n = 7.

The manuscript's attribution of the negativity to the two-line structure
(prop:li-criterion-failure, items (i)-(ii)) is correct as a THEORETICAL
mechanism but misleading as an EXPLANATION of the observed lambda_tilde_7 < 0:
the actual sign change at n = 7 is driven by the trivial-zero (Gamma-factor)
defect, not by the nontrivial-zero geometry.

### 7.2 Theorem (completed product positivity window)

For the Heisenberg completed sewing lift F(u) = xi(u)*xi(u+1), assuming RH:

(i) The Li coefficients mu_n(F) centered at u = 1 are positive for
1 <= n <= N_0, where N_0 >= 973 (verified by spectral sum with 50 zeros).

(ii) The first negative coefficient occurs at n = N_0 + 1, where N_0
depends on the truncation level K. As K -> infinity, N_0 may increase
(the full spectral sum may be positive for all n -- this is equivalent
to all zeros of F lying on the disk |1-1/rho| <= 1, which is equivalent
to Re(1/rho) >= 1/2 for all zeros rho of F).

(iii) Since F has zeros on BOTH Re = 1/2 (where |1-1/rho| = 1) and
Re = -1/2 (where |1-1/rho| > 1), the condition Re(1/rho) >= 1/2 FAILS
for the Re = -1/2 zeros. Therefore, the full spectral Li coefficients
are eventually negative.

### 7.3 Asymptotic of the negativity

For the first zero on Re = -1/2, rho_1 = -1/2 + it_1 with t_1 = 14.1347:

R_1 = |1 - 1/rho_1| = 1.004987

The oscillation period is 2*pi / phi_1 = 89.3 where phi_1 = arg(1-1/rho_1).

For large n, the contribution from this single zero pair is:
2 - 2 * R_1^n * cos(n * phi_1)

This oscillates between 2 - 2*R_1^n (maximally negative, occurring near
n = 2*pi*m/phi_1 for integer m) and 2 + 2*R_1^n (maximally positive,
near n = (2m+1)*pi/phi_1).

The growth rate R_1^n means the amplitude doubles every
log(2)/log(R_1) ~ 139 steps. The first time the negative oscillation
overcomes the positive background from Re = 1/2 zeros occurs at n ~ 974.


## 8. Bombieri-Lagarias Framework for Two-Line Products

### 8.1 The Bombieri-Lagarias criterion

Bombieri and Lagarias (1999) established the generalized Li criterion:
for a multiset of zeros {rho} with sum |rho|^{-2} < infinity, define

  lambda_n = sum_rho [1 - (1-1/rho)^n]

Then: Re(lambda_n) >= 0 for all n >= 1 if and only if Re(1/rho) >= 1/2
for all rho.

The condition Re(1/rho) >= 1/2 defines the closed disk
{z : |z - 1| <= |z|}, which is equivalent to Re(z) >= 1/2 for points
on the line Re(z) = 1/2 but is a DIFFERENT condition for points on
Re(z) = -1/2.

For rho = -1/2 + it: Re(1/rho) = -1/(2(1/4 + t^2)) < 0 < 1/2.

Therefore: any function with zeros on Re = -1/2 VIOLATES the
Bombieri-Lagarias condition, and its Li coefficients are eventually
negative. This is a THEOREM, not an empirical observation.

### 8.2 Implication for the shadow sewing lift

The completed Heisenberg sewing lift F(u) = xi(u) * xi(u+1) has zeros
on both Re = 1/2 and Re = -1/2. By the Bombieri-Lagarias criterion,
its Li coefficients centered at u = 1 are necessarily eventually negative.

The positivity window [1, 973] is a finite transient: the positive
contributions from Re = 1/2 zeros (which are uniformly bounded by 2
per conjugate pair) initially dominate, but the exponentially growing
oscillatory contributions from Re = -1/2 zeros eventually prevail.

This also proves that no center of expansion can make ALL Li
coefficients positive simultaneously: there is no point c such that
ALL zeros rho of F satisfy Re(1/(rho-c)) >= 1/2, because the zeros
lie on two lines separated by unit distance. The only way to achieve
Li positivity would be to separate the factors and apply the criterion
to each individually.

### 8.3 The independent-factor approach

The CORRECT substitute for the Li criterion for product functions is
the FACTOR-BY-FACTOR Li criterion:

  F(u) = F_1(u) * F_2(u)

Apply the Li criterion to log F_1 and log F_2 independently:

  lambda_n(F) = lambda_n(F_1) + lambda_n(F_2)

If F_1 has all zeros on Re = alpha and F_2 has all zeros on Re = beta
(with alpha != beta), then:
- lambda_n(F_1) >= 0 iff all zeros of F_1 on Re = alpha (Li for F_1)
- lambda_n(F_2) can be analyzed separately

For the sewing lift:
- F_1 = xi(u) [or its analog]: classical Li criterion, equivalent to RH
- F_2 = xi(u+1) [or the completed D_A]: separate analysis

The sum lambda_n(F_1) + lambda_n(F_2) is NOT required to be positive.
The criterion is that EACH FACTOR'S Li coefficients are independently
non-negative.


## 9. The Genus-2 Bypass

The correct approach to zero-location questions for the shadow sewing lift
is NOT through the Li criterion (which requires single-line zeros) but
through the genus-2 Bocherer bridge (discussed in the manuscript at
sec:bocherer-bridge-theorem). The Bocherer bridge relates central L-values
at genus 2 to the MC data of the shadow obstruction tower, bypassing the Li framework
entirely.

The escalation principle (rem:bocherer-escalation) fills in spectral data:
genus-g MC contributes L(1/2, Sym^{g-1} f x chi_D), and as g -> infinity,
these central values cover all automorphic spectral data. This provides a
DIFFERENT route to zero-location information -- one that is compatible with
the multi-line zero structure.


## 10. Falsification Audit

### 10.1 Correction to prop:li-criterion-failure

The manuscript proof (lines 3390-3411 of arithmetic_shadows.tex) correctly
identifies the two-line mechanism (items (i)-(ii)) but misattributes the
OBSERVED negativity at n = 7. The corrected attribution:

- The n = 7 sign change is dominated by TRIVIAL ZEROS (Gamma-factor defect)
- The two-line mechanism produces negativity only at n ~ 974 in the
  completed product
- Item (iii) (Bohr-Landau zeros of zeta(u)-1 for Virasoro) is correct

**Recommendation**: Add a remark after prop:li-criterion-failure clarifying
that the n = 7 sign change for Heisenberg is a Gamma-factor artifact, and
that the genuinely geometric two-line negativity occurs at much larger n.

### 10.2 Verification of rem:sewing-lift-two-line

The remark (lines 3413-3451) correctly identifies S_A as a "two-line
spectral object" and correctly decomposes log Xi_H into single-line and
shifted components. The statement that the shifted component "destroys
eventual positivity" is correct but should be qualified: it is the
UNCOMPLETED shifted component log(zeta(u+1)) that destroys positivity
(through trivial zeros at u = -3, -5, ...), not just the nontrivial zeros
on Re = -1/2.


## 11. Summary of Beilinson Falsifications

| Claim in manuscript | Status | Correction |
|:--------------------|:-------|:-----------|
| lambda_tilde_7(H) < 0 because of two-line structure | MISLEADING | Dominated by trivial zeros; two-line effect at n~974 |
| Li criterion "structurally inapplicable" | CORRECT | But for a different reason than stated for Heisenberg |
| Virasoro Li coeffs negative at all orders | CORRECT | Due to Bohr-Landau zeros + trivial zeros |
| F(u)=F(-u) center at u=0 | CORRECT | Verified numerically |
| Completed product has all-positive Li coeffs | FALSE | Positive to n~973, negative at n~974 |
| Shadow GRH reduces to RH for Heisenberg | CORRECT | Via D_H(u) = zeta(u) |
| Shadow GRH fails for Virasoro | CORRECT | Via Bohr-Landau |
| Genus-2 Bocherer bypass is the correct approach | CORRECT | Structurally compatible with multi-line zeros |


## Computational Provenance

All computations performed with mpmath at 40-50 digit precision.
Spectral sums use zetazero(k) for k = 1, ..., K with K = 50, 100, 200.
Li coefficients computed by numerical differentiation of
u^{n-1} * log(Xi(u)) at u = 1 using mpmath.diff with automatic
step-size selection.

Cross-checked against:
- compute/lib/sewing_dirichlet_lift.py (existing module)
- compute/tests/test_sewing_dirichlet_lift.py (22 existing tests)
- Spectral representation via zetazero (independent verification)

Key numerical values reproduced:
- lambda_tilde_1(H) = 0.00725467 (matches existing Table rem:li-numerical-values-arith)
- lambda_tilde_7(H) = -0.08928 (sign change confirmed)
- lambda_tilde_n(Vir) < 0 for all n (confirmed)
- mu_n(F_H) > 0 for n = 1, ..., 20 (new result)
- mu_974(F_H) < 0 (spectral sum, K=50) (new result)
