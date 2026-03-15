"""
Quantum lattice screening algebra computations.

Computes braiding matrices, screening operator relations, and
comparison data for the quantum group identification programme
(conj:lattice:quantum-group-connection).

Focused on simply-laced root lattices of rank >= 2 with
cocycle deformation (N, q).
"""

import numpy as np
from itertools import product as iter_product


def cartan_matrix(lie_type: str) -> np.ndarray:
    """Return the Cartan matrix for a simply-laced Lie algebra."""
    if lie_type == "A2":
        return np.array([[2, -1], [-1, 2]])
    elif lie_type == "A3":
        return np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    elif lie_type == "D4":
        return np.array([
            [2, -1, 0, 0],
            [-1, 2, -1, -1],
            [0, -1, 2, 0],
            [0, -1, 0, 2],
        ])
    elif lie_type == "A1":
        return np.array([[2]])
    else:
        raise ValueError(f"Unsupported Lie type: {lie_type}")


def inner_product_matrix(lie_type: str) -> np.ndarray:
    """Return the inner product matrix <alpha_i, alpha_j> for simple roots.

    For simply-laced, this equals the Cartan matrix.
    """
    return cartan_matrix(lie_type)


def standard_antisymmetric_form(r: int, N: int) -> np.ndarray:
    """Return the standard antisymmetric form q on a rank-r lattice.

    For rank 2: q(alpha_1, alpha_2) = 1 = -q(alpha_2, alpha_1).
    For rank >= 3: q(alpha_i, alpha_{i+1}) = 1, others = 0.
    """
    q = np.zeros((r, r), dtype=int)
    for i in range(r - 1):
        q[i, i + 1] = 1
        q[i + 1, i] = N - 1  # = -1 mod N
    return q % N


def cocycle_commutator(
    ip_matrix: np.ndarray, q_form: np.ndarray, N: int
) -> np.ndarray:
    """Compute the cocycle commutator matrix c_{eps_{N,q}}(alpha_i, alpha_j).

    Returns a complex matrix where entry (i,j) is:
      (-1)^{<alpha_i, alpha_j>} * zeta_N^{2*q(alpha_i, alpha_j)}

    This is the braiding phase from Proposition prop:lattice:deformation-properties(ii).
    """
    zeta = np.exp(2j * np.pi / N)
    r = ip_matrix.shape[0]
    c = np.zeros((r, r), dtype=complex)
    for i in range(r):
        for j in range(r):
            sign = (-1.0) ** int(ip_matrix[i, j])
            phase = zeta ** (2 * int(q_form[i, j]))
            c[i, j] = sign * phase
    return c


def screening_braiding_table(lie_type: str, N: int, q_form=None):
    """Compute the screening current braiding table.

    Returns:
        dict with keys:
        - 'braiding': complex matrix of c_{eps_{N,q}}(alpha_i, alpha_j)
        - 'diagonal': diagonal entries (should all be 1)
        - 'off_diagonal_adjacent': list of off-diagonal entries for adjacent pairs
        - 'nilpotency_order': 2 for all generators (from <alpha_i, alpha_i> = 2)
    """
    ip = inner_product_matrix(lie_type)
    r = ip.shape[0]

    if q_form is None:
        q_form = standard_antisymmetric_form(r, N)

    c = cocycle_commutator(ip, q_form, N)

    diagonal = [c[i, i] for i in range(r)]
    adjacent = []
    for i in range(r):
        for j in range(r):
            if i != j and ip[i, j] == -1:
                adjacent.append((i, j, c[i, j]))

    return {
        "braiding": c,
        "diagonal": diagonal,
        "off_diagonal_adjacent": adjacent,
        "nilpotency_order": [2] * r,  # Q_i^2 = 0 for all i (simply-laced)
    }


def quantum_group_dimension(lie_type: str, N: int) -> int:
    """Dimension of the small quantum group u_zeta(g) at zeta = e^{2pi i/N}.

    dim u_zeta(g) = N^{dim g} for N odd.
    """
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    # Number of positive roots for simply-laced
    if lie_type.startswith("A"):
        n = r
        num_pos_roots = n * (n + 1) // 2
    elif lie_type == "D4":
        num_pos_roots = 12
    else:
        raise ValueError(f"Unsupported: {lie_type}")
    dim_g = 2 * num_pos_roots + r
    return N**dim_g


def quantum_group_num_simples(lie_type: str, N: int) -> int:
    """Number of simple modules of u_zeta(g) at zeta = e^{2pi i/N}.

    For N odd and coprime to |P/Q|:
      number of simples = N^r
    where r = rank.
    """
    A = cartan_matrix(lie_type)
    r = A.shape[0]
    return N**r


def a2_screening_analysis(N: int, verbose: bool = False):
    """Full screening analysis for A_2 at deformation order N.

    Returns a dict with:
    - braiding data
    - quantum group comparison
    - nilpotency data
    """
    ip = inner_product_matrix("A2")
    q = standard_antisymmetric_form(2, N)
    c = cocycle_commutator(ip, q, N)
    zeta = np.exp(2j * np.pi / N)

    # Screening braiding
    table = screening_braiding_table("A2", N)

    # Quantum group data
    qg_dim = quantum_group_dimension("A2", N)
    qg_simples = quantum_group_num_simples("A2", N)

    # Off-diagonal braiding phase
    # For A_2 with q(alpha_1, alpha_2) = 1:
    # c(alpha_1, alpha_2) = (-1)^{-1} * zeta^2 = -zeta^2
    expected_braiding_12 = -zeta**2
    actual_braiding_12 = c[0, 1]

    result = {
        "N": N,
        "braiding_matrix": c,
        "diagonal_entries": [c[i, i] for i in range(2)],
        "c_12": actual_braiding_12,
        "c_21": c[1, 0],
        "expected_c_12": expected_braiding_12,
        "braiding_match": np.isclose(actual_braiding_12, expected_braiding_12),
        "diagonal_trivial": all(np.isclose(c[i, i], 1.0) for i in range(2)),
        "nilpotency_orders": [2, 2],
        "qg_dim": qg_dim,
        "qg_num_simples": qg_simples,
        "product_c12_c21": c[0, 1] * c[1, 0],
    }

    if verbose:
        print(f"A_2 screening analysis at N = {N}")
        print(f"  zeta = e^{{2pi i/{N}}}")
        print(f"  Braiding matrix:")
        print(f"    c_11 = {c[0,0]:.6f}  (expected 1)")
        print(f"    c_12 = {c[0,1]:.6f}  (expected -zeta^2 = {expected_braiding_12:.6f})")
        print(f"    c_21 = {c[1,0]:.6f}")
        print(f"    c_22 = {c[1,1]:.6f}  (expected 1)")
        print(f"  c_12 * c_21 = {c[0,1]*c[1,0]:.6f}  (should be 1)")
        print(f"  Nilpotency: Q_i^2 = 0 for both generators")
        print(f"  u_zeta(sl_3) dimension: {qg_dim}")
        print(f"  u_zeta(sl_3) simples: {qg_simples}")

    return result


def verify_antisymmetry(q_form: np.ndarray, N: int) -> bool:
    """Verify that q is antisymmetric mod N."""
    r = q_form.shape[0]
    for i in range(r):
        for j in range(r):
            if (q_form[i, j] + q_form[j, i]) % N != 0:
                return False
    return True


def all_antisymmetric_forms(r: int, N: int):
    """Enumerate all non-zero antisymmetric bilinear forms on Z^r -> Z/NZ.

    For rank 2, these are parametrized by q(alpha_1, alpha_2) in {1, ..., N-1}.
    """
    if r == 2:
        for a in range(1, N):
            q = np.zeros((2, 2), dtype=int)
            q[0, 1] = a
            q[1, 0] = (N - a) % N
            yield q
    else:
        raise NotImplementedError("Only rank 2 enumeration implemented")


def a2_full_scan(N_max: int = 10):
    """Scan A_2 screening braiding for N = 3, ..., N_max.

    For each N, compute the braiding matrix and quantum group data.
    Returns list of analysis dicts.
    """
    results = []
    for N in range(3, N_max + 1):
        result = a2_screening_analysis(N)
        results.append(result)
    return results
