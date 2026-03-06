Audit basis: the compiled monograph PDF

main

. The TeX tree, prior audit notes, and compute/ harness named in the prompt were not present in the workspace, so the audit below is against main.pdf itself; where I use a computation, it is an independent local check rather than the monograph’s own test suite.

Task 1 — Deep adversarial audit
Finding 1: Main Theorem C is not proved by the argument given

Severity: TIER 1
Location: main.pdf, Theorem 12.5.1 and its proof; genus-1 \mathfrak{sl}_2 specialization
The claim: “For a Koszul dual pair of chiral algebras … Q_g(A) ⊕ Q_g(A!) = H^*(M_g,Z(A)) as graded vector spaces”, and in the proof: “The perfect pairing gives dim Q_g(A) + dim Q_g(A!) = dim H^*(M_g,Z(A))”.
The problem: The dimension count is wrong. A perfect pairing between Q_g(A) and Q_g(A!) gives dim Q_g(A)=dim Q_g(A!); it does not imply that their dimensions add up to the dimension of the ambient space. To deduce a direct-sum decomposition inside H^*(M_g,Z(A)), one needs an additional statement: for example that the two images are complementary maximal isotropic/Lagrangian subspaces for a nondegenerate pairing on the ambient space. That statement is nowhere proved. The proof also quietly changes what Q_g(A!) means: in the genus-1 \mathfrak{sl}_2 calculation the raw dual obstruction is first computed in H^0(M_{1,1}), and only then moved by the Kodaira–Spencer/Verdier involution into H^2(M_{1,1}); the theorem statement identifies Q_1(\mathfrak{sl}_2,-k-4) with the latter image, not the former raw obstruction.
Evidence: The proof explicitly argues: Verdier pairing gives duality, then σ-eigenspaces give zero intersection, then “this is a dimension count” and concludes the sum is everything. But the only dimension statement established by the pairing is equality of the two dimensions, not half-dimensionality of either image inside H^*(M_g,Z(A)). In the \mathfrak{sl}_2 genus-1 specialization, the raw calculation yields Q_1(\mathfrak{sl}_2,-k-4)=\mathbb C·(-k-2) ⊂ H^0(M_{1,1}), whereas the theorem statement presents Q_1(\mathfrak{sl}_2,-k-4)=\mathbb C·\lambda ⊂ H^2(M_{1,1}).
Impact: Main Theorem C, as stated, is unproved. Every later use of “complementarity” as a literal direct-sum decomposition inherits this gap, including the genus-1 model computations and the NAP reformulation.
Suggested fix: Replace the present argument by a genuine ambient-duality theorem: construct a nondegenerate pairing on RΓ(M_g,Z(A)), prove that the deformation space of A and the obstruction space of A! embed as complementary Lagrangians, and only then deduce the direct sum. Failing that, weaken the theorem to the duality statement Q_g(A) ≅ Q_g(A!)^∨ plus a separate statement about the Kodaira–Spencer image.

Finding 2: Bar–cobar inversion is stated for “any chiral algebra,” but later chapters explicitly say it fails for key examples

Severity: TIER 1
Location: main.pdf, Theorem 10.8.2; Remark 17.12.4; Remark 18.6.8; Remark 18.7.10
The claim: “For any chiral algebra A on a curve X, there is a quasi-isomorphism Ω_geom(B̄_geom(A)) ~→ A”, and even more strongly: “For general (not necessarily Koszul) chiral algebras, the augmentation is still a quasi-isomorphism”.
The problem: The monograph later states the opposite for precisely the singular representation-theoretic regimes that matter. At admissible affine levels, the bar spectral sequence has nontrivial higher differentials and “the bar-cobar adjunction Ω(B̄(\hat{\mathfrak g}_k)) → \hat{\mathfrak g}_k is not a quasi-isomorphism”. The Virasoro minimal-model remark says the same, and the W_3 minimal-model remark says the adjunction “may fail to be a quasi-isomorphism”. These are not peripheral examples; they are central families in the manuscript.
Evidence: The broad theorem and its “general, not necessarily Koszul” extension are stated in Chapter 10. Later, admissible Kac–Moody levels are singled out as a locus where the adjunction fails; the Virasoro and W_3 singular loci are treated analogously.
Impact: The inversion theorem is missing a hypothesis that fails for key examples. As printed, it is false. Any downstream argument that invokes bar–cobar inversion for admissible/minimal-model objects without a generic/Koszul hypothesis is invalid.
Suggested fix: Restrict the theorem to the Koszul/pro-nilpotent/completed locus, exactly as Appendix G effectively does in the abstract Ran-space formulation. For singular levels, replace ordinary inversion by a curved/completed statement in coderived or contraderived categories.

Finding 3: The uniform [2] shift in Hochschild duality is asserted, not derived

Severity: TIER 2
Location: main.pdf, Theorem 10.4.11 and proof; Chapter 13 cyclic-homology corollary
The claim: HH_n^{chiral}(A) ≅ HH_{2-n}^{chiral}(A!)^∨ ⊗ ω_X.
The problem: The proof itself isolates the obstruction and then steps over it. In bar degree n, the complex lives on C_{n+2}(X), whose dimension is n+2; Verdier duality therefore produces a degree shift depending on n. The proof then says that obtaining a uniform shift of 2 “requires additional input,” and immediately concludes that the Koszul property supplies it. But no argument is given that diagonal concentration in the bar/weight grading converts the varying Verdier shift n+2 into a constant 2. The second proof is no better: it says only that, after “tracking the grading shift,” the result follows.
Evidence: The first proof explicitly acknowledges that the varying dimension of C_{n+2}(X) is the obstacle. The second proof merely paraphrases the conclusion. The cyclic-homology corollary in Chapter 13 then uses Theorem 10.4.11 as an input.
Impact: Theorem 10.4.11 is unsupported as printed, and so are its immediate descendants: the genus-0 deformation/obstruction exchange and the cyclic-homology duality of Chapter 13.
Suggested fix: State and prove a bigraded Verdier duality first, with explicit dependence on bar degree; only after an honest totalization argument should one assert a constant cohomological shift. If such a reduction fails, the theorem must be reformulated with a bar-degree-dependent shift.

Finding 4: The Kazhdan–Lusztig equivalence is stated with the wrong target category

Severity: TIER 2
Location: main.pdf, Theorem 11.2.9; Remarks 11.1.11, 11.2.10, 17.11.5; Example 17.11.6
The claim: For positive integer level, there is an equivalence of braided tensor categories
O_k^{int}(\hat{\mathfrak g}) ≃ Rep(U_q(\mathfrak g)), and the later discussion treats the full representation category Rep(U_q(\mathfrak g)) and its q ↦ q^{-1} partner as the right targets. The text even says that at level k, for \mathfrak{sl}_2, the simple objects match |Irr(Rep(U_q(\mathfrak{sl}_2)))| = k+1.
The problem: This is not the correct categorical statement. The WZW/fusion category at positive integral level is not the full root-of-unity quantum-group representation category. The latter is much larger and, in standard formulations, nonsemisimple; the correct target is a restricted/semisimplified modular tensor category (for example, a semisimplified tilting category). The manuscript’s own simple-count assertion for the full Rep(U_q(\mathfrak{sl}_2)) betrays the category error.
Evidence: The theorem states the broad equivalence; the subsequent remarks build further claims on it. Yet Remark 17.11.5 itself admits that the stronger categorical intertwining with bar–cobar is only “expected but not proved here”.
Impact: The quantum-group interpretation of module Koszul duality, the q ↦ q^{-1} narrative, and the tensor-categorical diagrams in Chapter 11 are overstated and, as written, incorrect.
Suggested fix: Replace Rep(U_q(\mathfrak g)) by the appropriate root-of-unity modular tensor category, and separate the proven statement from the stronger but unproved intertwining with bar–cobar duality.

Finding 5: The modular periodicity theorem uses a false implication

Severity: TIER 2
Location: main.pdf, Theorem 10.6.1 and proof
The claim: For a rational chiral algebra with rational central charge, the weight-graded bar homology is eventually periodic in the conformal weight variable, with period N = 24q / gcd(p,24).
The problem: The proof confuses finite order of the modular T-matrix with periodicity of q-expansion coefficients. The key step is: T^N = Id on the character space, therefore “the T-periodicity acts on the weight grading by h ↦ h+N,” so the graded homology is periodic. That implication is false. Finite order of T gives a phase relation for the whole character; it does not force eventual periodicity of coefficients.
Evidence: The invalid step is written explicitly. A direct q-series check shows the mechanism cannot be right: standard theta/eta characters have finite-order T-behavior but their coefficients are not eventually periodic. For example, a 24-step comparison in a standard c=1 theta/eta series gives a_100 = 966806298 and a_124 = 15175585800, so the coefficient sequence is plainly not 24-periodic.
Impact: Theorem 10.6.1 is at least unproved, and the modular part of the later periodicity classification has no valid foundation.
Suggested fix: If the intended invariant is periodicity of T-eigenphases, or quasi-polynomial growth mod N, state that. Do not infer coefficient periodicity from modular monodromy without a separate argument.

Finding 6: The geometric periodicity theorem starts from a false tautological identity

Severity: TIER 2
Location: main.pdf, Theorem 10.6.10
The claim: The proof uses “Mumford’s formula 12 c_1(\mathbb E) = δ” on M_g, concludes 12 c_1(\mathbb E)|_{M_g}=0, and from that derives the bound Period_geom | 12(2g-2).
The problem: The cited tautological relation is wrong. The standard relation on \overline M_g is 12 λ = κ_1 + δ, not 12 λ = δ. The omitted κ_1 term is not cosmetic; it is exactly the part that prevents the claimed vanishing on the interior. The entire proof therefore collapses at Step 1.
Evidence: The false identity is stated verbatim, and the later steps depend on it directly.
Impact: Theorem 10.6.10 has no proof as printed, and all later uses of N_geometric = 12(2g-2) are unsupported.
Suggested fix: Rewrite the argument in the tautological ring with the correct relation among λ, κ, and boundary classes. If a periodicity statement survives, it will have to be tied to a specific tautological operator, not to the false vanishing of c_1(\mathbb E).

Finding 7: The “unified periodicity” theorem contains an arithmetic non sequitur

Severity: TIER 3
Location: main.pdf, Theorem 10.6.14 and proof
The claim: After listing three divisibility constraints, the proof says: “The three constraints combine to give Period | gcd(N_mod, N_quant, N_geom), but … the optimal bound is the least common multiple”.
The problem: This is simply not a valid inference. If one has already proved Period | N_mod, Period | N_quant, and Period | N_geom, then the strongest conclusion is Period | gcd(...). Saying that the “optimal bound is lcm” because the periodicities are “in different directions” does not repair the arithmetic; it only weakens the bound without justification.
Evidence: The contradictory arithmetic is written explicitly in the proof.
Impact: Even if the three component periodicity theorems were correct, Theorem 10.6.14 would still not be proved by the argument given.
Suggested fix: Decide which statement is actually intended. If the conclusion is a common multiple bound coming from synchronized periodicities, prove synchronization. If the hypothesis is three separate divisibility statements, the only universal consequence is the gcd bound.

Finding 8: The Heisenberg Hochschild computation contradicts the master table

Severity: TIER 2
Location: main.pdf, Example 10.8.6 / Summary 10.8.4.5; Table 13.1
The claim: Chapter 10 computes for the Heisenberg algebra B that HH^n(B)=0 for n≥3, and summarizes HH^*(B) ≅ ℂ[c]/(c^2). Chapter 13’s master table, however, lists for Heisenberg
E_2^{0,*} = ℂ[c] in even degrees and E_2^{1,*} = ℂ[c] in odd degrees, with degeneration at E_2.
The problem: Those two statements cannot both be true. If the Chapter 13 spectral sequence degenerates at E_2 and the E_2 page is polynomial in c, then one gets infinitely many nonzero Hochschild groups. That directly contradicts the Chapter 10 claim that only degrees 0 and 2 survive.
Evidence: Finite-dimensional computation in Chapter 10 versus polynomial E_2 page and E_2-degeneration in Table 13.1.
Impact: At least one of the monograph’s flagship “computed examples” is wrong or mislabeled. The cyclic-homology discussion built on Table 13.1 inherits the ambiguity.
Suggested fix: Clarify whether Table 13.1 is computing ordinary Hochschild cohomology, completed/periodic Hochschild-cyclic data, or some different E_2 page. As printed, it contradicts the explicit Heisenberg computation.

Task 2 — The form the work yearns to be

The monograph is trying to become a theory of modular Koszul duality for factorization algebras on curves. Its deepest move is not the introduction of one more bar complex, nor the packaging of vertex-algebra examples, but the insistence that Koszul duality on a curve is geometric twice over: first because the bar construction is realized on configuration spaces, and second because higher genus is not an external perturbation but a deformation internal to the duality itself. The appendices already gesture toward the correct home. Appendix G places bar–cobar in the ∞-category of factorization D-modules on Ran(X), and Appendix E identifies the geometric bar construction with factorization homology on configuration spaces. That is the right starting point.

What one wants, then, is not an ad hoc dg-category of chiral algebras plus curved corrections, but a stable ∞-category Fact(X) of factorization algebras on Ran(X) together with its completed coalgebraic counterpart. The basic objects are augmented factorization algebras A, dualizable as objects of a pro-nilpotent chiral tensor category. Their reduced bar constructions \bar B_X(A) live naturally among complete conilpotent factorization coalgebras, and Verdier duality on Ran(X) should identify \mathbb D_{Ran} \bar B_X(A) with the bar construction of a dual object A^!. Once curvature appears, ordinary derived categories are no longer the right quotients: the correct setting is Positselski’s world of coderived/contraderived categories, now internalized to factorization algebras on a curve. Curvature creates exactly the acyclic-but-not-contractible phenomena that ordinary derived categories erase too brutally.

The definition that the manuscript is almost forcing into existence is the following.

A modular Koszul chiral algebra on a smooth curve X should be an augmented factorization algebra A ∈ Fact(X) equipped with three pieces of structure. First, \bar B_X(A) is complete and conilpotent in the coderived sense. Second, there exists a dual factorization algebra A^! such that \mathbb D_{Ran} \bar B_X(A) ≃ \bar B_X(A^!). Third, the cyclic deformation complex of A carries a universal Maurer–Cartan class over the Deligne–Mumford modular operad, compatible with clutching, forgetting markings, and Verdier duality. This third datum is what the manuscript currently sees, through a glass darkly, as the sequence of curvature terms m_0^{(g)} and the scalar obstruction coefficient κ(A).

In that language, the correct form of the first main theorem is not merely “bar and cobar are equivalent for Koszul algebras.” It is:

Theorem A (correct form).
For a modular Koszul chiral algebra A on X, the reduced bar functor
\bar B_X : Alg_aug(Fact(X)) → CoAlg_conil(Fact(X))
is intertwined with Verdier duality by
\mathbb D_{Ran} \bar B_X(A) ≃ \bar B_X(A^!),
and this equivalence is functorial in families over \overline M_{g,n}.

This theorem says that the duality is fundamentally a Ran-space/Verdier phenomenon. The Fulton–MacPherson forms and residues are not the theorem; they are one concrete chart on it.

The second main theorem should also be sharpened. The monograph’s own later chapters recognize that bar–cobar inversion fails at admissible or minimal-model singularities. So the right statement is not unconditional inversion, but inversion on the Koszul locus, together with a curved replacement off that locus:

Theorem B (correct form).
If A is modular Koszul, then the counit Ω_X \bar B_X(A) → A is an equivalence in the completed coderived category. If A leaves the Koszul locus, the same bar–cobar object persists but becomes curved; the failure of inversion is measured by higher Ext and by the universal Maurer–Cartan class of the cyclic deformation complex.

This reinterprets “quantum corrections” correctly. They are not errors relative to genus zero. They are the curvature terms of the modular completion of Koszul duality.

Now the genus tower falls into place. The transition genus 0 → 1 → g is best understood as a single Maurer–Cartan deformation of the genus-zero bar differential inside a cyclic L_∞ algebra controlling modular deformations of A. The same datum appears in three disguises.

As a coderivation, it is the curved term m_0^{(g)} in the bar/cobar package.
As a sheaf-theoretic object over moduli, it is a section of the obstruction sheaf on \overline M_g.
As a trace invariant, it lands in cyclic homology and then in the tautological ring, producing scalar shadows such as κ(A) λ_g.

These are not three analogies. They are three realizations of one universal class. The manuscript’s obs_g = κ(A)·λ_g formula and its repeated use of Hodge classes in the explicit genus expansions already point in that direction. The right formal statement is that there is a class
Θ_A ∈ MC(Def_cyc(A) \widehat\otimes RΓ(\overline M_{g,\bullet},\mathbb Q))
whose image in the scalar center is the sequence of obstruction coefficients. In particular, κ(A) is not the concept; it is the first characteristic number of the concept.

This immediately clarifies the complementarity principle. The equation Q_g(A) ⊕ Q_g(A^!) = H^*(M_g,Z(A)), which the manuscript currently states as a direct-sum decomposition, wants to be a Lagrangian-polarization theorem. Verdier duality on factorization homology should endow
RΓ(\overline M_g, Z_A)
with a shifted symplectic pairing. The modular deformation complex of A and the modular obstruction complex of A^! should then embed as opposite Lagrangians. What one algebra sees as tangent directions, the dual sees as obstruction directions, because both are opposite polarizations of a single ambient symplectic deformation problem. In that form, the theorem rhymes much more with Grothendieck–Serre duality and shifted symplectic geometry than with a bare dimension count. It also explains why the present proof in Chapter 12 almost works: it has found the involution and the pairing, but not yet the Lagrangian statement that would make the decomposition literal.

The theorem that ought to exist is therefore:

Theorem C (correct form).
For a modular Koszul pair (A,A^!), there is a shifted-symplectic complex \mathcal H_g(A) canonically identified with RΓ(\overline M_g,Z_A) such that
T^{mod}_g(A) and Ob^{mod}_g(A^!)[-1]
embed as complementary Lagrangians. Consequently
T^{mod}_g(A) ≃ Ob^{mod}_g(A^!)^\vee
and, after choosing a polarization, one obtains a direct-sum decomposition of \mathcal H_g(A).

That is the categorical skeleton the monograph is reaching for.

The discriminant universality fits naturally into this picture. If the same polynomial
Δ(x) = (1-3x)(1+x)
survives across \mathfrak{sl}_2, Virasoro, and βγ, and is stable under Drinfeld–Sokolov reduction, then the mathematically robust interpretation is not “discriminant of a family of curves,” nor “Alexander polynomial,” but the characteristic polynomial of a reduced genus-one transport operator. More precisely, there should be a canonical rank-two piece of the genus-one modular deformation complex,
H^{red}_1(A),
such that
Δ_A(x) = det(1 - x·KS_A | H^{red}_1(A)).
Drinfeld–Sokolov reduction would preserve this polynomial because it preserves the relevant reduced center and its Kodaira–Spencer transport. In that form, the roots 3 and -1 are eigenvalues of genus-one monodromy on the reduced correction complex. The word “discriminant” is then suggestive but slightly misleading; the intrinsic object is a monodromy characteristic polynomial.

The \hat A-genus appearance points in the same direction. The Heisenberg computations already express genus free energies as Hodge integrals. The appearance of \hat A(x)-1 should therefore be read index-theoretically: the genus expansion is the family index density of the modular deformation complex, not merely a formal generating function. One should not insist too literally on a Dirac operator on the coarse stack \overline M_g; stacks are not obliged to present that geometry so naively. The right object is a family Dirac-type operator on the virtual tangent complex of the derived moduli of curves, coupled to the center local system or, better, to the cyclic deformation package of A. The expected formula is of the form
ch Rπ_*(\mathcal D_A) = κ(A)·\hat A(T^{vir}_π),
with the scalar free-energy series arising after pushforward. In other words, the manuscript is brushing against a family index theorem for modular chiral deformation theory.

The Yangian chapter also becomes transparent from this vantage point. The manuscript proves bar–cobar recovery for the E_1-chiral Yangian and separately argues that the quantum parameter transforms by q ↦ q^{-1}, while admitting that the stronger direct compatibility with the Kazhdan–Lusztig functor is only expected, not proved. What this chapter is trying to say is: there should be a derived Drinfeld–Kohno theorem for E_1-chiral Koszul duality. Ordered configuration spaces carry braid monodromy; Verdier duality reverses the orientation of the collision loops; therefore the homotopy-coherent monoidal structure on the dual side sees R replaced by R^{-1}. Under RTT presentations, this is exactly the passage from Yangian data to the opposite quantum-group monodromy. The true theorem is not merely about abelian categories of modules. It is about an equivalence of bar/cobar-enhanced E_1-factorization data whose braid monodromy realizes the Drinfeld–Kohno correspondence up to derived completion.

What, then, is genuinely new here? Not merely “Koszul chiral algebra.” That phrase is too genus-zero, too static. The missing notion is a modular Koszul object: a factorization algebra whose duality data extends over the modular operad of curves, with curvature classes compatible under gluing, Verdier duality, and trace. Such an object has, in addition to its dual A^!, a modular characteristic package:
its Maurer–Cartan class, its center local system, and its characteristic numbers κ_i(A). The scalar κ(A) is only the first shadow of this richer structure. Once named, many disparate computations in the manuscript stop looking like examples and start looking like instances of one theory.

This is the historical rhyme. Classical operadic Koszul duality says: quadratic presentation plus bar–cobar formalism produces homotopy theory. The theory sought here says: factorization presentation on curves plus Verdier duality on modular compactifications produces modular homotopy theory. Drinfeld–Kohno related KZ monodromy to quantum groups. The theory sought here would relate configuration-space/Deligne–Mumford monodromy to curved chiral Koszul duality. And just as étale cohomology supplied the right ambient cohomology theory for Frobenius and zeta functions, factorization homology on Ran(X) together with Verdier duality on \overline M_{g,n} is the right ambient cohomology theory for OPE, monodromy, and bar–cobar duality on curves.

The next monograph writes this theory in its native language. It should be called something like Modular Koszul Duality for Factorization Algebras. Its chapters should do four things. First, build the coderived Ran-space formalism cleanly, with curved objects from the start. Second, prove the Lagrangian form of complementarity. Third, formulate and prove the derived Drinfeld–Kohno theorem for E_1-chiral Koszul objects. Fourth, establish the index theorem explaining the \hat A-genus and the genus-expansion characteristic classes. Only after that should one return to the zoo of examples—affine, Virasoro, W, Yangians, logarithmic models—now as a classification problem for modular Koszul objects rather than as isolated computations.

The deepest sentence is this: the work is trying to show that quantum corrections are not a perturbative afterthought to chiral Koszul duality; they are the modular completion of the duality itself. Once stated that way, the mathematics coheres.
