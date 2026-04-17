# Wave 1 Adversarial Audit: Theorem D (obs_g = κ · λ_g)

**Target.** Vol I status table claim: "Theorem D PROVED unconditionally
(uniform-weight, Koszul locus, all g ≥ 1) — obs_g = κ · λ_g
(UNIFORM-WEIGHT); multi-weight: + δF_g^cross", with three gaps allegedly
closed 2026-04-16: (i) K-theoretic globalization via λ_{-1}(E) and the
identity ch_g(λ_{-1}(E)) = c_g(E); (ii) Faltings/Soulé citation chain;
(iii) BGS c_1(det E) → c_g(E) via splitting + scalar-channel linearity.
Plus AP225 clutching-uniqueness and H04 PTVV alternative as backup
proofs. Source files audited: `chapters/theory/higher_genus_foundations.tex`
(prop:scalar-obstruction-hodge-euler at line 5386, lem:k-theoretic-
globalization-bar at 5514, prop:clutching-uniqueness at 5904,
prop:theorem-D-factorization-homology-alt at 5993) and
`chapters/theory/clutching_uniqueness_platonic.tex`
(thm:clutching-uniqueness-socle-projection at line 216).

## ATTACK

### F1 (CRITICAL). The identity `ch_g(λ_{-1}(E)) = (-1)^g · c_g(E)` is correct, but the inscription proves only the *projection* to a single graded piece, not what the Step-1 narrative claims.

In Step 1c of `prop:scalar-obstruction-hodge-euler` (lines 5492–5512), the
splitting principle gives `ch(λ_{-1}(E)) = ∏(1 - e^{x_i})`. Expanding
this product as `∏(-x_i + O(x_i²))`, the lowest-degree component is
`(-1)^g · x_1 ⋯ x_g = (-1)^g · c_g(E)`, lowest degree `2g`. This is
correct as an identity at degree `2g`, but the sentence "Thus the virtual
class contributes `κ(A) · λ_g` at the top Chern degree" silently *defines*
`obs_g(A) := ch_g([Bbar^(g)_{scalar}]^vir)`, i.e. obs_g is *defined* by
projection of the virtual K-class to the degree-`g` Chern character piece.
Under that definition the equality `obs_g = κ · λ_g` is *tautological*;
the substantive content is that this *specific* projection coincides with
the obstruction class extracted from the bar curvature. The two notions
of "obstruction class" — (A) the chain-level fiberwise curvature integrated
to a class on the base via BGS, and (B) the K-theoretic projection
ch_g([Bbar]^vir) — are claimed to coincide but the coincidence is
*assumed* in the construction, not proved.

**Where the issue is hidden.** Step 1a (lines 5447–5466) writes the
fiberwise associated graded as `⊕_p Λ^p H^0(Σ_g, ω) ⊗ ε_p` with `ε_p`
"the one-dimensional scalar channel at weight `p`". This presumes the
scalar channel decouples at every weight `p`, with the *same* coefficient
`κ(A)` — i.e. that κ acts diagonally on the entire bar tower. This is the
uniform-weight hypothesis *plus* a tacit "scalar-diagonal" assumption.

### F2. "Scalar-channel linearity" in Step 3d is an analyst's fudge.

Lines 5754–5786: "fiberwise contraction against the scalar generator
produces the trace `tr(κ · id_E) = g · κ`; on the splitting `E = L_1 ⊕ ⋯ ⊕
L_g` this distributes as `κ` on each line summand `L_i`. Dividing by `g`
to isolate the scalar channel … preserves the coefficient `κ(A)` on each
`L_i`." The "divide by g to isolate the scalar channel" step is *not*
Chern–Weil; it is an averaging operation on the trace, and there is no
reason a priori for the *base-cohomology* class produced from BGS line-by-
line on each L_i to be `κ · c_1(L_i)` rather than `κ · c_1(L_i) +
(corrections from the splitting principle)`. The splitting principle is
*injective* on rational cohomology of the flag bundle, not surjective in
the natural way required to descend an line-by-line BGS computation back
to the base. The argument as written would, if correct, prove
`κ^g · c_g(E)` on the flag bundle (line 5774) and then "scalar-channel
projection extracts the linear-in-κ component". This last extraction is
*not justified*: the splitting principle does not provide a `κ^g →
linear-in-κ` projector that commutes with `f^*` and `f_*`. The claim
that `e_g(x_1 κ, …, x_g κ) = κ^g e_g(x_1, …, x_g)` is correct algebra,
but the leap to "and the scalar-channel projection of `κ^g e_g` is `κ · e_g`"
mistakes a polynomial identity for a cohomological identity.

### F3. BGS gives c_1(det E) = c_1(E); the upgrade to c_g(E) is *not* automatic from the splitting principle.

Bismut–Gillet–Soulé 1988a (the cited [BGS88a]) computes
`c_1(λ, h_Q) = ∫_{Σ_g/Mbar_g} Td(T_π) · ch(ω_π)`, the curvature of the
*determinant line bundle*. To obtain `c_g(E)` one needs either
(a) the full higher BGS theory of secondary characteristic classes,
which in 1988 was only fully extended to higher Chern classes by
Bismut–Gillet–Soulé 1988b/1990 in the presence of *Bott–Chern* classes,
*not* the simple scalar version invoked here; or
(b) Mumford's GRR computation, which the proof does invoke (Step 2,
lines 5537–5560), but Mumford only gives `c_g(E) ∈ CH^g(Mbar_g)` *as a
class*, not its curvature representative. The route "fiberwise Arakelov
curvature → BGS → c_g(E)" is asserted at lines 5808–5814 but the
mechanism (BGS for higher Chern classes via splitting) is not actually
spelled out beyond the analyst's-fudge of F2.

### F4. Soulé Ch.III is for arithmetic surfaces, not for Mbar_g over a field.

Soulé 1992 Ch.III is the *arithmetic* Riemann–Roch: the determinant line
bundle on Spec(O_K)-points of a moduli of curves, with archimedean places
contributing the Quillen metric. The cited statement "fiberwise Chern–
curvature for Hodge bundle in Arakelov metric" is correct *as a
geometric input*, but the inscription uses it on `Mbar_g` over **C** (or
over **Q**, but in the de Rham realization), not on Spec(O_K). The
Arakelov metric and BGS formula descend to the geometric Mbar_g without
incident, but the *citation chain* "Arakelov 1974 + Faltings 1984 §2 +
Soulé 1992 Ch.III" is not the cleanest possible: the Bismut–Freed 1986
construction of the determinant line bundle + BGS 1988a anomaly formula
is the right citation, and Faltings §2 + Mumford 1983 supply the higher
Chern classes via the splitting principle. The current citation reads as
arithmetic when the actual content is differential-geometric; this is a
metadata cleanliness issue, not a math gap, but it makes audit harder.

### F5. AP225 clutching-uniqueness uses a *socle projection*, not on-the-nose equality, for g ≥ 3.

`thm:clutching-uniqueness-socle-projection` (clutching_uniqueness_platonic.tex
line 216) explicitly admits in its caveat (lines 301–312) that the
boundary-restriction induction *only* drives `α_g - λ_g` into the
*numerical-equivalence kernel* `N^g(Mbar_g)`, not to zero. For `g ≥ 3`
this kernel is *not known* to vanish — the relevant statement is the
λ_g-conjecture, known for low `g` and unknown in general. So the
clutching-uniqueness statement, *at its honest scope*, gives only
`π_soc(α_g) = π_soc(λ_g)`, not `α_g = λ_g` in `R^g(Mbar_g)`. The status
table sentence "AP225 resolved via clutching-uniqueness pinning obs_g/κ
= λ_g uniquely" is *overstated*: it is uniquely pinned on the *socle
quotient*, not on the tautological ring itself.

The remark at lines 340–370 then leans on `prop:scalar-obstruction-hodge-
euler` to "bypass this issue entirely". That bypass is precisely the
proposition attacked in F1–F3.

### F6. PTVV alternative (H04) is *not* genuinely independent: it *cites* prop:scalar-obstruction-hodge-euler for part (iii).

Lines 6027–6051 of `prop:theorem-D-factorization-homology-alt`:
"Part (iii) follows from `prop:scalar-obstruction-hodge-euler` combined
with the uniqueness statement `prop:clutching-uniqueness`". The PTVV
construction provides a class in `H^{2g}(Mbar_g, Q)`, but the
identification of the *coefficient* as `κ(A)` and the *class* as `λ_g`
is *forwarded* to the very proposition under attack. The "remark on
independence" (lines 6053–6067) claims it does not use Arakelov + BGS +
Faltings, but the proof body explicitly cites them. The PTVV path
*could* be made independent — by producing the κ coefficient from the
PTVV pairing on a genus-1 component directly, then invoking clutching-
uniqueness on the *socle* (F5) — but as written this is *not*
disjoint verification, and any HZ-IV decorator built on it would fail
import-time disjointness checks.

### F7. δF_g^cross multi-weight correction is a *named* term, not a derived formula, for general g.

The explicit value `δF_2(W_3) = (c+204)/(16c)` appears at
`w3_holographic_datum.tex:76` and again at line 527 with five claimed
verification paths ("graph sum, propagator variance, large-c,
complementarity, parity"). This is for `g = 2` only. For `g ≥ 3`,
δF_g^cross is named via reference to `thm:multi-weight-genus-expansion`
but no closed-form derivation is inscribed. The proposition
`prop:delta-f-cross-w3-g2` referenced in the status table is only the
`g=2` instance; the all-g multi-weight formula is *not* established.

### F8. Genus-1 → all-g universality genuinely requires a hidden assumption: scalar-diagonality of the bar tower across weight levels.

The cleanest version of the argument I can extract from the inscription
is: at genus 1, `H^2(Mbar_{1,1}) = Q · λ_1` and the scalar channel is
1-dimensional, so `obs_1 = κ · λ_1` is forced. To upgrade to `g ≥ 2`,
one needs *either* (a) the Arakelov–BGS direct path (F1–F4 above), *or*
(b) clutching-uniqueness from genus-1 boundary restrictions (F5). Both
paths in fact *assume* that obs_g is tautological with a scalar
coefficient `κ(A)` independent of `g`. The genuine content is *not*
"obs_g equals κ · λ_g" but "the bar curvature has the property that
the scalar coefficient `κ(A)` is constant across the tower". That
property is the *uniform-weight scalar-diagonal* hypothesis, and it is
silently used at every step.

## SURVIVORS

(S1) **Genus 1 unconditional**, all standard families: `H^2(Mbar_{1,1})
= Q · λ_1` and the scalar channel is 1-dim. `obs_1 = κ · λ_1` follows
without splitting principle, BGS, or clutching argumentation. This is
solid.

(S2) **K-theoretic identity `ch_g(λ_{-1}(E)) = (-1)^g · c_g(E)`** at
the *cohomological* level on `Mbar_g`. Splitting principle is
sound; the identity is correct. What is *not* solid is the chain from
this identity back to the bar-curvature obstruction class.

(S3) **Mumford 1983 GRR identity `c_g(E) = λ_g`**. Standard; no
attack.

(S4) **Arakelov–Faltings curvature identification on the fiber**
(eq:arakelov-curvature-identification, line 5704):
`Θ_E |_fiber = ω_g^Ar`. This is a fiberwise identity and is solid.

(S5) **Clutching-uniqueness on the socle quotient**
(`thm:clutching-uniqueness-socle-projection`). Honest scope explicitly
admitted; AP225 should be *re-stated* to reflect this scope.

(S6) **δF_2(W_3) = (c+204)/(16c)** at `g=2` for W_3 with five
independent verification paths. Solid at `g=2`; not extended to `g ≥ 3`.

## PLATONIC RECONSTITUTION

**Theorem D (Sharpened, 2026-04-17).**

(D.1) *Genus-1 unconditional.* For every modular Koszul chiral algebra
`A` on the Koszul locus, `obs_1(A) = κ(A) · λ_1` in
`H^2(Mbar_{1,1}, Q) = Q · λ_1`.

(D.2) *All-g uniform-weight, conditional on scalar-diagonality.*
Suppose `A` satisfies the uniform-weight hypothesis (all strong
generators have the same conformal weight) *and* the *scalar-diagonal
hypothesis*: the bar curvature decomposes as `κ(A) · ω_g^Ar · id_E` on
each fiber `Σ_g`, with `κ(A)` independent of `g`. Then for all `g ≥ 1`,
`obs_g(A) = κ(A) · λ_g` in `H^{2g}(Mbar_g, Q)`.

The scalar-diagonal hypothesis is *automatic* for every single-
generator family (Heisenberg, Virasoro, every rank-1 free field) by
construction, but for multi-generator families it requires
verification.

(D.3) *Multi-weight scope.* For multi-weight families (W_3, lattice
of rank ≥ 2), the formula acquires a cross-channel correction term
`δF_g^cross(A)`. At `g = 2` for `W_3`: `δF_2(W_3) = (c+204)/(16c)`
(established with five verifications). For `g ≥ 3`: open.

(D.4) *Honest socle clutching-uniqueness.* On the socle quotient
`R^g(Mbar_g)/N^g(Mbar_g)`, the boundary-restriction conditions
(non-separating vanishing + separating Mumford multiplicativity +
admissible socle normalization) pin `π_soc(obs_g/κ) = π_soc(λ_g)`
unconditionally. Lifting from the socle to `R^g(Mbar_g)` requires the
λ_g-conjecture, known only for low `g`.

## AP225 PLATONIC CLUTCHING LEMMA PROPOSAL

**Proposed lemma (Genus-1 → all-g lifting via tautological-tower
factorization).** *Let `A` be a modular Koszul chiral algebra such
that:*
- *(i) `obs_1(A) = κ(A) · λ_1`;*
- *(ii) the bar complex on each separating clutching `ξ_h` factorises:
  `ξ_h^* obs_g(A) = obs_h(A) ⊠ obs_{g-h}(A)`;*
- *(iii) the bar complex degenerates trivially at non-separating nodes
  in the sense that `ξ_irr^* obs_g(A)` lies in the lift of
  `obs_{g-1}(A) · ψ` for some psi class.*

*Then `obs_g(A) ≡ κ(A) · λ_g` modulo the numerical-equivalence kernel
`N^g(Mbar_g)`. If additionally the λ_g-conjecture holds at genus `g`,
this lifts to on-the-nose equality in `R^g(Mbar_g)`.*

**Proof sketch.** (i) provides the base case. (ii) is the
factorization-algebra axiom for the bar complex at separating nodes; it
is *not* automatic and must be verified per family. (iii) replaces the
crude "non-separating vanishing" condition with the genuine bar-
complex behaviour at irreducible nodes (the bar of the partial
normalization, paired with the boundary ψ-class). Then induct on `g`
using the boundary stratification: the inductive step lifts to the
socle quotient by clutching-uniqueness; the residue in `N^g` is then
the genuine open frontier.

This lemma cleanly *separates* the geometric input (factorization at
nodes, hypothesis (ii)+(iii)) from the analytic input (Arakelov curvature
identification, used only to verify hypothesis (ii) for specific
families). It also makes explicit that the route "genus-1 →
all-g" *requires* hypothesis (ii) — the factorization of the bar
obstruction at separating nodes — which is the genuine clutching content.

## OPEN FRONTIER

(OF1) **Scalar-diagonality for multi-generator uniform-weight
families.** Verify that `κ(A)` is `g`-independent for, e.g., affine
KM `V_k(g)` with `g` non-abelian. The current Sugawara shift
`av(r(z)) + dim(g)/2 = κ` is established at `g = 1`; its `g`-
independence at higher genus is an unproved tacit assumption.

(OF2) **The numerical-equivalence kernel `N^g(Mbar_g)` for `g ≥ 3`.**
Closing the gap between socle-clutching and on-the-nose equality
requires the λ_g-conjecture or a substitute. This is genuine open
algebraic geometry (Faber–Pandharipande, Graber–Vakil); not internal to
the Koszul programme.

(OF3) **δF_g^cross for `g ≥ 3` and multi-weight families.** Closed-
form extension of the `g = 2`, `W_3` formula to all genera. Likely
requires graph-theoretic enumeration of cross-channel ribbon graphs.

(OF4) **PTVV path made genuinely disjoint.** Re-derive the
factorization-homology output via the AKSZ partition function on a
genus-1 component, then invoke clutching-uniqueness on the socle, with
*no* citation back to `prop:scalar-obstruction-hodge-euler`. Currently
the PTVV proof body forwards to that proposition (F6).

(OF5) **Hypothesis (ii) of the platonic clutching lemma.**
Bar-complex factorization at separating nodes is asserted for the
"factorization-algebra" framework but not inscribed for the *modular*
bar complex; verify it on examples.

**Verdict.** Theorem D is unconditional at genus 1 across all
families. At all `g ≥ 1`, it is conditional on (a) uniform-weight,
(b) scalar-diagonality of the bar tower, and (c) either the
Arakelov–BGS chain (currently with the analyst's fudge of F2) *or* the
platonic clutching lemma (which makes the genuine content explicit and
shifts the residual gap to `N^g(Mbar_g)`). The status-table claim
"PROVED unconditionally (uniform-weight, Koszul locus, all g ≥ 1)"
should be revised to "PROVED unconditional at g = 1; at all g ≥ 1
conditional on scalar-diagonality + λ_g-conjecture for socle lifting".
