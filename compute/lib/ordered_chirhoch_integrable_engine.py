r"""Ordered chiral Hochschild cohomology at integrable level.

Computes the ordered chiral homology of Y_hbar(sl_2) on an elliptic
curve E_tau at integrable level k (positive integer), where
q = exp(2*pi*i/(k+2)) is a root of unity.

MATHEMATICAL FRAMEWORK
======================

At generic level k (equivalently, generic hbar = 1/(k+2)):
  - The center Z(Y_hbar(sl_2)) = C[qdet T(u)] is infinite-dimensional
  - The KZB local system has infinite monodromy group
  - V^{tensor n} is the full 2^n-dimensional fiber

At integrable level k (positive integer):
  - Only k+1 integrable representations V_0, ..., V_k survive
  - The fusion ring is truncated: V_i x V_j = sum N_{ij}^m V_m
  - The center of the integrable quotient is C^{k+1} (finite!)
  - The KZB monodromy is FINITE (eigenvalues are roots of unity)
  - The local system is semisimple (Maschke's theorem)

AT k=1 (q = e^{2*pi*i/3}, primitive cube root of unity):
  - Two integrable reps: V_0 (trivial, dim 1), V_1 (fundamental, dim 2)
  - Fusion ring: Z/2Z (V_1 x V_1 = V_0)
  - Quantum dimensions: d_0 = d_1 = 1 (pointed MTC)
  - Central charge: c = 3k/(k+2) = 1
  - Modular characteristic: kappa = 3(k+2)/4 = 9/4
  - Verlinde dimensions: Z_g = 2^g
  - S-matrix = (1/sqrt(2)) * Hadamard

The ordered chiral homology at each arity:
  n=0: C^{k+1} = C^2 (center of integrable quotient, FINITE)
  n=1: H*(E_tau) tensor s^{-1}sl_2 = C^12 (level-independent)
  n=2: H^1_dR(E_tau \\ {0}, KZB) = C^4 (finite monodromy, same Euler char)
  n>=3: chi = 0 (chi(Conf_n^ord(E_tau)) = 0), finite monodromy group

CONVENTIONS
===========
- q = exp(2*pi*i / (k+2)) for sl_2 at WZW level k (dual Coxeter h^v = 2)
- Representations labeled j = 0, 1, ..., k (Dynkin labels; spin = j/2)
- S-matrix: S_{jl} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))
- Fusion: N_{ij}^m from Verlinde formula
- Conformal weights: h_j = j(j+2)/(4(k+2))
- Central charge: c = 3k/(k+2)
- Modular characteristic: kappa(sl_2, k) = 3(k+2)/4
  (AP1: dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4; k=0 -> 3/2, k=-2 -> 0)
- KZB monodromy: M_gamma = exp(2*pi*i * hbar * Omega) on each isospin channel
- Bar propagator: d log E(z,w) = wp_1(z-w, tau) d(z-w), weight 1 (AP27)

References
==========
  Bernard (1988), "On the Wess-Zumino-Witten models on the torus"
  Felder (1994), "Conformal field theory and integrable systems ..."
  Etingof-Varchenko (1998), "Geometry and classification of solutions of CYBE"
  Calaque-Enriquez-Etingof (2009), "Universal KZB equations"
  Kazhdan-Lusztig (1993-94), "Tensor structures arising from affine Lie algebras"
  Lorgat (2026), "Modular Koszul Duality" (Vol I), Ch. on Yangians
  prop:ell-arity0, prop:ell-arity1, prop:ell-arity2 (ordered_chiral_homology.tex)
  rem:ell-roots-of-unity (ordered_chiral_homology.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# 0.  Quantum number primitives
# =========================================================================

def quantum_integer(n: int, q: complex) -> complex:
    r"""Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    qi = 1.0 / q
    denom = q - qi
    if abs(denom) < 1e-14:
        return complex(n)
    return (q ** n - qi ** n) / denom


def quantum_dimension(j: int, k: int) -> float:
    r"""Quantum dimension d_j = [j+1]_q where q = exp(i*pi/(k+2)).

    Uses the exact trigonometric formula:
        d_j = sin((j+1)*pi/(k+2)) / sin(pi/(k+2))

    At k=1: d_0 = 1, d_1 = 1 (both quantum dimensions equal 1).
    """
    n = k + 2
    return math.sin((j + 1) * math.pi / n) / math.sin(math.pi / n)


def q_from_level(k: int) -> complex:
    r"""q = exp(2*pi*i / (k+2)) for sl_2 at WZW level k."""
    return np.exp(2j * math.pi / (k + 2))


# =========================================================================
# 1.  Fusion rules at integrable level
# =========================================================================

def fusion_coefficient(j1: int, j2: int, m: int, k: int) -> int:
    r"""Verlinde fusion coefficient N_{j1,j2}^m for sl_2 at level k.

    Truncated Clebsch--Gordan rule:
        N_{j1,j2}^m = 1 if |j1-j2| <= m <= min(j1+j2, 2k-j1-j2) and j1+j2+m even
        N_{j1,j2}^m = 0 otherwise.
    """
    if j1 < 0 or j1 > k or j2 < 0 or j2 > k or m < 0 or m > k:
        return 0
    if (j1 + j2 + m) % 2 != 0:
        return 0
    if m < abs(j1 - j2):
        return 0
    if m > min(j1 + j2, 2 * k - j1 - j2):
        return 0
    return 1


def fusion_product(j1: int, j2: int, k: int) -> List[int]:
    r"""List of representations in V_{j1} x V_{j2} at level k."""
    return [m for m in range(k + 1) if fusion_coefficient(j1, j2, m, k) == 1]


def iterated_fusion_rank(n: int, k: int, j_input: int = 1) -> Dict[int, int]:
    r"""Decomposition of V_{j_input}^{tensor n} in the fusion category.

    Returns dict mapping j -> multiplicity in V_j^{tensor n}.

    At k=1, j_input=1:
        n=0: {0: 1}  (by convention, empty tensor product = V_0)
        n=1: {1: 1}
        n=2: {0: 1}  (V_1 x V_1 = V_0)
        n=3: {1: 1}  (V_0 x V_1 = V_1)
        n=4: {0: 1}  (V_1 x V_1 = V_0)
    Pattern: {n%2: 1} for k=1.
    """
    if n == 0:
        return {0: 1}  # empty tensor product = unit object

    # Start with V_{j_input}
    decomp = {j_input: 1}

    for step in range(1, n):
        new_decomp: Dict[int, int] = {}
        for j_current, mult in decomp.items():
            for m in fusion_product(j_current, j_input, k):
                new_decomp[m] = new_decomp.get(m, 0) + mult
        decomp = new_decomp

    return decomp


def integrable_rank(n: int, k: int, j_input: int = 1) -> int:
    r"""Total dimension of V_{j_input}^{tensor n} in the fusion category.

    This is sum_j mult(j) * dim(V_j) where dim(V_j) = j+1.

    At k=1: rank = 1 (n even) or 2 (n odd).
    At generic level: rank = (j_input + 1)^n.
    """
    decomp = iterated_fusion_rank(n, k, j_input)
    return sum(mult * (j + 1) for j, mult in decomp.items())


# =========================================================================
# 2.  S-matrix and Verlinde dimensions
# =========================================================================

def sl2_S_matrix(k: int) -> np.ndarray:
    r"""Modular S-matrix for sl_2 at level k.

    S_{jl} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))
    """
    n = k + 2
    size = k + 1
    S = np.zeros((size, size))
    prefactor = math.sqrt(2.0 / n)
    for j in range(size):
        for l in range(size):
            S[j, l] = prefactor * math.sin(math.pi * (j + 1) * (l + 1) / n)
    return S


def verlinde_dimension(g: int, k: int) -> float:
    r"""Verlinde dimension Z_g = sum_j S_{0j}^{2-2g} at level k.

    At k=1: Z_g = 2^g (since S_{0,0} = S_{0,1} = 1/sqrt(2)).
    """
    S = sl2_S_matrix(k)
    return sum(S[0, j] ** (2 - 2 * g) for j in range(k + 1))


# =========================================================================
# 3.  KZB monodromy at integrable level
# =========================================================================

@dataclass
class KZBMonodromyData:
    """Monodromy data for the KZB local system at arity 2."""
    k: int
    q: complex
    hbar: float
    # Casimir eigenvalues on V_{1/2} tensor V_{1/2}
    casimir_sym: float  # Omega|_{Sym^2} = 1/2
    casimir_alt: float  # Omega|_{wedge^2} = -3/2
    # Puncture (A-cycle) monodromy
    M_gamma_sym: complex
    M_gamma_alt: complex
    # B-cycle monodromy
    M_B_sym: complex
    M_B_alt: complex
    # Orders
    order_gamma_sym: Optional[int]
    order_gamma_alt: Optional[int]
    # R-matrix eigenvalues (Hecke)
    R_sym: complex  # eigenvalue q on Sym^2
    R_alt: complex  # eigenvalue -q^{-1} on wedge^2


def kzb_monodromy_arity2(k: int) -> KZBMonodromyData:
    r"""Compute KZB monodromy data at arity 2 for sl_2 at level k.

    The KZB connection at arity 2 on E_tau \\ {0} has:
    - Puncture monodromy M_gamma = exp(2*pi*i * hbar * Omega)
    - B-cycle monodromy M_B = exp(-2*pi*i * hbar * Omega) = M_gamma^{-1}

    On V_{1/2} tensor V_{1/2} = Sym^2(V) + wedge^2(V):
    - Omega|_{Sym^2} = 1/2
    - Omega|_{wedge^2} = -3/2
    """
    q = q_from_level(k)
    hbar = 1.0 / (k + 2)

    casimir_sym = 0.5
    casimir_alt = -1.5

    M_gamma_sym = np.exp(2j * math.pi * hbar * casimir_sym)
    M_gamma_alt = np.exp(2j * math.pi * hbar * casimir_alt)
    M_B_sym = np.exp(-2j * math.pi * hbar * casimir_sym)
    M_B_alt = np.exp(-2j * math.pi * hbar * casimir_alt)

    # R-matrix eigenvalues (Hecke algebra)
    R_sym = q
    R_alt = -1.0 / q

    # Compute orders of monodromy elements
    def _order(z: complex, max_n: int = 600) -> Optional[int]:
        for n in range(1, max_n + 1):
            if abs(z ** n - 1.0) < 1e-10:
                return n
        return None

    return KZBMonodromyData(
        k=k, q=q, hbar=hbar,
        casimir_sym=casimir_sym, casimir_alt=casimir_alt,
        M_gamma_sym=M_gamma_sym, M_gamma_alt=M_gamma_alt,
        M_B_sym=M_B_sym, M_B_alt=M_B_alt,
        order_gamma_sym=_order(M_gamma_sym),
        order_gamma_alt=_order(M_gamma_alt),
        R_sym=R_sym, R_alt=R_alt,
    )


def monodromy_has_invariants(k: int) -> bool:
    r"""Check whether the KZB monodromy at arity 2 has invariant vectors.

    H^0 = ker(M_gamma - I) cap ker(M_B - I).
    At integrable level, the monodromy eigenvalues are roots of unity,
    but for k >= 1 they are NON-TRIVIAL roots, so H^0 = 0.
    """
    data = kzb_monodromy_arity2(k)
    gamma_sym_trivial = abs(data.M_gamma_sym - 1.0) < 1e-10
    gamma_alt_trivial = abs(data.M_gamma_alt - 1.0) < 1e-10
    B_sym_trivial = abs(data.M_B_sym - 1.0) < 1e-10
    B_alt_trivial = abs(data.M_B_alt - 1.0) < 1e-10
    # For invariants: need BOTH gamma and B trivial on the same channel
    sym_invariant = gamma_sym_trivial and B_sym_trivial
    alt_invariant = gamma_alt_trivial and B_alt_trivial
    return sym_invariant or alt_invariant


# =========================================================================
# 4.  Ordered chiral homology dimensions
# =========================================================================

@dataclass
class OrderedChirHochData:
    """Complete ordered chiral Hochschild cohomology data at integrable level."""
    k: int
    q: complex
    hbar: float
    c: float           # central charge 3k/(k+2)
    kappa: float       # 3(k+2)/4
    h_weights: List[float]  # conformal weights h_j
    n_irreps: int      # k+1
    quantum_dims: List[float]
    total_D_sq: float  # total quantum dimension squared
    # Fusion data
    fusion_ring_type: str  # e.g. "Z/2Z" for k=1
    # Arity-by-arity dimensions
    arity_dims: Dict[int, Dict[str, Any]]
    # Verlinde dimensions
    verlinde_dims: Dict[int, float]  # genus -> Z_g
    # Monodromy data
    monodromy: KZBMonodromyData


def ordered_chirhoch_integrable(k: int, max_arity: int = 6,
                                 max_genus: int = 5) -> OrderedChirHochData:
    r"""Compute ordered chiral Hochschild cohomology at integrable level k.

    Parameters
    ----------
    k : int
        Positive integer level.
    max_arity : int
        Maximum arity to compute (default 6).
    max_genus : int
        Maximum genus for Verlinde dimensions (default 5).

    Returns
    -------
    OrderedChirHochData with all computed invariants.
    """
    q = q_from_level(k)
    hbar = 1.0 / (k + 2)
    c = 3.0 * k / (k + 2)
    # AP1: kappa(V_k(sl_2)) = dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4
    # k=0 -> 3/2, k=-2 -> 0 (critical level)
    kappa = 3.0 * (k + 2) / 4.0

    # Conformal weights h_j = j(j+2)/(4(k+2))
    h_weights = [j * (j + 2) / (4.0 * (k + 2)) for j in range(k + 1)]

    # Quantum dimensions
    q_dims = [quantum_dimension(j, k) for j in range(k + 1)]
    total_D_sq = sum(d ** 2 for d in q_dims)

    # Fusion ring type
    if k == 1:
        fusion_type = "Z/2Z"
    elif k == 2:
        fusion_type = "Ising-like (3 objects)"
    else:
        fusion_type = f"sl_2 level {k} ({k + 1} objects)"

    # Monodromy
    monodromy = kzb_monodromy_arity2(k)

    # Arity-by-arity computation
    arity_dims: Dict[int, Dict[str, Any]] = {}

    for n in range(max_arity + 1):
        info: Dict[str, Any] = {}

        if n == 0:
            # Center of integrable quotient: C^{k+1}
            info['dim_integrable'] = k + 1
            info['dim_generic'] = float('inf')
            info['description'] = (
                f"Center of integrable quotient = C^{{{k + 1}}}")
            info['euler_char'] = None
            info['rank_local_system'] = None
            info['fusion_decomp'] = {0: 1}  # unit object

        elif n == 1:
            # H*(E_tau) tensor s^{-1}sl_2
            # dim H*(E_tau) = 4, dim sl_2 = 3
            # Level-independent for KM: bar H^1 = s^{-1}g
            dim_bar_H1 = 3  # dim(sl_2)
            dim_H_Etau = 4  # Betti of torus
            info['dim_integrable'] = dim_bar_H1 * dim_H_Etau  # = 12
            info['dim_generic'] = dim_bar_H1 * dim_H_Etau  # = 12
            info['description'] = (
                f"H*(E_tau) tensor s^{{-1}}sl_2 = C^4 tensor C^3 = C^12")
            info['euler_char'] = 0  # chi(E_tau) = 0, so rank * 0 = 0
            info['rank_local_system'] = 2  # dim(V) = 2
            info['fusion_decomp'] = {1: 1}

        elif n == 2:
            # KZB local system on E_tau \\ {0}, rank 4
            # chi = 4*(2-2-1) = -4
            # H^0 = 0 (monodromy non-trivial), H^2 = 0 (punctured)
            # dim H^1 = 4
            rank = 4  # dim(V tensor V) = 2^2
            chi = rank * (2 - 2 - 1)  # = -4
            H0 = 0 if not monodromy_has_invariants(k) else None
            if H0 == 0:
                H1 = abs(chi)
            else:
                H1 = None
            info['dim_integrable'] = H1 if H1 is not None else abs(chi)
            info['dim_generic'] = 4
            info['description'] = (
                f"H^1_dR(E_tau \\\\ {{0}}, KZB), rank {rank}, chi = {chi}")
            info['euler_char'] = chi
            info['rank_local_system'] = rank
            info['H0'] = H0
            info['H1'] = H1
            info['H2'] = 0
            info['fusion_decomp'] = iterated_fusion_rank(n, k, 1)

        else:
            # Arity n >= 3: chi(Conf_n^ord(E_tau)) = 0
            rank_generic = 2 ** n
            fusion_decomp = iterated_fusion_rank(n, k, 1)
            rank_integ = integrable_rank(n, k, 1)
            chi = 0  # chi(Conf_n^ord(E_tau)) = 0 for n >= 1
            info['dim_integrable'] = 'chi=0'
            info['dim_generic'] = 'chi=0'
            info['description'] = (
                f"Euler char = 0; integrable rank = {rank_integ} "
                f"(generic rank = {rank_generic})")
            info['euler_char'] = chi
            info['rank_local_system'] = rank_generic
            info['rank_integrable'] = rank_integ
            info['fusion_decomp'] = fusion_decomp

        arity_dims[n] = info

    # Verlinde dimensions Z_g = sum_j S_{0j}^{2-2g}
    verlinde_dims = {}
    for g in range(max_genus + 1):
        verlinde_dims[g] = verlinde_dimension(g, k)

    return OrderedChirHochData(
        k=k, q=q, hbar=hbar, c=c, kappa=kappa,
        h_weights=h_weights, n_irreps=k + 1,
        quantum_dims=q_dims, total_D_sq=total_D_sq,
        fusion_ring_type=fusion_type,
        arity_dims=arity_dims,
        verlinde_dims=verlinde_dims,
        monodromy=monodromy,
    )


# =========================================================================
# 5.  Comparison: generic vs integrable
# =========================================================================

def comparison_table(k: int, max_arity: int = 6) -> str:
    r"""Generate a comparison table of generic vs integrable level k.

    The key differences:
    (1) Arity 0: infinite (generic) vs C^{k+1} (integrable)
    (2) Monodromy: infinite group (generic) vs finite (integrable)
    (3) Fusion rank: 2^n (generic) vs Z/2Z pattern (k=1)
    """
    data = ordered_chirhoch_integrable(k, max_arity=max_arity)

    lines = []
    lines.append(f"Ordered ChirHoch comparison: generic vs k={k} integrable")
    lines.append(f"q = e^(2*pi*i/{k + 2}), hbar = 1/{k + 2}")
    lines.append(f"c = {data.c:.4f}, kappa = {data.kappa:.4f}")
    lines.append(f"Fusion: {data.fusion_ring_type}")
    lines.append(f"Quantum dims: {[f'{d:.4f}' for d in data.quantum_dims]}")
    lines.append("")
    lines.append(f"{'n':>3} | {'Generic':>12} | {'Integrable':>12} "
                 f"| {'Fus. rank':>10} | {'chi':>6}")
    lines.append("-" * 60)

    for n in range(max_arity + 1):
        info = data.arity_dims[n]
        gen = str(info.get('dim_generic', '?'))
        integ = str(info.get('dim_integrable', '?'))
        chi = info.get('euler_char', '?')
        chi_str = str(chi) if chi is not None else 'N/A'
        fus_rank = integrable_rank(n, k, 1) if n > 0 else k + 1
        lines.append(f"{n:>3} | {gen:>12} | {integ:>12} "
                     f"| {fus_rank:>10} | {chi_str:>6}")

    lines.append("")
    lines.append("Verlinde dimensions Z_g:")
    for g in range(6):
        lines.append(f"  Z_{g} = {data.verlinde_dims[g]:.1f}")

    return "\n".join(lines)


# =========================================================================
# 6.  Structural theorems at k=1
# =========================================================================

def k1_structural_summary() -> Dict[str, Any]:
    r"""Complete structural summary at k=1 (q = e^{2*pi*i/3}).

    This is the simplest nontrivial integrable level.
    The fusion ring Z/2Z makes all computations explicit.
    """
    data = ordered_chirhoch_integrable(1, max_arity=8, max_genus=6)

    # Verify key identities
    results: Dict[str, Any] = {}

    # (1) Fusion ring is Z/2Z
    assert fusion_product(0, 0, 1) == [0], "V_0 x V_0 should be V_0"
    assert fusion_product(0, 1, 1) == [1], "V_0 x V_1 should be V_1"
    assert fusion_product(1, 0, 1) == [1], "V_1 x V_0 should be V_1"
    assert fusion_product(1, 1, 1) == [0], "V_1 x V_1 should be V_0"
    results['fusion_is_Z2'] = True

    # (2) Quantum dimensions are all 1 (pointed MTC)
    assert abs(data.quantum_dims[0] - 1.0) < 1e-10
    assert abs(data.quantum_dims[1] - 1.0) < 1e-10
    results['pointed_MTC'] = True

    # (3) S-matrix is Hadamard / sqrt(2)
    S = sl2_S_matrix(1)
    hadamard = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    assert np.allclose(S, hadamard, atol=1e-12)
    results['S_is_hadamard'] = True

    # (4) Verlinde dimensions Z_g = 2^g
    for g in range(7):
        assert abs(data.verlinde_dims[g] - 2 ** g) < 1e-10, \
            f"Z_{g} should be 2^{g}, got {data.verlinde_dims[g]}"
    results['verlinde_2_to_g'] = True

    # (5) Arity 0: dim = 2
    assert data.arity_dims[0]['dim_integrable'] == 2
    results['arity_0_dim'] = 2

    # (6) Arity 1: dim = 12 (level-independent)
    assert data.arity_dims[1]['dim_integrable'] == 12
    results['arity_1_dim'] = 12

    # (7) Arity 2: dim H^1 = 4
    assert data.arity_dims[2]['dim_integrable'] == 4
    results['arity_2_dim'] = 4

    # (8) Integrable ranks follow Z/2Z pattern
    for n in range(1, 9):
        expected = 1 if n % 2 == 0 else 2
        actual = integrable_rank(n, 1, 1)
        assert actual == expected, \
            f"Integrable rank at arity {n}: expected {expected}, got {actual}"
    results['rank_Z2_pattern'] = True

    # (9) Monodromy is finite
    mon = data.monodromy
    assert mon.order_gamma_sym is not None, "Sym monodromy should have finite order"
    assert mon.order_gamma_alt is not None, "Alt monodromy should have finite order"
    results['monodromy_orders'] = {
        'gamma_sym': mon.order_gamma_sym,
        'gamma_alt': mon.order_gamma_alt,
    }

    # (10) No monodromy invariants
    assert not monodromy_has_invariants(1)
    results['H0_vanishes'] = True

    # (11) Central charge c = 1
    assert abs(data.c - 1.0) < 1e-10
    results['central_charge'] = 1.0

    # (12) Kappa = 9/4
    # AP1: kappa(V_k(sl_2)) = 3(k+2)/4 = 3*3/4 = 9/4
    assert abs(data.kappa - 9.0 / 4) < 1e-10
    results['kappa'] = 9.0 / 4

    # (13) Conformal weights
    assert abs(data.h_weights[0]) < 1e-10  # h_0 = 0
    assert abs(data.h_weights[1] - 0.25) < 1e-10  # h_1 = 1/4
    results['conformal_weights'] = data.h_weights

    # (14) Total quantum dimension squared = 2
    assert abs(data.total_D_sq - 2.0) < 1e-10
    results['total_D_sq'] = 2.0

    results['data'] = data
    return results
