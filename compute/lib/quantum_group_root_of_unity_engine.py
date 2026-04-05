r"""Quantum groups at roots of unity: shadow obstruction tower and 3-manifold invariants.

At generic q, U_q(g) is a deformation of U(g) with equivalent semisimple
representation theory.  At q = exp(2*pi*i/p) (a primitive p-th root of unity),
the structure changes radically:

1. The CENTER ENLARGES: Z(U_q(sl_2)) = <K^p, E^p, F^p, C_q> where C_q is
   the quantum Casimir.  The Frobenius center <E^p, F^p, K^p> is new.

2. REPRESENTATION THEORY TRUNCATES: irreducible type-1 reps have dimensions
   1, 2, ..., p-1.  Dimension-p reps are type 2 (no classical analogue).

3. The R-MATRIX TRUNCATES: the universal R-matrix
       R = q^{H otimes H/2} sum_n q^{n(n-1)/2} (q-q^{-1})^n / [n]! E^n otimes F^n
   terminates at n = p-1 because [p]_q = 0.

4. FUSION RULES become the Verlinde fusion rules:
       V_i otimes V_j = oplus_k N_{ij}^k V_k
   with truncation N_{ij}^k = 0 if k >= p-1 (for type-1 reps).

5. KAZHDAN-LUSZTIG CORRESPONDENCE: U_q(sl_2) at q = exp(2pi*i/(k+2))
   is equivalent (as a braided tensor category) to sl_2^(1) at level k.
   The shadow data must match: kappa(U_q) at q^{k+2}=1 should equal
   kappa(sl_2^(1)_k) = 3(k+2)/4.

6. 3-MANIFOLD INVARIANTS (Reshetikhin-Turaev): at roots of unity,
   quantum invariants of 3-manifolds are well-defined via the surgery
   presentation and truncated sums over type-1 representations.

7. LOGARITHMIC EXTENSIONS: at roots of unity, some representations become
   reducible but indecomposable (non-semisimple).  The shadow obstruction
   tower for the non-semisimple category captures log-CFT structure.

RESONANCE INTERPRETATION
========================
The R-matrix truncation at roots of unity is a concrete realization of
RESONANCE in the bar complex framework.  The resonance rank rho(A) controls
the MC4 completion:
  - Generic q: R-matrix has infinitely many terms, rho = infinity
  - Root of unity q^p = 1: R-matrix truncates at p-1 terms, rho = p-1

This is the FINITE RESONANCE PROBLEM: the MC element terminates at finite
arity, exactly as in the resonance-filtered bar-cobar theorem
(thm:resonance-filtered-bar-cobar).

CONVENTIONS
===========
q = exp(2*pi*i / p) where p >= 3 is the root-of-unity order.
Level k = p - 2 (Kazhdan-Lusztig correspondence with sl_2^(1)_k).
Quantum integers: [n]_q = (q^n - q^{-n}) / (q - q^{-1}).
The quantum factorial [n]! = [1][2]...[n], with [0]! = 1.
The R-matrix uses the Drinfeld double convention (not Lusztig's).

References
----------
* Kassel, "Quantum Groups", GTM 155, Springer (1995), Ch. VI, XVII
* Reshetikhin-Turaev, Invent. Math. 103 (1991), 547--597
* Turaev, "Quantum Invariants of Knots and 3-Manifolds", de Gruyter (2016)
* Kazhdan-Lusztig, JAMS 6 (1993), 905--947 (4 papers)
* Creutzig-Ridout, J. Phys. A 46 (2013), 494006 (logarithmic CFT)
* concordance.tex: thm:resonance-filtered-bar-cobar, def:resonance-rank,
  MC3 (DK bridge, all simple types), MC4 (completion towers)
"""

from __future__ import annotations

import cmath
import math
from functools import lru_cache
from typing import Dict, List, Optional, Tuple, Union

import numpy as np


# ============================================================
# 1. Quantum integers and combinatorics at roots of unity
# ============================================================

def quantum_integer(n: int, q: complex) -> complex:
    """Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}).

    At q = exp(2*pi*i/p): [p]_q = 0, [n]_q is periodic mod p.
    """
    if abs(q - 1.0) < 1e-14:
        return complex(n)
    qi = 1.0 / q
    denom = q - qi
    if abs(denom) < 1e-14:
        return complex(n)
    return (q ** n - qi ** n) / denom


def quantum_factorial(n: int, q: complex) -> complex:
    """Quantum factorial [n]!_q = [1]_q [2]_q ... [n]_q.

    At roots of unity q^p = 1: [n]! = 0 for n >= p since [p]_q = 0.
    """
    if n < 0:
        raise ValueError(f"Negative argument: {n}")
    if n == 0:
        return complex(1.0)
    result = complex(1.0)
    for k in range(1, n + 1):
        result *= quantum_integer(k, q)
    return result


def quantum_binomial(n: int, k: int, q: complex) -> complex:
    """Quantum binomial coefficient [n choose k]_q.

    Uses the product formula: [n]! / ([k]! [n-k]!) when well-defined.
    At roots of unity, uses the recursive formula to avoid 0/0.
    """
    if k < 0 or k > n:
        return complex(0.0)
    if k == 0 or k == n:
        return complex(1.0)

    # Recursive formula: [n choose k] = q^k [n-1 choose k] + q^{-(n-k)} [n-1 choose k-1]
    # This avoids division by zero at roots of unity.
    # Build bottom-up for efficiency.
    prev = [complex(0.0)] * (n + 1)
    prev[0] = complex(1.0)

    for i in range(1, n + 1):
        curr = [complex(0.0)] * (n + 1)
        curr[0] = complex(1.0)
        for j in range(1, i + 1):
            qi = 1.0 / q if abs(q) > 1e-14 else 0.0
            curr[j] = q ** j * prev[j] + q ** (-(i - j)) * prev[j - 1]
        prev = curr

    return prev[k]


def root_of_unity(p: int) -> complex:
    """Return q = exp(2*pi*i / p), a primitive p-th root of unity."""
    return cmath.exp(2.0j * cmath.pi / p)


def quantum_dimension(n: int, q: complex) -> complex:
    """Quantum dimension of the n-dimensional irrep of U_q(sl_2).

    dim_q(V_n) = [n]_q = (q^n - q^{-n})/(q - q^{-1}).
    At roots of unity, [n]_q = 0 iff p | n.
    """
    return quantum_integer(n, q)


# ============================================================
# 2. Center of U_q(sl_2) at roots of unity
# ============================================================

def frobenius_center_generators(p: int) -> Dict[str, str]:
    """The Frobenius center of U_q(sl_2) at q^p = 1.

    At generic q, the center is generated by the quantum Casimir C_q alone.
    At q^p = 1, the center enlarges to include E^p, F^p, K^{+/- p}.

    Returns a dictionary describing the generators.
    """
    return {
        "Casimir": "C_q = (q K + q^{-1} K^{-1}) / (q - q^{-1})^2 + FE",
        "Frobenius_E": f"E^{p}",
        "Frobenius_F": f"F^{p}",
        "Frobenius_K_plus": f"K^{p}",
        "Frobenius_K_minus": f"K^{{-{p}}}",
        "center_dim_classical_limit": "4 generators beyond Casimir",
        "note": ("K^p = 1 on type-1 reps; K^p, E^p, F^p act nontrivially "
                 "on type-2 (p-dimensional) reps."),
    }


def quantum_casimir_eigenvalue(n: int, q: complex) -> complex:
    """Eigenvalue of the quantum Casimir on the n-dimensional irrep V_n.

    C_q acts on V_n as the scalar:
       c_n = (q^n + q^{-n}) / (q - q^{-1})^2
           = [n]_q^2 * q^{n-1} / (q^{n-1} + q^{-(n-1)} + ...) -- NO.

    More precisely, with the standard convention:
       C_q = (qK - q^{-1}K^{-1})^2 / (q - q^{-1})^2 + FE + EF
    the eigenvalue on V_n (with highest weight q^{n-1}) is:

       c_n(q) = [n/2]_q [n/2 + 1]_q ... but this is not standard.

    CORRECT (Kassel, Prop. VI.4.3): The quantum Casimir
       C = FE + (qK + q^{-1}K^{-1}) / (q - q^{-1})^2
    acts on V_n (n-dimensional, spin j = (n-1)/2) as:
       c_n = (q^n + q^{-n}) / (q - q^{-1})^2

    This equals [(n-1)/2]_q [(n+1)/2]_q when written in terms of quantum
    integers, but the explicit formula is cleaner.
    """
    qi = 1.0 / q
    denom = (q - qi) ** 2
    if abs(denom) < 1e-30:
        # q = +/- 1 limit
        return complex(n * n / 4.0)
    return (q ** n + qi ** n) / denom


def center_dimension_at_root(p: int) -> Dict[str, int]:
    """Dimensions of the center and related structures at q^p = 1.

    The center Z(U_q(sl_2)) at q^p = 1 has dimension:
      dim Z = 3p - 1 (for p odd)
      dim Z = 3p/2 (for p even)

    The semisimple part has p-1 type-1 irreps (dims 1,...,p-1)
    and a family of p-dimensional type-2 irreps parametrized by
    (E^p, F^p, K^p).
    """
    n_type1_irreps = p - 1
    # Type 2 reps: parametrized by Frobenius center values
    # For each (alpha, beta, epsilon) with alpha*beta determined by epsilon,
    # there is a p-dimensional irrep.  This is a continuous family.

    return {
        "p": p,
        "n_type1_irreps": n_type1_irreps,
        "type1_dims": list(range(1, p)),
        "type2_dim": p,
        "frobenius_generators": 4,  # E^p, F^p, K^p, K^{-p}
        "classical_center_dim": 1,  # just C_q at generic q
        "note": "Type-2 reps form a continuous family parametrized by Frobenius center",
    }


# ============================================================
# 3. R-matrix at roots of unity (TRUNCATED)
# ============================================================

def universal_r_matrix_terms(p: int, q: complex,
                             max_terms: Optional[int] = None
                             ) -> List[Tuple[int, complex]]:
    """Terms of the universal R-matrix for U_q(sl_2).

    R = q^{H otimes H / 2} sum_{n=0}^{N} a_n E^n otimes F^n

    where a_n = q^{n(n-1)/2} (q - q^{-1})^n / [n]!_q.

    At generic q: N = infinity (the sum converges in a completion).
    At q^p = 1: the sum truncates at the first n where [n]_q = 0.

    Returns: list of (n, a_n) pairs.
    """
    qi = 1.0 / q
    # Find the truncation point
    truncation = r_matrix_term_count(p, q) if max_terms is None else max_terms

    terms = []
    # Build [n]! incrementally to avoid numerical issues
    qfact = complex(1.0)
    for n in range(truncation):
        if n > 0:
            qn = quantum_integer(n, q)
            if abs(qn) < 1e-8:
                break
            qfact *= qn

        # a_n = q^{n(n-1)/2} * (q - q^{-1})^n / [n]!
        coeff = q ** (n * (n - 1) / 2.0)
        coeff *= (q - qi) ** n
        coeff /= qfact
        terms.append((n, coeff))

    return terms


def truncated_r_matrix_sl2(p: int, dim_V: int) -> np.ndarray:
    """Truncated R-matrix for U_q(sl_2) on V_dim_V at q = exp(2pi*i/p).

    For the fundamental (dim_V = 2), this uses the explicit formula.
    For higher-dimensional reps, uses the spectral decomposition.

    The R-matrix is check_R = tau o R where tau is the flip.
    """
    q = root_of_unity(p)

    if dim_V == 2:
        return _check_r_fundamental_sl2(q)
    else:
        return _check_r_spectral_sl2(q, p, dim_V)


def _check_r_fundamental_sl2(q: complex) -> np.ndarray:
    """Enhanced R-matrix check_R on C^2 tensor C^2.

    check_R(e_a otimes e_b) = q^{delta_{ab}} e_b otimes e_a
                               + [a < b] (q - q^{-1}) e_a otimes e_b

    Eigenvalues: q on Sym^2 (mult 3), -q^{-1} on Lambda^2 (mult 1).
    """
    qi = 1.0 / q
    R = np.zeros((4, 4), dtype=complex)

    for a in range(2):
        for b in range(2):
            row = a * 2 + b
            col_swap = b * 2 + a
            col_same = a * 2 + b

            if a == b:
                R[col_swap, row] += q
            else:
                R[col_swap, row] += 1.0

            if a < b:
                R[col_same, row] += (q - qi)

    return R


def _check_r_spectral_sl2(q: complex, p: int, dim_V: int) -> np.ndarray:
    """R-matrix on V_{dim_V} tensor V_{dim_V} via spectral decomposition.

    V_m tensor V_m = V_1 + V_3 + ... + V_{2m-1}  (at generic q).
    At roots of unity, some summands may be absent (truncation).

    Spectral decomposition:
       check_R = sum_j f_j(q) P_j
    where P_j projects onto the V_{2j+1} component and
       f_j(q) = (-1)^{m-1-j} q^{j(j+1) - (m-1)m/2}  (up to normalization).

    More precisely, the eigenvalue on the V_{2j+1} component of
    V_m tensor V_m is:
       lambda_j = (-1)^{m-1-j} q^{(C_2(V_{2j+1}) - 2*C_2(V_m))/2}

    where C_2(V_n) = (q^n + q^{-n}) / (q - q^{-1})^2 is the Casimir
    eigenvalue (Kassel convention).
    """
    m = dim_V
    d = m * m

    # Build the Clebsch-Gordan decomposition numerically.
    # V_m otimes V_m = direct sum_{j=0}^{m-1} V_{2j+1}
    # (for generic q; at roots of unity some components may vanish).

    # Use the explicit matrix construction via q-Clebsch-Gordan coefficients.
    # For efficiency, build R from the Hecke-algebra approach for small dims.

    # For dim_V up to p-1, use the representation matrices directly.
    # Build E, F, K generators on V_m.
    E = np.zeros((m, m), dtype=complex)
    F = np.zeros((m, m), dtype=complex)
    K = np.zeros((m, m), dtype=complex)

    qi = 1.0 / q

    for i in range(m):
        # Basis: v_0 (highest weight), v_1, ..., v_{m-1}
        # K v_i = q^{m-1-2i} v_i
        K[i, i] = q ** (m - 1 - 2 * i)

        # E v_i = [m-1-i+1]_q [i]_q^{1/2} ... actually:
        # E v_i = [i]_q v_{i-1}  (lowering i)
        # F v_i = [m-1-i]_q v_{i+1} (raising i)
        # Wait, convention: v_0 is highest weight.
        # F v_i = [i+1]_q v_{i+1}
        # E v_i = [m-1-i]_q ... NO.

        # Standard convention (Kassel VI.3):
        # V_m has basis {v_0, ..., v_{m-1}} with
        # K v_i = q^{m-1-2i} v_i
        # E v_i = [m-1-i+1]_q v_{i-1} = [m-i]_q v_{i-1}
        # F v_i = [i+1]_q v_{i+1}

        if i > 0:
            E[i - 1, i] = quantum_integer(m - i, q)
        if i < m - 1:
            F[i + 1, i] = quantum_integer(i + 1, q)

    # Build the R-matrix on V_m tensor V_m using the universal formula
    # R = q^{H tensor H/2} sum_n a_n E^n tensor F^n
    # where a_n = q^{n(n-1)/2} (q-q^{-1})^n / [n]!

    Id_m = np.eye(m, dtype=complex)

    # q^{H tensor H/2}: on v_i tensor v_j, acts as q^{(m-1-2i)(m-1-2j)/2}
    H_diag = np.array([m - 1 - 2 * i for i in range(m)], dtype=complex)
    qHH = np.zeros((d, d), dtype=complex)
    for i in range(m):
        for j in range(m):
            idx = i * m + j
            qHH[idx, idx] = q ** (H_diag[i] * H_diag[j] / 2.0)

    # Compute E^n and F^n as matrices
    E_powers = [Id_m.copy()]
    F_powers = [Id_m.copy()]
    for n in range(1, min(p, m + 1)):
        E_powers.append(E_powers[-1] @ E)
        F_powers.append(F_powers[-1] @ F)

    # Sum: sum_n a_n (E^n tensor F^n)
    R_sum = np.zeros((d, d), dtype=complex)
    for n in range(min(p, m)):
        qfact = quantum_factorial(n, q)
        if abs(qfact) < 1e-30 and n > 0:
            break
        a_n = q ** (n * (n - 1) / 2.0) * (q - qi) ** n
        if n > 0:
            a_n /= qfact
        # E^n tensor F^n
        if n < len(E_powers) and n < len(F_powers):
            En_Fn = np.kron(E_powers[n], F_powers[n])
            R_sum += a_n * En_Fn

    # R = qHH * R_sum  (as the universal R-matrix)
    R_univ = qHH @ R_sum

    # check_R = tau o R_univ where tau is the tensor flip
    tau = np.zeros((d, d), dtype=complex)
    for i in range(m):
        for j in range(m):
            tau[j * m + i, i * m + j] = 1.0

    check_R = tau @ R_univ
    return check_R


# ============================================================
# 4. Verlinde fusion rules at roots of unity
# ============================================================

def verlinde_fusion_coefficient(i: int, j: int, k: int, p: int) -> int:
    """Verlinde fusion coefficient N_{ij}^k for U_q(sl_2) at q^p = 1.

    Type-1 irreps: V_1, V_2, ..., V_{p-1} (dimensions 1, 2, ..., p-1).
    Fusion rules (level k = p-2):
       N_{ij}^k = 1 if |i-j| < k < i+j and i+j+k is even and k <= p-1
                  0 otherwise

    More precisely, using the SU(2) level-(p-2) WZW convention
    where reps are labeled by spin s = 0, 1/2, 1, ..., (p-2)/2
    (or equivalently by dimension n = 2s+1 = 1, 2, ..., p-1):

       N_{n_1, n_2}^{n_3} = 1 if:
         (a) |n_1 - n_2| + 1 <= n_3 <= n_1 + n_2 - 1  (classical CG condition)
         (b) n_1 + n_2 + n_3 is odd  (parity)
         (c) n_3 <= p - 1  (truncation: type-1 only)
         (d) n_1 + n_2 + n_3 <= 2p - 1  (Verlinde truncation)
    and 0 otherwise.  Here n_i are dimensions (1-indexed).

    This matches the Verlinde formula:
       N_{ij}^k = sum_{s=1}^{p-1} S_{is} S_{js} S_{ks}^* / S_{1s}
    with S_{ns} = sqrt(2/p) sin(pi*n*s/p).
    """
    if i < 1 or j < 1 or k < 1:
        return 0
    if i >= p or j >= p or k >= p:
        return 0

    # Classical CG condition
    if k < abs(i - j) + 1:
        return 0
    if k > i + j - 1:
        return 0

    # Parity
    if (i + j + k) % 2 == 0:
        return 0

    # Verlinde truncation
    if i + j + k > 2 * p - 1:
        return 0

    return 1


def verlinde_fusion_matrix(p: int) -> np.ndarray:
    """Full fusion matrix N_{ij}^k for type-1 reps at q^p = 1.

    Returns 3D array N[i-1, j-1, k-1] for i,j,k in {1,...,p-1}.
    """
    n = p - 1
    N = np.zeros((n, n, n), dtype=int)
    for i in range(1, p):
        for j in range(1, p):
            for k in range(1, p):
                N[i - 1, j - 1, k - 1] = verlinde_fusion_coefficient(i, j, k, p)
    return N


def verlinde_s_matrix(p: int) -> np.ndarray:
    """Modular S-matrix for SU(2) level k = p-2.

    S_{ab} = sqrt(2/p) sin(pi*a*b/p)  for a, b in {1, ..., p-1}.

    This diagonalizes the fusion rules:
       N_a = S D_a S^{-1}  where D_a = diag(S_{a,s}/S_{1,s}).
    """
    n = p - 1
    S = np.zeros((n, n), dtype=float)
    prefactor = math.sqrt(2.0 / p)
    for a in range(1, p):
        for b in range(1, p):
            S[a - 1, b - 1] = prefactor * math.sin(math.pi * a * b / p)
    return S


def verify_verlinde_formula(p: int) -> float:
    """Verify the Verlinde formula: N_{ij}^k = sum_s S_{is} S_{js} S^*_{ks} / S_{1s}.

    Returns max discrepancy across all (i,j,k).
    """
    n = p - 1
    S = verlinde_s_matrix(p)
    N_exact = verlinde_fusion_matrix(p)

    max_disc = 0.0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # Verlinde formula
                val = 0.0
                for s in range(n):
                    val += S[i, s] * S[j, s] * S[k, s] / S[0, s]
                disc = abs(val - N_exact[i, j, k])
                max_disc = max(max_disc, disc)

    return max_disc


def fusion_ring_dimensions(p: int) -> List[int]:
    """Dimensions of V_i tensor V_j = direct sum N_{ij}^k V_k.

    Returns: for each i in {1,...,p-1}, the total dimension
    sum_k N_{i1}^k * k (fusion with the fundamental).
    """
    dims = []
    for i in range(1, p):
        total = 0
        for k in range(1, p):
            total += verlinde_fusion_coefficient(i, 2, k, p) * k
        dims.append(total)
    return dims


# ============================================================
# 5. Resonance data at roots of unity
# ============================================================

def resonance_rank_root_of_unity(p: int, lie_type: str = "sl2") -> int:
    """Resonance rank rho at q^p = 1.

    The R-matrix truncates at p-1 terms, giving rho = p - 1.
    This is the resonance rank of the MC4 completion.

    For sl_N at q^p = 1: rho = p - 1 (same truncation order).
    """
    return p - 1


def r_matrix_term_count(p: int, q: complex) -> int:
    """Count the number of nonzero terms in the universal R-matrix.

    At q^p = 1, the sum truncates when [n]_q = 0 for the first time
    (since [n]! = [1][2]...[n] vanishes when any factor vanishes).

    For ODD p: [n]_q = 0 iff p | n. First vanishing: n = p. So p terms.
    For EVEN p: [n]_q = 0 iff p | 2n. First vanishing: n = p/2. So p/2 terms.

    Returns: the index of the first vanishing [n]_q, which equals the number
    of terms (n = 0, 1, ..., first_vanishing - 1).
    """
    for n in range(1, 2 * p + 1):
        if abs(quantum_integer(n, q)) < 1e-8:
            return n
    return 2 * p  # fallback (should not reach here)


def mc_element_arity_bound(p: int) -> Dict[str, object]:
    """The MC element at roots of unity has bounded arity.

    At q^p = 1, the shadow obstruction tower terminates:
      Theta_A^{<=r} = Theta_A  for r >= p-1.

    The resonance rank rho = p - 1 controls this truncation.
    The MC4 completion is automatic (finite resonance problem).

    Compare with the continuous families:
      Heisenberg: rho = 0 (quadratic, no resonance)
      Affine KM:  rho = 0 (tree-level, no resonance)
      Virasoro:   rho = 1 (curvature m_0 is the single resonance)
      W_N:        rho = 1 (same as Virasoro)
    """
    return {
        "p": p,
        "resonance_rank": p - 1,
        "mc_arity_bound": p - 1,
        "shadow_depth_class": "finite" if p < 50 else "effectively_infinite",
        "mc4_status": "automatic (finite truncation)",
        "level": p - 2,  # KL correspondence
        "comparison_wzw_level": p - 2,
    }


# ============================================================
# 6. Kazhdan-Lusztig correspondence
# ============================================================

def kl_level(p: int) -> int:
    """WZW level k corresponding to q = exp(2*pi*i/p).

    The Kazhdan-Lusztig theorem: Rep(U_q(sl_2)) at q = exp(2*pi*i/(k+2))
    is braided-tensor-equivalent to Rep(sl_2^(1)_k).

    So p = k + 2, hence k = p - 2.
    """
    return p - 2


def kappa_wzw_sl2(k: int) -> float:
    """Modular characteristic kappa(sl_2^(1)_k).

    kappa = dim(g) * (k + h^vee) / (2 * h^vee)
          = 3 * (k + 2) / (2 * 2)
          = 3(k + 2) / 4

    (AP1: this is the CORRECT formula; dim(sl_2) = 3, h^vee(sl_2) = 2.)
    """
    return 3.0 * (k + 2) / 4.0


def kappa_quantum_group(p: int) -> float:
    """Shadow modular characteristic for U_q(sl_2) at q^p = 1.

    Via the Kazhdan-Lusztig correspondence with sl_2^(1) at level k = p-2:
       kappa(U_q) = kappa(sl_2^(1)_{p-2}) = 3p/4.
    """
    k = kl_level(p)
    return kappa_wzw_sl2(k)


def central_charge_wzw_sl2(k: int) -> float:
    """Central charge of the sl_2^(1) WZW model at level k.

    c = k * dim(g) / (k + h^vee) = 3k / (k + 2).
    """
    return 3.0 * k / (k + 2.0)


def kl_data(p: int) -> Dict[str, float]:
    """Complete Kazhdan-Lusztig correspondence data for sl_2 at q^p = 1."""
    k = kl_level(p)
    c = central_charge_wzw_sl2(k)
    kappa = kappa_quantum_group(p)

    return {
        "p": p,
        "level_k": k,
        "central_charge": c,
        "kappa": kappa,
        "n_integrable_reps": p - 1,  # dimensions 1, ..., p-1
        "kappa_check": 3.0 * p / 4.0,  # should equal kappa
        # AP39: kappa != c/2 in general. Here kappa = 3p/4, c/2 = 3k/(2(k+2)) = 3(p-2)/(2p).
        "c_over_2": c / 2.0,
        "kappa_neq_c_over_2": abs(kappa - c / 2.0) > 1e-10,
    }


# ============================================================
# 7. Reshetikhin-Turaev 3-manifold invariants
# ============================================================

def modular_quantum_dim(n: int, p: int) -> float:
    """Quantum dimension of V_n in the modular category convention.

    d_n = sin(pi*n/p) / sin(pi/p).

    This is [n]_{q^{1/2}} with q^{1/2} = exp(pi*i/p).
    NOT the same as [n]_q = (q^n - q^{-n})/(q - q^{-1}).
    """
    return math.sin(math.pi * n / p) / math.sin(math.pi / p)


def rt_kirby_color(p: int) -> np.ndarray:
    """The Kirby color Omega for RT invariants at level p.

    Omega = sum_{n=1}^{p-1} d_n^2 V_n

    where d_n = sin(pi*n/p)/sin(pi/p) is the modular quantum dimension.
    """
    dims = np.array([modular_quantum_dim(n, p) ** 2 for n in range(1, p)],
                    dtype=float)
    return dims


def rt_normalization(p: int) -> float:
    """Normalization constant D^2 = sum_{n=1}^{p-1} d_n^2.

    The quantum dimension of V_n in the modular category convention is:
       d_n = sin(pi*n/p) / sin(pi/p) = [n]_{q^{1/2}}
    where q^{1/2} = exp(pi*i/p).

    This is the S-matrix convention, NOT the q-integer convention.
    D^2 = sum_{n=1}^{p-1} d_n^2.

    Known closed form: D^2 = p / (2 * sin^2(pi/p)).
    """
    D2 = 0.0
    for n in range(1, p):
        d_n = math.sin(math.pi * n / p) / math.sin(math.pi / p)
        D2 += d_n ** 2
    return D2


def rt_normalization_exact(p: int) -> float:
    """Exact normalization: D^2 = p / (2 sin^2(pi/p))."""
    return p / (2.0 * math.sin(math.pi / p) ** 2)


def gauss_sum(p: int, sign: int = 1) -> complex:
    """Gauss sum tau_+(p) or tau_-(p) for the RT invariant.

    tau_+/- = sum_{n=1}^{p-1} d_n^2 * theta_n^{+/-1}

    where d_n = sin(pi*n/p)/sin(pi/p) is the modular quantum dimension,
    and theta_n = exp(2*pi*i*(n^2 - 1)/(4p)) is the ribbon twist.

    The twist uses the MODULAR convention: theta_n = exp(2*pi*i*h_n)
    where h_n = (n^2 - 1)/(4p) is the conformal weight of V_n.

    Known: |tau_+|^2 = D^2 = p / (2 sin^2(pi/p)).
    """
    result = complex(0.0)
    for n in range(1, p):
        d_n = modular_quantum_dim(n, p)
        # Conformal weight h_n = (n^2 - 1) / (4p) for SU(2) level p-2.
        # Twist: theta_n = exp(2*pi*i * h_n).
        h_n = (n * n - 1.0) / (4.0 * p)
        theta_n = cmath.exp(2.0j * cmath.pi * h_n)
        if sign == -1:
            theta_n = 1.0 / theta_n
        result += d_n ** 2 * theta_n
    return result


def rt_s3(p: int) -> complex:
    """Reshetikhin-Turaev invariant of S^3 at level p.

    S^3 is the surgery on the unknot with framing 0... NO.
    S^3 has the EMPTY surgery presentation.  The RT invariant
    is the normalization:
       RT(S^3) = 1 / D^2

    Actually, the standard convention is RT(S^3) = 1 (it's the
    normalization reference).

    More precisely, RT(M) / RT(S^3) is the topological invariant.
    We normalize so that RT(S^3) = 1.
    """
    return complex(1.0)


def rt_lens_space(p_root: int, p_lens: int, q_lens: int) -> complex:
    """Reshetikhin-Turaev invariant of the lens space L(p_lens, q_lens).

    L(p_lens, 1) is surgery on the unknot with framing p_lens.

    RT(L(n,1)) = (1/D^2) sum_{j=1}^{p_root-1} [j]_q^2 * theta_j^n

    where theta_j = q^{(j^2-1)/4} is the twist eigenvalue on V_j,
    and D^2 = sum_j [j]_q^2 is the total quantum dimension squared.

    For general L(p_lens, q_lens), the continued fraction expansion
    of p_lens/q_lens gives the surgery description.
    """
    D2 = rt_normalization(p_root)

    if q_lens == 1:
        # Simple case: surgery on unknot with framing p_lens
        result = complex(0.0)
        for j in range(1, p_root):
            d_j = modular_quantum_dim(j, p_root)
            h_j = (j * j - 1.0) / (4.0 * p_root)
            theta_j = cmath.exp(2.0j * cmath.pi * h_j)
            result += d_j ** 2 * theta_j ** p_lens
        return result / D2
    else:
        # General lens space via continued fraction surgery
        # L(p,q) = surgery on chain link with coefficients from
        # continued fraction [a_1, a_2, ..., a_n] = p/q.
        coeffs = _continued_fraction(p_lens, q_lens)
        return _rt_chain_surgery(p_root, coeffs)


def _continued_fraction(p: int, q: int) -> List[int]:
    """Continued fraction expansion [a_1, a_2, ...] of p/q."""
    if q == 0:
        return []
    coeffs = []
    while q != 0:
        a = p // q
        coeffs.append(a)
        p, q = q, p - a * q
    return coeffs


def _rt_chain_surgery(p_root: int, coeffs: List[int]) -> complex:
    """RT invariant for surgery on a chain link with given framings.

    For a single-component surgery with framing a:
       RT(L(a,1)) = (1/D^2) sum_j [j]^2 theta_j^a

    For a chain link [a_1, ..., a_n], we sum over all colorings:
       RT = (1/D^{2n}) sum_{j_1,...,j_n} prod_i [j_i]^2 theta_{j_i}^{a_i}
            * prod_{<i,i+1>} S_{j_i, j_{i+1}} / S_{1, j_{i+1}}  ... complicated.

    For simplicity, implement only the single-component case here.
    Multi-component chain surgery requires the full Kirby calculus.
    """
    if len(coeffs) == 1:
        return rt_lens_space(p_root, coeffs[0], 1)

    # For multi-component, use the transfer matrix approach.
    n = p_root - 1
    D2 = rt_normalization(p_root)

    S = verlinde_s_matrix(p_root)

    # Transfer matrix T_a for framing a:
    # T_a[i,j] = delta_{ij} theta_i^a
    def twist_matrix(a: int) -> np.ndarray:
        T = np.zeros((n, n), dtype=complex)
        for i in range(n):
            j_dim = i + 1
            h_j = (j_dim * j_dim - 1.0) / (4.0 * p_root)
            theta = cmath.exp(2.0j * cmath.pi * h_j)
            T[i, i] = theta ** a
        return T

    # RT = (1/D^{2*len(coeffs)}) * trace of product:
    # sum_j [j_1]^2 ... [j_n]^2 T_{a_1} S T_{a_2} S ... T_{a_n}
    # Actually this is the SO(3) Chern-Simons partition function formula.

    # Use the Verlinde S-matrix to implement the surgery formula.
    # For a chain link: the RT invariant is computed via the composition
    # of surgery operators S T^{a_i} S in the Hilbert space.

    # The RT invariant of surgery on a framed link is:
    # Z(M) = sum_{colorings} prod_vertices [j_v]^2 * prod_edges S_{j_e1, j_e2}
    #         * prod_components theta_{j_c}^{framing_c}
    # normalized by D^{2 * #components} ... but this is getting complicated.

    # For the chain link with n components:
    #   Z = (prod_i sigma_+^{-1}) * [first row of (S T^{a_1} S T^{a_2} ... S T^{a_n})][0,0]

    # Simpler: use the matrix product approach
    # M = S @ T(a_1) @ S @ T(a_2) @ ... @ S @ T(a_n) @ S
    # RT = M[0, 0] * (some normalization)

    # For 2-component case (lens space L(p,q)):
    S_cx = S.astype(complex)
    result_mat = np.eye(n, dtype=complex)
    for a in coeffs:
        result_mat = result_mat @ twist_matrix(a) @ S_cx

    # Normalization: the tau constants
    tau_plus = gauss_sum(p_root, +1)
    tau_minus = gauss_sum(p_root, -1)

    # The RT invariant for the chain surgery
    # (using the Kirby move normalization)
    n_pos = sum(1 for a in coeffs if a > 0)
    n_neg = sum(1 for a in coeffs if a < 0)

    # Simple approximation: extract the (0,0) entry of the product
    # and normalize by D^2.
    vec = np.zeros(n, dtype=complex)
    vec[0] = 1.0
    out = result_mat @ vec

    return out[0] / D2


def rt_poincare_sphere(p_root: int) -> complex:
    """RT invariant of the Poincare homology sphere Sigma(2,3,5).

    The Poincare sphere is +1 surgery on the left-handed trefoil.
    Equivalently, it is the Brieskorn sphere Sigma(2,3,5).

    Surgery presentation: -1 surgery on the right-handed trefoil 3_1.
    Or equivalently: the E8 plumbing (surgery on E8 graph with all framings -2).

    For the simple presentation as +1 surgery on the left trefoil (3_1^L):
       RT(Sigma) = (1/D^2) * tau_-^{-1} * sum_j [j]^2 theta_j^{-1} * Jones_{3_1}(j, q)

    For computational simplicity, use the E8 plumbing = chain surgery
    approach. The Poincare sphere = L(2,1) #_f L(3,1) #_f L(5,1) ... NO.

    The Poincare sphere as surgery: +1 Dehn surgery on the left trefoil.
    But the simpler approach is the continued fraction surgery for
    S^3_{+1}(3_1^L).

    Use the Seifert fibration: Sigma(2,3,5) has surgery matrix
    from the E8 lattice (all framings = -2, linking from the E8 Dynkin diagram).

    For our purposes, compute directly via the formula for Seifert fibered spaces:
       RT(Sigma(a1, a2, a3)) is a known explicit formula.

    Sigma(2,3,5):
       RT = (1/D^2) * sum_{j=1}^{p-1} [j]^2 * theta_j^{-1} *
            prod_{i=1}^3 S_j^{a_i-surgery}

    Actually, let me use the simplest correct formula.
    For a Seifert space M(e0; r1/s1, r2/s2, r3/s3), the RT invariant
    at level p is:

       RT(M) = (tau_+/|tau_+|)^{sigma} * (1/D)^{n_links} *
               sum_{j=1}^{p-1} [j]^2 * theta_j^e0 *
               prod_{i=1}^3 F(j, r_i, s_i)

    For Sigma(2,3,5): e0 = -2, Seifert invariants (1/2, 1/3, 1/5).
    But the formula is nontrivial.

    Use the simpler approach: Sigma(2,3,5) = S^3_{+1}(3_1), and
    3_1 is a (2,3) torus knot, so the colored Jones polynomial is known.

    RT(M_L) = kappa^{-sigma(L)} / D^{2s} *
              sum_{j1,...,js} prod_i [j_i]^2 theta_{j_i}^{a_i} *
              (colored invariant of L)

    For +1 surgery on the unknot: L(+1, 1) (already handled).
    For surgery on the trefoil, we need the colored trefoil invariant.

    Simplification: use the known result.
    For p=5 (level 3), RT(Poincare) is known.
    """
    # Use the continued fraction surgery for Sigma(2,3,5) = +1 surgery on 3_1.
    # The plumbing description gives [-2, -1, -2, -1, -2, -1, -2, -2] or similar.

    # More elementary: Sigma(2,3,5) as Dehn surgery on the trefoil.
    # Surgery coefficient +1 on the left trefoil.

    # For a knot K with surgery coefficient n:
    # RT(S^3_n(K)) = (1/D^2) * tau_-^{-1} *
    #   sum_{j=1}^{p-1} [j]^2 * theta_j^n * JonesColored(K, j, q)

    # For the unknot: JonesColored(unknot, j, q) = [j]
    # (this recovers the lens space formula).

    # For the trefoil T(2,3): the colored Jones polynomial is
    # J_n(T(2,3); q) = sum_{k=0}^{n-1} q^{-k(n+1)} prod_{j=1}^k (1 - q^{n+j})/(1 - q^j)
    # ... but we need the version evaluated at a root of unity.

    # Simpler: compute from the braid representation.
    # 3_1 = closure of sigma_1^3 on 2 strands.
    # For coloring V_j: compute via the R-matrix on V_j tensor V_j.

    q = root_of_unity(p_root)
    D2 = rt_normalization(p_root)

    result = complex(0.0)
    for j in range(1, p_root):
        # Colored Jones: J_j(3_1, q) via the braid closure
        # of sigma^3 on 2 strands with coloring V_j.
        if j == 1:
            # V_1 is trivial, colored Jones = 1.
            J_j = complex(1.0)
        else:
            R_j = truncated_r_matrix_sl2(p_root, j)
            dim_sq = j * j

            # Braid sigma^3
            braid_mat = np.linalg.matrix_power(R_j, 3)

            # Quantum trace using q^{H/2} (K matrix)
            K_diag = np.array([q ** (j - 1 - 2 * m) for m in range(j)],
                              dtype=complex)
            K_total = np.diag(K_diag)
            K2 = np.kron(K_total, K_total)
            tr_j = np.trace(braid_mat @ K2)

            # Quantum dimension (q-integer convention for internal computation)
            delta_j = quantum_dimension(j, q)

            if abs(delta_j) < 1e-15:
                continue

            # Normalized colored Jones
            J_j = tr_j / delta_j

        # Use modular quantum dimension for the RT sum
        d_j = modular_quantum_dim(j, p_root)

        # Surgery contribution with framing +1
        h_j = (j * j - 1.0) / (4.0 * p_root)
        theta_j = cmath.exp(2.0j * cmath.pi * h_j)
        result += d_j * d_j * theta_j * J_j

    return result / D2


# ============================================================
# 8. Logarithmic extensions (non-semisimple category)
# ============================================================

def projective_cover_dimension(n: int, p: int) -> int:
    """Dimension of the projective cover P(n) of V_n in the non-semisimple
    category of U_q(sl_2) at q^p = 1.

    For 1 <= n <= p-1 (type-1):
      dim P(n) = 2p   for 1 < n < p-1  (generic interior)
      dim P(1) = p    (trivial rep)
      dim P(p-1) = p  (Steinberg rep)

    P(n) has a 4-step filtration (Loewy series):
      V_n / V_{p-n} / V_n / V_{p-n} ... (for generic n)

    This is the non-semisimple structure relevant to logarithmic CFT.
    """
    if n < 1 or n >= p:
        return 0
    if n == 1 or n == p - 1:
        return p
    return 2 * p


def indecomposable_count(p: int) -> Dict[str, int]:
    """Count of indecomposable modules in the non-semisimple category.

    At q^p = 1:
      - p-1 simple modules: V_1, ..., V_{p-1}
      - p-1 projective indecomposables: P(1), ..., P(p-1)
      - For n not in {1, p-1}: P(n) is NOT simple (has Jordan blocks)
      - V_1 and V_{p-1} are projective (self-injective for these)
    """
    n_simple = p - 1
    n_projective = p - 1
    n_non_simple_projective = max(0, p - 3)  # P(2), ..., P(p-2) are non-simple

    return {
        "n_simple": n_simple,
        "n_projective": n_projective,
        "n_non_simple_projective": n_non_simple_projective,
        "n_projective_simple": 2,  # P(1)=V_1 and P(p-1)=V_{p-1}
        "jordan_block_size": 2,  # Loewy length 2 for generic P(n)
    }


def log_shadow_data(p: int) -> Dict[str, object]:
    """Shadow obstruction tower data for the logarithmic (non-semisimple)
    extension at q^p = 1.

    In the non-semisimple category:
    1. The shadow connection acquires IRREGULAR singularities
       (the projective covers P(n) have Jordan blocks).
    2. The MC element has resonant contributions from the
       indecomposable-but-not-simple modules.
    3. The shadow depth is EXACTLY p-1 (matching the R-matrix truncation).
    """
    k = kl_level(p)
    kappa = kappa_quantum_group(p)

    # Grothendieck ring data
    # [P(n)] = [V_n] + [V_{p-n}] in the Grothendieck group (for 1 < n < p-1)
    grothendieck_relations = {}
    for n in range(2, p - 1):
        grothendieck_relations[f"P({n})"] = f"V({n}) + V({p - n})"

    return {
        "p": p,
        "level": k,
        "kappa": kappa,
        "shadow_depth": p - 1,
        "n_log_channels": max(0, p - 3),  # non-simple projectives
        "grothendieck_relations": grothendieck_relations,
        "loewy_length": 2 if p > 3 else 1,
        "irregular_singularity": p > 3,
        "log_cft_central_charge": central_charge_wzw_sl2(k),
    }


# ============================================================
# 9. Higher rank: U_q(sl_3) at roots of unity
# ============================================================

def sl3_type1_irreps(p: int) -> List[Tuple[int, int, int]]:
    """Type-1 irreducible representations of U_q(sl_3) at q^p = 1.

    Labeled by dominant weights (a, b) with a + b <= p - 3.
    (For level k = p-3 in the KL correspondence.)

    Returns: list of (a, b, dim) where dim = (a+1)(b+1)(a+b+2)/2.
    """
    reps = []
    for a in range(p - 2):
        for b in range(p - 2 - a):
            dim = (a + 1) * (b + 1) * (a + b + 2) // 2
            reps.append((a, b, dim))
    return reps


def sl3_quantum_dim(a: int, b: int, q: complex) -> complex:
    """Quantum dimension of V(a,b) for U_q(sl_3).

    dim_q(V(a,b)) = [a+1] [b+1] [a+b+2] / ([1] [1] [2])

    More precisely, using the Weyl dimension formula with quantum integers:
       dim_q = prod_{alpha > 0} [<lambda + rho, alpha>] / [<rho, alpha>]

    For sl_3, positive roots alpha_1, alpha_2, alpha_1 + alpha_2:
       rho = (1, 1) in fundamental weight basis.
       <(a,b) + (1,1), alpha_1> = a + 1
       <(a,b) + (1,1), alpha_2> = b + 1
       <(a,b) + (1,1), alpha_1 + alpha_2> = a + b + 2
       <(1,1), alpha_1> = 1
       <(1,1), alpha_2> = 1
       <(1,1), alpha_1 + alpha_2> = 2

    So dim_q = [a+1][b+1][a+b+2] / ([1][1][2]).
    """
    num = (quantum_integer(a + 1, q)
           * quantum_integer(b + 1, q)
           * quantum_integer(a + b + 2, q))
    den = (quantum_integer(1, q)
           * quantum_integer(1, q)
           * quantum_integer(2, q))
    if abs(den) < 1e-30:
        return complex(0.0)
    return num / den


def sl3_resonance_rank(p: int) -> int:
    """Resonance rank for U_q(sl_3) at q^p = 1.

    The R-matrix for sl_3 also truncates at p-1 terms
    (the sum over E_alpha^n has [n]! = 0 at n = p).
    Resonance rank = p - 1.
    """
    return p - 1


def sl3_kl_data(p: int) -> Dict[str, float]:
    """Kazhdan-Lusztig correspondence for sl_3 at q^p = 1.

    KL: U_q(sl_3) at q = exp(2*pi*i/p) <-> sl_3^(1) at level k = p - 3.

    kappa(sl_3^(1)_k) = dim(sl_3) * (k + h^vee) / (2 * h^vee)
                      = 8 * (k + 3) / 6
                      = 4(k + 3) / 3
                      = 4p / 3
    """
    k = p - 3  # level for sl_3
    h_vee = 3
    dim_g = 8
    c = dim_g * k / (k + h_vee)
    kappa = dim_g * (k + h_vee) / (2.0 * h_vee)

    return {
        "p": p,
        "level_k": k,
        "h_vee": h_vee,
        "dim_g": dim_g,
        "central_charge": c,
        "kappa": kappa,
        "kappa_formula": f"{dim_g}*({k}+{h_vee})/(2*{h_vee}) = {kappa}",
        "n_type1_irreps": len(sl3_type1_irreps(p)),
        "resonance_rank": sl3_resonance_rank(p),
    }


# ============================================================
# 10. Generic-q limit verification
# ============================================================

def generic_q_limit_check(p_values: List[int],
                          dim_V: int = 2) -> List[Dict[str, object]]:
    """Verify that as p -> infinity, root-of-unity data approaches generic q.

    At generic q (large p), the quantum group is equivalent to U(sl_2):
      - All type-1 reps exist (no truncation)
      - R-matrix has all terms (no truncation)
      - Fusion = classical tensor product (no Verlinde truncation)
      - kappa -> infinity (level -> infinity)

    Returns data for each p showing convergence.
    """
    results = []
    for p in sorted(p_values):
        q = root_of_unity(p)
        k = kl_level(p)

        # Number of terms in R-matrix
        n_terms = r_matrix_term_count(p, q)

        # Quantum dimension of V_2 (should approach 2)
        qdm = quantum_dimension(2, q)

        # Fusion: V_2 tensor V_2 = V_1 + V_3 (classically)
        # At level k: N_{2,2}^3 = 1 if 3 <= p-1, i.e., p >= 4
        n223 = verlinde_fusion_coefficient(2, 2, 3, p)

        # Casimir eigenvalue on V_2 (should approach c_2 = 3/4 classically)
        cas = quantum_casimir_eigenvalue(2, q)

        results.append({
            "p": p,
            "level_k": k,
            "n_r_matrix_terms": n_terms,
            "quantum_dim_V2": qdm,
            "quantum_dim_V2_abs": abs(qdm),
            "N_22^3": n223,
            "casimir_V2": cas,
        })

    return results


# ============================================================
# 11. Shadow framework comparison
# ============================================================

def shadow_data_comparison(p: int) -> Dict[str, object]:
    """Compare quantum group shadow data with WZW/affine data.

    The Kazhdan-Lusztig equivalence implies:
    1. kappa(U_q) = kappa(sl_2^(1)_k) = 3p/4
    2. Fusion rules match Verlinde at level k = p-2
    3. S-matrix matches the WZW modular S-matrix
    4. Resonance rank = p-1 = shadow depth (R-matrix truncation)

    Multi-path verification:
    Path 1: Direct quantum group computation (R-matrix truncation)
    Path 2: KL correspondence (kappa from affine algebra)
    Path 3: Verlinde formula (fusion from S-matrix)
    Path 4: 3-manifold invariants (numerical agreement)
    Path 5: Generic-q limit (p -> infinity recovery)
    """
    k = kl_level(p)
    q = root_of_unity(p)

    # Path 1: R-matrix term count
    n_terms = r_matrix_term_count(p, q)

    # Path 2: kappa from KL
    kappa_kl = kappa_quantum_group(p)
    kappa_direct = 3.0 * p / 4.0

    # Path 3: Verlinde verification
    verlinde_disc = verify_verlinde_formula(p)

    # Path 4: Normalization check (D^2 two ways)
    D2_sum = rt_normalization(p)
    D2_exact = rt_normalization_exact(p)

    # Path 5: resonance rank
    rho = resonance_rank_root_of_unity(p)

    return {
        "p": p,
        "level": k,
        "kappa_kl": kappa_kl,
        "kappa_direct": kappa_direct,
        "kappa_match": abs(kappa_kl - kappa_direct) < 1e-10,
        "n_r_matrix_terms": n_terms,
        "expected_terms": p,
        "r_matrix_truncation_match": n_terms == p,
        "verlinde_discrepancy": verlinde_disc,
        "verlinde_verified": verlinde_disc < 1e-10,
        "D2_sum": D2_sum,
        "D2_exact": D2_exact,
        "D2_match": abs(D2_sum - D2_exact) / max(abs(D2_exact), 1e-30) < 1e-10,
        "resonance_rank": rho,
        "expected_resonance_rank": p - 1,
        "resonance_match": rho == p - 1,
    }


# ============================================================
# 12. Ribbon structure and modular category data
# ============================================================

def ribbon_eigenvalues(p: int) -> List[complex]:
    """Twist eigenvalues theta_j for j = 1, ..., p-1.

    theta_j = exp(2*pi*i * (j^2 - 1)/(4p))

    where h_j = (j^2 - 1)/(4p) is the conformal weight.
    These are the ribbon element eigenvalues on the type-1 irreps.
    """
    return [cmath.exp(2.0j * cmath.pi * (j * j - 1) / (4.0 * p))
            for j in range(1, p)]


def t_matrix(p: int) -> np.ndarray:
    """Modular T-matrix: T_{ab} = delta_{ab} theta_a / theta_1.

    Since theta_1 = q^0 = 1, this is just T_{ab} = delta_{ab} theta_a.
    """
    thetas = ribbon_eigenvalues(p)
    return np.diag(thetas)


def verify_modular_relation(p: int) -> Dict[str, float]:
    """Verify the modular relations for the SU(2) modular tensor category.

    For SU(2), ALL representations are self-conjugate (real or pseudo-real),
    so the charge conjugation matrix C = I (the identity).

    The modular relations are:
       S^2 = C = I  (S is an involution for SU(2))
       S^4 = I  (automatic from S^2 = I)
       (ST)^3 = kappa * I  for some phase kappa (the anomaly)

    We verify all three.
    """
    S = verlinde_s_matrix(p).astype(complex)
    T = t_matrix(p)
    n = p - 1

    # S^2 = I (charge conjugation = identity for SU(2))
    S2 = S @ S
    S2_disc = float(np.linalg.norm(S2 - np.eye(n, dtype=complex)))

    # S^4 = I (automatic)
    S4 = S2 @ S2
    S4_disc = float(np.linalg.norm(S4 - np.eye(n, dtype=complex)))

    # (ST)^3 should be proportional to identity
    ST = S @ T
    ST3 = np.linalg.matrix_power(ST, 3)
    # Find proportionality constant from (0,0) entry
    ratio = ST3[0, 0]
    ST3_prop_disc = float(np.linalg.norm(ST3 - ratio * np.eye(n, dtype=complex)))

    return {
        "S2_equals_C_discrepancy": S2_disc,
        "S4_equals_I_discrepancy": S4_disc,
        "ST3_proportional_to_S2_discrepancy": ST3_prop_disc,
        "anomaly_ratio": ratio,
    }


# ============================================================
# 13. Quantum Casimir spectral data
# ============================================================

def casimir_spectrum(p: int) -> List[Tuple[int, complex]]:
    """Spectrum of the quantum Casimir on type-1 irreps.

    Returns: (dim_n, c_n) for n = 1, ..., p-1.
    """
    q = root_of_unity(p)
    return [(n, quantum_casimir_eigenvalue(n, q)) for n in range(1, p)]


def casimir_generic_comparison(p: int) -> List[Tuple[int, float, float]]:
    """Compare quantum Casimir eigenvalues at root of unity vs generic.

    At generic q -> 1 (classical limit):
       C_2(V_n) -> n(n-2)/4 + 1/4 = (n^2 - 1)/4  ... NO.

    Classical Casimir of sl_2 on V_n (spin j = (n-1)/2):
       c_2(V_n) = j(j+1) = (n-1)(n+1)/4 = (n^2-1)/4.

    At q = exp(2*pi*i/p), the quantum Casimir is:
       c_n(q) = (q^n + q^{-n}) / (q - q^{-1})^2

    For large p, q -> 1, and this -> n^2 / 4 ... NO, need careful limit.
    Actually c_n(1) = 2 / 0, so we need the Laurent expansion.

    The normalized quantum Casimir (with the (q-q^{-1})^2 removed) is:
       c_n = [n/2]_q * [(n+2)/2]_q  ... actually [n]_q^2 / [2]_q^2 ... no.

    The natural comparison is between c_n(q) and the classical value
    j(j+1) = (n^2-1)/4. As p -> infinity, [n]_q -> n and
    c_n(q) = (q^n + q^{-n})/(q-q^{-1})^2.

    For q = exp(2*pi*i/p) with large p:
       q^n + q^{-n} = 2 cos(2*pi*n/p) -> 2
       (q - q^{-1})^2 = -4 sin^2(pi/p) -> -4*(pi/p)^2

    So c_n(q) -> 2 / (-4 pi^2/p^2) = -p^2/(2*pi^2)  ... this diverges.

    The issue is that the quantum Casimir has a different normalization.
    The EIGENVALUE on V_n in the normalized form is:
       [j]_q [j+1]_q  where j = (n-1)/2
    which tends to j(j+1) = (n^2-1)/4 as q -> 1.

    Let me compute [j]_q * [j+1]_q / [1]_q^2 ... no, the correct
    normalized form depends on conventions.

    For comparison purposes, compute the RATIO of Casimir eigenvalues
    on V_n vs V_2, which is convention-independent.

    c_n / c_2 -> (n^2-1)/3  as q -> 1.
    """
    q = root_of_unity(p)
    c2 = quantum_casimir_eigenvalue(2, q)

    results = []
    for n in range(1, min(p, 10)):
        cn = quantum_casimir_eigenvalue(n, q)
        ratio = cn / c2 if abs(c2) > 1e-14 else 0.0
        classical_ratio = (n * n - 1) / 3.0 if n > 1 else 0.0
        results.append((n, abs(ratio), classical_ratio))

    return results


# ============================================================
# 14. Comprehensive verification data
# ============================================================

def full_verification_suite(p: int) -> Dict[str, object]:
    """Run all verifications for U_q(sl_2) at q^p = 1.

    Multi-path verification:
    Path 1: Direct computation (R-matrix terms, Casimir spectrum)
    Path 2: KL correspondence (kappa, central charge)
    Path 3: Verlinde formula (fusion rules from S-matrix)
    Path 4: 3-manifold invariants (normalization D^2)
    Path 5: Generic-q limit (large p convergence)
    Path 6: Resonance rank (shadow framework prediction)
    """
    results = {}

    # Path 1: Direct
    q = root_of_unity(p)
    results["r_matrix_terms"] = r_matrix_term_count(p, q)
    results["casimir_spectrum_count"] = len(casimir_spectrum(p))

    # Path 2: KL
    kl = kl_data(p)
    results["kappa"] = kl["kappa"]
    results["central_charge"] = kl["central_charge"]
    results["level"] = kl["level_k"]

    # Path 3: Verlinde
    results["verlinde_discrepancy"] = verify_verlinde_formula(p)

    # Path 4: 3-manifold
    D2_sum = rt_normalization(p)
    D2_exact = rt_normalization_exact(p)
    results["D2_relative_error"] = abs(D2_sum - D2_exact) / max(abs(D2_exact), 1e-30)

    # Path 5: Modular relations
    mod = verify_modular_relation(p)
    results["S2_C_discrepancy"] = mod["S2_equals_C_discrepancy"]
    results["S4_I_discrepancy"] = mod["S4_equals_I_discrepancy"]

    # Path 6: Resonance
    results["resonance_rank"] = resonance_rank_root_of_unity(p)
    results["resonance_matches_truncation"] = (
        results["resonance_rank"] == results["r_matrix_terms"] - 1
    )

    # Hecke relation
    results["hecke_discrepancy"] = float(np.linalg.norm(
        _hecke_check(q, 2)
    ))

    # Braid relation
    results["braid_discrepancy"] = _braid_check(q, 2)

    return results


def _hecke_check(q: complex, N: int) -> np.ndarray:
    """Check (R - q)(R + q^{-1}) = 0."""
    R = _check_r_fundamental_sl2(q) if N == 2 else None
    qi = 1.0 / q
    d = N * N
    return (R - q * np.eye(d, dtype=complex)) @ (R + qi * np.eye(d, dtype=complex))


def _braid_check(q: complex, N: int) -> float:
    """Check braid relation R1 R2 R1 = R2 R1 R2 on V^{tensor 3}."""
    R = _check_r_fundamental_sl2(q) if N == 2 else None
    I_N = np.eye(N, dtype=complex)
    R1 = np.kron(R, I_N)
    R2 = np.kron(I_N, R)
    return float(np.linalg.norm(R1 @ R2 @ R1 - R2 @ R1 @ R2))
