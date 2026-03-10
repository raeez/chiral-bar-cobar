# Old Abstract (pre-modular homotopy theory rewrite)

Saved 2026-03-10 before deepening pass.

---

Classical Koszul duality is a theorem about quadratic algebras on a point.
Chiral algebras live on algebraic curves.
We develop a geometric analogue of Koszul duality in one dimension,
relating chiral algebras to their duals through the global geometry of
configuration spaces.
The duality is a higher-dimensional Fourier transform, with the
logarithmic propagator as kernel and Verdier duality as inversion
formula; for the Heisenberg algebra it specializes to the classical
Fourier transform on the Jacobian.

For a chiral algebra A on a smooth algebraic curve X, we realize the
bar-cobar adjunction through residue calculus on the Fulton–MacPherson
compactification C̄_n(X).
The logarithmic form η_{ij} = dlog(z_i - z_j) is the propagator:
its residues extract operator product coefficients from boundary divisors,
and the Arnold relations force the differential to square to zero.
Verdier duality on Ran(X) intertwines the bar of A
with the bar of its Koszul dual A!, realizing chiral Koszul duality
as non-abelian Poincaré duality.

At genus zero this recovers Beilinson–Drinfeld.
At genus g ≥ 1 the bar differential acquires curvature:
d_fib² = κ(A)·ω_g,
where κ(A) is a scalar extracted from the leading OPE singularity
and ω_g is a tautological class on M̄_g.
Period integrals along cycles of the curve restore nilpotence of the total
differential.  The curvature is the geometric origin of central extensions
and anomalies in conformal field theory; its cancellation between dual
algebras is the content of a complementarity that has no classical
analogue.

Four main theorems are established.
(A) Geometric bar-cobar duality with Verdier intertwining,
functorial over M̄_{g,n}.
(B) Bar-cobar inversion on the Koszul locus: the counit
Ω(B̄(A)) → A is a quasi-isomorphism and the spectral
sequence collapses at E_2.
(C) Deformation-obstruction complementarity: for a Koszul pair (A, A!),
Q_g(A) ⊕ Q_g(A!) ≃ H*(M̄_g, Z(A)),
so that the genus-g quantum corrections of an algebra and its dual are
complementary Lagrangians in the cohomology of moduli—what one sees as
deformation, the other sees as obstruction.
(D) The modular characteristic theorem: κ(A) is universal,
additive under tensor product, anti-symmetric under Koszul duality, and
its generating function is the Â-genus.

All constructions are rendered explicitly computable through chain-level
algorithms.
Complete worked examples include the Heisenberg algebra, affine Kac–Moody
algebras at dual levels k ↔ −k − 2h∨, and W-algebras
with their curved A∞ Koszul duals.
