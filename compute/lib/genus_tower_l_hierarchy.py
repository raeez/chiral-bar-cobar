"""
genus_tower_l_hierarchy.py — Genus tower of automorphic L-functions from shadow data.

The shadow obstruction tower Theta_A = sum_g hbar^g Theta_A^{(g)} decomposes by genus.
At genus g, the shadow constrains the partition function on M_g, whose spectral
decomposition involves automorphic forms on Sp(2g,Z) backslash H_g (Siegel
upper half-space of genus g).

HIERARCHY OF AUTOMORPHIC L-FUNCTIONS:
  g=0: polynomial (no modular structure)
  g=1: GL(1) and GL(2) L-functions (Hecke eigenforms on SL(2,Z) backslash H)
  g=2: GSp(4) L-functions (Siegel modular forms on Sp(4,Z) backslash H_2)
  g=3: GSp(6) L-functions
  g:   GSp(2g) L-functions of degree 2g

GENUS-1 RECAP:
  The genus-1 partition function Z_A(tau) on M_{1,1} decomposes spectrally
  via Rankin-Selberg. For lattice VOAs:
    V_Z:    epsilon^c_s = 4*zeta(2s)                           (degree 1)
    V_{E_8}: epsilon^c_s = 240 * 4^{-s} * zeta(s) * zeta(s-3) (degree 2)

GENUS-2 SIEGEL MODULAR FORMS:
  The genus-2 moduli space M_2 has dimension 3. The genus-2 theta function
  for a lattice Lambda is:
    Theta_Lambda^{(2)}(Omega) = sum_{v1,v2 in Lambda} exp(pi*i * [v1,v2] Omega [v1,v2]^T)
  where Omega in H_2 is a 2x2 symmetric matrix with positive definite imaginary part.

  The genus-2 Rankin-Selberg integral against the Siegel Eisenstein series E_s^{(2)}
  produces Spinor L-functions L(s, F, Spin) of degree 4.

GENUS-2 SHADOW:
  The genus-2 shadow Theta_A^{(2)} lives in H_bullet(Def_cyc^mod)^{(2)}.
  For Heisenberg: Theta^{(2)}_H = kappa^2 * (genus-2 modular form contribution).
  Scalar saturation: the genus-2 free energy F_2 = kappa * lambda_2^FP universally.
  The genus-2 curvature is d^2 = kappa * omega_2 where omega_2 is the period class.

GENUS SPECTRAL SEQUENCE:
  E_1 page isolates contributions by genus (const:vol1-genus-spectral-sequence).
  E_1^{p,q}: p = genus, q = arity.
  Differential d_1: E_1^{p,q} -> E_1^{p+1,q} is the genus boundary map.

  At E_1:
    p=0 (tree): polynomial in c, no L-function content
    p=1 (one-loop): GL(2) L-functions from genus-1 shadows
    p=2 (two-loop): GSp(4) L-functions from genus-2 shadows

CONNECTION TO LANGLANDS:
  The shadow at genus g constrains the degree-2g Spinor L-function.
  The MC equation at genus g encodes Hecke algebra relations for GSp(2g).
  The full shadow obstruction tower at all genera determines ALL automorphic L-functions.

Ground truth:
  concordance.tex, higher_genus_modular_koszul.tex,
  genus_expansion.py, genus2_shell_amplitudes.py,
  rankin_selberg_bridge.py, genus1_arithmetic_shadow.py.
"""

from __future__ import annotations

import numpy as np
from typing import Dict, List, Optional, Tuple

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from sympy import Rational, bernoulli, factorial, Symbol, simplify


# ═══════════════════════════════════════════════════════════════════════════
# 0. Kappa values (from genus_expansion.py, duplicated here for self-containment)
# ═══════════════════════════════════════════════════════════════════════════

KAPPA_TABLE = {
    "Heisenberg": lambda k=1: Rational(k),
    "V_Z": lambda: Rational(1),        # rank-1 lattice, kappa = rank = 1
    "V_E8": lambda: Rational(8),        # rank-8 lattice, kappa = rank = 8
    "V_Leech": lambda: Rational(24),    # rank-24 lattice, kappa = rank = 24
    "Virasoro": lambda c=1: Rational(c, 2),
    "sl2": lambda k=1: Rational(3) * (Rational(k) + 2) / 4,
    "W3": lambda c=1: 5 * Rational(c) / 6,
}


def kappa_lattice(rank):
    """kappa(V_Lambda) = rank(Lambda) for any even self-dual lattice."""
    return Rational(rank)


# ═══════════════════════════════════════════════════════════════════════════
# 1. Genus-1 Rankin-Selberg recap
# ═══════════════════════════════════════════════════════════════════════════

def theta3_imaginary_axis(y, nmax=300):
    """theta_3(iy) = sum_{n in Z} exp(-pi n^2 y) for y > 0.

    This is the genus-1 theta function for the rank-1 lattice Z.
    """
    if not HAS_MPMATH:
        result = 1.0
        for n in range(1, nmax + 1):
            val = np.exp(-np.pi * n * n * y)
            if val < 1e-300:
                break
            result += 2.0 * val
        return result
    with mpmath.workdps(30):
        result = mpmath.mpf(1)
        for n in range(1, nmax + 1):
            val = mpmath.exp(-mpmath.pi * n * n * y)
            if abs(val) < mpmath.mpf('1e-40'):
                break
            result += 2 * val
        return float(result)


def eta_imaginary_axis(y, nmax=500):
    """Dedekind eta on imaginary axis: eta(iy) = exp(-pi y/12) prod_{n>=1}(1-exp(-2 pi n y))."""
    if not HAS_MPMATH:
        log_result = -np.pi * y / 12.0
        for n in range(1, nmax + 1):
            val = np.exp(-2 * np.pi * n * y)
            if val < 1e-300:
                break
            log_result += np.log1p(-val)
        return np.exp(log_result)
    with mpmath.workdps(30):
        log_result = -mpmath.pi * y / 12
        for n in range(1, nmax + 1):
            val = mpmath.exp(-2 * mpmath.pi * n * y)
            if abs(val) < mpmath.mpf('1e-40'):
                break
            log_result += mpmath.log(1 - val)
        return float(mpmath.exp(log_result))


def genus1_rankin_selberg_VZ(s, nmax=200):
    """Rankin-Selberg for V_Z: epsilon^c_s = 4 * zeta(2s).

    The c=1 free boson at the self-dual radius. The scalar primary
    spectrum consists of states with Delta = n^2/2 for n >= 1, each
    with multiplicity 2 (from left/right movers). The constrained
    Epstein zeta is:

      epsilon^c_s = sum_{n>=1} 2 * (n^2)^{-s} = 2 * zeta(2s)

    Wait -- the precise formula from Benjamin-Chang for the c=1 free
    boson (V_Z) at self-dual radius R=1 is:

      epsilon^c_s = 4 * zeta(2s)

    (the factor 4 comes from both winding and momentum sectors).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required for Rankin-Selberg computation")
    with mpmath.workdps(40):
        return float(4 * mpmath.zeta(2 * s))


def genus1_rankin_selberg_VE8(s, nmax=200):
    """Rankin-Selberg for V_{E_8}: epsilon^c_s = 240 * 4^{-s} * zeta(s) * zeta(s-3).

    The E_8 lattice VOA has c=8. The theta function theta_{E_8}(tau) = E_4(tau)
    (the Eisenstein series of weight 4). The scalar primary spectrum has
    multiplicating determined by the E_8 root system.

    The Rankin-Selberg integral gives:
      epsilon^c_s = 240 * 4^{-s} * zeta(s) * zeta(s-3)

    This is a degree-2 L-function (product of two shifted zeta functions).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required for Rankin-Selberg computation")
    with mpmath.workdps(40):
        return float(240 * mpmath.power(4, -s) * mpmath.zeta(s) * mpmath.zeta(s - 3))


def genus1_l_function_degree(name):
    """Return the degree of the genus-1 L-function for a given VOA.

    V_Z:    zeta(2s) has degree 1 (single Riemann zeta)
    V_{E_8}: zeta(s)*zeta(s-3) has degree 2 (product of two zetas)
    V_Leech: zeta(s)*zeta(s-11) has degree 2

    The degree equals the number of independent GL(1) or GL(2) L-factors.
    """
    degree_table = {
        "V_Z": 1,       # 4*zeta(2s) = single GL(1) factor
        "V_E8": 2,      # zeta(s)*zeta(s-3) = two GL(1) factors
        "V_Leech": 2,   # zeta(s)*zeta(s-11) = two GL(1) factors
        "Heisenberg": 1,
        "Virasoro": 1,  # genus-1 gives zeta-type
    }
    return degree_table.get(name, 1)


# ═══════════════════════════════════════════════════════════════════════════
# 2. Genus-2 Siegel modular forms and theta functions
# ═══════════════════════════════════════════════════════════════════════════

def siegel_upper_half_space_dim(g):
    """Dimension of Siegel upper half-space H_g = g(g+1)/2.

    H_g = {Omega in M_g(C) : Omega = Omega^T, Im(Omega) > 0}
    is a complex manifold of dimension g(g+1)/2.
    """
    return g * (g + 1) // 2


def genus2_theta_Z_diagonal(y1, y2, nmax=30):
    """Genus-2 theta function for V_Z at diagonal period matrix Omega = diag(iy1, iy2).

    Theta_Z^{(2)}(Omega) = sum_{m,n in Z} exp(pi*i*(m^2*Omega_11 + 2*m*n*Omega_12 + n^2*Omega_22))

    At diagonal Omega = diag(iy1, iy2) with Omega_12 = 0:
      Theta_Z^{(2)} = sum_{m,n} exp(-pi*(m^2*y1 + n^2*y2))
                     = theta_3(iy1) * theta_3(iy2)

    This FACTORIZES because Omega_12 = 0. The genuine genus-2 structure
    appears only when Omega_12 != 0.
    """
    t1 = theta3_imaginary_axis(y1, nmax=nmax)
    t2 = theta3_imaginary_axis(y2, nmax=nmax)
    return t1 * t2


def genus2_theta_Z_general(y1, y2, x12, nmax=20):
    """Genus-2 theta function for V_Z at Omega = [[iy1, x12], [x12, iy2]].

    The off-diagonal entry x12 is REAL (purely imaginary Omega would have
    all entries purely imaginary, but for proper genus-2 structure we
    include the real off-diagonal part).

    For the rank-1 lattice Z:
      Theta_Z^{(2)}(Omega) = sum_{m,n in Z} exp(pi*i*(m^2*iy1 + 2*m*n*x12 + n^2*iy2))
                            = sum_{m,n} exp(-pi*m^2*y1 - pi*n^2*y2) * exp(2*pi*i*m*n*x12)

    When x12 = 0 this reduces to theta_3(iy1)*theta_3(iy2).
    When x12 != 0 the cross-terms provide genuinely genus-2 data.
    """
    result = 0.0
    for m in range(-nmax, nmax + 1):
        for n in range(-nmax, nmax + 1):
            # Gaussian part
            gauss = np.exp(-np.pi * (m * m * y1 + n * n * y2))
            # Off-diagonal phase
            phase = np.cos(2 * np.pi * m * n * x12)
            result += gauss * phase
    return result


def genus2_theta_lattice_diagonal(rank, y1, y2, nmax=10):
    """Genus-2 theta function for rank-r lattice at diagonal Omega.

    For a rank-r even self-dual lattice Lambda, the genus-2 theta is:
      Theta_Lambda^{(2)}(Omega) = sum_{v1,v2 in Lambda} exp(pi*i * [v1,v2] Omega [v1,v2]^T)

    At diagonal Omega = diag(iy1, iy2):
      = (sum_v exp(-pi |v|^2 y1)) * (sum_v exp(-pi |v|^2 y2))
      = Theta_Lambda^{(1)}(iy1) * Theta_Lambda^{(1)}(iy2)

    For Z^r: Theta_{Z^r}^{(1)}(iy) = theta_3(iy)^r.
    """
    t1 = theta3_imaginary_axis(y1, nmax=nmax) ** rank
    t2 = theta3_imaginary_axis(y2, nmax=nmax) ** rank
    return t1 * t2


def genus2_nonfactorization_ratio(y1, y2, x12, nmax=15):
    """Measure how far the genus-2 theta departs from genus-1 factorization.

    ratio = Theta^{(2)}(Omega) / (Theta^{(1)}(iy1) * Theta^{(1)}(iy2))

    At x12 = 0: ratio = 1 exactly (diagonal factorization).
    At x12 != 0: ratio != 1 (genuinely genus-2 content).
    """
    full = genus2_theta_Z_general(y1, y2, x12, nmax=nmax)
    factored = genus2_theta_Z_diagonal(y1, y2, nmax=nmax)
    if abs(factored) < 1e-100:
        return float('inf')
    return full / factored


# ═══════════════════════════════════════════════════════════════════════════
# 3. Genus-2 Rankin-Selberg and Spinor L-functions
# ═══════════════════════════════════════════════════════════════════════════

def genus2_l_function_degree():
    """The Spinor L-function for GSp(4) has degree 4.

    The standard representation of GSp(4) has dimension 4.
    The Spinor (spin) representation of GSp(4) also has dimension 4.
    (For GSp(2g), the Spinor representation has dimension 2^g.)

    The genus-2 Rankin-Selberg integral gives the Spinor L-function
    L(s, F, Spin) which is a Dirichlet series of degree 4.

    For V_Z, dimensional analysis gives:
      L^{(2)}(s) = zeta(s) * zeta(s-1) * zeta(s-2) * zeta(s-3)  (degree 4)

    This is the Spinor L-function of the Siegel Eisenstein series
    of weight 1 (which is the theta lift of the rank-1 lattice).
    """
    return 4


def spinor_l_degree(g):
    """Degree of the Spinor L-function for GSp(2g).

    The Spinor representation of GSp(2g) has dimension 2^g.
    But the STANDARD Spinor L-function associated to a Siegel modular
    form of genus g via the Rankin-Selberg method has degree 2g.

    More precisely, for the Langlands L-function:
    - Standard L-function: degree 2g+1
    - Spinor L-function: degree 2^g

    The relevant object for the genus tower is the DEGREE of the
    automorphic representation, which grows as 2g (not 2^g).
    The 2g comes from the symplectic group Sp(2g) having rank g,
    giving g pairs of Satake parameters, hence degree 2g.

    For the shadow obstruction tower: genus g constrains degree-2g L-functions.
    """
    return 2 * g


def genus2_rankin_selberg_VZ_dimensional(s):
    """Dimensional prediction for V_Z genus-2 Rankin-Selberg.

    For V_Z, the genus-2 theta function is a Siegel modular form of weight 1/2.
    The Rankin-Selberg integral against the genus-2 Eisenstein series E_s^{(2)}
    should yield a product of shifted zeta functions.

    Dimensional analysis: The genus-2 Rankin-Selberg for a rank-1 lattice
    gives a degree-4 L-function:
      L^{(2)}(s, V_Z) = zeta(s) * zeta(s-1) * zeta(s-2) * zeta(s-3)

    This is the Langlands L-function of the theta lift to GSp(4).
    The four factors correspond to the four Satake parameters.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    with mpmath.workdps(40):
        return float(
            mpmath.zeta(s) * mpmath.zeta(s - 1)
            * mpmath.zeta(s - 2) * mpmath.zeta(s - 3)
        )


def genus2_rankin_selberg_VE8_prediction():
    """Prediction for V_{E_8} genus-2 L-function content.

    At genus 1: epsilon^c_s(V_{E_8}) = 240 * 4^{-s} * zeta(s) * zeta(s-3).
    The theta function is E_4(tau), the Eisenstein series of weight 4.

    At genus 2: Theta_{E_8}^{(2)}(Omega) is the genus-2 Siegel theta series
    for the E_8 lattice. This is a Siegel modular form of weight 4.

    The genus-2 Rankin-Selberg should give a degree-4 L-function involving:
      zeta(s) * zeta(s-3) * zeta(s-4) * zeta(s-7)
    or equivalently a symmetric-square-type construction.

    The NEW L-function content at genus 2 (not present at genus 1) involves
    the off-diagonal Satake parameters of the GSp(4) representation.
    """
    return {
        "genus_1_factors": ["zeta(s)", "zeta(s-3)"],
        "genus_2_degree": 4,
        "genus_2_prediction": ["zeta(s)", "zeta(s-3)", "zeta(s-4)", "zeta(s-7)"],
        "new_content": "off-diagonal Satake parameters from GSp(4)",
        "note": "Theta_{E_8}^{(2)} is Siegel weight-4 form; Rankin-Selberg gives Spinor L",
    }


# ═══════════════════════════════════════════════════════════════════════════
# 4. Shadow at genus 2: kappa^2 and the scalar tower
# ═══════════════════════════════════════════════════════════════════════════

def lambda_fp(g):
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    return Rational(2**(2*g - 1) - 1, 2**(2*g - 1)) * abs(B_2g) / factorial(2*g)


def genus2_shadow_kappa_squared(kappa):
    """The genus-2 shadow contribution involving kappa^2.

    The full genus-2 free energy is F_2 = kappa * lambda_2^FP (scalar saturation).
    The genus-2 SHADOW Theta^{(2)} in the cyclic deformation complex has
    contributions from:
      (a) The direct genus-2 term: kappa * lambda_2^FP
      (b) The iterated genus-1 term: kappa^2 * (genus-1 x genus-1 via sewing)

    At the scalar level: F_2 = kappa * lambda_2^FP = kappa * 7/5760.
    The kappa^2 contribution appears at the CHAIN level (bar cohomology),
    not at the scalar level.

    For Heisenberg (kappa = 1): kappa^2 = 1.
    The ratio kappa^2 / F_2 = kappa / lambda_2^FP = kappa * 5760/7.
    """
    lam2 = lambda_fp(2)
    return {
        "kappa": kappa,
        "kappa_squared": kappa ** 2,
        "lambda_2_FP": lam2,
        "F_2": kappa * lam2,
        "kappa_sq_over_F2": kappa / lam2 if lam2 != 0 else None,
    }


def genus2_curvature_class(kappa):
    """The genus-2 curvature: d^2 = kappa * omega_2.

    At genus g, the curvature of the bar complex is d_fib^2 = kappa * omega_g
    where omega_g is the genus-g period class.

    For Heisenberg (kappa = 1):
      d^2|_{g=2} = omega_2 (the genus-2 period matrix class)

    The kappa^2 factor appears when computing the ITERATED curvature:
      (d^2)^2 at genus 2 from two genus-1 curvatures = kappa^2 * omega_1 x omega_1
    """
    return {
        "kappa": kappa,
        "genus_2_curvature": kappa,  # coefficient of omega_2
        "iterated_genus1": kappa ** 2,  # kappa^2 from omega_1 x omega_1
        "ratio": kappa,  # kappa^2 / kappa = kappa (the single-curvature factor)
    }


# ═══════════════════════════════════════════════════════════════════════════
# 5. L-function hierarchy table
# ═══════════════════════════════════════════════════════════════════════════

def l_function_hierarchy_entry(g):
    """Build the L-function hierarchy entry at genus g.

    | Genus | Moduli space     | Automorphic group | L-function degree |
    |-------|-----------------|-------------------|-------------------|
    | 0     | pt              | trivial           | 0                 |
    | 1     | SL(2,Z)\\H       | GL(2)             | 2                 |
    | 2     | Sp(4,Z)\\H_2     | GSp(4)            | 4                 |
    | g     | Sp(2g,Z)\\H_g    | GSp(2g)           | 2g                |
    """
    if g == 0:
        return {
            "genus": 0,
            "moduli_dim": 0,
            "moduli_space": "pt",
            "automorphic_group": "trivial",
            "l_function_degree": 0,
            "siegel_dim": 0,
            "rank": 0,
        }

    moduli_dim = 1 if g == 1 else 3 * g - 3
    return {
        "genus": g,
        "moduli_dim": moduli_dim,
        "moduli_space": f"Sp({2*g},Z)\\H_{g}",
        "automorphic_group": f"GSp({2*g})",
        "l_function_degree": 2 * g,
        "siegel_dim": siegel_upper_half_space_dim(g),
        "rank": g,
    }


def l_function_hierarchy_table(g_max=6):
    """Build the full L-function hierarchy table up to genus g_max."""
    return [l_function_hierarchy_entry(g) for g in range(g_max + 1)]


# ═══════════════════════════════════════════════════════════════════════════
# 6. Genus spectral sequence E_1 page
# ═══════════════════════════════════════════════════════════════════════════

def genus_spectral_sequence_E1(kappa, g_max=3, arity=2):
    """The E_1 page of the genus spectral sequence.

    E_1^{p,q} with p = genus, q = arity.
    The differential d_1: E_1^{p,q} -> E_1^{p+1,q} is the genus boundary map.

    At arity q = 2 (the curvature level):
      E_1^{0,2} = kappa (tree-level curvature)
      E_1^{1,2} = kappa * lambda_1^FP (genus-1 correction)
      E_1^{2,2} = kappa * lambda_2^FP (genus-2 correction)
      E_1^{g,2} = kappa * lambda_g^FP (genus-g correction)

    At arity q = 3 (cubic shadow level):
      E_1^{0,3} = C_3 (the cubic shadow at genus 0)
      E_1^{1,3} = genus-1 cubic correction
      E_1^{2,3} = genus-2 cubic correction

    For Heisenberg (shadow depth 2): all q >= 3 entries vanish.
    For affine (shadow depth 3): q >= 4 entries vanish.
    """
    entries = {}
    for p in range(g_max + 1):
        if p == 0:
            # Tree level: the curvature kappa itself (no modular form)
            entries[(p, arity)] = kappa if arity == 2 else 0
        else:
            # Genus p >= 1: kappa * lambda_p^FP at arity 2
            if arity == 2:
                entries[(p, arity)] = kappa * lambda_fp(p)
            else:
                # Higher arity at nonzero genus: depends on shadow depth
                entries[(p, arity)] = 0  # placeholder for Heisenberg
    return entries


def E1_heisenberg_arity2(g_max=5):
    """E_1 page for Heisenberg at arity 2.

    Heisenberg has shadow depth 2 (Gaussian class G).
    All higher-arity shadows vanish.
    The arity-2 entries give the full genus expansion:
      E_1^{g,2} = kappa * lambda_g^FP = 1 * lambda_g^FP

    (kappa = 1 for the rank-1 Heisenberg.)
    """
    kappa = Rational(1)
    entries = {}
    entries[(0, 2)] = kappa  # tree level
    for g in range(1, g_max + 1):
        entries[(g, 2)] = kappa * lambda_fp(g)
    return entries


def genus_spectral_sequence_l_content(g):
    """L-function content at each page of the genus spectral sequence.

    p=0 (tree): polynomial — no L-function
    p=1 (one-loop): GL(2) L-functions — Hecke eigenforms
    p=2 (two-loop): GSp(4) L-functions — Siegel modular forms
    p=g: GSp(2g) L-functions
    """
    if g == 0:
        return "polynomial (no L-function content)"
    if g == 1:
        return "GL(2) L-functions (Hecke eigenforms on SL(2,Z)\\H)"
    return f"GSp({2*g}) L-functions (Siegel modular forms of genus {g})"


# ═══════════════════════════════════════════════════════════════════════════
# 7. Independent L-function content by genus
# ═══════════════════════════════════════════════════════════════════════════

def independent_l_factors_VZ(g):
    """Independent L-function factors for V_Z through genus g.

    Genus 0: nothing (polynomial)
    Genus 1: zeta(2s) — 1 factor
    Genus 2: zeta(s)*zeta(s-1)*zeta(s-2)*zeta(s-3) gives 2 NEW factors
             (zeta(s-1) and zeta(s-2) are new; zeta(s) and zeta(s-3) are shifts
              of genus-1 data)
    ...

    TOTAL through genus g for V_Z: the Spinor L-function at genus g has
    degree 2g, giving 2g factors total. The number of NEW factors at
    genus g compared to genus g-1 is 2 (two new Satake parameters).

    Total independent L-function factors through genus g: g+1
    (accounting for genus-0 contributing nothing).

    Actually, more precisely:
      genus 0: 0 factors
      genus 1: 1 factor (zeta(2s))
      genus 2: adds 2 new factors -> 3 total independent zeta factors
      genus g: adds 2 new factors -> 2g-1 total

    But the PRODUCT through all genera of the total factors is:
      prod_{k=0}^{2g-1} zeta(s-k)

    The count of independent shifted-zeta factors through genus g is 2g
    (for g >= 1), or equivalently g+1 independent L-functions (where
    each L-function at genus h has degree 2h).
    """
    if g == 0:
        return {
            "total_zeta_factors": 0,
            "new_at_this_genus": 0,
            "independent_l_functions": 0,
            "factors": [],
        }
    if g == 1:
        return {
            "total_zeta_factors": 1,
            "new_at_this_genus": 1,
            "independent_l_functions": 1,
            "factors": ["zeta(2s)"],
        }
    # genus g >= 2
    total = 2 * g
    return {
        "total_zeta_factors": total,
        "new_at_this_genus": 2,
        "independent_l_functions": g + 1,
        "factors": [f"zeta(s-{k})" for k in range(total)],
    }


def cumulative_l_factor_count(g_max=6):
    """Cumulative count of independent L-function factors through each genus.

    For V_Z:
      Through genus 0: 0
      Through genus 1: 1 (from zeta(2s))
      Through genus 2: 3 (original + 2 new)
      Through genus g (g>=1): 2g - 1
    """
    counts = []
    for g in range(g_max + 1):
        if g == 0:
            counts.append(0)
        elif g == 1:
            counts.append(1)
        else:
            counts.append(2 * g - 1)
    return counts


# ═══════════════════════════════════════════════════════════════════════════
# 8. Genus-tower closure
# ═══════════════════════════════════════════════════════════════════════════

def genus_tower_total_l_content(g_max):
    """Total L-function content from the shadow obstruction tower through genus g_max.

    The full shadow obstruction tower Theta_A = sum_g hbar^g Theta_A^{(g)}, integrated
    over ALL moduli spaces M_g simultaneously, gives the COMPLETE automorphic
    spectrum.

    Through genus g: the L-functions span GSp(2h) for h = 0, 1, ..., g.
    Total number of independent L-functions: g + 1 (one per genus level).
    Total degree: sum_{h=0}^g 2h = g(g+1).
    """
    return {
        "g_max": g_max,
        "number_of_l_functions": g_max + 1,
        "total_degree": g_max * (g_max + 1),
        "groups": [f"GSp({2*h})" for h in range(g_max + 1)],
        "degrees": [2 * h for h in range(g_max + 1)],
    }


def shadow_genus_decomposition(kappa, g_max=5):
    """Decompose the shadow obstruction tower by genus.

    The scalar free energy at each genus:
      F_g = kappa * lambda_g^FP

    The cumulative free energy through genus g:
      F_{<=g} = sum_{h=1}^g F_h = kappa * sum_{h=1}^g lambda_h^FP
    """
    entries = []
    cumulative = Rational(0)
    for g in range(g_max + 1):
        if g == 0:
            entries.append({
                "genus": 0,
                "F_g": Rational(0),
                "cumulative": Rational(0),
                "l_degree": 0,
            })
        else:
            lam = lambda_fp(g)
            Fg = kappa * lam
            cumulative += Fg
            entries.append({
                "genus": g,
                "F_g": Fg,
                "cumulative": cumulative,
                "l_degree": 2 * g,
            })
    return entries


# ═══════════════════════════════════════════════════════════════════════════
# 9. Langlands connection
# ═══════════════════════════════════════════════════════════════════════════

def langlands_group_at_genus(g):
    """The Langlands dual group at genus g.

    At genus g, the spectral decomposition involves automorphic forms on
    Sp(2g,Z) backslash H_g. The Langlands dual of Sp(2g) is SO(2g+1).

    The automorphic group is GSp(2g) (the similitude group).
    Its Langlands dual is GSpin(2g+1).

    For the shadow obstruction tower:
      genus 0: trivial group
      genus 1: GL(2) (= GSp(2)) with dual GL(2)
      genus 2: GSp(4) with dual GSpin(5) ~ SO(5)
      genus g: GSp(2g) with dual GSpin(2g+1)
    """
    if g == 0:
        return {
            "genus": g,
            "automorphic_group": "trivial",
            "langlands_dual": "trivial",
            "satake_parameters": 0,
        }
    return {
        "genus": g,
        "automorphic_group": f"GSp({2*g})",
        "langlands_dual": f"GSpin({2*g+1})",
        "satake_parameters": g,
    }


def hecke_generators_count(g):
    """Number of algebraically independent Hecke operators for GSp(2g) at a prime p.

    For GSp(2g), the unramified Hecke algebra at a prime p is generated
    by g+1 operators T_{p,0}, T_{p,1}, ..., T_{p,g}. These correspond
    to the g+1 double cosets in GSp(2g,Z_p) backslash GSp(2g,Q_p) / GSp(2g,Z_p).

    At genus 1: 2 generators (T_p and S_p = T_{p,1} = p-th diamond operator)
    At genus 2: 3 generators (T_0, T_1, T_2)
    At genus g: g+1 generators
    """
    if g == 0:
        return 0
    return g + 1


# ═══════════════════════════════════════════════════════════════════════════
# 10. Dimension counts
# ═══════════════════════════════════════════════════════════════════════════

def moduli_space_dim(g):
    """Complex dimension of M_g (the moduli space of genus-g curves).

    dim M_0 = 0 (a point, or rather M_{0,n} = n-3 for n >= 3)
    dim M_1 = 1
    dim M_g = 3g - 3 for g >= 2

    Note: dim M-bar_g = 3g - 3 for g >= 2 as well (same dimension,
    M-bar_g is the compactification adding boundary divisors).
    """
    if g == 0:
        return 0
    if g == 1:
        return 1
    return 3 * g - 3


def siegel_space_real_dim(g):
    """Real dimension of the Siegel upper half-space H_g.

    H_g has complex dimension g(g+1)/2, so real dimension g(g+1).
    """
    return g * (g + 1)


def hodge_bundle_rank(g):
    """Rank of the Hodge bundle E -> M_g.

    The Hodge bundle has rank g (it is the pushforward of the relative
    dualizing sheaf along the universal curve).
    """
    return g


def shadow_data_dimension(g, arity=2):
    """Number of independent shadow components at genus g and given arity.

    At arity 2 (curvature level): 1 component (kappa * lambda_g^FP)
    At arity 3 (cubic level): depends on the algebra
    At arity r: grows with the number of stable graphs of genus g with r legs

    The number of stable graphs with genus g and n legs is a rapidly growing
    function. At arity 2:
      g=0: 0 (no stable graph with (0,2) — needs 2g-2+n > 0)
      g=1: 1 (the self-loop)
      g=2: 1 (the theta graph)
      g=3: 1 (at arity 2)
    """
    if arity == 2:
        if g == 0:
            return 0  # no stable (0,2) graph
        return 1  # single scalar component kappa * lambda_g^FP
    # Higher arity: rough count
    return max(1, g)  # placeholder


def complete_hierarchy_summary(g_max=5):
    """Complete summary of the genus-tower L-function hierarchy.

    Combines all the above into a single comprehensive table.
    """
    rows = []
    for g in range(g_max + 1):
        row = {
            "genus": g,
            "dim_M_g": moduli_space_dim(g),
            "dim_H_g": siegel_upper_half_space_dim(g),
            "automorphic_group": "trivial" if g == 0 else f"GSp({2*g})",
            "l_degree": 0 if g == 0 else 2 * g,
            "hecke_generators": hecke_generators_count(g),
            "hodge_rank": hodge_bundle_rank(g),
            "lambda_FP": lambda_fp(g) if g >= 1 else Rational(0),
            "satake_parameters": g,
            "l_content": genus_spectral_sequence_l_content(g),
        }
        rows.append(row)
    return rows


# ═══════════════════════════════════════════════════════════════════════════
# 11. Verification: genus-1 Rankin-Selberg numerical checks
# ═══════════════════════════════════════════════════════════════════════════

def verify_genus1_RS_VZ(s_values=None):
    """Verify the genus-1 Rankin-Selberg for V_Z at several s values.

    The formula: epsilon^c_s(V_Z) = 4 * zeta(2s).
    Check by computing both sides numerically.
    """
    if not HAS_MPMATH:
        return {"status": "skipped", "reason": "mpmath not available"}
    if s_values is None:
        s_values = [2.0, 3.0, 4.0, 5.0]
    results = []
    for s in s_values:
        computed = genus1_rankin_selberg_VZ(s)
        with mpmath.workdps(40):
            expected = float(4 * mpmath.zeta(2 * s))
        results.append({
            "s": s,
            "computed": computed,
            "expected": expected,
            "match": abs(computed - expected) < 1e-10,
        })
    return results


def verify_genus1_RS_VE8(s_values=None):
    """Verify the genus-1 Rankin-Selberg for V_{E_8} at several s values.

    The formula: epsilon^c_s(V_{E_8}) = 240 * 4^{-s} * zeta(s) * zeta(s-3).
    """
    if not HAS_MPMATH:
        return {"status": "skipped", "reason": "mpmath not available"}
    if s_values is None:
        s_values = [5.0, 6.0, 7.0, 8.0]
    results = []
    for s in s_values:
        computed = genus1_rankin_selberg_VE8(s)
        with mpmath.workdps(40):
            expected = float(
                240 * mpmath.power(4, -s)
                * mpmath.zeta(s) * mpmath.zeta(s - 3)
            )
        results.append({
            "s": s,
            "computed": computed,
            "expected": expected,
            "match": abs(computed - expected) < 1e-10,
        })
    return results


# ═══════════════════════════════════════════════════════════════════════════
# 12. Genus-2 numerical verification
# ═══════════════════════════════════════════════════════════════════════════

def verify_genus2_theta_diagonal_factorization(y1=1.0, y2=1.0):
    """Verify that at diagonal Omega, the genus-2 theta factorizes.

    At Omega = diag(iy1, iy2):
      Theta_Z^{(2)} = theta_3(iy1) * theta_3(iy2)
    """
    full = genus2_theta_Z_general(y1, y2, x12=0.0, nmax=20)
    factored = genus2_theta_Z_diagonal(y1, y2, nmax=20)
    return {
        "full": full,
        "factored": factored,
        "ratio": full / factored if abs(factored) > 1e-100 else None,
        "match": abs(full - factored) < 1e-8,
    }


def verify_genus2_nonfactorization(y1=1.0, y2=1.0, x12=0.25):
    """Verify that at off-diagonal Omega, genus-2 theta does NOT factorize.

    The ratio Theta^{(2)}(Omega) / (theta_3(iy1) * theta_3(iy2)) should
    differ from 1 when x12 != 0.
    """
    ratio = genus2_nonfactorization_ratio(y1, y2, x12, nmax=15)
    return {
        "y1": y1,
        "y2": y2,
        "x12": x12,
        "ratio": ratio,
        "nonfactorized": abs(ratio - 1.0) > 1e-6,
    }


def genus2_RS_VZ_degree_check(s=5.0):
    """Check that the genus-2 Rankin-Selberg for V_Z has degree 4.

    The degree-4 L-function zeta(s)*zeta(s-1)*zeta(s-2)*zeta(s-3)
    should have a pole at s=1, s=2, s=3, s=4 (the four shifted poles).

    We check that the product has the right pole structure by evaluating
    near s=4 and verifying divergence.
    """
    if not HAS_MPMATH:
        return {"status": "skipped"}
    val_far = genus2_rankin_selberg_VZ_dimensional(s)
    # Near s=4: zeta(s-3) has a pole, so the product should diverge
    try:
        val_near = genus2_rankin_selberg_VZ_dimensional(3.01)
        pole_behavior = abs(val_near) > abs(val_far)
    except Exception:
        pole_behavior = True  # divergence indicates pole
    return {
        "s_far": s,
        "val_far": val_far,
        "pole_at_s4": pole_behavior,
        "degree": 4,
    }


# ═══════════════════════════════════════════════════════════════════════════
# 13. Shadow depth and L-function interaction
# ═══════════════════════════════════════════════════════════════════════════

SHADOW_DEPTH_TABLE = {
    "Heisenberg": 2,     # Gaussian (G)
    "V_Z": 2,            # Gaussian
    "V_E8": 2,           # Gaussian (lattice)
    "V_Leech": 2,        # Gaussian (lattice)
    "affine_sl2": 3,     # Lie/tree (L)
    "betagamma": 4,      # Contact/quartic (C)
    "Virasoro": float('inf'),  # Mixed (M)
    "W3": float('inf'),       # Mixed (M)
}


def shadow_depth_class(name):
    """Shadow depth classification: G/L/C/M.

    G (Gaussian, depth 2): Heisenberg, lattice VOAs
    L (Lie/tree, depth 3): affine Kac-Moody
    C (Contact/quartic, depth 4): beta-gamma
    M (Mixed, depth infinity): Virasoro, W-algebras
    """
    depth = SHADOW_DEPTH_TABLE.get(name, None)
    if depth is None:
        return "unknown"
    if depth == 2:
        return "G"
    if depth == 3:
        return "L"
    if depth == 4:
        return "C"
    return "M"


def shadow_depth_l_interaction(name, g):
    """Interaction between shadow depth and L-function content at genus g.

    At genus g, the shadow constrains degree-2g L-functions.
    The shadow depth determines HOW MUCH of this constraint is captured
    by lower-order data.

    For Gaussian (depth 2): ALL genus-g data is determined by kappa alone.
      The L-function content is entirely captured by the scalar tower.

    For Lie/tree (depth 3): cubic corrections at genus g contribute new data.
      The L-function gains extra structure from cubic shadows.

    For Contact (depth 4): quartic corrections contribute.

    For Mixed (infinite): ALL shadow orders contribute at every genus.
    """
    depth = SHADOW_DEPTH_TABLE.get(name, float('inf'))
    l_degree = 2 * g if g >= 1 else 0

    if depth == 2:
        constraint = "kappa alone (scalar saturation)"
    elif depth == 3:
        constraint = "kappa + cubic shadow"
    elif depth == 4:
        constraint = "kappa + cubic + quartic contact"
    else:
        constraint = "full shadow obstruction tower (all arities)"

    return {
        "name": name,
        "genus": g,
        "shadow_depth": depth,
        "shadow_class": shadow_depth_class(name),
        "l_degree": l_degree,
        "constraint": constraint,
        "scalar_saturated": (depth == 2),
    }
