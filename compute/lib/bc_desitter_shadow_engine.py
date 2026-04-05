r"""De Sitter entropy and cosmological observables from the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The shadow CohFT (thm:shadow-cohft) assigns to every modular Koszul algebra A
a genus-g free energy F_g(A) = kappa(A) * lambda_g^FP (scalar lane; class G/L
algebras terminate; class M has planted-forest corrections at g >= 2).

In de Sitter space, the Gibbons-Hawking entropy replaces the BTZ entropy as
the zeroth-order object.  The cosmological horizon of dS_3 at radius ell has

    S_GH = pi * ell^2 / (4 G_N)

Via Brown-Henneaux c = 3*ell/(2*G_N) (with ell the dS radius playing the
role of the AdS radius in the analytic continuation), one obtains

    S_GH = pi * c / 3

This is the de Sitter analogue of the Cardy formula.  The shadow obstruction
tower provides quantum corrections:

    S_dS = S_GH + sum_{r>=2} c_r(A) * S_r(A) * ell^{2-r}

where S_r are the shadow coefficients of the underlying chiral algebra.


QUASINORMAL MODES
=================

De Sitter quasinormal modes are purely imaginary (no real part, unlike AdS):

    omega_n^dS = i * (n + h) / ell

where h is the conformal weight.  Shadow corrections modify the spacing:

    delta_omega_n^dS = sum_r delta_r(S_r, kappa) / ell^r


NARIAI LIMIT
============

The Schwarzschild-de Sitter solution has two horizons: the black hole horizon
r_+ and the cosmological horizon r_c.  When r_+ -> r_c (the Nariai limit),
the two horizons coincide and S_BH -> S_dS.  The shadow tower controls the
approach to this critical point through the planted-forest corrections.


INFLATIONARY OBSERVABLES
========================

In slow-roll inflation, the Hubble parameter H = 1/ell.  The slow-roll
parameters epsilon = -H_dot/H^2 and eta = epsilon_dot/(H*epsilon) encode
deviations from exact de Sitter.  The shadow tower provides a natural
expansion: epsilon and eta can be expressed as functions of the shadow
invariants kappa, S_3, S_4 at leading order.

Cosmological correlators (power spectrum, bispectrum) receive shadow
corrections.  The two-point function

    <zeta(k) zeta(-k)> = H^2 / (2 * epsilon * k^3)

acquires corrections proportional to S_r at each arity r.  The bispectrum
determines f_NL, which is controlled by S_3/kappa^2 (the cubic shadow
normalized by the quadratic).  Class G algebras (S_3 = 0) give f_NL = 0
(exact Gaussianity); class M algebras (S_3 != 0) are non-Gaussian.


STATIC PATCH THERMALITY
========================

The Gibbons-Hawking temperature T_GH = H/(2*pi) receives shadow corrections:

    T_dS = T_GH * (1 + sum_r s_r * S_r)

The thermal spectrum in the static patch is controlled by the shadow partition
function evaluated at beta_GH = 2*pi*ell.


DE SITTER COMPLEMENTARITY
==========================

Opposite static-patch observers in de Sitter describe complementary Hilbert
spaces.  The Koszul complementarity kappa(A) + kappa(A!) encodes the overlap.
For KM/free fields: kappa + kappa' = 0, so the two patches are completely
independent.  For Virasoro: kappa + kappa' = 13, giving a 13-dimensional
overlap at the scalar level.

TRANS-PLANCKIAN CENSORSHIP
===========================

The shadow growth rate rho(A) provides a natural UV cutoff.  The Bedroya-Vafa
TCC bound N_e < 1/H (in Planck units) translates to rho < 1 for shadow
consistency.  The critical cubic 5c^3 + 22c^2 - 180c - 872 = 0 (locus
rho = 1) is the shadow boundary of TCC-violating cosmologies.


References:
  Gibbons-Hawking 1977: "Cosmological event horizons, thermodynamics..."
  Brown-Henneaux 1986: "Central charges in the canonical realization..."
  Bedroya-Vafa 2019: 1909.11063 (Trans-Planckian censorship)
  Anninos-Hartman-Strominger 2012: 1108.5735 (dS/CFT)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:theorem-d (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PI = math.pi
TWO_PI = 2.0 * PI


# =========================================================================
# Section 1: Faber-Pandharipande intersection numbers (exact)
# =========================================================================

@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Positive for all g >= 1 (AP22: Bernoulli signs).

    Verified:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
        g=5: 73/3503554560
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B_2g = _bernoulli_2g(g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B_2g)
    den = power * _factorial_fraction(2 * g)
    return num / den


@lru_cache(maxsize=64)
def _bernoulli_2g(g: int) -> Fraction:
    """Exact Bernoulli number B_{2g} as a Fraction."""
    _BERNOULLI = {
        1: Fraction(1, 6),
        2: Fraction(-1, 30),
        3: Fraction(1, 42),
        4: Fraction(-1, 30),
        5: Fraction(5, 66),
        6: Fraction(-691, 2730),
        7: Fraction(7, 6),
        8: Fraction(-3617, 510),
        9: Fraction(43867, 798),
        10: Fraction(-174611, 330),
    }
    if g in _BERNOULLI:
        return _BERNOULLI[g]
    try:
        from sympy import bernoulli as sympy_bernoulli, Rational
        return Fraction(Rational(sympy_bernoulli(2 * g)))
    except ImportError:
        raise ValueError(f"Bernoulli B_{2*g} not hardcoded and sympy unavailable")


def _factorial_fraction(n: int) -> Fraction:
    """n! as a Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


# =========================================================================
# Section 2: Shadow data for standard families
# =========================================================================

def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.

    AP1/AP9: authoritative formula from landscape_census.tex.
    AP20: this is kappa(A) for A = Vir_c, NOT kappa_eff.
    """
    return Fraction(c) / Fraction(2)


def kappa_heisenberg(k) -> Fraction:
    """kappa(H_k) = k."""
    return Fraction(k)


def kappa_kac_moody(dim_g, k, h_dual) -> Fraction:
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v).

    AP1: recompute from first principles, never copy between families.
    """
    return Fraction(dim_g) * (Fraction(k) + Fraction(h_dual)) / (2 * Fraction(h_dual))


def kappa_w3(c) -> Fraction:
    """kappa(W_3) = 5c/6.

    AP1: from landscape_census.tex.  W_3 has generators of weights 2,3.
    kappa = c * (H_3 - 1) where H_3 = 1 + 1/2 + 1/3 = 11/6.
    So kappa = c * 5/6 = 5c/6.
    """
    return Fraction(5) * Fraction(c) / Fraction(6)


def kappa_betagamma(lam) -> Fraction:
    """kappa(beta-gamma) at conformal weight lambda.

    c = 12*lambda^2 - 12*lambda + 2,  kappa = c/2.
    """
    lam = Fraction(lam)
    c = 12 * lam**2 - 12 * lam + 2
    return c / 2


def virasoro_S3() -> Fraction:
    """Cubic shadow for Virasoro: S_3 = 2 (c-independent)."""
    return Fraction(2)


def virasoro_S4(c) -> Fraction:
    """Quartic contact invariant: Q^contact = 10 / [c(5c+22)]."""
    c = Fraction(c)
    return Fraction(10) / (c * (5 * c + 22))


def virasoro_S5(c) -> Fraction:
    """Quintic shadow: S_5 = -48 / [c^2(5c+22)]."""
    c = Fraction(c)
    return Fraction(-48) / (c**2 * (5 * c + 22))


def heisenberg_S3() -> Fraction:
    """Cubic shadow for Heisenberg: S_3 = 0 (class G)."""
    return Fraction(0)


def heisenberg_S4() -> Fraction:
    """Quartic shadow for Heisenberg: S_4 = 0 (class G, tower terminates)."""
    return Fraction(0)


def heisenberg_S5() -> Fraction:
    """Quintic shadow for Heisenberg: S_5 = 0."""
    return Fraction(0)


def affine_sl2_S3(k_val=1) -> Fraction:
    """Cubic shadow for affine sl_2: S_3 = 4/(k+2).

    Class L: tower terminates at arity 3 (S_4 = 0).
    """
    return Fraction(4) / (Fraction(k_val) + 2)


def affine_sl2_S4() -> Fraction:
    """Quartic shadow for affine sl_2: S_4 = 0 (class L)."""
    return Fraction(0)


def affine_sl2_S5() -> Fraction:
    """Quintic shadow for affine sl_2: S_5 = 0."""
    return Fraction(0)


def betagamma_S3() -> Fraction:
    """Cubic shadow for beta-gamma: S_3 = 2."""
    return Fraction(2)


def betagamma_S4(lam) -> Fraction:
    """Quartic shadow for beta-gamma at weight lambda.

    Class C: nonzero S_4 (terminates at arity 4).
    For lambda = 1: c = 2, kappa = 1, Q^contact from beta-gamma OPE.
    """
    lam = Fraction(lam)
    c = 12 * lam**2 - 12 * lam + 2
    if c == 0:
        return Fraction(0)
    return Fraction(10) / (c * (5 * c + 22))


# =========================================================================
# Section 3: Shadow family data bundles
# =========================================================================

class ShadowFamily:
    """Collects shadow data for a chiral algebra family."""

    def __init__(self, name: str, kappa: Fraction,
                 S3: Fraction, S4: Fraction, S5: Fraction,
                 depth_class: str, c: Fraction):
        self.name = name
        self.kappa = kappa
        self.S3 = S3
        self.S4 = S4
        self.S5 = S5
        self.depth_class = depth_class
        self.c = c

    def __repr__(self):
        return (f"ShadowFamily({self.name}, kappa={self.kappa}, "
                f"S3={self.S3}, S4={self.S4}, S5={self.S5}, "
                f"class={self.depth_class})")


def virasoro_family(c) -> ShadowFamily:
    """Shadow data for Virasoro at central charge c."""
    c_f = Fraction(c)
    return ShadowFamily(
        name=f"Vir_{c}",
        kappa=kappa_virasoro(c_f),
        S3=virasoro_S3(),
        S4=virasoro_S4(c_f) if c_f != 0 else Fraction(0),
        S5=virasoro_S5(c_f) if c_f != 0 else Fraction(0),
        depth_class='M',
        c=c_f,
    )


def heisenberg_family(k) -> ShadowFamily:
    """Shadow data for Heisenberg at level k."""
    k_f = Fraction(k)
    return ShadowFamily(
        name=f"H_{k}",
        kappa=kappa_heisenberg(k_f),
        S3=heisenberg_S3(),
        S4=heisenberg_S4(),
        S5=heisenberg_S5(),
        depth_class='G',
        c=k_f,  # c = 1 for rank-1 Heisenberg, but kappa = k
    )


def affine_sl2_family(k) -> ShadowFamily:
    """Shadow data for affine sl_2 at level k."""
    k_f = Fraction(k)
    kappa = kappa_kac_moody(3, k_f, 2)  # dim(sl_2) = 3, h^v = 2
    c_val = Fraction(3 * k_f, k_f + 2)
    return ShadowFamily(
        name=f"sl2_{k}",
        kappa=kappa,
        S3=affine_sl2_S3(),
        S4=affine_sl2_S4(),
        S5=affine_sl2_S5(),
        depth_class='L',
        c=c_val,
    )


def betagamma_family(lam) -> ShadowFamily:
    """Shadow data for beta-gamma at weight lambda."""
    lam_f = Fraction(lam)
    c_val = 12 * lam_f**2 - 12 * lam_f + 2
    return ShadowFamily(
        name=f"bg_{lam}",
        kappa=kappa_betagamma(lam_f),
        S3=betagamma_S3(),
        S4=betagamma_S4(lam_f),
        S5=Fraction(0),  # class C terminates at arity 4
        depth_class='C',
        c=c_val,
    )


def w3_family(c) -> ShadowFamily:
    """Shadow data for W_3 at central charge c."""
    c_f = Fraction(c)
    return ShadowFamily(
        name=f"W3_{c}",
        kappa=kappa_w3(c_f),
        S3=Fraction(2),  # cubic shadow for W_3
        S4=virasoro_S4(c_f) if c_f != 0 else Fraction(0),
        S5=virasoro_S5(c_f) if c_f != 0 else Fraction(0),
        depth_class='M',
        c=c_f,
    )


def standard_families() -> List[ShadowFamily]:
    """All standard families at representative parameters."""
    families = []
    # Heisenberg at k=1
    families.append(heisenberg_family(1))
    # Affine sl_2 at k=1
    families.append(affine_sl2_family(1))
    # Beta-gamma at lambda=1
    families.append(betagamma_family(1))
    # Virasoro at c=26 (bosonic string)
    families.append(virasoro_family(26))
    # Virasoro at c=1
    families.append(virasoro_family(1))
    # Virasoro at c=13 (self-dual)
    families.append(virasoro_family(13))
    return families


# =========================================================================
# Section 4: Free energies F_g (scalar + planted-forest)
# =========================================================================

def F_g_scalar(kappa: Fraction, g: int) -> Fraction:
    """Scalar free energy: F_g^{sc} = kappa * lambda_g^FP."""
    return kappa * lambda_fp(g)


def planted_forest_g2(kappa: Fraction, S3: Fraction) -> Fraction:
    r"""Planted-forest correction at genus 2.

    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48
    """
    return S3 * (10 * S3 - kappa) / Fraction(48)


def planted_forest_g3(kappa: Fraction, S3: Fraction,
                      S4: Fraction, S5: Fraction) -> Fraction:
    r"""Planted-forest correction at genus 3 (11-term polynomial)."""
    numerator = (
        - kappa**2 * S3
        + 60 * kappa * S3**2
        - 500 * S3**3
        + 6 * kappa**2 * S4
        - 120 * kappa * S3 * S4
        + 600 * S3**2 * S4
        + 72 * kappa * S4**2
        - 720 * S3 * S4**2
        + 120 * kappa * S3 * S5
        - 1200 * S3**2 * S5
        + 1440 * S4 * S5
    )
    return numerator / Fraction(11520)


def family_free_energy(fam: ShadowFamily, g: int) -> Fraction:
    """Full F_g for a shadow family."""
    scalar = F_g_scalar(fam.kappa, g)
    if g == 1:
        return scalar
    elif g == 2:
        return scalar + planted_forest_g2(fam.kappa, fam.S3)
    elif g == 3:
        return scalar + planted_forest_g3(fam.kappa, fam.S3, fam.S4, fam.S5)
    else:
        return scalar


# =========================================================================
# Section 5: Gibbons-Hawking entropy from shadow
# =========================================================================

def gibbons_hawking_entropy(c) -> float:
    """Classical Gibbons-Hawking entropy: S_GH = pi * c / 3.

    Via Brown-Henneaux c = 3*ell/(2*G_N):
        S_GH = pi * ell^2 / (4*G_N)
             = pi * ell * (3*ell / (2*G_N)) / 6
             = pi * c / 3

    This is the dS_3 analogue of the Cardy formula.

    Verification path 1: S_GH = Area / (4*G_N) = 2*pi*ell / (4*G_N) = pi*ell/(2*G_N).
      With c = 3*ell/(2*G_N), ell = 2*c*G_N/3, so S_GH = pi*c/3.
    Verification path 2: Euclidean dS_3 is S^3 with action I_E = -pi*ell/(2*G_N) = -pi*c/3.
      S = -I_E = pi*c/3 (Gibbons-Hawking 1977).
    Verification path 3: Analytic continuation from BTZ S_BH = 2*pi*sqrt(c*M/6)
      at M = c/6 (vacuum energy), gives S = 2*pi*c/6 = pi*c/3.
    """
    return PI * float(c) / 3.0


def gibbons_hawking_entropy_from_kappa(kappa) -> float:
    """S_GH = 2*pi*kappa/3.

    Since kappa = c/2 for Virasoro, S_GH = 2*pi*(c/2)/3 = pi*c/3.
    This formulation makes the shadow tower structure manifest:
    the leading term is 2*pi*kappa/3.
    """
    return 2.0 * PI * float(kappa) / 3.0


def shadow_entropy_correction_arity_r(fam: ShadowFamily, r: int,
                                       ell: float = 1.0) -> float:
    """Shadow correction to S_dS at arity r.

    The shadow obstruction tower gives additive corrections:
        delta_S_r = c_r * S_r * ell^{2-r}

    The coupling constant c_r is determined by matching to the genus expansion.
    At arity 2: c_2 = 2*pi/3 (reproduces S_GH from kappa).
    At arity r >= 3: c_r = pi * ell^{2-r} * S_r / (3 * kappa).

    The normalization is fixed by demanding that at r=2 the result is
    S_GH = (2*pi/3)*kappa, so c_2*S_2 = (2*pi/3)*kappa.
    Since S_2 = kappa (the shadow at arity 2 IS kappa), c_2 = 2*pi/3.

    For r >= 3, the contribution to the entropy comes from the
    genus expansion. The leading-order contribution of S_r appears
    at genus floor(r/2) + 1 (shadow visibility genus), weighted by
    the appropriate power of the expansion parameter.
    """
    S_r_vals = {2: fam.kappa, 3: fam.S3, 4: fam.S4, 5: fam.S5}

    if r not in S_r_vals:
        return 0.0

    S_r = float(S_r_vals[r])
    if r == 2:
        # Leading Gibbons-Hawking: c_2 = 2*pi/3
        return (2.0 * PI / 3.0) * S_r
    else:
        # Higher-arity corrections: c_r = pi/(3*kappa) * ell^{2-r}
        kappa_f = float(fam.kappa)
        if abs(kappa_f) < 1e-30:
            return 0.0
        return (PI / 3.0) * S_r * ell ** (2 - r) / kappa_f


def shadow_corrected_entropy(fam: ShadowFamily, ell: float = 1.0,
                              max_r: int = 5) -> Dict[str, Any]:
    """Full shadow-corrected de Sitter entropy.

    S_dS = S_GH + sum_{r=3}^{max_r} delta_S_r

    Returns dict with individual contributions and total.
    """
    S_GH = gibbons_hawking_entropy_from_kappa(fam.kappa)

    result = {
        'family': fam.name,
        'kappa': float(fam.kappa),
        'c': float(fam.c),
        'S_GH': S_GH,
        'ell': ell,
        'corrections': {},
    }

    total = S_GH
    for r in range(3, max_r + 1):
        delta_r = shadow_entropy_correction_arity_r(fam, r, ell)
        result['corrections'][r] = delta_r
        total += delta_r

    result['S_total'] = total
    result['relative_correction'] = (total - S_GH) / S_GH if abs(S_GH) > 1e-30 else 0.0

    return result


# =========================================================================
# Section 6: dS_3 quasinormal modes
# =========================================================================

def ds_quasinormal_mode(n: int, h: float, ell: float = 1.0) -> complex:
    """De Sitter quasinormal mode: omega_n = i*(n+h)/ell.

    Unlike AdS (BTZ) where omega has both real and imaginary parts,
    dS quasinormal modes are purely imaginary (no oscillatory part,
    only decay).  This is because the dS static patch is thermally
    populated at T_GH = 1/(2*pi*ell).

    Parameters
    ----------
    n : mode number (n >= 0)
    h : conformal weight of the field
    ell : dS radius
    """
    return 1j * (n + h) / ell


def ds_qnm_shadow_correction(n: int, h: float, fam: ShadowFamily,
                               ell: float = 1.0) -> complex:
    """Shadow correction to dS quasinormal mode at arity r.

    The shadow tower modifies the mode spacing through the
    genus expansion.  The leading correction comes from S_3
    (the cubic shadow), which shifts the imaginary part:

        delta_omega_n = i * sum_r delta_r(n, h, S_r) / ell^r

    At arity 2: already included in the tree-level mode.
    At arity 3: delta_3 = -S_3 * (n+h) / (2*kappa*ell^2)
    At arity 4: delta_4 = S_4 * (n+h)^2 / (2*kappa^2*ell^3)
    At arity 5: delta_5 = -S_5 * (n+h)^3 / (2*kappa^3*ell^4)

    The alternating sign comes from the Taylor expansion of the
    shadow generating function H(t) = t^2 * sqrt(Q_L(t)).
    """
    kappa_f = float(fam.kappa)
    if abs(kappa_f) < 1e-30:
        return 0j

    nh = n + h
    corrections = 0j

    # Arity 3: cubic shadow
    S3_f = float(fam.S3)
    if abs(S3_f) > 1e-30:
        corrections += -S3_f * nh / (2.0 * kappa_f * ell**2)

    # Arity 4: quartic shadow
    S4_f = float(fam.S4)
    if abs(S4_f) > 1e-30:
        corrections += S4_f * nh**2 / (2.0 * kappa_f**2 * ell**3)

    # Arity 5: quintic shadow
    S5_f = float(fam.S5)
    if abs(S5_f) > 1e-30:
        corrections += -S5_f * nh**3 / (2.0 * kappa_f**3 * ell**4)

    return 1j * corrections / ell


def ds_qnm_full(n: int, h: float, fam: ShadowFamily,
                  ell: float = 1.0) -> complex:
    """Full shadow-corrected dS quasinormal mode.

    omega_n = omega_n^tree + delta_omega_n^shadow
    """
    return ds_quasinormal_mode(n, h, ell) + ds_qnm_shadow_correction(n, h, fam, ell)


def ds_qnm_table(n_max: int, h: float, fam: ShadowFamily,
                   ell: float = 1.0) -> List[Dict[str, Any]]:
    """Table of dS quasinormal modes for n = 0..n_max."""
    rows = []
    for n in range(n_max + 1):
        tree = ds_quasinormal_mode(n, h, ell)
        correction = ds_qnm_shadow_correction(n, h, fam, ell)
        full = tree + correction
        rows.append({
            'n': n,
            'omega_tree': tree,
            'delta_omega': correction,
            'omega_full': full,
            'relative_correction': abs(correction) / abs(tree) if abs(tree) > 1e-30 else 0.0,
        })
    return rows


# =========================================================================
# Section 7: Nariai limit
# =========================================================================

def schwarzschild_ds_horizons(M: float, ell: float) -> Tuple[float, float]:
    """Horizon radii of the Schwarzschild-dS_3 solution.

    In 2+1d the metric is ds^2 = -f(r)dt^2 + dr^2/f(r) + r^2 dphi^2
    with f(r) = -8*G*M + r^2/ell^2.

    The horizons are at f(r) = 0:
        r_+^2 = 8*G*M * ell^2
        r_+ = ell * sqrt(8*G*M)

    For the cosmological horizon in SdS:
        r_c = ell  (the cosmological horizon is at r = ell in pure dS)

    In the SdS case with both horizons:
        f(r) = r^2/ell^2 - 8*G*M = 0 gives r = ell*sqrt(8*G*M).

    The Nariai limit is r_+ -> r_c, i.e., 8*G*M -> 1.
    We parametrize by x = 8*G*M (0 < x < 1 for sub-Nariai).
    """
    x = 8.0 * M  # G = 1 units
    if x <= 0:
        return (0.0, ell)
    if x >= 1.0:
        # At or beyond Nariai
        return (ell, ell)
    r_plus = ell * math.sqrt(x)
    r_cosmo = ell
    return (r_plus, r_cosmo)


def nariai_entropy(c) -> float:
    """Nariai entropy: S_Nariai = S_dS = pi*c/3.

    In the Nariai limit r_+ -> r_c = ell, the BH entropy and the
    cosmological entropy coincide:
        S_BH = 2*pi*r_+ / (4*G) -> 2*pi*ell / (4*G) = pi*c/3 = S_GH.
    """
    return gibbons_hawking_entropy(c)


def nariai_shadow_corrected(fam: ShadowFamily, ell: float = 1.0,
                             max_r: int = 5) -> Dict[str, Any]:
    """Shadow-corrected Nariai entropy.

    At the Nariai limit, the BH shadow corrections and the dS shadow
    corrections coincide, giving

        S_Nariai = S_GH + sum corrections

    The approach to Nariai is controlled by the shadow discriminant:
        Delta(A) = 8*kappa*S_4.
    For class G (Delta=0): instant coalescence (no subleading barrier).
    For class M (Delta!=0): logarithmic approach controlled by shadow depth.
    """
    kappa_f = float(fam.kappa)
    delta_A = 8.0 * kappa_f * float(fam.S4) if fam.S4 != 0 else 0.0

    base = shadow_corrected_entropy(fam, ell, max_r)
    base['nariai'] = True
    base['discriminant'] = delta_A
    base['coalescence_class'] = 'instant' if abs(delta_A) < 1e-30 else 'logarithmic'

    return base


def nariai_approach(fam: ShadowFamily, x_values: Optional[List[float]] = None,
                     ell: float = 1.0) -> List[Dict[str, float]]:
    """Track entropy as r_+ approaches ell (the Nariai limit).

    x = (r_+/ell)^2.  At x = 0: pure dS.  At x = 1: Nariai.

    S_BH(x) = pi*c*sqrt(x)/3 (BH entropy, grows with x)
    S_cosmo(x) = pi*c/3 (cosmological entropy, constant)
    S_shadow(x) = shadow corrections that interpolate.
    """
    if x_values is None:
        x_values = [0.01, 0.1, 0.2, 0.5, 0.8, 0.9, 0.95, 0.99, 1.0]

    c_f = float(fam.c)
    kappa_f = float(fam.kappa)

    rows = []
    for x in x_values:
        x = min(max(x, 0.0), 1.0)
        S_BH = PI * c_f * math.sqrt(x) / 3.0 if x > 0 else 0.0
        S_cosmo = PI * c_f / 3.0
        # Shadow correction scales with the gap
        gap = S_cosmo - S_BH
        S3_correction = float(fam.S3) * gap / (3.0 * kappa_f) if abs(kappa_f) > 1e-30 else 0.0

        rows.append({
            'x': x,
            'r_plus_over_ell': math.sqrt(x),
            'S_BH': S_BH,
            'S_cosmo': S_cosmo,
            'gap': gap,
            'S3_correction': S3_correction,
        })

    return rows


# =========================================================================
# Section 8: Slow-roll parameters from shadow invariants
# =========================================================================

def slow_roll_epsilon(kappa, S3, S4) -> float:
    r"""Slow-roll parameter epsilon from shadow data.

    The slow-roll parameter epsilon = -H_dot / H^2 measures the deviation
    from exact de Sitter (epsilon = 0).

    In the shadow framework, the departure from pure dS is controlled by
    the shadow tower.  The leading-order identification:

        epsilon = S_3^2 / (4 * kappa^2)

    Derivation: the shadow generating function H(t) = t^2 sqrt(Q_L(t))
    has derivative H'(t) = t(2 sqrt(Q) + t Q'/(2 sqrt(Q))).
    At t = t_0 (the physical expansion rate),
    epsilon = (H'(t_0)/H(t_0) - 2/t_0)^2 at leading order.
    The cubic shadow S_3 = alpha enters as the leading deviation.

    For class G (S_3 = 0): epsilon = 0 (exact de Sitter).
    For class L (S_3 != 0, S_4 = 0): epsilon = S_3^2 / (4*kappa^2).
    For class M (S_3, S_4 both nonzero): quartic correction.
    """
    kappa_f = float(kappa)
    S3_f = float(S3)
    S4_f = float(S4)

    if abs(kappa_f) < 1e-30:
        return 0.0

    epsilon_0 = S3_f**2 / (4.0 * kappa_f**2)

    # Quartic correction from S_4
    epsilon_1 = -S3_f * S4_f / (2.0 * kappa_f**3) if abs(kappa_f) > 1e-30 else 0.0

    return epsilon_0 + epsilon_1


def slow_roll_eta(kappa, S3, S4) -> float:
    r"""Slow-roll parameter eta from shadow data.

    eta = epsilon_dot / (H * epsilon) = d(ln epsilon) / d(ln a)

    In the shadow tower framework:
        eta = S_3^2 / (2 * kappa^2) - 2 * S_4 / kappa

    The first term is 2*epsilon_0, the second is the direct quartic contribution.

    For class G: eta = 0.
    For class L: eta = 2*epsilon_0 = S_3^2 / (2*kappa^2).
    For class M: eta = S_3^2 / (2*kappa^2) - 2*S_4/kappa.
    """
    kappa_f = float(kappa)
    S3_f = float(S3)
    S4_f = float(S4)

    if abs(kappa_f) < 1e-30:
        return 0.0

    return S3_f**2 / (2.0 * kappa_f**2) - 2.0 * S4_f / kappa_f


def slow_roll_from_family(fam: ShadowFamily) -> Dict[str, float]:
    """Compute slow-roll parameters for a shadow family."""
    eps = slow_roll_epsilon(fam.kappa, fam.S3, fam.S4)
    eta = slow_roll_eta(fam.kappa, fam.S3, fam.S4)

    # Spectral tilt: n_s - 1 = -2*epsilon - eta
    n_s = 1.0 - 2.0 * eps - eta

    # Tensor-to-scalar ratio: r_tensor = 16*epsilon
    r_tensor = 16.0 * eps

    return {
        'family': fam.name,
        'kappa': float(fam.kappa),
        'S3': float(fam.S3),
        'S4': float(fam.S4),
        'epsilon': eps,
        'eta': eta,
        'n_s': n_s,
        'r_tensor': r_tensor,
        'depth_class': fam.depth_class,
    }


# =========================================================================
# Section 9: Cosmological correlators
# =========================================================================

def power_spectrum_correction(fam: ShadowFamily, k_over_H: float) -> Dict[str, float]:
    r"""Shadow correction to the scalar power spectrum.

    The two-point function: <zeta(k) zeta(-k)> = H^2 / (2*epsilon*k^3).
    Shadow corrections:

        delta<zeta zeta> / <zeta zeta> = sum_r f_r(S_r) * (k/H)^{r-2}

    where:
        f_2 = 0 (absorbed into epsilon)
        f_3 = S_3 / kappa  (from cubic shadow)
        f_4 = S_4 / kappa^2 - S_3^2 / (2*kappa^3)  (quartic minus cross-term)
    """
    kappa_f = float(fam.kappa)
    S3_f = float(fam.S3)
    S4_f = float(fam.S4)

    if abs(kappa_f) < 1e-30:
        return {'f_2': 0.0, 'f_3': 0.0, 'f_4': 0.0, 'total': 0.0}

    f_2 = 0.0  # absorbed into epsilon
    f_3 = S3_f / kappa_f
    f_4 = S4_f / kappa_f**2 - S3_f**2 / (2.0 * kappa_f**3)

    total = (f_2 * k_over_H**0
             + f_3 * k_over_H**1
             + f_4 * k_over_H**2)

    return {
        'f_2': f_2,
        'f_3': f_3,
        'f_4': f_4,
        'k_over_H': k_over_H,
        'total': total,
    }


def non_gaussianity_fNL(fam: ShadowFamily) -> float:
    r"""f_NL from the shadow tower.

    The three-point function (bispectrum) gives the non-Gaussianity parameter
    f_NL.  In the shadow language:

        f_NL = (5/6) * S_3 / kappa

    This is the equilateral f_NL determined by the cubic shadow.

    Class G (S_3 = 0): f_NL = 0 (Gaussian).
    Class L (S_3 = 2, large kappa): f_NL ~ 1/kappa (small).
    Class M (S_3 = 2, kappa = c/2): f_NL = 5/(3c) for Virasoro.

    The 5/6 prefactor comes from the standard convention for f_NL
    relating the bispectrum to the square of the power spectrum:
        B(k1,k2,k3) = (6/5) * f_NL * [P(k1)*P(k2) + cyclic].
    """
    kappa_f = float(fam.kappa)
    S3_f = float(fam.S3)

    if abs(kappa_f) < 1e-30:
        return 0.0

    return (5.0 / 6.0) * S3_f / kappa_f


def non_gaussianity_gNL(fam: ShadowFamily) -> float:
    r"""g_NL from the shadow tower (quartic non-Gaussianity).

    The trispectrum (four-point connected function) gives g_NL.
    In shadow language:

        g_NL = (25/54) * S_4 / kappa^2

    from the quartic shadow.

    Class G,L (S_4 = 0): g_NL = 0.
    Class C (S_4 != 0): first nonzero g_NL.
    Class M (S_4 = Q^contact): g_NL = (25/54) * Q^contact / kappa^2.
    """
    kappa_f = float(fam.kappa)
    S4_f = float(fam.S4)

    if abs(kappa_f) < 1e-30:
        return 0.0

    return (25.0 / 54.0) * S4_f / kappa_f**2


# =========================================================================
# Section 10: Spectral tilt
# =========================================================================

def spectral_tilt(fam: ShadowFamily) -> float:
    """Spectral tilt: n_s - 1 = -2*epsilon - eta.

    Verification path 1: direct from slow-roll.
    Verification path 2: n_s = 1 - S_3^2/kappa^2 - S_3^2/(2*kappa^2) + 2*S_4/kappa
                        = 1 - 3*S_3^2/(2*kappa^2) + 2*S_4/kappa.

    For class G: n_s = 1 (exact scale invariance).
    For class M (Virasoro): n_s = 1 - 6/c^2 + 40/(c(5c+22)).
    """
    sr = slow_roll_from_family(fam)
    return sr['n_s']


def spectral_tilt_virasoro(c) -> float:
    """n_s for Virasoro at central charge c.

    n_s = 1 - 3*S_3^2/(2*kappa^2) + 2*S_4/kappa
        = 1 - 3*4/(2*(c/2)^2) + 2*10/(c*(5c+22)*(c/2))
        = 1 - 6/c^2 + 40/(c^2*(5c+22))
        = 1 - (30c + 132 - 40) / (c^2*(5c+22))
        = 1 - (30c + 92) / (c^2*(5c+22))

    Numerical examples:
        c = 1: n_s = 1 - 122/27 ~ -3.52 (far from scale-invariant)
        c = 13: n_s = 1 - (390 + 92)/(169*87) = 1 - 482/14703 ~ 0.967
        c = 26: n_s = 1 - (780 + 92)/(676*152) = 1 - 872/102752 ~ 0.992
    """
    c_f = float(c)
    if abs(c_f) < 1e-30:
        return float('nan')
    return 1.0 - (30.0 * c_f + 92.0) / (c_f**2 * (5.0 * c_f + 22.0))


def planck_consistency_test(fam: ShadowFamily) -> Dict[str, Any]:
    """Test whether a shadow family is consistent with Planck 2018 constraints.

    Planck 2018 (TT,TE,EE+lowE+lensing):
        n_s = 0.9649 +/- 0.0042 (68% CL)
        r < 0.10 (95% CL)
        f_NL^equil = -26 +/- 47 (68% CL)

    Returns dict with observables and pass/fail flags.
    """
    sr = slow_roll_from_family(fam)
    fNL = non_gaussianity_fNL(fam)

    n_s_obs = 0.9649
    n_s_err = 0.0042
    r_bound = 0.10
    fNL_obs = -26.0
    fNL_err = 47.0

    n_s_pass = abs(sr['n_s'] - n_s_obs) < 3.0 * n_s_err
    r_pass = sr['r_tensor'] < r_bound
    fNL_pass = abs(fNL - fNL_obs) < 3.0 * fNL_err

    return {
        'family': fam.name,
        'n_s': sr['n_s'],
        'n_s_planck': n_s_obs,
        'n_s_pass': n_s_pass,
        'r_tensor': sr['r_tensor'],
        'r_bound': r_bound,
        'r_pass': r_pass,
        'f_NL': fNL,
        'f_NL_planck': fNL_obs,
        'f_NL_pass': fNL_pass,
        'overall_pass': n_s_pass and r_pass and fNL_pass,
    }


# =========================================================================
# Section 11: Trans-Planckian censorship
# =========================================================================

def shadow_growth_rate(fam: ShadowFamily) -> float:
    """Shadow growth rate rho(A).

    rho^2 = (9*S_3^2 + 2*Delta) / (4*kappa^2)

    where Delta = 8*kappa*S_4 (the shadow discriminant).

    For class G (S_3 = 0, S_4 = 0): rho = 0.
    For class L (S_3 != 0, S_4 = 0): rho = 3*|S_3|/(2*kappa).
    For class M (Virasoro): rho = sqrt((180c+872)/(c^2(5c+22))).
    """
    kappa_f = float(fam.kappa)
    S3_f = float(fam.S3)
    S4_f = float(fam.S4)

    if abs(kappa_f) < 1e-30:
        return 0.0

    Delta = 8.0 * kappa_f * S4_f
    rho_sq = (9.0 * S3_f**2 + 2.0 * Delta) / (4.0 * kappa_f**2)

    if rho_sq < 0:
        return 0.0
    return math.sqrt(rho_sq)


def trans_planckian_threshold(fam: ShadowFamily) -> float:
    """Trans-Planckian censorship threshold from shadow convergence radius.

    The TCC bound (Bedroya-Vafa 2019) requires that modes stretched
    beyond the Planck scale never re-enter the horizon.  In Planck units:
        N_e < 1/H  (maximum number of e-folds)

    The shadow convergence radius R_conv = 1/rho(A) provides a natural
    UV cutoff.  The TCC threshold becomes:

        N_e^max = R_conv / ell = 1 / (rho * ell)

    The condition rho < 1 (shadow tower convergent at t = ell) is
    the shadow analogue of the TCC bound.  The critical cubic
    5c^3 + 22c^2 - 180c - 872 = 0 at c ~ 6.125 marks the boundary.

    Returns the maximum number of e-folds for ell = 1.
    """
    rho = shadow_growth_rate(fam)
    if rho < 1e-30:
        return float('inf')  # exact dS: no TCC constraint
    return 1.0 / rho


def tcc_consistency(fam: ShadowFamily) -> Dict[str, Any]:
    """Test shadow family against the trans-Planckian censorship conjecture.

    TCC requires rho < 1 for shadow-consistent cosmologies.
    """
    rho = shadow_growth_rate(fam)
    N_max = trans_planckian_threshold(fam)

    return {
        'family': fam.name,
        'rho': rho,
        'convergent': rho < 1.0,
        'N_e_max': N_max,
        'tcc_safe': rho < 1.0,
        'depth_class': fam.depth_class,
    }


# =========================================================================
# Section 12: Static patch thermality
# =========================================================================

def gibbons_hawking_temperature(ell: float) -> float:
    """Gibbons-Hawking temperature: T_GH = 1/(2*pi*ell).

    The static-patch observer in dS sees thermal radiation at this temperature.
    Analogue of Hawking temperature for black holes.
    """
    if ell <= 0:
        return float('inf')
    return 1.0 / (TWO_PI * ell)


def static_patch_temperature_correction(fam: ShadowFamily,
                                         ell: float = 1.0) -> Dict[str, float]:
    """Shadow correction to the Gibbons-Hawking temperature.

    T_dS = T_GH * (1 + sum_r s_r * S_r)

    The thermal corrections come from the genus expansion of the
    partition function on the static-patch solid torus.  The
    correction coefficients s_r are:

        s_2 = 0 (absorbed into T_GH)
        s_3 = -S_3 / (6*kappa) * ell^{-1}
        s_4 = S_4 / (12*kappa^2) * ell^{-2}

    The sign of s_3 is NEGATIVE because higher shadow terms represent
    quantum corrections that REDUCE the effective temperature (the
    horizon area shrinks under quantum effects).
    """
    T_GH = gibbons_hawking_temperature(ell)
    kappa_f = float(fam.kappa)

    if abs(kappa_f) < 1e-30:
        return {
            'T_GH': T_GH,
            's_2': 0.0, 's_3': 0.0, 's_4': 0.0,
            'delta_T_over_T': 0.0,
            'T_corrected': T_GH,
        }

    S3_f = float(fam.S3)
    S4_f = float(fam.S4)

    s_2 = 0.0
    s_3 = -S3_f / (6.0 * kappa_f) / ell
    s_4 = S4_f / (12.0 * kappa_f**2) / ell**2

    delta_T_over_T = s_2 + s_3 * S3_f + s_4 * S4_f
    T_corrected = T_GH * (1.0 + delta_T_over_T)

    return {
        'T_GH': T_GH,
        's_2': s_2,
        's_3': s_3,
        's_4': s_4,
        'delta_T_over_T': delta_T_over_T,
        'T_corrected': T_corrected,
    }


# =========================================================================
# Section 13: de Sitter complementarity
# =========================================================================

def ds_complementarity_overlap(fam: ShadowFamily) -> Dict[str, Any]:
    """De Sitter complementarity from shadow Koszul duality.

    In the dS complementarity framework, opposite static-patch observers
    describe complementary Hilbert spaces.  The Koszul complementarity
    sum kappa(A) + kappa(A!) encodes the overlap dimension.

    For KM/free fields: kappa + kappa' = 0 (completely independent patches).
    For Virasoro: kappa + kappa' = 13 (13-dimensional overlap at scalar level).
    For W_3: kappa(c) + kappa(26-c) = 5*c/6 + 5*(26-c)/6 = 65/3.

    The complementarity entropy is:
        S_comp = pi * (kappa + kappa') / 3

    This is the entropy shared between the two patches.
    """
    kappa_f = float(fam.kappa)

    # Compute kappa' = kappa(A!) for each family
    if fam.depth_class == 'G':
        # Heisenberg: Koszul dual has kappa' = -kappa (AP24: kappa+kappa'=0)
        kappa_dual = -kappa_f
    elif fam.depth_class == 'L':
        # Affine KM: kappa + kappa' = 0 (Feigin-Frenkel involution)
        kappa_dual = -kappa_f
    elif fam.depth_class == 'C':
        # Beta-gamma: kappa + kappa' = 0 (free field)
        kappa_dual = -kappa_f
    elif fam.depth_class == 'M':
        # Virasoro/W_N: kappa(c) + kappa(26-c) = 13 for Virasoro
        # AP24: kappa + kappa' = rho*K for W-algebras
        if fam.name.startswith('Vir'):
            kappa_dual = float(kappa_virasoro(26 - fam.c))
        elif fam.name.startswith('W3'):
            kappa_dual = float(kappa_w3(26 - fam.c))
        else:
            kappa_dual = -kappa_f  # default for unknown class M
    else:
        kappa_dual = -kappa_f

    overlap = kappa_f + kappa_dual
    S_comp = PI * overlap / 3.0

    return {
        'family': fam.name,
        'kappa': kappa_f,
        'kappa_dual': kappa_dual,
        'overlap': overlap,
        'S_complementarity': S_comp,
        'independent_patches': abs(overlap) < 1e-10,
        'depth_class': fam.depth_class,
    }


def ds_complementarity_virasoro(c) -> Dict[str, float]:
    """De Sitter complementarity for Virasoro at central charge c.

    kappa(Vir_c) = c/2
    kappa(Vir_{26-c}) = (26-c)/2
    kappa + kappa' = 13

    AP24: this is NOT zero.  The asymmetry around 0 is because
    Koszul duality c -> 26-c is anti-symmetric around c=13, not c=0.

    At c=13 (self-dual): kappa = kappa' = 13/2, overlap = 13.
    At c=26 (bosonic string): kappa = 13, kappa' = 0, overlap = 13.
    At c=0: kappa = 0, kappa' = 13, overlap = 13.

    The overlap is CONSTANT at 13 for all c. This is the de Sitter
    complementarity invariant for the Virasoro family.
    """
    c_f = float(c)
    kappa = c_f / 2.0
    kappa_dual = (26.0 - c_f) / 2.0
    overlap = kappa + kappa_dual  # always 13

    return {
        'c': c_f,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'overlap': overlap,
        'S_complementarity': PI * overlap / 3.0,
        'self_dual': abs(c_f - 13.0) < 1e-10,
    }


# =========================================================================
# Section 14: Genus expansion for dS entropy
# =========================================================================

def ds_entropy_genus_expansion(fam: ShadowFamily, g_max: int = 5,
                                ell: float = 1.0) -> Dict[str, Any]:
    """Full genus expansion of the de Sitter entropy.

    S_dS = S_GH + sum_{g=1}^{g_max} S_g

    where S_g = F_g(A) * epsilon^{2g-2} with epsilon = 2*pi/S_GH.

    At genus 1: S_1 = F_1 * epsilon^0 = kappa/24 (constant correction).
    At genus g >= 2: S_g = F_g * (2*pi/(pi*c/3))^{2g-2} = F_g * (6/c)^{2g-2}.
    """
    S_GH = gibbons_hawking_entropy_from_kappa(fam.kappa)

    if abs(S_GH) < 1e-30:
        return {
            'family': fam.name,
            'S_GH': 0.0,
            'S_total': 0.0,
            'genus_contributions': {},
        }

    epsilon = TWO_PI / S_GH

    contributions = {}
    total = S_GH

    for g in range(1, g_max + 1):
        Fg = family_free_energy(fam, g)
        Fg_f = float(Fg)

        if g == 1:
            # One-loop: constant contribution
            Sg = Fg_f
        else:
            Sg = Fg_f * epsilon ** (2 * g - 2)

        contributions[g] = {
            'F_g': Fg_f,
            'S_g': Sg,
            'epsilon_power': 2 * g - 2,
        }
        total += Sg

    return {
        'family': fam.name,
        'kappa': float(fam.kappa),
        'c': float(fam.c),
        'S_GH': S_GH,
        'epsilon': epsilon,
        'S_total': total,
        'relative_correction': (total - S_GH) / S_GH if abs(S_GH) > 1e-30 else 0.0,
        'genus_contributions': contributions,
    }


# =========================================================================
# Section 15: Master computation table
# =========================================================================

def full_desitter_analysis(fam: ShadowFamily, ell: float = 1.0,
                            g_max: int = 5, n_max_qnm: int = 10) -> Dict[str, Any]:
    """Complete de Sitter analysis for a shadow family.

    Assembles all observables:
    - Gibbons-Hawking entropy and shadow corrections
    - Quasinormal modes
    - Nariai limit
    - Slow-roll parameters
    - Cosmological correlators
    - Non-Gaussianity
    - Spectral tilt and Planck consistency
    - Trans-Planckian censorship
    - Static patch temperature
    - Complementarity
    - Genus expansion
    """
    result = {
        'family': fam.name,
        'depth_class': fam.depth_class,
        'kappa': float(fam.kappa),
        'S3': float(fam.S3),
        'S4': float(fam.S4),
        'S5': float(fam.S5),
        'c': float(fam.c),
    }

    # 1. Entropy
    result['entropy'] = shadow_corrected_entropy(fam, ell)
    result['genus_expansion'] = ds_entropy_genus_expansion(fam, g_max, ell)

    # 2. QNMs (for h = 2, the graviton)
    result['qnm_table'] = ds_qnm_table(min(n_max_qnm, 20), 2.0, fam, ell)

    # 3. Nariai
    result['nariai'] = nariai_shadow_corrected(fam, ell)

    # 4. Slow-roll
    result['slow_roll'] = slow_roll_from_family(fam)

    # 5. Correlators
    result['power_spectrum'] = power_spectrum_correction(fam, 0.1)

    # 6. Non-Gaussianity
    result['f_NL'] = non_gaussianity_fNL(fam)
    result['g_NL'] = non_gaussianity_gNL(fam)

    # 7. Spectral tilt
    result['n_s'] = spectral_tilt(fam)

    # 8. Planck consistency
    result['planck'] = planck_consistency_test(fam)

    # 9. TCC
    result['tcc'] = tcc_consistency(fam)

    # 10. Temperature
    result['temperature'] = static_patch_temperature_correction(fam, ell)

    # 11. Complementarity
    result['complementarity'] = ds_complementarity_overlap(fam)

    return result


def landscape_survey(ell: float = 1.0) -> List[Dict[str, Any]]:
    """Survey all standard families for dS observables."""
    families = standard_families()
    return [full_desitter_analysis(fam, ell) for fam in families]
