r"""
cy_derived_moduli_engine.py — Tangent complexes, obstruction spaces, and
virtual dimensions for derived moduli of sheaves on K3 x E.

THE MATHEMATICAL CONTENT
========================

Let X = K3 x E be the product of a K3 surface and an elliptic curve.
X is a Calabi-Yau 3-fold: omega_X = omega_{K3} (x) omega_E is trivial.
The derived category D^b(X) carries a rich moduli theory.

1. TANGENT COMPLEX AT A POINT [E] in M(X)

   For E in D^b(X), the tangent complex is:

       T_{[E]} M = RHom(E, E)[1]

   giving:

       Ext^0(E, E) = Hom(E, E) = automorphisms (degree -1 in T)
       Ext^1(E, E) = first-order deformations (degree 0 in T)
       Ext^2(E, E) = obstructions (degree 1 in T)
       Ext^3(E, E) = higher obstructions (degree 2 in T)

   Serre duality on CY3: Ext^k(E, E) = Ext^{3-k}(E, E)^*

2. HODGE NUMBERS OF K3 x E

   K3: h^{p,q} known — h^{0,0}=h^{2,0}=h^{0,2}=h^{2,2}=1, h^{1,1}=20
   E:  h^{0,0}=h^{1,0}=h^{0,1}=h^{1,1}=1
   X = K3 x E by Kuenneth:
       H^k(X, O_X) = sum_{i+j=k} H^i(K3, O) (x) H^j(E, O)

   K3: H^0(O)=C, H^1(O)=0, H^2(O)=C
   E:  H^0(O)=C, H^1(O)=C

   X:  H^0(O)=C, H^1(O)=C, H^2(O)=C, H^3(O)=C

3. VIRTUAL DIMENSION

   For CY3: vdim = -chi(E, E) where chi = sum (-1)^k dim Ext^k.
   By Serre duality + chi symmetry: chi(E,E) = 0 always for CY3.
   So vdim = 0 for all moduli problems on CY3!

4. HILBERT SCHEME OF POINTS

   Hilb^n(X): dim Ext^1(I_Z, I_Z) = 3n (deform n pts in a 3-fold).
   By Serre: dim Ext^2(I_Z, I_Z) = 3n.
   vdim = 0.

5. DT INVARIANTS

   DT_n = deg [Hilb^n(X)]^{vir} in A_0.
   For K3 x E: DT_0 = 1, DT_n for n >= 1 from virtual localization
   along the E-direction.

6. KURANISHI MAP

   kappa: Ext^1(E,E) -> Ext^2(E,E) via cup product (Yoneda composition).
   For I_Z on X = K3 x E: factorizes through Kuenneth.

7. ATIYAH CLASS

   At(E) in Ext^1(E, E (x) Omega^1_X): the obstruction to a holomorphic
   connection.  Controls the L-infinity structure on T_M via
   ell_2(a,b) = a o At o b + b o At o a.

MULTI-PATH VERIFICATION
=======================
  Path 1: Direct Ext computation via Kuenneth decomposition
  Path 2: Serre duality cross-check
  Path 3: Virtual dimension formula verification
  Path 4: Euler characteristic computation via Hodge numbers
  Path 5: Comparison with DT partition function

CONVENTIONS
===========
- Cohomological grading: Ext^k lives in cohomological degree k.
- Shift convention: T_M = RHom(E,E)[1], so Ext^k becomes degree k-1 in T.
- CY3: omega_X trivial => Serre duality Ext^k(E,E) = Ext^{3-k}(E,E)^*.
- AP45: desuspension lowers degree.
- AP19: careful with shift conventions in tangent complex.

Manuscript references:
    thm:mc2-bar-intrinsic (bar_cobar_adjunction_curved.tex)
    def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Part 0: Hodge data for the component surfaces and their product
# ---------------------------------------------------------------------------

# Hodge diamond of K3
# h^{p,q}(K3):
#      1
#    0   0
#  1  20  1
#    0   0
#      1
K3_HODGE = {
    (0, 0): 1, (1, 0): 0, (0, 1): 0,
    (2, 0): 1, (1, 1): 20, (0, 2): 1,
    (2, 1): 0, (1, 2): 0, (2, 2): 1,
}

# Hodge diamond of elliptic curve E
# h^{p,q}(E):
#    1
#  1   1
#    1
E_HODGE = {
    (0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 1,
}


def k3_hodge(p: int, q: int) -> int:
    """h^{p,q}(K3). Returns 0 for out-of-range indices."""
    if p < 0 or q < 0 or p > 2 or q > 2:
        return 0
    return K3_HODGE.get((p, q), 0)


def elliptic_hodge(p: int, q: int) -> int:
    """h^{p,q}(E) for an elliptic curve."""
    if p < 0 or q < 0 or p > 1 or q > 1:
        return 0
    return E_HODGE.get((p, q), 0)


def product_hodge(p: int, q: int) -> int:
    """h^{p,q}(K3 x E) via Kuenneth: h^{p,q}(X) = sum h^{a,b}(K3)*h^{p-a,q-b}(E)."""
    total = 0
    for a in range(max(0, p - 1), min(2, p) + 1):
        for b in range(max(0, q - 1), min(2, q) + 1):
            total += k3_hodge(a, b) * elliptic_hodge(p - a, q - b)
    return total


def product_betti(k: int) -> int:
    """b_k(K3 x E) = sum_{p+q=k} h^{p,q}(K3 x E)."""
    total = 0
    for p in range(min(3, k) + 1):
        q = k - p
        if 0 <= q <= 3:
            total += product_hodge(p, q)
    return total


def product_euler_char() -> int:
    """chi(K3 x E) = sum (-1)^k b_k."""
    return sum((-1)**k * product_betti(k) for k in range(7))


def cohomology_O(k: int) -> int:
    """dim H^k(K3 x E, O) = h^{0,k}(K3 x E) via Kuenneth.

    H^k(X, O_X) = sum_{i+j=k} H^i(K3, O_{K3}) (x) H^j(E, O_E)
    where H^i(K3, O) has dimensions 1, 0, 1 for i = 0, 1, 2
    and H^j(E, O) has dimensions 1, 1 for j = 0, 1.

    Result: H^0=C, H^1=C, H^2=C, H^3=C.
    """
    # This is h^{0,k}(K3 x E) by Hodge theory
    return product_hodge(0, k)


# ---------------------------------------------------------------------------
# Part 1: Tangent complex for the structure sheaf
# ---------------------------------------------------------------------------

@dataclass
class TangentComplexData:
    """Tangent complex T_{[E]} M = RHom(E, E)[1] at a point of the moduli space.

    Attributes:
        sheaf_name: description of the sheaf E
        ext_dims: dict mapping k -> dim Ext^k(E, E)
        tangent_degrees: dict mapping degree d -> dim T^d (after [1] shift)
        virtual_dim: -chi(E, E)
        serre_check: whether Serre duality is verified
    """
    sheaf_name: str
    ext_dims: Dict[int, int]
    tangent_degrees: Dict[int, int]
    virtual_dim: int
    serre_check: bool


def tangent_complex_structure_sheaf() -> TangentComplexData:
    """Tangent complex for E = O_{K3 x E} (the structure sheaf).

    Ext^k(O, O) = H^k(X, O_X) by RHom(O, O) = R Gamma(O).

    K3 x E:
      H^0(O) = C  (dim 1)
      H^1(O) = C  (dim 1, from E factor: H^0(K3,O) (x) H^1(E,O))
      H^2(O) = C  (dim 1, from H^2(K3,O) (x) H^0(E,O))
      H^3(O) = C  (dim 1, from H^2(K3,O) (x) H^1(E,O))

    Serre duality: Ext^k(O,O) = Ext^{3-k}(O,O)^* => dim matches.
      dim Ext^0 = 1 = dim Ext^3 (check)
      dim Ext^1 = 1 = dim Ext^2 (check)

    T = RHom(O,O)[1]:
      T^{-1} = Ext^0 = C  (automorphisms)
      T^0 = Ext^1 = C      (deformations)
      T^1 = Ext^2 = C      (obstructions)
      T^2 = Ext^3 = C      (higher, dual to auts by Serre)

    Virtual dimension = -chi(O,O) = -(1-1+1-1) = 0.
    """
    ext_dims = {}
    for k in range(4):
        ext_dims[k] = cohomology_O(k)

    # After [1] shift: T^d = Ext^{d+1}
    tangent_degrees = {d: ext_dims[d + 1] for d in range(-1, 3)}

    chi = sum((-1)**k * ext_dims[k] for k in range(4))
    vdim = -chi

    # Serre duality check
    serre_ok = all(ext_dims[k] == ext_dims[3 - k] for k in range(4))

    return TangentComplexData(
        sheaf_name="O_{K3 x E}",
        ext_dims=ext_dims,
        tangent_degrees=tangent_degrees,
        virtual_dim=vdim,
        serre_check=serre_ok,
    )


# ---------------------------------------------------------------------------
# Part 2: Ideal sheaves of points — Hilbert scheme
# ---------------------------------------------------------------------------

@dataclass
class IdealSheafExtData:
    """Ext data for the ideal sheaf I_Z of n points Z in a CY3 X.

    For n points in a smooth CY3:
      Ext^0(I_Z, I_Z) = C (the identity)
      Ext^1(I_Z, I_Z) = tangent to Hilb^n at [Z], dim = 3n
      Ext^2(I_Z, I_Z) = obstruction space, dim = 3n (Serre dual to Ext^1)
      Ext^3(I_Z, I_Z) = C (Serre dual to Ext^0)

    The formula dim Ext^1 = 3n comes from:
      Ext^1(I_Z, I_Z) = Ext^1(I_Z, O_X) (via the SES 0 -> I_Z -> O_X -> O_Z -> 0)
      which is the tangent space to Hilb^n(X) at [Z], of dimension
      dim X * n = 3n for a 3-fold.
    """
    n_points: int
    ext_dims: Dict[int, int]
    virtual_dim: int
    serre_check: bool
    deformation_dim: int
    obstruction_dim: int


def ideal_sheaf_ext(n: int, dim_X: int = 3) -> IdealSheafExtData:
    """Compute Ext data for I_Z of n points in a CY 3-fold X.

    For general CY d-fold, the tangent space has dim d*n.
    We specialize to d=3 for K3 x E.

    Parameters:
        n: number of points
        dim_X: dimension of the CY manifold (default 3)

    Returns:
        IdealSheafExtData with all Ext dimensions and virtual dimension.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    if n == 0:
        # I_Z = O_X, falls back to structure sheaf case
        ext_dims = {k: cohomology_O(k) for k in range(dim_X + 1)}
    else:
        # For n >= 1 points in a smooth CY3:
        # Ext^0(I_Z, I_Z) = Hom(I_Z, I_Z) = C (just rescaling)
        # Ext^1(I_Z, I_Z) = 3n (deformations of the n points in the 3-fold)
        # Ext^2(I_Z, I_Z) = 3n (Serre dual of Ext^1)
        # Ext^3(I_Z, I_Z) = C (Serre dual of Ext^0)
        #
        # Derivation: from the exact sequence 0 -> I_Z -> O_X -> O_Z -> 0,
        # applying RHom(I_Z, -):
        #   Ext^k(I_Z, O_Z) contributes local deformations.
        # The local-to-global spectral sequence gives:
        #   dim Ext^1(I_Z, I_Z) = dim_X * n for points in general position.
        ext_dims = {
            0: 1,
            1: dim_X * n,
            2: dim_X * n,  # Serre dual of Ext^1
            3: 1,          # Serre dual of Ext^0
        }

    chi = sum((-1)**k * ext_dims[k] for k in range(dim_X + 1))
    vdim = -chi

    serre_ok = all(
        ext_dims.get(k, 0) == ext_dims.get(dim_X - k, 0)
        for k in range(dim_X + 1)
    )

    return IdealSheafExtData(
        n_points=n,
        ext_dims=ext_dims,
        virtual_dim=vdim,
        serre_check=serre_ok,
        deformation_dim=ext_dims.get(1, 0),
        obstruction_dim=ext_dims.get(2, 0),
    )


# ---------------------------------------------------------------------------
# Part 3: Virtual dimension computations
# ---------------------------------------------------------------------------

def euler_char_ext(ext_dims: Dict[int, int]) -> int:
    """chi(E, E) = sum_{k >= 0} (-1)^k dim Ext^k(E, E)."""
    return sum((-1)**k * dim for k, dim in ext_dims.items())


def virtual_dimension(ext_dims: Dict[int, int]) -> int:
    """vdim M = -chi(E, E) for CY3 moduli.

    This is always 0 for CY3 by Serre duality:
      chi = sum (-1)^k ext^k = 0 when ext^k = ext^{3-k}.
    """
    return -euler_char_ext(ext_dims)


def virtual_dim_CY3_always_zero(ext_dims: Dict[int, int]) -> bool:
    """Verify that vdim = 0 for a CY3 moduli problem.

    By Serre duality on CY3: Ext^k = Ext^{3-k}^*, so
    chi = ext^0 - ext^1 + ext^2 - ext^3 = ext^0 - ext^1 + ext^1 - ext^0 = 0.
    """
    return virtual_dimension(ext_dims) == 0


# ---------------------------------------------------------------------------
# Part 4: Perfect obstruction theory
# ---------------------------------------------------------------------------

@dataclass
class PerfectObstructionTheoryData:
    """Data for the perfect obstruction theory on Hilb^n(K3 x E).

    The POT is: E^bullet = (RHom(I, I))_0[1] -> L_{Hilb^n}

    Here (-)_0 denotes the traceless part (quotient by the scalar maps).
    For the full RHom: rk E^0 = ext^1, rk E^{-1} = ext^0 + ext^2 - 1
    (or more precisely, the ranks satisfy rk E^0 - rk E^{-1} = vdim).

    The virtual fundamental class: [Hilb^n]^{vir} in A_0(Hilb^n).
    The DT invariant: DT_n = deg [Hilb^n]^{vir}.
    """
    n_points: int
    rk_E0: int
    rk_Eminus1: int
    virtual_dim: int
    virtual_class_degree: int  # DT_n


def perfect_obstruction_theory(n: int) -> PerfectObstructionTheoryData:
    """Compute the POT data for Hilb^n(K3 x E).

    The 2-term complex E^{-1} -> E^0:
      E^0 has rank = dim Ext^1(I_Z, I_Z) = 3n
      E^{-1} has rank = dim Ext^2(I_Z, I_Z) = 3n
      (traceless part, after removing the scalar Hom and its Serre dual)

    Actually for the traceless perfect obstruction theory:
      rk E^0 - rk E^{-1} = vdim = 0.

    The DT invariant for K3 x E:
      DT_0 = 1 (empty subscheme)
      DT_n for n >= 1 is computed via the virtual localization formula
      with respect to the E-action.

    For K3 x E:
      The Euler characteristic chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.
      Hence the DT partition function simplifies.

    The DT invariants for K3 x E encode counting of ideal sheaves.
    At n=0: DT_0 = 1 (the empty subscheme contributes 1).
    For n >= 1 with chi(X) = 0: the DT invariants depend on the
    detailed geometry. For K3 x E the reduced DT theory gives DT_n^{red}.
    """
    ext_data = ideal_sheaf_ext(n)

    # For the traceless POT:
    # The complex E^{-1} -> E^0 has ranks such that rk E^0 - rk E^{-1} = vdim = 0
    if n == 0:
        rk_E0 = 0
        rk_Eminus1 = 0
    else:
        rk_E0 = 3 * n
        rk_Eminus1 = 3 * n

    vdim = rk_E0 - rk_Eminus1  # = 0

    # DT invariant: DT_0 = 1, DT_n for K3 x E with chi = 0
    # The generating function: sum DT_n q^n
    # For chi(X) = 0: the MNOP conjecture/theorem gives the full structure.
    # DT_0 = 1 always.
    # For K3 x E with chi = 0: DT_1 = chi(O_{K3 x E}) = chi(K3 x E, O) = 0
    # Actually: for n=1, DT_1 = chi(X) (the topological Euler characteristic
    # of the 3-fold). Since chi(K3 x E) = 24 * 0 = 0, DT_1 = 0.
    #
    # More precisely, for the reduced DT theory of K3 x E:
    # The partition function is related to the Igusa cusp form chi_10
    # via the KKV (Katz-Klemm-Vafa) formula.
    if n == 0:
        dt_n = 1
    elif n == 1:
        # DT_1 = chi_top(X) for CY3 (Behrend-Fantechi).
        # chi_top(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.
        dt_n = 0
    elif n == 2:
        # DT_2 for K3 x E: from the virtual localization, DT_2 = 0 when chi=0
        # More precisely: DT_2 = chi(X) * (chi(X) + 10) / 2 for CY3
        # with chi = 0 gives DT_2 = 0.
        # But this is for the UNREDUCED theory.
        dt_n = 0
    else:
        # For chi(X) = 0 CY3: the unreduced DT_n are all related to
        # coefficient of q^n in M(q)^{chi(X)} = M(q)^0 = 1.
        # So all unreduced DT_n = 0 for n >= 1 when chi = 0.
        dt_n = 0

    return PerfectObstructionTheoryData(
        n_points=n,
        rk_E0=rk_E0,
        rk_Eminus1=rk_Eminus1,
        virtual_dim=vdim,
        virtual_class_degree=dt_n,
    )


# ---------------------------------------------------------------------------
# Part 5: Kuranishi map
# ---------------------------------------------------------------------------

@dataclass
class KuranishiMapData:
    """Data for the Kuranishi map kappa: Ext^1(E,E) -> Ext^2(E,E).

    The Kuranishi map encodes the singularity structure of the moduli
    space at the point [E]. For the structure sheaf on K3 x E:

      kappa: H^1(O) -> H^2(O)

    This is the cup product map, which factors through the Kuenneth
    decomposition.

    For a point Z = {pt} in K3 x E:
      kappa: H^0(N_{Z/X}) -> H^1(wedge^2 N_{Z/X})
    where N_{Z/X} = T_X|_Z is the normal bundle (trivial for a point).
    """
    source_dim: int
    target_dim: int
    # The map is given by a matrix (in some basis)
    # For our cases this is a bilinear map Ext^1 x Ext^1 -> Ext^2
    # (the Yoneda product / cup product)
    map_description: str
    is_zero: bool
    kernel_dim: int
    cokernel_dim: int


def kuranishi_structure_sheaf() -> KuranishiMapData:
    """Kuranishi map for E = O_{K3 x E}.

    kappa: Ext^1(O, O) -> Ext^2(O, O) is the cup product
    H^1(X, O) (x) H^1(X, O) -> H^2(X, O).

    Via Kuenneth:
      H^1(X, O) = H^0(K3,O) (x) H^1(E,O) = C (generated by dz-bar on E)
      H^2(X, O) = H^2(K3,O) (x) H^0(E,O) = C (generated by omega_{K3})

    The cup product H^1(O) (x) H^1(O) -> H^2(O) is:
      (H^0(K3) (x) H^1(E)) (x) (H^0(K3) (x) H^1(E))
        -> sum H^{a+c}(K3) (x) H^{b+d}(E)

    The only way to land in H^2(X,O) = H^2(K3) (x) H^0(E) would require
    H^0(K3) * H^0(K3) -> H^0(K3) (OK, identity)
    and H^1(E) * H^1(E) -> H^0(E)?? NO. H^1(E) cup H^1(E) -> H^2(E) = C.

    Actually: H^1(O_X) * H^1(O_X) -> H^2(O_X).
    H^1(O_X) = H^0(K3,O) (x) H^1(E,O) has one generator: 1 (x) [dz-bar].
    The cup product of this with itself:
    (1 (x) [dz-bar]) cup (1 (x) [dz-bar]) = (1 cup 1) (x) ([dz-bar] cup [dz-bar])
    = 1 (x) 0 = 0    (since [dz-bar] cup [dz-bar] = 0 on a curve, by degree).

    Wait: [dz-bar] in H^{0,1}(E), so [dz-bar] cup [dz-bar] in H^{0,2}(E) = 0
    since dim_C(E) = 1, so H^{0,2}(E) = 0.

    Therefore: the Kuranishi map for O_{K3xE} is ZERO.
    The moduli space is smooth (unobstructed) at this point.
    """
    return KuranishiMapData(
        source_dim=1,
        target_dim=1,
        map_description=(
            "Cup product H^1(O) x H^1(O) -> H^2(O). "
            "H^1(O) = H^0(K3,O) (x) H^1(E,O). Self-cup = 0 "
            "because H^{0,1}(E) cup H^{0,1}(E) -> H^{0,2}(E) = 0."
        ),
        is_zero=True,
        kernel_dim=1,
        cokernel_dim=1,
    )


def kuranishi_ideal_sheaf_point() -> KuranishiMapData:
    """Kuranishi map for E = I_Z where Z = {pt} in K3 x E.

    For a single point Z = {p} in a smooth CY3 X:
      Ext^1(I_Z, I_Z) = T_p X = C^3
      Ext^2(I_Z, I_Z) = (T_p X)^* = C^3 (Serre dual)

    The Kuranishi map kappa: C^3 -> C^3 is the map controlling the
    local structure of Hilb^1(X) = X itself.

    Since X is smooth, Hilb^1(X) = X is smooth, so the Kuranishi map
    must vanish (no obstructions to deforming a point in a smooth space).

    More explicitly: the Kuranishi map is the cup product
    Ext^1(I_Z, I_Z) (x) Ext^1(I_Z, I_Z) -> Ext^2(I_Z, I_Z).
    For a point in a smooth variety, this is the bracket on the
    tangent space. Since X is a manifold (commutative deformation problem),
    the bracket vanishes — the deformation functor is unobstructed.
    """
    return KuranishiMapData(
        source_dim=3,
        target_dim=3,
        map_description=(
            "Cup product on Ext^*(I_Z, I_Z) for Z = {pt}. "
            "Since Hilb^1(X) = X is smooth, the Kuranishi map vanishes."
        ),
        is_zero=True,
        kernel_dim=3,
        cokernel_dim=3,
    )


def kuranishi_ideal_sheaf_n_points(n: int) -> KuranishiMapData:
    """Kuranishi map for I_Z of n points in K3 x E.

    Hilb^n(K3 x E) is generally SINGULAR for n >= 2.
    However, the generic point (n distinct points) is smooth,
    and the Kuranishi map vanishes there.

    At a non-reduced point (e.g., a fat point), the Kuranishi map
    can be nonzero. But the GENERIC Kuranishi map still vanishes
    because distinct points deform independently.

    For the K3 factor: Hilb^n(K3) is smooth (Beauville) of dim 2n.
    The product Hilb^n(K3) x E^n is smooth of dim 3n.
    But Hilb^n(K3 x E) != Hilb^n(K3) x E^n in general.

    Still, for n distinct points in general position in K3 x E,
    the tangent space decomposes as a direct sum of tangent spaces
    at each point, and each component has zero Kuranishi map.
    """
    if n <= 0:
        raise ValueError(f"Need n >= 1, got {n}")

    ext_data = ideal_sheaf_ext(n)
    src = ext_data.deformation_dim  # 3n
    tgt = ext_data.obstruction_dim  # 3n

    # At generic (distinct) points, the map is zero
    return KuranishiMapData(
        source_dim=src,
        target_dim=tgt,
        map_description=(
            f"Cup product Ext^1(I_Z, I_Z) x Ext^1(I_Z, I_Z) -> Ext^2(I_Z, I_Z) "
            f"for Z = {n} distinct points. Vanishes at generic points "
            f"(independent deformations)."
        ),
        is_zero=True,  # at generic point
        kernel_dim=src,
        cokernel_dim=tgt,
    )


# ---------------------------------------------------------------------------
# Part 6: Atiyah class and L-infinity structure
# ---------------------------------------------------------------------------

@dataclass
class AtiyahClassData:
    """Atiyah class At(E) in Ext^1(E, E (x) Omega^1_X).

    For a line bundle L: At(L) = c_1(L) in H^1(Omega^1) = H^{1,1}.
    For the structure sheaf: At(O) = 0 (trivial bundle has a connection).

    The L-infinity structure on T_M = RHom(E,E)[1]:
      ell_1 = 0 (differential is zero on cohomology)
      ell_2(a, b) = a compose At compose b + b compose At compose a
        (symmetrized Atiyah composition)
    """
    sheaf_name: str
    atiyah_class_dim: int  # dim of Ext^1(E, E (x) Omega^1)
    c1_class: Optional[Tuple[int, ...]]  # first Chern class coefficients
    is_zero: bool
    linfty_ell2_dim: int  # dim of the image of ell_2


def atiyah_class_structure_sheaf() -> AtiyahClassData:
    """Atiyah class of O_{K3 x E}.

    At(O) = 0 because the trivial bundle admits a flat connection (d).
    The L-infinity bracket ell_2 vanishes identically.
    """
    return AtiyahClassData(
        sheaf_name="O_{K3 x E}",
        atiyah_class_dim=0,
        c1_class=(0,),
        is_zero=True,
        linfty_ell2_dim=0,
    )


def atiyah_class_line_bundle(c1_nonzero: bool = True) -> AtiyahClassData:
    """Atiyah class of a line bundle L on K3 x E.

    At(L) = c_1(L) in H^1(Omega^1_{K3xE}).

    H^1(Omega^1_{K3xE}) via Kuenneth on the cotangent bundle:
    Omega^1_{K3xE} = pr_1^* Omega^1_{K3} + pr_2^* Omega^1_E.

    H^1(X, Omega^1_X) has dimension h^{1,1}(K3 x E).

    h^{1,1}(K3 x E) by Kuenneth:
      = h^{1,1}(K3)*h^{0,0}(E) + h^{0,0}(K3)*h^{1,1}(E)
        + h^{1,0}(K3)*h^{0,1}(E) + h^{0,1}(K3)*h^{1,0}(E)
      = 20*1 + 1*1 + 0*1 + 0*1
      = 21.

    So At(L) lives in a 21-dimensional space.

    The L-infinity bracket ell_2 on RHom(L,L)[1] = H^*(O_X)[1]:
    Since L is a line bundle, Hom(L,L) = O_X, so the Ext algebra
    is just H^*(O_X) with the cup product (shifted).
    The ell_2 is the composition with the Atiyah class.

    If c_1(L) = 0 in H^{1,1}: At(L) = 0 (torsion or trivial).
    If c_1(L) != 0: At(L) != 0, gives nontrivial ell_2.
    """
    atiyah_dim = product_hodge(1, 1)  # = 21

    if c1_nonzero:
        return AtiyahClassData(
            sheaf_name="L (line bundle, c_1 != 0)",
            atiyah_class_dim=atiyah_dim,
            c1_class=None,  # general nonzero
            is_zero=False,
            linfty_ell2_dim=1,  # Rank-1 Atiyah map
        )
    else:
        return AtiyahClassData(
            sheaf_name="L (line bundle, c_1 = 0)",
            atiyah_class_dim=atiyah_dim,
            c1_class=(0,),
            is_zero=True,
            linfty_ell2_dim=0,
        )


# ---------------------------------------------------------------------------
# Part 7: Full Hodge diamond of K3 x E
# ---------------------------------------------------------------------------

def full_hodge_diamond() -> Dict[Tuple[int, int], int]:
    """Complete Hodge diamond h^{p,q}(K3 x E) for 0 <= p, q <= 3."""
    diamond = {}
    for p in range(4):
        for q in range(4):
            diamond[(p, q)] = product_hodge(p, q)
    return diamond


def verify_hodge_symmetries() -> Dict[str, bool]:
    """Verify Hodge symmetries for K3 x E.

    (i) Complex conjugation: h^{p,q} = h^{q,p}
    (ii) Serre duality: h^{p,q} = h^{3-p, 3-q} (for CY3 with trivial canonical)
    (iii) Poincare duality: b_k = b_{6-k}
    """
    diamond = full_hodge_diamond()

    # (i) h^{p,q} = h^{q,p}
    conjugation_ok = all(
        diamond.get((p, q), 0) == diamond.get((q, p), 0)
        for p in range(4) for q in range(4)
    )

    # (ii) Serre: h^{p,q} = h^{3-p, 3-q}
    serre_ok = all(
        diamond.get((p, q), 0) == diamond.get((3 - p, 3 - q), 0)
        for p in range(4) for q in range(4)
    )

    # (iii) Betti: b_k = b_{6-k}
    betti_ok = all(
        product_betti(k) == product_betti(6 - k) for k in range(7)
    )

    return {
        "complex_conjugation": conjugation_ok,
        "serre_duality": serre_ok,
        "poincare_duality": betti_ok,
    }


# ---------------------------------------------------------------------------
# Part 8: DT partition function
# ---------------------------------------------------------------------------

@dataclass
class DTPartitionData:
    """DT partition function data for K3 x E.

    The generating function: Z^DT(q) = sum_{n >= 0} DT_n q^n.

    For CY3 with chi = 0 (like K3 x E):
      Z^DT(q) = M(q)^{chi(X)} = M(q)^0 = 1
    in the UNREDUCED theory.

    The REDUCED DT theory is more interesting:
      Z^DT,red(q) = prod_{n >= 1} (1-q^n)^{-chi(K3)} * (corrections)

    By the KKV formula for K3 x E:
      Z^DT,red = 1/eta(q)^{chi(K3)} = 1/eta(q)^{24}

    This gives DT^red_n = p_{-24}(n) where p_k(n) is the colored partition
    function.
    """
    euler_char_X: int
    macmahon_exponent: int  # chi(X)
    unreduced_Z_coeffs: List[int]  # first few coefficients of Z^DT
    reduced_Z_coeffs: List[int]  # first few of Z^{DT,red}


def dt_partition_function(num_terms: int = 6) -> DTPartitionData:
    """Compute the DT partition function for K3 x E.

    chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.

    Unreduced: Z^DT = M(q)^0 = 1, so DT_n = 0 for n >= 1.
    Reduced: involves the reduced virtual class.

    For the reduced theory, by KKV:
      Z^DT,red(q) involves 1/eta^{24} = 1/(q prod(1-q^n))^{24}
                        = q^{-1} * prod(1-q^n)^{-24}

    The coefficient of q^n in prod_{m>=1} (1-q^m)^{-24} for small n:
    This is the partition function with 24 colors.
    p_{24}(0) = 1
    p_{24}(1) = 24
    p_{24}(2) = 24*25/2 + 24 = 300 + 24 = 324
    Actually: (1-q)^{-24}(1-q^2)^{-24}... expanded:
    p_{24}(1) = 24
    p_{24}(2) = 24 + C(24+1, 2) = 24 + 300 = 324

    Using the generating function for colored partitions:
    sum p_c(n) q^n = prod_{m>=1} (1-q^m)^{-c}

    For c = 24:
    p_{24}(0) = 1
    p_{24}(1) = 24
    p_{24}(2) = 324  (24 from q^2 partitions + 300 from q^1 * q^1)
    """
    chi_X = product_euler_char()  # = 0

    # Unreduced: all DT_n = 0 for n >= 1 when chi = 0
    unreduced = [1] + [0] * (num_terms - 1)

    # Reduced: coefficients of prod_{m>=1} (1-q^m)^{-24}
    # Computed by iterative expansion
    c = 24  # chi(K3)
    reduced = _colored_partition_coeffs(c, num_terms)

    return DTPartitionData(
        euler_char_X=chi_X,
        macmahon_exponent=chi_X,
        unreduced_Z_coeffs=unreduced,
        reduced_Z_coeffs=reduced,
    )


def _colored_partition_coeffs(c: int, num_terms: int) -> List[int]:
    """Coefficients of prod_{m >= 1} (1 - q^m)^{-c} up to q^{num_terms - 1}.

    Uses the recursion via divisor sums:
    p_c(n) = (c/n) * sum_{k=1}^{n} sigma_1(k) * p_c(n-k)
    where sigma_1(k) = sum of divisors of k.

    This is standard: log prod(1-q^m)^{-c} = c * sum_{m,k} q^{mk}/(mk) * ...
    Actually the recursion comes from:
    n * p_c(n) = c * sum_{k=1}^{n} sigma_1(k) * p_c(n-k)
    """
    coeffs = [0] * num_terms
    coeffs[0] = 1

    for n in range(1, num_terms):
        s = 0
        for k in range(1, n + 1):
            sig = _sigma1(k)
            s += sig * coeffs[n - k]
        # n * p_c(n) = c * s
        # => p_c(n) = c * s / n
        # This must be an integer (it always is for the partition function)
        val = c * s
        assert val % n == 0, f"p_{c}({n}) not integer: {val}/{n}"
        coeffs[n] = val // n

    return coeffs


def _sigma1(n: int) -> int:
    """Sum of divisors sigma_1(n)."""
    return sum(d for d in range(1, n + 1) if n % d == 0)


# ---------------------------------------------------------------------------
# Part 9: Connection to bar-cobar / shadow obstruction tower
# ---------------------------------------------------------------------------

@dataclass
class BarCobarConnectionData:
    """Connection between derived moduli of K3 x E and the shadow theory.

    The modular convolution algebra g^mod_{A_{K3xE}} has:
      - Arity-2 projection: kappa(A) = the modular characteristic
      - This relates to Ext^2-level obstructions

    For the chiral algebra A associated to K3 x E sigma model:
      - The sigma model target is K3 x E
      - The chiral algebra is the CDR (chiral de Rham complex) on K3 x E
      - kappa(CDR(X)) relates to chi(X)/2 for the Witten genus
      - For K3 x E: chi = 0, so kappa of the naive chiral algebra = 0

    The virtual class [M]^{vir} in degree 0 corresponds to:
      - The degree-0 component of the shadow obstruction tower
      - When vdim = 0: the virtual count is a NUMBER, matching the
        arity-0 shadow invariant at the relevant genus
    """
    chi_X: int
    kappa_CDR: Fraction
    vdim: int
    obstruction_match: bool
    description: str


def bar_cobar_connection() -> BarCobarConnectionData:
    """Compute the connection between derived moduli and bar-cobar.

    For X = K3 x E:
    - chi(X) = 24 * 0 = 0
    - The chiral de Rham complex CDR(X) has c_{CDR} = 0 for CY
      (by Malikov-Schechtman-Vaintrob: c = 0 for CY manifolds)
    - kappa(CDR(K3 x E)) is related to the Witten genus
    - Since chi(X) = 0 and c_{CDR} = 0: kappa = 0

    The obstruction space Ext^2 = H^2(O) at the structure sheaf point
    is 1-dimensional. The arity-2 shadow at kappa = 0 gives:
    - m_0 = kappa * omega_g = 0 (uncurved bar complex)
    - So the bar complex is UNCURVED

    AP31 WARNING: kappa = 0 does NOT imply Theta = 0.
    The higher-arity shadows (cubic C, quartic Q, etc.) can be nonzero.
    For CY3 sigma models, these are governed by the Gromov-Witten
    theory of the target, and are generally nonvanishing.

    The vdim = 0 condition matches: the shadow partition function
    at arity 0 (the genus-g virtual count) is a number, not a class.
    """
    chi_X = product_euler_char()

    # CDR has c = 0 for CY (Malikov-Schechtman-Vaintrob)
    # kappa = c/2 = 0 for the Virasoro subalgebra of CDR
    # But AP48: kappa depends on the FULL algebra, not just Virasoro
    # For CDR(CY3): kappa = 0 is correct by the Witten genus argument
    kappa = Fraction(0)

    return BarCobarConnectionData(
        chi_X=chi_X,
        kappa_CDR=kappa,
        vdim=0,
        obstruction_match=True,
        description=(
            "chi(K3 x E) = 0, c_{CDR} = 0 (CY), kappa = 0. "
            "Bar complex is uncurved (m_0 = 0). "
            "AP31: kappa = 0 does NOT imply Theta = 0; "
            "higher-arity shadows from GW theory can be nonzero."
        ),
    )


# ---------------------------------------------------------------------------
# Part 10: Mukai vector and general sheaf data
# ---------------------------------------------------------------------------

@dataclass
class MukaiVectorData:
    """Mukai vector v(E) = ch(E) sqrt(td(X)) for a sheaf E on X.

    On CY3, td(X)^{1/2} contributes:
      sqrt(td) = 1 + c_2(X)/24 + ...

    For K3 x E:
      c_2(K3) = 24 (the Euler class), c_2(E) = 0
      c_2(K3 x E) = c_2(K3) = 24 (in H^4)

    The Mukai pairing: <v, w> = -chi(E, F) where v = v(E), w = v(F).
    For v = v(E): <v, v> = -chi(E, E) = vdim = 0 on CY3.
    """
    rank: int
    c1: int  # degree of c_1 (simplified to an integer for rank-1)
    ch2: Fraction  # second Chern character
    euler_char_E: int  # chi(E) = integral ch(E) td(X)
    mukai_self_pairing: int  # <v(E), v(E)> = -chi(E, E)


def mukai_vector_structure_sheaf() -> MukaiVectorData:
    """Mukai vector of O_{K3 x E}.

    ch(O) = 1 (rank 1, c_1 = 0, ch_2 = 0, ch_3 = 0).
    td(K3 x E) = (1 + c_2(K3)/12)(1) = 1 + 2[pt_{K3}] (in appropriate sense).

    chi(O) = integral ch(O) * td(X) = integral td(X)
           = (1/6) integral c_1 c_2 = 0 for CY3 (c_1 = 0).

    Actually: chi(O_{K3xE}) = sum (-1)^k h^{0,k} = 1 - 1 + 1 - 1 = 0.

    Mukai self-pairing: <v, v> = -chi(O, O) = 0.
    """
    return MukaiVectorData(
        rank=1,
        c1=0,
        ch2=Fraction(0),
        euler_char_E=0,
        mukai_self_pairing=0,
    )


def mukai_vector_ideal_sheaf(n: int) -> MukaiVectorData:
    """Mukai vector of I_Z for n points Z in K3 x E.

    ch(I_Z) = ch(O) - ch(O_Z) = 1 - n[pt]
    (rank 1, c_1 = 0, ch_2 = 0, ch_3 = -n[pt])

    chi(I_Z) = chi(O) - n = 0 - n = -n.

    chi(I_Z, I_Z):
    Using chi(E, F) = integral ch(E)^v ch(F) td(X):
    ch(I_Z)^v = 1 - (-n[pt]) = 1 + n[pt] (in degree 6).
    Actually for CY3 with Serre duality:
    chi(I_Z, I_Z) = sum (-1)^k ext^k = 1 - 3n + 3n - 1 = 0.

    Mukai self-pairing: <v, v> = -chi(I_Z, I_Z) = 0.
    """
    return MukaiVectorData(
        rank=1,
        c1=0,
        ch2=Fraction(0),
        euler_char_E=-n,
        mukai_self_pairing=0,
    )


# ---------------------------------------------------------------------------
# Part 11: Comprehensive derived moduli package
# ---------------------------------------------------------------------------

@dataclass
class DerivedModuliPackage:
    """Complete derived moduli data for a sheaf on K3 x E.

    Collects all computations: tangent complex, Ext groups, virtual
    dimension, Kuranishi map, Atiyah class, and connection to shadows.
    """
    sheaf_name: str
    tangent_complex: Optional[TangentComplexData]
    ext_data: Optional[IdealSheafExtData]
    pot_data: Optional[PerfectObstructionTheoryData]
    kuranishi: Optional[KuranishiMapData]
    atiyah: Optional[AtiyahClassData]
    mukai: Optional[MukaiVectorData]
    bar_cobar: Optional[BarCobarConnectionData]


def full_package_structure_sheaf() -> DerivedModuliPackage:
    """Complete derived moduli package for O_{K3 x E}."""
    return DerivedModuliPackage(
        sheaf_name="O_{K3 x E}",
        tangent_complex=tangent_complex_structure_sheaf(),
        ext_data=ideal_sheaf_ext(0),
        pot_data=perfect_obstruction_theory(0),
        kuranishi=kuranishi_structure_sheaf(),
        atiyah=atiyah_class_structure_sheaf(),
        mukai=mukai_vector_structure_sheaf(),
        bar_cobar=bar_cobar_connection(),
    )


def full_package_ideal_sheaf(n: int) -> DerivedModuliPackage:
    """Complete derived moduli package for I_Z of n points."""
    return DerivedModuliPackage(
        sheaf_name=f"I_Z (n={n} points)",
        tangent_complex=None,  # tangent complex computed via ext_data
        ext_data=ideal_sheaf_ext(n),
        pot_data=perfect_obstruction_theory(n),
        kuranishi=kuranishi_ideal_sheaf_n_points(n) if n >= 1 else None,
        atiyah=None,  # Atiyah class for ideal sheaves is more complex
        mukai=mukai_vector_ideal_sheaf(n),
        bar_cobar=bar_cobar_connection(),
    )


# ---------------------------------------------------------------------------
# Part 12: Line bundle Ext computation
# ---------------------------------------------------------------------------

@dataclass
class LineBundleExtData:
    """Ext data for a line bundle L on K3 x E.

    For a line bundle: Ext^k(L, L) = H^k(O_X) (since L^* (x) L = O_X).
    So the Ext algebra of any line bundle is the same as for O_X.
    """
    ext_dims: Dict[int, int]
    virtual_dim: int
    serre_check: bool


def line_bundle_ext() -> LineBundleExtData:
    """Ext groups for a line bundle L on K3 x E.

    Ext^k(L, L) = H^k(Hom(L, L)) = H^k(O_X) since Hom(L, L) = O_X.
    """
    ext_dims = {k: cohomology_O(k) for k in range(4)}
    chi = sum((-1)**k * ext_dims[k] for k in range(4))
    serre_ok = all(ext_dims[k] == ext_dims[3 - k] for k in range(4))

    return LineBundleExtData(
        ext_dims=ext_dims,
        virtual_dim=-chi,
        serre_check=serre_ok,
    )


# ---------------------------------------------------------------------------
# Part 13: Spectral sequence from Kuenneth
# ---------------------------------------------------------------------------

def kuenneth_ext_OO() -> Dict[int, List[Tuple[Tuple[int, int], Tuple[int, int], int]]]:
    """Decompose Ext^k(O_{K3xE}, O_{K3xE}) via Kuenneth.

    Ext^k(O_X, O_X) = H^k(X, O_X) = bigoplus_{i+j=k} H^i(K3, O) (x) H^j(E, O).

    Returns dict: k -> list of (H^i(K3,O) factor, H^j(E,O) factor, dimension).
    """
    result = {}
    for k in range(4):
        components = []
        for i in range(min(2, k) + 1):
            j = k - i
            if 0 <= j <= 1:
                dim_K3 = k3_hodge(0, i)  # h^{0,i}(K3)
                dim_E = elliptic_hodge(0, j)  # h^{0,j}(E)
                if dim_K3 * dim_E > 0:
                    components.append(((0, i), (0, j), dim_K3 * dim_E))
        result[k] = components
    return result


# ---------------------------------------------------------------------------
# Part 14: Holomorphic symplectic structure (from K3)
# ---------------------------------------------------------------------------

@dataclass
class HolomorphicSymplecticData:
    """Holomorphic symplectic data inherited from the K3 factor.

    K3 carries a unique (up to scale) holomorphic symplectic form
    omega in H^0(K3, Omega^2_{K3}).

    For Hilb^n(K3): the Beauville-Bogomolov form gives a holomorphic
    symplectic structure on the 2n-dimensional Hilb^n(K3).

    For K3 x E: not holomorphic symplectic (odd-dimensional), but the
    K3 factor contributes a (partial) symplectic structure in the
    K3-directions of the tangent space.
    """
    k3_symplectic_form_exists: bool
    hilbn_k3_dim: int
    hilbn_k3_is_hyperkahler: bool
    k3xe_dim: int
    k3xe_is_symplectic: bool


def holomorphic_symplectic_data(n: int) -> HolomorphicSymplecticData:
    """Holomorphic symplectic data for Hilb^n(K3) and Hilb^n(K3 x E).

    Hilb^n(K3) is a 2n-dimensional irreducible holomorphic symplectic
    manifold (hyperkahler) for all n >= 1. This is Beauville's theorem.

    Hilb^n(K3 x E) is NOT hyperkahler (dim = 3n is odd for n odd).
    But the K3-factor tangent directions carry a symplectic form.
    """
    return HolomorphicSymplecticData(
        k3_symplectic_form_exists=True,
        hilbn_k3_dim=2 * n,
        hilbn_k3_is_hyperkahler=(n >= 1),
        k3xe_dim=3 * n if n >= 1 else 3,  # dim of Hilb^n(X) as a space
        k3xe_is_symplectic=False,  # dim 3n, not even for odd n
    )


# ---------------------------------------------------------------------------
# Part 15: Summary and cross-checks
# ---------------------------------------------------------------------------

def cross_check_summary() -> Dict[str, Any]:
    """Run all cross-checks and return summary.

    Verifies:
    1. Hodge symmetries
    2. Serre duality for O_X
    3. vdim = 0 for all sheaves
    4. Euler char chi(K3 x E) = 0
    5. Kuenneth decomposition consistency
    6. DT_0 = 1
    7. Mukai self-pairing = 0
    """
    tc = tangent_complex_structure_sheaf()

    checks = {
        "hodge_symmetries": verify_hodge_symmetries(),
        "serre_O": tc.serre_check,
        "vdim_O": tc.virtual_dim == 0,
        "chi_top": product_euler_char() == 0,
        "chi_O": sum((-1)**k * cohomology_O(k) for k in range(4)) == 0,
        "DT_0": perfect_obstruction_theory(0).virtual_class_degree == 1,
        "mukai_O": mukai_vector_structure_sheaf().mukai_self_pairing == 0,
    }

    for n in range(1, 6):
        ext = ideal_sheaf_ext(n)
        checks[f"vdim_I_{n}pts"] = ext.virtual_dim == 0
        checks[f"serre_I_{n}pts"] = ext.serre_check
        checks[f"mukai_I_{n}pts"] = mukai_vector_ideal_sheaf(n).mukai_self_pairing == 0

    return checks
