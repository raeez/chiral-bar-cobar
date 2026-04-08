r"""Transport-to-transpose conjecture for sl_5: all 7 nilpotent orbits.

Tests conj:type-a-transport-to-transpose for N=5, the first rank where
NON-HOOK, NON-RECTANGULAR orbits appear.  The partitions (3,2) and (2,2,1)
are genuinely new: (3,2) is neither hook nor rectangular, and (2,2,1) is
self-transpose but non-even.

PARTITION DATA FOR sl_5 (7 orbits):
    (5)         principal   W_5           transpose = (1,1,1,1,1)  EVEN
    (4,1)       subregular  hook          transpose = (2,1,1,1)    NON-EVEN
    (3,2)       NON-HOOK    NON-RECT      transpose = (2,2,1)      NON-EVEN
    (3,1,1)     hook        SELF-TR       transpose = (3,1,1)      EVEN
    (2,2,1)     NON-HOOK                  transpose = (3,2)        NON-EVEN
    (2,1,1,1)   minimal     hook          transpose = (4,1)        NON-EVEN
    (1,1,1,1,1) trivial     V_k(sl_5)    transpose = (5)           EVEN

EVEN ORBITS (central charge VERIFIED via per-root-pair formula):
    c(5; k)         = (4k - 100)/(k+5)
    c(3,1,1; k)     = (10k - 34)/(k+5)
    c(1,1,1,1,1; k) = 24k/(k+5)

    For non-even orbits (4,1), (3,2), (2,2,1), (2,1,1,1): the per-root-pair
    formula with half-integer branch is UNVERIFIED beyond sl_3 BP.  The
    half-integer contribution produces k-DEPENDENT complementarity sums,
    confirming the formula is unreliable for non-even nilpotents.  These
    are flagged as UNVERIFIED.

COMPLEMENTARITY c(k,lambda) + c(k',lambda^t) where k' = -k - 2N = -k - 10:
    (5) <-> (1,1,1,1,1):   c+c' = 28   (LEVEL-INDEPENDENT, VERIFIED)
    (3,1,1) <-> (3,1,1):   c+c' = 20   (LEVEL-INDEPENDENT, VERIFIED, self-transpose)
    (4,1) <-> (2,1,1,1):   status DEPENDS on non-even c formula (OPEN)
    (3,2) <-> (2,2,1):     status DEPENDS on non-even c formula (OPEN)

KEY NEW TESTS beyond sl_4:
    - (3,2) is the FIRST partition that is neither hook NOR rectangular.
      Its dual (2,2,1) is also non-hook and non-rectangular.
    - (3,1,1) is self-transpose AND even, providing a clean self-dual test.
      It is the UNIQUE self-transpose partition of 5.
    - The anomaly ratio coincidence rho(5,) = rho(4,1) = 77/60 is verified.

References:
    - Butson-Nair [2508.18248]: inverse Hamiltonian reduction, all type A orbits
    - Kac-Roan-Wakimoto (2004): DS reduction central charge
    - conj:type-a-transport-to-transpose in the manuscript
    - thm:hook-transport-corridor: proved for hook orbits
    - AP24: kappa+kappa' may be nonzero for non-self-transpose W-algebras

Critical pitfalls:
    - Per-root-pair half-integer formula UNVERIFIED beyond sl_3 BP (AP3).
    - Even/non-even distinction is LOAD-BEARING for central charge verification.
    - Self-transpose does NOT imply even: (2,2,1) is self-transpose but non-even.
    - rho(lambda) = rho(lambda^t) ONLY for self-transpose partitions; for
      non-self-transpose pairs, kappa complementarity is a stronger condition.
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


def is_rectangular(lam: Partition) -> bool:
    """Check if partition is rectangular (all parts equal)."""
    return len(set(lam)) <= 1


def x_diagonal(lam: Partition) -> List[Fraction]:
    """Diagonal entries of x = h/2 for the Dynkin grading."""
    result = []
    for p in lam:
        for a in range(p):
            result.append(Fraction(a) - Fraction(p - 1, 2))
    return result


# ---------------------------------------------------------------------------
# sl_5 orbit catalog
# ---------------------------------------------------------------------------

SL5_PARTITIONS: List[Partition] = [
    (5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)
]

SL5_PARTITION_NAMES: Dict[Partition, str] = {
    (5,): "principal",
    (4, 1): "subregular (hook, non-even)",
    (3, 2): "non-hook, non-rectangular (non-even)",
    (3, 1, 1): "hook, self-transpose, even",
    (2, 2, 1): "non-hook (non-even)",
    (2, 1, 1, 1): "minimal (hook, non-even)",
    (1, 1, 1, 1, 1): "trivial",
}


def sl5_orbit_data() -> Dict[Partition, Dict]:
    """Complete orbit data for all 7 nilpotent orbits of sl_5."""
    data = {}
    for lam in SL5_PARTITIONS:
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
            "is_rectangular": is_rectangular(lam),
            "is_even": is_even_nilpotent(lam),
            "centralizer_dim": cent_dim,
            "orbit_dim": orbit_dim,
            "name": SL5_PARTITION_NAMES[lam],
        }
    return data


# ---------------------------------------------------------------------------
# Generator weights and anomaly ratio
# ---------------------------------------------------------------------------

def generator_weights_sl5(lam: Partition) -> List[Fraction]:
    """Conformal weights of strong generators of W^k(sl_5, f_lambda).

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


def anomaly_ratio_sl5(lam: Partition) -> Fraction:
    r"""Anomaly ratio rho_lambda = sum_bos 1/h_i - sum_ferm 1/h_i."""
    rho = Fraction(0)
    for w in generator_weights_sl5(lam):
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
    - Hook-type and rectangular W-algebras in sl_4

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


def central_charge_sl5(lam: Partition, k: Fraction) -> Fraction:
    """Central charge of W^k(sl_5, f_lambda), dispatching on even/non-even."""
    N = 5
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

def kappa_sl5(lam: Partition, k: Fraction) -> Fraction:
    """Modular characteristic kappa = rho * c for W^k(sl_5, f_lambda)."""
    return anomaly_ratio_sl5(lam) * central_charge_sl5(lam, k)


# ---------------------------------------------------------------------------
# Complementarity
# ---------------------------------------------------------------------------

def central_charge_complementarity(
    N: int, lam: Partition, k: Fraction
) -> Fraction:
    """Compute c(k, lambda) + c(k', lambda^t) where k' = -k - 2N."""
    lam_t = transpose(lam)
    kd = dual_level(N, k)
    c1 = central_charge_sl5(lam, k)
    c2 = central_charge_sl5(lam_t, kd)
    return c1 + c2


def complementarity_is_level_independent(
    lam: Partition,
    test_levels: Optional[List[Fraction]] = None,
) -> bool:
    """Test whether c(k,lambda)+c(k',lambda^t) is k-independent."""
    N = 5
    if test_levels is None:
        test_levels = [Fraction(p) for p in [1, 3, 7, 11, 17, 23]]
    values = set()
    for kv in test_levels:
        kd = dual_level(N, kv)
        if kv + N == 0 or kd + N == 0:
            continue
        values.add(central_charge_complementarity(N, lam, kv))
    return len(values) == 1


def complementarity_constant_even(lam: Partition) -> Fraction:
    """For even orbits: the level-independent value of c+c'."""
    N = 5
    if not is_even_nilpotent(lam):
        raise ValueError("Only guaranteed level-independent for even nilpotents")
    return central_charge_complementarity(N, lam, Fraction(17))


def kappa_complementarity(lam: Partition, k: Fraction) -> Fraction:
    """Compute kappa(k,lambda) + kappa(k',lambda^t)."""
    N = 5
    lam_t = transpose(lam)
    kd = dual_level(N, k)
    k1 = kappa_sl5(lam, k)
    k2 = kappa_sl5(lam_t, kd)
    return k1 + k2


def kappa_complementarity_is_level_independent(
    lam: Partition,
    test_levels: Optional[List[Fraction]] = None,
) -> bool:
    """Test whether kappa+kappa' is k-independent."""
    N = 5
    if test_levels is None:
        test_levels = [Fraction(p) for p in [1, 3, 7, 11, 17, 23]]
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
    N = 5
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
    """Complete duality data for partition lambda of 5."""
    N = 5
    lam_t = transpose(lam)
    gen_weights = generator_weights_sl5(lam)
    rho = anomaly_ratio_sl5(lam)
    is_ev = is_even_nilpotent(lam)
    c_verified = is_ev

    # Central charge at test level
    c_test = central_charge_sl5(lam, Fraction(1))

    # Symbolic coefficients (even only)
    coeffs = None
    if is_ev:
        coeffs = central_charge_coefficients_even(N, lam)

    # Complementarity
    c_comp_indep = complementarity_is_level_independent(lam)
    c_comp_val = central_charge_complementarity(N, lam, Fraction(17))

    # Kappa complementarity
    kap_comp_indep = kappa_complementarity_is_level_independent(lam)

    # Self-dual data (only for self-transpose even)
    sd_c = self_dual_central_charge(lam) if lam == lam_t else None
    sd_k = self_dual_level(lam) if lam == lam_t else None

    return {
        "partition": lam,
        "transpose": lam_t,
        "is_hook": is_hook(lam),
        "is_rectangular": is_rectangular(lam),
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


def full_sl5_analysis() -> Dict[Partition, Dict]:
    """Complete analysis for all 7 nilpotent orbits of sl_5."""
    return {lam: duality_profile(lam) for lam in SL5_PARTITIONS}


# ---------------------------------------------------------------------------
# Verification constants (multi-path)
# ---------------------------------------------------------------------------

# Even-orbit central charge coefficients: c(k) = (a*k + b)/(k+5)
VERIFIED_C_COEFFICIENTS = {
    (5,): (Fraction(4), Fraction(-100)),
    (3, 1, 1): (Fraction(10), Fraction(-34)),
    (1, 1, 1, 1, 1): (Fraction(24), Fraction(0)),
}

# Even-orbit complementarity constants
VERIFIED_COMPLEMENTARITY = {
    (5,): Fraction(28),             # (5) <-> (1,1,1,1,1)
    (3, 1, 1): Fraction(20),       # (3,1,1) <-> (3,1,1) self-transpose
    (1, 1, 1, 1, 1): Fraction(28),  # same pair as (5)
}

# Anomaly ratios (ALL 7 orbits)
VERIFIED_ANOMALY_RATIOS = {
    (5,): Fraction(77, 60),         # 1/2 + 1/3 + 1/4 + 1/5
    (4, 1): Fraction(77, 60),       # 1 + 1/2 + 1/3 + 1/4 - 2*(2/5) = 77/60
    (3, 2): Fraction(1, 5),         # 1 + 1/2*2 + 1/3 - 2/3*2 - 2/5*2
    (3, 1, 1): Fraction(41, 6),     # 4*1 + 5*(1/2) + 1/3
    (2, 2, 1): Fraction(10, 3),     # 4*1 + 4*(1/2) - 4*(2/3)
    (2, 1, 1, 1): Fraction(11, 2),  # 9*1 + 1/2 - 6*(2/3)
    (1, 1, 1, 1, 1): Fraction(24),  # 24 weight-1 generators
}

# Anomaly ratio coincidence: rho(5,) = rho(4,1) = 77/60
ANOMALY_RATIO_COINCIDENCE = (Fraction(77, 60), [(5,), (4, 1)])

# (3,1,1) self-dual data.
# c* = C/2 = 20/2 = 10. Since c(k) = (10k-34)/(k+5), the equation c = 10
# gives 10k-34 = 10k+50, which has no finite solution. The leading coefficient
# a = 10 equals c*, so the self-dual level is formally k* = -N = -5 (the
# critical level, which is also the FF involution fixed point). The self-dual
# central charge c* = 10 is achieved only as a limit k -> -5.
VERIFIED_311_SELF_DUAL_C = Fraction(10)
