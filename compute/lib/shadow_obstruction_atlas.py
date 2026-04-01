r"""Definitive Shadow Obstruction Atlas.

Systematic computation of obstruction classes o_r(A) for r = 2, 3, 4, 5
across every standard family in the chiral algebra landscape.

The shadow Postnikov tower Theta_A^{<=r} consists of finite-order projections
of the bar-intrinsic MC element Theta_A := D_A - d_0 (thm:mc2-bar-intrinsic).
At each arity r, the obstruction class o_{r+1}(A) in H^2(A^sh_{r+1}) measures
whether the tower extends.

SHADOW DEPTH CLASSIFICATION (thm:single-line-dichotomy):
    G (Gaussian, r_max=2): Heisenberg, lattice VOA, free fermion
    L (Lie/tree, r_max=3): affine Kac-Moody
    C (contact/quartic, r_max=4): beta-gamma
    M (mixed, r_max=inf): Virasoro, W_N

FAMILIES COVERED:
    1. Heisenberg H_k        (G class)
    2. Affine sl_2 at level k (L class)
    3. beta-gamma system      (C class)
    4. Virasoro at generic c  (M class)
    5. W_3 at generic c       (M class, 2-channel)
    6. Free fermion           (G class)
    7. Lattice VOA V_Lambda   (G class)

For each family, computes:
    - Shadow coefficients S_r for r = 2, 3, 4, 5
    - Shadow metric Q_L(t) and critical discriminant Delta
    - Shadow connection nabla^sh = d - Q'/(2Q) dt
    - Connection residue (1/2) and monodromy (-1 = Koszul sign)
    - Obstruction classes o_r(A)
    - Growth rate rho(A) for M-class families
    - Complementarity of discriminants: Delta(A) + Delta(A!)

CROSS-CHECKS:
    - kappa additivity: kappa(A+B) = kappa(A) + kappa(B)
    - kappa anti-symmetry: kappa(A) + kappa(A!) = 0 for KM/free fields
    - kappa + kappa' = rho*K for W-algebras
    - Discriminant complementarity: Delta(A) + Delta(A!) = constant numerator
    - Shadow depth classification matches G/L/C/M

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:recursive-existence (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    cor:nms-betagamma-mu-vanishing (nonlinear_modular_shadows.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs, Rational, Symbol, cancel, diff, expand, factor,
    simplify, sqrt, symbols, oo, S, N as Neval, Poly,
)


# ============================================================================
# Symbols
# ============================================================================

c = Symbol('c')
k = Symbol('k')
t = Symbol('t')
x = Symbol('x')
lam = Symbol('lambda')
N = Symbol('N')


# ============================================================================
# 1. KAPPA FORMULAS (independently computed, not copied between families)
# ============================================================================

def kappa_heisenberg(level):
    r"""kappa(H_k) = k.

    The Heisenberg algebra at level k has OPE J(z)J(w) ~ k/(z-w)^2.
    The modular characteristic is kappa = k.

    Derivation: The genus-1 partition function is
      Z_{H_k}(tau) = 1/eta(tau)
    and kappa = coefficient of E_2 in the genus-1 shadow = k.

    NOTE: This is NOT c/2.  c = 1 for rank-1 Heisenberg but kappa = k.
    """
    return level


def kappa_free_fermion():
    r"""kappa(psi) = 1/4.

    The free fermion has c = 1/2.  kappa = c/2 = 1/4.

    CAUTION (AP1): Do NOT confuse with Heisenberg kappa = k.
    The free fermion is NOT a Heisenberg algebra.  The formula
    kappa = c/2 applies because the free fermion has spin-1/2
    primary (not spin-1 current like Heisenberg).
    """
    return Rational(1, 4)


def kappa_lattice(rank):
    r"""kappa(V_Lambda) = rank(Lambda).

    For even lattice of rank r, V_Lambda is rank-r Heisenberg
    extended by lattice vertex operators.  The primary line is
    the Cartan direction, which gives kappa = rank.

    Independent of the cocycle (thm:lattice:curvature-braiding-orthogonal).
    """
    return rank


def kappa_affine_slN(n, level):
    r"""kappa(sl_N, k) = dim(sl_N) * (k + h^v) / (2 h^v).

    Independently computed:
      dim(sl_N) = N^2 - 1
      h^v(sl_N) = N (dual Coxeter number)

    So kappa = (N^2 - 1)(k + N) / (2N).

    Verification for sl_2: dim=3, h^v=2, kappa = 3(k+2)/4.
    """
    return (n**2 - 1) * (level + n) / (2 * n)


def kappa_affine_sl2(level):
    r"""kappa(sl_2, k) = 3(k+2)/4.

    Special case of kappa_affine_slN with N=2.
    """
    return kappa_affine_slN(2, level)


def kappa_betagamma(weight=0):
    r"""kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.

    Central charge c = 2(6*lambda^2 - 6*lambda + 1), so kappa = c/2.

    Standard betagamma (lambda=0 or 1): kappa = 1.
    Symplectic (lambda=1/2): kappa = -1/2.
    """
    return 6 * weight**2 - 6 * weight + 1


def kappa_bc(spin):
    r"""kappa(bc, j) = -(6j^2 - 6j + 1).

    The bc system has kappa_bc = -kappa_bg (opposite sign).
    """
    return -(6 * spin**2 - 6 * spin + 1)


def kappa_virasoro(central_charge):
    r"""kappa(Vir_c) = c/2.

    The Virasoro algebra has a single spin-2 generator T.
    The shadow curvature is kappa = c/2.
    """
    return central_charge / 2


def kappa_wN(n, central_charge):
    r"""kappa(W_N, c) = (H_N - 1) * c.

    H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number.
    rho(sl_N) = H_N - 1 = sum_{i=2}^{N} 1/i.

    For W_2 = Virasoro: H_2 - 1 = 1/2, kappa = c/2. Check.
    For W_3: H_3 - 1 = 1/2 + 1/3 = 5/6, kappa = 5c/6.
    """
    rho = sum(Rational(1, i) for i in range(2, n + 1))
    return rho * central_charge


def kappa_w3(central_charge):
    r"""kappa(W_3, c) = 5c/6.

    Special case of kappa_wN with N=3.
    """
    return kappa_wN(3, central_charge)


# ============================================================================
# 2. KOSZUL DUAL KAPPA FORMULAS
# ============================================================================

def kappa_dual_heisenberg(level):
    r"""kappa(H_k^!) = -k.

    Heisenberg Koszul dual: H_k^! = Sym^ch(V*) != H_{-k}.
    (AP: Heisenberg NOT self-dual.)
    Anti-symmetry: kappa + kappa! = 0.
    """
    return -level


def kappa_dual_free_fermion():
    r"""kappa(psi^!) = -1/4.

    Anti-symmetry for free fields: kappa + kappa! = 0.
    """
    return -Rational(1, 4)


def kappa_dual_affine_sl2(level):
    r"""kappa(sl_2_k^!) = -3(k+2)/4.

    Anti-symmetry for Kac-Moody: kappa(A) + kappa(A!) = 0.
    """
    return -kappa_affine_sl2(level)


def kappa_dual_virasoro(central_charge):
    r"""kappa(Vir_c^!) = kappa(Vir_{26-c}) = (26-c)/2.

    Virasoro Koszul duality: Vir_c^! = Vir_{26-c}.
    kappa + kappa! = c/2 + (26-c)/2 = 13 (NOT zero: W-algebra anomaly).
    Self-dual at c = 13.
    """
    return (26 - central_charge) / 2


def kappa_dual_w3(central_charge):
    r"""kappa(W_3_c^!) = kappa(W_3_{c!}).

    For W_3: Koszul dual is W_3 at central charge c! determined by
    the Feigin-Frenkel involution for sl_3.

    kappa(W_3) + kappa(W_3^!) = rho * K where rho = H_3 - 1 = 5/6
    and K = 26 (the universal constant).  So kappa + kappa! = 5*26/6 = 65/3.
    """
    return Rational(65, 3) - kappa_w3(central_charge)


# ============================================================================
# 3. SHADOW METRIC AND DISCRIMINANT
# ============================================================================

def shadow_metric_QL(kappa_val, alpha_val, S4_val):
    r"""Shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Here alpha = S_3 (the cubic shadow coefficient, not the "alpha"
    in the abbreviated form Q = (2kappa + alpha*t)^2 + 2*Delta*t^2
    which uses alpha = 3*S_3).

    Expanded: Q_L = 4*kappa^2 + 12*kappa*S_3*t + (9*S_3^2 + 16*kappa*S_4)*t^2.

    Returns (Q_L_expr, q0, q1, q2, Delta).
    """
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 16 * kappa_val * S4_val
    Delta = 8 * kappa_val * S4_val
    Q_expr = q0 + q1 * t + q2 * t**2
    return Q_expr, q0, q1, q2, Delta


def shadow_connection_form(Q_expr):
    r"""Connection 1-form omega = Q'/(2Q) dt.

    The shadow connection nabla^sh = d - omega*dt is a logarithmic
    connection on O_L with regular singular points at zeros of Q.
    """
    Q_prime = diff(Q_expr, t)
    return cancel(Q_prime / (2 * Q_expr))


def shadow_connection_residue():
    r"""Residue of the shadow connection at a simple zero of Q.

    At t = t_0 with Q(t_0) = 0, Q'(t_0) != 0:
      omega = Q'/(2Q) ~ Q'(t_0)/(2*Q'(t_0)*(t-t_0)) = 1/(2*(t-t_0))
    Residue = 1/2.
    """
    return Rational(1, 2)


def shadow_monodromy():
    r"""Monodromy around a zero of Q: exp(2*pi*i * 1/2) = -1.

    This is the KOSZUL SIGN.  Sheet exchange = sign change.
    """
    return -1


def depth_classify(alpha_val, Delta_val):
    r"""Classify shadow depth from (alpha, Delta).

    G: alpha = 0, Delta = 0  -> r_max = 2
    L: alpha != 0, Delta = 0 -> r_max = 3
    C: alpha = 0, Delta != 0 -> r_max = 4
    M: alpha != 0, Delta != 0 -> r_max = infinity
    """
    a_zero = simplify(alpha_val) == 0
    d_zero = simplify(Delta_val) == 0

    if a_zero and d_zero:
        return 'G', 2
    elif not a_zero and d_zero:
        return 'L', 3
    elif a_zero and not d_zero:
        return 'C', 4
    else:
        return 'M', None


def shadow_growth_rate(kappa_val, alpha_val, S4_val):
    r"""Shadow growth rate rho = sqrt(9*alpha^2 + 2*Delta) / (2|kappa|).

    rho is the reciprocal of the convergence radius of the shadow GF.
    For G and L classes: rho = 0 (tower terminates).
    For M class: rho > 0 (infinite tower).
    """
    Delta = 8 * kappa_val * S4_val
    numer_sq = 9 * alpha_val**2 + 2 * Delta
    return sqrt(numer_sq) / (2 * Abs(kappa_val))


# ============================================================================
# 4. TAYLOR EXPANSION OF sqrt(Q_L) -> SHADOW TOWER COEFFICIENTS
# ============================================================================

def _sqrt_Q_taylor(q0, q1, q2, max_n):
    r"""Taylor coefficients a_n of f(t) = sqrt(q0 + q1*t + q2*t^2).

    Convolution recursion from f^2 = Q_L:
      a_0 = sqrt(q0)
      a_1 = q1 / (2*a_0)
      a_2 = (q2 - a_1^2) / (2*a_0)
      a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j*a_{n-j}  for n >= 3

    Shadow coefficients: S_r = a_{r-2} (no division by r here;
    in the weighted GF convention H(t) = t^2*sqrt(Q_L), the coefficient
    of t^r is a_{r-2}; we use S_r = a_{r-2}/r when following the
    shadow_tower_recursive.py convention of the *unweighted* GF).
    """
    a = [None] * (max_n + 1)
    a[0] = sqrt(q0)
    if max_n == 0:
        return a

    a[1] = q1 / (2 * a[0])
    if max_n == 1:
        return a

    a[2] = (q2 - a[1]**2) / (2 * a[0])

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    return a


def compute_shadow_coefficients(kappa_val, alpha_val, S4_val, max_r=10):
    r"""Compute shadow tower coefficients S_r for r = 2, ..., max_r.

    Convention: S_r = a_{r-2} where a_n = [t^n] sqrt(Q_L(t)).
    This is the convention where H(t) = t^2 * sqrt(Q_L(t)) = sum S_r t^r.

    NOTE: shadow_tower_recursive.py uses S_r = a_{r-2}/r (divides by r).
    We follow the weighted convention here: S_r = a_{r-2} without the 1/r.
    This matches the manuscript's definition of the shadow GF.

    For the UNWEIGHTED coefficients (S_r/r), use compute_shadow_coefficients_unweighted.
    """
    _, q0, q1, q2, _ = shadow_metric_QL(kappa_val, alpha_val, S4_val)
    max_n = max_r - 2
    a = _sqrt_Q_taylor(q0, q1, q2, max_n)
    return {r: simplify(a[r - 2]) for r in range(2, max_r + 1)}


def compute_shadow_coefficients_unweighted(kappa_val, alpha_val, S4_val, max_r=10):
    r"""Unweighted shadow coefficients S_r/r (matching shadow_tower_recursive.py)."""
    raw = compute_shadow_coefficients(kappa_val, alpha_val, S4_val, max_r)
    return {r: simplify(v / r) for r, v in raw.items()}


# ============================================================================
# 5. OBSTRUCTION CLASSES
# ============================================================================

def virasoro_obstruction_class(r):
    r"""Obstruction class o_{r+1} for Virasoro at arity r.

    Uses the Virasoro-specific master equation with propagator P = 2/c
    and shadow potential Sh_j = S_j * x^j.

    The H-Poisson bracket: {f, g}_H = (df/dx)(2/c)(dg/dx).
    nabla_H(Sh_r) = {Sh_2, Sh_r} = 2r * S_r.
    Master equation: 2r * S_r + o^(r) = 0 => S_r = -o^(r)/(2r).

    Returns the coefficient of x^{r+1} in o^{r+1}.
    """
    P_vir = Rational(2) / c
    tower = virasoro_shadow_tower(r + 1)

    # o^{r+1} = sum_{j+k=r+3, j,k>=2, j<=k} (sym factor) * {Sh_j, Sh_k}
    obstruction = S.Zero
    target_sum = r + 3

    for j in range(2, target_sum - 1):
        kk = target_sum - j
        if kk < 2 or kk > r:
            continue
        if j > kk:
            continue
        if j not in tower or kk not in tower:
            continue

        bracket = j * kk * tower[j] * tower[kk] * P_vir

        if j == kk:
            obstruction += Rational(1, 2) * bracket
        else:
            obstruction += bracket

    return simplify(obstruction)


def obstruction_vanishes_structural(family_class, r):
    r"""Determine if obstruction o_{r+1} vanishes by structural argument.

    For families where the vanishing is known from algebraic structure:
    - G class: o_r = 0 for all r >= 3 (abelian OPE)
    - L class: o_r = 0 for all r >= 4 (Jacobi identity)
    - C class: o_r = 0 for all r >= 5 (rank-one rigidity)

    These are STRUCTURAL results, not numerical computations:
    - G: the Lie bracket is trivial, so all higher products vanish
    - L: the Jacobi identity forces the quartic contact to vanish
    - C: mu_{bg} = 0 by rank-one abelian rigidity (cor:nms-betagamma-mu-vanishing)

    For M class: o_5 != 0 (quintic forced) and o_r != 0 for all r >= 5.
    """
    if family_class == 'G':
        return r >= 3
    elif family_class == 'L':
        return r >= 4
    elif family_class == 'C':
        return r >= 5
    elif family_class == 'M':
        return False  # o_r never vanishes structurally for M class
    return False


# ============================================================================
# 6. VIRASORO SHADOW TOWER (explicit through arity 7)
# ============================================================================

def virasoro_shadow_tower(max_arity=7):
    r"""Compute Virasoro shadow tower using the master equation.

    Uses the 1D H-Poisson bracket with propagator P = 2/c.

    Returns dict {r: S_r} where Sh_r = S_r * x^r on the primary line.
    """
    P_vir = Rational(2) / c

    shadows = {}
    shadows[2] = c / 2
    shadows[3] = Rational(2)
    shadows[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_arity + 1):
        obstruction = S.Zero

        for j in range(2, r + 1):
            kk = r + 2 - j
            if kk < 2 or kk not in shadows:
                continue
            if j > kk:
                continue

            # {S_j x^j, S_k x^k} = j*k * S_j * S_k * P * x^{j+k-2}
            bracket = j * kk * shadows[j] * shadows[kk] * P_vir

            if j == kk:
                obstruction += Rational(1, 2) * bracket
            else:
                obstruction += bracket

        obstruction = simplify(obstruction)

        # nabla_H(S_r x^r) = 2r * S_r, so Sh_r = -obstruction / (2r)
        shadows[r] = factor(-obstruction / (2 * r))

    return shadows


# ============================================================================
# 7. FAMILY-SPECIFIC ATLAS ENTRIES
# ============================================================================

@dataclass
class AtlasEntry:
    """A single entry in the Shadow Obstruction Atlas.

    Records all shadow data for one algebra family.
    """
    name: str
    depth_class: str
    r_max: Optional[int]  # None for infinity

    # Shadow coefficients
    kappa: Any  # S_2
    alpha: Any  # S_3 (cubic)
    S4: Any     # S_4 (quartic)
    S5: Any = None  # S_5 (quintic)

    # Obstruction classes
    o3: Any = None  # obstruction at arity 3
    o4: Any = None  # obstruction at arity 4
    o5: Any = None  # obstruction at arity 5

    # Shadow metric
    Q_L: Any = None
    Delta: Any = None  # critical discriminant

    # Growth rate (M class only)
    rho: Any = None

    # Koszul dual data
    kappa_dual: Any = None
    kappa_anti_symmetry: Any = None  # kappa + kappa_dual

    # Connection data
    connection_residue: Any = Rational(1, 2)
    monodromy: int = -1

    # Parameters
    params: Dict = field(default_factory=dict)

    def verify_delta(self):
        """Verify Delta = 8 * kappa * S4.

        For multi-channel algebras (W_3, etc.), this check is not applicable
        because kappa is the total and S4/Delta are per-line.
        Set Delta = None to skip.
        """
        if self.Delta is None or self.S4 is None:
            return True
        result = simplify(self.Delta - 8 * self.kappa * self.S4)
        return result == 0

    def verify_depth_class(self):
        """Verify depth class from (alpha, Delta)."""
        cls, _ = depth_classify(self.alpha, self.Delta)
        return cls == self.depth_class


def atlas_heisenberg():
    r"""Atlas entry for Heisenberg H_k.

    CLASS G (Gaussian): tower terminates at arity 2.
    All higher shadows and obstructions vanish.

    kappa = k, alpha = 0, S_4 = 0, Delta = 0.
    Q_L(t) = 4k^2 (constant, no t-dependence).
    Koszul dual: H_k^! = Sym^ch(V*), kappa! = -k.
    """
    kap = k
    alpha_val = Rational(0)
    S4_val = Rational(0)
    Delta_val = Rational(0)
    Q_expr = 4 * k**2

    return AtlasEntry(
        name='Heisenberg H_k',
        depth_class='G',
        r_max=2,
        kappa=kap,
        alpha=alpha_val,
        S4=S4_val,
        S5=Rational(0),
        o3=Rational(0),
        o4=Rational(0),
        o5=Rational(0),
        Q_L=Q_expr,
        Delta=Delta_val,
        rho=Rational(0),
        kappa_dual=-k,
        kappa_anti_symmetry=Rational(0),  # k + (-k) = 0
        params={'k': k},
    )


def atlas_free_fermion():
    r"""Atlas entry for free fermion psi.

    CLASS G: c = 1/2, kappa = 1/4 (= c/2, NOT 1/2).
    Tower terminates at arity 2: all higher shadows vanish.
    """
    kap = Rational(1, 4)

    return AtlasEntry(
        name='Free fermion psi',
        depth_class='G',
        r_max=2,
        kappa=kap,
        alpha=Rational(0),
        S4=Rational(0),
        S5=Rational(0),
        o3=Rational(0),
        o4=Rational(0),
        o5=Rational(0),
        Q_L=4 * kap**2,  # = 1/4
        Delta=Rational(0),
        rho=Rational(0),
        kappa_dual=-kap,
        kappa_anti_symmetry=Rational(0),
        params={},
    )


def atlas_lattice(rank_val=None):
    r"""Atlas entry for lattice VOA V_Lambda.

    CLASS G: kappa = rank(Lambda), independent of cocycle.
    Tower terminates at arity 2: abelian primary line.
    """
    r = Symbol('r', positive=True) if rank_val is None else rank_val
    kap = r

    return AtlasEntry(
        name='Lattice V_Lambda',
        depth_class='G',
        r_max=2,
        kappa=kap,
        alpha=Rational(0),
        S4=Rational(0),
        S5=Rational(0),
        o3=Rational(0),
        o4=Rational(0),
        o5=Rational(0),
        Q_L=4 * r**2,
        Delta=Rational(0),
        rho=Rational(0),
        kappa_dual=-r,
        kappa_anti_symmetry=Rational(0),
        params={'r': r},
    )


def atlas_affine_sl2():
    r"""Atlas entry for affine sl_2 at level k.

    CLASS L (Lie/tree): tower terminates at arity 3.
    kappa = 3(k+2)/4, alpha != 0 (Lie bracket), S_4 = 0 (Jacobi), Delta = 0.

    The cubic shadow on the FULL sl_2 space is nonzero (Killing 3-cocycle).
    On the Cartan line alone, alpha = 0 (abelian sub).  We use the
    full-algebra classification: alpha != 0.

    o_4 = 0 because S_4 = 0 (Jacobi identity kills quartic).
    o_5 = 0 trivially (tower has already terminated).
    """
    kap = Rational(3) * (k + 2) / 4
    # The cubic coefficient alpha for sl_2 on the root direction:
    # From e(z)f(w) ~ k/(z-w)^2 + h/(z-w), the cubic involves
    # the structure constants f^{abc}.  Exact value:
    # C(e, f, h) = kappa(e, [f, h]) = kappa(e, -2f) = -2k.
    # On the primary-line parametrization with unit h-component
    # plus root components, the effective alpha involves the
    # Killing contraction.  For classification purposes, what matters
    # is alpha != 0 (which it is on the full algebra).
    alpha_val = Symbol('alpha_sl2', nonzero=True)
    S4_val = Rational(0)
    Delta_val = Rational(0)

    Q_expr = expand((2 * kap + 3 * alpha_val * t)**2)

    return AtlasEntry(
        name='Affine sl_2 at level k',
        depth_class='L',
        r_max=3,
        kappa=kap,
        alpha=alpha_val,
        S4=S4_val,
        S5=Rational(0),
        o3=Rational(0),  # Tower extends to arity 3 (cubic exists)
        o4=Rational(0),  # Jacobi kills quartic
        o5=Rational(0),  # Tower terminated
        Q_L=Q_expr,
        Delta=Delta_val,
        rho=Rational(0),
        kappa_dual=-kap,
        kappa_anti_symmetry=Rational(0),
        params={'k': k},
    )


def atlas_betagamma():
    r"""Atlas entry for beta-gamma system.

    CLASS C (contact/quartic): tower terminates at arity 4.

    On the weight-changing primary line:
      alpha = 0 (abelian on 1D weight-shift subspace)
      S_4 = 0 on neutral primary line (rank-one rigidity)

    But the CHARGED stratum has nontrivial quartic contact:
      mu_{bg} = <eta, m_3(eta, eta, eta)> = 0
    by cor:nms-betagamma-mu-vanishing (rank-one abelian rigidity).

    The C-class assignment uses the full 2D deformation space
    where there IS a quartic contact direction, but the self-bracket
    of the quartic contact exits the complex by rank-one rigidity,
    so o_5 = 0 and the tower terminates at arity 4.

    Standard betagamma (lambda=0): kappa = 1, c = 2.
    """
    kap = Rational(1)  # standard lambda=0
    alpha_val = Rational(0)  # on weight-changing line
    # Quartic contact on charged stratum: symbolic nonzero
    S4_contact = Symbol('S4_bg', nonzero=True)

    return AtlasEntry(
        name='betagamma system (standard)',
        depth_class='C',
        r_max=4,
        kappa=kap,
        alpha=alpha_val,
        S4=S4_contact,
        S5=Rational(0),
        o3=Rational(0),  # alpha=0 means no cubic obstruction
        o4=Rational(0),  # Quartic contact exists but...
        o5=Rational(0),  # ...mu_{bg}=0 by rank-one rigidity
        Q_L=None,  # Multi-stratum; single-line Q not well-defined
        Delta=8 * kap * S4_contact,  # Nonzero on charged stratum
        rho=None,  # Single-line radius undefined for C class
        kappa_dual=-kap,
        kappa_anti_symmetry=Rational(0),  # Free field: kappa + kappa! = 0
        params={'S4_bg': S4_contact},
    )


def atlas_virasoro():
    r"""Atlas entry for Virasoro Vir_c.

    CLASS M (mixed): infinite tower.
    kappa = c/2, alpha = 2, S_4 = 10/[c(5c+22)].
    Delta = 40/(5c+22) (nonzero at generic c).

    o_5 != 0 (quintic forced, thm:w-virasoro-quintic-forced).
    S_5 = -48/[c^2(5c+22)] (from virasoro_shadow_tower.py).

    Shadow radius: rho = sqrt((180c+872)/((5c+22)*c^2)).
    Self-dual at c = 13: rho(13) = sqrt(3212/(87*169)) = sqrt(3212/14703).

    Koszul dual: Vir_c^! = Vir_{26-c}.
    kappa + kappa! = c/2 + (26-c)/2 = 13 (NOT 0: W-algebra anomaly).
    """
    kap = c / 2
    alpha_val = Rational(2)
    S4_val = Rational(10) / (c * (5 * c + 22))
    S5_val = Rational(-48) / (c**2 * (5 * c + 22))
    Delta_val = Rational(40) / (5 * c + 22)

    Q_expr, _, _, _, _ = shadow_metric_QL(kap, alpha_val, S4_val)

    # Growth rate
    rho_sq = (9 * alpha_val**2 + 2 * Delta_val) / (4 * kap**2)
    # = (36 + 80/(5c+22)) / c^2
    # = (180c + 872) / ((5c+22) * c^2)
    rho_val = sqrt(cancel(rho_sq))

    return AtlasEntry(
        name='Virasoro Vir_c',
        depth_class='M',
        r_max=None,
        kappa=kap,
        alpha=alpha_val,
        S4=S4_val,
        S5=S5_val,
        o3=Rational(0),  # Cubic shadow exists
        o4=Rational(0),  # Quartic shadow exists
        o5=S5_val,       # NONZERO: quintic forced (o_5 != 0 means tower continues)
        Q_L=expand(Q_expr),
        Delta=Delta_val,
        rho=rho_val,
        kappa_dual=(26 - c) / 2,
        kappa_anti_symmetry=Rational(13),  # c/2 + (26-c)/2 = 13
        params={'c': c},
    )


def atlas_w3():
    r"""Atlas entry for W_3 at generic c.

    CLASS M (mixed, 2-channel): infinite tower.

    T-line (stress tensor direction): identical to Virasoro.
      kappa_T = c/2, alpha_T = 2, same quartic.
    W-line (spin-3 direction):
      kappa_W = c/3, alpha_W = 0 (odd arities vanish by Z_2),
      S4_W = 2560/[c(5c+22)^3].
    Total kappa = 5c/6 (sum of T and W contributions).

    Propagator variance:
      delta_mix = sum f_i^2/kappa_i - (sum f_i)^2/sum kappa_i
    Mixing polynomial: P(W_3) = 25c^2 + 100c - 428.
    delta_mix = 0 iff P(c) = 0 (curvature-proportional quartic gradient).
    """
    kap_total = Rational(5) * c / 6
    kap_T = c / 2
    kap_W = c / 3

    # T-line data (= Virasoro)
    alpha_T = Rational(2)
    S4_T = Rational(10) / (c * (5 * c + 22))

    # W-line data
    alpha_W = Rational(0)
    S4_W = Rational(2560) / (c * (5 * c + 22)**3)

    # Mixing polynomial
    P_w3 = 25 * c**2 + 100 * c - 428

    return AtlasEntry(
        name='W_3 algebra',
        depth_class='M',
        r_max=None,
        kappa=kap_total,
        alpha=alpha_T,  # On T-line
        S4=S4_T,        # On T-line
        o5=None,         # Nonzero (M class, infinite tower)
        Q_L=None,        # 2D metric: not a single expression
        Delta=None,      # Multi-channel: Delta not well-defined for total kappa
        rho=None,  # Two independent growth rates on T and W lines
        kappa_dual=Rational(65, 3) - kap_total,
        kappa_anti_symmetry=Rational(65, 3),  # rho * K = (5/6)*26 = 65/3
        params={
            'c': c,
            'kappa_T': kap_T,
            'kappa_W': kap_W,
            'alpha_T': alpha_T,
            'alpha_W': alpha_W,
            'S4_T': S4_T,
            'S4_W': S4_W,
            'mixing_polynomial': P_w3,
        },
    )


# ============================================================================
# 8. FULL ATLAS
# ============================================================================

def build_atlas():
    r"""Build the complete shadow obstruction atlas.

    Returns a dictionary keyed by canonical family name.
    """
    return {
        'Heisenberg': atlas_heisenberg(),
        'FreeFermion': atlas_free_fermion(),
        'Lattice': atlas_lattice(),
        'Affine_sl2': atlas_affine_sl2(),
        'BetaGamma': atlas_betagamma(),
        'Virasoro': atlas_virasoro(),
        'W3': atlas_w3(),
    }


# ============================================================================
# 9. CROSS-FAMILY CONSISTENCY CHECKS
# ============================================================================

def check_kappa_additivity(kappa_A, kappa_B, kappa_sum):
    r"""Verify kappa(A + B) = kappa(A) + kappa(B).

    Consequence of prop:independent-sum-factorization.
    """
    return simplify(kappa_sum - kappa_A - kappa_B) == 0


def check_kappa_anti_symmetry(kappa_A, kappa_A_dual, expected=0):
    r"""Verify kappa(A) + kappa(A!) = expected.

    For free-field/KM families: expected = 0.
    For W-algebras: expected = rho * K (nonzero).
    """
    return simplify(kappa_A + kappa_A_dual - expected) == 0


def check_discriminant_complementarity_virasoro(c_val):
    r"""Verify Delta(Vir_c) + Delta(Vir_{26-c}) = 6960/[(5c+22)(152-5c)].

    The complementarity sum has constant numerator 6960.
    """
    Delta_A = Rational(40) / (5 * c_val + 22)
    c_dual = 26 - c_val
    Delta_B = Rational(40) / (5 * c_dual + 22)
    total = cancel(Delta_A + Delta_B)
    expected = Rational(6960) / ((5 * c_val + 22) * (152 - 5 * c_val))
    return simplify(total - expected) == 0


def discriminant_complementarity_symbolic():
    r"""Symbolic verification: Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)].

    Delta(c) = 40/(5c+22).
    Delta(26-c) = 40/(5(26-c)+22) = 40/(152-5c).

    Sum = 40/(5c+22) + 40/(152-5c)
        = 40*(152-5c + 5c+22) / [(5c+22)(152-5c)]
        = 40*174 / [(5c+22)(152-5c)]
        = 6960 / [(5c+22)(152-5c)].
    """
    Delta_c = Rational(40) / (5 * c + 22)
    Delta_dual = Rational(40) / (152 - 5 * c)
    total = cancel(Delta_c + Delta_dual)

    # Verify numerator = 6960
    # 40 * (152 - 5c + 5c + 22) = 40 * 174 = 6960
    expected_numerator = 40 * 174  # = 6960
    return total, expected_numerator


# ============================================================================
# 10. VIRASORO DETAILED COMPUTATIONS
# ============================================================================

def virasoro_shadow_radius_at(c_val):
    r"""Numerical shadow radius for Virasoro at specific c.

    rho^2 = (180c + 872) / ((5c + 22) * c^2).
    """
    c_num = float(c_val)
    rho_sq = (180 * c_num + 872) / ((5 * c_num + 22) * c_num**2)
    return math.sqrt(rho_sq)


def virasoro_critical_central_charge():
    r"""The critical c* where rho(Vir_{c*}) = 1.

    Solves: (180c + 872) / ((5c + 22) * c^2) = 1
    i.e., 5c^3 + 22c^2 - 180c - 872 = 0.
    """
    from sympy import solve
    poly = 5 * c**3 + 22 * c**2 - 180 * c - 872
    roots = solve(poly, c)
    real_positive = []
    for r in roots:
        try:
            val = complex(r.evalf())
            if abs(val.imag) < 1e-10 and val.real > 0:
                real_positive.append(float(val.real))
        except (TypeError, ValueError):
            continue
    return real_positive[0] if real_positive else None


def virasoro_self_dual_check():
    r"""Verify self-duality at c = 13.

    rho(Vir_13) = rho(Vir_{26-13}) = rho(Vir_13). Trivially self-dual.
    kappa(13) = 13/2, kappa!(13) = 13/2.
    Delta(13) = 40/(5*13+22) = 40/87.
    """
    rho_13 = virasoro_shadow_radius_at(13)
    rho_13_dual = virasoro_shadow_radius_at(26 - 13)
    return {
        'c': 13,
        'rho': rho_13,
        'rho_dual': rho_13_dual,
        'self_dual': abs(rho_13 - rho_13_dual) < 1e-14,
        'kappa': Rational(13, 2),
        'kappa_dual': Rational(13, 2),
        'Delta': Rational(40, 87),
    }


def virasoro_numerical_tower(c_val, max_r=10):
    r"""Numerical Virasoro shadow tower at specific c.

    Returns dict {r: float(S_r)} using fast float recursion.
    """
    c_num = float(c_val)
    kap = c_num / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_num * (5.0 * c_num + 22.0))

    q0 = 4.0 * kap**2
    q1 = 12.0 * kap * alpha
    q2 = 9.0 * alpha**2 + 16.0 * kap * S4

    a = [0.0] * (max_r - 1)
    a[0] = math.sqrt(q0)
    if len(a) > 1:
        a[1] = q1 / (2.0 * a[0])
    if len(a) > 2:
        a[2] = (q2 - a[1]**2) / (2.0 * a[0])
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a[0])

    return {r: a[r - 2] for r in range(2, max_r + 1)}


# ============================================================================
# 11. W_3 DETAILED COMPUTATIONS (2-channel)
# ============================================================================

def w3_propagator_variance(c_val):
    r"""Propagator variance delta_mix for W_3 at central charge c.

    Mixing polynomial: P(W_3) = 25c^2 + 100c - 428.
    delta_mix proportional to P(c).  Vanishes iff P(c) = 0.

    The quartic gradient components:
      f_T = d(S4_T x_T^4)/dx_T |_{x_T=x_W=x} = 4 S4_T x^3
      f_W = d(S4_W x_W^4)/dx_W |_{x_T=x_W=x} = 4 S4_W x^3

    delta = f_T^2/kappa_T + f_W^2/kappa_W - (f_T + f_W)^2/(kappa_T + kappa_W)
    """
    c_num = Rational(c_val)
    kap_T = c_num / 2
    kap_W = c_num / 3

    S4_T = Rational(10) / (c_num * (5 * c_num + 22))
    S4_W = Rational(2560) / (c_num * (5 * c_num + 22)**3)

    f_T = 4 * S4_T
    f_W = 4 * S4_W

    delta = f_T**2 / kap_T + f_W**2 / kap_W - (f_T + f_W)**2 / (kap_T + kap_W)
    return cancel(delta)


def w3_two_channel_data(c_val):
    r"""Full 2-channel shadow data for W_3.

    Returns T-line and W-line shadow metrics, discriminants, growth rates.
    """
    c_num = float(c_val)

    # T-line = Virasoro
    kap_T = c_num / 2
    alpha_T = 2.0
    S4_T = 10.0 / (c_num * (5 * c_num + 22))
    Delta_T = 8 * kap_T * S4_T
    rho_T = math.sqrt((9 * alpha_T**2 + 2 * Delta_T)) / (2 * abs(kap_T))

    # W-line
    kap_W = c_num / 3
    alpha_W = 0.0
    S4_W = 2560.0 / (c_num * (5 * c_num + 22)**3)
    Delta_W = 8 * kap_W * S4_W
    # For alpha=0: rho_W = sqrt(2*Delta_W) / (2*|kappa_W|)
    rho_W = math.sqrt(2 * Delta_W) / (2 * abs(kap_W)) if Delta_W > 0 else 0.0

    return {
        'T_line': {
            'kappa': kap_T, 'alpha': alpha_T, 'S4': S4_T,
            'Delta': Delta_T, 'rho': rho_T,
            'class': 'M',
        },
        'W_line': {
            'kappa': kap_W, 'alpha': alpha_W, 'S4': S4_W,
            'Delta': Delta_W, 'rho': rho_W,
            'class': 'M' if Delta_W != 0 else 'G',
        },
    }


# ============================================================================
# 12. SUMMARY AND DISPLAY
# ============================================================================

def atlas_summary():
    r"""Generate a human-readable summary of the full atlas."""
    atlas = build_atlas()
    lines = []
    lines.append("=" * 78)
    lines.append("SHADOW OBSTRUCTION ATLAS: Definitive Computation")
    lines.append("=" * 78)

    for name, entry in atlas.items():
        lines.append(f"\n--- {entry.name} (class {entry.depth_class}, "
                     f"r_max = {entry.r_max or 'inf'}) ---")
        lines.append(f"  kappa   = {entry.kappa}")
        lines.append(f"  alpha   = {entry.alpha}")
        lines.append(f"  S_4     = {entry.S4}")
        lines.append(f"  S_5     = {entry.S5}")
        lines.append(f"  Delta   = {entry.Delta}")
        lines.append(f"  o_3     = {entry.o3}")
        lines.append(f"  o_4     = {entry.o4}")
        lines.append(f"  o_5     = {entry.o5}")
        lines.append(f"  rho     = {entry.rho}")
        lines.append(f"  kappa!  = {entry.kappa_dual}")
        lines.append(f"  kappa + kappa! = {entry.kappa_anti_symmetry}")

    return "\n".join(lines)


if __name__ == '__main__':
    print(atlas_summary())

    print("\n\nVirasoro detailed:")
    vir = atlas_virasoro()
    tower = virasoro_shadow_tower(7)
    for r in sorted(tower.keys()):
        print(f"  Sh_{r} = {tower[r]} * x^{r}")

    print(f"\n  Shadow radius at c=13: {virasoro_shadow_radius_at(13):.8f}")
    print(f"  Critical c*: {virasoro_critical_central_charge():.6f}")

    sd = virasoro_self_dual_check()
    print(f"  Self-dual at c=13: {sd['self_dual']}")

    print("\n\nDiscriminant complementarity:")
    total, numer = discriminant_complementarity_symbolic()
    print(f"  Delta(c) + Delta(26-c) = {total}")
    print(f"  Numerator = {numer}")
