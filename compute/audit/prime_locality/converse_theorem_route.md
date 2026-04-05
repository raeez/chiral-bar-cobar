# Adversarial Audit: The Converse Theorem Route to Automorphy

**Date**: 2026-04-01
**Target**: The CPS converse theorem application in arithmetic_shadows.tex,
specifically thm:cps-from-mc, cor:moment-automorphy, and the complete chain
(rem:complete-chain).
**Method**: Independent verification of each hypothesis of CPS against
the actual objects M_r(s) produced by the shadow programme.

---

## Executive Summary

The manuscript's Route A claims: M_r(s) satisfies the four CPS hypotheses
(thm:cps-from-mc, tagged ProvedHere), therefore M_r(s) = L(s, pi_r) for
an automorphic representation pi_r of GL(r) (cor:moment-automorphy, tagged
ProvedHere).

**Verdict: The CPS application has at least FOUR serious gaps, two of
which are potentially fatal.** The manuscript's own caveat (lines 4952-4958)
acknowledges that the functional equation and polynomial growth "require
detailed spectral analysis beyond the scope of this chapter." This caveat
is honest but it undermines the ProvedHere tag on both thm:cps-from-mc
and cor:moment-automorphy.

---

## Finding 1 (CRITICAL): CPS requires twists by ALL cuspidal
representations of GL(r-1), not just Dirichlet characters

**The claim** (thm:cps-from-mc, line 4934): "These hold for all twists
by Dirichlet characters chi."

**The actual CPS hypothesis** (Cogdell-Piatetski-Shapiro 1999, Theorem 2):
For a Dirichlet series D(s) to be the L-function of a cuspidal automorphic
representation of GL(n), one must verify the analytic properties (meromorphic
continuation, functional equation, bounded in vertical strips) not merely
for twists by Dirichlet characters (= GL(1) twists), but for twists by
ALL cuspidal automorphic representations of GL(j) for 1 <= j <= n-2.

- For GL(1): Hamburger's theorem. Twists by GL(0) = nothing. OK.
- For GL(2): Weil's converse theorem (later Jacquet-Langlands).
  Twists by GL(1) = Dirichlet characters. This is what the manuscript
  verifies.
- For GL(3): CPS requires twists by GL(1) automorphic forms (Dirichlet
  characters). This is what the manuscript verifies.
- For GL(r), r >= 4: CPS requires twists by cuspidal automorphic
  representations of GL(j) for ALL 1 <= j <= r-2. In particular,
  for r = 4 one needs twists by GL(1) AND GL(2). For r = 5, twists by
  GL(1), GL(2), AND GL(3).

The manuscript claims the four CPS hypotheses hold "for all twists by
Dirichlet characters chi" (line 4934). This is GL(1) twists ONLY. For
M_r(s) to be automorphic on GL(r) via CPS when r >= 4, one needs the
functional equation and polynomial growth for M_r(s) twisted by arbitrary
cuspidal automorphic representations of GL(j), j <= r-2.

The proof (lines 4937-4959) addresses only Dirichlet character twists
("the functional equation follows from E*(s) = E*(1-s)") and gestures
at "cuspidal twists use the triple-product integral
(Garrett-Piatetski-Shapiro-Rallis)" without ANY detail.

**This is not a minor gap. For r >= 4, the full CPS twist hypothesis is
a substantial analytic requirement that the manuscript does not verify.**

**Note**: There is a refinement due to Cogdell-Piatetski-Shapiro (2003,
"Remarks on Rankin-Selberg convolutions") that, for GL(n), it suffices
to twist by cuspidal automorphic representations of GL(j) for
1 <= j <= n-1 (not n-2) in return for a weaker growth condition.
And Booker-Krishnamurthy (2011) give a version where twists by GL(1) alone
suffice IF one has additional analytic information (e.g., boundedness in
vertical strips, no pole at s=1, etc.). The manuscript does not cite these
refinements, does not specify which version of CPS is being used, and
does not verify the additional conditions any refinement requires.

**Severity**: CRITICAL for r >= 4. The gap is potentially bridgeable
(the Rankin-Selberg method may provide the twisted functional equation)
but the bridge is NOT written.

---

## Finding 2 (CRITICAL): M_r(s) is not generically a cuspidal L-function

CPS produces a CUSPIDAL automorphic representation. But the moment
L-functions M_r(s) are, for the standard families, NOT cuspidal L-functions.

### Heisenberg (rank 1)

The sewing Fredholm determinant gives (eq:sigma-minus-1-dirichlet):

    sum sigma_{-1}(N) N^{-s} = zeta(s) * zeta(s+1)

This is the Rankin-Selberg convolution of the trivial GL(1)
representation with itself, shifted. It equals L(s, 1 x 1) up to shift.
As a function on GL(2), it is the L-function of the EISENSTEIN series
E(s), NOT of a cuspidal representation. Specifically:

    zeta(s) * zeta(s+1) = L(s, Ind(|.|^{1/2}, |.|^{-1/2}))

which is the L-function of the principal series representation
Ind(|.|^{1/2}, |.|^{-1/2}) of GL(2), an ISOBARIC sum, not a cuspidal
representation. CPS does not apply to Eisenstein representations.

The CPS converse theorem's conclusion is that D(s) = L(s, pi) for a
CUSPIDAL automorphic representation pi. If M_r(s) has poles (as
zeta(s)*zeta(s+1) does at s=0 and s=1), then either:
(a) it is not cuspidal (and CPS does not apply), or
(b) one must use the generalized converse theorem that allows poles
    (Jacquet-Shalika, which produces an isobaric representation).

The manuscript states "finitely many poles, at most simple poles from E_s"
(line 4926-4927) as one of the four hypotheses. The original CPS theorem
for CUSPIDAL representations requires the L-function to be ENTIRE (no poles
at all, except possibly at s=0 and s=1 for the untwisted case).

For Heisenberg: M_2(s) = kappa^2 * const * zeta(2s), which has a pole
at s = 1/2. This is the L-function of a GL(1) character, not a GL(2)
cusp form.

### Lattice VOAs

For E_8: the Epstein zeta is 240 * 2^{-s} * zeta(s) * zeta(s-3)
(eq:e8-epstein). This is a product of GL(1) L-functions (Eisenstein).
It is NOT the L-function of a cuspidal representation of GL(anything).

For Leech: the Epstein zeta involves BOTH an Eisenstein part
(zeta(s)*zeta(s-11)) AND a cuspidal part (L(s, Delta_12)). The
full Epstein zeta is an ISOBARIC sum, not a single cuspidal L-function.

**The manuscript's objects M_r(s) generically contain Eisenstein
components. CPS applies only to produce cuspidal representations. The
correct tool for the general case is the Jacquet-Shalika converse
theorem or the Langlands spectral decomposition, which produces
isobaric automorphic representations (not necessarily cuspidal).**

**Severity**: CRITICAL. The distinction between cuspidal and isobaric is
not cosmetic. For the lattice case, the manuscript correctly handles this
by decomposing into Hecke eigencomponents FIRST (each of which IS
automorphic individually), bypassing the need for CPS on the full M_r.
But thm:cps-from-mc and cor:moment-automorphy apply CPS to M_r(s)
directly, without separating into cuspidal and Eisenstein parts.

---

## Finding 3 (SERIOUS): The functional equation for M_r(s) does not
follow from E*(s) = E*(1-s) alone

**The claim** (thm:cps-from-mc(d), lines 4930-4932): "Functional equation:
from E*(s) = E*(1-s) and the MC recursion."

**The problem**: The Rankin-Selberg integral
M_r(s) = int Sh_r(tau) E*(s, tau) d mu(tau)
inherits the functional equation E*(s) = E*(1-s) ONLY IF Sh_r(tau) is
an eigenfunction of the relevant involution. In the standard
Rankin-Selberg theory:

For a holomorphic Hecke eigenform f of weight k:
    int |f|^2 E*(s) d mu = completed L(s, f x f-bar)
and the functional equation comes from Hecke theory on f, not from
E*(s) alone.

For a general function Sh_r(tau): the Rankin-Selberg unfolding gives
    M_r(s) = sum a_n(Sh_r) n^{-s} * gamma(s)
The functional equation of this Dirichlet series requires Sh_r to
transform appropriately under tau -> -1/tau (i.e., to be a modular
form or have a known modular transformation law).

Now Sh_r^{(1)} involves products of E_2*(tau), which is QUASI-MODULAR
(transforms with an additive anomaly under SL(2,Z)). The Rankin-Selberg
theory for quasi-modular forms is NOT the same as for modular forms.
The manuscript itself acknowledges this (rem:quasimodular-obstruction,
lines 5184-5210):

> "The unfolding theory for such integrals is more subtle than for
> holomorphic eigenforms (it involves the non-holomorphic completion
> of E_2 and Zagier's theory of quasi-modular Rankin-Selberg integrals)."

This is exactly right. But then thm:cps-from-mc claims the functional
equation IS proved ("from E*(s) = E*(1-s) and the MC recursion"), while
the quasi-modular obstruction remark says the analysis "has not been
carried out." These two claims are IN DIRECT CONTRADICTION.

**Severity**: SERIOUS. The functional equation claim in thm:cps-from-mc
is inconsistent with the quasi-modular obstruction remark. At minimum,
thm:cps-from-mc should be restricted to arities where Sh_r is a genuine
modular form (arity 2, where Sh_2 = kappa * E_2* and the non-holomorphic
completion E_2-hat IS modular).

---

## Finding 4 (SERIOUS): The "all twists" claim is unverified even for
Dirichlet character twists

**The claim** (thm:cps-from-mc, line 4934): "These hold for all twists
by Dirichlet characters chi."

**The proof** (lines 4937-4951): The twisted version
M_r(s, chi) = int Sh_r(tau) E*(s, chi, tau) d mu(tau)
requires:
- The twisted Eisenstein series E*(s, chi, tau) to have the correct
  functional equation. This is standard.
- The Rankin-Selberg integral to unfold correctly with the character
  twist. This requires Sh_r to be invariant under Gamma_0(N) where N
  is the conductor of chi, OR the integral must be computed on the
  appropriate congruence subgroup.

The shadow projection Sh_r^{(1)} is defined on SL(2,Z)\H. For a
Dirichlet character chi of conductor N > 1, the twisted integral
requires working on Gamma_0(N)\H. The unfolding argument changes.
This is standard in the Rankin-Selberg literature but the manuscript
does not carry out the computation.

The proof's only comment on this is "The functional equation for all
twists and the polynomial growth estimates require detailed spectral
analysis beyond the scope of this chapter" (lines 4954-4956). This
caveat is honest but it means the theorem is NOT actually proved.

**Severity**: SERIOUS. The caveat effectively retracts the ProvedHere
status. The theorem should be tagged ProvedHere only for untwisted
M_r(s), and ConjecturedOrConditional for twisted versions.

---

## Finding 5 (SERIOUS): The Virasoro case is structurally incompatible
with the converse theorem route

For Virasoro at generic c:

(a) The shadow obstruction tower has infinite depth (class M, r_max = infinity).
(b) The shadow coefficients S_r(c) are rational functions of c (not
    Hecke eigenvalues of modular forms).
(c) The genus-1 propagator is E_2*(tau) (quasi-modular, not modular).
(d) The partition function chi_0(tau) = q^{-c/24} prod (1-q^n)^{-1}
    is NOT a modular form (it transforms with a character under SL(2,Z)).

The moment L-functions M_r(s) for Virasoro are Rankin-Selberg integrals
of QUASI-MODULAR forms. The remark on line 5082-5084 is honest:

> "The moment L-function M_r(s) = int Sh_r E(s) d mu is the correct
> object; its Euler product status remains the central open problem."

But cor:moment-automorphy (tagged ProvedHere!) claims M_r(s) = L(s, pi_r)
for ALL chirally Koszul algebras with HS-sewing. This includes Virasoro.
The corollary is derived from thm:cps-from-mc, which itself has an
unverified functional equation for quasi-modular shadows.

For Virasoro specifically, S_Vir(u) = (1/u) * sum_{r>=2} S_r(c) u^r
where S_2 = c/2, S_3 = 0, S_4 = -3c/(5c+22), etc. The generating
function involves 1/sqrt(Q(t)) where Q is a quadratic. This is NOT a
Hecke eigenvalue sequence at ANY single prime. There is no Euler product
decomposition of S_r into prime-local factors, because S_r is a FIXED
rational function of c, independent of any prime p.

The notion of "prime-locality" for Virasoro (conj:prime-locality-transfer,
line 4987: "trivially satisfied for Virasoro at leading 1/c") is vacuous
at leading order: a single spectral atom is trivially "multiplicative"
because there is only one factor. At subleading order in 1/c, the
question becomes nontrivial but is OPEN (the manuscript says so at
rem:hecke-defect-leading, lines 7547-7559).

**Severity**: SERIOUS. The Virasoro case exposes that cor:moment-automorphy
overclaims. M_r(s) for Virasoro at generic c has NO reason to be an
automorphic L-function.

---

## Finding 6 (MODERATE): Conflation of objects across families

The attack questions posed by the user contain some imprecisions that
should be addressed, but the core concerns are valid:

**User's question 1**: "S_H(u) = zeta(u) zeta(u+1) is a PRODUCT of two
GL_1 L-functions."

Correct. The Heisenberg sewing determinant gives sum sigma_{-1}(N) N^{-s}
= zeta(s) zeta(s+1). This is a Rankin-Selberg convolution at the GL(2)
level, specifically the L-function of an Eisenstein series. CPS cannot
produce this (CPS outputs cuspidal representations).

However, this is M_2 for the Heisenberg, not the full S_A. The Heisenberg
shadow obstruction tower terminates at r=2, so there are no higher M_r to consider.
The CPS question is moot for Heisenberg: zeta(s) zeta(s+1) is already
identified as a known automorphic L-function (Eisenstein on GL(2)) without
needing CPS.

**User's question 2**: "S_Vir(u) = zeta(u+1)(zeta(u)-1)"

This formulation is incorrect. The manuscript does not write S_Vir(u) in
this form. The shadow obstruction tower for Virasoro gives S_r = kappa * Bernoulli-type
coefficients. The moment L-functions M_r(s) for Virasoro are Rankin-Selberg
integrals of quasi-modular forms, not simple products of zeta values.
However, the user's core point is valid: the Virasoro shadow data does
not decompose into automorphic L-functions in any obvious way.

**User's question 3**: "For lattice VOAs: the converse theorem of Hecke
DOES apply."

Correct. For lattice VOAs, the theta function Theta_Lambda is a genuine
modular form, and the Hecke decomposition produces genuine automorphic
L-functions. The converse theorem works (more precisely: no converse
theorem is needed, because the L-functions are already identified as
automorphic by Hecke theory). The lattice case is the one place where
the arithmetic programme is on firm ground, and the manuscript is honest
about this distinction.

**User's question 4**: "Is there a quasi-automorphic L-function theory?"

This is a genuine open question in number theory. Zagier's theory of
quasi-modular forms and their Rankin-Selberg integrals provides partial
answers, but there is no "quasi-automorphic converse theorem." The
manuscript's rem:quasimodular-obstruction correctly identifies this gap.

---

## Finding 7 (MODERATE): Status tag inconsistency

thm:cps-from-mc is tagged \ClaimStatusProvedHere (line 4916) but its own
proof contains the caveat (lines 4952-4958):

> "The functional equation for all twists and the polynomial growth
> estimates require detailed spectral analysis beyond the scope of
> this chapter; the argument sketched above establishes the structure
> of the proof, with the analytic estimates relegated to the standard
> Rankin-Selberg machinery."

This is an AP4 violation (status tag as ground truth). The theorem
claims to prove four hypotheses; its proof acknowledges two of them are
not fully proved. The correct tag is \ClaimStatusHeuristic or at best
\ClaimStatusProvedElsewhere with a citation to where the "standard
Rankin-Selberg machinery" is deployed in this specific setting.

Similarly, cor:moment-automorphy is tagged \ClaimStatusProvedHere (line
4963) but depends on thm:cps-from-mc, which has the above caveat, AND
applies CPS to a potentially non-cuspidal function (Finding 2), AND
does not verify cuspidal twists for r >= 4 (Finding 1).

---

## Finding 8 (MODERATE): The non-lattice Ramanujan theorem
(thm:non-lattice-ramanujan) has an independent CPS problem

The proof of thm:non-lattice-ramanujan (lines 5529-5611) goes through
Observation C (Franc-Mason vector-valued Hecke decomposition) to establish
prime-locality, then invokes CPS.

But at Station 8 (lines 5733-5739): "The CPS hypotheses hold
(Theorem ref:thm:cps-from-mc); CPS gives automorphy."

This inherits all the gaps from thm:cps-from-mc (Findings 1-4). Moreover,
Observation B's claim that "The CPS hypotheses are satisfied
(Theorem ref:thm:cps-from-mc)" on line 5575-5576 cites the problematic
theorem.

The theorem is tagged ProvedHere, but its proof chain passes through an
insufficiently proved intermediate result.

---

## Finding 9 (MINOR): The complete status table overclaims

The status table (lines 5786-5813) shows:

| Result | Lattice | Non-lattice |
|--------|---------|-------------|
| CPS hypotheses | ProvedHere | ProvedHere |
| CPS => pi_r automorphic | ProvedHere | ProvedHere |

Both entries should be downgraded. For lattice VOAs, CPS is not needed
(the L-functions are identified directly from the Hecke decomposition).
For non-lattice VOAs, CPS is applied through the problematic
thm:cps-from-mc.

---

## Structural Analysis: What IS proved, honestly

Separating the proved from the claimed:

### Firmly proved:
1. M_r(s) has meromorphic continuation (from HS-sewing + RS unfolding).
   This is standard and correct.
2. For LATTICE VOAs: the theta function decomposes into Hecke eigenforms,
   each of which is automorphic. The Hecke-Newton closure
   (thm:hecke-newton-lattice) is on solid ground. The Ramanujan bound
   follows from Deligne's theorem. The MC equation provides an
   alternative packaging, not an alternative proof.
3. For RATIONAL VOAs with diagonal modular invariant: the Franc-Mason
   vector-valued Hecke theory provides a decomposition into eigenforms.
   This IS genuine automorphic data, and the Ramanujan bound follows
   for the eigencomponents (by Deligne for holomorphic eigenforms).
4. The algebraic structure: shadow-symmetric power identification
   (prop:shadow-symmetric-power), Newton's identities, the MC recursion
   on moment L-functions. These are algebraic facts, not analytic ones.

### Not proved (but claimed ProvedHere):
1. The full CPS hypotheses for M_r(s) at all arities for non-lattice
   theories (thm:cps-from-mc).
2. The functional equation of M_r(s) for quasi-modular shadow
   projections (Finding 3).
3. The twisted functional equation for all Dirichlet characters
   (Finding 4).
4. The cuspidal twist hypothesis for r >= 4 (Finding 1).
5. That M_r(s) is the L-function of a cuspidal (not isobaric)
   representation (Finding 2).

### Honestly open:
1. Euler product status of M_r(s) for non-lattice theories
   (rem:algebraic-analytic-divide, rem:quasimodular-obstruction).
2. Prime-locality for Virasoro at subleading order in 1/c.
3. The operadic Rankin-Selberg conjecture
   (conj:operadic-rankin-selberg-main).
4. Ramanujan for irrational VOAs (conj:irrational-ramanujan).

---

## Recommendations

### Status corrections needed:

1. **thm:cps-from-mc**: Downgrade from ProvedHere to Heuristic, or
   split into: (a) ProvedHere for lattice VOAs at arity 2 with
   untwisted M_r, and (b) Conjectured/Heuristic for general families
   and twisted versions.

2. **cor:moment-automorphy**: Downgrade from ProvedHere. For lattice
   VOAs, automorphy is proved by Hecke theory (not CPS). For non-lattice
   theories, it depends on the problematic thm:cps-from-mc.

3. **thm:non-lattice-ramanujan**: The proof's Observation B cites
   thm:cps-from-mc. The argument should clarify that for rational VOAs
   with Franc-Mason decomposition, the L-functions ARE automorphic by
   the Hecke eigenform property (not by CPS). CPS is not needed when
   you have a direct Hecke decomposition.

4. **The status table** (lines 5786-5813): Correct "CPS hypotheses:
   ProvedHere" for non-lattice to "ProvedHere for lattice; Heuristic
   for non-lattice at arities >= 3."

### Mathematical corrections needed:

5. The proof of thm:cps-from-mc should specify which version of CPS is
   being used (original 1999, or refinements by Cogdell-PS 2003 or
   Booker-Krishnamurthy 2011). Different versions have different twist
   requirements.

6. The argument should separate the Eisenstein and cuspidal components
   of M_r(s) before applying CPS. CPS produces cuspidal representations;
   Eisenstein components must be identified separately.

7. The quasi-modular obstruction (rem:quasimodular-obstruction) should
   be cited in the proof of thm:cps-from-mc as a RESTRICTION on the
   functional equation claim, not left as a separate remark that
   contradicts the theorem.

8. For the Virasoro and W_N cases: add an explicit remark that the CPS
   route is CONDITIONAL on resolving the quasi-modular Rankin-Selberg
   analysis, and that no converse theorem is known for quasi-automorphic
   L-functions.

---

## Finding 10 (MODERATE): The non-lattice Ramanujan theorem does NOT
actually need CPS

A careful re-reading reveals that thm:non-lattice-ramanujan's proof has
a REDUNDANT CPS invocation. The logical chain is:

1. Observation A: chi_i is holomorphic. (Standard VOA theory.)
2. Observation B: RS integral of |chi_i|^2 gives L(s, chi_i x chi_i-bar).
   Then claims "CPS hypotheses are satisfied (thm:cps-from-mc)."
3. Observation C: Franc-Mason decomposition gives chi_i = sum of
   vector-valued Hecke eigenforms phi_j. Each phi_j has multiplicative
   Fourier coefficients.
4. Observation D: Apply the twelve-station argument component-by-component.

But Observation C makes Observation B's CPS invocation UNNECESSARY. If
chi_i decomposes into Hecke eigenforms phi_j, then L(s, phi_j x phi_j-bar)
is ALREADY the Rankin-Selberg convolution of a known automorphic form.
Its automorphicity follows from Rankin-Selberg theory directly, not from
CPS. The Ramanujan bound then follows from Deligne's theorem (for
holomorphic eigenforms) without needing CPS at all.

The twelve-station chain's CPS step is a vestige of the general argument
applied without optimization to the rational case. For rational VOAs,
the proof could be simplified to: Franc-Mason decomposition + Hecke
eigenform property + Deligne's theorem. No CPS needed.

This means thm:non-lattice-ramanujan is CORRECT but its proof contains
unnecessary machinery. The ProvedHere tag is justified (the result IS
proved), but the proof's logical structure is suboptimal: it invokes a
problematic intermediate result (thm:cps-from-mc) when a direct argument
suffices.

**Severity**: MODERATE. The theorem is correct; the proof cites more than
it needs.

---

## Finding 11 (MINOR): The irrational Ramanujan conjecture is correctly
conditional but understates the difficulty

conj:irrational-ramanujan (line 5643) is correctly tagged Conjectured and
the proof sketch correctly identifies the conditionality on Langlands
functoriality (Sym^r for all r). However, the proof sketch invokes CPS
at Stations 8-12 (line 5734-5739) through thm:cps-from-mc, inheriting
all its gaps.

More fundamentally: for irrational VOAs, the spectral decomposition
produces Maass forms, and the Ramanujan conjecture for Maass forms is
OPEN (the best result is Kim-Sarnak exponent 7/64, as the manuscript
notes on line 5753-5756). The conjecture essentially asserts that the
Selberg eigenvalue conjecture holds for Maass forms appearing in VOA
partition functions. This is a deep conjecture that the MC equation
cannot resolve without external analytic input.

The manuscript is honest about this conditionality. No status correction
needed.

---

## Anti-pattern classification

- **AP4** (Status tag as ground truth): thm:cps-from-mc and
  cor:moment-automorphy both tagged ProvedHere with proof caveats
  that acknowledge unverified hypotheses.
- **AP7** (Scope inflation): "For a chirally Koszul algebra A with
  HS-sewing" = universal claim. Proved only for lattice VOAs via Hecke
  decomposition. The non-lattice case routes through an incomplete CPS
  verification.
- **AP13** (Forward references hiding gaps): cor:moment-automorphy cites
  thm:cps-from-mc as if it is proved; the proof of thm:cps-from-mc
  contains a caveat that the key estimates are not carried out.
- **AP17** (Narrative velocity): The twelve-station chain was written
  with forward momentum; each station's proof cites the previous
  station without independently verifying the full hypothesis match.
  The CPS application at station 8 inherits all upstream gaps.
