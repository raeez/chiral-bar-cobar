r"""Lattice integrable model shadows: XXX, XXZ, XYZ spin chains.

Computes shadow obstruction tower invariants for the continuum limits of integrable
spin chains, bridging the modular Koszul duality engine to the most
concrete physical systems in condensed matter and statistical mechanics.

THE DICTIONARY:
    Integrable spin chain <-> Chiral algebra (continuum limit) <-> Shadow obstruction tower

    XXX (Heisenberg magnet):
        H = -J sum S_i . S_{i+1}
        Continuum limit: V_1(sl_2) (SU(2) WZW at level 1)
        c = 1, kappa = 9/4 (on current line), class L
        Shadow: alpha = 1, S_4 = 0, tower terminates at arity 3

    XXZ (anisotropic Heisenberg):
        H = -sum (S^x S^x + S^y S^y + Delta S^z S^z), Delta = cos(pi nu)
        Continuum limit: compactified boson / Coulomb gas
        c = 1 - 6(1-nu)^2/nu
        For nu = p/(p+1): unitary minimal model M(p, p+1)
        For general nu: Heisenberg at effective level with compactification

    XYZ (fully anisotropic):
        H = sum (J_x S^x S^x + J_y S^y S^y + J_z S^z S^z)
        Continuum limit: related to Virasoro via 8-vertex / SOS model
        c determined by elliptic modular parameter tau
        Shadow involves quasi-modular forms (AP15: E_2* is quasi-modular!)

TRANSFER MATRIX <-> SHADOW DICTIONARY:
    The transfer matrix T(u) = tr_a prod_i R_{ai}(u) encodes integrability.
    log T(u) = sum_n I_n u^{n-1} / (n-1)! where I_n are conserved charges.

    I_1 = total momentum (translation generator)
    I_2 = Hamiltonian (energy)
    I_3 = third conserved charge (relates to cubic shadow)
    I_n = nth conserved charge (relates to S_n shadow coefficient)

    The precise dictionary (for XXX at level k):
        kappa = (energy density normalization) * dim(g)(k+h^v)/(2h^v)
        S_3   = (I_3 density normalization) * (Lie bracket contribution)
        S_4   = 0 (Jacobi identity kills quartic for Lie-type)

FINITE SIZE CORRECTIONS (Cardy formula and beyond):
    E_n(L) = e_inf * L + 2*pi*v_F/L * (x_n - c/24) + O(1/L^2)

    where x_n = scaling dimension, c = central charge.
    The O(1/L^2) correction involves the shadow:
        f_n^{(2)} = kappa * irrelevant_coupling + ...

BETHE ANSATZ:
    For XXX with L sites and M down-spins (half-filling M = L/2):
    E = -J * sum_{i=1}^M 2/(u_i^2 + 1/4) where u_i = Bethe roots

    Thermodynamic limit E/L -> e_inf involves kappa through:
    F_1 = kappa/24 (the first shadow free energy = finite-size correction)

R-MATRIX AND SHADOW:
    The trigonometric R-matrix of XXZ:
        R(u, gamma) = [sin(u+gamma) P + sin(u)(1-P)] / sin(gamma)
    decomposes as R = 1 + sin(u)/sin(gamma) * (P - 1)

    In the u -> 0 limit: R(u) ~ 1 + u * r where r = P / sin(gamma)
    The classical r-matrix is r(u) = Omega / u (collision residue).

    The elliptic R-matrix (XYZ / 8-vertex):
        Uses Jacobi theta functions theta_i(u | tau).
    In the trigonometric limit tau -> i*infty: theta_1/theta_4 -> sin.

CAUTION (AP1): kappa formulas are family-specific.
    kappa(V_k(sl_2)) = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4.  NOT c/2.
    kappa(Heis_k) = k.  NOT k/2.
    kappa(Vir_c) = c/2.

CAUTION (AP15): XYZ shadow involves E_2* (quasi-modular), NOT holomorphic
    modular forms.  The genus-1 propagator is E_2*, and products of E_2*
    are quasi-modular polynomials in {E_2*, E_4, E_6}.

CAUTION (AP19): The r-matrix r(z) from the collision residue has pole
    orders ONE LESS than the OPE, because d log(z-w) absorbs a pole.
    For affine sl_2: OPE has z^{-2} and z^{-1}; r-matrix has z^{-1} only.

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    full_shadow_landscape.py: shadow_tower_coefficients, affine_data
    quantum_group_shadow.py: ClassicalRMatrix, affine_sl2_r_matrix
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from sympy import (
    Abs,
    E as sym_E,
    I,
    Matrix,
    Rational,
    Symbol,
    bernoulli,
    cancel,
    cos,
    exp,
    expand,
    factorial,
    log,
    pi,
    simplify,
    sin,
    sqrt,
    symbols,
    oo,
    S,
)


# =========================================================================
# 0. Constants and symbols
# =========================================================================

k_sym = Symbol('k', positive=True)
c_sym = Symbol('c')
gamma_sym = Symbol('gamma', positive=True)
nu_sym = Symbol('nu', positive=True)
L_sym = Symbol('L', positive=True, integer=True)
u_sym = Symbol('u')
tau_sym = Symbol('tau')


# =========================================================================
# 1. XXX spin chain: V_1(sl_2) shadow obstruction tower
# =========================================================================

def xxx_continuum_data() -> Dict[str, Any]:
    r"""Shadow data for XXX spin chain continuum limit = V_1(sl_2).

    The XXX Heisenberg magnet H = -J sum S_i . S_{i+1} has continuum
    limit the SU(2) WZW model at level k=1, i.e. V_1(sl_2).

    For V_k(sl_2): dim(sl_2) = 3, h^v = 2.
        c = 3k/(k+2)
        kappa = 3(k+2)/4    (on the current/Lie algebra line)
        kappa_T = c/2        (on the T/Sugawara line)

    At k=1:
        c = 3*1/3 = 1
        kappa = 3*3/4 = 9/4  (current line)
        kappa_T = 1/2         (T-line)

    CAUTION (AP1): kappa = 9/4, NOT 1/2.
    kappa = 1/2 would be the Virasoro (T-line) value.
    The full affine sl_2 algebra has kappa = 9/4 because it
    includes the three-dimensional Lie algebra structure.

    Shadow class: L (Lie/tree, tower terminates at arity 3).
    alpha = 1 (on current line, from Lie bracket).
    S_4 = 0 (killed by Jacobi identity).

    Returns shadow data dict with both current-line and T-line data.
    """
    k = 1
    dim_g = 3
    h_vee = 2
    c = Rational(dim_g * k, k + h_vee)  # 3*1/3 = 1
    kappa_current = Rational(dim_g * (k + h_vee), 2 * h_vee)  # 3*3/4 = 9/4
    alpha_current = Rational(1)  # universal for affine KM on current line
    S4_current = Rational(0)  # Jacobi identity

    # T-line (Sugawara stress tensor) data
    kappa_T = c / 2  # = 1/2
    alpha_T = Rational(2)  # universal for Virasoro / T-line
    S4_T = Rational(10) / (c * (5 * c + 22))  # = 10/27

    return {
        'chain': 'XXX',
        'algebra': 'V_1(sl_2)',
        'c': c,
        'k': Rational(k),
        'dim_g': dim_g,
        'h_vee': h_vee,
        # Current line (Lie algebra directions)
        'kappa_current': kappa_current,
        'alpha_current': alpha_current,
        'S4_current': S4_current,
        'class_current': 'L',
        # T-line (Sugawara / stress tensor)
        'kappa_T': kappa_T,
        'alpha_T': alpha_T,
        'S4_T': S4_T,
        'class_T': 'M',
        # Koszul dual: V_{-5}(sl_2) (k' = -k - 2*h^v = -5)
        'k_dual': Rational(-5),
    }


def xxx_shadow_tower(max_r: int = 20, line: str = 'current') -> Dict[int, Rational]:
    r"""Shadow obstruction tower coefficients for XXX chain (V_1(sl_2)).

    On the current line: class L, terminates at arity 3.
        S_2 = kappa = 9/4
        S_3 = alpha/3 = 1/3
        S_r = 0 for r >= 4

    On the T-line: class M, infinite tower.
        S_2 = 1/2, S_3 = alpha_T/3 = 2/3
        S_4 = 10/27 / 4 = 5/54
        ... (infinite, from Virasoro shadow with c=1)

    The S_r = a_{r-2}/r formula.
    """
    data = xxx_continuum_data()
    if line == 'current':
        kappa = data['kappa_current']
        alpha = data['alpha_current']
        S4 = data['S4_current']
    elif line == 'T':
        kappa = data['kappa_T']
        alpha = data['alpha_T']
        S4 = data['S4_T']
    else:
        raise ValueError(f"Unknown line: {line}. Use 'current' or 'T'.")
    return _shadow_tower_from_data(kappa, alpha, S4, max_r)


def _shadow_tower_from_data(
    kappa: Rational,
    alpha: Rational,
    S4: Rational,
    max_r: int = 20,
) -> Dict[int, Rational]:
    r"""Compute shadow obstruction tower coefficients S_2, ..., S_{max_r}.

    From the shadow metric Q_L(t) = q0 + q1*t + q2*t^2:
        q0 = 4*kappa^2, q1 = 12*kappa*alpha, q2 = 9*alpha^2 + 16*kappa*S4

    H(t) = t^2 * sqrt(Q_L(t)), and S_r = a_{r-2}/r
    where a_n are Taylor coefficients of sqrt(Q_L(t)).

    Recursion:
        a_0 = 2*kappa (signed)
        a_1 = q1/(2*a_0) = 3*alpha
        a_2 = (q2 - a_1^2)/(2*a_0) = 4*S4
        a_n = -(sum_{j=1}^{n-1} a_j*a_{n-j}) / (2*a_0)  for n >= 3
    """
    if kappa == 0:
        raise ValueError("kappa = 0: uncurved, shadow obstruction tower undefined")

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    a0 = 2 * kappa
    a = [a0]

    max_n = max_r - 2

    if max_n >= 1:
        a.append(q1 / (2 * a0))  # = 3*alpha

    if max_n >= 2:
        a.append((q2 - a[1] ** 2) / (2 * a0))  # = 4*S4

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))

    result = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = Rational(a[idx], r) if isinstance(a[idx], int) else a[idx] / r

    return result


def xxx_kappa() -> Rational:
    """kappa for XXX chain = V_1(sl_2) on current line = 9/4."""
    return Rational(9, 4)


def xxx_central_charge() -> Rational:
    """Central charge c = 1 for XXX = V_1(sl_2)."""
    return Rational(1)


def xxx_f1() -> Rational:
    r"""First genus free energy F_1 = kappa * lambda_1^FP.

    lambda_1 = (2^1 - 1)/(2^1) * |B_2|/(2!) = 1/2 * 1/6 / 2 = 1/24.
    Wait: lambda_1^FP = (2^{2*1-1} - 1) / 2^{2*1-1} * |B_{2}| / (2)!
                       = (2-1)/2 * (1/6) / 2 = 1/2 * 1/6 / 2

    Actually: lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!

    For g=1: lambda_1 = (2^1-1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24.

    F_1 = kappa * 1/24 = 9/4 * 1/24 = 9/96 = 3/32 (current line).

    On the T-line: F_1 = 1/2 * 1/24 = 1/48.
    """
    return Rational(9, 4) * Rational(1, 24)


def xxx_f1_tline() -> Rational:
    """F_1 on the T-line = kappa_T * lambda_1 = 1/2 * 1/24 = 1/48."""
    return Rational(1, 48)


# =========================================================================
# 2. XXZ spin chain: shadow as function of anisotropy
# =========================================================================

def xxz_central_charge(nu: Any) -> Any:
    r"""Central charge for XXZ chain with anisotropy Delta = cos(pi*nu).

    The standard result (Coulomb gas / compactified boson):
        c = 1 - 6*(1 - nu)^2 / nu

    where Delta = cos(pi*nu), 0 < nu < 1 for the critical regime |Delta| < 1.

    Special cases:
        nu = 1: c = 1 (XXX limit, Delta = -1 antiferromagnetic)
        nu -> 0: c -> -inf (Delta -> 1, ferromagnetic)
        nu = p/(p+1): c = 1 - 6/[p(p+1)] (unitary minimal model M(p,p+1))

    NOTE: The XXX chain (isotropic, Delta = 1) is NOT the nu -> 0 limit;
    the XXX chain has a DIFFERENT continuum limit (SU(2)_1 WZW, c=1).
    The Coulomb gas formula applies to |Delta| < 1 only.
    The XXX antiferromagnet (Delta = 1 in the standard convention
    with H = -sum S.S) also has c = 1 but via SU(2) symmetry enhancement.
    """
    return 1 - 6 * (1 - nu) ** 2 / nu


def xxz_central_charge_rational(p: int) -> Rational:
    r"""Central charge at the rational point nu = p/(p+1).

    c = 1 - 6/[p(p+1)] for the unitary minimal model M(p, p+1).

    p=2: c = 1/2 (Ising model)
    p=3: c = 7/10 (tricritical Ising)
    p=4: c = 4/5 (3-state Potts)
    p=5: c = 6/7
    """
    return Rational(1) - Rational(6, p * (p + 1))


def xxz_kappa_virasoro(nu: Any) -> Any:
    r"""kappa on the Virasoro (T) line for XXZ at coupling nu.

    kappa_T = c/2 = [1 - 6(1-nu)^2/nu] / 2
    """
    c = xxz_central_charge(nu)
    return c / 2


def xxz_shadow_data(nu: Any) -> Dict[str, Any]:
    r"""Full shadow data for XXZ chain at coupling parameter nu.

    Delta_anisotropy = cos(pi*nu), 0 < nu < 1.

    The continuum limit is a compactified boson (Coulomb gas).
    On the Virasoro (T) line:
        kappa = c/2
        alpha = 2 (universal gravitational)
        S_4 = 10/[c(5c+22)] (universal Virasoro quartic)

    The shadow class is M (mixed, infinite tower) whenever S_4 != 0,
    which holds for all c != 0.

    For the unitary minimal models (nu = p/(p+1)):
        c = 1 - 6/[p(p+1)]
        These are QUOTIENTS of the Virasoro algebra, so the shadow
        tower is that of Virasoro at the appropriate c.
    """
    c = xxz_central_charge(nu)
    kappa = c / 2
    alpha = 2  # universal on T-line
    S4 = 10 / (c * (5 * c + 22)) if c != 0 else None
    return {
        'chain': 'XXZ',
        'nu': nu,
        'Delta_anisotropy': None,  # cos(pi*nu), symbolic
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'M' if S4 is not None and S4 != 0 else 'G',
    }


def xxz_shadow_data_rational(p: int) -> Dict[str, Any]:
    r"""Shadow data at the rational point nu = p/(p+1).

    Produces exact rational values for the unitary minimal model M(p, p+1).
    """
    c = xxz_central_charge_rational(p)
    kappa = c / 2
    alpha = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    return {
        'chain': 'XXZ',
        'p': p,
        'nu': Rational(p, p + 1),
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'M',
    }


def xxz_shadow_tower_rational(p: int, max_r: int = 20) -> Dict[int, Rational]:
    r"""Shadow obstruction tower for XXZ at rational point nu = p/(p+1).

    This is the Virasoro shadow obstruction tower at c = 1 - 6/[p(p+1)].
    """
    data = xxz_shadow_data_rational(p)
    return _shadow_tower_from_data(data['kappa'], data['alpha'], data['S4'], max_r)


# =========================================================================
# 3. XYZ spin chain: elliptic shadow
# =========================================================================

def xyz_central_charge(J_x: float, J_y: float, J_z: float) -> float:
    r"""Central charge for XYZ chain (Baxter's 8-vertex model).

    The XYZ chain H = sum (J_x S^x S^x + J_y S^y S^y + J_z S^z S^z)
    in the critical regime is related to the Virasoro algebra through
    the elliptic parametrization.

    Parametrize: J_x = 1, J_y = cn(2K*gamma/pi, k_ell), J_z = dn(2K*gamma/pi, k_ell)
    where k_ell is the elliptic modulus and K = K(k_ell) is the complete
    elliptic integral.

    The modular parameter tau = iK'/K where K' = K(k_ell').

    Central charge: c = 1 - 6*(1 - nu)^2/nu where nu = nu(tau).

    For generic (J_x, J_y, J_z) with |J_z| <= max(|J_x|, |J_y|):
    c is determined by the anisotropy ratios.

    Simplified computation: when (J_x, J_y, J_z) = (1, 1, Delta),
    this reduces to XXZ with anisotropy Delta.

    For the fully anisotropic case, we need the elliptic nome.
    """
    # Normalize so largest coupling = 1
    J_max = max(abs(J_x), abs(J_y), abs(J_z))
    if J_max == 0:
        return 0.0
    jx, jy, jz = J_x / J_max, J_y / J_max, J_z / J_max

    # XXZ limit: J_x = J_y
    if abs(jx - jy) < 1e-12:
        Delta = jz / jx if abs(jx) > 1e-12 else 0
        if abs(Delta) >= 1.0 - 1e-12:
            return 1.0  # XXX / isotropic limit
        # c = 1 - 6(1-nu)^2/nu where cos(pi*nu) = Delta
        nu = math.acos(max(-1, min(1, Delta))) / math.pi
        if nu < 1e-12:
            return 1.0
        return 1.0 - 6.0 * (1.0 - nu) ** 2 / nu

    # General XYZ: the central charge depends on the elliptic nome
    # Parametrize via the cross-ratio of the coupling constants
    # Using Baxter's parametrization: c depends on the modular parameter tau
    # The exact formula involves theta functions; for a numerical approximation
    # we use the effective anisotropy
    # Sort |J|: J_a >= J_b >= J_c
    js = sorted([abs(jx), abs(jy), abs(jz)], reverse=True)
    if js[0] < 1e-12:
        return 0.0

    # Effective anisotropy parameter from elliptic parametrization
    # k_ell^2 = (J_a^2 - J_b^2) / (J_a^2 - J_c^2) when J_a > J_b >= J_c
    denom = js[0] ** 2 - js[2] ** 2
    if denom < 1e-14:
        # Isotropic case
        return 1.0
    k_ell_sq = (js[0] ** 2 - js[1] ** 2) / denom

    # nu parameter (crossing parameter)
    # In the critical regime, nu is determined by the ratio J_b/J_a
    # through the Jacobi elliptic functions
    # For small k_ell (near XXZ): nu ~ arccos(J_c/J_a)/pi
    if k_ell_sq < 1e-10:
        # Near XXZ limit
        Delta_eff = js[2] / js[0]
        if abs(Delta_eff) >= 1.0 - 1e-12:
            return 1.0
        nu = math.acos(max(-1, min(1, Delta_eff))) / math.pi
        if nu < 1e-12:
            return 1.0
        return 1.0 - 6.0 * (1.0 - nu) ** 2 / nu

    # General elliptic case: compute K and K' from k_ell
    from scipy.special import ellipk
    k_ell = math.sqrt(max(0, min(1, k_ell_sq)))
    k_ell_prime = math.sqrt(max(0, 1 - k_ell_sq))
    K_val = ellipk(k_ell_sq)
    K_prime = ellipk(1 - k_ell_sq) if k_ell_sq < 1 else float('inf')

    # tau = i * K'/K (the nome of the elliptic curve)
    if K_val < 1e-12:
        return 1.0
    tau_im = K_prime / K_val

    # For the 8-vertex model, the crossing parameter gamma determines c:
    # gamma/pi relates to nu through the elliptic uniformization
    # cos(pi*nu) = J_z / J_x in the appropriate parametrization
    # In the critical regime: c = 1 - 6(1-nu)^2/nu with nu depending on tau
    nu = math.acos(max(-1, min(1, js[2] / js[0]))) / math.pi
    if nu < 1e-12:
        return 1.0
    return 1.0 - 6.0 * (1.0 - nu) ** 2 / nu


def xyz_shadow_data(J_x: float, J_y: float, J_z: float) -> Dict[str, Any]:
    r"""Shadow data for XYZ chain.

    CAUTION (AP15): the XYZ shadow involves quasi-modular forms.
    The genus-1 propagator is E_2*(tau), NOT a holomorphic modular form.
    Graph amplitudes are quasi-modular polynomials in {E_2*, E_4, E_6}.
    """
    c = xyz_central_charge(J_x, J_y, J_z)
    kappa = c / 2.0
    alpha = 2.0  # universal on T-line
    if abs(c) < 1e-14 or abs(5 * c + 22) < 1e-14:
        S4 = None
    else:
        S4 = 10.0 / (c * (5 * c + 22))

    return {
        'chain': 'XYZ',
        'J': (J_x, J_y, J_z),
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'M' if S4 is not None and abs(S4) > 1e-14 else 'G',
        'quasi_modular': True,  # AP15: always quasi-modular for XYZ
    }


# =========================================================================
# 4. Faber-Pandharipande numbers and genus free energies
# =========================================================================

def lambda_fp(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    g=1: 1/24, g=2: 7/5760, g=3: 31/967680.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    num = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    den = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(num, den)


def genus_free_energy(kappa_val: Any, g: int) -> Any:
    """F_g(A) = kappa(A) * lambda_g^FP."""
    return kappa_val * lambda_fp(g)


# =========================================================================
# 5. Transfer matrix <-> shadow dictionary
# =========================================================================

def xxx_transfer_matrix_shadow_dict() -> Dict[str, str]:
    r"""Dictionary: transfer matrix conserved charges <-> shadow invariants.

    For the XXX Heisenberg chain (SU(2) symmetry), the transfer matrix
    T(u) = tr_a prod_i R_{ai}(u) with R(u) = u + P (Yang's R-matrix).

    log T(u) generates conserved charges I_n.

    The DICTIONARY (for the current line of V_k(sl_2)):

    Transfer matrix side        Shadow obstruction tower side
    -------------------         -----------------
    I_1 (momentum)              Translation on Ran(X)
    I_2 (Hamiltonian)           kappa = 9/4 (modular characteristic)
    I_3 (3rd charge)            alpha = 1 (cubic shadow, Lie bracket)
    I_4 = 0 (Jacobi!)           S_4 = 0 (quartic contact, Jacobi)
    I_n = 0 for n >= 4          S_n = 0 for n >= 4 (class L termination)

    Precise normalization: The conserved charges I_n have the natural
    normalization from the R-matrix expansion:
        R(u) = 1 + (1/u) P + O(1/u^2)

    The shadow coefficients S_n = a_{n-2}/n are the Taylor coefficients
    of the generating function H(t) = t^2 sqrt(Q_L(t)).

    The physical dictionary at the thermodynamic level:
        F_g = kappa * lambda_g^FP = (shadow free energy at genus g)
        = 1/L^{2g} correction to the extensive free energy
    """
    return {
        'I_1': 'Translation on Ran(X) / momentum operator',
        'I_2': 'kappa = dim(g)*(k+h^v)/(2*h^v) = 9/4 for k=1',
        'I_3': 'alpha = 1 (cubic shadow from Lie bracket)',
        'I_n>=4': 'S_n = 0 (class L: tower terminates, Jacobi identity)',
        'log_T(u)': 'Shadow generating function H(t) on current line',
        'E/L -> e_inf + F_1/L + ...': 'F_1 = kappa/24 (first shadow free energy)',
    }


# =========================================================================
# 6. R-matrices from shadow obstruction tower
# =========================================================================

def xxx_r_matrix_yang() -> Dict[str, Any]:
    r"""Yang's R-matrix for XXX chain.

    R(u) = u*I + P  (rational, sl_2-invariant)

    In the 4x4 matrix form (acting on C^2 tensor C^2):
        R(u) = [[u+1, 0, 0, 0],
                [0,   u, 1, 0],
                [0,   1, u, 0],
                [0,   0, 0, u+1]]

    The classical r-matrix (shadow collision residue):
        r = P / u (simple pole, as per AP19: one less than OPE)

    This is equivalent to r(z) = Omega/z where Omega = Casimir.
    """
    return {
        'type': 'rational',
        'formula': 'R(u) = u*I + P',
        'r_matrix_classical': 'r = P/u = Omega/u',
        'shadow_class': 'L',
        'shadow_depth': 3,
        'poles': {1: 'P (permutation operator)'},
    }


def xxz_r_matrix_trigonometric(gamma: float) -> np.ndarray:
    r"""Trigonometric R-matrix for XXZ chain.

    R(u, gamma) acting on C^2 tensor C^2:

        R(u) = [[sin(u+gamma),    0,         0,           0      ],
                [0,            sin(u),    sin(gamma),      0      ],
                [0,          sin(gamma),   sin(u),         0      ],
                [0,               0,         0,       sin(u+gamma)]]

    divided by sin(gamma) for standard normalization.

    For u -> 0: R(0) = P (permutation).
    Classical limit gamma -> 0: R(u) ~ u*I + gamma*P + O(gamma^2).

    This is the 6-vertex model R-matrix.

    Parameters:
        gamma: anisotropy parameter, Delta = cos(gamma)

    Returns: 4x4 R-matrix at u = spectral parameter (as a function)
    """
    def R(u):
        sg = math.sin(gamma)
        if abs(sg) < 1e-14:
            return np.eye(4)
        mat = np.zeros((4, 4))
        mat[0, 0] = math.sin(u + gamma) / sg
        mat[1, 1] = math.sin(u) / sg
        mat[1, 2] = 1.0  # sin(gamma)/sin(gamma)
        mat[2, 1] = 1.0
        mat[2, 2] = math.sin(u) / sg
        mat[3, 3] = math.sin(u + gamma) / sg
        return mat
    return R


def xxz_classical_r_matrix(gamma: float, u: float) -> np.ndarray:
    r"""Classical r-matrix for XXZ from the trigonometric R-matrix.

    r(u) = d/d(hbar) R(u, hbar*gamma)|_{hbar=0}

    For the 6-vertex model: r(u) = cot(u)*diag(1,-1,-1,1)/2 + csc(u)*P_12

    Actually, the shadow collision residue gives (AP19):
        r(z) = Omega / z  (simple pole only)
    with Omega the Casimir element.

    The trigonometric deformation means:
        r^{trig}(u) = cot(u) * H_Cartan + P_{root} / sin(u)
    """
    sg = math.sin(gamma)
    if abs(sg) < 1e-14:
        # Isotropic limit: Yang's r-matrix
        mat = np.zeros((4, 4))
        if abs(u) < 1e-14:
            return mat
        mat[0, 0] = 1.0 / u
        mat[1, 1] = 0
        mat[1, 2] = 1.0 / u
        mat[2, 1] = 1.0 / u
        mat[2, 2] = 0
        mat[3, 3] = 1.0 / u
        return mat

    # Trigonometric r-matrix
    su = math.sin(u)
    cu = math.cos(u)
    mat = np.zeros((4, 4))
    mat[0, 0] = cu / su if abs(su) > 1e-14 else 0
    mat[1, 1] = 0
    mat[1, 2] = 1.0 / su if abs(su) > 1e-14 else 0
    mat[2, 1] = 1.0 / su if abs(su) > 1e-14 else 0
    mat[2, 2] = 0
    mat[3, 3] = cu / su if abs(su) > 1e-14 else 0
    return mat


# =========================================================================
# 7. Bethe ansatz energies and finite-size corrections
# =========================================================================

def xxx_bethe_energy(bethe_roots: np.ndarray, J: float = 1.0) -> float:
    r"""Energy of a Bethe state for XXX chain.

    E = -J * sum_{i=1}^M 2 / (u_i^2 + 1/4)

    where u_i are the Bethe roots (rapidities).

    For the antiferromagnetic ground state at half-filling:
        E/L -> e_inf = -J * ln(2)  (in the thermodynamic limit)
    """
    return -J * np.sum(2.0 / (bethe_roots ** 2 + 0.25))


def xxx_bethe_equations(rapidities: np.ndarray, L: int) -> np.ndarray:
    r"""Bethe ansatz equations for XXX chain with L sites.

    (u_j + i/2)^L / (u_j - i/2)^L = prod_{k != j} (u_j - u_k + i) / (u_j - u_k - i)

    In logarithmic form (for real rapidities):
    L * arctan(2*u_j) = pi*I_j + sum_{k != j} arctan(u_j - u_k)

    where I_j are integer/half-integer quantum numbers.

    Returns the residuals of the Bethe equations (should be zero at solution).
    """
    M = len(rapidities)
    residuals = np.zeros(M)
    for j in range(M):
        lhs = L * np.arctan(2 * rapidities[j])
        rhs = 0.0
        for k in range(M):
            if k != j:
                rhs += np.arctan(rapidities[j] - rapidities[k])
        residuals[j] = lhs - rhs
    return residuals


def xxx_ground_state_energy_exact(L: int, antiferromagnetic: bool = True) -> float:
    r"""Ground state energy of XXX Heisenberg chain with L sites (PBC).

    Computed by exact diagonalization of the Hamiltonian:

    Antiferromagnetic (default): H = +sum_{i=1}^L S_i . S_{i+1}
        Ground state is a singlet. CFT description: SU(2)_1, c=1.
        L=2: E = -3/4 (singlet of H_AFM = S_1.S_2 + S_2.S_1 = 2*S_1.S_2)
             Wait: S_1.S_2 for singlet = -3/4.
             H = sum S_i.S_{i+1} with PBC and L=2: H = 2*S_1.S_2.
             Singlet: E = 2*(-3/4) = -3/2. Triplet: E = 2*(1/4) = 1/2.
             Ground state: E = -3/2.
        L=4: E = -2 (exact from Bethe ansatz).

    Ferromagnetic: H = -sum_{i=1}^L S_i . S_{i+1}
        Ground state is fully polarized. E = -L/4.

    Uses the spin-1/2 representation: each site has 2 states, total dim = 2^L.
    Restricted to L <= 16 for computational feasibility.
    """
    if L > 16:
        raise ValueError(f"L={L} too large for exact diag (max 16)")
    if L < 2:
        raise ValueError(f"L={L} must be >= 2")

    dim = 2 ** L

    # Build Hamiltonian using Pauli matrices (spin-1/2 operators)
    sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
    sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2
    I2 = np.eye(2, dtype=complex)

    def kron_chain(ops):
        """Tensor product of a list of 2x2 matrices."""
        result = ops[0]
        for op in ops[1:]:
            result = np.kron(result, op)
        return result

    sign = +1 if antiferromagnetic else -1
    H = np.zeros((dim, dim), dtype=complex)

    for i in range(L):
        j = (i + 1) % L  # periodic BC
        for s_op in [sx, sy, sz]:
            # Build S_i^a S_j^a
            ops_list = [I2] * L
            ops_list[i] = s_op
            ops_list[j] = s_op
            H += sign * kron_chain(ops_list)

    # Diagonalize
    eigenvalues = np.linalg.eigvalsh(H.real)
    return float(eigenvalues[0])


def xxx_energy_density_thermodynamic() -> float:
    r"""Thermodynamic energy density e_inf for XXX antiferromagnet.

    e_inf = 1/4 - ln(2) = 0.25 - 0.6931... = -0.4431...

    This is the exact result from Bethe ansatz (Hulthén 1938).
    H = sum S_i . S_{i+1} (note sign: antiferromagnetic).
    """
    return 0.25 - math.log(2)


def xxx_finite_size_energy(L: int, n: int = 0) -> float:
    r"""Finite-size energy prediction for XXX chain using shadow/CFT.

    E_n(L) / L = e_inf + 2*pi*v_F / L^2 * (x_n - c/24) + O(1/L^3)

    For the ground state (n=0): x_0 = 0, so
    E_0(L) / L = e_inf - 2*pi*v_F * c / (24 * L^2) + ...

    For XXX:
        e_inf = 1/4 - ln(2)
        c = 1
        v_F = pi/2 (Fermi velocity)

    The Cardy formula gives the leading finite-size correction.
    The SHADOW gives the next order:
        E_0(L) / L = e_inf - pi^2/(6*L^2) * c + F_1_correction / L^2 + ...

    where the F_1 correction comes from F_1 = kappa/24 on the appropriate line.

    Note: the standard Cardy formula E = e_inf*L - pi*v_F*c/(6L) + ...
    (total energy, not per site).
    """
    e_inf = 0.25 - math.log(2)
    c = 1.0
    v_F = math.pi / 2.0

    # Leading: Cardy formula
    E_leading = e_inf * L - math.pi * v_F * c / (6.0 * L)

    # For excited state n: add 2*pi*v_F * x_n / L
    # Ground state: x_0 = 0
    E = E_leading + 2 * math.pi * v_F * n / L

    return E


def xxx_cardy_formula(L: int) -> float:
    r"""Cardy formula for XXX ground state energy.

    E_0(L) = e_inf * L - pi * v_F * c / (6 * L)

    For XXX: e_inf = 1/4 - ln(2), v_F = pi/2, c = 1.
    E_0(L) = (1/4 - ln(2)) * L - pi^2 / (12 * L)
    """
    e_inf = 0.25 - math.log(2)
    v_F = math.pi / 2.0
    c = 1.0
    return e_inf * L - math.pi * v_F * c / (6.0 * L)


# =========================================================================
# 8. Shadow-predicted correlation functions
# =========================================================================

def xxx_two_point_prediction(r: int) -> float:
    r"""Shadow prediction for the XXX two-point function.

    <S_z(0) S_z(r)> ~ (-1)^r / (r^2 * (2*pi)) * C_2

    The leading power law r^{-2} comes from the scaling dimension
    of the staggered magnetization operator, which has x = 1 for SU(2)_1.

    The coefficient is related to kappa through the normalization:
    C_2 ~ kappa * (normalization factor from OPE).

    For SU(2)_1: the two-point function of the spin-1/2 primary
    <phi(z) phi(w)> ~ 1/(z-w)^{2*1/(k+2)} = 1/(z-w)^{2/3}

    In the lattice, the staggered part dominates:
    <S_z(0) S_z(r)> = (-1)^r * A / r + B / r^2 + ...

    where A is a nonuniversal constant (depends on lattice regularization)
    and the power law r^{-1} comes from the marginal operator (x=1/2 for
    the staggered field in SU(2)_1).

    Actually for the XXX chain: <S_z(0) S_z(r)> ~ (-1)^r * C / (r * sqrt(ln r))
    with LOGARITHMIC corrections (this is the well-known Bethe ansatz result).
    The log corrections come from the marginally irrelevant operator.
    """
    if r == 0:
        return 0.25  # <S_z^2> = 1/4
    # Leading behavior with log correction (Affleck 1998)
    sign = (-1) ** r
    log_corr = 1.0 / math.sqrt(max(1, math.log(max(2, abs(r))))) if abs(r) > 1 else 1.0
    return sign * 0.14 / abs(r) * log_corr  # approximate prefactor


def xxx_four_point_shadow_prediction(r1: int, r2: int, r3: int) -> Dict[str, Any]:
    r"""Shadow prediction for the four-point function.

    <S_z(0) S_z(r1) S_z(r2) S_z(r3)> involves the quartic shadow.

    For XXX on the current line: S_4 = 0 (class L, Jacobi identity).
    This means the connected four-point function at leading order
    receives NO quartic shadow contribution.

    The four-point function decomposes:
    <S_z S_z S_z S_z>_connected = (disconnected Wick contractions) + Q_4 * R_4

    where Q_4 is the quartic shadow and R_4 involves position-dependent
    propagators.

    For class L algebras: Q_4 = 0, so the connected 4-point is given
    entirely by the cubic shadow (arity-3 tree graphs):
    <SSSS>_conn = C * C * (tree contributions from S_3 = alpha = 1)

    On the T-line: S_4 = 10/27 != 0, so there IS a quartic contact
    correction. This gives the gravitational (stress tensor) channel
    contribution to the four-point function.
    """
    return {
        'current_line': {
            'S_4': 0,
            'quartic_contact': 0,
            'leading_connected': 'tree graphs from S_3 = 1',
            'class': 'L',
        },
        'T_line': {
            'S_4': float(Rational(10, 27)),
            'quartic_contact': float(Rational(10, 27)),
            'leading_connected': 'tree + contact from S_4 = 10/27',
            'class': 'M',
        },
    }


# =========================================================================
# 9. Shadow growth rate and convergence
# =========================================================================

def shadow_growth_rate(kappa_val: Any, alpha_val: Any, S4_val: Any) -> float:
    r"""Shadow growth rate rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|).

    Delta = 8*kappa*S4 (critical discriminant).

    rho = 0 for classes G and L (tower terminates).
    rho > 0 for class M (infinite tower).

    For the XXX chain:
        Current line: rho = 0 (class L)
        T-line: rho = shadow_growth_rate(1/2, 2, 10/27) > 0
    """
    kappa_f = float(kappa_val)
    alpha_f = float(alpha_val)
    S4_f = float(S4_val)
    Delta = 8 * kappa_f * S4_f
    val = 9 * alpha_f ** 2 + 2 * Delta
    if abs(kappa_f) < 1e-30:
        return float('inf')
    return math.sqrt(abs(val)) / (2 * abs(kappa_f))


# =========================================================================
# 10. Affine sl_2 at general level k (XXX generalization)
# =========================================================================

def affine_sl2_shadow_data(k_val: Any) -> Dict[str, Any]:
    r"""Shadow data for V_k(sl_2) at level k.

    c = 3k/(k+2)

    Current line:
        kappa = 3(k+2)/4
        alpha = 1 (universal for affine KM)
        S_4 = 0 (class L)

    T-line (Sugawara):
        kappa_T = c/2 = 3k/(2(k+2))
        alpha_T = 2 (universal gravitational)
        S_4_T = 10/[c(5c+22)]
    """
    if isinstance(k_val, (int, Rational)):
        k_r = Rational(k_val)
        c = Rational(3) * k_r / (k_r + 2)
        kappa = Rational(3) * (k_r + 2) / 4
        kappa_T = c / 2
        S4_T = Rational(10) / (c * (5 * c + 22)) if c != 0 else None
    else:
        c = 3 * k_val / (k_val + 2)
        kappa = 3 * (k_val + 2) / 4.0
        kappa_T = c / 2.0
        S4_T = 10.0 / (c * (5 * c + 22)) if abs(c) > 1e-14 else None

    return {
        'algebra': f'V_{{{k_val}}}(sl_2)',
        'c': c,
        'k': k_val,
        # Current line
        'kappa_current': kappa,
        'alpha_current': Rational(1) if isinstance(k_val, (int, Rational)) else 1.0,
        'S4_current': Rational(0) if isinstance(k_val, (int, Rational)) else 0.0,
        'class_current': 'L',
        # T-line
        'kappa_T': kappa_T,
        'alpha_T': Rational(2) if isinstance(k_val, (int, Rational)) else 2.0,
        'S4_T': S4_T,
        'class_T': 'M' if S4_T is not None and S4_T != 0 else 'G',
    }


def affine_sl2_kappa(k_val: Any) -> Any:
    """kappa for V_k(sl_2) on current line = 3(k+2)/4."""
    if isinstance(k_val, (int, Rational)):
        return Rational(3) * (Rational(k_val) + 2) / 4
    return 3.0 * (k_val + 2) / 4.0


def affine_sl2_dual_level(k_val: Any) -> Any:
    """Feigin-Frenkel dual level: k' = -k - 2*h^v = -k - 4."""
    if isinstance(k_val, (int, Rational)):
        return -Rational(k_val) - 4
    return -k_val - 4.0


# =========================================================================
# 11. XXZ at general anisotropy: R-matrix verification
# =========================================================================

def xxz_yang_baxter_check(gamma: float, u: float, v: float, tol: float = 1e-10) -> bool:
    r"""Verify the Yang-Baxter equation for the trigonometric R-matrix.

    YBE: R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

    acting on C^2 tensor C^2 tensor C^2 = C^8.
    """
    R = xxz_r_matrix_trigonometric(gamma)

    # R_{12}: acts on spaces 1,2 with identity on 3
    R12_u = np.kron(R(u), np.eye(2))

    # R_{23}: acts on spaces 2,3 with identity on 1
    R23_v = np.kron(np.eye(2), R(v))

    # R_{13}: acts on spaces 1,3 with identity on 2
    # Need to permute: apply P_{23} R_{12} P_{23} to get R_{13}
    P23 = np.zeros((8, 8))
    for a in range(2):
        for b in range(2):
            for c in range(2):
                # |a,b,c> -> |a,c,b>
                i_in = a * 4 + b * 2 + c
                i_out = a * 4 + c * 2 + b
                P23[i_out, i_in] = 1.0
    R13_uv = P23 @ np.kron(R(u + v), np.eye(2)) @ P23

    lhs = R12_u @ R13_uv @ R23_v
    rhs = R23_v @ R13_uv @ R12_u

    return np.allclose(lhs, rhs, atol=tol)


# =========================================================================
# 12. Exact diagonalization utilities
# =========================================================================

def xxz_hamiltonian(L: int, Delta: float, antiferromagnetic: bool = True) -> np.ndarray:
    r"""Build the XXZ Hamiltonian for L sites with PBC.

    Antiferromagnetic (default):
        H = +sum_{i=1}^L (S_i^x S_{i+1}^x + S_i^y S_{i+1}^y + Delta S_i^z S_{i+1}^z)

    Ferromagnetic:
        H = -sum_{i=1}^L (...)

    The antiferromagnetic convention is standard for finite-size CFT
    (Cardy formula, Bethe ansatz with c=1).
    """
    dim = 2 ** L
    sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
    sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2
    I2 = np.eye(2, dtype=complex)

    def kron_chain(ops):
        result = ops[0]
        for op in ops[1:]:
            result = np.kron(result, op)
        return result

    sign = +1 if antiferromagnetic else -1
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        for s_op, coupling in [(sx, 1.0), (sy, 1.0), (sz, Delta)]:
            ops = [I2] * L
            ops[i] = s_op
            ops[j] = s_op
            H += sign * coupling * kron_chain(ops)

    return H.real


def xxz_ground_state_energy(L: int, Delta: float, antiferromagnetic: bool = True) -> float:
    """Ground state energy of the XXZ chain by exact diagonalization."""
    if L > 16:
        raise ValueError(f"L={L} too large for exact diag")
    H = xxz_hamiltonian(L, Delta, antiferromagnetic)
    eigenvalues = np.linalg.eigvalsh(H)
    return float(eigenvalues[0])


def xxx_spectrum(L: int, n_levels: int = 10, antiferromagnetic: bool = True) -> np.ndarray:
    """First n_levels energy eigenvalues of the XXX chain with L sites."""
    H = xxz_hamiltonian(L, 1.0, antiferromagnetic)
    eigenvalues = np.sort(np.linalg.eigvalsh(H))
    return eigenvalues[:min(n_levels, len(eigenvalues))]


def extract_central_charge(L_values: List[int], E0_values: List[float],
                           v_F: float = math.pi / 2) -> float:
    r"""Extract central charge from finite-size scaling.

    From E_0(L) = e_inf * L - pi * v_F * c / (6*L) + O(1/L^2):

    Plot L * E_0(L) vs 1/L^2:
        L * E_0(L) = e_inf * L^2 - pi * v_F * c / 6 + O(1/L)

    Or better: from E_0(L) = e_inf * L - pi*v_F*c/(6L),
    the finite-difference method:
        c = -6/(pi*v_F) * [L * E_0(L) - (L+2)*E_0(L+2)] / [1/L - 1/(L+2)]
    is not clean. Use a fit instead.

    Method: E_0(L)/L = e_inf - pi*v_F*c/(6*L^2)
    Linear fit of E_0(L)/L vs 1/L^2 gives slope = -pi*v_F*c/6.
    """
    e_per_site = [E / L for E, L in zip(E0_values, L_values)]
    inv_L2 = [1.0 / L ** 2 for L in L_values]

    # Linear fit: y = a + b * x where x = 1/L^2, y = E/L
    x = np.array(inv_L2)
    y = np.array(e_per_site)
    A = np.vstack([np.ones_like(x), x]).T
    result = np.linalg.lstsq(A, y, rcond=None)
    a, b = result[0]

    # b = -pi * v_F * c / 6 => c = -6 * b / (pi * v_F)
    c_extracted = -6.0 * b / (math.pi * v_F)
    return c_extracted


def extract_kappa_from_finite_size(
    L_values: List[int],
    E0_values: List[float],
    v_F: float = math.pi / 2,
    c: float = 1.0,
) -> float:
    r"""Extract kappa from next-order finite-size corrections.

    Beyond the Cardy formula:
    E_0(L)/L = e_inf - pi*v_F*c/(6L^2) + f_2/L^4 + ...

    The f_2 correction involves the shadow free energy F_2.
    For the T-line: F_2 = kappa_T * lambda_2^FP = kappa_T * 7/5760.

    Method: subtract Cardy term, fit the residual to 1/L^4.
    This requires high-precision data at large L, which exact diag
    at L <= 16 cannot reliably provide. Included for completeness.
    """
    e_inf = 0.25 - math.log(2)  # XXX specific
    residuals = []
    inv_L4 = []
    for E, L in zip(E0_values, L_values):
        cardy = e_inf - math.pi * v_F * c / (6.0 * L ** 2)
        residuals.append(E / L - cardy)
        inv_L4.append(1.0 / L ** 4)

    x = np.array(inv_L4)
    y = np.array(residuals)
    if len(x) < 2:
        return float('nan')
    A = np.vstack([np.ones_like(x), x]).T
    result = np.linalg.lstsq(A, y, rcond=None)
    a, b = result[0]

    # b ~ (2*pi*v_F)^2 * kappa * lambda_2 / ... (subleading, approximate)
    # The exact relation is model-dependent; this gives an order-of-magnitude estimate
    return b


# =========================================================================
# 13. Shadow discriminant and depth for spin chain families
# =========================================================================

def spin_chain_shadow_census() -> List[Dict[str, Any]]:
    r"""Census of shadow data for all spin chain continuum limits.

    Returns a list of shadow data dicts for the standard spin chain family.
    """
    census = []

    # XXX at various k
    for k_val in [1, 2, 3, 4, 5, 10]:
        data = affine_sl2_shadow_data(k_val)
        data['chain'] = f'XXX(k={k_val})'
        census.append(data)

    # XXZ at rational points (minimal models)
    for p in [2, 3, 4, 5, 6, 10]:
        data = xxz_shadow_data_rational(p)
        census.append(data)

    # XYZ examples
    for params in [(1.0, 0.8, 0.5), (1.0, 0.5, 0.3), (1.0, 0.9, 0.7)]:
        data = xyz_shadow_data(*params)
        census.append(data)

    return census


# =========================================================================
# 14. Bethe ansatz thermodynamic quantities
# =========================================================================

def xxx_dressed_energy_density() -> float:
    r"""Dressed energy density from Bethe ansatz.

    The thermodynamic Bethe ansatz gives:
    e_inf = integral_{-infty}^{infty} e_0(u) * rho(u) du

    where e_0(u) = -2/(u^2 + 1/4) is the bare energy per rapidity
    and rho(u) = 1/(2*cosh(pi*u)) is the ground state rapidity distribution.

    e_inf = integral -2/(u^2+1/4) * 1/(2*cosh(pi*u)) du = 1/4 - ln(2)

    This is the Hulthén result (1938).
    """
    return 0.25 - math.log(2)


def xxx_f1_from_shadow() -> Rational:
    r"""F_1 from the shadow obstruction tower for XXX (V_1(sl_2)).

    On the T-line (physically relevant for finite-size energy):
        F_1 = kappa_T * lambda_1^FP = (1/2) * (1/24) = 1/48.

    This gives the O(1/L) correction coefficient (via the Cardy formula).
    The Cardy formula at c=1: E_0(L) = e_inf*L - pi^2/(6*L).
    The 1/48 enters through the stress tensor contribution.

    On the current line (algebraic shadow):
        F_1 = kappa * lambda_1^FP = (9/4) * (1/24) = 3/32.

    The physical finite-size correction uses the T-line value.
    """
    return Rational(1, 2) * Rational(1, 24)  # = 1/48


def xxz_f1_rational(p: int) -> Rational:
    r"""F_1 for the XXZ chain at the rational point nu = p/(p+1).

    F_1 = kappa * lambda_1 = c/2 * 1/24 = c/48

    where c = 1 - 6/[p(p+1)].
    """
    c = xxz_central_charge_rational(p)
    return c / 2 * Rational(1, 24)


# =========================================================================
# 15. Quantum group deformation parameter from shadow
# =========================================================================

def xxz_quantum_parameter(gamma: float) -> complex:
    r"""Quantum group parameter q for XXZ chain.

    q = exp(i*gamma) where Delta = cos(gamma).

    The XXZ chain has U_q(sl_2) symmetry with q = exp(i*gamma).

    At the rational points gamma = pi/(p+1):
        q = exp(i*pi/(p+1)) (root of unity for the minimal model)

    The shadow encodes q through the relation:
        c(q) = 1 - 6*(1 - gamma/pi)^2 / (gamma/pi)
    """
    return complex(math.cos(gamma), math.sin(gamma))


def xxz_shadow_vs_quantum_group(gamma: float) -> Dict[str, Any]:
    r"""Compare shadow invariants with quantum group data.

    The shadow (kappa, alpha, S_4) on the T-line determines c and hence q.
    Conversely, q = e^{i*gamma} determines the shadow through c(gamma).

    This is the shadow <-> quantum group dictionary for the XXZ family.
    """
    nu = gamma / math.pi
    c = xxz_central_charge(nu)
    q = xxz_quantum_parameter(gamma)
    kappa = c / 2.0
    alpha = 2.0
    S4 = 10.0 / (c * (5 * c + 22)) if abs(c) > 1e-14 else float('inf')

    return {
        'gamma': gamma,
        'q': q,
        'Delta_anisotropy': math.cos(gamma),
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'rho': shadow_growth_rate(kappa, alpha, S4) if abs(kappa) > 1e-14 else float('inf'),
    }
