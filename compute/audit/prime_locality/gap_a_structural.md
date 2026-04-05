# Gap A Structural Analysis: Bar-Cobar vs Scattering

## The Question

Gap A (rem:langlands-gap-a in concordance.tex, line 6937) states:

> The bar-cobar adjunction produces *twisting morphisms*: algebraic maps
> tau : B(A) -> A controlling the coupling between a chiral algebra and
> its Koszul dual. The Langlands programme requires *scattering amplitudes*:
> analytic objects whose poles on the complex s-plane encode L-function zeros.
> These are different types of mathematical objects.

This document attacks the following questions:
1. What is the bridge between these two types of objects?
2. What are the "primes" for chiral algebras?
3. Is the obstruction fundamentally about the lack of a lattice?
4. What has been proved and what remains open?


## 1. The Bridge That Exists (for Lattice VOAs)

The manuscript constructs a two-step bridge for lattice VOAs (concordance.tex, lines 6955-6971; arithmetic_shadows.tex, full chapter):

**Step (i): Sewing-shadow intertwining** (thm:sewing-shadow-intertwining, PROVED).
The connected genus-1 free energy F_1^{conn}(q; A) equals the shadow expansion
sum_{r >= 2} Sh_r^{(1)}(A) * G_r(q). This identifies the sewing Fredholm
determinant det(1 - K_q) with a Chern-Weil pairing of Theta_A. The bridge
is: the algebraic object (MC element Theta_A) determines the analytic object
(partition function on M_{1,1}) via graph sums evaluated on elliptic curves.

**Step (ii): Hecke module structure** (thm:spectral-continuation-bridge, PROVED for lattice VOAs).
For a lattice VOA V_Lambda of rank r, the theta function
Theta_Lambda = E_{r/2} + sum c_j f_j decomposes into Hecke eigenforms.
This decomposition passes through the sewing differential, making the
graph amplitudes Hecke-equivariant. Rankin-Selberg unfolding then produces
the L-functions L(s, f_j) from the moment integrals M_r(s).

The full chain for lattice VOAs:

    Theta_A  --(sewing-shadow)-->  det(1-K_q)
             --(Mellin)-->         M_r(s) = int Sh_r * E_s d mu
             --(Hecke decomp)-->   sum c_j L(s, f_j)
             --(CPS converse)-->   automorphic pi_r
             --(prime-locality)--> Euler product at each p
             --(Serre)-->          Ramanujan

Every arrow is proved for lattice VOAs.


## 2. Where the Bridge Breaks for Non-Lattice Algebras

For non-lattice theories, step (ii) fails. The precise obstruction:

**Missing: Hecke module structure.**
The Hecke operators T_p act on modular forms M_k(SL(2,Z)) by
(T_p f)(tau) = p^{k-1} f(p tau) + (1/p) sum_{j=0}^{p-1} f((tau+j)/p).
For lattice VOAs, the partition function chi(tau) = Theta_Lambda / eta^r
lives in a finite-dimensional space of modular forms on which T_p acts
semisimply. The theta function Theta_Lambda decomposes into eigenforms
because the space M_{r/2}(Gamma) has a Hecke eigenbasis.

For Virasoro at generic c: the partition function 1/eta(tau) is NOT a Hecke
eigenform. It is an element of weight -1/2 of a space of modular forms for
Gamma_0(4) (by Dedekind's transformation), but this space is
infinite-dimensional when embedded in the Roelcke-Selberg spectral
decomposition, and the relevant Hecke theory is that of Maass forms and
the continuous spectrum.

For rational CFTs (minimal models): the characters chi_{r,s}(tau) are
components of a vector-valued modular form (VVMF) on a congruence subgroup
Gamma(4pq). The individual characters are NOT Hecke eigenforms
(verified computationally: 0/3 Ising characters and 0/6 tricritical Ising
characters are eigenforms of T_p at p = 2, 3, 5 -- see
prime_locality_minimal_model.py and prop:rational-cft-multiplicativity-failure).

**Consequence:** The partition function Dirichlet coefficients a_n are NOT
multiplicative for rational CFTs. This is proved by direct computation
(14 coprime failures for Ising at m,n <= 20).


## 3. What Are the "Primes" for a Chiral Algebra?

This is the core structural question. In classical number theory:

| Number theory | Chiral algebras | Status |
|---|---|---|
| Primes p | ??? | UNDEFINED in general |
| Local Galois group G_p | ??? | No analogue |
| Local factor det(1 - p^{-s} Frob_p)^{-1} | ??? | Exists only for lattice VOAs |
| Euler product prod_p L_p(s) | M_r(s) moment L-function | Has Euler product ONLY for lattice VOAs |

Three candidate notions of "prime" appear in the manuscript, none satisfactory:

### Candidate A: Conformal weights Delta as primes

The primary spectrum S = {Delta_1, Delta_2, ...} is the natural "prime-like"
data of a chiral algebra. The constrained Epstein zeta
epsilon^c_s(A) = sum c_Delta (2 Delta)^{-s}
is defined by summing over primaries (def:scattering-coupling).

**Problem:** Conformal weights are NOT multiplicative. The product of two
primaries of weights Delta_1, Delta_2 is not a primary of weight
Delta_1 * Delta_2 or Delta_1 + Delta_2 in any useful sense.
There is no analogue of "coprime" conformal weights.
The sewing determinant det(1-K_q) = prod_n (1-q^n)^{-mult(n)} has an infinite
product over positive integers n (the Fock space grading), but these integers
are NOT primes -- they are weight levels, and the product is over ALL
positive integers, not a subset of "prime" ones.

### Candidate B: Rational primes p via partition function Fourier coefficients

For a lattice VOA, the representation count r_Lambda(n) (number of lattice
vectors of norm n) is the n-th Fourier coefficient of Theta_Lambda. When
Theta_Lambda decomposes into Hecke eigenforms, the eigenvalues a_p(f_j)
provide "local data at p." The Euler product
L(s, f_j) = prod_p (1 - a_p p^{-s} + p^{k-1-2s})^{-1}
is indexed by rational primes.

**Problem:** This works only because the lattice provides:
(a) A Z-form: the lattice Lambda is a free Z-module, and its representation
    counts r_Lambda(n) = |{v in Lambda : |v|^2 = n}| are integers.
(b) Hecke structure: the theta function Theta_Lambda is a modular form for a
    congruence subgroup, on which T_p acts and commutes with everything.
(c) Multiplicativity: r_Lambda is NOT multiplicative in general (e.g., for
    the Z-lattice, r_Z(n) = 2 * #{d | n : d odd} is multiplicative, but
    for the A_2 root lattice the formula involves Jacobi symbols).
    The eigenform COMPONENTS have multiplicative coefficients.

Without a lattice, there is no Z-form, no Hecke, and rational primes have
no canonical action on the chiral algebra data.

### Candidate C: Arity r as "prime direction"

The shadow obstruction tower Theta_A^{<= r} is indexed by arity. The shadow coefficient
S_r at arity r is a scalar invariant of A. The conjecture
conj:prime-locality-transfer states that S_r decomposes "prime-by-prime":
S_r^{(p)} proportional to p_{r-1}(alpha_p, beta_p).

**Problem:** This conflates two different meanings of "local."
In the Langlands sense, "local at p" means "determined by the restriction of
the automorphic representation to the local group G(Q_p)."
In the shadow obstruction tower, "arity r" is a filtration level in a deformation complex,
not a localization at a place. The MC recursion relating S_{r+1} to
{S_j}_{j <= r} is a GLOBAL constraint, not a collection of independent
local constraints. Indeed, the MC bracket is fundamentally non-local:
it involves stable-graph gluing on M_{g,n}, which couples all arities.


## 4. The Structural Diagnosis: Three Independent Obstructions

Gap A is not a single missing theorem. It decomposes into three independent
structural obstructions, each at a different level:

### Obstruction 1: Algebraic multiplicativity vs arithmetic multiplicativity

The independent-sum factorization (prop:independent-sum-factorization) gives:
det_{A_1 tensor A_2}(1 - K_q) = det_{A_1}(1 - K_q) * det_{A_2}(1 - K_q).

This is multiplicativity under TENSOR DECOMPOSITION of chiral algebras. It
is NOT multiplicativity of Fourier coefficients, which would require
a_{mn} = a_m * a_n for coprime m, n (multiplicativity under multiplication
of positive integers). The manuscript is honest about this
(rem:euler-product-from-independent-sum, lines 3480-3489):

> "This algebraic multiplicativity does not produce an Euler product indexed
> by primes unless the algebra itself decomposes prime-by-prime."

The Heisenberg algebra decomposes prime-by-prime because its partition function
1/prod(1-q^n) = sum sigma_{-1}(n) q^n has multiplicative Fourier coefficients
(sigma_{-1} is a multiplicative arithmetic function). The Euler product
zeta(s) zeta(s+1) follows (cor:sewing-euler-product).

For non-free-field families, no such decomposition exists.
The compute engine euler_product_from_mc.py establishes this directly:
the MC recursion does NOT preserve multiplicativity of Fourier coefficients
because the graph sum at arity r involves convolution over stable graphs that
does not respect coprimality (lines 36-46).

**Verdict:** This obstruction is STRUCTURAL and cannot be removed by cleverness.
The MC equation constrains shadow coefficients via nonlinear operations
(graph sums, convolutions) that do not preserve multiplicativity.
Multiplicativity is an EXTERNAL input, present for lattice VOAs (from the
lattice) and absent in general.

### Obstruction 2: Z-form and Hecke action

For a lattice VOA V_Lambda, the Z-form is the lattice Lambda itself.
The Hecke operators T_p act on the theta function by a known explicit formula
involving sublattices of index p^k. This action produces a semisimple
decomposition into eigenforms.

For non-lattice algebras, there is no Z-form in the relevant sense.
The "Hecke defect" (subsec:hecke-defect-obstruction, lines 5920-5956)
measures the failure of Hecke equivariance:
delta_p^{Hecke}(A) := [T_p, pi_{1,r}(Theta_A)] in H^1(g^mod_A, ad_{T_p}).

If H^1 = 0, the Hecke operators automatically commute with the MC data,
and the extension from lattice to non-lattice is possible (line 5948).
Whether H^1 vanishes is OPEN for all non-lattice families.

The Virasoro case is particularly instructive. The vacuum character
1/eta(tau) transforms under SL(2,Z) with a multiplier system, but the
resulting modular form lives in the space of weight -1/2 forms.
The Hecke theory for half-integral weight is more delicate (Shimura
correspondence, Kohnen plus-space), and the standard T_p operators
do not act simply.

The W_N case adds another layer: the Miura defect
(thm:finite-miura-defect) shows that the W_N sewing lift differs from
the (N-1)-fold Heisenberg sewing lift by a FINITE polynomial:
D^{prime}_{W_N}(u) = -zeta(u+1) sum H_j(u).
The Heisenberg core carries the Euler product; the defect sector carries
the family-specific arithmetic content but has no independent Hecke structure.
The Miura packet splitting (prop:miura-packet-splitting) decomposes the
arithmetic packet connection into a diagonal Heisenberg part and a
finite-rank defect part, with all obstructions in the defect sector.

**Verdict:** The Z-form obstruction is the deepest. In classical number theory,
the Z-form is what turns geometry into arithmetic (etale cohomology needs a
scheme over Spec Z). For chiral algebras, the analogous structure would be
a "chiral algebra over Z" -- an integral form of the OPE algebra. Lattice
VOAs have this (the lattice IS the integral structure). Non-lattice algebras
generally do not.

### Obstruction 3: Analytic continuation and functional equation

Even when the moment L-function M_r(s) is defined (which it is for all
chirally Koszul algebras with HS-sewing, by thm:cps-from-mc), the question
of whether it has an Euler product is independent of whether it has
analytic continuation and functional equation.

The CPS converse theorem converts:
  (meromorphic continuation) + (functional equation) + (polynomial growth)
  + (all twists) --> automorphic representation pi_r.

This is PROVED (thm:cps-from-mc). But the resulting automorphic pi_r is on
GL(r), not GL(2). To extract an Euler product, one needs pi_r to be a
functorial transfer from GL(2) -- specifically, pi_r = Sym^{r-1}(f) for
some automorphic f on GL(2). This identification requires:
(a) Prime-locality (conj:prime-locality-transfer): OPEN for non-lattice.
(b) Strong multiplicity one (Jacquet-Shalika): PROVED.
(c) Langlands functoriality GL(2) -> GL(r+1): PROVED for r <= 4 (Kim-Shahidi),
    OPEN for r >= 5.

The "complete chain" (rem:complete-chain, line 5255) makes this explicit:

    MC --(HS-sewing)--> RS method --(unfolding)--> M_r(s) meromorphic
       --(CPS)--> pi_r in Aut(GL(r))
       --[prime-locality]--> M_r = Sym^{r-1} --(Serre)--> Ramanujan

The bracket around [prime-locality] means: this is the single unproved step
for non-lattice theories.


## 5. Is the Obstruction Fundamentally About the Lack of a Lattice?

**Yes, at the deepest level.** Here is the argument:

### What the lattice provides

A lattice Lambda in R^r provides ALL THREE of:

1. **Z-form:** Lambda is a free Z-module. The representation counts
   r_Lambda(n) are integers. The theta function Theta_Lambda is a modular
   form with algebraic Fourier coefficients.

2. **Hecke action:** The Hecke operators T_p act on Theta_Lambda via
   sublattice enumeration. The action is semisimple on the finite-dimensional
   space M_{r/2}(Gamma_0(N), chi) with eigenform decomposition.

3. **Prime-by-prime decomposition:** Each eigenform f_j has an Euler product
   L(s, f_j) = prod_p (1 - a_p(f_j) p^{-s} + chi(p) p^{k-1-2s})^{-1}.
   The shadow coefficients decompose as S_r^{(p)} ~ p_{r-1}(alpha_p, beta_p)
   where alpha_p, beta_p are the Satake parameters at p.

### What non-lattice algebras lack

For Virasoro at generic c:

1. **No Z-form:** The OPE coefficients C_{abc} involve rational functions
   of c (e.g., C_{TTT} = c/2). For irrational c, these are transcendental.
   There is no canonical integral structure.

2. **No Hecke action on the partition function:** The vacuum character
   1/eta(tau) does not live in a space with Hecke eigenbasis. The Maass
   forms on SL(2,Z)\H provide a spectral decomposition, but this is the
   Roelcke-Selberg decomposition (continuous + discrete), not a finite Hecke
   decomposition.

3. **No prime-by-prime decomposition:** The shadow coefficients S_r(c) are
   GLOBAL invariants of the algebra (rational functions of c). They do not
   decompose into "local" data at individual primes.

### The shadow arithmetic trichotomy (prop:shadow-arithmetic-trichotomy)

The manuscript proves a precise trichotomy for rational CFTs:

- **Level 0** (partition function): Dirichlet coefficients are NOT
  multiplicative. Cross-channel terms between conformal families destroy
  multiplicativity at O(1) level.

- **Level 1** (per-channel): Each character eta * chi_{r,s} is a theta
  function on Gamma(4pq), but per-channel multiplicativity fails even
  away from level primes.

- **Level 2** (shadow projections): Sh_2^{(1)} has multiplicative Fourier
  coefficients (because E_2* has multiplicative coefficients). At arities
  r >= 3, the Euler product status is OPEN; the obstruction is the
  quasi-modular nature of E_2* (rem:quasimodular-obstruction).

This trichotomy shows that prime-locality might hold at the SHADOW level
even when it fails at the partition-function level. The critical question:

> Does Sh_r(Theta_A; tau) have an Euler product structure that Z(tau) lacks?

This is conj:prime-locality-transfer. The manuscript's own analysis
(rem:naive-prime-locality-obstruction, lines 5054-5085) recognizes that
this conjecture "cannot be tested via the partition function Euler product
for non-lattice theories" and must be formulated at the shadow-projection
level.


## 6. The Arithmetic Packet Connection: A Partial Bridge

The arithmetic packet connection nabla^{arith}_A
(def:arithmetic-packet-connection) provides a geometric reformulation of
Gap A that partially bridges the divide.

**What it does:** For ANY chirally Koszul algebra with HS-sewing:
- The arithmetic packet module M_A = direct sum of generalized Hecke
  eigenspaces (even when Hecke eigenbasis does not exist, one can still
  define generalized eigenspaces via Jordan decomposition).
- The packet connection nabla = d - (d log Lambda_chi / ds) is a flat
  meromorphic connection on M_A tensor O_C.
- Its singular divisor D_A = union div(Lambda_chi) is the union of the
  L-function zeros.
- The frontier defect form Omega_A = d log Lambda_{Eis} - d log phi measures
  the discrepancy between the activated L-packets and the automorphic
  scattering matrix.

**What it does NOT do:** The arithmetic comparison conjecture
(conj:arithmetic-comparison) asserts that Theta_A canonically DETERMINES
nabla^{arith}_A. This is OPEN. The frontier defect form Omega_A encodes
exactly the residual gap: the gauge criterion (prop:gauge-criterion-scattering)
says that Omega_A = 0 (i.e., the MC data matches the scattering data) iff
the Eisenstein block of the sewing lift equals the scattering matrix.
For lattice VOAs, Omega_A != 0 in general (because zeta(s) and zeta(2s)
have different zero sets), so even in the lattice case the bridge is not
perfect.


## 7. What Computable Evidence Exists

The compute layer has extensive infrastructure testing these questions:

| Module | What it tests | Findings |
|---|---|---|
| prime_locality_minimal_model.py | Stieltjes moments, multiplicativity, Newton bridge for minimal models | Signed Stieltjes measure for all c > -22/5; 14 multiplicativity failures for Ising |
| euler_product_from_mc.py | Whether MC forces Euler products on M_r(s) | NO: MC recursion does not preserve multiplicativity |
| sewing_euler_product.py | Heisenberg Euler product zeta(s)*zeta(s+1) | Verified |
| shadow_level_arithmetic.py | Shadow-level multiplicativity testing | Level-1 multiplicativity proved; level-2 open at r >= 3 |
| hecke_defect.py | Hecke defect delta_p^{Hecke}(A) | Computational test infrastructure |
| vvmf_hecke.py | VVMF Hecke eigenvalue extraction for minimal models | 0/3 Ising characters are eigenforms |


## 8. The False Idea to Dismiss (Beilinson Principle)

**FALSE IDEA: "The shadow obstruction tower S_r at arity r serves as a local factor
at arity r, analogous to the local factor L_p(s) at prime p."**

This is wrong for a precise reason: the MC recursion that determines S_{r+1}
from {S_j}_{j <= r} is a GLOBAL constraint (it involves sums over stable
graphs on M_{g,n}, coupling all arities simultaneously), while the local
factor L_p(s) is determined INDEPENDENTLY at each prime p by the local Galois
representation. In the Langlands programme, the miracle is that independently
determined local data assembles into a global object (the L-function). In the
shadow obstruction tower, there is no independence -- the MC equation couples all arities.

The correct analogy, if one exists at all, is:

| Langlands | Chiral algebras |
|---|---|
| Local Galois group G_p | Shadow coefficient S_r at arity r |
| Frobenius Frob_p | The arity-r graph sum evaluated at the r-th stable stratum |
| Local factor L_p(s) | The r-th moment L-function M_r(s) |
| Independence of local factors at different p | FAILS: MC recursion couples arities |
| Euler product = global L-function | Moment sequence {M_r(s)} (no product structure) |

The bottom row is the key: there is no "product" that assembles the moment
L-functions into a single L-function. The moment L-functions M_r(s) for
different r are DIFFERENT functions (not factors of a single function).
The shadow obstruction tower is an infinite sequence, not an infinite product.

**COUNTERARGUMENT (partial):** The manuscript does identify one setting where
a product structure emerges: the sewing Fredholm determinant
det(1-K_q) = prod_n (1-q^n)^{-mult(n)}. This is a product over weight levels n,
and when mult(n) is multiplicative (as for the Heisenberg), it gives an Euler
product. But this is a product over INTEGERS, not over PRIMES. The passage
to primes requires the fundamental theorem of arithmetic (unique factorization
of integers), which is a property of Z, not of the chiral algebra.


## 9. The Honest Assessment

Gap A decomposes into a hierarchy of sub-gaps:

**Level 1 (PROVED):** The MC element Theta_A determines the scattering
coupling E_rho(A) at every nontrivial zero rho. This is
thm:scattering-coupling-factorization. The algebra-dependent factor is the
constrained Epstein zeta epsilon^c_s(A), which is controlled by the shadow
tower. The MC equation exhausts the algebraic content of the genus-1
arithmetic interface (thm:structural-separation).

**Level 2 (PARTIALLY PROVED):** For lattice VOAs, the Hecke module structure
provides the complete bridge from twisting morphisms to scattering amplitudes.
The chain MC -> prime-locality -> CPS -> Sym^{r-1} -> Ramanujan is closed.

**Level 3 (OPEN):** For non-lattice theories:
(a) Prime-locality (conj:prime-locality-transfer) is open.
(b) The arithmetic comparison conjecture (conj:arithmetic-comparison) is open.
(c) The Hecke defect H^1(g^mod_A, ad_{T_p}) is uncomputed.
(d) The shadow-level Euler product at arities r >= 3 is open.

**Level 4 (STRUCTURAL):** The zero-location question (where are the zeros of
zeta?) is STRUCTURALLY inaccessible from the MC equation at genus 1.
The MC equation constrains the Kahler potential (arithmetic part
2 log |eta|^2), but this part is pluriharmonic (killed by d-dbar), hence
invisible to the Weil-Petersson metric. The "unfolding erasure" shows that
the Rankin-Selberg integral is holomorphic at scattering poles, carrying
no zero-location information. This is a THEOREM about what the MC equation
cannot do at genus 1 (thm:structural-separation, item (ii)).

The genuine frontier is whether HIGHER-GENUS MC data (genus g >= 2)
can supply the missing information. This is the content of the arithmetic
comparison conjecture, item (iii): the residue of the frontier defect form
Omega_A at each scattering pole s = rho/2 should be computable from
{Theta_A^{(g)}}_{g >= 2}. Whether this is possible is the deepest open
question in the arithmetic programme.


## 10. Summary Verdict

**Gap A is real, structural, and honestly stated in the manuscript.**

The bridge from algebraic (bar-cobar) to analytic (scattering) exists for
lattice VOAs because the lattice provides the Z-form, Hecke action, and
prime-by-prime decomposition that define the notion of "prime" in this
context. The rational primes p ARE the primes of the chiral algebra in the
lattice case -- they index the sublattice structure of Lambda.

For non-lattice algebras, the notion of "prime" is undefined because there is
no lattice, no Z-form, no canonical integral structure. The shadow obstruction tower
coefficients S_r are global invariants (rational functions of c), not local
data at individual primes. The MC recursion couples all arities and does not
respect coprimality.

The manuscript's own conclusion (rem:algebraic-analytic-divide) is correct:
the MC equation organizes the algebraic face completely, and every analytic
conclusion requires independent external input. The single open hypothesis
for the Ramanujan bound is prime-locality. For lattice VOAs, this is proved.
For everything else, it is the central open problem.

The most penetrating question is whether the shadow obstruction tower at the
shadow-projection level (Sh_r, not Z) has Euler product structure even when
the partition function does not. The shadow arithmetic trichotomy suggests
this is possible (Level 2 multiplicativity proved at arity 2, open at r >= 3).
If true, it would mean the MC element encodes a notion of "prime" that the
partition function obscures. This would be a genuinely new arithmetic
structure, not reducible to classical notions.


---

*Generated 2026-04-01. Source files: concordance.tex (lines 6920-7050),
arithmetic_shadows.tex (full chapter, ~9200 lines). Compute infrastructure:
prime_locality_minimal_model.py, euler_product_from_mc.py, sewing_euler_product.py,
shadow_level_arithmetic.py, hecke_defect.py, vvmf_hecke.py.*
