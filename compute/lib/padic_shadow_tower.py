r"""p-adic shadow obstruction tower interpolation.

This module investigates the p-adic structure of the shadow Postnikov tower,
connecting the Maurer-Cartan framework to Iwasawa theory and p-adic
L-functions.

MATHEMATICAL FRAMEWORK
======================

1. VIRASORO SHADOW COEFFICIENTS ARE RATIONAL POLYNOMIALS IN c.

   At leading order (tree level on the Kummer-motive diagonal):
     S_r(c) = (-1)^{r+1} * (6/c)^r / r    for r >= 2

   These are rational functions of c. For any prime p and any c in Z_p^*,
   the shadow coefficients S_r(c) lie in Q_p.

2. THE SCALAR GENUS EXPANSION INVOLVES BERNOULLI NUMBERS.

   F_g(A) = kappa(A) * lambda_g^FP, where
   lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

   The generating function Z^sh(hbar) = kappa * (A-hat(i*hbar) - 1)
   where A-hat(ix) = (x/2)/sin(x/2).

3. KUMMER CONGRUENCES.

   The Bernoulli numbers satisfy Kummer congruences:
     B_m/m = B_n/n  (mod p)
   when m = n (mod p-1), m, n even positive, (p-1) does not divide m or n.

   These congruences define the Kubota-Leopoldt p-adic L-function
   L_p(s, chi) that interpolates L(1-n, chi) at positive integers n.

4. p-ADIC CONVERGENCE OF Z^sh.

   The p-adic valuation v_p(lambda_g^FP) is controlled by:
   - v_p(B_{2g}): by Clausen-von Staudt, denom(B_{2g}) = prod_{(p-1)|2g} p,
     so v_p(B_{2g}) = -1 when (p-1)|2g, else v_p(B_{2g}) >= 0.
   - v_p((2g)!): by Legendre's formula, = (2g - s_p(2g))/(p-1) where
     s_p(n) is the digit sum of n in base p.
   - v_p(2^{2g-1} - 1): vanishes iff p = 2 (Fermat little theorem gives
     2^{p-1} = 1 mod p for odd p).

   Asymptotically, v_p(lambda_g^FP) / (2g) -> -1/(p-1) as g -> infinity.
   The p-adic radius of convergence of sum lambda_g^FP * hbar^{2g} is
   therefore R_p = p^{1/(p-1)}, the p-adic exponential convergence radius.

   This is NOT a coincidence: the A-hat genus is related to the Todd class
   via the exponential function, and the p-adic exponential exp_p(x)
   converges on the disc |x|_p < p^{-1/(p-1)}.

5. p-ADIC SHADOW METRIC.

   The shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
   has discriminant Delta = 8*kappa*S_4.

   For Virasoro: Delta(c) = c^2(5c+22)/30.
   The zeros of Delta in Q_p: c = 0 and c = -22/5 (in Z_p when p != 5).

   The p-adic valuation v_p(Delta(c)) controls the p-adic shadow depth:
   large v_p(Delta) means the shadow obstruction tower is p-adically close to degenerate
   (class G/L where Delta = 0).

6. IWASAWA-THEORETIC INTERPRETATION (SPECULATIVE).

   The scalar shadow partition function Z^sh(hbar, kappa) = kappa * (A-hat(ihbar) - 1)
   is an ANALYTIC FUNCTION on the p-adic disc |hbar|_p < R_p = p^{1/(p-1)}.

   For kappa = c/2 with c in Z_p, this defines a p-adic family of shadow
   generating functions parametrized by c in Z_p. The analogy with Iwasawa
   theory:
   - The p-adic shadow GF plays the role of a p-adic L-function
   - The shadow depth classification (G/L/C/M) is the analogue of the
     mu-invariant / lambda-invariant decomposition
   - The Kummer congruences for lambda_g^FP are exactly the interpolation
     conditions that define L_p(s, chi)
   - The zeros of the p-adic shadow metric are the analogue of Iwasawa
     zero sets

   The connection to the actual Kubota-Leopoldt L-function:
   zeta_p(1-2g) = (1 - p^{2g-1}) * B_{2g}/(2g)
   The lambda_g^FP involves B_{2g}/(2g)! = B_{2g}/(2g) * 1/(2g-1)!
   So lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |zeta(1-2g)| / (2g-1)!
                  * 1/(1 - p^{2g-1})  [up to the p-Euler factor]

   The shadow partition function is therefore built from special values
   of the Riemann zeta function at negative odd integers, modified by
   the Euler factor at 2 and the factorial denominators.

Manuscript references:
    chap:arithmetic-shadows (arithmetic_shadows.tex)
    rem:kummer-motive (arithmetic_shadows.tex)
    thm:shadow-spectral-correspondence (arithmetic_shadows.tex)
    cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, gcd, log
from typing import Dict, List, Optional, Tuple


# ============================================================================
# 1. Exact Bernoulli numbers
# ============================================================================

def bernoulli_numbers(max_n: int) -> List[Fraction]:
    """Compute Bernoulli numbers B_0, B_1, ..., B_{max_n} as exact fractions.

    Uses the standard recursion from the generating function x/(e^x - 1).
    Convention: B_1 = -1/2 (the 'first Bernoulli number' convention).
    B_n = 0 for odd n >= 3.
    """
    B = [Fraction(0)] * (max_n + 1)
    B[0] = Fraction(1)
    if max_n >= 1:
        B[1] = Fraction(-1, 2)
    for k in range(2, max_n + 1):
        if k % 2 == 1:
            B[k] = Fraction(0)
            continue
        s = Fraction(0)
        for j in range(k):
            s += Fraction(comb(k + 1, j)) * B[j]
        B[k] = -s / (k + 1)
    return B


# ============================================================================
# 2. p-adic valuation
# ============================================================================

def v_p(x: Fraction, p: int) -> int:
    """Compute the p-adic valuation v_p(x) for a rational number x.

    Returns the unique integer v such that x = p^v * (a/b) with
    gcd(a, p) = gcd(b, p) = 1.

    Raises ValueError if x = 0 (v_p(0) = +infinity).
    """
    if x == 0:
        raise ValueError("v_p(0) is +infinity")
    f = Fraction(x)
    num = abs(f.numerator)
    den = f.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def v_p_safe(x: Fraction, p: int) -> float:
    """v_p with infinity for zero."""
    if x == 0:
        return float('inf')
    return float(v_p(x, p))


# ============================================================================
# 3. Faber-Pandharipande coefficients lambda_g^FP
# ============================================================================

def faber_pandharipande_coefficient(g: int, bernoulli_cache: Optional[List[Fraction]] = None) -> Fraction:
    """Compute lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    This is the genus-g coefficient in the scalar free energy:
    F_g(A) = kappa(A) * lambda_g^FP.

    The generating function is kappa * (A-hat(i*hbar) - 1) = sum_{g>=1} kappa * lambda_g * hbar^{2g}.
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    if bernoulli_cache is not None:
        B2g = bernoulli_cache[2 * g]
    else:
        B2g = bernoulli_numbers(2 * g)[2 * g]
    numerator = (2 ** (2 * g - 1) - 1) * abs(B2g)
    denominator = 2 ** (2 * g - 1) * factorial(2 * g)
    return Fraction(numerator) / Fraction(denominator)


# ============================================================================
# 4. Kummer congruences verification
# ============================================================================

def verify_kummer_congruence(m: int, n: int, p: int,
                              bernoulli_cache: Optional[List[Fraction]] = None) -> Tuple[bool, int]:
    """Verify the Kummer congruence B_m/m ≡ B_n/n (mod p).

    Conditions: m, n even positive, m ≡ n (mod p-1), (p-1) does not divide m or n.

    Returns (holds, v_p_of_difference):
        holds: True if v_p(B_m/m - B_n/n) >= 1
        v_p_of_difference: the exact p-adic valuation of the difference
    """
    if m % 2 != 0 or n % 2 != 0 or m <= 0 or n <= 0:
        raise ValueError(f"m={m}, n={n} must be even positive integers")
    if (m - n) % (p - 1) != 0:
        raise ValueError(f"m={m}, n={n} must be congruent mod p-1={p-1}")
    if m % (p - 1) == 0 or n % (p - 1) == 0:
        raise ValueError(f"(p-1)={p-1} must not divide m={m} or n={n}")

    if bernoulli_cache is None:
        max_idx = max(m, n)
        bernoulli_cache = bernoulli_numbers(max_idx)

    bm = bernoulli_cache[m] / m
    bn = bernoulli_cache[n] / n
    diff = bm - bn
    if diff == 0:
        return True, float('inf')
    vp = v_p(diff, p)
    return vp >= 1, vp


def kummer_congruence_table(p: int, max_index: int = 30) -> List[Dict]:
    """Generate a table of all Kummer congruence verifications for prime p.

    Returns list of dicts with keys: m, n, holds, v_p.
    """
    Bs = bernoulli_numbers(max_index)
    results = []
    for m in range(2, max_index + 1, 2):
        if m % (p - 1) == 0:
            continue
        for n in range(m + (p - 1), max_index + 1, p - 1):
            if n % 2 != 0:
                continue
            if n % (p - 1) == 0:
                continue
            holds, vp = verify_kummer_congruence(m, n, p, Bs)
            results.append({'m': m, 'n': n, 'p': p, 'holds': holds, 'v_p': vp})
    return results


# ============================================================================
# 5. Virasoro shadow coefficients (tree-level / Kummer-motive diagonal)
# ============================================================================

def virasoro_shadow_coefficient_tree(r: int, c: Fraction) -> Fraction:
    """Tree-level Virasoro shadow coefficient S_r(c) = (-1)^{r+1} * (6/c)^r / r.

    This is the leading-order (Kummer motive diagonal) contribution.
    From rem:kummer-motive: G(t) = -log(1 + 6t/c), so
    S_r = [t^r] G(t) / r = (-1)^{r+1} * (6/c)^r / r.

    Parameters:
        r: arity (>= 2)
        c: central charge as a Fraction (must be nonzero)
    """
    if r < 2:
        raise ValueError(f"arity must be >= 2, got {r}")
    if c == 0:
        raise ValueError("c must be nonzero")
    c = Fraction(c)
    return Fraction((-1) ** (r + 1)) * Fraction(6, 1) ** r / (c ** r * r)


def virasoro_shadow_exact(r: int, c: Fraction) -> Fraction:
    """Exact shadow coefficient S_r for Virasoro from the full recursive tower.

    Uses the exact formulas:
      S_2 = c/2 (kappa)
      S_3 = 5c/6 (cubic shadow)
      S_4 = c(5c+22)/120 (quartic contact)

    Then recursion from the shadow metric Q_L(t).

    For higher r, uses the Taylor expansion of sqrt(Q_L).
    """
    c = Fraction(c)
    kappa = c / 2
    alpha = Fraction(5) * c / 6  # S_3
    S4 = c * (5 * c + 22) / 120

    # Shadow metric coefficients
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    # Taylor expansion of sqrt(Q_L)
    # S_r = a_{r-2} where a_n = [t^n] sqrt(Q_L(t))
    # Wait: S_r = a_{r-2} is not divided by r here since
    # H(t) = t^2 sqrt(Q_L(t)) = sum_r r S_r t^r
    # So r S_r = a_{r-2}, hence S_r = a_{r-2}/r
    # ... but a_0 = 2|kappa| = c (for c > 0), and S_2 = a_0/2 = c/2 = kappa. Check.

    max_n = r - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = 2 * kappa  # sqrt(q0) = sqrt(4*kappa^2) = 2*|kappa|; take positive branch
    if max_n >= 1:
        a[1] = q1 / (2 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a[0])
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    return a[max_n] / r


# ============================================================================
# 6. p-adic convergence analysis of the genus expansion
# ============================================================================

def padic_genus_expansion_analysis(p: int, max_genus: int = 30) -> Dict:
    """Analyze p-adic convergence of the genus expansion sum lambda_g hbar^{2g}.

    Returns dict with:
      - valuations: list of (g, v_p(lambda_g)) pairs
      - ratios: list of (g, v_p(lambda_g)/(2g)) pairs
      - limiting_ratio: the limiting value of v_p(lambda_g)/(2g) as g -> inf
      - radius: the p-adic radius of convergence R_p
      - theoretical_ratio: -1/(p-1) (the theoretical prediction)
      - theoretical_radius: p^{1/(p-1)} (the theoretical prediction)
    """
    Bs = bernoulli_numbers(2 * max_genus)
    valuations = []
    ratios = []

    for g in range(1, max_genus + 1):
        lam = faber_pandharipande_coefficient(g, Bs)
        vp = v_p(lam, p)
        ratio = vp / (2 * g)
        valuations.append((g, vp))
        ratios.append((g, ratio))

    # Theoretical prediction: v_p(lambda_g)/(2g) -> -1/(p-1)
    # because v_p((2g)!) ~ 2g/(p-1) and v_p(B_{2g}) is bounded
    theoretical_ratio = -1.0 / (p - 1)
    theoretical_radius = p ** (1.0 / (p - 1))

    # Empirical limiting ratio (take last 5 values)
    recent = [r for _, r in ratios[-5:]]
    empirical = min(recent)  # lim inf

    return {
        'p': p,
        'valuations': valuations,
        'ratios': ratios,
        'limiting_ratio': empirical,
        'theoretical_ratio': theoretical_ratio,
        'radius': p ** (-empirical),
        'theoretical_radius': theoretical_radius,
    }


# ============================================================================
# 7. p-adic shadow metric analysis
# ============================================================================

def virasoro_discriminant(c: Fraction) -> Fraction:
    """Critical discriminant Delta(c) = c^2(5c+22)/30 for Virasoro.

    Delta = 8 * kappa * S_4 = 8 * (c/2) * c(5c+22)/120 = c^2(5c+22)/30.
    """
    c = Fraction(c)
    return c ** 2 * (5 * c + 22) / 30


def padic_shadow_metric_table(p: int, max_c: int = None) -> List[Dict]:
    """Compute v_p(Delta(c)) for c = 1, ..., p-1 and related invariants.

    Returns list of dicts with keys: c, Delta, v_p_Delta, depth_class.
    """
    if max_c is None:
        max_c = p - 1
    results = []
    for c_val in range(1, max_c + 1):
        c = Fraction(c_val)
        delta = virasoro_discriminant(c)
        if delta == 0:
            vp_delta = float('inf')
            depth = 'G/L'
        else:
            vp_delta = v_p(delta, p)
            depth = 'M' if vp_delta < float('inf') else 'G/L'

        results.append({
            'c': c_val,
            'Delta': delta,
            'v_p_Delta': vp_delta,
            'depth_class': depth,
            'p': p,
        })
    return results


# ============================================================================
# 8. p-adic Virasoro shadow obstruction tower valuation table
# ============================================================================

def padic_virasoro_shadow_table(p: int, c_val: int, max_arity: int = 20) -> List[Dict]:
    """Compute v_p(S_r(c)) for the exact Virasoro shadow obstruction tower at integer c.

    Returns list of dicts with keys: r, S_r, v_p_S_r.
    """
    c = Fraction(c_val)
    results = []
    for r in range(2, max_arity + 1):
        Sr = virasoro_shadow_exact(r, c)
        if Sr == 0:
            vp_Sr = float('inf')
        else:
            vp_Sr = v_p(Sr, p)
        results.append({
            'r': r,
            'S_r': Sr,
            'v_p_S_r': vp_Sr,
        })
    return results


def padic_virasoro_tree_table(p: int, c_val: int, max_arity: int = 20) -> List[Dict]:
    """Compute v_p(S_r^tree(c)) for the tree-level Kummer shadow obstruction tower.

    S_r^tree = (-1)^{r+1} * (6/c)^r / r.
    v_p(S_r^tree) = r * v_p(6/c) - v_p(r).
    """
    c = Fraction(c_val)
    results = []
    for r in range(2, max_arity + 1):
        Sr = virasoro_shadow_coefficient_tree(r, c)
        if Sr == 0:
            vp_Sr = float('inf')
        else:
            vp_Sr = v_p(Sr, p)
        results.append({
            'r': r,
            'S_r_tree': Sr,
            'v_p_S_r_tree': vp_Sr,
        })
    return results


# ============================================================================
# 9. p-adic interpolation: Kubota-Leopoldt connection
# ============================================================================

def kubota_leopoldt_interpolation_data(p: int, max_n: int = 20) -> List[Dict]:
    """Compute the data for Kubota-Leopoldt interpolation.

    The p-adic zeta function zeta_p(s) interpolates:
      zeta_p(1 - 2g) = -(1 - p^{2g-1}) * B_{2g} / (2g)

    at even positive integers 2g with 2g not divisible by p-1.

    The Faber-Pandharipande coefficient involves:
      lambda_g^FP = (2^{2g-1}-1) / 2^{2g-1} * |B_{2g}| / (2g)!
                  = (2^{2g-1}-1) / 2^{2g-1} * |zeta(1-2g)| * 2 / (2g-1)!

    Returns data showing the p-adic relationship between lambda_g and zeta_p values.
    """
    Bs = bernoulli_numbers(2 * max_n)
    results = []
    for g in range(1, max_n + 1):
        B2g = Bs[2 * g]
        # zeta(1-2g) = -B_{2g}/(2g)
        zeta_val = -B2g / (2 * g)
        # (1 - p^{2g-1}) factor for p-adic interpolation
        euler_factor = 1 - Fraction(p) ** (2 * g - 1)
        # p-adic zeta value: zeta_p(1-2g) = -(1-p^{2g-1}) B_{2g}/(2g) = (1-p^{2g-1}) zeta(1-2g)
        zeta_p_val = euler_factor * zeta_val
        # lambda_g^FP
        lam = faber_pandharipande_coefficient(g, Bs)
        # Ratio: lambda_g / zeta_p_val
        if zeta_p_val != 0:
            ratio = lam / abs(zeta_p_val)
        else:
            ratio = None

        skip = (2 * g) % (p - 1) == 0  # Kummer congruence does not apply

        results.append({
            'g': g,
            'B_2g': B2g,
            'zeta_1_minus_2g': zeta_val,
            'euler_factor': euler_factor,
            'zeta_p_1_minus_2g': zeta_p_val,
            'lambda_g_FP': lam,
            'ratio': ratio,
            'skip': skip,
            'v_p_lambda': v_p(lam, p) if lam != 0 else float('inf'),
            'v_p_zeta_p': v_p(zeta_p_val, p) if zeta_p_val != 0 else float('inf'),
        })
    return results


# ============================================================================
# 10. Lambda-invariant analysis (Iwasawa-theoretic)
# ============================================================================

def iwasawa_lambda_analysis(p: int, max_genus: int = 30) -> Dict:
    """Analyze the Iwasawa lambda-invariant of the shadow obstruction tower.

    In Iwasawa theory, if f(T) = sum a_n T^n is a power series in Z_p[[T]],
    the mu-invariant is min_n v_p(a_n) and the lambda-invariant is the
    smallest n such that v_p(a_n) = mu.

    For the shadow obstruction tower: the 'Iwasawa series' is
    f(T) = sum_{g>=1} lambda_g^FP * T^g  (with T = hbar^2)

    mu_shadow = min_g v_p(lambda_g^FP)
    lambda_shadow = smallest g achieving mu_shadow

    The classical Iwasawa mu = 0 conjecture (proved by Ferrero-Washington
    for abelian extensions) would correspond to mu_shadow = min_g v_p(lambda_g) being finite.
    """
    Bs = bernoulli_numbers(2 * max_genus)
    min_vp = float('inf')
    lambda_idx = None

    valuations = []
    for g in range(1, max_genus + 1):
        lam = faber_pandharipande_coefficient(g, Bs)
        vp = v_p(lam, p)
        valuations.append((g, vp))
        if vp < min_vp:
            min_vp = vp
            lambda_idx = g

    return {
        'p': p,
        'mu_shadow': min_vp,
        'lambda_shadow': lambda_idx,
        'valuations': valuations,
        'interpretation': (
            f"mu = {min_vp} (achieved at g = {lambda_idx}). "
            f"The shadow Iwasawa series has mu-invariant {min_vp}, "
            f"meaning the characteristic power of p dividing all coefficients is p^{min_vp}. "
            f"The lambda-invariant {lambda_idx} is the first genus where this minimum is achieved."
        ),
    }


# ============================================================================
# 11. p-adic shadow obstruction tower convergence on Z_p-family
# ============================================================================

def padic_shadow_family(p: int, max_arity: int = 15) -> List[Dict]:
    """For each c = 1, ..., p-1, compute the p-adic shadow obstruction tower.

    Shows how the shadow obstruction tower varies over the p-adic family parametrized by c.
    """
    results = []
    for c_val in range(1, p):
        c = Fraction(c_val)
        kappa = c / 2
        delta = virasoro_discriminant(c)

        tower_data = []
        for r in range(2, max_arity + 1):
            Sr = virasoro_shadow_exact(r, c)
            vp = v_p_safe(Sr, p)
            tower_data.append({'r': r, 'S_r': float(Sr), 'v_p': vp})

        results.append({
            'c': c_val,
            'kappa': float(kappa),
            'Delta': float(delta),
            'v_p_Delta': v_p_safe(delta, p),
            'tower': tower_data,
        })
    return results


# ============================================================================
# 12. Kummer congruence for shadow generating function
# ============================================================================

def shadow_kummer_congruences(p: int, max_genus: int = 20) -> List[Dict]:
    """Test whether the shadow generating function inherits Kummer congruences.

    The lambda_g^FP involve B_{2g}/(2g)!. If m = n (mod p-1) with
    the standard Kummer conditions, do we have
      lambda_m^FP ≡ lambda_n^FP * (correction factor)  (mod p) ?

    The correction factor comes from the (2^{2g-1}-1)/2^{2g-1} and (2g)! terms.
    """
    Bs = bernoulli_numbers(2 * max_genus)
    results = []

    for m in range(1, max_genus + 1):
        if (2 * m) % (p - 1) == 0:
            continue
        for n in range(m + (p - 1) // 2, max_genus + 1, (p - 1) // 2 if (p - 1) % 2 == 0 else p - 1):
            if (2 * n) % (p - 1) == 0:
                continue
            if (2 * m - 2 * n) % (p - 1) != 0:
                continue
            lam_m = faber_pandharipande_coefficient(m, Bs)
            lam_n = faber_pandharipande_coefficient(n, Bs)
            if lam_m == 0 or lam_n == 0:
                continue
            # The Bernoulli part: B_{2m}/(2m) vs B_{2n}/(2n) satisfies Kummer
            # The extra factors: (2^{2m-1}-1)/2^{2m-1} * 1/(2m-1)! vs same for n
            bern_m = Bs[2 * m] / (2 * m)
            bern_n = Bs[2 * n] / (2 * n)
            bern_diff = bern_m - bern_n
            bern_vp = v_p_safe(bern_diff, p)

            lam_diff = lam_m - lam_n
            lam_vp = v_p_safe(lam_diff, p)

            results.append({
                'g_m': m, 'g_n': n,
                '2m': 2 * m, '2n': 2 * n,
                'v_p_bernoulli_diff': bern_vp,
                'v_p_lambda_diff': lam_vp,
                'bernoulli_kummer_holds': bern_vp >= 1,
            })
    return results


# ============================================================================
# 13. Clausen-von Staudt theorem verification
# ============================================================================

def clausen_von_staudt_verification(max_n: int = 30) -> List[Dict]:
    """Verify Clausen-von Staudt: denom(B_{2n}) = prod_{(p-1)|2n} p.

    B_{2n} + sum_{(p-1)|2n} 1/p is an integer.
    Equivalently: the denominator of B_{2n} is exactly prod_{(p-1)|2n} p.
    """
    Bs = bernoulli_numbers(2 * max_n)
    results = []

    for n in range(1, max_n + 1):
        B2n = Bs[2 * n]
        denom = B2n.denominator

        # Compute the Clausen-von Staudt product
        cvs_product = 1
        dividing_primes = []
        # A prime p divides the CVS product iff (p-1) | 2n
        # Check primes up to 2n + 1
        for p in range(2, 2 * n + 2):
            if not _is_prime(p):
                continue
            if (2 * n) % (p - 1) == 0:
                dividing_primes.append(p)
                cvs_product *= p

        match = (denom == cvs_product)
        results.append({
            'n': n,
            '2n': 2 * n,
            'B_2n': B2n,
            'denom': denom,
            'cvs_product': cvs_product,
            'dividing_primes': dividing_primes,
            'match': match,
        })
    return results


def _is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ============================================================================
# 14. Summary / diagnostic
# ============================================================================

def full_padic_analysis(p: int, c_val: int = 1, max_genus: int = 20, max_arity: int = 15) -> Dict:
    """Complete p-adic shadow obstruction tower analysis for given prime and central charge.

    Returns a comprehensive dict with all computed invariants.
    """
    # Genus expansion analysis
    genus_data = padic_genus_expansion_analysis(p, max_genus)

    # Shadow metric
    delta = virasoro_discriminant(Fraction(c_val))
    vp_delta = v_p_safe(delta, p)

    # Shadow obstruction tower
    tower = padic_virasoro_shadow_table(p, c_val, max_arity)

    # Tree-level tower
    tree_tower = padic_virasoro_tree_table(p, c_val, max_arity)

    # Kubota-Leopoldt data
    kl_data = kubota_leopoldt_interpolation_data(p, max_genus)

    # Iwasawa analysis
    iwasawa = iwasawa_lambda_analysis(p, max_genus)

    return {
        'p': p,
        'c': c_val,
        'kappa': float(Fraction(c_val) / 2),
        'Delta': float(delta),
        'v_p_Delta': vp_delta,
        'genus_expansion': genus_data,
        'shadow_tower': tower,
        'tree_tower': tree_tower,
        'kubota_leopoldt': kl_data,
        'iwasawa': iwasawa,
        'padic_radius_theoretical': p ** (1.0 / (p - 1)),
        'padic_radius_empirical': genus_data['radius'],
        'summary': (
            f"p-adic shadow obstruction tower for Virasoro at c={c_val}, p={p}.\n"
            f"  kappa = {c_val}/2 = {Fraction(c_val, 2)}\n"
            f"  Delta = {delta}, v_p(Delta) = {vp_delta}\n"
            f"  p-adic radius (theoretical): R_p = p^{{1/(p-1)}} = {p ** (1.0 / (p - 1)):.6f}\n"
            f"  p-adic radius (empirical): {genus_data['radius']:.6f}\n"
            f"  Iwasawa mu = {iwasawa['mu_shadow']}, lambda = {iwasawa['lambda_shadow']}\n"
        ),
    }
