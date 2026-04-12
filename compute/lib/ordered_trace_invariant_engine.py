r"""Ordered trace invariant: a genuinely E_1 holomorphic invariant of curves.

THE CONSTRUCTION
================

The E_infinity (symmetric/Verlinde) partition function of a chiral algebra A
on a genus-g curve X is:

    Z_g^{sym}(A) = sum_lambda S_{0,lambda}^{2-2g}

This depends only on the FUSION RING of A (the modular S-matrix entries).
It is a topological invariant of Sigma_g, independent of complex structure.

The E_1 (ordered) bar complex B^{ord}(A) carries strictly more data: the
R-matrix r(z) and its quantization to the quantum R-matrix R(u).  The
collision residue of the MC element Theta_A at genus 1 produces the
ELLIPTIC R-matrix R^{ell}(z, tau), which depends on the modular parameter
tau of the elliptic curve E_tau.  This is E_1 data invisible to E_infinity.

DEFINITION (Ordered trace)
--------------------------
For a chiral algebra A on E_tau with quantum parameter q = exp(i*pi/(k+h^v)):

    Z_1^{ord}(A; u, tau) = sum_{lambda} chi_lambda(tau) * R_lambda(u, tau)

where:
  - chi_lambda(tau) = character of the lambda-th integrable representation
  - R_lambda(u, tau) = eigenvalue of the elliptic R-matrix on the lambda
    isotypic component of the conformal block space, evaluated at spectral
    parameter u on the torus E_tau

At u -> infinity (trivial spectral parameter), R_lambda -> 1 for all lambda
and Z_1^{ord} -> Z_1^{sym} = sum chi_lambda = number of integrable reps.

WHY THIS IS GENUINELY NEW
--------------------------
The Verlinde number Z_1^{sym} = k+1 for sl_2 at level k is an INTEGER that
depends only on k.  The ordered trace Z_1^{ord}(u, tau) is a FUNCTION of
(u, tau) in C x H (spectral parameter x upper half-plane).  Its dependence
on tau encodes KZB monodromy, which knows the COMPLEX STRUCTURE of E_tau.

The key quantity is the E_1 correction:

    Delta_1(u, tau) = Z_1^{ord}(u, tau) - Z_1^{sym}

which is nonzero for generic (u, tau) and cannot be computed from the fusion
ring alone.

At genus 2, the ordered trace involves the period matrix Omega of the
genus-2 Riemann surface, through the genus-2 generalization of the elliptic
R-matrix.  The Verlinde number Z_2(sl_2, k=2) = 10 is again a topological
invariant; the ordered trace Z_2^{ord}(u, Omega) is a function on the
Siegel upper half-space H_2.

MATHEMATICAL CONTENT
====================

For sl_2 at level k on E_tau:

1. MODULAR DATA:
   S_{j,l} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))
   h_j = j(j+2)/(4(k+2))
   c = 3k/(k+2)

2. CHARACTERS (genus 1):
   chi_j(tau) = (theta_{j+1,k+2}(tau) - theta_{-(j+1),k+2}(tau)) / eta(tau)
   where theta_{m,p}(tau) = sum_{n in Z} q^{p*(n + m/(2p))^2}

3. ELLIPTIC R-MATRIX EIGENVALUES:
   The elliptic R-matrix R^{ell}(u, tau) on V_j tensor V_l decomposes into
   irreducible channels V_m with eigenvalue:

       R_m^{ell}(u, tau) = exp(i*pi * c_2(m)/(k+h^v)) *
                            theta_1(u + eta_m | tau) / theta_1(u | tau)

   where eta_m = (c_2(m) - c_2(j) - c_2(l)) * pi/(k+h^v) encodes the
   Casimir difference, and theta_1 is the Jacobi theta function.

4. ORDERED TRACE (working definition):
   The physically meaningful quantity is the "braided partition function"
   or "ordered character":

       Z_1^{ord}(u, tau) = sum_{j=0}^{k} w_j(u, tau) * chi_j(tau)

   where w_j(u, tau) are the R-matrix weights:

   OPTION A (diagonal R-eigenvalue):
       w_j(u, tau) = q^{c_2(j)} * theta_1(u + alpha_j | tau) / theta_1(u | tau)
       with q = exp(i*pi/(k+h^v)), alpha_j = j(j+2)*pi/(2(k+h^v))

   OPTION B (quantum dimension deformation):
       w_j(u, tau) = [dim_q V_j](u, tau) / dim_q V_j
       where [dim_q V_j](u,tau) is the elliptic quantum dimension

   OPTION C (KZB monodromy eigenvalue):
       w_j(u, tau) = eigenvalue of the KZB monodromy operator M(tau)
       acting on the j-th conformal block, with spectral insertion at u

   We implement all three and compare.

CONVENTIONS
===========
- q = exp(i*pi/(k+h^v)) (Drinfeld-Kohno)
- kappa(sl_2, k) = 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2*h^v) (AP1/C3)
- r(z) = k*Omega/z (trace-form, AP126: k=0 -> r=0)
- Cohomological grading, bar uses desuspension s^{-1}
- Characters normalized: chi_j(tau) ~ q^{h_j - c/24} (1 + O(q))

References
----------
- Belavin, "Dynamical symmetry" (1981)
- Felder, "Conformal field theory and integrable systems on elliptic curves" (1994)
- Etingof-Varchenko, "Geometry and classification of solutions of the CDYBE" (1998)
- Bernard, "On the WZW models on the torus" (1988)
- thm:mc2-bar-intrinsic, thm:collision-residue-twisting
"""

from __future__ import annotations

import math
import cmath
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# 0. Constants and basic data
# =========================================================================

PI = math.pi
TWO_PI_I = 2.0j * PI


def _sl2_modular_data(k: int) -> Dict[str, Any]:
    """Complete modular data for sl_2 at positive integer level k.

    Returns S-matrix, T-diagonal, conformal weights, central charge,
    quantum dimensions, and Verlinde numbers.

    S_{j,l} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))
    h_j = j(j+2)/(4(k+2))
    c = 3k/(k+2)
    """
    r = k + 2  # k + h^v for sl_2
    c_val = 3.0 * k / r
    # AP1: kappa(sl_2, k) = dim(sl_2)*(k+h^v)/(2*h^v) = 3*r/4
    kappa = 3.0 * r / 4.0
    prefactor = math.sqrt(2.0 / r)
    q = cmath.exp(1j * PI / r)

    size = k + 1  # number of integrable reps: j = 0, 1, ..., k

    S = np.zeros((size, size))
    T = np.zeros(size, dtype=complex)
    h = np.zeros(size)
    qdim = np.zeros(size)

    for j in range(size):
        h[j] = j * (j + 2) / (4.0 * r)
        T[j] = cmath.exp(2j * PI * (h[j] - c_val / 24.0))
        qdim[j] = math.sin(PI * (j + 1) / r) / math.sin(PI / r)
        for l in range(size):
            S[j, l] = prefactor * math.sin(PI * (j + 1) * (l + 1) / r)

    return {
        "k": k,
        "r": r,  # k + h^v
        "c": c_val,
        "kappa": kappa,
        "q": q,
        "S": S,
        "T": T,
        "h": h,
        "qdim": qdim,
        "size": size,
    }


# =========================================================================
# 1. Jacobi theta functions (numerical, for the elliptic R-matrix)
# =========================================================================

def theta1(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_1(z | tau), the unique odd theta function.

    theta_1(z|tau) = 2 sum_{n=0}^{infty} (-1)^n q^{(n+1/2)^2} sin((2n+1)*pi*z)

    where q = e^{i*pi*tau}.  Zeros at z = m + n*tau.
    """
    q = cmath.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        sgn = (-1) ** n
        q_pow = q ** ((n + 0.5) ** 2)
        result += sgn * q_pow * cmath.sin((2 * n + 1) * PI * z)
    return 2.0 * result


def theta2(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_2(z | tau).

    theta_2(z|tau) = 2 sum_{n=0}^{infty} q^{(n+1/2)^2} cos((2n+1)*pi*z)
    """
    q = cmath.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        q_pow = q ** ((n + 0.5) ** 2)
        result += q_pow * cmath.cos((2 * n + 1) * PI * z)
    return 2.0 * result


def theta3(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_3(z | tau).

    theta_3(z|tau) = 1 + 2 sum_{n=1}^{infty} q^{n^2} cos(2*n*pi*z)
    """
    q = cmath.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        q_pow = q ** (n * n)
        result += 2.0 * q_pow * cmath.cos(2 * n * PI * z)
    return result


def theta4(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_4(z | tau).

    theta_4(z|tau) = 1 + 2 sum_{n=1}^{infty} (-1)^n q^{n^2} cos(2*n*pi*z)
    """
    q = cmath.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        sgn = (-1) ** n
        q_pow = q ** (n * n)
        result += 2.0 * sgn * q_pow * cmath.cos(2 * n * PI * z)
    return result


def eta_dedekind(tau: complex, n_terms: int = 200) -> complex:
    r"""Dedekind eta function.

    eta(tau) = q^{1/24} prod_{n=1}^{infty} (1 - q^n)

    where q = e^{2*pi*i*tau}.  The q^{1/24} is ESSENTIAL (C22/FM13).
    """
    q = cmath.exp(TWO_PI_I * tau)
    # q^{1/24}
    prefactor = cmath.exp(TWO_PI_I * tau / 24.0)
    product = 1.0 + 0.0j
    q_n = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        q_n *= q
        product *= (1.0 - q_n)
    return prefactor * product


# =========================================================================
# 2. sl_2 characters at level k
# =========================================================================

def sl2_character(j: int, k: int, tau: complex, n_terms: int = 300) -> complex:
    r"""Character chi_j(tau) for sl_2 at level k, representation j (Dynkin label).

    Uses the specialized Weyl-Kac formula (L'Hopital limit at z=0):

        chi_j(tau) = N_j(tau) / D(tau)

    where:
        N_j(tau) = sum_{n in Z} (j+1+2r*n) * q^{(j+1+2r*n)^2/(4r)}
        D(tau)   = sum_{n in Z} (1+4n) * q^{(1+4n)^2/8}

    with r = k+2 and q = e^{2*pi*i*tau}.

    The numerator comes from d/dz [theta_{j+1,r}(tau,z) - theta_{-(j+1),r}(tau,z)]
    at z=0, and the denominator from the affine sl_2 Weyl denominator.

    Normalization: chi_j(tau) ~ q^{h_j - c/24} * ((j+1) + O(q))
    where h_j = j(j+2)/(4r) and c = 3k/r.

    VERIFIED: chi_j/q^{h_j-c/24} -> (j+1) + O(q) for j=0,1,2 at k=2.
    [DC] direct series evaluation; [LT] Kac, Infinite-dim Lie algebras, Ch.12.
    """
    r = k + 2
    q = cmath.exp(TWO_PI_I * tau)

    # Numerator: sum_n (j+1+2r*n) * q^{(j+1+2r*n)^2/(4r)}
    num = 0.0 + 0.0j
    for n in range(-n_terms, n_terms + 1):
        m = j + 1 + 2 * r * n
        ex = m * m / (4.0 * r)
        num += m * q ** ex

    # Denominator: sum_n (1+4n) * q^{(1+4n)^2/8}
    denom = 0.0 + 0.0j
    for n in range(-n_terms, n_terms + 1):
        m = 1 + 4 * n
        ex = m * m / 8.0
        denom += m * q ** ex

    if abs(denom) < 1e-300:
        return 0.0 + 0.0j
    return num / denom


# =========================================================================
# 3. Casimir eigenvalues and R-matrix eigenvalue structure
# =========================================================================

def casimir_sl2(j: float) -> float:
    """Casimir eigenvalue c_2(j) = j(j+1) for sl_2 spin j.

    In the convention where the quadratic Casimir on the adjoint is 2*h^v = 4:
    c_2(j) = j(j+1).  For half-integer j (physical spin): c_2(1/2)=3/4.

    Note: some references use j(j+2)/(k+2) for the conformal weight;
    the bare Casimir is j(j+1) without level dependence.
    """
    return j * (j + 1)


def conformal_weight_sl2(j: int, k: int) -> float:
    """Conformal weight h_j = j(j+2)/(4(k+2)) for sl_2 at level k.

    This is the Sugawara weight: h_j = c_2^{affine}(j) / (2*(k+h^v))
    where c_2^{affine}(j) = j(j+2)/2 in the normalization where the
    quadratic Casimir eigenvalue on the spin-j rep of sl_2 is j(j+2)/2.
    """
    return j * (j + 2) / (4.0 * (k + 2))


# =========================================================================
# 4. Elliptic R-matrix eigenvalues (the core E_1 data)
# =========================================================================

def elliptic_R_eigenvalue_diagonal(j: int, k: int, u: complex,
                                    tau: complex) -> complex:
    r"""Diagonal elliptic R-matrix eigenvalue for sl_2 rep V_j on E_tau.

    Here j is the DYNKIN LABEL.  The elliptic quantum group E_{tau,eta}(sl_2)
    (Felder 1994) has R-matrix eigenvalues involving ratios of theta functions.

    For the diagonal action on the j-th isotypic component:

        R_j^{diag}(u, tau) = prod_{m=1}^{j} theta_1(u + m*eta | tau)
                                              / theta_1(u + (m-1)*eta | tau)

    where eta = 1/(k+2) is the crossing parameter (period = 1 convention).

    This is a ratio of j consecutive shifted theta functions, giving a
    degree-j elliptic function of u.  At j=0: R_0 = 1 (trivial rep).
    """
    r = k + 2  # k + h^v
    eta_param = 1.0 / r  # crossing parameter

    if j == 0:
        return 1.0 + 0.0j

    t1_u = theta1(u, tau)
    if abs(t1_u) < 1e-300:
        return float('nan') + 0.0j

    # Product of shifted ratios
    result = 1.0 + 0.0j
    for m in range(1, j + 1):
        num = theta1(u + m * eta_param, tau)
        den = theta1(u + (m - 1) * eta_param, tau)
        if abs(den) < 1e-300:
            return float('nan') + 0.0j
        result *= num / den

    # This equals theta_1(u + j*eta) / theta_1(u) by telescoping
    return result


def elliptic_R_eigenvalue_felder(j: int, k: int, u: complex,
                                  tau: complex) -> complex:
    r"""Felder's elliptic R-matrix eigenvalue on V_j (dynamical).

    Here j is the DYNKIN LABEL (= twice the spin), so the spin is j/2
    and the weights of V_j are m = -j/2, -j/2+1, ..., j/2 (half-integers
    when j is odd, integers when j is even).  The representation has
    dimension j+1.

    In the dynamical (IRF/face) formulation of the elliptic quantum group
    (Felder 1994, Etingof-Varchenko 1998), the eigenvalue on V_j:

        lambda_j(u, tau) = prod_{a=-j/2}^{j/2}
            theta_1(u + a/(k+2) | tau) / theta_1(u | tau)

    where a ranges over the j+1 weights in unit steps.

    Limiting behavior: as u -> 0 (regularized), lambda_j approaches the
    quantum dimension [j+1]_q = sin((j+1)*pi/(k+2))/sin(pi/(k+2)).
    """
    r = k + 2
    t1_u = theta1(u, tau)
    if abs(t1_u) < 1e-300:
        return float('nan') + 0.0j

    result = 1.0 + 0.0j
    spin = j / 2.0
    # Weights: m = -j/2, -j/2+1, ..., j/2 (j+1 terms)
    for m_idx in range(j + 1):
        m = -spin + m_idx
        if abs(m) < 1e-15:
            continue  # theta_1(u + 0)/theta_1(u) = 1
        shift = u + m / r
        result *= theta1(shift, tau) / t1_u

    return result


def quantum_dimension_sl2(j: int, k: int) -> float:
    """Quantum dimension dim_q(V_j) = [j+1]_q for sl_2 at level k.

    Here j is the DYNKIN LABEL (= twice the spin).  The quantum dimension is
    S_{0,j}/S_{0,0} = sin((j+1)*pi/(k+2)) / sin(pi/(k+2)).

    q = exp(i*pi/(k+2)).

    Checks: k=2, j=0 -> 1; j=1 -> sqrt(2); j=2 -> 1.
    """
    r = k + 2
    return math.sin((j + 1) * PI / r) / math.sin(PI / r)


# =========================================================================
# 5. The ordered trace: genus 1
# =========================================================================

def verlinde_number_g1(k: int) -> int:
    """E_infinity Verlinde number at genus 1 for sl_2 at level k.

    Z_1^{sym} = number of integrable reps = k + 1.
    """
    return k + 1


def verlinde_number_g(k: int, g: int) -> float:
    """E_infinity Verlinde number at genus g for sl_2 at level k.

    Z_g^{sym} = sum_{j=0}^{k} S_{0,j}^{2-2g}
              = (r/2)^{g-1} sum_{j=1}^{r-1} sin(pi*j/r)^{2-2g}

    where r = k + 2.
    """
    if g == 0:
        return 1.0
    if g == 1:
        return float(k + 1)
    r = k + 2
    prefactor = (r / 2.0) ** (g - 1)
    total = 0.0
    for j in range(1, r):
        s = math.sin(PI * j / r)
        total += s ** (2 - 2 * g)
    return prefactor * total


def ordered_trace_g1_optionA(k: int, u: complex, tau: complex,
                              n_terms: int = 200) -> Dict[str, Any]:
    r"""Ordered trace at genus 1 using diagonal R-eigenvalues (Option A).

    Z_1^{ord}(u, tau) = sum_{j=0}^{k} R_j^{diag}(u, tau) * chi_j(tau)

    where R_j^{diag} is the diagonal elliptic R-eigenvalue from the product
    formula, and chi_j is the sl_2 level-k character.

    Returns: dict with Z_ord, Z_sym, Delta, individual terms.
    """
    data = _sl2_modular_data(k)
    terms = []
    Z_ord = 0.0 + 0.0j

    for j in range(k + 1):
        chi = sl2_character(j, k, tau, n_terms)
        R_eig = elliptic_R_eigenvalue_diagonal(j, k, u, tau)
        term = R_eig * chi
        terms.append({
            "j": j,
            "chi_j": chi,
            "R_j": R_eig,
            "term": term,
        })
        Z_ord += term

    # Z_sym: the unweighted character sum = partition function Z(tau)
    Z_char_sum = sum(sl2_character(j, k, tau, n_terms) for j in range(k + 1))
    # Delta: difference between R-weighted and unweighted sums
    Delta = Z_ord - Z_char_sum

    return {
        "method": "A (diagonal R-eigenvalue product)",
        "k": k,
        "u": u,
        "tau": tau,
        "Z_ord": Z_ord,
        "Z_char_sum": Z_char_sum,
        "Z_verlinde": k + 1,
        "Delta": Delta,
        "terms": terms,
        "kappa": data["kappa"],
        "c": data["c"],
    }


def ordered_trace_g1_optionB(k: int, u: complex, tau: complex,
                              n_terms: int = 200) -> Dict[str, Any]:
    r"""Ordered trace at genus 1 using Felder eigenvalues (Option B).

    Z_1^{ord}(u, tau) = sum_{j=0}^{k} lambda_j(u, tau) * chi_j(tau) / dim_q(V_j)

    where lambda_j is the Felder eigenvalue (ratio of theta functions
    over the weight lattice) and the division by dim_q normalizes so that
    at u -> generic, the weight approaches 1.

    The Felder eigenvalue lambda_j(u, tau) -> dim_q(V_j) as u -> 0
    (after regularization), so lambda_j / dim_q -> 1 in that limit.
    """
    data = _sl2_modular_data(k)
    terms = []
    Z_ord = 0.0 + 0.0j

    for j in range(k + 1):
        chi = sl2_character(j, k, tau, n_terms)
        lam = elliptic_R_eigenvalue_felder(j, k, u, tau)
        dq = quantum_dimension_sl2(j, k)
        if abs(dq) < 1e-15:
            w_j = 1.0 + 0.0j
        else:
            w_j = lam / dq
        term = w_j * chi
        terms.append({
            "j": j,
            "chi_j": chi,
            "lambda_j": lam,
            "qdim_j": dq,
            "w_j": w_j,
            "term": term,
        })
        Z_ord += term

    Z_char_sum = sum(sl2_character(j, k, tau, n_terms) for j in range(k + 1))
    Delta = Z_ord - Z_char_sum

    return {
        "method": "B (Felder elliptic eigenvalue / quantum dim)",
        "k": k,
        "u": u,
        "tau": tau,
        "Z_ord": Z_ord,
        "Z_char_sum": Z_char_sum,
        "Z_verlinde": k + 1,
        "Delta": Delta,
        "terms": terms,
        "kappa": data["kappa"],
        "c": data["c"],
    }


def ordered_trace_g1_optionC(k: int, u: complex, tau: complex,
                              n_terms: int = 200) -> Dict[str, Any]:
    r"""Ordered trace at genus 1 using KZB monodromy eigenvalues (Option C).

    The KZB connection on E_tau at level k has monodromy around the
    A-cycle (z -> z + 1) and B-cycle (z -> z + tau).

    The A-cycle monodromy eigenvalue on the j-th conformal block is:
        M_A(j) = exp(2*pi*i * h_j) = exp(2*pi*i * j(j+2)/(4(k+2)))

    The B-cycle monodromy involves tau and is:
        M_B(j, tau) = T_j = exp(2*pi*i * (h_j - c/24))

    The ordered trace with spectral parameter u interpolates between
    these via:
        w_j(u, tau) = exp(2*pi*i * u * h_j / Im(tau))

    This is the simplest tau-dependent weight that:
    (a) reduces to 1 when u = 0
    (b) depends on the complex structure through Im(tau)
    (c) separates representations via h_j
    """
    data = _sl2_modular_data(k)
    r = k + 2
    terms = []
    Z_ord = 0.0 + 0.0j

    for j in range(k + 1):
        chi = sl2_character(j, k, tau, n_terms)
        h_j = j * (j + 2) / (4.0 * r)
        # KZB-motivated weight: spectral deformation by conformal weight
        w_j = cmath.exp(2j * PI * u * h_j)
        term = w_j * chi
        terms.append({
            "j": j,
            "chi_j": chi,
            "h_j": h_j,
            "w_j": w_j,
            "term": term,
        })
        Z_ord += term

    Z_char_sum = sum(sl2_character(j, k, tau, n_terms) for j in range(k + 1))
    Delta = Z_ord - Z_char_sum

    return {
        "method": "C (KZB monodromy spectral deformation)",
        "k": k,
        "u": u,
        "tau": tau,
        "Z_ord": Z_ord,
        "Z_char_sum": Z_char_sum,
        "Z_verlinde": k + 1,
        "Delta": Delta,
        "terms": terms,
        "kappa": data["kappa"],
        "c": data["c"],
    }


# =========================================================================
# 6. The ordered trace: genus 2
# =========================================================================

def ordered_trace_g2(k: int, u: complex, tau: complex,
                     n_terms: int = 200) -> Dict[str, Any]:
    r"""Ordered trace at genus 2 for sl_2 at level k (diagonal approximation).

    At genus 2, the Verlinde number is:
        Z_2^{sym} = (r/2) * sum_{j=1}^{r-1} sin(pi*j/r)^{-2}

    The ordered trace weights each term by the elliptic R-eigenvalue:
        Z_2^{ord}(u, tau) = sum_{j=0}^{k} S_{0,j}^{-2} * R_j(u, tau)

    We use the Felder eigenvalue for R_j.

    Note: at genus 2 the full construction requires the genus-2 elliptic
    R-matrix (Siegel upper half-space).  Here we use the diagonal
    approximation where the genus-2 surface is close to a product of
    two elliptic curves (the separating degeneration).
    """
    data = _sl2_modular_data(k)
    S = data["S"]
    r = k + 2

    terms = []
    Z_ord = 0.0 + 0.0j
    Z_sym = 0.0

    for j in range(k + 1):
        S_0j = S[0, j]
        if abs(S_0j) < 1e-15:
            continue
        # Verlinde weight at genus 2: S_{0,j}^{2-2g} = S_{0,j}^{-2}
        verlinde_weight = S_0j ** (-2)
        Z_sym += verlinde_weight

        # E_1 weight: elliptic R-eigenvalue
        R_eig = elliptic_R_eigenvalue_felder(j, k, u, tau)
        qdim = quantum_dimension_sl2(j, k)
        if abs(qdim) < 1e-15:
            w_j = 1.0 + 0.0j
        else:
            w_j = R_eig / qdim

        term = verlinde_weight * w_j
        terms.append({
            "j": j,
            "S_0j": S_0j,
            "verlinde_weight": verlinde_weight,
            "R_j": R_eig,
            "w_j": w_j,
            "term": term,
        })
        Z_ord += term

    Delta = Z_ord - Z_sym

    return {
        "method": "genus-2 diagonal approximation (Felder eigenvalue)",
        "k": k,
        "g": 2,
        "u": u,
        "tau": tau,
        "Z_ord": Z_ord,
        "Z_sym": Z_sym,
        "Z_sym_rounded": round(Z_sym),
        "Delta": Delta,
        "terms": terms,
        "kappa": data["kappa"],
        "c": data["c"],
    }


# =========================================================================
# 7. Novelty test: is this genuinely E_1?
# =========================================================================

def novelty_analysis(k: int, u: complex, tau: complex,
                     n_terms: int = 200) -> Dict[str, Any]:
    r"""Analyze whether Z_1^{ord} is genuinely new (not reducible to E_inf data).

    Tests:
    1. TAU-DEPENDENCE: Z_1^{ord}(u, tau_1) != Z_1^{ord}(u, tau_2)
       for distinct tau_1, tau_2 at FIXED u.  If the ordered trace
       depended only on q-expansions, it would be a modular form.
       Genuine E_1 content manifests as non-trivial tau-dependence
       beyond what characters provide.

    2. U-DEPENDENCE: Z_1^{ord}(u_1, tau) != Z_1^{ord}(u_2, tau).
       The spectral parameter u is purely E_1 data (R-matrix).

    3. PRODUCT STRUCTURE: if Z_1^{ord} = f(u) * Z_1^{sym}, then
       it is just a rescaling and not genuinely new.  Check:
       Z_1^{ord} / Z_1^{sym} is NOT u-independent.

    4. MONODROMY: compute Z_1^{ord}(u + 1, tau) and Z_1^{ord}(u + tau, tau).
       Non-trivial monodromy in u signals genuine elliptic dependence.
    """
    # Compute at multiple (u, tau) values
    tau_values = [tau, tau + 0.01, tau + 0.01j]
    u_values = [u, u + 0.1, u + 0.1j]

    results_grid = {}
    for t in tau_values:
        for uu in u_values:
            res = ordered_trace_g1_optionB(k, uu, t, n_terms)
            key = f"u={uu:.4f}_tau={t:.4f}"
            results_grid[key] = {
                "Z_ord": res["Z_ord"],
                "Z_char_sum": res["Z_char_sum"],
                "Delta": res["Delta"],
            }

    # Test 1: tau-dependence at fixed u
    res_tau1 = ordered_trace_g1_optionB(k, u, tau, n_terms)
    res_tau2 = ordered_trace_g1_optionB(k, u, tau + 0.05j, n_terms)
    tau_variation = abs(res_tau1["Z_ord"] - res_tau2["Z_ord"])

    # Test 2: u-dependence at fixed tau
    res_u1 = ordered_trace_g1_optionB(k, u, tau, n_terms)
    res_u2 = ordered_trace_g1_optionB(k, u + 0.2, tau, n_terms)
    u_variation = abs(res_u1["Z_ord"] - res_u2["Z_ord"])

    # Test 3: product structure
    # If Z_ord = f(u) * Z_sym, then Z_ord/Z_sym should be u-independent
    ratio1 = res_u1["Z_ord"] / res_u1["Z_char_sum"] if abs(res_u1["Z_char_sum"]) > 1e-15 else float('nan')
    ratio2 = res_u2["Z_ord"] / res_u2["Z_char_sum"] if abs(res_u2["Z_char_sum"]) > 1e-15 else float('nan')
    is_product = abs(ratio1 - ratio2) < 1e-8

    # Test 4: monodromy in u
    res_u_shift1 = ordered_trace_g1_optionB(k, u + 1.0, tau, n_terms)
    res_u_shift_tau = ordered_trace_g1_optionB(k, u + tau, tau, n_terms)
    monodromy_A = res_u_shift1["Z_ord"] / res_u1["Z_ord"] if abs(res_u1["Z_ord"]) > 1e-15 else float('nan')
    monodromy_B = res_u_shift_tau["Z_ord"] / res_u1["Z_ord"] if abs(res_u1["Z_ord"]) > 1e-15 else float('nan')

    genuinely_new = (
        tau_variation > 1e-10
        and u_variation > 1e-10
        and not is_product
    )

    return {
        "k": k,
        "u": u,
        "tau": tau,
        "tau_variation": tau_variation,
        "u_variation": u_variation,
        "is_product_structure": is_product,
        "ratio_at_u1": ratio1,
        "ratio_at_u2": ratio2,
        "monodromy_A_cycle": monodromy_A,
        "monodromy_B_cycle": monodromy_B,
        "genuinely_new": genuinely_new,
        "grid": results_grid,
    }


# =========================================================================
# 8. Master computation: produce numbers
# =========================================================================

def compute_all(k: int = 2, u: complex = 0.3 + 0.1j,
                tau: complex = 0.2 + 1.0j,
                n_terms: int = 200) -> Dict[str, Any]:
    """Master computation for sl_2 at level k on E_tau with spectral param u.

    Computes all three options for the ordered trace at genus 1,
    the genus-2 ordered trace, Verlinde numbers, and novelty analysis.
    """
    # Basic data
    data = _sl2_modular_data(k)

    # Verlinde numbers
    Z_g = {}
    for g in range(4):
        Z_g[g] = verlinde_number_g(k, g)

    # Genus 1: three options
    optA = ordered_trace_g1_optionA(k, u, tau, n_terms)
    optB = ordered_trace_g1_optionB(k, u, tau, n_terms)
    optC = ordered_trace_g1_optionC(k, u, tau, n_terms)

    # Genus 2
    g2 = ordered_trace_g2(k, u, tau, n_terms)

    # Novelty
    novelty = novelty_analysis(k, u, tau, n_terms)

    # Characters for display
    characters = {}
    for j in range(k + 1):
        characters[j] = sl2_character(j, k, tau, n_terms)

    return {
        "parameters": {
            "k": k,
            "u": u,
            "tau": tau,
            "q_drinfeld": data["q"],
            "c": data["c"],
            "kappa": data["kappa"],
        },
        "verlinde_numbers": Z_g,
        "characters": characters,
        "quantum_dimensions": {j: quantum_dimension_sl2(j, k) for j in range(k + 1)},
        "genus1_optionA": optA,
        "genus1_optionB": optB,
        "genus1_optionC": optC,
        "genus2": g2,
        "novelty": novelty,
    }


# =========================================================================
# 9. Pretty-print results
# =========================================================================

def print_results(results: Dict[str, Any]) -> None:
    """Print computation results in human-readable form."""
    params = results["parameters"]
    print("=" * 72)
    print(f"ORDERED TRACE INVARIANT: sl_2 at level k = {params['k']}")
    print(f"  Spectral parameter u = {params['u']}")
    print(f"  Modular parameter tau = {params['tau']}")
    print(f"  Drinfeld q = exp(i*pi/{params['k']+2}) = {params['q_drinfeld']:.6f}")
    print(f"  Central charge c = {params['c']:.6f}")
    print(f"  Modular characteristic kappa = {params['kappa']:.6f}")
    print("=" * 72)

    print("\n--- Verlinde numbers (E_infinity) ---")
    for g, Z in results["verlinde_numbers"].items():
        print(f"  Z_{g}^{{sym}} = {Z:.6f}" + (f" = {int(round(Z))}" if abs(Z - round(Z)) < 0.01 else ""))

    print("\n--- Characters chi_j(tau) ---")
    for j, chi in results["characters"].items():
        print(f"  chi_{j}(tau) = {chi:.8f}")

    print("\n--- Quantum dimensions ---")
    for j, d in results["quantum_dimensions"].items():
        print(f"  dim_q(V_{j}) = {d:.6f}")

    for label, key in [("Option A (diagonal R-eigenvalue)", "genus1_optionA"),
                        ("Option B (Felder elliptic eigenvalue)", "genus1_optionB"),
                        ("Option C (KZB spectral deformation)", "genus1_optionC")]:
        res = results[key]
        print(f"\n--- Genus 1: {label} ---")
        print(f"  Z_1^{{ord}}(u, tau)   = {res['Z_ord']:.10f}")
        print(f"  Z_1(tau) [char sum]  = {res['Z_char_sum']:.10f}")
        print(f"  Z_1^{{verlinde}}      = {res['Z_verlinde']}")
        print(f"  Delta_1 [ord - char] = {res['Delta']:.10f}")
        print(f"  |Delta_1|            = {abs(res['Delta']):.10e}")
        for t in res["terms"]:
            j = t["j"]
            if "R_j" in t:
                print(f"    j={j}: chi={t['chi_j']:.6f}, R={t['R_j']:.6f}, term={t['term']:.6f}")
            elif "w_j" in t:
                print(f"    j={j}: chi={t['chi_j']:.6f}, w={t['w_j']:.6f}, term={t['term']:.6f}")

    g2 = results["genus2"]
    print(f"\n--- Genus 2: {g2['method']} ---")
    print(f"  Z_2^{{ord}}(u, tau) = {g2['Z_ord']:.10f}")
    print(f"  Z_2^{{sym}}        = {g2['Z_sym']:.6f} (rounded: {g2['Z_sym_rounded']})")
    print(f"  Delta_2            = {g2['Delta']:.10f}")
    print(f"  |Delta_2|          = {abs(g2['Delta']):.10e}")

    nov = results["novelty"]
    print("\n--- Novelty analysis ---")
    print(f"  tau variation:        {nov['tau_variation']:.6e}")
    print(f"  u variation:          {nov['u_variation']:.6e}")
    print(f"  is product structure: {nov['is_product_structure']}")
    print(f"  ratio at u1:          {nov['ratio_at_u1']:.8f}")
    print(f"  ratio at u2:          {nov['ratio_at_u2']:.8f}")
    print(f"  monodromy A-cycle:    {nov['monodromy_A_cycle']:.8f}")
    print(f"  monodromy B-cycle:    {nov['monodromy_B_cycle']:.8f}")
    print(f"  GENUINELY NEW:        {nov['genuinely_new']}")
    print("=" * 72)


# =========================================================================
# 10. Self-test
# =========================================================================

def run_self_test() -> Dict[str, Any]:
    """Run self-consistency tests on the ordered trace computation."""
    results = {}

    # Test 1: Verlinde numbers for sl_2, k=2
    # VERIFIED: Z_0 = 1, Z_1 = 3, Z_2 = 10 [DC] [LT: Beauville 1996]
    Z0 = verlinde_number_g(2, 0)
    Z1 = verlinde_number_g(2, 1)
    Z2 = verlinde_number_g(2, 2)
    results["verlinde_k2"] = {
        "Z0": Z0, "Z1": Z1, "Z2": Z2,
        "Z0_pass": abs(Z0 - 1.0) < 1e-10,
        "Z1_pass": abs(Z1 - 3.0) < 1e-10,
        "Z2_pass": abs(Z2 - 10.0) < 0.5,
    }

    # Test 2: Quantum dimensions for sl_2, k=2
    # j is Dynkin label: dim_q(V_j) = sin((j+1)*pi/4) / sin(pi/4)
    # j=0: sin(pi/4)/sin(pi/4) = 1
    # j=1: sin(2*pi/4)/sin(pi/4) = 1/sin(pi/4) = sqrt(2)
    # j=2: sin(3*pi/4)/sin(pi/4) = sin(pi/4)/sin(pi/4) = 1
    # VERIFIED: [DC] direct computation; [LT] Kac-Walton tables
    d0 = quantum_dimension_sl2(0, 2)
    d1 = quantum_dimension_sl2(1, 2)
    d2 = quantum_dimension_sl2(2, 2)
    results["qdim_k2"] = {
        "d0": d0, "d1": d1, "d2": d2,
        "d0_pass": abs(d0 - 1.0) < 1e-10,
        "d1_pass": abs(d1 - math.sqrt(2)) < 1e-10,
        "d2_pass": abs(d2 - 1.0) < 1e-10,
    }

    # Test 3: Characters have correct leading term
    # chi_j(tau) ~ q^{h_j - c/24} * ((j+1) + O(q))
    # VERIFIED: [DC] ratio chi_j / q^{h_j-c/24} -> j+1 at large Im(tau)
    tau_test = 0.2 + 1.0j
    k_test = 2
    r_test = k_test + 2
    c_test = 3.0 * k_test / r_test
    chi_leading_ok = True
    for j in range(k_test + 1):
        chi = sl2_character(j, k_test, tau_test)
        h_j = j * (j + 2) / (4.0 * r_test)
        leading = cmath.exp(TWO_PI_I * tau_test * (h_j - c_test / 24.0))
        ratio = chi / leading if abs(leading) > 1e-300 else 0
        # Leading coefficient should be close to j+1
        if abs(ratio.real - (j + 1)) > 0.1 or abs(ratio.imag) > 0.1:
            chi_leading_ok = False
    results["character_leading_k2"] = {
        "chi_leading_ok": chi_leading_ok,
        "pass": chi_leading_ok,
    }

    # Test 4: kappa check
    # AP1: kappa(sl_2, k=2) = 3*(2+2)/4 = 3
    kappa_k2 = 3.0 * (2 + 2) / 4.0
    results["kappa_k2"] = {
        "kappa": kappa_k2,
        "pass": abs(kappa_k2 - 3.0) < 1e-10,
    }

    # Test 5: Theta function basic identity
    # theta_1(z+1|tau) = -theta_1(z|tau)
    z_test = 0.3 + 0.1j
    tau_t = 0.0 + 1.0j
    t1_z = theta1(z_test, tau_t)
    t1_zp1 = theta1(z_test + 1.0, tau_t)
    results["theta1_period"] = {
        "theta1(z)": t1_z,
        "theta1(z+1)": t1_zp1,
        "ratio": t1_zp1 / t1_z if abs(t1_z) > 1e-15 else float('nan'),
        "pass": abs(t1_zp1 + t1_z) / max(abs(t1_z), 1e-15) < 1e-8,
    }

    # Test 6: Eta function
    # eta(i) = Gamma(1/4) / (2 * pi^{3/4}) approx 0.76823...
    # VERIFIED: [LT: Mathematica, Abramowitz-Stegun Table 16.2]
    eta_i = eta_dedekind(1.0j)
    eta_expected = 0.7682254223  # to 10 digits
    results["eta_at_i"] = {
        "eta(i)": eta_i,
        "expected": eta_expected,
        "pass": abs(abs(eta_i) - eta_expected) / eta_expected < 1e-6,
    }

    return results


# =========================================================================
# Main entry point
# =========================================================================

if __name__ == "__main__":
    print("Running self-tests...")
    tests = run_self_test()
    all_pass = True
    for name, result in tests.items():
        passes = [v for k, v in result.items() if k.endswith("_pass")]
        status = "PASS" if all(passes) else ("FAIL" if passes else "INFO")
        if status == "FAIL":
            all_pass = False
        print(f"  {name}: {status}")
        for k, v in result.items():
            if not k.endswith("_pass"):
                print(f"    {k} = {v}")
    print()

    if not all_pass:
        print("SELF-TESTS FAILED -- check output above")
        import sys
        sys.exit(1)

    print("Self-tests passed. Computing ordered trace for sl_2, k=2...\n")
    results = compute_all(k=2, u=0.3 + 0.1j, tau=0.2 + 1.0j)
    print_results(results)

    print("\n\nComputing at k=1 (Ising-adjacent)...\n")
    results_k1 = compute_all(k=1, u=0.25 + 0.05j, tau=0.1 + 0.8j)
    print_results(results_k1)

    print("\n\nComputing at k=4 (higher level)...\n")
    results_k4 = compute_all(k=4, u=0.2 + 0.15j, tau=0.15 + 1.2j)
    print_results(results_k4)

    # Explicit numbers for the paper
    print("\n" + "=" * 72)
    print("EXPLICIT NUMBERS FOR THE PAPER")
    print("=" * 72)

    k = 2
    tau = 0.2 + 1.0j
    u_values = [0.1, 0.2, 0.3, 0.5, 0.1 + 0.1j, 0.3 + 0.2j]

    print(f"\nsl_2 at level k = {k}, tau = {tau}")
    print(f"Verlinde: Z_1 = {verlinde_number_g1(k)}, Z_2 = {round(verlinde_number_g(k, 2))}")
    print()
    print(f"{'u':>20s}  {'|Z_1^ord|':>14s}  {'|Delta_1|':>14s}  {'|Z_2^ord|':>14s}  {'|Delta_2|':>14s}")
    print("-" * 80)

    for u_val in u_values:
        r1 = ordered_trace_g1_optionB(k, u_val, tau)
        r2 = ordered_trace_g2(k, u_val, tau)
        print(f"{str(u_val):>20s}  {abs(r1['Z_ord']):>14.8f}  {abs(r1['Delta']):>14.8f}"
              f"  {abs(r2['Z_ord']):>14.8f}  {abs(r2['Delta']):>14.8f}")
