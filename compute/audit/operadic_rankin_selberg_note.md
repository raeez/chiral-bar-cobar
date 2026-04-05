# The Operadic Rankin-Selberg Theorem: Precise Status and Gap Analysis

**Date**: 2026-04-04
**Agent**: L7 (L-function frontier)
**Target**: `conj:operadic-rankin-selberg-main` in `chapters/connections/arithmetic_shadows.tex`
(line 5646), the MC recursion on moment L-functions (thm:mc-recursion-moment, line 5713),
the CPS application (thm:cps-from-mc, line 5314), and the Hecke-Newton closure
(thm:hecke-newton-lattice, line 5856).

---

## 1. Precise Theorem Status: Proved vs Conjectured

### 1.1. The operadic Rankin-Selberg conjecture

The main result is a **CONJECTURE**, not a theorem:

```latex
\begin{conjecture}[Operadic Rankin--Selberg, main form]
\label{conj:operadic-rankin-selberg-main}
\ClaimStatusConjectured
Assume prime-locality (Conjecture conj:prime-locality-transfer).
Then M_r = L(s, Sym^{r-1} f) and the Ramanujan bound
|alpha_p| = |beta_p| = p^{(k-1)/2} follows.
\end{conjecture}
```

The manuscript is honest about this: the label is `conj:`, the status tag is
`\ClaimStatusConjectured`, and the proof is explicitly marked "conditional on
prime-locality."

### 1.2. What IS proved (unconditionally)

| Result | Label | Status | Location |
|--------|-------|--------|----------|
| MC recursion on moment L-functions | thm:mc-recursion-moment | ProvedHere | line 5713 |
| MC bracket determines spectral atoms (Newton's identities) | prop:mc-bracket-determines-atoms | ProvedHere | line 2609 |
| Shadow-symmetric power identification | prop:shadow-symmetric-power | ProvedHere | line 4842 |
| Weight bound for genus-1 shadow projections | prop:genus1-weight-bound | ProvedHere | line 5580 |
| Hecke-Newton closure for lattice VOAs | thm:hecke-newton-lattice | ProvedHere | line 5856 |
| Unconditional Ramanujan for lattice VOAs | cor:unconditional-lattice | ProvedHere | line 5919 |
| Route C: MC rigidity forces character-level prime-locality | thm:route-c-propagation | ProvedHere | line 6533 |
| Non-lattice Ramanujan (rational VOAs, diagonal invariant) | thm:non-lattice-ramanujan | ProvedHere | line 5947 |
| Hecke defect vanishing: Heisenberg | prop:hecke-defect-families(i) | ProvedHere | line 8053 |
| Hecke defect vanishing: Virasoro | prop:hecke-defect-families(ii) | ProvedHere | line 8053 |
| Newton-shadow-Hecke correspondence | prop:newton-shadow-hecke | ProvedHere | line 6877 |

### 1.3. What is tagged ProvedHere but has known gaps

| Result | Label | Issue |
|--------|-------|-------|
| CPS hypotheses from MC + HS-sewing | thm:cps-from-mc | Tagged `\ClaimStatusConditional` (line 5316). Proof's own caveat (line 5353-5358) acknowledges "functional equation for all twists and polynomial growth estimates require detailed spectral analysis beyond the scope of this chapter." The converse_theorem_route.md audit identifies FOUR serious gaps: (1) CPS requires GL(j) twists for j >= 2, not just Dirichlet characters; (2) M_r(s) is generically not a cuspidal L-function (it is isobaric); (3) The functional equation does not follow from E*(s) = E*(1-s) alone for quasi-modular shadow projections; (4) Twisted functional equations unverified. |
| Automorphy of moment L-functions | cor:moment-automorphy | Tagged `\ClaimStatusConditional` (line 5381). Conditional on thm:cps-from-mc. |

### 1.4. What is conjectured

| Result | Label | Status |
|--------|-------|--------|
| Operadic Rankin-Selberg main form | conj:operadic-rankin-selberg-main | Conjectured |
| Prime-locality for general algebras | conj:prime-locality-transfer | Conjectured (proved for lattice + rational VOAs) |
| Ramanujan for irrational VOAs | conj:irrational-ramanujan | Conjectured |
| Hecke defect vanishing for W_3 cross-channel | prop:hecke-defect-families(iii) | Conjectured |

---

## 2. The CPS Converse Theorem: Which Properties Does MC Provide?

The Cogdell-Piatetski-Shapiro converse theorem (CPS 1999) states: if M_r(s) is a
Dirichlet series satisfying

  (a) meromorphic continuation to all of C,
  (b) finitely many poles,
  (c) polynomial growth in vertical strips (for all GL(j) twists, j = 1, ..., r-2),
  (d) functional equation with correct gamma factors,

then M_r(s) = L(s, pi_r) for a cuspidal automorphic representation pi_r of GL(r).

### What the MC programme provides:

**(a) Meromorphic continuation: YES (with qualifications).**
The moment L-function M_r(s) = int Sh_r(Theta_A; tau) E*(s, tau) d mu(tau)
has meromorphic continuation to all s via the standard Rankin-Selberg unfolding,
combined with the HS-sewing decay (thm:general-hs-sewing) which guarantees the
integral converges. This is an unconditional theorem for all chirally Koszul
algebras with HS-sewing.

**(b) Finitely many poles: YES.**
The poles come from the Eisenstein series E*(s), which has poles at s = 0 and
s = 1. At most simple poles. This is standard.

**(c) Polynomial growth in vertical strips: PARTIALLY.**
- For j = 1 twists (Dirichlet characters): the polynomial OPE growth of A
  combined with the standard Phragmen-Lindelof argument gives the bound. YES.
- For j >= 2 twists (cuspidal representations of GL(j)): UNVERIFIED.
  The proof (line 5345) says polynomial growth follows from "the polynomial
  OPE growth of A and the standard Phragmen-Lindelof argument," but this
  addresses only the untwisted case and GL(1) twists. For GL(j) twists with
  j >= 2, one needs the Rankin-Selberg integral of Sh_r twisted by a cuspidal
  form on GL(j) to have polynomial growth. The manuscript's own caveat
  (rem:cps-conditional-status, line 5361) explicitly acknowledges this gap.
- For the ORIGINAL CPS (1999): twists by cuspidal representations of GL(j)
  for ALL j = 1, ..., r-2 are required. For r >= 4, this includes j >= 2.
- For the refined CPS (Booker-Krishnamurthy 2011): GL(1) twists may suffice
  with additional analytic conditions. The manuscript does not cite or verify
  these conditions.

**(d) Functional equation: PARTIALLY.**
- For lattice VOAs with holomorphic shadow projections: YES, from the Hecke
  theory of the eigencomponents.
- For general algebras with quasi-modular shadow projections (Virasoro, W_N):
  the quasi-modular obstruction (rem:quasimodular-obstruction, line 5602)
  explicitly notes that the Rankin-Selberg theory for quasi-modular forms "is
  more subtle" and "has not been carried out." The functional equation claim in
  thm:cps-from-mc(d) ("from E*(s) = E*(1-s) and the MC recursion") is
  inconsistent with this remark for non-holomorphic shadow projections.

### Summary:
```
                     Lattice     Rational    Irrational
(a) Meromorphic      PROVED      PROVED      PROVED
(b) Finite poles     PROVED      PROVED      PROVED
(c) Poly growth j=1  PROVED      PROVED      PROVED
(c) Poly growth j>=2 PROVED*     OPEN        OPEN
(d) Funct'l eq       PROVED      PROVED**    OPEN

* For lattice VOAs, the Hecke eigencomponent L-functions are standard
  automorphic L-functions with known twisted functional equations.
** For rational VOAs, the Franc-Mason vector-valued Hecke decomposition
   gives eigencomponents that are genuine modular forms.
```

---

## 3. The Precise Gap at r >= 5

### 3.1. The Langlands functoriality gap

The complete chain from MC to Ramanujan passes through:

```
MC (all arities) --> Sym^r data --> L(s, Sym^r f) analytic cont. --> Ramanujan
      |                  |                    |                         |
   PROVED             PROVED              r<=4 PROVED              CONDITIONAL
                                          r>=5 OPEN                  on Sym^r
```

At each prime p, the MC recursion gives Newton's identity:
  p_r(alpha_p, beta_p) = e_1 * p_{r-1} - e_2 * p_{r-2}

This determines the power sums p_r = alpha_p^r + beta_p^r at each prime, which
are the Dirichlet coefficients of -d/ds log L(s, Sym^{r-1} f). So the MC
equation determines ALL the local data.

The gap is the passage from LOCAL data to GLOBAL analytic properties:

- **r = 1**: Rankin-Selberg (classical). L(s, f) has analytic continuation from
  the Hecke eigenform property. PROVED.
- **r = 2**: Shimura (1971), Gelbart-Jacquet (1978). L(s, Sym^1 f) = L(s, f).
  Automorphy of symmetric square. PROVED.
- **r = 3**: Kim-Shahidi (2002). L(s, Sym^2 f) analytic continuation. PROVED.
- **r = 4**: Kim (2003). L(s, Sym^3 f) via base change + Langlands-Shahidi method.
  PROVED.
- **r >= 5**: OPEN. L(s, Sym^4 f) analytic continuation is unknown in full
  generality (Kim-Sarnak 2003 gave partial results: the standard L-function
  of a degree-5 automorphic form, which gives Sym^4 bounds but not full
  automorphy).

### 3.2. What the MC programme provides vs what is needed

The MC programme provides:
1. **All power sums p_r at every prime** (Newton's identities from MC at all arities).
2. **The moment L-function M_r(s)** as a Rankin-Selberg integral (meromorphic, with
   finitely many poles).
3. **The CPS hypotheses (partially)** for M_r(s) as a GL(r) L-function.

What is STILL needed to close the gap:
1. **M_r(s) is a SINGLE Dirichlet series**, not a product of Sym^j L-functions.
   The Clebsch-Gordan decomposition M_r = sum of L(s, Sym^j f) requires
   INDEPENDENCE of the spectral parameters, which a single-variable
   Rankin-Selberg integral does not provide.
2. **The local-to-global passage**: knowing p_r(alpha_p, beta_p) at each prime
   gives the local Euler factor of L(s, Sym^{r-1} f), but assembling the
   global Euler product requires Langlands functoriality GL(2) -> GL(r).

### 3.3. The three possible routes to closing the gap

**(a) Multiple Rankin-Selberg integrals with independent variables.**
This would require a higher-dimensional Rankin-Selberg construction (a la
Bump-Friedberg-Ginzburg) using the genus-0 MC equation at multiple arities
simultaneously. The MC equation at genus 0 gives the OPE, which encodes the
Hecke eigenvalue a_f(p) = alpha_p + beta_p. The genus-1 MC equation at
arity r gives the power sum p_r. A multi-variable Rankin-Selberg integral
using genus-g MC data for g > 1 could in principle provide the additional
analytic structure. This is SPECULATIVE.

**(b) Langlands functoriality (known for r <= 4, open for r >= 5).**
This is the standard number-theoretic route. The MC programme would be
self-sufficient if Langlands functoriality were known. Arthur-Clozel transfer
for GL(2) -> GL(r) gives automorphy of L(s, Sym^{r-1} f) for all r, but this
is the Langlands programme itself.

**(c) A new argument from the MC structure.**
The MC equation at genus g and arity r gives constraints beyond Newton's
identities. At genus >= 2, the MC equation involves contributions from
stable graphs of higher genus, which introduce TAUTOLOGICAL CLASS data
(lambda_g, psi-classes, boundary strata) that is not present in the genus-1
moment L-function. Whether this higher-genus data provides the additional
analytic structure needed for Sym^r automorphy is the CENTRAL OPEN QUESTION
of the operadic Rankin-Selberg programme.

---

## 4. The Genus-1 Correction to Newton's Identities

### 4.1. The genus decomposition

The MC equation D*Theta + (1/2)[Theta, Theta] = 0 decomposes by genus:

- **Genus 0**: The MC equation at genus 0 encodes the OPE structure: m_2,
  composition, associativity. In spectral coordinates, this gives e_1 = a_f(p)
  (the Hecke eigenvalue) and e_2 = alpha_p * beta_p = p^{k-1}.

- **Genus 1**: The MC equation at genus 1 and arity r gives the SHADOW
  PROJECTION Sh_r^{(1)} = tr(m_2^{r-1}) (the power sum p_{r-1} integrated
  against the genus-1 propagator E_2*(tau)).

- **Genus g >= 2**: The MC equation at genus g and arity r gives corrections
  involving stable graphs of genus g. These contribute TAUTOLOGICAL CLASSES
  (lambda_g, delta_irr, delta_{ij}) that are not visible at genus 1.

### 4.2. The genus-1 MC equation at arity 6

At arity 6, the genus-1 MC equation is:

  nabla_H(Sh_6^{(1)}) + sum_{j+k=8} {Sh_j^{(1)}, Sh_k^{(1)}}_H = 0

plus contributions from genus-0 data at arity 6 (the hexagonal OPE contact terms)
and genus-2 data at lower arities (the planted-forest corrections delta_pf).

The critical new feature at arity 6: the weight bound (prop:genus1-weight-bound)
shows that the necklace graph at arity 6 has modular weight 2*6 = 12, which is
exactly the weight of the Ramanujan cusp form Delta.

This means that at arity 6, the genus-1 shadow projection Sh_6^{(1)}(tau) can
contain a CUSP-FORM COMPONENT proportional to Delta(tau). For arities <= 5, the
shadow projections are quasi-modular forms of weight <= 10, which lies below the
cusp-form threshold. The first nontrivial interaction between the MC equation and
the arithmetic of cusp forms occurs at arity 6.

### 4.3. What the genus-1 correction provides at r = 5

The MC recursion at arity 6 determines Sh_6 from {Sh_2, ..., Sh_5} plus the
arity-6 contact terms. In Newton's identity language, this gives:

  p_5 = e_1 * p_4 - e_2 * p_3

which is a LINEAR relation among known quantities (assuming p_2, p_3, p_4 are
already determined). This does NOT provide new information for Sym^5 analytic
continuation, because:

1. Newton's identity at arity 6 is an ALGEBRAIC identity among power sums
   and elementary symmetric polynomials. It holds identically for any two
   complex numbers alpha, beta.

2. The analytic continuation of L(s, Sym^4 f) requires AUTOMORPHIC DATA
   (a functional equation, Euler product, polynomial growth for GL(j) twists)
   that Newton's identities alone do not provide.

3. The genus-1 correction involves quasi-modular forms (products of E_2*),
   whose Rankin-Selberg theory is incomplete (rem:quasimodular-obstruction).

### 4.4. The genus-2 contribution at arity 6

The genus-2 planted-forest correction delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48
(from pixton_shadow_bridge.py) enters the MC equation at genus 2 and arity 0.
At genus 2 and arity 6, the planted-forest correction involves the 35 stable
graphs of M-bar_{3,0} and their genus-2 specializations.

The key question: does the genus-2 data at arity 6 provide ADDITIONAL constraints
on the Hecke eigenvalues beyond Newton's identities?

**Assessment**: No, in the following sense. The genus-g MC equation at arity r
gives a relation of the form

  [MC constraint]_g,r = sum over stable graphs of genus g

Each stable graph contributes an amplitude that involves the OPE coefficients
(which are the SAME at all genera -- they are genus-0 data) composed with
tautological classes on M-bar_{g,r}. The tautological classes provide new
GEOMETRIC structure, but the OPE data is unchanged. The constraint on the
Hecke eigenvalues therefore factors through the same Newton relations.

The genus-g correction does NOT provide additional ARITHMETIC constraints.
It provides additional GEOMETRIC constraints (the shadow amplitudes must be
compatible with the boundary stratification of M-bar_{g,r}), but these are
constraints on the GEOMETRIC side (tautological relations), not on the
ARITHMETIC side (Hecke eigenvalues).

---

## 5. The Hecke-Newton Closure and Unconditional Lattice Ramanujan

### 5.1. The lattice case: complete

For lattice VOAs, the chain is fully closed:

  MC equation --> Hecke-Newton closure (thm:hecke-newton-lattice)
  --> prime-locality --> CPS automorphy --> Sym^{r-1} identification
  --> Ramanujan bound

The key insight: the lattice theta function Theta_Lambda decomposes into
Hecke eigenforms by the theory of modular forms. The MC recursion respects
this decomposition (because the Hecke operators are multiplicative and the MC
bracket is polynomial). Therefore prime-locality holds for lattice VOAs.

The Ramanujan bound then follows from Deligne's theorem (or, equivalently,
from the MC chain itself applied to the individual Hecke eigencomponents).

### 5.2. The first non-lattice family where the gap matters

The **Virasoro algebra at generic central charge** is the first non-lattice
family where the gap matters. Specifically:

- For Virasoro at irrational c: the shadow obstruction tower has infinite depth (class M),
  the shadow coefficients S_r(c) are rational functions of c (tau-independent),
  and the genus-1 propagator is quasi-modular (E_2*). The Hecke defect vanishes
  trivially (prop:hecke-defect-families(ii)) because the shadow coefficients
  are tau-independent, so T_p(S_r) = S_r. But this vanishing is "not dynamical"
  (line 8078): it follows from tau-independence, not from the Hecke module
  structure.

- For rational VOAs with diagonal modular invariant: the Franc-Mason
  vector-valued Hecke theory (Observation C in thm:non-lattice-ramanujan)
  provides the decomposition into eigencomponents. The Ramanujan bound for
  these eigencomponents follows from Deligne's theorem (they are holomorphic
  eigenforms of integral weight >= 2 for a congruence subgroup).

So the gap matters for:
1. **Virasoro at irrational c**: no Hecke decomposition, continuous spectrum.
   The Ramanujan bound is conjectural (conj:irrational-ramanujan).
2. **W-algebras at generic (irrational) level**: same issue.
3. Any VOA whose characters are NOT modular forms for a congruence subgroup.

### 5.3. The irrational extension

For irrational c, the partition function |chi_0(tau)|^2 enters the
Roelcke-Selberg decomposition as a linear combination of Eisenstein series
and Maass eigenforms. The MC equation constrains this decomposition, but the
Ramanujan bound for Maass forms is itself CONJECTURAL (the Ramanujan conjecture
for Maass forms is one of the great open problems in analytic number theory,
equivalent to the Selberg eigenvalue conjecture).

The Virasoro case is therefore doubly conditional:
(a) The MC equation must force prime-locality for the Roelcke-Selberg components.
(b) The Ramanujan conjecture for Maass forms must hold.

Neither (a) nor (b) is proved.

---

## 6. Assessment: Can the MC Programme Close the Langlands Gap?

### 6.1. What the MC programme genuinely provides

The MC equation is an ALGEBRAIC structure (a Maurer-Cartan equation in a
dg Lie algebra) that produces ANALYTIC objects (the moment L-functions M_r(s)
via Rankin-Selberg integrals). The algebraic content is:

1. Newton's identities at all arities (the power sums p_r are polynomially
   determined by e_1, e_2).
2. The MC recursion on M_r(s) (thm:mc-recursion-moment): a recursive formula
   for M_{r+1} in terms of lower arities.
3. The shadow bracket form (def:shadow-bracket-form): a bilinear form on the
   shadow space that is positive-definite on the cusp-form subspace.

### 6.2. What the MC programme does NOT provide

The MC programme does not provide:

1. **Langlands functoriality for r >= 5**: the passage from local Euler factors
   (which the MC equation determines at each prime) to global automorphy
   (which requires the full force of the Langlands programme).

2. **The Clebsch-Gordan decomposition of M_r(s)**: the moment L-function is
   a SINGLE Dirichlet series. Decomposing it into a direct sum of
   L(s, Sym^j f) requires spectral independence that the single-variable
   Rankin-Selberg integral does not provide.

3. **The quasi-modular Rankin-Selberg theory**: for non-lattice algebras,
   the shadow projections involve quasi-modular forms, and the Rankin-Selberg
   theory for quasi-modular forms is more subtle than for holomorphic forms.

### 6.3. Could the all-genera coherence close the gap?

The tantalizing possibility is that the MC equation at ALL genera simultaneously
provides more information than at any single genus. Specifically:

- At genus 0: the OPE (local data).
- At genus 1: the moment L-functions (Rankin-Selberg integrals).
- At genus g >= 2: tautological constraints on M-bar_{g,n} boundary strata.

The genus-g MC equation gives a system of constraints on the shadow amplitudes
at each genus, and the compatibility of these constraints across genera is a
GLOBAL condition. Whether this global condition implies Langlands functoriality
is the central open question.

**My assessment: NO, the all-genera coherence alone cannot close the Langlands gap.**

The reason is structural: the MC equation is a FLATNESS condition (D^2 = 0),
which gives INTEGRABILITY constraints. Langlands functoriality is an
AUTOMORPHY condition, which requires SPECTRAL data (eigenvalues of Hecke
operators, Ramanujan bounds). The passage from integrability to automorphy
is precisely the content of the Langlands programme, and it is not a formal
consequence of any flatness condition.

More concretely: the MC equation at genus g and arity r gives a constraint
that involves the SAME OPE coefficients at all genera (the vertices of stable
graphs carry the genus-0 OPE data). The genus-g tautological classes provide
new geometric structure, but they do not provide new arithmetic structure.
The Hecke eigenvalues are determined by the genus-0 data alone (the OPE at
each prime p), and the higher-genus MC constraints are consistency conditions
on the GEOMETRIC side, not additional constraints on the ARITHMETIC side.

### 6.4. The honest status

The operadic Rankin-Selberg programme provides:

1. **For lattice VOAs**: a COMPLETE alternative derivation of the Ramanujan
   bound, via the Hecke-Newton closure. This is a genuine theorem
   (cor:unconditional-lattice), giving a new proof of Deligne's theorem
   from the homotopy theory of chiral algebras rather than etale cohomology.

2. **For rational VOAs**: a COMPLETE argument via the Franc-Mason
   vector-valued Hecke theory (thm:non-lattice-ramanujan). The Ramanujan
   bound follows for all Hecke eigenforms in the spectral decomposition.

3. **For irrational VOAs**: the argument is CONDITIONAL on (a) the Hecke
   defect vanishing (prime-locality for irrational theories), and (b)
   Langlands functoriality for Sym^r with r >= 5. The MC programme provides
   the algebraic infrastructure (Newton's identities, moment L-functions,
   MC recursion) but not the analytic input (Sym^r automorphy).

4. **The Langlands gap is NOT closable by MC methods alone**. The MC equation
   determines the local Euler factors at each prime (via Newton's identities),
   but assembling the global Euler product is a number-theoretic problem that
   requires either Langlands functoriality or an entirely new approach.

### 6.5. What WOULD be needed to close the gap at r = 5

To prove the automorphy of L(s, Sym^4 f) from MC methods, one would need:

1. **A multi-variable Rankin-Selberg construction** that uses the MC equation
   at multiple arities simultaneously to produce a degree-5 L-function
   (not just a single Dirichlet series M_5(s)). This would require a
   higher-dimensional integral representation (analogous to
   Bump-Friedberg-Ginzburg for GL(n) x GL(n)).

2. **OR** a proof that the MC recursion on M_r(s), combined with the known
   automorphy of M_2, M_3, M_4 (from Rankin-Selberg, Kim-Shahidi, Kim),
   implies the automorphy of M_5. This would require showing that the
   MC recursion is compatible with the Langlands spectral decomposition
   at the level of automorphic representations, not just L-functions.

3. **OR** an entirely new argument that bypasses Langlands functoriality.
   The MC equation is a DIFFERENT algebraic structure from the Langlands
   programme (it is a dg Lie algebra MC equation, not a Hecke algebra
   action), and it is conceivable (but unproved) that this different
   algebraic structure provides a new route to Sym^r automorphy.

None of these three routes is currently available. The gap is genuine and
deep.

---

## 7. Status Honesty Assessment

### 7.1. Items where the manuscript is honest

- `conj:operadic-rankin-selberg-main` is correctly tagged Conjectured.
- `thm:cps-from-mc` is correctly tagged Conditional (line 5316), with an
  explicit caveat (rem:cps-conditional-status, line 5361).
- `cor:moment-automorphy` is correctly tagged Conditional.
- The four-station table (rem:mc-ramanujan-bridge, line 2666) correctly
  identifies Station 3 as "Open (r >= 5)".
- The complete chain (rem:complete-chain, line 5673) correctly states
  "Every arrow is proved except prime-locality for non-lattice theories."
- The assessment table (line 8254) correctly identifies the open problems.

### 7.2. Items where status could be tightened

1. **thm:cps-from-mc**: Currently `\ClaimStatusConditional`. The converse
   theorem route audit (compute/audit/prime_locality/converse_theorem_route.md)
   identified FOUR serious gaps. The tag should be accompanied by a more
   explicit list of conditions.

2. **The status table at line 6199**: Shows "CPS hypotheses: ProvedHere" for
   both lattice AND non-lattice columns. For non-lattice theories, the CPS
   hypotheses are NOT fully verified (the quasi-modular obstruction and the
   GL(j) twist requirement are not resolved). The non-lattice column should
   read Conditional, not ProvedHere.

3. **thm:non-lattice-ramanujan (line 5947)**: Tagged ProvedHere. The proof's
   Observation B cites thm:cps-from-mc, but Observation C (Franc-Mason) makes
   this citation redundant -- the eigencomponents are already automorphic by
   Hecke theory, so CPS is not needed. The proof is correct but uses a
   sledgehammer (CPS) where a screwdriver (Hecke eigenform automorphy) suffices.
   Not a status error, but an argument that could be streamlined.

### 7.3. One structural concern

The complete status table (line 6199) shows ALL SIX rows as ProvedHere for
both lattice and non-lattice columns. This gives the visual impression that
the entire programme is complete. The fact that the "ProvedHere" for
non-lattice theories in rows 2, 4, 5 depends on the Franc-Mason Hecke
decomposition (which is specific to rational VOAs with diagonal modular
invariant) is not visible in the table. A footnote or qualification would
help.

---

## Summary

The operadic Rankin-Selberg programme is a mathematically rich connection
between chiral algebra homotopy theory and analytic number theory. Its
status is:

- **For lattice VOAs**: COMPLETE. The Hecke-Newton closure provides an
  unconditional alternative derivation of the Ramanujan bound.
- **For rational VOAs (diagonal invariant)**: COMPLETE. The Franc-Mason
  Hecke theory provides prime-locality.
- **For irrational VOAs**: CONDITIONAL on Langlands functoriality (r >= 5)
  and the Hecke defect vanishing. The MC programme provides the algebraic
  infrastructure but not the analytic input.
- **The Langlands gap at r >= 5**: GENUINE and DEEP. The MC equation
  determines local Euler factors at each prime but cannot assemble the
  global Euler product. The genus-1 correction at arity 6 introduces the
  cusp form Delta but does not provide new arithmetic constraints beyond
  Newton's identities.
- **The all-genera coherence**: provides geometric constraints (tautological
  relations on M-bar_{g,n}) but not arithmetic constraints (Hecke eigenvalues).
  Cannot close the Langlands gap by itself.

The manuscript's status tags and caveats are largely honest. The main result
(conj:operadic-rankin-selberg-main) is correctly identified as a conjecture.
The assessment table correctly identifies the open problems. The one area
where tightening would help is the status table at line 6199, which gives
a more optimistic visual impression than the detailed discussion warrants.
