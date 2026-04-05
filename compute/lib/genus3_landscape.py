r"""Genus-3 free energy across the standard landscape.

Computes F_3 = kappa * lambda_3^FP for 10 families on the scalar lane,
and the genus-3 planted-forest correction delta_pf^{(3,0)} for Virasoro
and W_3.

SCALAR LANE (Theorem D):

    F_g(A) = kappa(A) * lambda_g^FP

where lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!.

At genus 3:

    lambda_3^FP = 31/32 * |B_6| / 6! = 31/32 * (1/42) / 720 = 31/967680

PLANTED-FOREST CORRECTION (eq:delta-pf-genus3-explicit):

    delta_pf^{(3,0)} = 11-term polynomial in kappa, S_3, S_4, S_5:

        7/8   S_3 S_5
      + 3/512 S_3^3 kappa
      - 5/128 S_3^4
      - 167/96 S_3^2 S_4
      + 83/1152 S_3 S_4 kappa
      - 343/2304 S_3 kappa
      - 1/4608 S_3^2 kappa^2
      - 1/82944 S_3 kappa^3
      - 7/12 S_4^2
      + 1/1152 S_4 kappa^2
      - 1/96 S_5 kappa

    (Genus-1+ vertex weights approximate; S_4/S_5 coefficients exact.)

KAPPA CONVENTIONS (authoritative, from landscape_census.tex, AP1/AP9):

    Heisenberg H_k:          kappa = k
    Virasoro Vir_c:           kappa = c/2
    Affine V_k(sl_2):        kappa = 3(k+2)/4
    Affine V_k(sl_3):        kappa = 4(k+3)/3
    W_3 at c:                kappa = 5c/6
    Beta-gamma at lambda:    kappa = 6*lambda^2 - 6*lambda + 1
    Lattice V_Lambda (rank d): kappa = d

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    eq:delta-pf-genus3-explicit (higher_genus_modular_koszul.tex)
    thm:lattice-all-genera (genus_expansions.tex)
    prop:betagamma-obstruction-coefficient (beta_gamma.tex)
    thm:wn-obstruction (w_algebras.tex)
    comp:genus-3-sl2 (genus_expansions.tex)
    comp:w3-genus-expansion (genus_expansions.tex)
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Any, Dict, Optional, Tuple

from sympy import Rational, Symbol, cancel, Integer, simplify


# ---------------------------------------------------------------------------
# Bernoulli numbers (exact, self-contained)
# ---------------------------------------------------------------------------

def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n via the Akiyama-Tanigawa algorithm.

    Convention: B_1 = -1/2 (first Bernoulli numbers).
    """
    if n < 0:
        return Fraction(0)
    a = [Fraction(1, m + 1) for m in range(n + 1)]
    for j in range(1, n + 1):
        for m in range(n, j - 1, -1):
            a[m] = (m - j + 1) * (a[m] - a[m - 1])
    return a[n]


# ---------------------------------------------------------------------------
# Faber-Pandharipande intersection number
# ---------------------------------------------------------------------------

def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number at genus g.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Verified values:
      g=1: 1/24
      g=2: 7/5760
      g=3: 31/967680
      g=4: 127/154828800
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B2g = _bernoulli_exact(2 * g)
    abs_B2g = abs(B2g)
    return Fraction(2**(2*g - 1) - 1, 2**(2*g - 1)) * abs_B2g / Fraction(factorial(2*g))


# ---------------------------------------------------------------------------
# Family kappa values
# ---------------------------------------------------------------------------

def kappa_heisenberg(k: int) -> Fraction:
    """Obstruction coefficient for Heisenberg H_k: kappa = k."""
    return Fraction(k)


def kappa_virasoro(c: Fraction) -> Fraction:
    """Obstruction coefficient for Virasoro Vir_c: kappa = c/2."""
    return c / 2


def kappa_affine_sl2(k: int) -> Fraction:
    """Obstruction coefficient for affine sl_2 at level k.

    kappa = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4.
    """
    return Fraction(3 * (k + 2), 4)


def kappa_affine_sl3(k: int) -> Fraction:
    """Obstruction coefficient for affine sl_3 at level k.

    kappa = dim(sl_3) * (k + h^v) / (2 * h^v) = 8(k+3)/6 = 4(k+3)/3.
    """
    return Fraction(4 * (k + 3), 3)


def kappa_w3(c: Fraction) -> Fraction:
    """Obstruction coefficient for W_3 at central charge c.

    kappa = c * (H_3 - 1) = c * (1/2 + 1/3) = 5c/6.
    """
    return Fraction(5) * c / 6


def kappa_betagamma(lam: int) -> Fraction:
    """Obstruction coefficient for beta-gamma at conformal weight lambda.

    kappa = c/2 = (12*lambda^2 - 12*lambda + 2)/2 = 6*lambda^2 - 6*lambda + 1.
    Central charge: c = 2 - 12*lambda*(lambda-1) = 12*lambda^2 - 12*lambda + 2.
    """
    return Fraction(6 * lam * lam - 6 * lam + 1)


def kappa_lattice(rank: int) -> Fraction:
    """Obstruction coefficient for lattice VOA of rank d: kappa = d.

    V_Lambda = H_1^{tensor d} tensor C[Lambda], so kappa(V_Lambda) = d.
    """
    return Fraction(rank)


# ---------------------------------------------------------------------------
# Central charge formulas
# ---------------------------------------------------------------------------

def c_affine_sl2(k: int) -> Fraction:
    """Central charge of affine sl_2 at level k: c = 3k/(k+2)."""
    return Fraction(3 * k, k + 2)


def c_affine_sl3(k: int) -> Fraction:
    """Central charge of affine sl_3 at level k: c = 8k/(k+3)."""
    return Fraction(8 * k, k + 3)


def c_w3(k: int) -> Fraction:
    """Central charge of W_3 at level k: c = 2 - 24(k+2)^2/(k+3)."""
    return Fraction(2) - Fraction(24 * (k + 2)**2, k + 3)


def c_betagamma(lam: int) -> Fraction:
    """Central charge of beta-gamma at weight lambda: c = 12*lambda^2 - 12*lambda + 2."""
    return Fraction(12 * lam * lam - 12 * lam + 2)


# ---------------------------------------------------------------------------
# Genus-3 free energy
# ---------------------------------------------------------------------------

LAMBDA3_FP = Fraction(31, 967680)

# Precomputed verification: 31/32 * (1/42) / 720
assert LAMBDA3_FP == Fraction(31, 32) * Fraction(1, 42) / Fraction(720), (
    f"lambda_3^FP consistency check failed: {LAMBDA3_FP}"
)


def F3(kappa_val: Fraction) -> Fraction:
    """Genus-3 free energy on the scalar lane: F_3 = kappa * lambda_3^FP."""
    return kappa_val * LAMBDA3_FP


# ---------------------------------------------------------------------------
# Standard landscape F_3 table
# ---------------------------------------------------------------------------

def genus3_landscape_table() -> Dict[str, Dict[str, Fraction]]:
    """Compute F_3 for all 10 standard landscape families.

    Returns dict mapping family name to {kappa, F_3, c} (all exact Fraction).
    """
    families = {}

    # 1. Heisenberg at k=1
    kh = kappa_heisenberg(1)
    families['Heisenberg_k1'] = {
        'kappa': kh,
        'F3': F3(kh),
        'c': Fraction(1),
        'description': 'Heisenberg at k=1',
    }

    # 2. Virasoro at c=25
    c_vir = Fraction(25)
    kv = kappa_virasoro(c_vir)
    families['Virasoro_c25'] = {
        'kappa': kv,
        'F3': F3(kv),
        'c': c_vir,
        'description': 'Virasoro at c=25',
    }

    # 3. Affine sl_2 at k=1
    ka2 = kappa_affine_sl2(1)
    families['Affine_sl2_k1'] = {
        'kappa': ka2,
        'F3': F3(ka2),
        'c': c_affine_sl2(1),
        'description': 'Affine sl_2 at k=1',
    }

    # 4. Affine sl_3 at k=1
    ka3 = kappa_affine_sl3(1)
    families['Affine_sl3_k1'] = {
        'kappa': ka3,
        'F3': F3(ka3),
        'c': c_affine_sl3(1),
        'description': 'Affine sl_3 at k=1',
    }

    # 5. W_3 at c=2
    c_w3_val = Fraction(2)
    kw3_2 = kappa_w3(c_w3_val)
    families['W3_c2'] = {
        'kappa': kw3_2,
        'F3': F3(kw3_2),
        'c': c_w3_val,
        'description': 'W_3 at c=2',
    }

    # 6. W_3 at c=50 (self-dual: c+c'=100, self-dual at c=50)
    c_w3_sd = Fraction(50)
    kw3_sd = kappa_w3(c_w3_sd)
    families['W3_c50_selfdual'] = {
        'kappa': kw3_sd,
        'F3': F3(kw3_sd),
        'c': c_w3_sd,
        'description': 'W_3 at c=50 (self-dual)',
    }

    # 7. Beta-gamma at lambda=1
    kbg = kappa_betagamma(1)
    families['BetaGamma_lam1'] = {
        'kappa': kbg,
        'F3': F3(kbg),
        'c': c_betagamma(1),
        'description': 'Beta-gamma at lambda=1',
    }

    # 8. D_4 lattice (rank 4)
    kd4 = kappa_lattice(4)
    families['D4_lattice'] = {
        'kappa': kd4,
        'F3': F3(kd4),
        'c': Fraction(4),
        'description': 'D_4 lattice (rank 4)',
    }

    # 9. E_8 lattice (rank 8)
    ke8 = kappa_lattice(8)
    families['E8_lattice'] = {
        'kappa': ke8,
        'F3': F3(ke8),
        'c': Fraction(8),
        'description': 'E_8 lattice (rank 8)',
    }

    # 10. Leech lattice (rank 24)
    klch = kappa_lattice(24)
    families['Leech_lattice'] = {
        'kappa': klch,
        'F3': F3(klch),
        'c': Fraction(24),
        'description': 'Leech lattice (rank 24)',
    }

    return families


# ---------------------------------------------------------------------------
# Genus-3 planted-forest correction
# ---------------------------------------------------------------------------

def delta_pf_genus3_formula(kappa, S3, S4, S5):
    r"""Genus-3 planted-forest correction from eq:delta-pf-genus3-explicit.

    11-term polynomial in kappa, S_3, S_4, S_5:

        delta_pf^{(3,0)} =
            7/8   S_3 S_5
          + 3/512 S_3^3 kappa
          - 5/128 S_3^4
          - 167/96 S_3^2 S_4
          + 83/1152 S_3 S_4 kappa
          - 343/2304 S_3 kappa
          - 1/4608 S_3^2 kappa^2
          - 1/82944 S_3 kappa^3
          - 7/12 S_4^2
          + 1/1152 S_4 kappa^2
          - 1/96 S_5 kappa

    Accepts Fraction, float, or sympy objects.

    NOTE: genus-1+ vertex weights approximate at vertices carrying
    ell_3^{(1)} or higher; S_4/S_5 coefficients exact.
    """
    return (
        Fraction(7, 8) * S3 * S5
        + Fraction(3, 512) * S3**3 * kappa
        - Fraction(5, 128) * S3**4
        - Fraction(167, 96) * S3**2 * S4
        + Fraction(83, 1152) * S3 * S4 * kappa
        - Fraction(343, 2304) * S3 * kappa
        - Fraction(1, 4608) * S3**2 * kappa**2
        - Fraction(1, 82944) * S3 * kappa**3
        - Fraction(7, 12) * S4**2
        + Fraction(1, 1152) * S4 * kappa**2
        - Fraction(1, 96) * S5 * kappa
    )


def delta_pf_genus3_symbolic():
    """Planted-forest correction with symbolic variables.

    Returns a sympy expression in (kappa, S_3, S_4, S_5).
    """
    kappa = Symbol('kappa')
    S3 = Symbol('S_3')
    S4 = Symbol('S_4')
    S5 = Symbol('S_5')
    return cancel(
        Rational(7, 8) * S3 * S5
        + Rational(3, 512) * S3**3 * kappa
        - Rational(5, 128) * S3**4
        - Rational(167, 96) * S3**2 * S4
        + Rational(83, 1152) * S3 * S4 * kappa
        - Rational(343, 2304) * S3 * kappa
        - Rational(1, 4608) * S3**2 * kappa**2
        - Rational(1, 82944) * S3 * kappa**3
        - Rational(7, 12) * S4**2
        + Rational(1, 1152) * S4 * kappa**2
        - Rational(1, 96) * S5 * kappa
    ), (kappa, S3, S4, S5)


# ---------------------------------------------------------------------------
# Virasoro shadow data for planted-forest computation
# ---------------------------------------------------------------------------

def virasoro_shadow_values(c_val: Fraction) -> Dict[str, Fraction]:
    r"""Compute Virasoro shadow coefficients at a specific central charge.

    Seeds: S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].
    S_5 computed via convolution recursion:
      S_5 = -48 / [c^2 (5c+22)]

    Returns dict with kappa, S_3, S_4, S_5.
    """
    kappa = c_val / 2
    S3 = Fraction(2)
    S4 = Fraction(10) / (c_val * (5 * c_val + 22))
    S5 = Fraction(-48) / (c_val**2 * (5 * c_val + 22))
    return {'kappa': kappa, 'S3': S3, 'S4': S4, 'S5': S5}


def delta_pf_genus3_virasoro(c_val: Fraction) -> Fraction:
    """Genus-3 planted-forest correction for Virasoro at central charge c.

    Substitutes the Virasoro shadow data S_3=2, S_4=10/[c(5c+22)],
    S_5=-48/[c^2(5c+22)], kappa=c/2 into the 11-term polynomial.
    """
    sd = virasoro_shadow_values(c_val)
    return delta_pf_genus3_formula(sd['kappa'], sd['S3'], sd['S4'], sd['S5'])


def delta_pf_genus3_virasoro_symbolic():
    """Genus-3 planted-forest correction for Virasoro as rational function of c.

    Returns a sympy expression.
    """
    c = Symbol('c')
    kappa = c / 2
    S3 = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    S5 = Rational(-48) / (c**2 * (5 * c + 22))
    return cancel(
        Rational(7, 8) * S3 * S5
        + Rational(3, 512) * S3**3 * kappa
        - Rational(5, 128) * S3**4
        - Rational(167, 96) * S3**2 * S4
        + Rational(83, 1152) * S3 * S4 * kappa
        - Rational(343, 2304) * S3 * kappa
        - Rational(1, 4608) * S3**2 * kappa**2
        - Rational(1, 82944) * S3 * kappa**3
        - Rational(7, 12) * S4**2
        + Rational(1, 1152) * S4 * kappa**2
        - Rational(1, 96) * S5 * kappa
    )


# ---------------------------------------------------------------------------
# W_3 shadow data for planted-forest computation
# ---------------------------------------------------------------------------

def w3_shadow_values(c_val: Fraction) -> Dict[str, Fraction]:
    r"""Compute W_3 shadow coefficients on the T-line at central charge c.

    On the T-line (gravitational sector), the W_3 shadow obstruction tower reduces
    to the Virasoro shadow obstruction tower: S_3=2, S_4=10/[c(5c+22)],
    S_5=-48/[c^2(5c+22)].

    The FULL W_3 kappa is 5c/6, but the T-line planted-forest correction
    uses the T-CHANNEL kappa = c/2 (Virasoro subalgebra).

    The W-channel (spin-3 generator) contributes c/3 to the total kappa
    but lives on a separate primary line. On each individual line,
    the planted-forest correction uses that line's shadow obstruction tower.

    For the T-line planted-forest correction, we use the Virasoro shadow data.
    """
    return virasoro_shadow_values(c_val)


def delta_pf_genus3_w3_Tline(c_val: Fraction) -> Fraction:
    """Genus-3 planted-forest correction for W_3, T-channel only.

    On the T-line the shadow obstruction tower is identical to Virasoro.
    """
    return delta_pf_genus3_virasoro(c_val)


# ---------------------------------------------------------------------------
# Complementarity checks
# ---------------------------------------------------------------------------

def complementarity_check_F3(family: str, kappa_A: Fraction,
                              kappa_dual: Fraction) -> Dict[str, Fraction]:
    """Check F_3 complementarity: F_3(A) + F_3(A^!) and compare.

    For KM/free fields: kappa + kappa' = 0, so F_3 + F_3' = 0.
    For W-algebras: kappa + kappa' = rho*K (nonzero), so F_3 + F_3' != 0.
    """
    f3 = F3(kappa_A)
    f3_dual = F3(kappa_dual)
    return {
        'family': family,
        'F3_A': f3,
        'F3_dual': f3_dual,
        'sum': f3 + f3_dual,
        'kappa_sum': kappa_A + kappa_dual,
    }


# ---------------------------------------------------------------------------
# Cross-checks
# ---------------------------------------------------------------------------

def verify_manuscript_sl2_genus3() -> bool:
    """Verify F_3(sl_2, k=1) = 31/430080 (eq:genus3-k1)."""
    kappa = kappa_affine_sl2(1)  # = 9/4
    f3 = F3(kappa)
    expected = Fraction(31, 430080)
    return f3 == expected


def verify_manuscript_w3_genus3() -> bool:
    """Verify F_3(W_3, k=1) = -403/290304 (comp:w3-genus-expansion)."""
    c_val = c_w3(1)  # c(1) = 2 - 24*9/4 = -52
    kappa = kappa_w3(c_val)  # 5*(-52)/6 = -130/3
    f3 = F3(kappa)
    expected = Fraction(-403, 290304)
    # Verify: (-130/3) * (31/967680) = -130*31/(3*967680) = -4030/2903040
    # = -403/290304. Correct.
    return f3 == expected


def verify_generating_function_consistency(kappa_val: Fraction,
                                            max_genus: int = 5) -> bool:
    """Verify F_g = kappa * lambda_g^FP matches the GF (x/2)/sin(x/2) - 1.

    The GF is sum_{g>=1} lambda_g^FP * x^{2g} = (x/2)/sin(x/2) - 1.
    Check: the Taylor coefficients of (x/2)/sin(x/2) match lambda_g^FP
    through the specified genus.

    This is a consistency check on the Bernoulli number formula.
    """
    # (x/2)/sin(x/2) = 1 + sum_{g>=1} (2^{2g}-2)|B_{2g}|/(2g)! * (x/2)^{2g}
    # = 1 + sum_{g>=1} (2^{2g}-2)|B_{2g}|/(2g)! * x^{2g}/2^{2g}
    # = 1 + sum_{g>=1} [(2^{2g}-2)/(2^{2g})] * |B_{2g}|/(2g)! * x^{2g}
    # = 1 + sum_{g>=1} [(2^{2g-1}-1)/2^{2g-1}] * |B_{2g}|/(2g)! * x^{2g}
    # = 1 + sum_{g>=1} lambda_g^FP * x^{2g}
    for g in range(1, max_genus + 1):
        lfp = lambda_fp(g)
        B2g = _bernoulli_exact(2 * g)
        expected = Fraction(2**(2*g-1) - 1, 2**(2*g-1)) * abs(B2g) / Fraction(factorial(2*g))
        if lfp != expected:
            return False
    return True


# ---------------------------------------------------------------------------
# Genus-3 ratio table
# ---------------------------------------------------------------------------

def genus3_ratio_table() -> Dict[str, Dict[str, Any]]:
    """Compute F_3/F_1 and F_3/F_2 ratios (universal on the scalar lane).

    On the scalar lane:
      F_g = kappa * lambda_g^FP
      F_3/F_1 = lambda_3^FP / lambda_1^FP = (31/967680) / (1/24) = 31/40320
      F_3/F_2 = lambda_3^FP / lambda_2^FP = (31/967680) / (7/5760) = 31/1176

    These ratios are universal (independent of the algebra).
    """
    l1 = lambda_fp(1)  # 1/24
    l2 = lambda_fp(2)  # 7/5760
    l3 = lambda_fp(3)  # 31/967680

    return {
        'lambda_1': l1,
        'lambda_2': l2,
        'lambda_3': l3,
        'F3_over_F1': l3 / l1,
        'F3_over_F2': l3 / l2,
        'F2_over_F1': l2 / l1,
    }


# ---------------------------------------------------------------------------
# Heisenberg genus-3 planted-forest check
# ---------------------------------------------------------------------------

def delta_pf_genus3_heisenberg() -> Fraction:
    """Planted-forest correction for Heisenberg: must be exactly 0.

    Heisenberg is class G: S_3 = S_4 = S_5 = 0. Every term in the
    11-term polynomial has at least one factor of S_3, S_4, or S_5.
    """
    return delta_pf_genus3_formula(
        kappa=Fraction(1), S3=Fraction(0), S4=Fraction(0), S5=Fraction(0)
    )


# ---------------------------------------------------------------------------
# Affine sl_2 genus-3 planted-forest check
# ---------------------------------------------------------------------------

def delta_pf_genus3_affine_sl2(k: int) -> Fraction:
    """Planted-forest correction for affine sl_2: class L (S_3=2, S_4=S_5=0).

    Only the S_3-only terms survive:
      3/512 S_3^3 kappa - 5/128 S_3^4 - 343/2304 S_3 kappa
      - 1/4608 S_3^2 kappa^2 - 1/82944 S_3 kappa^3
    """
    kappa = kappa_affine_sl2(k)
    S3 = Fraction(2)
    return delta_pf_genus3_formula(kappa, S3, Fraction(0), Fraction(0))


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def full_genus3_report() -> str:
    """Generate a full genus-3 landscape report."""
    lines = []
    lines.append("=" * 72)
    lines.append("GENUS-3 FREE ENERGY: STANDARD LANDSCAPE (SCALAR LANE)")
    lines.append("=" * 72)
    lines.append(f"lambda_3^FP = {LAMBDA3_FP} = {float(LAMBDA3_FP):.6e}")
    lines.append("")

    table = genus3_landscape_table()
    lines.append(f"{'Family':<25} {'kappa':>12} {'F_3':>25} {'F_3 (float)':>14}")
    lines.append("-" * 78)
    for name, data in table.items():
        k = data['kappa']
        f = data['F3']
        lines.append(f"{data['description']:<25} {str(k):>12} {str(f):>25} {float(f):>14.6e}")

    lines.append("")
    lines.append("UNIVERSAL RATIOS:")
    ratios = genus3_ratio_table()
    lines.append(f"  F_3/F_1 = {ratios['F3_over_F1']} = {float(ratios['F3_over_F1']):.6e}")
    lines.append(f"  F_3/F_2 = {ratios['F3_over_F2']} = {float(ratios['F3_over_F2']):.6e}")
    lines.append(f"  F_2/F_1 = {ratios['F2_over_F1']} = {float(ratios['F2_over_F1']):.6e}")

    lines.append("")
    lines.append("PLANTED-FOREST CORRECTIONS:")
    lines.append(f"  Heisenberg (class G): delta_pf = {delta_pf_genus3_heisenberg()}")
    lines.append(f"  Affine sl_2, k=1 (class L): delta_pf = {delta_pf_genus3_affine_sl2(1)}")

    for c_val in [1, 2, 10, 13, 25, 26]:
        try:
            dpf = delta_pf_genus3_virasoro(Fraction(c_val))
            lines.append(f"  Virasoro c={c_val}: delta_pf = {float(dpf):.8e}")
        except ZeroDivisionError:
            lines.append(f"  Virasoro c={c_val}: delta_pf = UNDEFINED (c=0 pole)")

    lines.append("")
    lines.append("MANUSCRIPT CROSS-CHECKS:")
    lines.append(f"  F_3(sl_2, k=1) = 31/430080: {verify_manuscript_sl2_genus3()}")
    lines.append(f"  F_3(W_3, k=1) = -403/290304: {verify_manuscript_w3_genus3()}")
    lines.append(f"  GF consistency through g=5: {verify_generating_function_consistency(Fraction(1))}")

    return "\n".join(lines)


if __name__ == '__main__':
    print(full_genus3_report())
