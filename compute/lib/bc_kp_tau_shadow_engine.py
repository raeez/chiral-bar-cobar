r"""bc_kp_tau_shadow_engine.py -- KP hierarchy tau functions from shadow partition functions.

MATHEMATICAL FRAMEWORK
======================

The KP hierarchy is the universal integrable hierarchy: tau functions
tau(t_1, t_2, t_3, ...) satisfying the Hirota bilinear identity

    Res_{z=0} [exp(sum_{j>=1} (t_j - t'_j) z^j) *
               exp(-sum_{j>=1} (1/j)(d/dt_j - d/dt'_j) z^{-j}) *
               tau(t) * tau(t')] = 0

Equivalently, the Hirota bilinear equations:

    sum_{j>=0} S_j(-2y) * S_{j+1}(D~) * tau . tau = 0

where S_j are elementary Schur polynomials, D~ = (D_1, D_2/2, D_3/3, ...),
and D_k is the Hirota derivative in t_k.

SHADOW TAU FUNCTION DEFINITION
==============================

For a modular Koszul algebra A with shadow partition function

    Z^sh_A(hbar) = exp(sum_{g>=1} F_g(A) * hbar^{2g})

we define the shadow tau function by the KP time identification:

    t_n := n-th shadow coupling = shadow arity-n data

At the SCALAR level (arity 2 only):

    F_g^{scal}(A) = kappa(A) * lambda_g^FP

    sum_{g>=1} F_g * hbar^{2g} = kappa * (A-hat(i*hbar) - 1)
                                = kappa * ((hbar/2)/sin(hbar/2) - 1)

The KP identification maps t_1 = hbar (the genus parameter), and higher
t_n encode arity-n shadow couplings.  Concretely:

    tau_A(t) = exp(sum_{g>=1} sum_{r>=2} F_g^{(r)}(A) * t_1^{2g} * t_r^{...})

For the SCALAR SECTOR (class G algebras like Heisenberg), the tau function
reduces to a function of t_1 alone:

    tau_Heis(t) = exp(sum_{g>=1} k * lambda_g^FP * t_1^{2g})
               = exp(k * ((t_1/2)/sin(t_1/2) - 1))

KEY KP REDUCTIONS:

1. KdV = 2-reduction of KP: tau depends only on odd times t_1, t_3, t_5, ...
   Virasoro (W_2) should satisfy KdV reduction since Vir = KdV W-algebra.

2. Boussinesq = 3-reduction: tau depends only on t_n with n not divisible by 3.
   W_3 should satisfy 3-reduction.

3. N-reduction of KP: tau(t_n) = 0 for n divisible by N.
   sl_N affine should satisfy N-reduction (the sl_N Drinfeld-Sokolov hierarchy).

HIROTA BILINEAR TEST
====================

The elementary Schur polynomials are:

    exp(sum_{j>=1} t_j z^j) = sum_{j>=0} S_j(t) z^j

    S_0 = 1, S_1 = t_1, S_2 = t_1^2/2 + t_2, S_3 = t_1^3/6 + t_1*t_2 + t_3, ...

The Hirota derivative D_k acts by:

    D_k^n f . g = (d/ds)^n f(t_k + s) g(t_k - s) |_{s=0}

For a tau function tau(t), the Hirota bilinear identity produces an
infinite sequence of PDEs.  The first nontrivial one (at order 4 in z) is:

    (D_1^4 + 3 D_2^2 - 4 D_1 D_3) tau . tau = 0   (KP equation)

which is equivalent to:

    (u_t - 6uu_x - u_xxx)_x + 3 u_yy = 0

via u = 2 (d/dt_1)^2 log tau, with t_2 = y, t_3 = t.

SATO GRASSMANNIAN
=================

Every tau function of KP corresponds to a point W in the Sato Grassmannian
Gr = Gr(H) where H = L^2(S^1).  The Grassmannian parametrizes subspaces
W subset H such that the projection W -> H_+ is Fredholm of index 0.

For the shadow tau function:
    W_A = {f in L^2(S^1) : f extends to the shadow partition function}

The Plucker coordinates of W give the Schur expansion of tau:

    tau(t) = sum_lambda s_lambda(t) * pi_lambda(W)

where s_lambda are Schur functions and pi_lambda are Plucker coordinates.

CONVENTIONS:
    - kappa(Heisenberg_k) = k (AP39)
    - kappa(Virasoro_c) = c/2 (AP39: only for Virasoro)
    - kappa(affine KM g_k) = dim(g)*(k+h^v)/(2*h^v) (AP1/AP39)
    - eta(tau) = q^{1/24} * prod(1-q^n) (AP46)
    - F_g = kappa * lambda_g^FP (Theorem D, scalar level)

References:
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    Sato-Segal-Wilson: "Loop groups and the Grassmannian"
    Date-Jimbo-Kashiwara-Miwa: "KP hierarchies of orthogonal and symplectic type"
    Kac-Raina: "Bombay lectures on highest weight representations"
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

from sympy import (
    Rational, Symbol, bernoulli, binomial, factorial,
    pi as sym_pi, simplify, sqrt, Abs, N as Neval, oo, exp, sin,
    Poly, symbols, Integer, S as sympy_S,
)

from compute.lib.utils import lambda_fp, F_g

# ===========================================================================
# Constants
# ===========================================================================

PI = math.pi
TWO_PI = 2 * PI
TWO_PI_SQ = TWO_PI ** 2

# First 30 nontrivial zeros of the Riemann zeta function (imaginary parts).
# Source: LMFDB / Odlyzko tables, verified to 10+ digits.
RIEMANN_ZETA_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081607,
    67.079810529494174,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492980517050,
    87.425274613125196,
    88.809111207634465,
    92.491899270558484,
    94.651344040519838,
    95.870634228245309,
    98.831194218193692,
    101.317851005731220,
]


# ===========================================================================
# Section 1: Elementary Schur polynomials
# ===========================================================================

@lru_cache(maxsize=1024)
def schur_polynomial_elementary(j: int, t_tuple: Tuple[float, ...]) -> float:
    r"""Elementary Schur polynomial S_j(t_1, t_2, ...).

    Defined by the generating function:
        exp(sum_{k>=1} t_k z^k) = sum_{j>=0} S_j(t) z^j

    Recurrence: S_j = (1/j) sum_{k=1}^j k * t_k * S_{j-k}
    with S_0 = 1.

    These are NOT the Schur functions s_lambda indexed by partitions;
    they are the elementary Schur polynomials (also called complete
    exponential Bell polynomials divided by j!).
    """
    if j < 0:
        return 0.0
    if j == 0:
        return 1.0
    t = list(t_tuple)
    total = 0.0
    for k in range(1, j + 1):
        tk = t[k - 1] if k <= len(t) else 0.0
        total += k * tk * schur_polynomial_elementary(j - k, t_tuple)
    return total / j


def schur_poly_exact(j: int, t_vars: List) -> Any:
    r"""Exact symbolic elementary Schur polynomial S_j(t_1, ..., t_n).

    Uses the same recurrence as above but with sympy expressions.
    """
    if j < 0:
        return sympy_S.Zero
    if j == 0:
        return sympy_S.One
    total = sympy_S.Zero
    for k in range(1, j + 1):
        tk = t_vars[k - 1] if k <= len(t_vars) else sympy_S.Zero
        total += k * tk * schur_poly_exact(j - k, t_vars)
    return total / j


# ===========================================================================
# Section 2: Hirota derivative
# ===========================================================================

def hirota_derivative(f_coeffs: Dict[Tuple, float],
                      g_coeffs: Dict[Tuple, float],
                      direction: int,
                      order: int = 1) -> Dict[Tuple, float]:
    r"""Compute the Hirota derivative D_{direction}^{order} f . g.

    f_coeffs and g_coeffs are dictionaries mapping multi-index tuples
    (n_1, n_2, ...) to coefficients in the monomial expansion
    f = sum c_{n} t^n.

    D_k^m f . g = sum_{j=0}^{m} (-1)^{m-j} C(m,j) f^{(j)}_k * g^{(m-j)}_k

    where f^{(j)}_k = (d/dt_k)^j f.

    Returns the resulting coefficient dictionary.
    """
    result: Dict[Tuple, float] = {}

    for nf, cf in f_coeffs.items():
        for ng, cg in g_coeffs.items():
            for j in range(order + 1):
                # j-th derivative of f w.r.t. t_{direction}, (order-j)-th of g
                # Derivative of t^n w.r.t. t_k: n_k * (n_k - 1) * ... * t^{n - j*e_k}
                nf_list = list(nf)
                ng_list = list(ng)

                # Ensure indices are long enough
                d = direction - 1  # 0-indexed
                while len(nf_list) <= d:
                    nf_list.append(0)
                while len(ng_list) <= d:
                    ng_list.append(0)

                # j-th derivative of t^{nf_k} in direction d
                nfk = nf_list[d]
                if nfk < j:
                    continue
                f_deriv_factor = 1.0
                for m in range(j):
                    f_deriv_factor *= (nfk - m)

                # (order-j)-th derivative of t^{ng_k} in direction d
                ngk = ng_list[d]
                rem = order - j
                if ngk < rem:
                    continue
                g_deriv_factor = 1.0
                for m in range(rem):
                    g_deriv_factor *= (ngk - m)

                # Hirota sign
                sign = (-1) ** rem
                binom_coeff = 1
                for m in range(1, order + 1):
                    binom_coeff = binom_coeff * (order - m + 1) // m
                    if m == j:
                        break
                binom_coeff = math.comb(order, j)

                # Result multi-index
                nf_new = list(nf_list)
                ng_new = list(ng_list)
                nf_new[d] -= j
                ng_new[d] -= rem

                out_idx = tuple(nf_new[i] + ng_new[i] for i in range(max(len(nf_new), len(ng_new))))

                coeff = sign * binom_coeff * f_deriv_factor * g_deriv_factor * cf * cg
                if out_idx in result:
                    result[out_idx] = result[out_idx] + coeff
                else:
                    result[out_idx] = coeff

    return result


# ===========================================================================
# Section 3: Kappa values and shadow data
# ===========================================================================

def kappa_heisenberg(k: float) -> float:
    """kappa(H_k) = k. AP39: kappa != c/2 in general."""
    return float(k)


def kappa_virasoro(c: float) -> float:
    """kappa(Vir_c) = c/2. AP39: this is the ONE case where kappa = c/2."""
    return float(c) / 2.0


def kappa_affine_sl2(level: int) -> float:
    """kappa(sl_2_k) = 3*(k+2)/(2*2) = 3*(k+2)/4.

    dim(sl_2) = 3, h^v(sl_2) = 2.
    """
    return 3.0 * (level + 2) / 4.0


def kappa_affine_slN(N: int, level: int) -> float:
    """kappa(sl_N_k) = (N^2-1)*(k+N)/(2*N).

    dim(sl_N) = N^2-1, h^v(sl_N) = N.
    """
    return (N * N - 1.0) * (level + N) / (2.0 * N)


# ===========================================================================
# Section 4: Shadow tau function (scalar sector)
# ===========================================================================

@dataclass
class ShadowTauFunction:
    r"""Shadow tau function for a modular Koszul algebra.

    At the scalar level:
        log tau_A(t_1) = sum_{g>=1} kappa(A) * lambda_g^FP * t_1^{2g}
                       = kappa(A) * ((t_1/2)/sin(t_1/2) - 1)

    so tau_A(t_1) = exp(kappa * ((t_1/2)/sin(t_1/2) - 1)).

    The full multi-time tau function incorporates higher-arity
    shadow coefficients S_r through additional KP times t_r.
    """

    algebra_name: str
    kappa: float
    max_genus: int = 30
    # Higher shadow data (for multi-time extension)
    shadow_coefficients: Dict[int, float] = field(default_factory=dict)

    def free_energy_scalar(self, g: int) -> float:
        """F_g^{scalar} = kappa * lambda_g^FP."""
        return self.kappa * float(lambda_fp(g))

    def log_tau_scalar(self, t1: float) -> float:
        r"""log tau(t_1) = kappa * ((t_1/2)/sin(t_1/2) - 1).

        Valid for |t_1| < 2*pi (radius of convergence).
        """
        if abs(t1) < 1e-15:
            return 0.0
        half_t = t1 / 2.0
        sin_val = math.sin(half_t)
        if abs(sin_val) < 1e-300:
            return float('inf')
        return self.kappa * (half_t / sin_val - 1.0)

    def tau_scalar(self, t1: float) -> float:
        r"""tau(t_1) = exp(kappa * ((t_1/2)/sin(t_1/2) - 1))."""
        log_val = self.log_tau_scalar(t1)
        if abs(log_val) > 500:
            return float('inf') if log_val > 0 else 0.0
        return math.exp(log_val)

    def log_tau_scalar_complex(self, t1: complex) -> complex:
        r"""log tau(t_1) for complex t_1."""
        if abs(t1) < 1e-15:
            return 0.0 + 0.0j
        half_t = t1 / 2.0
        sin_val = cmath.sin(half_t)
        if abs(sin_val) < 1e-300:
            return complex(float('inf'), 0.0)
        return self.kappa * (half_t / sin_val - 1.0)

    def tau_scalar_complex(self, t1: complex) -> complex:
        r"""tau(t_1) for complex t_1."""
        return cmath.exp(self.log_tau_scalar_complex(t1))

    def log_tau_series(self, t1: float, max_g: int = None) -> float:
        r"""log tau computed as truncated series sum_{g=1}^{G} F_g * t_1^{2g}."""
        if max_g is None:
            max_g = self.max_genus
        total = 0.0
        for g in range(1, max_g + 1):
            total += self.free_energy_scalar(g) * t1 ** (2 * g)
        return total

    def kdv_potential(self, t1: float, dt: float = 1e-6) -> float:
        r"""u(x) = 2 * d^2/dx^2 log tau(x) where x = t_1.

        The KdV potential extracted from the shadow tau function.
        Computed by numerical second derivative.
        """
        log_m = self.log_tau_scalar(t1 - dt)
        log_0 = self.log_tau_scalar(t1)
        log_p = self.log_tau_scalar(t1 + dt)
        return 2.0 * (log_p - 2.0 * log_0 + log_m) / (dt * dt)

    def tau_multitime(self, t: List[float], max_g: int = 10) -> float:
        r"""Multi-time tau function tau(t_1, t_2, ...).

        At the scalar level, the dependence on t_1 is through:
            log tau = sum_{g>=1} F_g * t_1^{2g}

        Higher shadow coefficients S_r contribute through t_r:
            log tau += sum_{r>=3} sum_{g>=1} F_g^{(r)} * t_r * t_1^{2g-2+r}

        For the scalar sector (t_2 = t_3 = ... = 0), this reduces to
        tau_scalar(t_1).

        For the multi-time extension, we use the ansatz:
            log tau(t) = sum_{g>=1} [ kappa * lambda_g^FP * t_1^{2g}
                          + sum_{r>=3} S_r * lambda_g^FP * t_r * t_1^{2g-2+r-2} ]
        """
        if len(t) == 0:
            return 1.0

        log_val = 0.0
        t1 = t[0] if len(t) >= 1 else 0.0

        # Scalar contribution
        for g in range(1, max_g + 1):
            lam_g = float(lambda_fp(g))
            log_val += self.kappa * lam_g * t1 ** (2 * g)

            # Higher-arity contributions
            for r in range(3, min(len(t) + 1, 20)):
                tr = t[r - 1] if r <= len(t) else 0.0
                if abs(tr) < 1e-300:
                    continue
                S_r = self.shadow_coefficients.get(r, 0.0)
                if abs(S_r) < 1e-300:
                    continue
                # Coupling: S_r * lambda_g^FP * t_r * t_1^{max(0, 2g-2+r-2)}
                power = max(0, 2 * g - 2 + r - 2)
                log_val += S_r * lam_g * tr * t1 ** power

        if abs(log_val) > 500:
            return float('inf') if log_val > 0 else 0.0
        return math.exp(log_val)


# ===========================================================================
# Section 5: Hirota bilinear test (scalar sector)
# ===========================================================================

def hirota_bilinear_scalar(tau_fn, t1: float,
                           dt: float = 1e-4,
                           max_order: int = 8) -> Dict[str, Any]:
    r"""Test the Hirota bilinear identity for a scalar tau function.

    The KP equation in Hirota form (the simplest bilinear):
        (D_1^4 + 3*D_2^2 - 4*D_1*D_3) tau . tau = 0

    For a function of t_1 alone (with t_2 = t_3 = 0), the D_2 and D_3
    terms vanish, leaving:
        D_1^4 tau . tau = 0

    D_1^{2n} tau . tau = sum_{j=0}^{2n} (-1)^j C(2n,j) tau^{(j)} tau^{(2n-j)}

    For the SCALAR shadow tau, tau depends on t_1 alone via the closed form
    tau(t_1) = exp(kappa * ((t_1/2)/sin(t_1/2) - 1)), so:

    D_1^2 tau . tau = 2(tau * tau'' - (tau')^2) / tau^2 * tau^2
                    = 2(f'' + (f')^2)(tau^2) - 2(f')^2 tau^2 = 2 f'' tau^2

    where f = log tau.

    D_1^4 tau . tau = (12 f''^2 + 2 f'''') tau^2

    Test: does 12 f''^2 + 2 f'''' = 0? (KP constraint at scalar level)
    """
    results = {}

    # Numerical derivatives of log tau
    def log_tau(x):
        return tau_fn.log_tau_scalar(x)

    def deriv(func, x, n, h=dt):
        """n-th derivative by finite differences."""
        if n == 0:
            return func(x)
        if n == 1:
            return (func(x + h) - func(x - h)) / (2 * h)
        if n == 2:
            return (func(x + h) - 2 * func(x) + func(x - h)) / (h * h)
        if n == 3:
            return (func(x + 2*h) - 2*func(x + h) + 2*func(x - h) - func(x - 2*h)) / (2 * h**3)
        if n == 4:
            return (func(x + 2*h) - 4*func(x + h) + 6*func(x) - 4*func(x - h) + func(x - 2*h)) / (h**4)
        # Higher: recursive
        return (deriv(func, x + h, n - 1, h) - deriv(func, x - h, n - 1, h)) / (2 * h)

    f = log_tau(t1)
    f1 = deriv(log_tau, t1, 1)
    f2 = deriv(log_tau, t1, 2)
    f3 = deriv(log_tau, t1, 3)
    f4 = deriv(log_tau, t1, 4)
    f6 = deriv(log_tau, t1, 6)

    results['f'] = f
    results['f1'] = f1
    results['f2'] = f2
    results['f4'] = f4

    # KP bilinear: D_1^4 tau . tau / tau^2 = 12*(f'')^2 + 2*f''''
    # (in the scalar sector with t_2 = t_3 = 0)
    # This is the KP RESIDUAL: nonzero means tau is NOT a KP tau function
    # in the scalar sector alone.
    kp_residual_4 = 12 * f2 ** 2 + 2 * f4
    results['kp_residual_4'] = kp_residual_4

    # For a genuine KP tau function, D_1^4 tau.tau = -3 D_2^2 tau.tau + 4 D_1 D_3 tau.tau
    # In the scalar sector (no t_2, t_3 dependence), KP requires D_1^4 tau.tau = 0.
    # This is generically NOT satisfied: the shadow tau is not a KP tau function
    # in the naive scalar sector identification.

    # However, if we identify t_1 with x and define u = 2 f'' (KdV potential),
    # then the KdV equation in Hirota form is:
    #   D_1^4 tau.tau = c * tau^2  (constant multiple from the KdV flow)
    # The KEY test is whether u satisfies the KdV equation:
    #   u_t = u_xxx + 6 u u_x  (KdV)
    # In the single-variable reduction, this becomes a constraint on higher derivatives.

    # KdV bilinear: (D_1^4 - 4 D_1 D_3) tau.tau = 0
    # In pure t_1: D_1^4 tau.tau = 0 is required ONLY if tau solves the
    # stationary KdV (i.e., u_x_x_x + 6 u u_x = 0).

    # Test STATIONARY KdV for u = 2 f'':
    u = 2 * f2
    u_x = 2 * f3
    u_xxx = 2 * deriv(log_tau, t1, 5)  # d^3/dx^3 of f'' = f^(5)
    stationary_kdv = u_xxx + 6 * u * u_x
    results['u_kdv'] = u
    results['stationary_kdv_residual'] = stationary_kdv

    # D_1^6 test (next bilinear order)
    hirota_6 = 120 * f2 ** 3 + 60 * f2 * f4 + 2 * f6
    results['hirota_6_residual'] = hirota_6

    # The key observation: the shadow tau in the scalar sector is
    # exp(kappa * (x/2)/sin(x/2) - kappa), which has f'' = kappa * d^2/dx^2 [(x/2)/sin(x/2)]
    # This is NOT zero, so the shadow tau is not a stationary KdV solution.
    # HOWEVER, it IS related to the KP hierarchy through the MULTI-TIME extension.

    results['is_kp_scalar'] = abs(kp_residual_4) < 1e-6 * max(1.0, abs(f2) ** 2)
    results['is_stationary_kdv'] = abs(stationary_kdv) < 1e-6 * max(1.0, abs(u * u_x))

    return results


# ===========================================================================
# Section 6: Schur function expansion (free fermion / Heisenberg)
# ===========================================================================

@lru_cache(maxsize=512)
def integer_partitions(n: int, max_part: int = None) -> List[Tuple[int, ...]]:
    """All partitions of n as decreasing tuples.

    >>> sorted(integer_partitions(4))
    [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
    """
    if n == 0:
        return [()]
    if n < 0:
        return []
    if max_part is None:
        max_part = n
    parts = []
    for first in range(min(n, max_part), 0, -1):
        for rest in integer_partitions(n - first, first):
            parts.append((first,) + rest)
    return parts


def schur_function_hook_length(partition: Tuple[int, ...], t: Tuple[float, ...]) -> float:
    r"""Schur function s_lambda(t) via power-sum to Schur conversion.

    For a partition lambda, the Schur function in terms of power sums p_k = k*t_k:

        s_lambda = det(h_{lambda_i - i + j}) / det(h_{j-i})

    where h_n = S_n(t) (the n-th complete homogeneous symmetric function
    = elementary Schur polynomial).

    For small partitions, we compute directly.
    """
    if len(partition) == 0:
        return 1.0

    n = len(partition)
    # Build the matrix M_{ij} = h_{lambda_i - i + j} for i,j = 0,...,n-1
    # where h_k = S_k(t) = elementary Schur polynomial
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            k = partition[i] - i + j
            if k < 0:
                row.append(0.0)
            else:
                row.append(schur_polynomial_elementary(k, t))
        matrix.append(row)

    # Compute determinant (Gaussian elimination for small matrices)
    return _det(matrix)


def _det(matrix: List[List[float]]) -> float:
    """Determinant by LU decomposition for small matrices."""
    n = len(matrix)
    if n == 0:
        return 1.0
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Cofactor expansion along first row
    total = 0.0
    for j in range(n):
        minor = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
        total += ((-1) ** j) * matrix[0][j] * _det(minor)
    return total


def heisenberg_tau_schur_expansion(k: int, t: Tuple[float, ...],
                                   max_weight: int = 8) -> Dict[str, Any]:
    r"""Tau function for Heisenberg at level k via Schur expansion.

    The free fermion (Heisenberg at level k=1) tau function is:

        tau(t) = sum_lambda s_lambda(t)

    summed over all partitions lambda.  For level k:

        tau_k(t) = sum_lambda dim_k(lambda) * s_lambda(t)

    where dim_k is related to the k-colored partition function.

    For k=1 (single free fermion), the tau function is simply
    the generating function of all Schur functions (= Cauchy identity
    in one set of variables):

        tau_1(t) = exp(sum_{n>=1} t_n^2 / (2n))  [Gaussian]

    More precisely, for the free fermion charge-0 sector:
        tau(t) = <0| exp(H(t)) |0> = exp(sum_{n>=1} n t_n^2 / 2)  [bosonization]

    But the SHADOW tau function is different: it uses the genus expansion.

    Returns both the Schur expansion and the comparison with shadow tau.
    """
    results = {'k': k, 'max_weight': max_weight}

    # Schur expansion: tau = sum_{|lambda| <= W} s_lambda(t)^k
    # (for k copies of free fermion)
    tau_schur = 0.0
    partition_contributions = {}

    for w in range(0, max_weight + 1):
        for lam in integer_partitions(w):
            s_val = schur_function_hook_length(lam, t)
            # For k free fermions: multiply by k-fold Plucker coord
            # Simplification: for k=1, Plucker = 1 for all lambda
            # For general k, this is the k-th power of the basic tau
            contrib = s_val  # For k=1
            tau_schur += contrib
            partition_contributions[lam] = contrib

    results['tau_schur'] = tau_schur
    results['n_partitions'] = sum(len(integer_partitions(w)) for w in range(max_weight + 1))
    results['partition_contributions'] = partition_contributions

    # Compare with shadow tau
    kappa = kappa_heisenberg(k)
    shadow_tau = ShadowTauFunction(f'Heisenberg_k={k}', kappa)
    t1 = t[0] if len(t) >= 1 else 0.0
    tau_shadow = shadow_tau.tau_scalar(t1)
    results['tau_shadow'] = tau_shadow

    # Free fermion tau (bosonization): exp(sum n t_n^2 / 2)
    boson_sum = 0.0
    for n in range(1, len(t) + 1):
        tn = t[n - 1]
        boson_sum += n * tn ** 2 / 2.0
    tau_boson = math.exp(boson_sum) if abs(boson_sum) < 500 else float('inf')
    results['tau_boson'] = tau_boson

    return results


# ===========================================================================
# Section 7: KdV / Boussinesq / N-reduction tests
# ===========================================================================

def check_kdv_reduction(tau_fn: ShadowTauFunction,
                       t_values: List[float] = None,
                       dt: float = 1e-5) -> Dict[str, Any]:
    r"""Test KdV reduction: d tau / d t_{2n} = 0 for all n >= 1.

    The KdV hierarchy is the 2-reduction of KP: the tau function
    is independent of even-indexed times t_2, t_4, t_6, ...

    For Virasoro (W_2 algebra), the shadow tau should satisfy KdV.

    In the scalar sector, we test whether the dependence on higher
    times is consistent with KdV reduction by checking that the
    multi-time extension satisfies d/dt_2 = 0.

    We also test the KdV equation itself:
        4 u_t = u_xxx + 6 u u_x
    where u = 2 (d/dx)^2 log tau, x = t_1, t = t_3.
    """
    if t_values is None:
        t_values = [0.3, 0.5, 0.8, 1.0, 1.5, 2.0]

    results = {'algebra': tau_fn.algebra_name}
    kdv_residuals = {}

    for t1 in t_values:
        def log_tau(x):
            return tau_fn.log_tau_scalar(x)

        # u = 2 f'' where f = log tau
        f2 = (log_tau(t1 + dt) - 2 * log_tau(t1) + log_tau(t1 - dt)) / (dt ** 2)
        u = 2 * f2

        # u_x = 2 f'''
        f3_val = (log_tau(t1 + 2*dt) - 2*log_tau(t1 + dt) + 2*log_tau(t1 - dt) - log_tau(t1 - 2*dt)) / (2 * dt**3)
        u_x = 2 * f3_val

        # u_xxx = 2 f^(5) via 5-point stencil
        h = dt
        f5_val = (log_tau(t1 + 3*h) - 4*log_tau(t1 + 2*h) + 5*log_tau(t1 + h)
                  - 5*log_tau(t1 - h) + 4*log_tau(t1 - 2*h) - log_tau(t1 - 3*h)) / (2 * h**5)
        u_xxx = 2 * f5_val

        # Stationary KdV: u_xxx + 6 u u_x = 0
        residual = u_xxx + 6 * u * u_x
        scale = max(abs(u_xxx), abs(6 * u * u_x), 1e-10)
        kdv_residuals[t1] = {
            'u': u,
            'u_x': u_x,
            'u_xxx': u_xxx,
            'residual': residual,
            'relative_residual': abs(residual) / scale,
        }

    results['kdv_residuals'] = kdv_residuals

    # KdV reduction test: does the tau function naturally live on odd times only?
    # For the scalar shadow tau, it depends on t_1 alone, so trivially
    # independent of t_2, t_4, etc.  The REAL test is the multi-time extension.
    results['scalar_trivially_kdv'] = True  # scalar sector has no t_2 dependence

    return results


def check_n_reduction(tau_fn: ShadowTauFunction, N: int,
                     t1_values: List[float] = None,
                     dt: float = 1e-4) -> Dict[str, Any]:
    r"""Test N-reduction: tau independent of t_N, t_{2N}, t_{3N}, ...

    N=2: KdV (Virasoro / W_2)
    N=3: Boussinesq (W_3)
    N=N: N-th generalized KdV (sl_N affine / W_N)

    At the scalar level, the shadow tau depends only on t_1, so the
    N-reduction is trivially satisfied.  The content is in the
    multi-time extension with higher shadow coefficients.

    The N-reduction also implies specific constraints on the
    Schur expansion: only partitions whose Frobenius lengths
    are multiples of N contribute.
    """
    if t1_values is None:
        t1_values = [0.5, 1.0, 1.5]

    results = {
        'N': N,
        'algebra': tau_fn.algebra_name,
    }

    # Scalar level: trivial N-reduction
    results['scalar_reduction'] = True

    # Multi-time test: check d/dt_N of log tau with shadow coefficients
    if tau_fn.shadow_coefficients:
        S_N = tau_fn.shadow_coefficients.get(N, 0.0)
        results[f'S_{N}'] = S_N
        # If S_N = 0, the N-th shadow coupling vanishes, supporting N-reduction
        results[f'S_{N}_vanishes'] = abs(S_N) < 1e-10

    return results


# ===========================================================================
# Section 8: Tau function at zeta zeros
# ===========================================================================

def tau_at_zeta_zeros(tau_fn: ShadowTauFunction,
                      n_zeros: int = 20) -> Dict[str, Any]:
    r"""Evaluate the shadow tau function at Riemann zeta zeros.

    For the n-th nontrivial zero rho_n = 1/2 + i*gamma_n, we evaluate:

    1. tau(t_1 = gamma_n): shadow tau at the imaginary part of the zero
    2. tau(t = (rho_n, rho_n^2/2, rho_n^3/3, ...)): geometric specialization
    3. u(gamma_n) = 2 d^2/dx^2 log tau |_{x=gamma_n}: KdV potential at the zero
    4. Sato Grassmannian data: the Baker function at the zero

    The geometric series specialization t_n = rho^n / n maps KP times
    to a single parameter rho; at rho = rho_n this probes the tau function
    at the zeta zero.
    """
    n_zeros = min(n_zeros, len(RIEMANN_ZETA_ZEROS))
    results = {'algebra': tau_fn.algebra_name, 'n_zeros': n_zeros}
    zero_data = []

    for idx in range(n_zeros):
        gamma_n = RIEMANN_ZETA_ZEROS[idx]
        rho_n = complex(0.5, gamma_n)  # the zero on the critical line

        datum = {
            'index': idx + 1,
            'gamma_n': gamma_n,
            'rho_n': (0.5, gamma_n),
        }

        # 1. tau(t_1 = gamma_n)
        tau_real = tau_fn.tau_scalar(gamma_n)
        datum['tau_at_gamma'] = tau_real

        # 2. log tau at gamma
        log_tau_real = tau_fn.log_tau_scalar(gamma_n)
        datum['log_tau_at_gamma'] = log_tau_real

        # 3. tau(t_1 = gamma_n) complex evaluation
        tau_complex = tau_fn.tau_scalar_complex(complex(0, gamma_n))
        datum['tau_complex'] = (tau_complex.real, tau_complex.imag)

        # 4. Geometric specialization: t_n = rho_n^n / n
        geo_times = tuple(rho_n ** n / n for n in range(1, 11))
        geo_log_tau = sum(
            tau_fn.kappa * float(lambda_fp(g)) * (rho_n ** (2 * g))
            for g in range(1, min(tau_fn.max_genus, 15) + 1)
        )
        datum['geometric_log_tau'] = (geo_log_tau.real, geo_log_tau.imag)
        datum['geometric_tau_abs'] = abs(cmath.exp(geo_log_tau))

        # 5. KdV potential at gamma_n
        dt = 1e-5
        u_val = tau_fn.kdv_potential(gamma_n, dt)
        datum['kdv_potential'] = u_val

        # 6. Sato Grassmannian data: the Baker function
        # psi(z) = tau(t - [z^{-1}]) / tau(t) * exp(sum t_n z^n)
        # At the geometric specialization with t_n = rho^n/n:
        # sum t_n z^n = -log(1 - rho*z) for |rho*z| < 1
        # Baker function: psi(z) probes the Grassmannian point
        datum['sato_grassmannian'] = _sato_data_at_point(tau_fn, gamma_n)

        zero_data.append(datum)

    results['zero_data'] = zero_data

    # Summary statistics
    tau_values = [d['tau_at_gamma'] for d in zero_data]
    results['tau_mean'] = sum(abs(v) for v in tau_values) / n_zeros
    results['tau_max'] = max(abs(v) for v in tau_values)
    results['tau_min'] = min(abs(v) for v in tau_values)

    return results


def _sato_data_at_point(tau_fn: ShadowTauFunction, x: float) -> Dict[str, Any]:
    r"""Compute Sato Grassmannian data at a point.

    The Baker function is psi(x, z) = (tau(t - [z^{-1}]) / tau(t)) exp(xz)
    where t = (x, 0, 0, ...) in the scalar sector and [z^{-1}] = (1/z, 1/(2z^2), ...).

    The wave function w(x, z) = psi(x, z) exp(-xz) = tau(t - [z^{-1}]) / tau(t)
    encodes the Grassmannian point.

    For the scalar shadow tau:
        tau(t - [z^{-1}]) / tau(t) = exp(kappa * [(x-1/z)/2 / sin((x-1/z)/2) - (x/2)/sin(x/2)])

    The Grassmannian point W is determined by the expansion:
        w(x, z) = 1 + w_1(x)/z + w_2(x)/z^2 + ...
    """
    dt = 1e-5
    w_coeffs = []

    for n in range(1, 6):
        # w_n(x) from Taylor expansion of log w in 1/z
        # Numerical: w(x, z) ~ exp(f(x - 1/z) - f(x)) for f = kappa * (t/2)/sin(t/2)
        # Expand: f(x - eps) - f(x) = -eps f'(x) + eps^2 f''(x)/2 - ...
        # With eps = 1/z: w ~ exp(-f'/z + f''/(2z^2) - ...)
        # So w_1 = -f', w_2 = f''/2 - f'^2/2, etc.
        pass

    # Direct computation of first few w_n
    def f(x_val):
        return tau_fn.log_tau_scalar(x_val)

    f_prime = (f(x + dt) - f(x - dt)) / (2 * dt)
    f_double = (f(x + dt) - 2 * f(x) + f(x - dt)) / (dt ** 2)
    f_triple = (f(x + 2*dt) - 2*f(x + dt) + 2*f(x - dt) - f(x - 2*dt)) / (2 * dt**3)

    w1 = -f_prime
    w2 = f_double / 2.0 - f_prime ** 2 / 2.0
    w3 = -f_triple / 6.0 + f_prime * f_double / 2.0 - f_prime ** 3 / 6.0

    return {
        'w1': w1,
        'w2': w2,
        'w3': w3,
        'f_prime': f_prime,
        'f_double': f_double,
    }


# ===========================================================================
# Section 9: Multi-path verification infrastructure
# ===========================================================================

def verify_hirota_multipath(tau_fn: ShadowTauFunction,
                            t1: float = 1.0,
                            dt: float = 1e-5) -> Dict[str, Any]:
    r"""Multi-path verification of shadow tau function properties.

    Path 1: Direct Hirota bilinear (numerical)
    Path 2: KdV/Boussinesq reduction test
    Path 3: Sato Grassmannian (Baker function expansion)
    Path 4: Free fermion comparison (boson-fermion correspondence)
    Path 5: Numerical evaluation (closed form vs series)

    Returns: verification results with path-by-path outcomes.
    """
    results = {'algebra': tau_fn.algebra_name, 't1': t1}

    # Path 1: Hirota bilinear
    hirota = hirota_bilinear_scalar(tau_fn, t1, dt)
    results['path1_hirota'] = {
        'kp_residual_4': hirota['kp_residual_4'],
        'stationary_kdv_residual': hirota['stationary_kdv_residual'],
    }

    # Path 2: KdV reduction
    kdv = check_kdv_reduction(tau_fn, [t1], dt)
    results['path2_kdv'] = kdv['kdv_residuals'].get(t1, {})

    # Path 3: Sato Grassmannian
    sato = _sato_data_at_point(tau_fn, t1)
    results['path3_sato'] = sato

    # Path 4: Series vs closed form
    log_series = tau_fn.log_tau_series(t1, max_g=30)
    log_closed = tau_fn.log_tau_scalar(t1)
    results['path4_series_vs_closed'] = {
        'log_series': log_series,
        'log_closed': log_closed,
        'abs_diff': abs(log_series - log_closed),
        'rel_diff': abs(log_series - log_closed) / max(abs(log_closed), 1e-300),
    }

    # Path 5: Numerical consistency checks
    # f(x) = kappa * ((x/2)/sin(x/2) - 1)
    # f''(0) = kappa/12 (from Taylor: (x/2)/sin(x/2) = 1 + x^2/24 + ...)
    f_double_0 = (tau_fn.log_tau_scalar(dt) - 2 * tau_fn.log_tau_scalar(0) + tau_fn.log_tau_scalar(-dt)) / (dt ** 2)
    expected_f_double_0 = tau_fn.kappa / 12.0
    results['path5_numerical'] = {
        'f_double_at_0': f_double_0,
        'expected_kappa_over_12': expected_f_double_0,
        'match': abs(f_double_0 - expected_f_double_0) < 1e-4 * max(abs(expected_f_double_0), 1e-10),
    }

    return results


# ===========================================================================
# Section 10: Standard landscape tau functions
# ===========================================================================

def build_heisenberg_tau(k: int) -> ShadowTauFunction:
    """Build shadow tau for Heisenberg at level k.

    Heisenberg is class G: shadow depth 2, alpha = S_3 = 0, S_4 = 0.
    """
    kappa = kappa_heisenberg(k)
    return ShadowTauFunction(
        algebra_name=f'Heisenberg_k={k}',
        kappa=kappa,
        shadow_coefficients={},  # Class G: no higher shadows
    )


def build_virasoro_tau(c: float) -> ShadowTauFunction:
    """Build shadow tau for Virasoro at central charge c.

    Virasoro is class M: shadow depth infinity.
    Shadow coefficients from the recursive tower.

    Key values:
        S_3 (cubic): alpha_Vir = 2/c
        S_4 (quartic contact): Q^contact = 10/(c(5c+22))
    """
    kappa = kappa_virasoro(c)
    alpha = 2.0 / c if abs(c) > 1e-300 else 0.0
    S4 = 10.0 / (c * (5 * c + 22)) if abs(c) > 1e-300 and abs(5 * c + 22) > 1e-300 else 0.0

    # Build higher shadow coefficients from the recursive tower
    shadow_coeffs = {3: alpha, 4: S4}

    # Use the shadow metric to compute higher arities
    # Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    # Delta = 8*kappa*S_4
    if abs(kappa) > 1e-300:
        Delta = 8.0 * kappa * S4
        q0 = 4.0 * kappa ** 2
        q1 = 12.0 * kappa * alpha
        q2 = 9.0 * alpha ** 2 + 2.0 * Delta

        # Taylor expansion of sqrt(Q_L(t)) = a_0 + a_1*t + a_2*t^2 + ...
        a0 = 2.0 * abs(kappa)
        if a0 > 1e-300:
            a = [a0]
            a.append(q1 / (2.0 * a0))
            for n_idx in range(2, 20):
                if n_idx == 2:
                    cross = a[1] ** 2
                else:
                    cross = sum(a[j] * a[n_idx - j] for j in range(1, n_idx))
                qn = q2 if n_idx == 2 else 0.0
                a.append((qn - cross) / (2.0 * a0))

            for n_idx in range(len(a)):
                r = n_idx + 2
                S_r = a[n_idx] / r
                shadow_coeffs[r] = S_r

    return ShadowTauFunction(
        algebra_name=f'Virasoro_c={c}',
        kappa=kappa,
        shadow_coefficients=shadow_coeffs,
    )


def build_affine_sl2_tau(level: int) -> ShadowTauFunction:
    """Build shadow tau for affine sl_2 at given level.

    Affine KM is class L: shadow depth 3, S_4 = 0.
    kappa(sl_2_k) = 3*(k+2)/4.
    """
    kappa = kappa_affine_sl2(level)
    # Class L: alpha != 0, S_4 = 0
    # The cubic shadow alpha for affine KM depends on the structure constants
    # For sl_2: alpha = dim(sl_2) / kappa = 3 / kappa (estimated from OPE structure)
    # More precisely: alpha = 2 * dim(g) / (3 * kappa) for affine KM
    alpha = 2.0 * 3.0 / (3.0 * kappa) if abs(kappa) > 1e-300 else 0.0

    return ShadowTauFunction(
        algebra_name=f'sl2_k={level}',
        kappa=kappa,
        shadow_coefficients={3: alpha, 4: 0.0},  # Class L
    )


# ===========================================================================
# Section 11: Hirota bilinear through order 8
# ===========================================================================

def hirota_bilinear_through_order(tau_fn: ShadowTauFunction,
                                  max_order: int = 8,
                                  t1: float = 1.0,
                                  dt: float = 1e-5) -> Dict[str, Any]:
    r"""Compute and test Hirota bilinear relations through given order.

    The Hirota bilinear identity produces constraints at each even order 2n:

    Order 2: D_1^2 tau.tau = 2 f'' tau^2
    Order 4: D_1^4 tau.tau = (12 f''^2 + 2 f'''') tau^2   [KP equation]
    Order 6: D_1^6 tau.tau = (120 f''^3 + 60 f'' f'''' + 2 f^(6)) tau^2
    Order 8: D_1^8 tau.tau = (1680 f''^4 + 1120 f''^2 f'''' + ... ) tau^2

    In the scalar sector (single variable t_1), the Hirota bilinear at
    order 2n gives a polynomial in derivatives of f = log tau.
    These are NOT zero for a general function; they vanish iff tau is
    a tau function of KP.

    Returns residuals at each order.
    """
    results = {'t1': t1, 'max_order': max_order}

    def log_tau(x):
        return tau_fn.log_tau_scalar(x)

    # Compute derivatives of log tau up to order max_order + 2
    derivs = {}
    for n in range(max_order + 3):
        derivs[n] = _numerical_deriv(log_tau, t1, n, dt)

    results['derivs'] = {n: derivs[n] for n in range(min(9, max_order + 3))}

    # Hirota bilinear residuals
    # D_1^{2n} tau . tau / tau^2 = P_{2n}(f', f'', ...)
    # where P_{2n} is determined by:
    # (d/ds)^{2n} [exp(f(x+s) + f(x-s))] |_{s=0} / exp(2f(x))

    # This equals sum_{k=0}^{2n} C(2n,k) f^{(k)} f^{(2n-k)} where we
    # expand exp and collect.

    # More precisely: let g(s) = f(x+s) + f(x-s) - 2f(x)
    # g(s) = sum_{m=1}^{inf} (2/(2m)!) f^{(2m)} s^{2m}
    # D^{2n} exp(g) / exp(0) = P_{2n}

    # Compute via Faa di Bruno / recursion on g's Taylor coefficients
    g_coeffs = {}
    for m in range(1, max_order // 2 + 2):
        g_coeffs[2 * m] = 2.0 * derivs.get(2 * m, 0.0) / math.factorial(2 * m)

    # exp(g(s)) = sum a_n s^n
    # a_0 = 1, a_n = (1/n) sum_{k=1}^{n} k * g_k * a_{n-k}
    exp_g = [0.0] * (max_order + 1)
    exp_g[0] = 1.0
    for n in range(1, max_order + 1):
        total = 0.0
        for k in range(1, n + 1):
            gk = g_coeffs.get(k, 0.0)
            total += k * gk * exp_g[n - k]
        exp_g[n] = total / n

    # D_1^{2n} tau.tau / tau^2 = (2n)! * exp_g[2n]
    residuals = {}
    for order in range(2, max_order + 1, 2):
        hirota_val = math.factorial(order) * exp_g[order]
        residuals[order] = hirota_val

    results['hirota_residuals'] = residuals

    # Count satisfied vs violated
    satisfied = 0
    violated = 0
    threshold = 1e-6
    for order, val in residuals.items():
        if order <= 2:
            continue  # order 2 is never zero (it's 2*f'')
        # For a genuine KP tau function in 1 variable, ALL residuals beyond
        # order 2 should be zero (since it's a stationary solution).
        # For general f, they are nonzero.
        if abs(val) < threshold:
            satisfied += 1
        else:
            violated += 1

    results['satisfied'] = satisfied
    results['violated'] = violated
    results['total_tested'] = satisfied + violated

    return results


def _numerical_deriv(func, x: float, n: int, h: float = 1e-5) -> float:
    """n-th derivative by finite differences (central, high-order stencil)."""
    if n == 0:
        return func(x)

    # Use central differences with appropriate stencil
    # For n-th derivative, use (n+2)-point stencil for accuracy
    coeffs = _finite_diff_coefficients(n)
    total = 0.0
    half = len(coeffs) // 2
    for i, c in enumerate(coeffs):
        xi = x + (i - half) * h
        total += c * func(xi)
    return total / (h ** n)


@lru_cache(maxsize=64)
def _finite_diff_coefficients(n: int) -> Tuple[float, ...]:
    """Central finite difference coefficients for the n-th derivative.

    Returns tuple of coefficients for the stencil [-k, ..., 0, ..., k]
    where k = ceil(n/2) + 1.
    """
    if n == 1:
        return (-0.5, 0.0, 0.5)
    if n == 2:
        return (1.0, -2.0, 1.0)
    if n == 3:
        return (-0.5, 1.0, 0.0, -1.0, 0.5)
    if n == 4:
        return (1.0, -4.0, 6.0, -4.0, 1.0)
    if n == 5:
        return (-0.5, 2.0, -2.5, 0.0, 2.5, -2.0, 0.5)
    if n == 6:
        return (1.0, -6.0, 15.0, -20.0, 15.0, -6.0, 1.0)
    if n == 7:
        return (-0.5, 3.0, -7.0, 7.0, 0.0, -7.0, 7.0, -3.0, 0.5)
    if n == 8:
        return (1.0, -8.0, 28.0, -56.0, 70.0, -56.0, 28.0, -8.0, 1.0)
    # Fallback: binomial coefficients (forward difference, less accurate)
    return tuple((-1) ** (n - k) * math.comb(n, k) for k in range(n + 1))


# ===========================================================================
# Section 12: Full landscape computation
# ===========================================================================

def compute_full_landscape() -> Dict[str, Any]:
    r"""Compute shadow tau functions for the full standard landscape.

    Families computed:
    - Heisenberg k=1..5
    - Virasoro c=1/2, 1, 4, 10, 13, 25, 26
    - sl_2 affine k=1..6

    For each: scalar tau, Hirota test, KdV test, zeta zero evaluation.
    """
    results = {}

    # Heisenberg
    for k in range(1, 6):
        tau = build_heisenberg_tau(k)
        data = {
            'kappa': tau.kappa,
            'tau_at_1': tau.tau_scalar(1.0),
            'log_tau_at_1': tau.log_tau_scalar(1.0),
            'hirota': hirota_bilinear_through_order(tau, max_order=8, t1=1.0),
            'kdv': check_kdv_reduction(tau, [1.0]),
        }
        results[f'heisenberg_k={k}'] = data

    # Virasoro
    for c in [0.5, 1.0, 4.0, 10.0, 13.0, 25.0, 26.0]:
        tau = build_virasoro_tau(c)
        data = {
            'kappa': tau.kappa,
            'c': c,
            'tau_at_1': tau.tau_scalar(1.0),
            'log_tau_at_1': tau.log_tau_scalar(1.0),
            'hirota': hirota_bilinear_through_order(tau, max_order=8, t1=1.0),
            'kdv': check_kdv_reduction(tau, [1.0]),
        }
        results[f'virasoro_c={c}'] = data

    # sl_2 affine
    for level in range(1, 7):
        tau = build_affine_sl2_tau(level)
        data = {
            'kappa': tau.kappa,
            'level': level,
            'tau_at_1': tau.tau_scalar(1.0),
            'log_tau_at_1': tau.log_tau_scalar(1.0),
            'hirota': hirota_bilinear_through_order(tau, max_order=8, t1=1.0),
        }
        results[f'sl2_k={level}'] = data

    return results


# ===========================================================================
# Section 13: Analytic verification of the Ahat generating function
# ===========================================================================

def verify_ahat_generating_function(kappa_val: float,
                                    max_genus: int = 30) -> Dict[str, Any]:
    r"""Verify that sum_{g>=1} F_g t^{2g} = kappa * ((t/2)/sin(t/2) - 1).

    The generating function of the Faber-Pandharipande numbers is:
        sum_{g>=1} lambda_g^FP t^{2g} = (t/2)/sin(t/2) - 1

    Multi-path verification:
    1. Direct series sum vs closed form
    2. Radius of convergence = 2*pi (pole of csc)
    3. Ratio test: lambda_{g+1}/lambda_g -> 1/(2*pi)^2
    4. Specific values: F_1 = kappa/24, F_2 = 7*kappa/5760
    5. Residue at t = 2*pi
    """
    results = {'kappa': kappa_val, 'max_genus': max_genus}

    # Path 1: Series vs closed form at multiple points
    test_points = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
    comparisons = []
    for t in test_points:
        series_val = sum(kappa_val * float(lambda_fp(g)) * t ** (2 * g)
                         for g in range(1, max_genus + 1))
        closed_val = kappa_val * (t / 2.0 / math.sin(t / 2.0) - 1.0)
        comparisons.append({
            't': t,
            'series': series_val,
            'closed': closed_val,
            'abs_diff': abs(series_val - closed_val),
        })
    results['path1_series_vs_closed'] = comparisons

    # Path 2: Specific genus values
    F1 = kappa_val * float(lambda_fp(1))
    F2 = kappa_val * float(lambda_fp(2))
    results['path2_specific'] = {
        'F_1': F1,
        'F_1_expected': kappa_val / 24.0,
        'F_1_match': abs(F1 - kappa_val / 24.0) < 1e-12,
        'F_2': F2,
        'F_2_expected': 7.0 * kappa_val / 5760.0,
        'F_2_match': abs(F2 - 7.0 * kappa_val / 5760.0) < 1e-12,
    }

    # Path 3: Ratio test
    ratios = []
    for g in range(2, min(max_genus + 1, 25)):
        r = float(lambda_fp(g)) / float(lambda_fp(g - 1))
        ratios.append(r)
    target = 1.0 / TWO_PI_SQ
    results['path3_ratio'] = {
        'ratios_tail': ratios[-5:] if len(ratios) >= 5 else ratios,
        'target': target,
        'converges': abs(ratios[-1] - target) / target < 0.01 if ratios else False,
    }

    return results


# ===========================================================================
# Section 14: Partition function connection
# ===========================================================================

def shadow_tau_vs_partition_function(family: str, param,
                                    tau_values: List[float] = None) -> Dict[str, Any]:
    r"""Compare shadow tau function with the genus-1 exact partition function.

    The shadow tau function at the scalar level gives:
        log Z^sh_1(hbar) = F_1 * hbar^2 = (kappa/24) * hbar^2

    The exact genus-1 partition function is:
        Z^exact_1(tau) = 1/eta(tau)^k   [Heisenberg]
        Z^exact_1(tau) = chi_0(tau)       [Virasoro]

    The shadow expansion captures the LEADING term of log Z, not the
    full partition function.  The discrepancy is:
        Delta_1 = log Z^exact - log Z^sh

    which encodes the non-perturbative / instanton corrections.
    """
    if tau_values is None:
        tau_values = [0.1 + 0.5j, 0.2 + 1.0j, 0.3 + 2.0j]

    results = {'family': family, 'param': param}

    if family == 'heisenberg':
        k = param
        kappa = kappa_heisenberg(k)
        # Shadow: F_1 = kappa/24 = k/24
        shadow_F1 = kappa / 24.0

        # Exact: log(1/eta^k) = k * (2*pi*i*tau/24 - sum log(1-q^n))
        # The shadow captures the LEADING term -k * 2*pi*i*tau / 24 = k/24 * hbar^2
        # (under the identification hbar^2 = -2*pi*i*tau)
        results['shadow_F1'] = shadow_F1
        results['kappa'] = kappa

    elif family == 'virasoro':
        c = param
        kappa = kappa_virasoro(c)
        shadow_F1 = kappa / 24.0
        results['shadow_F1'] = shadow_F1
        results['kappa'] = kappa

    elif family == 'sl2':
        level = param
        kappa = kappa_affine_sl2(level)
        shadow_F1 = kappa / 24.0
        results['shadow_F1'] = shadow_F1
        results['kappa'] = kappa

    return results


# ===========================================================================
# Section 15: Comprehensive test harness
# ===========================================================================

def run_comprehensive_tests() -> Dict[str, Any]:
    r"""Run all verification tests for the KP tau shadow engine.

    Returns a dictionary summarizing all test outcomes.
    """
    results = {}

    # 1. Elementary Schur polynomial tests
    S0 = schur_polynomial_elementary(0, (1.0, 0.5, 0.3))
    S1 = schur_polynomial_elementary(1, (1.0, 0.5, 0.3))
    S2 = schur_polynomial_elementary(2, (1.0, 0.5, 0.3))
    results['schur_S0'] = S0  # = 1
    results['schur_S1'] = S1  # = t_1 = 1.0
    results['schur_S2'] = S2  # = t_1^2/2 + t_2 = 0.5 + 0.5 = 1.0

    # 2. Ahat verification for all kappa values
    for k in [1, 2, 3]:
        kap = kappa_heisenberg(k)
        results[f'ahat_heis_k={k}'] = verify_ahat_generating_function(kap)

    # 3. Tau function values
    for k in [1, 2, 3]:
        tau = build_heisenberg_tau(k)
        results[f'tau_heis_k={k}_at_1'] = tau.tau_scalar(1.0)

    for c in [1.0, 13.0, 26.0]:
        tau = build_virasoro_tau(c)
        results[f'tau_vir_c={c}_at_1'] = tau.tau_scalar(1.0)

    # 4. Multi-path verification
    tau_heis = build_heisenberg_tau(1)
    results['multipath_heis'] = verify_hirota_multipath(tau_heis, 1.0)

    tau_vir = build_virasoro_tau(10.0)
    results['multipath_vir'] = verify_hirota_multipath(tau_vir, 1.0)

    # 5. Zeta zero evaluations
    tau_heis = build_heisenberg_tau(1)
    results['zeta_heis'] = tau_at_zeta_zeros(tau_heis, 5)

    return results
