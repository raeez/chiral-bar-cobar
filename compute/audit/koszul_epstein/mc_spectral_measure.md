# MC Equation, Spectral Measure, and the Koszul-Epstein Function

## Deep Analysis: How the MC equation constrains the spectral measure

**Date**: 2026-04-01
**Status**: Falsification-first analysis per Beilinson Principle

---

## 1. The Mathematical Setup

### 1.1 The shadow obstruction tower as an algebraic function

The shadow Postnikov tower on a one-dimensional primary slice L produces
coefficients S_r (r >= 2) determined by the MC equation. The key theorem
(thm:riccati-algebraicity, higher_genus_modular_koszul.tex line 14827) is:

**Theorem.** The weighted shadow generating function H(t) = sum_{r>=2} r S_r t^r
satisfies H(t)^2 = t^4 Q_L(t), hence H(t) = t^2 sqrt(Q_L(t)), where

    Q_L(t) = 4 kappa^2 + 12 kappa alpha t + (9 alpha^2 + 16 kappa S_4) t^2

is a quadratic polynomial determined by three genus-0 invariants (kappa, alpha, S_4).

The shadow coefficients are therefore the Taylor coefficients:

    S_r = (1/r) [t^{r-2}] sqrt(Q_L(t))

This is PROVED. The MC equation forces the recursion (eq:single-line-inversion):

    S_r = -(P/2r) sum_{j+k=r+2, 3<=j<=k} c_{jk} jk S_j S_k

which is equivalent to F(t)^2 = Q_L(t) where F(t) = H(t)/t^2.

### 1.2 The constrained Epstein zeta

For a VOA A with scalar primary spectrum {Delta_i} (with multiplicity), the
constrained Epstein zeta is:

    epsilon^c_s(A) = sum_{Delta in Spec(A)} (2 Delta)^{-s}

For lattice VOAs V_Lambda, this factors via Hecke theory:

    epsilon^r_s(V_Lambda) = 2^{-s} (c_E C_E(s) zeta(s) zeta(s - r/2 + 1)
                           + sum_j c_j C_j(s) L(s, f_j))

(thm:shadow-spectral-correspondence, arithmetic_shadows.tex line 100).

### 1.3 The sewing Dirichlet lift

The sewing Dirichlet lift S_A(u) = zeta(u+1) sum_i (zeta(u) - H_{w_i-1}(u))
encodes the weight multiset W(A) = {w_i} of generating fields.

---

## 2. Making the "Moment Interpretation" Precise

### 2.1 The claim from rn105

> "MC equation at each arity gives a moment constraint on the spectral measure;
> for Gaussian class (V_Z), the moment is determined by kappa alone."

**Falsification analysis**: This claim requires disambiguation. There are TWO
distinct objects called "spectral" in the manuscript:

(A) The **shadow-Epstein spectral decomposition**: the Roelcke-Selberg
decomposition of the primary-counting function Z-hat^c on M_{1,1} into
Eisenstein continuous spectrum + Maass discrete spectrum + holomorphic forms.
Here the "spectral measure" is the spectral density c(t) on the real
spectral line Re(s) = 1/2, s = 1/2 + it.

(B) The **shadow obstruction tower as moments of an algebraic function**: the Taylor
coefficients S_r = (1/r)[t^{r-2}] sqrt(Q_L) viewed as "moments" of
some measure.

**These are DIFFERENT objects.** The shadow coefficients S_r are determined
by (kappa, alpha, S_4) alone -- three numbers. The spectral measure in
sense (A) is an infinite-dimensional object (a function c(t) on R). The
shadow obstruction tower constrains the spectral decomposition only INDIRECTLY, through
the Rankin-Selberg integral that connects the shadow-generating data to
the spectral coefficients.

### 2.2 The precise moment interpretation

The shadow generating function H(t) = t^2 sqrt(Q_L(t)) is algebraic of
degree 2. Write F(t) = sqrt(Q_L(t)) with Q_L(t) = q_0 + q_1 t + q_2 t^2.
Then:

    F(t) = sqrt(q_0) (1 + (q_1/(2q_0)) t + ((4q_0 q_2 - q_1^2)/(8q_0^2)) t^2 + ...)

The Taylor coefficients a_n = [t^n] F(t) satisfy the recursion from
F^2 = Q_L, which forces a_n for n >= 3 to vanish (the convolution
sum_{i+j=n} a_i a_j = 0 for n >= 3). This is equivalent to the MC
equation.

**Can these be moments?** Define the "shadow measure" formally as
the distribution mu_sh on R such that:

    S_r = integral x^{r-2} d mu_sh(x)

for r >= 2. Then S_2 = mu_sh(R) = kappa, S_3 = integral x d mu_sh(x) = alpha,
S_4 = integral x^2 d mu_sh(x), etc.

**CRITICAL POINT**: For class M (infinite tower), the S_r grow as
rho^r r^{-5/2} (thm:shadow-radius). This means:

    |S_r| ~ A rho^r r^{-5/2}

So the "moments" grow exponentially when rho > 0. A measure with
exponentially growing moments is supported on an UNBOUNDED set, or
more precisely, the moment-generating function has finite radius
of convergence 1/rho.

But this is EXACTLY the statement that F(t) = sqrt(Q_L(t)) has
branch points at distance 1/rho from the origin. The "measure"
is the jump of the square root across the branch cut.

### 2.3 The Stieltjes-Perron representation

For the ALGEBRAIC function F(t) = sqrt(Q_L(t)) with Q_L quadratic,
the branch cut connects the two zeros t_+, t_- of Q_L. The
Stieltjes-Perron inversion formula gives:

    F(t) = F(0) + (1/(2 pi i)) integral_{t_-}^{t_+} disc(F)(s) / (s - t) ds

where disc(F)(s) = F(s + i0) - F(s - i0) = 2i sqrt(|Q_L(s)|) for s
on the branch cut (where Q_L(s) < 0).

**THEOREM (precise moment interpretation):**
*The shadow coefficients S_r are the moments of the signed spectral
density*

    d mu_sh(x) = (1/(pi)) Im(sqrt(Q_L(x + i0))) dx

*supported on the arc/interval between the branch points t_+, t_-
of Q_L in the complex plane.*

**Proof.** By Cauchy's integral formula, [t^n] F(t) = (1/(2pi i))
oint F(z)/z^{n+1} dz. Deforming the contour to wrap around the branch
cut gives [t^n] F(t) = (1/(2pi i)) integral disc(F)(s) / s^{n+1} ds.
Since S_r = (1/r)[t^{r-2}]F(t), this gives S_r as a moment of the
spectral weight function on the cut. QED.

**For class G/L (Delta = 0):** Q_L is a perfect square, the branch
points coalesce, the cut degenerates, and the "measure" is a point
mass. The tower terminates.

**For class M (Delta != 0, complex branch points):** The "measure" is
supported on an arc in the complex plane (not the real line). This is
a COMPLEX measure, not a positive measure. The moments S_r are therefore
real but the support is complex.

---

## 3. The Hamburger Moment Problem and Carleman's Condition

### 3.1 Statement of the problem

The Hamburger moment problem asks: given a sequence of real numbers
{m_r}_{r=0}^{infty}, does there exist a positive Borel measure mu on R
such that m_r = integral x^r d mu(x)?

The Carleman condition for uniqueness:

    sum_{r=1}^{infty} m_{2r}^{-1/(2r)} = infty

implies the measure (if it exists) is UNIQUE.

### 3.2 Application to the shadow obstruction tower

**FALSIFICATION: The Hamburger framework is the WRONG framework.**

The shadow coefficients S_r do NOT satisfy the hypotheses of the
Hamburger moment problem for three independent reasons:

**(i) The shadow "measure" is COMPLEX, not positive.**
For class M with Delta > 0 (the generic case), the branch points
of sqrt(Q_L) are complex conjugate. The spectral density on the
branch cut is therefore a complex-valued function on an arc in C.
The moments S_r are real (because the complex branch points are
conjugate), but the underlying "measure" is not positive on R.

The Hamburger theorem requires a POSITIVE measure on R. The
Stieltjes transform requires positivity on R_+. Neither applies.

**(ii) The tower is ALREADY determined -- uniqueness is trivial.**
The shadow obstruction tower is determined by three numbers (kappa, alpha, S_4).
The "moment problem" is solved by construction: the unique
"measure" is the spectral density of sqrt(Q_L) on the branch cut.
There is no indeterminacy to resolve.

The question "does a unique measure exist?" is vacuous: we HAVE
the algebraic function, we HAVE its Taylor coefficients, we HAVE
the spectral density. The "moment problem" is answered by the
Riccati algebraicity theorem itself.

**(iii) Carleman's condition is satisfied trivially when the answer is
already known.**
Nevertheless, let us check: |S_r| ~ A rho^r r^{-5/2}.

    S_{2r}^{-1/(2r)} ~ (A rho^{2r} (2r)^{-5/2})^{-1/(2r)}
                      = A^{-1/(2r)} rho^{-1} (2r)^{5/(4r)}

As r -> infinity: A^{-1/(2r)} -> 1, (2r)^{5/(4r)} -> 1, so
S_{2r}^{-1/(2r)} -> rho^{-1} > 0 (for rho finite and nonzero).

Therefore:

    sum S_{2r}^{-1/(2r)} ~ sum rho^{-1} = infty (diverges)

**The Carleman condition IS satisfied.** But this is vacuous:
we already know the generating function is algebraic of degree 2.
The Carleman condition merely confirms that the exponential growth
rate rho^r r^{-5/2} is slow enough that the moments determine the
measure -- which is a tautology when the measure is known to be
the spectral density of a quadratic algebraic function.

### 3.3 What about the Stieltjes case?

For Delta < 0 (rare, requires S_4 < 0), the branch points are REAL.
The spectral density is then a POSITIVE measure on a real interval
[t_-, t_+]. In this case the Stieltjes moment problem has a positive
answer, Carleman is satisfied, and the measure is unique.

But this case is non-generic and does not occur for the Virasoro
algebra (where Delta = 80/(5c+22) > 0 for c > 0, c != -22/5).

---

## 4. Does the MC-determined spectrum force zeta zeros onto the critical line?

### 4.1 The structural separation

The manuscript's structural obstruction (rem:structural-obstruction,
arithmetic_shadows.tex line 300) identifies the GAP precisely:

> The shadow obstruction tower and the MC equation constrain the spectral
> coefficients c(t) on the REAL t-axis; the zeta zeros live at
> COMPLEX spectral parameters. This separation is structural:
> algebraic constraints on the spectral line cannot reach the
> scattering poles without analytic continuation of the spectral
> data off the real axis.

**This is CORRECT and PROVED.** The argument:

(1) The Roelcke-Selberg spectral decomposition of Z-hat^c decomposes
it into Eisenstein E_s(tau) (continuous, s = 1/2 + it, t real) and
discrete Maass forms. The spectral coefficients c(t) are determined
by inner products on M_{1,1}.

(2) The scattering matrix phi(s) = Lambda(1-s)/Lambda(s) has poles at
s = rho/2 where rho are nontrivial zeros of zeta. For t real,
phi(1/2 + it) is regular. The poles are at COMPLEX values of t.

(3) The MC equation, through the shadow obstruction tower, constrains the spectral
coefficients c(t) for REAL t. This gives infinitely many moment
constraints on the continuous-spectrum side, but these constraints
live on the wrong contour to see the zeta zeros.

### 4.2 Quantitative verification

The Li coefficient computation (li_criterion_deep.py) provides
direct evidence:

**FACT (computed):** The modified Li coefficients lambda-tilde_n(H)
for the Heisenberg sewing lift S_H(u) = zeta(u) zeta(u+1) are
positive for n = 1,...,6 and NEGATIVE at n = 7.

This means: the Taylor expansion of log Xi_A(1/(1-w)) has
coefficients of alternating sign. The derivative-formula Li
coefficients are NOT the same as the zero-sum Li coefficients
(li_criterion_deep.py lines 13-39 document this precisely).

**The Hadamard gap:** For the classical Riemann xi function
xi(s) = (s-1) pi^{-s/2} Gamma(s/2) zeta(s), the Li-Keiper
coefficients are lambda_n = sum_rho [1 - (1 - 1/rho)^n] where
the sum is over nontrivial zeros. RH is equivalent to lambda_n > 0
for all n.

For the sewing lift Xi_A(u) = (u-1) S_A(u), this Hadamard product
structure is ABSENT. Xi_A has poles (from zeta(u+1)), making the
Hadamard representation involve exponential factors that shift the
Taylor coefficients relative to the zero-sum formula. The derivative
formula and the zero-sum formula DISAGREE (li_criterion_deep.py
lines 24-31 prove this numerically: lambda-tilde^{red}_1 = 0.577 =
Euler-Mascheroni gamma, while the classical lambda_1 = 0.021).

### 4.3 The fundamental obstruction

**Why the gap cannot be closed by any shadow-tower mechanism:**

(A) **Finite determination.** The shadow obstruction tower on ANY single primary
line is determined by THREE numbers (kappa, alpha, S_4). The
constrained Epstein zeta epsilon^c_s(A) involves INFINITELY many
independent primary dimensions {Delta_i}. Three constraints cannot
determine infinitely many unknowns.

(B) **Class M does not help.** For Virasoro (class M, infinite tower),
the shadow coefficients S_r for r >= 5 are ALL determined by
(kappa, alpha, S_4). The infinite tower provides no ADDITIONAL
constraints beyond the three initial invariants. This is the content
of thm:riccati-algebraicity: F^2 = Q_L forces all higher Taylor
coefficients to vanish, so S_r for r >= 5 is a CONSEQUENCE of
S_2, S_3, S_4.

(C) **Multi-line data.** On a multi-dimensional primary space (e.g.,
W_3 with T and W lines), the shadow metric Q_L(t) depends on the
choice of line. The full data includes the propagator variance
delta_mix (thm:propagator-variance). But this is still a FINITE
amount of data (the quadratic form on the primary space), while the
spectrum is infinite-dimensional.

(D) **Real vs complex separation.** Even if the shadow obstruction tower gave
infinitely many INDEPENDENT constraints (it does not, by (A)-(B)),
these constraints are on the SPECTRAL COEFFICIENTS c(t) for real t.
The zeta zeros are at COMPLEX t. The Rankin-Selberg transform that
connects them is an integral transform -- it is NOT sign-preserving.
A positivity constraint on c(t) does not imply a positivity
constraint on the zero sum.

### 4.4 The Narain universality theorem as a proof of impossibility

The Narain universality theorem (thm:narain-universality,
arithmetic_shadows.tex line 333) provides a concrete demonstration:

    epsilon^1_s(R) = 2(R^{2s} + R^{-2s}) zeta(2s)

The zeros of epsilon^1_s are EXACTLY the zeros of zeta(2s),
independent of the compactification radius R. The Koszul self-duality
R <-> 1/R preserves epsilon^1_s identically. The shadow obstruction tower data
(kappa, alpha, S_4 for V_Z at various radii) does NOT change the
zero locations. The MC equation constraints are satisfied for ALL R,
and the zeta zeros are unchanged for ALL R.

**This is a no-go result:** the MC equation admits a continuous
family of solutions (parametrized by R) ALL having the same zeta
zeros. The zeros are not determined by the MC data.

---

## 5. What the Shadow Tower DOES Determine

### 5.1 For lattice VOAs (the positive result)

The shadow-spectral correspondence (thm:shadow-spectral-correspondence)
IS a theorem: for lattice VOAs, the shadow depth counts the number of
independent L-functions in the Hecke factorization of the Epstein zeta.
This is the CORRECT relationship between the shadow obstruction tower and the
spectrum:

| Arity | Shadow       | Arithmetic object        | L-function           |
|-------|-------------|--------------------------|----------------------|
| 2     | kappa       | total spectral weight    | zeta(s)              |
| 3     | alpha       | Eisenstein structure     | zeta(s) zeta(s-k+1)  |
| 3+j   | Sh_{3+j}    | j-th cusp eigenform f_j  | L(s, f_j)            |

The shadow obstruction tower COUNTS the L-functions; it does not CONTROL their zeros.

### 5.2 The depth decomposition (the structural theorem)

The depth decomposition d(A) = 1 + d_arith(A) + d_alg(A)
(thm:depth-decomposition) separates arithmetic content
(L-functions) from homotopy-theoretic content (A-infinity
non-formality). This is proved and structurally illuminating.

### 5.3 The shadow-Epstein zeta (a secondary construction)

The shadow-Epstein zeta Z_sh(s, c) := sum_{r>=2} |S_r(c)|^2 r^{-s}
(constr:shadow-epstein-eisenstein, arithmetic_shadows.tex line 1884)
is a Dirichlet series in the shadow coefficients themselves (not
the primary dimensions). Its analytic properties inherit from the
shadow growth rate:

- rho < 1: Z_sh entire
- rho = 1: Z_sh converges for Re(s) > -3/2
- rho > 1: Z_sh diverges

This is a DISTINCT object from the constrained Epstein zeta
epsilon^c_s(A). The shadow-Epstein zeta is determined by
(kappa, alpha, S_4); the constrained Epstein zeta depends on the
full spectrum.

---

## 6. The Precise Answer to Each Question

### Q1: "What is the spectral measure mu?"

The spectral measure associated to the shadow obstruction tower is the
Stieltjes-Perron spectral density of the algebraic function
sqrt(Q_L(t)):

    d mu_sh(x) = (1/pi) Im(sqrt(Q_L(x + i0))) dx

supported on the branch cut of Q_L in the complex t-plane.
For class M with Delta > 0, this is a COMPLEX measure on a
complex arc. For the rare case Delta < 0, it is a positive
measure on a real interval.

This measure is COMPLETELY DETERMINED by (kappa, alpha, S_4).
It has nothing to do with the primary spectrum {Delta_i} of the VOA.

### Q2: "Does the shadow obstruction tower satisfy the Carleman condition?"

YES, trivially. |S_r| ~ A rho^r r^{-5/2} gives
sum S_{2r}^{-1/(2r)} ~ sum rho^{-1} = infty. But this is vacuous:
the generating function is algebraic of degree 2, so the "moment
problem" has an explicit solution.

### Q3: "Does the MC equation determine the spectrum?"

NO. The MC equation determines three invariants (kappa, alpha, S_4)
on each primary line. The full spectrum {Delta_i} is an
infinite-dimensional object that the shadow obstruction tower does not control.
Even the infinite tower (class M) is determined by these three numbers.

### Q4: "Does the MC-determined spectrum force zeta zeros onto the critical line?"

NO. This is proved by:
(a) Structural separation: MC constraints act on real spectral
parameters; zeta zeros are at complex spectral parameters
(rem:structural-obstruction).
(b) Narain universality: a continuous family of MC solutions all
have the same zeta zeros (thm:narain-universality).
(c) Li coefficient failure: the derivative-formula Li coefficients
are eventually negative for ALL families (prop:li-criterion-failure).
(d) Finite determination: three invariants cannot constrain infinitely
many zeros.

### Q5: "Can the gap be closed?"

The gap CANNOT be closed by shadow-tower methods alone. The
manuscript states this correctly (arithmetic_shadows.tex line 2656):

> "The claim that these two facts are levels of a 'descent chain'
> that continues to L-functions and the Riemann hypothesis is false."

The structural obstruction (rem:structural-obstruction) is a THEOREM,
not a conjecture. The algebraic constraints from the MC equation act
on the real spectral line. The zeta zeros live at complex spectral
parameters. No amount of shadow obstruction tower data can bridge this gap
because:

1. The shadow obstruction tower is finitely determined (3 invariants).
2. The Rankin-Selberg transform is not sign-preserving.
3. The Li criterion does not apply to the sewing lift (Hadamard gap).

---

## 7. Summary of Falsification Results

| Claim from rn105                                          | Status      |
|-----------------------------------------------------------|-------------|
| "MC equation gives moment constraints on spectral measure" | IMPRECISE   |
| "For Gaussian class, moment determined by kappa alone"     | TRUE but trivial |
| Hamburger moment problem applies to shadow obstruction tower           | FALSE (complex measure) |
| Carleman condition satisfied                               | TRUE but vacuous |
| Shadow obstruction tower determines spectrum                           | FALSE (3 invariants vs infinity) |
| MC-determined spectrum forces critical-line zeros           | FALSE (structural obstruction) |
| The gap can be closed                                      | FALSE (proved no-go) |

**The manuscript's own analysis is CORRECT**: the bar construction
detects arithmetic (proved) but does not control it (proved impossible).
The working_notes passage (lines 2650-2690) is an honest and accurate
assessment. The rn105 claim about "moment constraints" is a suggestive
but misleading formulation of a relationship that is real (the shadow-
spectral correspondence) but limited (to counting L-functions, not
controlling their zeros).

---

## References to manuscript source

- thm:riccati-algebraicity: higher_genus_modular_koszul.tex line 14827
- thm:shadow-spectral-correspondence: arithmetic_shadows.tex line 100
- rem:structural-obstruction: arithmetic_shadows.tex line 300
- thm:narain-universality: arithmetic_shadows.tex line 333
- thm:depth-decomposition: arithmetic_shadows.tex line 1326
- thm:shadow-radius: higher_genus_modular_koszul.tex (via shadow_radius.py)
- prop:li-criterion-failure: li_criterion_deep.py (adversarial analysis)
- constr:shadow-epstein-eisenstein: arithmetic_shadows.tex line 1884
- working_notes.tex lines 2565-2690 (structural obstruction section)
