"""Modular tangent complex: L-infinity twisted differential d_{Theta_A}.

The modular tangent complex L_A is the cyclic deformation complex Def_cyc(A)
equipped with the twisted differential d_{Theta_A}. It governs infinitesimal
deformations of A as a chiral algebra.

STRUCTURE:
  The strict model is a dg Lie algebra (Def_cyc(A), d + [Theta_A, -]).
  The full L-infinity model uses higher brackets ell_k with k >= 3.

  For Koszul algebras (shadow depth finite), the twist terminates:
    d_{Theta_A} = d + [Theta_A^{<=r_max}, -]

  For infinite shadow depth (class M, e.g., Virasoro at generic c), the full tower contributes.
  Note: Virasoro IS chirally Koszul; shadow depth classifies complexity within the Koszul world.

COMPUTATIONAL APPROACH:
  At the level of the CE complex C*(g, g) = Hom(Lambda^* g, g):
  - C^0 = g (dim d) -- the Lie algebra itself (inner derivations)
  - C^1 = Hom(g, g) (dim d^2) -- endomorphisms / deformations
  - C^2 = Hom(Lambda^2 g, g) (dim d * C(d,2)) -- obstructions
  - C^3 = Hom(Lambda^3 g, g) (dim d * C(d,3)) -- higher obstructions

  The Lie bracket mu in C^1(g,g) is itself an MC element: d_CE(mu) + (1/2)[mu,mu]_NR = 0
  is the Jacobi identity. The twisted differential d_mu is the standard CE differential.

  The modular tangent complex adds the shadow tower data:
  - Theta_A^{<=2} = kappa(A) * eta (Killing cocycle, kappa = dim(g)(k+h^v)/(2h^v))
  - Theta_A^{<=3} = kappa*eta + C_3 (cubic shadow)
  - Theta_A^{<=4} = kappa*eta + C_3 + Q_4 (quartic shadow)

MATHEMATICAL IDENTIFICATIONS:
  For V_k(g) (universal affine vertex algebra at level k):
  - The CE complex C*(g, g) is the genus-0, critical-level specialization
    of the chiral deformation complex
  - The kappa-twist d_{kappa*eta} has (d_{kappa*eta})^2 proportional to kappa,
    giving the genus-1 curvature
  - H^0(L_A) = center of g (= 0 for semisimple g)
  - H^1(L_A) = infinitesimal deformations modulo gauge
  - H^2(L_A) = obstructions to extending deformations

CONVENTIONS:
  - Cohomological grading, |d| = +1
  - Nijenhuis-Richardson bracket on C*(g, g)
  - Structure constants: [e_i, e_j] = c^k_{ij} e_k
  - Killing form: kap(e_i, e_j) = kap_{ij}
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from typing import Dict, List, Optional, Tuple

import numpy as np

from compute.lib.mc2_cyclic_ce import (
    _exact_rank,
    _null_space,
    ce_cohomology,
    ce_differential_0,
    ce_differential_1,
    ce_differential_2,
    ce_adjoint_differential,
    ce_exterior_differential,
    cyclic_ce_cohomology,
    sl2_structure_constants,
    sl2_killing_form,
    sl3_structure_constants,
    sl3_killing_form,
)


# ---------------------------------------------------------------------------
# Exact linear algebra helpers
# ---------------------------------------------------------------------------

def _frac(x) -> Fraction:
    """Coerce to Fraction."""
    if isinstance(x, Fraction):
        return x
    return Fraction(x)


def _np_zeros(rows: int, cols: int) -> np.ndarray:
    """Create a zero matrix of Fractions."""
    M = np.zeros((rows, cols), dtype=object)
    for i in range(rows):
        for j in range(cols):
            M[i, j] = Fraction(0)
    return M


def _mat_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Exact matrix multiplication over Fraction."""
    m, n = A.shape
    n2, p = B.shape
    assert n == n2, f"Incompatible shapes: {A.shape} x {B.shape}"
    C = _np_zeros(m, p)
    for i in range(m):
        for j in range(p):
            s = Fraction(0)
            for k in range(n):
                s += _frac(A[i, k]) * _frac(B[k, j])
            C[i, j] = s
    return C


def _mat_add(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Exact matrix addition over Fraction."""
    assert A.shape == B.shape
    C = _np_zeros(*A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i, j] = _frac(A[i, j]) + _frac(B[i, j])
    return C


def _mat_scale(c: Fraction, A: np.ndarray) -> np.ndarray:
    """Scale matrix by a Fraction."""
    B = _np_zeros(*A.shape)
    c = _frac(c)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[i, j] = c * _frac(A[i, j])
    return B


def _is_zero_matrix(M: np.ndarray) -> bool:
    """Check if a matrix is identically zero."""
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i, j] != 0:
                return False
    return True


# ---------------------------------------------------------------------------
# Wedge indexing helpers
# ---------------------------------------------------------------------------

def _sorted_tuples(dim: int, degree: int) -> List[Tuple[int, ...]]:
    """Sorted tuples (i_1, ..., i_degree) with 0 <= i_1 < ... < i_degree < dim."""
    return list(combinations(range(dim), degree))


def _wedge_pairs(dim: int) -> List[Tuple[int, int]]:
    """Ordered pairs (i,j) with i < j for Lambda^2."""
    return [(i, j) for i in range(dim) for j in range(i + 1, dim)]


# ---------------------------------------------------------------------------
# Nijenhuis-Richardson bracket on C*(g, g)
# ---------------------------------------------------------------------------

def nijenhuis_richardson_bracket(
    f_vec: np.ndarray,
    f_degree: int,
    g_vec: np.ndarray,
    g_degree: int,
    dim: int,
    sc: np.ndarray,
) -> np.ndarray:
    """Compute [f, g]_NR for f in C^p(g,g), g in C^q(g,g).

    The Nijenhuis-Richardson bracket [f,g]_NR in C^{p+q}(g,g) is defined by:

    [f,g]_NR(x_1,...,x_{p+q}) =
      sum_{sigma in Sh(q,p)} sgn(sigma) f(g(x_{sigma(1)},...,x_{sigma(q)}),
                                           x_{sigma(q+1)},...,x_{sigma(p+q)})
      - (-1)^{pq} sum_{sigma in Sh(p,q)} sgn(sigma) g(f(x_{sigma(1)},...,x_{sigma(p)}),
                                                        x_{sigma(p+1)},...,x_{sigma(p+q)})

    For the special case p=1, q=1 (both in C^1 = Hom(g,g)):
    [f,g]_NR(x) = f(g(x)) - g(f(x))   (commutator of endomorphisms)

    For p=1, q=0 (f in C^1, g = v in C^0 = g):
    [f,v]_NR(x) = f(v) is not standard; we use the bracket below for MC twist.

    We implement only the cases needed for the tangent complex computations.
    """
    p, q = f_degree, g_degree
    result_degree = p + q

    if result_degree < 0:
        return np.array([], dtype=object)

    # Case p=1, q=1: [f,g] in C^2 is the commutator bracket
    if p == 1 and q == 1:
        # f, g: Hom(g, g), both dim*dim vectors
        # [f,g](x) = f(g(x)) - g(f(x))
        # Represent as dim x dim matrices
        f_mat = np.reshape(f_vec[:dim * dim].copy(), (dim, dim))  # f_mat[k,j] = f_kj
        g_mat = np.reshape(g_vec[:dim * dim].copy(), (dim, dim))
        fg = _mat_multiply(f_mat, g_mat)
        gf = _mat_multiply(g_mat, f_mat)
        result_mat = _mat_add(fg, _mat_scale(Fraction(-1), gf))
        return result_mat.reshape(-1)

    raise NotImplementedError(
        f"NR bracket for (p={p}, q={q}) not yet implemented"
    )


# ---------------------------------------------------------------------------
# Killing cocycle (the arity-2 shadow generator)
# ---------------------------------------------------------------------------

def killing_cocycle(sc: np.ndarray, kap: np.ndarray, dim: int) -> np.ndarray:
    """The Killing 3-cocycle phi(a,b,c) = kap([a,b], c) as an element of C^2_cyc(g,g).

    Returns a vector in C^2(g,g) = Hom(Lambda^2 g, g) representation.
    phi is the CE representative of the generator of H^2_cyc(g,g) = C.

    As an element of Hom(Lambda^2 g, g):
      phi(e_a, e_b) = sum_k c^k_{ab} * sum_m kap^{km} * ... NO.

    Actually, the Killing 3-form phi(a,b,c) = kap([a,b], c) = sum_k c^k_{ab} kap_{kc}
    is a 3-form, i.e., an element of Lambda^3(g*).

    To get an element of C^2(g,g) = Hom(Lambda^2 g, g), we use the Killing form
    to lower an index: phi_vec(a,b) = sum_k c^k_{ab} * sum_m kap^{mk} * e_m
    where kap^{mk} is the inverse Killing form.

    Actually, phi as a cyclic 2-cochain means:
      phi in C^2_cyc(g,g) iff kap(phi(a,b), d) = kap([a,b], d) is totally skew.
    So phi(a,b) = [a,b] works directly: kap([a,b], d) is the Killing 3-form.

    phi(e_a, e_b) = [e_a, e_b] = sum_k c^k_{ab} e_k.
    """
    pairs = _wedge_pairs(dim)
    n_pairs = len(pairs)
    vec = _np_zeros(dim * n_pairs, 1).reshape(-1)
    for p_idx, (a, b) in enumerate(pairs):
        for k in range(dim):
            if sc[a, b, k] != 0:
                vec[k * n_pairs + p_idx] = _frac(sc[a, b, k])
    return vec


def killing_3form_value(sc: np.ndarray, kap: np.ndarray, dim: int) -> Fraction:
    """Evaluate kap([e_0, e_1], e_2) for the first triple."""
    val = Fraction(0)
    for k in range(dim):
        if sc[0, 1, k] != 0:
            val += _frac(sc[0, 1, k]) * _frac(kap[k, 2])
    return val


# ---------------------------------------------------------------------------
# CyclicDeformationComplex
# ---------------------------------------------------------------------------

@dataclass
class CyclicDeformationComplex:
    """The CE complex C*(g, g) with adjoint coefficients for a Lie algebra g.

    Provides:
      - Degree dimensions
      - CE differentials d: C^n -> C^{n+1}
      - Cohomology H^*(g, g)
      - The cyclic subcomplex C*_cyc(g, g) via the Killing form
      - Cyclic cohomology H*_cyc(g, g) = H^{*+1}(g)
    """

    dim: int
    sc: np.ndarray   # structure constants c[i,j,k]
    kap: np.ndarray  # Killing form kap[i,j]

    def degree_dim(self, n: int) -> int:
        """Dimension of C^n(g, g) = Hom(Lambda^n g, g)."""
        if n < 0 or n > self.dim:
            return 0
        return self.dim * comb(self.dim, n)

    def differential(self, n: int) -> np.ndarray:
        """Matrix of d: C^n -> C^{n+1} in the CE complex with adjoint coefficients."""
        if n < 0:
            return _np_zeros(self.degree_dim(0), 0)
        if n == 0:
            return ce_differential_0(self.sc, self.dim)
        if n == 1:
            return ce_differential_1(self.sc, self.dim)
        if n == 2:
            return ce_differential_2(self.sc, self.dim)
        return ce_adjoint_differential(self.sc, self.dim, n)

    def verify_d_squared(self, n: int) -> bool:
        """Check d^{n+1} o d^n = 0."""
        d_low = self.differential(n)
        d_high = self.differential(n + 1)
        product = _mat_multiply(d_high, d_low)
        return _is_zero_matrix(product)

    def cohomology_dims(self) -> Dict[int, int]:
        """Compute dim H^n(g, g) for n = 0, 1, 2, 3."""
        return ce_cohomology(self.sc, self.dim)

    def cyclic_cohomology(self) -> Dict[str, object]:
        """Compute cyclic CE cohomology H^n_cyc(g, g).

        Uses the identification H^n_cyc(g,g) = H^{n+1}(g) (CE with trivial
        coefficients, degree shifted by 1).
        """
        return cyclic_ce_cohomology(self.sc, self.kap, self.dim)

    def killing_cocycle(self) -> np.ndarray:
        """The Killing cocycle [a,b] as an element of C^2(g,g)."""
        return killing_cocycle(self.sc, self.kap, self.dim)


def sl2_deformation_complex() -> CyclicDeformationComplex:
    """The cyclic deformation complex for sl_2."""
    return CyclicDeformationComplex(
        dim=3,
        sc=sl2_structure_constants(),
        kap=sl2_killing_form(),
    )


def sl3_deformation_complex() -> CyclicDeformationComplex:
    """The cyclic deformation complex for sl_3."""
    return CyclicDeformationComplex(
        dim=8,
        sc=sl3_structure_constants(),
        kap=sl3_killing_form(),
    )


# ---------------------------------------------------------------------------
# NOTE on Theta in C^1(g,g) vs C^2(g,g) and the NR Lie algebra
# ---------------------------------------------------------------------------
#
# The NR bracket on C*(g,g) = Hom(Lambda^* g, g) has degree -1:
#   [-,-]_NR: C^p x C^q -> C^{p+q-1}
#
# The Lie bracket mu in C^1(g,g) (taking 1 argument) is NOT an MC element
# of the shifted NR Lie algebra; it is the structure that defines d_CE.
# The CE differential d_CE encodes mu; the NR bracket [mu, mu]_NR = 0
# is the Jacobi identity.
#
# MC elements of the SHIFTED NR Lie algebra C*(g,g)[1] live in C^2(g,g).
# The Killing cocycle eta in C^2(g,g) is such an MC candidate.
# Since eta = mu (as computed: eta(a,b) = [a,b]), and [mu,mu]_NR = 0 (Jacobi),
# eta is automatically MC. The twisted differential d_CE + kappa*[eta,-]
# has d^2 = 0 for all kappa.
#
# Genus-1 curvature arises in the CHIRAL deformation complex, which is
# infinite-dimensional and carries the OPE/sewing data beyond the Lie bracket.
# The KillingTwistedDifferential class below computes at the CE level.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Killing cocycle bracket [eta, -] on C*(g, g)
# ---------------------------------------------------------------------------

def _killing_bracket_matrix(
    eta_vec: np.ndarray,
    sc: np.ndarray,
    kap: np.ndarray,
    dim: int,
    n: int,
) -> np.ndarray:
    """Matrix of [eta, -]_NR: C^n(g,g) -> C^{n+1}(g,g) for eta in C^2(g,g).

    The NR bracket [eta, x]_NR for eta in C^2, x in C^n gives an element of C^{n+1}.

    For the specific eta = killing cocycle where eta(e_a, e_b) = [e_a, e_b]:
    [eta, x]_NR is computed by the standard NR formula.

    For eta in C^2 (takes 2 arguments), x in C^n (takes n arguments):
    [eta, x]_NR takes n+1 arguments and is given by:

    [eta, x]_NR(v_0,...,v_n) =
      sum_{i<j} (-1)^{i+j} eta(x(v_0,...,hat{i},...,hat{j},...,v_n), v_i, v_j)  [wrong degree]

    Actually, the correct NR bracket for multilinear maps:
    For f in Hom(V^{otimes p}, V), g in Hom(V^{otimes q}, V):
    [f,g]_NR = f circ g - (-1)^{(p-1)(q-1)} g circ f

    where (f circ g)(v_1,...,v_{p+q-1}) =
      sum_{i=1}^p (-1)^{(i-1)(q-1)} f(v_1,...,v_{i-1}, g(v_i,...,v_{i+q-1}), v_{i+q},...,v_{p+q-1})

    For eta (p=2), x (q=n): [eta, x]_NR = eta circ x - (-1)^{n-1} x circ eta.

    (eta circ x)(v_1,...,v_{n+1}) =
      x(v_2,...,v_{n+1}) inserted into eta's 1st slot: eta(x(v_2,...,v_{n+1}), v_1) * (-1)^0
      + x(v_1, v_3,...,v_{n+1}) inserted into eta's 2nd slot:
        eta(v_1, x(v_2,...)) * ... too complicated.

    For ANTISYMMETRIC maps on g (Lie algebra cochains):
    (eta circ x)(v_0,...,v_n) = sum_{sigma} sgn(sigma) eta(x(v_{sigma(0)},...,v_{sigma(n-1)}), v_{sigma(n)})

    where we sum over (n, 1)-unshuffles. This means: choose which v goes into eta's second slot.

    (eta circ x)(v_0,...,v_n) = sum_{j=0}^{n} (-1)^{n-j} eta(x(v_0,...,hat{j},...,v_n), v_j)

    And (x circ eta) picks 2 consecutive and replaces them by eta's output:
    (x circ eta)(v_0,...,v_n) = sum_{i<j} (-1)^{?} x(v_0,...,hat{i},...,hat{j},..., eta(v_i, v_j),...)

    For Lie algebra cochains (antisymmetric), the formula simplifies.

    Let me implement this directly for small n via explicit evaluation.
    """
    pairs = _wedge_pairs(dim)
    n_pairs = len(pairs)
    pairs_idx = {p: i for i, p in enumerate(pairs)}

    # Parse eta: eta_vec represents eta in C^2(g,g) = Hom(Lambda^2 g, g)
    # eta_vec[m * n_pairs + p] = coefficient of e_m when eta(e_a, e_b) is evaluated
    # for p = pairs_idx[(a,b)].
    def eval_eta(a: int, b: int) -> Dict[int, Fraction]:
        """Evaluate eta(e_a, e_b) as a vector in g."""
        if a == b:
            return {}
        if a < b:
            p = pairs_idx[(a, b)]
            sgn = Fraction(1)
        else:
            p = pairs_idx[(b, a)]
            sgn = Fraction(-1)
        result = {}
        for m in range(dim):
            val = sgn * _frac(eta_vec[m * n_pairs + p])
            if val != 0:
                result[m] = val
        return result

    if n == 0:
        # [eta, v] for v in C^0 = g, result in C^1 = Hom(g,g)
        # [eta, v]_NR = eta circ v - (-1)^{0} v circ eta
        # eta circ v: not well-defined (v takes 0 arguments, eta needs to insert output)
        # v circ eta: eta(v_0, v_1) then apply... v takes 0 arguments.
        #
        # For p=2, q=0: [C^2, C^0]_NR -> C^1.
        # (eta circ v)(w) = eta(v, w) -- eta takes the 0-arg output of "v" plus w.
        # Actually v in C^0 = g is just a vector. The NR bracket with a degree-0 element:
        # For f in C^p, v in C^0 = g: [f, v]_NR(w_1,...,w_p) = -sum_i f(w_1,...,[w_i, v],...,w_p)
        #   (the infinitesimal gauge action of v on f).
        #
        # Hmm, this is the standard formula for the dg Lie algebra action.
        #
        # For eta in C^2, v in C^0:
        # [eta, v]_NR(w) = ??? This should be in C^1.
        #
        # Using the explicit NR formula for antisymmetric cochains:
        # [f, g]_NR for f in C^p, g in C^q, result in C^{p+q-1}:
        # For p=2, q=0: result in C^1.
        # [eta, v]_NR(w) = eta(v, w) - (-1)^{1*(-1)} ...
        #
        # The standard convention: for v in C^0 = g identified with inner derivations,
        # [eta, v](w) = -eta(v, w) + [sum over insertions].
        #
        # Let me use the EXPLICIT formula. For the dg Lie algebra (C*(g,g)[1], [-,-]):
        # MC elements are in degree 1 of the shifted complex = C^2(g,g).
        # For eta in C^2(g,g) and v in C^0(g,g) = g:
        # [eta, v]_NR in C^1(g,g) = Hom(g,g).
        # [eta, v](w) = eta(v, w)  (the composition formula for NR bracket).
        #
        # This is the correct formula: [eta, v](w) = eta(v, w).

        mat = _np_zeros(dim * dim, dim)
        for vi in range(dim):  # basis e_{vi} in C^0
            for j in range(dim):  # argument e_j of the result in C^1
                eta_val = eval_eta(vi, j)
                for m, coeff in eta_val.items():
                    mat[m * dim + j, vi] += coeff
        return mat

    if n == 1:
        # Nijenhuis-Richardson bracket [eta, f]_NR for |eta|=2, |f|=1:
        # (eta circ f)(a, b) = eta(f(a), b) + eta(a, f(b))
        # (f circ eta)(a, b) = f(eta(a, b))
        # [eta, f]_NR(a, b) = eta(f(a), b) + eta(a, f(b)) - f(eta(a, b))

        mat = _np_zeros(dim * n_pairs, dim * dim)
        for f_k in range(dim):
            for f_j in range(dim):
                f_idx = f_k * dim + f_j  # basis: e_j -> e_k (f(e_j) = e_k)
                # [eta, (e_j -> e_k)](e_a, e_b) for each (a,b) pair
                for p_idx, (a, b) in enumerate(pairs):
                    result_vec = {}

                    # Term 1: eta(f(e_a), e_b)
                    # f(e_a) = delta_{a,j} * e_k
                    if a == f_j:
                        eta_val = eval_eta(f_k, b)
                        for m, c in eta_val.items():
                            result_vec[m] = result_vec.get(m, Fraction(0)) + c

                    # Term 2: eta(e_a, f(e_b))
                    # f(e_b) = delta_{b,j} * e_k
                    if b == f_j:
                        eta_val = eval_eta(a, f_k)
                        for m, c in eta_val.items():
                            result_vec[m] = result_vec.get(m, Fraction(0)) + c

                    # Term 3: -f(eta(e_a, e_b))
                    # eta(e_a, e_b) = sum_l eta_l e_l
                    # f(sum_l eta_l e_l) = sum_l eta_l delta_{l,j} e_k = eta_j * e_k
                    eta_val = eval_eta(a, b)
                    if f_j in eta_val:
                        result_vec[f_k] = result_vec.get(f_k, Fraction(0)) - eta_val[f_j]

                    for m, c in result_vec.items():
                        if c != 0:
                            mat[m * n_pairs + p_idx, f_idx] += c
        return mat

    if n == 2:
        # [eta, g] for eta in C^2, g in C^2 -> result in C^3 = Hom(Lambda^3 g, g)
        triples = _sorted_tuples(dim, 3)
        n_triples = len(triples)

        mat = _np_zeros(dim * n_triples, dim * n_pairs)
        for g_m in range(dim):
            for g_p_idx in range(n_pairs):
                g_idx = g_m * n_pairs + g_p_idx  # basis: (e_a, e_b) -> e_m
                (ga, gb) = pairs[g_p_idx]
                # g is the map: (e_a, e_b) -> e_m (antisymmetric)

                for t_idx, (x, y, z) in enumerate(triples):
                    result_vec = {}

                    # [eta, g]_NR = eta circ g - g circ eta
                    #
                    # (eta circ g)(x,y,z): eta has 2 slots, g has 2 slots.
                    # eta circ g inserts g's output into each of eta's 2 slots:
                    # sum over ways to choose 2 of (x,y,z) for g, remaining 1 for eta.
                    # = eta(g(x,y), z) - eta(g(x,z), y) + eta(g(y,z), x)
                    #   [signs from antisymmetry/shuffle]
                    #
                    # Actually, the explicit formula for (eta circ g)(v_0, v_1, v_2):
                    # = sum over (2,1)-shuffles sigma of Lambda^3:
                    #   sgn(sigma) eta(g(v_{sigma(0)}, v_{sigma(1)}), v_{sigma(2)})
                    # (2,1)-shuffles of {0,1,2}: choose 2 for g, 1 for eta's other slot.
                    # {(0,1),2} sgn=+1: eta(g(x,y), z)
                    # {(0,2),1} sgn=-1: -eta(g(x,z), y)
                    # {(1,2),0} sgn=+1: eta(g(y,z), x)

                    def eval_g(a: int, b: int) -> Dict[int, Fraction]:
                        if a == b:
                            return {}
                        if a < b:
                            p = pairs_idx.get((a, b))
                            if p is None:
                                return {}
                            sgn = Fraction(1)
                        else:
                            p = pairs_idx.get((b, a))
                            if p is None:
                                return {}
                            sgn = Fraction(-1)
                        # g basis element maps (e_{ga}, e_{gb}) -> e_{g_m}
                        # eval_g for the SPECIFIC basis element:
                        if (a < b and (a, b) == (ga, gb)) or (a > b and (b, a) == (ga, gb)):
                            return {g_m: sgn if a < b else -sgn}
                        if (a < b and (a, b) != (ga, gb)):
                            return {}
                        return {}

                    # Evaluate g on basis: g(e_a, e_b) = sgn * delta_{(min,max),(ga,gb)} * e_{g_m}
                    def _g_eval(a: int, b: int) -> Dict[int, Fraction]:
                        if a == b:
                            return {}
                        aa, bb = (a, b) if a < b else (b, a)
                        sgn = Fraction(1) if a < b else Fraction(-1)
                        if (aa, bb) == (ga, gb):
                            return {g_m: sgn}
                        return {}

                    # eta circ g terms
                    for (i, j, k), sign in [((x, y, z), Fraction(1)),
                                             ((x, z, y), Fraction(-1)),
                                             ((y, z, x), Fraction(1))]:
                        gv = _g_eval(i, j)
                        for l, c in gv.items():
                            eta_val = eval_eta(l, k)
                            for m, ec in eta_val.items():
                                result_vec[m] = result_vec.get(m, Fraction(0)) + sign * c * ec

                    # (g circ eta)(v_0, v_1, v_2):
                    # = sum over (1,2)-shuffles: choose 2 for eta, 1 for g's other slot.
                    # g has 2 slots; insert eta's output into one of g's 2 slots,
                    # with the remaining argument in g's other slot.
                    #
                    # (g circ eta)(x,y,z) =
                    #   g(eta(x,y), z) - g(eta(x,z), y) + g(eta(y,z), x)
                    #   [same shuffle structure]

                    for (i, j, k), sign in [((x, y, z), Fraction(1)),
                                             ((x, z, y), Fraction(-1)),
                                             ((y, z, x), Fraction(1))]:
                        eta_val = eval_eta(i, j)
                        for l, c in eta_val.items():
                            gv = _g_eval(l, k)
                            for m, gc in gv.items():
                                result_vec[m] = result_vec.get(m, Fraction(0)) - sign * c * gc

                    for m, c in result_vec.items():
                        if c != 0:
                            mat[m * n_triples + t_idx, g_idx] += c
        return mat

    raise NotImplementedError(f"Killing bracket for n={n} not implemented")


# ---------------------------------------------------------------------------
# Killing-twisted differential
# ---------------------------------------------------------------------------

@dataclass
class KillingTwistedDifferential:
    """The differential d_CE + kappa * [eta, -] on C*(g, g).

    Here eta is the Killing cocycle eta(a,b) = [a,b] in C^2(g,g), identified
    with the Lie bracket mu. The kappa parameter is the modular characteristic.

    KEY MATHEMATICAL FACT: Since eta = mu (the Lie bracket), the NR bracket
    [eta, eta]_NR = [mu, mu]_NR = 0 is precisely the Jacobi identity.
    Therefore (d_CE + kappa*[eta,-])^2 = 0 for ALL values of kappa.

    This means the kappa-twisted CE complex is ALWAYS exact as a chain complex.
    It represents rescaling the Lie bracket mu -> (1 + kappa)*mu, which
    preserves the Jacobi identity.

    The genus-1 CURVATURE (d_{Theta_A})^2 proportional to kappa is a
    phenomenon of the full CHIRAL deformation complex Def_cyc^mod(A),
    NOT of the finite-dimensional CE complex. In the chiral complex:
    - The OPE poles contribute additional terms beyond the Lie bracket
    - The sewing/genus structure produces genuine curvature at genus >= 1
    - The kappa term couples to the modular form omega_g on M_{g,n}

    This module computes the CE-level twisted differential as a BASELINE:
    it verifies that d^2 = 0 always holds at the Lie algebra level,
    consistent with the Jacobi identity. The chiral curvature is computed
    by the full bar complex machinery (see bar_cobar_adjunction_curved.tex).
    """

    complex: CyclicDeformationComplex
    kappa: Fraction

    def eta_vec(self) -> np.ndarray:
        """The Killing cocycle eta = [-, -] in C^2(g,g)."""
        return self.complex.killing_cocycle()

    def bracket_matrix(self, n: int) -> np.ndarray:
        """Matrix of kappa * [eta, -]: C^n -> C^{n+1}."""
        eta = self.eta_vec()
        bracket = _killing_bracket_matrix(
            eta, self.complex.sc, self.complex.kap, self.complex.dim, n
        )
        return _mat_scale(self.kappa, bracket)

    def d_twisted_matrix(self, n: int) -> np.ndarray:
        """Matrix of d_kappa = d_CE + kappa * [eta, -]: C^n -> C^{n+1}."""
        d_ce = self.complex.differential(n)
        bracket = self.bracket_matrix(n)
        return _mat_add(d_ce, bracket)

    def d_squared_matrix(self, n: int) -> np.ndarray:
        """Compute (d_kappa)^2: C^n -> C^{n+2}."""
        d_low = self.d_twisted_matrix(n)
        d_high = self.d_twisted_matrix(n + 1)
        return _mat_multiply(d_high, d_low)

    def verify_d_squared_zero(self, n: int) -> bool:
        """Check (d_kappa)^2 = 0 at degree n."""
        return _is_zero_matrix(self.d_squared_matrix(n))

    def verify_jacobi_implies_d_squared_zero(self, n: int) -> bool:
        """Verify that (d_kappa)^2 = 0 for all kappa.

        Since eta = mu (the Lie bracket), [mu, mu]_NR = 0 (Jacobi identity).
        Therefore d_CE + kappa*[eta,-] always has d^2 = 0.
        This is a consistency check of the Jacobi identity.
        """
        return self.verify_d_squared_zero(n)

    def twisted_cohomology_dims(self) -> Dict[int, int]:
        """Cohomology of the twisted complex at kappa=0 (= CE cohomology).

        At kappa != 0, (d_kappa)^2 != 0 in general, so this is only
        meaningful at kappa = 0 (the CE baseline) or when the curvature vanishes.
        """
        return self.complex.cohomology_dims()


# ---------------------------------------------------------------------------
# Standard family tangent complexes
# ---------------------------------------------------------------------------

def kappa_affine_sl2(k: Fraction) -> Fraction:
    """Modular characteristic kappa for V_k(sl_2).

    kappa = dim(g) * (k + h^v) / (2 * h^v) = 3(k+2)/4.
    """
    return Fraction(3) * (k + Fraction(2)) / Fraction(4)


def kappa_affine(dim_g: int, k: Fraction, h_dual: int) -> Fraction:
    """Modular characteristic kappa for V_k(g).

    kappa = dim(g) * (k + h^v) / (2 * h^v).
    """
    return Fraction(dim_g) * (k + Fraction(h_dual)) / (Fraction(2) * Fraction(h_dual))


def kappa_heisenberg() -> Fraction:
    """Modular characteristic for the Heisenberg VOA.

    kappa = 1 (rank 1, anomaly ratio rho = 1).
    """
    return Fraction(1)


def kappa_virasoro(c: Fraction) -> Fraction:
    """Modular characteristic for the Virasoro algebra at central charge c.

    kappa = c/2.
    """
    return c / Fraction(2)


def heisenberg_tangent() -> Dict[str, object]:
    """Tangent complex data for the Heisenberg VOA (rank 1).

    Theta_A = kappa * eta = 1 * eta where eta is the Killing form on the
    abelian Lie algebra (dim 1). Since dim(g) = 1 and g is abelian:
    - C^0 = k (dim 1)
    - C^1 = k (dim 1)
    - C^n = 0 for n >= 2
    - All CE differentials are zero (abelian)
    - H^0 = k (center = g for abelian g)
    - H^1 = k (the level/scaling deformation)
    - H^n = 0 for n >= 2

    Shadow depth: r_max = 2 (Gaussian class). Theta_A = kappa*eta terminates.
    d_{Theta}^2 = 0 exactly (no obstruction because dim=1, no higher brackets).
    """
    return {
        "kappa": kappa_heisenberg(),
        "shadow_depth": 2,
        "shadow_class": "G",
        "h0": 1,  # center = g (abelian)
        "h1": 1,  # level deformation
        "h2": 0,  # unobstructed
        "d_theta_squared_zero": True,
    }


def affine_sl2_tangent(k: Fraction) -> Dict[str, object]:
    """Tangent complex data for V_k(sl_2) at level k.

    The tangent complex is the CE complex C*(sl_2, sl_2) at genus 0.
    By Whitehead's theorem, H^*(sl_2, sl_2) = 0 in all degrees.
    This means sl_2 (hence V_k(sl_2)) is RIGID as a Lie algebra.

    But as a CHIRAL algebra, V_k(sl_2) has a 1-parameter deformation (the level k).
    This deformation lives in H^2_cyc(sl_2, sl_2) = k (the Killing 3-cocycle),
    NOT in H^2(sl_2, sl_2) = 0. The cyclic deformation complex is the correct home.

    Cyclic cohomology: H^n_cyc(sl_2, sl_2) = H^{n+1}(sl_2) via the Killing form.
    - H^0_cyc = H^1(sl_2) = 0
    - H^1_cyc = H^2(sl_2) = 0
    - H^2_cyc = H^3(sl_2) = k (Killing 3-cocycle)
    - H^3_cyc = 0 (for dim reasons)

    Shadow depth: r_max = 3 (Lie/tree class L). C_3 = Killing 3-form.
    The obstruction o_4 = 0 (the quartic shadow vanishes for affine algebras).
    """
    kap = kappa_affine_sl2(k)
    is_critical = (k == Fraction(-2))

    return {
        "kappa": kap,
        "shadow_depth": 3,
        "shadow_class": "L",
        "h0_ce": 0,  # center of sl_2 = 0
        "h1_ce": 0,  # sl_2 is rigid (Whitehead)
        "h2_ce": 0,  # no obstructions in CE
        "h2_cyc": 1,  # Killing 3-cocycle = level deformation
        "is_critical": is_critical,
        "obstruction_o4": Fraction(0),  # quartic vanishes
    }


def virasoro_tangent(c: Fraction) -> Dict[str, object]:
    """Tangent complex data for the Virasoro algebra at central charge c.

    The Virasoro algebra Vir_c has:
    - H^1(L_A) = k (the central charge deformation)
    - Shadow depth: r_max = infinity (mixed class M)
    - Shadow class: M (mixed/infinite)
    - The quintic obstruction o_5 != 0 (forced by the infinite tower)

    The quartic contact invariant:
    Q^contact_Vir = 10 / (c * (5c + 22))

    The Hessian correction:
    delta_H^(1)_Vir = 120 / (c^2 * (5c + 22)) * x^2
    """
    kap = kappa_virasoro(c)
    # Quartic contact invariant (undefined at c=0 or 5c+22=0)
    if c != 0 and 5 * c + 22 != 0:
        q_contact = Fraction(10) / (c * (5 * c + 22))
    else:
        q_contact = None

    return {
        "kappa": kap,
        "shadow_depth": None,  # infinite
        "shadow_class": "M",
        "h1_deformation": 1,  # central charge direction
        "q_contact": q_contact,
        "obstruction_o5_nonzero": True,
    }


# ---------------------------------------------------------------------------
# Obstruction class computation
# ---------------------------------------------------------------------------

def obstruction_class_affine_o4(sc: np.ndarray, kap: np.ndarray, dim: int) -> bool:
    """Check that the quartic obstruction o_4 vanishes for affine algebras.

    For V_k(g), the shadow tower has:
    Theta_A^{<=2} = kappa * eta
    Theta_A^{<=3} = kappa * eta + C_3

    The obstruction to extending to arity 4 is:
    o_4(A) = d_CE(C_3) + kappa * [eta, C_3]_NR + ... projected to H^2

    For affine algebras, the cubic shadow C_3 is gauge-trivial when
    H^1(F^3 g / F^4 g, d_2) = 0 (thm:cubic-gauge-triviality).
    The quartic class [Theta'_4] is then canonical and VANISHES
    for the affine (Lie/tree) class.

    This function verifies o_4 = 0 by checking that the cubic gauge triviality
    condition holds: H^1_cyc at the relevant filtration level is zero.
    For semisimple g, this follows from H^2(g) = 0 (Whitehead).
    """
    # H^2(g) = H^1_cyc(g,g) = 0 for semisimple g (Whitehead)
    # This implies the cubic shadow is gauge-trivial
    # and the quartic obstruction vanishes.
    cohom = ce_cohomology(sc, dim)
    # H^1(g,g) = 0 implies no infinitesimal Lie algebra deformations
    # H^2(g,g) = 0 implies no obstructions
    return cohom[1] == 0 and cohom[2] == 0


def shadow_depth_classification(family: str) -> Dict[str, object]:
    """Shadow depth classification for standard families.

    G (Gaussian, r_max=2): Heisenberg, lattice VOAs
    L (Lie/tree, r_max=3): affine V_k(g)
    C (contact/quartic, r_max=4): beta-gamma
    M (mixed, r_max=infinity): Virasoro, W_N
    """
    table = {
        "heisenberg": {"class": "G", "r_max": 2, "description": "Gaussian termination"},
        "affine": {"class": "L", "r_max": 3, "description": "Lie/tree, cubic shadow"},
        "betagamma": {"class": "C", "r_max": 4, "description": "contact/quartic termination"},
        "virasoro": {"class": "M", "r_max": None, "description": "mixed, infinite tower"},
        "w_n": {"class": "M", "r_max": None, "description": "mixed, infinite tower"},
    }
    if family not in table:
        raise ValueError(f"Unknown family: {family}")
    return table[family]


# ---------------------------------------------------------------------------
# Verification entry points
# ---------------------------------------------------------------------------

def verify_ce_d_squared_sl2() -> Dict[str, bool]:
    """Verify d^2 = 0 for the CE complex of sl_2 with adjoint coefficients."""
    cx = sl2_deformation_complex()
    return {
        "d0_d1_zero": cx.verify_d_squared(0),
        "d1_d2_zero": cx.verify_d_squared(1),
    }


def verify_sl2_rigidity() -> Dict[str, bool]:
    """Verify that sl_2 is rigid: H^*(sl_2, sl_2) = 0 (Whitehead)."""
    cx = sl2_deformation_complex()
    h = cx.cohomology_dims()
    return {
        "h0_zero": h[0] == 0,
        "h1_zero": h[1] == 0,
        "h2_zero": h[2] == 0,
        "h3_zero": h[3] == 0,
    }


def verify_sl2_killing_cocycle() -> Dict[str, bool]:
    """Verify properties of the Killing 3-cocycle for sl_2."""
    sc = sl2_structure_constants()
    kap = sl2_killing_form()
    dim = 3

    # The Killing 3-form phi(a,b,c) = kap([a,b], c)
    phi_012 = killing_3form_value(sc, kap, dim)

    # The Killing cocycle eta in C^2(g,g) satisfies d_CE(eta) = 0
    eta = killing_cocycle(sc, kap, dim)
    d2 = ce_differential_2(sc, dim)
    d_eta = _mat_multiply(d2, eta.reshape(-1, 1))
    eta_is_cocycle = _is_zero_matrix(d_eta)

    return {
        "killing_3form_nonzero": phi_012 != 0,
        "killing_3form_value": phi_012,
        "eta_is_ce_cocycle": eta_is_cocycle,
    }


def verify_killing_bracket_d_intertwining_sl2() -> Dict[str, bool]:
    """Verify that [eta, -] intertwines with d_CE at degree 0 for sl_2.

    The identity d_CE([eta, x]) = [eta, d_CE(x)] + [d_CE(eta), x]
    holds because d_CE(eta) = 0 (eta is a cocycle).
    So [eta, d_CE(x)] = d_CE([eta, x]) for all x in C^0.
    """
    sc = sl2_structure_constants()
    kap = sl2_killing_form()
    dim = 3
    eta = killing_cocycle(sc, kap, dim)

    # [eta, -]: C^0 -> C^1
    bracket_0 = _killing_bracket_matrix(eta, sc, kap, dim, 0)
    # [eta, -]: C^1 -> C^2
    bracket_1 = _killing_bracket_matrix(eta, sc, kap, dim, 1)
    # d_CE: C^0 -> C^1
    d0 = ce_differential_0(sc, dim)
    # d_CE: C^1 -> C^2
    d1 = ce_differential_1(sc, dim)

    # Check: d1 * bracket_0 = bracket_1 * d0 (intertwining)
    lhs = _mat_multiply(d1, bracket_0)
    rhs = _mat_multiply(bracket_1, d0)
    diff = _mat_add(lhs, _mat_scale(Fraction(-1), rhs))

    return {
        "intertwining_holds": _is_zero_matrix(diff),
    }


def verify_kappa_twist_curvature_sl2(k: Fraction) -> Dict[str, bool]:
    """Verify d^2 = 0 for the kappa-twisted CE differential of sl_2.

    Since eta = mu (Lie bracket), [mu, mu]_NR = 0 (Jacobi identity),
    so (d_CE + kappa*[eta,-])^2 = 0 for ALL kappa. This holds at the
    CE level; the genus-1 curvature is a chiral phenomenon.
    """
    cx = sl2_deformation_complex()
    kap = kappa_affine_sl2(k)
    tw = KillingTwistedDifferential(complex=cx, kappa=kap)

    d2_zero_at_0 = tw.verify_d_squared_zero(0)
    d2_zero_at_1 = tw.verify_d_squared_zero(1)

    return {
        "kappa_value": kap,
        "d_squared_zero_at_deg0": d2_zero_at_0,
        "d_squared_zero_at_deg1": d2_zero_at_1,
        "jacobi_consistent": tw.verify_jacobi_implies_d_squared_zero(0),
    }


def verify_affine_sl2_o4_vanishes() -> Dict[str, bool]:
    """Verify the quartic obstruction o_4 = 0 for affine sl_2."""
    sc = sl2_structure_constants()
    kap = sl2_killing_form()
    return {
        "o4_vanishes": obstruction_class_affine_o4(sc, kap, 3),
    }
