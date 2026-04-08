# E_1 Verdier Intertwining: Investigation

## The Question

Theorem A (thm:bar-cobar-isomorphism-main) establishes the Verdier
intertwining D_Ran(B(A)) = B(A!) for the symmetric bar B = B^Sigma.
Does an ordered version exist: D^ord_Ran(B^ord(A)) = B^ord(A!)?
Or does the ordering break Verdier duality?

## What Theorem A Says

The Verdier intertwining (bar_cobar_adjunction_curved.tex, line 52
and cor:koszul-dual-cooperad at line 6469) states:

  D_Ran B_X(A) = A^!_infty

where D_Ran is Verdier duality on the Ran space, B_X(A) is the
symmetric bar (a cocommutative factorization coalgebra), and
A^!_infty is the homotopy Koszul dual (a factorization algebra
whose underlying complex is B(A!)).  Convention conv:bar-coalgebra-
identity records this identification.

The key structural input: D_Ran acts on sheaves on Ran(X), which
parametrizes finite subsets of X.  The symmetric bar lives on
Ran(X) precisely because it is Sigma_n-coinvariant: it assigns
data to unordered collections of points.

## What the Manuscript Says About E_1 Verdier Intertwining

### Theorem A^{E_1} (e1_modular_koszul.tex, thm:e1-theorem-A-modular)

The E_1 version of Theorem A establishes the ordered bar-cobar
adjunction:

  Cobar^(g) -| B^ord(g) : Alg_{FAss} <-> Coalg_{FAss}

This is an adjunction between FAss-algebras and FAss-coalgebras
(the associative modular operad), NOT between sheaves on Ran(X).

The Verdier intertwining content appears only in the proof
(line 828): "the opposite-duality identification B^ord(A^op) =
B^ord(A)^cop is encoded at the arity-2 shadow level by
R^{E_1,bin}(z;hbar).  This is the E_1 analogue of Verdier
intertwining on the ordered bar surface."

### The Categorical DK Report (categorical_dk_e1_report.md)

The report identifies this explicitly as a gap (lines 126-131):

  "Theorem A includes Verdier intertwining D_Ran(B(A)) = B(A!),
  which is an E_infty statement with no direct E_1 counterpart
  in the manuscript.  An E_1 Verdier intertwining would identify
  D_Ran(B^ord(A)) with something involving A!, but the ordered
  Verdier duality has not been developed."

The report formulates a natural conjecture (lines 161-166):

  "There exists an E_1 Verdier intertwining theorem identifying
  D_Ran(B^ord(A)) with an ordered version of B(A!), and the
  full DK-5 comparison is the categorical shadow of this E_1
  intertwining at the module-category level."

### The Two-Colour Double Koszul Duality
(ordered_associative_chiral_kd.tex, thm:two-colour-double-kd)

This theorem treats the two-colour structure: the closed colour
(symmetric bar on Ran(X)/Sigma_n, dualised by D_Ran) and the open
colour (ordered bar on Conf_n^<(R), dualised by linear duality).
The open colour uses LINEAR DUALITY, not Verdier/Ran duality.
This is the key structural difference.

## Why the Ordering Complicates Verdier Duality

Three obstructions prevent a naive D_Ran(B^ord(A)) = B^ord(A!):

### 1. Domain mismatch

B^ord(A) lives on ORDERED configurations Conf_n^<(X), not on
Ran(X).  The Ran space parametrises unordered finite subsets;
Conf_n^< parametrises ordered tuples of distinct points.  Verdier
duality D_Ran is defined on sheaves on Ran(X).  To apply it to
B^ord(A), one would need either:

(a) A "Verdier duality on ordered configuration spaces"
    D_{Conf^<}, which is not standard, or

(b) To view B^ord(A) as a sheaf on Ran(X) via the projection
    Conf_n^< -> Ran(X), then apply D_Ran.  But this projection
    is the Sigma_n-quotient map, so the pushforward recovers
    B^Sigma(A) = B(A), losing the ordering.

### 2. Coalgebra structure mismatch

B^ord(A) is a coassociative (but not cocommutative) coalgebra
with deconcatenation coproduct.  D_Ran converts coalgebras to
algebras.  For the symmetric bar (cocommutative), D_Ran(B(A))
is naturally a commutative factorization algebra.  For the ordered
bar, D_Ran would need to convert a non-cocommutative coalgebra
to an algebra, producing an associative (non-commutative)
factorization algebra.  This is possible but requires the ribbon
modular operad structure, not the commutative one.

### 3. The correct E_1 analogue is opposite-duality, not Verdier

The manuscript (e1_modular_koszul.tex, line 828) already identifies
the correct E_1 analogue: opposite-duality.  The identification

  B^ord(A^op) = B^ord(A)^cop

is the ordered version of Verdier intertwining.  Here A^op is the
opposite algebra (reversing the cyclic ordering at each vertex of
the ribbon modular operad), and ()^cop is the co-opposite coalgebra
(reversing the deconcatenation).  This is a statement about the
SAME algebra, not about the Koszul dual A!.

The Koszul dual enters through the R-matrix: the arity-2 shadow
R^{E_1,bin}(z;hbar) satisfies the anti-symmetry property

  R^{E_1,bin}_{A^op}(z;hbar) = R^{E_1,bin}_A(z;hbar)^{-1}

which encodes the relationship between A and A! at the E_1 level.
Taking Sigma_2-coinvariants recovers the scalar statement
kappa(A) + kappa(A!) = 0 (for KM/free fields).

## Assessment

An ordered Verdier intertwining D_Ran(B^ord(A)) = B^ord(A!) in
the naive sense does NOT exist, because of the domain mismatch
(Ran vs ordered configurations) and the coalgebra type mismatch
(cocommutative vs coassociative).

The correct E_1 analogue is the OPPOSITE-DUALITY identification

  B^ord(A^op) = B^ord(A)^cop

which is proved (thm:e1-theorem-A-modular proof, line 822-829).
This is a statement within the FAss world (ribbon surfaces, ordered
configurations), not a statement about Ran-space Verdier duality.

The passage from E_1 to E_infty is the averaging map av, which
sends the opposite-duality identification to Verdier intertwining:

  av(B^ord(A^op) = B^ord(A)^cop)
      |-> D_Ran(B(A)) = B(A!)

This is consistent with the general principle: Theorem A is an
E_infty statement, and its E_1 ancestor uses the ribbon modular
operad and opposite-duality rather than Ran-space Verdier duality.

To make "DK = un-averaged Theorem A" literally true at the Verdier
level, one would need to develop D_{Conf^<} (Verdier duality on
ordered configuration spaces) or work with the ribbon Ran space
Ran^{rib}(X).  This is not developed in the manuscript and is a
genuine open direction.

## Sources

- chapters/theory/bar_cobar_adjunction_curved.tex lines 42-52,
  6463-6470
- chapters/theory/e1_modular_koszul.tex lines 775-830
- chapters/theory/ordered_associative_chiral_kd.tex lines 2822-2860
- compute/audit/categorical_dk_e1_report.md lines 74-170
