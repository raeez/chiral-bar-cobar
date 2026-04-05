# Level 2.5: The Mellin Bridge in the Descent Chain

## The Descent Chain

```
A  --bar-->  B(A)  --shadow-->  {S_r}  --GF-->  sqrt(Q_L)  --???-->  S_A(u)  --Mellin?-->  functional equation
```

This document analyzes the "???" step: what connects the shadow obstruction tower
generating function sqrt(Q_L) to the arithmetic Dirichlet series S_A(u),
and what role the Mellin transform plays.

## 1. The Classical Model

The prototype is the Jacobi theta function chain:

```
theta(t) = sum_{n in Z} e^{-pi*n^2*t}
     |
     | modular: theta(1/t) = sqrt(t) * theta(t)
     |
     v
xi(s) = int_0^infty (theta(t)-1)/2 * t^{s/2-1} dt = pi^{-s/2} Gamma(s/2) zeta(s)
     |
     | the Mellin transform converts the modular transformation into:
     v
xi(s) = xi(1-s)   (functional equation)
```

The key mechanism: theta(t) has a MODULAR TRANSFORMATION LAW under t -> 1/t.
The Mellin transform converts this multiplicative symmetry into a functional
equation for the completed L-function xi(s). Without the modular law, the
Mellin transform is just an integral; with it, you get the functional equation.

## 2. The Partition Function Mellin (Computation)

For Heisenberg at rank 1, the genus-1 partition function is:

```
Z_1(q) = 1/eta(q)^2
```

Setting q = e^{-t} and attempting the direct Mellin transform:

```
int_0^infty eta(e^{-t})^{-2} * t^{s-1} dt = ???
```

**This integral DIVERGES.** By the modular transformation of eta:

```
eta(e^{-t}) = sqrt(2*pi/t) * eta(e^{-4*pi^2/t})
```

As t -> 0:
```
eta(e^{-t})^{-2} ~ (t/(2*pi)) * e^{pi^2/(3t)} -> infinity  (essential singularity)
```

The exponential growth e^{pi^2/(3t)} as t -> 0+ kills the integral for all s.
Therefore:

> **The Mellin transform of the partition function Z_1(q) = eta(q)^{-2}
> does NOT exist as a function of the modular parameter t = -log(q).**

This is a fundamental difference from the theta function case, where
theta(t) - 1 decays exponentially as t -> infinity AND as t -> 0 (by the
modular transformation).

## 3. The Connected Free Energy: What DOES Work

The correct object for the Mellin transform is the CONNECTED free energy:

```
F^conn(t) := -log(eta(e^{-t})^2) = t/12 + 2*sum_{N>=1} sigma_{-1}(N) e^{-Nt}
```

where sigma_{-1}(N) = sum_{d|N} 1/d. After subtracting the linear divergence
t/12 (regularization), the Mellin transform is:

```
Mellin[F^conn_reg](s) = 2*Gamma(s) * sum sigma_{-1}(N) N^{-s}
                       = 2*Gamma(s) * zeta(s) * zeta(s+1)
```

This follows term by term from int_0^infty e^{-Nt} t^{s-1} dt = Gamma(s)/N^s,
using the Ramanujan identity sum sigma_{-1}(N) N^{-s} = zeta(s)*zeta(s+1).

**Verified numerically:**

| s | 2*Gamma(s)*zeta(s)*zeta(s+1) |
|---|------------------------------|
| 2 | 3.9546087006 |
| 3 | 5.2040564581 |
| 4 | 13.4674920129 |
| 5 | 50.6357403588 |

The critical algebraic fact: the coefficients sigma_{-1}(N) are MULTIPLICATIVE
(sigma_{-1}(mn) = sigma_{-1}(m)*sigma_{-1}(n) for gcd(m,n) = 1), which is
why the Dirichlet series factors as a product of two zeta functions. The
partition function coefficients p(N) are NOT multiplicative:

```
p(4) = 5  but  p(2)*p(2) = 4      (FAIL)
p(6) = 11 but  p(2)*p(3) = 6      (FAIL)
```

This is the algebraic reason why the logarithm (connected part) must be
taken before the Mellin transform.

## 4. The Sewing Dirichlet Series S_A(u)

The connected Dirichlet-sewing lift for a chiral algebra A with bosonic
weight multiset W(A) = {w_i} is:

```
S_A(u) = zeta(u+1) * sum_i (zeta(u) - H_{w_i-1}(u))
```

where H_n(u) = sum_{j=1}^n j^{-u} is the partial zeta sum.

Standard families:

| Family | Weights | S_A(u) |
|--------|---------|--------|
| Heisenberg | {1} | zeta(u)*zeta(u+1) |
| Virasoro | {2} | zeta(u+1)*(zeta(u) - 1) |
| beta-gamma | {1,1} | 2*zeta(u)*zeta(u+1) |
| W_N | {2,...,N} | zeta(u+1)*((N-1)*zeta(u) - sum H_j) |

The Euler defect D_A(u) := S_A(u) / (rank * zeta(u)*zeta(u+1)) measures
the departure from pure Euler-Koszul structure:

| u | D_Vir(u) = 1 - 1/zeta(u) |
|---|---------------------------|
| 2 | 0.3921 |
| 3 | 0.1681 |
| 5 | 0.0356 |
| 10 | 0.0010 |

For Heisenberg (weight 1): D = 1 identically (exact Euler-Koszul).
For Virasoro (weight 2): S_Vir = S_H - zeta(u+1), the removed weight-1 mode
appears as the defect zeta(u+1).

## 5. The Rankin-Selberg Integral: The Correct "Mellin"

The correct analogue of the classical theta-Mellin is NOT a direct Mellin
transform but the **Rankin-Selberg integral** of the primary-counting
function against the real-analytic Eisenstein series:

```
I(s) := int_{SL(2,Z)\H} Z-hat^c(tau) * E_s(tau) d*mu(tau)
```

where Z-hat^c = y^{c/2} |eta|^{2c} Z is the primary-counting function
(strips descendants by the |eta|^{2c} factor).

The Rankin-Selberg unfolding reduces this to a Mellin integral:

```
I(s) = int_0^infty a_0(y) y^{s-2} dy
```

where a_0(y) = int_0^1 Z-hat^c(x+iy) dx is the zeroth Fourier mode.

For the Heisenberg sewing free energy, the sewing-Selberg formula gives:

```
int_{M_{1,1}} F^conn * E_s d*mu = 2*(2*pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)
```

**Verified:**

| s | RS(s) | S_H(s-1) | RS/S_H = 2*(2pi)^{-(s-1)}*Gamma(s-1) |
|---|-------|----------|--------------------------------------|
| 3 | 0.10017 | 1.97730 | 0.05066 |
| 4 | 0.02098 | 1.30101 | 0.01613 |
| 5 | 0.00864 | 1.12229 | 0.00770 |
| 6 | 0.00517 | 1.05491 | 0.00490 |

The relation is:

```
RS(s) = 2*(2*pi)^{-(s-1)} * Gamma(s-1) * S_H(s-1)
```

The factor 2*(2*pi)^{-(s-1)} * Gamma(s-1) is the ARCHIMEDEAN COMPLETION --
the Gamma factor that converts the finite Dirichlet series into the
completed L-function with its functional equation.

## 6. Four Variables and Their Relationships

The descent chain involves FOUR independent complex variables:

| Variable | Object | Domain | Role |
|----------|--------|--------|------|
| t | G_A(t) = sum S_r t^r | formal disk near 0 | arity |
| q | F^conn(q) = sum a_N q^N | unit disk \|q\|<1 | modular |
| u | S_A(u) = sum a_N N^{-u} | Re(u) > 1 | prime |
| s | RS(s) = int...E_s d*mu | all C | spectral |

### Bridge q -> u (standard Mellin)

```
int_0^infty (sum a_N e^{-Nt}) t^{u-1} dt = Gamma(u) * sum a_N N^{-u} = Gamma(u) * S_A(u)
```

This is the STANDARD Mellin transform. The substitution t = -log(q) converts
the q-expansion into a Laplace-type integral, and the Mellin transform
extracts the Dirichlet series.

### Bridge q -> s (Rankin-Selberg)

```
int_{M_{1,1}} F^conn * E_s d*mu = archimedean_factor * S_A(s-1)
```

This is the RS integral. The unfolding procedure replaces integration
over the modular surface by a Mellin integral of the zeroth Fourier mode,
producing the completed L-function.

### Bridge u -> s (shift + completion)

```
RS(s) = 2*(2*pi)^{-(s-1)} * Gamma(s-1) * S_A(s-1)
```

Simply a shift s -> s-1 plus multiplication by the archimedean factor.

### Bridge t -> u: THE GAP

**There is no direct transform from the shadow GF variable t to the
Dirichlet series variable u.** The connection requires the GRAPH SUM
as an irreducible intermediate step:

```
G_A(t) --[graph sum at genus g]--> F_g(q) --[Mellin]--> contribution to S_A(u)
```

The graph sum integrates the shadow couplings S_r against the Schottky
data of the curve. At genus g, arity r, one sums over all connected
graphs with g loops and r vertices, with edge integrals involving the
prime form E(z,w) on the algebraic curve.

## 7. The Shadow Generating Function: A Different Kind of Mellin

The formal Mellin transform of G_A(t) = sum S_r t^r gives:

```
L_A^{formal}(s) = int_0^1 G_A(t) t^{s-1} dt = sum_r S_r/(s+r)
```

This is a meromorphic function with simple poles at s = -r (r = 2, 3, 4, ...)
with residues S_r. For the four archetype classes:

| Class | Depth | Poles | Nature |
|-------|-------|-------|--------|
| G (Heisenberg) | 2 | s = -2 | single pole |
| L (affine) | 3 | s = -2, -3 | two poles |
| C (beta-gamma) | 4 | s = -2, -3, -4 | three poles |
| M (Virasoro) | infinity | s = -2, -3, -4, ... | infinitely many |

For class M, the closed form is the Mellin transform of t^2*sqrt(Q_L(t))
where Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S_4)*t^2.
The branch cut of sqrt(Q_L) at the complex zeros of Q_L produces a branch
cut in L_A^{formal}(s) -- this is the analytic reflection of the infinite
shadow depth.

**This L-function encodes the A-infinity homotopy data, NOT the arithmetic.**
Its poles are at negative integers (the arity values), not related to
prime numbers or zeta zeros. It is the Mellin-domain avatar of the
shadow obstruction tower's ALGEBRAIC structure.

## 8. Why sqrt(Q_L) Cannot Directly See Zeta Zeros

The shadow generating function sqrt(Q_L(t)) is:
- A Taylor series in the arity variable t (algebraic, from OPE data)
- Determined by three genus-0 invariants (kappa, alpha, S_4)
- An ALGEBRAIC function of degree 2 (square root of a quadratic)

The theta function theta(t) is:
- A function of the MODULAR variable t (analytic, from lattice data)
- Satisfying a modular transformation law theta(1/t) = sqrt(t)*theta(t)
- A TRANSCENDENTAL function (product over integers)

The modular transformation law is what converts the Mellin transform into
a functional equation, and the functional equation is what locates the
zeros on a critical line. sqrt(Q_L) has NO modular transformation law --
the arity variable t has no analogue of t -> 1/t. Therefore:

> **The formal Mellin transform of sqrt(Q_L) does not produce a functional
> equation and cannot directly access zeta zeros.**

This is not a limitation of the shadow obstruction tower; it is a CATEGORY ERROR.
The shadow obstruction tower encodes the OPE complexity of A (the homotopy-theoretic
axis), not the modular arithmetic (the number-theoretic axis).

## 9. The Correct Bridge: Graph Sum as Convolution

The missing step is the GRAPH SUM, which converts arity data into modular data.

**Important distinction.** There are two genus-1 objects that must not be
conflated:

1. **F^conn(tau)** = -2*kappa * log eta(tau) (for Heisenberg): a FUNCTION on
   the upper half plane H, before integration over the moduli space.
   This is the input to the Rankin-Selberg integral.

2. **F_1** = kappa * int_{Mbar_1} lambda_1 = kappa/24: a NUMBER, the result
   of integrating the leading tautological class over Mbar_1. This is the
   genus-1 shadow partition function (Theorem D).

The relationship: F^conn(tau) is the genus-1 graph-sum amplitude as a
function of the curve E_tau; F_1 is a derived invariant obtained by
integrating a specific component of F^conn against the modular measure.

At genus 1, for a modular Koszul algebra A, the graph-sum amplitude is:

```
F^{graph}_1(A, tau) = sum_{r>=2} sum_{Gamma: connected, g(Gamma)=1, |V(Gamma)|=r}
                      (1/|Aut(Gamma)|) * prod_{v} S_{val(v)} * prod_{e} P_e(tau)
```

where P_e(tau) is the edge propagator (the Green's function / Bergman kernel
on E_tau). The edge integrals depend on tau through the prime form E(z,w):

```
P_e(tau) = int_{E_tau x E_tau} d_z d_w log E(z,w) * (vertex insertions)
```

This is an AUTOMORPHIC object (it transforms modularly in tau). The graph
sum converts the shadow couplings S_r (algebraic, arity data) into a function
of tau (modular, arithmetic data) by integrating against the modular geometry.

The tautological shadow contribution at arity 2 gives:

```
F_1 = kappa(A) * lambda_1^FP = kappa(A)/24
```

a topological constant. The q-dependent part of F^conn(tau) comes from the
full character formula, which for Heisenberg is:

```
F^conn(tau) = -2 * log eta(tau) = tau/12 + 2*sum sigma_{-1}(N) q^N
```

The Mellin transform of this q-expansion (the connected free energy as a
function of tau, not the number F_1) produces S_A(u).

## 10. The Constrained Epstein: A Third Object

The constrained Epstein zeta epsilon^c_s(A) = sum_{Delta in S} (2*Delta)^{-s}
is a THIRD Dirichlet series, distinct from both S_A(u) and the formal
shadow Mellin. It sums over SCALAR PRIMARIES (bar cohomology generators),
not over sewing mode levels.

For rank-1 Narain at self-dual radius:

```
epsilon^1_s(R=1) = 4*zeta(2s)
```

The relationship to S_H is:

```
S_H(u) = zeta(u)*zeta(u+1)   (sums over mode levels with sigma_{-1} weights)
epsilon^1_s = 4*zeta(2s)       (sums over primary dimensions n^2/2)
```

These involve different arithmetic functions (sigma_{-1}(N) vs constant 4)
over different index sets (positive integers N vs squares n^2/2). They are
connected by the Rankin-Selberg transform:

```
int_{M_{1,1}} Z-hat^1 * E_s d*mu = (archimedean) * epsilon^1_s + (Maass spectrum)
```

The epsilon^c_s carries the zeta zeros through the functional equation factor
zeta(2s)/zeta(2s-1), but the structural obstruction (Proposition
prop:scattering-residue in arithmetic_shadows.tex) shows that the
RS unfolding ERASES the scattering matrix from the integral, making the
zeta-zero information inaccessible to algebraic constraints on Z-hat^c.

## 11. Summary: The Two Mellin Transforms

The descent chain contains TWO fundamentally different Mellin transforms:

### Mellin 1: Shadow -> A-infinity L-function (algebraic axis)

```
G_A(t) = sum S_r t^r  --Mellin-->  L_A^{formal}(s) = sum S_r/(s+r)
```

- Encodes: A-infinity homotopy structure of bar cohomology
- Poles: at s = -r (negative integers), residues = shadow coefficients
- Branch cut: from sqrt(Q_L), at complex zeros of Q_L
- Functional equation: NONE (no modular law for the arity variable)
- Connection to zeta: NONE (different axis entirely)

### Mellin 2: q-expansion -> arithmetic L-function (modular axis)

```
F^conn(q) = sum a_N q^N  --Mellin-->  S_A(u) = sum a_N N^{-u}
```

- Encodes: arithmetic structure of the partition function
- Poles: at u = 1 (from zeta(u)) and u = 0 (from zeta(u+1))
- Euler product: iff all weights = 1 (Euler-Koszul exact)
- Functional equation: inherited from modular invariance of Z via RS
- Connection to zeta: yes, through the Eisenstein spectral decomposition

### The Irreducible Bridge

The connection from Mellin 1 to Mellin 2 is the GRAPH SUM:

```
{S_r}  --[graph sum over genus-g graphs]--> {a_N(g)}  --[Mellin]--> S_A^{(g)}(u)
```

This is not a simple integral transform. It requires:
1. Enumerating all connected graphs at each genus and arity
2. Computing edge integrals (prime form) on the algebraic curve
3. Summing with the automorphism-weighted shadow couplings
4. Integrating over the moduli space M_g (for the Rankin-Selberg version)

The graph sum is the mechanism that converts ALGEBRAIC data (the OPE,
encoded in the shadow obstruction tower) into ARITHMETIC data (the q-expansion,
which sees prime numbers through its Fourier coefficients).

## 12. Honest Assessment

The descent chain question "does sqrt(Q_L) produce S_A(u) via Mellin?"
has a definitive negative answer: NO, not directly. The arity variable t
and the modular variable q live in fundamentally different spaces, and
no integral transform connects them without the graph-sum intermediary.

What IS true:
- The shadow obstruction tower sqrt(Q_L) determines the OPE couplings S_r
- The OPE couplings, via graph sums, determine the genus-g free energies F_g(q)
- The Mellin transform of F_g(q) produces S_A(u)
- The Rankin-Selberg integral of F_g against E_s produces the completed L-function
- The manuscript's eight-step chain in arithmetic_shadows.tex (sec:sewing-RS-bridge)
  correctly identifies each step and does not conflate them

What is OPEN:
- Whether the MC equation on the shadow obstruction tower constrains the resulting
  L-functions beyond what the character data alone provides (the quartic
  shadow Q^contact is the first interacting correction beyond character level)
- Whether the structural obstruction (RS unfolding erasing the scattering
  matrix) can be circumvented at higher genus (Gap P1-P3 in arithmetic_shadows.tex)

---

*Computed 2026-04-01. All numerical values verified to 10+ digits using
mpmath at 30-digit precision. Algebraic identities verified symbolically.*
