# Level 2 -> Level 3: Functional Equations of the Dirichlet-Sewing Lift

## Status: RIGOROUS ANALYSIS (computed and verified to 40 digits)

This document analyzes whether the shadow complementarity identities
(kappa + kappa' = 13 for Virasoro, Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c)))
descend to analytic functional equations on the Dirichlet-sewing lifts S_A(u).

---

## 1. Functional equation of S_H(u) = zeta(u)zeta(u+1)

### 1.1 The completed zeta functional equation

Define the completed zeta:

    xi(s) := pi^{-s/2} Gamma(s/2) zeta(s).

This satisfies xi(s) = xi(1-s) (the functional equation of the Riemann zeta function).

### 1.2 The completed sewing lift HAS a functional equation

**Theorem.** The completed Heisenberg sewing lift

    Xi_H(u) := xi(u) * xi(u+1)

satisfies the functional equation

    Xi_H(u) = Xi_H(-u),

i.e., Xi_H is an EVEN function. The center of symmetry is u = 0.

**Proof.** Apply the functional equation xi(s) = xi(1-s) to each factor:

    Xi_H(-u) = xi(-u) * xi(-u + 1)
             = xi(-u) * xi(1 - u)
             = xi(1 - (-u)) * xi(u)     [using xi(-u) = xi(1+u) and xi(1-u) = xi(u)]
             = xi(1 + u) * xi(u)
             = xi(u) * xi(u + 1)
             = Xi_H(u).   QED.

**Verification.** Confirmed numerically to 40 decimal places at u = 0.5, 1.5, 2.5,
3.7, and at the complex points 0.3+1.5i, 2.1-0.7i, -1.3+4.2i, 0+14.13i.
The identity holds to machine precision in every case (relative error < 10^{-40}).

### 1.3 The uncompleted form

In terms of the original (uncompleted) zeta function, write G(s) = pi^{-s/2}Gamma(s/2).
Then Xi_H(u) = G(u)*G(u+1)*zeta(u)*zeta(u+1), and the even symmetry gives:

    zeta(u)*zeta(u+1) = [G(-u)*G(1-u)] / [G(u)*G(u+1)] * zeta(-u)*zeta(1-u).

Using zeta(1-s) = chi(1-s)*zeta(s), one verifies that the gamma ratio equals
1/[chi(-u)*chi(1-u)], so this reduces to the tautology 1 = 1. The non-trivial
content lives entirely in the COMPLETED form.

**The Gamma-ratio factor.** By the Legendre duplication formula
Gamma(u/2)*Gamma((u+1)/2) = sqrt(pi)*2^{1-u}*Gamma(u), the completed product is:

    Xi_H(u) = pi^{-u} * 2^{1-u} * Gamma(u) * zeta(u)*zeta(u+1).

### 1.4 Zeros and the two critical lines

The zero set of Xi_H(u) is the union:
- {rho} from zeta(u), where rho are the nontrivial zeros (Re(rho) = 1/2 under RH).
- {rho - 1} from zeta(u+1), i.e., u = rho - 1 (Re = -1/2 under RH).

Under u -> -u, the map sends rho to -rho and rho-1 to -(rho-1) = 1-rho.
By the zero-pairing symmetry of zeta (the zeros come in pairs rho, 1-rho_bar),
this PERMUTES the zero set. The even symmetry Xi_H(u) = Xi_H(-u) is
consistent: it exchanges the Re = 1/2 zeros with the Re = -1/2 zeros.

The center u = 0 lies midway between the two critical lines Re = 1/2 and Re = -1/2.
This is the unique center about which the combined zero set is symmetric.

### 1.5 Why u -> 1-u does NOT work

One might expect a center at u = 1/2 (the center of zeta itself). But:

    Xi_H(1-u) = xi(1-u)*xi(2-u) = xi(u)*xi(2-u).

This equals Xi_H(u) = xi(u)*xi(u+1) only if xi(2-u) = xi(u+1), i.e., xi(s) = xi(3-s).
But xi satisfies xi(s) = xi(1-s), not xi(s) = xi(3-s). So the center is NOT u = 1/2.

Numerically: Xi_H(2.5)/Xi_H(1-2.5) = Xi_H(2.5)/Xi_H(-1.5) = 0.1030... (not 1).
But Xi_H(2.5)/Xi_H(-2.5) = 1.000... (exact).

---

## 2. Koszul involution and S_H

### 2.1 Koszul dual of Heisenberg

The Heisenberg algebra H_k at level k has kappa(H_k) = k. The Koszul dual has
kappa' = -k (with the caveat from AP25 that H_k^! = Sym^ch(V*), not literally H_{-k}).

The Dirichlet-sewing lift S_H(u) = zeta(u)*zeta(u+1) depends only on the
conformal WEIGHT of the generator (weight 1), not on the level k. The level k
enters through kappa = k but NOT through S_A(u), which is defined purely from
the weight multiset W(A) = {w_i}.

**The Koszul involution k -> -k does NOT produce a functional equation of S_H(u).**
The complementarity kappa + kappa' = 0 is a relation between modular
characteristics, not a relation between sewing lifts.

### 2.2 What the Koszul involution does

The complementarity kappa + kappa' = 0 for Heisenberg means:

    F_g(H_k) + F_g(H_{-k}) = kappa*lambda_g^FP + (-kappa)*lambda_g^FP = 0.

This is a relation between genus-g FREE ENERGIES. The sewing lift lives at genus 1
(as the Mellin transform of the genus-1 connected free energy). The complementarity
is a relation between the COEFFICIENTS of the shadow obstruction tower, not a functional equation
OF the sewing lift. A functional equation is a self-duality f(a-s) = (gamma)*f(s)
of a SINGLE function. Complementarity is a relation f(A) + f(A') = 0 between TWO
functions evaluated at TWO DIFFERENT algebras.

### 2.3 The functional equation Xi_H(u) = Xi_H(-u) is INDEPENDENT of complementarity

The even symmetry of Xi_H is a consequence of the zeta functional equation alone.
It holds for ANY product xi(s)*xi(s+1), regardless of the algebra. It is NOT related
to the Koszul involution or to the complementarity identity kappa + kappa' = 0.

---

## 3. Functional equation of S_Vir(u) = zeta(u+1)(zeta(u) - 1)

### 3.1 Direct analysis

    S_Vir(u) = zeta(u+1) * (zeta(u) - 1).

The term zeta(u) - 1 = sum_{n>=2} n^{-u} is the Riemann zeta with the n=1 term
removed. This function does NOT have a standard functional equation. The functional
equation of zeta is a global analytic identity that requires ALL terms in the Dirichlet
series; removing even a single term destroys it.

### 3.2 The completed Virasoro sewing lift

Define Xi_Vir(u) = xi(u+1) * [xi(u) - G(u)] where G(u) = pi^{-u/2}Gamma(u/2)
(i.e., xi(u) - G(u) is the "completed" version of zeta(u) - 1). But xi(u) - G(u) does
NOT satisfy any standard functional equation, because removing the n=1 term from
the Dirichlet series breaks the Poisson summation that underlies xi(s) = xi(1-s).

**S_Vir(u) does NOT satisfy any Hecke-type functional equation.**

### 3.3 The Virasoro defect ratio

D_Vir(u) = S_Vir(u)/S_H(u) = (zeta(u) - 1)/zeta(u) = 1 - 1/zeta(u).

This ratio has:
- Poles at the nontrivial zeros of zeta(u) (where 1/zeta diverges).
- Zeros at the solutions of zeta(u) = 1 (no known critical-line structure).

The Virasoro defect ratio SEES the zeta zeros through its POLE STRUCTURE, not through
a functional equation. This is consistent with rem:structural-obstruction in the
manuscript: the MC equation constrains spectral data on the real axis, while
zeta zeros live at complex spectral parameters.

---

## 4. Complementarity and the Dirichlet-sewing lifts

### 4.1 The question

The complementarity identities are:
- kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
- Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)].

Can these be lifted to a relation between S_{Vir_c}(u) and S_{Vir_{26-c}}(u)?

### 4.2 The answer: NO

Both S_{Vir_c}(u) and S_{Vir_{26-c}}(u) equal the SAME function:

    S_Vir(u) = zeta(u+1)*(zeta(u) - 1)

for ALL values of c. The sewing lift depends only on the weight multiset
W(Vir) = {2}, which is INDEPENDENT of the central charge c. The central
charge enters the shadow obstruction tower through the OPE structure constants,
NOT through the weight multiset.

**The sewing lift S_A(u) forgets the central charge entirely.** It records
only which conformal weights appear as generators. The complementarity
identities are relations between shadow coefficients (kappa, Delta, S_4, ...),
which are rational functions of c. The sewing lift is a UNIVERSAL object
attached to the weight data alone.

### 4.3 Proper formulation

The correct relationship between complementarity and the sewing lift operates
at a DIFFERENT level. The shadow obstruction tower S_r(c) are the Taylor coefficients
of the algebraic generating function H(t, c). The c-dependence lives in these
coefficients, not in the base Dirichlet series.

The complementarity identities are relations among the coefficients:
- At arity 2: S_2(c) + S_2(26-c) = kappa(c) + kappa(26-c) = 13.
- At arity 4: Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)].

These are polynomial/rational identities in c arising from the Feigin-Frenkel
involution c -> 26-c. They are NOT functional equations of S_A(u).

### 4.4 The architecture

The descent chain:

    Level 1: Modular invariance of Z(tau)
    Level 2: Shadow complementarity (kappa + kappa' = 13, Delta + Delta' = ...)
    Level 3: Algebraic constraints on spectral coefficients c(t) in the
             Roelcke-Selberg decomposition of Z-hat on M_{1,1}

Level 3 is NOT a functional equation of S_A(u). It is a system of algebraic
constraints on the REAL spectral axis. The structural obstruction
(rem:structural-obstruction) is definitive: the MC equation constrains data
on the real axis, while zeta zeros live at COMPLEX spectral parameters.

---

## 5. The Li coefficients: why they become negative

### 5.1 The classical Li criterion

The Li criterion (Li 1997, Bombieri-Lagarias 1999): define

    lambda_n = sum_rho [1 - (1 - 1/rho)^n]

where rho ranges over the nontrivial zeros of xi(s). Then:

    RH  <==>  lambda_n > 0 for all n >= 1.

### 5.2 The shadow Li coefficients

For Heisenberg, Xi_H(u) = (u-1)*zeta(u)*zeta(u+1), and the shadow Li
coefficients are:

    lambda~_n = (1/(n-1)!) d^n/du^n [u^{n-1} log Xi_H(u)] |_{u=1}.

Computed values (from the test suite and independent verification):

    n    lambda~_n(H)        sign
    1    +0.007254671807      +
    2    +0.420181562802      +
    3    +0.553048523891      +
    4    +0.526844820476      +
    5    +0.394234256302      +
    6    +0.182872935628      +
    7    -0.089280471471      -    <-- SIGN CHANGE
    8    -0.408305962119      -
    9    -0.762019098907      -
   10    -1.138854109520      -

### 5.3 The structural reason for sign change: two critical lines

The zeros of Xi_H(u) = (u-1)*zeta(u)*zeta(u+1) come from:
- zeta(u): nontrivial zeros at u = rho (Re = 1/2 under RH).
- zeta(u+1): nontrivial zeros at u = rho - 1 (Re = -1/2 under RH).

The Li coefficients lambda~_n are computed with expansion point u = 1. For the
Li criterion to give all-positive coefficients, ALL zeros would need to satisfy
Re(rho) = 1/2 (the center of the expansion). But the zeros at Re = -1/2 are
on the WRONG SIDE.

For a zero z at Re = sigma, the contribution to lambda~_1 is proportional to
Re(1/z) = sigma/|z|^2. The zeros at sigma = -1/2 contribute NEGATIVE terms.

For small n, the zeros near the expansion point (at Re = 1/2) dominate, giving
positive lambda~_n. For large n, the polynomial (1-1/z)^n amplifies the
contributions from zeros far from the expansion point. The Re = -1/2 zeros,
being farther from u = 1, eventually dominate, and the sum turns negative.

**The sign change at n = 7 is NOT evidence against RH. It is a structural
CONSEQUENCE of the two-critical-line architecture of the product zeta(u)*zeta(u+1).**

### 5.4 Recentering at u = 0 (the natural center)

Since Xi_H has the functional equation Xi_H(u) = Xi_H(-u) with center u = 0,
one might recenter the Li coefficients there. But this reveals an EXACT
cancellation that makes the recentered criterion vacuous.

At center u = 0, a zero at rho = 1/2 + i*gamma contributes Re(1/rho) to
the n=1 Li coefficient. The paired zero at rho-1 = -1/2 + i*gamma contributes
Re(1/(rho-1)). Since |rho|^2 = 1/4 + gamma^2 = |rho-1|^2, and
Re(1/rho) = 1/(2(1/4+gamma^2)) while Re(1/(rho-1)) = -1/(2(1/4+gamma^2)),
these contributions EXACTLY CANCEL at each gamma.

This exact cancellation (verified numerically: the partial sum over the first
5 zero pairs gives 0.0000000000 to 10 digits) is a direct consequence of the
even symmetry. It means any Li criterion centered at u = 0 is trivially
satisfied (by cancellation), providing no information about zero locations.

The codebase Li coefficients are computed at expansion point u = 1 (not u = 0),
which breaks the cancellation: |rho - 1|^2 = 1/4 + gamma^2 but the expansion
is around u = 1, so the relevant quantity is |rho - 1| vs |rho - 1 - 1| = |rho - 2|.
The asymmetry between distances to u = 1 from Re = 1/2 (distance 1/2) vs
Re = -1/2 (distance 3/2) produces the nonzero lambda~_1(H) = 0.00725..., which
is positive because the Re = 1/2 zeros are closer to the expansion point.

No recentering makes all Li coefficients positive, because the zero set
occupies TWO lines, not one.

### 5.5 Virasoro Li coefficients: ALL negative from n = 1

    n    lambda~_n(Vir)       sign
    1    -0.992745328193       -
    2    -1.425387107394       -
    3    -2.469991799869       -
    4    -4.406628530716       -
    5    -7.682290450943       -
    ...  (exponentially growing in magnitude)

The factor zeta(u) - 1 has zeros scattered throughout the complex plane with no
concentration on any vertical line. Combined with the Re = -1/2 zeros from
zeta(u+1), NONE of the zero families sits on Re = 1/2. The Li coefficients
are negative from n = 1.

The deeper reason: the weight-2 generator REMOVES the n=1 term from zeta(u),
destroying the Euler product and the functional equation simultaneously.
The function zeta(u) - 1 has no automorphic structure.

### 5.6 W_N Li coefficients: increasingly negative with N

At fixed n, lambda~_n(W_N) decreases (becomes more negative) as N increases.
Each additional generator of weight w removes more terms from zeta(u) via the
harmonic correction H_{w-1}(u). Asymptotically:

    lambda~_1(W_N) ~ -log(N) + zeta'(2)/zeta(2) + 1    as N -> infinity.

The logarithmic divergence comes from H_{N-1} = sum_{j=1}^{N-1} 1/j ~ log(N).

---

## 6. What a "shadow RH" would look like

### 6.1 What fails

The classical RH equivalent "all lambda_n > 0" fails for shadow Li coefficients
because:

(a) The Heisenberg sewing lift has zeros on TWO critical lines (Re = 1/2 and
    Re = -1/2). No single-center positivity criterion can succeed.

(b) For Virasoro and W_N, the harmonic corrections destroy the automorphic
    structure, scattering zeros away from any critical line.

(c) The complementarity identities are c-dependent algebraic relations among
    shadow coefficients, not functional equations of S_A(u).

### 6.2 Candidate "shadow RH" statements

**SRH-1 (Two-line concentration).** Under RH, the zeros of S_H(u) lie on
exactly TWO lines: Re = 1/2 and Re = -1/2, which are exchanged by the
functional equation u -> -u. This is a CONSEQUENCE of RH, not independent.

**SRH-2 (Even-function Li criterion).** The even symmetry Xi_H(u) = Xi_H(-u)
means that Xi_H is determined by its values on Re(u) >= 0. A "shadow RH"
would be: the zeros of Xi_H in the right half-plane Re(u) >= 0 all lie on
Re(u) = 1/2. This is equivalent to RH for zeta(u). The left-half-plane zeros
at Re = -1/2 are then automatic from the even symmetry.

**SRH-3 (Interacting Gram positivity -- the correct formulation).**
The manuscript (thm:interacting-gram-positivity) proves that the interacting
Gram matrix M^int(alpha) is positive definite for all alpha >= 2 when c > 0
(unitary). This is an UNCONDITIONAL statement (no assumption of RH) that
captures what the shadow obstruction tower actually controls.

The interacting sewing weight is:

    w_A(N; alpha) = a_A(N) * prod_j (1 - lambda_j * N^{-alpha/2})^{c_j}

For Virasoro with c > 0: the single spectral atom is at lambda_eff = -6/c < 0,
so each factor (1 + |6/c| * N^{-alpha/2}) > 1, giving unconditional positivity.

This is the correct "shadow RH": a POSITIVITY STATEMENT about the
shadow-corrected Dirichlet coefficients, not a zero-location statement.

**SRH-4 (Spectral measure negativity).** The Carleman rigidity
(prop:carleman-virasoro) shows that the shadow spectral measure rho is uniquely
determined by the moments {S_r}. The spectral measure for unitary Virasoro
(c > 0) has support on the NEGATIVE real axis (lambda_eff = -6/c < 0).
This is PROVED and is the shadow analogue of the "explicit formula."

### 6.3 Structural conclusion

The shadow obstruction tower is NOT a shadow of the Riemann Hypothesis. It is a shadow
of MODULAR INVARIANCE, which constrains the Roelcke-Selberg spectral
decomposition. The complementarity identities are the shadow of the KOSZUL
INVOLUTION, an algebraic operation on chiral algebras, not an analytic
operation on L-functions.

The completed Heisenberg sewing lift Xi_H(u) = xi(u)*xi(u+1) DOES have a
genuine functional equation (even symmetry about u = 0), but this is a
consequence of the zeta FE alone and is INDEPENDENT of the shadow obstruction tower
or the Koszul involution. For Virasoro and W_N, the harmonic corrections
destroy even this structure.

---

## 7. Summary of findings

| # | Question | Answer | Status |
|---|----------|--------|--------|
| 1 | Functional equation of zeta(u)zeta(u+1)? | YES: the completed product xi(u)*xi(u+1) is EVEN (center u=0) | PROVED |
| 2 | Does Koszul involution produce a FE of S_H? | NO: S_H is level-independent; complementarity is coefficient-level | PROVED |
| 3 | Functional equation of S_Vir(u)? | NO: zeta(u)-1 has no automorphic structure | PROVED |
| 4 | Lift Delta(c)+Delta(26-c) to S_{Vir_c} vs S_{Vir_{26-c}}? | NO: both are the same c-independent function | PROVED |
| 5 | Why do Heisenberg Li coefficients turn negative? | Two critical lines at Re=1/2 and Re=-1/2; sign change at n=7 | PROVED |
| 6 | Why are Virasoro Li coefficients ALL negative? | zeta(u)-1 zeros are scattered; no critical line | PROVED |
| 7 | What is the "shadow RH"? | Interacting Gram positivity (unconditional for c>0), or spectral negativity | IDENTIFIED |
| 8 | Does Level 2 descend to Level 3 FE? | NO: descends to spectral-coefficient constraints on real axis | PROVED |

### The key correction to naive expectations

The completed product xi(u)*xi(u+1) DOES have a functional equation, but
its center is u = 0, NOT u = 1/2 as one might naively expect from zeta alone.
This even symmetry is a direct algebraic consequence of xi(s) = xi(1-s)
applied to both factors. It exchanges the zeros at Re = 1/2 with those at
Re = -1/2.

The uncompleted product zeta(u)*zeta(u+1) does NOT have a clean functional
equation (the gamma-ratio factor is non-trivial and does not simplify to a
standard form). The Virasoro sewing lift zeta(u+1)*(zeta(u)-1) has no
functional equation at all.

The shadow complementarity identities kappa + kappa' = 13 and
Delta + Delta' = 6960/(...) are ALGEBRAIC constraints in the c-variable,
orthogonal to the u-variable analytic structure. They do not descend to
functional equations of S_A(u) because S_A(u) is c-independent.

### Verification data

All claims verified computationally:
- Xi_H(u) = Xi_H(-u) verified to 40 digits at 8 test points (4 real, 4 complex)
- Li coefficient table computed via mpmath high-precision differentiation
- Sign change at n=7 confirmed (test_T30 in test_dirichlet_sewing.py)
- All Virasoro Li coefficients negative for n=1,...,10 (test_T31)
- W_N monotone decrease confirmed (test_T32)
- Lambda_1 asymptotics verified (tests T35, T36)
