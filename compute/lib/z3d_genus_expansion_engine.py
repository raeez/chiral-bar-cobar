"""
Z_{3d}(q) from genus expansion for chiral Koszul duality.

Computes the perturbative 3d gravity partition function via the genus expansion:

    log Z(gs, kappa) = sum_{g >= 0} F_g(kappa) * gs^{2g-2}

where:
    F_0 = 0                                         (regularized)
    F_1 = kappa / 24                                (one-loop)
    F_g = kappa * B_{2g} / (2g(2g-2))  for g >= 2  (Harer-Zagier)

and kappa = c/2 for Virasoro_c.  (UNIFORM-WEIGHT)

The BTZ partition function is:

    Z_BTZ(q) = prod_{n >= 2} 1/(1 - q^n)

whose q-expansion coefficients count partitions into parts >= 2.

References:
    [HZ86]  Harer-Zagier, "The Euler characteristic of the moduli space of curves",
            Invent. Math. 85 (1986), 457-485.
    [FP00]  Faber-Pandharipande, "Hodge integrals and moduli spaces of curves",
            RIMS Kokyuroku Bessatsu, 2000.
    [MW07]  Maloney-Witten, "Quantum gravity partition functions in three dimensions",
            JHEP 02 (2010) 029, arXiv:0712.0155.
    [DMPV11] Dijkgraaf-Maldacena-Papadodimas-Vafa, "Baby universes in string theory",
             Phys. Rev. D 73 (2006) 066002.
"""

from fractions import Fraction
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Bernoulli numbers (exact, standard convention: B_1 = -1/2)
# ---------------------------------------------------------------------------

def bernoulli_numbers(n: int) -> List[Fraction]:
    """Compute B_0, B_1, ..., B_n via the recursive definition.

    Uses: sum_{k=0}^{m} C(m+1, k) B_k = 0 for m >= 1, B_0 = 1.
    """
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        s = Fraction(0)
        for k in range(m):
            # binomial coefficient C(m+1, k)
            c = Fraction(1)
            for j in range(k):
                c = c * (m + 1 - j) / (j + 1)
            s += c * B[k]
        B[m] = -s / (m + 1)
    return B


# Precompute Bernoulli numbers up to B_40 (covers g up to 20)
_BERNOULLI_CACHE = bernoulli_numbers(40)


def bernoulli(n: int) -> Fraction:
    """Return the n-th Bernoulli number B_n (exact).

    Convention: B_1 = -1/2; B_{2k+1} = 0 for k >= 1.
    """
    if n < len(_BERNOULLI_CACHE):
        return _BERNOULLI_CACHE[n]
    # Extend cache if needed
    extended = bernoulli_numbers(n)
    return extended[n]


# ---------------------------------------------------------------------------
# Moduli space data
# ---------------------------------------------------------------------------

def harer_zagier_chi(g: int) -> Fraction:
    r"""Virtual (orbifold) Euler characteristic of M_g.

    For g >= 2:
        chi(M_g) = B_{2g} / (2g * (2g - 2))

    This is the Harer-Zagier formula [HZ86].  The sign alternates as
    (-1)^{g-1} since B_{2g} alternates in sign.

    For g = 1, chi(M_{1,1}) = -1/12 = -B_2/2; but the genus-1 free
    energy uses the separate convention F_1 = kappa/24 (see below).

    Raises ValueError for g < 2.
    """
    if g < 2:
        raise ValueError(
            f"harer_zagier_chi requires g >= 2; g=1 handled separately via F_1 = kappa/24"
        )
    return bernoulli(2 * g) / (2 * g * (2 * g - 2))


# ---------------------------------------------------------------------------
# Free energy coefficients
# ---------------------------------------------------------------------------

def free_energy_coefficient(g: int) -> Fraction:
    r"""The universal moduli coefficient b_g such that F_g(kappa) = kappa * b_g.

    (UNIFORM-WEIGHT: scalar formula, valid for all genera in the
    uniform-weight sector; see CLAUDE.md AP32.)

    Conventions:
        b_0 = 0                                      (regularized)
        b_1 = 1/24                                   (one-loop, eta function)
        b_g = B_{2g} / (2g * (2g - 2))  for g >= 2  (Harer-Zagier)

    The sign of b_g for g >= 2 alternates as (-1)^{g-1}.
    """
    if g < 0:
        raise ValueError(f"genus must be non-negative, got {g}")
    if g == 0:
        return Fraction(0)
    if g == 1:
        # F_1 = kappa/24 per CLAUDE.md C24 / AP120 sanity check.
        # VERIFIED: [DC] eta(tau) = q^{1/24} prod(1-q^n) gives 1/24 coefficient;
        #           [LT] Bershadsky-Cecotti-Ooguri-Vafa (1994), eq. (3.1).
        return Fraction(1, 24)
    return harer_zagier_chi(g)


def free_energy(g: int, kappa: Fraction) -> Fraction:
    r"""Genus-g free energy F_g(kappa) = kappa * b_g.

    (UNIFORM-WEIGHT)

    Parameters
    ----------
    g : int
        Genus (>= 0).
    kappa : Fraction
        The Koszul invariant kappa(A).  For Virasoro_c, kappa = c/2.
    """
    return kappa * free_energy_coefficient(g)


def virasoro_kappa(c: Fraction) -> Fraction:
    r"""kappa(Vir_c) = c/2.

    VERIFIED: [DC] C2 in CLAUDE.md true formula census;
              [LC] c=0 -> kappa=0; c=13 -> kappa=13/2 (self-dual).
    """
    return c / 2


# ---------------------------------------------------------------------------
# Genus expansion series
# ---------------------------------------------------------------------------

def log_z3d_coefficients(
    kappa: Fraction, num_terms: int = 10
) -> List[Fraction]:
    r"""Coefficients [F_0, F_1, ..., F_{num_terms-1}] of the genus expansion.

    log Z(gs, kappa) = sum_{g=0}^{num_terms-1} F_g(kappa) * gs^{2g-2}

    (UNIFORM-WEIGHT)
    """
    return [free_energy(g, kappa) for g in range(num_terms)]


def z3d_series(
    kappa: Fraction, num_terms: int = 10
) -> List[Fraction]:
    r"""First `num_terms` coefficients of Z_{3d} = exp(sum F_g gs^{2g-2}).

    We exponentiate the formal power series in gs^2 (ignoring the gs^{-2}
    divergent piece from F_0 = 0 and treating the gs^0 term from F_1 as
    the leading coefficient).

    Concretely, define the shifted series:
        S(x) = sum_{g >= 1} F_g * x^{g-1}    where x = gs^2
    so that log Z = gs^{-2} * F_0 + S(gs^2) = S(gs^2) since F_0 = 0.
    Then Z(x) = exp(S(x)) as a formal power series in x.

    Returns [Z_0, Z_1, ..., Z_{num_terms-1}] where Z(x) = sum Z_k x^k.
    """
    # Build the shifted log series: S_k = F_{k+1} for k = 0, 1, ..., num_terms-1
    S = [free_energy(g + 1, kappa) for g in range(num_terms)]

    # Exponentiate: Z = exp(S) via the standard recursive formula
    # Z_0 = exp(S_0) -- but S_0 = F_1 = kappa/24 is a Fraction, and exp is
    # transcendental.  For EXACT arithmetic we keep things formal:
    # if S_0 = 0, Z_0 = 1.  Otherwise we use the FORMAL exponential
    # where Z_0 = 1 (setting the overall normalization to 1, i.e., absorbing
    # exp(F_1) into the definition of Z).
    #
    # This is the standard convention: the genus expansion gives
    # Z_pert / Z_1-loop, and Z_1-loop = exp(F_1) is absorbed.
    #
    # ALTERNATIVE: keep Z_0 = exp(kappa/24) as a float.  For exact work
    # we use the formal version.
    #
    # We compute exp(S - S_0) * exp(S_0).  The formal part exp(S - S_0) is
    # exact (since S - S_0 has zero constant term).

    # Compute the perturbative correction: T(x) = S(x) - S(0), T_0 = 0
    T = [Fraction(0)] * num_terms
    for k in range(1, num_terms):
        T[k] = S[k]

    # exp(T) via recurrence: Z_0 = 1, Z_n = (1/n) sum_{k=1}^n k T_k Z_{n-k}
    Z = [Fraction(0)] * num_terms
    Z[0] = Fraction(1)
    for n in range(1, num_terms):
        s = Fraction(0)
        for k in range(1, n + 1):
            if k < num_terms:
                s += k * T[k] * Z[n - k]
        Z[n] = s / n

    return Z


# ---------------------------------------------------------------------------
# BTZ partition function
# ---------------------------------------------------------------------------

def btz_coefficients(num_terms: int = 30) -> List[Fraction]:
    r"""Coefficients of Z_BTZ(q) = prod_{n >= 2} 1/(1 - q^n).

    The coefficient of q^k counts the number of integer partitions of k
    into parts >= 2.

    VERIFIED: [DC] direct product expansion;
              [LT] OEIS A000041 minus partitions with 1s;
              [NE] first terms (1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, ...).
    """
    # Dynamic programming: partitions into parts >= 2
    dp = [Fraction(0)] * num_terms
    dp[0] = Fraction(1)
    for part in range(2, num_terms):
        for j in range(part, num_terms):
            dp[j] += dp[j - part]
    return dp


def btz_series(num_terms: int = 30) -> List[Fraction]:
    """Alias for btz_coefficients."""
    return btz_coefficients(num_terms)


# ---------------------------------------------------------------------------
# Ratio Z_{3d} / Z_BTZ
# ---------------------------------------------------------------------------

def ratio_series(
    kappa: Fraction, num_terms_z3d: int = 10, num_terms_btz: int = 30
) -> Tuple[List[Fraction], List[Fraction], List[Fraction]]:
    r"""Compute Z_{3d}, Z_BTZ, and their ratio as formal power series.

    The ratio is computed as a formal power series quotient up to
    min(num_terms_z3d, num_terms_btz) terms.

    Returns (z3d_coeffs, btz_coeffs, ratio_coeffs).

    Note: Z_{3d} is a series in x = gs^2 (coupling constant),
    while Z_BTZ is a series in q (modular parameter).  The comparison
    is meaningful when we identify the expansion parameter, which
    requires a choice of saddle point.  Here we compute both series
    and their formal ratio for structural comparison.
    """
    z3d = z3d_series(kappa, num_terms_z3d)
    btz = btz_coefficients(num_terms_btz)

    n = min(len(z3d), len(btz))
    # Formal power series division: R = Z3d / BTZ
    # R_0 = Z3d_0 / BTZ_0, R_n = (1/BTZ_0)(Z3d_n - sum_{k=1}^n BTZ_k R_{n-k})
    ratio = [Fraction(0)] * n
    if btz[0] == 0:
        raise ValueError("BTZ leading coefficient is zero; cannot divide")
    ratio[0] = z3d[0] / btz[0]
    for i in range(1, n):
        s = z3d[i] if i < len(z3d) else Fraction(0)
        for k in range(1, i + 1):
            if k < len(btz):
                s -= btz[k] * ratio[i - k]
        ratio[i] = s / btz[0]

    return z3d[:n], btz[:n], ratio


# ---------------------------------------------------------------------------
# Summary tables
# ---------------------------------------------------------------------------

def summary(c_values: Optional[List[int]] = None, num_genus: int = 10) -> str:
    """Print a summary table of genus expansion data for given central charges."""
    if c_values is None:
        c_values = [13, 26]

    lines = []
    for c in c_values:
        kappa = virasoro_kappa(Fraction(c))
        lines.append(f"=== Virasoro c = {c}, kappa = {kappa} ===")
        lines.append("")

        # Free energies
        lines.append("Genus expansion coefficients F_g(kappa) = kappa * b_g:")
        lines.append(f"  {'g':>3}  {'b_g':>25}  {'F_g':>25}  {'F_g (float)':>20}")
        for g in range(num_genus):
            bg = free_energy_coefficient(g)
            fg = free_energy(g, kappa)
            lines.append(f"  {g:>3}  {str(bg):>25}  {str(fg):>25}  {float(fg):>20.12e}")
        lines.append("")

        # Z_{3d} formal series
        z = z3d_series(kappa, num_genus)
        lines.append("Z_{3d} formal power series (perturbative, normalized Z_0 = 1):")
        for k in range(len(z)):
            lines.append(f"  x^{k}: {z[k]}  ({float(z[k]):.12e})")
        lines.append("")

    # BTZ
    btz = btz_coefficients(20)
    lines.append("BTZ partition function Z_BTZ(q) = prod_{n>=2} 1/(1-q^n):")
    for k in range(15):
        lines.append(f"  q^{k}: {btz[k]}")
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    print(summary())
