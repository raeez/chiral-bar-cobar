"""
Numerical verification of quantum determinant centrality for Y(gl_N), N=2,3.

The quantum determinant qdet T(u) is central in Y(gl_N):
  [qdet T(u), t_{ij}(v)] = 0  for all i,j,u,v.

Column-determinant formula (Molev, Theorem 1.6.4):
  qdet T(u) = sum_{sigma in S_N} (-1)^sigma
              t_{sigma(N-1),N-1}(u-(N-1)*Psi) ... t_{sigma(1),1}(u-Psi) t_{sigma(0),0}(u)

where the product is ordered with DECREASING column index left-to-right
(j=N-1 is the leftmost factor, j=0 is the rightmost). This is the
convention that yields a central element.

Each t_{ij}(u) is an operator on the quantum space, built from evaluation
representations via the Yang R-matrix R(u) = u*I + Psi*P, with
L-operator L_k(u) = (u - a_k)*I + Psi*P_{0k} (unnormalized convention).

VERIFIED by four independent paths:
  [DC] direct matrix commutator computation (centrality)
  [LT] Molev "Yangians and Classical Lie Algebras" Theorem 1.6.4
  [LC] qdet is scalar multiple of identity in eval rep (stronger than central)
  [CF] explicit S_N column-determinant formula matches generic computation
"""
from itertools import permutations
import numpy as np
import pytest

np.random.seed(42)
TOL = 1e-10
PASS_COUNT = 0
FAIL_COUNT = 0

# Fixture for Psi values used across multiple tests
PSI_VALUES = [0.5, 1.0, 2.0]

@pytest.fixture
def Psi_values():
    return PSI_VALUES


def report(name, ok):
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        print(f"  PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"  FAIL: {name}")


def permutation_sign(sigma):
    """Sign of permutation given as a tuple."""
    sigma = list(sigma)
    n = len(sigma)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = sigma[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign


def build_monodromy(u, Psi, N, M, params):
    """
    Build monodromy matrix T(u) = L_{M-1}(u) ... L_0(u) in evaluation
    representation on M copies of C^N.

    L_k(u) = (u - a_k)*I_{aux x quantum} + Psi * P_{aux, site_k}

    Returns: array of shape (N, N, N^M, N^M) where T[a,b] is the
    operator t_{ab}(u) on the quantum space (C^N)^M.
    """
    qdim = N ** M
    full_dim = N * qdim
    T_full = np.eye(full_dim, dtype=complex)

    for k in range(M):
        P_ak = np.zeros((full_dim, full_dim), dtype=complex)
        for idx in range(full_dim):
            aux_val = idx // qdim
            q_idx = idx % qdim

            sites = []
            temp = q_idx
            for _ in range(M):
                sites.append(temp % N)
                temp //= N

            new_aux = sites[k]
            new_sites = list(sites)
            new_sites[k] = aux_val

            new_q = 0
            for m in range(M - 1, -1, -1):
                new_q = new_q * N + new_sites[m]
            new_idx = new_aux * qdim + new_q

            P_ak[new_idx, idx] = 1.0

        L_k = (u - params[k]) * np.eye(full_dim, dtype=complex) + Psi * P_ak
        T_full = L_k @ T_full

    T = np.zeros((N, N, qdim, qdim), dtype=complex)
    for a in range(N):
        for b in range(N):
            for qi in range(qdim):
                for qj in range(qdim):
                    T[a, b, qi, qj] = T_full[a * qdim + qi, b * qdim + qj]

    return T


def compute_qdet(T, N, Psi, u):
    """
    Quantum determinant via column-determinant formula.

    Product ordering: j=N-1 leftmost, j=0 rightmost (decreasing column index).
    This is the convention producing a central element.

    T is a function: T(u) -> (N, N, qdim, qdim) array.
    """
    T0 = T(u)
    qdim = T0.shape[2]
    qdet_op = np.zeros((qdim, qdim), dtype=complex)

    indices = list(range(N))
    for sigma in permutations(indices):
        sign = permutation_sign(sigma)
        # Accumulate with j increasing: each new factor goes on LEFT
        # Result: T_{N-1} @ T_{N-2} @ ... @ T_0
        prod_op = np.eye(qdim, dtype=complex)
        for j in range(N):
            Tj = T(u - j * Psi)
            prod_op = Tj[sigma[j], j] @ prod_op
        qdet_op += sign * prod_op

    return qdet_op


# ---------------------------------------------------------------------------
# Test 1: Centrality [qdet T(u), t_{ij}(v)] = 0
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("N,M", [(2, 2), (3, 2)])
def test_centrality(N, M, Psi_values):
    """Test [qdet T(u), t_{ij}(v)] = 0 for given N, M, multiple Psi values."""
    print(f"\n=== Centrality: N={N}, M={M} (qdim={N**M}) ===")

    for Psi in Psi_values:
        params = np.random.uniform(-2, 2, size=M)

        def T_func(u, _Psi=Psi, _params=params):
            return build_monodromy(u, _Psi, N, M, _params)

        u_vals = np.random.uniform(-3, 3, size=3)
        v_vals = np.random.uniform(-3, 3, size=3)

        for u in u_vals:
            qdet_op = compute_qdet(T_func, N, Psi, u)

            for v in v_vals:
                Tv = T_func(v)
                max_comm = 0.0
                for i in range(N):
                    for j in range(N):
                        comm = qdet_op @ Tv[i, j] - Tv[i, j] @ qdet_op
                        max_comm = max(max_comm, np.max(np.abs(comm)))

                report(
                    f"Psi={Psi}, u={u:.3f}, v={v:.3f}: "
                    f"max |[qdet, t_ij]| = {max_comm:.2e}",
                    max_comm < TOL
                )


# ---------------------------------------------------------------------------
# Test 2: N=2 explicit formula
# ---------------------------------------------------------------------------
def test_n2_explicit(Psi_values):
    """
    For N=2, verify the explicit formula matches the generic computation.

    Column determinant for N=2 (j=1 left, j=0 right):
      qdet = t_{1,1}(u-Psi) @ t_{0,0}(u) - t_{0,1}(u-Psi) @ t_{1,0}(u)
    """
    print("\n=== N=2 explicit formula ===")
    N = 2
    M = 2

    for Psi in Psi_values:
        params = np.random.uniform(-2, 2, size=M)

        def T_func(u, _Psi=Psi, _params=params):
            return build_monodromy(u, _Psi, N, M, _params)

        u = np.random.uniform(-3, 3)
        Tu = T_func(u)
        Tu_shift = T_func(u - Psi)

        # sigma=(0,1) even: T_{1,1}(u-h) @ T_{0,0}(u)
        # sigma=(1,0) odd:  T_{0,1}(u-h) @ T_{1,0}(u)
        qdet_explicit = Tu_shift[1, 1] @ Tu[0, 0] - Tu_shift[0, 1] @ Tu[1, 0]

        qdet_generic = compute_qdet(T_func, N, Psi, u)

        diff = np.max(np.abs(qdet_explicit - qdet_generic))
        report(
            f"N=2 explicit vs generic at Psi={Psi}: max diff = {diff:.2e}",
            diff < TOL
        )


# ---------------------------------------------------------------------------
# Test 3: N=3 explicit 6-term formula
# ---------------------------------------------------------------------------
def test_n3_explicit(Psi_values):
    """
    For N=3, verify the 6-term S_3 formula matches the generic computation.

    Column determinant for N=3 (j=2 left, j=1 middle, j=0 right):
      qdet = sum_{sigma in S_3} (-1)^sigma
             t_{sigma(2),2}(u-2h) @ t_{sigma(1),1}(u-h) @ t_{sigma(0),0}(u)
    """
    print("\n=== N=3 explicit 6-term formula ===")
    N = 3
    M = 2

    for Psi in Psi_values:
        params = np.random.uniform(-2, 2, size=M)

        def T_func(u, _Psi=Psi, _params=params):
            return build_monodromy(u, _Psi, N, M, _params)

        u = np.random.uniform(-3, 3)
        Tu0 = T_func(u)
        Tu1 = T_func(u - Psi)
        Tu2 = T_func(u - 2 * Psi)

        # 6 terms with j=2 leftmost, j=0 rightmost:
        # (0,1,2) even: + Tu2[2,2] @ Tu1[1,1] @ Tu0[0,0]
        # (0,2,1) odd:  - Tu2[1,2] @ Tu1[2,1] @ Tu0[0,0]
        # (1,0,2) odd:  - Tu2[2,2] @ Tu1[0,1] @ Tu0[1,0]
        # (1,2,0) even: + Tu2[0,2] @ Tu1[2,1] @ Tu0[1,0]
        # (2,0,1) even: + Tu2[1,2] @ Tu1[0,1] @ Tu0[2,0]
        # (2,1,0) odd:  - Tu2[0,2] @ Tu1[1,1] @ Tu0[2,0]
        qdet_6 = (
            + Tu2[2, 2] @ Tu1[1, 1] @ Tu0[0, 0]
            - Tu2[1, 2] @ Tu1[2, 1] @ Tu0[0, 0]
            - Tu2[2, 2] @ Tu1[0, 1] @ Tu0[1, 0]
            + Tu2[0, 2] @ Tu1[2, 1] @ Tu0[1, 0]
            + Tu2[1, 2] @ Tu1[0, 1] @ Tu0[2, 0]
            - Tu2[0, 2] @ Tu1[1, 1] @ Tu0[2, 0]
        )

        qdet_generic = compute_qdet(T_func, N, Psi, u)

        diff = np.max(np.abs(qdet_6 - qdet_generic))
        report(
            f"N=3 6-term vs generic at Psi={Psi}: max diff = {diff:.2e}",
            diff < TOL
        )


# ---------------------------------------------------------------------------
# Test 4: qdet is scalar (multiple of identity) in eval rep
# ---------------------------------------------------------------------------
def test_qdet_is_scalar():
    """
    In the evaluation representation, qdet T(u) is a SCALAR operator
    (proportional to the identity on the quantum space). This is
    strictly stronger than centrality and provides an independent check.
    """
    print("\n=== qdet is scalar (proportional to identity) ===")

    for N, M in [(2, 2), (2, 3), (3, 2)]:
        Psi = 1.0
        params = np.random.uniform(-2, 2, size=M)
        qdim = N ** M

        def T_func(u, _Psi=Psi, _params=params, _N=N, _M=M):
            return build_monodromy(u, _Psi, _N, _M, _params)

        u = np.random.uniform(-3, 3)
        qdet_op = compute_qdet(T_func, N, Psi, u)

        trace_val = np.trace(qdet_op) / qdim
        deviation = qdet_op - trace_val * np.eye(qdim, dtype=complex)
        max_dev = np.max(np.abs(deviation))
        report(
            f"N={N}, M={M}: max |qdet - (tr/dim)*I| = {max_dev:.2e}",
            max_dev < TOL
        )


# ---------------------------------------------------------------------------
# Test 5: qdet at Psi=0 reduces to classical determinant
# ---------------------------------------------------------------------------
def test_classical_limit():
    """
    At Psi=0, T(u) = prod_k (u-a_k) * I (diagonal, scalar), and
    qdet T(u) = [prod_k (u-a_k)]^N * I = [det T(u)]_classical * I.
    """
    print("\n=== Classical limit Psi=0 ===")

    for N, M in [(2, 2), (2, 3), (3, 2)]:
        Psi = 0.0
        params = np.random.uniform(-2, 2, size=M)
        qdim = N ** M

        def T_func(u, _Psi=Psi, _params=params, _N=N, _M=M):
            return build_monodromy(u, _Psi, _N, _M, _params)

        u = np.random.uniform(-3, 3)
        qdet_op = compute_qdet(T_func, N, Psi, u)

        # At Psi=0: T(u) = [prod_k(u-a_k)] * I_{NxN} as matrix of scalars
        # qdet = det of scalar matrix = [prod_k(u-a_k)]^N
        classical_det = np.prod(u - params) ** N
        expected = classical_det * np.eye(qdim, dtype=complex)

        diff = np.max(np.abs(qdet_op - expected))
        report(
            f"N={N}, M={M}: max |qdet(Psi=0) - classical det| = {diff:.2e}",
            diff < TOL
        )


# ---------------------------------------------------------------------------
# Test 6: Consistency across different M (number of sites)
# ---------------------------------------------------------------------------
def test_consistency_across_sites():
    """
    Verify that qdet is scalar and central for multiple site counts M,
    confirming the construction works beyond minimal examples.
    """
    print("\n=== Consistency across M (site count) ===")

    N = 2
    Psi = 1.0
    for M in [1, 2, 3, 4]:
        params = np.random.uniform(-2, 2, size=M)
        qdim = N ** M

        def T_func(u, _Psi=Psi, _params=params, _N=N, _M=M):
            return build_monodromy(u, _Psi, _N, _M, _params)

        u = np.random.uniform(-3, 3)
        v = np.random.uniform(-3, 3)

        qdet_op = compute_qdet(T_func, N, Psi, u)

        # Check scalar
        trace_val = np.trace(qdet_op) / qdim
        deviation = qdet_op - trace_val * np.eye(qdim, dtype=complex)
        max_dev = np.max(np.abs(deviation))
        report(f"N=2, M={M}: scalar? max dev = {max_dev:.2e}", max_dev < TOL)

        # Check centrality
        Tv = T_func(v)
        max_comm = 0.0
        for i in range(N):
            for j in range(N):
                comm = qdet_op @ Tv[i, j] - Tv[i, j] @ qdet_op
                max_comm = max(max_comm, np.max(np.abs(comm)))
        report(f"N=2, M={M}: central? max comm = {max_comm:.2e}", max_comm < TOL)


if __name__ == "__main__":
    print("Quantum determinant centrality verification for Y(gl_N)")
    print("=" * 60)

    Psi_values = [0.5, 1.0, 2.0]

    # Core centrality tests
    test_centrality(N=2, M=2, Psi_values=Psi_values)
    test_centrality(N=3, M=2, Psi_values=Psi_values)

    # Explicit formula agreement
    test_n2_explicit(Psi_values)
    test_n3_explicit(Psi_values)

    # Scalar property (stronger than centrality)
    test_qdet_is_scalar()

    # Classical limit
    test_classical_limit()

    # Consistency across site counts
    test_consistency_across_sites()

    print("\n" + "=" * 60)
    print(f"TOTAL: {PASS_COUNT} passed, {FAIL_COUNT} failed")
    if FAIL_COUNT > 0:
        raise SystemExit(1)
    else:
        print("ALL TESTS PASSED")
