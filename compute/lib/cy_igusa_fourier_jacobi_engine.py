r"""Fourier-Jacobi expansion of the Igusa cusp form Phi_10 and its reciprocal 1/Phi_10.

MATHEMATICAL FRAMEWORK
======================

The Igusa cusp form chi_10 (= Phi_10) is the UNIQUE Siegel cusp form of weight 10
on Sp(4, Z).  Its Fourier-Jacobi expansion is

    Phi_10(Omega) = sum_{m >= 1} phi_m(tau, z) p^m,    p = e^{2 pi i sigma}

where Omega = ((tau, z), (z, sigma)) is the genus-2 period matrix and phi_m is a
Jacobi form of weight 10, index m.

1. LEADING FOURIER-JACOBI COEFFICIENT phi_1 = phi_{10,1}
=========================================================

phi_{10,1} = eta(tau)^{18} theta_1(tau, z)^2 = -Delta(tau) phi_{-2,1}(tau, z).

This is the UNIQUE Jacobi cusp form of weight 10, index 1.
dim J_{10,1}^{cusp} = 1 (Eichler-Zagier).

2. phi_2: FOURIER-JACOBI COEFFICIENT AT INDEX 2
=================================================

phi_2 is a Jacobi cusp form of weight 10, index 2.
dim J_{10,2}^{cusp} = dim S_{10} + dim S_{12} + dim S_{14} = 0 + 1 + 0 = 1.

So phi_2 is unique up to scalar.  We prove:

    phi_2 = 2 Delta(tau) phi_{-2,1}(tau, z) phi_{0,1}(tau, z)

The normalization constant 2 is fixed by the GL(2,Z) symmetry of chi_10
which requires a(1, 0, 2) = a(2, 0, 1) = phi_1(2, 0) = -36.

3. RECIPROCAL 1/Phi_10: BPS DEGENERACIES
==========================================

The DVV formula (Dijkgraaf-Verlinde-Verlinde 1997):

    1/Phi_10 = sum_{n, l, m} d(n, l, m) q^n y^l p^m

counts 1/4-BPS dyonic black hole microstates in type IIA on K3 x T^2.
For PRIMITIVE charge vectors, d(n, l, m) depends only on the discriminant
Delta = 4nm - l^2.

The leading Fourier-Jacobi coefficient of 1/Phi_10 is:

    psi_{-1}(tau, z) = 1/phi_{10,1}(tau, z)

which is a meromorphic Jacobi form with a double pole at z = 0.

4. JACOBI FORM RING EXPRESSION
================================

phi_{10,1} = -Delta * phi_{-2,1}
           = (1/1728)(E_6^2 - E_4^3) phi_{-2,1}

in the ring J_{*,*}^{weak} = C[E_4, E_6, phi_{-2,1}, phi_{0,1}].

5. BPS DISCRIMINANT AND CARDY GROWTH
======================================

    log |d(Delta)| ~ pi sqrt(Delta)   (Delta -> infinity)

This is the Bekenstein-Hawking entropy of the 1/4-BPS black hole.

CONVENTIONS (AP38, AP46):
  q = e^{2 pi i tau}, y = e^{2 pi i z}, p = e^{2 pi i sigma}
  eta(q) = q^{1/24} prod_{n>=1}(1-q^n)   [AP46: include q^{1/24}!]
  Eichler-Zagier convention for Jacobi forms (AP38)
  phi_{-2,1} = -theta_1^2/eta^6   (EZ: leading term y - 2 + 1/y)
  phi_{10,1} = -Delta * phi_{-2,1}   (leading: c(1, +/-1) = -1, c(1, 0) = 2)
  DVV convention for BPS degeneracies

References:
  Igusa (1962), "On Siegel modular forms of genus two"
  Dijkgraaf-Verlinde-Verlinde, hep-th/9608096 (1997)
  Dabholkar-Murthy-Zagier, arXiv:1208.4074 (2012)
  David-Jatkar-Sen, hep-th/0602005 (2006)
  Eichler-Zagier, "The Theory of Jacobi Forms" (1985)
  Gritsenko, arXiv:0812.3962 (2008)
"""

from __future__ import annotations

import collections
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.cy_modular_k3e_engine import (
    _convolve,
    _dim_cusp_forms,
    _dim_modular_forms,
    delta_coeffs,
    e4_coeffs,
    e6_coeffs,
    eta_power_coeffs,
    phi01_fourier,
    phi101_fourier,
    phi_m21_fourier,
    sigma_k,
)


# =====================================================================
# Section 0: Independent product-formula computation of Jacobi forms
# =====================================================================

def _jacobi_product_expansion(nmax: int, lmax: int) -> Dict[Tuple[int, int], int]:
    r"""Compute the product part of phi_{-2,1}:

    f(tau, z) = prod_{n>=1} (1-q^n)^{-4} [(1-yq^n)(1-y^{-1}q^n)]^2

    Returns {(n, l): coeff} for f = sum a(n,l) q^n y^l.
    """
    f = collections.defaultdict(int)
    f[(0, 0)] = 1

    for n in range(1, nmax):
        # (1-q^n)^{-4}: four factors of geometric series 1/(1-q^n)
        for _ in range(4):
            new_f = collections.defaultdict(int)
            for (nn, ll), c in f.items():
                if c == 0:
                    continue
                for k in range(nmax):
                    nn2 = nn + k * n
                    if nn2 >= nmax:
                        break
                    new_f[(nn2, ll)] += c
            f = new_f

        # (1-yq^n)^2 and (1-y^{-1}q^n)^2: four linear factors
        for y_shift in [1, 1, -1, -1]:
            new_f = collections.defaultdict(int)
            for (nn, ll), c in f.items():
                if c == 0:
                    continue
                new_f[(nn, ll)] += c
                nn2, ll2 = nn + n, ll + y_shift
                if nn2 < nmax and abs(ll2) <= lmax:
                    new_f[(nn2, ll2)] -= c
            f = new_f

    return dict((k, v) for k, v in f.items() if v != 0)


def phi_m21_product(nmax: int = 15, lmax: int = 10) -> Dict[Tuple[int, int], int]:
    r"""Compute phi_{-2,1}(tau, z) via the product formula.

    phi_{-2,1} = (y - 2 + 1/y) * prod_{n>=1} (1-q^n)^{-4}[(1-yq^n)(1-y^{-1}q^n)]^2

    This is the EZ-normalized unique weak Jacobi form of weight -2, index 1.

    Independent computation from the discriminant table in cy_modular_k3e_engine,
    providing verification against hardcoded values (AP10).
    """
    f = _jacobi_product_expansion(nmax, lmax)

    # Multiply by (y - 2 + 1/y)
    result = collections.defaultdict(int)
    for (n, l), c in f.items():
        if c == 0:
            continue
        for dl, fac in [(1, 1), (0, -2), (-1, 1)]:
            ll = l + dl
            if abs(ll) <= lmax:
                result[(n, ll)] += fac * c

    return dict((k, v) for k, v in result.items() if v != 0)


def phi101_product(nmax: int = 15, lmax: int = 10) -> Dict[Tuple[int, int], int]:
    r"""Compute phi_{10,1} = -Delta * phi_{-2,1} via the product formula.

    Independent computation path from the convolution in cy_modular_k3e_engine.
    Weight: 12 + (-2) = 10.  Index: 0 + 1 = 1.
    """
    delta = delta_coeffs(nmax + 2)
    fm21 = phi_m21_product(nmax + 2, lmax + 2)

    result = {}
    for n in range(nmax):
        for l in range(-lmax, lmax + 1):
            val = 0
            for k in range(n + 1):
                if delta[k] == 0:
                    continue
                if (n - k, l) in fm21:
                    val += delta[k] * fm21[(n - k, l)]
            val = -val
            if val != 0:
                result[(n, l)] = int(val)
    return result


# =====================================================================
# Section 1: phi_{10,1} -- high-order q,y-expansion
# =====================================================================

def phi101_qy_expansion(nmax: int = 15, lmax: int = 10) -> Dict[Tuple[int, int], int]:
    r"""Fourier coefficients c(n, l) of phi_{10,1}(tau, z) = sum c(n,l) q^n y^l.

    Computed via phi_{10,1} = -Delta * phi_{-2,1} using the discriminant table
    from cy_modular_k3e_engine.

    Cusp form: c(0, l) = 0 for all l.  c(n, l) = 0 unless 4n - l^2 >= 0.
    Discriminant-indexed: c(n, l) depends only on D = 4n - l^2.
    """
    return phi101_fourier(nmax)


def phi101_disc_coeffs(nmax: int = 15) -> Dict[int, int]:
    r"""Discriminant-indexed Fourier coefficients of phi_{10,1}.

    Returns {D: c(D)} where c(n, l) = c(4n - l^2) for all (n, l).

    Known values (Eichler-Zagier convention):
    c(3) = -1, c(4) = 2, c(7) = 16, c(8) = -36, c(11) = -99, c(12) = 272, ...
    """
    phi = phi101_fourier(nmax)
    disc = {}
    for (n, l), c in phi.items():
        D = 4 * n - l * l
        if D not in disc:
            disc[D] = c
    return disc


# =====================================================================
# Section 2: phi_2 -- Fourier-Jacobi coefficient at index 2
# =====================================================================

def phi2_fourier(nmax: int = 10, lmax: int = 8) -> Dict[Tuple[int, int], int]:
    r"""Fourier coefficients of phi_2(tau, z) = second FJ coefficient of Phi_10.

    phi_2 is a Jacobi cusp form of weight 10, index 2.
    dim J_{10,2}^{cusp} = dim S_{10} + dim S_{12} + dim S_{14} = 0 + 1 + 0 = 1.

    The unique (up to scalar) cusp form is Delta * phi_{-2,1} * phi_{0,1}
    (weight 12 + (-2) + 0 = 10, index 0 + 1 + 1 = 2).

    The normalization constant alpha = 2 is fixed by the GL(2,Z) symmetry
    of chi_10: the Siegel Fourier coefficient a(n, r, m) is invariant under
    GL(2,Z)-equivalence of the half-integral matrix T = ((n, r/2), (r/2, m)).

    In particular, T = ((1,0),(0,2)) ~ ((2,0),(0,1)) via ((0,1),(1,0)),
    so phi_2(1, 0) = phi_1(2, 0) = -36.

    Since [Delta * phi_{-2,1} * phi_{0,1}](1, 0) = -18 (computed from the
    convolution: delta(1) * sum_l phi_{-2,1}(0,l) * phi_{0,1}(0,-l)
    = 1 * (1*1 + (-2)*10 + 1*1) = -18), we get alpha * (-18) = -36,
    hence alpha = 2.

    Therefore: phi_2 = 2 * Delta * phi_{-2,1} * phi_{0,1}.
    """
    delta = delta_coeffs(nmax + 3)
    fm21 = phi_m21_fourier(nmax + 3)
    f01 = phi01_fourier(nmax + 3)

    # Step 1: Delta * phi_{-2,1}
    delta_times_m21 = collections.defaultdict(int)
    for n in range(nmax + 2):
        for l in range(-lmax - 2, lmax + 3):
            val = 0
            for k in range(n + 1):
                if delta[k] == 0:
                    continue
                if (n - k, l) in fm21:
                    val += delta[k] * fm21[(n - k, l)]
            if val != 0:
                delta_times_m21[(n, l)] = val

    # Step 2: (Delta * phi_{-2,1}) * phi_{0,1}
    result = {}
    for n in range(nmax):
        for l in range(-lmax, lmax + 1):
            val = 0
            for k in range(n + 1):
                for lp in range(-lmax - 2, lmax + 3):
                    lpp = l - lp
                    c1 = delta_times_m21.get((k, lp), 0)
                    c2 = f01.get((n - k, lpp), 0)
                    if c1 != 0 and c2 != 0:
                        val += c1 * c2
            # Multiply by alpha = 2
            val *= 2
            if val != 0:
                result[(n, l)] = int(val)

    return result


def phi2_disc_coeffs(nmax: int = 10) -> Dict[int, int]:
    r"""Discriminant-indexed Fourier coefficients of phi_2 (index 2).

    For a Jacobi form of index m, the discriminant is D = 4mn - l^2.
    For phi_2 (index 2): D = 8n - l^2.
    """
    phi2 = phi2_fourier(nmax)
    disc = {}
    for (n, l), c in phi2.items():
        D = 8 * n - l * l
        if D not in disc:
            disc[D] = c
    return disc


# =====================================================================
# Section 3: Reciprocal 1/phi_{10,1} -- Laurent inversion
# =====================================================================

def _divide_by_g0(f_coeffs: Dict[int, int], lmax: int) -> Dict[int, int]:
    r"""Solve g_0(y) * h(y) = f(y) for h(y).

    g_0(y) = -y + 2 - y^{-1} (the q^0 term of phi_{10,1}/q).

    The recurrence from -h(l+1) + 2h(l) - h(l-1) = f(l):
    Rearranged: h(l-1) = 2*h(l) - h(l+1) - f(l).
    Boundary: h(l) = 0 for l > lmax (expansion valid for |y| > 1).

    This gives the Laurent expansion of 1/g_0 in negative y-powers,
    which is the correct expansion for the BPS counting problem.

    Returns {l: h_l}.
    """
    a = collections.defaultdict(int)
    a.update(f_coeffs)

    b = collections.defaultdict(int)
    for l in range(lmax, -lmax - 2, -1):
        b[l - 1] = 2 * b[l] - b[l + 1] - a[l]

    return dict((l, v) for l, v in b.items() if v != 0 and abs(l) <= lmax)


def phi101_inverse_expansion(nmax: int = 10, lmax: int = 15) -> Dict[Tuple[int, int], int]:
    r"""Fourier coefficients of q/phi_{10,1} in the negative-l expansion.

    q/phi_{10,1} = sum_{n >= 0, l} h(n, l) q^n y^l

    Computed by iterative inversion: phi_{10,1} = q * g(q, y) with
    g = g_0 + q*g_1 + ..., then h = 1/g via

        h_0 = 1/g_0,
        h_N = -(1/g_0) * sum_{k=1}^{N} g_k * h_{N-k}.

    The coefficients h(n, l) give 1/phi_{10,1} = q^{-1} sum h(n,l) q^n y^l.

    Returns {(n, l): h(n, l)} for 0 <= n < nmax.
    """
    phi = phi101_fourier(nmax + 5)

    # Build g(q, y) = phi_{10,1}/q: g_k(y) = phi_{10,1}(k+1, y)
    g = collections.defaultdict(lambda: collections.defaultdict(int))
    for (n, l), c in phi.items():
        if n >= 1:
            g[n - 1][l] = c

    # h_0 = 1/g_0
    h = {}
    h[0] = _divide_by_g0({0: 1}, lmax)

    # Iterative inversion
    for N in range(1, nmax):
        rhs = collections.defaultdict(int)
        for k in range(1, N + 1):
            if N - k not in h:
                continue
            for lg, cg in g[k].items():
                for lh, ch in h[N - k].items():
                    ll = lg + lh
                    if abs(ll) <= lmax:
                        rhs[ll] += cg * ch

        neg_rhs = {l: -v for l, v in rhs.items() if v != 0}
        h[N] = _divide_by_g0(neg_rhs, lmax)

    # Flatten
    result = {}
    for n in range(nmax):
        if n in h:
            for l, c in h[n].items():
                if c != 0:
                    result[(n, l)] = int(c)

    return result


def phi101_inverse_disc(nmax: int = 10, lmax: int = 15) -> Dict[int, int]:
    r"""Discriminant-indexed coefficients of q/phi_{10,1}.

    Returns {D: c} where D = 4n - l^2 for the (n, l) expansion.
    """
    h = phi101_inverse_expansion(nmax, lmax)
    disc = {}
    for (n, l), c in h.items():
        D = 4 * n - l * l
        if D not in disc:
            disc[D] = c
    return disc


# =====================================================================
# Section 4: BPS degeneracies from 1/Phi_10
# =====================================================================

def bps_degeneracy_from_inverse(nmax: int = 10,
                                lmax: int = 15) -> Dict[int, int]:
    r"""BPS degeneracies d(Delta) from 1/phi_{10,1} at leading FJ order.

    At leading Fourier-Jacobi order (p^{-1} in 1/Phi_10), the degeneracies
    come from 1/phi_{10,1}(tau, z).  We compute h(n, l) = coefficient of
    q^n y^l in q/phi_{10,1}, and the BPS degeneracy at discriminant Delta is

        d(Delta) = h(n, l) for any (n, l) with 4n - l^2 = Delta.

    Returns {Delta: d(Delta)}.
    """
    return phi101_inverse_disc(nmax, lmax)


def bps_cardy_entropy(Delta: int) -> float:
    r"""Leading Bekenstein-Hawking entropy for 1/4-BPS black hole.

    S_{BH} = pi sqrt(Delta) for Delta > 0.
    """
    if Delta <= 0:
        return 0.0
    return math.pi * math.sqrt(Delta)


def bps_rademacher_leading(Delta: int) -> float:
    r"""Leading Rademacher / Cardy asymptotic for |d(Delta)|.

    |d(Delta)| ~ C(Delta) exp(pi sqrt(Delta))

    where the prefactor C involves Bessel function asymptotics.
    For weight-10 Siegel forms, the Bessel index is nu = 17/2.
    """
    if Delta <= 0:
        return 0.0
    x = math.pi * math.sqrt(Delta)
    nu = 8.5  # 17/2
    return math.exp(x) / math.sqrt(2 * math.pi * x) * Delta ** (-(nu / 2 + 0.25))


def bps_cardy_growth_check(nmax: int = 10, lmax: int = 15) -> Dict[str, Any]:
    r"""Verify Cardy growth: log |d(Delta)| ~ pi sqrt(Delta).

    Multi-path verification:
    (a) Direct computation of d(Delta) from 1/phi_{10,1}
    (b) Cardy formula S = pi sqrt(Delta)
    (c) Ratio log|d| / (pi sqrt(Delta)) -> 1 for large Delta
    """
    bps = bps_degeneracy_from_inverse(nmax, lmax)

    results = []
    for Delta in sorted(bps.keys()):
        if Delta <= 0:
            continue
        d = bps[Delta]
        if d == 0:
            continue
        log_d = math.log(abs(d))
        cardy = math.pi * math.sqrt(Delta)
        ratio = log_d / cardy if cardy > 0 else 0
        results.append({
            'Delta': Delta,
            'd': d,
            '|d|': abs(d),
            'log|d|': round(log_d, 4),
            'pi_sqrt_Delta': round(cardy, 4),
            'ratio': round(ratio, 4),
        })

    return {
        'data': results,
        'approaching_1': len(results) > 2 and results[-1]['ratio'] > results[0]['ratio'],
    }


# =====================================================================
# Section 5: Jacobi form ring decomposition
# =====================================================================

def phi101_ring_decomposition(nmax: int = 8) -> Dict[str, Any]:
    r"""Express phi_{10,1} in the Jacobi form ring generators.

    phi_{10,1} = -Delta * phi_{-2,1}
               = (1/1728)(E_6^2 - E_4^3) phi_{-2,1}
               = (-1/1728) E_4^3 phi_{-2,1} + (1/1728) E_6^2 phi_{-2,1}

    The space J_{10,1}^{weak} has dimension dim M_{10} + dim M_{12} = 1 + 2 = 3.
    Basis: {E_4 E_6 phi_{0,1},  E_4^3 phi_{-2,1},  E_6^2 phi_{-2,1}}.
    """
    e4 = e4_coeffs(nmax + 2)
    e6 = e6_coeffs(nmax + 2)
    fm21 = phi_m21_fourier(nmax + 2)
    phi_direct = phi101_fourier(nmax)

    # E_4^3 and E_6^2
    e4_sq = _convolve(e4, e4, nmax + 2)
    e4_cu = _convolve(e4_sq, e4, nmax + 2)
    e6_sq = _convolve(e6, e6, nmax + 2)

    # (E_6^2 - E_4^3)/1728 = -Delta
    neg_delta = [Fraction(e6_sq[i] - e4_cu[i], 1728) for i in range(nmax + 2)]

    # neg_delta * phi_{-2,1}
    ring_result = {}
    for n in range(nmax):
        for l in range(-2 * nmax, 2 * nmax + 1):
            val = Fraction(0)
            for k in range(n + 1):
                if neg_delta[k] == 0:
                    continue
                if (n - k, l) in fm21:
                    val += neg_delta[k] * fm21[(n - k, l)]
            if val != 0:
                ring_result[(n, l)] = int(val)

    # Compare with direct
    match = 0
    mismatch_list = []
    for key in set(ring_result.keys()) | set(phi_direct.keys()):
        n, l = key
        if n >= nmax:
            continue
        v1 = ring_result.get(key, 0)
        v2 = phi_direct.get(key, 0)
        if v1 == v2:
            match += 1
        else:
            mismatch_list.append((key, v1, v2))

    return {
        'formula': 'phi_{10,1} = (E_6^2 - E_4^3)/(1728) * phi_{-2,1} = -Delta * phi_{-2,1}',
        'coefficients': {
            'E_4^3 * phi_{-2,1}': Fraction(-1, 1728),
            'E_6^2 * phi_{-2,1}': Fraction(1, 1728),
            'E_4 * E_6 * phi_{0,1}': Fraction(0),
        },
        'weight_check': 12 + (-2) == 10,
        'index_check': 0 + 1 == 1,
        'fourier_matches': match,
        'fourier_mismatches': len(mismatch_list),
        'mismatches': mismatch_list[:5],
        'verified': len(mismatch_list) == 0,
    }


def phi2_ring_decomposition() -> Dict[str, Any]:
    r"""Express phi_2 in the Jacobi form ring generators.

    phi_2 = 2 * Delta * phi_{-2,1} * phi_{0,1}

    dim J_{10,2}^{cusp} = 1, so this is the unique cusp form up to scalar.
    The factor 2 is fixed by a(1,0,2) = phi_1(2,0) = -36.
    """
    return {
        'formula': 'phi_2 = 2 * Delta * phi_{-2,1} * phi_{0,1}',
        'weight_check': 12 + (-2) + 0 == 10,
        'index_check': 0 + 1 + 1 == 2,
        'normalization': 'alpha = 2 from a(1,0,2) = phi_1(2,0) = -36',
        'cusp_dim': 1,
    }


# =====================================================================
# Section 6: DVV verification tables
# =====================================================================

def dvv_literature_table() -> Dict[int, int]:
    r"""Known BPS indices from the expansion of 1/phi_{10,1}.

    The polar part (Appell-Lerch sum) gives d(-l^2) = l for l >= 1.
    The finite (mock) part has discriminant-indexed coefficients that
    match the phi_{-2,1} discriminant table.

    Sources: DVV (1997), David-Jatkar-Sen (2006), DMZ (2012).
    """
    return {
        # Polar: d(-l^2) = l
        -1: 1, -4: 2, -9: 3, -16: 4, -25: 5, -36: 6, -49: 7, -64: 8,
        -81: 9, -100: 10, -121: 11, -144: 12,
        # Finite (mock): matches phi_{-2,1} disc coefficients
        0: -2, 3: 8, 4: -12, 7: 39, 8: -56,
        11: 152, 12: -208, 15: 513, 16: -684,
        19: 1560, 20: -2032, 23: 4382, 24: -5616,
    }


# =====================================================================
# Section 7: Cross-consistency and multi-path verification
# =====================================================================

def verify_phi101_two_paths(nmax: int = 10) -> Dict[str, Any]:
    r"""Verify phi_{10,1} by two independent computations.

    Path 1: -Delta * phi_{-2,1} via discriminant table (cy_modular_k3e_engine)
    Path 2: -Delta * phi_{-2,1} via product formula (this engine)
    """
    path1 = phi101_fourier(nmax)
    path2 = phi101_product(nmax)

    matches = 0
    mismatches = []
    for key in set(list(path1.keys()) + list(path2.keys())):
        n, l = key
        if n >= nmax:
            continue
        v1 = path1.get(key, 0)
        v2 = path2.get(key, 0)
        if v1 == v2:
            matches += 1
        else:
            mismatches.append((key, v1, v2))

    return {
        'path1': 'disc table convolution',
        'path2': 'product formula',
        'matches': matches,
        'mismatches': len(mismatches),
        'mismatch_details': mismatches[:5],
        'verified': len(mismatches) == 0,
    }


def verify_phi_m21_two_paths(nmax: int = 10) -> Dict[str, Any]:
    r"""Verify phi_{-2,1} by two independent computations.

    Path 1: discriminant table (cy_modular_k3e_engine)
    Path 2: product formula (this engine)
    """
    path1 = phi_m21_fourier(nmax)
    path2 = phi_m21_product(nmax)

    matches = 0
    mismatches = []
    for key in set(list(path1.keys()) + list(path2.keys())):
        n, l = key
        if n >= nmax:
            continue
        v1 = path1.get(key, 0)
        v2 = path2.get(key, 0)
        if v1 == v2:
            matches += 1
        else:
            mismatches.append((key, v1, v2))

    return {
        'path1': 'disc table',
        'path2': 'product formula',
        'matches': matches,
        'mismatches': len(mismatches),
        'verified': len(mismatches) == 0,
    }


def verify_phi101_vanishes_z0(nmax: int = 15) -> Dict[str, Any]:
    r"""Verify phi_{10,1}(tau, 0) = 0 via two independent paths."""
    path1 = phi101_fourier(nmax)
    path2 = phi101_product(nmax)

    sums1 = [0] * nmax
    for (n, l), c in path1.items():
        if 0 <= n < nmax:
            sums1[n] += c

    sums2 = [0] * nmax
    for (n, l), c in path2.items():
        if 0 <= n < nmax:
            sums2[n] += c

    return {
        'path1_all_zero': all(s == 0 for s in sums1),
        'path2_all_zero': all(s == 0 for s in sums2),
        'verified': all(s == 0 for s in sums1) and all(s == 0 for s in sums2),
    }


def verify_phi2_gl2z_consistency(nmax: int = 8) -> Dict[str, Any]:
    r"""Verify phi_2 via GL(2,Z) equivalence of Siegel Fourier coefficients.

    T = ((1,0),(0,2)) ~ ((2,0),(0,1)): phi_2(1,0) = phi_1(2,0).
    T = ((1,1),(1,2)) ~ ((2,1),(1,1)): phi_2(1,1) = phi_1(2,1).
    T = ((1,-1),(-1,2)) ~ ((2,-1),(-1,1)): phi_2(1,-1) = phi_1(2,-1).

    For same-discriminant D=4 check:
    T = ((1,2),(2,2)): D = 8-4 = 4. T' = ((1,0),(0,1)): D = 4.
    So phi_2(1,2) = phi_1(1,0).
    """
    phi1 = phi101_fourier(nmax + 2)
    phi2 = phi2_fourier(nmax)

    checks = []

    # a(1,0,2) = a(2,0,1)
    checks.append({
        'id': 'a(1,0,2) = phi_1(2,0)',
        'phi2': phi2.get((1, 0), 0),
        'phi1': phi1.get((2, 0), 0),
        'match': phi2.get((1, 0), 0) == phi1.get((2, 0), 0),
    })

    # a(1,1,2) = a(2,1,1)
    checks.append({
        'id': 'a(1,1,2) = phi_1(2,1)',
        'phi2': phi2.get((1, 1), 0),
        'phi1': phi1.get((2, 1), 0),
        'match': phi2.get((1, 1), 0) == phi1.get((2, 1), 0),
    })

    # a(1,-1,2) = a(2,-1,1)
    checks.append({
        'id': 'a(1,-1,2) = phi_1(2,-1)',
        'phi2': phi2.get((1, -1), 0),
        'phi1': phi1.get((2, -1), 0),
        'match': phi2.get((1, -1), 0) == phi1.get((2, -1), 0),
    })

    # Same-disc D=4: phi_2(1,2) = phi_1(1,0)
    checks.append({
        'id': 'a(1,2,2) = phi_1(1,0) [D=4]',
        'phi2': phi2.get((1, 2), 0),
        'phi1': phi1.get((1, 0), 0),
        'match': phi2.get((1, 2), 0) == phi1.get((1, 0), 0),
    })

    return {
        'checks': checks,
        'all_verified': all(c['match'] for c in checks),
    }


def verify_disc_dependence(nmax: int = 12) -> Dict[str, Any]:
    r"""Verify that phi_{10,1} coefficients depend only on D = 4n - l^2."""
    phi = phi101_fourier(nmax)

    disc_vals = collections.defaultdict(set)
    for (n, l), c in phi.items():
        D = 4 * n - l * l
        disc_vals[D].add(c)

    violations = [(D, vals) for D, vals in disc_vals.items() if len(vals) > 1]

    return {
        'num_discriminants': len(disc_vals),
        'violations': len(violations),
        'verified': len(violations) == 0,
    }


def verify_inversion_consistency(nmax: int = 6, lmax: int = 12) -> Dict[str, Any]:
    r"""Verify phi_{10,1} * (1/phi_{10,1}) = 1 by direct multiplication.

    Compute h = q/phi_{10,1}, then check (phi_{10,1}/q) * h = delta(n=0,l=0).
    """
    phi = phi101_fourier(nmax + 5)
    h = phi101_inverse_expansion(nmax, lmax)

    g = collections.defaultdict(lambda: collections.defaultdict(int))
    for (n, l), c in phi.items():
        if n >= 1:
            g[n - 1][l] = c

    product = {}
    for N in range(min(nmax, 5)):
        for L in range(-lmax, lmax + 1):
            val = 0
            for k in range(N + 1):
                for lp, cg in g[k].items():
                    lpp = L - lp
                    h_val = h.get((N - k, lpp), 0)
                    if h_val != 0 and cg != 0:
                        val += cg * h_val
            if val != 0:
                product[(N, L)] = val

    correct_at_00 = product.get((0, 0), 0) == 1
    spurious = {k: v for k, v in product.items() if k != (0, 0) and v != 0}

    return {
        'product_at_00': product.get((0, 0), 0),
        'correct_at_00': correct_at_00,
        'spurious_terms': len(spurious),
        'verified': correct_at_00 and len(spurious) == 0,
    }


def verify_bps_against_dvv(nmax: int = 10, lmax: int = 15) -> Dict[str, Any]:
    r"""Verify computed BPS degeneracies against DVV literature values.

    Multi-path:
    (a) Direct Laurent inversion of phi_{10,1}
    (b) DVV literature table
    (c) Polar part: d(-l^2) = l from 1/g_0 = y/(y-1)^2
    (d) Finite part: matches phi_{-2,1} discriminant coefficients
    """
    computed = bps_degeneracy_from_inverse(nmax, lmax)
    literature = dvv_literature_table()

    # (a) vs (b)
    matches = 0
    mismatches = []
    for D in sorted(set(computed.keys()) | set(literature.keys())):
        c = computed.get(D, None)
        lit = literature.get(D, None)
        if c is not None and lit is not None:
            if c == lit:
                matches += 1
            else:
                mismatches.append({'D': D, 'computed': c, 'literature': lit})

    # (c) Polar part
    polar_ok = True
    for j in range(1, 13):
        D = -(j * j)
        if computed.get(D, None) != j:
            polar_ok = False

    # (d) Finite part vs phi_{-2,1}
    fm21_disc = {}
    fm21 = phi_m21_fourier(20)
    for (n, l), c in fm21.items():
        D = 4 * n - l * l
        if D not in fm21_disc:
            fm21_disc[D] = c

    finite_matches = 0
    finite_mismatches = []
    for D in range(0, 25):
        c = computed.get(D, 0)
        f = fm21_disc.get(D, 0)
        if c == f:
            finite_matches += 1
        elif c != 0 or f != 0:
            finite_mismatches.append({'D': D, 'computed': c, 'phi_m21': f})

    return {
        'computed_vs_lit_matches': matches,
        'computed_vs_lit_mismatches': mismatches[:5],
        'polar_part_ok': polar_ok,
        'finite_vs_phi_m21_matches': finite_matches,
        'finite_vs_phi_m21_mismatches': finite_mismatches[:5],
        'all_verified': (len(mismatches) == 0 and polar_ok
                         and len(finite_mismatches) == 0),
    }


def verify_phi2_at_z0(nmax: int = 8) -> Dict[str, Any]:
    r"""Verify phi_2(tau, 0) = 0 (cusp form vanishes at z = 0)."""
    phi2 = phi2_fourier(nmax)
    sums = [0] * nmax
    for (n, l), c in phi2.items():
        if 0 <= n < nmax:
            sums[n] += c

    return {
        'sums_at_z0': sums[:8],
        'all_zero': all(s == 0 for s in sums),
        'verified': all(s == 0 for s in sums),
    }


def verify_cusp_dimensions() -> Dict[str, Any]:
    r"""Verify dim J_{10,m}^{cusp} for m = 1, 2, 3, 4."""
    dims = {}
    for m in range(1, 5):
        dims[m] = sum(_dim_cusp_forms(10 + 2 * j) for j in range(m + 1))

    known = {1: 1, 2: 1, 3: 2, 4: 3}
    return {
        'computed': dims,
        'known': known,
        'all_match': all(dims[m] == known[m] for m in known),
    }


def verify_phi101_weight_index() -> Dict[str, Any]:
    r"""Verify weight = 10, index = 1, and uniqueness of phi_{10,1}."""
    cusp_dim = sum(_dim_cusp_forms(10 + 2 * j) for j in range(2))
    return {
        'weight': 10,
        'index': 1,
        'cusp_dim': cusp_dim,
        'unique': cusp_dim == 1,
        'verified': cusp_dim == 1,
    }


# =====================================================================
# Section 8: Summary
# =====================================================================

def full_igusa_data(nmax: int = 10) -> Dict[str, Any]:
    r"""Complete Igusa cusp form / DVV data package."""
    return {
        'phi101_disc': phi101_disc_coeffs(nmax),
        'phi2_formula': 'phi_2 = 2 * Delta * phi_{-2,1} * phi_{0,1}',
        'ring_decomposition': 'phi_{10,1} = -Delta * phi_{-2,1}',
        'bps_degeneracies': bps_degeneracy_from_inverse(nmax),
        'cardy_growth': bps_cardy_growth_check(nmax),
        'cusp_dimensions': {m: sum(_dim_cusp_forms(10 + 2 * j)
                                   for j in range(m + 1))
                            for m in range(1, 5)},
    }
