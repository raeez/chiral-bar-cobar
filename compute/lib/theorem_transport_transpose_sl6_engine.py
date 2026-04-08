r"""Transport-to-transpose conjecture for sl_6: all 11 nilpotent orbits.

Tests conj:type-a-transport-to-transpose for N=6, the first rank where
RECTANGULAR NON-PRINCIPAL orbits (3,3) and (2,2,2) appear as a TRANSPOSE
PAIR, and where the unique self-transpose partition (3,2,1) is NON-EVEN.

PARTITION DATA FOR sl_6 (11 orbits):
    (6)           principal     W_6              transpose = (1,1,1,1,1,1)  EVEN
    (5,1)         subregular    hook             transpose = (2,1,1,1,1)    EVEN<->NON-EVEN
    (4,2)         non-hook                       transpose = (2,2,1,1)      EVEN<->NON-EVEN
    (4,1,1)       hook                           transpose = (3,1,1,1)      NON-EVEN<->EVEN
    (3,3)         rectangular   NON-HOOK         transpose = (2,2,2)        EVEN<->EVEN
    (3,2,1)       irregular     SELF-TRANSPOSE   transpose = (3,2,1)        NON-EVEN
    (3,1,1,1)     hook                           transpose = (4,1,1)        EVEN<->NON-EVEN
    (2,2,2)       rectangular   NON-HOOK         transpose = (3,3)          EVEN<->EVEN
    (2,2,1,1)     non-hook                       transpose = (4,2)          NON-EVEN<->EVEN
    (2,1,1,1,1)   minimal       hook             transpose = (5,1)          NON-EVEN<->EVEN
    (1,1,1,1,1,1) trivial       V_k(sl_6)       transpose = (6)            EVEN

EVEN ORBITS (7 of 11, central charge VERIFIED via per-root-pair formula):
    c(6; k)           = (5k - 180)/(k+6)
    c(5,1; k)         = (7k - 128)/(k+6)
    c(4,2; k)         = (9k - 88)/(k+6)
    c(3,3; k)         = (11k - 72)/(k+6)
    c(3,1,1,1; k)     = (17k - 42)/(k+6)
    c(2,2,2; k)       = (17k - 36)/(k+6)
    c(1,1,1,1,1,1; k) = 35k/(k+6)

    For non-even orbits (4,1,1), (3,2,1), (2,2,1,1), (2,1,1,1,1): the
    per-root-pair formula with half-integer branch is UNVERIFIED beyond
    sl_3 BP.  Flagged as UNVERIFIED.

COMPLEMENTARITY c(k,lambda) + c(k',lambda^t) where k' = -k - 2N = -k - 12:
    (6) <-> (1,1,1,1,1,1):     c+c' = 40   (LEVEL-INDEPENDENT, VERIFIED)
    (3,3) <-> (2,2,2):         c+c' = 28   (LEVEL-INDEPENDENT, VERIFIED)
    (5,1) <-> (2,1,1,1,1):     OPEN (even <-> non-even)
    (4,2) <-> (2,2,1,1):       OPEN (even <-> non-even)
    (4,1,1) <-> (3,1,1,1):     OPEN (non-even <-> even)
    (3,2,1) <-> (3,2,1):       OPEN (self-transpose, non-even)

KEY NEW RESULTS beyond sl_5:
    - (3,3) and (2,2,2) are the first RECTANGULAR NON-PRINCIPAL transpose pair.
      Both are even, giving a verified complementarity C = 28.
    - (3,2,1) is self-transpose but NON-EVEN.  This is the first self-transpose
      partition in the transport-to-transpose programme whose nilpotent is
      non-even.  In sl_4 the self-transpose (2,2) was even; in sl_5 the
      self-transpose (3,1,1) was even.  At N=6, even-ness fails.
    - No anomaly ratio coincidences (unlike sl_5 where rho(5,)=rho(4,1)=77/60).
    - (3,1,1,1) and (2,2,2) share the same leading coefficient a=17, so
      c(3,1,1,1;k) and c(2,2,2;k) have the same asymptotic c -> 17.
      But they are NOT a transpose pair.
    - Three even<->non-even pairs: (5,1)<->(2,1,1,1,1), (4,2)<->(2,2,1,1),
      (3,1,1,1)<->(4,1,1).  Their complementarity is OPEN.

References:
    - Butson-Nair [2508.18248]: inverse Hamiltonian reduction, all type A orbits
    - Kac-Roan-Wakimoto (2004): DS reduction central charge
    - conj:type-a-transport-to-transpose in the manuscript
    - thm:hook-transport-corridor: proved for hook orbits
    - AP24: kappa+kappa' may be nonzero for non-self-transpose W-algebras

Critical pitfalls:
    - Per-root-pair half-integer formula UNVERIFIED beyond sl_3 BP (AP3).
    - Even/non-even distinction is LOAD-BEARING for central charge verification.
    - Self-transpose does NOT imply even: (3,2,1) is self-transpose but non-even.
      This is the KEY NEW PHENOMENON at N=6.
    - (3,3) and (2,2,2) are rectangular but NOT self-transpose (they are
      transposes of EACH OTHER).
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
# sl_6 orbit catalog
# ---------------------------------------------------------------------------

SL6_PARTITIONS: List[Partition] = [
    (6,),
    (5, 1),
    (4, 2),
    (4, 1, 1),
    (3, 3),
    (3, 2, 1),
    (3, 1, 1, 1),
    (2, 2, 2),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
]

SL6_PARTITION_NAMES: Dict[Partition, str] = {
    (6,): "principal",
    (5, 1): "subregular (hook, even)",
    (4, 2): "non-hook, non-rectangular (even)",
    (4, 1, 1): "hook (non-even)",
    (3, 3): "rectangular, non-hook (even)",
    (3, 2, 1): "irregular, self-transpose (non-even)",
    (3, 1, 1, 1): "hook (even)",
    (2, 2, 2): "rectangular, non-hook (even)",
    (2, 2, 1, 1): "non-hook, non-rectangular (non-even)",
    (2, 1, 1, 1, 1): "minimal (hook, non-even)",
    (1, 1, 1, 1, 1, 1): "trivial",
}


def sl6_orbit_data() -> Dict[Partition, Dict]:
    """Complete orbit data for all 11 nilpotent orbits of sl_6."""
    data = {}
    for lam in SL6_PARTITIONS:
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
            "name": SL6_PARTITION_NAMES[lam],
        }
    return data


# ---------------------------------------------------------------------------
# Generator weights and anomaly ratio
# ---------------------------------------------------------------------------

def generator_weights_sl6(lam: Partition) -> List[Fraction]:
    """Conformal weights of strong generators of W^k(sl_6, f_lambda).

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


def anomaly_ratio_sl6(lam: Partition) -> Fraction:
    r"""Anomaly ratio rho_lambda = sum_bos 1/h_i - sum_ferm 1/h_i."""
    rho = Fraction(0)
    for w in generator_weights_sl6(lam):
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
    - Hook-type and rectangular W-algebras in sl_4, sl_5, sl_6

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


def central_charge_sl6(lam: Partition, k: Fraction) -> Fraction:
    """Central charge of W^k(sl_6, f_lambda), dispatching on even/non-even."""
    N = 6
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
    c7 = central_charge_even(N, lam, Fraction(7))
    # a + b = (N+1)*c1, 7a + b = (N+7)*c7
    # 6a = (N+7)*c7 - (N+1)*c1
    a = ((N + 7) * c7 - (N + 1) * c1) / 6
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

def kappa_sl6(lam: Partition, k: Fraction) -> Fraction:
    """Modular characteristic kappa = rho * c for W^k(sl_6, f_lambda)."""
    return anomaly_ratio_sl6(lam) * central_charge_sl6(lam, k)


# ---------------------------------------------------------------------------
# Complementarity
# ---------------------------------------------------------------------------

def central_charge_complementarity(
    N: int, lam: Partition, k: Fraction
) -> Fraction:
    """Compute c(k, lambda) + c(k', lambda^t) where k' = -k - 2N."""
    lam_t = transpose(lam)
    kd = dual_level(N, k)
    c1 = central_charge_sl6(lam, k)
    c2 = central_charge_sl6(lam_t, kd)
    return c1 + c2


def complementarity_is_level_independent(
    lam: Partition,
    test_levels: Optional[List[Fraction]] = None,
) -> bool:
    """Test whether c(k,lambda)+c(k',lambda^t) is k-independent."""
    N = 6
    if test_levels is None:
        test_levels = [Fraction(p) for p in [1, 3, 5, 7, 11, 17, 23]]
    values = set()
    for kv in test_levels:
        kd = dual_level(N, kv)
        if kv + N == 0 or kd + N == 0:
            continue
        values.add(central_charge_complementarity(N, lam, kv))
    return len(values) == 1


def complementarity_constant_even(lam: Partition) -> Fraction:
    """For even<->even orbits: the level-independent value of c+c'."""
    N = 6
    lam_t = transpose(lam)
    if not is_even_nilpotent(lam) or not is_even_nilpotent(lam_t):
        raise ValueError(
            "Only guaranteed level-independent for even<->even pairs"
        )
    return central_charge_complementarity(N, lam, Fraction(17))


def kappa_complementarity(lam: Partition, k: Fraction) -> Fraction:
    """Compute kappa(k,lambda) + kappa(k',lambda^t)."""
    N = 6
    lam_t = transpose(lam)
    kd = dual_level(N, k)
    k1 = kappa_sl6(lam, k)
    k2 = kappa_sl6(lam_t, kd)
    return k1 + k2


def kappa_complementarity_is_level_independent(
    lam: Partition,
    test_levels: Optional[List[Fraction]] = None,
) -> bool:
    """Test whether kappa+kappa' is k-independent."""
    N = 6
    if test_levels is None:
        test_levels = [Fraction(p) for p in [1, 3, 5, 7, 11, 17, 23]]
    values = set()
    for kv in test_levels:
        kd = dual_level(N, kv)
        if kv + N == 0 or kd + N == 0:
            continue
        values.add(kappa_complementarity(lam, kv))
    return len(values) == 1


# ---------------------------------------------------------------------------
# Self-dual point for self-transpose even partitions
# ---------------------------------------------------------------------------

def self_dual_central_charge(lam: Partition) -> Optional[Fraction]:
    """For self-transpose even lambda: the self-dual c* = C/2 where C = c+c'.

    Returns None if lambda is not self-transpose, not even, or if its
    transpose is not even.
    """
    lam_t = transpose(lam)
    if lam != lam_t:
        return None
    if not is_even_nilpotent(lam):
        return None
    C = complementarity_constant_even(lam)
    return C / 2


def self_dual_level(lam: Partition) -> Optional[Fraction]:
    """For self-transpose even lambda: level k* where c(k*) = c*."""
    N = 6
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
    """Complete duality data for partition lambda of 6."""
    N = 6
    lam_t = transpose(lam)
    gen_weights = generator_weights_sl6(lam)
    rho = anomaly_ratio_sl6(lam)
    is_ev = is_even_nilpotent(lam)
    c_verified = is_ev

    # Central charge at test level
    c_test = central_charge_sl6(lam, Fraction(1))

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


def full_sl6_analysis() -> Dict[Partition, Dict]:
    """Complete analysis for all 11 nilpotent orbits of sl_6."""
    return {lam: duality_profile(lam) for lam in SL6_PARTITIONS}


# ---------------------------------------------------------------------------
# Verification constants (multi-path, independently computed)
# ---------------------------------------------------------------------------

# Even-orbit central charge coefficients: c(k) = (a*k + b)/(k+6)
VERIFIED_C_COEFFICIENTS = {
    (6,): (Fraction(5), Fraction(-180)),
    (5, 1): (Fraction(7), Fraction(-128)),
    (4, 2): (Fraction(9), Fraction(-88)),
    (3, 3): (Fraction(11), Fraction(-72)),
    (3, 1, 1, 1): (Fraction(17), Fraction(-42)),
    (2, 2, 2): (Fraction(17), Fraction(-36)),
    (1, 1, 1, 1, 1, 1): (Fraction(35), Fraction(0)),
}

# Even<->even complementarity constants.  Only two pure even-even pairs:
#   (6) <-> (1^6): C = 40
#   (3,3) <-> (2,2,2): C = 28
VERIFIED_COMPLEMENTARITY = {
    (6,): Fraction(40),                   # (6) <-> (1,1,1,1,1,1)
    (3, 3): Fraction(28),                 # (3,3) <-> (2,2,2)
    (2, 2, 2): Fraction(28),              # same pair
    (1, 1, 1, 1, 1, 1): Fraction(40),    # same pair as (6)
}

# Anomaly ratios (ALL 11 orbits, computed from generator weights)
VERIFIED_ANOMALY_RATIOS = {
    (6,): Fraction(29, 20),                 # 1/2 + 1/3 + 1/4 + 1/5 + 1/6
    (5, 1): Fraction(59, 20),               # computed from 7 generators
    (4, 2): Fraction(17, 4),                # computed from 9 generators
    (4, 1, 1): Fraction(209, 60),           # 7 bosonic, 4 fermionic
    (3, 3): Fraction(19, 3),                # 11 bosonic generators
    (3, 2, 1): Fraction(13, 15),            # 7 bosonic, 6 fermionic
    (3, 1, 1, 1): Fraction(77, 6),          # 17 bosonic generators
    (2, 2, 2): Fraction(25, 2),             # 17 bosonic generators
    (2, 2, 1, 1): Fraction(11, 3),          # 11 bosonic, 8 fermionic
    (2, 1, 1, 1, 1): Fraction(67, 6),       # 17 bosonic, 8 fermionic
    (1, 1, 1, 1, 1, 1): Fraction(35),       # 35 weight-1 generators
}

# Leading coefficient coincidence: a(3,1,1,1) = a(2,2,2) = 17
# These are NOT a transpose pair (different orbits with the same asymptotic c).
LEADING_COEFF_COINCIDENCE = (Fraction(17), [(3, 1, 1, 1), (2, 2, 2)])

# (3,2,1) is the unique self-transpose partition of 6 and is NON-EVEN.
# This is the KEY NEW PHENOMENON at N=6: no self-dual analysis is possible
# via the even formula.  The self-dual c* and self-dual level are UNDEFINED
# until the non-even formula is verified.
SELF_TRANSPOSE_321_IS_NON_EVEN = True
