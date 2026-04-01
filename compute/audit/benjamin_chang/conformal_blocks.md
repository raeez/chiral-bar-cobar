# Conformal Blocks, KZ/BPZ Monodromy, and the Recovery of epsilon^c_s

## The Question

Does the KZ/WZW connection (or its BPZ substitute for Virasoro) capture
the constrained Epstein zeta epsilon^c_s through its monodromy?  More
precisely: does the monodromy of the flat connection on conformal blocks
determine the primary spectrum {h_lambda}, and thereby determine
epsilon^c_s = sum (2*Delta)^{-s}?

## Summary of Findings

The answer stratifies sharply by the four-level hierarchy of the
manuscript (rem:four-levels in concordance.tex, line 4152):

- **Level 0** (scalar invariant kappa): captures ONE number, the modular
  characteristic.  This is Theorem D.  It does NOT determine the primary
  spectrum.

- **Level 1** (bar cohomology H*(B^(g)(A))): captures the DIMENSIONS of
  conformal block spaces at each genus.  For sl_2 at level k, genus 1:
  a (k+1)-dimensional space.  This is richer than kappa alone but still
  does not determine individual primary weights.

- **Level 2** (flat connection on the variation of bar cohomology over
  M_g): the KZ/Hitchin connection lives here.  Its MONODROMY carries
  representation-theoretic data.  The Chern character ch(V_{g,0})
  recovers the spectral discriminant Delta_A (rem:spectral-characteristic-programme,
  higher_genus_modular_koszul.tex line 2774).

- **Level 3** (full factorization and sewing): the chain-level modular
  functor, which includes the sewing data that produces the partition
  function and thereby epsilon^c_s.

The precise answer to the question is: **KZ/Hitchin monodromy captures
the spectral discriminant Delta_A (a polynomial invariant) but NOT the
full primary spectrum.  The full spectrum requires Level 3 (sewing),
which produces the partition function Z_A(tau) and thereby epsilon^c_s.**

## Detailed Analysis

### 1. Affine KM at Integrable Level: KZ Connection and Monodromy

The manuscript proves (thm:shadow-connection-kz, frontier_modular_holography_platonic.tex
line 2055):

For A = hat{g}_k at level k != -h^v, the genus-0 shadow connection on
n-point conformal blocks identifies with the KZ connection:

    nabla^hol_{0,n} = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij}/(z_i - z_j) dz_i = nabla^KZ

This is the arity-2 genus-0 shadow projection:
Sh_{0,2}(Theta_A) = (k+h^v)^{-1} * sum Omega_{ij} * d log(z_i - z_j).

The KZ monodromy is a representation of the braid group B_n on the space
of conformal blocks.  By the classical Kohno-Drinfeld theorem
(thm:derived-dk-affine, yangians_drinfeld_kohno.tex line 181), this
monodromy is identified with the R-matrix representation of U_q(g) at
q = exp(pi*i/(k+h^v)).

**Does this determine the spectrum {h_lambda}?**

The KZ monodromy eigenvalues on V_lambda tensor V_mu are:

    exp(2*pi*i * (h_nu - h_lambda - h_mu) / (k+h^v))

where h_lambda = <lambda, lambda+2*rho> / (2(k+h^v)) is the conformal
weight.  So the KZ monodromy eigenvalues are EXPONENTIALS of DIFFERENCES
of conformal weights divided by (k+h^v).  The individual h_lambda are
not directly visible -- only the differences h_nu - h_lambda - h_mu
modulo (k+h^v)*Z appear.

For INTEGRABLE representations (finite set of lambda), the fusion rules
determine which nu appear in lambda tensor mu, and the Verlinde formula
gives the multiplicities.  The monodromy eigenvalues then determine
h_nu - h_lambda - h_mu mod (k+h^v)*Z for all triples (lambda, mu, nu)
in the fusion ring.  This system of modular-arithmetic equations CAN in
principle be solved for {h_lambda} up to an overall additive constant
(which is fixed by h_0 = 0 for the vacuum).

**Verdict for affine KM at integrable level**: Yes, KZ monodromy
determines the primary spectrum {h_lambda} for the FINITE set of
integrable representations.  But this is a finite set; epsilon^c_s sums
over ALL primaries (including non-integrable modules), so KZ at a single
integrable level does NOT determine epsilon^c_s.

### 2. The DK Hierarchy and the Path from B(A) to the Spectrum

The DK hierarchy (constr:dk-shadow-projections, yangians_drinfeld_kohno.tex
line 112) organizes the comparison:

| DK Level | Shadow datum                    | Content                          |
|----------|---------------------------------|----------------------------------|
| DK-0     | pi_sc(Theta^E1_A), pi_{2,0}    | Chain-level Koszul duality       |
| DK-1     | pi_{2,0} on Ran_n               | Evaluation-locus factorization   |
| DK-2/3   | pi_{3,0}                        | Generated-core (CYBE, KZ assoc.) |
| DK-4     | pi_{4,0}                        | Formal moduli + quartic resonance|
| DK-5     | pi_{bullet,bullet}              | Full categorical equivalence     |

DK-0/1 and the generated-core comparison surface (traditionally DK-2/3)
are PROVED for all simple types (cor:dk23-all-types).  DK-4/5 are
conjectural.

The key structural point: r(z) = Res^coll_{0,2}(Theta_A) is the binary
genus-0 shadow of the MC element.  The KZ connection IS this shadow
acting on conformal blocks.  Higher arity shadows (pi_{r,0} for r >= 3)
encode:

- r = 3: the cubic shadow = KZ associator + CYBE + first Massey obstruction
- r = 4: the quartic resonance class

These higher projections give L-infinity corrections to the KZ system:
the shadow connection at arity r is

    nabla^{shadow}_{0,r} = d - Sh_{0,r}(Theta_A)

(see kz_shadow_connection.py line 28).

**Does the DK hierarchy provide a path from B(A) to the primary
spectrum?**

The DK hierarchy provides a path from B(A) to the REPRESENTATION THEORY
of the quantum group U_q(g).  The quantum group representation theory
encodes:

- Fusion rules (tensor product multiplicities)
- R-matrix eigenvalues (related to h_lambda via the Kazhdan-Lusztig
  equivalence)
- The modular S and T matrices (at integrable levels)

The S-matrix determines the conformal weights modulo integers (by the
Verlinde formula and the relation S = exp(2*pi*i * h) on the diagonal).
The T-matrix T_{lambda,mu} = delta_{lambda,mu} * exp(2*pi*i*(h_lambda - c/24))
directly encodes h_lambda mod Z.

So the DK hierarchy, through the KL equivalence, provides access to
h_lambda mod Z.  To determine the exact conformal weights (not just mod Z),
one needs the level k and the Casimir eigenvalue formula.  But BOTH of
these are encoded in the bar complex: k appears as the level, and the
Casimir eigenvalue formula is the binary shadow r(z) = Omega/z.

**Verdict**: The DK hierarchy does provide a homotopy-theoretic path from
B(A) to the primary spectrum -- but only for the INTEGRABLE sector at a
given level.  The full epsilon^c_s requires summing over all primaries at
all levels, which requires the sewing/partition function data (Level 3).

### 3. Virasoro: BPZ Equations as Shadow Connection

For the Virasoro algebra, there is no affine Lie algebra structure and
hence no KZ connection in the classical sense.  The manuscript proves
(prop:shadow-connection-bpz, frontier_modular_holography_platonic.tex
line 2120):

The genus-0 shadow connection on n-point blocks of Virasoro primaries
with conformal weights h_1, ..., h_n is:

    nabla^hol_{0,n} = d - sum_i (sum_{j!=i} h_j/(z_i-z_j)^2 + partial_{z_j}/(z_i-z_j)) dz_i

This is the conformal Ward identity.  The BPZ differential equations for
degenerate representations arise from the HIGHER collision residues
Res^coll_{0,k}(Theta_Vir) for k >= 3, which encode the infinite shadow
tower of class M.

The key structural difference from affine KM:

- For affine KM (class L, r_max = 3): the shadow tower terminates.  The
  KZ connection is the COMPLETE genus-0 binary data.  Higher arities
  contribute only through the CYBE (which is automatic from Arnold).

- For Virasoro (class M, r_max = infinity): the shadow tower does NOT
  terminate.  The shadow connection at arity 2 gives only the conformal
  Ward identity -- the simplest constraint.  The BPZ null-vector
  equations require higher collision residues from the FULL infinite
  tower.  The quartic contact invariant Q^contact_Vir = 10/[c(5c+22)]
  (comp:thqg-V-quartic-graviton, thqg_gravitational_yangian.tex line 1836)
  is the first obstruction to the binary r-matrix being a complete
  description.

**Does BPZ monodromy determine epsilon^c_s for Virasoro?**

The BPZ equations for degenerate representations (e.g., phi_{1,2} with
h = (5-c +/- sqrt((c-1)(c-25)))/16) are second-order ODEs whose
monodromy determines the FUSION RULES of these degenerate fields
(the BPZ selection rules: phi_{1,2} x phi_{r,s} = phi_{r,s-1} + phi_{r,s+1}).
For minimal models M(p,q), this finite set of fusion rules determines
the full primary spectrum h_{r,s} = ((p*s - q*r)^2 - (p-q)^2) / (4*p*q).

For GENERIC c (not a minimal model), the degenerate representation
phi_{1,2} is a single special module.  Its BPZ monodromy determines the
fusion coefficients with OTHER primaries, but the Virasoro has a
continuous spectrum of primaries (all h >= 0 for c >= 1) and the BPZ
monodromy of finitely many degenerate modules does not determine which
h values have nonzero multiplicity in the partition function.

**Verdict**: For minimal models: Yes, BPZ monodromy determines the
finite primary spectrum and hence epsilon^c_s (which is a finite Dirichlet
series).  For generic c: No, BPZ monodromy of degenerate modules does
not determine the full primary spectrum.

### 4. The Hitchin Connection and the Shadow Tower

The Hitchin connection on conformal blocks over M_g is the higher-genus
analogue of the KZ connection.  The manuscript describes this at
rem:moduli-variation (genus_complete.tex line 394):

The chain-level modular functor produces a sheaf V_{g,n} over M-bar_{g,n}.
Its cohomology V_{g,n} := H*(V_{g,n}) carries a flat Gauss-Manin
connection nabla^GM.  For hat{g}_k at integrable level, this flat
connection is the bar-side comparison surface for the KZ/Hitchin package.

The curvature structure:
- The FIRST CHERN CLASS of V_{g,0} recovers kappa(A) * lambda_g
  (Theorem D).
- The FULL CHERN CHARACTER ch(V_{g,0}) recovers the spectral discriminant
  Delta_A (rem:spectral-characteristic-programme).

The spectral discriminant Delta_A(x) = det(1 - x * T_{br,A}) is a
POLYNOMIAL invariant (the characteristic polynomial of the branch
operator T_{br,A}).  It encodes more than kappa but LESS than the full
primary spectrum.

Specifically, Delta_A determines the eigenvalues of the branch operator,
which are related to the conformal weights of the algebra's generators
(not of its primaries).  For example, several distinct algebras share
the same discriminant: sl_2-hat, Vir_c, and beta-gamma all have
Delta_A(x) = (1-3x)(1+x) (rem:shared-discriminant-sheet,
higher_genus_modular_koszul.tex line 2783).

**Does the shadow tower control the Hitchin connection?**

At the scalar level (kappa): the curvature of the Hitchin connection
is controlled by the Sugawara tensor, which at leading order gives
c/2 = kappa.  This is the genus-0, arity-2 shadow.

At the spectral level (Delta_A): the Chern character of the flat bundle
is controlled by the branch operator, which is a finite-arity shadow
datum.

At higher levels: the resonance classes R^mod_{r} for r >= 4 carry
information not determined by kappa and Delta alone.  These are the
shadow-tower data that distinguish algebras with the same scalar curvature.

The shadow tower provides a FILTRATION of the Hitchin connection data:
each arity truncation Theta_A^{<=r} gives a finite-order approximation.
But the full Hitchin connection (its monodromy representation of the
mapping class group) requires the COMPLETE MC element Theta_A, not just
its finite-order projections.

### 5. The Critical Structural Insight

The manuscript's Modular Chern-Weil Transform (def:modular-chern-weil-transform,
genus_complete.tex line 902) makes the hierarchy explicit:

    MC(g^amb_A) ---CW---> (scalar kappa) x (spectral Delta_A) x (resonance R^mod_r) x (line kernel r_A(z))

The four projections correspond to:
- c_1 -> kappa
- ch -> Delta_A
- Higher char. classes -> R^mod_{r>=4}
- Holonomy -> r_A(z)

The KZ/Hitchin connection lives at the HOLONOMY level (the fourth and
most refined projection).  Its monodromy is a representation of pi_1(M_{g,n})
in GL(V_{g,n}), which IS the line-kernel datum r_A(z) evaluated at the
specific representations inserted at the punctures.

So the KZ/Hitchin monodromy is one PROJECTION of Theta_A.  The constrained
Epstein zeta epsilon^c_s is a DIFFERENT projection -- it requires the
partition function Z_A(tau), which is the genus-1 sewing trace:

    Z_A(tau) = Tr_{H_A}(q^{L_0 - c/24})

This trace requires the FULL spectrum of L_0, not just its monodromy
representation.  The sewing-Rankin-Selberg bridge (sec:sewing-RS-bridge,
arithmetic_shadows.tex line 162) shows that epsilon^c_s factors through
the partition function, which in turn factors through the sewing operator
(Fredholm determinant).

### 6. Summary: Three Distinct Invariants, One MC Element

| Invariant          | Level | Input from Theta_A        | Determines spectrum? |
|--------------------|-------|---------------------------|---------------------|
| kappa(A)           | 0     | Scalar trace              | No (one number)     |
| Delta_A(x)         | 1.5   | Chern character           | No (polynomial)     |
| KZ/Hitchin monod.  | 2     | Holonomy on V_{g,n}       | Partially (mod Z)   |
| epsilon^c_s        | 3     | Sewing trace Z_A(tau)     | Yes (by definition) |

The relationship is:

    Theta_A (universal MC element)
       |
       |--- scalar trace ---> kappa ---> F_g = kappa * lambda_g (Theorem D)
       |
       |--- ch(V_g) --------> Delta_A (spectral discriminant)
       |
       |--- monodromy -------> KZ/Hitchin connection -> braid rep -> {h mod Z}
       |                       (affine: proved; Virasoro: via BPZ)
       |
       |--- sewing ----------> Z_A(tau) -> epsilon^c_s (full spectrum)

Each successive invariant requires strictly MORE data from Theta_A.

## Precise Answers to the Five Sub-Questions

**Q1**: Does KZ monodromy determine the spectrum {h_lambda} for affine KM
at integrable level?

**A1**: Yes, for the FINITE integrable sector.  The T-matrix gives
h_lambda mod Z; combined with the level k and the Casimir formula
h_lambda = <lambda, lambda+2rho>/(2(k+h^v)), the spectrum is determined.
But epsilon^c_s sums over ALL primaries, not just integrable ones.

**Q2**: Does the DK hierarchy provide a homotopy-theoretic path from B(A)
to the primary spectrum?

**A2**: DK-0/1 and the generated-core DK-2/3 (proved for all simple
types) provide a path to the quantum-group representation theory, which
encodes fusion rules and R-matrix eigenvalues.  This determines conformal
weights of integrable representations.  The full DK-5 (conjectural)
would provide the complete categorical equivalence.

**Q3**: For Virasoro, does BPZ monodromy determine epsilon^c_s?

**A3**: For minimal models M(p,q): yes.  For generic c: no.  The BPZ
equations for degenerate representations constrain but do not determine
the continuous spectrum.  The infinite shadow tower (class M, r_max = infinity)
encodes the full BPZ system, but extracting the spectrum from the
monodromy of these equations requires additional input (the partition
function itself, or equivalently the sewing data).

**Q4**: Does the shadow tower control the Hitchin connection?

**A4**: The shadow tower provides a FILTERED approximation to the Hitchin
connection data.  The scalar level gives c_1 (= kappa * lambda_g).  The
spectral level gives ch (= Delta_A).  Higher arities give resonance
classes.  But the full Hitchin connection (its monodromy) requires the
complete Theta_A, not just its finite-order projections.  The manuscript
proves that the genus-0 shadow connection EQUALS the KZ connection on the
affine comparison surface (thm:shadow-connection-kz); at higher genus,
the relationship is structural (conj:categorical-modular-kd is still
conjectural).

**Q5**: Do finite-order shadow projections determine finitely many
primary dimensions?

**A5**: Each arity-r shadow Sh_{0,r}(Theta_A) constrains the n-point
functions of primaries through r-th order differential equations.  For
CLASS G (r_max = 2, Heisenberg): the arity-2 shadow (kappa) determines
the SINGLE primary weight (h = 0 for the vacuum).  For CLASS L (r_max = 3,
affine KM): the arity-3 shadow (CYBE + KZ associator) determines the
fusion rules, constraining the finite integrable spectrum.  For CLASS C
(r_max = 4, beta-gamma): the quartic shadow determines one additional
datum.  For CLASS M (r_max = infinity, Virasoro/W_N): NO finite truncation
suffices -- the infinite tower is needed, and the primary spectrum is
continuous for generic c.

## Key References in the Manuscript

- thm:shadow-connection-kz: frontier_modular_holography_platonic.tex line 2055
- prop:shadow-connection-bpz: frontier_modular_holography_platonic.tex line 2120
- thm:derived-dk-affine: yangians_drinfeld_kohno.tex line 181
- constr:dk-shadow-projections: yangians_drinfeld_kohno.tex line 112
- rem:four-levels: concordance.tex line 4152
- rem:moduli-variation: genus_complete.tex line 394
- def:modular-chern-weil-transform: genus_complete.tex line 902
- rem:spectral-characteristic-programme: higher_genus_modular_koszul.tex line 2774
- conj:categorical-modular-kd: concordance.tex line 4832
- thm:shadow-spectral-correspondence: arithmetic_shadows.tex line 101
- kz_shadow_connection.py: compute/lib/kz_shadow_connection.py (KZ from shadow tower implementation)
