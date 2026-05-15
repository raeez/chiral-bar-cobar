"""Exact W_4 stage-4 identity packet analysis.

Ground truth from the manuscript
(bar_cobar_adjunction_curved.tex, editorial_constitution.tex):
  rem:mc4-winfty-computation-target: isolate the exact six-entry stage-4
  identity packet on I_4, make the principal DS targets explicit, and compare
  the bar-side coefficients with those values.

  Stage-3 packet (prop:winfty-ds-stage3-explicit-packet):
    C^DS_{2,2;2;0,2}(3) = 2   (T x T -> T at pole 2)
    C^DS_{2,3;3;0,2}(3) = 3   (T x W -> W at pole 2)
    C^DS_{3,3;2;0,4}(3) = 2   (W x W -> T at pole 4)
    All other C in I_3 = 0.

  Stage-4 exact identity packet:
    Six channels on I_4:
      C_{3,3;4;0,2}, C_{4,4;4;0,4}, C_{3,4;3;0,4}, C_{3,4;4;0,3},
      C_{4,4;2;0,6}, C_{3,4;2;0,5}.
    Packet split:
      - four residual higher-spin channels;
      - two Virasoro-target identities with principal values 2 and 0.

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
  - The top primary W^{(u)} channel occurs at pole order n = s + t - u
  - The vacuum leading pole is 2s for a same-spin self-OPE and vanishes
    for mixed different-weight primaries
  - Central charge relation: c_DS(k) + c_DS(k') = sigma (complementarity sum)
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from sympy import Rational, Symbol, simplify


# ---------------------------------------------------------------------------
# Central charge
# ---------------------------------------------------------------------------

def w4_central_charge(k):
    """Central charge of principal W_4 = DS of sl_4-hat at level k.

    c = 3 - 60(k+3)^2/(k+4)

    Fateev-Lukyanov formula at N=4.  Decisive test: k=1 gives c=-189.
    """
    kN = k + 4
    k_shift = k + 3  # k + N - 1
    return Rational(3) - Rational(60) * k_shift**2 / kN


def w4_dual_level(k):
    """Feigin-Frenkel dual level: k' = -k - 2h^vee = -k - 8 (sl_4)."""
    return -k - 8


def w4_complementarity_sum(k=None):
    r"""c(k) + c(k') for the W_4 algebra.

    For the principal W_N algebra from sl_N, the complementarity sum is
    2(N-1) + 4N(N^2-1) = 246 at N=4 (Freudenthal-de Vries).
    """
    if k is None:
        k = Symbol('k')
    c1 = w4_central_charge(k)
    k_dual = w4_dual_level(k)
    c2 = w4_central_charge(k_dual)
    return simplify(c1 + c2)


# ---------------------------------------------------------------------------
# Scope and firewall surface
# ---------------------------------------------------------------------------

def stage4_scope_certificate() -> Dict[str, object]:
    """Machine-readable scope certificate for this finite W_4 surface.

    The engine records the finite primary top-pole packet at stage 4. It
    does not certify a full OPE, an all-genus shadow tower, a full
    multiweight package, or a Maurer-Cartan solution.
    """
    return {
        "object": "principal W_4 stage-4 coefficient surface",
        "finite_statement": "stage-4 primary top-pole scalar packet on I_4",
        "certified_stage": 4,
        "negative_claims": {
            "not_full_ope": True,
            "not_all_genus": True,
            "not_full_multiweight": True,
            "not_full_mc_data": True,
            "not_koszul_duality": True,
            "not_derived_center_or_bulk": True,
        },
        "holographic_package_entries": (
            "A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol",
        ),
        "modular_koszul_compute_package_projections": (
            "Fact_X(L)", "barB_X(L)", "Theta_L", "L_L",
            "(V_br,T_br)", "R4_mod(L)",
        ),
        "object_firewall": {
            "bar_cobar_inversion": (
                "Omega(B(A))=A is bar-cobar inversion, not Koszul duality"
            ),
            "verdier_branch": (
                "A^! is the Verdier/continuous-linear dual branch under "
                "finite-type/completed hypotheses"
            ),
            "derived_center": (
                "Z_ch^der(A)=ChirHoch^*(A,A) is Hochschild/bulk, "
                "not Koszul dual"
            ),
        },
        "kernel_constants": {
            "affine_raw": "k*Omega_tr/z",
            "kz": "Omega/((k+h^vee)z)",
            "heisenberg": "k/z",
            "virasoro": "(c/2)/z^3 + 2T/z",
        },
    }


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


def incremental_virasoro_new_packet(stage: int) -> List[Tuple[int, int, int, int]]:
    r"""I_stage^{Vir,new} = I_stage^{Vir} \ I_{stage-1}.

    This is the exact new Virasoro-source block introduced in
    prop:winfty-ds-stage-growth-packet, with ``stage = N+1``.
    """
    if stage < 4:
        raise ValueError("incremental packets are defined for stage >= 4")
    prev = set(seed_set(stage - 1))
    return sorted(
        entry for entry in virasoro_subset(stage)
        if entry not in prev
    )


def incremental_interacting_packet(stage: int) -> List[Tuple[int, int, int, int]]:
    r"""J_stage = I_stage \ (I_{stage-1} cup I_stage^{Vir,new}).

    This is the stage-growth packet of
    prop:winfty-ds-stage-growth-packet, written with ``stage = N+1``.
    """
    if stage < 4:
        raise ValueError("incremental packets are defined for stage >= 4")
    current = set(seed_set(stage))
    prev = set(seed_set(stage - 1))
    vir_new = set(incremental_virasoro_new_packet(stage))
    return sorted(current - prev - vir_new)


def incremental_top_pole_packet(stage: int) -> List[Tuple[int, int, int, int]]:
    r"""J_stage^{top}: top-pole subset of the incremental interacting packet."""
    return sorted(
        entry for entry in incremental_interacting_packet(stage)
        if entry[3] == entry[0] + entry[1] - entry[2]
    )


def incremental_reduced_packet(stage: int) -> List[Tuple[int, int, int, int]]:
    r"""J_stage^{red}: top-pole packet after odd self-OPE parity removal."""
    reduced = []
    for s, t, u, n in incremental_top_pole_packet(stage):
        if s == t and u % 2 == 1:
            continue
        reduced.append((s, t, u, n))
    return sorted(reduced)


def incremental_reduced_block_decomposition(
    stage: int,
) -> Dict[Tuple[int, int], List[Tuple[int, int, int, int]]]:
    r"""Partition J_stage^{red} by source pair (s,t)."""
    blocks: Dict[Tuple[int, int], List[Tuple[int, int, int, int]]] = {}
    for entry in incremental_reduced_packet(stage):
        pair = (entry[0], entry[1])
        blocks.setdefault(pair, []).append(entry)
    return dict(sorted(blocks.items()))


def incremental_higher_spin_channels(stage: int) -> List[Tuple[int, int, int, int]]:
    """Higher-spin channels in the reduced incremental packet."""
    return sorted(
        entry for entry in incremental_reduced_packet(stage)
        if entry[2] != 2
    )


def incremental_higher_spin_block_decomposition(
    stage: int,
) -> Dict[Tuple[int, int], List[Tuple[int, int, int, int]]]:
    r"""Partition J_stage^{hs} by source pair (s,t)."""
    blocks: Dict[Tuple[int, int], List[Tuple[int, int, int, int]]] = {}
    for entry in incremental_higher_spin_channels(stage):
        pair = (entry[0], entry[1])
        blocks.setdefault(pair, []).append(entry)
    return dict(sorted(blocks.items()))


def incremental_higher_spin_block(
    stage: int,
    source_pair: Tuple[int, int],
) -> List[Tuple[int, int, int, int]]:
    r"""Return the source-pair block inside J_stage^{hs}."""
    return incremental_higher_spin_block_decomposition(stage).get(source_pair, [])


def incremental_higher_spin_singleton_blocks(
    stage: int,
) -> Dict[Tuple[int, int], List[Tuple[int, int, int, int]]]:
    r"""Source-pair blocks of J_stage^{hs} having exactly one channel."""
    return {
        pair: block
        for pair, block in incremental_higher_spin_block_decomposition(stage).items()
        if len(block) == 1
    }


def incremental_higher_spin_nonsingleton_blocks(
    stage: int,
) -> Dict[Tuple[int, int], List[Tuple[int, int, int, int]]]:
    r"""Source-pair blocks of J_stage^{hs} having more than one channel."""
    return {
        pair: block
        for pair, block in incremental_higher_spin_block_decomposition(stage).items()
        if len(block) > 1
    }


def incremental_higher_spin_target_decomposition(
    stage: int,
) -> Dict[int, List[Tuple[int, int, int, int]]]:
    r"""Partition J_stage^{hs} by target spin u."""
    blocks: Dict[int, List[Tuple[int, int, int, int]]] = {}
    for entry in incremental_higher_spin_channels(stage):
        blocks.setdefault(entry[2], []).append(entry)
    return dict(sorted((u, sorted(block)) for u, block in blocks.items()))


def incremental_higher_spin_nonsingleton_target_decomposition(
    stage: int,
) -> Dict[int, List[Tuple[int, int, int, int]]]:
    r"""Partition the nonsingleton part of J_stage^{hs} by target spin u."""
    blocks: Dict[int, List[Tuple[int, int, int, int]]] = {}
    for block in incremental_higher_spin_nonsingleton_blocks(stage).values():
        for entry in block:
            blocks.setdefault(entry[2], []).append(entry)
    return dict(sorted((u, sorted(block)) for u, block in blocks.items()))


def incremental_virasoro_target_channels(stage: int) -> List[Tuple[int, int, int, int]]:
    """Virasoro-target channels in the reduced incremental packet."""
    return sorted(
        entry for entry in incremental_reduced_packet(stage)
        if entry[2] == 2
    )


def incremental_virasoro_target_identities(stage: int) -> Dict[Tuple[int, int, int, int], int]:
    r"""Formal Virasoro-target values in J_stage^{red} under normalized pairings.

    Mixed channels with target spin 2 vanish by mixed-weight orthogonality,
    while self-coupling target-2 channels equal 2 by the universal
    stress-tensor coefficient.
    """
    values: Dict[Tuple[int, int, int, int], int] = {}
    for s, t, u, n in incremental_virasoro_target_channels(stage):
        values[(s, t, u, n)] = 2 if s == t else 0
    return values


def analyze_incremental_packet(stage: int) -> Dict[str, object]:
    """Summary of J_stage, J_stage^{top}, and J_stage^{red}.

    For stages beyond 4, Virasoro-target values are formal diagnostics
    from the normalized-pairing pattern, not certified DS coefficients.
    """
    J = incremental_interacting_packet(stage)
    top = incremental_top_pole_packet(stage)
    red = incremental_reduced_packet(stage)
    return {
        "stage": stage,
        "J_size": len(J),
        "top_size": len(top),
        "red_size": len(red),
        "blocks": incremental_reduced_block_decomposition(stage),
        "higher_spin_channels": incremental_higher_spin_channels(stage),
        "higher_spin_blocks": incremental_higher_spin_block_decomposition(stage),
        "higher_spin_singletons": incremental_higher_spin_singleton_blocks(stage),
        "higher_spin_nonsingletons": incremental_higher_spin_nonsingleton_blocks(stage),
        "higher_spin_targets": incremental_higher_spin_target_decomposition(stage),
        "higher_spin_nonsingleton_targets": incremental_higher_spin_nonsingleton_target_decomposition(stage),
        "virasoro_target_channels": incremental_virasoro_target_channels(stage),
        "virasoro_target_values": incremental_virasoro_target_identities(stage),
        "virasoro_target_value_scope": (
            "formal normalized-pairing diagnostic; stage 4 is the W_4 "
            "principal DS finite packet checked by this module"
        ),
        "virasoro_target_values_certified_for_stage": stage == 4,
    }


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
# Stage-4 exact packet on I_4
# ---------------------------------------------------------------------------

def stage4_exact_identity_packet_labels() -> List[str]:
    """Labels for the exact six-entry stage-4 identity packet on I_4."""
    return [
        "C_{3,3;4;0,2}",
        "C_{4,4;4;0,4}",
        "C_{3,4;3;0,4}",
        "C_{3,4;4;0,3}",
        "C_{4,4;2;0,6}",
        "C_{3,4;2;0,5}",
    ]


def stage4_live_targets() -> List[str]:
    """Compatibility alias for the exact six-entry stage-4 packet labels."""
    return stage4_exact_identity_packet_labels()


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


def stage4_exact_identity_packet() -> List[Tuple[int, int, int, int]]:
    """Exact six-entry stage-4 identity packet on I_4."""
    return parity_compressed_packet()


def stage4_principal_higher_spin_squared_couplings(c=None) -> Dict[
    Tuple[int, int, int, int], object
]:
    r"""Squared principal DS higher-spin couplings in the stage-4 packet.

    These are the four higher-spin entries of the finite stage-4 packet,
    in the Zamolodchikov normalization
    ``<W^(s)(z) W^(s)(0)> = (c/s) z^(-2s)``.  The function deliberately
    returns squared rational functions in ``Q(c)``. It does not choose a
    square-root branch for the OPE coefficients themselves.

    Manuscript anchors:
      eq:c334-explicit,
      eq:c444-explicit,
      eq:c343-explicit,
      eq:c344-explicit.
    """
    if c is None:
        c = Symbol('c')

    c334_sq = (
        Rational(42) * c**2 * (5 * c + 22)
        / ((c + 24) * (7 * c + 68) * (3 * c + 46))
    )
    c444_sq = (
        Rational(112) * c**2 * (2 * c - 1) * (3 * c + 46)
        / ((c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3))
    )
    return {
        (3, 3, 4, 2): simplify(c334_sq),
        (4, 4, 4, 4): simplify(c444_sq),
        (3, 4, 3, 4): simplify(Rational(9, 16) * c334_sq),
        (3, 4, 4, 3): simplify(Rational(5, 7) * c334_sq),
    }


def stage4_coefficient_field_policy() -> Dict[str, object]:
    """Field-extension policy for the stage-4 higher-spin coefficients."""
    return {
        "base_field": "Q(c)",
        "stored_values": "squared principal DS rational functions",
        "branch_certified": False,
        "branch_policy": (
            "this scaffold records squared values only; square-root signs "
            "and field embeddings are not chosen here"
        ),
        "generic_extension_generators": (
            "sqrt(c_334^2)", "sqrt(c_444^2)",
        ),
        "mixed_square_relations": {
            "C_{3,4;3;0,4}^2": "(9/16)*c_334^2",
            "C_{3,4;4;0,3}^2": "(5/7)*c_334^2",
        },
    }


def stage4_residual_higher_spin_channels() -> List[Tuple[int, int, int, int]]:
    """Residual higher-spin channels inside the exact stage-4 packet."""
    return [
        (3, 3, 4, 2),
        (3, 4, 3, 4),
        (3, 4, 4, 3),
        (4, 4, 4, 4),
    ]


def stage4_virasoro_target_channels() -> List[Tuple[int, int, int, int]]:
    """Virasoro-target channels inside the exact stage-4 packet."""
    return [
        (3, 4, 2, 5),
        (4, 4, 2, 6),
    ]


def stage4_virasoro_target_identities() -> Dict[Tuple[int, int, int, int], int]:
    """Principal DS values for the Virasoro-target channels at stage 4."""
    return {
        (4, 4, 2, 6): 2,
        (3, 4, 2, 5): 0,
    }


# ---------------------------------------------------------------------------
# OPE weight bounds
# ---------------------------------------------------------------------------

def ope_max_pole_order(s: int, t: int) -> int:
    """Maximum pole order in W_s(z) W_t(w) OPE.

    Same-spin self-OPEs have the vacuum two-point leading pole 2s:
    T x T has pole 4, W_3 x W_3 has pole 6, and W_4 x W_4 has pole 8.
    Mixed different-weight primaries have no vacuum pairing, so their
    first possible singular order is s + t - 1.
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

    Target weight = s + t - n. This is a primary generator if the weight
    matches a generator spin (2, 3, or 4 for W_4).
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
    """Channel-refined kappa entries for the W_4 scalar shadow lane.

    These are the leading same-spin vacuum OPE coefficients c/s in the
    principal-DS strong-generator normalization. They are scalar
    bar-complex inputs, not a Hochschild derived-centre computation and
    not a physical-bulk reconstruction.

    m_0^(T) = c/2   (from quartic pole T_{(3)}T)
    m_0^(W_3) = c/3  (from sixth-order pole W_3_{(5)}W_3)
    m_0^(W_4) = c/4  (from eighth-order pole W_4_{(7)}W_4)

    Kappa total: c(1/2 + 1/3 + 1/4) = 13c/12
    """
    c = Symbol('c')
    return {"T": c / 2, "W3": c / 3, "W4": c / 4}


def w4_kappa_total():
    """Total scalar kappa for W_4: trace of the channel-refined entries.

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
      Principal DS / Ward-normalized value = 2.
    Pole 5: weight 3 = W_3 channel (or dT descendant).
    Pole 4: weight 4 = W_4 channel (plus composites).
      The W_4 primary coefficient is c_444.
    """
    c = Symbol('c')
    c444 = Symbol('c_444')

    return {
        # Pole 8 (n-th product index 7): vacuum
        8: {"vac": c / 4},
        # Pole 6: T channel; principal DS / Ward-normalized value.
        6: {"T": Rational(2)},
        # Pole 4: W_4 primary channel, modulo Virasoro composites.
        4: {"W4": c444},
    }


# ---------------------------------------------------------------------------
# W_3 x W_4 OPE leading structure
# ---------------------------------------------------------------------------

def w3w4_leading_ope():
    """Leading poles of W_3(z) W_4(w) OPE.

    Maximum pole order: s + t - 1 = 6.
    Pole 6: target weight s+t-6 = 1. There is no weight-1 generator
      in the vacuum module, so no primary seed is recorded there.
    Pole 5: target weight 2 => T channel.
      C^res_{3,4;2;0,5} = coefficient of T.

    The principal W_4 value of this mixed T-channel is zero: the Ward
    identity reduces the three-point function <T W_3 W_4> to the
    two-point function <W_3 W_4>, which vanishes by conformal-weight
    orthogonality.

    Pole 4: target weight 3 => W_3 channel.
      C_{3,4;3;0,4} = coupling constant.
    Pole 3: target weight 4 => W_4 channel.
      C_{3,4;4;0,3} = coupling constant.
    """
    c343 = Symbol('c_343')
    c344 = Symbol('c_344')

    return {
        # Pole 5: T channel, fixed by mixed-source orthogonality.
        5: {"T": Rational(0)},
        # Pole 4: W_3 primary channel.
        4: {"W3": c343},
        # Pole 3: W_4 primary channel.
        3: {"W4": c344},
    }


# ---------------------------------------------------------------------------
# Distinguished Virasoro-target channels
# ---------------------------------------------------------------------------

def stage4_virasoro_target_identity_data() -> Dict[str, object]:
    """Data for the two distinguished stage-4 Virasoro-target channels.

    On the theorem surface these are the two distinguished stage-4
    Virasoro-target channels whose principal DS values are already fixed.
    They become residue-side checks only after the normalized residue
    two-point/Ward package is supplied.
    """
    return {
        "C_{4,4;2;0,6}": {
            "principal_value": 2,
            "verified_value": 2,
            "theorematic_value": 2,  # Compatibility alias.
            "value_scope": "principal DS; residue side fixed on the Ward-normalized locus",
            "certified_side": "principal DS",
            "residue_certified": False,
            "residue_certification": (
                "requires the normalized residue two-point/Ward package"
            ),
            "not_derived_center_or_bulk": True,
            "not_full_mc_data": True,
            "not_full_multiweight_data": True,
            "source_pair": (4, 4),
            "target_spin": 2,
            "pole_order": 6,
            "mechanism": "Universal T-coupling: C_{s,s;2;0,2s-2} = 2",
        },
        "C_{3,4;2;0,5}": {
            "principal_value": 0,
            "verified_value": 0,
            "theorematic_value": 0,  # Compatibility alias.
            "value_scope": "principal DS; residue side fixed on the Ward-normalized locus",
            "certified_side": "principal DS",
            "residue_certified": False,
            "residue_certification": (
                "requires the normalized residue two-point/Ward package"
            ),
            "not_derived_center_or_bulk": True,
            "not_full_mc_data": True,
            "not_full_multiweight_data": True,
            "source_pair": (3, 4),
            "target_spin": 2,
            "pole_order": 5,
            "mechanism": "Mixed-source orthogonality: T at leading mixed pole vanishes",
        },
    }



def verify_universal_t_coupling_pattern() -> Dict[str, bool]:
    """Check the universal pattern C_{s,s;2;0,2s-2} = 2.

    Values:
      s=2: C_{2,2;2;0,2} = 2  (Virasoro OPE)
      s=3: C_{3,3;2;0,4} = 2  (W_3 OPE)
      s=4: C_{4,4;2;0,6} = 2  (W_4 Ward identity)
    """
    stage3 = stage3_ds_coefficients()
    stage4 = stage4_virasoro_target_identities()
    return {
        "s=2_equals_2": stage3[(2, 2, 2, 2)] == 2,
        "s=3_equals_2": stage3[(3, 3, 2, 4)] == 2,
        "s=4_equals_2": stage4[(4, 4, 2, 6)] == 2,
    }


# ---------------------------------------------------------------------------
# Full reduction chain: J_4 (29) -> J_4^top (7) -> J_4^par (6) -> exact split (4+2)
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

    For s=t (self-OPE), odd top-pole order n = 2s-u vanishes by
    skew-symmetry (prop:winfty-ds-self-ope-parity).
    Removes (4,4,3,5) from J_4^top.
    cor:winfty-ds-stage4-parity-packet: |J_4^par| = 6.
    """
    top = top_pole_packet()
    par = []
    for s, t, u, n in top:
        if s == t and n % 2 == 1:
            # Self-OPE: odd top-pole channel vanishes.
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


def stage4_exact_packet_split() -> Dict[str, object]:
    """Split the exact six-entry W_4 stage-4 packet as 4 + 2.

    The exact stage-4 identity packet on I_4 has six entries:
      - four residual higher-spin channels;
      - two Virasoro-target channels with fixed principal DS values.

    Legacy free/check aliases are returned for downstream compute callers.
    """
    exact_packet = stage4_exact_identity_packet()
    higher_spin = stage4_residual_higher_spin_channels()
    virasoro_targets = stage4_virasoro_target_channels()
    virasoro_values = stage4_virasoro_target_identities()

    return {
        "coefficient_scope": "finite primary top-pole scalar packet on I_4",
        "certified_stage": 4,
        "not_full_ope": True,
        "not_all_genus": True,
        "not_full_multiweight": True,
        "not_full_mc_data": True,
        "exact_identity_packet": exact_packet,
        "higher_spin_channels": higher_spin,
        "higher_spin_squared_couplings": stage4_principal_higher_spin_squared_couplings(),
        "coefficient_field_policy": stage4_coefficient_field_policy(),
        "virasoro_target_channels": virasoro_targets,
        "virasoro_target_values": virasoro_values,
        "n_packet": len(exact_packet),
        "n_higher_spin": len(higher_spin),
        "n_virasoro_target": len(virasoro_targets),
        # Backward-compatible aliases.
        "free_coefficients": higher_spin,
        "residue_checks": virasoro_targets,
        "check_values": virasoro_values,
        "n_free": len(higher_spin),
        "n_checks": len(virasoro_targets),
    }


def frontier_package() -> Dict[str, object]:
    """Compatibility alias for stage4_exact_packet_split()."""
    return stage4_exact_packet_split()


def verify_full_reduction_chain() -> Dict[str, object]:
    """Verify every step of the stage-4 reduction chain.

    J_4 (29) -> J_4^top (7) -> J_4^par (6) -> exact packet (4 + 2)

    Returns verification results for each step.
    """
    J4 = residual_packet(4)
    top = top_pole_packet()
    par = parity_compressed_packet()
    blocks = ope_block_decomposition()
    ms = mixed_self_split()
    front = stage4_exact_packet_split()

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
    expected_higher_spin = [
        (3, 3, 4, 2), (3, 4, 3, 4), (3, 4, 4, 3), (4, 4, 4, 4),
    ]
    expected_virasoro_targets = [(3, 4, 2, 5), (4, 4, 2, 6)]
    top_matches = sorted(top) == sorted(expected_top)
    par_matches = sorted(par) == sorted(expected_par)
    parity_eliminated = sorted(
        [x for x in top if x not in par]
    ) == sorted(expected_removed_by_parity)
    higher_spin_matches = (
        sorted(front["higher_spin_channels"]) == sorted(expected_higher_spin)
    )
    virasoro_target_matches = (
        sorted(front["virasoro_target_channels"]) == sorted(expected_virasoro_targets)
    )
    virasoro_target_values_correct = (
        front["virasoro_target_values"].get((4, 4, 2, 6)) == 2
        and front["virasoro_target_values"].get((3, 4, 2, 5)) == 0
    )
    free_matches = (
        sorted(front["free_coefficients"]) == sorted(expected_higher_spin)
    )
    checks_match = (
        sorted(front["residue_checks"]) == sorted(expected_virasoro_targets)
    )
    check_values_correct = (
        front["check_values"].get((4, 4, 2, 6)) == 2
        and front["check_values"].get((3, 4, 2, 5)) == 0
    )

    return {
        # Step 1: J_4 -> J_4^top (primaryity)
        "J4_size": len(J4),
        "J4_top_size": len(top),
        "J4_top_matches": top_matches,
        "primaryity_eliminated": len(J4) - len(top),
        # Step 2: J_4^top -> J_4^par (parity)
        "J4_par_size": len(par),
        "J4_par_matches": par_matches,
        "parity_eliminated": parity_eliminated,
        # Step 3: OPE block organization
        "block_33_size": len(blocks["block_33"]),
        "block_34_size": len(blocks["block_34"]),
        "block_44_size": len(blocks["block_44"]),
        "block_sum": sum(len(v) for v in blocks.values()),
        # Step 4: mixed-self split
        "self_coupling_size": len(ms["self_coupling"]),
        "mixed_size": len(ms["mixed"]),
        # Step 5: exact packet split
        "n_packet": front["n_packet"],
        "n_higher_spin": front["n_higher_spin"],
        "n_virasoro_target": front["n_virasoro_target"],
        "higher_spin_matches": higher_spin_matches,
        "virasoro_target_matches": virasoro_target_matches,
        "virasoro_target_values_correct": virasoro_target_values_correct,
        # Backward-compatible aliases.
        "n_free": front["n_free"],
        "n_checks": front["n_checks"],
        "free_matches": free_matches,
        "checks_match": checks_match,
        "check_values_correct": check_values_correct,
        # Summary
        "chain_valid": (
            len(J4) == 29 and len(top) == 7 and len(par) == 6
            and front["n_higher_spin"] == 4 and front["n_virasoro_target"] == 2
            and top_matches and par_matches and parity_eliminated
            and higher_spin_matches and virasoro_target_matches
            and virasoro_target_values_correct and free_matches
            and checks_match and check_values_correct
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
    front = stage4_exact_packet_split()

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
        "exact_identity_packet": front["exact_identity_packet"],
        "higher_spin_channels": front["higher_spin_channels"],
        "virasoro_target_channels": front["virasoro_target_channels"],
        "virasoro_target_values": front["virasoro_target_values"],
        "virasoro_target_identity_data": stage4_virasoro_target_identity_data(),
        "higher_spin_squared_couplings": front["higher_spin_squared_couplings"],
        "coefficient_field_policy": front["coefficient_field_policy"],
        "scope_certificate": stage4_scope_certificate(),
        "exact_identity_packet_labels": stage4_exact_identity_packet_labels(),
        "live_targets": stage4_live_targets(),
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

    # Distinguished Virasoro-target channels
    preds = stage4_virasoro_target_identity_data()
    print(f"\nStage-4 Virasoro-target identities:")
    for name, data in preds.items():
        print(f"  {name} = {data['principal_value']}")
        print(f"    ({data['mechanism']})")
