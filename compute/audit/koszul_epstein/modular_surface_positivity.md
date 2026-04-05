# Modular Surface Positivity: Deep Analysis

## The question

Can the shadow obstruction tower, via the MC recursion on modular surfaces, supply
the positivity that the Li criterion requires? Specifically: can the
Hodge polarization on M-bar_{1,1} (or higher-genus moduli spaces),
combined with Koszul-structural constraints, force Li-type positivity
of Weil sums adapted to shadow test functions?

## Executive summary

**No.** The manuscript already contains a rigorous proof that this
programme is structurally blocked (Prop. 3463, `prop:li-criterion-failure`
in `arithmetic_shadows.tex`). The analysis below independently verifies
this obstruction, identifies why each proposed mechanism fails, and
states precisely what theorem would be needed to close the gap. The
missing lemma does not exist in any form that would follow from MC
constraints alone, and the Beilinson Principle demands that we say so.

---

## 1. The Weil explicit formula and shadow test functions

The Weil explicit formula for a Dirichlet series L(s,f) with
functional equation is:

  sum_rho h(rho) = (main terms) + sum_p log(p) * h-hat(log p) * (local terms)

For each shadow arity r, the shadow coefficient S_r determines a
test function h_r via the Mellin correspondence:

  M_r(s) = integral_{SL(2,Z)\H} Sh_r(Theta_A; tau) * E(s, tau) d mu(tau)

(Theorem `thm:mc-recursion-moment`). The question is whether the
collection {h_r}_{r >= 2} forms a sufficiently rich family to force
all Weil sums positive.

### 1.1. What the MC recursion gives

The MC recursion at arity r+1 gives:

  D * Sh_{r+1} + sum_{a+b=r+1} [Sh_a, Sh_b] = 0

This is a POLYNOMIAL relation between shadow amplitudes. Via the
Mellin correspondence (Prop. `prop:shadow-symmetric-power`), this
becomes Newton's identity:

  p_r = sum_{j=1}^{r} (-1)^{j-1} e_{r-j} p_j

connecting power sums p_r = sum lambda_j^r to elementary symmetric
polynomials of the spectral atoms {lambda_j}.

### 1.2. Shadow test functions are NOT arbitrary

The shadow test functions h_r are constrained by:

(a) The MC recursion (Newton's identities) -- each h_{r+1} is
    algebraically determined by h_2, ..., h_r.

(b) The shadow metric Q_L(t) = (2 kappa + 3 alpha t)^2 + 2 Delta t^2
    -- the generating function H(t) = t^2 sqrt(Q_L(t)) has algebraic
    branch points, so the h_r decay/grow at the rate determined by
    the shadow radius rho(A).

(c) Modularity -- each M_r(s) is a Rankin-Selberg transform of a
    modular-invariant function.

**These constraints HELP in the sense that they select a coherent
family of test functions, but they HURT in the sense that the family
is not dense in any function space relevant to the Li criterion.**

The Li criterion requires positivity of

  lambda_n = sum_rho [1 - (1 - 1/rho)^n]

for ALL n >= 1. This is a statement about a SPECIFIC family of test
functions h_n(s) = 1 - (1 - 1/s)^n. The shadow test functions {h_r}
are a DIFFERENT family. The Weil sums with shadow test functions being
positive does not imply the Li sums being positive, and vice versa.

---

## 2. Why modular surface positivity does not close Gap A

### 2.1. The structural obstruction (already proved)

Proposition `prop:li-criterion-failure` proves that the Li criterion
is structurally inapplicable to the sewing lift S_A(u) for EVERY
standard family. The root cause:

The sewing lift Xi_A(u) = (u-1) S_A(u) has zeros on AT LEAST TWO
critical lines:

- Heisenberg: Xi_H(u) = (u-1) zeta(u) * zeta(u+1)
  Zeros on Re(u) = 1/2 (from zeta(u)) AND Re(u) = -1/2 (from zeta(u+1))

- Virasoro: Xi_Vir(u) = (u-1) zeta(u+1) * (zeta(u) - 1)
  Zeros spread across ALL of R (from zeta(u) - 1, Bohr-Landau)

The Li criterion requires ALL zeros on a SINGLE line Re(u) = 1/2.
With zeros on two or more lines, |1 - 1/rho| > 1 for off-line zeros,
making (1 - 1/rho)^n grow exponentially and lambda_n exponentially
negative. This is STRUCTURAL, not a failure of test function choice.

**This obstruction is independent of any polarization or pairing.**
No positive-definite form on a modular surface can change the fact
that the sewing lift has zeros on multiple lines.

### 2.2. The Hodge polarization argument and its failure

The proposal: the Hodge class lambda on M-bar_{1,1} provides a natural
polarization. The shadow obstruction tower is the Taylor expansion of sqrt(Q_L) on
the tangent space of the shadow moduli. Could the POSITIVITY of the
Hodge polarization translate to Li-type positivity?

The answer is no, for three independent reasons:

**(a) Hodge positivity constrains weights, not eigenvalues.**

Proposition `prop:bracket-hodge-index` proves that the MC bracket
B(Sh_r, Sh_s) = [Sh_r, Sh_s]_{r+s-2} has definite signature on the
shadow space: positive-definite on the cusp-form subspace, Hodge-index
signature (1, d_arith - 1) on the Eisenstein subspace. This constrains
the WEIGHTS c_j in the Hecke decomposition (they must have definite
sign), but NOT the EIGENVALUES a_{f_j}(p).

The Ramanujan bound |a_{f_j}(p)| <= 2 p^{(k-1)/2} is a statement
about eigenvalues. The Hodge index constrains the c_j but is blind to
the Satake parameters alpha_p, beta_p. (Remark `rem:positivity-limitation`)

**(b) The Mellin transform is not sign-preserving.**

The Rankin-Selberg transform Sh_r -> M_r(s) is a Mellin integral.
Mellin transforms of positive functions CAN be negative. Even if
the MC data have definite sign with respect to the Hodge pairing,
the spectral transform M_r(s) evaluated at the zeta zeros need not
be positive. The claim that "surface polarization would require a
positive-definite pairing on a modular surface under which the MC
data have definite sign" is explicitly flagged as open in the
manuscript, with the assessment: "No candidate pairing has been
constructed" (Remark `rem:beilinson-four-gaps`, item (i)).

**(c) The bar-cobar quasi-isomorphism preserves homotopy type, not
positivity.**

The claim that "the quasi-isomorphism is STRONGER than a functional
equation -- it preserves the entire chain-level structure, including
positivity of the Hodge metric" requires scrutiny.

The bar-cobar quasi-isomorphism Omega(B(A)) -> A is a CHAIN-LEVEL
equivalence. It preserves:
- cohomology (by definition of quasi-isomorphism)
- A-infinity structure (by transfer)
- the Hodge CLASS lambda (by Theorem D)

It does NOT preserve:
- spectral positivity (absolute values of Hecke eigenvalues)
- the Li criterion (which is about zero locations, not chain-level
  data)
- Euler product structure (Gap C: Davenport-Heilbronn counterexamples
  have functional equations and quasi-isomorphic bar complexes but
  off-critical zeros)

The distinction is between HOMOTOPICAL strength (chain-level, algebraic)
and SPECTRAL-POSITIVE strength (analytic, absolute-value bounds).
Bar-cobar is strong in the first sense and irrelevant in the second.

---

## 3. Does the infinite family help?

### 3.1. Infinitely many arities -> infinitely many test functions

The shadow obstruction tower at class M algebras (Virasoro, W_N) gives infinitely
many arities and hence infinitely many test functions {h_r}_{r >= 2}.
Could the TOTALITY of these force all Weil sums positive?

No, because:

(i) The test functions are algebraically constrained (Newton's
identities). Each h_{r+1} is determined by h_2, ..., h_r. The space
of attainable test functions is a 2m-dimensional algebraic variety
(where m is the number of spectral atoms), not an infinite-dimensional
function space.

(ii) For class M algebras, m = infinity (continuous spectral support).
The rigidity defect delta(m, r) = r - 1 - 2m = -infinity at every
finite arity (Prop. `prop:rigidity-threshold`). The system is NEVER
overdetermined. No finite number of MC constraints produces
overdetermination when the spectral measure is continuous.

(iii) The shadow test functions probe the SAME spectral data (the
Hecke eigenvalues) at increasing powers. Knowing all power sums
sum lambda_j^r for r = 2, 3, ... determines the spectral measure
uniquely (by the moment problem), but does not constrain the
ABSOLUTE VALUES of the atoms. Knowing a polynomial's roots does not
determine their moduli.

### 3.2. The MC constraint selects a positive cone -- but the wrong one

The MC recursion D Theta + (1/2)[Theta, Theta] = 0 is an
INTEGRABILITY constraint: it says the deformation is flat, the
curvature vanishes, the differential squares to zero. This is
analogous to Frob^2 = q in the Weil proof.

In the Weil proof for curves over F_q, the key additional ingredient
is the Hodge-Riemann bilinear relations on H^1(C). These provide
positivity (the Castelnuovo-Hodge inequality) which, combined with
Frob^2 = q, forces |alpha_i| = q^{1/2}.

The MC bracket B(Sh_r, Sh_s) is the analogue of the Hodge-Riemann
form. And indeed it IS positive-definite on the cusp-form subspace
(Theorem `thm:petersson-identification`). But this positivity operates
on the WRONG object: it constrains the decomposition weights c_j, not
the spectral eigenvalues a_f(p).

In the Weil proof, the Hodge-Riemann form constrains the Frobenius
EIGENVALUES directly because:
- Frobenius acts on H^1, which carries the bilinear form
- The form is Galois-equivariant
- The eigenvalues of Frobenius on H^1 ARE the zeros of the zeta function

In the MC setting:
- The bracket acts on the SHADOW SPACE (projections of Theta)
- The shadow space parameterizes the WEIGHTS c_j, not the eigenvalues
- The eigenvalues are determined by the SPECTRAL MEASURE, which is
  a DIFFERENT object

The analogy breaks precisely at the point where it matters: the
Frobenius eigenvalues and the L-function zeros are THE SAME OBJECT
in the Weil proof, but the shadow bracket entries and the Hecke
eigenvalues are DIFFERENT OBJECTS in the MC setting.

---

## 4. The precise missing lemma

What theorem would close the gap from MC constraints to Li positivity?

### 4.1. Statement of the missing lemma

**Missing Lemma (does not exist):** There exists a positive-definite
pairing

  <.,.>_surf : Def_cyc^{(0,r)} x Def_cyc^{(0,r)} -> R

on the genus-0 shadow space such that:

(a) The MC equation D Theta + (1/2)[Theta, Theta] = 0 implies
    <Sh_r, Sh_r>_surf >= 0 for all r >= 2.

(b) For lattice VOAs, the Rankin-Selberg transform of <Sh_r, Sh_r>_surf
    equals sum_rho h_r(rho) where h_r are the Li test functions
    h_n(s) = 1 - (1 - 1/s)^n (NOT the shadow test functions).

(c) Positivity of <Sh_r, Sh_r>_surf for all r implies that all zeros
    of L(s, f_j) lie on the critical line.

### 4.2. Why it cannot exist

Condition (a) is achievable: the Petersson inner product provides such
a pairing for the cusp-form subspace.

Condition (b) is the fatal obstruction. It requires the pairing to
intertwine the shadow test functions (determined by the MC recursion)
with the Li test functions (determined by the binomial expansion
(1 - 1/s)^n). These are DIFFERENT families of test functions, and
no bilinear form can simultaneously:
- be positive-definite (condition a)
- map shadow amplitudes to Li coefficients (condition b)
- produce sign-definite Li sums (condition c)

because the Mellin transform is not sign-preserving (2.2(b) above).

More precisely: if such a pairing existed, it would have to satisfy

  <Sh_r, Sh_r>_surf = sum_rho [1 - (1 - 1/rho)^r]

But the right side is sum of (1 - (1-1/rho)^r) over ALL zeros rho.
For the sewing lift, these include zeros on Re(rho) = -1/2, where
|1 - 1/rho| > 1 and the contribution is exponentially negative.
No positive-definite pairing can produce an exponentially negative sum.

### 4.3. What WOULD suffice (but is not available)

The actual missing ingredient is one of:

**(Route A) Analytic continuation of symmetric power L-functions.**
If L(s, Sym^r f) has analytic continuation and satisfies GRH for ALL
r >= 1, then the Serre reduction gives the Ramanujan bound. The MC
equation supplies the algebraic data (Newton's identities on the
symmetric power traces) but NOT the analytic continuation. Known for
r <= 4 (Kim-Shahidi); open for r >= 5. This is Langlands functoriality
GL(2) -> GL(r+1).

**(Route B) The clutching closure conjecture.**
Conjecture `conj:clutching-closure`: the intersection of the
residue-clutching compatibility loci over all modular Koszul families
and all boundary strata of M-bar_{g,n} is exactly
{rho : Re(rho) = 1/2}. This bypasses the Li criterion entirely and
uses the full nonlinear modular structure (clutching law, proved from
Mok's degeneration formula) rather than scalar positivity. The decisive
chain is:

  Theta_A -> residue kernel -> residue Gram matrix -> Schur complement
  -> quartic resonance -> clutching law -> geometric zero test

Each arrow is either proved or explicitly defined; the conjectural
content is concentrated in the closure statement alone.

**(Route C) The operadic Rankin-Selberg theorem.**
Conjecture `conj:operadic-rankin-selberg-main`: the all-genera operadic
coherence of Theta_A provides the analytic continuation that Langlands
functoriality predicts. This would make the MC equation self-sufficient
for Ramanujan bounds. The CPS hypotheses (meromorphic continuation,
finitely many poles, polynomial growth, functional equation) are
verified for the moment L-function M_r(s) by Theorem `thm:cps-from-mc`.
The gap is assembling the global Euler product from the p-local factors.

---

## 5. Assessment of the five proposed mechanisms

### 5.1. "Shadow obstruction tower supplies ENOUGH test functions"

FALSE. The shadow test functions are a 1-parameter algebraic family
(indexed by arity r), not a dense subset of any function space. For
class M algebras, the spectral measure has continuous support and the
system is never overdetermined.

### 5.2. "MC constraint selects a positive cone"

TRUE but IRRELEVANT. The MC bracket is positive on the cusp-form
subspace (Theorem `thm:petersson-identification`), but this constrains
weights, not eigenvalues. The positive cone is the WRONG one for
Li positivity.

### 5.3. "Hodge polarization on M-bar_{1,1} translates to Li positivity"

FALSE. The Hodge class lambda = kappa at genus 1 provides a
polarization on the shadow moduli, but the Rankin-Selberg transform
from this polarized space to spectral sums is not sign-preserving.
The manuscript explicitly states: "No candidate pairing has been
constructed; the problem is open."

### 5.4. "Bar-cobar preserves Hodge class, hence preserves positivity"

CONFLATION. Bar-cobar preserves the Hodge CLASS (Theorem D: obs_g =
kappa * lambda_g). This is a statement about CLASSES in H^2(M-bar_g),
not about positivity of spectral quantities. Preserving a cohomology
class is homotopical; forcing sign-definiteness of analytic
continuations is spectral. These are different categories (AP14-type
error: conflating two properties that agree in special cases).

### 5.5. "The clutching closure is the replacement"

CORRECT. The manuscript identifies the clutching closure conjecture
(Conjecture `conj:clutching-closure`) as the geometric replacement for
Li positivity. It uses the full boundary stratification of M-bar_{g,n}
and is therefore sensitive to the higher-genus modular structure. This
is the only proposed mechanism that bypasses the structural obstruction
of Gap A.

---

## 6. The honest state of affairs

### 6.1. What IS proved

- The shadow-spectral correspondence for lattice VOAs (Theorem
  `thm:shadow-spectral-correspondence`): each arity of the shadow
  tower detects one Hecke eigenform.

- The Li criterion is structurally inapplicable to the sewing lift
  (Prop. `prop:li-criterion-failure`): zeros on multiple lines force
  exponentially negative Li coefficients.

- The bracket positivity on cusp-form subspace (Theorem
  `thm:petersson-identification`): positive-definite Petersson form.

- The Ramanujan bound for lattice spectral measures (Prop.
  `prop:lattice-ramanujan`): via Deligne's theorem, external to MC.

- The algebraic-analytic divide (Remark `rem:algebraic-analytic-divide`):
  every analytic conclusion requires input external to the MC equation.

### 6.2. What is conjectured

- Clutching closure (Conjecture `conj:clutching-closure`): the geometric
  zero test using full boundary stratification.

- Modular spectral rigidity (Conjecture `conj:modular-spectral-rigidity`):
  the MC element plays the role of Frobenius.

- Operadic Rankin-Selberg (Conjecture `conj:operadic-rankin-selberg-main`):
  all-genera coherence provides analytic continuation.

### 6.3. What is structurally blocked

- MC -> Li positivity (Gap A): proved impossible by Prop.
  `prop:li-criterion-failure`.

- Bar-cobar -> RH (Gap C): Davenport-Heilbronn counterexamples show
  that functional-equation symmetry (which bar-cobar provides) does
  not force critical-line zeros.

- Surface polarization -> Li positivity: no candidate pairing exists.
  The Mellin transform is not sign-preserving. The Hodge positivity
  constrains the wrong objects (weights vs eigenvalues).

---

## 7. The meta-principle

The recurring pattern in this analysis is the INTEGRABILITY-POSITIVITY
DICHOTOMY (Remark `rem:beilinson-four-gaps`):

- The MC equation is an INTEGRABILITY constraint (flatness, D^2 = 0).
- Every spectral conclusion requires POSITIVITY (sign-definiteness,
  absolute-value bounds).
- These are logically independent properties.

A flat connection can have eigenvalues of any absolute value. D^2 = 0
does not constrain |alpha|. The Weil proof for curves over F_q
succeeds because Frobenius simultaneously satisfies BOTH integrability
(Frob^2 = q) and positivity (Hodge-Riemann on H^1, with Frobenius
acting on the SAME space that carries the bilinear form). In the MC
setting, integrability (D^2 = 0) and positivity (bracket form on
shadows) act on DIFFERENT objects, and the bridge between them
(the Rankin-Selberg/Mellin transform) is not sign-preserving.

The honest conclusion: modular surfaces cannot supply the missing
positivity through any mechanism that operates within the MC framework
alone. The positivity must come from an EXTERNAL source (Deligne,
Langlands functoriality, or the clutching closure which uses boundary
geometry beyond the MC equation itself).

---

## References within the manuscript

- `prop:li-criterion-failure` (line ~3463): structural failure of Li criterion
- `rem:beilinson-four-gaps` (line ~3251): integrability vs positivity
- `prop:bracket-hodge-index` (line ~4409): bracket positivity and Hodge index
- `thm:petersson-identification` (line ~4726): Petersson identification
- `rem:positivity-limitation` (line ~4771): positivity does not force Ramanujan
- `conj:clutching-closure` (line ~4007): clutching closure conjecture
- `rem:arithmetic-end-state` (line ~4308): the end-state of the programme
- `rem:algebraic-analytic-divide` (line ~4985): the algebraic-analytic divide
- `sec:geometric-positivity` (line ~4696): geometric positivity programme
- `thm:shadow-spectral-correspondence` (line ~100): shadow-spectral correspondence
- `conj:modular-spectral-rigidity` (line ~4450): modular spectral rigidity
- `conj:operadic-rankin-selberg-main`: operadic Rankin-Selberg theorem
