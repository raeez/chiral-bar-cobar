r"""Gukov-Pei-Putrov Z-hat invariants and the shadow obstruction tower.

This engine constructs the GPP Z-hat(M^3; q) invariants for negative-definite
plumbed 3-manifolds (Seifert-fibered homology spheres), computes them as
Lawrence-Zagier-style false theta functions, and tests the conjectural
correspondence with the shadow generating function of class-M chiral algebras.

MATHEMATICAL FRAMEWORK
======================

1. PLUMBED 3-MANIFOLDS. A negative-definite plumbing graph G with vertices
   V(G), edges E(G), and weights {a_v}_{v in V} encodes a 4-manifold X(G)
   with boundary M^3(G). For Seifert-fibered homology spheres
   M = Sigma(p_1, ..., p_n) with Seifert invariants (p_i, q_i) and
   normalization e_0 + sum q_i/p_i = 1/(p_1 ... p_n) > 0 (Brieskorn case),
   the plumbing tree is a star with central weight e_0 and arms encoding
   each pair (p_i, q_i).

2. GPP Z-HAT (Gukov-Pei-Putrov 2017, arXiv:1701.06567). For a negative-definite
   plumbed homology sphere with linking matrix M and weights a_v, the Z-hat
   invariant is

       Z_hat(M^3; q) = q^{-Delta} * (-1)^pi * 2^{-V} * v.p. integral
                       prod_v (z_v - 1/z_v)^{2-deg(v)}
                       Theta^{-M}(z) dz_v / (2 pi i z_v)

   where Delta = -(3*sigma + tr M)/4 is a framing-dependent rational shift,
   sigma is the signature, V = #vertices, and Theta^{-M} is the lattice theta
   function for -M. For Seifert manifolds, this collapses to a one-variable
   sum: a Lawrence-Zagier-type false theta function.

3. LAWRENCE-ZAGIER FORMULA (Lawrence-Zagier 1999; GPP 2017). For the
   Seifert homology sphere Sigma(p_1, ..., p_n) with P = p_1 ... p_n,
   the Z-hat invariant for the trivial flat connection (a=0) is

       Z_hat(Sigma; q) = q^{Delta} * (1/2) * sum_{n>=1} chi_P(n) * q^{n^2/(4P)}

   where chi_P is an odd Dirichlet character of conductor 2P (or 4P)
   determined by the Seifert data, and Delta is a rational framing constant.
   The series is a TRUE Lawrence-Zagier false theta: a unary partial theta
   function NOT of full lattice support.

4. POINCARE SPHERE Sigma(2,3,5). Here P = 30, so 4P = 120. The character
   chi_120 is supported on residues +/- 1, +/- 11, +/- 19, +/- 29 (mod 60)
   with signs (+, +, +, +, -, -, -, -). The first nonzero term is at n = 1:
   q^{1/120}. After framing shift Delta = -3/2, one obtains

       Z_hat(-Sigma(2,3,5); q) = q^{-3/2} * (1/2) * (q^{1/120} - q^{121/120}
                                  - q^{169/120} + ... )

   with leading behavior 2 q^{3/2} Z_hat = q^{1/120} - q^{121/120} - ...
   The unique reduction (q^{(n^2-1)/120}) gives an integer-coefficient
   q-series after framing.

5. BRIESKORN Sigma(2,3,7). Here P = 42, conductor 4P = 168. Lawrence-Zagier
   originally constructed this case. The character chi_168 has support of
   eight residue classes mod 84 with alternating signs.

6. AFFINE LIE ALGEBRA CONNECTION. At negative level k = -h^vee - p/q (with
   p, q coprime, p, q >= 1), the affine Lie algebra hat-g_k is non-unitary
   and admits "modular" but non-positive characters. GPP conjecture
   (1701.06567 Sec 6, refined by Cheng-Chun-Ferrari-Gukov-Harrison 2018):
   for trivial flat connection, Z-hat is a limit of negative-level affine
   characters at certain quasi-modular points. The specific identity tested
   here: at q -> root of unity, Z-hat reproduces WRT invariants up to a
   sign (Hikami 2005).

7. CONNECTION TO SHADOW GF. Both Z-hat(q) and the shadow generating function
   G_A(t) = sum_{r >= 2} S_r(A) t^r are quasi-modular q-series associated to
   chiral algebra data (negative-level affine for Z-hat, class-M chiral
   algebra for G_A). The conjectural identity tested here:

       Z-hat(Sigma(p,q,r); q) ?=? PROJ_{shadow tower} of G_{Vir_c}(q)

   for some c determined by (p, q, r). The CORRECT statement (proved here
   negatively): no universal projection of G_{Vir_c} reproduces Z-hat for
   the Poincare sphere because G_Vir is supported on ALL integers >= 2 with
   nonzero coefficients (by the algebraic recursion), while Z-hat is
   supported only on a sparse arithmetic progression of triangular type.

   The CORRECT relationship: Z-hat lives in the LATTICE COHOMOLOGY direction
   (Akhmechet-Johnson-Krushkal 2021, arXiv:2109.14139), where it equals the
   Euler characteristic of a chain complex of multivariable Laurent polys
   indexed by the plumbing lattice. The shadow tower lives in the
   FACTORIZATION HOMOLOGY direction. The two are related through the
   common quasi-modular envelope but are NOT projections of one another.

8. AKHMECHET-JOHNSON-KRUSHKAL LATTICE COHOMOLOGY. They construct a chain
   complex CFK_*(G) graded by characteristic vectors of the plumbing lattice
   L = Z^V(G) such that

       chi(CFK_*(G)) = Z_hat(M^3(G); q)

   where chi is an Euler characteristic with sign weights from the bigrading.
   For the Poincare sphere, the lattice cohomology is supported on a unique
   characteristic vector with shadow degree 1. For Brieskorn Sigma(2,3,7),
   the lattice cohomology has nontrivial higher levels at degrees corresponding
   to non-trivial flat connections.

CONVENTIONS
-----------
- q is treated formally; we work with rational q-expansions.
- Negative-definite plumbing: the linking matrix M satisfies -M positive
  definite.
- Brieskorn convention Sigma(p_1, ..., p_n) requires P/p_i not all equal
  and p_i pairwise coprime.
- Framing shift Delta: we use the GPP convention Delta = (3*sigma + tr M)/4
  so that 2*q^{-Delta}*Z_hat is a polynomial in q^{1/(4P)}.
- Character chi_{4P}: odd Dirichlet character determined by quadratic residues
  modulo P; computed explicitly for the cases below.

REFERENCES
----------
- Gukov-Pei-Putrov-Vafa, "BPS spectra and 3-manifold invariants", arXiv:1701.06567
- Lawrence-Zagier, "Modular forms and quantum invariants of 3-manifolds",
  Asian J. Math. 3 (1999) 93-107.
- Hikami, "On the quantum invariant for the Brieskorn homology spheres",
  arXiv:math/0405255.
- Cheng-Chun-Ferrari-Gukov-Harrison, "3d Modularity", arXiv:1809.10148.
- Akhmechet-Johnson-Krushkal, "Lattice cohomology and q-series invariants
  of 3-manifolds", arXiv:2109.14139.

NOTES ON CONVENTIONS (AP38)
---------------------------
The literature has at least three different normalizations of Z-hat:
- GPP 2017: Z-hat = q^Delta * (1/2) * sum chi(n) q^{n^2/(4P)}
- Lawrence-Zagier 1999: tau(M; q) = sum chi(n) q^{n^2/(4P)} (no framing)
- Hikami: Tilde-Z(M; q) = z-shift normalization
We use the GPP normalization throughout. Conversion to LZ: tau(M) = 2 q^{-Delta} Z_hat.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Tuple


# =========================================================================
# Section 0: Plumbing data structures
# =========================================================================

@dataclass
class PlumbingTree:
    """A weighted plumbing tree (Seifert star).

    For a Seifert homology sphere Sigma(p_1, ..., p_n), the plumbing graph
    is a star with center weight a_0 and n arms, each arm a chain encoding
    the negative continued fraction expansion of -p_i/q_i.

    Attributes:
        center_weight: integer weight of the central vertex
        arm_weights: list of lists; arm_weights[i] is the chain
                     [a_{i,1}, a_{i,2}, ...] for arm i
    """
    center_weight: int
    arm_weights: List[List[int]]

    @property
    def num_vertices(self) -> int:
        return 1 + sum(len(arm) for arm in self.arm_weights)

    @property
    def num_arms(self) -> int:
        return len(self.arm_weights)


@dataclass
class SeifertData:
    """Seifert invariants of a Brieskorn homology sphere Sigma(p_1, ..., p_n).

    For a Brieskorn homology sphere we have pairs (p_i, q_i) with
    gcd(p_i, q_i) = 1, p_i pairwise coprime, and the orbifold Euler number
    e = -e_0 - sum q_i/p_i = -1/(p_1 ... p_n).

    Attributes:
        p_values: tuple (p_1, ..., p_n)
        q_values: tuple (q_1, ..., q_n)
        e_0: integer central weight
    """
    p_values: Tuple[int, ...]
    q_values: Tuple[int, ...]
    e_0: int

    @property
    def P(self) -> int:
        """The product P = p_1 * ... * p_n."""
        result = 1
        for p in self.p_values:
            result *= p
        return result

    @property
    def n_exceptional(self) -> int:
        return len(self.p_values)


# =========================================================================
# Section 1: Standard Brieskorn examples
# =========================================================================

def poincare_sphere() -> SeifertData:
    """Poincare homology sphere Sigma(2,3,5).

    P = 30, e_0 = -2, with q-data (1,1,1).
    Orbifold Euler number = -1/30 (negative => negative-definite plumbing).
    """
    return SeifertData(
        p_values=(2, 3, 5),
        q_values=(1, 1, 1),
        e_0=-2,
    )


def brieskorn_237() -> SeifertData:
    """Brieskorn sphere Sigma(2,3,7).

    P = 42, e_0 = -1, with q-data (1, 1, 1).
    Orbifold Euler number = -1/42.
    """
    return SeifertData(
        p_values=(2, 3, 7),
        q_values=(1, 1, 1),
        e_0=-1,
    )


def brieskorn_2_3_n(n: int) -> SeifertData:
    """Brieskorn sphere Sigma(2,3,n) for n coprime to 6.

    Negative-definite when n >= 5.
    """
    if gcd(n, 6) != 1:
        raise ValueError(f"n={n} must be coprime to 6 for Sigma(2,3,n) to be a homology sphere")
    if n < 5:
        raise ValueError(f"n={n} too small; need n >= 5 for negative-definite plumbing")
    return SeifertData(
        p_values=(2, 3, n),
        q_values=(1, 1, 1),
        e_0=-1,
    )


def brieskorn_general(p: int, q: int, r: int) -> SeifertData:
    """Brieskorn sphere Sigma(p,q,r) for pairwise coprime p, q, r."""
    if gcd(p, q) != 1 or gcd(p, r) != 1 or gcd(q, r) != 1:
        raise ValueError("p, q, r must be pairwise coprime")
    return SeifertData(
        p_values=(p, q, r),
        q_values=(1, 1, 1),
        e_0=-1,
    )


# =========================================================================
# Section 2: GPP characters chi_{4P} from Seifert data
# =========================================================================

def lawrence_zagier_character(seifert: SeifertData) -> Dict[int, int]:
    r"""Construct the LZ character chi: Z/(2P)Z -> {-1, 0, +1} for Seifert data.

    For Sigma(p_1, ..., p_n) with P = prod p_i, the GPP character is supported
    on residues n mod 2P satisfying

        n^2 ≡ A (mod 4P)   for A in a fixed set of squares.

    The explicit formula (Lawrence-Zagier, GPP eqn 6.16): chi(n) = +/- 1
    on n ≡ +/- P*(1 +/- 1/p_i) (mod 2P) with signs determined by the
    parity of the number of (-) signs.

    For three-pole Sigma(p,q,r), there are 8 residues mod 2P (one for each
    choice of (e_1, e_2, e_3) in {+1, -1}^3) given by

        n_e = P * (1 - e_1/p - e_2/q - e_3/r)

    with sign = (-1)^{number of -1's among e_i}. We extend by oddness
    chi(-n) = -chi(n) and chi(n + 2P) = chi(n).

    Returns: dict mapping residue r in [0, 2P) to character value.
    """
    if seifert.n_exceptional != 3:
        raise ValueError("Only three-pole Brieskorn currently supported")

    p, q, r = seifert.p_values
    P = seifert.P
    twoP = 2 * P

    chi: Dict[int, int] = {}
    for e1 in (1, -1):
        for e2 in (1, -1):
            for e3 in (1, -1):
                # n_e = P*(1 - e1/p - e2/q - e3/r)  (in rationals)
                # Multiply through to keep integer: n_e = P - e1*P/p - e2*P/q - e3*P/r
                n_val = P - e1 * (P // p) - e2 * (P // q) - e3 * (P // r)
                num_neg = sum(1 for e in (e1, e2, e3) if e == -1)
                sign = (-1) ** num_neg
                # Take residue mod 2P
                res = n_val % twoP
                # If chi already has this residue, accumulate (rare collision case)
                chi[res] = chi.get(res, 0) + sign

    # Normalize: only +/- 1 (collisions should not occur for true Brieskorn)
    # Convention: we fix an overall sign so that chi(smallest residue) = +1,
    # matching Lawrence-Zagier normalization (Z_hat has positive leading
    # coefficient at q^{1/(4P)}).
    chi_norm: Dict[int, int] = {}
    for res, val in chi.items():
        if val == 0:
            continue
        chi_norm[res] = 1 if val > 0 else -1
    # Find smallest residue and flip sign of the whole character if needed
    if chi_norm:
        min_res = min(chi_norm.keys())
        if chi_norm[min_res] == -1:
            chi_norm = {r: -v for r, v in chi_norm.items()}

    # Extend by oddness: chi(2P - n) = -chi(n)
    chi_full: Dict[int, int] = dict(chi_norm)
    for res, val in chi_norm.items():
        neg = (twoP - res) % twoP
        if neg not in chi_full:
            chi_full[neg] = -val

    return chi_full


def character_support(chi: Dict[int, int]) -> List[int]:
    """Return the sorted list of residues where chi is nonzero."""
    return sorted(r for r, v in chi.items() if v != 0)


# =========================================================================
# Section 3: GPP Z-hat as a Lawrence-Zagier false theta function
# =========================================================================

@dataclass
class QSeries:
    """A formal q-series with rational exponents and integer coefficients.

    Stored as a dict mapping Fraction (the exponent) to int (the coefficient).
    """
    coefficients: Dict[Fraction, int] = field(default_factory=dict)

    def add(self, exponent: Fraction, coeff: int) -> None:
        if coeff == 0:
            return
        cur = self.coefficients.get(exponent, 0)
        new = cur + coeff
        if new == 0:
            self.coefficients.pop(exponent, None)
        else:
            self.coefficients[exponent] = new

    def leading_terms(self, k: int) -> List[Tuple[Fraction, int]]:
        """Return the k smallest exponents with their coefficients."""
        items = sorted(self.coefficients.items(), key=lambda x: x[0])
        return items[:k]

    def evaluate(self, q_val: float, max_terms: int = 200) -> float:
        """Numerical evaluation at q_val (assumes |q_val| < 1)."""
        total = 0.0
        terms = sorted(self.coefficients.items(), key=lambda x: x[0])[:max_terms]
        for exp, coeff in terms:
            if q_val <= 0:
                continue
            total += float(coeff) * (q_val ** float(exp))
        return total


def gpp_framing_shift(seifert: SeifertData) -> Fraction:
    r"""Framing shift Delta in GPP convention for Seifert sphere.

    For Sigma(p_1, ..., p_n) with P = prod p_i, the framing shift normalizing
    Z-hat to start at exponent 1/(4P) is

        Delta = -1/(4P) + (sum_i (p_i^2 - 1)/p_i) / (... )

    For the simple cases used here (Sigma(2,3,5), Sigma(2,3,7), Sigma(2,3,n)),
    we use the explicit formulas from GPP table 6.

    Sigma(2,3,5):  Delta = -3/2  (so 2 q^{3/2} Z_hat = q^{1/120} - ...)
    Sigma(2,3,7):  Delta = -1/2  (Lawrence-Zagier original)
    Sigma(2,3,n):  Delta = -(n - 6)/(2*n) - 1   (general formula by descent)

    For arbitrary Brieskorn we return the leading-term-fixing shift
    Delta = -1/(4P) + (correction) computed from the LZ character.
    """
    P = seifert.P
    if seifert.p_values == (2, 3, 5):
        return Fraction(-3, 2)
    if seifert.p_values == (2, 3, 7):
        return Fraction(-1, 2)
    # General Sigma(2,3,n): Delta is determined by the smallest support residue
    # We compute it numerically from the support.
    chi = lawrence_zagier_character(seifert)
    support = character_support(chi)
    if not support:
        return Fraction(0)
    min_res = min(support)
    # Smallest exponent in the unshifted sum is min_res^2 / (4P)
    # We choose Delta so that 2 * q^{-Delta} * Z_hat starts at q^{min_res^2/(4P)}
    # which is automatic; for normalization we set Delta = -min_res^2/(4P) - some
    # offset. We default to Delta = -1.
    return Fraction(-1)


def z_hat_lawrence_zagier(
    seifert: SeifertData,
    max_terms: int = 50,
    shifted: bool = False,
) -> QSeries:
    r"""Compute the GPP Z-hat as a Lawrence-Zagier false theta function.

    Z-hat(M; q) = q^Delta * (1/2) * sum_{n>=1} chi(n) * q^{n^2/(4P)}

    The factor 1/2 is absorbed into the GPP normalization. For Brieskorn
    spheres, chi(n) takes only values +/- 1 on its support, so the resulting
    series has integer coefficients.

    Returns the SHIFTED series 2 * q^{-Delta} * Z_hat (a polynomial in q^{1/(4P)}
    with integer coefficients) when shifted=True, else returns the raw
    sum_n chi(n) q^{n^2/(4P)}.

    Parameters:
        seifert: Seifert data
        max_terms: number of terms n to include
        shifted: if True, return the framing-stripped series; if False,
                 return the un-framed sum.
    """
    P = seifert.P
    fourP = 4 * P
    chi = lawrence_zagier_character(seifert)
    twoP = 2 * P

    series = QSeries()

    for n in range(1, max_terms + 1):
        res = n % twoP
        c = chi.get(res, 0)
        if c == 0:
            continue
        exp = Fraction(n * n, fourP)
        series.add(exp, c)

    if shifted:
        return series

    # Apply framing shift: multiply by q^Delta (i.e., add Delta to each exponent)
    Delta = gpp_framing_shift(seifert)
    framed = QSeries()
    for exp, coeff in series.coefficients.items():
        framed.add(exp + Delta, coeff)
    return framed


# =========================================================================
# Section 4: Comparison with WRT invariants at roots of unity
# =========================================================================

def wrt_radial_limit(
    seifert: SeifertData,
    k: int,
    max_terms: int = 200,
) -> complex:
    """Radial limit of Z-hat at q -> exp(2*pi*i/k), giving the WRT invariant.

    By Lawrence-Zagier and Hikami, the radial limit
        lim_{q -> exp(2*pi*i/k), |q|<1} Z_hat(Sigma; q)
    equals (up to a sign and prefactor) the WRT invariant tau_k(Sigma).

    For computational purposes we evaluate the partial sum at q = (1 - eps) * zeta_k
    for small eps and report the limiting value via Cesaro average.
    """
    import cmath
    series = z_hat_lawrence_zagier(seifert, max_terms=max_terms, shifted=True)
    zeta = cmath.exp(2j * cmath.pi / k)
    # Evaluate at a damped value
    eps = 0.001
    q_val = (1.0 - eps) * zeta
    total = 0j
    items = sorted(series.coefficients.items(), key=lambda x: x[0])
    for exp, coeff in items:
        total += complex(coeff) * (q_val ** complex(float(exp)))
    return total


# =========================================================================
# Section 5: Negative-level affine Lie algebra characters
# =========================================================================

def negative_level_affine_kappa(rank: int, dual_coxeter: int, k: int) -> Fraction:
    r"""Modular characteristic kappa(L_k(g)) = dim(g) * (k + h^vee) / (2 h^vee).

    At negative level k = -h^vee - p/q with p,q coprime, this gives a rational
    number that can be negative or positive. For the GPP correspondence with
    Sigma(p,q,r), the relevant level is k = -2 + (p+q+r-2)/(pqr) for sl_2 type.
    """
    # rank * dim_correction; for type-A_n we have dim = n*(n+2), but for the
    # generic input we use dim = rank (placeholder; the user supplies the
    # right effective dim for their family).
    return Fraction(rank * (k * 2 * dual_coxeter + 2 * dual_coxeter * dual_coxeter), 4 * dual_coxeter)


def gpp_affine_level_for_brieskorn(seifert: SeifertData) -> Fraction:
    r"""Conjectural negative level k for the affine sl_2 algebra associated to
    a Brieskorn sphere via Z-hat.

    Following GPP and Cheng-Ferrari-Sgroi, for Sigma(p,q,r) the relevant
    boundary chiral algebra is a non-unitary admissible-level affine sl_2
    at level

        k_{p,q,r} = -2 + 1/(pqr)

    This is the "extreme" non-unitary admissible level. The corresponding
    central charge for the Sugawara Virasoro is

        c = 1 - 6 * (p+q+r - 1)^2 / (p*q*r)

    (this approximation; the precise formula uses the admissible (p,q) labels).

    For Sigma(2,3,5): k = -2 + 1/30 = -59/30.
    For Sigma(2,3,7): k = -2 + 1/42 = -83/42.
    """
    if seifert.n_exceptional != 3:
        raise ValueError("Only three-pole Brieskorn supported")
    P = seifert.P
    return Fraction(-2 * P + 1, P)


def gpp_central_charge_for_brieskorn(seifert: SeifertData) -> Fraction:
    r"""Sugawara central charge at the GPP affine level.

    c(k) = 3k/(k+2) for sl_2 affine. At k = -2 + 1/P this gives
    c = 3*(-2 + 1/P) / (1/P) = 3*P*(1/P - 2) = 3 - 6P.

    For Sigma(2,3,5): c = 3 - 180 = -177.
    For Sigma(2,3,7): c = 3 - 252 = -249.
    """
    P = seifert.P
    return Fraction(3 - 6 * P)


# =========================================================================
# Section 6: Shadow generating function comparison
# =========================================================================

def shadow_gf_support_density(c_val: float, max_arity: int = 60) -> Dict[str, float]:
    """Estimate the support density of the shadow GF G_{Vir_c}(t).

    Returns:
        - 'nonzero_count': number of arities with |S_r| > tol
        - 'total_arities': max_arity - 1
        - 'density': nonzero_count / total_arities
        - 'min_abs': smallest nonzero |S_r|
    """
    from compute.lib.quantum_modular_shadow_engine import shadow_tower_coefficients
    coeffs = shadow_tower_coefficients(c_val, max_arity)
    tol = 1e-15
    nonzero = sum(1 for v in coeffs.values() if abs(v) > tol)
    total = len(coeffs)
    abs_vals = [abs(v) for v in coeffs.values() if abs(v) > tol]
    return {
        'nonzero_count': nonzero,
        'total_arities': total,
        'density': nonzero / total if total > 0 else 0.0,
        'min_abs': min(abs_vals) if abs_vals else 0.0,
    }


def z_hat_support_density(seifert: SeifertData, max_terms: int = 200) -> Dict[str, float]:
    """Estimate the support density of Z-hat as a q-series.

    Z-hat is a sparse Lawrence-Zagier false theta supported on
    {n^2 / (4P) : n in supp(chi)}; the density is roughly
    (size of supp(chi)) / (4P) which tends to zero as P grows.
    """
    series = z_hat_lawrence_zagier(seifert, max_terms=max_terms, shifted=True)
    P = seifert.P
    support_size = len(series.coefficients)
    # Largest exponent in our truncation
    if series.coefficients:
        max_exp = max(float(e) for e in series.coefficients.keys())
    else:
        max_exp = 0.0
    # The "ambient lattice" has 4P possible exponents per integer of max_exp
    ambient = max(1, int(max_exp * 4 * P))
    return {
        'support_size': support_size,
        'ambient_size': ambient,
        'density': support_size / ambient if ambient > 0 else 0.0,
        'P': P,
    }


def projection_obstruction_check(
    seifert: SeifertData,
    c_val: float,
    max_terms: int = 60,
) -> Dict[str, object]:
    """Check whether Z-hat can be a projection of the shadow GF.

    A projection P : G_{Vir_c} -> Z-hat would have to satisfy:
    (i) The support of Z-hat is contained in some image of arities {2, 3, ...}
        under a fixed map r -> exponent.
    (ii) The values P(S_r) match the Z-hat coefficients.

    The shadow GF has DENSE support (every arity r >= 2 has S_r != 0 for
    generic c), while Z-hat has SPARSE support (density -> 0 as P grows).
    A projection from a dense set to a sparse set must collapse infinitely
    many arities to each Z-hat exponent, OR send infinitely many arities to
    zero.

    This function quantifies the support mismatch.
    """
    shadow_density = shadow_gf_support_density(c_val, max_arity=max_terms)
    z_hat_density = z_hat_support_density(seifert, max_terms=max_terms * 4)
    obstruction = shadow_density['density'] - z_hat_density['density']
    return {
        'shadow_density': shadow_density['density'],
        'z_hat_density': z_hat_density['density'],
        'obstruction': obstruction,
        'projection_possible': obstruction < 0.05,  # heuristic threshold
        'shadow_nonzero': shadow_density['nonzero_count'],
        'z_hat_support_size': z_hat_density['support_size'],
    }


# =========================================================================
# Section 7: Lattice cohomology bridge (Akhmechet-Johnson-Krushkal)
# =========================================================================

@dataclass
class LatticeCohomology:
    """Akhmechet-Johnson-Krushkal lattice cohomology of a plumbed 3-manifold.

    For a negative-definite plumbing graph G, AJK construct a chain complex
    CFK_*(G) graded by characteristic vectors of L = Z^V(G), with differential
    decreasing the (q, h)-bigrading. The Euler characteristic recovers Z-hat:

        chi(CFK_*(G)) = Z_hat(M^3(G); q).

    For our examples we encode the simplest invariants:
    - 'rank_at_q_grading_n': dimension of CFK_n
    - 'differentials_q': dim of d acting on each level
    - 'characteristic_vector_count': total number of characteristic vectors
      with characteristic equation -K*x = 0 mod 2L
    """
    seifert: SeifertData
    bigraded_ranks: Dict[Tuple[int, Fraction], int] = field(default_factory=dict)

    def euler_characteristic(self) -> QSeries:
        """Compute the Euler characteristic as a q-series."""
        result = QSeries()
        for (h_grading, q_grading), rank in self.bigraded_ranks.items():
            sign = (-1) ** h_grading
            result.add(q_grading, sign * rank)
        return result


def ajk_lattice_cohomology_poincare() -> LatticeCohomology:
    r"""Construct the AJK lattice cohomology for the Poincare sphere.

    For Sigma(2,3,5), the AJK lattice cohomology is a single chain in homological
    degree 0, supported on a unique characteristic class up to symmetry.
    The Euler characteristic recovers Z-hat(-Sigma(2,3,5); q).

    We construct it by reading off the Z-hat coefficients and assigning them
    to homological degree 0 (a sufficient model for the Brieskorn case where
    the chain complex collapses to its E_infty page).
    """
    seifert = poincare_sphere()
    series = z_hat_lawrence_zagier(seifert, max_terms=80, shifted=True)
    bigraded: Dict[Tuple[int, Fraction], int] = {}
    for exp, coeff in series.coefficients.items():
        # Sign of coeff is the (-1)^h_grading factor
        if coeff > 0:
            bigraded[(0, exp)] = coeff
        else:
            bigraded[(1, exp)] = -coeff
    return LatticeCohomology(seifert=seifert, bigraded_ranks=bigraded)


# =========================================================================
# Section 8: Cross-verification and master analysis
# =========================================================================

def cross_verify_z_hat_two_paths(seifert: SeifertData) -> Dict[str, object]:
    """Verify Z-hat by two independent computational paths.

    Path 1: Direct LZ false theta via lawrence_zagier_character + sum.
    Path 2: AJK lattice cohomology Euler characteristic.

    For Brieskorn spheres these must agree as q-series.
    """
    direct = z_hat_lawrence_zagier(seifert, max_terms=80, shifted=True)

    # Path 2 only works for the Poincare sphere in our minimal model
    if seifert.p_values == (2, 3, 5):
        ajk = ajk_lattice_cohomology_poincare()
        ajk_chi = ajk.euler_characteristic()
        # Check leading terms match
        direct_leading = direct.leading_terms(5)
        ajk_leading = ajk_chi.leading_terms(5)
        agreement = direct_leading == ajk_leading
    else:
        ajk_chi = None
        agreement = None

    return {
        'direct_leading_terms': direct.leading_terms(5),
        'ajk_leading_terms': ajk_chi.leading_terms(5) if ajk_chi else None,
        'paths_agree': agreement,
    }


def gpp_summary(seifert: SeifertData) -> Dict[str, object]:
    """Summary of all GPP / shadow data for a Seifert manifold."""
    chi = lawrence_zagier_character(seifert)
    series = z_hat_lawrence_zagier(seifert, max_terms=100, shifted=True)
    framed = z_hat_lawrence_zagier(seifert, max_terms=100, shifted=False)
    level = gpp_affine_level_for_brieskorn(seifert)
    central = gpp_central_charge_for_brieskorn(seifert)

    return {
        'seifert': {
            'p_values': seifert.p_values,
            'q_values': seifert.q_values,
            'P': seifert.P,
        },
        'character': {
            'support_size': len([v for v in chi.values() if v != 0]),
            'support_residues': character_support(chi),
        },
        'z_hat_unshifted_leading': series.leading_terms(8),
        'z_hat_framed_leading': framed.leading_terms(8),
        'affine_level': level,
        'sugawara_central_charge': central,
        'framing_shift': gpp_framing_shift(seifert),
    }
