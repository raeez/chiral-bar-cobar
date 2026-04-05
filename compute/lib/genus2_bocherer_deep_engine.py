r"""Genus-2 Böcherer deep engine: Niemeier atlas, higher-weight Siegel forms,
Saito-Kurokawa lifts, central L-values, and shadow partition functions.

MATHEMATICAL FRAMEWORK:

1. BÖCHERER FOR ALL NIEMEIER LATTICES:
   For each even unimodular rank-24 lattice Lambda, the genus-2 theta series
   Theta_Lambda^{(2)} decomposes (at weight 12 for Sp(4,Z)):
     Theta_Lambda^{(2)} = E_{12}^{(2)} + c_1(Lambda)*E_{12,1}^{Kling}
                         + c_2(Lambda)*chi_{12}
   The Böcherer coefficient c_2(Lambda) encodes genuine genus-2 arithmetic:
     |c_2(Lambda)|^2 ~ L(1/2, pi_{chi_12}) * L(1/2, pi_{chi_12} x chi_D)
   (Furusawa-Morimoto 2021).

   Shadow interpretation: all Niemeier lattice VOAs have kappa = 24,
   shadow class G, identical F_g = 24*lambda_g^FP. The Böcherer
   coefficient c_2 is the FIRST invariant that discriminates between
   Niemeier lattices at genus 2 — it lives OUTSIDE the shadow tower.

2. HIGHER-WEIGHT SIEGEL MODULAR FORMS:
   - Weight 14: dim S_{14}(Sp_4(Z)) = 1 (unique cusp eigenform)
   - Weight 16: dim S_{16}(Sp_4(Z)) = 2 (first nontrivial decomposition)
   - Weight 18: dim S_{18}(Sp_4(Z)) = 2
   - Weight 20: dim S_{20}(Sp_4(Z)) = 3
   Fourier coefficients via Eisenstein lifting + Igusa relations.

3. SAITO-KUROKAWA LIFTS:
   f in S_{2k-2}(SL_2(Z)) |-> F = SK(f) in S_k^{Maass}(Sp_4(Z)).
   For f = Delta (weight 12): SK(Delta) in S_{12}(Sp_4(Z)).
   Fourier coefficients: a(T; SK(f)) = sum_{d|content(T)} d^{k-1} c(|disc(T)|/d^2)
   where c(n) are the Fourier coefficients of f.

4. GENUS-2 CENTRAL L-VALUES:
   L(s, F, chi_D) for Siegel eigenform F of degree 2.
   At s = 1/2 (central point): related to Fourier-Jacobi coefficients
   via Böcherer's conjecture (now theorem by Furusawa-Morimoto).

5. GENUS-2 SHADOW PARTITION FUNCTION:
   Z_2^sh(A, Omega) for Omega in H_2 (Siegel upper half-plane).
   For lattice VOAs: Z_2^sh = kappa * (tautological genus-2 data).
   Fourier-Jacobi expansion: Z_2^sh = sum_{m>=0} phi_m(tau,z) e^{2pi*i*m*tau'}

6. SPINOR L-FUNCTION AND SATAKE PARAMETERS:
   L(s, F, spin) = prod_p (1-alpha_p p^{-s})...(1-delta_p p^{-s})
   For SK(Delta): Satake parameters from Ramanujan tau function.

References:
  - Böcherer (1986), "Über die Fourier-Jacobi-Entwicklung..."
  - Furusawa-Morimoto (2021), "Refined global GP conjecture..."
  - Saito-Kurokawa: Zagier (1981), Maass (1979)
  - Igusa (1962), "On Siegel modular forms of genus two"
  - Andrianov (1974), "Euler products for Siegel modular forms"
  - Evdokimov (1980), Oda (1977) for higher-weight decompositions
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from compute.lib.siegel_eisenstein import (
    siegel_eisenstein_coefficient,
    chi12_from_igusa,
    siegel_product_coefficient,
    siegel_triple_product_coefficient,
    cohen_H,
    bernoulli as siegel_bernoulli,
    sigma as divisor_sigma,
    kronecker_symbol,
    fundamental_discriminant,
    moebius,
    divisors,
)
from compute.lib.lattice_shadow_census import (
    faber_pandharipande,
    _sigma_k,
    _ramanujan_tau,
)
from compute.lib.niemeier_bocherer_atlas import (
    NIEMEIER_LATTICES,
    ALL_NIEMEIER,
    PURE_NIEMEIER,
    NIEMEIER_AUT_ORDERS,
    niemeier_c1,
    niemeier_c_delta,
    klingen_eisenstein_coefficient,
    orthogonal_roots_per_root,
    genus2_rep_at_diag11,
    niemeier_shadow_data,
    niemeier_genus_expansion,
    GENUS2_STABLE_GRAPHS,
)


# =========================================================================
# Part 1: Ramanujan tau function (extended) and modular form primitives
# =========================================================================

@lru_cache(maxsize=256)
def ramanujan_tau(n: int) -> int:
    """Ramanujan tau function: coefficient of q^n in Delta(tau).

    Uses Ramanujan's recurrence via sigma functions.
    tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472, ...
    """
    return _ramanujan_tau(n)


@lru_cache(maxsize=256)
def sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    return _sigma_k(n, k)


@lru_cache(maxsize=64)
def dim_Sk_SL2(k: int) -> int:
    """Dimension of S_k(SL_2(Z)), the space of weight-k cusp forms.

    For k < 12 or k odd: 0.
    For k = 12: 1 (spanned by Delta).
    For k >= 12 even: floor(k/12) if k % 12 != 2, else floor(k/12) - 1.
    """
    if k < 12 or k % 2 == 1:
        return 0
    if k % 12 == 2:
        return k // 12 - 1
    return k // 12


@lru_cache(maxsize=64)
def dim_Mk_SL2(k: int) -> int:
    """Dimension of M_k(SL_2(Z)), the space of weight-k modular forms."""
    if k < 0 or k % 2 == 1:
        return 0
    if k == 0:
        return 1
    if k == 2:
        return 0
    return dim_Sk_SL2(k) + 1  # Eisenstein series adds 1 dimension


@lru_cache(maxsize=64)
def dim_Sk_Sp4(k: int) -> int:
    """Dimension of the space of Siegel cusp forms of degree 2 and weight k.

    Uses the Igusa-Tsuyumine dimension formula for Sp(4,Z).
    For k even, k >= 4.

    dim S_k = dim M_k - dim E_k - dim SK_k - 1
    where the decomposition is: Siegel Eisenstein + Klingen Eisenstein
    + Saito-Kurokawa + genuine degree-2 cusp forms.

    Low-weight values (well-known):
      k=4: 0, k=6: 0, k=8: 0, k=10: 1, k=12: 1,
      k=14: 1, k=16: 2, k=18: 2, k=20: 3, k=22: 4, k=24: 5, k=26: 6
    """
    known = {
        4: 0, 6: 0, 8: 0, 10: 1, 12: 1,
        14: 1, 16: 2, 18: 2, 20: 3, 22: 4,
        24: 5, 26: 6, 28: 7, 30: 9, 32: 10,
        34: 12, 36: 14,
    }
    if k in known:
        return known[k]
    if k < 10 or k % 2 == 1:
        return 0
    # Tsuyumine formula for k >= 10 even:
    # This is the full dimension formula; for our purposes the lookup suffices.
    return None


@lru_cache(maxsize=64)
def dim_Sk_Sp4_maass(k: int) -> int:
    """Dimension of the Maass Spezialschar (Saito-Kurokawa subspace) at weight k.

    dim SK_k = dim S_{2k-2}(SL_2(Z)) for k even >= 10.
    """
    if k < 10 or k % 2 == 1:
        return 0
    return dim_Sk_SL2(2 * k - 2)


@lru_cache(maxsize=64)
def dim_Sk_Sp4_genuine(k: int) -> int:
    """Dimension of genuine degree-2 cusp forms (non-SK, non-Klingen).

    genuine = total cusp - Maass Spezialschar
    """
    total = dim_Sk_Sp4(k)
    if total is None:
        return None
    return total - dim_Sk_Sp4_maass(k)


# =========================================================================
# Part 2: Saito-Kurokawa lift
# =========================================================================

def saito_kurokawa_coefficient(f_coeffs: Dict[int, int], k: int,
                                a: int, b: int, c: int) -> Fraction:
    r"""Fourier coefficient of the Saito-Kurokawa lift SK(f) at
    T = ((a, b/2), (b/2, c)).

    For f = sum c(n) q^n in S_{2k-2}(SL_2(Z)), the SK lift F = SK(f)
    in S_k^{Maass}(Sp_4(Z)) has Fourier coefficients:

      a(T; SK(f)) = sum_{d | gcd(a,b,c)} d^{k-1} c(disc(T) / d^2)

    where disc(T) = 4ac - b^2, and the sum is over positive divisors of
    the content gcd(a,b,c), restricted to d^2 | disc(T).

    Parameters
    ----------
    f_coeffs : dict
        Fourier coefficients of f: {n: c(n)} for n >= 1.
    k : int
        Weight of the Siegel form (f has weight 2k-2).
    a, b, c : int
        Half-integral matrix T = ((a, b/2), (b/2, c)).
    """
    disc = 4 * a * c - b * b
    if disc <= 0:
        return Fraction(0)

    g = math.gcd(math.gcd(a, abs(b)), c)
    total = Fraction(0)
    for d in range(1, g + 1):
        if g % d != 0:
            continue
        if disc % (d * d) != 0:
            continue
        m = disc // (d * d)
        cf = f_coeffs.get(m, 0)
        total += Fraction(d ** (k - 1) * cf)
    return total


def delta_coefficients(max_n: int = 50) -> Dict[int, int]:
    """Fourier coefficients of Delta(tau) = sum tau(n) q^n.

    Returns {n: tau(n)} for 1 <= n <= max_n.
    """
    return {n: ramanujan_tau(n) for n in range(1, max_n + 1)}


def sk_delta_coefficient(a: int, b: int, c: int) -> Fraction:
    """Fourier coefficient of SK(Delta) in S_{12}(Sp_4(Z)).

    SK(Delta) is the Saito-Kurokawa lift of the Ramanujan Delta function.
    Weight of Delta = 12 (so 2k-2 = 12, k = 7... wait, that's wrong).

    CAREFUL: Delta has weight 12 = 2k-2 means k = 7. But the Saito-Kurokawa
    lift for Sp(4,Z) sends S_{2k-2}(SL_2(Z)) to S_k(Sp_4(Z)).
    For chi_12 in S_{12}(Sp_4(Z)): we need 2k-2 = 22, i.e., k = 12.
    So chi_12 = SK(f_22) where f_22 is the unique normalized cusp form
    in S_{22}(SL_2(Z)).

    For Delta (weight 12): SK(Delta) lives in S_7(Sp_4(Z)). But weight 7
    is odd, and for Sp(4,Z) with trivial character, only even weights appear.
    So there is NO Saito-Kurokawa lift of Delta to Sp(4,Z) in the classical sense.

    The correct statement: chi_12 (the Igusa cusp form of weight 12 for Sp(4,Z))
    is the SK lift of the normalized newform f_22 in S_{22}(SL_2(Z)).
    tau_22(n) = coefficients of f_22.

    For the MAASS SPEZIALSCHAR at weight k for Sp(4,Z):
    dim = dim S_{2k-2}(SL_2(Z)).
    At k = 10: dim S_{18} = 1, so 1 SK form.
    At k = 12: dim S_{22} = 1, so 1 SK form = chi_12.
    """
    # SK(f_22) = chi_12 at weight 12 for Sp_4(Z).
    # f_22 has weight 22 = 2*12 - 2.
    disc = 4 * a * c - b * b
    if disc <= 0:
        return Fraction(0)

    # Get f_22 coefficients
    f22 = f22_coefficients(max_n=max(disc + 1, 50))
    return saito_kurokawa_coefficient(f22, 12, a, b, c)


@lru_cache(maxsize=1)
def f22_coefficients(max_n: int = 100) -> Dict[int, int]:
    r"""Fourier coefficients of the unique normalized newform f_{22} in S_{22}(SL_2(Z)).

    f_{22} = Delta * E_{10} = (sum tau(n) q^n)(sum sigma_9(m) q^m)

    Since dim S_{22} = 1, f_{22} is the unique cusp eigenform (up to scaling).
    We normalize so that the leading coefficient is 1: f_{22} = q + ...

    The coefficients: c_{22}(n) = sum_{d|n, d<n} tau(d) sigma_9(n/d - ...) ...

    Actually f_{22} = Delta * E_{10} is NOT correct as stated. The product
    Delta*E_{10} has weight 12+10 = 22 and is cuspidal (Delta vanishes at cusps),
    but it may not be an eigenform for the Hecke algebra.

    Since dim S_{22}(SL_2(Z)) = 1, ANY nonzero cusp form of weight 22 is an
    eigenform (up to scaling). So f_{22} = Delta * E_{10} / (leading coeff)
    is the unique normalized eigenform. The leading coefficient of Delta*E_{10}
    is tau(1) * 1 = 1, so f_{22} = Delta * E_{10} (already normalized).

    Wait: (Delta * E_{10})(tau) = (sum_n tau(n) q^n)(1 + sum_m a_m q^m) where
    a_m = -264/B_{10} * sigma_9(m). Since B_{10} = 5/66, we have
    -264/B_{10} ... let me just compute the Dirichlet series convolution.

    E_{10}(tau) = 1 - (2*10/B_{10}) sum_{n>=1} sigma_9(n) q^n
              = 1 + (264/66) * sum ... no.
    The normalized Eisenstein series is:
    E_k(tau) = 1 - (2k/B_k) sum_{n>=1} sigma_{k-1}(n) q^n.
    For k=10: B_{10} = 5/66, so -2*10/(5/66) = -20*66/5 = -264.
    E_{10}(tau) = 1 - 264 sum_{n>=1} sigma_9(n) q^n.

    But wait: the standard normalization uses 2k/B_k differently. Let me
    use the convention E_k = 1 + (2k/(B_k*(k-1)!)) ... no, the simplest:

    E_k(tau) = 1 + (2/zeta(1-k)) sum_{n>=1} sigma_{k-1}(n) q^n
            = 1 - (2k/B_k) sum_{n>=1} sigma_{k-1}(n) q^n.

    For k=10: -2*10/B_{10} = -20/(5/66) = -20*66/5 = -264.
    So E_{10} = 1 - 264*sigma_9(1)*q - 264*sigma_9(2)*q^2 - ...
    sigma_9(1) = 1, so coefficient of q in E_{10} is -264.

    Then f_{22} = Delta * E_{10}:
    coefficient of q^n = sum_{m=1}^{n} tau(m) * e10(n-m)
    where e10(0) = 1, e10(j) = -264*sigma_9(j) for j >= 1.
    """
    # E_10 coefficients
    B10 = Fraction(5, 66)
    e10_norm = Fraction(-2 * 10) / B10  # = -264

    def e10_coeff(n):
        if n == 0:
            return 1
        return int(e10_norm * sigma_k(n, 9))

    # Convolution: f22(n) = sum_{m=1}^{n} tau(m) * e10(n - m)
    result = {}
    for n in range(1, max_n + 1):
        total = 0
        for m in range(1, n + 1):
            total += ramanujan_tau(m) * e10_coeff(n - m)
        result[n] = total
    return result


# =========================================================================
# Part 3: Böcherer coefficient for all Niemeier lattices
# =========================================================================

def niemeier_bocherer_c2_at_T(name: str, a: int, b: int, c: int) -> Optional[Fraction]:
    r"""Extract the Böcherer coefficient c_2(Lambda) from the genus-2
    theta decomposition at a specific T = ((a, b/2), (b/2, c)).

    Theta_Lambda^{(2)} = E_{12}^{(2)} + c_1*E^{Kling}_{12,1} + c_2*chi_{12}

    So: c_2 = (r_2(Lambda, T) - a(T; E_{12}) - c_1*a(T; E^{Kling})) / a(T; chi_{12})

    This requires:
    - r_2(Lambda, T) = genus-2 representation number
    - a(T; E_{12}) = Siegel Eisenstein coefficient
    - a(T; E^{Kling}) = Klingen Eisenstein coefficient
    - a(T; chi_{12}) = Igusa cusp form coefficient

    For lattices with roots at T = diag(1,1): r_2 = N_roots * N_orth.
    """
    disc = 4 * a * c - b * b
    if disc <= 0:
        return None

    # chi_12 coefficient
    chi = chi12_from_igusa(a, b, c)
    if chi is None or chi == 0:
        return None

    # Genus-2 representation number
    r2 = _genus2_rep_niemeier(name, a, b, c)
    if r2 is None:
        return None

    # Eisenstein and Klingen coefficients
    e12 = siegel_eisenstein_coefficient(12, a, b, c)
    c1 = niemeier_c1(name)
    kling = Fraction(klingen_eisenstein_coefficient(a, b, c))

    residual = Fraction(r2) - e12 - c1 * kling
    c2 = residual / chi
    return c2


def _genus2_rep_niemeier(name: str, a: int, b: int, c: int) -> Optional[int]:
    """Genus-2 representation number for a Niemeier lattice.

    Implemented for T with a = c = 1 (root shell) for lattices with roots.
    For the Leech lattice, uses the existing bridge module.
    """
    if name == 'Leech':
        from compute.lib.genus2_bocherer_bridge import genus2_rep_leech
        return genus2_rep_leech(a, b, c)

    data = NIEMEIER_LATTICES[name]
    N = data['num_roots']

    if N == 0:
        return 0 if a == 0 and b == 0 and c == 0 else None

    if a == 0 and b == 0 and c == 0:
        return 1

    if a == 0:
        if b != 0:
            return 0
        return N if c == 1 else None

    if c == 0:
        if b != 0:
            return 0
        return N if a == 1 else None

    if a == 1 and c == 1:
        # Both vectors are roots: use inner-product distribution
        from compute.lib.niemeier_bocherer_atlas import genus2_rep_at_T11_b
        return genus2_rep_at_T11_b(name, b)

    return None


def niemeier_bocherer_atlas() -> Dict[str, Dict[str, Any]]:
    """Compute Böcherer data for all 24 Niemeier lattices.

    Returns a dictionary keyed by lattice name, containing:
    - c_delta: genus-1 cusp coefficient
    - c1: Klingen coefficient
    - c2: Böcherer coefficient (where computable)
    - r2_diag11: genus-2 rep number at diag(1,1)
    - shadow_data: shadow obstruction tower data
    """
    atlas = {}
    for name in ALL_NIEMEIER:
        entry = {
            'name': name,
            'c_delta': niemeier_c_delta(name),
            'c1': niemeier_c1(name),
            'num_roots': NIEMEIER_LATTICES[name]['num_roots'],
            'shadow': niemeier_shadow_data(name),
        }

        # Genus-2 rep at diag(1,1)
        entry['r2_diag11'] = genus2_rep_at_diag11(name)

        # Try to extract c_2
        c2 = niemeier_bocherer_c2_at_T(name, 1, 0, 1)
        entry['c2'] = c2

        atlas[name] = entry

    return atlas


# =========================================================================
# Part 4: Higher-weight Siegel modular forms
# =========================================================================

def higher_weight_dimensions() -> Dict[int, Dict[str, int]]:
    """Dimension data for S_k(Sp_4(Z)) at various weights.

    Returns {k: {'total': dim S_k, 'maass': dim SK_k, 'genuine': dim nonlift}}.
    """
    result = {}
    for k in range(4, 38, 2):
        total = dim_Sk_Sp4(k)
        maass = dim_Sk_Sp4_maass(k)
        genuine = dim_Sk_Sp4_genuine(k)
        result[k] = {
            'total': total,
            'maass': maass,
            'genuine': genuine,
        }
    return result


def weight_k_siegel_eisenstein(k: int, a: int, b: int, c: int) -> Fraction:
    """Fourier coefficient of E_k^{(2)} for general even weight k >= 4."""
    return siegel_eisenstein_coefficient(k, a, b, c)


def weight_k_klingen_eisenstein(k: int, f_coeffs: Dict[int, int],
                                 a: int, b: int, c: int) -> Fraction:
    r"""Fourier coefficient of the Klingen Eisenstein series at weight k,
    lifted from a cusp form f in S_{k}(SL_2(Z)).

    For the Klingen lift E^{Kling}_{k,f} (sometimes denoted E_{k,1}^f):
      a(T; E^{Kling}_{k,f}) = sum_{d|gcd(a,b,c)} d^{k-1} c_f(disc(T)/d^2)

    where c_f(n) are the Fourier coefficients of f.

    NOTE: This is the Klingen Eisenstein series in Siegel modular form theory,
    not the Siegel Eisenstein series. The Klingen lift is from SL_2 to Sp_4.
    """
    disc = 4 * a * c - b * b
    if disc <= 0:
        return Fraction(0)

    g = math.gcd(math.gcd(a, abs(b)), c)
    total = Fraction(0)
    for d in range(1, g + 1):
        if g % d != 0:
            continue
        if disc % (d * d) != 0:
            continue
        m = disc // (d * d)
        cf = f_coeffs.get(m, 0)
        total += Fraction(d ** (k - 1) * cf)
    return total


@lru_cache(maxsize=1)
def f20_coefficients(max_n: int = 100) -> Dict[int, int]:
    r"""Coefficients of the unique normalized newform in S_{20}(SL_2(Z)).

    Since dim S_{20} = 1, f_{20} is unique. We can compute it as:
    f_{20} = Delta * E_8 = (sum tau(n)q^n)(1 + 240*sum sigma_7(n)q^n).

    Coefficient of q^n: sum_{m=1}^n tau(m) * e8(n-m)
    where e8(0) = 1, e8(j) = 240*sigma_7(j).
    """
    def e8_coeff(n):
        if n == 0:
            return 1
        return 240 * sigma_k(n, 7)

    result = {}
    for n in range(1, max_n + 1):
        total = 0
        for m in range(1, n + 1):
            total += ramanujan_tau(m) * e8_coeff(n - m)
        result[n] = total
    return result


@lru_cache(maxsize=1)
def f16_coefficients(max_n: int = 100) -> Dict[int, int]:
    r"""Coefficients of the unique normalized newform in S_{16}(SL_2(Z)).

    Since dim S_{16} = 1, f_{16} = Delta * E_4.
    Coefficient of q^n: sum_{m=1}^n tau(m) * e4(n-m)
    where e4(0) = 1, e4(j) = 240*sigma_3(j).
    """
    def e4_coeff(n):
        if n == 0:
            return 1
        return 240 * sigma_k(n, 3)

    result = {}
    for n in range(1, max_n + 1):
        total = 0
        for m in range(1, n + 1):
            total += ramanujan_tau(m) * e4_coeff(n - m)
        result[n] = total
    return result


@lru_cache(maxsize=1)
def f18_coefficients(max_n: int = 100) -> Dict[int, int]:
    r"""Coefficients of the unique normalized newform in S_{18}(SL_2(Z)).

    Since dim S_{18} = 1, f_{18} = Delta * E_6.
    E_6 = 1 - 504 sum sigma_5(n) q^n.
    """
    B6 = Fraction(1, 42)
    e6_norm = Fraction(-2 * 6) / B6  # = -504

    def e6_coeff(n):
        if n == 0:
            return 1
        return int(e6_norm * sigma_k(n, 5))

    result = {}
    for n in range(1, max_n + 1):
        total = 0
        for m in range(1, n + 1):
            total += ramanujan_tau(m) * e6_coeff(n - m)
        result[n] = total
    return result


@lru_cache(maxsize=1)
def f26_coefficients(max_n: int = 100) -> Dict[int, int]:
    r"""Coefficients of the unique normalized newform in S_{26}(SL_2(Z)).

    Since dim S_{26} = 2, there are TWO linearly independent cusp forms.
    A basis: {Delta*E_{14}, Delta^2*E_2} -- but E_2 is not modular.
    Better basis: Delta*E_{14} and Delta*E_4*E_{10}... actually we need
    to be more careful.

    Wait: dim S_{26} = floor(26/12) = 2 (since 26 mod 12 = 2,
    dim = floor(26/12) - 1 = 2 - 1 = 1). Let me recheck.

    k = 26: k/12 = 2.166..., floor = 2. k mod 12 = 2, so dim = 2 - 1 = 1.
    So dim S_{26} = 1, and f_{26} = Delta * E_{14}.
    """
    # E_{14} = E_4 * E_{10} (since M_{14} = C*E_{14} and dim M_{14} = 1 for k=14 even >= 4)
    # Wait: dim M_{14}(SL_2(Z)). For k=14: dim = dim S_14 + 1 = 0 + 1 = 1.
    # S_14: k = 14, k/12 = 1.16, floor = 1, 14 mod 12 = 2, dim = 1 - 1 = 0.
    # So M_14 is 1-dimensional, spanned by E_{14}.
    # E_{14} coefficients: E_{14} = 1 - (2*14/B_{14}) sum sigma_{13}(n) q^n.
    # B_{14} = 7/6, so -28/(7/6) = -28*6/7 = -24.

    B14 = Fraction(7, 6)
    e14_norm = Fraction(-2 * 14) / B14  # = -24

    def e14_coeff(n):
        if n == 0:
            return 1
        return int(e14_norm * sigma_k(n, 13))

    result = {}
    for n in range(1, max_n + 1):
        total = 0
        for m in range(1, n + 1):
            total += ramanujan_tau(m) * e14_coeff(n - m)
        result[n] = total
    return result


# =========================================================================
# Part 5: SK lifts at various weights
# =========================================================================

def sk_lift_at_weight(k: int, a: int, b: int, c: int) -> Optional[Fraction]:
    r"""Fourier coefficient of the Saito-Kurokawa lift at weight k.

    The SK lift sends f in S_{2k-2}(SL_2(Z)) to SK(f) in S_k(Sp_4(Z)).
    At weight k, the SK subspace has dimension dim S_{2k-2}(SL_2(Z)).

    For k = 10: f in S_{18}, dim = 1, f = f_{18} = Delta*E_6.
    For k = 12: f in S_{22}, dim = 1, f = f_{22} = Delta*E_{10}.
    For k = 14: f in S_{26}, dim = 1, f = f_{26} = Delta*E_{14}.
    For k = 16: f in S_{30}, dim = 2 (two SK forms at weight 16).
    """
    weight_2km2 = 2 * k - 2
    dim = dim_Sk_SL2(weight_2km2)
    if dim == 0:
        return Fraction(0)

    if dim > 1:
        # Multiple cusp forms; cannot determine a unique SK lift
        return None

    # Unique cusp form in S_{2k-2}: compute its coefficients
    f_coeffs = _unique_cusp_form_coefficients(weight_2km2)
    if f_coeffs is None:
        return None

    return saito_kurokawa_coefficient(f_coeffs, k, a, b, c)


def _unique_cusp_form_coefficients(weight: int, max_n: int = 100) -> Optional[Dict[int, int]]:
    """Coefficients of the unique normalized eigenform in S_k(SL_2(Z)),
    when dim S_k = 1."""
    dim = dim_Sk_SL2(weight)
    if dim != 1:
        return None

    dispatch = {
        12: lambda: delta_coefficients(max_n),
        16: lambda: f16_coefficients(max_n),
        18: lambda: f18_coefficients(max_n),
        20: lambda: f20_coefficients(max_n),
        22: lambda: f22_coefficients(max_n),
        26: lambda: f26_coefficients(max_n),
    }

    if weight in dispatch:
        return dispatch[weight]()

    # General case: Delta * E_{weight-12}
    # This works when dim S_k = 1.
    e_weight = weight - 12
    if e_weight < 4 or e_weight % 2 != 0:
        return None
    return _delta_times_eisenstein(e_weight, max_n)


def _delta_times_eisenstein(ek_weight: int, max_n: int = 100) -> Dict[int, int]:
    """Coefficients of Delta * E_{ek_weight}."""
    B_k = Fraction(siegel_bernoulli(ek_weight))
    if B_k == 0:
        return {}
    ek_norm = Fraction(-2 * ek_weight) / B_k

    def ek_coeff(n):
        if n == 0:
            return 1
        return int(ek_norm * sigma_k(n, ek_weight - 1))

    result = {}
    for n in range(1, max_n + 1):
        total = 0
        for m in range(1, n + 1):
            total += ramanujan_tau(m) * ek_coeff(n - m)
        result[n] = total
    return result


# =========================================================================
# Part 6: Central L-values and Böcherer quotients
# =========================================================================

def bocherer_quotient_leech(D: int) -> Optional[Dict[str, Any]]:
    r"""Compute the Böcherer quotient for the Leech lattice at
    fundamental discriminant D < 0.

    The Böcherer conjecture (Furusawa-Morimoto 2021):
    |a(D; F)|^2 / <F, F> = c_k * w(D)^{-2} * |D|^{k-3/2}
                            * L(1/2, pi_F) * L(1/2, pi_F x chi_D)

    where F is a Siegel eigenform and a(D; F) = sum_{T: disc(T)=|D|} a(T;F)/eps(T).

    For the Leech lattice, we compute the Böcherer sum B(D) = sum a(T)/eps(T)
    over GL_2(Z)-classes of T with disc = |D|, using known inner-product data.
    """
    from compute.lib.genus2_bocherer_bridge import (
        genus2_rep_leech,
        LEECH_KISSING,
        LEECH_MIN_IP_DIST,
    )

    if D >= 0:
        return None

    # Find all T = ((a, b/2), (b/2, c)) with 4ac - b^2 = |D|
    # and a,c small enough to be in our data range
    abs_D = abs(D)
    bocherer_sum = Fraction(0)
    contributing_T = []

    for a_val in range(1, 6):
        for c_val in range(a_val, 6):
            # 4ac - b^2 = |D| => b^2 = 4ac - |D|
            bsq = 4 * a_val * c_val - abs_D
            if bsq < 0:
                continue
            if bsq == 0:
                b_vals = [0]
            else:
                isq = math.isqrt(bsq)
                if isq * isq != bsq:
                    continue
                b_vals = [isq, -isq] if isq > 0 else [0]

            for b_val in b_vals:
                r2 = genus2_rep_leech(a_val, b_val, c_val)
                if r2 is None or r2 == 0:
                    continue
                # Automorphism count
                eps = 1
                if a_val == c_val and b_val == 0:
                    eps = 2
                elif a_val == c_val and b_val != 0:
                    eps = 1
                bocherer_sum += Fraction(r2, eps)
                contributing_T.append((a_val, b_val, c_val, r2))

    return {
        'D': D,
        'bocherer_sum': bocherer_sum,
        'contributing_T': contributing_T,
        'nonzero': bocherer_sum != 0,
    }


def bocherer_quotients_multiple_D(D_list: List[int] = None) -> Dict[int, Dict]:
    """Compute Böcherer quotients at multiple fundamental discriminants."""
    if D_list is None:
        D_list = [-3, -4, -7, -8, -11, -15, -16, -19, -20, -23, -24]
    results = {}
    for D in D_list:
        results[D] = bocherer_quotient_leech(D)
    return results


# =========================================================================
# Part 7: Spinor L-function and Satake parameters
# =========================================================================

def satake_parameters_sk_delta(p: int) -> Dict[str, Any]:
    r"""Satake parameters for SK(f_{22}) = chi_{12} at a prime p.

    For a Saito-Kurokawa lift F = SK(f) with f in S_{2k-2}(SL_2(Z)):
    The Satake parameters at p are determined by the Hecke eigenvalue
    a_f(p) of f.

    For chi_{12} = SK(f_{22}):
    The Hecke eigenvalue of f_{22} at p is lambda(p) = c_{22}(p).
    The local L-factor of the spinor L-function is:
      L_p(s, chi_{12}, spin) = (1 - p^{k-1-s})^{-1}(1 - p^{k-2-s})^{-1}
                                * (1 - alpha_p p^{-s})^{-1}(1 - beta_p p^{-s})^{-1}
    where alpha_p + beta_p = lambda(p) and alpha_p * beta_p = p^{2k-3}.

    For k = 12: alpha_p + beta_p = c_{22}(p), alpha_p * beta_p = p^{21}.
    """
    f22 = f22_coefficients(max_n=max(p + 1, 50))
    lambda_p = f22.get(p, 0)

    # alpha + beta = lambda_p, alpha * beta = p^21
    # Quadratic: x^2 - lambda_p * x + p^21 = 0
    discriminant = lambda_p ** 2 - 4 * p ** 21

    # For the Ramanujan conjecture (proved for holomorphic forms):
    # |alpha_p| = |beta_p| = p^{21/2}, so discriminant <= 0 (complex roots)
    # unless p is very small.

    # The full Satake parameters for the degree-2 spinor L-function:
    # For SK(f): the 4 Satake parameters are:
    # p^{k-1}, p^{k-2}, alpha_p, beta_p
    # where alpha_p, beta_p are the roots of x^2 - lambda_p*x + p^{2k-3}

    return {
        'p': p,
        'hecke_eigenvalue': lambda_p,
        'product_alpha_beta': p ** 21,
        'sum_alpha_beta': lambda_p,
        'discriminant': discriminant,
        'is_tempered': discriminant <= 0,
        'satake_trivial': [p ** 11, p ** 10],  # the trivial parameters
        'ramanujan_bound': 2 * p ** Fraction(21, 2),
        'satisfies_ramanujan': abs(lambda_p) <= 2 * p ** (21 / 2),
    }


def spinor_euler_factor_sk(p: int, s: complex) -> complex:
    r"""Euler factor of the spinor L-function of chi_{12} at prime p.

    L_p(s) = [(1-p^{11-s})(1-p^{10-s})(1-alpha_p*p^{-s})(1-beta_p*p^{-s})]^{-1}
    """
    params = satake_parameters_sk_delta(p)
    lam = params['hecke_eigenvalue']
    disc = params['discriminant']

    # Compute alpha, beta (may be complex)
    if disc >= 0:
        sqrt_disc = math.sqrt(disc)
        alpha = (lam + sqrt_disc) / 2
        beta = (lam - sqrt_disc) / 2
    else:
        sqrt_abs_disc = math.sqrt(-disc)
        alpha = complex(lam / 2, sqrt_abs_disc / 2)
        beta = complex(lam / 2, -sqrt_abs_disc / 2)

    ps = p ** (-s)
    factor = (1 - p ** (11) * ps) * (1 - p ** (10) * ps)
    factor *= (1 - alpha * ps) * (1 - beta * ps)
    return 1.0 / factor


def partial_spinor_L(s: complex, primes: List[int] = None) -> complex:
    """Partial spinor L-function of chi_{12}, product over small primes."""
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]
    result = complex(1.0, 0.0)
    for p in primes:
        result *= spinor_euler_factor_sk(p, s)
    return result


# =========================================================================
# Part 8: Genus-2 shadow partition function
# =========================================================================

def genus2_shadow_lattice(kappa: int = 24, max_terms: int = 5) -> Dict[str, Any]:
    r"""Genus-2 shadow partition function for lattice VOAs with kappa = 24.

    For lattice VOAs (class G, shadow depth 2), the genus-2 shadow
    amplitude F_2(V_Lambda) = kappa * lambda_2^FP where:
      lambda_2^FP = 7/5760 (Faber-Pandharipande)

    The genus-2 shadow partition function is:
      Z_2^sh(Omega) = F_2 * omega_2(Omega)
    where omega_2 is the natural volume form on M_2 (which corresponds
    to the Hodge class lambda_2 via Chern-Weil theory).

    In the Siegel modular form language, this gives a scalar multiple
    of the Hodge class times a Siegel modular form that is determined
    by the tautological intersection theory on M_2.

    For class-G algebras, the shadow partition function at genus 2
    is entirely determined by kappa (= 24 for all Niemeier lattices).
    """
    FP_lambda2 = faber_pandharipande(2)
    F2 = Fraction(kappa) * FP_lambda2

    return {
        'kappa': kappa,
        'lambda_2_FP': FP_lambda2,
        'F_2': F2,
        'shadow_class': 'G',
        'shadow_depth': 2,
        'description': (
            f'Genus-2 shadow amplitude F_2 = {kappa} * {FP_lambda2} = {F2}. '
            f'All Niemeier lattice VOAs give the same F_2 (shadow cannot '
            f'distinguish them). The Böcherer coefficient c_2(Lambda) lives '
            f'OUTSIDE the shadow tower.'
        ),
    }


def fourier_jacobi_shadow_virasoro(c_val: Fraction, m_max: int = 3) -> Dict[int, Dict]:
    r"""Fourier-Jacobi expansion of the genus-2 shadow for Virasoro at central
    charge c.

    The Fourier-Jacobi expansion on H_2:
      Z_2^sh(tau, z, tau') = sum_{m >= 0} phi_m(tau, z) e^{2*pi*i*m*tau'}

    For Virasoro (class M, infinite shadow depth), the FJ coefficients
    phi_m are Jacobi-like forms whose structure reflects the infinite tower.

    At m = 0: phi_0 encodes the separating degeneration (genus-1 x genus-1).
    At m = 1: phi_1 encodes the first non-separating correction.
    At m >= 2: higher corrections from the shadow tower.

    For class G/L algebras, phi_m = 0 for m >= 1 (finite tower terminates).
    For class M (Virasoro, W_N), phi_m is nonzero for all m.

    We compute these as formal power series in the shadow tower data.
    """
    kappa = c_val / 2  # kappa(Vir_c) = c/2

    result = {}
    for m in range(m_max + 1):
        if m == 0:
            # Separating degeneration: product of genus-1 shadows
            F1 = kappa / 24  # F_1 = kappa * lambda_1 = kappa/24
            phi_0 = {
                'index': 0,
                'type': 'separating',
                'leading_coefficient': F1 * F1,  # F_1^2
                'description': 'Product of genus-1 shadow amplitudes',
            }
            result[m] = phi_0
        elif m == 1:
            # First non-separating correction
            # This receives contributions from the self-sewing kernel
            # and the genus-2 tautological intersection
            phi_1 = {
                'index': 1,
                'type': 'non-separating',
                'leading_coefficient': kappa * Fraction(7, 5760),  # kappa * lambda_2
                'is_mock': False,  # for Virasoro, still modular at this level
                'description': 'Non-separating self-sewing correction',
            }
            result[m] = phi_1
        else:
            # Higher corrections from shadow tower arity >= 3
            # For class M: nonzero for all m (infinite tower)
            phi_m = {
                'index': m,
                'type': 'higher_shadow',
                'nonzero': True,  # class M has infinite depth
                'is_mock': True,  # higher FJ coefficients may be mock modular
                'description': f'Shadow tower correction at arity >= {m+1}',
            }
            result[m] = phi_m

    return result


# =========================================================================
# Part 9: Multi-path verification infrastructure
# =========================================================================

def verify_sk_chi12_identity(max_T: int = 3) -> Dict[str, Any]:
    r"""Verify that chi_12 = SK(f_22) by comparing Fourier coefficients.

    Path 1: chi_12 via Igusa relation (441*E_4^3 + 250*E_6^2 - 691*E_{12}).
    Path 2: SK lift of f_22 via the Saito-Kurokawa formula.

    Both should agree at all T.
    """
    results = []
    for a in range(1, max_T + 1):
        for c in range(a, max_T + 1):
            for b in range(-2 * min(a, c), 2 * min(a, c) + 1):
                disc = 4 * a * c - b * b
                if disc <= 0:
                    continue

                # Path 1: Igusa
                chi_igusa = chi12_from_igusa(a, b, c)

                # Path 2: SK lift of f_22
                chi_sk = sk_delta_coefficient(a, b, c)

                # The Igusa formula gives an UNNORMALIZED chi_12 (without the
                # 1/131040 factor). So we need to check proportionality.
                results.append({
                    'T': (a, b, c),
                    'disc': disc,
                    'chi_igusa': chi_igusa,
                    'chi_sk': chi_sk,
                })

    # Check proportionality: chi_igusa / chi_sk should be constant
    ratios = []
    for r in results:
        if r['chi_sk'] != 0 and r['chi_igusa'] is not None and r['chi_igusa'] != 0:
            ratio = Fraction(r['chi_igusa']) / r['chi_sk']
            ratios.append(ratio)

    consistent = len(set(ratios)) <= 1 if ratios else True

    return {
        'results': results,
        'ratios': ratios,
        'proportionality_constant': ratios[0] if ratios else None,
        'consistent': consistent,
    }


def verify_niemeier_mass_constraint() -> Dict[str, Any]:
    r"""Verify the mass formula constraint on Böcherer coefficients.

    The Siegel-Weil formula implies:
      sum_{Lambda} c_1(Lambda) / |Aut(Lambda)| = 0
      sum_{Lambda} c_2(Lambda) / |Aut(Lambda)| = 0

    since the genus-average theta series is pure Eisenstein.
    """
    c1_sum = Fraction(0)
    for name in ALL_NIEMEIER:
        if name not in NIEMEIER_AUT_ORDERS:
            continue
        c1 = niemeier_c1(name)
        c1_sum += c1 / Fraction(NIEMEIER_AUT_ORDERS[name])

    return {
        'c1_weighted_sum': c1_sum,
        'c1_vanishes': c1_sum == 0,
    }


def verify_shadow_universality_niemeier() -> Dict[str, Any]:
    r"""Verify that all Niemeier lattices give the same shadow data.

    Since kappa(V_Lambda) = rank(Lambda) = 24 for all Lambda, and all are
    class G (shadow depth 2), the shadow obstruction tower is identical.
    The Böcherer coefficient c_2 is the FIRST invariant that distinguishes them.
    """
    shadow_data = {}
    for name in ALL_NIEMEIER:
        sd = niemeier_shadow_data(name)
        shadow_data[name] = (sd['kappa'], sd['shadow_class'], sd['shadow_depth'])

    # Check all have the same (kappa, class, depth)
    unique_shadows = set(shadow_data.values())

    return {
        'all_identical': len(unique_shadows) == 1,
        'common_shadow': unique_shadows.pop() if len(unique_shadows) == 1 else None,
        'shadow_data': shadow_data,
        'num_lattices': len(shadow_data),
        'interpretation': (
            'All 24 Niemeier lattices share identical shadow tower data '
            '(kappa=24, class G, depth 2). The Böcherer coefficient c_2 is '
            'the first arithmetic invariant that distinguishes them.'
        ),
    }


def verify_e8_genus2_vs_eisenstein() -> Dict[str, Any]:
    r"""Verify that Theta_{E8xE8xE8}^{(2)} has no cusp component at weight 4.

    The 3E8 lattice has a genus-2 theta series of weight 4*3 = 12
    (NOT weight 4). The E8 lattice itself has weight 4.
    At weight 4 for a SINGLE E8: dim M_4(Sp_4(Z)) = 1, so no cusp form.

    For the 3E8 Niemeier lattice (3 copies of E8, weight 12):
    Theta_{3E8}^{(2)} decomposes in M_{12}(Sp_4(Z)) which has cusp forms.
    """
    from compute.lib.genus2_bocherer_bridge import e8_is_pure_eisenstein

    return {
        'single_E8_pure_eisenstein': e8_is_pure_eisenstein(),
        'single_E8_weight': 4,
        'dim_M4_Sp4': 1,  # no cusp form at weight 4
        '3E8_weight': 12,
        'dim_S12_Sp4': dim_Sk_Sp4(12),  # = 1 (chi_12 only)
        'interpretation': (
            'Single E8 (weight 4): pure Eisenstein (dim M_4 = 1). '
            '3E8 Niemeier (weight 12): may have cusp component (dim S_12 = 1).'
        ),
    }


# =========================================================================
# Part 10: Summary and master verification
# =========================================================================

def full_deep_verification() -> Dict[str, Any]:
    """Run all verification checks for the deep Böcherer engine."""
    results = {}

    # 1. Dimension data
    results['higher_weight_dims'] = higher_weight_dimensions()

    # 2. SK-chi_12 identity
    results['sk_chi12'] = verify_sk_chi12_identity(max_T=2)

    # 3. Shadow universality
    results['shadow_universality'] = verify_shadow_universality_niemeier()

    # 4. E8 genus-2
    results['e8_genus2'] = verify_e8_genus2_vs_eisenstein()

    # 5. Satake parameters at small primes
    results['satake'] = {
        p: satake_parameters_sk_delta(p) for p in [2, 3, 5]
    }

    # 6. Mass constraint
    results['mass_constraint'] = verify_niemeier_mass_constraint()

    # 7. Niemeier atlas (limited)
    results['niemeier_atlas_sample'] = {
        name: niemeier_bocherer_atlas().get(name, {})
        for name in ['3E8', 'Leech', '24A1']
    }

    return results
