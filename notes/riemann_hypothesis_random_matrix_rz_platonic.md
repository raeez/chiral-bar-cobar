# RH via Random Matrix Theory of the Spectral R(z): First-Principles Audit

Montgomery 1973 + Keating-Snaith 2000 identify the non-trivial zeros of ζ(s),
normalized, with eigenvalue statistics of the Gaussian Unitary Ensemble (GUE).
Katz-Sarnak embed this into a broader trace-formula picture linking L-function
zeros to eigenvalues of Frobenius on étale cohomology. The programme's
spectral R-matrix R(z) ∈ End(V ⊗ V) is the genus-zero, binary-collision
residue of the open/closed Maurer-Cartan element (`thm:spectral-R-as-residue`
in spectral-braiding-core.tex). The present question: do R(z) eigenvalues, in
appropriate limits, exhibit GUE statistics, and if so is there a chiral
algebra A_RH whose R-matrix spectrum matches the Riemann zeros?

## (1) R(z) eigenvalues on V_k(sl_2) fundamental

For the rational Yangian Y_ℏ(sl_2) (provenance (b) of
`rem:two-provenances`), the R-matrix on the fundamental V = C^2 is Yang's
matrix:

```
R(u) = (u · I + ℏ · P) / (u + ℏ) ∈ End(V ⊗ V)
```

where P(v ⊗ w) = w ⊗ v is the permutation, u is the spectral parameter
(difference of evaluation parameters), and ℏ is the loop parameter. On
V ⊗ V = Sym²(V) ⊕ ∧²(V) = C³ ⊕ C:

- **Sym² (triplet):** P = +id, R(u) = (u + ℏ)/(u + ℏ) = 1. Eigenvalue 1,
  multiplicity 3.
- **∧² (singlet):** P = -id, R(u) = (u - ℏ)/(u + ℏ). Single eigenvalue
  f(u) := (u − ℏ)/(u + ℏ), multiplicity 1.

**At level k for V_k(sl_2) via KL94.** Under Kazhdan-Lusztig
semisimplification at non-critical level k, the chiral R-matrix is the
trigonometric q-deformation with q = exp(iπ/(k+2)):

```
R_k(u) on ∧²: λ_k(u) = (q⁻¹ u − q)/(u − 1) = (u − q²)/q(u − 1)
```

There are **only two distinct eigenvalues** on V ⊗ V for fundamental sl_2:
one on Sym² and one on ∧². A four-level spectrum with multiplicity
structure (3, 1) cannot exhibit GUE pair correlation: the Wigner surmise
R_2(r) = 1 − (sin πr/πr)² requires a continuous unfolded density, and two
levels give a degenerate point mass at r = 0 from the triple degeneracy plus
one isolated gap. **The fundamental representation carries no GUE signal.**

## (2) Large-dim V_λ limit and pair correlation

For V = V_λ of dimension λ + 1, Tarasov-Jimbo's decomposition gives

```
V_λ ⊗ V_λ = ⊕_{j=0}^{λ} V_{2λ − 2j}
```

and R(u) acts as the scalar

```
R_j(u) = ∏_{i=1}^{j} (u − iℏ)/(u + iℏ),    j = 0, 1, ..., λ
```

on the j-th component with multiplicity dim(V_{2λ − 2j}) = 2λ − 2j + 1.
This is a classical Drinfeld-Chari-Pressley formula; independent source:
Molev 2007 §2.5 (Theorem 2.3.1). **Eigenvalues are parameterised by a
discrete index j ∈ {0, ..., λ}, NOT by a continuous parameter.**

**Taking log: θ_j(u) := −i log R_j(u) = Σ_{i=1}^{j} [arg(u − iℏ) − arg(u + iℏ)].**
At fixed real u with ℏ small, θ_j(u) ≈ −2ℏ Σ_{i=1}^{j} i/(u² + i²ℏ²).
The spacings s_j = θ_{j+1} − θ_j satisfy

```
s_j ≈ −2ℏ(j+1)/(u² + (j+1)²ℏ²),    j = 0, ..., λ − 1
```

**Unfolded density.** With j-density normalized to unity on the interval
[0, λ], the unfolded gaps are ρ(j) ds_j = dj, giving ρ(s) ∝ 1/s² locally
(Wigner-Dyson small-s repulsion **absent**) and clustering toward s = 0
as j → λ.

**Verdict.** The spacing distribution is NOT GUE. It is not GOE or GSE
either. It is a **deterministic arithmetic distribution** dominated by the
rational structure (u − iℏ)/(u + iℏ); the eigenvalues are points on the
unit circle at angles θ_j with θ_j − θ_{j−1} monotonically decreasing, no
level repulsion, no Dyson P(s) ∝ s^β small-s behaviour. The Yangian
R-matrix eigenvalues are rigid, not random.

**Root-of-unity case (KL94 reduced tensor category at k ∈ Z_{>0}).** At
integer admissible level k, the reduced category R(k+2) has finitely many
simple objects labeled λ ∈ {0, 1, ..., k}. R-matrix eigenvalues are roots
of unity at q² = exp(2πi/(k+2)). Level-spacing distribution here IS
computed by Keating-Snaith-style methods for characteristic polynomials
of unitary matrices in specific ensembles. **This is where the RMT
connection could live, not in the generic rational setting.**

## (3) Candidate A_RH: Russian school criterion

The Berry-Keating H = xp heuristic identifies ζ-zeros as eigenvalues of a
hypothetical Hermitian H ≈ xp on a Hilbert space. Connes 1999 proposes an
absorption-spectrum version on adele-class space. The programme's natural
candidate is:

**A_RH := H^*(BGL_1(A)) · V_E8 · C[x]/(ζ(s))**, the E_8 lattice VOA
(kappa_BKM-saturated per Vol III AP-CY37) paired with adelic GL_1 via
Frenkel-Zhu Zhu algebra. The level-k lattice theta of V_E8 factors (via
`thm:shadow-spectral-correspondence`) as

```
ε⁸_s(V_E8) = 240 · 2⁻ˢ · ζ(s) · ζ(s − 3).
```

The shadow-spectral correspondence gives shadow depth d(V_E8) = 1 (one
L-factor Eisenstein, zero cuspidal). This identifies d with a critical-line
count, not a zero count.

**Counting check.** Number of Riemann zeros in [T, T + ΔT] satisfies
Riemann-von Mangoldt: N(T) = (T/2π) log(T/2π) − T/2π + O(log T). Number
of eigenvalues of R_E8(z) on V_E8 ⊗ V_E8 in a corresponding spectral
window: the 248-dimensional adjoint E_8 paired tensor has 248² = 61504
eigenvalues, bounded, independent of T. **These two counts do not match:
finitely many R-matrix eigenvalues cannot encode the infinite ζ-zero
count.**

For an infinite-dimensional candidate: affine E_8 at level k has infinite
character decomposition, but eigenvalues of R̂(z) on L(Λ_0) ⊗ L(Λ_0) are
labeled by weights of integrable highest-weight modules, discrete lattice
points in the positive Weyl chamber. The count in a spectral window
grows polynomially in T (Weyl-denominator asymptotic), NOT like
(T log T)/2π. **Mismatch persists.**

## Conclusion: RMT-RH route does NOT close through the programme's R(z)

**Three honest conclusions:**

1. The Yangian R-matrix on fundamental V_k(sl_2) has a 2-eigenvalue
   spectrum (3, 1) on V ⊗ V; no statistical content. **No GUE.**

2. The generic V_λ (large λ) R-matrix has rigid, deterministic
   eigenvalue spacings θ_j − θ_{j−1} ∝ 1/j with no level repulsion; this
   is the OPPOSITE of Wigner-Dyson. At roots of unity the reduced
   category's finite eigenvalue list is uniformly distributed on the
   circle (Haar-like by Weyl integration), potentially Keating-Snaith-
   matching for characteristic polynomials of specific ensembles —
   but this is a sub-convexity observation, not a route to Montgomery.

3. The Riemann-von Mangoldt count (T log T)/2π does not match any
   algebraic eigenvalue growth from a finite-generator chiral algebra's
   R-matrix. Infinite-rank affine / W_∞ / full Virasoro tensor categories
   give polynomial or exponential growth in T, not (T log T)/2π. The
   arithmetic density of ζ-zeros is structurally incompatible with
   algebraic spectra of Yangian / W-algebra R-matrices.

**Structural obstruction (restating rem:structural-obstruction of the
motivic-shadow note).** The spectral parameter u in R(u) lives on C with
poles at u = iℏZ (rational Yangian) or on C* with roots-of-unity poles
(trigonometric). Riemann zeros live at fixed real part 1/2 with imaginary
part given by a transcendental density (T log T)/2π. The programme's
R-matrix poles and the ζ-zero imaginary parts live on a priori different
loci; no algebraic bijection is possible.

**What the programme CAN say about RMT-RH.** Keating-Snaith's identification
of ζ-moments with moments of |det(I − U)| for Haar-random U has a
programme-internal analogue: moments of the chiral Casimir divisor
determinant on R-twisted Σ_n-descent in Thm A^{∞,2} produce a Hurwitz-Lerch
moment formula. `cor:casimir-moments` computes the first three moments;
they match the Keating-Snaith Mₖ(U(N)) values at k = 1, 2 but diverge at
k = 3 because the programme's moments are rational in the level k, while
Keating-Snaith's are polynomial in N with Barnes-G coefficients. **The
moments match at low order, diverge at order 3, and therefore do not give
a programme-internal ζ-moment prediction.**

**Where a weak positive result lives.** For the E_8 lattice VOA at level
k = 1, the R-matrix eigenvalues on V_{E_8} ⊗ V_{E_8} distribute on the
Weyl orbit of a fundamental weight. By Weyl's equidistribution, this is a
discrete uniform measure on a 240-point orbit. Its pair-correlation
function is computable exactly and matches a Poisson process at scale
≫ 1/240, NOT GUE at scale ≪ 1. Thus **even for the E_8 case, the
statistics are Poisson at the visible scale, not GUE**. GUE emerges only
for random Hermitian matrices with continuous spectrum; the programme's
R-matrices are quantum group elements with algebraic spectrum.

## Verdict

The RMT-RH route does not close through the programme's R(z). Three
obstructions:

- (i) finite/discrete spectrum of R(z) on any fixed tensor product;
- (ii) arithmetic density mismatch: (T log T)/2π vs. polynomial growth;
- (iii) Keating-Snaith moments diverge from programme moments at k = 3.

The motivic-shadow route (existing note `riemann_hypothesis_motivic_shadow_platonic.md`)
remains the nearest programme-internal connection, giving a combinatorial
prediction of Hecke-factor counts for lattice-VOA theta series and a
sub-convexity Ramanujan bound independent of Weil. No RMT-based closure
is available.

**Strongest honest form.** The programme gives:
(a) a combinatorial shadow-depth / Hecke-factor count identity for
    lattice VOAs (Theorem `thm:shadow-spectral-correspondence`);
(b) a Rankin-type subconvexity bound for admissible V_k(sl_2) characters
    independent of Deligne/Weil;
(c) a verification that R-matrix eigenvalue statistics are algebraic,
    not Wigner-Dyson, even in large-representation limits.

None of (a)-(c) reach Montgomery's pair correlation conjecture or RH.
The honest position after the Platonic reconstitution is that the R(z)
route to RMT-RH is **structurally closed against**; progress on
zero-location questions lies outside the programme's current scope
(requires analytic continuation of shadow-L off the real spectral line,
which the programme does not yet provide beyond classical Rankin-Selberg).

## Literature pointers and anchors

- Montgomery 1973: pair correlation R_2(r) = 1 − (sin πr/πr)² for ζ-zeros
  on the unfolded scale; established for the 2-point function only.
- Odlyzko 1989-2001: computational verification at T ≈ 10^{20}; extends to
  n-point correlations; 8+ significant digits.
- Keating-Snaith 2000: ζ-moments = moments of |det(I − U)| for Haar-random
  U ∈ U(N); reproduces Conrey-Ghosh and Conrey-Gonek conjectures.
- Katz-Sarnak 1999: local statistics of L-function zeros near low heights
  match different symmetry classes (U, USp, O) depending on L-function
  family; NOT universal GUE.
- Berry-Keating 1999: H = xp heuristic; non-rigorous.
- Rudnick-Sarnak 1996: n-point correlations for principal L-functions
  conjecturally GUE; proven for partial sum restrictions.
- Sieber-Richter 2001: periodic-orbit pair correlation formula.

## Cross-references

- Vol II `thm:spectral-R-as-residue`: R(z) = Res^{coll}_{0,2}(Θ^{oc}).
- Vol II `thm:shadow-spectral-correspondence`: shadow depth ↔ Hecke factor
  count for lattice VOAs.
- `rem:structural-obstruction` (motivic-shadow note): real-line vs
  complex-line spectral parameter barrier.
- Vol III AP-CY37: κ_BKM = c_N(0)/2 for Borcherds-weight lattices.
- Vol II `rem:two-provenances`: R(z) from chiral OPE vs. independent
  Yangian input; the latter is what is tested here.
- Vol II FM99 (landscape_census): Yangian-Gaudin normalisation via GRT^fin
  Casimir rescaling; irrelevant to eigenvalue-statistics question.
