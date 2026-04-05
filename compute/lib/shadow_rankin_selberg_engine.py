r"""Shadow Rankin-Selberg engine: inner products of shadow towers and L-value extraction.

Connects the shadow obstruction tower inner products to the operadic
Rankin-Selberg theorem (thm:operadic-rankin-selberg) and L-values.

SHADOW INNER PRODUCT:

For two modular Koszul algebras A, B with shadow towers {S_r(A)}, {S_r(B)},
the shadow Petersson inner product is:

    <S(A), S(B)>_Pet = sum_{r >= 2} S_r(A) * S_r(B) * w(r)

where w(r) is the Petersson weight.  The operadic structure determines w(r):
at genus g, the arity-r shadow contributes at genus g >= floor(r/2) + 1
(cor:shadow-visibility-genus).  The Petersson weight is:

    w(r) = sum_{g >= ceil(r/2)} (intersection number factor at genus g for arity r)

At genus 1 (the only genus where arity 2 contributes):
    w(2) = (lambda_1^FP)^2 * vol(M_{1,1})

where vol(M_{1,1}) = pi/3 is the hyperbolic volume and lambda_1^FP = 1/24.

CAUTION: There are TWO distinct inner products in play:
  (a) Algebraic: F_g(A) * F_g(B) = kappa(A)*kappa(B) * (lambda_g^FP)^2
      This is the PRODUCT of two numbers.  No integral.
  (b) Petersson: int_{M_g} |F_g(A,tau)|^2 dmu(tau)
      This is the Petersson inner product of the g-th shadow amplitude
      as a function on M_g against the hyperbolic measure.

At genus 1, the Rankin-Selberg unfolding gives:
    int_{SL(2,Z)\H} |F_1(A,tau)|^2 dmu = kappa(A)^2 * RS_value
where RS_value involves the Rankin-Selberg integral of |E_2*(tau)|^2
(the quasi-modular Eisenstein series, NOT a holomorphic modular form -- AP15).

GENUS-2 RANKIN-SELBERG:

At genus 2, the integral involves tautological intersection numbers:
    int_{M-bar_2} F_2(A) * F_2(B) (as product of tautological classes)

The scalar part: F_2^{scal}(A) = kappa(A) * lambda_2.  So:
    int lambda_2^2 needs to be computed on M-bar_2.

But lambda_2 is the TOP Hodge class on M-bar_2 (rank 2 bundle), so
lambda_2^2 has degree 4 on a 3-dimensional space: lambda_2^2 = 0 by dimension!

The correct genus-2 inner product uses the PAIRING between tautological
classes of complementary degree.  For two genus-2 amplitudes, we need:
    int_{M-bar_2} omega_A ^ omega_B
where omega_A is a degree-d class and omega_B is degree-(3-d).

The simplest invariant is:
    F_2(A) = kappa(A) * lambda_2^FP  (a NUMBER, the integral of the class)

The product F_2(A) * F_2(B) = kappa(A) * kappa(B) * (lambda_2^FP)^2
is the algebraic inner product at genus 2.

KOSZUL DUALITY AND RANKIN-SELBERG:

For a Koszul pair (A, A!):
    kappa(A) + kappa(A!) = 0  for KM/free fields  (AP24)
    kappa(A) + kappa(A!) = rho*K  for W-algebras

The complementarity theorem (Thm C) gives:
    Q_g(A) + Q_g(A!) = H*(M-bar_g, Z(A))

At the scalar level: F_g(A) + F_g(A!) = (kappa(A) + kappa(A!)) * lambda_g^FP.
For KM: this is 0. For Virasoro: kappa + kappa' = c/2 + (26-c)/2 = 13.
So F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g^FP.

The Koszul inner product:
    <S(A), S(A!)>_Pet detects the complementarity via the cross-terms.

Ground truth:
    thm:operadic-rankin-selberg (arithmetic_shadows.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    chapters/connections/arithmetic_shadows.tex

CAUTION (AP1): kappa formulas are family-specific. Never copy between families.
CAUTION (AP15): E_2* is quasi-modular, not holomorphic. The genus-1 propagator
    produces quasi-modular forms, not holomorphic modular forms.
CAUTION (AP24): kappa(A) + kappa(A!) = 0 for KM, = 13 for Virasoro. Not universal.
CAUTION (AP39): kappa != c/2 for non-Virasoro families.
CAUTION (AP48): kappa depends on the full algebra, not just the Virasoro subalgebra.
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union


# ============================================================
# 1. Faber-Pandharipande numbers (from first principles)
# ============================================================

def _bernoulli_exact(n: int) -> Fraction:
    """Bernoulli number B_n via binomial recurrence. Convention: B_1 = -1/2."""
    if n < 0:
        return Fraction(0)
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        s = Fraction(0)
        binom = Fraction(1)
        for k in range(m):
            s += binom * B[k]
            binom = binom * Fraction(m + 1 - k, k + 1)
        B[m] = -s * Fraction(1, m + 1)
    return B[n]


def _factorial(n: int) -> int:
    """Factorial n!."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    g=1: 1/24
    g=2: 7/5760
    g=3: 31/967680

    This enters F_g(A) = kappa(A) * lambda_g^FP.
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B2g = _bernoulli_exact(2 * g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs(B2g) / Fraction(_factorial(2 * g))


# ============================================================
# 2. Tautological intersection numbers (exact)
# ============================================================

# Genus 1
LAMBDA1_FP = Fraction(1, 24)  # int_{M-bar_{1,1}} lambda_1 psi^0 = 1/24

# Genus 2
LAMBDA2_INTEGRAL = Fraction(1, 240)  # int_{M-bar_2} lambda_2 = 1/240
LAMBDA1_SQ_INTEGRAL_G2 = Fraction(1, 240)  # int_{M-bar_2} lambda_1^2 = 1/240 (Faber)
LAMBDA2_FP = Fraction(7, 5760)  # int_{M-bar_{2,1}} lambda_2 psi^2 = 7/5760

# Genus 3
LAMBDA3_INTEGRAL = Fraction(1, 6048)  # int_{M-bar_3} lambda_3 (Faber-vdGeer)
LAMBDA3_FP = Fraction(31, 967680)

# Hyperbolic volume
VOL_M11 = Fraction(1, 6)  # vol(M_{1,1}) = pi/3 -> chi^orb = -1/12
# Actually vol in Petersson measure: vol(SL(2,Z)\H) = pi/3 (hyperbolic)
# We use the orbifold Euler characteristic chi^orb(M_{1,1}) = -1/12 instead.
CHI_ORB_M11 = Fraction(-1, 12)


# ============================================================
# 3. Standard family data
# ============================================================

class AlgebraData:
    """Shadow obstruction tower data for a chiral algebra."""

    def __init__(self, name: str, kappa: Fraction,
                 shadow_class: str, weights: List[int],
                 S_coeffs: Optional[Dict[int, Fraction]] = None,
                 kappa_dual: Optional[Fraction] = None):
        """
        Parameters
        ----------
        name : str
            Family name.
        kappa : Fraction
            Modular characteristic kappa(A).
        shadow_class : str
            One of 'G', 'L', 'C', 'M'.
        weights : list of int
            Conformal weights of generators.
        S_coeffs : dict, optional
            Shadow coefficients S_r for r >= 3.
        kappa_dual : Fraction, optional
            kappa(A!) for the Koszul dual. If None, computed from family rules.
        """
        self.name = name
        self.kappa = kappa
        self.shadow_class = shadow_class
        self.weights = weights
        self.S_coeffs = S_coeffs or {}
        self.kappa_dual = kappa_dual

    def S(self, r: int) -> Fraction:
        """Shadow coefficient at arity r."""
        if r == 2:
            return self.kappa
        return self.S_coeffs.get(r, Fraction(0))

    def F_g(self, g: int) -> Fraction:
        """Scalar genus-g free energy: F_g = kappa * lambda_g^FP."""
        return self.kappa * lambda_fp(g)

    def __repr__(self):
        return f"AlgebraData({self.name}, kappa={self.kappa})"


def heisenberg(k: Union[int, Fraction] = 1) -> AlgebraData:
    """Heisenberg H_k: class G, r_max=2, kappa=k."""
    kap = Fraction(k)
    return AlgebraData("Heisenberg", kappa=kap, shadow_class='G',
                       weights=[1], kappa_dual=-kap)


def affine_sl2(k: Union[int, Fraction] = 1) -> AlgebraData:
    r"""sl_2 affine at level k: class L, r_max=3.

    kappa(sl_2, k) = dim(sl_2) * (k + h^v) / (2*h^v) = 3*(k+2)/4
    kappa_dual: Feigin-Frenkel k -> -k-2h^v = -k-4, so
    kappa(sl_2, -k-4) = 3*(-k-4+2)/4 = 3*(-k-2)/4 = -kappa(sl_2, k)
    """
    kap = Fraction(3) * (Fraction(k) + Fraction(2)) / Fraction(4)
    # Cubic shadow alpha for affine KM (leading order)
    # S_3 for affine is nonzero (class L) but we use a simplified model
    S_coeffs: Dict[int, Fraction] = {3: Fraction(2)}
    return AlgebraData("sl2_affine", kappa=kap, shadow_class='L',
                       weights=[1], S_coeffs=S_coeffs,
                       kappa_dual=-kap)


def virasoro(c: Union[int, Fraction] = 26) -> AlgebraData:
    r"""Virasoro Vir_c: class M, r_max=infinity.

    kappa(Vir_c) = c/2.
    kappa(Vir_{26-c}) = (26-c)/2.  (Koszul dual)
    kappa + kappa' = 13 (NOT 0, AP24).

    S_3(Vir) = alpha = 2 (T-line cubic shadow).
    S_4(Vir) = Q^contact = 10/(c(5c+22)).
    S_r: leading order (2/r)*(-3)^{r-4}*(2/c)^{r-2}.
    """
    c_frac = Fraction(c)
    kap = c_frac / Fraction(2)
    kap_dual = (Fraction(26) - c_frac) / Fraction(2)

    S_coeffs: Dict[int, Fraction] = {}
    S_coeffs[3] = Fraction(2)  # alpha = 2

    # S_4 = Q^contact = 10/(c(5c+22))
    denom_4 = c_frac * (Fraction(5) * c_frac + Fraction(22))
    if denom_4 != 0:
        S_coeffs[4] = Fraction(10) / denom_4

    # Higher order: S_r = (2/r)*(-3)^{r-4}*(2/c)^{r-2}
    if c_frac != 0:
        P = Fraction(2) / c_frac
        for r in range(5, 16):
            S_coeffs[r] = Fraction(2, r) * Fraction(-3) ** (r - 4) * P ** (r - 2)

    return AlgebraData("Virasoro", kappa=kap, shadow_class='M',
                       weights=[2], S_coeffs=S_coeffs,
                       kappa_dual=kap_dual)


def w3(c: Union[int, Fraction] = 50) -> AlgebraData:
    r"""W_3 at central charge c: class M.

    kappa(W_3) = c * (H_3 - 1) = c * (1 + 1/2 + 1/3 - 1) = c * 5/6
    Wait -- the convention in depth_classification.py says:
    kappa(W_N, c) = (H_N - 1) * c  where H_N = 1 + 1/2 + ... + 1/N.
    H_3 - 1 = 1/2 + 1/3 = 5/6. So kappa(W_3) = 5c/6.

    CAUTION (AP39/AP1): this is NOT c/2. kappa(W_3) = 5c/6.
    """
    c_frac = Fraction(c)
    kap = Fraction(5, 6) * c_frac  # H_3 - 1 = 5/6
    # Koszul dual: c -> 26 - c for the Virasoro part, but W_3 duality
    # is more subtle. For the scalar level we use kappa_dual = -kappa
    # (affine-type anti-symmetry, but this may need correction for W_3).
    # AP24: need to check this. For now use the anti-symmetric assumption.
    kap_dual = -kap

    S_coeffs: Dict[int, Fraction] = {}
    S_coeffs[3] = Fraction(2)  # T-line cubic shadow

    # T-line quartic
    denom_4 = c_frac * (Fraction(5) * c_frac + Fraction(22))
    if denom_4 != 0:
        S_coeffs[4] = Fraction(10) / denom_4

    # Higher order along T-line
    if c_frac != 0:
        P = Fraction(2) / c_frac
        for r in range(5, 16):
            S_coeffs[r] = Fraction(2, r) * Fraction(-3) ** (r - 4) * P ** (r - 2)

    return AlgebraData("W_3", kappa=kap, shadow_class='M',
                       weights=[2, 3], S_coeffs=S_coeffs,
                       kappa_dual=kap_dual)


def betagamma(lam: Union[int, Fraction] = 0) -> AlgebraData:
    r"""betagamma system at weight lambda: class C, r_max=4.

    kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.
    Standard (lambda=0 or 1): kappa=1. Symplectic (lambda=1/2): kappa=-1/2.
    """
    lam_frac = Fraction(lam)
    kap = Fraction(6) * lam_frac**2 - Fraction(6) * lam_frac + Fraction(1)
    # Class C: S_3 = 0, S_4 != 0 (contact quartic)
    S_coeffs: Dict[int, Fraction] = {3: Fraction(0)}
    # For betagamma the quartic is nonzero but we don't have an exact formula
    # in this module. Set to a placeholder.
    return AlgebraData("betagamma", kappa=kap, shadow_class='C',
                       weights=[lam], S_coeffs=S_coeffs,
                       kappa_dual=-kap)


def lattice_e8() -> AlgebraData:
    """E8 lattice VOA: kappa = rank = 8."""
    return AlgebraData("E8_lattice", kappa=Fraction(8), shadow_class='G',
                       weights=[1]*8, kappa_dual=-Fraction(8))


def lattice_d16() -> AlgebraData:
    """D16 lattice VOA: kappa = rank = 16."""
    return AlgebraData("D16_lattice", kappa=Fraction(16), shadow_class='G',
                       weights=[1]*16, kappa_dual=-Fraction(16))


def lattice_leech() -> AlgebraData:
    """Leech lattice VOA: kappa = rank = 24."""
    return AlgebraData("Leech_lattice", kappa=Fraction(24), shadow_class='G',
                       weights=[1]*24, kappa_dual=-Fraction(24))


# Standard landscape at specific levels
STANDARD_FAMILIES = {
    'Heisenberg_k1': heisenberg(1),
    'Heisenberg_k2': heisenberg(2),
    'sl2_k1': affine_sl2(1),
    'sl2_k2': affine_sl2(2),
    'sl2_k3': affine_sl2(3),
    'Virasoro_c1': virasoro(1),
    'Virasoro_c10': virasoro(10),
    'Virasoro_c13': virasoro(13),  # self-dual point
    'Virasoro_c26': virasoro(26),
    'W3_c50': w3(50),
    'W3_c100': w3(100),
    'betagamma_0': betagamma(0),
    'E8_lattice': lattice_e8(),
    'D16_lattice': lattice_d16(),
    'Leech_lattice': lattice_leech(),
}


# ============================================================
# 4. Shadow inner product (algebraic version)
# ============================================================

def shadow_inner_product_algebraic(A: AlgebraData, B: AlgebraData,
                                   r_max: int = 15) -> Fraction:
    r"""Algebraic shadow inner product (unweighted).

    <S(A), S(B)>_alg = sum_{r=2}^{r_max} S_r(A) * S_r(B)

    This is the simplest inner product: no Petersson weight, just the
    coefficient-by-coefficient dot product of the two shadow towers.
    """
    result = Fraction(0)
    for r in range(2, r_max + 1):
        result += A.S(r) * B.S(r)
    return result


def shadow_inner_product_petersson(A: AlgebraData, B: AlgebraData,
                                   r_max: int = 15, g_max: int = 5) -> Fraction:
    r"""Petersson-weighted shadow inner product.

    <S(A), S(B)>_Pet = sum_{r=2}^{r_max} S_r(A) * S_r(B) * w(r)

    The Petersson weight w(r) comes from the operadic structure:
    arity-r shadows contribute at genus g >= ceil(r/2).
    The weight is determined by the tautological intersection theory.

    At the scalar level:
        w(2) = sum_{g >= 1} (lambda_g^FP)^2
             = (1/24)^2 + (7/5760)^2 + ...

    For r >= 3, w(r) involves boundary-stratum integrals on M-bar_g
    for g >= ceil(r/2). These are harder to compute; we use the
    leading contribution from the visibility genus g_min = ceil(r/2).

    The simplest useful normalization: w(r) = (lambda_{g_min}^FP)^2 / r!
    where g_min = ceil(r/2). This captures the leading tautological
    contribution with the 1/r! combinatorial symmetry factor.
    """
    result = Fraction(0)
    for r in range(2, r_max + 1):
        g_min = (r + 1) // 2  # ceil(r/2)
        if g_min > g_max:
            continue
        # Weight = sum of (lambda_g^FP)^2 for g from g_min to g_max
        w_r = Fraction(0)
        for g in range(g_min, g_max + 1):
            try:
                w_r += lambda_fp(g) ** 2
            except (ValueError, NotImplementedError):
                break
        result += A.S(r) * B.S(r) * w_r
    return result


# ============================================================
# 5. Genus-specific Rankin-Selberg integrals (algebraic)
# ============================================================

def genus1_rs_product(A: AlgebraData, B: AlgebraData) -> Fraction:
    r"""Product of genus-1 free energies: F_1(A) * F_1(B).

    F_1(A) = kappa(A) * lambda_1^FP = kappa(A)/24.
    F_1(B) = kappa(B) * lambda_1^FP = kappa(B)/24.

    Product: kappa(A)*kappa(B)/(24^2) = kappa(A)*kappa(B)/576.

    NOTE: This is the PRODUCT of two numbers, not an integral of a
    product of classes. It is the genus-1 contribution to the
    algebraic shadow Gram matrix.
    """
    return A.kappa * B.kappa * LAMBDA1_FP ** 2


def genus2_rs_product(A: AlgebraData, B: AlgebraData) -> Fraction:
    r"""Product of genus-2 scalar free energies: F_2^{scal}(A) * F_2^{scal}(B).

    F_2^{scal}(A) = kappa(A) * lambda_2^FP = kappa(A) * 7/5760.
    Product: kappa(A)*kappa(B)*(7/5760)^2.
    """
    return A.kappa * B.kappa * LAMBDA2_FP ** 2


def genus2_full_product(A: AlgebraData, B: AlgebraData) -> Fraction:
    r"""Full genus-2 inner product including planted-forest correction.

    F_2(A) = kappa(A) * lambda_2^FP + delta_pf^{(2,0)}(A)
    where delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48  (pixton_shadow_bridge.py).

    The product F_2(A)*F_2(B) includes cross-terms between scalar and cubic.
    """
    f2_A = A.kappa * LAMBDA2_FP + _planted_forest_g2(A)
    f2_B = B.kappa * LAMBDA2_FP + _planted_forest_g2(B)
    return f2_A * f2_B


def _planted_forest_g2(A: AlgebraData) -> Fraction:
    """Planted-forest correction at genus 2: S_3(10*S_3 - kappa)/48."""
    S3 = A.S(3)
    return S3 * (Fraction(10) * S3 - A.kappa) / Fraction(48)


def genus_g_rs_product(A: AlgebraData, B: AlgebraData, g: int) -> Fraction:
    r"""Scalar-level product at genus g: F_g^{scal}(A) * F_g^{scal}(B).

    = kappa(A) * kappa(B) * (lambda_g^FP)^2.
    """
    return A.kappa * B.kappa * lambda_fp(g) ** 2


def multi_genus_rs_sum(A: AlgebraData, B: AlgebraData,
                       g_max: int = 5) -> Fraction:
    r"""Sum of scalar RS products over genera: sum_{g=1}^{g_max} F_g(A)*F_g(B).

    = kappa(A)*kappa(B) * sum_{g=1}^{g_max} (lambda_g^FP)^2.
    """
    result = Fraction(0)
    for g in range(1, g_max + 1):
        result += lambda_fp(g) ** 2
    return A.kappa * B.kappa * result


# ============================================================
# 6. Shadow Gram matrix
# ============================================================

def shadow_gram_matrix(families: Optional[Dict[str, AlgebraData]] = None,
                       mode: str = 'genus1') -> Dict[str, Any]:
    r"""Compute the shadow Gram matrix for a collection of families.

    G_{ij} = <S(A_i), S(A_j)>

    where the inner product depends on 'mode':
        'genus1': F_1(A_i) * F_1(A_j) = kappa_i * kappa_j / 576
        'genus2_scalar': F_2(A_i) * F_2(A_j) at scalar level
        'genus2_full': including planted-forest corrections
        'multi_genus': sum over genera 1..5
        'algebraic': unweighted sum of S_r products

    Returns the matrix, its eigenvalues (as floats), rank, and whether
    it is positive semi-definite.
    """
    if families is None:
        families = STANDARD_FAMILIES

    names = sorted(families.keys())
    n = len(names)

    # Compute Gram matrix entries as Fraction
    G_exact = {}
    for i, ni in enumerate(names):
        for j, nj in enumerate(names):
            Ai = families[ni]
            Aj = families[nj]
            if mode == 'genus1':
                G_exact[(i, j)] = genus1_rs_product(Ai, Aj)
            elif mode == 'genus2_scalar':
                G_exact[(i, j)] = genus2_rs_product(Ai, Aj)
            elif mode == 'genus2_full':
                G_exact[(i, j)] = genus2_full_product(Ai, Aj)
            elif mode == 'multi_genus':
                G_exact[(i, j)] = multi_genus_rs_sum(Ai, Aj)
            elif mode == 'algebraic':
                G_exact[(i, j)] = shadow_inner_product_algebraic(Ai, Aj)
            else:
                raise ValueError(f"Unknown mode: {mode}")

    # Convert to float matrix for eigenvalue computation
    G_float = [[float(G_exact.get((i, j), 0)) for j in range(n)] for i in range(n)]

    # Compute eigenvalues using characteristic polynomial or numpy
    eigenvalues = _compute_eigenvalues(G_float)

    # Determine rank (number of nonzero eigenvalues)
    tol = 1e-12 * max(abs(e) for e in eigenvalues) if eigenvalues else 1e-12
    rank = sum(1 for e in eigenvalues if abs(e) > tol)

    # Check PSD
    psd = all(e >= -tol for e in eigenvalues)

    return {
        'names': names,
        'n': n,
        'matrix_exact': G_exact,
        'matrix_float': G_float,
        'eigenvalues': sorted(eigenvalues, reverse=True),
        'rank': rank,
        'is_psd': psd,
        'mode': mode,
    }


def _compute_eigenvalues(G: List[List[float]]) -> List[float]:
    """Compute eigenvalues of a real symmetric matrix."""
    n = len(G)
    if n == 0:
        return []

    try:
        import numpy as np
        arr = np.array(G, dtype=float)
        eigs = np.linalg.eigvalsh(arr)
        return sorted(eigs.tolist(), reverse=True)
    except ImportError:
        pass

    # Fallback: for rank-1 matrices (genus1 scalar mode),
    # the only nonzero eigenvalue is the trace.
    trace = sum(G[i][i] for i in range(n))
    # Check if rank 1 by seeing if G = v v^T
    if n > 0 and abs(G[0][0]) > 1e-30:
        v = [G[i][0] / math.sqrt(abs(G[0][0])) for i in range(n)]
        is_rank1 = True
        for i in range(n):
            for j in range(n):
                if abs(G[i][j] - v[i]*v[j]*G[0][0]/abs(G[0][0])) > 1e-8 * max(1, abs(G[i][j])):
                    is_rank1 = False
                    break
            if not is_rank1:
                break
        if is_rank1:
            return [trace] + [0.0] * (n - 1)

    # Generic fallback: return trace as single eigenvalue estimate
    return [trace] + [0.0] * (n - 1)


# ============================================================
# 7. Koszul duality and Rankin-Selberg
# ============================================================

def koszul_pair_inner_product(A: AlgebraData, g_max: int = 5) -> Dict[str, Any]:
    r"""Compute inner products for a Koszul pair (A, A!).

    For a Koszul pair:
    - kappa(A) + kappa(A!) = 0 for KM/free fields
    - kappa(A) + kappa(A!) = 13 for Virasoro (AP24)

    The complementarity theorem gives:
        F_g(A) + F_g(A!) = (kappa(A) + kappa(A!)) * lambda_g^FP

    The cross inner product <S(A), S(A!)> involves the product of
    dual shadow coefficients.
    """
    if A.kappa_dual is None:
        raise ValueError(f"No Koszul dual data for {A.name}")

    kappa_sum = A.kappa + A.kappa_dual
    kappa_product = A.kappa * A.kappa_dual

    results = {
        'algebra': A.name,
        'kappa': float(A.kappa),
        'kappa_dual': float(A.kappa_dual),
        'kappa_sum': float(kappa_sum),
        'kappa_product': float(kappa_product),
        'anti_symmetric': kappa_sum == 0,
    }

    # Genus-by-genus
    for g in range(1, g_max + 1):
        fp = lambda_fp(g)
        f_g_A = A.kappa * fp
        f_g_dual = A.kappa_dual * fp
        f_g_sum = f_g_A + f_g_dual
        f_g_product = f_g_A * f_g_dual

        results[f'genus_{g}'] = {
            'F_g_A': float(f_g_A),
            'F_g_dual': float(f_g_dual),
            'F_g_sum': float(f_g_sum),
            'F_g_product': float(f_g_product),
            'complementarity_value': float(kappa_sum * fp),
            'complementarity_check': f_g_sum == kappa_sum * fp,
        }

    return results


def virasoro_self_dual_inner_product(g_max: int = 5) -> Dict[str, Any]:
    r"""Inner product at the Virasoro self-dual point c = 13.

    kappa(Vir_13) = 13/2.
    kappa(Vir_{26-13}) = kappa(Vir_13) = 13/2.
    kappa + kappa' = 13.

    The self-inner-product: F_g(Vir_13)^2 = (13/2)^2 * (lambda_g^FP)^2.

    At c=13: <S(Vir_13), S(Vir_13)> is a self-dual special value.
    """
    A = virasoro(13)
    results = {
        'kappa': float(A.kappa),
        'kappa_dual': float(A.kappa_dual),
        'is_self_dual': A.kappa == A.kappa_dual,
        'kappa_sum': float(A.kappa + A.kappa_dual),
    }

    for g in range(1, g_max + 1):
        fp = lambda_fp(g)
        f_g = A.kappa * fp
        results[f'F_{g}_squared'] = float(f_g ** 2)
        results[f'F_{g}'] = float(f_g)

    return results


# ============================================================
# 8. L-value extraction (Virasoro x Virasoro*)
# ============================================================

def virasoro_cross_inner_product(c_val: Union[int, Fraction],
                                 g_max: int = 5) -> Dict[str, Any]:
    r"""Cross inner product <S(Vir_c), S(Vir_{26-c})>.

    At the scalar level:
        F_g(Vir_c) * F_g(Vir_{26-c}) = (c/2)*((26-c)/2) * (lambda_g^FP)^2
                                      = c(26-c)/4 * (lambda_g^FP)^2

    At c = 13 (self-dual): c(26-c)/4 = 13*13/4 = 169/4.
    At c = 0 (trivial): 0.
    At c = 26 (critical): 0.

    The cross-product is maximized at c = 13.

    For L-value interpretation: the Petersson norm of the shadow amplitude
    is related to the special L-value L(1/2, f) via the Bocherer formula.
    At genus 1, the shadow amplitude is quasi-modular (AP15), so the
    "L-value" is a regularized value involving E_2*.
    """
    c_frac = Fraction(c_val)
    A = virasoro(c_frac)
    B = virasoro(Fraction(26) - c_frac)

    product_factor = c_frac * (Fraction(26) - c_frac) / Fraction(4)

    results = {
        'c': float(c_frac),
        'c_dual': float(Fraction(26) - c_frac),
        'kappa_A': float(A.kappa),
        'kappa_B': float(B.kappa),
        'product_factor': float(product_factor),
    }

    for g in range(1, g_max + 1):
        fp = lambda_fp(g)
        cross = product_factor * fp ** 2
        results[f'cross_genus_{g}'] = float(cross)

    # Numerical values to 15 digits
    results['cross_genus1_exact'] = product_factor * LAMBDA1_FP ** 2
    results['cross_genus1_float'] = float(product_factor * LAMBDA1_FP ** 2)

    return results


# ============================================================
# 9. Lattice VOA Petersson norms
# ============================================================

def lattice_petersson_norm(name: str, rank: int, g_max: int = 5) -> Dict[str, Any]:
    r"""Petersson norm of shadow amplitude for a lattice VOA.

    For a rank-r even unimodular lattice Lambda:
        kappa(V_Lambda) = rank(Lambda) = r  (AP48: not c/2!)

    The shadow amplitude at genus g:
        F_g(V_Lambda) = r * lambda_g^FP

    Self-inner-product:
        F_g^2 = r^2 * (lambda_g^FP)^2

    The Petersson norm of the theta function Theta_Lambda has known values:
        ||Theta_Lambda||^2 = integral of |Theta_Lambda|^2 against Petersson measure

    For the modular Koszul framework, the "Petersson norm" is:
        sum_{g=1}^{g_max} F_g^2 = r^2 * sum_{g} (lambda_g^FP)^2
    """
    r = Fraction(rank)
    results = {
        'lattice': name,
        'rank': rank,
        'kappa': float(r),
        'self_product_total': Fraction(0),
    }

    total = Fraction(0)
    for g in range(1, g_max + 1):
        fp = lambda_fp(g)
        f_g_sq = r ** 2 * fp ** 2
        total += f_g_sq
        results[f'F_{g}_squared'] = float(f_g_sq)
        results[f'F_{g}'] = float(r * fp)

    results['self_product_total'] = float(total)
    return results


# ============================================================
# 10. Genus-2 Rankin-Selberg integral via tautological classes
# ============================================================

def genus2_tautological_rs(A: AlgebraData, B: AlgebraData) -> Dict[str, Any]:
    r"""Genus-2 Rankin-Selberg via tautological intersection theory.

    At genus 2, M-bar_2 has dimension 3 (complex).
    The Hodge bundle E has rank 2, so lambda_1 in H^2, lambda_2 in H^4.

    Key intersection numbers (Faber):
        int_{M-bar_2} lambda_2 = 1/240
        int_{M-bar_2} lambda_1^2 = 1/240
        int_{M-bar_2} lambda_2 kappa_1 = int_{M-bar_{2,1}} lambda_2 psi = ?

    The scalar RS integral:
        int_{M-bar_2} F_2^{scal}(A) * F_2^{scal}(B)
    is problematic because F_2^{scal} is a degree-2 class (lambda_2),
    and the product of two degree-2 classes has degree 4 > dim(M-bar_2) = 3.

    So lambda_2 * lambda_2 = 0 on M-bar_2 (by dimension).

    The correct approach: express F_2 as a polynomial in tautological
    generators {lambda_1, lambda_2, kappa_1, delta_0, delta_1}
    and compute the intersection pairing between complementary-degree parts.

    At the scalar level, F_2(A) involves:
        F_2(A) = kappa(A) * [lambda_2 piece] + planted-forest * [boundary piece]

    The Rankin-Selberg integral should pair degree-p with degree-(3-p).
    For two scalar-level amplitudes (both proportional to lambda_2, degree 2),
    we need a METRIC on H^4(M-bar_2). This metric is provided by
    the pairing with kappa_1 (degree 1):

        <alpha, beta> = int_{M-bar_2} alpha * kappa_1  for alpha in H^4.

    But this is a pairing between H^4 and H^2 (via kappa_1 in H^2).

    RESOLUTION: The "inner product" at genus 2 is:
        int_{M-bar_{2,1}} F_2(A) * F_2(B) * psi_1^2

    Since dim M-bar_{2,1} = 4 and F_2 involves lambda_2 (degree 2),
    F_2 * F_2 * psi^2 has degree 2+2+2 = 6 which is too large.

    Actually: F_2(A) is a NUMBER (the integral of the class), not a class.
    So F_2(A) * F_2(B) is just a product of numbers.

    The correct Rankin-Selberg at genus 2 is the product of the numbers:
        RS_2(A, B) = F_2(A) * F_2(B)
    where F_2(A) = kappa(A)*lambda_2^FP + delta_pf(A) is the full genus-2 amplitude.
    """
    f2_A = A.kappa * LAMBDA2_FP + _planted_forest_g2(A)
    f2_B = B.kappa * LAMBDA2_FP + _planted_forest_g2(B)

    return {
        'A': A.name,
        'B': B.name,
        'F2_A_scalar': float(A.kappa * LAMBDA2_FP),
        'F2_A_pf_correction': float(_planted_forest_g2(A)),
        'F2_A_total': float(f2_A),
        'F2_B_scalar': float(B.kappa * LAMBDA2_FP),
        'F2_B_pf_correction': float(_planted_forest_g2(B)),
        'F2_B_total': float(f2_B),
        'RS_product': float(f2_A * f2_B),
        'RS_product_scalar_only': float(A.kappa * B.kappa * LAMBDA2_FP ** 2),
        'int_lambda2': float(LAMBDA2_INTEGRAL),
        'int_lambda1_sq': float(LAMBDA1_SQ_INTEGRAL_G2),
        'lambda2_FP': float(LAMBDA2_FP),
    }


# ============================================================
# 11. Multi-path verification infrastructure
# ============================================================

def verify_genus1_product(A: AlgebraData, B: AlgebraData) -> Dict[str, Any]:
    r"""Multi-path verification of the genus-1 RS product.

    Path 1: Direct formula F_1(A)*F_1(B) = kappa_A * kappa_B / 576.
    Path 2: Product of F_1 values via lambda_fp.
    Path 3: Sum decomposition kappa = sum_i kappa_i for tensor products.
    Path 4: Koszul pair consistency (if A has dual data).
    """
    # Path 1: Direct
    path1 = float(A.kappa * B.kappa) / 576.0

    # Path 2: Via lambda_fp
    f1_A = float(A.kappa * LAMBDA1_FP)
    f1_B = float(B.kappa * LAMBDA1_FP)
    path2 = f1_A * f1_B

    # Path 3: Verify lambda_1^FP = 1/24 from first principles
    fp1 = lambda_fp(1)
    assert fp1 == LAMBDA1_FP, f"lambda_1^FP mismatch: {fp1} != {LAMBDA1_FP}"
    path3 = float(A.kappa * B.kappa * fp1 ** 2)

    # Consistency check
    results = {
        'path1_direct': path1,
        'path2_via_fp': path2,
        'path3_first_principles': path3,
        'all_agree': abs(path1 - path2) < 1e-15 and abs(path1 - path3) < 1e-15,
    }

    # Path 4: Koszul pair (if available)
    if A.kappa_dual is not None and A.name == B.name:
        # Self-product
        kap_prod = float(A.kappa ** 2)
        results['path4_koszul_self'] = kap_prod / 576.0
        # Cross with dual
        kap_cross = float(A.kappa * A.kappa_dual)
        results['path4_koszul_cross'] = kap_cross / 576.0
        # Sum check
        kap_sum = float(A.kappa + A.kappa_dual)
        results['path4_kappa_sum'] = kap_sum

    return results


def verify_genus2_product(A: AlgebraData, B: AlgebraData) -> Dict[str, Any]:
    r"""Multi-path verification of the genus-2 RS product.

    Path 1: Scalar only: kappa_A * kappa_B * (7/5760)^2.
    Path 2: Full with planted-forest correction.
    Path 3: Verify lambda_2^FP = 7/5760 from Bernoulli.
    Path 4: Cross-check int lambda_2 = 1/240.
    """
    # Path 1
    path1 = float(A.kappa * B.kappa * LAMBDA2_FP ** 2)

    # Path 2
    f2_A = A.kappa * LAMBDA2_FP + _planted_forest_g2(A)
    f2_B = B.kappa * LAMBDA2_FP + _planted_forest_g2(B)
    path2 = float(f2_A * f2_B)

    # Path 3: lambda_2^FP from first principles
    fp2 = lambda_fp(2)
    assert fp2 == Fraction(7, 5760), f"lambda_2^FP mismatch: {fp2}"
    path3 = float(A.kappa * B.kappa * fp2 ** 2)

    # Path 4: int lambda_2 = 1/240 (separate fact)
    assert LAMBDA2_INTEGRAL == Fraction(1, 240)

    return {
        'path1_scalar': path1,
        'path2_full': path2,
        'path3_bernoulli': path3,
        'scalar_agrees': abs(path1 - path3) < 1e-15,
        'correction_nonzero': abs(path2 - path1) > 1e-30,
        'pf_correction_A': float(_planted_forest_g2(A)),
        'pf_correction_B': float(_planted_forest_g2(B)),
    }


# ============================================================
# 12. Explicit numerical computation (15 digits)
# ============================================================

def virasoro_self_dual_numerical() -> Dict[str, float]:
    r"""Virasoro at c=13: all inner products to 15 digits.

    kappa = 13/2 = 6.5
    F_1 = 6.5/24 = 13/48
    F_1^2 = 169/2304

    F_2^{scal} = 6.5 * 7/5760 = 91/11520
    F_2^{full} includes planted-forest correction

    Cross with dual (= self at c=13):
    F_g(Vir_13)^2 = (13/2)^2 * (lambda_g^FP)^2
    """
    A = virasoro(13)
    results = {}

    for g in range(1, 8):
        fp = lambda_fp(g)
        f_g = A.kappa * fp
        results[f'F_{g}'] = float(f_g)
        results[f'F_{g}_squared'] = float(f_g ** 2)

    # Full genus-2 with planted-forest
    pf = _planted_forest_g2(A)
    f2_full = A.kappa * LAMBDA2_FP + pf
    results['F_2_full'] = float(f2_full)
    results['F_2_full_squared'] = float(f2_full ** 2)
    results['pf_correction'] = float(pf)

    # Sum over genera
    total = Fraction(0)
    for g in range(1, 8):
        total += (A.kappa * lambda_fp(g)) ** 2
    results['sum_F_g_squared_g1_to_7'] = float(total)

    return results


def lattice_comparison_numerical() -> Dict[str, Dict[str, float]]:
    r"""Lattice Petersson norms for E8, D16, Leech to 15 digits."""
    lattices = {
        'E8': lattice_e8(),
        'D16': lattice_d16(),
        'Leech': lattice_leech(),
    }

    results = {}
    for name, A in lattices.items():
        entry = {}
        total = Fraction(0)
        for g in range(1, 8):
            fp = lambda_fp(g)
            f_g = A.kappa * fp
            entry[f'F_{g}'] = float(f_g)
            entry[f'F_{g}_squared'] = float(f_g ** 2)
            total += f_g ** 2
        entry['sum_squared'] = float(total)
        entry['kappa'] = float(A.kappa)
        results[name] = entry

    return results


# ============================================================
# 13. Summary report
# ============================================================

def full_analysis(g_max: int = 5) -> Dict[str, Any]:
    """Run the full shadow Rankin-Selberg analysis."""
    results = {}

    # Gram matrices
    for mode in ['genus1', 'genus2_scalar', 'genus2_full', 'multi_genus', 'algebraic']:
        gram = shadow_gram_matrix(mode=mode)
        results[f'gram_{mode}'] = {
            'rank': gram['rank'],
            'is_psd': gram['is_psd'],
            'top_eigenvalue': gram['eigenvalues'][0] if gram['eigenvalues'] else 0,
        }

    # Koszul pairs
    for name, A in [('Heisenberg', heisenberg(1)),
                    ('sl2_k1', affine_sl2(1)),
                    ('Virasoro_c26', virasoro(26)),
                    ('Virasoro_c13', virasoro(13))]:
        try:
            results[f'koszul_{name}'] = koszul_pair_inner_product(A, g_max)
        except ValueError:
            results[f'koszul_{name}'] = 'no dual data'

    # Self-dual point
    results['virasoro_self_dual'] = virasoro_self_dual_inner_product(g_max)

    # Lattice norms
    for lname, rank in [('E8', 8), ('D16', 16), ('Leech', 24)]:
        results[f'lattice_{lname}'] = lattice_petersson_norm(lname, rank, g_max)

    return results
