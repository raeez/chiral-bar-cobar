# Langlands Correspondence for Chiral Algebras: Analysis

## 1. Analogy vs Genuine Instance

### The classical Langlands correspondence

For a number field K, the Langlands programme is a web of conjectures
and theorems relating two kinds of objects:

- **Automorphic side**: Automorphic representations pi of GL_n(A_K),
  characterized by their L-functions L(s, pi) with Euler products,
  analytic continuation, and functional equations.

- **Galois side**: Continuous homomorphisms rho: Gal(K-bar/K) -> GL_n(Q_l),
  characterized by their Artin L-functions
  L(s, rho) = prod_p det(1 - rho(Frob_p) p^{-s})^{-1}.

The correspondence asserts L(s, pi) = L(s, rho): the same L-function
arises from both sides. The geometric Langlands programme (Beilinson,
Drinfeld, Frenkel, Gaitsgory, Raskin, et al.) is the function-field
analogue, where K = k(X) for a curve X/k, and both sides become
categories of sheaves:

    D-mod(Bun_G(X))  <-->  IndCoh(LocSys_{G^v}(X))

proved categorically in [GLC24] for G = GL_n over algebraically
closed fields of characteristic zero.

### What the manuscript constructs

The manuscript's "Langlands" programme for chiral algebras has three
components, which must be evaluated separately:

**(I) Critical level: bar complex = opers (GENUINE, LOCAL).**
At k = -h^v, the bar complex B(g-hat_{-h^v}) is uncurved and:

    H^n(B(g-hat_{-h^v})) = Omega^n(Op_{g^v}(D))    (thm:oper-bar)

This IS a genuine piece of the geometric Langlands correspondence.
The Feigin-Frenkel center z(g-hat_{-h^v}) = Fun(Op_{g^v}(D)) is the
LOCAL oper story, and the bar complex provides a chain-level
enhancement recovering the full differential-form package. Combined
with the FLE (Raskin [Raskin24]) identifying critical-level modules
with the Whittaker category, this places the bar construction
inside the categorical geometric Langlands framework.

However, this is the LOCAL statement on the formal disk D. The global
geometric Langlands correspondence involves Bun_G(X) and LocSys(X)
on a curve X, and the localization from the critical-level category
to D-modules on Bun_G is a separate (now proved) theorem. The bar
complex gives a concrete model for the local piece, not the global
correspondence.

**Verdict on (I)**: Genuine instance of local geometric Langlands.
The bar construction at critical level is a computational model for
the oper side. This is not an analogy; it is a theorem.

**(II) Off-critical shadow obstruction tower: arithmetic data from Theta_A
(STRUCTURAL ANALOGY, not genuine Langlands).**
At generic level kappa != 0, the shadow obstruction tower {S_r} encodes:

- For lattice VOAs: Hecke eigenform data via the period-shadow
  dictionary (thm:shadow-spectral-correspondence). The shadow
  at arity r detects the (r-3)-th cusp eigenform in the Hecke
  decomposition of Theta_Lambda. This gives L-functions
  L(s, f_j) from the Epstein zeta factorization.

- For non-lattice algebras (Virasoro, W_N): symmetric power
  traces via prop:shadow-symmetric-power. The MC equation at
  all arities encodes Newton's identities on the Satake
  parameters.

This is a STRUCTURAL ANALOGY with Langlands, not a genuine instance.
The reasons are precise:

(a) The L-functions produced are ALREADY KNOWN. For lattice VOAs,
the Hecke decomposition of Theta_Lambda gives L(s, f_j) by
classical Hecke theory. The shadow obstruction tower provides a new proof
route to these L-functions, not new L-functions. For Virasoro,
no L-functions are produced at all (d_arith = 0 for Ising;
the infinite shadow obstruction tower detects the algebra, not arithmetic).

(b) There is no Galois side. The Koszul involution A |-> A! is
called the "Galois involution" by analogy, but it is not a Galois
action. It is an algebraic duality on chiral algebras (Verdier
duality on Ran(X)), not a group action of Gal(K-bar/K) on
l-adic cohomology. The complementarity kappa(A) + kappa(A!)
= rho * K (Theorem D) is a constraint on modular characteristics,
not a reciprocity law.

(c) The automorphic objects are constructed over function fields
(complex curves), and the arithmetic descent to number fields
(Gap B) is completely absent. The shadow programme does not
even formulate what a number-field analogue would look like.

(d) The passage from algebraic MC data to analytic L-functions
(Gap C) requires the shadow series to converge and the moment
L-function M_r(s) to have an Euler product (prime-locality,
conj:prime-locality-transfer). Prime-locality is PROVED for
lattice VOAs and OPEN for all others. Without prime-locality,
the MC equation gives polynomial relations on power sums but
not the analytic continuation that Langlands requires.

**Verdict on (II)**: Structural analogy. The shadow obstruction tower
organizes arithmetic data in a way that resembles the automorphic
side, but it lacks the Galois/spectral side, the arithmetic descent,
and the analytic continuation that would make it genuine Langlands.

**(III) Prime-locality + Ramanujan chain (CONDITIONAL, USES Langlands).**
The twelve-station march:

    MC -> HS-sewing -> RS unfolding -> M_r(s) meromorphic
    -> [CPS converse theorem] -> pi_r in Aut(GL(r))
    -> [prime-locality] -> M_r = Sym^{r-1}
    -> [Serre reduction] -> Ramanujan

This chain USES the Langlands programme (CPS converse theorem,
strong multiplicity one, Langlands functoriality for Sym^r),
it does not PROVE it. The MC equation provides INPUT to the
Langlands machine; the Ramanujan bound is the OUTPUT. The
novel contribution is the input route (MC -> symmetric power
traces), not the Langlands machinery itself.

**Verdict on (III)**: Uses Langlands, does not prove or constitute
Langlands. The novel mathematical content is the MC-to-symmetric-power
identification, which is interesting independent of Langlands.

### What would need to be TRUE for genuine Langlands

For the shadow programme to constitute a genuine instance of the
Langlands correspondence, one would need:

1. **A spectral/Galois side**: An independent construction of
   Galois representations or local systems from chiral algebra
   data, such that L(s, rho) matches the shadow L-functions.
   Currently absent. The Koszul dual A! is an algebraic dual,
   not a Galois representation.

2. **Reciprocity**: A theorem identifying shadow obstruction tower data with
   Galois-theoretic data. Something of the form:
   "For every modular Koszul algebra A over a number field,
   the shadow spectral measure rho_A determines a compatible
   system of Galois representations." No such statement exists
   or is conjectured in the manuscript.

3. **Functoriality**: The MC equation at all arities giving
   Langlands functoriality (Sym^r transfer from GL(2) to GL(r+1)).
   This is the content of the prime-locality conjecture
   (conj:prime-locality-transfer), which is open for non-lattice
   theories and, for lattice theories, follows from classical
   Hecke theory without the MC equation.

4. **New L-functions**: The construction should produce L-functions
   not already accessible by other methods. Currently, all
   L-functions produced by the shadow programme are classical
   (zeta, Dedekind, Hecke L-functions of modular forms).

## 2. Assessment of the Three Langlands Gaps

### Gap A: Bar-cobar vs scattering (rem:langlands-gap-a)

**Statement**: Twisting morphisms (algebraic, chain-level, on Ran(X))
vs scattering amplitudes (analytic, on the complex s-plane).

**Assessment**: This is a CORRECT and DEEP gap. It is not merely a
technical difficulty; it is a categorical mismatch. The twisting
morphism tau: B(A) -> A is a morphism of factorization algebras;
a scattering amplitude phi(s) = Lambda(1-s)/Lambda(s) is a
meromorphic function on C whose poles encode L-function zeros.
The Mellin transform bridges them for specific objects (lattice
VOAs via the sewing determinant), but the bridge is not functorial
in the algebra A.

**Missing from Gap A**: The gap understates the problem. Even for
lattice VOAs where the Mellin bridge exists, the resulting
L-functions are the SAME L-functions one gets from classical
Hecke theory. The shadow programme provides a new proof route,
not new mathematical objects. The gap should also note that the
Rankin-Selberg unfolding ERASES the MC structure
(thm:structural-separation): the unfolded integral depends only
on the Fourier coefficients, not on the convolution-algebraic
structure that the MC equation controls. This means the MC
equation constrains the COEFFICIENTS of the spectral
decomposition (the c_j in Theta = c_E E_k + sum c_j f_j),
but the L-functions L(s, f_j) are properties of the eigenforms
f_j, which are independent of the algebra A.

### Gap B: Arithmetic descent (rem:langlands-gap-b)

**Statement**: Function field (complex curves) vs number field.

**Assessment**: This is CORRECT and is the standard deepest
problem in the Langlands programme. However, the gap description
is somewhat misleading in context. The geometric Langlands
programme IS a function-field story and IS now proved (GLC24).
The manuscript's critical-level bar/oper identification is
perfectly well-placed within geometric Langlands without
needing arithmetic descent. Gap B applies specifically to the
shadow obstruction tower's arithmetic claims (Ramanujan, L-functions),
not to the critical-level identification.

**A more precise formulation**: Gap B should distinguish between:
- (B1) Geometric Langlands at critical level: no gap
  (the bar complex computes opers, which is geometric Langlands).
- (B2) Arithmetic Langlands from shadow data: fundamental gap
  (shadow data lives over C, Langlands needs number fields).
The manuscript conflates these by treating "Langlands" as a
single programme.

### Gap C: Formal vs convergent (rem:langlands-gap-c)

**Statement**: Shadow obstruction tower is perturbative (formal power series
in arity); L-functions need non-perturbative analytic continuation.

**Assessment**: This is CORRECT but is actually a CONSEQUENCE of
a deeper obstruction, not an independent gap. The shadow obstruction tower's
formal nature is a feature of the algebraic MC equation: Theta_A
is a formal power series in the arity variable because it is
defined by a recursive obstruction tower. The convergence question
(whether rho(A) < 1) is interesting but is NOT the fundamental
issue. Even if the shadow series converges absolutely (as it does
for class G/L/C algebras where it terminates), the resulting
function is a POLYNOMIAL in the arity variable, not a meromorphic
function on the s-plane. The passage from arity-expansion to
s-plane requires the Mellin transform, which is Gap A.

**Deeper obstruction not captured by Gaps A-C**: There is a fourth
gap that the manuscript does not explicitly identify:

### Gap D: Absence of a spectral/Galois side

The Langlands correspondence is a CORRESPONDENCE: it requires two
sides and a matching between them. The manuscript constructs one
side (shadow/automorphic data from the MC element) but has no
construction of the other side (Galois representations or local
systems). The Koszul involution A |-> A! is not a Galois action;
it is an algebraic duality. The complementarity theorem
(Theorem C) is a constraint on the duality, not a reciprocity law.

Without a spectral/Galois side, there is nothing to correspond TO.
This is not a gap that can be bridged by further analysis of the
shadow obstruction tower; it requires an entirely new construction. One
possible source: if the bar complex at critical level computes
opers (Galois/spectral objects), and the shadow obstruction tower at generic
level deforms the critical story, then perhaps the deformed
shadow obstruction tower computes deformed opers. This leads to Question 4
below.

### Gap E: The moment problem (rem:structural-obstruction)

The manuscript correctly identifies that the scattering matrix
phi(s) has poles at complex spectral parameters, while the MC
equation constrains real spectral parameters. This is the
classical MOMENT PROBLEM: knowing all moments (shadow
coefficients) does not uniquely determine a distribution on the
complex plane. The Hamburger moment problem has a unique
solution when the Carleman condition is satisfied (verified for
Virasoro), but this gives uniqueness of the real spectral measure,
not the location of complex poles.

**Summary**: Gaps A and B are correct and fundamental. Gap C is
correct but derivative of Gap A. There are two additional gaps
(D and E) that are at least equally fundamental.

## 3. Feigin-Frenkel and the Bar Construction at Critical Level

### The precise statement

At k = -h^v:

    H^0(B(g-hat_{-h^v})) = z(g-hat_{-h^v}) = Fun(Op_{g^v}(D))
    H^n(B(g-hat_{-h^v})) = Omega^n(Op_{g^v}(D))   for all n >= 0

The first isomorphism is the Feigin-Frenkel center (proved by
Feigin-Frenkel, cited as thm:ff-center-dl). The full cohomological
package uses Frenkel-Teleman (FT06) via the bar-Ext identification.

### Is this "the" geometric Langlands correspondence?

**Short answer**: It is the LOCAL piece of the spectral side of
geometric Langlands, not the full correspondence.

**Detailed analysis**:

The geometric Langlands correspondence (GLC24) is:

    D-mod(Bun_G(X)) = IndCoh(LocSys_{G^v}(X))

as categories. This involves:
- A GLOBAL curve X (not just the formal disk D).
- The moduli stack Bun_G(X) of G-bundles on X.
- The moduli stack LocSys_{G^v}(X) of G^v-local systems on X.
- D-modules on Bun_G (automorphic side).
- IndCoh on LocSys (spectral side).

The bar complex at critical level gives the LOCAL spectral data:
functions and forms on the oper space Op_{g^v}(D) on the formal
disk. This is one ingredient in the spectral side (opers are a
special locus inside LocSys), not the full correspondence.

The relationship to the full geometric Langlands is:

1. The FLE (Raskin) identifies critical-level g-hat-modules with
   the Whittaker category, which is the automorphic side restricted
   to a particular stratum.

2. The localization theorem (Frenkel-Gaitsgory, now part of GLC24)
   relates critical-level modules to D-modules on Bun_G.

3. The oper space is the base of the Hitchin fibration, which
   provides the spectral side's geometry.

The bar construction provides a CHAIN-LEVEL MODEL for step 1:
it gives a concrete cochain complex whose cohomology computes
the oper data. This is a computational tool within geometric
Langlands, not the correspondence itself.

**What IS genuinely new**: The bar construction gives a unified
framework in which:
- The critical level recovers opers (H^* = Omega^*(Op)).
- The generic level recovers deformation theory (Theta_A, kappa).
- The admissible level conjecturally recovers quantum group
  categories (KL equivalence, periodic CDG structure).

This interpolation across levels is new and is not visible in
the original Langlands framework, where different levels are
treated separately. The bar complex provides a SINGLE algebraic
object that, as k varies, moves between geometric Langlands
(k = -h^v), deformation theory (generic k), and quantum groups
(admissible k).

## 4. The Shadow Tower as a Deformation of the Oper Story

### Critical level: Theta_A = 0, bar cohomology = opers

At k = -h^v: kappa = 0, the bar complex is uncurved,
H^*(B(g-hat_{-h^v})) = Omega^*(Op_{g^v}(D)), and the MC element
Theta_A = 0 (the OPE structure constants vanish for the
commutative critical-level algebra; see rem:dk-shadow-status
in concordance.tex). The shadow obstruction tower is trivial.

### Generic level: Theta_A != 0, curved bar, shadow obstruction tower nontrivial

At k != -h^v: kappa != 0, the bar complex is curved (d^2 = [kappa * omega_g, -]),
ordinary cohomology is undefined, and the MC element Theta_A != 0
controls the full shadow obstruction tower.

### What do the opers deform into?

This is the central mathematical question. The answer requires
distinguishing several deformation-theoretic layers:

**(a) The center deforms into the W-algebra.**
At critical level, z(g-hat_{-h^v}) = Fun(Op_{g^v}(D)). Away from
critical level, the center becomes trivial (z = C for generic k),
but the W-algebra W^k(g) (defined by Drinfeld-Sokolov reduction)
is the correct replacement. The W-algebra at generic level is NOT
commutative; its OPE encodes the shadow obstruction tower.

**(b) The oper space deforms into the MC moduli space.**
At critical level, the uncurved bar complex has cohomology
Fun(Op). Away from critical level, the curved bar complex has no
cohomology, but it has the MC moduli space MC(g^mod_A) and its
projections. The shadow Postnikov tower Theta_A^{<= r} is
the finite-order approximation to the universal MC element.
In this sense, the shadow obstruction tower IS the deformation of the oper
space.

However, this identification is at the level of formal deformation
theory, not at the level of algebraic geometry. The oper space
Op_{g^v}(D) is a smooth affine scheme. The MC moduli space is a
derived moduli problem. These are different types of objects.

**(c) The differential-form package deforms into the shadow algebra.**
At critical level, Omega^n(Op) is the n-th bar cohomology. Away
from critical level, the shadow algebra A^sh = H_*(Def_cyc^mod(A))
replaces the cohomology ring. The shadow coefficients (kappa, C,
Q, ...) are graded components of A^sh, playing the role that
the polynomial generators of Fun(Op) play at critical level.

### Is the shadow obstruction tower a deformation of the space of opers?

**Not precisely, but there is a meaningful sense in which it is.**

The precise relationship is:

At k = -h^v + epsilon (infinitesimal deformation from critical level):
- kappa = epsilon * (dim g) / (2h^v) + O(epsilon^2)
- The bar complex acquires curvature proportional to epsilon
- The MC element Theta_A = epsilon * Theta_1 + O(epsilon^2)
- The first shadow coefficient S_2 = kappa is the leading
  deformation parameter

The Feigin-Frenkel involution k |-> -k - 2h^v sends kappa |-> -kappa,
so the deformation in the positive kappa direction (A) and
negative kappa direction (A!) are related by Koszul duality.
At the critical point kappa = 0, the oper space sits as the
common limit of both deformations.

What the shadow obstruction tower captures is NOT the deformation of Op_{g^v}(D)
as a scheme, but rather the deformation of the ALGEBRAIC STRUCTURE
on Omega^*(Op). Specifically:
- At critical level: H^0 is commutative, H^1 is the module of
  Kahler differentials, the multiplication is the wedge product.
- Away from critical level: these structures are replaced by
  the MC equation, the shadow bracket, and the convolution
  algebra product. The commutativity of H^0 is broken by the
  curvature.

In the language of derived algebraic geometry, the critical-level
bar complex is a commutative cdga model for Omega^*(Op). The
generic-level bar complex is a CURVED cdga, which is a
noncommutative deformation. The shadow obstruction tower records the Taylor
coefficients of this deformation.

**In summary**: the shadow obstruction tower is the Taylor expansion of the
deformation of the oper differential-form algebra, not the
deformation of the oper space itself. The oper space does not
deform (it is the space of g^v-connections of a specific type);
what deforms is the ALGEBRA of functions/forms on it, which
becomes curved and noncommutative.

## 5. Testable Predictions

### What "Langlands for chiral algebras" would predict

If the shadow programme were a genuine Langlands correspondence,
it would predict specific identities between shadow obstruction tower data
and Galois-theoretic data. Here are the testable consequences,
organized by what is proved, what is conjectural, and what is
absent:

### Already proved (not new predictions)

**P1. Lattice L-functions from the shadow obstruction tower.**
For lattice VOAs, the shadow-spectral correspondence
(thm:shadow-spectral-correspondence) recovers the Hecke
L-functions of the theta function. This is proved, but the
L-functions are the same ones obtained from classical Hecke
theory. The shadow obstruction tower provides a new proof route, not new
data.

**P2. Depth = 1 + critical lines (lattice case).**
The shadow depth d(V_Lambda) = 3 + dim S_{r/2} counts the
number of L-functions in the Epstein zeta factorization.
Proved for lattice VOAs. Not applicable to non-lattice theories
where d_arith = 0.

**P3. Critical-level bar = opers (local geometric Langlands).**
H^n(B(g-hat_{-h^v})) = Omega^n(Op_{g^v}(D)). Proved. This IS
a genuine piece of geometric Langlands.

### Conditional predictions (require prime-locality)

**P4. Ramanujan bound from MC equation.**
Conditional on prime-locality (conj:prime-locality-transfer):
the MC equation at all arities, combined with the CPS converse
theorem and Serre's reduction, implies the Ramanujan bound for
Hecke eigenforms detected by the shadow obstruction tower. For lattice VOAs,
prime-locality is proved, giving an alternative route to
Ramanujan (but still using Langlands functoriality).

**P5. Symmetric power L-functions from shadow coefficients.**
Conditional on prime-locality: the shadow coefficient S_r
encodes the Dirichlet coefficients of L(s, Sym^{r-1} f)
(prop:shadow-symmetric-power). This would give a new source
for symmetric power L-functions, but requires Langlands
functoriality (GL(2) -> GL(r+1)) for r >= 5.

### Genuinely testable (accessible without new Langlands input)

**P6. Prime-locality at leading order in 1/c for Virasoro.**
The shadow coefficients S_r for Virasoro at leading order in
1/c are trivially prime-local (they depend on c alone, not on
primes). The first nontrivial test is at subleading order.
This is accessible by explicit computation of the genus-1
shadow amplitudes and their Fourier expansion.

**P7. Multiplicativity failure for non-lattice theories.**
Proved (prop:rational-cft-multiplicativity-failure): the
partition function Dirichlet coefficients of rational CFTs
are NOT multiplicative. This means the naive prime-locality
programme fails at the partition-function level. Whether
it holds at the shadow-projection level (Sh_r, not Z) is
the open question.

**P8. Arithmetic comparison conjecture (conj:arithmetic-comparison).**
The conjecture that Theta_A canonically determines the
arithmetic packet connection nabla^arith_A is testable in
principle: for each family, compute Theta_A and nabla^arith
independently and check whether the MC element determines
the connection. For lattice VOAs this should be verifiable
by explicit computation.

### Absent predictions (would be needed for genuine Langlands)

**P9. Galois representations from chiral algebras.**
A genuine Langlands correspondence would predict that every
modular Koszul algebra A determines a compatible system of
l-adic Galois representations. No such prediction exists.

**P10. Reciprocity law.**
A genuine Langlands correspondence would predict an identity
L(s, pi_A) = L(s, rho_A) where pi_A is the automorphic
representation from the shadow data and rho_A is the Galois
representation from the chiral algebra. No such identity exists.

**P11. New L-functions.**
A genuine Langlands programme would produce L-functions of
new automorphic objects (e.g., automorphic forms on G/K for
exceptional G), not merely recover classical L-functions of
modular forms. The shadow programme produces no new L-functions.

## Summary of Findings

### Classification

| Component | Status | Type |
|---|---|---|
| Critical-level bar = opers | PROVED | Local geometric Langlands (genuine) |
| Shadow-spectral correspondence (lattice) | PROVED | Classical Hecke theory by new route |
| Prime-locality + Ramanujan chain | CONDITIONAL | Uses Langlands, does not prove it |
| Koszul duality as "Galois involution" | ANALOGY | Not a Galois action |
| Arithmetic comparison conjecture | OPEN | Would strengthen the analogy |
| Shadow obstruction tower = deformation of opers | PARTIAL | Deformation of the algebra, not the space |

### The three Langlands gaps: assessment

| Gap | Correct? | Assessment |
|---|---|---|
| A (bar-cobar vs scattering) | Yes | Correct and fundamental; understates the Rankin-Selberg erasure problem |
| B (arithmetic descent) | Yes | Correct but should distinguish geometric (no gap) from arithmetic (fundamental gap) |
| C (formal vs convergent) | Yes | Correct but derivative of Gap A; convergence is necessary but not sufficient |

### Additional gaps not identified in the manuscript

| Gap | Description |
|---|---|
| D (no spectral/Galois side) | No construction of Galois representations from chiral algebras |
| E (moment problem) | Real spectral constraints cannot reach complex scattering poles |

### Bottom line

The manuscript is HONEST about the gaps (remarkably so for a
2000+ page monograph). The critical-level story is genuine local
geometric Langlands. The off-critical shadow programme is a rich
structural analogy that organizes arithmetic data through the MC
equation, but it is not a Langlands correspondence. The decisive
missing ingredients are: (1) a spectral/Galois side, (2) new
L-functions, and (3) a reciprocity law. The prime-locality
conjecture, if proved for non-lattice theories, would strengthen
the analogy significantly but would not close these three gaps.

The most promising direction for genuine Langlands content is the
INTERPOLATION across levels: the bar complex interpolates between
opers (k = -h^v), deformation theory (generic k), and quantum
groups (admissible k). If this interpolation can be understood
geometrically (as a family of spectral objects parametrized by k),
it would provide the spectral side that the current programme lacks.
The admissible-level periodic CDG structure (conjectured) and its
relationship to the Kazhdan-Lusztig equivalence is the natural
candidate for this geometric understanding.
