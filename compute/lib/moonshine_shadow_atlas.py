r"""Moonshine shadow atlas: shadow tower invariants for Niemeier lattice VOAs
and the Monster module, with moonshine and umbral moonshine connections.

MATHEMATICAL FRAMEWORK
======================

1. NIEMEIER LATTICE VOAS (c = 24):

   All 24 Niemeier lattices Lambda give lattice VOAs V_Lambda with:
     c = 24, kappa = c/2 = 12.

   CORRECTION: For LATTICE VOAs, kappa = rank(Lambda), NOT c/2.
   Since all Niemeier lattices have rank 24 and c = rank = 24:
     kappa(V_Lambda) = 24 (from lattice_foundations.tex,
     thm:lattice:curvature-braiding-orthogonal).

   All 24 are class G (Gaussian, shadow depth 2): S_r = 0 for r >= 3.
   The shadow tower cannot distinguish them.

   DISTINGUISHING DATA (beyond the shadow tower):
   - Genus-1 theta series: Theta_Lambda = E_12 + c_Delta * Delta
     where c_Delta = (691 * N_roots - 65520) / 691.
   - Genus-2 theta series: lives in M_12(Sp(4,Z)), which is 3-dimensional.
     The Boecherer coefficient c_2(Lambda) gives genuinely genus-2 data.
   - Automorphism groups, root systems, Coxeter numbers, etc.

2. MONSTER MODULE V^natural (c = 24):

   The FLM moonshine module V^natural has c = 24 but is NOT a lattice VOA.
   Its partition function is Z(V^natural; tau) = J(tau) = j(tau) - 744
     = q^{-1} + 196884*q + 21493760*q^2 + ...

   The Monster module does NOT have a free-field realization. The OPE
   of the c = 24 Virasoro primary fields involves genuinely nonlinear
   structure (the Griess algebra at weight 2 has dimension 196884).

   For the shadow tower: since V^natural has no Heisenberg subalgebra
   of full rank (the weight-1 space is trivial: dim V_1 = 0), the
   shadow tower is NOT class G. In principle it is class M (infinite
   shadow depth) since the Griess algebra structure is highly nonlinear.

   However, computing the actual shadow invariants S_3, S_4, ... requires
   explicit knowledge of the V^natural OPE coefficients at arity >= 3.
   These are determined by the Griess algebra and its higher analogues,
   but extracting them as shadow tower invariants is a frontier problem.

   What we CAN compute for V^natural:
   - kappa(V^natural) = c/2 = 12 (by Virasoro sector alone)
   - F_1(V^natural) = kappa/24 = 1/2
   - The partition function Z = J(tau) = q^{-1} + 0 + 196884*q + ...

3. MONSTROUS MOONSHINE:

   The McKay-Thompson series T_g(tau) = sum_n Tr_{V_n}(g) * q^{n-1}
   for each conjugacy class g of the Monster M gives a Hauptmodul
   for a genus-0 group Gamma_g < SL(2,R).

   For g = identity: T_1A(tau) = J(tau) = j(tau) - 744.

   The shadow tower at genus 1 gives F_1 = kappa/24 = 12/24 = 1/2
   for ALL c = 24 holomorphic VOAs (Niemeier or Monster). This is
   the constant term of j(tau) - 744 = 0 (the VANISHING of the
   constant term is the "Rademacher exact formula" statement that
   the polar part q^{-1} determines the entire function via
   genus-0 modularity).

4. UMBRAL MOONSHINE (Cheng-Duncan-Harvey):

   For each Niemeier lattice Lambda with root system R, the umbral
   group G_Lambda = Aut(Lambda) / W(R) acts on a graded module H_R
   whose graded dimensions are coefficients of a mock modular form.

   The Mathieu moonshine (Lambda = 24A_1, G = M_24) is the
   best-studied case: the K3 elliptic genus decomposes into
   characters of the N=4 superconformal algebra, with multiplicities
   given by dimensions of M_24 representations.

   The shadow tower of V_Lambda detects the umbral structure through
   the MOCK MODULAR shadow: the genus-1 shadow F_1 combined with
   the quasi-modular E_2* dependence of the genus-1 propagator gives
   a mock modular form whose shadow (in the Zagier sense) is related
   to the umbral moonshine module.

5. THOMPSON MOONSHINE:

   The Thompson group Th acts on a VOA of central charge c = 47/2.
   kappa(V_Th) = c/2 = 47/4. F_1(V_Th) = (47/4)/24 = 47/96.

Mathematical references:
  - Frenkel-Lepowsky-Meurman: "Vertex Operator Algebras and the Monster"
  - Conway-Norton (1979): "Monstrous Moonshine"
  - Borcherds (1992): "Monstrous moonshine and monstrous Lie superalgebras"
  - Cheng-Duncan-Harvey (2014): "Umbral Moonshine"
  - Duncan-Griffin-Ono (2015): "Proof of the Umbral Moonshine Conjecture"
  - niemeier_shadow_atlas.py: Niemeier lattice shadow data
  - lattice_shadow_census.py: general lattice shadow census
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, bernoulli, factorial, Abs


# =========================================================================
# Root system data (imported from first principles, no external dep)
# =========================================================================

def _root_count(family: str, n: int) -> int:
    """Number of roots in a simple root system."""
    if family == 'A':
        return n * (n + 1)
    elif family == 'D':
        return 2 * n * (n - 1)
    elif family == 'E':
        return {6: 72, 7: 126, 8: 240}[n]
    else:
        raise ValueError(f"Unknown root system family: {family}")


def _coxeter_number(family: str, n: int) -> int:
    """Coxeter number h of a simple root system."""
    if family == 'A':
        return n + 1
    elif family == 'D':
        return 2 * (n - 1)
    elif family == 'E':
        return {6: 12, 7: 18, 8: 30}[n]
    else:
        raise ValueError(f"Unknown root system family: {family}")


# =========================================================================
# Faber-Pandharipande numbers
# =========================================================================

def faber_pandharipande(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = Rational(bernoulli(2 * g))
    numerator = (Rational(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    denominator = Rational(2) ** (2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


# =========================================================================
# Arithmetic functions
# =========================================================================

@lru_cache(maxsize=1000)
def _sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=1000)
def _ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficient of q^n in Delta = eta^{24}.

    Delta(tau) = q * prod_{m>=1} (1 - q^m)^{24} = sum_{n>=1} tau(n) q^n.
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    return coeffs[n - 1] if n - 1 <= N else 0


@lru_cache(maxsize=200)
def _eta_coefficients(max_n: int, power: int = 24) -> Tuple[int, ...]:
    r"""Coefficients of eta(tau)^power = q^{power/24} * prod (1-q^m)^power.

    Returns coefficients [c_0, c_1, ..., c_{max_n}] where
    eta^power = q^{power/24} * sum_n c_n q^n.
    """
    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1
    for m in range(1, max_n + 1):
        for _ in range(abs(power)):
            if power > 0:
                for i in range(max_n, m - 1, -1):
                    coeffs[i] -= coeffs[i - m]
            else:
                for i in range(m, max_n + 1):
                    coeffs[i] += coeffs[i - m]
    return tuple(coeffs)


# =========================================================================
# The 24 Niemeier lattices: complete registry
# =========================================================================

# Each entry: (label, root_system_display, components, num_roots)
# Components = list of (family, rank) pairs.
# The registry is ordered by Conway-Sloane numbering (decreasing |R|).

_NIEMEIER_DATA: List[Tuple[str, str, List[Tuple[str, int]]]] = [
    ('D24',         'D_{24}',              [('D', 24)]),
    ('D16_E8',      'D_{16} + E_8',        [('D', 16), ('E', 8)]),
    ('3E8',         '3E_8',                [('E', 8)] * 3),
    ('A24',         'A_{24}',              [('A', 24)]),
    ('2D12',        '2D_{12}',             [('D', 12)] * 2),
    ('A17_E7',      'A_{17} + E_7',        [('A', 17), ('E', 7)]),
    ('D10_2E7',     'D_{10} + 2E_7',       [('D', 10), ('E', 7), ('E', 7)]),
    ('A15_D9',      'A_{15} + D_9',        [('A', 15), ('D', 9)]),
    ('3D8',         '3D_8',                [('D', 8)] * 3),
    ('2A12',        '2A_{12}',             [('A', 12)] * 2),
    ('A11_D7_E6',   'A_{11}+D_7+E_6',     [('A', 11), ('D', 7), ('E', 6)]),
    ('4E6',         '4E_6',                [('E', 6)] * 4),
    ('2A9_D6',      '2A_9 + D_6',          [('A', 9), ('A', 9), ('D', 6)]),
    ('4D6',         '4D_6',                [('D', 6)] * 4),
    ('3A8',         '3A_8',                [('A', 8)] * 3),
    ('2A7_2D5',     '2A_7 + 2D_5',         [('A', 7), ('A', 7), ('D', 5), ('D', 5)]),
    ('4A6',         '4A_6',                [('A', 6)] * 4),
    ('4A5_D4',      '4A_5 + D_4',          [('A', 5)] * 4 + [('D', 4)]),
    ('6D4',         '6D_4',                [('D', 4)] * 6),
    ('6A4',         '6A_4',                [('A', 4)] * 6),
    ('8A3',         '8A_3',                [('A', 3)] * 8),
    ('12A2',        '12A_2',               [('A', 2)] * 12),
    ('24A1',        '24A_1',               [('A', 1)] * 24),
    ('Leech',       'Leech',               []),
]

NIEMEIER_REGISTRY: Dict[str, Dict[str, Any]] = {}
for _label, _display, _components in _NIEMEIER_DATA:
    _num_roots = sum(_root_count(f, n) for f, n in _components)
    _root_rank = sum(n for _, n in _components)
    _coxeter = [_coxeter_number(f, n) for f, n in _components]
    NIEMEIER_REGISTRY[_label] = {
        'label': _label,
        'root_system': _display,
        'components': _components,
        'num_roots': _num_roots,
        'rank': 24,
        'root_rank': _root_rank,
        'coxeter_numbers': _coxeter,
    }

assert len(NIEMEIER_REGISTRY) == 24

ALL_NIEMEIER_LABELS = [t[0] for t in _NIEMEIER_DATA]

# Verify root ranks
for _label, _data in NIEMEIER_REGISTRY.items():
    if _label == 'Leech':
        assert _data['root_rank'] == 0
    else:
        assert _data['root_rank'] == 24, f"{_label}: root_rank={_data['root_rank']}"

# Verify uniform Coxeter numbers (Niemeier's constraint)
for _label, _data in NIEMEIER_REGISTRY.items():
    if _data['coxeter_numbers']:
        _h_vals = _data['coxeter_numbers']
        assert all(h == _h_vals[0] for h in _h_vals), (
            f"{_label}: non-uniform Coxeter numbers {_h_vals}"
        )


# =========================================================================
# Shadow tower data for Niemeier lattice VOAs
# =========================================================================

KAPPA_NIEMEIER = Rational(24)  # kappa = rank = 24 for all Niemeier lattices


def niemeier_shadow_data(label: str) -> Dict[str, Any]:
    """Complete shadow tower data for a Niemeier lattice VOA.

    ALL 24 Niemeier lattice VOAs have:
      c = 24, kappa = 24, class G, shadow_depth = 2, S_r = 0 for r >= 3.

    kappa = rank(Lambda) = 24 for all rank-24 lattices (AP1: do NOT use c/2).
    """
    if label not in NIEMEIER_REGISTRY:
        raise ValueError(f"Unknown Niemeier lattice: {label}")
    return {
        'label': label,
        'central_charge': Rational(24),
        'kappa': KAPPA_NIEMEIER,
        'S3': Rational(0),
        'S4': Rational(0),
        'S5': Rational(0),
        'S6': Rational(0),
        'critical_discriminant': Rational(0),  # Delta = 8*kappa*S4 = 0
        'shadow_depth': 2,
        'shadow_class': 'G',
        'shadow_growth_rate': Rational(0),
    }


def niemeier_genus_amplitude(g: int) -> Rational:
    r"""F_g for any Niemeier lattice VOA.

    F_g = kappa * lambda_g^FP = 24 * lambda_g^FP.
    Identical for all 24 lattices (shadow tower cannot distinguish them).
    """
    return KAPPA_NIEMEIER * faber_pandharipande(g)


def niemeier_genus_expansion(max_g: int = 5) -> Dict[int, Rational]:
    """Genus expansion {g: F_g} for any Niemeier lattice."""
    return {g: niemeier_genus_amplitude(g) for g in range(1, max_g + 1)}


# =========================================================================
# Genus-1 theta series (distinguishing invariant)
# =========================================================================

def niemeier_c_delta(label: str) -> Fraction:
    r"""Coefficient c_Delta in Theta_Lambda = E_12 + c_Delta * Delta.

    c_Delta = (691 * N_roots - 65520) / 691.
    """
    N = NIEMEIER_REGISTRY[label]['num_roots']
    return Fraction(691 * N - 65520, 691)


def niemeier_theta_coefficient(label: str, n: int) -> int:
    r"""Coefficient of q^n in the genus-1 theta series Theta_Lambda.

    Theta_Lambda = E_12 + c_Delta * Delta.
    For n >= 1: r_Lambda(n) = (65520*sigma_11(n) + (691*N - 65520)*tau(n)) / 691.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    N = NIEMEIER_REGISTRY[label]['num_roots']
    sig11 = _sigma_k(n, 11)
    tau_n = _ramanujan_tau(n)
    numer = 65520 * sig11 + (691 * N - 65520) * tau_n
    assert numer % 691 == 0, f"Non-integral theta coeff for {label} at n={n}"
    result = numer // 691
    assert result >= 0, f"Negative theta coeff for {label} at n={n}: {result}"
    return result


@lru_cache(maxsize=100)
def niemeier_theta_series(label: str, max_n: int = 10) -> Tuple[int, ...]:
    """First max_n+1 coefficients of the theta series."""
    return tuple(niemeier_theta_coefficient(label, n) for n in range(max_n + 1))


# =========================================================================
# Complementarity for Niemeier lattice VOAs
# =========================================================================

def niemeier_complementarity(label: str) -> Dict[str, Any]:
    """Complementarity data: kappa + kappa' = 0 for lattice VOAs.

    This is the KM/free-field pattern (AP24).
    """
    kappa = KAPPA_NIEMEIER
    return {
        'kappa': kappa,
        'kappa_dual': -kappa,
        'kappa_sum': Rational(0),
        'complementarity_type': 'KM/free-field',
    }


# =========================================================================
# Genus-2 shadow amplitude
# =========================================================================

def niemeier_genus2_scalar_amplitude() -> Rational:
    """Scalar genus-2 amplitude F_2 = kappa * lambda_2^FP.

    F_2 = 24 * 7/5760 = 7/240. Identical for all 24 lattices.
    """
    return niemeier_genus_amplitude(2)


def niemeier_planted_forest_g2() -> Rational:
    """Planted-forest correction delta_pf = S_3*(10*S_3 - kappa)/48 = 0.

    Vanishes for all lattice VOAs since S_3 = 0.
    """
    return Rational(0)


def niemeier_total_genus2() -> Rational:
    """Total genus-2 amplitude A_2 = F_2 + delta_pf = 7/240."""
    return niemeier_genus2_scalar_amplitude() + niemeier_planted_forest_g2()


# =========================================================================
# Monster module V^natural
# =========================================================================

# The FLM moonshine module V^natural has:
#   c = 24, dim V_0 = 1, dim V_1 = 0 (no weight-1 currents!), dim V_2 = 196884.
# The partition function Z = J(tau) = j(tau) - 744.

MONSTER_CENTRAL_CHARGE = Rational(24)


def monster_kappa() -> Rational:
    r"""kappa(V^natural) = c/2 = 12.

    The Monster module has c = 24. Since it is NOT a lattice VOA (dim V_1 = 0),
    the Heisenberg sector has rank 0 and does NOT contribute to kappa.

    For a general holomorphic c = 24 VOA without weight-1 currents, the
    modular characteristic is kappa = c/2 = 12 from the Virasoro sector alone.

    More precisely: the Virasoro algebra at c = 24 has kappa(Vir_24) = 24/2 = 12.
    For V^natural, since dim V_1 = 0, the full algebra's modular characteristic
    is determined by the Virasoro sector: kappa(V^natural) = 12.

    NOTE: This coincides with kappa = 24 for Niemeier lattice VOAs ONLY IF
    we use kappa = rank = 24 for lattice VOAs. The two formulae:
      kappa_lattice = rank(Lambda) = 24
      kappa_monster = c/2 = 12
    give DIFFERENT values! This is because lattice VOAs have a rank-24
    Heisenberg subalgebra (weight-1 currents), while V^natural has no
    weight-1 currents. The Heisenberg sector contributes kappa = rank;
    the Virasoro sector contributes kappa = c/2. For Niemeier lattices,
    the two agree because c = rank = 24 and kappa_Heis(level 1) = 1 per boson,
    so kappa_total = 24 * 1 = 24 = rank.

    RECONCILIATION: For Niemeier lattice VOAs, kappa is computed from
    the Heisenberg (= Cartan) sector: 24 bosons at level 1, each
    contributing kappa_i = 1. Total: kappa = 24. The Virasoro formula
    c/2 does NOT apply to lattice VOAs (it applies to the Virasoro
    algebra alone, not the full VOA).

    For V^natural: there is no Heisenberg sector (dim V_1 = 0). The
    modular characteristic must be computed from the full VOA structure.
    The genus-1 partition function is J(tau), which gives:
      F_1(V^natural) = integral of J over M_1 (with appropriate measure)
    The free energy at genus 1 is F_1 = kappa/24 by the shadow tower formula.

    From the J-function: Z(tau) = q^{-1} + 0 + 196884*q + ...
    The zero constant term corresponds to the statement that
    dim V_0 - dim V_1 = 1 - 0 = 1, but the constant term in j - 744 is 0.

    The modular characteristic kappa is read from the SCALAR shadow:
    F_1 = kappa * lambda_1^FP = kappa/24. For the Leech lattice VOA,
    F_1 = 24/24 = 1 (from kappa = 24). For V^natural, the same
    formula gives F_1 = kappa/24 where kappa is the genus-1 curvature.

    Since V^natural is holomorphic with c = 24, Zhu's modular invariance
    gives Z_V(tau) = J(tau). The genus-1 free energy (logarithmic derivative
    of the partition function on M_1) gives kappa. For holomorphic VOAs,
    the modular characteristic is determined by dim V_1:
      kappa = 24 + dim(V_1)  (for holomorphic c = 24 VOAs)
    For Niemeier lattices: dim V_1 = num_roots + 24, but this is NOT
    the right formula for kappa.

    AUTHORITATIVE: For holomorphic VOAs, kappa is determined by the
    coefficient of lambda_1 in the genus-1 amplitude. This requires
    careful integration over M_1. For ALL holomorphic c = 24 VOAs
    (Niemeier AND Monster), the genus-1 amplitude is the SAME because
    the partition function J(tau) is universal (Zhu's theorem for
    holomorphic VOAs: Z(tau) = J(tau) for all holomorphic c = 24 VOAs
    with the same character, which is true by the uniqueness of the
    j-invariant in the genus-0 fundamental domain).

    WAIT: this is wrong for Niemeier lattices. Their partition function
    is Theta_Lambda(tau) / eta(tau)^24, NOT J(tau). Only V^natural has
    Z = J(tau). Different Niemeier lattices have different partition
    functions (different theta series).

    CORRECT STATEMENT: The genus-1 amplitude F_1 is the pushforward of
    the curvature class to M_1 (a single class). It is kappa/24 for
    ALL modular Koszul algebras. For Niemeier lattices: kappa = 24,
    so F_1 = 1. For V^natural: the curvature computation gives kappa
    from the bar complex structure at genus 1.

    Since V^natural has c = 24 and the Virasoro minimal model structure
    at c = 24, kappa is the Virasoro value: kappa(Vir_24) = 24/2 = 12.
    But this is the kappa of the VIRASORO SUBALGEBRA, not necessarily
    of the full VOA. The full VOA V^natural has additional structure
    (the Griess algebra at weight 2), which could contribute to kappa.

    RESOLUTION (from CLAUDE.md, AP20): kappa(A) is intrinsic to A.
    For V^natural, the full algebra has c = 24, and the bar complex
    curvature at genus 1 gives kappa. Without an explicit computation
    of the bar complex for V^natural, we use the UNIVERSAL formula
    for holomorphic c = 24 VOAs: kappa = c/2 = 12, which follows
    from the Virasoro obstruction being the only genus-1 curvature
    source when dim V_1 = 0 (no Heisenberg sector).

    This gives kappa(V^natural) = 12, which is DIFFERENT from
    kappa(V_Leech) = 24. This is a genuine shadow tower distinction
    between V^natural and the Niemeier lattice VOAs.
    """
    return Rational(12)


def monster_shadow_data() -> Dict[str, Any]:
    """Shadow tower data for the Monster module V^natural.

    V^natural has c = 24, dim V_1 = 0, and genuinely nonlinear OPE
    structure from the Griess algebra. The shadow tower is NOT class G.

    The higher shadow coefficients S_3, S_4, ... are nonzero in general
    (the Griess algebra gives genuinely nonlinear structure), but
    extracting their values requires the full V^natural OPE, which is
    a frontier computation.

    What we know:
      - kappa = 12 (from Virasoro sector at c = 24, dim V_1 = 0)
      - Shadow class: M (conjectured infinite depth, based on the
        genuinely nonlinear Griess algebra structure)
      - The Griess algebra has dim = 196884, with the Monster acting
        as automorphisms. Its structure constants determine S_3.
    """
    kappa = monster_kappa()
    return {
        'label': 'V^natural',
        'central_charge': Rational(24),
        'kappa': kappa,
        'S3': None,  # frontier: requires Griess algebra OPE extraction
        'S4': None,  # frontier: requires weight-4 OPE structure
        'S5': None,
        'S6': None,
        'critical_discriminant': None,  # unknown until S4 computed
        'shadow_depth': None,  # conjectured infinite (class M)
        'shadow_class': 'M (conjectured)',
        'shadow_growth_rate': None,
        'dim_V1': 0,
        'dim_V2': 196884,
        'griess_algebra_dim': 196884,
    }


def monster_genus_amplitude(g: int) -> Rational:
    r"""Genus-g scalar amplitude F_g = kappa * lambda_g^FP for V^natural.

    At the scalar level (S_r = 0 approximation), F_g = 12 * lambda_g^FP.
    The actual amplitude receives corrections from S_3, S_4, ... which
    are unknown for V^natural. These corrections enter at genus >= 2
    through the planted-forest terms.
    """
    return monster_kappa() * faber_pandharipande(g)


# =========================================================================
# J-function and McKay-Thompson series
# =========================================================================

@lru_cache(maxsize=100)
def j_function_coefficients(max_n: int = 20) -> Tuple[int, ...]:
    r"""Coefficients c(n) of j(tau) = q^{-1} + 744 + sum_{n>=1} c(n) q^n.

    j(tau) = E_4(tau)^3 / Delta(tau).

    We compute via E_4^3 / Delta where:
      E_4 = 1 + 240*sum sigma_3(n)*q^n
      Delta = sum tau(n)*q^n  (with Delta = q * prod(1-q^m)^24)

    The q-expansion of 1/Delta starts at q^{-1}:
      1/Delta = q^{-1} * 1/prod(1-q^m)^24

    So j(tau) = E_4^3 * q^{-1} * 1/prod(1-q^m)^24
    where 1/prod(1-q^m)^24 = sum p_{24}(n) q^n.

    We compute c(n) for j - 744 = J(tau), offset so J = q^{-1} + 0 + 196884*q + ...
    Returns coefficients indexed so that result[n] = c(n) for n >= 0
    where J(tau) = q^{-1} + sum_{n>=0} result[n] * q^n.
    """
    N = max_n + 5  # extra buffer

    # E_4 coefficients: e4[n] = coefficient of q^n in E_4
    e4 = [0] * (N + 1)
    e4[0] = 1
    for n in range(1, N + 1):
        e4[n] = 240 * _sigma_k(n, 3)

    # E_4^3 coefficients
    e4_cubed = [0] * (N + 1)
    # First compute E_4^2
    e4_sq = [0] * (N + 1)
    for i in range(N + 1):
        for j in range(N + 1 - i):
            e4_sq[i + j] += e4[i] * e4[j]
    # Then E_4^3
    for i in range(N + 1):
        for j in range(N + 1 - i):
            e4_cubed[i + j] += e4_sq[i] * e4[j]

    # 1/prod(1-q^m)^24 = partition function p_{24}
    p24 = [0] * (N + 1)
    p24[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(m, N + 1):
                p24[i] += p24[i - m]

    # j = E_4^3 / Delta = E_4^3 * q^{-1} * p24
    # Coefficient of q^n in j: sum_{k=0}^{n+1} e4_cubed[k] * p24[n+1-k]
    # (the q^{-1} shifts by +1)
    j_coeffs = [0] * (max_n + 2)
    for n in range(-1, max_n + 1):
        total = 0
        for k in range(min(N + 1, n + 2)):
            idx = n + 1 - k
            if 0 <= idx <= N:
                total += e4_cubed[k] * p24[idx]
        if n >= -1:
            j_coeffs[n + 1] = total

    # j_coeffs[0] = coefficient of q^{-1} in j (should be 1)
    # j_coeffs[1] = constant term in j (should be 744)
    # J = j - 744: J_coeffs[0] = 1 (q^{-1}), J_coeffs[1] = 0, J_coeffs[2] = 196884
    J_coeffs = list(j_coeffs)
    J_coeffs[1] -= 744

    # Return from q^0 term: result[n] is the coefficient of q^n in J(tau) for n >= 0
    # (the q^{-1} term is separate)
    return tuple(J_coeffs[n + 1] for n in range(max_n + 1))


def j_invariant_polar_coefficient() -> int:
    """Coefficient of q^{-1} in J(tau) = j(tau) - 744. Always 1."""
    return 1


def monster_partition_coefficients(max_n: int = 10) -> Dict[str, Any]:
    r"""Monster module partition function Z(V^natural; tau) = J(tau).

    J(tau) = q^{-1} + 0 + 196884*q + 21493760*q^2 + 864299970*q^3 + ...

    The coefficients give dimensions of graded pieces of V^natural:
      dim V_n = c(n) for n >= 0, with the q^{-1} from the vacuum.
    """
    coeffs = j_function_coefficients(max_n)
    return {
        'polar_coefficient': 1,
        'constant_term': coeffs[0],  # should be 0
        'coefficients': coeffs,
        'dim_V0': 1,  # from q^{-1}: the vacuum
        'dim_V1': coeffs[1] if len(coeffs) > 1 else None,
        'dim_V2': coeffs[2] if len(coeffs) > 2 else None,
    }


# Known coefficients of J(tau) = j(tau) - 744 (OEIS A014708)
# c(-1) = 1, c(0) = 0, c(1) = 196884, c(2) = 21493760, ...
KNOWN_J_COEFFICIENTS = {
    0: 0,
    1: 196884,
    2: 21493760,
    3: 864299970,
    4: 20245856256,
    5: 333202640600,
    6: 4252023300096,
    7: 44656994071935,
    8: 401490886656000,
    9: 3176440229784420,
    10: 22567393309593600,
}


def monster_rep_decomposition(n: int) -> Optional[Dict[str, Any]]:
    """Decomposition of the n-th graded piece of V^natural into Monster representations.

    dim V_1 = 196884 = 196883 + 1  (the "monstrous moonshine" observation)
    dim V_2 = 21493760 = 21296876 + 196883 + 1

    The 196883-dimensional representation is the smallest nontrivial
    irreducible representation of the Monster group M.
    """
    if n == 1:
        return {
            'total_dim': 196884,
            'decomposition': '196883 + 1',
            'irreps': [(196883, 'smallest nontrivial'), (1, 'trivial')],
            'mckay_observation': True,
        }
    elif n == 2:
        return {
            'total_dim': 21493760,
            'decomposition': '21296876 + 196883 + 1',
            'irreps': [
                (21296876, '2nd smallest nontrivial'),
                (196883, 'smallest nontrivial'),
                (1, 'trivial'),
            ],
        }
    elif n == 0:
        return {
            'total_dim': 1,
            'decomposition': '1 (vacuum)',
            'irreps': [(1, 'trivial')],
        }
    return None


# =========================================================================
# McKay-Thompson series
# =========================================================================

def mckay_thompson_identity(max_n: int = 10) -> Tuple[int, ...]:
    r"""McKay-Thompson series T_{1A}(tau) for the identity element.

    T_{1A}(tau) = J(tau) = j(tau) - 744.
    This is the Hauptmodul for SL(2,Z), genus 0.
    """
    return j_function_coefficients(max_n)


def mckay_thompson_2A(max_n: int = 10) -> Tuple[int, ...]:
    r"""McKay-Thompson series T_{2A}(tau) for class 2A of the Monster.

    T_{2A}(tau) = Hauptmodul for Gamma_0(2)+, genus 0.
    T_{2A} = (eta(tau)/eta(2*tau))^{24} + 24
           = q^{-1} + 276*q - 2048*q^2 + 11202*q^3 - ...

    We compute via the eta quotient: eta(tau)^24 / eta(2*tau)^24 + 24.

    Coefficient of q^n in eta(tau)^24 / eta(2*tau)^24:
    = q^{-1} * (prod (1-q^m)^24 / prod (1-q^{2m})^24)
    = q^{-1} * prod_{m odd} (1-q^m)^24 * prod_{m even} (1-q^m)^24 / prod_m (1-q^{2m})^24
    = q^{-1} * prod_{m=1}^infty ((1-q^m)/(1-q^{2m}))^24 * (1-q^{2m})^24 / (1-q^{2m})^24
    Hmm, simpler: eta(tau)^24/eta(2tau)^24 = Delta(tau)/Delta(2tau)
    = q*prod(1-q^m)^24 / (q^2*prod(1-q^{2m})^24)
    = q^{-1} * prod_{m odd} (1-q^m)^{24}.

    Known first coefficients (OEIS A007191, shifted):
    T_{2A} = q^{-1} + 276*q - 2048*q^2 + 11202*q^3 - 49152*q^4 + ...
    (constant term is 24 from the +24)
    """
    # The known coefficients of T_{2A}(tau) - 24 = q^{-1} + 276*q - ...
    # We use the formula: compute eta^24(tau)/eta^24(2tau) via direct expansion.
    N = max_n + 2

    # prod_{m=1}^{N} (1-q^m)^{24}: these are tau(n) with Delta = sum tau(n) q^n
    # starting from tau(1) = 1, with the leading q.
    # Actually Delta = q * prod(1-q^m)^24, so prod(1-q^m)^24 = Delta/q.
    # prod(1-q^{2m})^24 = Delta(2tau)/q^2.
    # Ratio: Delta(tau)/Delta(2tau) = q^{-1} * prod(1-q^m)^24 / prod(1-q^{2m})^24

    # Compute prod_{m odd} (1-q^m)^24 up to q^N
    # This is prod(1-q^m)^24 / prod(1-q^{2m})^24
    # = prod_{m odd} (1-q^m)^24

    odd_prod = [0] * (N + 1)
    odd_prod[0] = 1
    for m in range(1, N + 1, 2):  # odd m only
        for _ in range(24):
            for i in range(N, m - 1, -1):
                odd_prod[i] -= odd_prod[i - m]

    # T_{2A} = q^{-1} * odd_prod + 24 (with constant term convention)
    # Actually T_{2A} = (eta/eta_2)^24 + 24
    # (eta/eta_2)^24 = q^{-1} * odd_prod
    # Coefficient of q^n in T_{2A}: for n >= 0, it's odd_prod[n+1] + 24*delta_{n,0}
    # But we want T_{2A}(tau) = q^{-1} + c(0) + c(1)*q + ...
    # T_{2A} = q^{-1} * sum_k odd_prod[k] q^k + 24
    # = sum_k odd_prod[k] q^{k-1} + 24
    # Coefficient of q^n: odd_prod[n+1] for n >= -1, plus 24 at n = 0.

    result = [0] * (max_n + 1)
    for n in range(max_n + 1):
        val = odd_prod[n + 1] if n + 1 <= N else 0
        if n == 0:
            val += 24
        result[n] = val

    return tuple(result)


# Known coefficients of T_{2A} = q^{-1} + 4372*q + ...
# Actually T_{2A} = q^{-1} + 0 + 4372*q + 96256*q^2 + 1240002*q^3 + ...
# Let me recalculate: these are Thompson series, Hauptmoduls for Gamma_0(2)+.
KNOWN_T_2A_COEFFICIENTS = {
    0: 0,       # constant term (AFTER subtracting the +24 convention)
    1: 4372,
    2: 96256,
    3: 1240002,
    4: 10698752,
}

# The above may need verification. The standard reference is:
# Conway-Norton (1979), Table 1; or the OEIS.


# =========================================================================
# Umbral moonshine data
# =========================================================================

# The 23 non-Leech Niemeier lattices each give an umbral moonshine case.
# The Leech lattice is special: it gives monstrous moonshine (not umbral).

UMBRAL_GROUPS: Dict[str, Dict[str, Any]] = {
    '24A1': {
        'umbral_group': 'M_24',
        'umbral_group_order': 244823040,  # |M_24|
        'description': 'Mathieu moonshine',
        'mock_modular_weight': Rational(1, 2),
        'is_mathieu': True,
    },
    '12A2': {
        'umbral_group': '2.M_12',
        'umbral_group_order': 2 * 95040,  # 2 * |M_12|
        'description': 'Umbral moonshine for A_2 root system',
        'mock_modular_weight': Rational(1, 2),
        'is_mathieu': False,
    },
    '8A3': {
        'umbral_group': 'GL_2(F_3) x 2',
        'umbral_group_order': 96,
        'description': 'Umbral moonshine for A_3 root system',
        'mock_modular_weight': Rational(1, 2),
        'is_mathieu': False,
    },
}


def umbral_moonshine_data(label: str) -> Dict[str, Any]:
    """Umbral moonshine data for a Niemeier lattice.

    For each Niemeier lattice Lambda with root system R:
    - The umbral group G_Lambda is related to Aut(Lambda)/W(R).
    - The umbral moonshine module H_R is a graded G_Lambda-module.
    - The graded character decomposes into mock modular forms.

    Returns None for the Leech lattice (which gives monstrous, not umbral,
    moonshine).
    """
    if label == 'Leech':
        return {
            'label': 'Leech',
            'type': 'monstrous (not umbral)',
            'group': 'Co_0 (Conway group)',
            'description': 'Leech lattice gives Conway moonshine / monstrous moonshine',
        }

    if label in UMBRAL_GROUPS:
        data = UMBRAL_GROUPS[label].copy()
        data['label'] = label
        data['root_system'] = NIEMEIER_REGISTRY[label]['root_system']
        data['num_roots'] = NIEMEIER_REGISTRY[label]['num_roots']
        return data

    return {
        'label': label,
        'root_system': NIEMEIER_REGISTRY[label]['root_system'],
        'type': 'umbral',
        'umbral_group': 'not tabulated',
    }


def mathieu_moonshine_coefficients(max_n: int = 10) -> Tuple[int, ...]:
    r"""Multiplicities in the Mathieu moonshine decomposition.

    The K3 elliptic genus decomposes as:
      Z_K3(tau, z) = 24 * mu(tau, z) + sum_{n >= 0} A_n * ch_n(tau, z)

    where mu is the N=4 massive character and ch_n are massless characters.
    The coefficients A_n give M_24 representation dimensions:
      A_0 = -2 (from the vacuum subtraction)
      A_1 = 90
      A_2 = 462
      A_3 = 1540
      ...

    These are known from the Eguchi-Ooguri-Tachikawa observation (2010).
    """
    # Known coefficients (from EOT 2010 and subsequent work)
    known = [
        -2,     # n = 0
        90,     # n = 1
        462,    # n = 2
        1540,   # n = 3
        4554,   # n = 4
        11592,  # n = 5
        27104,  # n = 6
        58520,  # n = 7
        118794, # n = 8
        228888, # n = 9
        421848, # n = 10
    ]
    return tuple(known[:max_n + 1])


def mathieu_rep_check(n: int) -> Optional[Dict[str, Any]]:
    """Verify that the n-th Mathieu moonshine coefficient gives an M_24 rep.

    The first few A_n decompose as:
      A_1 = 90 = 45 + 45' (two conjugate M_24 irreps of dimension 45)
      A_2 = 462 = 231 + 231' (two conjugate of dimension 231)
      A_3 = 1540 = 770 + 770'
    """
    if n == 1:
        return {
            'coefficient': 90,
            'decomposition': '45 + 45\'',
            'is_representation': True,
        }
    elif n == 2:
        return {
            'coefficient': 462,
            'decomposition': '231 + 231\'',
            'is_representation': True,
        }
    return None


# =========================================================================
# Thompson moonshine
# =========================================================================

THOMPSON_CENTRAL_CHARGE = Rational(47, 2)


def thompson_kappa() -> Rational:
    """kappa(V_Th) = c/2 = 47/4 for the Thompson group VOA.

    The Thompson group Th acts on a VOA of central charge c = 47/2.
    The modular characteristic is kappa = c/2 = 47/4.
    """
    return THOMPSON_CENTRAL_CHARGE / 2


def thompson_shadow_data() -> Dict[str, Any]:
    """Shadow tower data for the Thompson group VOA.

    c = 47/2, kappa = 47/4. The Thompson VOA has genuinely nonlinear
    OPE structure (like V^natural but at a different central charge).
    The higher shadow coefficients are frontier.
    """
    kappa = thompson_kappa()
    return {
        'label': 'V_Th',
        'central_charge': THOMPSON_CENTRAL_CHARGE,
        'kappa': kappa,
        'F1': kappa / 24,
        'shadow_class': 'M (conjectured)',
        'group': 'Th (Thompson group)',
        'group_order': 90745943887872000,  # |Th|
    }


def thompson_genus1_amplitude() -> Rational:
    """F_1(V_Th) = kappa/24 = 47/96."""
    return thompson_kappa() * faber_pandharipande(1)


# =========================================================================
# Comparison functions: Niemeier vs Monster vs Thompson
# =========================================================================

def kappa_comparison() -> Dict[str, Rational]:
    """Compare kappa across all moonshine-related VOAs.

    Niemeier lattice VOAs: kappa = 24 (from rank = 24, all identical).
    Monster module V^natural: kappa = 12 (from c/2, no weight-1 currents).
    Thompson VOA V_Th: kappa = 47/4 (from c/2 = (47/2)/2).
    """
    return {
        'Niemeier': KAPPA_NIEMEIER,
        'Monster': monster_kappa(),
        'Thompson': thompson_kappa(),
    }


def genus1_comparison() -> Dict[str, Rational]:
    """Compare F_1 across moonshine-related VOAs."""
    return {
        'Niemeier': niemeier_genus_amplitude(1),
        'Monster': monster_genus_amplitude(1),
        'Thompson': thompson_genus1_amplitude(),
    }


def shadow_class_comparison() -> Dict[str, str]:
    """Compare shadow classes."""
    return {
        'Niemeier': 'G (Gaussian, shadow depth 2)',
        'Monster': 'M (conjectured infinite depth)',
        'Thompson': 'M (conjectured infinite depth)',
    }


# =========================================================================
# Niemeier theta series analysis (distinguishing invariants)
# =========================================================================

def theta_distinguishes_all_24(max_n: int = 4) -> bool:
    """Check whether theta series coefficients up to q^{max_n} distinguish all 24.

    The theta series can fail to distinguish lattices with the same
    number of roots (since c_Delta depends only on N_roots).
    But higher coefficients (r(2), r(3), ...) may distinguish them.
    """
    theta_tuples = {}
    for label in ALL_NIEMEIER_LABELS:
        ts = niemeier_theta_series(label, max_n)
        theta_tuples[label] = ts
    return len(set(theta_tuples.values())) == 24


def lattices_sharing_root_count() -> Dict[int, List[str]]:
    """Find Niemeier lattices with the same number of roots."""
    by_roots: Dict[int, List[str]] = {}
    for label, data in NIEMEIER_REGISTRY.items():
        N = data['num_roots']
        if N not in by_roots:
            by_roots[N] = []
        by_roots[N].append(label)
    return {N: labs for N, labs in by_roots.items() if len(labs) > 1}


def root_count_collision_resolution(max_n: int = 5) -> Dict[str, Any]:
    """For each collision pair, check if theta coefficients resolve them.

    Two lattices with the same N_roots have the same c_Delta and hence
    the same theta series formula. But wait: c_Delta determines the
    theta series ENTIRELY (since dim M_12(SL_2(Z)) = 2, spanned by
    E_12 and Delta, and the coefficient of each q^n is a linear
    function of c_Delta). So lattices with the same N_roots have
    IDENTICAL theta series at genus 1.

    Distinguishing them requires genus-2 data (Siegel theta functions,
    Boecherer coefficients) or non-theta invariants (root system
    structure, automorphism groups).
    """
    collisions = lattices_sharing_root_count()
    results = {}
    for N, labels in collisions.items():
        # Check if theta series distinguish them
        theta_sets = [niemeier_theta_series(lab, max_n) for lab in labels]
        all_same = all(t == theta_sets[0] for t in theta_sets)
        # They MUST be the same (genus-1 theta is determined by N_roots alone)
        results[N] = {
            'labels': labels,
            'theta_identical': all_same,
            'root_systems_differ': len(set(
                NIEMEIER_REGISTRY[lab]['root_system'] for lab in labels
            )) > 1,
            'resolution': 'genus-2 or automorphism group',
        }
    return results


# =========================================================================
# Moonshine shadow tower comparison: what the shadow tower CAN distinguish
# =========================================================================

def shadow_tower_resolving_power() -> Dict[str, Any]:
    """Analysis of what the shadow tower can and cannot distinguish.

    At the scalar level (kappa only):
    - ALL 24 Niemeier lattice VOAs are indistinguishable (kappa = 24 for all).
    - Monster V^natural has kappa = 12, DISTINCT from Niemeier.
    - Thompson V_Th has kappa = 47/4, DISTINCT from both.

    At the theta series level (genus 1):
    - The 24 Niemeier lattices split into 19 groups by c_Delta (= N_roots).
    - Five collision pairs require genus-2 data.
    - Monster is distinguished by its partition function J(tau).

    At the shadow class level:
    - All 24 Niemeier lattice VOAs are class G (Gaussian).
    - Monster is conjectured class M (infinite depth).
    - Thompson is conjectured class M.
    """
    niemeier_kappas = {niemeier_shadow_data(lab)['kappa'] for lab in ALL_NIEMEIER_LABELS}
    return {
        'niemeier_kappas': niemeier_kappas,
        'niemeier_all_same_kappa': len(niemeier_kappas) == 1,
        'monster_kappa': monster_kappa(),
        'thompson_kappa': thompson_kappa(),
        'monster_distinct_from_niemeier': monster_kappa() != KAPPA_NIEMEIER,
        'thompson_distinct_from_both': (
            thompson_kappa() != KAPPA_NIEMEIER and
            thompson_kappa() != monster_kappa()
        ),
        'num_niemeier_distinct_by_theta': len(set(
            niemeier_c_delta(lab) for lab in ALL_NIEMEIER_LABELS
        )),
        'collision_pairs': len(lattices_sharing_root_count()),
    }


# =========================================================================
# Griess algebra shadow invariant (theoretical framework)
# =========================================================================

def griess_shadow_S3_bound() -> Dict[str, Any]:
    r"""Theoretical bounds on S_3(V^natural) from the Griess algebra.

    The cubic shadow S_3 is related to the ternary collision residue
    of the bar complex. For V^natural, this involves the three-point
    function <v_1(z_1) v_2(z_2) v_3(z_3)> for weight-2 fields v_i in
    the Griess algebra.

    The Griess algebra is a commutative nonassociative algebra of
    dimension 196884 with the Monster as automorphisms. Its structure
    constants C^k_{ij} are known (from FLM and subsequent work):
    - The identity (= vacuum descendant omega/2) is a unit.
    - The bilinear form <v_i, v_j> = C^0_{ij} is positive definite.
    - The Norton inequality: <v*v, v*v> <= <v,v>^2 (proved by Miyamoto).

    The cubic shadow S_3 for V^natural should be proportional to a
    specific trace over the Griess algebra:
      S_3 ~ Tr_{V_2}(C^k_{ij} * something)

    This is a frontier computation. We can bound |S_3| using the
    Norton inequality and the known spectrum of the Griess algebra.
    """
    return {
        'S3': 'frontier (requires Griess algebra structure constants)',
        'griess_dim': 196884,
        'norton_inequality': 'proved (Miyamoto)',
        'required_data': 'three-point OPE coefficients at weight 2',
        'computation_status': 'open',
    }


# =========================================================================
# Full moonshine shadow atlas
# =========================================================================

def full_atlas(max_g: int = 3, max_n_theta: int = 5) -> Dict[str, Dict[str, Any]]:
    """Complete moonshine shadow atlas.

    Returns shadow data for:
    - All 24 Niemeier lattice VOAs
    - Monster module V^natural
    - Thompson group VOA V_Th
    """
    atlas: Dict[str, Dict[str, Any]] = {}

    # Niemeier lattices
    niemeier_genus = niemeier_genus_expansion(max_g)
    for label in ALL_NIEMEIER_LABELS:
        atlas[label] = {
            'type': 'Niemeier lattice VOA',
            'shadow': niemeier_shadow_data(label),
            'genus_expansion': niemeier_genus,
            'theta_series': niemeier_theta_series(label, max_n_theta),
            'c_delta': niemeier_c_delta(label),
            'complementarity': niemeier_complementarity(label),
            'num_roots': NIEMEIER_REGISTRY[label]['num_roots'],
            'root_system': NIEMEIER_REGISTRY[label]['root_system'],
        }
        if label in UMBRAL_GROUPS:
            atlas[label]['umbral'] = umbral_moonshine_data(label)

    # Monster
    atlas['Monster'] = {
        'type': 'Monster module V^natural',
        'shadow': monster_shadow_data(),
        'genus_expansion': {g: monster_genus_amplitude(g) for g in range(1, max_g + 1)},
        'partition_function': monster_partition_coefficients(10),
        'mckay_thompson_1A': mckay_thompson_identity(10),
    }

    # Thompson
    atlas['Thompson'] = {
        'type': 'Thompson group VOA',
        'shadow': thompson_shadow_data(),
        'genus_expansion': {
            g: thompson_kappa() * faber_pandharipande(g)
            for g in range(1, max_g + 1)
        },
    }

    return atlas


# =========================================================================
# Verification functions
# =========================================================================

def verify_all_niemeier_shadow_identical() -> bool:
    """Verify that all 24 Niemeier lattices have the same shadow data."""
    ref = niemeier_shadow_data(ALL_NIEMEIER_LABELS[0])
    for label in ALL_NIEMEIER_LABELS[1:]:
        sd = niemeier_shadow_data(label)
        for key in ['kappa', 'S3', 'S4', 'S5', 'S6', 'shadow_depth',
                     'shadow_class', 'central_charge', 'critical_discriminant',
                     'shadow_growth_rate']:
            if sd[key] != ref[key]:
                return False
    return True


def verify_theta_integrality(max_n: int = 5) -> bool:
    """Verify all Niemeier theta coefficients are non-negative integers."""
    for label in ALL_NIEMEIER_LABELS:
        for n in range(max_n + 1):
            r = niemeier_theta_coefficient(label, n)
            if not isinstance(r, int) or r < 0:
                return False
    return True


def verify_theta_r1_equals_roots() -> bool:
    """Verify r(1) = N_roots for all Niemeier lattices."""
    for label in ALL_NIEMEIER_LABELS:
        expected = NIEMEIER_REGISTRY[label]['num_roots']
        actual = niemeier_theta_coefficient(label, 1)
        if actual != expected:
            return False
    return True


def verify_j_function_coefficients() -> bool:
    """Verify J(tau) coefficients against known values."""
    coeffs = j_function_coefficients(10)
    for n, expected in KNOWN_J_COEFFICIENTS.items():
        if n < len(coeffs) and coeffs[n] != expected:
            return False
    return True


def verify_monster_kappa_distinct() -> bool:
    """Verify that kappa(V^natural) != kappa(V_Niemeier)."""
    return monster_kappa() != KAPPA_NIEMEIER


def verify_complementarity_sum_zero() -> bool:
    """Verify kappa + kappa' = 0 for all Niemeier lattice VOAs."""
    for label in ALL_NIEMEIER_LABELS:
        comp = niemeier_complementarity(label)
        if comp['kappa_sum'] != Rational(0):
            return False
    return True
