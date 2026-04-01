# Adversarial Audit: Hecke Operators on Non-Lattice Algebras

## Date: 2026-04-01

## Target

The prime-locality programme for non-lattice algebras (arithmetic_shadows.tex,
compute/lib/hecke_defect.py). Specifically: is the Hecke operator T_p well-defined
on Virasoro at generic c, and does the "Hecke defect vanishes" claim in
hecke_defect.py prove anything nontrivial?

## Attack Summary

Five attack vectors:
1. Can T_p be defined on chi_0(Vir_c) at all?
2. Shadow coefficients S_r are tau-independent, so T_p(S_r) = S_r is vacuous.
3. Genus-1 amplitudes involve E_2*(tau), on which T_p is ill-defined in the
   standard (holomorphic modular form) sense.
4. Does hecke_defect.py address this?
5. Is the commutator [d_sew, T_p] meaningless if T_p doesn't act on the
   sewing complex?

## Findings

### Finding 1: The manuscript KNOWS this and handles it correctly

The manuscript is significantly more careful than the attack presupposes.
The key insight is that the programme operates at **three distinct levels**,
and the attack conflates them:

**Level 0: Shadow coefficients** (tau-independent OPE data).
The S_r are rational functions of c alone. T_p acts as identity.
The Hecke defect delta_p^{(r)} = 0 identically. This is acknowledged as
**not dynamical** in the manuscript (line 7624: "This vanishing is *not*
dynamical: it follows from the tau-independence of the shadow tower on the
scalar lane").

**Level 1: Genus-1 amplitudes** (tau-dependent graph sums).
Sh_r^{(1)}(tau) involves the propagator E_2*(tau). The Hecke action on
these is the substantive question.

**Level 2: The convolution algebra** g^mod_A.
The full Hecke defect [d_sew, T_p] lives here.

The attack is correct that Level 0 vanishing is vacuous. The manuscript says
so explicitly (Remark 7684-7715, rem:hecke-defect-two-levels). The substantive
content is at Levels 1 and 2.

**VERDICT on Attack Point 2: CORRECT but already acknowledged.** The manuscript
explicitly distinguishes shadow-coefficient-level vanishing (trivial) from
amplitude-level vanishing (substantive). The compute module tests the
trivial level. This is honest: the tests verify that the *code correctly
implements* the trivial vanishing, which is a code-correctness check, not
a mathematical depth claim.

### Finding 2: T_p IS defined on chi_0(Vir_c), but the mechanism varies

**Attack Point 1 asks: can T_p act on chi_0(Vir_c) at all?**

The answer is YES, through two mechanisms depending on rationality:

**(a) Rational c (minimal models, etc.):** The character vector
F(tau) = (chi_1, ..., chi_N) transforms as a vector-valued modular form
(VVMF) under a finite-dimensional representation rho: SL(2,Z) -> GL(N,C).
Franc-Mason (2017) define Hecke operators on VVMFs. This is
Observation C in the proof of thm:non-lattice-ramanujan (line 5580-5589).
The manuscript correctly uses this and tags it as PROVED (ClaimStatusProvedHere).

**(b) Irrational c:** chi_0(tau) is holomorphic in the upper half-plane with
at most polynomial growth (from HS-sewing). The function |chi_0(tau)|^2 is an
L^2_loc automorphic function on SL(2,Z)\H. The Roelcke-Selberg spectral theorem
decomposes it into Maass-Hecke eigenforms phi_j (discrete spectrum) and
Eisenstein series (continuous spectrum). Each phi_j is AUTOMATICALLY a Hecke
eigenfunction: T_p(phi_j) = lambda_p^{(j)} phi_j. This is the spectral theorem
for commuting self-adjoint operators on L^2(SL(2,Z)\H). See lines 5676-5693.

The manuscript tags the irrational case as CONJECTURED (conj:irrational-ramanujan,
line 5643), with the conditionality being on Langlands functoriality for Sym^r
at r >= 5 (needed for the Serre reduction step), NOT on the existence of the
Hecke action.

**VERDICT on Attack Point 1: PARTIALLY CORRECT.** T_p is well-defined on
chi_0(Vir_c) at all c, but the *mechanism* differs:
- Rational c: Franc-Mason VVMF Hecke theory (finite-dimensional, algebraic).
- Irrational c: Roelcke-Selberg spectral decomposition (infinite-dimensional,
  analytic).
The attack is wrong that T_p "is not defined" on chi_0. It IS defined, just not
via the classical "modular form of weight k" Hecke theory. The manuscript gets
this right.

### Finding 3: E_2* and the genus-1 propagator -- the real obstruction

**Attack Point 3 is the strongest part of the attack.**

The genus-1 propagator is E_2*(tau). The Hecke operator T_p on weight-2
quasi-modular forms gives:

  T_p(E_2)(tau) = (1/p) sum_{b=0}^{p-1} E_2((tau+b)/p) + p * E_2(p*tau)

For holomorphic modular forms of weight k, T_p is a well-defined endomorphism
of M_k. For E_2, which is QUASI-modular (transforms with an additive anomaly
6/(2pi*i*(c*tau+d))), the Hecke image T_p(E_2) is again quasi-modular of the
same weight (in fact, T_p(E_2) = sigma_1(p) * E_2 -- E_2 is a Hecke eigenform
in the quasi-modular sense, with eigenvalue sigma_1(p) = 1 + p).

**Key point the attack misses:** T_p IS well-defined on quasi-modular forms.
The space QM_k = C[E_2] * M_*(SL(2,Z)) is a ring, and T_p acts on it as a
ring homomorphism (extending the action on M_k). The issue is not that T_p
is undefined, but that:

1. E_2 is NOT a holomorphic modular form, so the standard Hecke theory for
   M_k does not directly apply.
2. Products of E_2 are quasi-modular polynomials in {E_2, E_4, E_6}, and the
   Hecke action on such products is determined by the ring homomorphism property
   plus the eigenvalue equation T_p(E_2) = (1+p) E_2.
3. The Rankin-Selberg integral of a quasi-modular form against E(s,tau)
   requires Zagier's non-holomorphic completion theory, which is more subtle
   than the holomorphic case.

The manuscript explicitly acknowledges this at lines 5184-5226
(rem:quasimodular-obstruction). The Euler product status of M_r(s) at arities
r <= 5 is flagged as OPEN. This is honest.

**However, the Route C theorem (thm:route-c-propagation, line 6113) claims
to resolve this.** The argument is:
- Shadow coefficients S_r are tau-independent rational functions of c.
- The MC recursion determining S_r from {S_2, S_3, S_4} is a polynomial
  operation that does not involve tau.
- Since T_p acts as identity on tau-independent quantities, and the MC
  recursion is a polynomial relation among tau-independent quantities,
  the Hecke equivariance propagates trivially.

**But wait.** The Route C proof (lines 6144-6188) writes:

  T_p(S_r) = -(1/(2r)) sum j*k*T_p(S_j)*T_p(S_k)*T_p(P)

This equation treats P as tau-independent (P = 2/c for Virasoro). And this is
correct at the SHADOW COEFFICIENT level. The shadow coefficients are defined as
the OPE-derived constants (kappa, alpha, S_4, etc.), which are tau-independent
by construction.

The attack conflates the shadow coefficient P = 2/c (the OPE-derived
propagator normalization, tau-independent) with the genus-1 propagator
P(z,w;tau) = E_2*(tau) * (...) (the sewing kernel, tau-dependent). These
are DIFFERENT objects:

- P = 2/c: the inverse OPE normalization. Enters the MC recursion for
  shadow coefficients. Tau-independent.
- P(z,w;tau): the genus-1 sewing kernel. Contains E_2*(tau). Enters the
  genus-1 amplitude Sh_r^{(1)}(tau). Tau-dependent.

The MC recursion for shadow coefficients uses P = 2/c (OPE normalization),
NOT the genus-1 sewing kernel. The shadow coefficients are extracted from the
OPE structure constants, not from genus-1 graph integrals. The genus-1 amplitude
Sh_r^{(1)}(tau) is a DIFFERENT object from the shadow coefficient S_r.

**VERDICT on Attack Point 3:** The attack correctly identifies that T_p on
E_2*(tau) is nontrivial, but incorrectly concludes this kills prime-locality.
The programme operates at two levels:
- Shadow coefficients: tau-independent, T_p trivial. Prime-locality at this
  level is vacuous but correctly stated.
- Genus-1 amplitudes: tau-dependent, T_p nontrivial. Prime-locality at this
  level is the CONTENT of Route C (thm:route-c-propagation), which reduces
  it to character-level Hecke equivariance.

The E_2* issue is real but addressed: the manuscript flags the Euler product
status as OPEN at arities r <= 5 (rem:quasimodular-obstruction) and handles
the irrational case via Roelcke-Selberg rather than via holomorphic Hecke theory.

### Finding 4: hecke_defect.py tests the trivial level -- honestly

**Attack Point 4 asks: does hecke_defect.py address the E_2* issue?**

No, and it should not. The module explicitly states (docstring lines 10-13):

  "At the shadow coefficient level (tau-independent OPE data), the defect
   vanishes identically for all algebraic families. At the genus-1 amplitude
   level (tau-dependent graph sums), the defect measures the obstruction to
   prime-locality."

The module tests the shadow coefficient level. This is a CODE CORRECTNESS test
(does hecke_operator_on_constant correctly return the identity? does the MC
recursion correctly reproduce the sqrt(Q_L) tower?), not a claim that
prime-locality is proved at the amplitude level.

**HOWEVER: there is a genuine AP10-type concern.** The test
`test_hecke_defect_invariant_under_central_charge` (line 468-473) runs:

  defects = hecke_defect_virasoro(c, 2, max_r=10)
  max_d = max(abs(d) for d in defects.values())
  assert max_d < 1e-13

This tests that the Hecke defect vanishes at the shadow coefficient level.
The test PASSES, but the result is tautological: T_p on constants is the
identity by definition (hecke_operator_on_constant returns value unchanged).
The test is checking that identity(x) - identity(x) = 0. This is not wrong,
but a reader could mistake the passing test for evidence of nontrivial
prime-locality.

**The Route C tests** (test_route_c_virasoro, lines 253-268) are genuinely
nontrivial: they verify that the MC recursion reproduces the sqrt(Q_L) tower,
confirming overdetermination. But the Hecke propagation test
(test_route_c_hecke_propagation, lines 294-304) again tests tau-independent
inputs only.

**VERDICT on Attack Point 4:** hecke_defect.py is honest about what it tests
(shadow coefficient level only). The tests are code-correctness checks. But
there is a risk of AP10 (hardcoded expected values that encode the same
triviality). The Route C overdetermination test is genuinely nontrivial; the
Hecke propagation test is not.

### Finding 5: The commutator [d_sew, T_p] IS well-defined

**Attack Point 5 claims the commutator is meaningless.**

This is incorrect. The sewing differential d_sew acts on the convolution
algebra g^mod_A. The Hecke operator T_p acts on any function of tau, and hence
acts on the genus-1 projection of g^mod_A. The commutator [d_sew, T_p] is
well-defined as an endomorphism of the graded vector space underlying g^mod_A.

The question is not whether the commutator EXISTS (it does), but whether it
VANISHES (which is prime-locality). The manuscript formulates this precisely
in rem:prime-locality-obstruction (lines 5883-5938):

  delta_p^Hecke(A) := [d_sew, T_p] in End(g^mod_A)

and identifies three components:
- [d_int, T_p] = 0: the internal differential is tau-independent. Trivial.
- [d_sew, T_p] = ?: the sewing differential involves P(z,w;tau). Nontrivial.
- [hbar*Delta, T_p] = ?: the BV operator involves contraction on E_tau.
  Nontrivial.

For lattice VOAs, all three commutators vanish because the graph amplitudes
factor through the theta function (a Hecke eigenform). For non-lattice algebras,
the vanishing of [d_sew, T_p] is the content of prime-locality. The manuscript
correctly tags this as CONJECTURED for irrational c.

**VERDICT on Attack Point 5:** Incorrect. The commutator is well-defined.
T_p acts on any function of tau, and d_sew produces functions of tau, so their
commutator is a well-defined endomorphism. The question is vanishing, not
existence.

## Assessment: Is Prime-Locality DEAD for Non-Lattice Algebras?

**No.** The programme is alive but stratified:

### What is PROVED:

1. **Lattice VOAs:** Full twelve-station proof complete. MC => prime-locality
   => CPS => Sym^{r-1} => Ramanujan. (thm:hecke-newton-lattice,
   cor:unconditional-lattice)

2. **Rational VOAs (diagonal modular invariant):** Prime-locality established
   via Franc-Mason VVMF Hecke theory. Full Ramanujan bound proved.
   (thm:non-lattice-ramanujan, ClaimStatusProvedHere)

3. **Shadow coefficient level (all algebraic families):** Hecke defect vanishes
   trivially (tau-independence). Not a dynamical result but correctly stated.

4. **Route C structural theorem:** MC overdetermination at high arity
   propagates character-level Hecke equivariance to all arities, CONDITIONAL
   on hypotheses (a) and (b) of thm:route-c-propagation. For the standard
   landscape with rational OPE coefficients, both hypotheses are verified
   (cor:route-c-standard-landscape).

### What is OPEN:

1. **Irrational c (Virasoro at generic c):** The Ramanujan bound requires
   automorphy of L(s, Sym^r phi_j) for Maass-Hecke eigenforms phi_j at all
   r >= 1. Known for r <= 4 (Gelbart-Jacquet, Kim-Shahidi, Kim). Open for
   r >= 5 (Langlands functoriality). Tagged as conj:irrational-ramanujan
   with ClaimStatusConjectured. HONEST.

2. **Euler product of M_r(s) at arities r <= 5:** The genus-1 propagator
   E_2*(tau) makes the graph-sum amplitudes quasi-modular. The Rankin-Selberg
   unfolding for quasi-modular forms requires Zagier's theory, which has not
   been explicitly carried out for the shadow amplitudes. Tagged as OPEN in
   rem:quasimodular-obstruction. HONEST.

3. **The Hecke defect class [delta_p(A)] in H^1(g^mod_A, ad_{T_p}):**
   Vanishing is the single remaining cohomological hypothesis
   (cor:conditional-ramanujan). Four routes to resolution are outlined
   (rem:prime-locality-routes). Route C (MC overdetermination) is the most
   promising and is proved conditional on character-level determination.

### What the attack CORRECTLY identifies:

- The compute tests in hecke_defect.py test only the trivial (tau-independent)
  level. This should be documented more prominently in the test docstrings.
- The shadow coefficient Hecke defect vanishing is vacuous, not dynamical.
  The manuscript says so, but the compute module's naming could mislead.
- The E_2* quasi-modular obstruction is real and the Euler product at low
  arities is genuinely open.

### What the attack INCORRECTLY claims:

- That T_p cannot act on chi_0(Vir_c). It can, via two mechanisms (Franc-Mason
  for rational c; Roelcke-Selberg for irrational c).
- That the commutator [d_sew, T_p] is meaningless. It is well-defined.
- That prime-locality is "dead." It is proved for lattice and rational VOAs,
  and conditional on Langlands functoriality for irrational VOAs.

## Specific Manuscript Issues Found

### Issue 1 (MODERATE): hecke_defect.py naming is misleading

The function `hecke_defect_virasoro` tests shadow-coefficient-level defect
(which vanishes tautologically), but the name suggests it tests the full
amplitude-level Hecke defect. Recommendation: rename to
`hecke_defect_virasoro_shadow_level` or add a prominent docstring caveat.

File: compute/lib/hecke_defect.py, line 390
File: compute/tests/test_hecke_defect.py, lines 103-151

### Issue 2 (MINOR): Route C proof has a subtle gap

The Route C proof (thm:route-c-propagation, line 6144) writes:

  T_p(S_r) = -(1/(2r)) sum j*k*T_p(S_j)*T_p(S_k)*T_p(P)

and claims "the bracket {-,-}_H is constructed from the Rankin-Selberg integral,
which intertwines the Hecke action by the multiplicativity of Hecke operators on
modular forms." But the propagator P in this equation is the OPE normalization
2/c (tau-independent), NOT the genus-1 sewing kernel. The Rankin-Selberg
intertwining claim is for modular forms; the OPE propagator is not a modular
form. The proof works because T_p acts as identity on constants, but the stated
justification (Rankin-Selberg intertwining) is the wrong reason.

File: chapters/connections/arithmetic_shadows.tex, lines 6169-6174

### Issue 3 (MODERATE): thm:non-lattice-ramanujan scope

The theorem (line 5529) claims ClaimStatusProvedHere for rational chirally
Koszul algebras with diagonal modular invariant. The proof uses Franc-Mason
VVMF Hecke theory. But Franc-Mason's theorem applies to representations of
SL(2,Z) that factor through a finite quotient. For general rational VOAs, the
representation rho may not have this property. The proof should cite the
specific Franc-Mason result and verify its hypotheses.

File: chapters/connections/arithmetic_shadows.tex, line 5529-5611

### Issue 4 (FALSE ALARM): Heisenberg kappa in test file

Line 67 of test_hecke_defect.py has:
  assert data['kappa'] == Fraction(1)

The Heisenberg at rank 1 and level 1 has kappa = k = 1 (the level).
Cross-checked against landscape_census.tex (line 69: "Heisenberg H_kappa:
kappa = kappa") and line 997-1001: "For the rank-d Heisenberg algebra
H_1^{oplus d} at level 1, rho = d/d = 1: the Polyakov formula F_1 = c/24
and the shadow formula F_1 = kappa/24 coincide because kappa = c = d."

For rank-1, level-1 Heisenberg: c = 1, kappa = 1, rho = kappa/c = 1.

This is CORRECT. The Heisenberg is NOT a sub-case of the kappa = c/2 formula
(which applies to Virasoro and betagamma). The Heisenberg has its own formula
kappa = k (the OPE coefficient in J(z)J(w) ~ k/(z-w)^2). The AP1/AP9 comment
in the code is accurate.

**STATUS**: Resolved -- false alarm. The code is correct.

### Issue 5 (MODERATE): Missing genus-1 amplitude Hecke test

The compute module tests Hecke defect only at the shadow coefficient level
(tau-independent). There is no test of the Hecke action on genus-1 amplitudes
Sh_r^{(1)}(tau), which is where the nontrivial content lives. Adding a test
that computes Sh_2^{(1)} = kappa * E_2*(tau) and verifies
T_p(Sh_2^{(1)}) = (1+p) * Sh_2^{(1)} would test the simplest nontrivial
case of amplitude-level Hecke equivariance.

## Summary Table

| Attack Point | Verdict | Severity |
|---|---|---|
| 1. T_p undefined on chi_0(Vir_c) | INCORRECT. T_p is defined via VVMF (rational) or Roelcke-Selberg (irrational) | N/A |
| 2. Shadow coefficients T_p = id is vacuous | CORRECT but already acknowledged in manuscript (rem:hecke-defect-two-levels) | MINOR |
| 3. T_p on E_2* ill-defined | PARTIALLY CORRECT. T_p IS defined on quasi-modular forms, but Euler product at low arities is genuinely OPEN | MODERATE |
| 4. hecke_defect.py doesn't address E_2* | CORRECT. Module tests shadow level only. Naming is misleading | MODERATE |
| 5. [d_sew, T_p] meaningless | INCORRECT. Commutator is well-defined; question is vanishing | N/A |

| Manuscript Issue | Verdict | Severity |
|---|---|---|
| 1. hecke_defect.py naming | Misleading but not mathematically wrong | MODERATE |
| 2. Route C proof justification | Wrong reason stated (RS intertwining vs tau-independence) | MINOR |
| 3. thm:non-lattice-ramanujan Franc-Mason hypotheses | Should verify FM theorem hypotheses | MODERATE |
| 4. Heisenberg kappa | FALSE ALARM. Code is correct (kappa = level k = 1) | RESOLVED |
| 5. Missing genus-1 amplitude Hecke test | Testing coverage gap | MODERATE |

## Overall Assessment

**The prime-locality programme is NOT dead for non-lattice algebras.** The
manuscript handles the stratification (lattice / rational / irrational)
correctly and honestly. The proved results (lattice Ramanujan, rational
Ramanujan) are sound. The open questions (irrational Ramanujan, quasi-modular
Euler product) are correctly flagged as conjectural.

The main gap is practical, not foundational: no compute tests exercise the
tau-dependent (genus-1 amplitude) level of the Hecke defect. The shadow
coefficient tests pass tautologically. This is not a mathematical error but
a testing coverage gap that could mislead readers about what has been
computationally verified.

The strongest remaining obstruction is not E_2* per se, but Langlands
functoriality for Sym^r at r >= 5. The manuscript correctly identifies this
(lines 5745-5749) and tags the irrational case as conjectural.

## Recommendations

1. Add docstring clarifications to hecke_defect.py emphasizing that tests
   operate at the trivial (shadow coefficient) level only.
2. Add a genus-1 amplitude Hecke test for the simplest case
   (Sh_2^{(1)} = kappa * E_2*).
3. Verify Heisenberg kappa convention against landscape_census.tex (Issue 4).
4. Fix the Route C proof justification: replace "Rankin-Selberg intertwining"
   with the correct reason (tau-independence of OPE data) at line 6172.
5. Verify Franc-Mason hypotheses for thm:non-lattice-ramanujan (Issue 3).
