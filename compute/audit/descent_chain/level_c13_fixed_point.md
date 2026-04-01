# The c=13 Fixed Point: Koszul Self-Duality vs the Critical Line

## Summary

The Koszul involution c -> 26-c for the Virasoro algebra and the
functional equation s -> 1-s for the Riemann zeta function are
**structurally analogous but mathematically disjoint**. Both are Z/2
involutions with distinguished fixed loci (c=13 and Re(s)=1/2
respectively), but they act on different spaces and encode different
information. This document establishes the negative result through
explicit computation and identifies the genuine mathematical content of
self-duality at c=13.


## 1. The Two Involutions

### Koszul involution

The Feigin-Frenkel involution for the Virasoro algebra is c -> 26-c,
so Vir_c^! = Vir_{26-c}. The fixed point c=13 gives Vir_13 = Vir_13^!
(the algebra is self-Koszul-dual). Key data at c=13:

- kappa(13) = 13/2 = 6.5
- kappa'(13) = (26-13)/2 = 13/2
- kappa + kappa' = 13 (AP24: NOT zero; cf. KM where kappa+kappa'=0)
- delta_kappa = kappa - kappa' = 0 (complementarity asymmetry vanishes)
- Delta(13) = 40/87 ~ 0.4598
- rho(13) = sqrt(3212/14703) ~ 0.4674

### Zeta functional equation

The completed Riemann zeta xi(s) = xi(1-s) under s -> 1-s. The fixed
line Re(s)=1/2 is the critical line. The Riemann Hypothesis asserts all
nontrivial zeros lie on this line.


## 2. Shadow Tower at c=13

The shadow tower S_r(Vir_c) satisfies S_r(13) = S_r(26-13) trivially,
since 26-13 = 13. Explicit values:

| r  | S_r(13)              |
|----|----------------------|
| 2  | +6.5000000000        |
| 3  | +2.0000000000        |
| 4  | +8.8417329797e-03    |
| 5  | -3.2646398694e-03    |
| 6  | +1.2476126429e-03    |
| 7  | -4.8721707323e-04    |
| 8  | +1.9293411797e-04    |
| 9  | -7.7077161298e-05    |
| 10 | +3.0953004201e-05    |
| 11 | -1.2460992640e-05    |
| 12 | +5.0178545748e-06    |

The tower has shadow radius rho(13) = 0.4674 < 1, so the shadow
partition function converges absolutely. The alternating sign pattern
(starting at r=5) reflects the branch-point argument theta ~ 2.983 ~
0.95*pi near but not equal to pi.


## 3. The Shadow Metric at c=13

Q_Vir(t, 13) = 169 + 156t + (3212/87)t^2

This quadratic has negative discriminant disc(Q) = -621.6, so the
branch points are complex conjugates:

    t_+/- = -2.1127 +/- 0.3377i,    |t_0| = 2.1395

The Gaussian decomposition: Q = (13 + 6t)^2 + (80/87)t^2.

### Vieta involution

The quadratic Q has a natural involution t -> (q0/q2)/t = (14703/3212)/t
~ 4.578/t that exchanges its two roots. Under this involution:

    Q(q0/(q2*t)) = (q0/(q2*t^2)) * Q(t)

This is a **Moebius transformation** of the shadow metric, not a
functional equation in the L-function sense. It relates the behavior of
the shadow generating function H(t) = t^2*sqrt(Q(t)) at t and at the
inverted point, but with a t-dependent prefactor (q0/(q2*t^2)), not a
constant gamma factor.


## 4. The Sewing Dirichlet Series

The sewing Dirichlet series for the Virasoro is:

    S_Vir(u) = zeta(u+1) * (zeta(u) - 1)

This is **independent of c**. The central charge enters the shadow
partition function only through kappa(c) = c/2 in the genus series
F_g = kappa * lambda_g^FP. The sewing lift sees only the conformal
weight h=2 of the stress tensor, not the central charge.

### Critical-line behavior

S_Vir(1/2+it) = zeta(3/2+it) * (zeta(1/2+it) - 1)

At a Riemann zero zeta(1/2+it_k) = 0:

    S_Vir(1/2+it_k) = zeta(3/2+it_k) * (0 - 1) = -zeta(3/2+it_k)

This is **nonzero** because zeta has no zeros for Re(s) > 1. The sewing
Dirichlet series does NOT vanish at Riemann zeros. Verified numerically
at the first zero t ~ 14.1347:

    |zeta(1/2+i*14.1347)| = 3.63e-19 (zero to numerical precision)
    |S_Vir(1/2+i*14.1347)| = 0.5444 (nonzero)


## 5. The Rankin-Selberg Connection

At c=13, the vacuum character is chi_0 = q^{-1/2}/eta(tau), and the
primary-counting function involves eta^{24} = Delta (the Ramanujan
discriminant form). This produces the Rankin-Selberg L-function:

    L(s, Delta x Delta) = sum |tau(n)|^2 n^{-s} = zeta(s-11) * L(s, Sym^2 Delta)

The functional equation has center s = 23/2 = 11.5 (from weight k=12),
NOT s = 1/2. The critical line is Re(s) = 11.5, shifted by 11 from the
zeta critical line.

Self-duality at c=13 manifests as tau(n) being real (integer-valued), so
Delta is self-conjugate. But tau(n) is real for ALL values of c where
this L-function is defined -- this is a property of the Ramanujan
tau function, not of the central charge. The c=13 self-duality adds
nothing beyond what tau(n) in Z already provides.


## 6. Three Centers of Symmetry

| Involution           | Center      | Space                     | Content                    |
|----------------------|-------------|---------------------------|----------------------------|
| c -> 26-c            | c = 13      | Vir central charge line   | Self-Koszul-duality        |
| s -> 1-s             | Re(s) = 1/2 | Complex s-plane           | Zeta functional equation   |
| s -> 23-s            | Re(s) = 11.5| Complex s-plane           | Rankin-Selberg of Delta    |

These are three different involutions on three different spaces. The
numerical values 13, 1/2, 11.5 bear no mathematical relation.


## 7. Genuine Consequences of Self-Duality at c=13

While the c=13 <-> Re(s)=1/2 analogy is purely structural, self-duality
at c=13 does produce genuine mathematical content:

### (A) Complementarity self-pairing

Theorem C: Q_g(A) + Q_g(A!) = H*(M-bar_g, Z(A)). At c=13 with A = A!:

    2 * Q_g(Vir_13) = H*(M-bar_g, Z(Vir_13))

Each side of complementarity contributes equally.

### (B) Vanishing complementarity asymmetry

delta_kappa = kappa - kappa' = 0 at c=13. The complementarity asymmetry
(AP29) vanishes, but the effective curvature kappa_eff = kappa(matter) +
kappa(ghost) = 13/2 - 13 = -13/2 does NOT vanish. Anomaly cancellation
occurs at c=26 (critical string), not at c=13 (self-dual point).

### (C) Verdier self-duality of the bar complex

D_Ran(B(Vir_13)) = B(Vir_13^!) = B(Vir_13). The Verdier dual of the bar
complex is the bar complex itself. This endows B(Vir_13) with a
self-duality structure (an involution on the factorization coalgebra).

This is the closest genuine analogue to an L-function being self-dual
(L(s,pi) = L(s,pi^v)), which forces zeros to be real or to come in
conjugate pairs on the critical line. But the analogy stops here: the bar
complex is a factorization coalgebra on Ran(X), not a Dirichlet series,
and its "zeros" (if any notion applies) live in a completely different
space from the zeros of zeta.

### (D) Shadow connection palindromic symmetry

The shadow connection nabla^sh = d - Q'/(2Q) dt at c=13 is invariant
under the Koszul involution. The monodromy around each branch point is
-1 (the Koszul sign), and this monodromy is self-dual. The discriminant
complement satisfies Delta(13) + Delta(13) = 80/87 = 2*Delta(13).

### (E) Shadow partition function convergence

The scalar shadow partition function at c=13 is:

    Z^sh(13, hbar) = (13/2) * ((hbar/2)/sin(hbar/2) - 1)

This is meromorphic in hbar with poles at hbar = 2*pi*n and convergence
radius 2*pi. It is an EVEN function of hbar (Z^sh(13,hbar) =
Z^sh(13,-hbar)), reflecting the genus-parity property of the A-hat
genus. This evenness is trivial (all F_g involve hbar^{2g}) and is
unrelated to any functional equation of zeta type.


## 8. The Shadow Dirichlet Series (Formal)

The formal Dirichlet series D_shadow(u) = sum_{r>=2} S_r(13) r^{-u} is
**not an L-function**:

1. S_r is not multiplicative in r (no Euler product)
2. Coefficients alternate in sign (starting at r=5)
3. No functional equation under u -> a-u for any center a (verified
   numerically for a = 1, 2, 3, 5 -- ratios D(a-u)/D(u) are not
   constant)

The shadow tower coefficients are determined by the OPE recursion on the
primary line, which has no multiplicative structure. The recursion
S_r = -nabla_H^{-1}(sum {S_j, S_k}_H) with j+k = r+2 produces rational
functions of c with denominators c^{r-2}(5c+22)^{floor(r/2)-1}, which
are algebraic but not arithmetic.


## 9. Verdict

**The c=13 fixed point of the Koszul involution and the Re(s)=1/2
critical line of the Riemann zeta function are structurally analogous
(both are fixed loci of Z/2 involutions) but mathematically disjoint.**

The analogy fails at every concrete level:

- The sewing Dirichlet series S_Vir(u) is independent of c
- S_Vir does not vanish at Riemann zeros
- The shadow Dirichlet series is not an L-function
- The Rankin-Selberg L-function at c=13 has center s=11.5, not s=1/2
- Self-duality of B(Vir_13) is a statement about factorization
  coalgebras, not about analytic continuation of Dirichlet series

The genuine content of c=13 is: complementarity self-pairing (Theorem C
becomes Q_g(A) = (1/2)H*(M-bar_g,Z(A))), vanishing complementarity
asymmetry (delta_kappa=0), and Verdier self-duality of the bar complex
(D_Ran(B(A)) = B(A)). These are nontrivial properties of the
factorization-algebraic framework but have no implications for the
Riemann Hypothesis or the distribution of zeta zeros.

**Beilinson verdict**: the c=13 <-> critical line analogy is a
**false idea** in the sense of the Beilinson Principle. It is a
surface-level pattern match (Z/2 involution -> fixed point) that does not
survive independent verification against the mathematical structures
involved. Dismissing it is progress.


## Appendix: Numerical Verification Summary

All computations performed with mpmath at 30-50 digit precision.

| Quantity                          | Value                    | Status    |
|-----------------------------------|--------------------------|-----------|
| kappa(13)                         | 13/2 = 6.5              | Exact     |
| Delta(13)                         | 40/87                    | Exact     |
| rho(13)                           | sqrt(3212/14703) ~ 0.467 | Exact     |
| S_r(13) = S_r(26-13) for r=2..12 | All match                | Verified  |
| S_Vir(1/2+i*14.1347) != 0        | |S| = 0.5444             | Verified  |
| D_shadow functional equation      | None found               | Verified  |
| Scalar Z^sh convergence           | Sum = 0.278946339534     | Verified  |
| Closed form match                 | (13/2)((1/2)/sin(1/2)-1) | Verified  |
| Complementarity 2*Delta(13)       | 80/87                    | Exact     |
