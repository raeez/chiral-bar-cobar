"""
Explicit E1 lattice bar complex computations for quantum lattice algebras.

For quantum lattice algebras V_Lambda^{N,q} with non-symmetric cocycle
deformations, computes every facet end-to-end:

1. Symmetric cocycle eps_0 (FLM upper-triangular convention)
2. Deformed cocycle eps_{N,q} with explicit numerical values
3. Cocycle commutator / braiding matrix
4. E1 bar differential matrices in each lattice sector
5. Ordering cycles (kernel of bar differential)
6. Bar cohomology dimensions (E1 vs E-infinity comparison)
7. Koszul dual identification
8. N-torsion verification

Supports A_2, A_3, D_4 root lattices with arbitrary (N, q).
"""

import numpy as np
from typing import Dict, List, Tuple, Optional


# =========================================================================
# Root lattice data
# =========================================================================

def cartan_matrix(lie_type: str) -> np.ndarray:
    """Cartan matrix for a simply-laced Lie algebra."""
    if lie_type == "A1":
        return np.array([[2]])
    elif lie_type == "A2":
        return np.array([[2, -1], [-1, 2]])
    elif lie_type == "A3":
        return np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    elif lie_type == "D4":
        # Bourbaki numbering: node 2 is central, connected to 1, 3, 4
        return np.array([
            [2, -1, 0, 0],
            [-1, 2, -1, -1],
            [0, -1, 2, 0],
            [0, -1, 0, 2],
        ])
    else:
        raise ValueError(f"Unsupported Lie type: {lie_type}")


def rank(lie_type: str) -> int:
    return cartan_matrix(lie_type).shape[0]


def num_positive_roots(lie_type: str) -> int:
    """Number of positive roots."""
    if lie_type == "A1":
        return 1
    elif lie_type == "A2":
        return 3
    elif lie_type == "A3":
        return 6
    elif lie_type == "D4":
        return 12
    else:
        raise ValueError(f"Unsupported: {lie_type}")


def adjacent_pairs(lie_type: str) -> List[Tuple[int, int]]:
    """Ordered pairs (i,j) with i != j and <alpha_i, alpha_j> = -1.

    These are the pairs contributing bar degree 2 ordering cycles.
    Returns 0-indexed pairs.
    """
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    pairs = []
    for i in range(r):
        for j in range(r):
            if i != j and A[i, j] == -1:
                pairs.append((i, j))
    return pairs


def simple_root_sectors(lie_type: str) -> List[Tuple[int, int]]:
    """Unordered pairs {i,j} (i < j) with <alpha_i, alpha_j> = -1.

    Each pair gives a sector gamma = alpha_i + alpha_j with an ordering cycle.
    Returns 0-indexed pairs.
    """
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    pairs = []
    for i in range(r):
        for j in range(i + 1, r):
            if A[i, j] == -1:
                pairs.append((i, j))
    return pairs


# =========================================================================
# Cocycle computations
# =========================================================================

def symmetric_cocycle(lie_type: str) -> np.ndarray:
    """Standard symmetric cocycle eps_0 on simple root pairs.

    FLM upper-triangular convention:
      eps_0(alpha_i, alpha_j) = (-1)^{<alpha_i, alpha_j>}  for i < j (adjacent)
      eps_0(alpha_i, alpha_j) = 1                           for i >= j or non-adjacent

    This satisfies Borcherds symmetry:
      eps_0(alpha_i, alpha_j) / eps_0(alpha_j, alpha_i) = (-1)^{<alpha_i, alpha_j>}

    Returns integer matrix of values in {-1, +1}.
    """
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    eps = np.ones((r, r), dtype=int)
    for i in range(r):
        for j in range(i + 1, r):
            if A[i, j] == -1:  # adjacent
                eps[i, j] = -1  # (-1)^{-1} = -1
    return eps


def verify_borcherds_symmetry(eps: np.ndarray, A: np.ndarray) -> bool:
    """Check eps(i,j)/eps(j,i) = (-1)^{<alpha_i, alpha_j>} for all i != j."""
    r = eps.shape[0]
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            ratio = eps[i, j] / eps[j, i]
            expected = (-1) ** int(A[i, j])
            if not np.isclose(ratio, expected):
                return False
    return True


def antisymmetric_form(lie_type: str, N: int, q_values: Optional[Dict] = None) -> np.ndarray:
    """Build antisymmetric bilinear form q: Lambda x Lambda -> Z/NZ.

    Args:
        lie_type: Root system type
        N: Deformation order
        q_values: Dict mapping (i,j) with i < j to q(alpha_i, alpha_j).
                  If None, uses standard form q(alpha_i, alpha_{i+1}) = 1.

    Returns:
        Integer matrix q[i,j] with values in {0, 1, ..., N-1}.
    """
    r = rank(lie_type)
    q = np.zeros((r, r), dtype=int)

    if q_values is None:
        # Standard edge form: q(alpha_i, alpha_{i+1}) = 1 for adjacent pairs
        A = cartan_matrix(lie_type)
        for i in range(r):
            for j in range(i + 1, r):
                if A[i, j] == -1:
                    q[i, j] = 1
                    q[j, i] = (N - 1) % N
    else:
        for (i, j), val in q_values.items():
            if i < j:
                q[i, j] = val % N
                q[j, i] = (N - val) % N
            else:
                q[j, i] = val % N
                q[i, j] = (N - val) % N

    return q


def deformed_cocycle(lie_type: str, N: int, q: np.ndarray) -> np.ndarray:
    """Deformed cocycle eps_{N,q}(alpha_i, alpha_j) = eps_0(i,j) * zeta_N^{q(i,j)}.

    Returns complex matrix of cocycle values on simple root pairs.
    """
    eps0 = symmetric_cocycle(lie_type)
    zeta = np.exp(2j * np.pi / N)
    r = rank(lie_type)
    eps = np.zeros((r, r), dtype=complex)
    for i in range(r):
        for j in range(r):
            eps[i, j] = eps0[i, j] * zeta ** int(q[i, j])
    return eps


def cocycle_commutator(lie_type: str, N: int, q: np.ndarray) -> np.ndarray:
    """Cocycle commutator c_{eps_{N,q}}(alpha_i, alpha_j).

    c(i,j) = eps_{N,q}(i,j) / eps_{N,q}(j,i) = (-1)^{<i,j>} * zeta_N^{2q(i,j)}.

    Returns complex matrix.
    """
    A = cartan_matrix(lie_type)
    zeta = np.exp(2j * np.pi / N)
    r = A.shape[0]
    c = np.zeros((r, r), dtype=complex)
    for i in range(r):
        for j in range(r):
            c[i, j] = ((-1.0) ** int(A[i, j])) * (zeta ** (2 * int(q[i, j])))
    return c


def verify_commutator_from_cocycle(lie_type: str, N: int, q: np.ndarray) -> bool:
    """Verify c(i,j) = eps(i,j)/eps(j,i) matches the formula."""
    eps = deformed_cocycle(lie_type, N, q)
    c_formula = cocycle_commutator(lie_type, N, q)
    r = rank(lie_type)
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            c_direct = eps[i, j] / eps[j, i]
            if not np.isclose(c_direct, c_formula[i, j]):
                return False
    return True


def is_symmetric_cocycle(eps: np.ndarray, A: np.ndarray) -> bool:
    """Check if deformed cocycle satisfies Borcherds symmetry.

    Borcherds: eps(i,j) = (-1)^{<i,j>} * eps(j,i).
    Equivalently: c(i,j) = (-1)^{<i,j>} for all i,j.
    """
    r = A.shape[0]
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            ratio = eps[i, j] / eps[j, i]
            expected = (-1.0) ** int(A[i, j])
            if not np.isclose(ratio, expected):
                return False
    return True


# =========================================================================
# E1 bar complex computation
# =========================================================================

def e1_bar_differential_sector(
    lie_type: str, N: int, q: np.ndarray, i: int, j: int
) -> Dict:
    """E1 bar differential in sector gamma = alpha_i + alpha_j.

    For <alpha_i, alpha_j> = -1, the E1 bar complex in degrees 1--2 is:
        0 -> C^2 --(d)--> C^1 -> 0
    where d = [eps_{N,q}(alpha_i, alpha_j),  eps_{N,q}(alpha_j, alpha_i)].

    Generators at bar degree 2: v_+ = [e^{alpha_i} | e^{alpha_j}],
                                 v_- = [e^{alpha_j} | e^{alpha_i}].
    Generator at bar degree 1: [e^{alpha_i + alpha_j}].

    Returns dict with:
        - 'differential': the row vector d as array of shape (2,)
        - 'rank': rank of d (always 1)
        - 'kernel_dim': dim ker d (always 1)
        - 'ordering_cycle': the kernel generator as array of shape (2,)
        - 'cycle_ratio': ratio of v_- coefficient to v_+ coefficient
        - 'h1': dim H^1 in this sector
        - 'h2': dim H^2 in this sector
    """
    A = cartan_matrix(lie_type)
    assert A[i, j] == -1, f"Roots {i},{j} not adjacent: <alpha_{i},alpha_{j}> = {A[i,j]}"

    eps = deformed_cocycle(lie_type, N, q)

    # Bar differential d: C^2 -> C^1
    # d([e^{alpha_i}|e^{alpha_j}]) = eps_{N,q}(alpha_i, alpha_j) * [e^gamma]
    # d([e^{alpha_j}|e^{alpha_i}]) = eps_{N,q}(alpha_j, alpha_i) * [e^gamma]
    d_vec = np.array([eps[i, j], eps[j, i]])

    # Both entries are nonzero (product of nonzero cocycle value and root of unity)
    assert not np.isclose(d_vec[0], 0) and not np.isclose(d_vec[1], 0)

    # Kernel: a*eps(i,j) + b*eps(j,i) = 0  =>  b = -eps(i,j)/eps(j,i) * a
    # Ordering cycle: xi = v_+ + lambda * v_-  where lambda = -eps(i,j)/eps(j,i)
    lam = -eps[i, j] / eps[j, i]
    cycle = np.array([1.0 + 0j, lam])

    # Verify it's in the kernel
    assert np.isclose(np.dot(d_vec, cycle), 0), "Ordering cycle not in kernel!"

    # H^1 = 0 (d is surjective: rank 1 = dim target)
    # H^2 = C (ker d / 0 = ker d = C * xi)
    return {
        "sector": (i, j),
        "gamma": f"alpha_{i+1} + alpha_{j+1}",
        "differential": d_vec,
        "rank": 1,
        "kernel_dim": 1,
        "ordering_cycle": cycle,
        "cycle_ratio": lam,
        "h1": 0,
        "h2": 1,
    }


def e1_bar_differential_sector_einf(
    lie_type: str, i: int, j: int
) -> Dict:
    """E-infinity bar differential in sector gamma = alpha_i + alpha_j.

    For comparison: the E-infinity bar complex has the symmetric quotient,
    so bar degree 2 has dimension 1 (not 2), and d is an isomorphism.

    Returns dict with h1, h2 for comparison.
    """
    A = cartan_matrix(lie_type)
    assert A[i, j] == -1
    eps0 = symmetric_cocycle(lie_type)

    # In the E-infinity complex, v_+ and v_- are identified (up to sign)
    # d: C^1 -> C^1 is multiplication by eps_0(alpha_i, alpha_j) (nonzero)
    # So d is an isomorphism: H^1 = H^2 = 0.
    return {
        "sector": (i, j),
        "gamma": f"alpha_{i+1} + alpha_{j+1}",
        "h1": 0,
        "h2": 0,
        "differential_rank": 1,
        "dim_bar2": 1,  # vs 2 for E1
    }


def n_torsion_check(lie_type: str, N: int, q: np.ndarray) -> Dict:
    """Verify N-torsion of braiding: c(i,j)^N = (-1)^{N<i,j>}.

    For each pair (i,j), check that the N-fold braiding iteration is trivial
    (up to the expected sign).
    """
    A = cartan_matrix(lie_type)
    c = cocycle_commutator(lie_type, N, q)
    r = A.shape[0]
    results = {}
    all_pass = True
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            c_N = c[i, j] ** N
            expected = (-1.0) ** (N * int(A[i, j]))
            ok = np.isclose(c_N, expected)
            if not ok:
                all_pass = False
            results[(i, j)] = {
                "c_ij": c[i, j],
                "c_ij_N": c_N,
                "expected": expected,
                "pass": ok,
            }
    return {"all_pass": all_pass, "details": results}


# =========================================================================
# Koszul dual computation
# =========================================================================

def koszul_dual_data(lie_type: str, N: int, q: np.ndarray) -> Dict:
    """Compute Koszul dual braiding for V_Lambda^{N,-q}.

    The Koszul dual carries the conjugate deformation -q.
    Returns comparison data between (N,q) and (N,-q).
    """
    q_dual = (N - q) % N  # -q mod N
    # Ensure diagonal is 0
    for i in range(q_dual.shape[0]):
        q_dual[i, i] = 0

    c_original = cocycle_commutator(lie_type, N, q)
    c_dual = cocycle_commutator(lie_type, N, q_dual)

    # Key identity: c_{N,-q}(i,j) = c_{N,q}(j,i) (transpose)
    r = rank(lie_type)
    transpose_identity = True
    for i in range(r):
        for j in range(r):
            if not np.isclose(c_dual[i, j], c_original[j, i]):
                transpose_identity = False

    # Also: c_{N,-q}(i,j) * c_{N,q}(i,j) = (-1)^{2<i,j>} = 1 (for even lattice)
    A = cartan_matrix(lie_type)
    product_identity = True
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            product = c_original[i, j] * c_dual[i, j]
            expected = (-1.0) ** (2 * int(A[i, j]))  # = 1 for even lattice
            if not np.isclose(product, expected):
                product_identity = False

    return {
        "q_original": q,
        "q_dual": q_dual,
        "braiding_original": c_original,
        "braiding_dual": c_dual,
        "transpose_identity": transpose_identity,
        "product_identity": product_identity,
    }


# =========================================================================
# Full end-to-end computation
# =========================================================================

def full_e1_computation(
    lie_type: str, N: int, q_values: Optional[Dict] = None, verbose: bool = False
) -> Dict:
    """Full end-to-end E1 bar complex computation for a quantum lattice algebra.

    Computes every facet:
    1. Lattice data (Cartan matrix, root count)
    2. Cocycle data (eps_0, eps_{N,q}, numerical values)
    3. Borcherds symmetry check (eps_0 symmetric, eps_{N,q} NOT)
    4. Commutator/braiding matrix with numerical values
    5. E1 bar differential in each simple-root sector
    6. Ordering cycles with explicit coefficients
    7. Bar cohomology dimensions (E1 vs E-infinity)
    8. Koszul dual identification and dual braiding
    9. N-torsion verification
    """
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    q = antisymmetric_form(lie_type, N, q_values)
    eps0 = symmetric_cocycle(lie_type)
    eps_deformed = deformed_cocycle(lie_type, N, q)
    zeta = np.exp(2j * np.pi / N)

    # 1. Lattice data
    lattice_data = {
        "lie_type": lie_type,
        "rank": r,
        "cartan_matrix": A,
        "num_positive_roots": num_positive_roots(lie_type),
    }

    # 2. Cocycle data
    cocycle_data = {
        "N": N,
        "zeta": zeta,
        "q_form": q,
        "eps0": eps0,
        "eps_deformed": eps_deformed,
    }

    # 3. Borcherds symmetry
    eps0_symmetric = verify_borcherds_symmetry(eps0, A)
    eps_deformed_symmetric = is_symmetric_cocycle(eps_deformed, A)
    symmetry_data = {
        "eps0_is_borcherds_symmetric": eps0_symmetric,
        "eps_deformed_is_borcherds_symmetric": eps_deformed_symmetric,
        "strictly_e1": not eps_deformed_symmetric,
    }

    # 4. Braiding matrix
    c = cocycle_commutator(lie_type, N, q)
    commutator_verified = verify_commutator_from_cocycle(lie_type, N, q)
    braiding_data = {
        "commutator_matrix": c,
        "commutator_formula_verified": commutator_verified,
        "diagonal_trivial": all(np.isclose(c[i, i], 1.0) for i in range(r)),
    }

    # 5-7. Sector computations
    sectors = simple_root_sectors(lie_type)
    sector_results = {}
    total_ordering_cycles = 0
    for (i, j) in sectors:
        e1_result = e1_bar_differential_sector(lie_type, N, q, i, j)
        einf_result = e1_bar_differential_sector_einf(lie_type, i, j)
        sector_results[(i, j)] = {
            "e1": e1_result,
            "einf": einf_result,
            "new_cohomology": e1_result["h2"] - einf_result["h2"],
        }
        total_ordering_cycles += e1_result["h2"]

    # 8. Koszul dual
    kd = koszul_dual_data(lie_type, N, q)

    # 9. N-torsion
    torsion = n_torsion_check(lie_type, N, q)

    result = {
        "lattice": lattice_data,
        "cocycle": cocycle_data,
        "symmetry": symmetry_data,
        "braiding": braiding_data,
        "sectors": sector_results,
        "total_ordering_cycles": total_ordering_cycles,
        "koszul_dual": kd,
        "n_torsion": torsion,
    }

    if verbose:
        _print_computation(result)

    return result


def _print_computation(result: Dict):
    """Pretty-print a full computation result."""
    lt = result["lattice"]["lie_type"]
    N = result["cocycle"]["N"]
    q = result["cocycle"]["q_form"]
    r = result["lattice"]["rank"]

    print(f"\n{'='*70}")
    print(f"QUANTUM LATTICE ALGEBRA: V_{{Lambda_{lt}}}^{{{N},q}}")
    print(f"{'='*70}")

    print(f"\n--- Lattice Data ---")
    print(f"Type: {lt}, Rank: {r}")
    print(f"Cartan matrix:\n{result['lattice']['cartan_matrix']}")
    print(f"Positive roots: {result['lattice']['num_positive_roots']}")

    print(f"\n--- Cocycle Data ---")
    print(f"N = {N}, zeta = e^{{2pi i/{N}}}")
    print(f"Deformation form q:")
    print(q)
    print(f"\nSymmetric cocycle eps_0:")
    print(result["cocycle"]["eps0"])
    print(f"\nDeformed cocycle eps_{{N,q}} (complex values):")
    eps = result["cocycle"]["eps_deformed"]
    for i in range(r):
        for j in range(r):
            if i != j:
                v = eps[i, j]
                print(f"  eps(alpha_{i+1}, alpha_{j+1}) = {v:.6f}")

    print(f"\n--- Borcherds Symmetry ---")
    print(f"eps_0 is Borcherds-symmetric: {result['symmetry']['eps0_is_borcherds_symmetric']}")
    print(f"eps_{{N,q}} is Borcherds-symmetric: {result['symmetry']['eps_deformed_is_borcherds_symmetric']}")
    print(f"Strictly E1 (not E-infinity): {result['symmetry']['strictly_e1']}")

    print(f"\n--- Braiding Matrix ---")
    c = result["braiding"]["commutator_matrix"]
    for i in range(r):
        for j in range(r):
            if i != j:
                v = c[i, j]
                print(f"  c(alpha_{i+1}, alpha_{j+1}) = {v:.6f}")
    print(f"Diagonal trivial: {result['braiding']['diagonal_trivial']}")
    print(f"Formula verified: {result['braiding']['commutator_formula_verified']}")

    print(f"\n--- E1 Bar Complex (sector-by-sector) ---")
    for (i, j), data in result["sectors"].items():
        e1 = data["e1"]
        einf = data["einf"]
        print(f"\n  Sector gamma = alpha_{i+1} + alpha_{j+1}:")
        d = e1["differential"]
        print(f"    d = ({d[0]:.6f}, {d[1]:.6f})")
        xi = e1["ordering_cycle"]
        print(f"    Ordering cycle: xi = v_+ + ({xi[1]:.6f}) * v_-")
        print(f"    Cycle ratio (v_- / v_+): {e1['cycle_ratio']:.6f}")
        print(f"    E1:   H^1 = {e1['h1']}, H^2 = {e1['h2']}")
        print(f"    Einf: H^1 = {einf['h1']}, H^2 = {einf['h2']}")
        print(f"    New cohomology from E1: {data['new_cohomology']} classes")

    print(f"\n  Total ordering cycles: {result['total_ordering_cycles']}")

    print(f"\n--- Koszul Dual ---")
    kd = result["koszul_dual"]
    print(f"  Original q:\n{kd['q_original']}")
    print(f"  Dual q (-q mod {N}):\n{kd['q_dual']}")
    print(f"  c_{{-q}}(i,j) = c_q(j,i): {kd['transpose_identity']}")
    print(f"  c_q * c_{{-q}} = 1: {kd['product_identity']}")

    print(f"\n--- N-torsion ---")
    print(f"  c(i,j)^{N} = (-1)^{{{N}<i,j>}} for all pairs: {result['n_torsion']['all_pass']}")


# =========================================================================
# Formatted output for LaTeX verification
# =========================================================================

def format_complex_exact(z: complex, N: int) -> str:
    """Format a complex number as an exact expression in terms of zeta_N.

    Attempts to identify z as eps_0 * zeta_N^k for some sign eps_0 and power k.
    """
    zeta = np.exp(2j * np.pi / N)
    for sign_val, sign_str in [(1, ""), (-1, "-")]:
        for k in range(N):
            if np.isclose(z, sign_val * zeta ** k):
                if k == 0:
                    return f"{sign_str}1"
                elif k == 1:
                    return f"{sign_str}\\zeta_{{{N}}}"
                else:
                    return f"{sign_str}\\zeta_{{{N}}}^{{{k}}}"
    # Fallback: numerical
    return f"{z:.6f}"


def latex_table_cocycle(lie_type: str, N: int, q: np.ndarray) -> str:
    """Generate LaTeX table of cocycle values."""
    eps = deformed_cocycle(lie_type, N, q)
    r = rank(lie_type)
    A = cartan_matrix(lie_type)
    lines = []
    lines.append(r"\begin{center}")
    lines.append(r"\renewcommand{\arraystretch}{1.3}")
    lines.append(r"\begin{tabular}{c c c c}")
    lines.append(r"$(i,j)$ & $\varepsilon_0(\alpha_i,\alpha_j)$ "
                 r"& $\zeta^{q(\alpha_i,\alpha_j)}$ "
                 r"& $\varepsilon_{N,q}(\alpha_i,\alpha_j)$ \\")
    lines.append(r"\hline")
    eps0 = symmetric_cocycle(lie_type)
    zeta = np.exp(2j * np.pi / N)
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            if A[i, j] != -1 and A[i, j] != 0:
                continue
            e0 = eps0[i, j]
            qij = int(q[i, j])
            phase = zeta ** qij
            total = eps[i, j]
            e0_str = f"{e0:+d}"
            phase_str = format_complex_exact(phase, N)
            total_str = format_complex_exact(total, N)
            lines.append(f"$({i+1},{j+1})$ & ${e0_str}$ & ${phase_str}$ & ${total_str}$ \\\\")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{center}")
    return "\n".join(lines)


def latex_table_braiding(lie_type: str, N: int, q: np.ndarray) -> str:
    """Generate LaTeX table of braiding values."""
    c = cocycle_commutator(lie_type, N, q)
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    lines = []
    lines.append(r"\begin{center}")
    lines.append(r"\renewcommand{\arraystretch}{1.3}")
    lines.append(r"\begin{tabular}{c c c}")
    lines.append(r"$(i,j)$ & $c(\alpha_i,\alpha_j)$ & Type \\")
    lines.append(r"\hline")
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            c_str = format_complex_exact(c[i, j], N)
            if A[i, j] == -1:
                tp = "adjacent"
            elif A[i, j] == 0:
                tp = "non-adj."
            else:
                tp = "self"
            lines.append(f"$({i+1},{j+1})$ & ${c_str}$ & {tp} \\\\")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{center}")
    return "\n".join(lines)


# =========================================================================
# Entry points for specific examples
# =========================================================================

def example_a2_n3():
    """A_2 with N=3, q(alpha_1,alpha_2) = 1.

    The critical case: N = h (Coxeter number of A_2).
    """
    return full_e1_computation("A2", 3, verbose=True)


def example_a2_n5_q2():
    """A_2 with N=5, q(alpha_1,alpha_2) = 2.

    Non-generator deformation parameter on the same lattice.
    """
    return full_e1_computation("A2", 5, q_values={(0, 1): 2}, verbose=True)


def example_d4_n3():
    """D_4 with N=3, standard edge form.

    Higher rank with triality. q(i,j)=1 for all adjacent pairs.
    """
    return full_e1_computation("D4", 3, verbose=True)


if __name__ == "__main__":
    print("Example 1: A_2, N=3, q=1")
    example_a2_n3()
    print("\n\nExample 2: A_2, N=5, q=2")
    example_a2_n5_q2()
    print("\n\nExample 3: D_4, N=3, standard edge form")
    example_d4_n3()
