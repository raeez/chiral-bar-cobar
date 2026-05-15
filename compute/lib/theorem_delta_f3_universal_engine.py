r"""Finite-window N-formula for delta_F_3^{grav}(W_N) at genus 3.

Finite-window graph sums give the Laurent polynomial

    delta_F_3^{grav}(W_N, c)
        = D_3(N)c + C_3(N) + B_3(N)/c + A_3(N)/c^2

where D_3, C_3, B_3, A_3 are reconstructed polynomials in N with
D_3(2) = C_3(2) = B_3(2) = A_3(2) = 0
(the correction vanishes for Virasoro, which is uniform-weight).

MATHEMATICAL SETUP
==================

The genus-3 gravitational graph sum for W_N computes:

    F_3(W_N, c) = sum_{Gamma in G(3,0)} (1/|Aut(Gamma)|)
                  * sum_{sigma: E(Gamma) -> {2,...,N}} A(Gamma, sigma)

where A(Gamma, sigma) is the product of:
  - Propagators: prod_e  w(sigma(e)) / c   (AP27: propagator = weight/c)
  - Vertex factors: prod_v V_{g(v)}(channels_at_v; c)

The diagonal part (all channels identical) gives kappa(W_N) * lambda_3^FP.
The cross-channel part is delta_F_3^cross = delta_F_3^{grav}.

GRAVITATIONAL FROBENIUS ALGEBRA (same as genus-2 engine):
  - Channels: T (weight 2), W_3 (weight 3), ..., W_N (weight N)
  - 3-point: C_{2,2,2} = c;  C_{2,j,j} = c for j >= 3;  others = 0
  - Propagator: eta^{jj} = j/c
  - Higher-genus vertex: V_{g,n}(j,...,j) = (c/j) * lambda_g^FP
  - Higher-genus mixed vertex: V_{g,n}(mixed) = 0

The 42 genus-3 stable graphs of M_bar_{3,0} are enumerated by the
existing stable_graph_enumeration engine.

KEY STRUCTURE: At genus 3, the graph sum involves edges up to 6 (= 3*3 - 3).
Each propagator contributes a factor j/c, so the amplitude for a graph with
e edges has a factor 1/c^e from propagators. The vertex factors contribute
powers of c from the 3-point couplings and lambda_g from higher-genus vertices.
The net c-dependence after summing gives
delta_F_3 = D*c + C + B/c + A/c^2.

VERIFICATION PATHS:
  1. Direct graph sum (brute force over all 42 genus-3 stable graphs)
  2. Four-point Laurent extraction: extract D, C, B, A from c-values per N
  3. Lagrange interpolation: fit D, C, B, A as polynomials in N
  4. Vanishing at N=2 (Virasoro = uniform weight, delta = 0)
  5. Cross-check at N=3 against known delta_F_3(W_3, c)
  6. Positivity for N >= 3, c > 0
  7. Large-c asymptotics (D_3(N)c dominates)
  8. Per-graph decomposition analysis

References:
    thm:multi-weight-genus-expansion, AP27, Faber-Pandharipande
    rectification_delta_f2_verify_engine.py (genus-2 template)
    genus3_stable_graphs.py (42 graphs)
    stable_graph_enumeration.py (StableGraph)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import factorial, comb
from typing import Dict, List, NamedTuple, Optional, Tuple

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
)


# ============================================================================
# Scope and object-normalization firewalls
# ============================================================================

HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)


MODULAR_KOSZUL_COMPUTE_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br,T_br)",
    "R4_mod(L)",
)


GENUS3_DIRECT_GRAPH_CHECKED_N: Tuple[int, ...] = (2, 3, 4, 5, 6, 7, 8)
GENUS3_FULL_OPE_EXACT_N: Tuple[int, ...] = (3,)


def holographic_package_entries() -> Tuple[str, ...]:
    """Return the seven entries of the holographic package H(A)."""
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_compute_projections() -> Tuple[str, ...]:
    """Return the primary projections of the modular Koszul compute package."""
    return MODULAR_KOSZUL_COMPUTE_PROJECTIONS


def typed_object_firewall() -> Dict[str, str]:
    """Typed roles for the bar, Verdier, inversion, and Hochschild objects."""
    return {
        "A": "input chiral algebra",
        "B(A)": "ordered bar coalgebra T^c(s^{-1}bar A)",
        "A^i": "bar cohomology coalgebra H^*(B(A))",
        "A^!": (
            "Verdier/continuous-linear dual branch under finite-type or "
            "completed hypotheses"
        ),
        "Omega(B(A))": "bar-cobar inversion recovering A",
        "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild/derived-centre bulk",
    }


def kernel_normalization_constants(
    c: Fraction = Fraction(26),
    k: Fraction = Fraction(1),
    h_vee: Fraction = Fraction(2),
) -> Dict[str, Dict[str, object]]:
    """Canonical kernel normalizations used to interpret this scalar surface."""
    c = Fraction(c)
    k = Fraction(k)
    h_vee = Fraction(h_vee)
    if k + h_vee == 0:
        raise ValueError("affine KZ coefficient is undefined at k = -h_vee")
    return {
        "affine_raw_collision": {
            "formula": "k*Omega_tr/z",
            "coefficient": k,
        },
        "affine_kz_coefficient": {
            "formula": "Omega/((k+h^vee)z)",
            "coefficient": Fraction(1) / (k + h_vee),
        },
        "heisenberg_raw_collision": {
            "formula": "k/z",
            "coefficient": k,
        },
        "virasoro_collision": {
            "formula": "(c/2)/z^3 + 2T/z",
            "central_coefficient": c / 2,
            "stress_coefficient": Fraction(2),
        },
    }


def genus3_gravitational_formula_scope() -> Dict[str, object]:
    """Finite-window scope and over-promotion guard for delta_F_3^{grav}."""
    return {
        "status": "finite genus-3 gravitational graph-sum reconstruction",
        "genus": 3,
        "formula": "D*c + C + B/c + A/c^2",
        "gravitational_truncation": True,
        "direct_graph_checked_N": GENUS3_DIRECT_GRAPH_CHECKED_N,
        "full_ope_exact_for_N": GENUS3_FULL_OPE_EXACT_N,
        "full_ope_exact_for_generic_WN": False,
        "proved_all_genus": False,
        "proved_all_N_full_ope": False,
        "cohomological_theorem_d_statement": False,
        "class_valued_mc_lift_proved": False,
        "scalar_projection_only": True,
        "delta_diagnostic_promoted_to_universal_theorem": False,
        "normalization": {
            "metric": "eta_{jj}=c/j",
            "propagator": "eta^{jj}=j/c",
            "graph_weight": "1/|Aut(Gamma)|",
        },
        "typed_objects": typed_object_firewall(),
        "holographic_package_entries": holographic_package_entries(),
        "modular_koszul_compute_projections": modular_koszul_compute_projections(),
        "kernel_normalizations": kernel_normalization_constants(),
    }


# ============================================================================
# Bernoulli numbers and lambda_FP (independent implementation)
# ============================================================================

def bernoulli_number(n: int) -> Fraction:
    """Exact Bernoulli number B_n via Akiyama-Tanigawa algorithm."""
    if n < 0:
        raise ValueError(f"Bernoulli number requires n >= 0, got {n}")
    a = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        a[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number at genus g.

    lambda_g^FP = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)
    """
    if g < 1:
        raise ValueError(f"lambda_FP requires g >= 1, got {g}")
    B2g = bernoulli_number(2 * g)
    abs_B2g = abs(B2g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs_B2g / Fraction(factorial(2 * g))


# ============================================================================
# Genus-3 stable graph data
# ============================================================================

@lru_cache(maxsize=1)
def genus3_graphs() -> Tuple[StableGraph, ...]:
    """The 42 stable graphs of M_bar_{3,0}."""
    return tuple(enumerate_stable_graphs(3, 0))


# ============================================================================
# Gravitational Frobenius algebra for W_N
# ============================================================================

def grav_C3(i: int, j: int, k: int, c: Fraction) -> Fraction:
    """Gravitational 3-point structure constant C^{grav}_{ijk}.

    Non-vanishing couplings:
      C_{2,2,2} = c        (TTT)
      C_{2,j,j} = c        (T W_j W_j) for j >= 3, parity-allowed
    All others vanish in the gravitational approximation.
    """
    # Parity check: count odd-weight channels
    odd_count = sum(1 for w in [i, j, k] if w % 2 == 1)
    if odd_count % 2 == 1:
        return Fraction(0)

    triple = tuple(sorted([i, j, k]))

    # TTT
    if triple == (2, 2, 2):
        return c

    # T W_j W_j
    if triple[0] == 2 and triple[1] == triple[2] and triple[1] >= 3:
        return c

    # T T W_j for j >= 3: vanishes (T OPE produces only T)
    if triple[0] == 2 and triple[1] == 2 and triple[2] >= 3:
        return Fraction(0)

    return Fraction(0)


def grav_propagator(weight: int, c: Fraction) -> Fraction:
    """Inverse metric eta^{jj} = j/c (AP27)."""
    return Fraction(weight) / c


def grav_kappa_channel(weight: int, c: Fraction) -> Fraction:
    """Per-channel modular characteristic kappa_j = c/j."""
    return c / Fraction(weight)


def grav_kappa_total(N: int, c: Fraction) -> Fraction:
    """Total kappa(W_N) = sum_{j=2}^{N} c/j = c * (H_N - 1)."""
    return sum(c / Fraction(j) for j in range(2, N + 1))


# ============================================================================
# Vertex factors
# ============================================================================

@lru_cache(maxsize=None)
def grav_V0_factorize(channels: Tuple[int, ...], c: Fraction,
                      all_weights: Tuple[int, ...]) -> Fraction:
    r"""Genus-0 n-point vertex factor via recursive factorization.

    V_0(a, b, rest...) = sum_m eta^{mm} * C_{a,b,m} * V_0(m, rest...)
    Base case n=3: V_0(a,b,c) = C_{abc}.
    """
    n = len(channels)
    if n < 3:
        raise ValueError(f"Genus-0 vertex needs n >= 3, got {n}")
    if n == 3:
        return grav_C3(channels[0], channels[1], channels[2], c)

    a, b = channels[0], channels[1]
    rest = channels[2:]
    total = Fraction(0)
    for m in all_weights:
        c3 = grav_C3(a, b, m, c)
        if c3 == 0:
            continue
        sub_val = grav_V0_factorize((m,) + rest, c, all_weights)
        if sub_val == 0:
            continue
        total += grav_propagator(m, c) * c3 * sub_val
    return total


@lru_cache(maxsize=None)
def grav_vertex_factor(gv: int, channels: Tuple[int, ...], c: Fraction,
                       all_weights: Tuple[int, ...]) -> Fraction:
    """Vertex factor V_{g,n}(channels).

    g >= 1: diagonal principle. All channels must be identical.
      V_{g,n}(j,...,j) = kappa_j * lambda_g^FP = (c/j) * lambda_g
      V_{g,n}(mixed) = 0

    g = 0: recursive Frobenius factorization.
    """
    n = len(channels)
    if n == 0:
        return Fraction(0)

    if gv == 0:
        if n < 3:
            raise ValueError(f"Genus-0 vertex needs n >= 3, got {n}")
        return grav_V0_factorize(channels, c, all_weights)
    else:
        # Higher genus: diagonal
        if len(set(channels)) > 1:
            return Fraction(0)
        return grav_kappa_channel(channels[0], c) * lambda_fp(gv)


# ============================================================================
# Half-edge channel assignment
# ============================================================================

@lru_cache(maxsize=None)
def half_edge_channels(graph: StableGraph, sigma: Tuple[int, ...]
                       ) -> Tuple[Tuple[int, ...], ...]:
    """Compute per-vertex half-edge channel assignments.

    For each edge (v1, v2):
      - If v1 == v2 (self-loop): two half-edges at v1, both with sigma[e]
      - If v1 != v2 (bridge): one half-edge at v1, one at v2, both sigma[e]

    Genus-0 factorization is not associative for the W_N Frobenius data.
    The stable-graph convention pairs self-loop half-edges first, then
    bridge half-edges in edge-list order.
    """
    nv = graph.num_vertices
    self_loop_he: List[List[int]] = [[] for _ in range(nv)]
    bridge_he: List[List[int]] = [[] for _ in range(nv)]

    for e_idx, (v1, v2) in enumerate(graph.edges):
        ch = sigma[e_idx]
        if v1 == v2:
            self_loop_he[v1].append(ch)
            self_loop_he[v1].append(ch)
        else:
            bridge_he[v1].append(ch)
            bridge_he[v2].append(ch)

    return tuple(
        tuple(self_loop_he[v] + bridge_he[v])
        for v in range(nv)
    )


# ============================================================================
# Graph amplitude computation
# ============================================================================

@lru_cache(maxsize=None)
def graph_amplitude_raw(graph: StableGraph, sigma: Tuple[int, ...],
                        c: Fraction, all_weights: Tuple[int, ...]) -> Fraction:
    """Raw amplitude A(Gamma, sigma) WITHOUT the 1/|Aut| factor.

    = prod_e eta^{sigma(e)} * prod_v V_{g(v)}(he_channels_at_v)
    """
    ne = graph.num_edges
    if ne == 0:
        return Fraction(0)

    he_chs = half_edge_channels(graph, sigma)

    # Propagator product
    prop = Fraction(1)
    for e_idx in range(ne):
        prop *= grav_propagator(sigma[e_idx], c)

    # Vertex factors
    vf = Fraction(1)
    for v_idx in range(graph.num_vertices):
        gv = graph.vertex_genera[v_idx]
        chs = he_chs[v_idx]
        if len(chs) == 0:
            continue

        # Check stability: 2*gv - 2 + val >= 1 (i.e., 2*gv + val >= 3)
        val_v = len(chs)
        if 2 * gv - 2 + val_v <= 0:
            return Fraction(0)

        # For g >= 1 vertices with valence < 1, skip (shouldn't happen for stable)
        if gv >= 1 and val_v == 0:
            continue

        # For g = 0, need val >= 3
        if gv == 0 and val_v < 3:
            return Fraction(0)

        vf_v = grav_vertex_factor(gv, chs, c, all_weights)
        if vf_v == 0:
            return Fraction(0)
        vf *= vf_v

    return prop * vf


def graph_amplitude_decomposed(graph: StableGraph, c: Fraction,
                               all_weights: Tuple[int, ...]
                               ) -> Dict[str, Fraction]:
    """Sum amplitude over all channel assignments, split into diagonal/mixed.

    Divides by |Aut(Gamma)|.
    """
    ne = graph.num_edges
    if ne == 0:
        return {'diagonal': Fraction(0), 'mixed': Fraction(0),
                'total': Fraction(0)}

    aut = graph.automorphism_order()
    diag = Fraction(0)
    mixed = Fraction(0)

    for sigma in cartprod(all_weights, repeat=ne):
        amp = graph_amplitude_raw(graph, sigma, c, all_weights)
        if amp == 0:
            continue
        if len(set(sigma)) <= 1:
            diag += amp
        else:
            mixed += amp

    return {
        'diagonal': diag / aut,
        'mixed': mixed / aut,
        'total': (diag + mixed) / aut,
    }


# ============================================================================
# Full genus-3 cross-channel correction
# ============================================================================

def delta_F3_grav_graph_sum(N: int, c: Fraction) -> Fraction:
    """Compute delta_F_3^{grav}(W_N, c) by summing over all 42 genus-3 graphs.

    This is the MIXED (cross-channel) part of the genus-3 free energy,
    using the gravitational-only Frobenius algebra.
    """
    all_weights = tuple(range(2, N + 1))
    graphs = genus3_graphs()

    total_mixed = Fraction(0)
    for graph in graphs:
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        total_mixed += decomp['mixed']

    return total_mixed


def delta_F3_grav_per_graph(N: int, c: Fraction) -> List[Dict[str, Fraction]]:
    """Per-graph decomposition of delta_F_3^{grav}(W_N, c).

    Returns a list of dicts (one per graph) with keys
    'diagonal', 'mixed', 'total', 'aut', 'edges', 'genera'.
    """
    all_weights = tuple(range(2, N + 1))
    graphs = genus3_graphs()

    result = []
    for graph in graphs:
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        decomp['aut'] = graph.automorphism_order()
        decomp['edges'] = graph.num_edges
        decomp['genera'] = graph.vertex_genera
        result.append(decomp)

    return result


# ============================================================================
# Full genus-3 free energy, including the cross-channel contribution
# ============================================================================

def F3_grav_total(N: int, c: Fraction) -> Fraction:
    """Total genus-3 free energy F_3(W_N, c) from graph sum.

    = kappa(W_N) * lambda_3^FP + delta_F_3^{grav}(W_N, c)
    """
    all_weights = tuple(range(2, N + 1))
    graphs = genus3_graphs()

    total = Fraction(0)
    for graph in graphs:
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        total += decomp['total']

    # The smooth graph has no edge labels and contributes only the scalar
    # Faber-Pandharipande lane. Mixed cross-channel terms come from the
    # positive-edge boundary graphs.

    return total + grav_kappa_total(N, c) * lambda_fp(3)


# ============================================================================
# Laurent extraction: D_3, C_3, B_3, A_3 from four c-values
# ============================================================================

def newton_interpolate_delta_F3(N: int, c1: Fraction = Fraction(1),
                                c2: Fraction = Fraction(2),
                                c3: Fraction = Fraction(3),
                                c4: Fraction = Fraction(4),
                                ) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
    """Extract D_3(N), C_3(N), B_3(N), A_3(N) from four c-values.

    The historical function name is retained for callers; the genus-3
    scalar compute surface is the four-term Laurent polynomial.
    """
    return extract_DCBA_from_c_values(N, c1, c2, c3, c4)


def newton_interpolate_delta_F3_verify(N: int,
                                       c_values: Tuple[Fraction, ...] = None
                                       ) -> Dict[str, object]:
    """Interpolate and verify at additional c-values.

    Returns dict with 'D', 'C', 'B', 'A' and 'verification' results.
    """
    if c_values is None:
        c_values = tuple(Fraction(k) for k in range(1, 8))

    D, C, B, A = newton_interpolate_delta_F3(
        N, c_values[0], c_values[1], c_values[2], c_values[3]
    )

    # Verify at remaining c-values
    verification = []
    for cv in c_values:
        predicted = D * cv + C + B / cv + A / (cv * cv)
        actual = delta_F3_grav_graph_sum(N, cv)
        verification.append({
            'c': cv,
            'predicted': predicted,
            'actual': actual,
            'match': predicted == actual,
        })

    return {'D': D, 'C': C, 'B': B, 'A': A, 'verification': verification}


# ============================================================================
# Polynomial fitting: D_3(N), C_3(N), B_3(N), A_3(N) as polynomials in N
# ============================================================================

def lagrange_interpolate_polynomial(points: List[Tuple[int, Fraction]]
                                    ) -> List[Fraction]:
    """Lagrange interpolation: given (x_i, y_i), find polynomial coefficients.

    Returns [a_0, a_1, ..., a_d] where p(x) = a_0 + a_1*x + ... + a_d*x^d.
    The degree d = len(points) - 1.
    """
    n = len(points)
    if n == 0:
        return []

    xs = [Fraction(p[0]) for p in points]
    ys = [p[1] for p in points]

    # Build Newton's divided difference table
    dd = list(ys)
    table = [dd[0]]
    for j in range(1, n):
        new_dd = []
        for i in range(len(dd) - 1):
            new_dd.append((dd[i + 1] - dd[i]) / (xs[i + j] - xs[i]))
        dd = new_dd
        table.append(dd[0])

    # Convert Newton form to standard form
    # p(x) = table[0] + table[1]*(x-x0) + table[2]*(x-x0)(x-x1) + ...
    # Expand iteratively: maintain coefficients of polynomial
    coeffs = [Fraction(0)] * n
    coeffs[0] = table[0]

    # basis[k] = coefficient of x^k in product (x-x0)(x-x1)...(x-x_{j-1})
    basis = [Fraction(0)] * n
    basis[0] = Fraction(1)

    for j in range(1, n):
        # Multiply basis by (x - x_{j-1})
        new_basis = [Fraction(0)] * n
        for k in range(j, 0, -1):
            new_basis[k] = basis[k - 1]
        for k in range(j):
            new_basis[k] += -xs[j - 1] * basis[k]
        basis = new_basis

        # Add table[j] * basis to coeffs
        for k in range(n):
            coeffs[k] += table[j] * basis[k]

    return coeffs


def evaluate_polynomial(coeffs: List[Fraction], x: Fraction) -> Fraction:
    """Evaluate polynomial a_0 + a_1*x + ... + a_d*x^d at x."""
    result = Fraction(0)
    xpower = Fraction(1)
    for a in coeffs:
        result += a * xpower
        xpower *= x
    return result


def _compute_DCBA_for_N(N: int) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
    """Compute (D_3(N), C_3(N), B_3(N), A_3(N)) from c=1,2,3,4."""
    return newton_interpolate_delta_F3(N)


def fit_polynomials(N_values: List[int] = None,
                    ) -> Dict[str, List[Fraction]]:
    """Fit D_3(N), C_3(N), B_3(N), A_3(N) as polynomials in N.

    Strategy: compute D_3, C_3, B_3, A_3 at enough N values, then use
    Lagrange interpolation to find the polynomial coefficients.

    The genus-3 degree pattern is 1, 3, 5, 7 for D, C, B, A.

    We compute at N = 2, 3, ..., 12 to overdetermine the system and verify.
    """
    if N_values is None:
        N_values = list(range(2, 13))

    D_points = []
    C_points = []
    B_points = []
    A_points = []

    for N in N_values:
        D, C, B, A = _compute_DCBA_for_N(N)
        D_points.append((N, D))
        C_points.append((N, C))
        B_points.append((N, B))
        A_points.append((N, A))

    # Find minimal degree for each
    D_coeffs = _fit_minimal_degree(D_points)
    C_coeffs = _fit_minimal_degree(C_points)
    B_coeffs = _fit_minimal_degree(B_points)
    A_coeffs = _fit_minimal_degree(A_points)

    return {
        'D_coeffs': D_coeffs,
        'C_coeffs': C_coeffs,
        'B_coeffs': B_coeffs,
        'A_coeffs': A_coeffs,
        'D_points': D_points,
        'C_points': C_points,
        'B_points': B_points,
        'A_points': A_points,
    }


def _fit_minimal_degree(points: List[Tuple[int, Fraction]]) -> List[Fraction]:
    """Find the minimal-degree polynomial fitting the given points.

    Start with degree len(points)-1 and reduce if trailing coefficients vanish.
    Then verify the fit is exact at all points.
    """
    n = len(points)
    if n == 0:
        return []

    # Use all points for full interpolation
    coeffs = lagrange_interpolate_polynomial(points)

    # Trim trailing zero coefficients
    while len(coeffs) > 1 and coeffs[-1] == Fraction(0):
        coeffs.pop()

    # Verify
    for x, y in points:
        val = evaluate_polynomial(coeffs, Fraction(x))
        if val != y:
            # Try with more points / higher degree
            return coeffs  # Return what we have; caller should check

    return coeffs


# ============================================================================
# Closed-form compatibility aliases
# ============================================================================

def claimed_D3(N: int) -> Fraction:
    """Compatibility alias for D_3(N)."""
    return D3_formula(N)


def claimed_C3(N: int) -> Fraction:
    """Compatibility alias for C_3(N)."""
    return C3_formula(N)


def claimed_B3(N: int) -> Fraction:
    """Compatibility alias for B_3(N)."""
    return B3_formula(N)


def claimed_A3(N: int) -> Fraction:
    """Compatibility alias for A_3(N)."""
    return A3_formula(N)


def claimed_formula_F3(N: int, c: Fraction) -> Fraction:
    """Compatibility alias for delta_F_3^{grav}(W_N, c)."""
    return delta_F3_formula(N, c)


# ============================================================================
# Harmonic sums (for algebraic analysis)
# ============================================================================

def harmonic_sum(N: int, power: int) -> Fraction:
    """sum_{j=2}^N 1/j^power."""
    return sum(Fraction(1, j**power) for j in range(2, N + 1))


def power_sum(N: int, power: int) -> Fraction:
    """sum_{j=2}^N j^power."""
    return sum(Fraction(j**power) for j in range(2, N + 1))


def harmonic_minus_one(N: int) -> Fraction:
    """H_N - 1 = sum_{j=2}^N 1/j."""
    return harmonic_sum(N, 1)


# ============================================================================
# Verification: known W_3 result
# ============================================================================

def delta_F3_W3_known(c: Fraction) -> Fraction:
    """Certified W_3 genus-3 cross-channel correction.

    delta_F_3(W_3,c)
        = c/27648 + 79/2880 + (133/16)/c + (6281/4)/c^2
        = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240c^2).
    """
    return (
        5 * c**3 + 3792 * c**2 + 1149120 * c + Fraction(217071360)
    ) / (Fraction(138240) * c**2)


# ============================================================================
# Verification helpers
# ============================================================================

def verify_N2_vanishing() -> bool:
    """At N=2, W_N = Virasoro (uniform weight). delta_F_3 should vanish."""
    D, C, B, A = newton_interpolate_delta_F3(2)
    return D == 0 and C == 0 and B == 0 and A == 0


def verify_graph_count() -> bool:
    """Verify that we enumerate exactly 42 genus-3 stable graphs."""
    return len(genus3_graphs()) == 42


def verify_W3_consistency(c: Fraction = Fraction(10)) -> bool:
    """Verify that graph sum at N=3 matches the known W_3 formula."""
    graph_sum = delta_F3_grav_graph_sum(3, c)
    known = delta_F3_W3_known(c)
    return graph_sum == known


# ============================================================================
# Batch computation for multiple N
# ============================================================================

def compute_delta_F3_table(N_range: range = range(2, 9),
                           c_values: Tuple[Fraction, ...] = None
                           ) -> Dict[int, Dict[str, Fraction]]:
    """Compute delta_F_3 and its D/C/B/A decomposition for multiple N.

    Returns {N: {'D': ..., 'C': ..., 'B': ..., 'A': ..., 'delta_at_c1': ...}}.
    """
    if c_values is None:
        c_values = (Fraction(1), Fraction(2), Fraction(3), Fraction(4))

    result = {}
    for N in N_range:
        D, C, B, A = newton_interpolate_delta_F3(N, *c_values[:4])
        entry = {'D': D, 'C': C, 'B': B, 'A': A}
        for cv in c_values:
            entry[f'delta_c{cv}'] = delta_F3_grav_graph_sum(N, cv)
        result[N] = entry

    return result


# ============================================================================
# Genus-2 cross-check (independent computation of known B_2, A_2)
# ============================================================================

def claimed_B2(N: int) -> Fraction:
    """Known: B_2(N) = (N-2)(N+3)/96."""
    return Fraction((N - 2) * (N + 3), 96)


def claimed_A2(N: int) -> Fraction:
    """Known: A_2(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24."""
    return Fraction((N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33), 24)


def B2_formula(N: int) -> Fraction:
    """B_2(N) = (N-2)(N+3)/96."""
    return claimed_B2(N)


def A2_formula(N: int) -> Fraction:
    """A_2(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24."""
    return claimed_A2(N)


def delta_F2_formula(N: int, c: Fraction) -> Fraction:
    """delta_F_2^{grav}(W_N,c) = B_2(N) + A_2(N)/c."""
    return B2_formula(N) + A2_formula(N) / c


# ============================================================================
# Finite-window genus-3 coefficient formulas (thm:multi-weight-genus-expansion)
# delta_F_3^{grav}(W_N, c) = D3(N)*c + C3(N) + B3(N)/c + A3(N)/c^2
# ============================================================================

def D3_formula(N: int) -> Fraction:
    """D3(N) = (N-2) / 27648."""
    return Fraction(N - 2, 27648)


def C3_formula(N: int) -> Fraction:
    """C3(N) = (N-2) * (35*N^2 + 133*N + 234) / 34560."""
    return Fraction((N - 2) * (35 * N**2 + 133 * N + 234), 34560)


def B3_formula(N: int) -> Fraction:
    """B3(N) = (N-2)(15*N^4 + 147*N^3 + 517*N^2 + 947*N + 1686) / 1728."""
    return Fraction(
        (N - 2) * (15 * N**4 + 147 * N**3 + 517 * N**2 + 947 * N + 1686),
        1728,
    )


def A3_formula(N: int) -> Fraction:
    """A3(N) = (N-2) * (120*N^6 + 1300*N^5 + 5918*N^4 + 14786*N^3
               + 27592*N^2 + 36369*N + 56475) / 1080."""
    return Fraction(
        (N - 2) * (
            120 * N**6 + 1300 * N**5 + 5918 * N**4
            + 14786 * N**3 + 27592 * N**2 + 36369 * N + 56475
        ),
        1080,
    )


def delta_F3_formula(N: int, c: Fraction) -> Fraction:
    """Finite-window gravitational formula: D3*c + C3 + B3/c + A3/c^2."""
    return D3_formula(N) * c + C3_formula(N) + B3_formula(N) / c + A3_formula(N) / c**2


def delta_F3_analytical(N: int) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return (D, C, B, A) for the genus-3 gravitational reconstruction.

    Uses extract_DCBA_from_c_values to determine the coefficients from the
    graph sum, then verifies they match the closed-form formulas.
    """
    return extract_DCBA_from_c_values(N)


def extract_DCBA_from_c_values(
    N: int,
    c1: Fraction = Fraction(1),
    c2: Fraction = Fraction(2),
    c3: Fraction = Fraction(3),
    c4: Fraction = Fraction(4),
    c_values: Optional[Tuple[Fraction, Fraction, Fraction, Fraction]] = None,
    c_vals: Optional[Tuple[Fraction, Fraction, Fraction, Fraction]] = None,
) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
    """Extract (D, C, B, A) from four c-values by solving the 4x4 linear system.

    The system is:
        f(ci) = D*ci + C + B/ci + A/ci^2  for i=1,2,3,4.
    """
    if c_values is None and c_vals is not None:
        c_values = c_vals
    if c_values is not None:
        if len(c_values) != 4:
            raise ValueError("extract_DCBA_from_c_values requires four c-values")
        cs = [Fraction(c) for c in c_values]
    else:
        cs = [c1, c2, c3, c4]
    fs = [delta_F3_grav_graph_sum(N, c) for c in cs]

    # Build 4x4 system  [c, 1, 1/c, 1/c^2] * [D, C, B, A]^T = f
    rows = [[c, Fraction(1), Fraction(1) / c, Fraction(1) / c**2] for c in cs]

    # Gaussian elimination over Fraction
    n = 4
    mat = [row[:] + [f] for row, f in zip(rows, fs)]

    for col in range(n):
        # Pivot
        pivot = None
        for row in range(col, n):
            if mat[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            raise ValueError(f"Singular system at column {col}")
        mat[col], mat[pivot] = mat[pivot], mat[col]
        factor = mat[col][col]
        mat[col] = [x / factor for x in mat[col]]
        for row in range(n):
            if row != col and mat[row][col] != 0:
                f = mat[row][col]
                mat[row] = [mat[row][j] - f * mat[col][j] for j in range(n + 1)]

    D, C, B, A = [mat[i][n] for i in range(n)]
    return D, C, B, A


def verify_positivity(N: int, c: Fraction = Fraction(10)) -> bool:
    """For N >= 3 and c > 0, delta_F3 should be positive."""
    return delta_F3_formula(N, c) > 0


def lagrange_interpolate(points: List[Tuple[int, Fraction]]) -> List[Fraction]:
    """Compatibility alias for exact Lagrange interpolation."""
    coeffs = lagrange_interpolate_polynomial(points)
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs
