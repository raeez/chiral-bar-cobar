# Literature Investigation: Bar Constructions for Factorization Algebras

## The Question

How do Costello-Gwilliam, Francis-Gaitsgory, and Lurie define the bar
construction for factorization algebras?  Does their construction
naturally produce E_1 coalgebra structure?  How does this relate to the
manuscript's bar complex B^ch(A), which carries both a differential
(from E_infty/chiral structure) and a coassociative coproduct (from
ordered interval-cutting)?

---

## 1. Three Bar Complexes in the Manuscript

The manuscript explicitly identifies three distinct bar constructions
(Vol I, `ordered_associative_chiral_kd.tex` lines 45-55; Vol II,
`introduction.tex` lines 260-275):

| Bar complex | OPE data used | Symmetry | Koszul dual produced |
|---|---|---|---|
| B^FG(A) (Francis-Gaitsgory) | Only a_{(0)}b (zeroth product = chiral Lie bracket) | Sigma_n-coinvariants | Chiral Lie Koszul dual |
| B^Sigma(A) (symmetric bar) | All OPE products {a_{(n)}b}_{n >= 0} | Sigma_n-coinvariants | Full chiral Koszul dual A^! (Vol I Theorem A) |
| B^ord(A) (ordered bar) | All OPE products | No Sigma_n quotient (retains linear ordering) | Ordered/line dual A^!_line (dg-shifted Yangian) |

The relationships:
- B^ord -> B^Sigma by taking Sigma_n-coinvariants
- The associated graded of B^Sigma (under the pole-order filtration) recovers B^FG

These are THREE DIFFERENT chain complexes with three different coproducts.

---

## 2. Francis-Gaitsgory (FG12, Selecta Math 2012)

**What FG12 constructs.**  Francis-Gaitsgory work in the infinity-category
D-mod^fact(Ran(X)) of factorization D-modules on the Ran space.  Their
bar-cobar adjunction is:

    B : E_1-Alg  <-->  E_1-CoAlg : Omega

This is stated at the abstract infinity-categorical level.  The key
theorem (FG12, main theorem) is that this adjunction is an *equivalence*
when the chiral tensor structure on D-mod(Ran(X)) is pro-nilpotent.
Pro-nilpotence means the tensor powers M^{otimes n} supported on
Ran_{>= n}(X) have vanishing homology as n -> infinity.

**Critical observation from the manuscript.**  Despite the name "chiral
Koszul duality," FG12's bar construction B^FG(A) uses ONLY the zeroth
product a_{(0)}b -- the chiral Lie bracket (simple-pole residue).  It
does NOT see higher OPE poles.  The manuscript states this explicitly:
"The Francis-Gaitsgory bar B^FG(A) uses only the zeroth product
a_{(0)}b and sees the chiral Lie structure" (Vol I,
`ordered_associative_chiral_kd.tex` line 47).

**Coalgebra structure.**  B^FG(A) is a factorization *coalgebra* on
Ran(X).  The coproduct comes from the factorization structure: when the
support set S decomposes as S = S_1 ⊔ S_2 with S_1 ∩ S_2 = empty
(the disjointness locus), the factorization isomorphism gives

    F|_{U_{S_1,S_2}}  ~->  F|_{U_{S_1}} ⊠ F|_{U_{S_2}}.

This coproduct is COCOMMUTATIVE because the factorization isomorphisms
satisfy commutativity constraints (the partition S = S_1 ⊔ S_2 is
unordered).  The factorizable D-module definition (Vol II,
`factorization_swiss_cheese.tex` lines 84-101) makes this explicit:
the factorization isomorphisms satisfy "associativity and commutativity
constraints inherited from the operadic composition for iterated
partitions I = I_1 ⊔ ... ⊔ I_r."

**FG bar = Chevalley-Eilenberg bar of a chiral Lie algebra.**  Since
B^FG uses only the Lie bracket a_{(0)}b, it is essentially the
Chevalley-Eilenberg complex of A viewed as a chiral Lie algebra.  The
output is a cocommutative coalgebra (the Chevalley-Eilenberg coalgebra
is always cocommutative, being the symmetric coalgebra on the
suspension of the Lie algebra).

**What FG12 misses.**  Because B^FG sees only zeroth poles, it does NOT
detect:
- The curvature kappa(A) (which comes from higher poles)
- The R-matrix (which requires the full OPE)
- The shadow obstruction tower beyond arity 2
- The A_infinity structure of the bar complex

The manuscript's `conj:FG-shadow` (now a theorem, Vol I line 5669)
states that B^FG is the *commutator shadow* of the ordered bar: there
is a spectral sequence E_1 = B^FG(gr_com A) ==> gr_com B^ord(A).

---

## 3. Costello-Gwilliam (CG17/CG21, Cambridge UP)

**What CG construct.**  Costello-Gwilliam work with prefactorization
algebras in the differential-geometric (not algebraic/D-module) setting.
Their factorization algebras satisfy a cosheaf condition (Weiss descent)
on opens of a manifold.

**Bar construction.**  For a factorization algebra F on a manifold M,
the bar construction is factorization homology:

    integral_M F  =  H_*(B^geom(A))

(Vol I, `bar_construction.tex` lines 287-294).  The coalgebra structure
arises from decompositions X = X_1 ⊔ X_2:

    integral_X A  ->  integral_{X_1} A  otimes  integral_{X_2} A

This coproduct is again cocommutative: it is indexed by UNORDERED
decompositions of the manifold.

**The CG framework is E_infty.**  CG's factorization algebras on a
manifold M of real dimension n are E_n-algebras (via the
Fulton-MacPherson operad FM_n ~ E_n).  For n = 2 (surfaces/curves),
these are E_2-algebras.  The associated bar construction produces
E_2-coalgebras.

**Connection to the manuscript.**  The manuscript identifies (Vol I,
`en_koszul_duality.tex` Corollary cor:n2-recovery, line 630): "the
chiral bar-cobar adjunction of Theorem A is recovered from the E_2
bar-cobar adjunction by equipping the underlying E_2-algebra A^top
with the holomorphic propagator eta_{ij} = d log(z_i - z_j) in place
of the topological propagator G."

The CG bar construction, as an E_2-coalgebra, carries a coproduct that
is cocommutative up to E_2-coherences.  This is the SYMMETRIC bar
B^Sigma(A) of the manuscript.

---

## 4. Lurie (Higher Algebra, Section 5.2)

**The general E_n Koszul duality.**  Lurie establishes:

    B_{E_n} : E_n-Alg  <-->  E_n-CoAlg : Omega_{E_n}

The bar of an E_n-algebra is an E_n-coalgebra.  The key instances:

| n | Algebra type | Bar produces | Coproduct type |
|---|---|---|---|
| 1 | Associative (A_infty) | Coassociative coalgebra | Non-cocommutative (deconcatenation) |
| 2 | E_2 (braided) | E_2-coalgebra | Cocommutative up to E_2-coherences |
| infty | Commutative (E_infty) | Cocommutative coalgebra | Fully cocommutative |

This is stated in the manuscript at Vol I, `en_koszul_duality.tex`
lines 562-582 and Theorem thm:en-koszul-duality (lines 585-618),
citing Lurie HA Section 5.2, Francis Theorem 4.20, and
Ayala-Francis Theorem 7.8.

**The critical point.**  An E_infty-algebra can be viewed as an
E_n-algebra for any n (by forgetting structure).  The bar RELATIVE TO
E_n then produces an E_n-coalgebra.  In particular:

- B_{E_infty}(A) is an E_infty-coalgebra (cocommutative)
- B_{E_1}(A) is an E_1-coalgebra (coassociative, non-cocommutative)

These are DIFFERENT objects applied to the SAME algebra A.  The bar
construction depends on which operad you are working relative to.

---

## 5. THE KEY QUESTION: Why Does the Manuscript's Bar Have a Non-Cocommutative Coproduct?

### The apparent paradox

A chiral algebra (vertex algebra) is E_infty-chiral (local,
Sigma_n-equivariant -- see Vol II CLAUDE.md AP35: "Every BD chiral
algebra is E_infty-chiral").  The E_infty bar B_{E_infty}(A) would
give a cocommutative coalgebra.  But the manuscript's ordered bar
B^ord(A) has a NON-cocommutative (coassociative, deconcatenation)
coproduct.  How?

### The resolution: two different bar constructions coexist

The manuscript actually has BOTH:

**(a) The symmetric bar B^Sigma(A) = Vol I Theorem A's bar complex.**
This is the E_infty (or more precisely E_2) bar.  Its coproduct sums
over ALL unordered bipartitions I ⊔ J = [0,n] of the index set
(Vol I, `bar_construction.tex` line 1431):

    Delta(a_0 ⊗ ... ⊗ a_n ⊗ omega)
      = sum_{I ⊔ J = [0,n]} (a_I ⊗ omega_I) ⊗ (a_J ⊗ omega_J)

This is a COCOMMUTATIVE coproduct.  It is the factorization coalgebra
on Ran(X).

**(b) The ordered bar B^ord(A) = Vol II's E_1 bar.**
This is the E_1 bar.  Its coproduct is DECONCATENATION: only
consecutive splits (Vol II, `foundations.tex` lines 1660-1673,
1728-1734):

    [a_1|...|a_n]  |->  sum_{i=0}^{n} [a_1|...|a_i] ⊗ [a_{i+1}|...|a_n]

This is a NON-cocommutative (coassociative) coproduct.  It is the
cofree conilpotent coalgebra T^c(s^{-1} A-bar) with its unique
coassociative coproduct compatible with the cogenerators.

### The Swiss-cheese structure unifies both

The central claim of Vol II (`foundations.tex` lines 1792-1797):

> "The bar complex of Volume I, equipped with its coproduct, is a
> coalgebra over SC^{ch,top}."

The two-coloured Swiss-cheese operad SC^{ch,top} has:
- **Closed colour** from FM_k(C): the differential d_B (from OPE
  residues on holomorphic configuration spaces)
- **Open colour** from E_1(m) = Conf_m^<(R): the coproduct Delta
  (from ordered interval-cutting on the real line)

A bar element of degree k is parametrised by FM_k(C) x Conf_k^<(R)
(Vol II, `introduction.tex` lines 204-207).

The differential is the E_infty/E_2 structure (symmetric,
holomorphic).  The coproduct is the E_1 structure (ordered,
topological).  Together they form an SC^{ch,top}-coalgebra.

### Why the E_1 bar is preferred

The ordered bar B^ord(A) carries STRICTLY MORE information than the
symmetric bar B^Sigma(A).  The descent map B^ord -> B^Sigma takes
Sigma_n-coinvariants, losing information.  The lost information is
precisely:

1. **The R-matrix** R(z): the monodromy of the OPE viewed on ordered
   configurations.  For E_infty-chiral algebras with poles (all
   interesting vertex algebras), R(z) != tau (the Koszul-signed flip)
   and carries nontrivial spectral content.

2. **The A_infinity operations** m_k: the coderivation of the cofree
   coalgebra T^c(s^{-1} A-bar) encodes ALL A_infinity operations
   simultaneously.  The symmetric bar sees only Sigma_n-coinvariants
   of these operations.

3. **The line category**: the open-colour Koszul dual A^!_line is the
   dg-shifted Yangian, which is invisible to the closed colour alone.

The universal property (Vol II, `foundations.tex` Corollary
cor:R-factorization-lagrangian, lines 1753-1770): the deconcatenation
coproduct is the UNIQUE coassociative coproduct on the cofree
conilpotent coalgebra T^c(s^{-1} A-bar) compatible with the
cogenerators.  It carries no independent data beyond the holomorphic
differential.  In other words: given the E_infty structure (the
differential), the E_1 structure (the coproduct) is FORCED.

---

## 6. Comparison Table

| Source | Bar type | Operad | Coproduct | Sees higher poles? |
|---|---|---|---|---|
| Francis-Gaitsgory | B^FG(A) | chiral Lie | Cocommutative (CE coalgebra) | No (only a_{(0)}b) |
| Costello-Gwilliam | factorization homology | E_2 / E_infty | Cocommutative (factorization) | Yes (all OPE) |
| Lurie HA 5.2 | B_{E_n}(A) | E_n | E_n-coalgebra | Depends on operad choice |
| Vol I Theorem A | B^Sigma(A) | E_infty-chiral | Cocommutative (unordered bipartitions) | Yes (all OPE) |
| Vol I/II ordered | B^ord(A) | E_1 on T^c | Coassociative (deconcatenation) | Yes (all OPE) |

---

## 7. Universal Property of B^ch(A)

The manuscript provides a universal characterization (Vol II,
`foundations.tex` lines 1753-1770 and Remark rem:R-factorization-lagrangian-heuristic):

**Theorem (Uniqueness of cofree coproduct).**  The topological
coproduct Delta carries no independent data beyond the holomorphic
differential.  The R-factorization is determined as the unique
coassociative coproduct on the cofree coalgebra T^c(s^{-1} A-bar)
compatible with the cogenerators.

**Lagrangian interpretation** (heuristic, lines 1772-1790): The cofree
coalgebra T^c(N*[-1]) on the shifted conormal bundle of a Lagrangian
embedding L -> M carries a canonical deconcatenation coproduct, and the
self-intersection L x_M L is presented by this coalgebra.  In this
picture:
- Delta is the diagonal of the self-intersection groupoid
- The desuspension s^{-1} is the cotangent shift T[-1] forced by the
  Lagrangian condition
- The cofree coalgebra is the symmetric algebra on conormal fibers

The E_1 bar is preferred over the E_infty bar because:
1. It is the cofree coalgebra on the cogenerating space -- the most
   natural algebraic object
2. It remembers the full A_infinity structure (not just its
   Sigma_n-coinvariant shadow)
3. It is the universal boundary condition: the cofree resolution of A
   viewed from the R-direction
4. Its linear dual (on the Koszul locus) is the dg-shifted Yangian --
   the open-colour Koszul dual
5. The coproduct is UNIQUE (no choices involved)

---

## 8. Summary of Findings

### How the three groups define bar constructions:

- **Francis-Gaitsgory**: infinity-categorical, uses only chiral Lie
  bracket (zeroth pole), produces cocommutative coalgebra.  This is the
  "weakest" bar -- it misses higher OPE poles entirely.

- **Costello-Gwilliam**: differential-geometric (prefactorization
  algebras), uses factorization homology, produces E_2-coalgebra
  (cocommutative up to E_2-coherences).  This is the "symmetric" bar.

- **Lurie**: infinity-categorical framework for E_n-Koszul duality.
  The bar of an E_n-algebra is an E_n-coalgebra.  For E_infty-algebras,
  the bar is E_infty-coalgebra (cocommutative).  But the SAME algebra
  can be barred relative to E_1, producing an E_1-coalgebra
  (coassociative).

### Does their construction naturally produce E_1 coalgebra structure?

NO for FG12 and CG17: their constructions produce cocommutative (or
E_2-cocommutative) coalgebras because they work with unordered
configuration spaces.

YES for Lurie, but only when you CHOOSE to bar relative to E_1.
Lurie's framework allows barring relative to any E_n; the choice of n
determines the coalgebra type.

### The manuscript's contribution:

The manuscript's key insight is that for a chiral algebra A, BOTH bars
coexist and carry complementary information:
- The E_infty bar B^Sigma(A) is the closed-colour factorization
  coalgebra on Ran(X)
- The E_1 bar B^ord(A) = T^c(s^{-1} A-bar) with deconcatenation
  coproduct is the open-colour coalgebra

Together they form an SC^{ch,top}-coalgebra.  The Swiss-cheese
structure is not an ansatz but a theorem: given the holomorphic
differential, the topological coproduct is forced by the universal
property of the cofree coalgebra.

### Key compatibility statement:

The Vol I bar_construction.tex chapter's coproduct (summing over
unordered bipartitions I ⊔ J) is the E_infty/symmetric coproduct,
consistent with B^Sigma(A) being a factorization coalgebra.  The Vol II
foundations.tex chapter's coproduct (deconcatenation) is the
E_1/ordered coproduct, consistent with B^ord(A) being the cofree
coalgebra.  The descent map B^ord -> B^Sigma takes coinvariants and
sends deconcatenation to the unshuffle coproduct.

---

## 9. Potential Issue in Vol I bar_construction.tex

**Observation.** The coproduct in Vol I `bar_construction.tex` Theorem
thm:coassociativity-complete (line 1420) is defined by summing over ALL
bipartitions I ⊔ J = [0,n] -- this is the UNSHUFFLE (cocommutative)
coproduct, appropriate for the symmetric bar B^Sigma(A).  However, the
coderivation proof at line 1563 mentions "the deconcatenation coproduct
Delta([a_1|...|a_n]) = sum_{i=0}^n [a_1|...|a_i] ⊗ [a_{i+1}|...|a_n]"
which is the ORDERED (non-cocommutative) coproduct.  These are two
different coproducts on the same underlying graded vector space.

This is not necessarily an error -- the same chapter may be discussing
both the symmetric bar (for Theorem A) and the ordered bar (for the
A_infinity structure) -- but the notation could be clearer about which
coproduct is meant in which context.  The chapter's Convention
conv:bar-coalgebra-identity identifies B(A) as a "factorization
coalgebra" which is the symmetric/cocommutative version.  The ordered
bar is developed in the separate chapter
`ordered_associative_chiral_kd.tex`.

---

## 10. Bibliographic References

- [FG12] J. Francis and D. Gaitsgory, "Chiral Koszul duality,"
  Selecta Math. 18 (2012), no. 1, 27-87.
- [CG17] K. Costello and O. Gwilliam, "Factorization Algebras in
  Quantum Field Theory," vols. 1-2, Cambridge UP, 2017/2021.
- [HA] J. Lurie, "Higher Algebra," Section 5.2.
- [AF15] D. Ayala and J. Francis, Theorem 7.8 (Poincare-Koszul duality).
- [Francis2013] J. Francis, Theorem 4.20 (E_n-Koszul inversion).
- [LV12] J.-L. Loday and B. Vallette, "Algebraic Operads,"
  Proposition 1.2.9 (cofree coalgebra uniqueness).
- [BD04] A. Beilinson and V. Drinfeld, "Chiral Algebras."
