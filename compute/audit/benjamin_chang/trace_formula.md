# Is epsilon^c_s the Spectral Side of a Trace Formula?

## Date: 2026-04-01
## Status: Falsification-first analysis per Beilinson Principle

---

## 0. Executive Summary

**The answer is: almost, but the analogy is structurally misleading at the
decisive point.** The Roelcke-Selberg decomposition of the partition function
on M_{1,1} is indeed a spectral decomposition of a trace, and it produces
epsilon^c_s as the Eisenstein spectral coefficient. But the analogy to the
Selberg trace formula breaks at three critical junctures:

1. The "geometric side" of the Selberg trace formula involves CLOSED GEODESICS
   (conjugacy classes in SL(2,Z)). The bar complex involves COLLISION
   CONFIGURATIONS (strata of FM_n(X)). These are different geometric objects:
   geodesics on the modular surface vs compactification strata of configuration
   spaces on the curve.

2. The Selberg trace formula equates a sum over EIGENVALUES (spectral) to a sum
   over CONJUGACY CLASSES (geometric). The sewing-shadow intertwining equates a
   sum over PRIMARY DIMENSIONS (spectral) to a sum over GRAPH AMPLITUDES
   (combinatorial). The graph amplitudes are not orbital integrals.

3. The MC equation D^2 = 0 is a constraint on the BAR COMPLEX (a coalgebra
   structure), not on the HEAT KERNEL of the Laplacian on the modular surface.
   The Selberg trace formula derives from the heat kernel. The MC equation
   derives from the boundary structure of FM compactifications.

The precise mathematical content is this: there exists a chain

    Bar complex --> Shadow obstruction tower --> Sewing determinant --> Roelcke-Selberg

in which each arrow is a proved theorem (thm:mc2-bar-intrinsic,
thm:sewing-shadow-intertwining, prop:sewing-trace-formula,
thm:sewing-selberg-formula). This chain connects OPE collision data to
spectral data. But calling this a "trace formula" imposes a false structural
parallel with Selberg/Arthur-Selberg that obscures both what is proved and
what is structurally impossible.

---

## 1. The Mathematical Objects

### 1.1. The Selberg trace formula (classical)

For PSL(2,Z)\H with test function h:

    Sigma_j h(r_j)  =  (area/4pi) int h(r) r tanh(pi r) dr     [identity]
                      + Sigma_{gamma hyp} log N(gamma_0)/(N(gamma)^{1/2}-N(gamma)^{-1/2}) g(log N(gamma))  [hyperbolic]
                      + (elliptic + parabolic terms)

**Spectral side**: Sum over eigenvalues r_j of the Laplacian on L^2(PSL(2,Z)\H).
These are the Maass eigenvalues: Delta u_j = (1/4 + r_j^2) u_j.

**Geometric side**: Sum over conjugacy classes of PSL(2,Z), classified as
{identity, hyperbolic, elliptic, parabolic}. Each class contributes an
"orbital integral" -- the integral of the test function's Fourier transform
evaluated at the displacement of the conjugacy class.

**Key structural feature**: The trace formula is an IDENTITY, valid for ALL
test functions h in a suitable class. It is not a constraint on h; it is a
duality between two representations of the SAME operator trace.

### 1.2. The VOA partition function as a trace

For a VOA V at central charge c:

    Z_V(tau, tau_bar) = Tr_V(q^{L_0 - c/24} q_bar^{L_0_bar - c/24})

This is literally a TRACE over the state space V. For a holomorphic VOA
(V_bar = 0): Z(tau) = Tr_V(q^{L_0 - c/24}).

The primary-counting function Z-hat^c = y^{c/2} |eta|^{2c} Z strips
descendants and retains only primary content.

### 1.3. The constrained Epstein zeta epsilon^c_s

**Definition** (Benjamin-Chang 2022, arXiv:2208.02259):

    epsilon^c_s = Sigma_{Delta in Spec(V)} (2 Delta)^{-s}

where Spec(V) is the multiset of scalar primary dimensions.

**Identification**: epsilon^c_s is the Eisenstein spectral coefficient
of Z-hat^c in the Roelcke-Selberg decomposition of L^2(SL(2,Z)\H):

    Z-hat^c = c_0 + (1/4pi i) int_{1/2-i*infty}^{1/2+i*infty}
              pi^{s-c/2} Gamma(c/2-s) epsilon^c_{c/2-s} E_s(tau) ds
              + (Maass cusp form projections)

(Benjamin-Chang eq. 3.6, verified in roelcke_selberg_decomposition.py.)

### 1.4. The bar complex and shadow obstruction tower

The bar complex B(A) of a chiral algebra A has:
- Underlying space: the tensor coalgebra on generators of A, graded by
  arity n and genus g.
- Differential D_A: encodes OPE collision data through the bar construction
  on FM_n(X).
- D_A^2 = 0: the MC equation (thm:convolution-d-squared-zero at convolution
  level; thm:ambient-d-squared-zero at ambient level).

The universal MC element Theta_A := D_A - d_0 lives in the modular cyclic
deformation complex Def_cyc^mod(A). Its projections are the shadow obstruction tower:

    pi_{g,r}(Theta_A) = Sh_r^{(g)}(A)

At (g,r) = (0,2): kappa (modular characteristic).
At (g,r) = (0,3): alpha (cubic shadow).
At (g,r) = (0,4): S_4 (quartic contact coupling).
At (g,r) = (1,r): the genus-1 shadow amplitudes entering F_1^conn.

### 1.5. The sewing-shadow intertwining

**Theorem** (thm:sewing-shadow-intertwining): The connected genus-1 free
energy admits the shadow expansion

    F_1^conn(q; A) = Sigma_{r >= 2} Sh_r^{(1)}(A) * G_r(q)

where G_r(q) are universal modular functions on M_{1,1} (Eisenstein-type
averages of the chiral Green's function over the torus).

**Consequence** (cor:spectral-measure-identification): For lattice VOAs,
the Rankin-Selberg integral of the sewing determinant equals the
Rankin-Selberg integral of the shadow Fredholm determinant:

    int_{M_{1,1}} |det(1-K)|^{-2} E_s d mu
    = int |exp(<Theta, [E_tau]>)|^2 E_s d mu

Both yield the constrained Epstein zeta epsilon^c_s with L-function
factorization.

---

## 2. Precise Assessment of Each Question

### Q1: Is epsilon^c_s the spectral side of a trace formula?

**PARTIALLY TRUE, but the analogy is misleading.**

epsilon^c_s arises as the Eisenstein spectral coefficient of Z-hat^c in
the Roelcke-Selberg decomposition. The Roelcke-Selberg theorem IS a
spectral decomposition -- it decomposes L^2(SL(2,Z)\H) into eigenspaces
of the Laplacian. In this sense, epsilon^c_s is on the "spectral side."

However, the Selberg TRACE FORMULA is a much stronger statement than the
Roelcke-Selberg SPECTRAL DECOMPOSITION. The trace formula equates two
DIFFERENT representations of the same trace: spectral = geometric. The
Roelcke-Selberg decomposition is just a spectral expansion -- it does not
by itself produce a "geometric side."

The object that has a genuine geometric side is the SELBERG ZETA FUNCTION

    Z_Selberg(s) = prod_{gamma prim} prod_{k=0}^infty (1 - N(gamma)^{-s-k})

whose zeros encode both the eigenvalues r_j AND the lengths of closed
geodesics on SL(2,Z)\H. The Selberg zeta function is defined by an Euler
product over PRIME GEODESICS (geometric), and its zeros are at s = 1/2 + ir_j
(spectral). THIS is the trace formula.

**The question is then: is there a "VOA Selberg zeta function" whose geometric
side involves the bar complex?**

### Q2: Is there a trace formula with spectral side = epsilon^c_s and geometric side = bar complex?

**NO, and here is why the analogy fails structurally.**

The Selberg trace formula for SL(2,Z)\H has:

    Spectral: eigenvalues r_j of Delta on L^2(Gamma\H)
    Geometric: conjugacy classes of Gamma = SL(2,Z), classified by trace

The proposed "VOA trace formula" would need:

    Spectral: primary dimensions Delta_i of V
    Geometric: ??? involving the bar complex B(A)

The bar complex encodes OPE collision data on configuration spaces FM_n(X)
of points on a CURVE X. The geometric side of the Selberg trace formula
involves closed GEODESICS on the MODULAR SURFACE M_{1,1} = SL(2,Z)\H.
These are fundamentally different geometric objects:

**(a) Different spaces.** The bar complex lives on FM_n(X) (configuration
space of n points on a curve). The Selberg geometric side lives on
SL(2,Z)\H (the modular surface). These are different moduli problems:
FM_n(X) parametrizes n-tuples of points on a FIXED curve; M_{1,1}
parametrizes the CURVE ITSELF.

**(b) Different combinatorics.** The bar differential sums over GRAPHS
(stable trees, planted forests) encoding collision patterns of marked
points. The Selberg geometric side sums over CONJUGACY CLASSES of the
fundamental group, encoding closed orbits of the geodesic flow.

**(c) Different operators being traced.** The Selberg trace formula traces
the HEAT KERNEL e^{-t Delta} on L^2(Gamma\H). The bar complex encodes the
DIFFERENTIAL D_A on B(A). The trace of the heat kernel is an analytic
object (e.g., theta function); D_A^2 = 0 is an algebraic identity.

**The structural failure**: In the Selberg trace formula, the spectral
and geometric sides are TWO REPRESENTATIONS of the SAME OPERATOR TRACE.
They are linked by a SINGLE operation (taking the trace of a kernel
function). In the proposed VOA setting, the "spectral side" (epsilon^c_s)
and the "geometric side" (bar complex) are linked by a CHAIN of four
separate theorems:

    B(A) --[bar-intrinsic]--> Theta_A --[sewing-shadow]--> F_1^conn
         --[Rankin-Selberg]--> epsilon^c_s --[Roelcke-Selberg]--> spectral

Each arrow is a different type of mathematical operation (homological
algebra, power series identity, integral transform, spectral theory).
The Selberg trace formula has ONE arrow: trace of an integral operator.
The "VOA trace formula" has FOUR arrows with different mathematical
characters. This is a chain of theorems, not a trace formula.

### Q3: Is the shadow obstruction tower the "orbital integral" side?

**NO.** An orbital integral is:

    O_gamma(f) = int_{G_gamma\G} f(x^{-1} gamma x) dx

where G_gamma is the centralizer of gamma in G. It measures how the
test function f "sees" the conjugacy class of gamma.

The shadow obstruction tower Sh_r^{(g)}(A) is a TAYLOR COEFFICIENT of the MC element
Theta_A, evaluated at genus g and arity r. It is determined by three
OPE invariants (kappa, alpha, S_4) via the Riccati algebraicity theorem
(thm:riccati-algebraicity): H(t) = t^2 sqrt(Q_L(t)).

The shadow obstruction tower is not an integral over a conjugacy class. It is a
coefficient in a power series expansion of an algebraic function. The
analogy "shadow obstruction tower = orbital integral" is category-incorrect: orbital
integrals are integrals over orbits in a group; shadow coefficients are
Taylor coefficients of an algebraic function on a deformation space.

**What the shadow obstruction tower IS**: the shadow obstruction tower is the arity-graded sequence
of obstructions to extending a Maurer-Cartan element from arity r to
arity r+1. In the language of deformation theory, it is the POSTNIKOV TOWER
of the MC space. This is a homotopy-theoretic object, not a number-theoretic
orbital integral.

### Q4: Does D^2 = 0 force spectral consequences?

**YES, but not through a trace formula mechanism.**

D^2 = 0 (thm:convolution-d-squared-zero, thm:ambient-d-squared-zero) is
a PROVED theorem. Its consequences for the spectral side flow through the
four-step chain:

Step 1: D^2 = 0 implies Theta_A is MC, hence the shadow obstruction tower is
COHERENT: the entire infinite tower {S_r}_{r >= 2} is determined by
three invariants (kappa, alpha, S_4).

Step 2: The MC recursion at arity r+1 gives Newton's identities for the
spectral atoms {lambda_j} of the spectral measure:

    p_r = Sigma_{j=1}^r (-1)^{j-1} e_{r-j} p_j

This is a CONSTRAINT: the power sums p_r = Sigma lambda_j^r satisfy
polynomial identities. Combined with Carleman's condition (the moments
grow at rate rho^r r^{-5/2}, which is summable in the Carleman sense),
the spectral measure is UNIQUELY DETERMINED by (kappa, alpha, S_4).

Step 3: The moment L-function M_r(s) = int Sh_r * E_s d mu is
meromorphic and satisfies the MC recursion in the spectral variable s
(thm:mc-recursion-moment). For lattice VOAs, this gives the Hecke
decomposition of epsilon^c_s.

Step 4: Route C prime-locality (thm:route-c-propagation): if the low-arity
shadow data (kappa, alpha) are Hecke-equivariant (i.e., come from a modular
form via the Hecke correspondence), then the MC recursion propagates
prime-locality to ALL arities.

**These are genuine spectral consequences of D^2 = 0.** But they are
consequences through a CHAIN OF FOUR THEOREMS, not through a single trace
formula identity. The mechanism is:

    algebraic constraint (D^2=0) --> finite determination (MC recursion)
    --> spectral measure uniqueness (Carleman) --> L-function structure (Hecke)

This is NOT analogous to the Selberg trace formula, which gives:

    spectral data <--> geometric data   (DIRECTLY, in one step)

---

## 3. What IS True: The Sewing Trace Formula

The manuscript DOES contain a genuine trace formula, but it is more
elementary than the Selberg trace formula and operates at a different
level. This is prop:sewing-trace-formula in arithmetic_shadows.tex:

    Sigma_{N >= 1} tr(K_q^N) / N = -log det(1 - K_q) = Sigma_{M >= 1} sigma_{-1}(M) q^M

and the sewing-Selberg formula (thm:sewing-selberg-formula):

    int_{M_{1,1}} log det(1-K(tau)) * E_s(tau) d mu(tau)
    = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)

**This IS a trace formula**, but of a much simpler kind:

- The "spectral side" is the Fredholm determinant det(1-K_q), which encodes
  the eigenvalues {q^n} of the sewing operator K_q on Fock space.
- The "geometric side" is the divisor sum sigma_{-1}(M), which counts
  ordered factorizations M = nm weighted by 1/m.
- The Rankin-Selberg integral against E_s(tau) produces zeta(s-1)*zeta(s),
  which has an Euler product over primes.

**The factorization into primes IS a trace formula identity**: the product
over primes p of (1-p^{-s})^{-1}(1-p^{-s-1})^{-1} equals the Dirichlet
series of sigma_{-1}(N). Each prime contributes a "local factor" (the
"orbital integral" at p), and the Dirichlet series is the "spectral side."

But this is the classical identity Sigma sigma_{-1}(N) N^{-s} = zeta(s)zeta(s+1),
which is elementary number theory. It does not involve the bar complex or the
MC equation in any essential way. The bar complex enters only through the
sewing-shadow intertwining, which connects det(1-K_q) to Theta_A -- and this
connection is a THEOREM about the relationship between sewing and bar
constructions, not a trace formula.

---

## 4. The Honest Structural Comparison

| Feature | Selberg trace formula | VOA sewing chain |
|---------|----------------------|------------------|
| **What is being traced** | Heat kernel on L^2(Gamma\H) | Sewing operator K_q on Fock space |
| **Spectral side** | Maass eigenvalues r_j | Primary dimensions Delta_i (via epsilon^c_s) |
| **Geometric side** | Closed geodesics on Gamma\H | Divisor sums sigma_{-1}(N) = graph combinatorics |
| **Connection mechanism** | ONE identity (Poisson summation / trace of kernel) | FOUR theorems (bar, sewing-shadow, Rankin-Selberg, Roelcke-Selberg) |
| **Group action** | SL(2,Z) acting on H | SL(2,Z) acting on tau (moduli) |
| **Test function freedom** | Arbitrary h in Paley-Wiener class | FIXED by the VOA (no free test function) |
| **Zeta zeros appear** | As poles of the scattering matrix phi(s) | Same (phi(s) = Lambda(1-s)/Lambda(s)) |
| **MC equation role** | None | Constrains shadow obstruction tower (algebraic input) |
| **Bar complex role** | None | Produces Theta_A (the MC element) |

**The critical distinction**: In the Selberg trace formula, the spectral
and geometric sides are EQUAL for ALL test functions h. This equality
CHARACTERIZES the spectrum: knowing the geometric side for all h
determines all eigenvalues. In the VOA chain, the "test function" is
FIXED by the choice of VOA -- there is no family of test functions to
vary. The MC equation constrains the shadow obstruction tower (one specific "test
function"), but this constraint is a single algebraic identity, not a
family of identities parametrized by test functions.

---

## 5. What Would a Genuine "VOA Trace Formula" Look Like?

A genuine trace formula for VOAs would need:

**(A) An operator whose trace produces both sides.** The candidate is the
sewing operator K_q varied over M_{1,1}. Its Fredholm determinant is
det(1-K(tau)), and Rankin-Selberg gives epsilon^c_s from its spectral
decomposition. But the "geometric side" of a trace of K requires
computing tr(K^N) for all N and applying the Selberg trace formula to
SL(2,Z)\H with test function h determined by K^N. This gives:

    Sigma_j h(r_j; K^N) = geometric terms at each N

where the geometric terms involve Kloosterman sums (the parabolic
contribution) and orbital integrals (the hyperbolic contribution).

**(B) Kloosterman sums.** The parabolic contribution to the Selberg
trace formula involves Kloosterman sums S(m,n;c). The Kuznetsov trace
formula (kuznetsov_bridge.py) converts Kloosterman sums to spectral
data. For rational VOA characters, the Rademacher expansion involves
generalized Kloosterman sums K^rho_{ij}(m,n;c) associated to the
modular representation rho: SL(2,Z) --> GL(d) of the character vector.

**This is the closest object to a genuine "VOA trace formula."** The
Kuznetsov formula converts:

    Sigma_c S(m,n;c)/c * h(c)  =  spectral sum

where the left side involves Kloosterman sums (geometric: orbits of
the parabolic subgroup) and the right side involves Hecke eigenvalues
(spectral). The Rademacher expansion of VOA characters provides the
Kloosterman sums; the Kuznetsov formula converts them to spectral data.

**(C) The bar complex's role.** In this framework, the bar complex enters
through the MC equation's constraint on the FOURIER COEFFICIENTS of the
partition function. The MC recursion (thm:mc-recursion-moment) constrains
the moment L-functions M_r(s), which are Rankin-Selberg transforms of
the shadow amplitudes. These shadow amplitudes are the genus-1 projections
of Theta_A, which is the bar-intrinsic MC element.

The chain is:

    Bar complex --> Theta_A --> Sh_r^{(1)} --> M_r(s)
    = int Sh_r * E_s d mu = Rankin-Selberg of shadow amplitude

and separately:

    Rademacher expansion of chi_V --> Kloosterman sums K^rho(m,n;c)
    --> Kuznetsov --> Hecke eigenvalues a_j(n) --> L(s, u_j)

The bar complex constrains the SAME spectral data that the Kloosterman
sums access, but through a DIFFERENT route. The MC recursion gives
polynomial constraints on the moments of the spectral measure; the
Kuznetsov formula gives a direct spectral-to-geometric duality.

**These two routes are COMPLEMENTARY, not equivalent.** The MC route
gives algebraic constraints (Newton's identities); the Kuznetsov route
gives analytic identities (trace formula). Neither subsumes the other.

---

## 6. The Shadow Tower and Orbital Integrals: A False Analogy

The suggestion that the shadow obstruction tower plays the role of "orbital integrals"
fails for a precise reason.

**Orbital integrals detect INDIVIDUAL conjugacy classes.** The orbital
integral O_gamma(f) tells you how the test function f interacts with ONE
conjugacy class gamma. Different conjugacy classes give different
orbital integrals. The spectral side pairs these: each eigenvalue sees
ALL conjugacy classes (through the trace).

**Shadow coefficients S_r are GLOBAL.** S_r = pi_{1,r}(Theta_A) is a
single number for each (g,r), not a function of a conjugacy class. The
full shadow obstruction tower {S_r}_{r >= 2} is determined by three numbers
(kappa, alpha, S_4). It does not decompose into "local contributions"
at individual geometric features (primes, geodesics, or conjugacy
classes).

**The correct analogy (if any) is between the shadow obstruction tower and the
FOURIER COEFFICIENTS of the partition function, not the orbital integrals.**
Both are sequences of numbers that encode the full content of a modular
object. The shadow obstruction tower encodes the MC element Theta_A through its
projections; the Fourier coefficients encode the partition function
through its q-expansion. The MC recursion is a constraint on the shadow
tower analogous to the Hecke relations as a constraint on Fourier
coefficients.

---

## 7. The Graph Sum as a "Geometric Side"

There IS a sense in which the graph sum formula (prop:chiral-graph-integral)
provides a "geometric side":

    F_1^conn = Sigma_Gamma |Aut(Gamma)|^{-1} ell_Gamma(tau)

where ell_Gamma(tau) is the chiral graph integral on E_tau:

    ell_Gamma(tau) = int_{E_tau^{|V|-1}} prod_{v} m_{val(v)}
                     * prod_{e} g(z_{s(e)}, z_{t(e)}; tau) prod_{v != v_0} dz_v

**This is a sum over GRAPHS, not a sum over conjugacy classes.** Each graph
Gamma contributes an amplitude ell_Gamma(tau) that is an integral over
the configuration space of its vertices on the torus E_tau. The vertex
factors m_{val(v)} are OPE data (the "collision data"). The edge factors
g(z,w;tau) are chiral Green's functions (the "propagators").

This graph sum is the analog of a FEYNMAN DIAGRAM expansion, not a trace
formula. In a trace formula:
- The geometric side is a sum over CONJUGACY CLASSES (discrete, group-theoretic)
- The sum is FINITE or COUNTABLE with explicit control

In the graph sum:
- The sum is over GRAPHS (combinatorial, but not group-theoretic)
- The sum is INFINITE with convergence controlled by HS-sewing

The graph sum is closer to a PERTURBATIVE EXPANSION than a trace formula.
The MC equation D^2 = 0 is the constraint that makes this expansion
CONSISTENT (analogous to gauge invariance making the perturbative
expansion well-defined), but it is not a spectral-geometric duality.

---

## 8. The Kuznetsov Bridge: The Closest True Object

The closest object in the manuscript to a genuine "VOA trace formula"
involving both spectral and geometric data is the Kuznetsov bridge
(kuznetsov_bridge.py):

    VOA character (Rademacher) --> generalized Kloosterman sums K^rho(m,n;c)
    --> Kuznetsov spectral inversion --> Hecke eigenvalues a_j(n)
    --> L-functions L(s, u_j) with Euler products

The Kuznetsov trace formula IS a trace formula:

    Sigma_c phi(c) S(m,n;c) / c = (spectral sum over Maass forms and Eisenstein)

The left side is geometric (Kloosterman sums = exponential sums over
units mod c, arising from the parabolic orbital integral). The right
side is spectral (Hecke eigenvalues of Maass forms).

For VOA characters with Rademacher expansions, the Kloosterman sums are
GENERALIZED (involving the modular representation), but the Kuznetsov
structure is the same.

**The bar complex's connection to the Kuznetsov bridge**: The MC recursion
constrains the SHADOW AMPLITUDES Sh_r, which are the Rankin-Selberg
transforms of the same spectral data that the Kuznetsov formula accesses
through Kloosterman sums. The connection is:

    MC recursion on Sh_r  <-->  Newton's identities on spectral atoms
    Kuznetsov on K^rho    <-->  spectral inversion of Kloosterman data

Both access the SAME spectral atoms {lambda_j}, but through different
algebraic/analytic mechanisms. The MC recursion is algebraic (polynomial
constraints from D^2=0); the Kuznetsov formula is analytic (integral
transforms of exponential sums).

**Is this the "missing bridge"?** No. The Kuznetsov formula relates
Kloosterman sums (geometric) to spectral data. The MC equation constrains
spectral data algebraically. These are TWO INDEPENDENT sources of
information about the same spectral object. Neither implies the other.
The bar complex does not produce Kloosterman sums, and the Kuznetsov
formula does not produce MC constraints.

---

## 9. Falsification Summary

| Claim | Status | Reason |
|-------|--------|--------|
| epsilon^c_s is a spectral object | TRUE | It IS the Eisenstein spectral coefficient of Z-hat^c |
| The bar complex provides "geometric" data | TRUE | But in the sense of OPE collision data, not orbital integrals |
| These two are "sides of a trace formula" | FALSE | They are connected by a 4-step chain, not a single trace identity |
| The shadow obstruction tower = "orbital integrals" | FALSE | Shadow coefficients are Taylor coefficients, not integrals over orbits |
| D^2=0 forces spectral consequences | TRUE | Through MC recursion + Carleman + Route C, not through trace formula |
| The MC equation is the "geometric constraint" | MISLEADING | It is an algebraic constraint on the bar complex, not a geometric identity |
| The graph sum is the "geometric side" | PARTIALLY TRUE | It is a perturbative expansion, not a trace formula geometric side |
| The Kuznetsov bridge provides the missing link | FALSE | It is a SEPARATE source of spectral information, not a consequence of MC |

---

## 10. What Could Be True

The following weaker statement is TRUE and provable:

**Theorem (the four-step chain).** Let A be a chirally Koszul vertex algebra
satisfying the HS-sewing condition. Then the following chain of identifications
holds:

    (i) The MC element Theta_A in MC(Def_cyc^mod(A)) determines the shadow
        tower {Sh_r^{(g)}(A)} by projection (thm:mc2-bar-intrinsic).

    (ii) The genus-1 shadow amplitudes determine the connected free energy
         F_1^conn(q;A) = Sigma_r Sh_r^{(1)} G_r(q)
         (thm:sewing-shadow-intertwining).

    (iii) The Rankin-Selberg integral of F_1^conn against E_s gives the
          moment L-function M_r(s), which satisfies the MC recursion
          (thm:mc-recursion-moment).

    (iv) For lattice VOAs, M_r(s) factors through Hecke eigenvalues, and
         the shadow-spectral correspondence counts critical lines
         (thm:shadow-spectral-correspondence).

This chain is NOT a trace formula. It is a sequence of proved theorems
connecting algebraic data (the bar complex) to analytic data (the
constrained Epstein zeta) through combinatorial intermediaries (the
shadow obstruction tower and graph sums). Each step involves a different mathematical
operation, and the chain cannot be collapsed into a single identity.

**The meta-lesson**: The temptation to call this a "trace formula" comes from
the superficial resemblance:
- Spectral data on one side (primary dimensions / epsilon^c_s)
- Geometric data on the other (OPE collision / bar complex)
- A modular symmetry (SL(2,Z)) relating them

But a trace formula requires MUCH more: a single operator whose trace
admits two representations. The VOA setting has the Fock-space trace
(partition function) and the Laplacian trace (Selberg), but these are
DIFFERENT traces of DIFFERENT operators on DIFFERENT spaces. The four-step
chain connects them, but the connection is a theorem, not an identity.

---

## References to manuscript source

- thm:mc2-bar-intrinsic: higher_genus_modular_koszul.tex
- thm:sewing-shadow-intertwining: arithmetic_shadows.tex line 2271
- prop:sewing-trace-formula: arithmetic_shadows.tex line 244
- thm:sewing-selberg-formula: arithmetic_shadows.tex line 276
- thm:mc-recursion-moment: arithmetic_shadows.tex line 5452
- thm:shadow-spectral-correspondence: arithmetic_shadows.tex line 100
- rem:structural-obstruction: arithmetic_shadows.tex line 300
- kuznetsov_bridge.py: compute/lib/kuznetsov_bridge.py
- roelcke_selberg_decomposition.py: compute/lib/roelcke_selberg_decomposition.py
- moduli_spectral_decomposition.py: compute/lib/moduli_spectral_decomposition.py

## Existing analyses consulted

- compute/audit/koszul_epstein/benjamin_chang.md (Object A vs B vs C disambiguation)
- compute/audit/koszul_epstein/mc_spectral_measure.md (falsification of moment problem framework)
- compute/audit/koszul_epstein/synthesis.md (Beilinson verdict on Koszul-Epstein programme)
- compute/audit/koszul_epstein/modular_surface_positivity.md (no-go for surface positivity)
