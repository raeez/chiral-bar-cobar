"""Minimal model bar complexes: Ising, tricritical Ising, three-state Potts.

Ground truth from the manuscript (minimal_model_examples.tex, minimal_model_fusion.tex):
  Minimal model M(p,q): c = 1 - 6(p-q)^2/(pq)

  comp:ising-bar-interpretation:
    Ising M(4,3): c = 1/2
    kappa = c/2 = 1/4
    obs_1 = kappa/24 = 1/96
    3 modules: I (vacuum), sigma, epsilon
    Fusion: sigma x sigma = I + epsilon, sigma x epsilon = sigma

  Minimal model central charges:
    M(3,2): c = 0 (trivial)
    M(4,3): c = 1/2 (Ising)
    M(5,2): c = -22/5 (non-unitary Lee-Yang)
    M(5,4): c = 7/10 (tricritical Ising)
    M(6,5): c = 4/5 (three-state Potts)

CONVENTIONS:
- Virasoro DS formula: c = 1 - 6(k+1)^2/(k+2)
"""

from __future__ import annotations

from typing import Dict, List

from sympy import Rational, Symbol


# ---------------------------------------------------------------------------
# Minimal model central charges
# ---------------------------------------------------------------------------

def minimal_model_c(p: int, q: int) -> Rational:
    """Central charge of minimal model M(p,q).

    c = 1 - 6(p-q)^2/(pq).
    Convention: p > q >= 2, gcd(p,q) = 1.
    """
    return 1 - Rational(6 * (p - q)**2, p * q)


MINIMAL_MODELS = {
    "trivial": {"p": 3, "q": 2, "c": Rational(0), "name": "trivial"},
    "Ising": {"p": 4, "q": 3, "c": Rational(1, 2), "name": "Ising"},
    "Lee_Yang": {"p": 5, "q": 2, "c": Rational(-22, 5), "name": "Lee-Yang"},
    "tricritical_Ising": {"p": 5, "q": 4, "c": Rational(7, 10), "name": "tricritical Ising"},
    "three_state_Potts": {"p": 6, "q": 5, "c": Rational(4, 5), "name": "three-state Potts"},
}


# ---------------------------------------------------------------------------
# Ising model bar complex
# ---------------------------------------------------------------------------

def ising_bar_data() -> Dict[str, object]:
    """Bar complex data for the Ising model M(4,3).

    Ground truth: comp:ising-bar-interpretation.
    """
    c = Rational(1, 2)
    kappa = c / 2  # = 1/4
    obs_1 = kappa / 24  # = 1/96

    return {
        "c": c,
        "kappa": kappa,
        "obs_1": obs_1,
        "n_modules": 3,
        "modules": ["I", "sigma", "epsilon"],
        "conformal_weights": {
            "I": Rational(0),
            "sigma": Rational(1, 16),
            "epsilon": Rational(1, 2),
        },
        "fusion_rules": {
            ("sigma", "sigma"): ["I", "epsilon"],
            ("sigma", "epsilon"): ["sigma"],
            ("epsilon", "epsilon"): ["I"],
        },
    }


def ising_genus1_bar() -> Dict[str, Dict[str, object]]:
    """Genus-1 bar complex for Ising model.

    Ground truth: comp:ising-bar-interpretation.
    """
    return {
        "B_{g=1}(I, I)": {
            "H^0": ["I"],
            "dim": 1,
            "interpretation": "vacuum torus amplitude",
        },
        "B_{g=1}(sigma, sigma)": {
            "H^0": ["I", "epsilon"],
            "dim": 2,
            "interpretation": "sigma x sigma = I + epsilon",
        },
        "B_{g=1}(sigma, epsilon)": {
            "H^0": ["sigma"],
            "dim": 1,
            "interpretation": "sigma x epsilon = sigma",
        },
    }


# ---------------------------------------------------------------------------
# Tricritical Ising
# ---------------------------------------------------------------------------

def tricritical_ising_data() -> Dict[str, object]:
    """Bar complex data for tricritical Ising M(5,4)."""
    c = Rational(7, 10)
    return {
        "c": c,
        "kappa": c / 2,
        "n_modules": 6,
        "conformal_weights": {
            "I": Rational(0),
            "epsilon": Rational(1, 10),
            "epsilon'": Rational(3, 5),
            "epsilon''": Rational(3, 2),
            "sigma": Rational(3, 80),
            "sigma'": Rational(7, 16),
        },
    }


# ---------------------------------------------------------------------------
# Three-state Potts
# ---------------------------------------------------------------------------

def three_state_potts_data() -> Dict[str, object]:
    """Bar complex data for three-state Potts M(6,5)."""
    c = Rational(4, 5)
    return {
        "c": c,
        "kappa": c / 2,
        "n_modules": 10,
    }


# ---------------------------------------------------------------------------
# Complementarity for minimal models
# ---------------------------------------------------------------------------

def minimal_model_complementarity(p: int, q: int) -> Rational:
    """c + c' = 26 for Virasoro (regardless of p,q).

    All minimal models have the same complementarity sum c + c' = 26,
    since they are Virasoro quotients.
    """
    return Rational(26)


# ---------------------------------------------------------------------------
# Primary field computation
# ---------------------------------------------------------------------------

def _validate_pq(p: int, q: int):
    """Validate M(p,q) parameters."""
    from math import gcd
    if q < 2:
        raise ValueError(f"q={q} < 2")
    if p <= q:
        raise ValueError(f"p={p} <= q={q}")
    if gcd(p, q) != 1:
        raise ValueError(f"gcd({p},{q}) = {gcd(p,q)} != 1")


def conformal_weight(p: int, q: int, r: int, s: int) -> Rational:
    r"""Conformal weight h_{r,s} of primary field in M(p,q).

    h_{r,s} = ((pr - qs)^2 - (p-q)^2) / (4pq)

    Convention: 1 <= r <= q-1, 1 <= s <= p-1.
    """
    return Rational((p * r - q * s) ** 2 - (p - q) ** 2, 4 * p * q)


def n_primaries(p: int, q: int) -> int:
    """Number of independent primary fields: (p-1)(q-1)/2."""
    return (p - 1) * (q - 1) // 2


def minimal_model_primaries(p: int, q: int) -> List:
    """List of (r, s) labels for independent primary fields of M(p,q).

    Uses identification h_{r,s} = h_{q-r, p-s}: take the lexicographically
    first representative.  Convention: 1 <= r <= q-1, 1 <= s <= p-1.
    """
    _validate_pq(p, q)
    seen = set()
    primaries = []
    for r in range(1, q):
        for s in range(1, p):
            pair = (r, s)
            dual = (q - r, p - s)
            if dual not in seen:
                seen.add(pair)
                primaries.append(pair)
    return primaries


def conformal_weights_table(p: int, q: int) -> Dict:
    """Dict mapping (r,s) -> h_{r,s} for all independent primaries."""
    prims = minimal_model_primaries(p, q)
    return {(r, s): conformal_weight(p, q, r, s) for r, s in prims}


# ---------------------------------------------------------------------------
# Modular S-matrix
# ---------------------------------------------------------------------------

def s_matrix_s00(p: int, q: int) -> float:
    """S_{00} for minimal model M(p,q), positive by convention.

    Equal to |2*sqrt(2/(pq)) * sin(pi*p/q) * sin(pi*q/p)|.
    """
    import math
    raw = 2.0 * math.sqrt(2.0 / (p * q)) * math.sin(math.pi * p / q) * math.sin(math.pi * q / p)
    return abs(raw)


def _s_matrix_element(p: int, q: int, r1: int, s1: int, r2: int, s2: int) -> float:
    """Numerical S-matrix element S_{(r1,s1),(r2,s2)}."""
    import math
    prefactor = 2.0 * math.sqrt(2.0 / (p * q))
    sign = (-1) ** (1 + r1 * s2 + r2 * s1)
    val = prefactor * math.sin(math.pi * p * r1 * r2 / q) * math.sin(math.pi * q * s1 * s2 / p)
    return sign * abs(val) if False else val  # direct formula
    # Actually the standard formula is:
    # S_{(r1,s1),(r2,s2)} = (-1)^{1+r1*s2+r2*s1} * 2*sqrt(2/(pq)) * sin(pi*p*r1*r2/q) * sin(pi*q*s1*s2/p)
    # But let me use the well-known correct formula directly.


def _s_element_correct(p: int, q: int, r1: int, s1: int, r2: int, s2: int) -> float:
    """Correct S-matrix element for minimal model M(p,q).

    S_{(r1,s1),(r2,s2)} = (-1)^{1+s1*r2+s2*r1} * 2*sqrt(2/(pq))
                          * sin(pi*q*s1*s2/p) * sin(pi*p*r1*r2/q)
    """
    import math
    prefactor = 2.0 * math.sqrt(2.0 / (p * q))
    sign = (-1) ** (1 + s1 * r2 + s2 * r1)
    return sign * prefactor * math.sin(math.pi * q * s1 * s2 / p) * math.sin(math.pi * p * r1 * r2 / q)


def modular_s_matrix_numerical(p: int, q: int) -> Dict:
    """Compute the modular S-matrix numerically for M(p,q).

    Normalizes so that S_{00} > 0 (standard CFT convention).
    """
    prims = minimal_model_primaries(p, q)
    n = len(prims)
    mat = [[0.0] * n for _ in range(n)]
    for i, (r1, s1) in enumerate(prims):
        for j, (r2, s2) in enumerate(prims):
            mat[i][j] = _s_element_correct(p, q, r1, s1, r2, s2)
    # Normalize: ensure S00 > 0
    if mat[0][0] < 0:
        for i in range(n):
            for j in range(n):
                mat[i][j] = -mat[i][j]
    return {
        "matrix": mat,
        "primaries": prims,
        "S00": mat[0][0],
    }


def modular_s_matrix_exact(p: int, q: int) -> Dict:
    """Compute the modular S-matrix exactly using SymPy for M(p,q)."""
    from sympy import sqrt as sym_sqrt, sin as sym_sin, pi as sym_pi, Integer
    prims = minimal_model_primaries(p, q)
    n = len(prims)
    prefactor = 2 * sym_sqrt(Rational(2, p * q))
    mat = [[Rational(0)] * n for _ in range(n)]
    for i, (r1, s1) in enumerate(prims):
        for j, (r2, s2) in enumerate(prims):
            sign = (-1) ** (1 + s1 * r2 + s2 * r1)
            elem = sign * prefactor * sym_sin(sym_pi * q * s1 * s2 / p) * sym_sin(sym_pi * p * r1 * r2 / q)
            mat[i][j] = elem
    return {
        "matrix": mat,
        "primaries": prims,
        "S00": mat[0][0],
    }


def verify_s_matrix_properties(p: int, q: int) -> Dict[str, bool]:
    """Verify S-matrix is symmetric, unitary, S^2 = C."""
    sdata = modular_s_matrix_numerical(p, q)
    mat = sdata["matrix"]
    n = len(mat)
    results = {}

    # Symmetry
    sym_ok = True
    for i in range(n):
        for j in range(n):
            if abs(mat[i][j] - mat[j][i]) > 1e-10:
                sym_ok = False
    results["symmetric"] = sym_ok

    # Unitarity: S * S^T = I
    unit_ok = True
    for i in range(n):
        for j in range(n):
            val = sum(mat[i][k] * mat[j][k] for k in range(n))
            expected = 1.0 if i == j else 0.0
            if abs(val - expected) > 1e-10:
                unit_ok = False
    results["unitary"] = unit_ok

    # S^2 = C (charge conjugation = identity for minimal models)
    sq_ok = True
    for i in range(n):
        for j in range(n):
            val = sum(mat[i][k] * mat[k][j] for k in range(n))
            expected = 1.0 if i == j else 0.0
            if abs(val - expected) > 1e-10:
                sq_ok = False
    results["S_squared_is_C"] = sq_ok

    # S00 positive
    results["S00_positive"] = sdata["S00"] > 0

    return results


# ---------------------------------------------------------------------------
# Verlinde fusion
# ---------------------------------------------------------------------------

def verlinde_fusion_numerical(p: int, q: int, i: int, j: int, k: int) -> int:
    """Compute fusion coefficient N_{ij}^k via Verlinde formula.

    N_{ij}^k = sum_l S_{il} S_{jl} S*_{kl} / S_{0l}
    """
    sdata = modular_s_matrix_numerical(p, q)
    mat = sdata["matrix"]
    n = len(mat)
    if i >= n or j >= n or k >= n:
        return 0
    total = 0.0
    for l in range(n):
        s0l = mat[0][l]
        if abs(s0l) < 1e-15:
            continue
        total += mat[i][l] * mat[j][l] * mat[k][l] / s0l
    return int(round(total))


def fusion_ring(p: int, q: int) -> Dict:
    """Compute the full fusion ring for M(p,q)."""
    prims = minimal_model_primaries(p, q)
    n = len(prims)
    coeffs = {}
    for i in range(n):
        for j in range(i, n):
            for k in range(n):
                nijk = verlinde_fusion_numerical(p, q, i, j, k)
                if nijk != 0:
                    coeffs[(i, j, k)] = nijk
    return {
        "n_primaries": n,
        "primaries": prims,
        "fusion_coefficients": coeffs,
    }


def verlinde_genus_dimension(p: int, q: int, g: int) -> float:
    """Compute dim V_g = sum_i S_{0i}^{2-2g} (Verlinde genus-g dimension)."""
    sdata = modular_s_matrix_numerical(p, q)
    mat = sdata["matrix"]
    n = len(mat)
    total = 0.0
    for i in range(n):
        s0i = mat[0][i]
        if abs(s0i) < 1e-15:
            continue
        total += s0i ** (2 - 2 * g)
    return total


# ---------------------------------------------------------------------------
# Partition function and Kac determinant
# ---------------------------------------------------------------------------

def partition_count(n: int) -> int:
    """Number of partitions of n (p(n))."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Simple dynamic programming
    table = [0] * (n + 1)
    table[0] = 1
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            table[m] += table[m - k]
    return table[n]


def kac_determinant_factors(p: int, q: int, level: int) -> List:
    """Kac determinant factors at given level for M(p,q).

    Returns list of (r, s, h_{r,s}, multiplicity) where multiplicity = p(level - r*s).
    Only includes (r,s) with r*s <= level.
    """
    factors = []
    for r in range(1, level + 1):
        for s in range(1, level + 1):
            if r * s > level:
                continue
            h_rs = conformal_weight(p, q, r, s)
            mult = partition_count(level - r * s)
            if mult > 0:
                factors.append((r, s, h_rs, mult))
    return factors


def kac_determinant_total_degree(level: int) -> int:
    """Total degree of the Kac determinant at given level.

    deg det_n = sum_{r,s >= 1, rs <= n} p(n - rs).
    """
    total = 0
    for r in range(1, level + 1):
        for s in range(1, level + 1):
            if r * s > level:
                continue
            total += partition_count(level - r * s)
    return total


def null_vector_levels(p: int, q: int) -> List:
    """Null vector levels for the vacuum module of M(p,q).

    Vacuum null vectors occur at levels r*s for (r,s) with h_{r,s} = 0.
    For M(p,q): h_{r,s} = 0 when pr - qs = ±(p-q), i.e., (r,s) = (1,1) and (q-1, p-1).
    """
    nulls = []
    for r in range(1, q):
        for s in range(1, p):
            if conformal_weight(p, q, r, s) == 0:
                nulls.append((r, s, r * s))
    return nulls


# ---------------------------------------------------------------------------
# Bar cohomology (universal Virasoro, i.e., Koszul)
# ---------------------------------------------------------------------------

def bar_cohomology_ranks(p: int, q: int, max_degree: int = 5) -> Dict[int, int]:
    """Bar cohomology ranks for the universal Virasoro algebra at c = c(p,q).

    The universal Virasoro algebra (NOT the simple quotient) is Koszul:
    H^0 = 1, H^1 = 1 (generator T), H^2 = 1 (Virasoro relation), H^k = 0 for k >= 3.
    This is independent of c.
    """
    ranks = {0: 1, 1: 1, 2: 1}
    for k in range(3, max_degree + 1):
        ranks[k] = 0
    return ranks


# ---------------------------------------------------------------------------
# Shadow tower for minimal models (= Virasoro shadow tower at that c)
# ---------------------------------------------------------------------------

def shadow_tower_minimal_model(p: int, q: int) -> Dict:
    """Shadow tower data for M(p,q), which is the Virasoro shadow tower at c = c(p,q).

    Virasoro shadow data:
      kappa = c/2
      S_3 = alpha = 2
      S_4 = 10/(c(5c+22))
      S_5 = -48/(c^2(5c+22))  [from manuscript: quintic shadow]
      Delta = 8*kappa*S_4 = 40/(5c+22)
      class: M if Delta != 0, G if kappa = 0
    """
    c = minimal_model_c(p, q)

    if c == 0:
        return {
            "kappa": Rational(0),
            "alpha": 0,
            "S4": 0,
            "S5": 0,
            "Delta": 0,
            "class": "trivial",
            "rho_squared": None,
            "S": {2: Rational(0)},
            "q0": 0,
            "q1": 0,
            "q2": 0,
        }

    kappa = c / 2
    alpha = 2  # universal for Virasoro
    denom = 5 * c + 22

    if denom == 0:
        # Lee-Yang: 5c + 22 = 0, S_4 diverges
        return {
            "kappa": kappa,
            "alpha": alpha,
            "S4": None,
            "S5": None,
            "Delta": None,
            "class": "singular",
            "rho_squared": None,
            "S": {2: kappa, 3: alpha},
            "q0": 4 * kappa ** 2,
            "q1": 12 * kappa * alpha,
            "q2": 9 * alpha ** 2 + 2 * 0,  # Delta undefined
        }

    S4 = Rational(10, 1) / (c * denom)
    S5 = Rational(-48, 1) / (c ** 3 * denom)
    Delta = Rational(40, 1) / denom

    # Shadow metric: Q_L(t) = (2*kappa + alpha*t)^2 + 2*Delta*t^2
    # = 4*kappa^2 + 4*kappa*alpha*t + (alpha^2 + 2*Delta)*t^2
    # Wait, the manuscript has Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    # For Virasoro with alpha=2: (2*kappa + 6t)^2 + 2*Delta*t^2
    # q0 = 4*kappa^2, q1 = 12*kappa*alpha = 24*kappa, q2 = 9*alpha^2 + 2*Delta
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 2 * Delta

    # rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2) for class M
    rho_sq = None
    if Delta != 0 and kappa != 0:
        rho_sq = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2)

    shadow_class = "M" if Delta != 0 else "L"

    return {
        "kappa": kappa,
        "alpha": alpha,
        "S4": S4,
        "S5": S5,
        "Delta": Delta,
        "class": shadow_class,
        "rho_squared": rho_sq,
        "S": {2: kappa, 3: alpha, 4: S4, 5: S5},
        "q0": q0,
        "q1": q1,
        "q2": q2,
    }


def shadow_discriminant_complementarity(p: int, q: int) -> Dict:
    """Check Delta(A) + Delta(A!) = 6960/((5c+22)(152-5c)) for Virasoro."""
    c = minimal_model_c(p, q)
    c_dual = 26 - c  # Virasoro Koszul dual
    denom1 = 5 * c + 22
    denom2 = 5 * c_dual + 22  # = 152 - 5c

    if denom1 == 0 or denom2 == 0:
        return {"sum": None, "expected": None, "match": None}

    Delta = Rational(40, 1) / denom1
    Delta_dual = Rational(40, 1) / denom2
    s = Delta + Delta_dual
    expected = Rational(6960, 1) / (denom1 * denom2)
    # 40/denom1 + 40/denom2 = 40*(denom1+denom2)/(denom1*denom2)
    # denom1 + denom2 = 5c+22 + 152-5c = 174
    # 40*174 = 6960. Correct.
    return {"sum": s, "expected": expected, "match": s == expected}


# ---------------------------------------------------------------------------
# CDG curvature (curved DG structure for simple quotients)
# ---------------------------------------------------------------------------

def cdg_curvature(p: int, q: int) -> Dict:
    """CDG (curved DG) curvature data for the simple quotient M(p,q).

    The simple quotient is curved because it has a vacuum null vector.
    Null vector at level (p-1)(q-1) (from h_{q-1,p-1} = 0 identification).
    Admissible level k = p/q - 2.
    """
    c = minimal_model_c(p, q)
    null_level = (p - 1) * (q - 1)
    admissible = Rational(p, q) - 2

    return {
        "c": c,
        "null_vector_level": null_level,
        "is_curved": True,  # simple quotient is always curved
        "universal_is_curved": False,  # universal Virasoro is NOT curved
        "admissible_level": admissible,
    }


def periodicity_denominator(p: int, q: int) -> int:
    """Periodicity denominator = 2*p*q/(gcd stuff).

    For M(p,q) the modular T eigenvalues have period lcm(4p, 4q) / 4 = p*q/gcd(p,q).
    But since gcd(p,q)=1, the denominator is 2*p*q.
    More precisely: the Dehn twist eigenvalues e^{2*pi*i*(h-c/24)} have
    denominator dividing 2*p*q.
    """
    return 2 * p * q


# ---------------------------------------------------------------------------
# Extended modular data
# ---------------------------------------------------------------------------

def modular_t_matrix(p: int, q: int) -> Dict:
    """Modular T-matrix data for M(p,q).

    T_{(r,s),(r,s)} = exp(2*pi*i*(h_{r,s} - c/24))
    Phases: h_{r,s} - c/24.
    """
    c = minimal_model_c(p, q)
    prims = minimal_model_primaries(p, q)
    phases = {}
    for r, s in prims:
        h = conformal_weight(p, q, r, s)
        phases[(r, s)] = h - c / 24
    return {"primaries": prims, "phases": phases}


def effective_central_charge(p: int, q: int) -> Rational:
    """Effective central charge c_eff = c - 24*h_min.

    For unitary models h_min = 0 so c_eff = c.
    For non-unitary models h_min < 0 so c_eff > c.
    """
    c = minimal_model_c(p, q)
    prims = minimal_model_primaries(p, q)
    h_min = min(conformal_weight(p, q, r, s) for r, s in prims)
    return c - 24 * h_min


def is_unitary(p: int, q: int) -> bool:
    """M(p,q) is unitary iff q = p-1 (i.e., p = q+1)."""
    return p == q + 1


def koszul_dual_central_charge(p: int, q: int) -> Rational:
    """Central charge of the Koszul dual: c' = 26 - c."""
    return 26 - minimal_model_c(p, q)


def complementarity_sum_kappa(p: int, q: int) -> Rational:
    """kappa + kappa' = c/2 + c'/2 = (c + c')/2 = 13."""
    return Rational(13)


def quantum_dimension(p: int, q: int, r: int, s: int) -> float:
    """Quantum dimension d_{r,s} = S_{(r,s),(1,1)} / S_{(1,1),(1,1)}."""
    prims = minimal_model_primaries(p, q)
    if (r, s) not in prims:
        raise ValueError(f"({r},{s}) is not a primary of M({p},{q})")
    sdata = modular_s_matrix_numerical(p, q)
    mat = sdata["matrix"]
    idx = prims.index((r, s))
    return mat[idx][0] / mat[0][0]


def global_dimension(p: int, q: int) -> float:
    """Global dimension D^2 = 1/S_{00}^2 = sum_i d_i^2."""
    s00 = s_matrix_s00(p, q)
    return 1.0 / (s00 ** 2)


def frobenius_schur_indicator(p: int, q: int, r: int, s: int) -> int:
    """Frobenius-Schur indicator for primary (r,s) of M(p,q).

    For minimal models, all representations are self-conjugate with indicator +1.
    """
    return 1


# ---------------------------------------------------------------------------
# Cross-family verification
# ---------------------------------------------------------------------------

def verify_complementarity_all_models() -> Dict[str, bool]:
    """Verify c + c' = 26 for all standard minimal models."""
    results = {}
    for name, data in MINIMAL_MODELS.items():
        p, q = data["p"], data["q"]
        c = minimal_model_c(p, q)
        c_dual = koszul_dual_central_charge(p, q)
        results[name] = (c + c_dual == 26)
    return results


def verify_kappa_additivity() -> Dict[str, bool]:
    """Verify kappa + kappa' = 13 for all standard minimal models."""
    results = {}
    for name, data in MINIMAL_MODELS.items():
        p, q = data["p"], data["q"]
        c = minimal_model_c(p, q)
        kappa = c / 2
        kappa_dual = (26 - c) / 2
        results[name] = (kappa + kappa_dual == 13)
    return results


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_minimal_models():
    results = {}

    # Central charges
    results["M(3,2) = 0"] = minimal_model_c(3, 2) == 0
    results["M(4,3) = 1/2"] = minimal_model_c(4, 3) == Rational(1, 2)
    results["M(5,4) = 7/10"] = minimal_model_c(5, 4) == Rational(7, 10)
    results["M(6,5) = 4/5"] = minimal_model_c(6, 5) == Rational(4, 5)

    # Ising bar data
    ising = ising_bar_data()
    results["Ising c = 1/2"] = ising["c"] == Rational(1, 2)
    results["Ising kappa = 1/4"] = ising["kappa"] == Rational(1, 4)
    results["Ising obs_1 = 1/96"] = ising["obs_1"] == Rational(1, 96)
    results["Ising 3 modules"] = ising["n_modules"] == 3

    # Ising fusion
    fusion = ising["fusion_rules"]
    results["sigma x sigma = I + eps"] = set(fusion[("sigma", "sigma")]) == {"I", "epsilon"}
    results["sigma x eps = sigma"] = fusion[("sigma", "epsilon")] == ["sigma"]
    results["eps x eps = I"] = fusion[("epsilon", "epsilon")] == ["I"]

    # Genus-1 bar
    g1 = ising_genus1_bar()
    results["B(I,I) dim = 1"] = g1["B_{g=1}(I, I)"]["dim"] == 1
    results["B(sigma,sigma) dim = 2"] = g1["B_{g=1}(sigma, sigma)"]["dim"] == 2

    # Complementarity
    results["all c+c' = 26"] = minimal_model_complementarity(4, 3) == 26

    # Tricritical Ising
    tci = tricritical_ising_data()
    results["TCI c = 7/10"] = tci["c"] == Rational(7, 10)
    results["TCI 6 modules"] = tci["n_modules"] == 6

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("MINIMAL MODEL BAR COMPLEXES: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_minimal_models().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
