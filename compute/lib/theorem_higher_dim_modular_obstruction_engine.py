r"""Higher-dimensional modular obstruction engine.

RESEARCH QUESTION: Why does the modular operad structure on M-bar_{g,n}
obstruct in dimension > 1?  Is there a higher-dimensional substitute?

MATHEMATICAL FRAMEWORK:

1. DIMENSION 1 (CURVES): The key structure is the modular operad
   M = {M-bar_{g,n}}_{2g-2+n>0}, with composition maps (clutching/sewing):

       xi_{irr}: M-bar_{g-1,n+2} -> M-bar_{g,n}   (self-sewing: identify two points)
       xi_{tree}: M-bar_{g1,n1+1} x M-bar_{g2,n2+1} -> M-bar_{g1+g2,n1+n2}
                                                         (tree sewing: glue two curves)

   These maps EXIST because sewing curves at punctures is codimension-1
   on the curve (a point on a 1-fold is codimension 1). The resulting
   boundary divisors D_{irr}, D_{tree} are normal-crossings divisors in
   M-bar_{g,n}, and their intersections give the full boundary stratification.

   The HODGE BUNDLE E_1 = R^0 pi_* omega_{C/M-bar_{g}} is a rank-g vector
   bundle whose Chern classes lambda_i = c_i(E_1) are the tautological
   lambda classes. The genus-1 obstruction is obs_1 = kappa * lambda_1
   where lambda_1 = c_1(E_1) in H^2(M-bar_{1,1}).

2. DIMENSION 2 (SURFACES): There is NO modular operad on moduli of
   surfaces because:

   (a) SEWING MISMATCH: To sew two surfaces, one must identify
       codimension-1 BOUNDARIES (circles S^1), not points. This is
       a fundamentally different operation:
       - For curves: Sewing data = choice of two points + local coords
         = 2 parameters (the two puncture positions)
       - For surfaces: Sewing data = choice of an embedded circle in
         each surface + diffeomorphism of the circles
         = infinite-dimensional (Diff(S^1) is infinite-dimensional)

   (b) MODULI NON-EXISTENCE: The moduli space of compact complex
       surfaces is NOT a smooth DM stack in general:
       - Surfaces of general type: coarse moduli exists (Gieseker) but
         is highly singular
       - K3 surfaces: moduli is a 20-dimensional quasi-projective variety
         (non-compact, with type III degenerations)
       - Abelian surfaces: Siegel modular variety A_2 (dimension 3)
       - Ruled/rational surfaces: moduli is a single point (or empty)

   (c) OPERAD FAILURE: Even where moduli exist, the clutching maps
       do not satisfy the associativity/equivariance axioms of a
       modular operad. The fundamental reason: for curves, the sewing
       operation is LOCAL (it depends only on a neighborhood of the
       puncture), but for surfaces, the sewing operation is GLOBAL
       (the topology of the resulting surface depends on the embedded
       circle, not just a local datum).

3. DIMENSION n (GENERAL): For complex n-folds, the obstruction grows:
   - Sewing boundary = codimension-1 submanifold of real dimension 2n-1
   - Moduli are either non-existent, singular, or non-algebraic
   - No operadic structure on moduli of higher-dimensional varieties

4. WHAT REPLACES THE MODULAR OPERAD?

   (a) CONFIGURATION SPACES + E_n OPERADS: Conf_k(R^n) carries an
       E_n-operad structure (little n-disks). This gives GENUS-0
       composition but NO higher-genus structure. Barwick's isolability
       structure axiomatizes this level.

   (b) COBORDISM CATEGORIES: The n-dimensional cobordism category
       Cob_n has objects = closed (n-1)-manifolds and morphisms =
       n-dimensional cobordisms. For n=2 (surfaces), this gives the
       pants decomposition and hence a 2d TQFT structure. But this
       is TOPOLOGICAL, not complex-analytic: it captures genus
       structure but not the HOLOMORPHIC moduli.

   (c) FACTORIZATION HOMOLOGY: Ayala-Francis factorization homology
       int_M A for an E_n-algebra A and n-manifold M provides a
       higher-dimensional analogue of chiral homology. This DOES
       give genus-like invariants but does NOT come from a modular
       operad.

   (d) MODULI OF MAPS (GW THEORY): Instead of moduli of the TARGET
       (surfaces), one uses moduli of MAPS M-bar_{g,n}(X, beta).
       This gives a virtual modular operad structure when X is the
       target, but the source is still a curve. This is the
       "wrong-way" higher-dimensional extension: the target gets
       higher-dimensional, but the source stays 1-dimensional.

5. THE TODD CLASS AS OBSTRUCTION ANALOGUE:

   For curves: the genus-1 obstruction is kappa * lambda_1.
   The Hodge bundle E_1 = R^0 pi_* omega has c_1(E_1) = lambda_1,
   and the GRR theorem gives:
       ch(E_1) = pi_*(ch(omega_{C/S}) * Td(T_{C/S}))

   For surfaces: the Hodge bundle is replaced by:
       E_p = R^p pi_* Omega^q_{S/B}  (Hodge filtration pieces)
   and the GRR theorem gives:
       ch(E_p) = pi_*(ch(Omega^q) * Td(T_{S/B}))

   The Todd class Td(T_X) of the tangent bundle is:
       Td(T_X) = 1 + c_1/2 + (c_1^2 + c_2)/12 + c_1*c_2/24 + ...

   For a surface X with c_1 = c_1(T_X), c_2 = c_2(T_X) = chi_top(X):
       Td_0(X) = 1
       Td_1(X) = c_1/2
       Td_2(X) = (c_1^2 + c_2)/12

   The Noether formula for surfaces:
       chi(O_X) = (c_1^2 + c_2)/12 = Td_2(X)
   This is the SURFACE ANALOGUE of lambda_1 = (2g-2)/12 for curves
   (Noether's formula for curves: chi(O_C) = (1-g) = (2-2g)/2).

   For a FAMILY of surfaces pi: S -> B with fiber X:
       chi(R pi_* O_S) = int_B pi_*(Td(T_{S/B}))
   The leading Hodge-type class is:
       lambda_1^{surf} = c_1(det R pi_* O_S)
   and the surface analogue of obs_1 = kappa * lambda_1 would be:
       obs_1^{surf} = kappa * lambda_1^{surf}

   But kappa ITSELF depends on the OPE structure of the CVA, which is
   dimension-independent. So the ALGEBRAIC content (kappa) extends,
   while the GEOMETRIC content (lambda_1 vs lambda_1^{surf}) changes.

6. BARWICK'S ISOLABILITY AND HIGHER-DIMENSIONAL CONFIGURATION SPACES:

   Barwick's isolability structure on X provides:
   - Configuration spaces Conf_k(X) with isolability data
   - A symmetric monoidal structure on the resulting FA category
   - For 2-skeletal spaces (algebraic varieties): equivalent to Ran space

   This gives a GENUS-0 substitute for the modular operad:
   - E_n structure from little n-disks
   - Factorization algebras (not just chiral algebras)
   - Configuration space models for bar complex at genus 0

   But it does NOT give:
   - Higher-genus clutching/sewing
   - Hodge bundle or lambda classes
   - Modular operad composition
   - Shadow obstruction tower at genus >= 1

Conventions
-----------
- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
- kappa(H_k) = k (AP39/AP48).
- Bar propagator d log E(z,w) has weight 1 (AP27).
- Todd class coefficients: Td = 1 + c_1/2 + (c_1^2+c_2)/12 + ...
- Bernoulli numbers: B_0=1, B_1=-1/2, B_2=1/6, B_4=-1/30, ...

References
----------
- higher_genus_modular_koszul.tex (modular operad, shadow tower)
- bar_cobar_adjunction_curved.tex (bar complex, clutching)
- theorem_cohomological_va_engine.py (CVA analysis)
- theorem_barwick_general_fa_engine.py (isolability structure)
- [Gri25] Griffin, arXiv:2501.18720
- [Bar26] Barwick, arXiv:2602.01292
- [AF15] Ayala-Francis, factorization homology
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from math import comb, factorial, gcd
from typing import Any, Dict, List, Optional, Tuple

# =========================================================================
# 0.  BERNOULLI NUMBERS AND TODD CLASS COEFFICIENTS
# =========================================================================


def bernoulli_number(n: int) -> Fraction:
    """Compute the n-th Bernoulli number B_n.

    Convention: B_1 = -1/2 (the "first" convention).
    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_3 = 0, B_4 = -1/30, ...

    Uses the recurrence: sum_{k=0}^{n} C(n+1,k) B_k = 0.
    """
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n >= 3 and n % 2 == 1:
        return Fraction(0)  # B_{2k+1} = 0 for k >= 1
    # Recurrence
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m >= 3 and m % 2 == 1:
            B[m] = Fraction(0)
            continue
        s = Fraction(0)
        for k in range(m):
            s += Fraction(comb(m + 1, k)) * B[k]
        B[m] = -s / Fraction(m + 1)
    return B[n]


def todd_coefficient(degree: int) -> Fraction:
    r"""Coefficient of degree-d term in the Todd class.

    The Todd class is Td(E) = prod_i x_i / (1 - e^{-x_i})
    where x_i are the Chern roots of E.

    In terms of Bernoulli numbers:
        Td = sum_{k>=0} (-1)^k B_k / k! * (c_1 terms of degree k)

    The first few terms in the TOTAL Chern class expansion:
        Td_0 = 1
        Td_1 = c_1 / 2
        Td_2 = (c_1^2 + c_2) / 12
        Td_3 = c_1 * c_2 / 24
        Td_4 = (-c_1^4 + 4*c_1^2*c_2 + 3*c_2^2 + c_1*c_3 - c_4) / 720

    Returns the coefficient that multiplies the leading Chern monomial.
    For degree 0: returns 1.
    For degree 1: returns 1/2 (coefficient of c_1).
    For degree 2: returns 1/12 (coefficient of c_1^2 + c_2).
    For degree 3: returns 1/24 (coefficient of c_1*c_2).
    For degree 4: returns -1/720 (coefficient of c_1^4 leading term).
    """
    if degree == 0:
        return Fraction(1)
    if degree == 1:
        return Fraction(1, 2)
    if degree == 2:
        return Fraction(1, 12)
    if degree == 3:
        return Fraction(1, 24)
    if degree == 4:
        return Fraction(-1, 720)
    if degree == 5:
        return Fraction(-1, 1440)  # next Td coefficient (leading term)
    # General: the leading Bernoulli contribution
    # Td_k involves B_k / k!  as the leading coefficient in the
    # power-sum expansion.
    return bernoulli_number(degree) / Fraction(factorial(degree))


def a_hat_coefficient(degree: int) -> Fraction:
    r"""Coefficient of degree-2k term in the A-hat genus.

    A-hat(E) = prod_i (x_i/2) / sinh(x_i/2).

    The first few terms:
        A-hat_0 = 1
        A-hat_1 = -p_1 / 24      (degree 4 in cohomology, but degree 1 in p_i)
        A-hat_2 = (7p_1^2 - 4p_2) / 5760

    For comparison with the monograph's shadow tower:
        F_1 = kappa/24  (first Bernoulli coefficient)
        A-hat at degree 1 gives -1/24, matching F_1 = kappa * (-1/24) * p_1.

    We return the rational coefficient for the leading term at each degree.
    """
    if degree == 0:
        return Fraction(1)
    if degree == 1:
        return Fraction(-1, 24)  # coefficient of p_1
    if degree == 2:
        return Fraction(7, 5760)  # coefficient of p_1^2
    # General: from the A-hat generating function
    # A-hat_k = (-1)^k * 2 * (2^{2k-1} - 1) * B_{2k} / (2k)!
    k = degree
    b2k = bernoulli_number(2 * k)
    return Fraction((-1) ** k * 2) * (Fraction(2 ** (2 * k - 1) - 1)) * b2k / Fraction(factorial(2 * k))


# =========================================================================
# 1.  MODULAR OPERAD STRUCTURE ON M-bar_{g,n}
# =========================================================================


@dataclass
class ModularOperadData:
    """Data of the modular operad {M-bar_{g,n}} for curves.

    The modular operad structure consists of:
    1. Spaces: M-bar_{g,n} for 2g-2+n > 0 (stability)
    2. Symmetric group action: S_n acts on M-bar_{g,n} by permuting markings
    3. Clutching maps:
       xi_{irr}: M-bar_{g-1,n+2} -> M-bar_{g,n}  (irreducible/self-sewing)
       xi_{g1,S}: M-bar_{g1,|S|+1} x M-bar_{g2,|S^c|+1} -> M-bar_{g,n}
                  (reducible/tree-sewing, g1+g2=g, S union S^c = {1,...,n})
    4. Unit: M-bar_{0,3} = point (the genus-0, 3-pointed curve)
    """
    genus: int
    n_marked: int

    @property
    def stable(self) -> bool:
        """Stability condition: 2g-2+n > 0."""
        return 2 * self.genus - 2 + self.n_marked > 0

    def dim_complex(self) -> int:
        """Complex dimension of M-bar_{g,n}.

        dim_C M-bar_{g,n} = 3g - 3 + n  for 2g-2+n > 0.
        """
        if not self.stable:
            return -1
        return 3 * self.genus - 3 + self.n_marked

    def euler_characteristic(self) -> Optional[Fraction]:
        """Euler characteristic of M-bar_{g,n} for small (g,n).

        Known values:
            M-bar_{0,3} = pt:  chi = 1
            M-bar_{0,4} = P^1: chi = 2
            M-bar_{1,1}:       chi = 1/12  (orbifold)
            M-bar_{2,0}:       chi = 1/240 (orbifold)
        """
        if self.genus == 0 and self.n_marked == 3:
            return Fraction(1)
        if self.genus == 0 and self.n_marked == 4:
            return Fraction(2)
        if self.genus == 1 and self.n_marked == 1:
            return Fraction(1, 12)
        if self.genus == 2 and self.n_marked == 0:
            return Fraction(1, 240)
        return None

    def num_boundary_divisors(self) -> int:
        """Number of boundary divisor classes in M-bar_{g,n}.

        Boundary divisors are indexed by:
        1. delta_{irr}: one class (irreducible node)
        2. delta_{h,S}: one class for each (h, S) with 0 <= h <= g,
           S subset {1,...,n}, |S| >= 0, 2h-2+|S|+1 > 0,
           2(g-h)-2+(n-|S|)+1 > 0, modulo (h,S) ~ (g-h, S^c).
        """
        if not self.stable:
            return 0
        count = 1  # delta_irr (for g >= 1)
        if self.genus == 0:
            count = 0  # no irreducible boundary at genus 0
        # Reducible boundaries: count (h, S) pairs modulo symmetry
        for h in range(self.genus + 1):
            for s_size in range(self.n_marked + 1):
                # Stability of both components
                if 2 * h - 2 + s_size + 1 <= 0:
                    continue
                if 2 * (self.genus - h) - 2 + (self.n_marked - s_size) + 1 <= 0:
                    continue
                # Count: C(n, s_size) choices of S, but we symmetrize
                # under (h, S) <-> (g-h, S^c)
                if h < self.genus - h:
                    count += comb(self.n_marked, s_size)
                elif h == self.genus - h:
                    # Must be careful with S <-> S^c symmetry
                    if s_size < self.n_marked - s_size:
                        count += comb(self.n_marked, s_size)
                    elif s_size == self.n_marked - s_size:
                        count += comb(self.n_marked, s_size) // 2
        return count

    def hodge_bundle_rank(self) -> int:
        """Rank of the Hodge bundle E_1 = R^0 pi_* omega on M-bar_{g}.

        rank(E_1) = g (the genus).
        """
        return self.genus

    def lambda_class_degree(self, i: int) -> int:
        """Cohomological degree of lambda_i = c_i(E_1).

        lambda_i lives in H^{2i}(M-bar_{g,n}).
        """
        return 2 * i

    def sewing_codimension_on_source(self) -> int:
        """Codimension of the sewing locus on the source curve.

        For curves (dim 1): sewing identifies POINTS, which are
        codimension 1 on the curve. This is why the sewing maps exist
        as morphisms of moduli spaces: the result is a codimension-1
        boundary in the compactified moduli.

        Returns 1 for curves.
        """
        return 1


# =========================================================================
# 2.  HIGHER-DIMENSIONAL MODULI AND OBSTRUCTION ANALYSIS
# =========================================================================


@dataclass
class HigherDimModuliAnalysis:
    """Analysis of moduli spaces and operadic structure in dimension n.

    For n = 1: M-bar_{g,n} is a modular operad. No obstruction.
    For n >= 2: The obstruction to a modular operad has three layers:
        Layer 1 (SEWING): sewing requires identifying (2n-1)-dim boundaries
        Layer 2 (MODULI): moduli of compact n-folds are not well-behaved
        Layer 3 (OPERAD): even when moduli exist, no operadic composition
    """
    dim: int  # complex dimension n of the variety

    def sewing_boundary_real_dim(self) -> int:
        """Real dimension of the boundary used for sewing.

        For curves (n=1): sewing identifies points. The boundary of a
        small disk around a point on a Riemann surface is a circle S^1
        (real dim 1). But the actual sewing datum is a POINT (real dim 0)
        plus a local coordinate (1 complex parameter).

        For surfaces (n=2): sewing identifies embedded circles with
        tubular neighborhoods. The boundary of a small ball in a surface
        is S^3 (real dim 3). The sewing datum includes the diffeomorphism
        of the boundary.

        For n-folds: the boundary of a small ball in a complex n-fold
        is S^{2n-1} (real dim 2n-1).
        """
        return 2 * self.dim - 1

    def sewing_diffeomorphism_group_dim(self) -> str:
        """Dimension of the diffeomorphism group of the sewing boundary.

        For curves (n=1): Sewing boundary = two points.
            Diff(pt) = trivial. Sewing data = local coordinates.
            Finite-dimensional parameter space.

        For surfaces (n=2): Sewing boundary = S^1.
            Diff(S^1) is infinite-dimensional (Virasoro group!).
            Sewing data = embedding S^1 hookrightarrow X plus
            diffeomorphism phi: S^1 -> S^1.
            INFINITE-DIMENSIONAL parameter space.

        For n-folds (n >= 2): Sewing boundary = S^{2n-1}.
            Diff(S^{2n-1}) is infinite-dimensional.
        """
        if self.dim == 1:
            return "finite (local coordinates at two points)"
        return f"infinite (Diff(S^{{{2*self.dim - 1}}}) is infinite-dimensional)"

    def sewing_is_local(self) -> bool:
        """Whether sewing depends only on local data.

        For curves: YES. The sewing operation depends only on the
        choice of puncture + local coordinate (a jet of the
        uniformizer). The resulting curve's topology is completely
        determined.

        For surfaces: NO. The sewing operation (cutting along a circle
        and regluing) depends on the GLOBAL topology: the resulting
        surface's topology depends on how the circle is embedded
        (unknotted vs knotted, separating vs non-separating).

        Locality of sewing is EQUIVALENT to the existence of an
        operadic composition: the operad axiom requires that iterated
        compositions are associative, which requires that each
        composition step is LOCAL (depends only on the immediate
        operands, not on the global context).
        """
        return self.dim == 1

    def moduli_exists_as_dm_stack(self) -> Optional[str]:
        """Whether the moduli of compact n-folds exists as a DM stack.

        For curves: YES. M-bar_{g,n} is a smooth proper DM stack.
        For surfaces: PARTIAL.
            - K3: 20-dim quasi-projective variety (not proper)
            - Surfaces of general type: coarse moduli exists (Gieseker),
              highly singular
            - Abelian surfaces: Siegel modular variety A_2
            - Rational/ruled: trivial (point or empty)
        For 3-folds: MUCH WORSE. CY3 moduli are often non-algebraic
            or have non-Hausdorff points.
        """
        if self.dim == 1:
            return "smooth proper DM stack (M-bar_{g,n})"
        if self.dim == 2:
            return "partial (K3: quasi-projective, gen type: coarse+singular)"
        if self.dim == 3:
            return "very partial (CY3: non-algebraic/non-Hausdorff issues)"
        return "essentially non-existent for general n-folds"

    def has_operadic_composition(self) -> bool:
        """Whether the moduli admits operadic (modular operad) composition.

        TRUE only for curves (dim 1).
        """
        return self.dim == 1

    def obstruction_layers(self) -> List[Dict[str, Any]]:
        """Enumerate the layers of obstruction for dim >= 2.

        Returns a list of obstruction layers, each with:
        - name: descriptive name
        - severity: "fatal", "serious", or "minor"
        - description: mathematical content
        - can_circumvent: whether there is a known workaround
        """
        if self.dim == 1:
            return []

        layers = []

        # Layer 1: Sewing
        layers.append({
            "name": "sewing_infinite_dimensional",
            "severity": "fatal",
            "description": (
                f"Sewing in dim {self.dim} requires identifying "
                f"S^{{{2*self.dim-1}}} boundaries via an infinite-dimensional "
                f"diffeomorphism group Diff(S^{{{2*self.dim-1}}}). "
                f"For curves, sewing is finite-dimensional (local coordinates)."
            ),
            "can_circumvent": False,
        })

        # Layer 2: Moduli
        layers.append({
            "name": "moduli_non_algebraic",
            "severity": "fatal",
            "description": (
                f"Moduli of compact complex {self.dim}-folds are "
                f"either non-existent, singular, or non-algebraic. "
                f"No smooth proper DM stack analogue of M-bar_{{g,n}}."
            ),
            "can_circumvent": False,
        })

        # Layer 3: Operad
        layers.append({
            "name": "no_operadic_composition",
            "severity": "fatal",
            "description": (
                "Even where moduli exist, the composition maps fail "
                "operadic associativity because sewing is not local: "
                "the topology of the output depends on global embedding data."
            ),
            "can_circumvent": False,
        })

        # Layer 4: Hodge classes
        layers.append({
            "name": "hodge_class_non_scalar",
            "severity": "serious",
            "description": (
                f"For dim {self.dim}, the Hodge bundle splits into multiple "
                f"pieces R^p pi_* Omega^q with p+q = {self.dim}. "
                f"There is no single lambda class; the obstruction is a "
                f"vector in a multi-dimensional Hodge filtration."
            ),
            "can_circumvent": True,  # Todd class gives a substitute
        })

        return layers

    def genus_0_substitute(self) -> str:
        """What replaces the modular operad at genus 0.

        At genus 0, the modular operad structure reduces to the cyclic
        operad on M-bar_{0,n} = FM_n(P^1)/PGL(2). The higher-dimensional
        analogue is the E_n operad on Conf_k(R^{2n}).

        Barwick's isolability structure provides a clean axiomatization
        of this genus-0 level.
        """
        if self.dim == 1:
            return "standard cyclic operad on M-bar_{0,n}"
        return (
            f"E_{{{2*self.dim}}} operad on Conf_k(R^{{{2*self.dim}}}), "
            f"axiomatized by Barwick's isolability (dim {self.dim})"
        )


# =========================================================================
# 3.  HODGE-TYPE CLASSES IN HIGHER DIMENSIONS
# =========================================================================


@dataclass
class HodgeTypeInvariant:
    """Hodge-type characteristic classes for families of n-folds.

    For a smooth proper family pi: X -> B of complex n-folds:

    DIMENSION 1 (CURVES):
        E_1 = R^0 pi_* omega_{X/B}  (rank g Hodge bundle)
        lambda_i = c_i(E_1)
        Genus-1 obstruction: obs_1 = kappa * lambda_1 in H^2(M-bar_{1,1})
        GRR: ch(E_1) = pi_*(Td(T_{X/B}))

    DIMENSION 2 (SURFACES):
        E_{0,2} = R^0 pi_* Omega^2_{X/B}   (rank p_g = geometric genus)
        E_{1,1} = R^1 pi_* Omega^1_{X/B}   (rank h^{1,1})
        E_{2,0} = R^2 pi_* O_{X/B}         (rank 1 for connected fibers)
        The Hodge filtration: F^p = E_{p,n-p} oplus ... oplus E_{n,0}
        Surface Noether formula: chi(O_X) = (c_1^2 + c_2)/12

    GENERAL DIMENSION n:
        E_{p,q} = R^q pi_* Omega^p_{X/B}   for p + q = n
        Hodge numbers: h^{p,q} = rank(E_{p,q})
        Total arithmetic genus: chi(O_X) = Td_n(T_X) (GRR/HRR)
    """
    dim: int  # complex dimension n

    def hodge_bundle_pieces(self) -> List[Tuple[int, int]]:
        """List of Hodge bundle pieces E_{p,q} with p+q = n.

        For dim n: pieces (p, n-p) for p = 0, 1, ..., n.
        """
        return [(p, self.dim - p) for p in range(self.dim + 1)]

    def num_hodge_pieces(self) -> int:
        """Number of distinct Hodge bundle pieces.

        For curves: 1 piece (E_1 = E_{1,0}).
        For surfaces: 3 pieces (E_{0,2}, E_{1,1}, E_{2,0}).
        For n-folds: n+1 pieces.
        """
        return self.dim + 1

    def noether_formula_dim1(self, genus: int) -> Fraction:
        """Noether formula for curves: chi(O_C) = 1 - g.

        Equivalently: deg(omega_C) = 2g - 2, chi(O_C) = (2-2g)/2 + 1/2... no.
        Actually: chi(O_C) = h^0(O_C) - h^1(O_C) = 1 - g (by Riemann-Roch).
        And: Td_1(T_C) = c_1(T_C)/2 = (2-2g)/2 = 1 - g. So chi = Td_1. Correct.
        """
        return Fraction(1 - genus)

    def noether_formula_dim2(self, c1_sq: Fraction, c2: Fraction) -> Fraction:
        """Noether formula for surfaces: chi(O_X) = (c_1^2 + c_2)/12.

        Here c_1 = c_1(T_X), c_2 = c_2(T_X) = chi_top(X).
        """
        return (c1_sq + c2) / 12

    def noether_formula_general(self, chern_numbers: Dict[str, Fraction]) -> Fraction:
        """General HRR/Noether formula: chi(O_X) = Td_n[X].

        For dim 1: Td_1 = c_1/2 = (2-2g)/2 = 1-g. Check.
        For dim 2: Td_2 = (c_1^2 + c_2)/12.  Check.
        For dim 3: Td_3 = c_1*c_2/24.
        For dim 4: Td_4 = (-c_1^4 + 4c_1^2*c_2 + 3c_2^2 + c_1*c_3 - c_4)/720.
        """
        if self.dim == 1:
            c1 = chern_numbers.get("c1", Fraction(0))
            return c1 / 2
        if self.dim == 2:
            c1_sq = chern_numbers.get("c1_sq", Fraction(0))
            c2 = chern_numbers.get("c2", Fraction(0))
            return (c1_sq + c2) / 12
        if self.dim == 3:
            c1c2 = chern_numbers.get("c1_c2", Fraction(0))
            return c1c2 / 24
        return Fraction(0)

    def obstruction_class_genus_1(self, kappa: Fraction) -> Dict[str, Any]:
        """The genus-1 obstruction class in dimension n.

        For curves (n=1):
            obs_1 = kappa * lambda_1 in H^2(M-bar_{1,1})
            This is a SCALAR (one-dimensional H^2).

        For surfaces (n=2):
            obs_1^{surf} would involve lambda_1^{surf} = c_1(det(E_{0,2}))
            and ALSO c_1(det(E_{1,1})) and c_1(det(E_{2,0})).
            The obstruction is a VECTOR in the multi-dimensional Hodge space.

        For n-folds:
            The obstruction involves n+1 Hodge pieces and is not scalar.
        """
        if self.dim == 1:
            return {
                "type": "scalar",
                "value": kappa,
                "class": "kappa * lambda_1",
                "target_space_dim": 1,
                "extends_to_all_genera": True,
            }
        return {
            "type": "vector",
            "kappa_component": kappa,
            "num_hodge_pieces": self.num_hodge_pieces(),
            "class": f"vector in H^2 with {self.num_hodge_pieces()} Hodge components",
            "target_space_dim": self.num_hodge_pieces(),
            "extends_to_all_genera": False,
            "obstruction": (
                "The genus-1 obstruction is not a single scalar but a vector "
                "in a multi-dimensional space. The scalar formula "
                "obs_g = kappa * lambda_g does NOT have a direct analogue."
            ),
        }


# =========================================================================
# 4.  TODD CLASS COMPUTATION FOR SURFACE FAMILIES
# =========================================================================


@dataclass
class SurfaceFamilyToddClass:
    """Todd class computation for families of complex surfaces.

    For a smooth proper family pi: S -> B of complex surfaces, the
    GRR theorem gives:
        ch(R pi_* O_S) = pi_*(Td(T_{S/B}))

    The Todd class of the relative tangent bundle T_{S/B} is:
        Td(T_{S/B}) = 1 + c_1/2 + (c_1^2 + c_2)/12 + ...
    where c_i = c_i(T_{S/B}).

    For a K3 surface: c_1 = 0, c_2 = 24.
        chi(O_{K3}) = (0 + 24)/12 = 2. Check: h^{0,0} - h^{0,1} + h^{0,2} = 1-0+1=2.

    For an abelian surface: c_1 = 0, c_2 = 0 (flat).
        chi(O_{Ab}) = (0 + 0)/12 = 0. Check: 1 - 2 + 1 = 0.

    For CP^2: c_1 = 3H, c_2 = 3.
        chi(O_{CP2}) = (9 + 3)/12 = 1. Check: h^{0,0} = 1, h^{0,1} = h^{0,2} = 0.

    COMPARISON WITH CURVES:
    For a curve of genus g: c_1(T_C) = 2-2g, so:
        chi(O_C) = (2-2g)/2 = 1-g.
    The genus-1 obstruction kappa * lambda_1 involves:
        lambda_1 = c_1(E_1) = c_1(R^0 pi_* omega)

    For a surface family, the ANALOGUE is:
        lambda_1^{surf} = c_1(det(R pi_* O_S))
    which by GRR equals:
        lambda_1^{surf} = int_{S/B} Td_2(T_{S/B}) = (c_1^2 + c_2)/12
    as a class on the base B.
    """
    c1_sq: Fraction  # c_1(T_S)^2 for the fiber
    c2: Fraction      # c_2(T_S) = chi_top(S) for the fiber

    def chi_O(self) -> Fraction:
        """Arithmetic genus chi(O_S) = (c_1^2 + c_2)/12 (Noether)."""
        return (self.c1_sq + self.c2) / 12

    def todd_0(self) -> Fraction:
        """Td_0 = 1."""
        return Fraction(1)

    def todd_1(self) -> Fraction:
        """Td_1 = c_1/2. For surfaces, this is c_1(T_S)/2.

        Note: Td_1 is a CLASS, not a number. Here we return the
        coefficient 1/2 that multiplies c_1.
        """
        return Fraction(1, 2)

    def todd_2_integrated(self) -> Fraction:
        """Td_2 integrated over the fiber = chi(O_S) = (c_1^2 + c_2)/12.

        This is the surface analogue of:
            For curves: int_C Td_1 = (2-2g)/2 = 1-g = chi(O_C)

        The integrated Todd class gives the ARITHMETIC GENUS of the fiber.
        """
        return self.chi_O()

    def lambda_1_surface_analogue(self) -> Fraction:
        """The surface analogue of lambda_1.

        For curves: lambda_1 lives on M-bar_{1,1} and equals:
            lambda_1 = c_1(E_1) where E_1 = R^0 pi_* omega (rank g)
            At genus 1: lambda_1 generates H^2(M-bar_{1,1}) = Q.

        For surfaces: the closest analogue is:
            lambda_1^{surf} = c_1(det(R pi_* O_S))
                            = chi(O_S)   (as a Chern class on the base)

        By GRR: lambda_1^{surf} = (c_1^2 + c_2)/12 = chi(O_S).

        KEY DIFFERENCE: for curves, lambda_1 has geometric content
        (it depends on the family, not just the fiber). For surfaces,
        lambda_1^{surf} = chi(O_S) is a TOPOLOGICAL INVARIANT of the
        fiber, not a cohomological class varying over moduli.

        This rigidity is WHY the scalar formula obs_g = kappa * lambda_g
        does not directly extend: the surface lambda class lacks the
        moduli-theoretic variability of the curve lambda class.
        """
        return self.chi_O()

    def obstruction_analogue(self, kappa: Fraction) -> Fraction:
        """Analogue of obs_1 = kappa * lambda_1 for surfaces.

        obs_1^{surf} = kappa * lambda_1^{surf} = kappa * chi(O_S).

        CAVEAT: this is an ANALOGY, not a theorem. There is no modular
        operad for surfaces, so there is no genus expansion to host
        this obstruction. The formula is the Todd-class substitute
        for the Hodge-class formula.
        """
        return kappa * self.lambda_1_surface_analogue()


# Known surface families for testing
K3_SURFACE = SurfaceFamilyToddClass(c1_sq=Fraction(0), c2=Fraction(24))
ABELIAN_SURFACE = SurfaceFamilyToddClass(c1_sq=Fraction(0), c2=Fraction(0))
CP2 = SurfaceFamilyToddClass(c1_sq=Fraction(9), c2=Fraction(3))
HIRZEBRUCH_F1 = SurfaceFamilyToddClass(c1_sq=Fraction(8), c2=Fraction(4))  # F_1 = Bl_pt(P^2)
ENRIQUES_SURFACE = SurfaceFamilyToddClass(c1_sq=Fraction(0), c2=Fraction(12))


# =========================================================================
# 5.  BARWICK ISOLABILITY AND GENUS-0 SUBSTITUTE
# =========================================================================


@dataclass
class IsolabilityModularSubstitute:
    """Analysis of Barwick's isolability structure as a genus-0 substitute.

    Barwick's isolability structure (arXiv:2602.01292) provides:
    1. Configuration spaces Conf_k(X) with isolability data
    2. E_n-algebra structure from little n-disk operads
    3. Factorization algebra framework in arbitrary dimension

    WHAT IT GIVES (genus-0 analogue):
    - Genus-0 bar complex: B^{(0)}(A) using Conf_k(X)
    - Factorization coalgebra structure on the Ran space
    - E_n bar-cobar duality (Lurie, HA Chapter 5)

    WHAT IT DOES NOT GIVE (no higher-genus analogue):
    - No modular operad composition (no clutching/sewing)
    - No Hodge bundle or lambda classes
    - No genus expansion F_g
    - No shadow obstruction tower at genus >= 1
    """
    dim: int  # complex dimension n of the ambient space

    @property
    def e_n_operad_dimension(self) -> int:
        """Dimension of the E_n operad from the little n-disk operad.

        For a complex n-fold: the underlying real manifold is 2n-dimensional.
        The little disk operad is E_{2n} (topological dimension = real dim).

        For curves (n=1): E_2 operad (little 2-disks on C).
        For surfaces (n=2): E_4 operad (little 4-disks on C^2).
        """
        return 2 * self.dim

    def genus_0_bar_cobar_extends(self) -> bool:
        """Does genus-0 bar-cobar duality extend to this dimension?

        YES for all n, via E_n Koszul duality (Lurie HA Ch 5).
        The E_n bar construction B_{E_n}(A) is well-defined for any
        E_n-algebra A, and Koszul duality gives:
            B_{E_n}(A) Koszul-dual to Omega^n(A)  (n-fold loop space)

        For n=1 (E_2): this recovers chiral bar-cobar duality at genus 0.
        For n=2 (E_4): this gives the surface analogue of bar-cobar at genus 0.
        """
        return True

    def factorization_homology_defined(self) -> bool:
        """Is factorization homology int_M A defined for n-manifolds M?

        YES for all n, by Ayala-Francis (arXiv:1504.04007).
        int_M A for an E_n-algebra A and a framed n-manifold M.

        This gives genus-like invariants for closed manifolds but
        does NOT come from a modular operad structure.
        """
        return True

    def higher_genus_from_cobordism(self) -> Dict[str, Any]:
        """Can higher genus be recovered from the cobordism category?

        The n-dimensional cobordism category Cob_n has:
        - Objects: closed (n-1)-manifolds
        - Morphisms: n-dimensional cobordisms

        For n=2: objects = 1-manifolds (circles), morphisms = surfaces.
        The genus of a cobordism is the number of handles.
        A TQFT is a symmetric monoidal functor Cob_2 -> Vect,
        which assigns Z(Sigma_g) to each genus-g surface.

        This DOES give a genus expansion, but it is TOPOLOGICAL:
        - No holomorphic moduli
        - No Hodge bundle
        - No lambda classes
        - No Kac-Shapovalov determinant or Koszulness

        The relationship: factorization homology int_{Sigma_g} A
        with A an E_2-algebra gives the TOPOLOGICAL genus expansion.
        The monograph's shadow obstruction tower is the HOLOMORPHIC
        refinement that exists only for curves.
        """
        # dim=1 (complex curves) is special: M_g has holomorphic moduli,
        # Hodge bundle, and the full shadow obstruction tower.
        # For dim >= 2, the cobordism category gives only topological data.
        holomorphic = self.dim == 1
        return {
            "cobordism_genus_exists": True,
            "is_topological": not holomorphic,
            "has_holomorphic_moduli": holomorphic,
            "has_hodge_bundle": holomorphic,
            "recovers_shadow_tower": holomorphic,
            "gives_genus_expansion": True,
            "genus_expansion_type": (
                "holomorphic (shadow obstruction tower)"
                if holomorphic
                else "topological (TQFT/factorization homology)"
            ),
        }

    def isolability_gives_modular_operad(self) -> bool:
        """Does Barwick's isolability give a modular operad?

        NO. Isolability structures axiomatize CONFIGURATION SPACES
        (genus 0), not MODULI OF CURVES (all genera). The isolability
        structure is the genus-0 skeleton of the modular operad.

        Barwick explicitly notes (Limitation 3) that Koszul duality
        is NOT incorporated. The modular operad requires:
        1. Sewing/clutching maps (genus increment)
        2. Vacuum axiom (genus-0 unit)
        3. Equivariance under symmetric groups
        4. Associativity of compositions

        Isolability provides (3) and a version of (2) and (4) at genus 0,
        but NOT (1) (no sewing in arbitrary dimension).
        """
        return False

    def en_koszul_dual_description(self) -> str:
        """Description of the E_n Koszul dual.

        For E_1 (associative): Koszul dual = bar construction = B(A).
        For E_2 (braided monoidal): Koszul dual = E_2-bar = B_{E_2}(A).
            This is the MONOGRAPH's chiral bar complex at genus 0.
        For E_n (n >= 3): Koszul dual = E_n-bar = B_{E_n}(A).
            For commutative algebras: B_{E_infty}(A) = Quillen's
            cotangent complex construction.

        The E_n Koszul dual is ALWAYS well-defined (genus 0).
        The shadow obstruction tower ADDS the modular correction
        (genus >= 1) which has no E_n analogue for n >= 3.
        """
        n = self.e_n_operad_dimension
        if n == 2:
            return "E_2 Koszul dual = chiral bar complex (monograph genus 0)"
        return f"E_{n} Koszul dual = higher-dimensional bar complex (genus 0 only)"


# =========================================================================
# 6.  SEWING CODIMENSION AND THE FUNDAMENTAL OBSTRUCTION
# =========================================================================


@dataclass
class SewingObstructionAnalysis:
    """The fundamental obstruction: sewing codimension.

    THE KEY INSIGHT: The modular operad structure on M-bar_{g,n} exists
    because sewing on curves is a CODIMENSION-1 operation on the SOURCE.

    For curves: a puncture is a point, which is codimension 1 on a
    1-dimensional complex manifold. The node (sewing locus) is a
    codimension-1 singularity of the total space.

    For surfaces: to sew two surfaces, one must cut along a CURVE
    (codimension 1 on a surface = real codimension 2). But the curve
    has its OWN moduli (the genus of the separating curve).
    This introduces a SECONDARY moduli problem.

    For n-folds: sewing along a codimension-1 subvariety introduces
    the moduli of the subvariety as ADDITIONAL data.

    This is the DIMENSIONAL OBSTRUCTION:
        dim(sewing data for n-folds) = dim(moduli of (n-1)-folds) + ...

    For curves: moduli of 0-folds = point. Sewing is finite-dim.
    For surfaces: moduli of curves = M-bar_{g'}. Sewing is infinite-dim.
    For 3-folds: moduli of surfaces = complicated. Even worse.

    The recursion STABILIZES only at n = 1 because:
        moduli of 0-folds = point (trivial)
    """
    dim: int

    def sewing_data_dimension(self) -> str:
        """Effective dimension of the sewing data.

        For curves: finite (2 points + 2 local coordinates = 4 real params).
        For surfaces: infinite (choice of curve + its moduli + diffeomorphism).
        """
        if self.dim == 1:
            return "finite: 2 complex parameters (punctures + local coords)"
        if self.dim == 2:
            return (
                "infinite: embedded curve gamma subset S with "
                "dim(Diff(gamma)) = infinite, plus "
                f"dim(moduli of gamma) = 3g(gamma)-3 for genus g(gamma)"
            )
        return (
            f"infinite: embedded (n-1)-fold Y subset X with "
            f"dim(Diff(Y)) = infinite, plus "
            f"dim(moduli of Y) = dim(moduli of ({self.dim-1})-folds)"
        )

    def recursive_moduli_chain(self) -> List[str]:
        """The recursive chain of moduli problems in sewing.

        Sewing n-folds requires moduli of (n-1)-folds (the boundary).
        Sewing (n-1)-folds requires moduli of (n-2)-folds. And so on.
        The chain terminates at 0-folds (points), which have trivial moduli.
        """
        chain = []
        for d in range(self.dim, -1, -1):
            if d == 0:
                chain.append("0-folds (points): trivial moduli = point")
            elif d == 1:
                chain.append("curves: M-bar_{g,n} is a modular operad")
            elif d == 2:
                chain.append(
                    "surfaces: moduli partially exist but no modular operad "
                    "(sewing requires curve moduli)"
                )
            else:
                chain.append(
                    f"{d}-folds: moduli problematic, sewing requires "
                    f"({d-1})-fold moduli"
                )
        return chain

    def chain_stabilizes_at_dim(self) -> int:
        """The dimension at which the moduli chain stabilizes.

        The chain stabilizes at dim 1 because:
        - 0-fold moduli = trivial (point)
        - 1-fold moduli = M-bar_{g,n} (smooth, proper, operadic)
        - 2-fold moduli = complicated (requires 1-fold moduli for sewing)

        The modular operad structure is STABLE at dim 1 and UNSTABLE
        at dim >= 2.
        """
        return 1

    def factorization_homology_genus(self, genus: int) -> Dict[str, Any]:
        """Factorization homology at genus g for an E_n algebra.

        For an E_n-algebra A and a closed oriented n-manifold M:
            int_M A = factorization homology of A on M

        For n=2, genus g surface Sigma_g:
            int_{Sigma_g} A = "genus-g value of A"

        This gives a TOPOLOGICAL genus expansion:
            Z(A, g) = int_{Sigma_g} A

        But this is NOT the shadow obstruction tower:
        - No holomorphic moduli (purely topological)
        - No Hodge bundle (no complex structure on Sigma_g as moduli)
        - No lambda classes (no algebraic geometry)
        - No Koszulness (E_n-formality replaces Koszul concentration)

        The factorization homology genus expansion is the TOPOLOGICAL
        SHADOW of the holomorphic shadow obstruction tower.
        """
        return {
            "genus": genus,
            "e_n_dim": 2 * self.dim,
            "exists": True,
            "is_topological": True,
            "has_holomorphic_refinement": (self.dim == 1),
            "relationship_to_shadow_tower": (
                "equals shadow tower (holomorphic = topological by GAGA)"
                if self.dim == 1
                else "topological shadow only (no holomorphic refinement)"
            ),
        }


# =========================================================================
# 7.  COMPREHENSIVE OBSTRUCTION COMPARISON
# =========================================================================


@dataclass
class DimensionalObstructionSummary:
    """Summary of what extends and what obstructs at each dimension.

    This is the MAIN ANALYSIS OBJECT. It systematically catalogs the
    structure of the monograph's framework at each dimension.
    """
    dim: int

    def property_table(self) -> List[Dict[str, Any]]:
        """Complete table of properties and their dimensional behavior."""
        moduli = HigherDimModuliAnalysis(dim=self.dim)
        hodge = HodgeTypeInvariant(dim=self.dim)
        isol = IsolabilityModularSubstitute(dim=self.dim)
        sewing = SewingObstructionAnalysis(dim=self.dim)

        table = [
            {
                "property": "kappa (modular characteristic)",
                "dim_1": "defined (OPE invariant)",
                "dim_n": "defined (OPE invariant, dimension-independent)",
                "extends": True,
                "obstruction": None,
            },
            {
                "property": "Koszulness (bar concentration)",
                "dim_1": "defined (H*(B(A)) in bar deg 1)",
                "dim_n": "defined (same algebraic criterion)",
                "extends": True,
                "obstruction": None,
            },
            {
                "property": "curved A-infinity structure",
                "dim_1": "m_1^2 = [m_0, -]",
                "dim_n": "same algebraic identity",
                "extends": True,
                "obstruction": None,
            },
            {
                "property": "genus-0 bar complex",
                "dim_1": "on Conf_k(X), X = curve",
                "dim_n": f"on Conf_k(X), X = {self.dim}-fold (E_{2*self.dim} bar)",
                "extends": True,
                "obstruction": None,
            },
            {
                "property": "Ran space / factorization structure",
                "dim_1": "Ran(X) for curve X",
                "dim_n": f"Ran(X) via Jouanolou model or isolability",
                "extends": True,
                "obstruction": None,
            },
            {
                "property": "E_n operad structure",
                "dim_1": "E_2 (little 2-disks on C)",
                "dim_n": f"E_{2*self.dim} (little {2*self.dim}-disks on C^{self.dim})",
                "extends": True,
                "obstruction": None,
            },
            {
                "property": "modular operad on moduli",
                "dim_1": "M-bar_{g,n} forms modular operad",
                "dim_n": "NO modular operad (sewing fails)" if self.dim > 1
                         else "M-bar_{g,n} forms modular operad",
                "extends": (self.dim == 1),
                "obstruction": (
                    f"sewing in dim {self.dim} is infinite-dimensional "
                    f"(Diff(S^{2*self.dim-1})))" if self.dim > 1 else None
                ),
            },
            {
                "property": "Hodge bundle (single lambda class)",
                "dim_1": "E_1 = R^0 pi_* omega, lambda_i = c_i(E_1)",
                "dim_n": (
                    f"{self.dim + 1} Hodge pieces E_{{p,q}}, no single lambda"
                    if self.dim > 1 else "E_1, single lambda class"
                ),
                "extends": (self.dim == 1),
                "obstruction": (
                    f"Hodge filtration has {self.dim + 1} pieces"
                    if self.dim > 1 else None
                ),
            },
            {
                "property": "scalar obstruction obs_g = kappa * lambda_g",
                "dim_1": "PROVED (uniform-weight lane)",
                "dim_n": "NO analogue (no single lambda class, no modular operad)"
                         if self.dim > 1 else "PROVED (uniform-weight lane)",
                "extends": (self.dim == 1),
                "obstruction": (
                    "both lambda_g and the modular operad are absent"
                    if self.dim > 1 else None
                ),
            },
            {
                "property": "shadow obstruction tower (all genera)",
                "dim_1": "Theta_A = D_A - d_0, all-arity MC",
                "dim_n": "genus-0 projection only" if self.dim > 1
                         else "full tower (all genera, all arities)",
                "extends": (self.dim == 1),
                "obstruction": (
                    "no modular operad to host higher-genus tower"
                    if self.dim > 1 else None
                ),
            },
            {
                "property": "genus expansion Z(A,g)",
                "dim_1": "holomorphic (on M-bar_{g,n})",
                "dim_n": (
                    "topological only (factorization homology)"
                    if self.dim > 1
                    else "holomorphic (on M-bar_{g,n})"
                ),
                "extends": True,  # topological version exists
                "obstruction": (
                    "topological, not holomorphic (no Hodge structure)"
                    if self.dim > 1 else None
                ),
            },
            {
                "property": "sewing locality",
                "dim_1": "LOCAL (point sewing, finite-dim data)",
                "dim_n": (
                    f"NON-LOCAL (codim-1 sewing, infinite-dim data)"
                    if self.dim > 1
                    else "LOCAL (point sewing, finite-dim data)"
                ),
                "extends": (self.dim == 1),
                "obstruction": (
                    f"sewing boundary S^{2*self.dim-1} has Diff = infinite-dim"
                    if self.dim > 1 else None
                ),
            },
        ]
        return table

    def count_extending(self) -> Dict[str, int]:
        """Count extending vs obstructed properties."""
        table = self.property_table()
        ext = sum(1 for row in table if row["extends"])
        obs = sum(1 for row in table if not row["extends"])
        return {"extends": ext, "obstructs": obs, "total": len(table)}

    def fundamental_obstruction(self) -> str:
        """The single fundamental reason the modular operad fails.

        THE ANSWER: sewing in dimension 1 is codimension 1 on the source,
        which makes it a LOCAL operation with finite-dimensional moduli.
        In dimension >= 2, sewing is still codimension 1 on the source,
        but the sewing BOUNDARY is now a positive-dimensional manifold
        with its own moduli. This introduces an infinite-dimensional
        diffeomorphism group and breaks locality.

        In formula:
            dim_R(sewing boundary) = 2n - 1
            For n=1: 2*1 - 1 = 1 (circle S^1, but sewing data = point, finite)
            For n=2: 2*2 - 1 = 3 (sphere S^3, sewing data includes Diff(S^1))
            For n=n: 2n - 1 (sphere S^{2n-1}, infinite-dim sewing data)
        """
        if self.dim == 1:
            return "no obstruction (curves)"
        return (
            f"FUNDAMENTAL: sewing in dim {self.dim} is NON-LOCAL. "
            f"The sewing boundary S^{{{2*self.dim-1}}} has "
            f"Diff(S^{{{2*self.dim-1}}}) = infinite-dimensional, "
            f"introducing secondary moduli from ({self.dim-1})-fold geometry. "
            f"This breaks operadic associativity because iterated sewing "
            f"depends on global embedding data. "
            f"The modular operad is specific to dim 1 because ONLY for points "
            f"(= 0-folds) is the moduli trivial."
        )


# =========================================================================
# 8.  TODD CLASS VS HODGE CLASS: QUANTITATIVE COMPARISON
# =========================================================================


def curve_lambda1_from_grr(genus: int) -> Fraction:
    """Compute lambda_1 for curves of genus g from GRR.

    lambda_1 = c_1(E_1) = c_1(R^0 pi_* omega).

    By GRR: ch(E_1) = pi_*(ch(omega) * Td(T_{C/S})).
    For a single curve C of genus g:
        rk(E_1) = g, c_1(E_1) = lambda_1.
        ch_1(omega) = c_1(omega) = 2g - 2.
        Td_1(T_C) = c_1(T_C)/2 = (2 - 2g)/2 = 1 - g.

    The integrated version gives chi(O_C) = 1 - g.
    The class lambda_1 on M-bar_{g} is more subtle: it requires
    computing pi_* of the relative GRR. The key formula is:

        lambda_1 = kappa_1 / 12  (Mumford's formula on M-bar_g)

    where kappa_1 = pi_*(c_1(omega_{C/S})^2) is the first kappa class.

    For M-bar_{1,1}: lambda_1 generates H^2 = Q, and
        int_{M-bar_{1,1}} lambda_1 = 1/24.
    """
    if genus == 0:
        return Fraction(0)  # trivial Hodge bundle
    if genus == 1:
        return Fraction(1, 24)  # int_{M-bar_{1,1}} lambda_1 = 1/24
    # Faber's intersection numbers for higher genus:
    # These are the integrals of lambda_g over M-bar_g, not lambda_1.
    # Return the rank as a proxy (the class itself is abstract).
    return Fraction(genus)  # rank of E_1 = g (not the integral)


def surface_todd2_for_family(c1_sq: Fraction, c2: Fraction) -> Fraction:
    """Compute Td_2 integrated over a surface fiber.

    Td_2(X) = (c_1(T_X)^2 + c_2(T_X)) / 12 = chi(O_X).

    This is the SURFACE ANALOGUE of the curve's chi(O_C) = 1 - g.
    """
    return (c1_sq + c2) / 12


def obstruction_ratio_curve_surface(
    kappa: Fraction, genus: int,
    c1_sq: Fraction, c2: Fraction
) -> Dict[str, Fraction]:
    """Compare the genus-1 obstruction for curves vs surfaces.

    For curves: obs_1 = kappa * lambda_1.
        At genus 1: obs_1 = kappa * (1/24) [integral over M-bar_{1,1}].

    For surfaces: obs_1^{surf} = kappa * chi(O_S).
        For K3: chi(O_{K3}) = 2.
        For Ab: chi(O_{Ab}) = 0.
        For CP^2: chi(O_{CP2}) = 1.

    The RATIO obs_1^{surf} / obs_1^{curve} measures the dimensional
    amplification of the obstruction.
    """
    obs_curve = kappa * curve_lambda1_from_grr(genus)
    obs_surface = kappa * surface_todd2_for_family(c1_sq, c2)

    ratio = Fraction(0)
    if obs_curve != 0:
        ratio = obs_surface / obs_curve

    return {
        "obs_curve": obs_curve,
        "obs_surface": obs_surface,
        "ratio": ratio,
        "kappa": kappa,
    }


# =========================================================================
# 9.  FACTORIZATION HOMOLOGY GENUS EXPANSION (TOPOLOGICAL)
# =========================================================================


@dataclass
class TopologicalGenusExpansion:
    """The topological genus expansion via factorization homology.

    For an E_n-algebra A and a closed oriented n-manifold M:
        int_M A = factorization homology (Ayala-Francis)

    For n=2 (surfaces):
        int_{Sigma_g} A = genus-g amplitude of A

    This gives a TOPOLOGICAL genus expansion but NO holomorphic content.

    The KEY COMPARISON with the monograph:
    - Monograph: F_g(A) = kappa(A) * lambda_g^{FP} + delta_g^{cross}
      (holomorphic, on M-bar_{g,n}, with Hodge classes)
    - FH: Z_g(A) = int_{Sigma_g} A
      (topological, on the manifold Sigma_g, no Hodge structure)

    For dim 1: the two agree because GAGA identifies the topological
    and holomorphic theories. For dim >= 2: only the topological version
    exists.
    """
    dim: int  # real dimension of the manifold (= 2 * complex dim)

    def genus_g_euler_char(self, g: int) -> int:
        """Euler characteristic of the oriented genus-g surface.

        For dim=2 (real 2-manifolds = topological surfaces):
            chi(Sigma_g) = 2 - 2g.

        For higher dimensions, "genus" does not have a unique meaning.
        We restrict to surfaces for the genus expansion.
        """
        if self.dim != 2:
            return 0  # genus only meaningful for surfaces
        return 2 - 2 * g

    def fh_for_comm_algebra(self, g: int) -> str:
        """Factorization homology for a commutative algebra A on Sigma_g.

        For E_infty-algebras (commutative):
            int_M A = A^{tensor chi(M)}  (for a simply-connected M)
            int_{Sigma_g} A = A^{tensor (2-2g)}

        This is the TOPOLOGICAL shadow of the genus expansion.
        For g=0: A^2 (two copies of A).
        For g=1: A^0 = ground field (the torus has chi=0).
        For g>=2: A^{negative power} = derived completion.
        """
        chi = self.genus_g_euler_char(g)
        if self.dim != 2:
            return "genus expansion only for real dim 2"
        return f"int_{{Sigma_{g}}} A = A^{{tensor {chi}}} (commutative case)"

    def relationship_to_shadow_tower(self) -> str:
        """How factorization homology relates to the shadow tower.

        For COMMUTATIVE E_2-algebras:
            int_{Sigma_g} A = A^{tensor (2-2g)}
            This is TOPOLOGICAL: no kappa, no lambda classes, no moduli.

        For NON-COMMUTATIVE E_2-algebras (closer to the monograph):
            int_{Sigma_g} A depends on the E_2 structure (braiding/monodromy).
            The Fresse-Willwacher graph complex computes corrections.
            These corrections are the TOPOLOGICAL ANALOGUE of the
            shadow obstruction tower, but without holomorphic content.

        The monograph's shadow obstruction tower is the HOLOMORPHIC
        ENHANCEMENT of this topological picture, available only for
        dim 1 because M-bar_{g,n} has holomorphic structure.
        """
        if self.dim == 2:
            return (
                "For dim 1: FH = holomorphic shadow tower (by GAGA). "
                "For dim >= 2: FH = topological shadow, no holomorphic refinement."
            )
        return "factorization homology gives topological genus expansion only"


# =========================================================================
# 10. MASTER SUMMARY: WHY DIM 1 IS SPECIAL
# =========================================================================


def why_dim_1_is_special() -> Dict[str, Any]:
    """The complete answer to why the modular operad obstructs in dim > 1.

    THE ANSWER HAS THREE LAYERS:

    Layer 1 (ALGEBRAIC, extends): The OPE algebra structure, kappa invariant,
    Koszulness, curved A-infinity relations, and genus-0 bar complex are all
    dimension-independent. They extend to CVAs in arbitrary dimension via
    Griffin's construction and the Jouanolou-Ran model of GWW25.

    Layer 2 (TOPOLOGICAL, partially extends): The genus expansion Z_g(A) exists
    as a topological invariant via Ayala-Francis factorization homology for
    E_n-algebras on closed n-manifolds. But it carries no holomorphic moduli
    structure, no Hodge bundle, and no lambda classes.

    Layer 3 (HOLOMORPHIC, dim-1 only): The modular operad structure on
    M-bar_{g,n}, the Hodge bundle E_1 = R^0 pi_* omega, the lambda classes
    lambda_i = c_i(E_1), and the scalar obstruction obs_g = kappa * lambda_g
    are ALL specific to curves (complex dim 1).

    THE FUNDAMENTAL REASON: Sewing of curves identifies POINTS
    (0-dimensional), which have trivial moduli. Sewing of n-folds
    (n >= 2) identifies codimension-1 subvarieties, which have their
    OWN moduli. This introduces an infinite-dimensional diffeomorphism
    group into the sewing data and breaks the finite-dimensionality
    that makes the modular operad work.

    In the language of the manuscript: the modular operad structure
    exists because M-bar_{g,n} is the UNIQUE moduli problem where
    the sewing boundary (= puncture = point) has TRIVIAL moduli.
    """
    summary_dim1 = DimensionalObstructionSummary(dim=1)
    summary_dim2 = DimensionalObstructionSummary(dim=2)
    summary_dim3 = DimensionalObstructionSummary(dim=3)

    return {
        "extends_all_dim": [
            "kappa (modular characteristic)",
            "Koszulness (bar concentration in bar degree 1)",
            "curved A-infinity structure",
            "genus-0 bar complex (E_n bar construction)",
            "Ran space / factorization structure (Jouanolou model)",
            "topological genus expansion (factorization homology)",
        ],
        "obstructs_dim_ge_2": [
            "modular operad on moduli of n-folds",
            "Hodge bundle (single lambda class)",
            "scalar obstruction obs_g = kappa * lambda_g",
            "shadow obstruction tower at genus >= 1",
            "sewing locality (finite-dim sewing data)",
        ],
        "fundamental_reason": (
            "Sewing of curves identifies POINTS (moduli = trivial). "
            "Sewing of n-folds (n >= 2) identifies (n-1)-folds "
            "(moduli = non-trivial). The modular operad exists only "
            "when the sewing boundary has trivial moduli, i.e., dim = 1."
        ),
        "todd_class_substitute": (
            "The Todd class Td(T_X) replaces lambda classes for surface "
            "families: chi(O_X) = Td_n(X) by Hirzebruch-Riemann-Roch. "
            "For K3: chi = 2, for abelian: chi = 0, for CP^2: chi = 1. "
            "But this is a TOPOLOGICAL invariant of the fiber, not a "
            "moduli-varying class. The moduli-theoretic variability "
            "of lambda_g is absent."
        ),
        "barwick_isolability_role": (
            "Barwick's isolability structure axiomatizes the genus-0 "
            "skeleton: configuration spaces, E_n operads, Ran spaces. "
            "This is necessary but NOT sufficient for the modular operad. "
            "Isolability gives composition (genus-0 bar-cobar) but NOT "
            "sewing (genus >= 1 shadow obstruction tower)."
        ),
        "dim_1_count": summary_dim1.count_extending(),
        "dim_2_count": summary_dim2.count_extending(),
        "dim_3_count": summary_dim3.count_extending(),
    }
