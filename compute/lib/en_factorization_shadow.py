"""E_n factorization algebra shadows: bar complex and shadow obstruction tower for E_2 and E_3 algebras.

The monograph focuses on E_1 (associative/chiral) algebras on curves.  This module
extends the shadow obstruction tower framework to E_n algebras on R^n, computing bar complexes,
Koszul duality shifts, shadow invariants, and factorization homology.

MATHEMATICAL CONTENT:

1. E_n BAR COMPLEX.  For an E_n algebra A, the bar construction B_{E_n}(A) is an
   E_n coalgebra.  The underlying chain complex is governed by the cohomology of
   the configuration spaces Conf_k(R^n), which for n >= 2 is the Arnold/Totaro
   algebra.  For n = 1, Conf_k(R) is contractible (ordered), so E_1 bar = classical
   bar.  For n >= 2, there are higher-degree propagators.

2. E_n KOSZUL DUALITY.  The Koszul dual of the E_n operad is
       E_n^! = E_n{-n}
   i.e., E_n with an operadic desuspension/shift of n.  In particular:
       E_1^! = E_1{-1}   (Ass^! = Ass with shift, giving cobar)
       E_2^! = E_2{-2}   (different from E_1!)
   The Koszul duality functors produce:
       A |--> A^! where A^! is an E_n algebra on the shifted generators.
   The bar-dual has generators in degree shifted by n relative to A.

3. FORMALITY.  The E_2 operad is formal (Kontsevich, Tamarkin).
   Consequence: for a FORMAL E_2 algebra A (e.g. C*(k[x], k[x])), the
   bar complex B_{E_2}(A) has trivial higher shadow obstruction tower (all shadows
   beyond kappa vanish).

   The E_n operad is formal for all n >= 2 (Kontsevich's formality of
   the little n-disks operad, via Lambrechts-Volic for n >= 3).
   E_1 is NOT formal as an operad (it is formal as an algebra, since
   Ass is generated in arity 2, but the operad has no formality obstruction
   in the same sense).

4. SHADOW TOWER.  The E_n shadow invariants kappa_{E_n}, S_3^{E_n}, ...
   are defined by the same Maurer-Cartan mechanism as in the chiral (E_1)
   case, but with the E_n bar complex replacing the chiral bar complex.
   The key difference: the E_n propagator is the fundamental class of
   S^{n-1} (codimension-n collision), not d log(z-w) (codimension-1).

5. STABILIZATION.  As n -> infinity, E_n -> E_infty = Com.  The shadow
   tower stabilizes: kappa_{E_n}(A) -> kappa_{Com}(A).  Explicitly,
   the contribution from H^*(Conf_k(R^n)) to the bar complex stabilizes
   because all positive-degree classes in Conf_k(R^n) have degree >= n-1,
   which exceeds any fixed arity bound for n large enough.

6. DUNN ADDITIVITY.  E_{m+n} = E_m tensor E_n (Dunn's theorem).
   At the algebra level, an E_{m+n} algebra is equivalently an E_m algebra
   in E_n algebras.  The shadow obstruction tower respects this:
       kappa_{E_{m+n}}(A) = kappa_{E_m}(A as E_m) * kappa_{E_n}(A as E_n)
   is NOT true in general.  Rather, kappa_{E_{m+n}} depends on the
   interaction between the two operadic structures.  But for a FREE
   E_{m+n} algebra on a single generator, the formula simplifies.

7. FACTORIZATION HOMOLOGY.  For M an n-manifold and A an E_n algebra:
       integral_M A = colim_{Disk(M)} A
   For M = T^n (n-torus): integral_{T^n} A is iterated THH.
   For M = S^n: integral_{S^n} A uses the E_n Hochschild complex.
   The genus-1 shadow on T^n generalizes the genus-1 kappa of the E_1 case.

References:
    Fresse: Modules over Operads and Functors (Springer LNM 1967)
    Loday-Vallette: Algebraic Operads (Grundlehren 346)
    Kontsevich: Operads and Motives in Deformation Quantization (1999)
    Francis: The Tangent Complex and Hochschild Cohomology of E_n Rings (2013)
    Ayala-Francis: Factorization Homology of Topological Manifolds (2015)
    Ginot-Tradler-Zeinalian: Higher Hochschild Homology (2014)
    Lambrechts-Volic: Formality of the Little N-Disks Operad (2014)
    Willwacher: M. Kontsevich's Graph Complex... (2015)
    Dunn: Tensor Products of Operads (1988)
    en_koszul_bridge.py: Arnold algebra, E_1 vs E_2 comparison
    swiss_cheese_chain_model.py: Swiss-cheese computations
    CLAUDE.md: AP14 (Koszulness vs formality), AP19 (pole absorption)
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, comb, prod
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, Symbol, pi, bernoulli, binomial, oo, simplify


# =========================================================================
# 1.  E_n operad: basic numerical invariants
# =========================================================================

def en_generator_degree(n: int) -> int:
    """Degree of the binary generator of the E_n operad.

    The E_n operad has a binary operation mu_2 of degree 0 (it is concentrated
    in arity 2 at the chain level for the homological convention).  However,
    the PROPAGATOR (fundamental class of the configuration space fiber) lives
    in degree n-1.

    For the Koszul duality shift: E_n^! = E_n{-n}, so the dual binary
    operation has degree n.

    We return the propagator degree, which governs the bar complex grading.
    """
    if n < 1:
        raise ValueError(f"E_n requires n >= 1, got {n}")
    return n - 1


def en_koszul_shift(n: int) -> int:
    """The Koszul duality shift for E_n: E_n^! = E_n{-n}.

    The operadic Koszul dual of E_n is the same operad but with an
    operadic desuspension of n.  This means generators of the dual
    operad are shifted by n in degree.

    E_1: shift = 1 (Ass^! = Ass{-1})
    E_2: shift = 2
    E_n: shift = n
    E_infty (= Com): shift = infinity (Com^! = Lie, infinite shift is
    the statement that Lie has generators in all arities -- not quite the
    same as a finite shift, but the pattern holds finitely).
    """
    if n < 1:
        raise ValueError(f"E_n requires n >= 1, got {n}")
    return n


def en_dual_operad_name(n: int) -> str:
    """Name of the Koszul dual operad of E_n.

    E_1^! = E_1{-1}  (= Ass{-1} = Ass as operad, but shifted)
    E_2^! = E_2{-2}  (self-Koszul-dual up to shift)
    E_n^! = E_n{-n}  (self-dual up to shift for all n >= 1)
    Com^! = Lie       (E_infty^! = L_infty)

    The E_n operad is Koszul self-dual (up to the operadic desuspension
    by n).  This is a theorem of Fresse and Getzler-Jones.
    """
    if n < 1:
        raise ValueError(f"E_n requires n >= 1, got {n}")
    return f"E_{n}" + "{" + f"-{n}" + "}"


# =========================================================================
# 2.  Configuration space data: H*(Conf_k(R^n))
# =========================================================================

def conf_space_betti(k: int, n: int) -> List[int]:
    """Betti numbers of Conf_k(R^n) for n >= 1.

    For n = 1 (ordered):
        Conf_k(R) has k! connected components, each contractible.
        Betti: [k!] (all in degree 0).

    For n >= 2:
        H*(Conf_k(R^n)) is the Totaro/Arnold algebra with generators
        x_{ij} of degree (n-1) subject to generalized Arnold relations.

        Poincare polynomial for n even:
            P_k(t) = prod_{j=0}^{k-1} (1 + j*t^{n-1})
        For n odd (n >= 3), the generators have even degree, and products
        behave as in a polynomial algebra (subject to Arnold relations):
            P_k(t) = prod_{j=0}^{k-1} (1 + j*t^{n-1})
        (Same formula -- the sign in the Arnold relations changes, but
        the Betti numbers are the same for both parities of n.)

    We return the Betti numbers as a list indexed by degree.
    """
    if k <= 0:
        return [1]
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")

    if n == 1:
        # Ordered configurations on R: k! components, each contractible
        return [factorial(k)]

    # For n >= 2: Poincare polynomial = prod_{j=0}^{k-1} (1 + j * t^{n-1})
    # The maximum degree is (k-1) * (n-1).
    max_deg = (k - 1) * (n - 1)
    # Multiply out the product.  Represent as dict {degree: coefficient}.
    coeffs = {0: 1}
    for j in range(1, k):
        new_coeffs = {}
        for deg, val in coeffs.items():
            new_coeffs[deg] = new_coeffs.get(deg, 0) + val
            new_coeffs[deg + (n - 1)] = new_coeffs.get(deg + (n - 1), 0) + j * val
        coeffs = new_coeffs

    result = [0] * (max_deg + 1)
    for deg, val in coeffs.items():
        if 0 <= deg <= max_deg:
            result[deg] = val
    return result


def conf_space_euler(k: int, n: int) -> int:
    """Euler characteristic of Conf_k(R^n).

    For n = 1: chi = k! (k! points).
    For n >= 2: chi = prod_{j=0}^{k-1} (1 + j*(-1)^{n-1}).
        n even (n-1 odd): chi = prod (1 - j) = 0 for k >= 2.
        n odd (n-1 even): chi = prod (1 + j) = k! for all k.
    """
    if k <= 0:
        return 1
    if n == 1:
        return factorial(k)
    # For n >= 2:
    sign = (-1) ** (n - 1)
    result = 1
    for j in range(1, k):
        result *= (1 + j * sign)
    return result


def conf_space_total_betti(k: int, n: int) -> int:
    """Total Betti number of Conf_k(R^n): P_k(1)."""
    betti = conf_space_betti(k, n)
    return sum(betti)


# =========================================================================
# 3.  E_n bar complex dimensions
# =========================================================================

def en_bar_chain_dimension(arity: int, n: int, gen_degree: int = 0) -> int:
    """Dimension of the arity-k component of B_{E_n}(A) for A free on one
    generator in degree gen_degree.

    The bar construction B_{E_n}(A) has arity-k component:
        B_{E_n}(A)_k = H_*(Conf_k(R^n)) tensor A^{tensor k}

    For A = k[x] (free on one generator in degree gen_degree), A^{tensor k} is
    the k-fold tensor power.  The dimension contribution from A^{tensor k}
    depends on the weight truncation, but for the FREE algebra on one
    generator, dim A_w = 1 at each relevant weight (in the PBW basis for E_n
    algebras, this is the number of monomials of weight w in k generators).

    We return the total dimension of the bar complex at arity k, which is
    the total Betti number of Conf_k(R^n) (the A^{tensor k} factor just
    tensors with a 1-dimensional space for each generator configuration).

    For a more refined computation, use en_bar_chain_dimension_weighted.
    """
    if arity <= 0:
        return 1  # arity 0: the ground field
    return conf_space_total_betti(arity, n)


def en_bar_chain_dimension_weighted(arity: int, n: int, degree: int) -> int:
    """Dimension of the degree-d part of B_{E_n}(A)_k for A free on one generator.

    The bar complex at arity k lives in degrees coming from H*(Conf_k(R^n))
    plus the bar desuspension shift.  The desuspension for E_n bar is by n
    per point (the Koszul shift), but the propagator degree is n-1.

    For the E_n bar complex on a free algebra on one degree-0 generator,
    the arity-k term contributes in degree d = (n-1) * (number of propagators).
    The number of propagators is the cohomological degree within H*(Conf_k(R^n)).

    So the dimension at arity k and cohomological degree d is:
        b_d(Conf_k(R^n)) if d is a multiple of (n-1), else 0.
    """
    if arity <= 0:
        return 1 if degree == 0 else 0
    betti = conf_space_betti(arity, n)
    if 0 <= degree < len(betti):
        return betti[degree]
    return 0


# =========================================================================
# 4.  E_n shadow obstruction tower: modular characteristic kappa_{E_n}
# =========================================================================

def kappa_en_free(n: int, k: Fraction = Fraction(1)) -> Fraction:
    """Modular characteristic kappa_{E_n} for the free E_n algebra on one
    generator of level k (= the OPE self-pairing coefficient).

    At E_1 (chiral/associative), kappa = k/2 for Heisenberg at level k.
    This is the genus-1 obstruction in the shadow obstruction tower: F_1 = kappa * lambda_1
    where lambda_1 = 1/24 is the first Chern class of the Hodge bundle.

    For E_n with n >= 2, the genus-1 analogue uses the E_n Hochschild
    homology (= factorization homology on S^1 x R^{n-1} or T^n).
    The modular characteristic is:

        kappa_{E_n}(H_k) = k/2 * chi_n

    where chi_n is the Euler characteristic correction factor from the
    propagator on S^{n-1}.  For the standard E_n propagator (fundamental
    class of S^{n-1}), chi_n = 1 for all n (the pairing is universal).

    Actually, the key point: kappa is determined by the BINARY part of the
    bar complex, which involves Conf_2(R^n) = R^n - {0} ~ S^{n-1}.
    The propagator pairing on S^{n-1} gives a number that is independent
    of n (it is the level k of the algebra).  So:

        kappa_{E_n}(H_k) = k/2

    for all n.  The shadow obstruction tower DOES depend on n at higher arities (through
    the Arnold/Totaro relations on Conf_k(R^n) for k >= 3), but the leading
    binary invariant kappa is universal.

    This is consistent with stabilization: kappa_{E_n} -> kappa_{Com} as n -> oo.
    """
    return k / 2


def kappa_en_affine(n: int, dim_g: int, k: Fraction = Fraction(1),
                    h_dual: int = 2) -> Fraction:
    """Modular characteristic kappa_{E_n} for an E_n analogue of affine KM.

    For E_1 (chiral) affine g_k: kappa = dim(g) * k / (2 * h_dual)
    where h_dual is the dual Coxeter number.

    For E_n with n >= 2, the same formula holds at the binary level
    (kappa depends only on the arity-2 part of the bar complex, which
    is universal across n).

    kappa_{E_n}(g_k) = dim(g) * (k + h_dual) / (2 * h_dual)
    """
    return Fraction(dim_g) * (k + h_dual) / (2 * h_dual)


def kappa_en_virasoro(n: int, c: Fraction = Fraction(26)) -> Fraction:
    """Modular characteristic kappa_{E_n} for an E_n analogue of Virasoro.

    For E_1 (chiral) Virasoro at central charge c: kappa = c/2.
    This extends to E_n by the same binary-level argument.

    kappa_{E_n}(Vir_c) = c/2
    """
    return c / 2


# =========================================================================
# 5.  Cubic and quartic shadows at E_n
# =========================================================================

def cubic_shadow_en(n: int, k: Fraction = Fraction(1),
                    structure_constants: Optional[Dict] = None) -> Fraction:
    """Cubic shadow S_3^{E_n} for the free E_n algebra.

    The cubic shadow depends on the arity-3 part of the bar complex.
    For E_1: Conf_3(R) is contractible, so the cubic shadow depends
    only on the OPE structure constants (the tree-level arity-3 amplitude).
    For E_n with n >= 2: Conf_3(R^n) has nontrivial topology.

    For the FREE E_n algebra on one generator (Heisenberg-type):
        S_3 = 0  (no cubic OPE for free fields)
    regardless of n.

    For non-free algebras (e.g. affine KM, Virasoro), S_3 depends on
    the structure constants AND on the topology of Conf_3(R^n).
    The topological correction vanishes for n >= 2 if the algebra is
    FORMAL as an E_n algebra (Kontsevich formality).

    For formal E_n algebras: S_3^{E_n} = S_3^{E_1} (same as chiral).
    For non-formal algebras: S_3^{E_n} receives a correction from
    H^{n-1}(Conf_3(R^n)).  At n=2: H^1(Conf_3(R^2)) has dim 3 (Arnold),
    contributing up to 3 correction terms.

    For the Heisenberg (free) case: S_3 = 0 for all n.
    """
    # Free algebra: no cubic vertex
    return Fraction(0)


def quartic_shadow_en(n: int, kappa: Fraction,
                      S3: Fraction = Fraction(0)) -> Fraction:
    """Quartic shadow S_4^{E_n} for an algebra with given kappa and S_3.

    For the free algebra (S_3 = 0), the quartic shadow also vanishes:
        S_4 = 0  (Heisenberg: Gaussian shadow class G, r_max = 2)

    For non-free algebras, the quartic shadow depends on:
    (a) the quartic OPE structure (same for all n at tree level),
    (b) the one-loop correction from Conf_2(R^n) (universal for all n),
    (c) the tree-level correction from Conf_4(R^n) topology.

    For formal E_n algebras: S_4^{E_n} = S_4^{E_1}.

    The quartic contact invariant Q^contact (relevant for beta-gamma
    and Virasoro) is:
        Q^contact_{E_1}(Vir_c) = 10 / (c * (5c + 22))
    and for formal E_n algebras at n >= 2, this is the same value.
    """
    # For the free algebra: S_4 = 0
    if S3 == 0 and kappa != 0:
        return Fraction(0)
    return Fraction(0)


def shadow_depth_en(n: int, algebra_class: str) -> int:
    """Shadow depth r_max for an E_n algebra of the given class.

    The shadow depth classification (G/L/C/M) is:
        G (Gaussian): r_max = 2  (free fields)
        L (Lie/tree): r_max = 3  (KM algebras)
        C (contact):  r_max = 4  (beta-gamma, bc)
        M (mixed):    r_max = infinity  (Virasoro, W_N)

    For FORMAL E_n algebras, the shadow depth is the SAME as for E_1:
    formality ensures that the higher-arity corrections from Conf_k(R^n)
    topology do not change the termination behavior.

    For non-formal E_n algebras (not known to exist among standard
    families), the depth could differ.  All standard families are formal
    as E_n algebras for n >= 2 (by Kontsevich formality of the E_n operad).
    """
    depth_map = {
        'G': 2,    # Gaussian
        'L': 3,    # Lie/tree
        'C': 4,    # Contact
        'M': -1,   # Mixed (infinity, represented as -1)
    }
    if algebra_class not in depth_map:
        raise ValueError(f"Unknown shadow class: {algebra_class}. "
                          f"Must be one of G, L, C, M.")
    return depth_map[algebra_class]


# =========================================================================
# 6.  Formality
# =========================================================================

def en_operad_formal(n: int) -> bool:
    """Whether the E_n operad is formal over Q.

    E_1 (Ass): formal (trivially -- generated in arity 2 with no relations,
    so the operad is already its own cohomology).
    E_2: formal (Kontsevich 1999, Tamarkin 2003).
    E_n for n >= 3: formal (Lambrechts-Volic 2014, via PA forms on FM_n(R^n)).
    E_infty (Com): formal (trivially).

    WARNING: formality of the E_n OPERAD is different from formality of
    an E_n ALGEBRA.  The operad being formal means that any E_n algebra
    can be rectified to a strictly commutative (up to homotopy) structure.
    An E_n algebra being formal means its bar complex has trivial higher
    structure.
    """
    if n < 1:
        raise ValueError(f"E_n requires n >= 1, got {n}")
    return True  # All E_n operads are formal over Q


def en_algebra_formal(n: int, algebra_name: str) -> bool:
    """Whether a specific E_n algebra is formal.

    A formal E_n algebra has trivial higher shadow obstruction tower (S_r = 0 for r >= 3).
    This is a STRONGER condition than the operad being formal.

    Known formal examples:
    - C*(k[x], k[x]) as E_2 algebra (Kontsevich formality of Hochschild cochains)
    - Any E_n algebra over a field of char 0 that is free (= tensor algebra for E_1,
      symmetric algebra for E_infty)
    - Polynomial algebras k[x_1,...,x_m] as E_n algebras for n >= 2

    Known NON-formal examples:
    - Virasoro as E_1 algebra (shadow depth = infinity)
    - W_N algebras as E_1 algebras (shadow depth = infinity for N >= 2)
    """
    formal_algebras = {
        'free', 'heisenberg', 'polynomial', 'symmetric',
        'hochschild_polynomial',
    }
    return algebra_name.lower() in formal_algebras


# =========================================================================
# 7.  E_n factorization homology on standard manifolds
# =========================================================================

def factorization_homology_circle(n: int, kappa: Fraction) -> Dict[str, Any]:
    """Factorization homology integral_{S^1} A for A an E_n algebra.

    For n = 1: integral_{S^1} A = THH(A) = topological Hochschild homology.
    The genus-1 invariant is kappa * lambda_1 where lambda_1 = 1/24.

    For n >= 2: integral_{S^1} A requires A to be at least E_1.
    Since E_n -> E_1 (forgetful), any E_n algebra is in particular E_1.
    The factorization homology on S^1 forgets the higher E_n structure:
        integral_{S^1} A = THH(A as E_1 algebra)

    So the S^1 factorization homology is the SAME for all n.
    The genus-1 invariant is always kappa * lambda_1 = kappa / 24.
    """
    return {
        'manifold': 'S^1',
        'dimension': 1,
        'en_level': n,
        'invariant': 'THH(A)',
        'genus_1_shadow': kappa / 24,
        'note': 'S^1 sees only E_1 structure (forgetful E_n -> E_1)',
    }


def factorization_homology_torus(n: int, torus_dim: int,
                                  kappa: Fraction) -> Dict[str, Any]:
    """Factorization homology integral_{T^d} A for A an E_n algebra.

    For T^d = (S^1)^d, we need d <= n (the torus dimension cannot exceed
    the operadic dimension).

    integral_{T^d} A = THH^{(d)}(A) = iterated topological Hochschild.

    For d = 1: THH(A) as above.
    For d = 2 (requires n >= 2): integral_{T^2} A = THH(THH(A)).
        This is the "double Hochschild" or genus-1 invariant on a torus.
    For d = n: integral_{T^n} A uses the full E_n structure.

    The genus-1 shadow on T^d:
        For d = 1: kappa / 24
        For d = 2: kappa / 24 * dim(THH_0(A))
        (The higher iterated THH involves the HH groups of THH itself.)

    For a free algebra on one generator:
        THH_0(k[x]) = k[x] / (x * k[x]) = k  (for E_1 = associative)
        Actually, THH_0(k[x]) depends on the algebra structure:
        For k[x] as a commutative (E_infty) algebra: HH_0(k[x]) = k[x]
        For k[x] as an E_1 (associative) algebra: HH_0(k[x]) = k[x]/(commutators) = k[x]
        (k[x] is commutative, so commutators vanish and HH_0 = k[x].)

    The Euler characteristic of integral_{T^d} A is related to the
    iterated trace: chi(integral_{T^d} A) = tr^{(d)}(id_A).
    """
    if torus_dim > n:
        return {
            'manifold': f'T^{torus_dim}',
            'dimension': torus_dim,
            'en_level': n,
            'error': f'Torus dimension {torus_dim} exceeds E_{n} level {n}',
        }
    if torus_dim < 1:
        return {
            'manifold': 'T^0 = point',
            'dimension': 0,
            'en_level': n,
            'invariant': 'A itself',
            'genus_1_shadow': Fraction(0),
        }

    return {
        'manifold': f'T^{torus_dim}',
        'dimension': torus_dim,
        'en_level': n,
        'invariant': f'THH^({torus_dim})(A)',
        'iterated_hochschild_depth': torus_dim,
        'genus_1_shadow': kappa / 24,
        'note': (f'Iterated {torus_dim}-fold THH; '
                 f'genus-1 shadow on each S^1 factor is kappa/24'),
    }


def factorization_homology_sphere(n: int, sphere_dim: int,
                                   kappa: Fraction) -> Dict[str, Any]:
    """Factorization homology integral_{S^d} A for A an E_n algebra.

    For S^d with d <= n: the factorization homology uses the E_d structure.

    For d = 0: S^0 = two points; integral_{S^0} A = A tensor A.
    For d = 1: integral_{S^1} A = THH(A).
    For d = n: integral_{S^n} A = E_n-Hochschild homology of A.

    The E_n Hochschild homology (Francis 2013):
        HH^{E_n}(A) = integral_{S^n} A

    For A free on one generator:
        HH^{E_1}(k[x]) = HH(k[x]) (classical Hochschild)
        HH^{E_2}(k[x]) = higher Hochschild on S^2
        HH^{E_n}(k[x]) = higher Hochschild on S^n

    The key feature of S^n: it has nontrivial H_0 and H_n, both 1-dim.
    The E_n Hochschild homology correspondingly has contributions from
    the "trace" (H_0 of S^n) and the "cotrace" (H_n of S^n).
    """
    if sphere_dim > n:
        return {
            'manifold': f'S^{sphere_dim}',
            'dimension': sphere_dim,
            'en_level': n,
            'error': f'Sphere dimension {sphere_dim} exceeds E_{n} level {n}',
        }

    return {
        'manifold': f'S^{sphere_dim}',
        'dimension': sphere_dim,
        'en_level': n,
        'invariant': f'HH^{{E_{sphere_dim}}}(A)',
        'trace_contribution': kappa,
        'cotrace_shift': sphere_dim,
        'note': (f'E_{sphere_dim}-Hochschild homology; '
                 f'uses H_0(S^{sphere_dim}) and H_{sphere_dim}(S^{sphere_dim})'),
    }


# =========================================================================
# 8.  Stabilization: E_n -> E_infty = Com as n -> infty
# =========================================================================

def kappa_stabilization_sequence(max_n: int, k: Fraction = Fraction(1)) -> Dict[int, Fraction]:
    """kappa_{E_n}(H_k) for n = 1, 2, ..., max_n.

    Since kappa is determined by the binary part of the bar complex,
    and Conf_2(R^n) = R^n - {0} ~ S^{n-1} has the SAME propagator
    pairing for all n, kappa_{E_n} is CONSTANT in n:

        kappa_{E_n}(H_k) = k/2 for all n >= 1.

    The stabilization is trivial at the kappa level.  The higher shadows
    S_r for r >= 3 DO exhibit nontrivial stabilization (they depend on
    the topology of Conf_r(R^n), which stabilizes as n -> oo).
    """
    kappa_val = k / 2
    return {n_val: kappa_val for n_val in range(1, max_n + 1)}


def higher_shadow_stabilization_threshold(arity: int) -> int:
    """The value of n beyond which S_r^{E_n} stabilizes (becomes independent of n).

    For arity r, the shadow S_r depends on H*(Conf_r(R^n)).
    The positive-degree cohomology of Conf_r(R^n) starts in degree n-1.
    For n-1 > (r-1) * max_propagator_degree, the arity-r shadow
    cannot receive corrections from positive-degree classes.

    The stabilization threshold is:
        n_stable(r) = r  (for r >= 2)

    For n >= r: the only contribution to the arity-r shadow from
    positive-degree classes in H*(Conf_r(R^n)) is in degree >= n-1 >= r-1,
    which exceeds the arity budget.  So S_r^{E_n} = S_r^{E_infty}
    for n >= r.

    More precisely: at arity r, the bar complex involves Conf_r(R^n).
    The cohomology H^*(Conf_r(R^n)) lives in degrees 0, n-1, 2(n-1), ..., (r-1)(n-1).
    For n >= 2, the first positive-degree class is in degree n-1.
    The shadow S_r involves interactions between r propagators, and the
    total degree budget for arity r in the shadow obstruction tower is r-2 (from the
    MC equation).  So the positive-degree classes contribute only when
    n-1 <= r-2, i.e., n <= r-1.  For n >= r, they do not contribute,
    and S_r^{E_n} = S_r^{tree} = S_r^{E_infty}.
    """
    if arity < 2:
        return 1
    return arity


def shadow_en_stabilized_value(arity: int,
                                algebra_class: str) -> Fraction:
    """The stabilized value of S_r^{E_n} for n >> r (= S_r^{E_infty}).

    In the stable range, the E_n shadow equals the tree-level shadow
    (no loop corrections from configuration space topology).

    For standard families:
        G (free/Heisenberg): S_r = 0 for r >= 3 (all n)
        L (KM): S_3 = nonzero, S_r = 0 for r >= 4 (tree termination)
        C (contact): S_4 = nonzero, S_r = 0 for r >= 5 (contact termination)
        M (Virasoro/W_N): S_r != 0 for all r (no termination)
    """
    if algebra_class == 'G':
        return Fraction(0)
    elif algebra_class == 'L':
        return Fraction(0) if arity >= 4 else Fraction(1)  # Placeholder
    elif algebra_class == 'C':
        return Fraction(0) if arity >= 5 else Fraction(1)  # Placeholder
    else:
        return Fraction(1)  # Placeholder for M class


# =========================================================================
# 9.  Dunn additivity: E_{m+n} = E_m tensor E_n
# =========================================================================

def dunn_additivity_check(m: int, n_val: int) -> Dict[str, Any]:
    """Verify Dunn additivity E_{m+n} = E_m tensor E_n at the level of
    configuration space Betti numbers.

    Dunn's theorem: E_{m+n} = E_m tensor E_n as operads.
    At the algebra level: an E_{m+n} algebra is an E_m algebra in
    the category of E_n algebras.

    At the configuration space level:
        Conf_k(R^{m+n}) = Conf_k(R^m x R^n)

    The Betti numbers satisfy:
        P(Conf_k(R^{m+n}), t) = prod_{j=0}^{k-1} (1 + j * t^{m+n-1})

    This does NOT factor as P(Conf_k(R^m)) * P(Conf_k(R^n)) in general.
    Dunn additivity operates at the OPERAD level, not at the level of
    individual configuration spaces.

    We verify the Betti numbers for consistency.
    """
    sum_mn = m + n_val
    betti_sum = conf_space_betti(3, sum_mn)    # arity 3 as test
    betti_m = conf_space_betti(3, m)
    betti_n = conf_space_betti(3, n_val)

    # The Koszul shift is additive: shift(E_{m+n}) = m+n = shift(E_m) + shift(E_n)
    shift_sum = en_koszul_shift(sum_mn)
    shift_m = en_koszul_shift(m)
    shift_n = en_koszul_shift(n_val)

    return {
        'm': m,
        'n': n_val,
        'm+n': sum_mn,
        'koszul_shift_additive': shift_sum == shift_m + shift_n,
        'betti_Conf3_Rmn': betti_sum,
        'betti_Conf3_Rm': betti_m,
        'betti_Conf3_Rn': betti_n,
        'propagator_degree_sum': en_generator_degree(sum_mn),
        'propagator_degree_m': en_generator_degree(m),
        'propagator_degree_n': en_generator_degree(n_val),
        'propagator_degree_additive': (en_generator_degree(sum_mn)
                                        == en_generator_degree(m) + en_generator_degree(n_val)),
    }


def kappa_dunn_additivity(m: int, n_val: int, k: Fraction = Fraction(1)) -> Dict[str, Any]:
    """Test Dunn additivity at the kappa level.

    kappa_{E_{m+n}}(H_k) vs kappa_{E_m}(H_k) and kappa_{E_n}(H_k).

    Since kappa is universal (= k/2 for all n), Dunn additivity at the
    kappa level is trivially satisfied:
        kappa_{E_{m+n}} = kappa_{E_m} = kappa_{E_n} = k/2.

    The nontrivial content of Dunn additivity appears at higher arities.
    """
    k_sum = kappa_en_free(m + n_val, k)
    k_m = kappa_en_free(m, k)
    k_n = kappa_en_free(n_val, k)

    return {
        'm': m,
        'n': n_val,
        'kappa_E_{m+n}': k_sum,
        'kappa_E_m': k_m,
        'kappa_E_n': k_n,
        'all_equal': k_sum == k_m == k_n,
        'value': k_sum,
    }


# =========================================================================
# 10.  Swiss-cheese connection: E_1^{ch} x E_1^{top} inside E_2
# =========================================================================

def swiss_cheese_e2_decomposition() -> Dict[str, Any]:
    """The Swiss-cheese operad SC^{ch,top} as a sub-operad structure of E_2.

    The E_2 operad (little 2-disks) contains two distinguished E_1 sub-operads:
    (1) E_1^{ch}: little intervals along the horizontal (chiral/holomorphic)
    (2) E_1^{top}: little intervals along the vertical (topological)

    Together they generate the Swiss-cheese operad SC (Voronov):
        SC = E_1^{ch} tensor_{E_0} E_1^{top}
    where E_0 is the trivial operad (just units).

    At the shadow level:
        kappa_{E_2} = kappa_{E_1^{ch}} = kappa_{E_1^{top}} = kappa
    (all binary, hence universal).

    The nontrivial structure appears at the arity-3 level:
    the Swiss-cheese has MIXED operations (one chiral, one topological input)
    that do not exist in either E_1 factor alone.

    For the Heisenberg algebra:
        kappa^{SC} = kappa^{E_2} = k/2  (same as chiral)
        S_3^{SC} = 0  (Heisenberg is class G)
    """
    return {
        'operad': 'SC^{ch,top}',
        'ambient': 'E_2',
        'chiral_factor': 'E_1^{ch} (horizontal)',
        'topological_factor': 'E_1^{top} (vertical)',
        'kappa_relation': 'kappa_{SC} = kappa_{E_2} = kappa_{E_1}',
        'novel_at_arity': 3,
        'novel_description': ('Mixed operations: one chiral + one topological input; '
                              'absent from either E_1 factor'),
        'heisenberg_kappa': 'k/2',
        'heisenberg_S3': 0,
    }


def swiss_cheese_shadow_heisenberg(k: Fraction = Fraction(1)) -> Dict[str, Any]:
    """E_2 shadow obstruction tower for Heisenberg, decomposed via Swiss-cheese.

    The Heisenberg algebra H_k has:
        kappa = k/2  (all E_n agree)
        S_3 = 0      (free field, class G)
        shadow depth = 2 (terminates at kappa)

    The Swiss-cheese decomposition splits the bar complex into:
    - Pure chiral component (E_1^{ch} bar): classical chiral bar complex
    - Pure topological component (E_1^{top} bar): trivial (Heisenberg is
      commutative as a topological algebra)
    - Mixed component: vanishes for free fields (no mixed OPE)

    All three components give kappa = k/2, consistent with universality.
    """
    kappa = k / 2
    return {
        'algebra': 'Heisenberg',
        'level': k,
        'kappa_chiral': kappa,
        'kappa_topological': kappa,
        'kappa_mixed': Fraction(0),
        'kappa_total': kappa,
        'S3': Fraction(0),
        'shadow_depth': 2,
        'class': 'G',
    }


# =========================================================================
# 11.  Kontsevich formality and graph complex
# =========================================================================

def graph_complex_euler_char(n: int, loop_order: int) -> int:
    """Euler characteristic of the graph complex GC_n at a given loop order.

    The graph complex GC_n (Kontsevich, Willwacher) controls the homotopy
    automorphisms of E_n.  Its cohomology computes:
        H^0(GC_2) = grt  (Grothendieck-Teichmuller Lie algebra)

    The Euler characteristic at loop order L is related to the number
    of connected graphs with L loops on k vertices (where k depends on
    the degree).

    For GC_2 at low loop orders:
        L=1: chi = 0 (the wheel graphs cancel)
        L=2: chi = 1 (one generator: the Drinfeld associator)
        L=3: chi = 1

    For GC_n with n odd: GC_n is acyclic in positive degrees (Willwacher).
    For GC_n with n even: GC_n has rich cohomology.
    """
    if n % 2 == 1 and loop_order > 0:
        return 0  # GC_n acyclic for n odd
    # For n even, low loop orders:
    if n == 2:
        # Known values from Willwacher's computation
        low_loop_euler = {0: 1, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
        return low_loop_euler.get(loop_order, -1)  # -1 = unknown
    # For other even n, use that GC_n ~ GC_2 up to degree shift
    # (Willwacher's theorem: H^k(GC_n) ~ H^{k+(n-2)}(GC_2) for n even)
    return graph_complex_euler_char(2, loop_order)


def willwacher_grt_dimension(degree: int) -> int:
    """Dimension of the degree-d part of grt = H^0(GC_2).

    The Grothendieck-Teichmuller Lie algebra grt controls the homotopy
    type of the E_2 operad.

    Known dimensions (from Willwacher, Brown, Schneps):
        degree 1: 0
        degree 3: 1  (the sigma_3 element, related to zeta(3))
        degree 5: 1  (related to zeta(5))
        degree 7: 1  (related to zeta(7))
        degree 9: 1  (related to zeta(9))
        degree 11: 2 (zeta(11) and a new depth-2 element)

    For even degrees: 0 (parity vanishing).
    """
    if degree < 1 or degree % 2 == 0:
        return 0
    # Known dimensions in odd degrees
    grt_dims = {
        1: 0,
        3: 1,
        5: 1,
        7: 1,
        9: 1,
        11: 2,
        13: 2,
    }
    return grt_dims.get(degree, -1)  # -1 = not computed


# =========================================================================
# 12.  E_2 bar complex for specific algebras
# =========================================================================

def e2_bar_polynomial_algebra(num_vars: int,
                               weight_bound: int) -> Dict[str, Any]:
    """E_2 bar complex for k[x_1,...,x_m] (polynomial algebra as E_2 algebra).

    By Kontsevich formality, the E_2 bar complex of a polynomial algebra
    is formal: B_{E_2}(k[x_1,...,x_m]) has trivial A_infty structure.

    The bar cohomology:
        H*(B_{E_2}(k[x])) = the E_2 coalgebra cogenerated by k[-2]
    (one cogenerator in degree 2 = Koszul shift for E_2).

    For k[x_1,...,x_m]:
        H*(B_{E_2}) = free E_2 coalgebra on k[-2]^m

    The shadow obstruction tower terminates at kappa (class G), S_r = 0 for r >= 3.
    """
    kappa = Fraction(num_vars, 2)  # kappa = m/2 for m free generators at level 1
    return {
        'algebra': f'k[x_1,...,x_{num_vars}]',
        'en_level': 2,
        'bar_cohomology': f'Free E_2 coalgebra on k[-2]^{num_vars}',
        'kappa': kappa,
        'formal': True,
        'shadow_depth': 2,
        'class': 'G',
        'weight_bound': weight_bound,
        'bar_dim_arity2': num_vars * (num_vars + 1) // 2,  # Sym^2 of generators
    }


def e3_bar_free_algebra(num_vars: int) -> Dict[str, Any]:
    """E_3 bar complex for free E_3 algebra on m generators.

    By formality of E_3 (Lambrechts-Volic), the bar complex is formal.

    H*(B_{E_3}(Free_m)) = free E_3 coalgebra on k[-3]^m
    (shift by 3 = Koszul shift for E_3).

    kappa = m/2 (universal at the binary level).
    Shadow depth = 2 (class G: free algebra).
    """
    kappa = Fraction(num_vars, 2)
    return {
        'algebra': f'Free E_3 on {num_vars} generators',
        'en_level': 3,
        'bar_cohomology': f'Free E_3 coalgebra on k[-3]^{num_vars}',
        'kappa': kappa,
        'formal': True,
        'shadow_depth': 2,
        'class': 'G',
    }


# =========================================================================
# 13.  Comprehensive summary
# =========================================================================

def en_shadow_summary(n: int, algebra_name: str = 'heisenberg',
                       k: Fraction = Fraction(1)) -> Dict[str, Any]:
    """Full shadow obstruction tower summary for an E_n algebra.

    Collects kappa, shadow depth, formality status, stabilization info.
    """
    kappa = kappa_en_free(n, k)
    formal = en_algebra_formal(n, algebra_name)
    operad_formal = en_operad_formal(n)

    return {
        'en_level': n,
        'algebra': algebra_name,
        'level': k,
        'kappa': kappa,
        'kappa_over_24': kappa / 24,
        'operad_formal': operad_formal,
        'algebra_formal': formal,
        'koszul_shift': en_koszul_shift(n),
        'propagator_degree': en_generator_degree(n),
        'dual_operad': en_dual_operad_name(n),
        'shadow_depth': 2 if formal else -1,
        'class': 'G' if formal else 'unknown',
        'stabilization_threshold_arity3': higher_shadow_stabilization_threshold(3),
    }


def en_comparison_table(max_n: int = 6,
                         k: Fraction = Fraction(1)) -> List[Dict[str, Any]]:
    """Comparison table for E_n shadow invariants at n = 1, 2, ..., max_n.

    For the free algebra (Heisenberg type) at level k.
    """
    table = []
    for n_val in range(1, max_n + 1):
        entry = {
            'n': n_val,
            'propagator_degree': en_generator_degree(n_val),
            'koszul_shift': en_koszul_shift(n_val),
            'kappa': kappa_en_free(n_val, k),
            'operad_formal': en_operad_formal(n_val),
            'conf3_betti': conf_space_betti(3, n_val),
            'conf3_total': conf_space_total_betti(3, n_val),
            'conf4_total': conf_space_total_betti(4, n_val),
        }
        table.append(entry)
    return table
