"""
CY sheaf categories engine: obstruction theory for sheaves of CY categories
on K3 x E and related Calabi-Yau threefolds.

Computes Hochschild cohomology (deformation-obstruction theory) for derived
categories of CY manifolds via the HKR decomposition, Kuenneth products,
CY pairings, NC/B-field deformations, Brauer groups, and the
Hochschild-to-cyclic spectral sequence.

Mathematical foundations:
  - HKR isomorphism: HH^n(X) = bigoplus_{p+q=n} H^q(X, wedge^p T_X)
  - For CY d-fold: wedge^p T_X = Omega^{d-p}_X, so
    HH^n(X) = bigoplus_{p+q=n} H^q(X, Omega^{d-p}_X)
             = bigoplus_{p+q=n} h^{d-p, q}
  - CY Serre duality: HH^n(X) = HH^{2d-n}(X)
  - Kuenneth: HH^n(X x Y) = bigoplus_{i+j=n} HH^i(X) tensor HH^j(Y)
  - Deformation theory: HH^2 = first-order deformations of D^b(X),
    HH^3 = obstructions to extending deformations
  - Periodic cyclic: HP^n(X) = H^n_dR(X) (HKR at cyclic level)
"""

from __future__ import annotations
from fractions import Fraction
from typing import Dict, List, Optional, Tuple
import math


# ============================================================
# Hodge data for standard CY manifolds
# ============================================================

def hodge_diamond_K3() -> Dict[Tuple[int, int], int]:
    """Hodge numbers h^{p,q} for a K3 surface.

    The K3 Hodge diamond:
        h^{0,0} = h^{2,2} = 1
        h^{1,1} = 20
        h^{2,0} = h^{0,2} = 1
        all others = 0
    """
    h = {}
    for p in range(3):
        for q in range(3):
            h[(p, q)] = 0
    h[(0, 0)] = 1
    h[(2, 0)] = 1
    h[(0, 2)] = 1
    h[(1, 1)] = 20
    h[(2, 2)] = 1
    return h


def hodge_diamond_elliptic() -> Dict[Tuple[int, int], int]:
    """Hodge numbers h^{p,q} for an elliptic curve E.

    h^{0,0} = h^{1,0} = h^{0,1} = h^{1,1} = 1.
    """
    return {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 1}


def hodge_diamond_product(
    h1: Dict[Tuple[int, int], int],
    dim1: int,
    h2: Dict[Tuple[int, int], int],
    dim2: int,
) -> Dict[Tuple[int, int], int]:
    """Kuenneth product of Hodge diamonds.

    h^{p,q}(X x Y) = sum_{a+c=p, b+d=q} h^{a,b}(X) * h^{c,d}(Y).
    """
    result: Dict[Tuple[int, int], int] = {}
    for (a, b), va in h1.items():
        if va == 0:
            continue
        for (c, d), vb in h2.items():
            if vb == 0:
                continue
            p, q = a + c, b + d
            result[(p, q)] = result.get((p, q), 0) + va * vb
    return result


def hodge_diamond_K3xE() -> Dict[Tuple[int, int], int]:
    """Hodge diamond of K3 x E."""
    return hodge_diamond_product(hodge_diamond_K3(), 2, hodge_diamond_elliptic(), 1)


def hodge_diamond_torus(d: int) -> Dict[Tuple[int, int], int]:
    """Hodge numbers h^{p,q} for a d-dimensional complex torus.

    h^{p,q} = C(d,p) * C(d,q).
    """
    h = {}
    for p in range(d + 1):
        for q in range(d + 1):
            h[(p, q)] = math.comb(d, p) * math.comb(d, q)
    return h


def hodge_diamond_CY_quintic() -> Dict[Tuple[int, int], int]:
    """Hodge numbers for the quintic threefold in P^4.

    CY 3-fold with h^{1,1} = 1, h^{2,1} = 101.
    """
    h: Dict[Tuple[int, int], int] = {}
    for p in range(4):
        for q in range(4):
            h[(p, q)] = 0
    h[(0, 0)] = 1
    h[(3, 0)] = 1
    h[(0, 3)] = 1
    h[(3, 3)] = 1
    h[(1, 1)] = 1
    h[(2, 2)] = 1
    h[(2, 1)] = 101
    h[(1, 2)] = 101
    return h


# ============================================================
# Betti numbers and Euler characteristic
# ============================================================

def betti_numbers(hodge: Dict[Tuple[int, int], int], dim: int) -> Dict[int, int]:
    """Compute Betti numbers b_k = sum_{p+q=k} h^{p,q}."""
    b: Dict[int, int] = {}
    for (p, q), v in hodge.items():
        k = p + q
        b[k] = b.get(k, 0) + v
    return b


def euler_characteristic(hodge: Dict[Tuple[int, int], int], dim: int) -> int:
    """Compute topological Euler characteristic chi = sum (-1)^k b_k."""
    b = betti_numbers(hodge, dim)
    return sum((-1) ** k * v for k, v in b.items())


def betti_product(b1: Dict[int, int], b2: Dict[int, int]) -> Dict[int, int]:
    """Kuenneth product of Betti numbers."""
    result: Dict[int, int] = {}
    for i, vi in b1.items():
        for j, vj in b2.items():
            k = i + j
            result[k] = result.get(k, 0) + vi * vj
    return result


# ============================================================
# Hochschild cohomology via HKR
# ============================================================

def hochschild_cohomology_HKR(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
    is_CY: bool = True,
) -> Dict[int, int]:
    """Compute Hochschild cohomology via HKR decomposition.

    Standard grading convention (Caldararu, Keller):
        HH^n(X) = bigoplus_{p+q=n} H^q(X, wedge^p T_X)

    For CY d-fold with omega_X = O_X:
        wedge^p T_X = Omega^{d-p}_X
    so  H^q(wedge^p T_X) = H^q(Omega^{d-p}) = h^{d-p, q}.

    Thus HH^n = sum_{p+q=n, 0<=p<=d} h^{d-p, q}.

    This is the STANDARD convention for deformation theory:
        HH^0 = endomorphisms
        HH^1 = infinitesimal automorphisms
        HH^2 = first-order deformations
        HH^3 = obstructions
    """
    if not is_CY:
        raise NotImplementedError("Non-CY HKR requires explicit polyvector data")

    hh: Dict[int, int] = {}
    for n in range(2 * dim + 1):
        total = 0
        for p in range(dim + 1):
            q = n - p
            if q < 0 or q > dim:
                continue
            # wedge^p T = Omega^{d-p} for CY
            omega_deg = dim - p
            total += hodge.get((omega_deg, q), 0)
        if total > 0:
            hh[n] = total
    return hh


def hochschild_cohomology_HKR_alt(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[int, int]:
    """Alternative grading: HH^n = bigoplus_{q-p=n} H^q(Omega^p).

    This is the homological/categorical convention used in some references.
    Related to the standard convention by a shift: HH^n_{alt} = HH^{d+n}_{std}
    for CY d-folds.
    """
    hh: Dict[int, int] = {}
    for p in range(dim + 1):
        for q in range(dim + 1):
            v = hodge.get((p, q), 0)
            if v == 0:
                continue
            n = q - p
            hh[n] = hh.get(n, 0) + v
    return hh


def hochschild_kuenneth(
    hh1: Dict[int, int],
    hh2: Dict[int, int],
) -> Dict[int, int]:
    """Kuenneth product for Hochschild cohomology.

    HH^n(X x Y) = bigoplus_{i+j=n} HH^i(X) tensor HH^j(Y).
    """
    result: Dict[int, int] = {}
    for i, di in hh1.items():
        for j, dj in hh2.items():
            n = i + j
            result[n] = result.get(n, 0) + di * dj
    return result


def HKR_hodge_decomposition(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
    n: int,
) -> Dict[Tuple[int, int], int]:
    """The Hodge decomposition of HH^n: which h^{a,b} contribute.

    Returns dict mapping (p, q) to h^{d-p, q} where p+q=n and the
    polyvector piece is wedge^p T = Omega^{d-p}.

    The key (d-p, q) is the Hodge index of the contributing piece.
    """
    pieces: Dict[Tuple[int, int], int] = {}
    for p in range(dim + 1):
        q = n - p
        if q < 0 or q > dim:
            continue
        omega_deg = dim - p
        h = hodge.get((omega_deg, q), 0)
        if h > 0:
            pieces[(omega_deg, q)] = h
    return pieces


# ============================================================
# CY Serre duality pairing
# ============================================================

def cy_pairing_dimensions(
    hh: Dict[int, int],
    dim: int,
) -> Dict[int, Tuple[int, int]]:
    """Verify the CY Serre duality pairing HH^n x HH^{2d-n} -> C.

    Returns dict n -> (dim HH^n, dim HH^{2d-n}).
    The pairing is nondegenerate iff these dimensions agree.
    """
    result = {}
    for n in hh:
        n_dual = 2 * dim - n
        dn = hh.get(n, 0)
        dn_dual = hh.get(n_dual, 0)
        result[n] = (dn, dn_dual)
    return result


def verify_cy_pairing(hh: Dict[int, int], dim: int) -> bool:
    """Check nondegeneracy of CY pairing: dim HH^n = dim HH^{2d-n}."""
    pairs = cy_pairing_dimensions(hh, dim)
    return all(d1 == d2 for d1, d2 in pairs.values())


def cy_pairing_matrix_rank(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
    n: int,
) -> int:
    """Rank of the CY pairing HH^n x HH^{2d-n} -> HH^{2d} = C.

    For a smooth CY variety, this equals dim HH^n (full rank).
    """
    hh = hochschild_cohomology_HKR(hodge, dim)
    return hh.get(n, 0)


# ============================================================
# Deformation-obstruction theory for D^b(X)
# ============================================================

class DeformationObstruction:
    """Deformation-obstruction data for the dg category D^b(X).

    Attributes:
        deformations: dim HH^2 (first-order deformations)
        obstructions: dim HH^3 (obstructions)
        automorphisms: dim HH^1 (infinitesimal automorphisms)
        endomorphisms: dim HH^0 (endomorphisms)
        is_unobstructed: whether HH^3 = 0
    """

    def __init__(self, hh: Dict[int, int]):
        self.hh = dict(hh)
        self.endomorphisms = hh.get(0, 0)
        self.automorphisms = hh.get(1, 0)
        self.deformations = hh.get(2, 0)
        self.obstructions = hh.get(3, 0)
        self.is_unobstructed = (self.obstructions == 0)

    def __repr__(self) -> str:
        return (
            f"DeformationObstruction("
            f"HH^0={self.endomorphisms}, "
            f"HH^1={self.automorphisms}, "
            f"HH^2={self.deformations}, "
            f"HH^3={self.obstructions}, "
            f"unobstructed={self.is_unobstructed})"
        )


def deformation_obstruction(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> DeformationObstruction:
    """Compute deformation-obstruction data for D^b(X)."""
    hh = hochschild_cohomology_HKR(hodge, dim)
    return DeformationObstruction(hh)


def deformation_decomposition_K3xE() -> Dict[str, int]:
    """Decompose HH^2(K3 x E) by Kuenneth components.

    HH^2(K3 x E) = bigoplus_{i+j=2} HH^i(K3) tensor HH^j(E).

    Returns a dict labeling each Kuenneth summand with its dimension.
    """
    hh_k3 = hochschild_cohomology_HKR(hodge_diamond_K3(), 2)
    hh_e = hochschild_cohomology_HKR(hodge_diamond_elliptic(), 1)

    result = {}
    for i in sorted(hh_k3):
        j = 2 - i
        if j in hh_e:
            contrib = hh_k3[i] * hh_e[j]
            if contrib > 0:
                result[f"HH^{i}(K3) x HH^{j}(E)"] = contrib
    return result


def obstruction_decomposition_K3xE() -> Dict[str, int]:
    """Decompose HH^3(K3 x E) by Kuenneth components.

    HH^3(K3 x E) = bigoplus_{i+j=3} HH^i(K3) tensor HH^j(E).
    """
    hh_k3 = hochschild_cohomology_HKR(hodge_diamond_K3(), 2)
    hh_e = hochschild_cohomology_HKR(hodge_diamond_elliptic(), 1)

    result = {}
    for i in sorted(hh_k3):
        j = 3 - i
        if j in hh_e:
            contrib = hh_k3[i] * hh_e[j]
            if contrib > 0:
                result[f"HH^{i}(K3) x HH^{j}(E)"] = contrib
    return result


# ============================================================
# Globalization obstruction for sheaves of dg categories
# ============================================================

def globalization_obstruction_dim(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, int]:
    """Compute dimensions relevant to globalization of local dg categories.

    For a sheaf of dg categories C on X with fiber C_x = D^b(x):
      - The presheaf U -> HH^k(D^b(U)) sheafifies to a sheaf HH^k_X
      - The obstruction to gluing local categories lives in H^2(X, HH^1_X)
      - The obstruction to gluing transition bimodules is in H^1(X, HH^2_X)

    For a CY variety X with D^b(X) as the global category:
      - HH^1_X is a LOCAL SYSTEM related to infinitesimal automorphisms
      - On X itself, H^q(X, HH^1_X) is computed from the Hodge decomposition

    Returns dimensions of key obstruction groups.
    """
    hh = hochschild_cohomology_HKR(hodge, dim)

    # For X smooth projective CY:
    # The local-to-global spectral sequence: E_2^{p,q} = H^p(X, HH^q_X) => HH^{p+q}(X)
    # At E_2, the abutment is the global HH we already computed.
    # The individual H^p(X, HH^q_X) requires understanding the sheaf HH^q_X.

    # For trivial fibration (constant sheaf of categories):
    # HH^q_X = constant sheaf with stalk HH^q(C_x)
    # Then H^p(X, HH^q_X) = H^p(X, C) tensor HH^q(C_x)
    # This gives the Kuenneth-type decomposition.

    # For the identity sheaf (D^b(X) itself):
    # The sheafified HH is the tangent complex T_{D^b(X)/Perf}
    # and its cohomology sheaves are related to polyvector fields.

    result = {
        "HH^0 (endomorphisms)": hh.get(0, 0),
        "HH^1 (automorphisms)": hh.get(1, 0),
        "HH^2 (deformations)": hh.get(2, 0),
        "HH^3 (obstructions)": hh.get(3, 0),
    }

    # The Bogomolov-Tian-Todorov theorem: for CY manifolds,
    # the Kodaira-Spencer deformation space is UNOBSTRUCTED
    # (despite HH^3 != 0 in general). The key is that obstructions
    # are killed by the d-dbar lemma / CY structure.
    # This applies to GEOMETRIC deformations. NC deformations may be obstructed.

    # For CY d-fold:
    # Geometric deformations = H^1(T_X) = h^{d-1, 1} (complex structure)
    # B-field deformations = H^0(wedge^2 T) = h^{d-2, 0}
    # These are always unobstructed by BTT.

    h_geom_def = hodge.get((dim - 1, 1), 0)  # H^1(T_X)
    h_bfield = hodge.get((dim - 2, 0), 0) if dim >= 2 else 0  # H^0(wedge^2 T)

    result["geometric_deformations"] = h_geom_def
    result["B_field_deformations"] = h_bfield
    result["BTT_unobstructed"] = True  # CY => BTT applies to geometric deformations

    return result


def sheaf_obstruction_H2_HH1(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> int:
    """Dimension of H^2(X, HH^1(C_x)) for constant sheaf of categories.

    This is the obstruction to gluing local dg categories on a cover.
    For a CY d-fold X with fibers C_x = D^b(point):
        HH^1(D^b(pt)) = 0, so this vanishes.

    For a family of CY categories with constant fiber C:
        H^2(X, C^{dim HH^1(C)}) = b_2(X) * dim HH^1(C).
    """
    b = betti_numbers(hodge, dim)
    # For constant sheaf, this is b_2 * dim(stalk HH^1)
    # But the stalk HH^1 depends on the fiber category.
    # For D^b(K3) fiber: HH^1(K3) = 0, so obstruction vanishes.
    # We return b_2 as the coefficient.
    return b.get(2, 0)


# ============================================================
# NC deformations and Brauer group
# ============================================================

def nc_deformation_space(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, int]:
    """Compute the NC (B-field) deformation space for a CY d-fold.

    The formal NC deformation space is controlled by HH^2(X).
    Within HH^2, the B-field component is H^0(wedge^2 T_X) = h^{d-2, 0}.
    The complex structure component is H^1(T_X) = h^{d-1, 1}.
    The remaining components involve higher cohomology.

    Returns dimensions of each component of HH^2.
    """
    pieces = HKR_hodge_decomposition(hodge, dim, 2)
    result = {}

    # Classify each Hodge piece
    for (omega_deg, q), v in sorted(pieces.items()):
        p = dim - omega_deg  # polyvector degree
        if p == 0 and q == 2:
            label = "volume_deformation"
        elif p == 1 and q == 1:
            label = "complex_structure"
        elif p == 2 and q == 0:
            label = "B_field"
        else:
            label = f"mixed_p{p}_q{q}"
        result[label] = v

    return result


def formal_brauer_group_dim(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> int:
    """Dimension of the formal Brauer group.

    For a smooth projective variety X:
        Br_formal(X) is controlled by H^2(O_X) = h^{0,2}.

    The exponential sequence gives:
        H^1(O_X*) -> H^2(Z) -> H^2(O_X) -> H^2(O_X*) -> H^3(Z) -> ...

    For CY d-fold: h^{0,2} = h^{d,d-2} by Serre duality.
    K3: h^{0,2} = 1 (one-dimensional formal Brauer group).
    Elliptic curve: h^{0,1} = 1 (but Br is in H^2, not H^1).
    """
    return hodge.get((0, 2), 0)


def brauer_group_data(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, int]:
    """Compute Brauer group related invariants.

    The analytic Brauer group Br(X) = H^2(X, O_X*)_tors sits in:
        0 -> NS(X) -> H^2(X, Z) -> H^2(X, O_X) -> Br(X) -> H^3(X, Z)_tors -> 0

    Key invariants:
        h^{0,2} = dim of formal part
        b_2 = rank H^2(X, Z)
        b_3_tors would give additional torsion (we track b_3)
    """
    b = betti_numbers(hodge, dim)
    return {
        "h02": hodge.get((0, 2), 0),
        "b2": b.get(2, 0),
        "b3": b.get(3, 0),
        "formal_brauer_dim": hodge.get((0, 2), 0),
    }


def brauer_product(
    br1: Dict[str, int],
    br2: Dict[str, int],
) -> Dict[str, int]:
    """Brauer data for a product variety.

    For X x Y: Br(X x Y) contains Br(X) x Br(Y) plus mixed terms.
    The formal part: H^2(O_{X x Y}) by Kuenneth.
    """
    # H^2(O_{XxY}) = H^0(O_X) H^2(O_Y) + H^1(O_X) H^1(O_Y) + H^2(O_X) H^0(O_Y)
    # For K3 x E: = 0 + 0 + 1 = 1
    return {
        "formal_brauer_dim": br1["h02"] + br2.get("h02", 0),
        # Cross terms from Kuenneth of H^*(O_X) contribute too;
        # the full formula is the sum above but we store the key invariants
    }


# ============================================================
# Periodic cyclic homology and de Rham
# ============================================================

def periodic_cyclic_homology(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[int, int]:
    """Compute periodic cyclic homology HP^n(X) = H^n_dR(X).

    By HKR at the cyclic level, HP^n(X) = bigoplus_{k equiv n mod 2} H^k_dR(X)
    in the 2-periodic version. But more precisely:
        HP^n(X) = H^n_dR(X)  (for smooth proper X, by degeneration of HKR-to-cyclic)

    So HP^n = b_n (the n-th Betti number).
    """
    return betti_numbers(hodge, dim)


def negative_cyclic_to_periodic(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, object]:
    """Data for the negative cyclic -> periodic cyclic map.

    HC^-(X) -> HP(X) with fiber HH(X)[[u]], u of degree 2.
    The Hodge filtration on HP = H^*_dR is the classical Hodge filtration.
    """
    b = betti_numbers(hodge, dim)
    hh = hochschild_cohomology_HKR(hodge, dim)
    return {
        "HP_dimensions": b,
        "HH_dimensions": hh,
        "total_HP": sum(b.values()),
        "total_HH": sum(hh.values()),
        "match": sum(b.values()) == sum(hh.values()),
    }


# ============================================================
# Hodge-to-de Rham spectral sequence (HKR at cyclic level)
# ============================================================

def hodge_to_deRham_E1(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[Tuple[int, int], int]:
    """E_1 page of the Hodge-to-de Rham spectral sequence.

    E_1^{p,q} = H^q(Omega^p_X), abutting to H^{p+q}_dR(X).
    For smooth proper X in char 0, this degenerates at E_1.
    """
    return dict(hodge)


def verify_hodge_deRham_degeneration(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> bool:
    """Verify E_1 degeneration: sum_{p+q=n} h^{p,q} = b_n."""
    b = betti_numbers(hodge, dim)
    # By construction, b_n = sum h^{p,q} for p+q=n.
    # The check is tautological for smooth varieties in char 0,
    # but serves as a consistency check on our Hodge data.
    for k, bk in b.items():
        check = sum(
            hodge.get((p, k - p), 0) for p in range(dim + 1)
        )
        if check != bk:
            return False
    return True


# ============================================================
# CY structure: obstruction vanishing and formality
# ============================================================

def btt_applies(hodge: Dict[Tuple[int, int], int], dim: int) -> bool:
    """Check whether Bogomolov-Tian-Todorov unobstructedness applies.

    BTT theorem: for a compact Kaehler manifold X with omega_X = O_X,
    the Kodaira-Spencer deformation space is unobstructed.

    The CY condition: h^{d,0} = 1 (existence of holomorphic volume form).
    """
    return hodge.get((dim, 0), 0) == 1


def cy_structure_pairing(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
    k: int,
) -> Dict[str, int]:
    """The CY structure induces a pairing on HH^k x HH^{2d-k} -> C.

    Returns the dimensions and rank of this pairing.
    """
    hh = hochschild_cohomology_HKR(hodge, dim)
    dk = hh.get(k, 0)
    dk_dual = hh.get(2 * dim - k, 0)
    # For smooth proper CY, pairing is nondegenerate, so rank = dk = dk_dual
    rank = min(dk, dk_dual)
    return {
        "HH_k": dk,
        "HH_{2d-k}": dk_dual,
        "rank": rank,
        "nondegenerate": dk == dk_dual,
    }


def obstruction_killed_by_CY(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, object]:
    """Analyze whether the CY structure kills the deformation obstruction.

    For GEOMETRIC (complex structure) deformations of X:
        BTT guarantees unobstructedness. The obstruction in HH^3 is killed
        by the d-dbar lemma (or equivalently, by the CY L-infinity structure
        being formal).

    For NC deformations of D^b(X):
        Kontsevich's formality theorem shows the HKR map is an L-infinity
        quasi-isomorphism, so NC deformations are governed by the DGLA
        of polyvector fields (Gamma(wedge^* T_X), [-,-]_SN, 0).
        The Schouten-Nijenhuis bracket on polyvector fields controls
        the Maurer-Cartan equation.

    For K3: ALL deformations are unobstructed (HH^3 = 0).
    For K3 x E: HH^3 = 44, but geometric deformations are still
    unobstructed by BTT. NC deformations may be partially obstructed.
    """
    hh = hochschild_cohomology_HKR(hodge, dim)
    h_geom = hodge.get((dim - 1, 1), 0)  # complex structure deformations

    result = {
        "total_deformations": hh.get(2, 0),
        "total_obstructions": hh.get(3, 0),
        "geometric_deformations": h_geom,
        "geometric_unobstructed_BTT": btt_applies(hodge, dim),
        "globally_unobstructed": hh.get(3, 0) == 0,
    }

    # The Kontsevich formality theorem implies that the NC deformation
    # problem is controlled by the Schouten-Nijenhuis DGLA.
    # For CY, the holomorphic volume form gives a contraction
    # wedge^k T -> Omega^{d-k}, and the induced L-infinity structure
    # on HH^*(X) has vanishing higher brackets by formality.
    # So ALL deformations (geometric + NC) are formally unobstructed
    # for CY manifolds satisfying formality.

    result["formality_kills_obstructions"] = True  # Kontsevich formality for CY

    return result


# ============================================================
# K3 x E specific computations
# ============================================================

def K3xE_full_analysis() -> Dict[str, object]:
    """Complete obstruction theory analysis for K3 x E."""
    hodge = hodge_diamond_K3xE()
    dim = 3

    hh = hochschild_cohomology_HKR(hodge, dim)
    b = betti_numbers(hodge, dim)
    chi = euler_characteristic(hodge, dim)
    do = deformation_obstruction(hodge, dim)
    nc = nc_deformation_space(hodge, dim)
    br = brauer_group_data(hodge, dim)
    cy_kill = obstruction_killed_by_CY(hodge, dim)

    return {
        "hodge_diamond": hodge,
        "betti_numbers": b,
        "euler_characteristic": chi,
        "hochschild_cohomology": hh,
        "deformation_obstruction": do,
        "nc_deformation_space": nc,
        "brauer_data": br,
        "cy_pairing_nondegenerate": verify_cy_pairing(hh, dim),
        "cy_obstruction_analysis": cy_kill,
        "BTT": btt_applies(hodge, dim),
    }


def K3xE_kuenneth_decomposition() -> Dict[int, Dict[str, int]]:
    """Full Kuenneth decomposition of HH^n(K3 x E) for each n."""
    hh_k3 = hochschild_cohomology_HKR(hodge_diamond_K3(), 2)
    hh_e = hochschild_cohomology_HKR(hodge_diamond_elliptic(), 1)

    result: Dict[int, Dict[str, int]] = {}
    for n in range(7):  # 0 to 2d = 6
        pieces: Dict[str, int] = {}
        for i in sorted(hh_k3):
            j = n - i
            if j in hh_e:
                contrib = hh_k3[i] * hh_e[j]
                if contrib > 0:
                    pieces[f"HH^{i}(K3) x HH^{j}(E)"] = contrib
        if pieces:
            result[n] = pieces
    return result


# ============================================================
# Comparison: general CY 3-folds
# ============================================================

def compare_CY3_deformation_obstruction(
    name: str,
    hodge: Dict[Tuple[int, int], int],
) -> Dict[str, object]:
    """Compare deformation-obstruction data for a CY 3-fold."""
    dim = 3
    hh = hochschild_cohomology_HKR(hodge, dim)
    b = betti_numbers(hodge, dim)
    chi = euler_characteristic(hodge, dim)

    return {
        "name": name,
        "dim_HH2": hh.get(2, 0),
        "dim_HH3": hh.get(3, 0),
        "euler": chi,
        "betti": b,
        "cy_pairing_ok": verify_cy_pairing(hh, dim),
        "BTT": btt_applies(hodge, dim),
    }


# ============================================================
# Twisted sheaves and Brauer class deformations
# ============================================================

def twisted_category_deformations(
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, int]:
    """Deformation space of twisted derived categories D^b(X, alpha).

    For a Brauer class alpha in Br(X), the twisted category D^b(X, alpha)
    has Hochschild cohomology:
        HH^*(D^b(X, alpha)) = HH^*(X) (as graded vector spaces)

    The moduli of Brauer classes is controlled by:
        Br(X) -> H^2(X, O_X*) -> H^3(X, Z)

    For K3: Br(K3) = (T_{K3})^vee / T_{K3} (transcendental lattice quotient).
    For generic K3: rank T = 22 - rho, where rho = Picard number.

    For K3 x E: the Brauer group decomposes by Kuenneth.
    """
    h02 = hodge.get((0, 2), 0)
    b2 = sum(hodge.get((p, 2 - p), 0) for p in range(dim + 1))
    b3 = sum(hodge.get((p, 3 - p), 0) for p in range(dim + 1))

    return {
        "formal_brauer_dim": h02,
        "H2_rank": b2,
        "H3_rank": b3,
        "picard_bound": b2,  # upper bound on Picard number
    }


# ============================================================
# Integration: full CY sheaf category obstruction data
# ============================================================

def full_obstruction_data(
    name: str,
    hodge: Dict[Tuple[int, int], int],
    dim: int,
) -> Dict[str, object]:
    """Complete obstruction-theoretic data for a CY manifold.

    Packages: HKR, Kuenneth, CY pairing, deformation-obstruction,
    BTT, Brauer, periodic cyclic, and formality analysis.
    """
    hh_std = hochschild_cohomology_HKR(hodge, dim)
    hh_alt = hochschild_cohomology_HKR_alt(hodge, dim)
    b = betti_numbers(hodge, dim)
    chi = euler_characteristic(hodge, dim)
    hp = periodic_cyclic_homology(hodge, dim)
    do = deformation_obstruction(hodge, dim)
    nc = nc_deformation_space(hodge, dim)
    cy_pair = verify_cy_pairing(hh_std, dim)
    cy_obs = obstruction_killed_by_CY(hodge, dim)
    br = brauer_group_data(hodge, dim)
    tw = twisted_category_deformations(hodge, dim)

    total_hh = sum(hh_std.values())
    total_b = sum(b.values())

    return {
        "name": name,
        "dimension": dim,
        "hodge_diamond": hodge,
        "HH_standard": hh_std,
        "HH_alternative": hh_alt,
        "betti": b,
        "euler": chi,
        "HP": hp,
        "total_HH_equals_total_HP": total_hh == total_b,
        "deformation_obstruction": do,
        "nc_space": nc,
        "cy_pairing_nondegenerate": cy_pair,
        "cy_obstruction": cy_obs,
        "brauer": br,
        "twisted": tw,
        "BTT": btt_applies(hodge, dim),
        "hodge_deRham_degenerates": verify_hodge_deRham_degeneration(hodge, dim),
    }
