# Coderived BV/BRST Formulation: Precise Assessment

## 1. The current conjecture and its failure

Conjecture `conj:master-bv-brst` (editorial_constitution.tex, line 433):

> For a holomorphic field theory on a Riemann surface, the BV/BRST
> complex coincides with the bar complex of the associated chiral algebra,
> at all genera.

This is FALSE at the ordinary chain level for class M (Virasoro, W_N).
The obstruction (bv_brst.tex, lines 1626--1638): the quartic harmonic
discrepancy delta_4^harm ~ Q^contact * kappa / Im(tau) is not a
coboundary because 1/Im(tau) is non-holomorphic, hence not in the image
of the holomorphic bar differential.  The Fay trisecant identity does
not cancel it.

Status by shadow depth class:
- G (Heisenberg, r_max=2): PROVED at all genera (thm:heisenberg-bv-bar-all-genera).
- L (affine KM, r_max=3): PROVED (Jacobi identity kills cubic harmonic correction).
- C (betagamma, r_max=4): PROVED at genus 1 (harmonic decoupling).
- M (Virasoro, W_N, r_max=inf): FALSE at ordinary chain level.

## 2. The precise coderived reformulation

### Conjecture (Coderived BV/BRST identification)

Let A be a modular Koszul chiral algebra on a smooth projective curve X
of genus g >= 1, with curvature m_0^(g) = kappa(A) * omega_g in
H^2(M-bar_g, Z(A)).  Let T denote the associated holomorphic field
theory in the Costello-Gwilliam framework.

**Statement.** There exists a coderived quasi-isomorphism

    Phi_g^co : (C_BV^(g)(T), Q_BV + hbar * Delta_BV)
               ---->
               (B^(g)_ch(A), D_bar^(g))

in the coderived category D^co(Fact(Ran(Sigma_g))), where:

(i) The source (C_BV^(g)(T), Q_BV + hbar * Delta_BV) is the genus-g
    BV complex of T with its curved differential satisfying
    (Q_BV + hbar * Delta_BV)^2 = (c - 26)/12 * c_0 (the conformal
    anomaly curvature, which vanishes only at c = 26).

(ii) The target (B^(g)_ch(A), D_bar^(g)) is the genus-g bar complex
    with its curved differential satisfying
    (D_bar^(g))^2 = m_0^(g) = kappa(A) * omega_g (the bar curvature,
    which vanishes only for uncurved algebras).

(iii) "Coderived quasi-isomorphism" means: Phi_g^co induces an
    equivalence on the coderived categories of curved comodules,

    D^co(C_BV^(g)-comod) ~= D^co(B^(g)_ch(A)-comod),

    in the sense of Positselski's framework (see below).

(iv) At the level of MC elements:

    Phi_g^co(Theta^BV_T) = Theta^oc_A |_{genus g}

    where the left side is the BV quantum master action and the right
    side is the genus-g component of the open/closed MC element.

**Hypotheses.**

(H1) A is a conformal vertex algebra of finite type (finitely many
     strong generators in each conformal weight).

(H2) A is modular Koszul (chirally Koszul in the sense of
     thm:koszul-equivalences-meta, with the modular axiom MK:modular
     ensuring genus >= 1 propagation).

(H3) The BV complex C_BV^(g)(T) is constructed via the Costello-Gwilliam
     perturbative framework: the free theory is quantized on Sigma_g
     using the BV propagator P(z,w) = dbar^{-1} delta(z,w), and
     interactions are introduced via the OPE of A.

(H4) The comparison map Phi_g^co extends the genus-0 chain map
     Phi_0 : (C_BV(T), Q_BV) -> (B^ch_0(A), d_bar) of
     thm:brst-bar-genus0.

## 3. The model-categorical framework

### 3.1 Positselski's coderived category: what it is

For a curved dg-coalgebra (C, d_C) with d_C^2 = h * id (curvature h),
the coderived category D^co(C-comod) is the Verdier quotient of the
homotopy category K(C-comod) by the thick subcategory of coacyclic
objects: those comodules M for which every morphism M -> N with N
injective-acyclic is null-homotopic.

Key property: in D^co, the curvature h is "absorbed" --- a curved
differential with d^2 = h * id is well-defined up to coacyclic
equivalence.  The bar complex B(A) with D_B^2 = m_0 * id is a
legitimate object of D^co.

Reference: Positselski, "Two kinds of derived categories, Koszul
duality, and comodule-contramodule correspondence" (Memoirs AMS, 2011),
Chapters 3--4.

### 3.2 Does Positselski apply directly?

**Partially, with modifications.** The three issues:

**(a) Factorization structure.**
Positselski's framework is developed for CDG-coalgebras over a field
(or a commutative ring).  The bar complex B^(g)(A) is a factorization
coalgebra on Ran(Sigma_g), which is a cosheaf of CDG-coalgebras on the
Ran space stratification.  The coderived category must be constructed
stratum-by-stratum and then assembled by conservative descent.

The concordance (subsec:coderived-ran, line 4433) already addresses
this: the assembly uses the stratified conservative restriction theorem
(thm:stratified-conservative-restriction) and the factorization
co-contra correspondence (thm:fact-co-contra-general).  The proof
follows Positselski [Theorem 7.2] on each stratum Ran_n, then glues
via factorization compatibility.

**Verdict: Positselski applies stratum-by-stratum; the factorization
assembly is already proved in the manuscript.**

**(b) Curved A-infinity structure.**
The BV complex at genus >= 1 is not merely a CDG-coalgebra: it carries
a curved A-infinity structure (the BV interaction vertices define
higher composition maps m_k with m_1^2 = [m_0, -]).  Positselski's
framework handles CDG-coalgebras (d^2 = h * id) but does not directly
address A-infinity curvature.

However: the bar construction converts curved A-infinity algebras into
CDG-coalgebras.  Specifically, if (A, {m_k}_{k>=0}) is a curved
A-infinity algebra with curvature m_0, then B(A) is a CDG-coalgebra
with differential D_B satisfying D_B^2 = m_0 * id.  This is the
standard bar-construction theorem (see Positselski, Section 6.1,
or Loday-Vallette, Section 2.2).  The passage from curved A-infinity
to CDG-coalgebra is exact: no information is lost.

**Verdict: the A-infinity structure is handled by the bar construction
itself.  No modification needed beyond what the manuscript already has.**

**(c) The BV side.**
The BV complex (C_BV, Q_BV + hbar * Delta_BV) is a CURVED complex:
(Q + hbar * Delta)^2 = (c-26)/12 * c_0 (the conformal anomaly).
To place it in D^co, one needs:

(i) A CDG-coalgebra structure on C_BV compatible with the BV bracket.
    This is provided by the BV antibracket (which is a coproduct on
    the antifield complex) --- the BV complex IS a CDG-coalgebra in
    the appropriate sense.

(ii) Identification of the BV curvature with the bar curvature.
    The BV curvature is (c-26)/12 * c_0, which acts on the vacuum
    as kappa(ghost) * omega_g = -13 * omega_g.  The bar curvature
    for the total system (matter + ghosts) is
    kappa(A_tot) * omega_g = (kappa(A) + kappa(ghost)) * omega_g
    = (kappa(A) - 13) * omega_g.
    At c = 26: kappa(A) = 13, so both vanish.  Off c = 26: both are
    nonzero and must be identified via the comparison map.

**Verdict: the BV side requires interpreting the BV antibracket as a
coalgebra coproduct, which is standard (Costello-Gwilliam, Chapter 5).
The curvature identification is the content of the conjecture.**

### 3.3 The model structure

The correct model structure is:

**On CDG-coalgebras**: Positselski's coderived model structure, where
weak equivalences are coderived quasi-isomorphisms (maps inducing
equivalences on D^co of comodules), fibrations are surjections, and
cofibrations are determined by the left lifting property.

**On curved A-infinity algebras**: the transferred model structure via
the bar-cobar adjunction B -| Omega.  A morphism f: A -> A' is a weak
equivalence iff B(f): B(A) -> B(A') is a coderived weak equivalence.

The manuscript already has a provisional coderived category
D^co_prov(X) (concordance line 4465, def:provisional-coderived) that
agrees with D^co on the flat finite-type locus.  For the BV
comparison, the full Positselski model structure is needed beyond the
provisional one.

## 4. What would constitute a proof

The proof would require three components:

**(Step 1) Genus-g comparison map construction.**
Extend the genus-0 chain map Phi_0 (thm:brst-bar-genus0) to a
comparison map Phi_g: C_BV^(g) -> B^(g)(A) at each genus g >= 1.
The extension must account for the Hodge decomposition
P = d log E + P_ex + P_harm of the BV propagator.  The holomorphic
part d log E matches the bar propagator; the exact part P_ex drops
in cohomology; the harmonic part P_harm is the obstruction at the
ordinary chain level.

**(Step 2) Coderived absorption of the harmonic obstruction.**
Show that the harmonic discrepancy delta_4^harm (and its higher-arity
analogues) is coacyclic: it is annihilated in the coderived category.
The mechanism: the harmonic part P_harm = dz * dw-bar / Im(tau) (at
genus 1) is a smooth (non-holomorphic) correction; in D^co, this
correction is absorbed into the curvature via the relation d^2 = m_0.
Concretely: the non-holomorphic terms that prevent delta_4^harm from
being a coboundary in the ordinary sense become coacyclic because the
curvature kappa * omega_g already encodes the full moduli dependence
(including the non-holomorphic part) at the level of D^co.

**(Step 3) MC element transport.**
Verify that Phi_g^co intertwines the BV quantum master action with
the genus-g component of Theta^oc_A.  At the scalar level this is
Theorem D (the free energies match).  At the chain level, this
requires the coderived equivalence of step 2.

## 5. Expected scope

- For classes G, L, C: the coderived reformulation reduces to the
  ordinary chain-level statement (already proved or provable), since
  the harmonic obstruction vanishes for these classes.

- For class M at genus 1: the coderived reformulation should be
  accessible, as the obstruction delta_4^harm has an explicit formula
  and the coderived absorption mechanism is concrete (single modular
  parameter tau).

- For class M at genus >= 2: genuinely open, as the harmonic
  obstruction couples to the full period matrix of Sigma_g and the
  coacyclicity argument requires controlling the higher-genus
  moduli dependence.

## 6. Relation to existing manuscript infrastructure

The manuscript already has:
- The provisional coderived category (concordance, subsec:coderived-ran).
- The factorization co-contra correspondence (thm:fact-co-contra-general).
- The stratified conservative restriction (thm:stratified-conservative-restriction).
- The provisional embedding (prop:provisional-embedding).
- The genus-g bar-cobar equivalence statement in D^co (concordance, line 5035).

What is MISSING for the precise coderived BV/BRST conjecture:
- A formal conjecture environment with the hypotheses above.
- The BV-side CDG-coalgebra structure (implicit in Costello-Gwilliam
  but not formalized in the manuscript).
- The curvature-matching condition (kappa(A_tot) * omega_g on the bar
  side vs (c-26)/12 * c_0 on the BV side).
- The coacyclicity argument for the harmonic obstruction.

## 7. Summary

The coderived reformulation of conj:master-bv-brst is:

> The BV/BRST complex and the bar complex are quasi-isomorphic in
> the coderived category D^co of curved factorization coalgebras on
> Ran(Sigma_g), for all modular Koszul chiral algebras at all genera.

Positselski's framework applies stratum-by-stratum on Ran(Sigma_g),
with the factorization assembly already proved in the manuscript.
The curved A-infinity structure is handled by the bar construction.
The genuine new content is the coacyclicity of the harmonic propagator
discrepancy, which is accessible at genus 1 for class M and open at
higher genus.
