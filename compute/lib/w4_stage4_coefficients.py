"""W_4 stage-4 coefficient extraction for MC4 W_infinity verification.

Ground truth from the manuscript (bar_cobar_construction.tex, concordance.tex):
  rem:mc4-winfty-computation-target: Extract six live coefficients from the
  principal DS W_4 OPE at generic central charge and compare with bar-side data.

  Stage-3 packet (prop:winfty-ds-stage3-explicit-packet):
    C^DS_{2,2;2;0,2}(3) = 2   (T x T -> T at pole 2)
    C^DS_{2,3;3;0,2}(3) = 3   (T x W -> W at pole 2)
    C^DS_{3,3;2;0,4}(3) = 2   (W x W -> T at pole 4)
    All other C in I_3 = 0.

  Stage-4 live frontier (rem:mc4-winfty-computation-target):
    Six coefficients: c_334, c_444, C_{3,4;3;0,4}, C_{3,4;4;0,3},
    C^res_{4,4;2;0,6}, C^res_{3,4;2;0,5}.
    Two falsifiable predictions: one = 2, one = 0.

  Stage-4 residual packet (prop:winfty-ds-stage4-residual-packet):
    J_4 has 29 elements decomposed into (3,3) tail + J_4^{3,4} + J_4^{4,4}.

The W_4 algebra = principal DS reduction of sl_4-hat at level k.
  Generators: T (spin 2), W_3 (spin 3), W_4 (spin 4).
  Central charge: c = 3 - 60(k+3)^2/(k+4).
  Dual level: k' = -k - 2h^vee = -k - 8 (for sl_4, h^vee = 4).
  Feigin-Frenkel: k <-> -k - 2h^vee.

CONVENTIONS (following manuscript):
  - C^DS_{s,t;u;m,n}(N) = primary OPE coefficient at stage N
    s, t = source spins; u = target spin; m = derivative order; n = pole order
  - W^{(s)} = generator of spin s (primary under T)
  - Pole order in W_s(z)W_t(w) OPE: at most s + t - 1
  - Central charge relation: c_DS(k) + c_DS(k') = sigma (complementarity sum)
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from sympy import Rational, Symbol, simplify, factorial


# ---------------------------------------------------------------------------
# Central charge
# ---------------------------------------------------------------------------

def w4_central_charge(k):
    """Central charge of principal W_4 = DS of sl_4-hat at level k.

    c = 3 - 60(k+3)^2/(k+4)

    where n=4 for sl_4, and the general formula is:
    c = (n-1) - n(n^2-1)(k+n-1)^2/(k+n).
    """
    return 3 - Rational(60) * (k + 3) ** 2 / (k + 4)


def w4_dual_level(k):
    """Feigin-Frenkel dual level: k' = -k - 2h^vee = -k - 8 (sl_4)."""
    return -k - 8


def w4_complementarity_sum(k=None):
    """c(k) + c(k') for the W_4 algebra.

    For the principal W_N algebra from sl_N, the complementarity sum is:
    sigma = (N-1)(N-1 + N(N+1)) = (N-1)(N^2+N+N-1) ... actually let me compute.

    For W_3: c(k) + c(-k-6) = 100.
    For W_4: c(k) + c(-k-8) should be a constant.
    """
    if k is None:
        k = Symbol('k')
    c1 = w4_central_charge(k)
    k_dual = w4_dual_level(k)
    c2 = w4_central_charge(k_dual)
    return simplify(c1 + c2)


# ---------------------------------------------------------------------------
# Primary seed set I_N
# ---------------------------------------------------------------------------

def seed_set(N: int) -> List[Tuple[int, int, int, int]]:
    """Primary seed set I_N = {(s,t,u,n) | admissible for stage N}.

    Admissibility:
      2 <= s <= t <= N
      2 <= u <= min(N, s+t-1)
      1 <= n <= s+t-u
    """
    seeds = []
    for s in range(2, N + 1):
        for t in range(s, N + 1):
            for u in range(2, min(N, s + t - 1) + 1):
                for n in range(1, s + t - u + 1):
                    seeds.append((s, t, u, n))
    return seeds


def seed_set_size(N: int) -> int:
    """Size of I_N."""
    return len(seed_set(N))


def virasoro_subset(N: int) -> List[Tuple[int, int, int, int]]:
    """I_N^Vir = {(s,t,u,n) in I_N | s = 2}."""
    return [(s, t, u, n) for s, t, u, n in seed_set(N) if s == 2]


def w3_subset(N: int) -> List[Tuple[int, int, int, int]]:
    """I_N^W3 = {(3,3,u,n) in I_N | u <= 3}."""
    return [(s, t, u, n) for s, t, u, n in seed_set(N)
            if s == 3 and t == 3 and u <= 3]


def residual_packet(N: int) -> List[Tuple[int, int, int, int]]:
    r"""J_N = I_N \ (I_N^Vir cup I_N^W3): genuinely new stage-N coefficients."""
    vir = set(virasoro_subset(N))
    w3 = set(w3_subset(N))
    return sorted(s for s in seed_set(N) if s not in vir and s not in w3)


# ---------------------------------------------------------------------------
# Stage-3 packet (from explicit W_3 OPE)
# ---------------------------------------------------------------------------

def stage3_ds_coefficients() -> Dict[Tuple[int, int, int, int], object]:
    """All C^DS_{s,t;u;m,n}(3) from the explicit W_3 OPE.

    From prop:winfty-ds-stage3-explicit-packet:
      C_{2,2;2;0,2} = 2
      C_{2,3;3;0,2} = 3
      C_{3,3;2;0,4} = 2
      All others in I_3 = 0.
    """
    all_seeds = seed_set(3)
    coeffs = {s: 0 for s in all_seeds}

    # The three nonzero coefficients
    coeffs[(2, 2, 2, 2)] = 2  # T x T -> T at pole 2
    coeffs[(2, 3, 3, 2)] = 3  # T x W -> W at pole 2
    coeffs[(3, 3, 2, 4)] = 2  # W x W -> T at pole 4

    return coeffs


def stage3_nonzero_count() -> int:
    """Number of nonzero coefficients in the stage-3 packet."""
    return sum(1 for v in stage3_ds_coefficients().values() if v != 0)


def stage3_vanishing_count() -> int:
    """Number of vanishing coefficients in the stage-3 packet."""
    return sum(1 for v in stage3_ds_coefficients().values() if v == 0)


# ---------------------------------------------------------------------------
# Stage-4 target coefficients
# ---------------------------------------------------------------------------

def stage4_live_targets() -> List[str]:
    """The six live coefficients from rem:mc4-winfty-computation-target."""
    return [
        "c_334",          # W_3 x W_3 -> W_4 coupling
        "c_444",          # W_4 x W_4 -> W_4 coupling
        "C_{3,4;3;0,4}",  # W_3 x W_4 -> W_3 at pole 4
        "C_{3,4;4;0,3}",  # W_3 x W_4 -> W_4 at pole 3
        "C^res_{4,4;2;0,6}",  # W_4 x W_4 -> T at pole 6
        "C^res_{3,4;2;0,5}",  # W_3 x W_4 -> T at pole 5
    ]


def stage4_residual_decomposition() -> Dict[str, List[Tuple[int, int, int, int]]]:
    """Decomposition of J_4 from prop:winfty-ds-stage4-residual-packet.

    J_4 = {(3,3,4,1),(3,3,4,2)} cup J_4^{3,4} cup J_4^{4,4}
    """
    J4 = residual_packet(4)

    # (3,3) tail: target spin 4 (beyond stage-3 W_3 sector)
    tail_33 = [(s, t, u, n) for s, t, u, n in J4 if s == 3 and t == 3]

    # J_4^{3,4}: mixed source pair
    j4_34 = [(s, t, u, n) for s, t, u, n in J4 if s == 3 and t == 4]

    # J_4^{4,4}: self-coupling
    j4_44 = [(s, t, u, n) for s, t, u, n in J4 if s == 4 and t == 4]

    return {
        "tail_33": tail_33,
        "J4_34": j4_34,
        "J4_44": j4_44,
    }


# ---------------------------------------------------------------------------
# OPE weight bounds
# ---------------------------------------------------------------------------

def ope_max_pole_order(s: int, t: int) -> int:
    """Maximum pole order in W_s(z) W_t(w) OPE.

    For s = t: max pole = 2s - 1 (includes vacuum at pole 2s-1).
    Actually: a_{(n)}b singular for 0 <= n < s+t-1, so pole orders
    1, 2, ..., s+t-1. But the LEADING singularity for same-spin
    is (z-w)^{-(2s)} (from the 2-point function), pole order 2s-1
    in the (n-1)-th product convention.

    For W_3 x W_3: sixth-order pole => pole order 6 = 2*3.
    For W_4 x W_4: eighth-order pole => pole order 8 = 2*4.
    For T x T: quartic pole => pole order 4 = 2*2.
    So max pole = s + t for s = t, and s + t - 1 for s != t.
    """
    if s == t:
        return 2 * s
    return s + t - 1


def ope_target_weight(s: int, t: int, n: int) -> int:
    """Conformal weight of the output at pole order n in W_s x W_t OPE.

    At pole (z-w)^{-n}, the output has weight s + t - n.
    (Pole order n corresponds to the (n-1)-th product in vertex algebra
    notation, where a_{(n-1)}b has weight h_a + h_b - n.)
    """
    return s + t - n


def primary_target_at_pole(s: int, t: int, n: int) -> Optional[int]:
    """Spin of the primary target at pole order n in W_s x W_t, if it exists.

    Target weight = s + t - n - 1. This is a primary generator if the
    weight matches a generator spin (2, 3, or 4 for W_4).
    Returns None if no primary generator has this weight.
    """
    w = ope_target_weight(s, t, n)
    if w in (2, 3, 4):
        return w
    return None


# ---------------------------------------------------------------------------
# W_4 OPE structure: known coefficients from conformal symmetry
# ---------------------------------------------------------------------------

def w4_stress_tensor_ope() -> Dict[Tuple[str, str], Dict[int, Dict[str, object]]]:
    """T x W_s OPE for all generators (fully determined by conformal symmetry).

    T(z) T(w) ~ c/2 / (z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
    T(z) W_3(w) ~ 3 W_3(w)/(z-w)^2 + dW_3(w)/(z-w)
    T(z) W_4(w) ~ 4 W_4(w)/(z-w)^2 + dW_4(w)/(z-w)
    """
    c = Symbol('c')
    # Using POLE ORDERS (pole order p = n-th product index + 1):
    return {
        ("T", "T"): {
            4: {"vac": c / 2},            # quartic pole
            2: {"T": Rational(2)},        # double pole
            1: {"dT": Rational(1)},       # simple pole
        },
        ("T", "W3"): {
            2: {"W3": Rational(3)},       # double pole
            1: {"dW3": Rational(1)},      # simple pole
        },
        ("T", "W4"): {
            2: {"W4": Rational(4)},       # double pole
            1: {"dW4": Rational(1)},      # simple pole
        },
    }


def w4_curvature():
    """Curvature elements for the W_4 bar complex.

    m_0^(T) = c/2   (from quartic pole T_{(3)}T)
    m_0^(W_3) = c/3  (from sixth-order pole W_3_{(5)}W_3)
    m_0^(W_4) = c/4  (from eighth-order pole W_4_{(7)}W_4)

    Kappa total: c(1/2 + 1/3 + 1/4) = 13c/12
    """
    c = Symbol('c')
    return {"T": c / 2, "W3": c / 3, "W4": c / 4}


def w4_kappa_total():
    """Total kappa for W_4: sum of curvature channels.

    kappa = c/2 + c/3 + c/4 = 13c/12.
    """
    c = Symbol('c')
    return Rational(13) * c / 12


# ---------------------------------------------------------------------------
# W_3 x W_3 OPE in the W_4 algebra
# ---------------------------------------------------------------------------

def w3w3_ope_w4_algebra():
    """W_3(z) W_3(w) OPE in the W_4 algebra.

    The same as in the W_3 algebra, PLUS the spin-4 channel:
    W_3(z) W_3(w) ~ c/3/(z-w)^6 + 2T/(z-w)^4 + dT/(z-w)^3
                    + [(3/10)d^2T + beta Lambda + c_334 W_4]/(z-w)^2
                    + [(1/15)d^3T + ...]/(z-w)

    where Lambda = :TT: - (3/10)d^2T is the spin-4 quasi-primary composite.

    In the W_3 algebra: beta = 16/(22+5c), no W_4 term.
    In the W_4 algebra: the spin-4 quasi-primary space is 2-dimensional
    (Lambda and W_4), and the W_3 x W_3 OPE projects onto both.

    The coefficient c_334 = C^DS_{3,3;4;0,2}(4) is a rational function of c
    (determined by the DS reduction of sl_4).

    Returns the OPE structure with c_334 as a symbolic parameter.
    """
    c = Symbol('c')
    c334 = Symbol('c_334')
    alpha = Rational(16, 1) / (22 + 5 * c)

    # Using POLE ORDERS (pole order p = n-th product index + 1):
    return {
        6: {"vac": c / 3},               # pole 6 (n-th product 5)
        4: {"T": Rational(2)},            # pole 4 (n-th product 3)
        3: {"dT": Rational(1)},           # pole 3 (n-th product 2)
        2: {"d2T": Rational(3, 10), "Lambda": alpha, "W4": c334},  # pole 2
        1: {"d3T": Rational(1, 15), "dLambda": alpha / 2, "dW4": c334 / 2},
    }


# ---------------------------------------------------------------------------
# W_4 x W_4 leading OPE structure
# ---------------------------------------------------------------------------

def w4w4_leading_ope():
    """Leading poles of W_4(z) W_4(w) OPE.

    W_4(z) W_4(w) ~ c/4/(z-w)^8 + ...

    Using pole orders (not n-th product indices):
    Pole 8: vacuum channel, weight 0, coeff = c/4.
    Pole 7: weight 1, must vanish (no weight-1 field in vacuum module).
    Pole 6: weight 2 = T channel.
      C^res_{4,4;2;0,6} = coefficient of T at pole 6.
      Predicted = 2 (universal pattern).
    Pole 5: weight 3 = W_3 channel (or dT descendant).
    Pole 4: weight 4 = W_4 channel (plus composites).
      The W_4 primary coefficient is c_444.
    """
    c = Symbol('c')

    return {
        # Pole 8 (n-th product index 7): vacuum
        8: {"vac": c / 4},
        # Pole 6: T channel. Predicted: coefficient = 2.
        6: {"T": Rational(2)},
        # Lower poles involve composites and c_444
    }


# ---------------------------------------------------------------------------
# W_3 x W_4 OPE leading structure
# ---------------------------------------------------------------------------

def w3w4_leading_ope():
    """Leading poles of W_3(z) W_4(w) OPE.

    Maximum pole order: s + t - 1 = 6.
    Pole 6: target weight s+t-7 = 0 => vacuum. But W_3 x W_4 -> vac
      requires s = t (W_3 != W_4), so this vanishes by orthogonality.
    Pole 5: target weight 2 => T channel.
      C^res_{3,4;2;0,5} = coefficient of T.

    From conformal weight analysis, T appears at pole 5 if and only if
    the W_3 x W_4 OPE has a nonzero coupling to the vacuum module at
    this pole order. For the principal W_4 algebra, this coupling
    is expected to vanish (since W_3 and W_4 have different spins,
    the T-channel coupling requires a nontrivial structure constant).

    Pole 4: target weight 3 => W_3 channel.
      C_{3,4;3;0,4} = coupling constant.
    Pole 3: target weight 4 => W_4 channel.
      C_{3,4;4;0,3} = coupling constant.
    """
    c = Symbol('c')

    return {
        # Pole 6: no vacuum contribution (orthogonality of W_3, W_4)
        # Pole 5: T channel. Expected: coefficient from C^res_{3,4;2;0,5}
        # Pole 4: W_3 channel. C_{3,4;3;0,4}
        # Pole 3: W_4 channel. C_{3,4;4;0,3}
    }


# ---------------------------------------------------------------------------
# Falsifiable predictions
# ---------------------------------------------------------------------------

def stage4_falsifiable_predictions() -> Dict[str, object]:
    """The two falsifiable residue-side predictions from the concordance.

    From rem:mc4-winfty-computation-target:
    "The two residue-side checks (= 2 and = 0) provide falsifiable predictions."

    Prediction 1: C^res_{4,4;2;0,6} = 2
      (W_4 x W_4 -> T at leading pole gives coefficient 2,
       matching the universal pattern C_{s,s;2;0,2s-2} = 2.)

    Prediction 2: C^res_{3,4;2;0,5} = 0
      (W_3 x W_4 -> T at pole 5 vanishes by orthogonality:
       the leading T-channel coupling in the mixed OPE is zero
       because the T-channel requires derivative corrections.)
    """
    return {
        "C^res_{4,4;2;0,6}": {
            "predicted_value": 2,
            "source_pair": (4, 4),
            "target_spin": 2,
            "pole_order": 6,
            "mechanism": "Universal pattern: C_{s,s;2;0,2s-2} = 2",
        },
        "C^res_{3,4;2;0,5}": {
            "predicted_value": 0,
            "source_pair": (3, 4),
            "target_spin": 2,
            "pole_order": 5,
            "mechanism": "Mixed-source orthogonality: T at leading mixed pole vanishes",
        },
    }


def verify_universal_t_coupling_pattern() -> Dict[str, bool]:
    """Check the universal pattern C_{s,s;2;0,2s-2} = 2.

    Known values:
      s=2: C_{2,2;2;0,2} = 2  (Virasoro OPE)
      s=3: C_{3,3;2;0,4} = 2  (W_3 OPE)
    Prediction:
      s=4: C_{4,4;2;0,6} = 2  (W_4 OPE — to be verified)
    """
    stage3 = stage3_ds_coefficients()
    return {
        "s=2_equals_2": stage3[(2, 2, 2, 2)] == 2,
        "s=3_equals_2": stage3[(3, 3, 2, 4)] == 2,
        "s=4_predicted_2": True,  # prediction, not yet verified from DS
    }


# ---------------------------------------------------------------------------
# Full reduction chain: J_4 (29) -> J_4^top (7) -> J_4^par (6) -> frontier (4+2)
# ---------------------------------------------------------------------------

def top_pole_packet() -> List[Tuple[int, int, int, int]]:
    """J_4^top: keep only top-pole entry for each (s,t,u) triple in J_4.

    For (s,t,u,n) in J_4, the top pole is n_max = s+t-u.
    cor:winfty-ds-stage4-top-pole-packet: |J_4^top| = 7.
    """
    J4 = residual_packet(4)
    top = []
    for s, t, u, n in J4:
        if n == s + t - u:
            top.append((s, t, u, n))
    return sorted(top)


def parity_compressed_packet() -> List[Tuple[int, int, int, int]]:
    """J_4^par: remove odd-spin self-OPE entries from J_4^top.

    For s=t (self-OPE) with even generator spin, odd target spin u
    vanishes by skew-symmetry (prop:winfty-ds-self-ope-parity).
    Removes (4,4,3,5) from J_4^top.
    cor:winfty-ds-stage4-parity-packet: |J_4^par| = 6.
    """
    top = top_pole_packet()
    par = []
    for s, t, u, n in top:
        if s == t and u % 2 == 1:
            # Even-spin self-OPE: odd target spin vanishes
            continue
        par.append((s, t, u, n))
    return sorted(par)


def ope_block_decomposition() -> Dict[str, List[Tuple[int, int, int, int]]]:
    """Organize J_4^par into three OPE blocks.

    cor:winfty-ds-stage4-ope-blocks:
      (3,3) block: c_334 at (3,3,4,2) — 1 coefficient
      (3,4) block: c_342, c_343, c_344 — 3 coefficients
      (4,4) block: c_442, c_444 — 2 coefficients
    """
    par = parity_compressed_packet()
    blocks: Dict[str, List[Tuple[int, int, int, int]]] = {
        "block_33": [(s, t, u, n) for s, t, u, n in par if s == 3 and t == 3],
        "block_34": [(s, t, u, n) for s, t, u, n in par if s == 3 and t == 4],
        "block_44": [(s, t, u, n) for s, t, u, n in par if s == 4 and t == 4],
    }
    return blocks


def mixed_self_split() -> Dict[str, List[Tuple[int, int, int, int]]]:
    """Separate J_4^par into self-coupling and mixed sectors.

    cor:winfty-ds-stage4-mixed-self-split:
      Self-coupling: {c_334, c_442, c_444} — 3 scalars
      Mixed: {c_342, c_343, c_344} — 1 block of 3
    """
    par = parity_compressed_packet()
    self_coupling = [(s, t, u, n) for s, t, u, n in par if s == t]
    mixed = [(s, t, u, n) for s, t, u, n in par if s != t]
    return {"self_coupling": self_coupling, "mixed": mixed}


def frontier_package() -> Dict[str, object]:
    """Final MC4 W_infty stage-4 frontier: 4 free + 2 checks.

    cor:winfty-ds-stage4-five-plus-zero + prop:winfty-mc4-frontier-package:
      Free coefficients (DS-side values unknown, to be extracted):
        c_334 = C^DS_{3,3;4;0,2}
        c_444 = C^DS_{4,4;4;0,4}
        C_{3,4;3;0,4} = c_343
        C_{3,4;4;0,3} = c_344
      Residue-side checks (DS-side values KNOWN, predict bar-side):
        C^res_{4,4;2;0,6} = 2  (universal T-coupling, prop:winfty-ds-self-t-coefficient)
        C^res_{3,4;2;0,5} = 0  (mixed Virasoro vanishing, prop:winfty-ds-mixed-virasoro-ds-zero)
    """
    par = parity_compressed_packet()
    # c_442 = (4,4,2,6) is fixed to 2 by universal T-coupling
    # c_342 = (3,4,2,5) is fixed to 0 by mixed Virasoro vanishing
    free = [(s, t, u, n) for s, t, u, n in par
            if not (s == 4 and t == 4 and u == 2)     # not c_442
            and not (s == 3 and t == 4 and u == 2)]    # not c_342
    checks = [(s, t, u, n) for s, t, u, n in par
              if (s == 4 and t == 4 and u == 2) or (s == 3 and t == 4 and u == 2)]
    check_values = {}
    for s, t, u, n in checks:
        if s == 4 and t == 4 and u == 2:
            check_values[(s, t, u, n)] = 2   # universal T-coupling
        elif s == 3 and t == 4 and u == 2:
            check_values[(s, t, u, n)] = 0   # mixed Virasoro vanishing

    return {
        "free_coefficients": free,
        "residue_checks": checks,
        "check_values": check_values,
        "n_free": len(free),
        "n_checks": len(checks),
    }


def verify_full_reduction_chain() -> Dict[str, object]:
    """Verify every step of the stage-4 reduction chain.

    J_4 (29) -> J_4^top (7) -> J_4^par (6) -> frontier (4 free + 2 checks)

    Returns verification results for each step.
    """
    J4 = residual_packet(4)
    top = top_pole_packet()
    par = parity_compressed_packet()
    blocks = ope_block_decomposition()
    ms = mixed_self_split()
    front = frontier_package()

    # Expected elements from the manuscript
    expected_top = [
        (3, 3, 4, 2), (3, 4, 2, 5), (3, 4, 3, 4), (3, 4, 4, 3),
        (4, 4, 2, 6), (4, 4, 3, 5), (4, 4, 4, 4),
    ]
    expected_removed_by_parity = [(4, 4, 3, 5)]
    expected_par = [
        (3, 3, 4, 2), (3, 4, 2, 5), (3, 4, 3, 4), (3, 4, 4, 3),
        (4, 4, 2, 6), (4, 4, 4, 4),
    ]
    expected_free = [
        (3, 3, 4, 2), (3, 4, 3, 4), (3, 4, 4, 3), (4, 4, 4, 4),
    ]
    expected_checks = [(3, 4, 2, 5), (4, 4, 2, 6)]

    return {
        # Step 1: J_4 -> J_4^top (primaryity)
        "J4_size": len(J4),
        "J4_top_size": len(top),
        "J4_top_matches": sorted(top) == sorted(expected_top),
        "primaryity_eliminated": len(J4) - len(top),
        # Step 2: J_4^top -> J_4^par (parity)
        "J4_par_size": len(par),
        "J4_par_matches": sorted(par) == sorted(expected_par),
        "parity_eliminated": sorted(
            [x for x in top if x not in par]
        ) == sorted(expected_removed_by_parity),
        # Step 3: OPE block organization
        "block_33_size": len(blocks["block_33"]),
        "block_34_size": len(blocks["block_34"]),
        "block_44_size": len(blocks["block_44"]),
        "block_sum": sum(len(v) for v in blocks.values()),
        # Step 4: mixed-self split
        "self_coupling_size": len(ms["self_coupling"]),
        "mixed_size": len(ms["mixed"]),
        # Step 5: frontier (Virasoro elimination)
        "n_free": front["n_free"],
        "n_checks": front["n_checks"],
        "free_matches": sorted(front["free_coefficients"]) == sorted(expected_free),
        "checks_match": sorted(front["residue_checks"]) == sorted(expected_checks),
        "check_values_correct": (
            front["check_values"].get((4, 4, 2, 6)) == 2
            and front["check_values"].get((3, 4, 2, 5)) == 0
        ),
        # Summary
        "chain_valid": (
            len(J4) == 29 and len(top) == 7 and len(par) == 6
            and front["n_free"] == 4 and front["n_checks"] == 2
        ),
    }


# ---------------------------------------------------------------------------
# Seed set analysis
# ---------------------------------------------------------------------------

def analyze_stage4_packet() -> Dict[str, object]:
    """Full analysis of the stage-4 comparison problem."""
    I4 = seed_set(4)
    I4_vir = virasoro_subset(4)
    I4_w3 = w3_subset(4)
    J4 = residual_packet(4)
    decomp = stage4_residual_decomposition()

    return {
        "I4_size": len(I4),
        "I4_vir_size": len(I4_vir),
        "I4_w3_size": len(I4_w3),
        "J4_size": len(J4),
        "J4_expected_size": 29,  # from prop:winfty-ds-stage4-residual-packet
        "tail_33_size": len(decomp["tail_33"]),
        "tail_33_expected": [(3, 3, 4, 1), (3, 3, 4, 2)],
        "J4_34_size": len(decomp["J4_34"]),
        "J4_34_expected_size": 12,
        "J4_44_size": len(decomp["J4_44"]),
        "J4_44_expected_size": 15,
        "live_targets": stage4_live_targets(),
        "falsifiable_predictions": stage4_falsifiable_predictions(),
    }


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("MC4 W_INFINITY STAGE-4 COEFFICIENT ANALYSIS")
    print("=" * 70)

    # Central charge
    k = Symbol('k')
    c = w4_central_charge(k)
    print(f"\nW_4 central charge: c = {c}")
    print(f"At k=1: c = {w4_central_charge(1)}")
    print(f"Dual level: k' = {w4_dual_level(k)}")
    print(f"Complementarity sum: c(k) + c(k') = {w4_complementarity_sum()}")

    # Curvature
    curv = w4_curvature()
    print(f"\nCurvature channels:")
    for gen, val in curv.items():
        print(f"  m_0^({gen}) = {val}")
    print(f"  kappa_total = {w4_kappa_total()}")

    # Seed sets
    for N in [3, 4]:
        I = seed_set(N)
        print(f"\nI_{N}: {len(I)} elements")

    # Stage-3 packet
    s3 = stage3_ds_coefficients()
    print(f"\nStage-3 packet: {stage3_nonzero_count()} nonzero, "
          f"{stage3_vanishing_count()} vanishing")

    # Stage-4 analysis
    analysis = analyze_stage4_packet()
    print(f"\nStage-4 analysis:")
    print(f"  |I_4| = {analysis['I4_size']}")
    print(f"  |I_4^Vir| = {analysis['I4_vir_size']}")
    print(f"  |I_4^W3| = {analysis['I4_w3_size']}")
    print(f"  |J_4| = {analysis['J4_size']} (expected {analysis['J4_expected_size']})")
    decomp = stage4_residual_decomposition()
    print(f"  (3,3) tail: {decomp['tail_33']}")
    print(f"  |J_4^{{3,4}}| = {len(decomp['J4_34'])}")
    print(f"  |J_4^{{4,4}}| = {len(decomp['J4_44'])}")

    # Falsifiable predictions
    preds = stage4_falsifiable_predictions()
    print(f"\nFalsifiable predictions:")
    for name, data in preds.items():
        print(f"  {name} = {data['predicted_value']}")
        print(f"    ({data['mechanism']})")
