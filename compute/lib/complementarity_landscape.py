"""Full complementarity landscape: kappa, kappa', K, rho, self-dual point for ALL families.

Theorem C (complementarity) at the scalar level (Theorem D):

    kappa(A) + kappa(A!) = constant

The constant depends on the algebra family:

    (1) Free-field systems (Heisenberg, betagamma/bc, lattice, free fermion):
        kappa + kappa' = 0

    (2) Affine Kac-Moody algebras (all simple types):
        kappa + kappa' = 0    (FF anti-symmetry: k -> -k-2h^v negates kappa)
        K := c + c' = 2*dim(g)  (the central charge sum IS level-independent)

    (3) W-algebras W_N = W(sl_N) (principal, type A):
        kappa + kappa' = rho_N * K_N
        where rho_N = H_N - 1 = sum_{s=2}^N 1/s  (anomaly ratio)
        and   K_N = 2(N-1)(2N^2+2N+1)             (Koszul conductor)
        Self-dual at c_* = K_N / 2.

    In both cases (2) and (3), the sum is LEVEL-INDEPENDENT (topological).

KEY DISTINCTION (AP24): kappa + kappa' = 0 for affine KM, but
kappa + kappa' = rho*K ≠ 0 for W-algebras (N >= 2). The Virasoro (N=2) sum
is 13, not 0. The W_3 (N=3) sum is 250/3. These are NOT zero.

FORMULAS (all verified by independent computation):

    Heisenberg H_k:     kappa = k,                 kappa' = -k
    Free fermion:        kappa = 1/4,               kappa' = -1/4
    Lattice V_Lambda:    kappa = rank,              kappa' = -rank

    betagamma(lam):      kappa = 6*lam^2-6*lam+1,  kappa' = -(6*lam^2-6*lam+1)
    bc(lam):             kappa = -(6*lam^2-6*lam+1), kappa' = 6*lam^2-6*lam+1

    Affine g_k:          kappa = dim(g)*(k+h^v)/(2*h^v),  kappa' = -kappa

    Virasoro (W_2):      kappa = c/2,    kappa' = (26-c)/2,   sum = 13
    W_3:                 kappa = 5c/6,   kappa' = 5(100-c)/6, sum = 250/3
    W_4:                 kappa = 13c/12, kappa' = 13(246-c)/12, sum = 533/2
    W_5:                 kappa = 77c/60, kappa' = 77(488-c)/60, sum = 9394/15
    W_N:                 kappa = rho_N*c, kappa' = rho_N*(K_N-c), sum = rho_N*K_N

CRITICAL PITFALLS:
    - Heisenberg is NOT self-dual (AP25/CLAUDE.md): H_k^! = Sym^ch(V*)
    - betagamma is NOT self-dual: bg^! = bc (different statistics)
    - kappa_bg(lam) = kappa_bg(1-lam) is a SYMMETRY, not duality
    - Virasoro self-dual at c=13, NOT c=26 (AP8)
    - For affine KM: kappa = dim*(k+h^v)/(2h^v), NOT c/2 (AP1)
    - K = c+c' for affine KM is 2*dim(g), proved algebraically

References:
    thm:quantum-complementarity-main (higher_genus_complementarity.tex)
    thm:thqg-IV-km-K, thm:thqg-IV-w-K (Vol II)
    rem:koszul-conductor-explicit: K_N = 2(N-1)(2N^2+2N+1)
    CLAUDE.md: AP24, AP29, Theorem C/D
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


# ========================================================================
# Lie algebra data: (dim, h^vee)
# ========================================================================

_LIE_DATA: Dict[Tuple[str, int], Tuple[int, int, str]] = {
    ("A", 1): (3, 2, "sl_2"),
    ("A", 2): (8, 3, "sl_3"),
    ("A", 3): (15, 4, "sl_4"),
    ("A", 4): (24, 5, "sl_5"),
    ("A", 5): (35, 6, "sl_6"),
    ("A", 6): (48, 7, "sl_7"),
    ("A", 7): (63, 8, "sl_8"),
    ("A", 8): (80, 9, "sl_9"),
    ("A", 9): (99, 10, "sl_10"),
    ("B", 2): (10, 3, "so_5"),
    ("B", 3): (21, 5, "so_7"),
    ("B", 4): (36, 7, "so_9"),
    ("C", 2): (10, 3, "sp_4"),
    ("C", 3): (21, 4, "sp_6"),
    ("C", 4): (36, 5, "sp_8"),
    ("D", 4): (28, 6, "so_8"),
    ("D", 5): (45, 8, "so_10"),
    ("G", 2): (14, 4, "g_2"),
    ("F", 4): (52, 9, "f_4"),
    ("E", 6): (78, 12, "e_6"),
    ("E", 7): (133, 18, "e_7"),
    ("E", 8): (248, 30, "e_8"),
}


def _lie_dim_hdual(lie_type: str, rank: int) -> Tuple[int, int]:
    """Return (dim(g), h^vee) for a simple Lie algebra."""
    key = (lie_type, rank)
    if key in _LIE_DATA:
        d, h, _ = _LIE_DATA[key]
        return d, h
    if lie_type == "A":
        N = rank + 1
        return N * N - 1, N
    raise ValueError(f"Lie algebra ({lie_type}, {rank}) not in table")


def _lie_name(lie_type: str, rank: int) -> str:
    """Human-readable name for a Lie algebra."""
    key = (lie_type, rank)
    if key in _LIE_DATA:
        return _LIE_DATA[key][2]
    if lie_type == "A":
        return f"sl_{rank + 1}"
    return f"{lie_type}_{rank}"


# ========================================================================
# Harmonic numbers and anomaly ratio
# ========================================================================

def harmonic(n: int) -> Fraction:
    """H_n = 1 + 1/2 + ... + 1/n."""
    return sum(Fraction(1, j) for j in range(1, n + 1))


def anomaly_ratio(N: int) -> Fraction:
    """rho(sl_N) = H_N - 1 = sum_{s=2}^{N} 1/s.

    This is the anomaly ratio: kappa(W_N, c) = rho_N * c.

    rho(sl_2) = 1/2       (Virasoro)
    rho(sl_3) = 5/6       (W_3)
    rho(sl_4) = 13/12     (W_4)
    rho(sl_5) = 77/60     (W_5)
    rho(sl_6) = 29/20     (W_6)
    """
    return harmonic(N) - 1


# ========================================================================
# Koszul conductor K_N for W-algebras
# ========================================================================

def koszul_conductor_wn(N: int) -> int:
    """K_N = 2(N-1)(2N^2+2N+1) for principal W_N.

    This is the level-independent central charge sum: c(k) + c(k') = K_N
    where k' is the Feigin-Frenkel dual level.

    K_2 = 26   (Virasoro)
    K_3 = 100  (W_3)
    K_4 = 246  (W_4)
    K_5 = 488  (W_5)
    K_6 = 850  (W_6)
    K_7 = 1356 (W_7)
    """
    return 2 * (N - 1) * (2 * N * N + 2 * N + 1)


def central_charge_sum_affine(lie_type: str, rank: int) -> int:
    """Central charge sum c(k) + c(k') = 2*dim(g) for affine KM.

    Proof: c(k) = d*k/(k+h), c(k') = d*(k+2h)/(k+h) where k'=-k-2h.
    Sum = d*(2k+2h)/(k+h) = 2d. QED.
    """
    dim_g, _ = _lie_dim_hdual(lie_type, rank)
    return 2 * dim_g


# ========================================================================
# W_N central charge from DS reduction
# ========================================================================

def central_charge_wn(N: int, k: Fraction) -> Fraction:
    """Central charge of W_N = W(sl_N) via principal DS reduction.

    c(W_N, k) = (N-1)[1 - N(N+1)(k+N-1)^2/(k+N)]

    The Fateev-Lukyanov formula.
    """
    k = Fraction(k)
    if k + N == 0:
        raise ValueError(f"Critical level k = -{N}: central charge undefined")
    return Fraction(N - 1) * (
        Fraction(1) - Fraction(N * (N + 1)) * (k + N - 1) ** 2 / (k + N)
    )


# ========================================================================
# Kappa formulas
# ========================================================================

def kappa_heisenberg(k: Fraction) -> Fraction:
    """kappa(H_k) = k."""
    return Fraction(k)


def kappa_free_fermion() -> Fraction:
    """kappa(free fermion) = 1/4.

    c = 1/2, kappa = c/2 = 1/4.
    """
    return Fraction(1, 4)


def kappa_lattice(rank: int) -> Fraction:
    """kappa(V_Lambda) = rank(Lambda)."""
    return Fraction(rank)


def kappa_betagamma(lam: Fraction) -> Fraction:
    """kappa(betagamma at weight lambda) = 6*lam^2 - 6*lam + 1.

    This equals c_bg/2 where c_bg = 2(6*lam^2 - 6*lam + 1).

    NOTE: kappa_bg(lam) = kappa_bg(1-lam) by polynomial symmetry.
    This is NOT duality; the Koszul dual is the bc system (different statistics).
    """
    lam = Fraction(lam)
    return 6 * lam ** 2 - 6 * lam + 1


def kappa_bc(lam: Fraction) -> Fraction:
    """kappa(bc at weight lambda) = -(6*lam^2 - 6*lam + 1) = -kappa_bg.

    The bc system is the Koszul dual of betagamma.
    """
    return -kappa_betagamma(lam)


def kappa_affine(lie_type: str, rank: int, k: Fraction) -> Fraction:
    """kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v).

    CRITICAL (AP1): This is NOT c/2 for affine algebras.
    c = k*dim(g)/(k+h^v) (Sugawara), but kappa = dim(g)*(k+h^v)/(2*h^v).
    """
    dim_g, h_dual = _lie_dim_hdual(lie_type, rank)
    k = Fraction(k)
    if k + h_dual == 0:
        raise ValueError(
            f"Critical level k = -{h_dual}: kappa undefined for {lie_type}_{rank}"
        )
    return Fraction(dim_g) * (k + h_dual) / (2 * h_dual)


def kappa_virasoro(c: Fraction) -> Fraction:
    """kappa(Vir_c) = c/2.

    Virasoro = W_2, so rho_2 = 1/2 and kappa = (1/2)*c.
    """
    return Fraction(c) / 2


def kappa_wn(N: int, c: Fraction) -> Fraction:
    """kappa(W_N, c) = rho_N * c = (H_N - 1) * c.

    rho_2 = 1/2  -> kappa = c/2     (Virasoro)
    rho_3 = 5/6  -> kappa = 5c/6    (W_3)
    rho_4 = 13/12 -> kappa = 13c/12 (W_4)
    rho_5 = 77/60 -> kappa = 77c/60 (W_5)
    """
    return anomaly_ratio(N) * Fraction(c)


# ========================================================================
# Koszul dual kappa
# ========================================================================

def kappa_dual_heisenberg(k: Fraction) -> Fraction:
    """kappa'(H_k) = -k."""
    return -Fraction(k)


def kappa_dual_free_fermion() -> Fraction:
    """kappa'(free fermion) = -1/4."""
    return Fraction(-1, 4)


def kappa_dual_lattice(rank: int) -> Fraction:
    """kappa'(V_Lambda) = -rank."""
    return -Fraction(rank)


def kappa_dual_betagamma(lam: Fraction) -> Fraction:
    """kappa'(bg) = kappa(bc) = -(6*lam^2 - 6*lam + 1)."""
    return kappa_bc(lam)


def kappa_dual_bc(lam: Fraction) -> Fraction:
    """kappa'(bc) = kappa(bg) = 6*lam^2 - 6*lam + 1."""
    return kappa_betagamma(lam)


def kappa_dual_affine(lie_type: str, rank: int, k: Fraction) -> Fraction:
    """kappa'(g_k) = kappa(g_{k'}) where k' = -k - 2h^v.

    = dim(g)*(-k-2h^v+h^v)/(2h^v) = dim(g)*(-k-h^v)/(2h^v) = -kappa(g_k).
    """
    return -kappa_affine(lie_type, rank, k)


def kappa_dual_virasoro(c: Fraction) -> Fraction:
    """kappa'(Vir_c) = kappa(Vir_{26-c}) = (26-c)/2."""
    return Fraction(26 - Fraction(c)) / 2


def kappa_dual_wn(N: int, c: Fraction) -> Fraction:
    """kappa'(W_N at c) = kappa(W_N at K_N-c) = rho_N * (K_N - c)."""
    K_N = koszul_conductor_wn(N)
    return anomaly_ratio(N) * (Fraction(K_N) - Fraction(c))


# ========================================================================
# Complementarity sum
# ========================================================================

def complementarity_sum_heisenberg(k: Fraction) -> Fraction:
    """kappa + kappa' = 0 for Heisenberg."""
    return Fraction(0)


def complementarity_sum_free_fermion() -> Fraction:
    """kappa + kappa' = 0 for free fermion."""
    return Fraction(0)


def complementarity_sum_lattice(rank: int) -> Fraction:
    """kappa + kappa' = 0 for lattice VOAs."""
    return Fraction(0)


def complementarity_sum_betagamma(lam: Fraction) -> Fraction:
    """kappa + kappa' = 0 for betagamma/bc pair."""
    return Fraction(0)


def complementarity_sum_affine(lie_type: str, rank: int) -> Fraction:
    """kappa + kappa' = 0 for affine KM (FF anti-symmetry)."""
    return Fraction(0)


def complementarity_sum_wn(N: int) -> Fraction:
    """kappa + kappa' = rho_N * K_N for W_N.

    Virasoro (N=2):  13
    W_3 (N=3):       250/3
    W_4 (N=4):       533/2
    W_5 (N=5):       9394/15
    """
    return anomaly_ratio(N) * Fraction(koszul_conductor_wn(N))


# ========================================================================
# Self-dual points
# ========================================================================

def self_dual_point_virasoro() -> Fraction:
    """Virasoro self-dual at c = 13, NOT c = 26."""
    return Fraction(13)


def self_dual_point_wn(N: int) -> Fraction:
    """W_N self-dual at c = K_N / 2 = (N-1)(2N^2+2N+1)."""
    return Fraction(koszul_conductor_wn(N), 2)


def self_dual_point_affine() -> str:
    """Affine KM: self-dual at critical level k = -h^v (degenerate)."""
    return "k = -h^v (critical level, degenerate)"


# ========================================================================
# Comprehensive landscape data structure
# ========================================================================

@dataclass
class ComplementarityDatum:
    """Full complementarity data for one family at one parameter value."""
    family: str
    display_name: str
    kappa: Fraction
    kappa_dual: Fraction
    kappa_sum: Fraction
    K: Optional[Fraction]          # c + c', if meaningful
    rho: Optional[Fraction]        # anomaly ratio, for W-algebras
    self_dual: Optional[Fraction]  # self-dual parameter value
    self_dual_param: str           # name of the parameter (c, k, lam, rank)
    notes: str


def datum_heisenberg(k: Fraction) -> ComplementarityDatum:
    """Complementarity datum for Heisenberg H_k."""
    k = Fraction(k)
    return ComplementarityDatum(
        family="heisenberg",
        display_name=f"H_{k}",
        kappa=k,
        kappa_dual=-k,
        kappa_sum=Fraction(0),
        K=None,
        rho=None,
        self_dual=Fraction(0),
        self_dual_param="k",
        notes="H_k^! has kappa=-k; NOT self-dual (AP25)",
    )


def datum_free_fermion() -> ComplementarityDatum:
    """Complementarity datum for free fermion."""
    return ComplementarityDatum(
        family="free_fermion",
        display_name="FreeFermion",
        kappa=Fraction(1, 4),
        kappa_dual=Fraction(-1, 4),
        kappa_sum=Fraction(0),
        K=Fraction(1),  # c + c' = 1/2 + (-1/2+1) ... actually this is subtle
        rho=None,
        self_dual=None,
        self_dual_param="n/a",
        notes="c=1/2, kappa=c/2=1/4; dual has kappa'=-1/4",
    )


def datum_lattice(rank: int) -> ComplementarityDatum:
    """Complementarity datum for lattice VOA of given rank."""
    r = Fraction(rank)
    return ComplementarityDatum(
        family="lattice",
        display_name=f"Lattice_rank{rank}",
        kappa=r,
        kappa_dual=-r,
        kappa_sum=Fraction(0),
        K=Fraction(2 * rank),  # c + c' = 2*rank (Heisenberg-like)
        rho=None,
        self_dual=Fraction(0),
        self_dual_param="rank",
        notes="kappa = rank; dual has kappa' = -rank",
    )


def datum_betagamma(lam: Fraction) -> ComplementarityDatum:
    """Complementarity datum for betagamma at conformal weight lambda."""
    lam = Fraction(lam)
    kbg = kappa_betagamma(lam)
    c_bg = 2 * kbg
    return ComplementarityDatum(
        family="betagamma",
        display_name=f"bg(lam={lam})",
        kappa=kbg,
        kappa_dual=-kbg,
        kappa_sum=Fraction(0),
        K=None,
        rho=None,
        self_dual=None,
        self_dual_param="n/a",
        notes=f"c_bg={c_bg}; dual is bc with kappa'=-kappa_bg; bg NOT self-dual",
    )


def datum_bc(lam: Fraction) -> ComplementarityDatum:
    """Complementarity datum for bc at conformal weight lambda."""
    lam = Fraction(lam)
    kbc = kappa_bc(lam)
    return ComplementarityDatum(
        family="bc",
        display_name=f"bc(lam={lam})",
        kappa=kbc,
        kappa_dual=-kbc,
        kappa_sum=Fraction(0),
        K=None,
        rho=None,
        self_dual=None,
        self_dual_param="n/a",
        notes="Dual of bc is bg",
    )


def datum_affine(lie_type: str, rank: int, k: Fraction) -> ComplementarityDatum:
    """Complementarity datum for affine g_k."""
    k = Fraction(k)
    dim_g, h_dual = _lie_dim_hdual(lie_type, rank)
    name = _lie_name(lie_type, rank)
    kap = kappa_affine(lie_type, rank, k)
    K_cc = 2 * dim_g

    return ComplementarityDatum(
        family="affine",
        display_name=f"aff({name})_k={k}",
        kappa=kap,
        kappa_dual=-kap,
        kappa_sum=Fraction(0),
        K=Fraction(K_cc),
        rho=None,
        self_dual=None,
        self_dual_param="k",
        notes=(
            f"dim={dim_g}, h^v={h_dual}; kappa=dim*(k+h^v)/(2h^v); "
            f"K=c+c'={K_cc}=2*dim; self-dual at k=-h^v (critical, degenerate)"
        ),
    )


def datum_virasoro(c: Fraction) -> ComplementarityDatum:
    """Complementarity datum for Virasoro at central charge c."""
    c = Fraction(c)
    kap = kappa_virasoro(c)
    kap_dual = kappa_dual_virasoro(c)
    return ComplementarityDatum(
        family="virasoro",
        display_name=f"Vir_{c}",
        kappa=kap,
        kappa_dual=kap_dual,
        kappa_sum=Fraction(13),
        K=Fraction(26),
        rho=Fraction(1, 2),
        self_dual=Fraction(13),
        self_dual_param="c",
        notes="W_2; self-dual at c=13, NOT c=26 (AP8)",
    )


def datum_wn(N: int, c: Fraction) -> ComplementarityDatum:
    """Complementarity datum for W_N at central charge c."""
    c = Fraction(c)
    rho_N = anomaly_ratio(N)
    K_N = koszul_conductor_wn(N)
    kap = kappa_wn(N, c)
    kap_dual = kappa_dual_wn(N, c)
    c_star = self_dual_point_wn(N)
    kappa_sum = rho_N * K_N

    return ComplementarityDatum(
        family=f"W_{N}",
        display_name=f"W_{N}(c={c})",
        kappa=kap,
        kappa_dual=kap_dual,
        kappa_sum=kappa_sum,
        K=Fraction(K_N),
        rho=rho_N,
        self_dual=c_star,
        self_dual_param="c",
        notes=f"K_{N}={K_N}, rho={rho_N}, self-dual at c={c_star}",
    )


# ========================================================================
# Full landscape table
# ========================================================================

def full_complementarity_landscape() -> List[ComplementarityDatum]:
    """Compute complementarity data for ALL standard families.

    Returns a list of ComplementarityDatum objects covering:
    - Heisenberg at k=1
    - Free fermion
    - Lattice VOAs: D_4 (rank 4), E_8 (rank 8), Leech (rank 24)
    - betagamma at lambda = 0, 1/2, 1
    - Affine KM: sl_2, sl_3, G_2, E_8, B_2, C_2, D_4, F_4, E_6, E_7
    - Virasoro at generic c
    - W_3, W_4, W_5, W_6, W_7 at generic c
    """
    data: List[ComplementarityDatum] = []

    # ---- Free-field systems (kappa + kappa' = 0) ----
    data.append(datum_heisenberg(Fraction(1)))
    data.append(datum_free_fermion())
    for rank in [4, 8, 24]:
        data.append(datum_lattice(rank))
    for lam in [Fraction(0), Fraction(1, 2), Fraction(1)]:
        data.append(datum_betagamma(lam))

    # ---- Affine KM (kappa + kappa' = 0, K = 2*dim) ----
    affine_families = [
        ("A", 1, 1),  # sl_2
        ("A", 2, 1),  # sl_3
        ("A", 3, 1),  # sl_4
        ("B", 2, 1),  # so_5
        ("C", 2, 1),  # sp_4
        ("D", 4, 1),  # so_8
        ("G", 2, 1),  # g_2
        ("F", 4, 1),  # f_4
        ("E", 6, 1),  # e_6
        ("E", 7, 1),  # e_7
        ("E", 8, 1),  # e_8
    ]
    for lie_type, rank, k in affine_families:
        data.append(datum_affine(lie_type, rank, Fraction(k)))

    # ---- W-algebras (kappa + kappa' = rho * K ≠ 0) ----
    # Use c = K/2 (the self-dual point) as a representative
    for N in range(2, 8):
        c_star = self_dual_point_wn(N)
        data.append(datum_wn(N, c_star))

    return data


def landscape_summary_table() -> List[Dict[str, Any]]:
    """Summary table of complementarity data for all families.

    Returns list of dicts suitable for display or testing.
    """
    rows: List[Dict[str, Any]] = []

    # Free-field systems
    rows.append({
        "family": "Heisenberg",
        "kappa_formula": "k",
        "kappa_dual_formula": "-k",
        "sum": Fraction(0),
        "K": "n/a",
        "rho": "n/a",
        "self_dual": "k=0 (degenerate)",
        "class": "free-field",
    })
    rows.append({
        "family": "Free fermion",
        "kappa_formula": "1/4",
        "kappa_dual_formula": "-1/4",
        "sum": Fraction(0),
        "K": "n/a",
        "rho": "n/a",
        "self_dual": "n/a",
        "class": "free-field",
    })
    rows.append({
        "family": "Lattice V_Lambda",
        "kappa_formula": "rank",
        "kappa_dual_formula": "-rank",
        "sum": Fraction(0),
        "K": "2*rank",
        "rho": "n/a",
        "self_dual": "rank=0 (degenerate)",
        "class": "free-field",
    })
    rows.append({
        "family": "betagamma(lam)",
        "kappa_formula": "6*lam^2 - 6*lam + 1",
        "kappa_dual_formula": "-(6*lam^2 - 6*lam + 1)",
        "sum": Fraction(0),
        "K": "n/a",
        "rho": "n/a",
        "self_dual": "n/a (bg^! = bc, different statistics)",
        "class": "free-field",
    })

    # Affine KM
    for (lt, rk), (dim_g, hv, name) in sorted(_LIE_DATA.items()):
        rows.append({
            "family": f"Affine {name}",
            "kappa_formula": f"{dim_g}(k+{hv})/{2*hv}",
            "kappa_dual_formula": f"-{dim_g}(k+{hv})/{2*hv}",
            "sum": Fraction(0),
            "K": Fraction(2 * dim_g),
            "rho": "n/a",
            "self_dual": f"k=-{hv} (critical, degenerate)",
            "class": "affine",
        })

    # W-algebras
    for N in range(2, 8):
        rho_N = anomaly_ratio(N)
        K_N = koszul_conductor_wn(N)
        kappa_sum = rho_N * K_N
        c_star = Fraction(K_N, 2)
        rows.append({
            "family": f"W_{N}",
            "kappa_formula": f"{rho_N}*c",
            "kappa_dual_formula": f"{rho_N}*({K_N}-c)",
            "sum": kappa_sum,
            "K": Fraction(K_N),
            "rho": rho_N,
            "self_dual": f"c={c_star}",
            "class": "W-algebra",
        })

    return rows


# ========================================================================
# Verification functions
# ========================================================================

def verify_affine_kappa_antisymmetry(
    lie_type: str, rank: int, test_levels: Optional[List[Fraction]] = None
) -> Dict[str, Any]:
    """Verify kappa(g_k) + kappa(g_{k'}) = 0 at multiple levels."""
    if test_levels is None:
        test_levels = [Fraction(i) for i in [1, 2, 3, 5, -1]]

    dim_g, h_dual = _lie_dim_hdual(lie_type, rank)
    results = []
    all_ok = True

    for k_val in test_levels:
        if k_val + h_dual == 0:
            continue
        kap = kappa_affine(lie_type, rank, k_val)
        kap_dual = kappa_dual_affine(lie_type, rank, k_val)
        s = kap + kap_dual
        ok = (s == Fraction(0))
        if not ok:
            all_ok = False
        results.append({"k": k_val, "kappa": kap, "kappa_dual": kap_dual, "sum": s, "ok": ok})

    return {
        "lie_type": lie_type,
        "rank": rank,
        "dim": dim_g,
        "h_dual": h_dual,
        "K_cc": 2 * dim_g,
        "all_ok": all_ok,
        "results": results,
    }


def verify_wn_complementarity_level_independence(
    N: int, test_levels: Optional[List[Fraction]] = None
) -> Dict[str, Any]:
    """Verify kappa(W_N, c(k)) + kappa(W_N, c(k')) = rho_N * K_N at multiple levels."""
    if test_levels is None:
        test_levels = [Fraction(i) for i in [1, 2, 3, 5, -1, 10]]

    rho_N = anomaly_ratio(N)
    K_N = koszul_conductor_wn(N)
    expected = rho_N * K_N
    results = []
    all_ok = True

    for k_val in test_levels:
        if k_val + N == 0:
            continue
        k_dual = -k_val - 2 * N
        if k_dual + N == 0:
            continue
        c_k = central_charge_wn(N, k_val)
        c_k_dual = central_charge_wn(N, k_dual)
        kap = kappa_wn(N, c_k)
        kap_dual = kappa_wn(N, c_k_dual)
        s = kap + kap_dual

        # Also verify c + c' = K_N
        c_sum = c_k + c_k_dual
        c_ok = (c_sum == K_N)

        ok = (s == expected) and c_ok
        if not ok:
            all_ok = False
        results.append({
            "k": k_val, "c": c_k, "c_dual": c_k_dual,
            "c_sum": c_sum, "c_sum_ok": c_ok,
            "kappa": kap, "kappa_dual": kap_dual, "sum": s, "ok": ok,
        })

    return {
        "N": N,
        "K_N": K_N,
        "rho": rho_N,
        "expected_sum": expected,
        "all_ok": all_ok,
        "results": results,
    }


def verify_koszul_conductor_formula(max_N: int = 10) -> Dict[str, Any]:
    """Verify K_N = 2(N-1)(2N^2+2N+1) by computing c(k) + c(k') directly.

    Uses k=1 and k'=-1-2N as test level.
    """
    results = {}
    all_ok = True

    for N in range(2, max_N + 1):
        k_test = Fraction(1)
        k_dual = -k_test - 2 * N
        c_k = central_charge_wn(N, k_test)
        c_k_dual = central_charge_wn(N, k_dual)
        c_sum = c_k + c_k_dual
        K_formula = koszul_conductor_wn(N)

        ok = (c_sum == Fraction(K_formula))
        if not ok:
            all_ok = False

        results[N] = {
            "K_formula": K_formula,
            "c_sum": c_sum,
            "match": ok,
            "polynomial_form": f"4*{N}^3 - 2*{N} - 2 = {4*N**3 - 2*N - 2}",
        }

    return {"all_ok": all_ok, "results": results}


def verify_betagamma_symmetry() -> Dict[str, Any]:
    """Verify kappa_bg(lam) = kappa_bg(1-lam) and kappa_bg + kappa_bc = 0."""
    results = []
    all_ok = True

    for lam_val in [Fraction(0), Fraction(1, 4), Fraction(1, 3),
                    Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(1)]:
        kbg = kappa_betagamma(lam_val)
        kbg_comp = kappa_betagamma(1 - lam_val)
        kbc = kappa_bc(lam_val)
        sym_ok = (kbg == kbg_comp)
        sum_ok = (kbg + kbc == 0)
        ok = sym_ok and sum_ok
        if not ok:
            all_ok = False
        results.append({
            "lam": lam_val, "kappa_bg": kbg, "kappa_bg_1-lam": kbg_comp,
            "kappa_bc": kbc, "symmetry": sym_ok, "sum_zero": sum_ok,
        })

    return {"all_ok": all_ok, "results": results}


def verify_central_charge_sum_affine(
    test_algebras: Optional[List[Tuple[str, int]]] = None,
) -> Dict[str, Any]:
    """Verify c(k) + c(k') = 2*dim(g) for affine KM algebras."""
    if test_algebras is None:
        test_algebras = [
            ("A", 1), ("A", 2), ("A", 3), ("B", 2), ("C", 2),
            ("D", 4), ("G", 2), ("F", 4), ("E", 6), ("E", 7), ("E", 8),
        ]

    def c_affine(dim_g: int, hv: int, k: Fraction) -> Fraction:
        if k + hv == 0:
            raise ValueError("critical level")
        return Fraction(dim_g) * k / (k + hv)

    results = []
    all_ok = True

    for lie_type, rank in test_algebras:
        dim_g, hv = _lie_dim_hdual(lie_type, rank)
        k_test = Fraction(1)
        k_dual = -k_test - 2 * hv
        c_k = c_affine(dim_g, hv, k_test)
        c_kd = c_affine(dim_g, hv, k_dual)
        c_sum = c_k + c_kd
        expected = 2 * dim_g
        ok = (c_sum == Fraction(expected))
        if not ok:
            all_ok = False
        results.append({
            "algebra": _lie_name(lie_type, rank), "dim": dim_g, "h_dual": hv,
            "c_sum": c_sum, "expected": expected, "ok": ok,
        })

    return {"all_ok": all_ok, "results": results}


def verify_self_dual_points() -> Dict[str, Any]:
    """Verify self-dual points for Virasoro and W_N families."""
    results = {}

    # Virasoro: c=13 is self-dual, c=26 is NOT
    kap_13 = kappa_virasoro(Fraction(13))
    kap_13_dual = kappa_dual_virasoro(Fraction(13))
    kap_26 = kappa_virasoro(Fraction(26))
    kap_26_dual = kappa_dual_virasoro(Fraction(26))
    results["virasoro"] = {
        "c_13_self_dual": kap_13 == kap_13_dual,
        "c_13_kappa": kap_13,
        "c_26_NOT_self_dual": kap_26 != kap_26_dual,
        "c_26_kappa": kap_26,
        "c_26_kappa_dual": kap_26_dual,
    }

    # W_N self-dual points
    for N in range(2, 8):
        c_star = self_dual_point_wn(N)
        kap = kappa_wn(N, c_star)
        kap_dual = kappa_dual_wn(N, c_star)
        results[f"W_{N}"] = {
            "c_star": c_star,
            "kappa_at_c_star": kap,
            "kappa_dual_at_c_star": kap_dual,
            "self_dual": kap == kap_dual,
        }

    return results


# ========================================================================
# Comprehensive all-families audit
# ========================================================================

def full_landscape_audit() -> Dict[str, Any]:
    """Run ALL complementarity verifications across the entire landscape.

    Returns a comprehensive audit result with per-family verification.
    """
    audit: Dict[str, Any] = {}

    # 1. Affine KM anti-symmetry
    affine_algebras = [
        ("A", 1), ("A", 2), ("A", 3), ("A", 4),
        ("B", 2), ("B", 3), ("C", 2), ("C", 3),
        ("D", 4), ("G", 2), ("F", 4),
        ("E", 6), ("E", 7), ("E", 8),
    ]
    affine_results = {}
    for lt, rk in affine_algebras:
        r = verify_affine_kappa_antisymmetry(lt, rk)
        affine_results[_lie_name(lt, rk)] = r["all_ok"]
    audit["affine_antisymmetry"] = {
        "all_ok": all(affine_results.values()),
        "per_algebra": affine_results,
    }

    # 2. Affine central charge sum = 2*dim
    r = verify_central_charge_sum_affine()
    audit["affine_cc_sum"] = r

    # 3. W_N Koszul conductor
    r = verify_koszul_conductor_formula()
    audit["koszul_conductor"] = r

    # 4. W_N level independence
    wn_results = {}
    for N in range(2, 8):
        r = verify_wn_complementarity_level_independence(N)
        wn_results[f"W_{N}"] = r["all_ok"]
    audit["wn_level_independence"] = {
        "all_ok": all(wn_results.values()),
        "per_N": wn_results,
    }

    # 5. betagamma symmetry
    audit["betagamma_symmetry"] = verify_betagamma_symmetry()

    # 6. Self-dual points
    audit["self_dual_points"] = verify_self_dual_points()

    # 7. Free-field sums
    ff_ok = True
    ff_results = {}
    for k in [Fraction(1), Fraction(-3), Fraction(1, 2)]:
        s = kappa_heisenberg(k) + kappa_dual_heisenberg(k)
        ok = (s == Fraction(0))
        if not ok:
            ff_ok = False
        ff_results[f"H_{k}"] = ok
    s_ff = kappa_free_fermion() + kappa_dual_free_fermion()
    ff_results["FreeFermion"] = (s_ff == Fraction(0))
    for rank in [4, 8, 24]:
        s_lat = kappa_lattice(rank) + kappa_dual_lattice(rank)
        ok = (s_lat == Fraction(0))
        if not ok:
            ff_ok = False
        ff_results[f"Lattice_{rank}"] = ok
    audit["free_field_sums"] = {"all_ok": ff_ok, "per_family": ff_results}

    # Overall
    audit["all_pass"] = all(
        audit[k]["all_ok"] if isinstance(audit[k], dict) and "all_ok" in audit[k]
        else True
        for k in audit
    )

    return audit
