# Mixed Sector at Genus >= 2: Investigation Report

## The Question

The mixed sector of the Swiss-cheese operad SC^{ch,top} controls
bulk-to-boundary maps at genus 0.  At genus g >= 1, the curvature
kappa(A) * omega_g is a closed-sector datum.  Does the mixed sector
acquire genus-dependent corrections?


## Architecture: the modular Swiss-cheese operad

The modular Swiss-cheese operad SC_mod (def:SC-mod,
modular_swiss_cheese_operad.tex line 1007) is a partially modular
two-coloured operad with three components:

| Component | Spaces | Genus | Symmetry |
|-----------|--------|-------|----------|
| Closed (cl) | C_*(FM_k(Sigma_g)) | all g >= 0 | S_k |
| Open (op) | E_1(m) (Stasheff associahedra) | g = 0 only | ordered |
| Mixed (mix) | C_*(FM_{k|m}(Sigma_g, partial)) | inherits g from closed | S_k x ordered |

**Critical structural fact**: The open colour carries NO genus.
The interval R has no genus.  The mixed operations inherit a genus
label from the closed factor but have no independent genus of their
own (rem:partially-modular, line 1242).

**Directionality (axiom A5)**: P(..., op, ...; cl) = 0.  No open
inputs produce closed outputs.  This is the mathematical expression
of bulk -> boundary one-way information flow.


## The product decomposition theorem

**Proposition prop:mixed-product-decomposition** (line 1041):

    C_*(FM_{k|m}(Sigma_g, partial)) ~ C_*(FM_k(Sigma_g)) x C_*(E_1(m))

This is the key structural result.  It says: the mixed operations
at genus g decompose as a product of closed-colour (genus-g FM chains)
and open-colour (genus-0 associahedra) data.

### Genus 0: strict isomorphism

At genus 0, Sigma_0 \ {pt} = C is contractible, so the product
decomposition is a STRICT isomorphism (rem:product-strictness,
line 1125):

    FM_{k|m}(C, partial) = FM_k(C) x E_1(m)

### Genus g >= 1: homotopy equivalence only

At genus g >= 1, the decomposition is only a homotopy equivalence,
NOT a strict isomorphism.  The failure is geometric: a boundary
point on I subset partial(Sigma_g) has a well-defined distance to
the nearest interior point only AFTER fixing a collar identification
partial(Sigma_g) x [0, epsilon) -> Sigma_g.  Different collar choices
produce homotopic but not identical projection maps.

**On chain complexes (rem:product-strictness, line 1143)**: the
homotopy equivalence induces a quasi-isomorphism

    C_*(FM_{k|m}) -> C_*(FM_k) x C_*(E_1(m))

that is NOT a chain map from a strict product differential.  The
cross-terms partial_collar arising from collar variation contribute
homotopically trivial corrections.


## Does the mixed sector acquire genus-dependent corrections?

### Answer: NO at the operadic level; the corrections are homotopically trivial.

The product decomposition holds at ALL genera as a HOMOTOPY
equivalence.  Since all subsequent constructions (bar-cobar,
Feynman transform, modular homotopy-Koszulity) are homotopy-invariant,
the homotopy equivalence suffices.

More precisely:

1. **The open colour is genus-independent.**  E_1(m) = K_m (Stasheff
   associahedra) at ALL genera.  The open factor of the mixed sector
   does not know the genus of the closed factor.

2. **The closed factor carries all genus dependence.**  The genus-g
   data in the mixed sector is C_*(FM_k(Sigma_g)), which is the SAME
   as the closed-colour data.  No new genus-dependent corrections
   appear in the mixed sector beyond what is already present in the
   closed sector.

3. **The collar corrections are homotopically trivial.**  At g >= 1,
   partial_collar corrections appear in the chain-level differential,
   but they are null-homotopic.  They do not contribute to cohomology.

4. **The curvature kappa * omega_g is a CLOSED-sector datum.**  It
   comes from the Arakelov propagator correction on FM_k(Sigma_g),
   which is the closed factor.  The open factor E_1(m) does not see
   the curvature.


### The genus-raising operations on mixed operations

The non-separating clutching on mixed operations (axiom C7,
def:partially-modular, line 876) is:

    xi^mix_nsep: P_mix(g, k+2, m) -> P_mix(g+1, k, m)

This contracts two CLOSED inputs of a mixed operation, raising genus.
The open inputs are unaffected.  The genus-raising compatibility
axiom (A4) ensures this is consistent with closed-colour clutching.

**Key point**: genus-raising acts ONLY on the closed inputs.  The
open inputs are passive spectators.  There is no "open-colour
genus-raising" because the interval has no genus.


## The annulus trace: first open-to-closed map at genus 1

While the mixed sector itself does not acquire corrections, there IS
a genus-1 open-to-closed map: the annulus trace.

The annulus S^1 x [0,1] is the simplest bordered surface with two
boundary components.  Its partition function in the open-closed theory
is the trace of the open sector:

    Z_ann = Tr_M(Id)

By the annulus trace theorem (thm:thqg-annulus-trace,
thqg_open_closed_realization.tex), this is the Hochschild homology
class [1] in HH_0(A_b).  This is described as "the first modular
shadow of the open sector" (rem:thqg-annulus-first-shadow): a
trace of the open world that precedes the genus-1 curvature
kappa * lambda_1 in the modular hierarchy.

**This is NOT a mixed-sector correction.**  The annulus trace is an
INDEPENDENT datum: it is the genus-1 open-sector trace, computed by
Hochschild homology.  It lives in a different part of the modular
hierarchy from the mixed SC operations.


## What the modular SC operad sees and misses

From rem:local-model-scope (line 49) and
prop:extraction-functor (line 1343):

**The modular SC operad sees (Models 1-2):**
- Collision data: OPE coefficients, Arnold relations, Fay trisecant
- The Koszul dual A! (from bar-cobar on FM compactifications)
- Swiss-cheese directionality (no open-to-closed)
- Flat bar differential D^2 = 0

**The modular SC operad misses (Model 3):**
- D-module monodromy around cycles of Sigma_g
- Period corrections from H^1(Sigma_g)
- The Arakelov propagator's non-holomorphic correction
- The curvature kappa * omega_g

The curved model (d_fib^2 = kappa * omega_g) is NOT operadic.  It
requires factorization input from the global theory.  This is
stated precisely in rem:curved-non-corollary (line 2931): the
curved bar-cobar equivalence requires (1) operadic modular
homotopy-Koszulity, (2) factorization Koszul duality, and (3) the
chiral Riemann-Hilbert correspondence.

**AP93 check (critical)**: the multi-weight cross-channel correction
delta_F_g^cross lives in the CLOSED sector, not the mixed sector.
"Mixed channels" (referring to propagator structure in multi-generator
graph sums) is a DIFFERENT use of "mixed" than "mixed sector"
(referring to closed-open SC interactions).  These must never be
conflated.


## Summary of findings

| Question | Answer | Status |
|----------|--------|--------|
| Does the mixed sector acquire genus corrections? | NO (homotopy-trivial collar terms only) | PROVED |
| Does the open colour depend on genus? | NO (E_1(m) = K_m at all genera) | PROVED |
| Is the product decomposition strict at g >= 1? | NO (homotopy equivalence, not isomorphism) | PROVED |
| Do the homotopy corrections affect cohomology? | NO (null-homotopic) | PROVED |
| Is curvature kappa * omega_g a mixed-sector datum? | NO (purely closed-sector) | PROVED |
| Does genus-raising act on open inputs? | NO (only on closed inputs) | PROVED |
| Is there an open-to-closed map at genus 1? | YES: annulus trace (but NOT a mixed-sector correction) | PROVED |

**Conclusion**: The mixed sector of SC_mod is structurally stable
across all genera.  Its genus dependence is inherited entirely from
the closed factor via the product decomposition, and the open factor
is genus-independent.  The curvature kappa * omega_g lives in the
closed sector; the mixed sector transmits it to boundary operators
without acquiring independent corrections.  The only genuinely new
genus-1 open/closed datum is the annulus trace, which is a modular
shadow of the open sector (Hochschild homology), not a mixed-sector
correction.


## Source files consulted

- chapters/theory/modular_swiss_cheese_operad.tex (the primary source):
  - def:SC-mod (line 1007): modular SC operad definition
  - prop:mixed-product-decomposition (line 1041): product decomposition
  - rem:product-strictness (line 1125): genus-0 strict vs g>=1 homotopy
  - rem:FM-boundary (line 1155): FM for manifolds with boundary
  - rem:partially-modular (line 1242): why "partially modular"
  - def:partially-modular (line 758): axioms C1-C7, A1-A5
  - prop:extraction-functor (line 1343): Loc functor properties
  - cor:flat-model-equiv (line 2858): flat bar-cobar equivalence
  - rem:curved-non-corollary (line 2931): curved model NOT operadic
  - rem:three-models-operadic (line 2967): operadic horizon

- chapters/connections/thqg_open_closed_realization.tex:
  - thm:thqg-annulus-trace: annulus trace theorem
  - rem:thqg-annulus-first-shadow (line 812): annulus as first shadow

- chapters/theory/introduction.tex:
  - thm:e1-primacy (line 378): E_1 primacy theorem
