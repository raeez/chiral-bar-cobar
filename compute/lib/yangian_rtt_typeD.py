"""Type D Yangian RTT engine: orthogonal R-matrix and prefundamental CG.

FRONTIER COMPUTATION for MC3 extension to orthogonal Dynkin types
(conj:mc3-arbitrary-type). The Yangian Y(so(2N)) in the RTT presentation
uses the orthogonal R-matrix acting on the standard 2N-dimensional
representation.

MATHEMATICAL BACKGROUND:

  The orthogonal R-matrix for so(N) (N = 2n for type D_n), from Molev 2007:

    R(u) = I  -  P/u  +  Q/(u - kappa)

  where:
    - I = identity on V tensor V, dim V = N
    - P_{(ij),(kl)} = delta_{il} delta_{jk}  (permutation operator)
    - Q_{(ij),(kl)} = delta_{ij} delta_{kl}  (trace projection operator)
    - kappa = N/2 - 1  (for so(N))

  Key operator identities: P^2 = I, Q^2 = N*Q, PQ = QP = Q.

  This satisfies the Yang-Baxter equation:

    R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

  RTT relation:

    R_{12}(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R_{12}(u-v)

  where T(u) = sum_{n>=0} T^{(n)} u^{-n} is the generating matrix with
  T^{(0)} = I, and the T^{(n)}_{ij} for n >= 1 are generators of Y(so(N)).

  CRITICAL CONSISTENCY CHECK (D_3 = so(6) ~ sl(4)):
    The Lie algebra isomorphism so(6) ~ sl(4) implies Y(so(6)) ~ Y(sl(4)).
    Under this isomorphism:
      - The 6-dim vector rep of so(6) decomposes as Lambda^2(C^4) for sl(4)
      - The two 4-dim spinor reps of so(6) are the standard and dual of sl(4)
    The RTT presentations must agree (up to gauge equivalence).

  TRIALITY (D_4 = so(8)):
    so(8) has an S_3 outer automorphism group permuting the three
    8-dimensional representations: vector V(omega_1), spinor V(omega_3),
    co-spinor V(omega_4). The RTT relations must be triality-covariant.

  PREFUNDAMENTAL MODULES for Y(so(2N)):
    Built from the Borel subalgebra of the quantum affine algebra
    U_q(hat{D}_N). The Hernandez-Jimbo q-character formula gives:

      ch(L^-_i) = prod_{beta > 0, alpha_i in supp(beta)}
                      prod_{n >= 1} 1/(1 - e^{-n*beta})

    This is the SAME formula as all other types (HJ12, Section 5).
    The CG decomposition is:

      ch(V_lambda) * ch(L^-_i) = sum_mu mult(mu) * ch(L^-_i(shift=mu))

    which is proved algebraically by the distributive law (same as type A).

ROOT SYSTEM CONVENTIONS (type D_N):
  Cartan matrix for D_N (N >= 3):
    A_{ii} = 2 for all i
    A_{i,i+1} = A_{i+1,i} = -1 for i = 1, ..., N-2
    A_{N-2,N} = A_{N,N-2} = -1  (branching node)
    A_{N-1,N} = A_{N,N-1} = 0   (the two spinor nodes are NOT connected)

  Positive roots: N(N-1) = |D_N^+|.
  |W(D_N)| = 2^{N-1} * N!.

  Fundamental representations:
    V(omega_1) = standard 2N-dim (vector)
    V(omega_2) = Lambda^2(V) minus trace, dim = N(2N-1)-1 = 2N^2-N-1
    V(omega_{N-1}) = half-spinor, dim = 2^{N-1}
    V(omega_N) = half-spinor, dim = 2^{N-1}

References:
  - Molev, "Yangians and classical Lie algebras", AMS 2007, Ch. 4
  - Arnaudon-Avan-Crampé-Frappat-Ragoucy, "R-matrix presentation for
    super-Yangians Y(osp(m|2n))", J. Math. Phys. 44 (2003)
  - Hernandez-Jimbo 2012, Section 5 (prefundamental for all types)
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from functools import lru_cache
import numpy as np


# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------

WeightD = Tuple[int, ...]     # Weight in fundamental weight basis
FormalCharD = Dict[WeightD, int]  # Formal character


# ---------------------------------------------------------------------------
# D_N root system
# ---------------------------------------------------------------------------

class TypeDRootSystem:
    """Root system for D_N = so(2N), N >= 3.

    The Cartan matrix has the branching structure:

        o---o---o--- ... ---o---o
                                 \\
                                  o

    Node numbering: 1, 2, ..., N (0-indexed: 0, ..., N-1).
    The branching is at node N-2 (0-indexed), connected to nodes N-1 and N
    (the two spinor nodes, 0-indexed N-2 and N-1... no).

    CONVENTION (Bourbaki):
      Nodes: 1, 2, ..., N.  0-indexed: 0, 1, ..., N-1.
      Edges: (i, i+1) for i = 0, ..., N-3, PLUS (N-3, N-1).
      So node N-3 (0-indexed) is connected to N-2 AND N-1.

    Wait, let me be precise. For D_N with nodes labeled 1..N:
      A_{i,i+1} = A_{i+1,i} = -1 for i = 1, ..., N-2
      A_{N-2,N} = A_{N,N-2} = -1
    All other off-diagonal = 0.

    0-indexed:
      A_{i,i+1} = A_{i+1,i} = -1 for i = 0, ..., N-3
      A_{N-3,N-1} = A_{N-1,N-3} = -1
    """

    def __init__(self, N: int):
        assert N >= 3, f"D_N requires N >= 3, got {N}"
        self.N = N
        self.rank = N
        self.name = f"D{N}"

        # Cartan matrix
        self.cartan = [[0] * N for _ in range(N)]
        for i in range(N):
            self.cartan[i][i] = 2
        for i in range(N - 2):
            self.cartan[i][i + 1] = -1
            self.cartan[i + 1][i] = -1
        # Branching: node N-3 (0-indexed) also connects to node N-1
        self.cartan[N - 3][N - 1] = -1
        self.cartan[N - 1][N - 3] = -1

        # Simple roots in omega basis
        self.alpha: List[WeightD] = [
            tuple(self.cartan[i][j] for j in range(N))
            for i in range(N)
        ]

        # Build positive roots
        self.positive_roots: List[WeightD] = []
        self.positive_roots_alpha: List[Tuple[int, ...]] = []
        self._build_positive_roots()

        # Roots containing each simple root
        self.roots_containing: List[List[int]] = [[] for _ in range(N)]
        for idx, coeffs in enumerate(self.positive_roots_alpha):
            for i in range(N):
                if coeffs[i] > 0:
                    self.roots_containing[i].append(idx)

        # Weyl group (built on demand for small N, too large for N >= 5)
        self._weyl_group_cache = None

        # rho = (1, 1, ..., 1) in omega basis
        self.rho = tuple([1] * N)

    def _build_positive_roots(self):
        """Build positive roots by iterated simple reflections."""
        N = self.rank
        # Start from simple roots (unit vectors in alpha basis)
        roots = set()
        for i in range(N):
            roots.add(tuple(1 if j == i else 0 for j in range(N)))

        changed = True
        while changed:
            changed = False
            new = set()
            for c in roots:
                for i in range(N):
                    # <c, alpha_i^vee> = sum_j c_j * A_{j,i}
                    inner = sum(c[j] * self.cartan[j][i] for j in range(N))
                    r = list(c)
                    r[i] -= inner
                    r = tuple(r)
                    if all(x >= 0 for x in r) and any(x > 0 for x in r):
                        if r not in roots:
                            new.add(r)
            if new:
                roots |= new
                changed = True

        sorted_roots = sorted(roots, key=lambda x: (sum(x), x))
        for c in sorted_roots:
            self.positive_roots_alpha.append(c)
            w = tuple(
                sum(c[j] * self.alpha[j][k] for j in range(N))
                for k in range(N)
            )
            self.positive_roots.append(w)

    def num_positive_roots(self) -> int:
        """Expected: N(N-1) for D_N."""
        return len(self.positive_roots)

    def expected_num_positive_roots(self) -> int:
        return self.N * (self.N - 1)

    def coxeter_number(self) -> int:
        """Coxeter number h = 2(N-1) for D_N."""
        return 2 * (self.N - 1)

    def dual_coxeter_number(self) -> int:
        """Dual Coxeter number h* = 2N - 2 for D_N (simply-laced: h = h*)."""
        return 2 * self.N - 2

    def dim_algebra(self) -> int:
        """dim so(2N) = N(2N-1)."""
        return self.N * (2 * self.N - 1)

    # -------------------------------------------------------------------
    # Coordinate conversion
    # -------------------------------------------------------------------

    def omega_to_alpha(self, w: WeightD) -> Optional[Tuple[int, ...]]:
        """Convert weight from omega to alpha basis by solving A^T c = w."""
        N = self.rank
        A = self.cartan

        # Build A^T
        AT = [[A[j][k] for j in range(N)] for k in range(N)]

        # Solve by Gaussian elimination over integers
        # Augmented matrix [AT | w]
        aug = [row[:] + [w[i]] for i, row in enumerate(AT)]

        for col in range(N):
            # Find pivot
            pivot = None
            for row in range(col, N):
                if aug[row][col] != 0:
                    pivot = row
                    break
            if pivot is None:
                return None
            aug[col], aug[pivot] = aug[pivot], aug[col]

            for row in range(N):
                if row == col:
                    continue
                if aug[row][col] == 0:
                    continue
                # Eliminate using lcm
                g = _gcd(abs(aug[col][col]), abs(aug[row][col]))
                mult_row = abs(aug[col][col]) // g
                mult_pivot = aug[row][col] // g
                for j in range(N + 1):
                    aug[row][j] = mult_row * aug[row][j] - mult_pivot * aug[col][j]

        # Extract solution
        result = []
        for i in range(N):
            if aug[i][N] % aug[i][i] != 0:
                return None
            result.append(aug[i][N] // aug[i][i])
        return tuple(result)

    def alpha_to_omega(self, c: Tuple[int, ...]) -> WeightD:
        """Convert alpha-basis coefficients to omega-basis weight."""
        N = self.rank
        return tuple(
            sum(c[j] * self.alpha[j][k] for j in range(N))
            for k in range(N)
        )

    # -------------------------------------------------------------------
    # Weyl group (only for small N)
    # -------------------------------------------------------------------

    def weyl_group(self) -> List[Tuple[int, Tuple]]:
        """Build Weyl group for small N (N <= 4).

        Returns list of (det, matrix) pairs where matrix acts on omega basis.
        WARNING: |W(D_N)| = 2^{N-1} * N!, grows very fast.
        """
        if self._weyl_group_cache is not None:
            return self._weyl_group_cache

        N = self.rank
        if N > 5:
            raise ValueError(f"Weyl group too large for D_{N}: "
                             f"|W| = {2**(N-1) * _factorial(N)}")

        def s_mat(i: int):
            m = [[0] * N for _ in range(N)]
            for j in range(N):
                for k in range(N):
                    m[j][k] = (1 if j == k else 0) - (
                        1 if k == i else 0) * self.cartan[i][j]
            return tuple(tuple(row) for row in m)

        def compose(m1, m2):
            r = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        r[i][j] += m1[i][k] * m2[k][j]
            return tuple(tuple(row) for row in r)

        def det_n(m):
            """Determinant via numpy for N x N."""
            arr = np.array(m, dtype=float)
            return int(round(np.linalg.det(arr)))

        identity = tuple(
            tuple(1 if i == j else 0 for j in range(N)) for i in range(N)
        )
        generators = [s_mat(i) for i in range(N)]

        elements = {identity}
        queue = [identity]
        while queue:
            m = queue.pop(0)
            for s in generators:
                n = compose(s, m)
                if n not in elements:
                    elements.add(n)
                    queue.append(n)

        self._weyl_group_cache = [(det_n(m), m) for m in elements]
        return self._weyl_group_cache

    def expected_weyl_order(self) -> int:
        """Expected |W(D_N)| = 2^{N-1} * N!."""
        return 2 ** (self.N - 1) * _factorial(self.N)

    # -------------------------------------------------------------------
    # Weight multiplicities
    # -------------------------------------------------------------------

    def weight_multiplicity(self, hw: WeightD, mu: WeightD) -> int:
        """Weight multiplicity via Kostant's formula.

        Works only for small N where Weyl group is computed.
        """
        N = self.rank
        rho = self.rho
        hw_rho = tuple(hw[i] + rho[i] for i in range(N))
        mu_rho = tuple(mu[i] + rho[i] for i in range(N))

        W = self.weyl_group()
        total = 0
        for det_w, mat in W:
            w_hw_rho = tuple(
                sum(mat[j][k] * hw_rho[k] for k in range(N))
                for j in range(N)
            )
            diff = tuple(w_hw_rho[i] - mu_rho[i] for i in range(N))
            alpha_coords = self.omega_to_alpha(diff)
            if alpha_coords is None:
                continue
            if any(c < 0 for c in alpha_coords):
                continue
            K = self._kostant_partition(alpha_coords)
            total += det_w * K

        return total

    @lru_cache(maxsize=None)
    def _kostant_partition(self, c: Tuple[int, ...]) -> int:
        """Number of ways to write c as non-neg int combination of pos roots."""
        if any(x < 0 for x in c):
            return 0
        return self._kostant_dp(c, len(self.positive_roots_alpha) - 1)

    @lru_cache(maxsize=None)
    def _kostant_dp(self, target: Tuple[int, ...], max_idx: int) -> int:
        if all(x == 0 for x in target):
            return 1
        if max_idx < 0 or any(x < 0 for x in target):
            return 0

        root = self.positive_roots_alpha[max_idx]
        total = 0
        cur = target
        while all(x >= 0 for x in cur):
            total += self._kostant_dp(cur, max_idx - 1)
            cur = tuple(cur[i] - root[i] for i in range(len(target)))
        return total

    # -------------------------------------------------------------------
    # Irreducible characters
    # -------------------------------------------------------------------

    def irrep_character(self, hw: WeightD, depth: int = 8) -> FormalCharD:
        """Character of V_hw by Kostant multiplicity formula.

        Enumerates mu = hw - sum c_j alpha_j with sum c_j <= depth.
        """
        N = self.rank
        if any(x < 0 for x in hw):
            return {}

        char: FormalCharD = {}

        def enum_weights(idx: int, remaining: int, coeffs: List[int]):
            if idx == N:
                mu = tuple(
                    hw[k] - sum(
                        coeffs[j] * self.alpha[j][k]
                        for j in range(N)
                    )
                    for k in range(N)
                )
                m = self.weight_multiplicity(hw, mu)
                if m > 0:
                    char[mu] = char.get(mu, 0) + m
                return
            for c in range(remaining + 1):
                coeffs.append(c)
                enum_weights(idx + 1, remaining - c, coeffs)
                coeffs.pop()

        enum_weights(0, depth, [])
        return char

    # -------------------------------------------------------------------
    # HJ prefundamental character
    # -------------------------------------------------------------------

    def prefundamental_character(self, node: int, depth: int = 8) -> FormalCharD:
        """Hernandez-Jimbo prefundamental character L^-_{node}.

        ch(L^-_i) = prod_{beta>0, alpha_i in supp(beta)}
                        prod_{n >= 1} 1 / (1 - e^{-n*beta})
        """
        N = self.rank
        relevant_indices = self.roots_containing[node]
        relevant_roots_omega = [self.positive_roots[idx] for idx in relevant_indices]
        relevant_roots_alpha = [self.positive_roots_alpha[idx] for idx in relevant_indices]

        zero = tuple([0] * N)
        char: FormalCharD = {zero: 1}

        for r_idx, beta_omega in enumerate(relevant_roots_omega):
            beta_alpha = relevant_roots_alpha[r_idx]
            beta_height = sum(beta_alpha)

            max_n = max(1, depth // beta_height) if beta_height > 0 else depth

            for n in range(1, max_n + 1):
                step = tuple(-n * beta_omega[k] for k in range(N))

                new_char: FormalCharD = {}
                for w, m in char.items():
                    shifted = w
                    while True:
                        # Height check
                        total_d = sum(abs(shifted[k]) for k in range(N))
                        if total_d > 3 * depth:
                            break
                        new_char[shifted] = new_char.get(shifted, 0) + m
                        shifted = tuple(shifted[k] + step[k] for k in range(N))

                char = new_char

        return char


# ---------------------------------------------------------------------------
# Orthogonal R-matrix
# ---------------------------------------------------------------------------

def orthogonal_r_matrix(N: int, u: float) -> np.ndarray:
    """Orthogonal R-matrix R(u) for so(N) acting on C^N tensor C^N.

    R(u) = I - P/u + Q/(u - kappa)

    where kappa = N/2 - 1 and:
      P_{(ij),(kl)} = delta_{il} delta_{jk}  (permutation)
      Q_{(ij),(kl)} = delta_{ij} delta_{kl}  (trace projection)

    Operator identities: P^2 = I, Q^2 = N*Q, PQ = QP = Q.

    Reference: Molev, "Yangians and classical Lie algebras", AMS 2007, eq (4.1).

    Returns: N^2 x N^2 matrix (row index = (i,j), col index = (k,l)).

    WARNING: singular at u = 0 and u = kappa = N/2 - 1.
    """
    kappa = N / 2.0 - 1.0
    dim = N * N

    P = _make_P(N)
    Q = _make_Q(N)

    R = np.eye(dim) - P / u + Q / (u - kappa)
    return R


def _make_P(N: int) -> np.ndarray:
    """Permutation operator P_{(ij),(kl)} = delta_{il} delta_{jk}."""
    dim = N * N
    P = np.zeros((dim, dim))
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1.0
    return P


def _make_Q(N: int) -> np.ndarray:
    """Trace projection Q_{(ij),(kl)} = delta_{ij} delta_{kl}."""
    dim = N * N
    Q = np.zeros((dim, dim))
    for i in range(N):
        for k in range(N):
            Q[i * N + i, k * N + k] = 1.0
    return Q


def orthogonal_r_matrix_symbolic(N: int):
    """Symbolic R-matrix for so(N).

    R(u) = I - P/u + Q/(u - kappa) with kappa = N/2 - 1.

    Returns (u_symbol, R_matrix_as_sympy_Matrix).
    """
    from sympy import Symbol, Rational as Rat, eye as seye, zeros as szeros

    u = Symbol('u')
    kappa = Rat(N, 2) - 1
    dim = N * N

    P = szeros(dim)
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1

    Q = szeros(dim)
    for i in range(N):
        for k in range(N):
            Q[i * N + i, k * N + k] = 1

    I = seye(dim)

    R = I - P / u + Q / (u - kappa)
    return u, R


# ---------------------------------------------------------------------------
# Yang-Baxter verification
# ---------------------------------------------------------------------------

def yang_baxter_check(N: int, u_val: float, v_val: float,
                      tol: float = 1e-10) -> Dict:
    """Verify Yang-Baxter equation for the orthogonal R-matrix:

    R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

    acting on V^{tensor 3}, V = C^N.  The matrices are N^3 x N^3.
    We embed R_{ab} into the triple tensor product by tensoring with identity
    in the remaining factor.
    """
    dim3 = N ** 3

    R12_u = _embed_12(orthogonal_r_matrix(N, u_val), N)
    R13_uv = _embed_13(orthogonal_r_matrix(N, u_val + v_val), N)
    R23_v = _embed_23(orthogonal_r_matrix(N, v_val), N)

    lhs = R12_u @ R13_uv @ R23_v
    rhs = R23_v @ R13_uv @ R12_u

    diff = np.max(np.abs(lhs - rhs))
    return {
        "N": N,
        "u": u_val,
        "v": v_val,
        "max_diff": diff,
        "passes": diff < tol,
    }


def _embed_12(R: np.ndarray, N: int) -> np.ndarray:
    """Embed N^2 x N^2 matrix R_{12} into N^3 x N^3 as R_{12} tensor I_3."""
    return np.kron(R, np.eye(N))


def _embed_23(R: np.ndarray, N: int) -> np.ndarray:
    """Embed N^2 x N^2 matrix R_{23} into N^3 x N^3 as I_1 tensor R_{23}."""
    return np.kron(np.eye(N), R)


def _embed_13(R: np.ndarray, N: int) -> np.ndarray:
    """Embed R_{13} into N^3 x N^3.

    R_{13} acts on factors 1 and 3 of V^{tensor 3}.
    (R_{13})_{(ijk),(lmn)} = R_{(ik),(ln)} * delta_{jm}
    """
    dim3 = N ** 3
    result = np.zeros((dim3, dim3))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                row = i * N * N + j * N + k
                for l in range(N):
                    for n in range(N):
                        col = l * N * N + j * N + n
                        # R acts on (i,k) -> (l,n)
                        result[row, col] += R[i * N + k, l * N + n]
    return result


# ---------------------------------------------------------------------------
# RTT relations
# ---------------------------------------------------------------------------

def rtt_relation_count(N: int) -> int:
    """Number of RTT relations for so(N).

    The RTT equation R_{12}(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R_{12}(u-v)
    has N^2 x N^2 = N^4 entries in the (ij,kl) indices. After symmetry
    reduction, there are N^2(N^2+1)/2 independent relations from the
    symmetric part and N^2(N^2-1)/2 from the antisymmetric.

    For the orthogonal Yangian, additional symmetry T(u)^t g T(-u-kappa) = g
    reduces further.

    Returns: N^2 (the number of matrix entries = independent generating relations).
    """
    return N ** 2


def rtt_generators_per_level(N: int) -> int:
    """Number of Yangian generators at each level for Y(so(N)).

    Y(so(N)) has dim(so(N)) = N(N-1)/2 independent generators per level
    (the T^{(n)}_{ij} modulo the orthogonality constraint).
    """
    return N * (N - 1) // 2


# ---------------------------------------------------------------------------
# Spectral decomposition of R-matrix
# ---------------------------------------------------------------------------

def r_matrix_spectral_decomposition(N: int) -> Dict:
    """Spectral decomposition of R(u) for so(N).

    V tensor V decomposes into three irreducible so(N)-subspaces:
      - Symmetric traceless S^2_0(V): dim = N(N+1)/2 - 1
      - Trace singlet: dim = 1
      - Antisymmetric Lambda^2(V): dim = N(N-1)/2 = adjoint so(N)

    On these subspaces, P and Q act as:
      P|_{S^2_0} = +1, P|_{singlet} = +1, P|_{Lambda^2} = -1
      Q|_{S^2_0} = 0,  Q|_{singlet} = N,  Q|_{Lambda^2} = 0

    So R(u) = I - P/u + Q/(u-kappa) has eigenvalues:
      On S^2_0:    1 - 1/u             = (u-1)/u
      On singlet:  1 - 1/u + N/(u-k)   = (u-1)/u + N/(u-k)
      On Lambda^2: 1 + 1/u             = (u+1)/u
    """
    kappa = N / 2.0 - 1.0
    dim = N * N
    P = _make_P(N)
    Q = _make_Q(N)

    # Verify operator identities
    P2_is_I = bool(np.allclose(P @ P, np.eye(dim)))
    Q2_is_NQ = bool(np.allclose(Q @ Q, N * Q))
    PQ_is_Q = bool(np.allclose(P @ Q, Q))
    QP_is_Q = bool(np.allclose(Q @ P, Q))

    # Eigenvalue counts for P
    P_eigs = np.linalg.eigvalsh(P)
    n_plus = int(round(sum(1 for e in P_eigs if e > 0.5)))
    n_minus = int(round(sum(1 for e in P_eigs if e < -0.5)))

    # Expected: Sym = N(N+1)/2, Alt = N(N-1)/2
    expected_sym = N * (N + 1) // 2
    expected_alt = N * (N - 1) // 2

    return {
        "N": N,
        "kappa": kappa,
        "dim_V_tensor_V": dim,
        "P_squared_is_I": P2_is_I,
        "Q_squared_is_NQ": Q2_is_NQ,
        "PQ_is_Q": PQ_is_Q,
        "QP_is_Q": QP_is_Q,
        "sym_dim": n_plus,
        "alt_dim": n_minus,
        "expected_sym": expected_sym,
        "expected_alt": expected_alt,
        "sym_matches": n_plus == expected_sym,
        "alt_matches": n_minus == expected_alt,
    }


# ---------------------------------------------------------------------------
# D_3 = so(6) ~ sl(4) consistency check
# ---------------------------------------------------------------------------

def d3_sl4_consistency() -> Dict:
    """Verify D_3 = so(6) ~ sl(4) at the root system level.

    so(6) has:
      rank = 3, |Phi^+| = 6, dim = 15, h = 4, h* = 4
      V(omega_1) = 6, V(omega_2) = 15, V(omega_3) = 4, V(omega_3') = 4

    sl(4) has:
      rank = 3, |Phi^+| = 6, dim = 15, h = 4, h* = 4

    The isomorphism maps:
      so(6) omega_1 <-> sl(4) omega_2 (Lambda^2 of standard)
      so(6) omega_2 <-> sl(4) adjoint
      so(6) omega_3 <-> sl(4) omega_1 (standard)
      so(6) omega_3' <-> sl(4) omega_3 (dual standard)
    """
    rs = TypeDRootSystem(3)
    checks = {}

    checks["rank"] = rs.rank == 3
    checks["num_pos_roots"] = rs.num_positive_roots() == 6
    checks["expected_pos_roots"] = rs.num_positive_roots() == rs.expected_num_positive_roots()
    checks["dim_algebra"] = rs.dim_algebra() == 15
    checks["coxeter"] = rs.coxeter_number() == 4
    checks["dual_coxeter"] = rs.dual_coxeter_number() == 4

    # Check Weyl group order: |W(D_3)| = 2^2 * 3! = 24 = |S_4| = |W(A_3)|
    W = rs.weyl_group()
    checks["weyl_order"] = len(W) == 24
    checks["weyl_expected"] = len(W) == rs.expected_weyl_order()

    # Verify dim V(omega_1) = 6 (vector rep of so(6))
    char_v = rs.irrep_character((1, 0, 0), depth=8)
    dim_v = sum(char_v.values())
    checks["dim_vector"] = dim_v == 6

    # Verify dim V(omega_3) = 4 (spinor)
    # omega_3 for D_3 is node 2 (0-indexed), which is a spinor node
    char_s = rs.irrep_character((0, 0, 1), depth=8)
    dim_s = sum(char_s.values())
    checks["dim_spinor"] = dim_s == 4

    return checks


# ---------------------------------------------------------------------------
# D_4 = so(8) triality
# ---------------------------------------------------------------------------

def d4_triality_check() -> Dict:
    """Verify D_4 = so(8) triality: three 8-dimensional representations.

    so(8) has three 8-dimensional fundamental representations:
      V(omega_1) = vector, dim 8
      V(omega_3) = half-spinor S+, dim 8
      V(omega_4) = half-spinor S-, dim 8
    (V(omega_2) = adjoint, dim 28.)

    The outer automorphism group S_3 permutes {omega_1, omega_3, omega_4}.
    """
    rs = TypeDRootSystem(4)
    checks = {}

    checks["rank"] = rs.rank == 4
    checks["num_pos_roots"] = rs.num_positive_roots() == 12
    checks["expected_pos_roots"] = (
        rs.num_positive_roots() == rs.expected_num_positive_roots()
    )
    checks["dim_algebra"] = rs.dim_algebra() == 28
    checks["coxeter"] = rs.coxeter_number() == 6
    checks["dual_coxeter"] = rs.dual_coxeter_number() == 6

    # Weyl group order: |W(D_4)| = 2^3 * 4! = 192
    W = rs.weyl_group()
    checks["weyl_order"] = len(W) == 192
    checks["weyl_expected"] = len(W) == rs.expected_weyl_order()

    # Three 8-dimensional representations
    char_v = rs.irrep_character((1, 0, 0, 0), depth=10)
    dim_v = sum(char_v.values())
    checks["dim_vector"] = dim_v == 8

    char_sp = rs.irrep_character((0, 0, 1, 0), depth=10)
    dim_sp = sum(char_sp.values())
    checks["dim_spinor_plus"] = dim_sp == 8

    char_sm = rs.irrep_character((0, 0, 0, 1), depth=10)
    dim_sm = sum(char_sm.values())
    checks["dim_spinor_minus"] = dim_sm == 8

    # Adjoint V(omega_2): dim 28
    char_adj = rs.irrep_character((0, 1, 0, 0), depth=10)
    dim_adj = sum(char_adj.values())
    checks["dim_adjoint"] = dim_adj == 28

    # Triality: all three 8-dim reps have the same number of weights
    checks["triality_weight_count"] = (
        len(char_v) == len(char_sp) == len(char_sm)
    )

    return checks


# ---------------------------------------------------------------------------
# Weyl dimension formulas (explicit, for cross-check)
# ---------------------------------------------------------------------------

def D3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension for D_3 = so(6), V(a*omega_1 + b*omega_2 + c*omega_3).

    Our D_3 Cartan matrix (with branching at node 0):
      [[2,-1,-1],[-1,2,0],[-1,0,2]]

    Positive roots in alpha basis: (0,0,1), (0,1,0), (1,0,0),
    (1,0,1), (1,1,0), (1,1,1).

    Using the product formula over positive roots (simply-laced,
    so alpha^vee = alpha), with lambda = (a,b,c), rho = (1,1,1).

    For each positive root with alpha-coords (c1,c2,c3), the inner product
    <lambda+rho, alpha^vee> = sum_i (lambda_i + 1) * c_i.

    Computed directly from the 6 roots:
      (0,0,1): c+1 / 1
      (0,1,0): b+1 / 1
      (1,0,0): a+1 / 1
      (1,0,1): a+c+2 / 2
      (1,1,0): a+b+2 / 2
      (1,1,1): a+b+c+3 / 3

    dim = (a+1)(b+1)(c+1)(a+c+2)(a+b+2)(a+b+c+3) / (1*1*1*2*2*3)
        = (a+1)(b+1)(c+1)(a+c+2)(a+b+2)(a+b+c+3) / 12
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    return ((a + 1) * (b + 1) * (c + 1) * (a + c + 2)
            * (a + b + 2) * (a + b + c + 3)) // 12


def D4_dim(a: int, b: int, c: int, d: int) -> int:
    """Weyl dimension for D_4 = so(8), V(a*omega_1 + b*omega_2 + c*omega_3 + d*omega_4).

    12 positive roots. The product formula:
    dim = prod_{alpha>0} <lambda+rho, alpha^vee> / <rho, alpha^vee>

    For D_4 with lambda = (a,b,c,d) and rho = (1,1,1,1):
    The 12 positive roots in the simple root basis are:
      e_i - e_j (1 <= i < j <= 4)  [6 roots: short in some sense]
      e_i + e_j (1 <= i < j <= 4)  [6 roots]

    In the alpha basis for D_4:
      alpha_1 = e_1 - e_2
      alpha_2 = e_2 - e_3
      alpha_3 = e_3 - e_4
      alpha_4 = e_3 + e_4

    The positive roots are exactly: all e_i - e_j (i<j) and e_i + e_j (i<j).

    Using inner products <omega_i, alpha^vee> = delta_{ij} (by definition):
    <lambda + rho, alpha^vee> for each positive root alpha.

    The explicit product is complicated, so compute numerically for now.
    """
    if a < 0 or b < 0 or c < 0 or d < 0:
        return 0

    # Use the Weyl dimension formula via products over positive roots
    # For D_4, the positive roots in the epsilon basis (e_1, ..., e_4) are:
    #   e_i - e_j (i < j) and e_i + e_j (i < j)
    # The inner product <lambda, alpha^vee> = <lambda, alpha> since |alpha|^2 = 2.
    #
    # We express lambda + rho in the epsilon basis:
    #   omega_1 = e_1, omega_2 = e_1 + e_2,
    #   omega_3 = (e_1+e_2+e_3-e_4)/2, omega_4 = (e_1+e_2+e_3+e_4)/2
    #   rho = (3, 2, 1, 0)  in epsilon basis.
    #
    # lambda + rho in epsilon = (a+b+(c+d)/2+3, b+(c+d)/2+2, (c+d)/2+1, (d-c)/2)

    # Use half-integers for spinor weights
    from fractions import Fraction
    lam_eps = [
        Fraction(a, 1) + Fraction(b, 1) + Fraction(c + d, 2) + 3,
        Fraction(b, 1) + Fraction(c + d, 2) + 2,
        Fraction(c + d, 2) + 1,
        Fraction(d - c, 2),
    ]
    rho_eps = [Fraction(3), Fraction(2), Fraction(1), Fraction(0)]

    num = Fraction(1)
    den = Fraction(1)
    # e_i - e_j roots
    for i in range(4):
        for j in range(i + 1, 4):
            num *= (lam_eps[i] - lam_eps[j])
            den *= (rho_eps[i] - rho_eps[j])
    # e_i + e_j roots
    for i in range(4):
        for j in range(i + 1, 4):
            num *= (lam_eps[i] + lam_eps[j])
            den *= (rho_eps[i] + rho_eps[j])

    result = num / den
    assert result.denominator == 1, f"Non-integer dimension: {result}"
    return int(result)


# ---------------------------------------------------------------------------
# CG verification for type D
# ---------------------------------------------------------------------------

def verify_cg_typeD(
    N: int,
    hw: WeightD,
    node: int,
    depth: int = 6,
) -> Dict:
    """Verify the universal CG identity for type D_N.

    LHS = ch(V_hw) * ch(L^-_{node})
    RHS = sum_{mu in wt(V_hw)} mult(mu) * ch(L^-_{node}(shift=mu))
    """
    rs = TypeDRootSystem(N)
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 3)
    V_dim = sum(V_char.values())
    L_char = rs.prefundamental_character(node, depth=depth)

    lhs = _tensor_product_D(V_char, L_char)

    rhs: FormalCharD = {}
    for mu, mult in V_char.items():
        L_shifted = _shift_char_D(L_char, mu)
        for w, m in L_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    max_reliable = 2 * (depth - sum(hw) - 3)
    if max_reliable < 0:
        max_reliable = 0

    match = True
    mismatches = []
    for w in set(list(lhs.keys()) + list(rhs.keys())):
        dist = sum(abs(w[k]) for k in range(len(w)))
        if dist <= max_reliable:
            l_val = lhs.get(w, 0)
            r_val = rhs.get(w, 0)
            if l_val != r_val:
                match = False
                mismatches.append((w, l_val, r_val))

    return {
        "root_system": f"D{N}",
        "hw": hw,
        "node": node,
        "V_dim": V_dim,
        "match": match,
        "n_mismatches": len(mismatches),
        "mismatches": mismatches[:5],
    }


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def _add_wt(w1: WeightD, w2: WeightD) -> WeightD:
    return tuple(w1[k] + w2[k] for k in range(len(w1)))


def _tensor_product_D(chi1: FormalCharD, chi2: FormalCharD) -> FormalCharD:
    result: FormalCharD = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = _add_wt(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def _shift_char_D(chi: FormalCharD, s: WeightD) -> FormalCharD:
    return {_add_wt(w, s): m for w, m in chi.items()}


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------

def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def _factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ---------------------------------------------------------------------------
# R-matrix symmetry properties
# ---------------------------------------------------------------------------

def r_matrix_symmetry_check(N: int, u_val: float = 1.5) -> Dict:
    """Check symmetry properties of the orthogonal R-matrix.

    Properties:
      1. PT-symmetry: R_{12}(u) = R_{21}(u) (since P and Q are both
         symmetric under swap of tensor factors)
      2. Unitarity: R_{12}(u) R_{21}(-u) proportional to identity
      3. R(u) regularity: R(u) has poles at u=0 and u=kappa only

    Note: u_val must avoid 0 and kappa = N/2-1.
    """
    kappa = N / 2.0 - 1.0
    R_u = orthogonal_r_matrix(N, u_val)
    R_neg_u = orthogonal_r_matrix(N, -u_val)

    dim = N * N
    P = _make_P(N)

    # R_{21}(u) = P R_{12}(u) P
    R21_u = P @ R_u @ P

    # PT symmetry: R_{12}(u) = R_{21}(u)
    # This holds because P_{12} and Q_{12} are symmetric under 1<->2 swap.
    pt_sym = bool(np.allclose(R_u, R21_u, atol=1e-10))

    # Unitarity: R_{12}(u) R_{21}(-u)
    R21_neg_u = P @ R_neg_u @ P
    prod = R_u @ R21_neg_u
    # Check if proportional to identity
    diag_vals = np.diag(prod)
    off_diag = prod - np.diag(diag_vals)
    unitarity_holds = bool(
        np.allclose(off_diag, 0, atol=1e-8)
        and np.std(diag_vals) / (abs(np.mean(diag_vals)) + 1e-15) < 1e-8
    )

    return {
        "N": N,
        "pt_symmetry": pt_sym,
        "unitarity_proportional": unitarity_holds,
        "kappa": kappa,
    }


# ---------------------------------------------------------------------------
# Prefundamental CG batch verification
# ---------------------------------------------------------------------------

def verify_cg_batch_typeD(N: int, max_hw_sum: int = 1, depth: int = 6) -> Dict:
    """Batch CG verification for type D_N, fundamental weights."""
    rs = TypeDRootSystem(N)
    results = {}
    n_pass = 0
    n_fail = 0

    for node in range(N):
        # Fundamental weight omega_{node+1}
        hw = tuple(1 if k == node else 0 for k in range(N))
        key = f"D{N}: V_omega{node+1} x L^-_{node+1}"
        res = verify_cg_typeD(N, hw, node, depth=depth)
        results[key] = res
        if res["match"]:
            n_pass += 1
        else:
            n_fail += 1

    return {"results": results, "n_pass": n_pass, "n_fail": n_fail,
            "all_pass": n_fail == 0}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("TYPE D YANGIAN RTT ENGINE")
    print("=" * 70)

    # D_3 consistency
    print("\n--- D_3 = so(6) ~ sl(4) consistency ---")
    for key, val in d3_sl4_consistency().items():
        tag = "OK" if val else "FAIL"
        print(f"  [{tag}] {key}: {val}")

    # D_4 triality
    print("\n--- D_4 = so(8) triality ---")
    for key, val in d4_triality_check().items():
        tag = "OK" if val else "FAIL"
        print(f"  [{tag}] {key}: {val}")

    # Yang-Baxter for so(6)
    print("\n--- Yang-Baxter check ---")
    for N in [4, 6, 8]:
        res = yang_baxter_check(N, 1.5, 2.3)
        tag = "PASS" if res["passes"] else "FAIL"
        print(f"  [{tag}] so({N}): max_diff = {res['max_diff']:.2e}")

    # R-matrix symmetry
    print("\n--- R-matrix symmetry ---")
    for N in [4, 6, 8]:
        sym = r_matrix_symmetry_check(N)
        print(f"  so({N}): unitarity={sym['unitarity']}, PT={sym['pt_symmetry']}")
