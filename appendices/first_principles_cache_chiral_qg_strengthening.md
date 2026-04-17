# First-Principles Cache: Chiral QG Equivalence Strengthening (2026-04-16)

Companion to `first_principles_cache.md`. Seven audit findings investigated from scratch; no labels swapped until the ghost theorem was identified.

## Audit finding (a): "Koszul locus" ill-typed for E_1-chiral input

**Wrong claim.** `thm:chiral-qg-equiv` invokes "the Koszul locus" as if a single notion; for E_1-chiral input the ambient Koszul locus (symmetric/unordered bar-cobar inversion) is inapplicable because B^Sigma does NOT exist for genuinely E_1 inputs (AP153).

**Ghost theorem.** There is a genuine Koszul locus defined by **ordered** bar-cobar inversion at g=0: Omega^ord(B^ord(A)) -> A is a qi. This includes Yangians (where B^Sigma is absent) and matches the ambient locus for E_inf inputs.

**Correct relationship.** Two loci coexist: ordered (applies to E_1 and E_inf) and symmetric (applies only to E_inf). The symmetric locus is the image of the ordered locus under av when av is defined. For Yangians, only the ordered locus exists; for affine KM, both do and they coincide on the shared domain.

**Type.** specific/general (the ambient Koszul was the specific case, ordered is general).

## Audit finding (b): sl_2 Yangian concrete verification absent

**Wrong claim.** `rem:independent-proof-coha` claims sl_2 verification, but the triangle arrows alpha/beta/gamma are not computed explicitly.

**Ghost theorem.** Drinfeld's second presentation of Y(sl_2) + Molev's PBW + the Yang R-matrix R(z) = 1 + hbar P/z + O(hbar^2) allow direct computation of all three arrows. The A_infty structure from the Drinfeld coproduct is the Hopf-cochain complex; the chiral coproduct is tensor-shift; the R-matrix extracts from Delta_op Delta^{-1}.

**Correct relationship.** For Y(sl_2) on the formal disk the triangle closes at first order in hbar by direct computation; higher orders by Drinfeld's universal pentagon. No E_inf hypothesis enters.

**Type.** construction/narration (the construction was narrated as possible, not inscribed).

## Audit finding (c): class-M chain-level contradiction

**Wrong claim.** `thm:w-infty-chiral-qg` asserts strict chain-level coproduct on W_{1+infty}; `conj:coderived-chiral-coproduct` says class M coproduct is only coderived.

**Ghost theorem.** The MC5 pattern (weight-completed chain-level PROVED, direct-sum chain-level FALSE) applies here verbatim. W_{1+infty} is positive-energy with finite-dim weight spaces; weight-completion gives a chain-level coproduct on the completion A^hat = prod_n A[n] even though it fails on the direct sum.

**Correct relationship.** Strict chain-level Delta^ch on A^hat exists; pullback to A fails only because finite sums do not converge. No genuine obstruction; the coderived statement is the WEAKER shadow of the completed statement. No contradiction.

**Type.** convention clash (direct-sum vs weight-completed categories).

## Audit finding (d): JKL26 phantom citation for gl_N

**Wrong claim.** `thm:glN-chiral-qg` proof cites JKL26 for the Drinfeld double construction.

**Ghost theorem.** Prochazka-Rapcak Miura factorization gives T(u) = prod_i (u + Lambda_i) directly. The universal (Psi-1)/Psi cross-coefficient (thm:miura-cross-universality) gives Stasheff relations by cross-arity cancellation. No external citation needed.

**Correct relationship.** The Drinfeld double of Y(gl_N)^ch is constructed from the Miura presentation + U(gl_1)-hat screening charges; axioms verified by the universal coefficient + Stasheff identities.

**Type.** hardcoded/symbolic (JKL26 was a placeholder for an internal derivation).

## Audit finding (e): associator dependence overclaimed

**Wrong claim.** The triangle is "up to associator Phi" as a cochain-level qualification, suggesting the equivalence is only canonical modulo GRT_1 action.

**Ghost theorem.** GRT_1 is pro-unipotent; its action on deformation-theoretic moduli is by coboundaries at the cohomology level (AP171 proved for sl_2; general case Kontsevich formality). On H^0 the triangle is rigid; on cochains the associator choice shifts by a controlled coboundary.

**Correct relationship.** Two statements: (i) H^0-level triangle is canonical, associator-free; (ii) cochain-level triangle is canonical up to GRT_1-equivalence, equivalences homotopic. Both are stronger than "up to Phi".

**Type.** level error (cohomological rigidity vs cochain-level gauge freedom).

## Audit finding (f): elliptic "partial" is underclaim

**Wrong claim.** "elliptic partial (KZB connection, no QG equiv at g=1)".

**Ghost theorem.** The Felder elliptic R-matrix R(z,tau) is the universal R-matrix of an E_1-chiral algebra on Sigma_1 (the elliptic KZB bundle). Its classical limit is Bernard's KZB connection. The ordered elliptic bar B^ord_{Sigma_1}(A) carries an elliptic chiral coproduct Delta^ch_{z,tau} by the same machinery as g=0, with Fay identity replacing the Drinfeld pentagon.

**Correct relationship.** Elliptic chiral QG equivalence holds at g=1 on the ordered Koszul locus, with Felder's DYBE replacing QYBE. "Partial" meant no closed-form R in literature; the equivalence itself extends.

**Type.** specific/general (genus-0 presentation assumed general).

## Audit finding (g): toroidal "absent" is underclaim

**Wrong claim.** "toroidal absent".

**Ghost theorem.** Schiffmann-Vasserot CoHA on C^2 + Miki's quantum toroidal algebra U_{q,t}(gl_hat_hat_1) + the DIM coproduct give a chiral QG datum on the formal disk (spectral parameters from the Omega-background). The (Psi-1)/Psi coefficient is the semiclassical limit of Miki's tetrahedron; cross-arity Stasheff gives A_infty coherence.

**Correct relationship.** Toroidal chiral QG equivalence holds at the formal-disk level; global statement (over curves C with two spectral parameters) is open.

**Type.** temporal (the construction exists, status was not updated).

## Summary

| Finding | Ghost Theorem | Strengthening |
|---|---|---|
| (a) Koszul locus | Ordered Koszul locus (E_1-compatible) | def:ordered-koszul-chiral-algebra |
| (b) sl_2 Yangian | Drinfeld 2nd presentation + Yang R | Concrete alpha, beta, gamma at order hbar |
| (c) class M | Weight-completed chain level | thm:w-infty-chiral-qg-completed |
| (d) JKL26 | Miura + screening | thm:glN-chiral-qg-internal |
| (e) associator | GRT_1 pro-unipotent | H^0 rigid, cochain homotopic |
| (f) elliptic | Felder + Fay | thm:chiral-qg-equiv-elliptic |
| (g) toroidal | CoHA + Miki DIM | thm:chiral-qg-equiv-toroidal-formal-disk |

Every wrong status hid a genuine theorem one scope-clarification away.
