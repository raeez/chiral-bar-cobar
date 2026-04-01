"""Shadow metric census: Q_L(t), critical discriminant Delta, and G/L/C/M classification.

For every standard family in the monograph, computes the shadow metric on the
1-dimensional primary line:

    Q_L(t) = (2kappa + 3*alpha*t)^2 + 2*Delta*t^2

where:
    kappa  = modular characteristic (arity-2 curvature)
    alpha  = cubic shadow coefficient on the primary line
    S_4    = quartic shadow coefficient on the primary line
    Delta  = 8*kappa*S_4  (critical discriminant)

The G/L/C/M classification:
    G (Gaussian):  Delta = 0, alpha = 0  =>  r_max = 2
    L (Lie/tree):  Delta = 0, alpha != 0  =>  r_max = 3
    C (Contact):   Delta != 0, alpha = 0  =>  r_max = 4
    M (Mixed):     Delta != 0, alpha != 0  =>  r_max = infinity

The shadow metric Q_L(t) encodes the second variation of the shadow potential
along the primary deformation line L.  When Q_L is a perfect square (Delta = 0),
the shadow tower terminates at finite arity.  When Delta != 0, the cross term
forces the tower to continue indefinitely.

Mathematical references:
    - def:shadow-depth-classification in higher_genus_modular_koszul.tex
    - thm:shadow-archetype-classification in higher_genus_modular_koszul.tex
    - thm:nms-mc-principle in nonlinear_modular_shadows.tex
    - cor:nms-betagamma-mu-vanishing in nonlinear_modular_shadows.tex
    - cor:general-w-obstruction in w_algebras.tex (eq:general-w-kappa)
    - w_algebras.tex: Q^contact_Vir = 10/[c(5c+22)]
    - virasoro_shadow_tower.py: Sh_3 = 2x^3 (alpha = 2 for Virasoro)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, expand, factor, simplify, sqrt, symbols, oo, S
)


# ========================================================================
# Symbols
# ========================================================================

k = Symbol('k')       # affine level / Heisenberg level
c = Symbol('c')       # central charge
N = Symbol('N')       # rank for sl_N
t = Symbol('t')       # deformation parameter on primary line
lam = Symbol('lambda')  # conformal weight for betagamma/bc


# ========================================================================
# Kappa formulas (from envelope_shadow_functor.py, reproduced symbolically)
# ========================================================================

def kappa_heisenberg(level):
    """kappa(Heis, k) = k."""
    return level


def kappa_lattice(rank):
    """kappa(V_Lambda) = rank(Lambda)."""
    return rank


def kappa_free_fermion():
    """kappa(FreeFermion) = 1/4.

    The free fermion has c = 1/2, kappa = c/2 = 1/4.
    See landscape_census.tex Table tab:master-invariants: free fermion psi,
    c = 1/2, kappa = 1/4.

    CAUTION (AP1): Do NOT use kappa = k (the Heisenberg formula) here.
    The free fermion is NOT a Heisenberg algebra. The formula kappa = c/2
    applies to the free fermion (same as bc ghosts and Virasoro).
    """
    return Rational(1, 4)


def kappa_affine_sl2(level):
    """kappa(sl_2, k) = 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2*h^v).

    dim(sl_2) = 3, h^v = 2.
    """
    return Rational(3) * (level + 2) / 4


def kappa_affine_slN(n, level):
    """kappa(sl_N, k) = (N^2-1)(k+N)/(2N).

    dim(sl_N) = N^2-1, h^v = N.
    """
    return (n**2 - 1) * (level + n) / (2 * n)


def kappa_betagamma(weight):
    """kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.

    This equals c_{bg}/2 where c_{bg} = 2(6*lambda^2 - 6*lambda + 1).
    Standard betagamma (lambda=0 or 1): kappa = 1.
    Symplectic (lambda=1/2): kappa = -1/2.
    """
    return 6 * weight**2 - 6 * weight + 1


def kappa_bc(spin):
    """kappa(bc, j) = -kappa(betagamma, j).

    The bc system has opposite kappa sign from betagamma.
    bc spin j corresponds to betagamma weight j.
    """
    return -(6 * spin**2 - 6 * spin + 1)


def kappa_virasoro(central_charge):
    """kappa(Vir, c) = c/2."""
    return central_charge / 2


def kappa_w3(central_charge):
    """kappa(W_3, c) = 5c/6.

    rho(sl_3) = H_3 - 1 = 1/2 + 1/3 = 5/6.
    """
    return Rational(5) * central_charge / 6


def kappa_wN(n, central_charge):
    """kappa(W_N, c) = (H_N - 1)*c.

    H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number.
    """
    # Compute H_N - 1 = sum_{i=2}^{N} 1/i
    rho = sum(Rational(1, i) for i in range(2, n + 1))
    return rho * central_charge


# ========================================================================
# Shadow metric data: the census
# ========================================================================

def _virasoro_S4(central_charge):
    """Quartic coefficient S_4 for Virasoro.

    Q^contact_Vir = 10/[c(5c+22)].
    """
    return Rational(10) / (central_charge * (5 * central_charge + 22))


def _virasoro_Delta(central_charge):
    """Critical discriminant Delta = 8*kappa*S_4 for Virasoro.

    Delta = 8 * (c/2) * 10/[c(5c+22)]
          = 8 * 10 / (2*(5c+22))
          = 80 / (2*(5c+22))
          = 40 / (5c+22).
    """
    return Rational(40) / (5 * central_charge + 22)


class ShadowMetricEntry:
    """A single entry in the shadow metric census.

    Attributes:
        name:   human-readable family name
        kappa:  modular characteristic (symbolic or numeric)
        alpha:  cubic shadow coefficient on primary line
        S4:     quartic shadow coefficient on primary line
        Delta:  critical discriminant 8*kappa*S4
        Q_L:    shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
        cls:    shadow class in {G, L, C, M}
        r_max:  shadow depth (2, 3, 4, or None for infinity)
        d_alg:  algebraic description of the family
        params: dictionary of parameter symbols used
    """

    def __init__(self, name, kappa, alpha, S4, cls, r_max, d_alg,
                 params=None, Delta_override=None):
        self.name = name
        self.kappa = kappa
        self.alpha = alpha
        self.S4 = S4
        if Delta_override is not None:
            self.Delta = Delta_override
        else:
            self.Delta = 8 * kappa * S4
        self.cls = cls
        self.r_max = r_max
        self.d_alg = d_alg
        self.params = params or {}

    def Q_L(self, deformation_param=None):
        """Shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        s = deformation_param if deformation_param is not None else t
        return expand((2 * self.kappa + 3 * self.alpha * s)**2
                      + 2 * self.Delta * s**2)

    def verify_class(self):
        """Verify that the G/L/C/M classification is consistent with Delta, alpha."""
        # For symbolic entries, check at generic parameter values
        Delta_is_zero = simplify(self.Delta) == 0
        alpha_is_zero = simplify(self.alpha) == 0

        if Delta_is_zero and alpha_is_zero:
            expected = 'G'
        elif Delta_is_zero and not alpha_is_zero:
            expected = 'L'
        elif not Delta_is_zero and alpha_is_zero:
            expected = 'C'
        else:
            expected = 'M'
        return expected == self.cls

    def verify_Delta(self):
        """Verify Delta = 8*kappa*S4."""
        return simplify(self.Delta - 8 * self.kappa * self.S4) == 0

    def to_dict(self):
        """Export as a plain dictionary."""
        return {
            'name': self.name,
            'kappa': self.kappa,
            'alpha': self.alpha,
            'S4': self.S4,
            'Delta': self.Delta,
            'Q_L': self.Q_L(),
            'class': self.cls,
            'r_max': self.r_max,
            'd_alg': self.d_alg,
        }


# ========================================================================
# The census: all standard families
# ========================================================================

def build_census() -> Dict[str, ShadowMetricEntry]:
    """Build the complete shadow metric census for all standard families.

    Returns a dictionary keyed by canonical family name.
    """
    census = {}

    # ------------------------------------------------------------------
    # 1. Heisenberg H_k
    # ------------------------------------------------------------------
    census['Heisenberg'] = ShadowMetricEntry(
        name='Heisenberg H_k',
        kappa=k,
        alpha=S.Zero,
        S4=S.Zero,
        cls='G',
        r_max=2,
        d_alg='Abelian current algebra at level k; OPE = k*delta, all shadows vanish beyond kappa',
        params={'k': k},
    )

    # ------------------------------------------------------------------
    # 2. Lattice V_Lambda
    # ------------------------------------------------------------------
    r = Symbol('r')  # rank
    census['Lattice'] = ShadowMetricEntry(
        name='Lattice V_Lambda',
        kappa=r,
        alpha=S.Zero,
        S4=S.Zero,
        cls='G',
        r_max=2,
        d_alg='Even self-dual lattice VOA; kappa = rank(Lambda), abelian primary line',
        params={'r': r},
    )

    # ------------------------------------------------------------------
    # 3. Free fermion
    # ------------------------------------------------------------------
    census['FreeFermion'] = ShadowMetricEntry(
        name='Free fermion',
        kappa=Rational(1, 4),
        alpha=S.Zero,
        S4=S.Zero,
        cls='G',
        r_max=2,
        d_alg='Single real fermion, c = 1/2, kappa = 1/4 = c/2; Clifford OPE is abelian on primary line',
        params={},
    )

    # ------------------------------------------------------------------
    # 4. Affine sl_2 at level k
    #    kappa = 3(k+2)/4
    #    alpha: nonzero (Lie bracket f_{abc})
    #    S_4 = 0 (Jacobi identity kills quartic on primary line)
    #    Delta = 0
    #    Class L
    # ------------------------------------------------------------------
    # The cubic coefficient alpha for sl_2:
    # From the Lie bracket structure constants, the cubic shadow on the
    # primary line (Cartan direction h) is:
    #   C(h,h,h) = 0 (Cartan is abelian)
    # but on the FULL sl_2 line (including e, f):
    #   Sh_3 = alpha * x^3 with alpha determined by the Killing form
    #   and structure constants.
    # For sl_2 with generators {e, f, h} and [e,f]=h, [h,e]=2e, [h,f]=-2f:
    # The cubic shadow coefficient on a generic primary direction is nonzero.
    # We record alpha symbolically as a nonzero constant.
    alpha_sl2 = Symbol('alpha_sl2', nonzero=True)
    census['Affine_sl2'] = ShadowMetricEntry(
        name='Affine sl_2 at level k',
        kappa=Rational(3) * (k + 2) / 4,
        alpha=alpha_sl2,
        S4=S.Zero,
        cls='L',
        r_max=3,
        d_alg='Affine Kac-Moody at level k; cubic from Lie bracket, quartic killed by Jacobi',
        params={'k': k, 'alpha_sl2': alpha_sl2},
    )

    # ------------------------------------------------------------------
    # 5. Affine sl_N at level k (N >= 2)
    #    kappa = (N^2-1)(k+N)/(2N)
    #    alpha: nonzero (Lie bracket)
    #    S_4 = 0 (Jacobi)
    #    Delta = 0
    #    Class L
    # ------------------------------------------------------------------
    alpha_slN = Symbol('alpha_slN', nonzero=True)
    census['Affine_slN'] = ShadowMetricEntry(
        name='Affine sl_N at level k',
        kappa=(N**2 - 1) * (k + N) / (2 * N),
        alpha=alpha_slN,
        S4=S.Zero,
        cls='L',
        r_max=3,
        d_alg='Affine Kac-Moody sl_N at level k; Jacobi kills quartic on primary line',
        params={'N': N, 'k': k, 'alpha_slN': alpha_slN},
    )

    # ------------------------------------------------------------------
    # 6. betagamma system
    #    On the weight-changing primary line:
    #      alpha = 0 (abelian on 1D weight-shift subspace)
    #      S_4 = 0 on neutral primary line (rank-one rigidity)
    #    But the CHARGED stratum has nontrivial quartic contact.
    #    Overall classification: class C (quartic contact on full deformation space)
    #
    #    kappa = 6*lambda^2 - 6*lambda + 1 (weight-dependent)
    #    For standard betagamma (lambda=0 or 1): kappa = 1
    #    For the primary line used in classification:
    #      alpha = 0 on weight-changing line (abelian)
    #      S_4 = 0 on weight-changing line (cor:nms-betagamma-mu-vanishing)
    #    But there exists a contact direction with S_4 != 0.
    #    Hence the overall classification uses the charged stratum.
    #
    #    We record the PRIMARY LINE data (alpha=0, S_4=0 on that line)
    #    but assign class C because the FULL deformation complex has
    #    nontrivial quartic contact on the 2D weight/contact slice.
    # ------------------------------------------------------------------
    # Contact quartic coefficient on charged stratum (nonzero, symbolic)
    S4_bg_contact = Symbol('S4_bg', nonzero=True)
    kappa_bg = 6 * lam**2 - 6 * lam + 1
    census['BetaGamma'] = ShadowMetricEntry(
        name='betagamma system (weight lambda)',
        kappa=kappa_bg,
        alpha=S.Zero,  # on weight-changing line
        S4=S4_bg_contact,  # on charged stratum
        cls='C',
        r_max=4,
        d_alg='betagamma at conformal weight lambda; alpha=0 on weight-changing line, quartic contact on charged stratum',
        params={'lambda': lam, 'S4_bg': S4_bg_contact},
        Delta_override=8 * kappa_bg * S4_bg_contact,
    )

    # ------------------------------------------------------------------
    # 7. bc system (spin j)
    #    Mirror of betagamma with opposite signs.
    #    kappa_bc = -(6j^2 - 6j + 1)
    #    Class C for same structural reasons.
    # ------------------------------------------------------------------
    j = Symbol('j')
    S4_bc_contact = Symbol('S4_bc', nonzero=True)
    kappa_bc_val = -(6 * j**2 - 6 * j + 1)
    census['bc'] = ShadowMetricEntry(
        name='bc system (spin j)',
        kappa=kappa_bc_val,
        alpha=S.Zero,
        S4=S4_bc_contact,
        cls='C',
        r_max=4,
        d_alg='bc ghosts at spin j; quartic contact on charged stratum, mirror of betagamma',
        params={'j': j, 'S4_bc': S4_bc_contact},
        Delta_override=8 * kappa_bc_val * S4_bc_contact,
    )

    # ------------------------------------------------------------------
    # 8. Virasoro Vir_c
    #    kappa = c/2
    #    alpha = 2 (from Sh_3 = 2x^3 in virasoro_shadow_tower.py)
    #    S_4 = Q^contact_Vir = 10/[c(5c+22)]
    #    Delta = 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)
    #    Class M (alpha != 0, Delta != 0)
    # ------------------------------------------------------------------
    census['Virasoro'] = ShadowMetricEntry(
        name='Virasoro Vir_c',
        kappa=c / 2,
        alpha=Rational(2),
        S4=Rational(10) / (c * (5 * c + 22)),
        cls='M',
        r_max=None,  # infinite tower
        d_alg='Virasoro at central charge c; gravitational cubic alpha=2, quartic Q^contact=10/[c(5c+22)]',
        params={'c': c},
        Delta_override=Rational(40) / (5 * c + 22),
    )

    # ------------------------------------------------------------------
    # 9. W_3 algebra
    #    kappa = 5c/6
    #    alpha: nonzero (cubic from W_3 bracket involving spin-3 generator)
    #    S_4: nonzero (quartic from W_3 normal ordering)
    #    Delta: nonzero
    #    Class M
    # ------------------------------------------------------------------
    alpha_w3 = Symbol('alpha_W3', nonzero=True)
    S4_w3 = Symbol('S4_W3', nonzero=True)
    census['W3'] = ShadowMetricEntry(
        name='W_3 algebra',
        kappa=Rational(5) * c / 6,
        alpha=alpha_w3,
        S4=S4_w3,
        cls='M',
        r_max=None,
        d_alg='W_3 at central charge c; cubic from W_3 bracket, quartic from normal ordering',
        params={'c': c, 'alpha_W3': alpha_w3, 'S4_W3': S4_w3},
    )

    # ------------------------------------------------------------------
    # 10. W_N algebra (N >= 3)
    #     kappa = (H_N - 1)*c where H_N = harmonic number
    #     alpha: nonzero for N >= 3
    #     S_4: nonzero for N >= 3
    #     Delta: nonzero
    #     Class M
    # ------------------------------------------------------------------
    alpha_wN = Symbol('alpha_WN', nonzero=True)
    S4_wN = Symbol('S4_WN', nonzero=True)
    # H_N - 1 kept symbolic via N
    rho_N = Symbol('rho_N', positive=True)  # = H_N - 1
    census['W_N'] = ShadowMetricEntry(
        name='W_N algebra (N >= 3)',
        kappa=rho_N * c,
        alpha=alpha_wN,
        S4=S4_wN,
        cls='M',
        r_max=None,
        d_alg='W_N at central charge c; kappa = (H_N - 1)*c, cubic and quartic from higher-spin normal ordering',
        params={'c': c, 'N': N, 'rho_N': rho_N,
                'alpha_WN': alpha_wN, 'S4_WN': S4_wN},
    )

    return census


# ========================================================================
# Specific numerical evaluations
# ========================================================================

def evaluate_heisenberg(level_val):
    """Evaluate shadow metric for Heisenberg at a specific level.

    Q_L(t) = (2k)^2 = 4k^2 (constant in t).
    """
    kap = level_val
    return {
        'kappa': kap,
        'alpha': 0,
        'S4': 0,
        'Delta': 0,
        'Q_L_const': 4 * kap**2,
    }


def evaluate_affine_sl2(level_val):
    """Evaluate shadow metric for affine sl_2 at a specific level.

    kappa = 3(k+2)/4.
    Delta = 0 (Jacobi).
    Q_L(t) = (2*kappa + 3*alpha*t)^2 = (3(k+2)/2 + 3*alpha*t)^2.
    """
    kap = Rational(3) * (level_val + 2) / 4
    return {
        'kappa': kap,
        'alpha': 'nonzero (Lie bracket)',
        'S4': 0,
        'Delta': 0,
        'Q_L_form': f'(2*{kap} + 3*alpha*t)^2 = ({2*kap} + 3*alpha*t)^2',
    }


def evaluate_virasoro(c_val):
    """Evaluate shadow metric for Virasoro at a specific central charge.

    kappa = c/2, alpha = 2, S_4 = 10/[c(5c+22)], Delta = 40/(5c+22).
    """
    kap = Rational(c_val) / 2
    S4 = Rational(10) / (Rational(c_val) * (5 * Rational(c_val) + 22))
    Delta = Rational(40) / (5 * Rational(c_val) + 22)
    Q_L_val = expand((2 * kap + 3 * Rational(2) * t)**2 + 2 * Delta * t**2)
    return {
        'kappa': kap,
        'alpha': Rational(2),
        'S4': S4,
        'Delta': Delta,
        'Delta_check': 8 * kap * S4,
        'Q_L': Q_L_val,
    }


def evaluate_wN(n_val, c_val):
    """Evaluate shadow metric for W_N at specific N and central charge.

    kappa = (H_N - 1)*c.
    """
    rho = sum(Rational(1, i) for i in range(2, n_val + 1))
    kap = rho * c_val
    return {
        'N': n_val,
        'rho_N': rho,
        'kappa': kap,
        'class': 'M',
        'r_max': None,
    }


# ========================================================================
# Classification engine
# ========================================================================

def classify(alpha_val, Delta_val) -> Tuple[str, Optional[int]]:
    """Classify shadow depth from alpha and Delta values.

    Returns (class_letter, r_max) where r_max is None for infinite tower.

    Classification logic:
        Delta = 0 and alpha = 0  =>  G, r_max = 2
        Delta = 0 and alpha != 0  =>  L, r_max = 3
        Delta != 0 and alpha = 0  =>  C, r_max = 4
        Delta != 0 and alpha != 0  =>  M, r_max = None (infinity)
    """
    D_zero = simplify(Delta_val) == 0
    a_zero = simplify(alpha_val) == 0

    if D_zero and a_zero:
        return ('G', 2)
    elif D_zero and not a_zero:
        return ('L', 3)
    elif not D_zero and a_zero:
        return ('C', 4)
    else:
        return ('M', None)


def classify_from_data(kappa_val, alpha_val, S4_val) -> Tuple[str, Optional[int]]:
    """Classify from raw shadow data: kappa, alpha, S4.

    Computes Delta = 8*kappa*S4, then classifies.
    """
    Delta = 8 * kappa_val * S4_val
    return classify(alpha_val, Delta)


# ========================================================================
# Harmonic numbers (for W_N formulas)
# ========================================================================

def harmonic_number(n):
    """H_n = 1 + 1/2 + ... + 1/n (exact rational)."""
    return sum(Rational(1, i) for i in range(1, n + 1))


def anomaly_ratio(n):
    """rho(sl_N) = H_N - 1 = 1/2 + 1/3 + ... + 1/N."""
    return harmonic_number(n) - 1


# ========================================================================
# Summary table
# ========================================================================

def summary_table() -> List[Dict[str, Any]]:
    """Generate a summary table of all families with their shadow metric data.

    Returns a list of dictionaries, one per family, with keys:
        name, kappa, alpha, S4, Delta, class, r_max, d_alg
    """
    census = build_census()
    rows = []
    # Canonical ordering
    order = ['Heisenberg', 'Lattice', 'FreeFermion',
             'Affine_sl2', 'Affine_slN',
             'BetaGamma', 'bc',
             'Virasoro', 'W3', 'W_N']
    for key in order:
        entry = census[key]
        rows.append(entry.to_dict())
    return rows


# ========================================================================
# Virasoro-specific detailed computation
# ========================================================================

def virasoro_shadow_metric_symbolic():
    """Full symbolic shadow metric for Virasoro.

    Q_L(t) = (2*(c/2) + 3*2*t)^2 + 2*(40/(5c+22))*t^2
           = (c + 6t)^2 + 80*t^2/(5c+22)

    Expanding:
           = c^2 + 12ct + 36t^2 + 80*t^2/(5c+22)
           = c^2 + 12ct + t^2*(36 + 80/(5c+22))
           = c^2 + 12ct + t^2*(36(5c+22) + 80)/(5c+22)
           = c^2 + 12ct + t^2*(180c + 792 + 80)/(5c+22)
           = c^2 + 12ct + t^2*(180c + 872)/(5c+22)
           = c^2 + 12ct + 4t^2*(45c + 218)/(5c+22)
    """
    kap = c / 2
    alpha = Rational(2)
    Delta = Rational(40) / (5 * c + 22)

    Q = expand((2 * kap + 3 * alpha * t)**2 + 2 * Delta * t**2)
    return {
        'kappa': kap,
        'alpha': alpha,
        'S4': Rational(10) / (c * (5 * c + 22)),
        'Delta': Delta,
        'Q_L': Q,
        'Q_L_factored': factor(Q),
    }


# ========================================================================
# Verification helpers
# ========================================================================

def verify_delta_identity(entry: ShadowMetricEntry) -> bool:
    """Verify that Delta = 8*kappa*S4 for a census entry."""
    return entry.verify_Delta()


def verify_all_deltas() -> Dict[str, bool]:
    """Verify Delta = 8*kappa*S4 for every entry in the census."""
    census = build_census()
    results = {}
    for name, entry in census.items():
        results[name] = entry.verify_Delta()
    return results


def verify_all_classes() -> Dict[str, bool]:
    """Verify G/L/C/M classification consistency for every entry."""
    census = build_census()
    results = {}
    for name, entry in census.items():
        results[name] = entry.verify_class()
    return results


def verify_Q_L_formula(entry: ShadowMetricEntry) -> bool:
    """Verify that Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
    Q = entry.Q_L()
    expected = expand((2 * entry.kappa + 3 * entry.alpha * t)**2
                      + 2 * entry.Delta * t**2)
    return simplify(Q - expected) == 0


def verify_all_Q_L() -> Dict[str, bool]:
    """Verify Q_L formula for every entry."""
    census = build_census()
    results = {}
    for name, entry in census.items():
        results[name] = verify_Q_L_formula(entry)
    return results


# ========================================================================
# Main
# ========================================================================

if __name__ == '__main__':
    print("=" * 78)
    print("SHADOW METRIC CENSUS: Q_L(t), Delta, and G/L/C/M classification")
    print("=" * 78)

    census = build_census()

    for name in ['Heisenberg', 'Lattice', 'FreeFermion',
                  'Affine_sl2', 'Affine_slN',
                  'BetaGamma', 'bc',
                  'Virasoro', 'W3', 'W_N']:
        entry = census[name]
        print(f"\n--- {entry.name} ---")
        print(f"  kappa = {entry.kappa}")
        print(f"  alpha = {entry.alpha}")
        print(f"  S_4   = {entry.S4}")
        print(f"  Delta = {entry.Delta}")
        print(f"  Q_L   = {entry.Q_L()}")
        print(f"  class = {entry.cls}, r_max = {entry.r_max}")
        print(f"  Delta = 8*kappa*S4: {entry.verify_Delta()}")
        print(f"  class consistent:   {entry.verify_class()}")

    print(f"\n{'=' * 78}")

    # Virasoro detailed
    vir = virasoro_shadow_metric_symbolic()
    print("\nVirasoro shadow metric (detailed):")
    print(f"  Q_L(t) = {vir['Q_L']}")
    print(f"  factored = {vir['Q_L_factored']}")
    print(f"  Delta = {vir['Delta']}")

    # Numerical examples
    print("\nVirasoro at c = 1:")
    v1 = evaluate_virasoro(1)
    print(f"  kappa = {v1['kappa']}, S4 = {v1['S4']}, Delta = {v1['Delta']}")
    print(f"  Delta check (8*kappa*S4): {v1['Delta_check']}")

    print("\nVirasoro at c = 26:")
    v26 = evaluate_virasoro(26)
    print(f"  kappa = {v26['kappa']}, S4 = {v26['S4']}, Delta = {v26['Delta']}")
    print(f"  Delta check (8*kappa*S4): {v26['Delta_check']}")
