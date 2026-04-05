"""Polyakov-shadow obstruction tower bridge verification.

The shadow obstruction tower at arity 2 projects to the modular characteristic
kappa(A), which replaces the central charge c in Polyakov's functional
determinant / conformal anomaly formula.  The anomaly ratio rho = kappa/c
measures the departure from the classical Polyakov coefficient.

Key structural results verified here:

  1. Polyakov coefficient kappa/12 replaces c/12 in the conformal anomaly.
  2. Complementarity kappa(A) + kappa(A!) is a level-independent constant
     for each algebraic family (Theorem C/D scalar projection).
  3. Faber-Pandharipande intersection numbers lambda_g^FP give exact
     genus-g free energies F_g = kappa * lambda_g^FP.
  4. BPZ parameters b^2 = 6/c, (b')^2 = 6/(26-c) encode Koszul duality
     at the Virasoro level; self-dual at c = 13.
  5. Shadow depth classification G/L/C/M captures the complexity of the
     shadow obstruction tower beyond arity 2.

Standard families:
  - Heisenberg H_k:     c = k,               kappa = k,  rho = 1
  - Virasoro Vir_c:     c = c,               kappa = c/2
  - Affine V_k(sl_N):   c = k*dim(g)/(k+h^v), kappa = dim(g)*(k+h^v)/(2*h^v)
  - betagamma (wt lam): c = 2(6lam^2-6lam+1), kappa = 6lam^2-6lam+1 = c/2
  - W_3 at c:           kappa = 5c/6
  - W_N at c:           kappa = c * sigma(g), sigma = sum 1/(m_i+1)
  - Lattice V_Lambda:   c = rank,            kappa = rank,  rho = 1

Ground truth:
  theorem_c_complementarity.py (kappa formulas, complementarity),
  betagamma_determinant.py (betagamma c and kappa),
  nonlinear_modular_shadows.tex (shadow obstruction tower, shadow depth),
  concordance.tex (shadow archetype classification, Faber-Pandharipande).

GRADING: Cohomological, |d| = +1.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, bernoulli, factorial, Abs


# =========================================================================
# Lie algebra data
# =========================================================================

_LIE_DATA: Dict[Tuple[str, int], Tuple[int, int]] = {
    ("A", 1): (3, 2),     # sl_2
    ("A", 2): (8, 3),     # sl_3
    ("A", 3): (15, 4),    # sl_4
    ("A", 4): (24, 5),    # sl_5
    ("A", 5): (35, 6),    # sl_6
    ("A", 6): (48, 7),    # sl_7
    ("A", 7): (63, 8),    # sl_8
    ("A", 8): (80, 9),    # sl_9
    ("A", 9): (99, 10),   # sl_10
    ("B", 2): (10, 3),    # so_5
    ("B", 3): (21, 5),    # so_7
    ("C", 2): (10, 3),    # sp_4
    ("C", 3): (21, 4),    # sp_6
    ("D", 4): (28, 6),    # so_8
    ("G", 2): (14, 4),    # g_2
    ("F", 4): (52, 9),    # f_4
    ("E", 6): (78, 12),   # e_6
    ("E", 7): (133, 18),  # e_7
    ("E", 8): (248, 30),  # e_8
}

_EXPONENTS: Dict[Tuple[str, int], List[int]] = {
    ("A", 1): [1],
    ("A", 2): [1, 2],
    ("A", 3): [1, 2, 3],
    ("A", 4): [1, 2, 3, 4],
    ("B", 2): [1, 3],
    ("B", 3): [1, 3, 5],
    ("C", 2): [1, 3],
    ("C", 3): [1, 3, 5],
    ("D", 4): [1, 3, 3, 5],
    ("G", 2): [1, 5],
    ("F", 4): [1, 5, 7, 11],
    ("E", 6): [1, 4, 5, 7, 8, 11],
    ("E", 7): [1, 5, 7, 9, 11, 13, 17],
    ("E", 8): [1, 7, 11, 13, 17, 19, 23, 29],
}


def _lie_dim_hdual(lie_type: str, rank: int) -> Tuple[int, int]:
    """Return (dim(g), h^vee) for a simple Lie algebra."""
    key = (lie_type, rank)
    if key in _LIE_DATA:
        return _LIE_DATA[key]
    if lie_type == "A":
        N = rank + 1
        return N * N - 1, N
    raise ValueError(f"Lie algebra ({lie_type}, {rank}) not available")


def _sigma_invariant(lie_type: str, rank: int) -> Fraction:
    """Root datum invariant sigma(g) = sum 1/(m_i + 1).

    m_i are the exponents of the Lie algebra.
    For A_n: exponents = 1, 2, ..., n, sigma = sum_{i=1}^{n} 1/(i+1).
    """
    key = (lie_type, rank)
    if key in _EXPONENTS:
        return sum(Fraction(1, m + 1) for m in _EXPONENTS[key])
    if lie_type == "A":
        return sum(Fraction(1, m + 1) for m in range(1, rank + 1))
    raise ValueError(f"Exponents for ({lie_type}, {rank}) not available")


# =========================================================================
# 1. central_charge(family, **params) -> Fraction
# =========================================================================

def central_charge(family: str, **params) -> Fraction:
    """Central charge c(A) for standard families.

    Families and parameters:
      "heisenberg":  k (level, default 1)
      "virasoro":    c (central charge)
      "affine":      lie_type, rank, k
      "betagamma":   lam (conformal weight, default 1), or c directly
      "w3":          c
      "wn":          lie_type, rank, k (computes c via DS reduction)
      "lattice":     rank
    """
    family = family.lower()

    if family == "heisenberg":
        k = params.get("k", 1)
        return Fraction(k)

    elif family == "virasoro":
        c = params.get("c")
        if c is None:
            raise ValueError("Central charge c required for Virasoro")
        return Fraction(c)

    elif family == "affine":
        lie_type = params.get("lie_type", "A")
        rank = params.get("rank", 1)
        k = Fraction(params.get("k", 1))
        dim_g, h_dual = _lie_dim_hdual(lie_type, rank)
        if k + h_dual == 0:
            raise ValueError(
                f"Critical level k = -{h_dual}: Sugawara undefined"
            )
        return k * Fraction(dim_g) / (k + h_dual)

    elif family == "betagamma":
        if "c" in params:
            return Fraction(params["c"])
        lam = Fraction(params.get("lam", 1))
        # c_{bg} = 2(6*lam^2 - 6*lam + 1)
        return 2 * (6 * lam ** 2 - 6 * lam + 1)

    elif family == "w3":
        c = params.get("c")
        if c is None:
            raise ValueError("Central charge c required for W_3")
        return Fraction(c)

    elif family == "wn":
        lie_type = params.get("lie_type", "A")
        rank = params.get("rank", 1)
        if "c" in params:
            return Fraction(params["c"])
        k = Fraction(params.get("k", 1))
        return _wn_ds_central_charge(lie_type, rank, k)

    elif family == "lattice":
        rank = params.get("rank", 1)
        return Fraction(rank)

    else:
        raise ValueError(f"Unknown family: {family}")


def _wn_ds_central_charge(lie_type: str, rank: int, k: Fraction) -> Fraction:
    """Central charge of W-algebra from principal DS reduction.

    c = rank(g) - dim(g) * (k + h^v - 1)^2 / (k + h^v)
    """
    if lie_type != "A":
        raise NotImplementedError(
            f"DS central charge for ({lie_type}, {rank})"
        )
    N = rank + 1
    dim_g = N * N - 1
    h_dual = N
    rk = N - 1
    k = Fraction(k)
    denom = k + h_dual
    if denom == 0:
        raise ValueError(f"Critical level k = -{h_dual}")
    return Fraction(rk) - Fraction(dim_g) * (k + h_dual - 1) ** 2 / denom


# =========================================================================
# 2. kappa(family, **params) -> Fraction
# =========================================================================

def kappa(family: str, **params) -> Fraction:
    """Modular characteristic kappa(A) for standard families.

    The arity-2 projection of the shadow obstruction tower.  Replaces c
    in the Polyakov functional-determinant formula.

    Families and parameters:
      "heisenberg":  k (level)         -> kappa = k
      "virasoro":    c                  -> kappa = c/2
      "affine":      lie_type, rank, k  -> kappa = dim(g)*(k+h^v)/(2*h^v)
      "betagamma":   lam or c           -> kappa = c/2 = 6*lam^2-6*lam+1
      "w3":          c                  -> kappa = 5c/6
      "wn":          lie_type, rank, c  -> kappa = c * sigma(g)
      "lattice":     rank               -> kappa = rank
    """
    family = family.lower()

    if family == "heisenberg":
        k = params.get("k", 1)
        return Fraction(k)

    elif family == "virasoro":
        c = params.get("c")
        if c is None:
            raise ValueError("Central charge c required for Virasoro")
        return Fraction(c) / 2

    elif family == "affine":
        lie_type = params.get("lie_type", "A")
        rank = params.get("rank", 1)
        k = Fraction(params.get("k", 1))
        dim_g, h_dual = _lie_dim_hdual(lie_type, rank)
        if k + h_dual == 0:
            raise ValueError(
                f"Critical level k = -{h_dual}: kappa undefined"
            )
        return Fraction(dim_g) * (k + h_dual) / (2 * h_dual)

    elif family == "betagamma":
        if "c" in params:
            return Fraction(params["c"]) / 2
        lam = Fraction(params.get("lam", 1))
        # kappa = c/2 = 6*lam^2 - 6*lam + 1
        return 6 * lam ** 2 - 6 * lam + 1

    elif family == "w3":
        c = params.get("c")
        if c is None:
            raise ValueError("Central charge c required for W_3")
        return Fraction(5) * Fraction(c) / 6

    elif family == "wn":
        lie_type = params.get("lie_type", "A")
        rank = params.get("rank", 1)
        c = params.get("c")
        if c is None:
            raise ValueError("Central charge c required for W_N")
        sigma = _sigma_invariant(lie_type, rank)
        return Fraction(c) * sigma

    elif family == "lattice":
        rank = params.get("rank", 1)
        return Fraction(rank)

    else:
        raise ValueError(f"Unknown family: {family}")


# =========================================================================
# 3. anomaly_ratio(family, **params) -> Fraction
# =========================================================================

def anomaly_ratio(family: str, **params) -> Fraction:
    """Anomaly ratio rho = kappa / c.

    Measures departure from the classical Polyakov coefficient.
    rho = 1 for Heisenberg (kappa = c = k).
    rho = 1/2 for Virasoro and betagamma.
    rho = 5/6 for W_3.
    """
    k = kappa(family, **params)
    c = central_charge(family, **params)
    if c == 0:
        raise ValueError("Central charge is zero; anomaly ratio undefined")
    return k / c


# =========================================================================
# 4. complementarity_sum(family, **params) -> Fraction
# =========================================================================

def _ff_dual_params(family: str, **params) -> dict:
    """Return the Feigin-Frenkel dual parameters for each family."""
    family = family.lower()

    if family == "heisenberg":
        k = params.get("k", 1)
        return {"k": -Fraction(k)}

    elif family == "virasoro":
        c = Fraction(params.get("c", 1))
        return {"c": Fraction(26) - c}

    elif family == "affine":
        lie_type = params.get("lie_type", "A")
        rank = params.get("rank", 1)
        k = Fraction(params.get("k", 1))
        _, h_dual = _lie_dim_hdual(lie_type, rank)
        return {"lie_type": lie_type, "rank": rank, "k": -k - 2 * h_dual}

    elif family == "betagamma":
        if "c" in params:
            return {"c": -Fraction(params["c"])}
        lam = Fraction(params.get("lam", 1))
        c_bg = 2 * (6 * lam ** 2 - 6 * lam + 1)
        return {"c": -c_bg}

    elif family == "w3":
        c = Fraction(params.get("c", 2))
        return {"c": Fraction(100) - c}

    elif family == "wn":
        lie_type = params.get("lie_type", "A")
        rank = params.get("rank", 1)
        c = Fraction(params.get("c"))
        c_sum = _w_central_charge_sum(lie_type, rank)
        return {"lie_type": lie_type, "rank": rank, "c": c_sum - c}

    elif family == "lattice":
        rank = params.get("rank", 1)
        return {"rank": rank}

    else:
        raise ValueError(f"Unknown family: {family}")


def _w_central_charge_sum(lie_type: str, rank: int) -> Fraction:
    """Sum c(k) + c(k') for W-algebra under FF involution.

    Level-independent.  For W(sl_2)=Vir: 26.  For W(sl_3)=W_3: 100.
    """
    if lie_type == "A" and rank == 1:
        return Fraction(26)
    if lie_type == "A" and rank == 2:
        return Fraction(100)
    if lie_type == "A":
        N = rank + 1
        k_test = Fraction(1)
        c1 = _wn_ds_central_charge("A", rank, k_test)
        c2 = _wn_ds_central_charge("A", rank, -k_test - 2 * N)
        return c1 + c2
    raise NotImplementedError(
        f"W-algebra central charge sum for ({lie_type}, {rank})"
    )


def _kappa_dual(family: str, **params) -> Fraction:
    """Modular characteristic of the Koszul dual algebra."""
    family_lower = family.lower()
    dual_params = _ff_dual_params(family, **params)

    if family_lower == "betagamma":
        return Fraction(dual_params["c"]) / 2

    elif family_lower == "lattice":
        return -Fraction(dual_params["rank"])

    elif family_lower in ("w3", "wn"):
        if family_lower == "w3":
            return kappa("w3", c=dual_params["c"])
        return kappa("wn", **dual_params)

    else:
        return kappa(family, **dual_params)


def complementarity_sum(family: str, **params) -> Fraction:
    """Compute kappa(A) + kappa(A!) for a given family.

    Level-independent constant for each family / root datum:
      Heisenberg: 0
      Virasoro:   13
      Affine:     0
      betagamma:  0
      W_3:        250/3
      Lattice:    0
    """
    return kappa(family, **params) + _kappa_dual(family, **params)


# =========================================================================
# 5. faber_pandharipande(g) -> Fraction
# =========================================================================

def faber_pandharipande(g: int) -> Fraction:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Returns exact Fraction.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    num = Rational(2 ** (2 * g - 1) - 1) * Abs(B_2g)
    den = Rational(2 ** (2 * g - 1)) * factorial(2 * g)
    result = num / den
    return Fraction(int(result.p), int(result.q))


# =========================================================================
# 6. genus_free_energy(family, g, **params) -> Fraction
# =========================================================================

def genus_free_energy(family: str, g: int, **params) -> Fraction:
    """Genus-g free energy F_g(A) = kappa(A) * lambda_g^FP.

    At genus 1: F_1 = kappa / 24.
    """
    k = kappa(family, **params)
    lam_g = faber_pandharipande(g)
    return k * lam_g


# =========================================================================
# 7. polyakov_coefficient(family, **params) -> Fraction
# =========================================================================

def polyakov_coefficient(family: str, **params) -> Fraction:
    """Polyakov functional-determinant coefficient kappa/12.

    Replaces the classical c/12 in the conformal anomaly action:
      S_Polyakov = (kappa/12) * integral(R * 1/Delta * R)
    """
    return kappa(family, **params) / 12


# =========================================================================
# 8. bpz_parameter(c) -> (Fraction, Fraction)
# =========================================================================

def bpz_parameter(c) -> Tuple[Fraction, Fraction]:
    """BPZ parameters under Koszul duality for Virasoro.

    b^2 = 6/c,   (b')^2 = 6/(26-c)

    Self-dual at c = 13: b^2 = (b')^2 = 6/13.
    """
    c = Fraction(c)
    if c == 0:
        raise ValueError("c = 0: BPZ parameter b^2 = 6/c undefined")
    if c == 26:
        raise ValueError("c = 26: dual BPZ parameter (b')^2 = 6/(26-c) undefined")
    b_sq = Fraction(6) / c
    b_prime_sq = Fraction(6) / (Fraction(26) - c)
    return b_sq, b_prime_sq


# =========================================================================
# 9. mumford_exponent(family, **params) -> Fraction
# =========================================================================

def mumford_exponent(family: str, **params) -> Fraction:
    """Mumford line bundle exponent.

    The Mumford isomorphism lambda^{otimes mu} ~ delta on M_g has
    exponent mu = 6*kappa + 1 for the Hodge-Mumford relation, but
    in the Polyakov context the exponent is the complementarity sum
    kappa + kappa! = the total curvature.

    For the d-dimensional bosonic string (d copies of Heisenberg at
    level 1 plus Virasoro at c = d):
      kappa_total = d + d/2 = 3d/2
    The critical case d = 26 gives kappa_total = 39, and the Mumford
    exponent (= complementarity constant for the combined system) is 13.

    For a single family, returns kappa + kappa!.
    """
    return complementarity_sum(family, **params)


# =========================================================================
# 10. shadow_depth_class(family, **params) -> str
# =========================================================================

def shadow_depth_class(family: str, **params) -> str:
    """Shadow depth classification: G, L, C, or M.

    G (Gaussian, r_max=2): Heisenberg, lattice.
        Shadow obstruction tower terminates at arity 2.  kappa captures everything.
    L (Lie/tree, r_max=3): affine Kac-Moody.
        Nonzero cubic shadow C; tower terminates at arity 3.
    C (contact/quartic, r_max=4): betagamma.
        Nonzero quartic contact invariant; terminates at arity 4.
    M (mixed, r_max=infinity): Virasoro, W_N.
        Infinite tower.  No finite truncation captures all shadows.
    """
    family = family.lower()
    _DEPTH_CLASS = {
        "heisenberg": "G",
        "lattice": "G",
        "affine": "L",
        "betagamma": "C",
        "virasoro": "M",
        "w3": "M",
        "wn": "M",
    }
    return _DEPTH_CLASS.get(family, "M")


def shadow_depth(family: str, **params) -> Optional[int]:
    """Finite shadow depth r_max, or None for infinite tower.

    G: 2,  L: 3,  C: 4,  M: None (infinity).
    """
    family = family.lower()
    _DEPTH = {
        "heisenberg": 2,
        "lattice": 2,
        "affine": 3,
        "betagamma": 4,
        "virasoro": None,
        "w3": None,
        "wn": None,
    }
    return _DEPTH.get(family)


# =========================================================================
# 11. bosonic_string_free_energy(d, g) -> Fraction
# =========================================================================

def bosonic_string_free_energy(d: int, g: int) -> Fraction:
    """Genus-g free energy for the d-dimensional bosonic string.

    The d-dimensional bosonic string has c = d (d copies of Heisenberg
    at level 1, then Virasoro gauged).  The total kappa = d/2 (Virasoro
    contribution; Heisenberg kappa cancels in the gauge-fixed theory,
    leaving the ghost contribution with kappa_total = c_matter/2 = d/2
    for the Polyakov determinant).

    Wait -- for the full bosonic string: d matter fields (c = d) plus
    bc ghost system (c = -26), giving c_total = d - 26.  The kappa for
    the Virasoro Polyakov action is c/2 = d/2 for the matter, and
    the ghost contribution is -13.  At d = 26 the total vanishes.

    For the genus expansion of the Polyakov determinant:
      F_g = (d/2 - 13) * lambda_g^FP

    This reproduces the known bosonic string partition function.
    At d = 26: F_g = 0 for all g (anomaly cancellation).
    """
    kappa_total = Fraction(d, 2) - 13
    lam_g = faber_pandharipande(g)
    return kappa_total * lam_g


def bosonic_string_critical_dimension() -> int:
    """Critical dimension where all genus contributions vanish.

    F_g = (d/2 - 13) * lambda_g = 0 for all g iff d = 26.
    """
    return 26


# =========================================================================
# 12. genus_growth_bound(family, max_g, **params) -> list
# =========================================================================

def genus_growth_bound(family: str, max_g: int, **params) -> List[Fraction]:
    r"""Absolute values |F_g| for g = 1 .. max_g.

    The Faber-Pandharipande numbers satisfy:
      lambda_g ~ (2g)! / (2*pi)^{2g} * (corrections)

    so |F_g| grows factorially.  This function returns the exact
    values for comparison.
    """
    k = kappa(family, **params)
    result = []
    for g in range(1, max_g + 1):
        fg = k * faber_pandharipande(g)
        result.append(abs(fg))
    return result


# =========================================================================
# Derived quantities
# =========================================================================

def polyakov_bridge_summary(family: str, max_g: int = 3,
                            **params) -> Dict[str, Any]:
    """Complete Polyakov-shadow bridge data for a given family.

    Returns dict with all computed quantities.
    """
    k = kappa(family, **params)
    c = central_charge(family, **params)
    rho = anomaly_ratio(family, **params) if c != 0 else None
    comp = complementarity_sum(family, **params)
    depth_cls = shadow_depth_class(family, **params)
    depth_val = shadow_depth(family, **params)
    poly_coeff = polyakov_coefficient(family, **params)

    free_energies = {}
    for g in range(1, max_g + 1):
        free_energies[g] = genus_free_energy(family, g, **params)

    return {
        "family": family,
        "params": params,
        "central_charge": c,
        "kappa": k,
        "anomaly_ratio": rho,
        "polyakov_coefficient": poly_coeff,
        "complementarity_sum": comp,
        "shadow_depth_class": depth_cls,
        "shadow_depth": depth_val,
        "genus_free_energies": free_energies,
    }


def anomaly_ratio_table() -> Dict[str, Fraction]:
    """Anomaly ratios for all standard families (at generic level).

    rho = kappa/c is level-independent for families where it is defined.
    """
    return {
        "heisenberg": Fraction(1),            # kappa = c = k
        "virasoro": Fraction(1, 2),           # kappa = c/2
        "affine_sl_2": Fraction(3, 4) * Fraction(3, 3),  # dim=3, h^v=2
                                              # kappa/c = (dim*(k+h^v)/(2h^v)) / (k*dim/(k+h^v))
                                              #         = (k+h^v)^2 / (2*h^v*k)
        "betagamma": Fraction(1, 2),          # kappa = c/2
        "w3": Fraction(5, 6),                 # kappa = 5c/6
        "lattice": Fraction(1),               # kappa = rank = c
    }


def affine_anomaly_ratio(lie_type: str, rank: int, k) -> Fraction:
    """Anomaly ratio for affine algebra at level k.

    rho = kappa/c = (k+h^v)^2 / (2 * h^v * k)

    This is NOT level-independent: it varies with k.
    """
    _, h_dual = _lie_dim_hdual(lie_type, rank)
    k = Fraction(k)
    if k == 0:
        raise ValueError("k = 0: central charge vanishes, ratio undefined")
    if k + h_dual == 0:
        raise ValueError(f"Critical level k = -{h_dual}")
    return (k + h_dual) ** 2 / (2 * h_dual * k)
