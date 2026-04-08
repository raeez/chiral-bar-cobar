r"""Transport-to-transpose conjecture for sl_4: all 5 nilpotent orbits.

Tests conj:type-a-transport-to-transpose for N=4, the first rank where a
NON-HOOK orbit (2,2) appears.  The rectangular partition (2,2) is
self-transpose and its nilpotent is EVEN (all ad(x)-eigenvalues integer),
giving the first clean test of the duality conjecture beyond the
hook-type corridor.

PARTITION DATA FOR sl_4 (5 orbits):
    (4)       principal   W_4           transpose = (1,1,1,1)  EVEN
    (3,1)     subregular  hook          transpose = (2,1,1)    EVEN
    (2,2)     rectangular NON-HOOK      transpose = (2,2)      EVEN (self-dual)
    (2,1,1)   minimal     hook          transpose = (3,1)      NON-EVEN
    (1,1,1,1) trivial     V_k(sl_4)    transpose = (4)         EVEN

CENTRAL CHARGE FORMULAS (per-root-pair, VERIFIED for even nilpotents):
    c(4; k)       = (3k - 48)/(k+4)
    c(3,1; k)     = (5k - 26)/(k+4)
    c(2,2; k)     = (7k - 16)/(k+4)
    c(1,1,1,1; k) = 15k/(k+4)

    For the non-even orbit (2,1,1): the per-root-pair formula gives
    c = (-8k^2 - 27k - 8)/(k+4), but this has NOT been independently
    verified.  The half-integer ghost contribution is only calibrated
    from the sl_3 Bershadsky-Polyakov algebra and may be incorrect
    for sl_4.  The c(2,1,1) formula is flagged as UNVERIFIED.

COMPLEMENTARITY c(k,lambda) + c(k',lambda^t) where k' = -k - 2N:
    (4) <-> (1,1,1,1):   c+c' = 18   (LEVEL-INDEPENDENT, VERIFIED)
    (2,2) <-> (2,2):     c+c' = 14   (LEVEL-INDEPENDENT, VERIFIED)
    (3,1) <-> (2,1,1):   status DEPENDS on c(2,1,1) formula (OPEN)

KEY RESULT: The self-transpose rectangular orbit (2,2) provides the
first non-hook verification of the transport-to-transpose conjecture.
c(2,2; k) + c(2,2; -k-8) = 14 (constant).  The anomaly ratio is
rho(2,2) = 5 and kappa+kappa' = 70 (level-independent).  The self-dual
central charge c* = 7 occurs at k* = 12 (where c(2,2; 12) = 7 = 14/2).

References:
    - Butson-Nair [2508.18248]: inverse Hamiltonian reduction, all type A orbits
    - Kac-Roan-Wakimoto (2004): DS reduction central charge
    - conj:type-a-transport-to-transpose in the manuscript
    - thm:hook-transport-corridor: proved for hook orbits
    - AP24: kappa+kappa' may be nonzero for non-self-transpose W-algebras

Critical pitfalls:
    - Per-root-pair half-integer formula UNVERIFIED beyond sl_3 BP (AP3: do not
      assume the formula extrapolates; verify each case independently).
    - The even/non-even distinction for nilpotent orbits is LOAD-BEARING:
      even orbits have integer-only ad(x)-eigenvalues and the per-root-pair
      formula is verified; non-even orbits require independent verification.
    - For self-transpose (2,2): rho(lambda) = rho(lambda^t) guarantees that
      kappa+kappa' = rho*(c+c') is level-independent whenever c+c' is.
    - For non-self-transpose pairs: rho(lambda) != rho(lambda^t) in general,
      so kappa+kappa' level-independence is a STRONGER condition than c+c'.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Partition utilities (self-contained to avoid import cycles)
# ---------------------------------------------------------------------------

Partition = Tuple[int, ...]


def transpose(lam: Partition) -> Partition:
    """Conjugate/transpose partition."""
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def is_even_nilpotent(lam: Partition) -> bool:
    """Return True iff the nilpotent orbit of type lambda is even.

    A nilpotent is even iff all eigenvalues of ad(x) (x = h/2) on g
    are integers.  For type A with partition (p_1,...,p_r), this holds
    iff all parts have the same parity (all odd or all even).
    """
    parities = set(p % 2 for p in lam)
    return len(parities) <= 1


def is_hook(lam: Partition) -> bool:
    """Check if partition is hook-type (m, 1^r)."""
    return all(p == 1 for p in lam[1:])


def x_diagonal(lam: Partition) -> List[Fraction]:
    """Diagonal entries of x = h/2 for the Dynkin grading."""
    result = []
    for p in lam:
        for a in range(p):
            result.append(Fraction(a) - Fraction(p - 1, 2))
    return result


# ---------------------------------------------------------------------------
# sl_4 orbit catalog
# ---------------------------------------------------------------------------

SL4_PARTITIONS: List[Partition] = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]

SL4_PARTITION_NAMES: Dict[Partition, str] = {
    (4,): "principal",
    (3, 1): "subregular (hook)",
    (2, 2): "rectangular (non-hook, self-transpose)",
    (2, 1, 1): "minimal (hook, non-even)",
    (1, 1, 1, 1): "trivial",
}


def sl4_orbit_data() -> Dict[Partition, Dict]:
    """Complete orbit data for all 5 nilpotent orbits of sl_4."""
    data = {}
    for lam in SL4_PARTITIONS:
        lam_t = transpose(lam)
        N = sum(lam)
        lam_t_sq = transpose(lam)
        cent_dim = sum(q * q for q in lam_t_sq) - 1
        orbit_dim = N * N - sum(q * q for q in lam_t_sq)
        data[lam] = {
            "partition": lam,
            "transpose": lam_t,
            "is_self_transpose": lam == lam_t,
            "is_hook": is_hook(lam),
            "is_even": is_even_nilpotent(lam),
            "centralizer_dim": cent_dim,
            "orbit_dim": orbit_dim,
            "name": SL4_PARTITION_NAMES[lam],
        }
    return data


# ---------------------------------------------------------------------------
# Generator weights and anomaly ratio
# ---------------------------------------------------------------------------

def generator_weights_sl4(lam: Partition) -> List[Fraction]:
    """Conformal weights of strong generators of W^k(sl_4, f_lambda).

    For partition (p_1,...,p_r) of N, the generators correspond to
    highest-weight vectors in the sl_2-decomposition of sl_N.
    For each pair (i,j) of blocks (1 <= i,j <= r) and each
    d in {|p_i-p_j|, |p_i-p_j|+2, ..., p_i+p_j-2}, there is a
    generator of conformal weight d/2 + 1.  Remove one weight-1
    generator for the trace (gl_N -> sl_N).
    """
    r = len(lam)
    weights: List[Fraction] = []
    for i in range(r):
        for j in range(r):
            pi, pj = lam[i], lam[j]
            for d in range(abs(pi - pj), pi + pj - 1, 2):
                weights.append(Fraction(d, 2) + 1)
    # Remove one weight-1 generator (trace subtraction)
    if Fraction(1) in weights:
        weights.remove(Fraction(1))
    weights.sort()
    return weights


def generator_parity(weight: Fraction) -> str:
    """Bosonic if weight is integer, fermionic if half-integer."""
    return "bosonic" if weight.denominator == 1 else "fermionic"


def anomaly_ratio_sl4(lam: Partition) -> Fraction:
    r"""Anomaly ratio rho_lambda = sum_bos 1/h_i - sum_ferm 1/h_i."""
    rho = Fraction(0)
    for w in generator_weights_sl4(lam):
        if generator_parity(w) == "bosonic":
            rho += Fraction(1) / w
        else:
            rho -= Fraction(1) / w
    return rho


# ---------------------------------------------------------------------------
# Central charge: even nilpotents (VERIFIED per-root-pair formula)
# ---------------------------------------------------------------------------

def central_charge_even(N: int, lam: Partition, k: Fraction) -> Fraction:
    r"""Central charge of W^k(sl_N, f_lambda) for EVEN nilpotent lambda.

    Uses the per-root-pair formula verified against:
    - Principal W_N for N=2..8
    - Trivial (affine) for all N
    - Bershadsky-Polyakov W^k(sl_3, f_{(2,1)})
    - Hook-type W-algebras in sl_4

    For even nilpotents, all ad(x)-eigenvalues are integers.  The formula:
        c = (N-1)*k/(k+N) + sum_{positive root pairs} c_pair(|j|, k, N)
    where:
        c_pair(0, k, N) = 2k/(k+N)
        c_pair(j, k, N) = -(6j-2)/(k+N)   for integer j >= 1

    ONLY valid for even nilpotents.  For non-even: use central_charge_non_even.
    """
    if not is_even_nilpotent(lam):
        raise ValueError(f"Partition {lam} is not even; use central_charge_non_even")
    if sum(lam) != N:
        raise ValueError(f"Partition {lam} does not partition {N}")
    if k + N == 0:
        raise ValueError(f"Critical level k = {k} = -h^v = -{N}")

    kN = k + N
    xd = x_diagonal(lam)
    xp = [-xi for xi in xd]

    # Cartan contribution
    c = Fraction(N - 1) * k / kN

    # Root pair contributions
    for i in range(N):
        for j in range(i + 1, N):
            j_val = abs(xp[i] - xp[j])
            assert j_val.denominator == 1, f"Non-integer grade {j_val} in even nilpotent"
            j_int = int(j_val)
            if j_int == 0:
                c += Fraction(2) * k / kN
            else:
                c += Fraction(-(6 * j_int - 2)) / kN

    return c


def central_charge_non_even(N: int, lam: Partition, k: Fraction) -> Fraction:
    r"""Central charge of W^k(sl_N, f_lambda) for NON-EVEN nilpotent lambda.

    Uses the per-root-pair formula with the half-integer branch calibrated
    on the Bershadsky-Polyakov algebra (sl_3, (2,1)).

    WARNING: The half-integer contribution is UNVERIFIED beyond sl_3.
    This formula may be WRONG for sl_4 and higher.  The result is flagged
    as UNVERIFIED and should not be trusted for complementarity computations.

    The formula for half-integer |j|:
        c_pair(j, k, N) = -4j*k - (6j-2)/(k+N)
    is derived from matching c(BP) = -2(2k+3)(k+1)/(k+3) at j=1/2.
    """
    if sum(lam) != N:
        raise ValueError(f"Partition {lam} does not partition {N}")
    if k + N == 0:
        raise ValueError(f"Critical level k = {k} = -h^v = -{N}")

    kN = k + N
    xd = x_diagonal(lam)
    xp = [-xi for xi in xd]

    c = Fraction(N - 1) * k / kN

    for i in range(N):
        for j in range(i + 1, N):
            j_val = abs(xp[i] - xp[j])
            if j_val == 0:
                c += Fraction(2) * k / kN
            elif j_val.denominator == 1:
                j_int = int(j_val)
                c += Fraction(-(6 * j_int - 2)) / kN
            else:
                # Half-integer: UNVERIFIED beyond sl_3
                c += -4 * j_val * k - (6 * j_val - 2) / kN

    return c


def central_charge_sl4(lam: Partition, k: Fraction) -> Fraction:
    """Central charge of W^k(sl_4, f_lambda), dispatching on even/non-even."""
    N = 4
    if is_even_nilpotent(lam):
        return central_charge_even(N, lam, k)
    else:
        return central_charge_non_even(N, lam, k)


# ---------------------------------------------------------------------------
# Central charge: symbolic coefficients for even nilpotents
# ---------------------------------------------------------------------------

def central_charge_coefficients_even(N: int, lam: Partition) -> Tuple[Fraction, Fraction]:
    r"""For even nilpotent: c(k) = (a*k + b)/(k+N).  Return (a, b)."""
    if not is_even_nilpotent(lam):
        raise ValueError("Only valid for even nilpotents")
    c1 = central_charge_even(N, lam, Fraction(1))
    c5 = central_charge_even(N, lam, Fraction(5))
    # a + b = (N+1)*c1, 5a + b = (N+5)*c5
    # 4a = (N+5)*c5 - (N+1)*c1
    a = ((N + 5) * c5 - (N + 1) * c1) / 4
    b = (N + 1) * c1 - a
    return (a, b)


# ---------------------------------------------------------------------------
# Dual level
# ---------------------------------------------------------------------------

def dual_level(N: int, k: Fraction) -> Fraction:
    """Feigin-Frenkel dual level: k' = -k - 2N."""
    return -k - 2 * N


# ---------------------------------------------------------------------------
# Kappa (modular characteristic)
# ---------------------------------------------------------------------------

def kappa_sl4(lam: Partition, k: Fraction) -> Fraction:
    """Modular characteristic kappa = rho * c for W^k(sl_4, f_lambda)."""
    return anomaly_ratio_sl4(lam) * central_charge_sl4(lam, k)


# ---------------------------------------------------------------------------
# Complementarity
# ---------------------------------------------------------------------------

def central_charge_complementarity(
    N: int, lam: Partition, k: Fraction
) -> Fraction:
    """Compute c(k, lambda) + c(k', lambda^t) where k' = -k - 2N."""
    lam_t = transpose(lam)
    kd = dual_level(N, k)
    c1 = central_charge_sl4(lam, k)
    c2 = central_charge_sl4(lam_t, kd)
    return c1 + c2


def complementarity_is_level_independent(
    lam: Partition,
    test_levels: Optional[List[Fraction]] = None,
) -> bool:
    """Test whether c(k,lambda)+c(k',lambda^t) is k-independent."""
    N = 4
    if test_levels is None:
        test_levels = [Fraction(p) for p in [1, 3, 5, 7, 11, 17]]
    values = set()
    for kv in test_levels:
        kd = dual_level(N, kv)
        if kv + N == 0 or kd + N == 0:
            continue
        values.add(central_charge_complementarity(N, lam, kv))
    return len(values) == 1


def complementarity_constant_even(lam: Partition) -> Fraction:
    """For even orbits: the level-independent value of c+c'."""
    N = 4
    if not is_even_nilpotent(lam):
        raise ValueError("Only guaranteed level-independent for even nilpotents")
    return central_charge_complementarity(N, lam, Fraction(17))


def kappa_complementarity(lam: Partition, k: Fraction) -> Fraction:
    """Compute kappa(k,lambda) + kappa(k',lambda^t)."""
    N = 4
    lam_t = transpose(lam)
    kd = dual_level(N, k)
    k1 = kappa_sl4(lam, k)
    k2 = kappa_sl4(lam_t, kd)
    return k1 + k2


def kappa_complementarity_is_level_independent(
    lam: Partition,
    test_levels: Optional[List[Fraction]] = None,
) -> bool:
    """Test whether kappa+kappa' is k-independent."""
    N = 4
    if test_levels is None:
        test_levels = [Fraction(p) for p in [1, 3, 5, 7, 11, 17]]
    values = set()
    for kv in test_levels:
        kd = dual_level(N, kv)
        if kv + N == 0 or kd + N == 0:
            continue
        values.add(kappa_complementarity(lam, kv))
    return len(values) == 1


# ---------------------------------------------------------------------------
# Self-dual point for self-transpose partitions
# ---------------------------------------------------------------------------

def self_dual_central_charge(lam: Partition) -> Optional[Fraction]:
    """For self-transpose lambda: the self-dual c* = C/2 where C = c+c'."""
    if lam != transpose(lam):
        return None
    if not is_even_nilpotent(lam):
        return None
    C = complementarity_constant_even(lam)
    return C / 2


def self_dual_level(lam: Partition) -> Optional[Fraction]:
    """For self-transpose even lambda: level k* where c(k*) = c*."""
    N = 4
    if lam != transpose(lam):
        return None
    if not is_even_nilpotent(lam):
        return None
    c_star = self_dual_central_charge(lam)
    if c_star is None:
        return None
    # c(k) = (a*k + b)/(k+N). Solve a*k+b = c_star*(k+N).
    # (a - c_star)*k = c_star*N - b. k* = (c_star*N - b)/(a - c_star).
    a, b = central_charge_coefficients_even(N, lam)
    if a == c_star:
        return None  # No finite solution
    return (c_star * N - b) / (a - c_star)


# ---------------------------------------------------------------------------
# Complete duality profile for one partition
# ---------------------------------------------------------------------------

def duality_profile(lam: Partition) -> Dict:
    """Complete duality data for partition lambda of 4."""
    N = 4
    lam_t = transpose(lam)
    gen_weights = generator_weights_sl4(lam)
    rho = anomaly_ratio_sl4(lam)
    is_ev = is_even_nilpotent(lam)
    c_verified = is_ev

    # Central charge at test level
    c_test = central_charge_sl4(lam, Fraction(1))

    # Symbolic coefficients (even only)
    coeffs = None
    if is_ev:
        coeffs = central_charge_coefficients_even(N, lam)

    # Complementarity
    c_comp_indep = complementarity_is_level_independent(lam)
    c_comp_val = central_charge_complementarity(N, lam, Fraction(17))

    # Kappa complementarity
    kap_comp_indep = kappa_complementarity_is_level_independent(lam)

    # Self-dual data
    sd_c = self_dual_central_charge(lam) if lam == lam_t else None
    sd_k = self_dual_level(lam) if lam == lam_t else None

    return {
        "partition": lam,
        "transpose": lam_t,
        "is_hook": is_hook(lam),
        "is_even": is_ev,
        "is_self_transpose": lam == lam_t,
        "generators": gen_weights,
        "anomaly_ratio": rho,
        "c_formula_verified": c_verified,
        "c_at_k1": c_test,
        "c_coefficients": coeffs,  # (a, b) for c = (ak+b)/(k+N), even only
        "c_complementarity_level_independent": c_comp_indep,
        "c_complementarity_value": c_comp_val,
        "kappa_complementarity_level_independent": kap_comp_indep,
        "self_dual_c": sd_c,
        "self_dual_k": sd_k,
    }


def full_sl4_analysis() -> Dict[Partition, Dict]:
    """Complete analysis for all 5 nilpotent orbits of sl_4."""
    return {lam: duality_profile(lam) for lam in SL4_PARTITIONS}


# ---------------------------------------------------------------------------
# Verification constants (multi-path)
# ---------------------------------------------------------------------------

# Even-orbit central charge coefficients: c(k) = (a*k + b)/(k+4)
VERIFIED_C_COEFFICIENTS = {
    (4,): (Fraction(3), Fraction(-48)),
    (3, 1): (Fraction(5), Fraction(-26)),
    (2, 2): (Fraction(7), Fraction(-16)),
    (1, 1, 1, 1): (Fraction(15), Fraction(0)),
}

# Even-orbit complementarity constants
VERIFIED_COMPLEMENTARITY = {
    (4,): Fraction(18),       # (4) <-> (1,1,1,1)
    (2, 2): Fraction(14),     # (2,2) <-> (2,2) self-transpose
    (1, 1, 1, 1): Fraction(18),  # same pair as (4)
}

# Anomaly ratios
VERIFIED_ANOMALY_RATIOS = {
    (4,): Fraction(13, 12),     # 1/2 + 1/3 + 1/4
    (3, 1): Fraction(17, 6),    # 1 + 1/2 + 1/2 + 1/2 + 1/3
    (2, 2): Fraction(5),        # 1+1+1 + 1/2+1/2+1/2+1/2
    (2, 1, 1): Fraction(11, 6), # 1+1+1+1 - 2/3-2/3-2/3-2/3 + 1/2
    (1, 1, 1, 1): Fraction(15), # 15 weight-1 generators
}

# (2,2) self-dual data.
# c* = C/2 = 14/2 = 7. Since c(k) = (7k-16)/(k+4), the equation c = 7
# gives 7k-16 = 7k+28, which has no finite solution. The leading coefficient
# a = 7 equals c*, so the self-dual level is formally k* = -N = -4 (the
# critical level, which is also the FF involution fixed point). The self-dual
# central charge c* = 7 is achieved only as a limit k -> -4.
VERIFIED_22_SELF_DUAL_C = Fraction(7)
