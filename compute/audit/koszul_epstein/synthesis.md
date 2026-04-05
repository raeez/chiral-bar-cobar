# The Koszul-Epstein Programme: Definitive Assessment

## Date: 2026-04-01

## Sources consulted

- raeeznotes105.md (the full 19K-line research log)
- compute/audit/descent_chain/ (10 analysis files, especially synthesizer_assessment.md)
- chapters/connections/arithmetic_shadows.tex (the manuscript chapter)
- The full compute test suite (euler_koszul_engine, dirichlet_sewing, shadow tests)
- Beilinson Principle and all 32 anti-patterns

---

## 1. Is the Koszul-Epstein programme viable? Or is it killed by Davenport-Heilbronn?

**It is not killed by Davenport-Heilbronn, but neither is it viable in its original form.**

The Davenport-Heilbronn argument shows that generic Epstein zeta functions
of non-unimodular lattices (class number h(D) >= 2) have zeros OFF the
critical line. This definitively kills the naive claim:

> "bar-cobar homotopy equivalence forces Epstein zeros onto Re(s) = 1/2"

That claim is FALSE and was correctly identified as false in rn105 itself.

However, Davenport-Heilbronn does NOT kill the narrower programme, because
the "Koszul-Epstein" subclass is defined precisely to exclude the generic
Epstein case. The question is whether the Koszul-Epstein subclass has
enough additional structure to support a critical-line theorem.

**The honest answer: no mechanism has been identified that would make
Koszul-Epstein functions satisfy RH.** The programme has identified
WHAT ADDITIONAL STRUCTURE EXISTS (see Section 2 below), but none of
that structure has been shown to force zeros onto the critical line.
The programme is alive in the sense that no counterexample has killed
it within its own terms; it is inert in the sense that no positive
result has been proved beyond what was already known from the theory
of L-functions.

---

## 2. Precise additional structure that Koszul-Epstein functions have beyond generic Epstein

### Structure 1: MC recursion on shadow coefficients

**What it is.** The MC equation D Theta + (1/2)[Theta, Theta] = 0 at arity
r+1 imposes a polynomial relation on the shadow coefficients {S_2, ..., S_{r+1}}.
This is proved (thm:mc-recursion-moment). The recursion is:

    S_r = -(1/(2r)) sum_{j+k=r+2, j,k>=2} j*k*S_j*S_k*P

where P is the propagator. For r >= 2m+2 (m = number of spectral atoms),
the system is overdetermined (prop:mc-constraint-counting): more equations
than unknowns.

**Does it help with the critical-line question?** NO. The MC recursion
constrains the MOMENTS of the spectral measure. Moments constrain the
MEASURE (uniquely, by Carleman -- see Section 3). The measure constrains
the ZEROS of the associated Dirichlet series. But this chain has two
fatal gaps:
(a) Moment constraints are algebraic; zero locations are transcendental.
    No algebraic identity among moments forces zeros onto a line.
(b) The spectral measure rho of the shadow obstruction tower is NOT the same object
    as the spectral measure of the automorphic Laplacian (rem:moment-
    problem-vs-zero-location in the manuscript). The zeros of zeta live
    in the SCATTERING MATRIX phi(s) = Lambda(1-s)/Lambda(s), not in the
    shadow measure.

### Structure 2: Carleman uniqueness of the spectral measure

**What it is.** The shadow moments {S_r} satisfy Carleman's condition:
sum |S_r|^{-1/(2r)} = infinity (because |S_r|^{-1/(2r)} -> (|c|/6)^{1/2}).
Therefore the Hamburger moment problem has a unique solution
(prop:carleman-virasoro). The spectral measure rho is UNIQUELY determined
by the shadow obstruction tower.

**Does it help?** PARTIALLY. It means the MC recursion, which determines all
moments from low-arity data, determines the spectral measure uniquely.
This is a genuine rigidity result: the infinite tower is controlled by
finitely many parameters. But uniqueness of rho does not determine the
zeros of the associated Dirichlet/Epstein series. The map from moments
to zeros is highly non-explicit (it goes through the Stieltjes transform,
not through any algebraic relation), and it is NOT positivity-preserving.

### Structure 3: Euler-product structure for Heisenberg (sewing determinant)

**What it is.** The Heisenberg sewing Fredholm determinant satisfies

    log det(1 - K_q) = -sum_{N>=1} sigma_{-1}(N) q^N

and sigma_{-1}(N) is multiplicative, giving the Euler product

    sum sigma_{-1}(N) N^{-s} = zeta(s)*zeta(s+1) = prod_p (1-p^{-s})^{-1}(1-p^{-s-1})^{-1}

**Does it help?** NO, beyond what was already known. The Euler product
is simply the product of two Riemann zeta functions. The zeros of
zeta(s)*zeta(s+1) lie on Re(s) = 1/2 and Re(s) = -1/2 IF AND ONLY IF
RH holds for zeta(s). The Koszul-Epstein structure does not add to what
is already known about zeta.

### Structure 4: Complementarity (kappa + kappa' constraints)

**What it is.** The Koszul involution A -> A! constrains:
- kappa(A) + kappa(A!) = 0 (for KM/free fields)
- kappa(A) + kappa(A!) = 13 (for Virasoro)
- Delta(A) + Delta(A!) = 6960/[(5c+22)(152-5c)]

**Does it help?** NO. The complementarity acts on the ARITY variable t,
not on the spectral variable u. The sewing lift S_A(u) depends only on
the conformal weight multiset W(A) = {w_i}, which is INDEPENDENT of
the central charge c. Therefore S_{Vir_c}(u) = S_{Vir_{26-c}}(u) for
all c. Complementarity is a constraint among shadow coefficients, not a
functional equation of S_A(u). (Proved in level_2_3_functional_equation.md.)

### Structure 5: Verdier-Hecke commutation

**What it is.** Verdier duality on the bar coalgebra commutes with Hecke
operators (thm:hecke-verdier-commutation). For self-dual algebras at c=13,
this forces the constrained Epstein zeta to factor into standard
L-functions (sec:koszul-self-duality-principle).

**Does it help?** THIS IS THE MOST PROMISING STRUCTURE, but it applies
only at the self-dual point c=13. For generic c, the Koszul dual is a
DIFFERENT algebra, not a symmetry of the same object. The factorization
into L-functions at self-dual points is a structural theorem, not a
critical-line theorem.

### Structure 6: Quartic resonance class with clutching law

**What it is.** The quartic resonance class R_4^mod(A) is the first
genuinely nonlinear shadow of Theta_A, with a clutching law from Mok's
log FM degeneration (constr:arity4-degeneration). For Virasoro:
Q^contact = 10/[c(5c+22)].

**Does it help?** IN PRINCIPLE this is where the programme becomes
nonlinear and where new information beyond the character could live.
But the quartic residue-matrix test (the Gram-side Schur complement)
has been computed for Liouville and A_2-Toda with genuine spectral
measures, and the mismatch is 4-5 orders of magnitude (rn105, line 18825).
The quartic matching condition is not even approximately satisfied with
bare spectral measures. The crossing-weighted bilinear residue kernel
is needed, and that computation has not been done.

### Structure 7: Route C (MC rigidity forces character-level prime-locality)

**What it is.** Theorem thm:route-c-propagation proves: if the low-arity
shadow data (kappa, alpha) are determined by Hecke-equivariant character
data, then prime-locality propagates to all arities via the MC recursion.
Proved for the standard landscape (cor:route-c-standard-landscape).

**Does it help with critical-line?** NO. Prime-locality is about Euler-
product structure of the shadow coefficients as functions of the modular
parameter tau. It is NOT about the zeros of zeta or any Epstein function.
It is a genuine and proved arithmetic result about the shadow obstruction tower, but
it speaks to a different question.

---

## 3. Does the MC recursion constrain enough moments to determine the spectral measure uniquely (Hamburger/Carleman)?

**YES.** This is proved:

(a) The MC recursion at arity r+1 determines S_{r+1} from {S_2,...,S_r}
    (thm:mc-recursion-moment).

(b) For r >= 2m+2 (where m is the number of spectral atoms), the system
    is overdetermined (prop:mc-constraint-counting).

(c) The Carleman condition is satisfied (prop:carleman-virasoro):
    sum |S_r|^{-1/(2r)} = infinity.

(d) Therefore the Hamburger moment problem has a UNIQUE solution: the
    spectral measure rho is uniquely determined by finitely many
    parameters (kappa, alpha, S_4).

**This is a genuine theorem about the shadow obstruction tower.** The entire infinite
tower of shadow coefficients, and the unique spectral measure they
determine, are controlled by three numbers for each primary line.

---

## 4. If yes: does the MC-determined spectrum force zeros onto the critical line?

**NO.** Three independent obstructions:

(a) **Different spectral objects.** The shadow spectral measure rho (atoms
    at effective couplings lambda_i) and the automorphic spectral measure
    (Maass eigenvalues, scattering poles of the Laplacian on SL(2,Z)\H)
    are DIFFERENT objects (rem:moment-problem-vs-zero-location). The map
    from rho to the automorphic spectrum goes through the Rankin-Selberg
    integral. This map is injective for lattice VOAs (Hecke correspondence)
    but ill-conditioned for non-lattice theories. The structural
    obstruction (rem:structural-obstruction) is that this map is NOT
    surjective.

(b) **Real vs complex spectral data.** The MC equation constrains data on
    the REAL spectral axis (s = 1/2 + it, t real). The zeta zeros live
    at COMPLEX t. Algebraic constraints on the spectral line cannot reach
    scattering poles without analytic continuation off the real axis.
    (This is the content of the structural obstruction.)

(c) **No positivity mechanism.** Li positivity requires positive definiteness
    of a specific bilinear form. The MC equation is a FLATNESS condition
    (quadratic integrability), not a POSITIVITY condition. The chain

        MC -> Rankin-Selberg -> Li positivity

    does not close because the Rankin-Selberg transform is NOT
    sign-preserving. This was identified in rn105 and verified
    computationally (the zeta-proxy test fails at the safe point sigma=1/2).

(d) **Li coefficients become negative.** For the Heisenberg sewing lift,
    the Li coefficients turn negative at n=7 (not because of off-critical
    zeros, but because the product zeta(u)*zeta(u+1) has zeros on TWO
    critical lines, Re=1/2 and Re=-1/2). For Virasoro, ALL Li coefficients
    are negative from n=1 (because zeta(u)-1 has no automorphic structure).

---

## 5. What is the HONEST status?

**The Koszul-Epstein programme is a well-posed research programme, not a
dead end, but not a viable path to a critical-line theorem either.**

More precisely:

### What is proved and genuine

1. The MC recursion uniquely determines the shadow spectral measure via
   Carleman (PROVED).

2. Prime-locality of the shadow obstruction tower for the standard landscape via
   Route C: MC overdetermination propagates Hecke equivariance (PROVED).

3. The shadow-spectral correspondence for lattice VOAs: shadow depth =
   number of critical lines minus 1 (PROVED).

4. Verdier-Hecke commutation forces L-function factorization at self-dual
   points (PROVED).

5. The quartic resonance class is the first nonlinear place where zeta
   zeros, Koszul duality, and modular geometry are forced to meet (DEFINED,
   not yet computed with correct crossing-weighted measures).

### What is false and must be dismissed

1. "Bar-cobar forces Epstein zeros onto the critical line" -- FALSE.
   Davenport-Heilbronn counterexamples exist for generic Epstein.
   Bar-cobar gives homotopy equivalence, not arithmetic positivity.

2. "MC implies Li positivity" -- FALSE. MC is flatness; Li is positivity.
   The Rankin-Selberg bridge is not sign-preserving.

3. "The shadow obstruction tower descends to a functional equation of S_A(u)" -- FALSE.
   The shadow obstruction tower acts on the arity variable t; the sewing lift acts on
   the spectral variable u. Complementarity does not produce a functional
   equation because S_A(u) is c-independent.

4. "Narain radius variation gives zero-location leverage" -- FALSE. Varying
   R changes coefficients, not zero locations.

5. "The zeta-proxy is a valid test" -- FALSE. It does not preserve the safe
   point sigma=1/2.

6. "Bare spectral measures close the quartic gap" -- FALSE. The mismatch
   is 4-5 orders of magnitude for Liouville/Toda (rn105, line 18825).

### What is open but meaningful

1. Whether the crossing-weighted bilinear residue kernel (not the bare
   spectral measure) satisfies the quartic Gram-side matching at on-line
   zeros. This is a well-defined computation requiring DOZZ/Toda structure
   constants and the modular transform kernel. UNTESTED.

2. Whether a modular-surface realization of the quartic Gram determinant
   admits a Hodge-index/Hodge-Riemann positivity argument. This would
   convert quartic compatibility into genuine positivity. CONJECTURAL.

3. Whether the simultaneous-family intersection

       cap_{A,g,n,u_0} {rho : D_{4,g,n}(A,rho;u_0) = 0} = {rho : Re(rho) = 1/2}

   could serve as a closure mechanism. CONJECTURAL, not even formulated as
   a precise conjecture.

### The classification

| Component | Status | Viability |
|-----------|--------|-----------|
| MC recursion -> moment determination | PROVED | Genuine theorem |
| Carleman uniqueness of spectral measure | PROVED | Genuine theorem |
| Route C prime-locality | PROVED | Genuine arithmetic result |
| Verdier-Hecke factorization | PROVED | Genuine at self-dual points |
| Shadow-spectral correspondence (lattice) | PROVED | Genuine |
| Quartic resonance + clutching | DEFINED | Genuine nonlinear object |
| MC -> Li positivity | KILLED | False idea |
| Bar-cobar -> critical line | KILLED | False idea |
| Complementarity -> FE of S_A | KILLED | False idea (different variables) |
| Quartic matching with bare measures | FAILED | 4-5 orders of magnitude mismatch |
| Quartic matching with crossing-weighted kernel | OPEN | Untested, correct formulation |
| Surface positivity | CONJECTURAL | No mechanism identified |
| Simultaneous-family closure | CONJECTURAL | Not formulated precisely |

---

## 6. Assessment of the rn105 conjectural statement

The rn105 synthesis states:

> "the right conjectural statement is not 'Koszul duality proves RH,' but
> rather: the universal modular MC class Theta_A, when pushed through
> Rankin-Selberg and paired by modular-surface polarization, should
> generate Li-type positivity constraints whose scalar shadow reproduces
> the zeta-zero asymptotics of the scalar bootstrap."

**This statement is HONEST in what it claims and OVEROPTIMISTIC in what
it implies.** Specifically:

(a) "Theta_A pushed through Rankin-Selberg" -- this is well-defined at
    genus 1 and produces the arithmetic shadow L_A(s,u). CORRECT.

(b) "paired by modular-surface polarization" -- no such pairing has been
    constructed. The modular surface (if it exists in the relevant
    derived-algebraic-geometric sense) would need to carry a polarization
    compatible with the quartic Gram determinant. NO CONSTRUCTION EXISTS.

(c) "should generate Li-type positivity constraints" -- the word "should"
    is doing all the work. No mechanism for positivity has been identified.
    The Hodge-index theorem on surfaces can give positivity of
    intersection numbers, but the connection between the quartic Gram
    determinant and intersection numbers on a modular surface is entirely
    conjectural. Furthermore, the Hodge-Riemann relations give positivity
    on the PRIMITIVE cohomology, and it is unknown whether the relevant
    classes are primitive.

(d) "whose scalar shadow reproduces the zeta-zero asymptotics of the
    scalar bootstrap" -- this would require the scalar shadow of the
    quartic Gram positivity to reduce to the Li coefficients. The Li
    coefficients for the Heisenberg turn negative at n=7 (or n=974 for
    the completed version). No scalar shadow of a positive Gram matrix
    should produce negative scalars, unless the matrix is not positive
    definite. So either the Gram matrix is not positive definite (killing
    the programme) or the scalar shadow is not the Li coefficients.

**The corrected statement should be:**

> The MC element Theta_A, through the graph sum and Rankin-Selberg integral,
> determines a regularized two-variable L-object L_A(s,u) whose quartic
> resonance section is the first nonlinear place where Koszul duality
> constrains the automorphic spectral decomposition beyond the character
> level. The proved content is: MC rigidity forces prime-locality of the
> shadow obstruction tower (Route C). Whether this L-object carries additional positivity
> or critical-line information beyond what is already contained in the
> automorphic spectral theory is an open question, with no positive evidence
> and no definitive obstruction.

This is weaker than the rn105 statement but more honest. The rn105
statement smuggles in a positivity mechanism ("surface polarization")
that does not exist, and a scalar-shadow identification ("reproduces
zeta-zero asymptotics") that is contradicted by the Li coefficient
computation.

---

## 7. The Beilinson verdict

**What must be dismissed NOW:**

1. Any claim that the Koszul-Epstein programme provides a path to RH.
   It does not. The programme identifies genuine algebraic structures
   (MC rigidity, Carleman uniqueness, Route C prime-locality, Verdier-
   Hecke factorization) but none of these is a critical-line theorem
   or a positivity result.

2. The "surface positivity" mechanism. No such surface has been constructed;
   no polarization has been identified; the Hodge-index argument is
   entirely hypothetical.

3. The "simultaneous-family closure" mechanism. The intersection of quartic
   compatibility loci over all families is not even formulated as a
   precise conjecture, and the computational tests with bare measures
   fail by 4-5 orders of magnitude.

4. The "scalar Li shadow" identification. Li coefficients for the
   Heisenberg become negative, contradicting any positive Gram matrix
   interpretation.

**What must be kept:**

1. The MC recursion + Carleman uniqueness theorem. This is a genuine
   and proved result about the internal structure of the shadow obstruction tower.

2. Route C prime-locality. This is a proved arithmetic theorem: the MC
   recursion propagates Hecke equivariance from low-arity character
   data to all arities, for the entire standard landscape.

3. The shadow-spectral correspondence for lattice VOAs. This is a proved
   theorem relating shadow depth to the number of critical lines.

4. The quartic resonance class as a mathematical object. Its definition,
   clutching law, and role as the first nonlinear shadow are genuine
   mathematics, independent of any connection to RH.

5. The observation that the naive Dirichlet/Epstein series over primaries
   is the wrong universal object for generic Virasoro/W_N. The correct
   object involves the crossing-weighted bilinear residue kernel, built
   from DOZZ/Toda structure constants.

**The meta-verdict:**

The Koszul-Epstein programme is an instance of a common pattern in
mathematics: genuine algebraic structure near a famous problem, but with
an unbridged gap between the algebraic content and the analytic conclusion.
The MC recursion, Carleman uniqueness, and Route C prime-locality are real
theorems about the arithmetic of modular Koszul algebras. They illuminate
the structure of the shadow obstruction tower and the arithmetic of the standard
landscape. They do NOT illuminate the zeros of the Riemann zeta function.

The programme should be recorded as a research programme that produced
genuine arithmetic results (prime-locality, shadow-spectral correspondence,
Verdier-Hecke factorization) and failed to produce a critical-line
theorem. The false ideas have been identified and dismissed. The surviving
content stands on its own mathematical merit, independent of RH.

---

## Files produced

- This synthesis: compute/audit/koszul_epstein/synthesis.md
- Vol I working notes: new section "The Koszul-Epstein frontier"
- Vol II working notes: new section "Koszul-Epstein and quantum gravity"
