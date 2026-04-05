r"""Kodaira-Spencer transport operator for bar complex growth rates.

Extracts bar cohomology asymptotics from finite-dimensional eigenvalue
problems rather than brute-force Hilbert series computation.

MATHEMATICAL FRAMEWORK (conj:discriminant-ks-operator):

For a chiral algebra A with Lie algebra g of rank r, there exists a
natural linear operator KS_g acting on H^1_red(B(A)) (the reduced first
bar cohomology) whose characteristic polynomial equals the discriminant
Delta_A(x) of the bar generating function P_A(x).

The bar generating function:
    P_A(x) = sum_{n>=0} dim H^n(B(A)) * x^n

The discriminant:
    Delta_A(x) = prod_i (1 - lambda_i * x)

where {lambda_i} are the eigenvalues of KS_g.  These eigenvalues are
the reciprocals of the singularities of the bar GF.

TWO REGIMES:

(1) Rational GF (sl_3, sl_N with N >= 3, W_N):
    P_A(x) = N(x) / Delta_A(x) for polynomial numerator N(x).
    Eigenvalues give exact partial-fractions formula:
        dim H^n(B(A)) = sum_i c_i * lambda_i^n.

(2) Algebraic GF of degree 2 (sl_2, Virasoro, betagamma):
    P_A(x) = (stuff +/- sqrt(Delta_A(x))) / (denominator).
    Delta appears inside a square root, so P has branch points at
    the zeros of Delta.  Eigenvalues give the exponential growth rate
    but with algebraic corrections:
        dim H^n(B(A)) ~ C * lambda_max^n * n^{-3/2}.
    Partial fractions do NOT give exact dims.

KEY EXAMPLES:

sl_2 (algebraic, degree 2):
    Singularities {1/3, -1}, eigenvalues {3, -1}.
    Delta = (1 - 3x)(1 + x) = 1 - 2x - 3x^2.
    Bar dims = Riordan numbers R(n+3).  Growth: R(n) ~ C * 3^n * n^{-3/2}.

sl_3 (rational):
    Eigenvalues {8, (3+sqrt(13))/2, (3-sqrt(13))/2}.
    Delta = (1 - 8x)(1 - 3x - x^2).
    Bar dims satisfy linear recurrence a_n = 11*a_{n-1} - 23*a_{n-2} - 8*a_{n-3}.
    Exact: dim H^n = c_1 * 8^n + c_2 * ((3+sqrt(13))/2)^n + c_3 * ((3-sqrt(13))/2)^n.
    DS-invariant subfactor = (1 - 3x - x^2), surviving sl_3 -> W_3.

Virasoro (algebraic, degree 2):
    Same discriminant as sl_2: Delta = (1 - 3x)(1 + x).
    Bar dims = Motzkin differences M(n+1) - M(n).
    Growth: ~ C * 3^n * n^{-3/2} (same exponential rate, different constant).

General sl_N:
    dim H^1_red = N, degree of Delta = N.
    DS reduction kills one eigenvalue, leaving degree-(N-1) subfactor.

Manuscript references:
    conj:discriminant-ks-operator (higher_genus_modular_koszul.tex)
    thm:ds-bar-gf-discriminant (landscape_census.tex)
    bar_gf_algebraicity.py (compute/lib)
    bar_gf_solver.py (compute/lib)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from sympy import (
    Abs,
    Integer,
    Matrix,
    Poly,
    Symbol,
    expand,
    prod,
    simplify,
    solve,
    sqrt,
    N as Neval,
)


x = Symbol('x')
lam = Symbol('lambda')


# =========================================================================
# 1. KSTransportOperator dataclass
# =========================================================================

@dataclass
class KSTransportOperator:
    r"""Kodaira-Spencer transport operator for a chiral algebra.

    The KS operator acts on H^1_red(B(A)) and its characteristic
    polynomial encodes the discriminant of the bar generating function.

    The eigenvalues {lambda_i} are the reciprocals of the singularities
    of P_A(x).  For rational GFs (sl_3+), these are poles and partial
    fractions give exact bar dims.  For algebraic GFs (sl_2, Virasoro),
    these are branch points and the exact formula involves n^{-3/2}
    corrections from the square-root singularity.

    Attributes
    ----------
    algebra_name : str
        Name of the chiral algebra (e.g. 'sl2', 'sl3', 'Virasoro').
    rank : int
        Rank of the underlying Lie algebra (= dim Cartan for sl_N).
    ks_dimension : int
        Dimension of H^1_red(B(A)).  For sl_N this equals N.
    eigenvalues : list
        Eigenvalues of KS (sympy expressions): reciprocals of GF singularities.
    characteristic_polynomial : Any
        char(KS, lambda) as a sympy Poly in ``lam``.
    discriminant : Any
        Delta_A(x) = prod(1 - lambda_i * x) as a sympy expression.
    gf_type : str
        'rational' or 'algebraic'.  Determines whether partial fractions
        give exact bar dimensions or only the exponential growth rate.
    ds_invariant_factor : optional
        The factor of Delta that survives Drinfeld-Sokolov reduction.
    growth_rates : list of float
        |lambda_i| for each eigenvalue (numerical).
    dominant_growth_rate : float
        max(|lambda_i|): controls the exponential growth of bar dims.
    """

    algebra_name: str
    rank: int
    ks_dimension: int
    eigenvalues: List[Any]
    characteristic_polynomial: Any
    discriminant: Any
    gf_type: str = 'rational'
    ds_invariant_factor: Optional[Any] = None
    growth_rates: List[float] = field(default_factory=list)
    dominant_growth_rate: float = 0.0

    def __post_init__(self):
        """Compute numerical growth rates from eigenvalues if not set."""
        if not self.growth_rates and self.eigenvalues:
            self.growth_rates = [
                float(Abs(Neval(ev))) for ev in self.eigenvalues
            ]
        if self.growth_rates and self.dominant_growth_rate == 0.0:
            self.dominant_growth_rate = max(self.growth_rates)

    def bar_gf_from_eigenvalues(self, var: str = 'x') -> Any:
        r"""Reconstruct Delta_A(x) = prod_i (1 - lambda_i * x) from eigenvalues.

        For rational GFs, the full bar GF is P_A(x) = N(x) / Delta_A(x).
        For algebraic GFs, Delta appears inside a square root in the
        algebraic equation satisfied by P_A.

        Parameters
        ----------
        var : str
            Variable name for the generating function variable.
        """
        t = Symbol(var)
        return expand(prod([1 - ev * t for ev in self.eigenvalues]))

    def asymptotic_formula(self, n: Symbol) -> Any:
        r"""Leading asymptotic for dim H^n(B(A)) from dominant eigenvalue.

        For rational GFs: dim H^n ~ C * lambda_max^n  (exact leading term).
        For algebraic GFs: dim H^n ~ C * lambda_max^n * n^{-3/2}
            (algebraic singularity correction from the branch point).

        Parameters
        ----------
        n : sympy Symbol
            The degree variable.

        Returns
        -------
        Expression for the leading exponential factor lambda_max^n.
        The prefactor C and possible n^{-3/2} are not determined
        without the full GF.
        """
        lam_max = max(self.eigenvalues, key=lambda ev: float(Abs(Neval(ev))))
        return lam_max ** n

    def ds_reduction_pattern(self) -> Dict[str, Any]:
        r"""Identify which eigenvalue factors survive DS reduction.

        For sl_N -> W_N, the DS reduction kills one eigenvalue (the
        'Lie' eigenvalue from the Cartan contribution), leaving a
        degree-(N-1) subfactor.

        Returns
        -------
        dict with keys:
            'killed_eigenvalues': eigenvalues removed by DS
            'surviving_eigenvalues': eigenvalues that survive
            'surviving_factor': the surviving polynomial factor
            'ds_invariant_factor': same as surviving_factor (alias)
        """
        if self.ds_invariant_factor is None:
            return {
                'killed_eigenvalues': [],
                'surviving_eigenvalues': list(self.eigenvalues),
                'surviving_factor': self.discriminant,
                'ds_invariant_factor': self.discriminant,
            }

        # Factor the discriminant and identify which roots survive
        t = Symbol('x')
        surviving_roots = solve(self.ds_invariant_factor.subs(x, t), t)
        surviving_evals = [simplify(1 / r) for r in surviving_roots if r != 0]
        killed = [ev for ev in self.eigenvalues
                  if not any(simplify(ev - s) == 0 for s in surviving_evals)]

        return {
            'killed_eigenvalues': killed,
            'surviving_eigenvalues': surviving_evals,
            'surviving_factor': self.ds_invariant_factor,
            'ds_invariant_factor': self.ds_invariant_factor,
        }


# =========================================================================
# 2. Constructors for standard families
# =========================================================================

def ks_operator_sl2(level: Optional[Any] = None) -> KSTransportOperator:
    r"""KS transport operator for sl_2 at non-critical level.

    The bar GF for sl_2 is the Riordan generating function, which is
    ALGEBRAIC of degree 2 satisfying:
        x(1+x) R^2 - (1+x) R + 1 = 0
    with discriminant (1+x)^2 - 4x(1+x) = (1+x)(1-3x).

    The eigenvalues {3, -1} are the reciprocals of the branch points
    x = 1/3 and x = -1.  Bar dims a_n = R(n+3) grow as:
        a_n ~ C * 3^n * n^{-3/2}
    (NOT C * 3^n as would be the case for a rational GF).

    Parameters
    ----------
    level : optional
        Level k of V_k(sl_2).  Not used in the eigenvalue computation
        (eigenvalues are level-independent for non-critical k).

    Returns
    -------
    KSTransportOperator
    """
    evals = [Integer(3), Integer(-1)]
    char_poly = expand((lam - 3) * (lam + 1))
    disc = expand((1 - 3 * x) * (1 + x))

    return KSTransportOperator(
        algebra_name='sl2',
        rank=1,
        ks_dimension=2,
        eigenvalues=evals,
        characteristic_polynomial=Poly(char_poly, lam),
        discriminant=disc,
        gf_type='algebraic',
        ds_invariant_factor=None,
    )


def ks_operator_sl3(level: Optional[Any] = None) -> KSTransportOperator:
    r"""KS transport operator for sl_3 at non-critical level.

    The bar GF for sl_3 is RATIONAL:
        P(x) = 4x(2 - 13x - 2x^2) / ((1 - 8x)(1 - 3x - x^2))

    Eigenvalues {8, (3+sqrt(13))/2, (3-sqrt(13))/2} are the poles.
    The bar dims satisfy the linear recurrence:
        a_n = 11*a_{n-1} - 23*a_{n-2} - 8*a_{n-3}
    with characteristic polynomial lambda^3 - 11*lambda^2 + 23*lambda + 8
    = (lambda - 8)(lambda^2 - 3*lambda - 1).

    Under DS reduction sl_3 -> W_3, the eigenvalue 8 is killed and
    the factor (1 - 3x - x^2) survives.

    Parameters
    ----------
    level : optional
        Level k.  Not used (eigenvalues are level-independent).
    """
    ev1 = Integer(8)
    ev2 = (3 + sqrt(13)) / 2
    ev3 = (3 - sqrt(13)) / 2
    evals = [ev1, ev2, ev3]

    char_poly = expand((lam - 8) * (lam - ev2) * (lam - ev3))
    disc = expand((1 - 8 * x) * (1 - 3 * x - x ** 2))
    ds_factor = expand(1 - 3 * x - x ** 2)

    return KSTransportOperator(
        algebra_name='sl3',
        rank=2,
        ks_dimension=3,
        eigenvalues=evals,
        characteristic_polynomial=Poly(char_poly, lam),
        discriminant=disc,
        gf_type='rational',
        ds_invariant_factor=ds_factor,
    )


def ks_operator_slN(N: int, level: Optional[Any] = None) -> KSTransportOperator:
    r"""KS transport operator for sl_N at non-critical level.

    For sl_N with rank r = N-1, the KS operator acts on an
    N-dimensional space (H^1_red has dimension N).

    Known cases:
        N = 2: eigenvalues {3, -1}, GF algebraic (Riordan)
        N = 3: eigenvalues {8, (3+sqrt(13))/2, (3-sqrt(13))/2}, GF rational

    For N >= 3, the GF is rational and the eigenvalues are the roots
    of the characteristic polynomial of the bar recursion.

    For N >= 4, eigenvalues are constructed from the transfer matrix
    encoding the weight-space decomposition of the bar complex.

    The DS-invariant subfactor has degree N-1 (one eigenvalue killed).

    Parameters
    ----------
    N : int
        Rank+1 of sl_N (so sl_2 has N=2, sl_3 has N=3, etc.).
    level : optional
        Level k.  Not used (eigenvalues are level-independent).
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    if N == 2:
        return ks_operator_sl2(level=level)
    if N == 3:
        return ks_operator_sl3(level=level)

    # For N >= 4: the bar recurrence and its characteristic polynomial
    # are not yet known.  The conjectural pattern is that the GF
    # remains rational with degree-N denominator, but the explicit
    # recurrence coefficients require bar cohomology computations at
    # sufficiently many degrees.
    #
    # For now, raise an error for N >= 4 since the transfer matrix /
    # recurrence data is not available.
    raise NotImplementedError(
        f"KS operator for sl_{N} (N >= 4) requires bar cohomology data "
        f"that is not yet computed.  Known cases: N = 2 (algebraic, "
        f"Riordan) and N = 3 (rational, recurrence [11, -23, -8])."
    )


def ks_operator_virasoro(central_charge: Optional[Any] = None) -> KSTransportOperator:
    r"""KS transport operator for the Virasoro algebra.

    The Virasoro bar GF is ALGEBRAIC of degree 2 (NOT rational).
    The Motzkin differences M(n+1) - M(n) satisfy an algebraic equation
    whose discriminant is Delta = (1 - 3x)(1 + x) = 1 - 2x - 3x^2.

    This is the SAME discriminant as sl_2.  The KS operator therefore
    has the same eigenvalues {3, -1}, reflecting the fact that Virasoro
    and sl_2 bar cohomology have the same exponential growth rate 3^n
    (with the same n^{-3/2} algebraic correction from the branch point).

    The rank is 1 (single Virasoro generator of weight 2), but the
    KS dimension is 2 because the GF has two branch points.

    IMPORTANT DISTINCTION: the KS eigenvalues detect bar cohomology
    growth.  The shadow radius rho_shadow(Vir_c) (from shadow_radius.py)
    detects shadow obstruction tower coefficient growth -- a different invariant.

    Parameters
    ----------
    central_charge : optional
        Central charge c.  Not used (KS eigenvalues are c-independent).
    """
    evals = [Integer(3), Integer(-1)]
    char_poly = expand((lam - 3) * (lam + 1))
    disc = expand((1 - 3 * x) * (1 + x))

    return KSTransportOperator(
        algebra_name='Virasoro',
        rank=1,
        ks_dimension=2,
        eigenvalues=evals,
        characteristic_polynomial=Poly(char_poly, lam),
        discriminant=disc,
        gf_type='algebraic',
        ds_invariant_factor=None,
    )


# =========================================================================
# 3. Discriminant and generating function utilities
# =========================================================================

def bar_gf_discriminant(eigenvalues: List[Any], var: str = 'x') -> Any:
    r"""Compute Delta_A(x) = prod_i (1 - lambda_i * x) from eigenvalues.

    For rational GFs, this is the denominator of P_A(x).
    For algebraic-degree-2 GFs, this is the discriminant appearing
    inside the square root of the algebraic equation.

    Parameters
    ----------
    eigenvalues : list
        Eigenvalues of the KS operator.
    var : str
        Variable name (default 'x').

    Returns
    -------
    sympy expression
        The discriminant polynomial.
    """
    t = Symbol(var)
    return expand(prod([1 - ev * t for ev in eigenvalues]))


def reconstruct_numerator(
    eigenvalues: List[Any],
    bar_dims: List[int],
    var: str = 'x',
) -> Any:
    r"""Reconstruct the numerator N(x) of P_A(x) = N(x)/Delta(x).

    Only valid for RATIONAL bar GFs (sl_3 and higher).  For algebraic
    GFs (sl_2, Virasoro), this gives the truncated product P * Delta
    which is NOT a polynomial.

    Given eigenvalues (determining Delta) and initial bar dimensions
    a_1, a_2, ..., determine N(x) so that

        N(x) / prod(1 - lambda_i * x) = sum a_n x^n + O(x^{len+1}).

    Parameters
    ----------
    eigenvalues : list
        Eigenvalues of KS (determining the denominator).
    bar_dims : list of int
        Bar cohomology dimensions [dim H^1, dim H^2, ...].
    var : str
        Variable name.

    Returns
    -------
    sympy expression
        The numerator polynomial N(x).
    """
    t = Symbol(var)
    delta = prod([1 - ev * t for ev in eigenvalues])

    # P(x) = sum_{n>=1} a_n x^n  (no constant term for reduced GF)
    p_trunc = sum(a * t ** (i + 1) for i, a in enumerate(bar_dims))

    # N(x) = P(x) * Delta(x), truncated to degree len(bar_dims)
    product = expand(p_trunc * delta)

    # Keep only terms up to degree len(bar_dims)
    numer = Integer(0)
    p = Poly(product, t)
    for monom, coeff in zip(p.monoms(), p.coeffs()):
        deg = monom[0]
        if deg <= len(bar_dims):
            numer += coeff * t ** deg

    return expand(numer)


def ds_invariant_subfactor(
    delta_parent: Any,
    delta_child: Any,
    var: str = 'x',
) -> Any:
    r"""Extract the common factor between parent and child discriminants.

    Given Delta_{sl_N}(x) and Delta_{W_N}(x), find the maximal common
    polynomial factor.  This is the DS-invariant subfactor.

    For sl_3 -> W_3:
        Delta_{sl_3} = (1 - 8x)(1 - 3x - x^2)
        Delta_{W_3}  = (1 - x)(1 - 3x - x^2)
        Common factor = (1 - 3x - x^2)

    Parameters
    ----------
    delta_parent : sympy expression
        Discriminant of the parent algebra (e.g. sl_N).
    delta_child : sympy expression
        Discriminant of the child algebra (e.g. W_N).
    var : str
        Variable name.

    Returns
    -------
    sympy expression
        The GCD of the two discriminants.
    """
    t = Symbol(var)
    p1 = Poly(delta_parent, t)
    p2 = Poly(delta_child, t)
    return Poly.gcd(p1, p2).as_expr()


# =========================================================================
# 4. Eigenvalue ladder and growth rate comparison
# =========================================================================

def eigenvalue_ladder(max_N: int = 3) -> Dict[int, KSTransportOperator]:
    r"""Compute KS operators for sl_2 through sl_{max_N}.

    Tracks how eigenvalues, dominant growth rates, and DS-invariant
    subfactors evolve with N.

    Currently only sl_2 and sl_3 have known bar recurrences.
    For N >= 4, the entry is skipped (bar recurrence data unavailable).

    Parameters
    ----------
    max_N : int
        Maximum N for sl_N (default 3).

    Returns
    -------
    dict mapping N -> KSTransportOperator
    """
    ladder = {}
    for N in range(2, max_N + 1):
        try:
            ladder[N] = ks_operator_slN(N)
        except NotImplementedError:
            pass
    return ladder


def growth_rate_comparison(
    families: Optional[List[str]] = None,
) -> Dict[str, Dict[str, Any]]:
    r"""Compare dominant bar growth rates across standard families.

    The dominant growth rate lambda_max controls the exponential growth
    of bar cohomology dimensions: dim H^n(B(A)) ~ C * lambda_max^n
    (rational) or C * lambda_max^n * n^{-3/2} (algebraic).

    Default families: Heisenberg, sl_2, sl_3, Virasoro.

    Heisenberg:
        GF = partition function.  Growth is subexponential
        (Hardy-Ramanujan: p(n) ~ exp(pi*sqrt(2n/3)) / (4n*sqrt(3))).
        No KS eigenvalues (no finite-degree discriminant).

    sl_2: dominant eigenvalue 3, algebraic GF.
    sl_3: dominant eigenvalue 8, rational GF.
    Virasoro: dominant eigenvalue 3, algebraic GF (same disc as sl_2).

    Parameters
    ----------
    families : list of str, optional
        Family names to compare.  Defaults to standard set.

    Returns
    -------
    dict mapping family name to info dict with keys:
        'dominant_growth_rate', 'eigenvalues', 'discriminant_degree',
        'gf_type'
    """
    if families is None:
        families = ['Heisenberg', 'sl2', 'sl3', 'Virasoro']

    result = {}

    for fam in families:
        if fam == 'Heisenberg':
            result[fam] = {
                'dominant_growth_rate': float('inf'),
                'eigenvalues': None,
                'discriminant_degree': None,
                'gf_type': 'transcendental',
                'note': 'Subexponential growth (Hardy-Ramanujan); no finite discriminant.',
            }
        elif fam == 'sl2':
            op = ks_operator_sl2()
            result[fam] = {
                'dominant_growth_rate': op.dominant_growth_rate,
                'eigenvalues': op.eigenvalues,
                'discriminant_degree': 2,
                'gf_type': op.gf_type,
            }
        elif fam == 'sl3':
            op = ks_operator_sl3()
            result[fam] = {
                'dominant_growth_rate': op.dominant_growth_rate,
                'eigenvalues': op.eigenvalues,
                'discriminant_degree': 3,
                'gf_type': op.gf_type,
            }
        elif fam == 'Virasoro':
            op = ks_operator_virasoro()
            result[fam] = {
                'dominant_growth_rate': op.dominant_growth_rate,
                'eigenvalues': op.eigenvalues,
                'discriminant_degree': 2,
                'gf_type': op.gf_type,
            }
        elif fam.startswith('sl') and fam[2:].isdigit():
            N = int(fam[2:])
            try:
                op = ks_operator_slN(N)
                result[fam] = {
                    'dominant_growth_rate': op.dominant_growth_rate,
                    'eigenvalues': op.eigenvalues,
                    'discriminant_degree': N,
                    'gf_type': op.gf_type,
                }
            except NotImplementedError:
                result[fam] = {
                    'dominant_growth_rate': None,
                    'eigenvalues': None,
                    'discriminant_degree': N,
                    'gf_type': None,
                    'note': f'Bar recurrence data not yet available for sl_{N}.',
                }
        else:
            result[fam] = {
                'dominant_growth_rate': None,
                'eigenvalues': None,
                'discriminant_degree': None,
                'gf_type': None,
                'note': f'Unknown family: {fam}',
            }

    return result


# =========================================================================
# 5. Partial fractions (for rational GFs only)
# =========================================================================

def partial_fractions_from_eigenvalues(
    eigenvalues: List[Any],
    bar_dims: List[int],
) -> List[Any]:
    r"""Compute partial fraction coefficients for the bar GF.

    Given eigenvalues {lambda_i} and bar dims [a_1, a_2, ...],
    solve for {c_i} such that a_n = sum c_i * lambda_i^n.

    ONLY VALID for rational GFs (sl_3, sl_N with N >= 3, W_N).
    For algebraic GFs (sl_2, Virasoro), the returned coefficients
    will NOT reproduce bar dims exactly.

    Parameters
    ----------
    eigenvalues : list
        KS eigenvalues.
    bar_dims : list of int
        [dim H^1, dim H^2, ...] (1-indexed).

    Returns
    -------
    list of sympy expressions
        The partial fraction coefficients [c_1, ..., c_d].
    """
    d = len(eigenvalues)
    if len(bar_dims) < d:
        raise ValueError(
            f"Need at least {d} bar dims for {d} eigenvalues, "
            f"got {len(bar_dims)}"
        )

    A_mat = Matrix([
        [ev ** (n + 1) for ev in eigenvalues]
        for n in range(d)
    ])
    b_vec = Matrix(bar_dims[:d])

    return list(A_mat.solve(b_vec))


def predict_bar_dims(
    eigenvalues: List[Any],
    pf_coefficients: List[Any],
    max_n: int = 20,
) -> List[Any]:
    r"""Predict bar dimensions from eigenvalues and partial fraction coefficients.

    For rational GFs, this gives exact bar dimensions.
    For algebraic GFs, this gives an approximation that diverges
    from the true values due to the missing n^{-3/2} correction.

    Parameters
    ----------
    eigenvalues : list
        KS eigenvalues.
    pf_coefficients : list
        Partial fraction coefficients [c_1, ..., c_d].
    max_n : int
        Number of terms to predict.

    Returns
    -------
    list of sympy expressions
        Predicted [dim H^1, dim H^2, ..., dim H^{max_n}].
    """
    return [
        simplify(sum(c * ev ** n for c, ev in zip(pf_coefficients, eigenvalues)))
        for n in range(1, max_n + 1)
    ]


# =========================================================================
# 6. Numerical verification
# =========================================================================

def verify_eigenvalue_discriminant(
    operator: KSTransportOperator,
    bar_dims: Dict[int, int],
    max_n: int = 20,
) -> Dict[str, Any]:
    r"""Verify that KS eigenvalues reproduce known bar dimensions.

    For RATIONAL GFs: uses partial fractions to check exact agreement.
    For ALGEBRAIC GFs: checks that the dominant eigenvalue gives the
    correct exponential growth rate by verifying a_n / lambda_max^n
    converges (rather than checking exact equality).

    Parameters
    ----------
    operator : KSTransportOperator
        The KS operator to verify.
    bar_dims : dict
        Mapping n -> dim H^n(B(A)) for known values.
    max_n : int
        Maximum n for extrapolation / growth rate check.

    Returns
    -------
    dict with keys:
        'consistent': bool
        'method': 'partial_fractions' or 'growth_rate'
        'details': method-specific details
    """
    evals = operator.eigenvalues
    d = len(evals)

    known_ns = sorted(bar_dims.keys())
    if len(known_ns) < d:
        return {
            'consistent': None,
            'method': None,
            'details': {
                'note': f'Need at least {d} known dims, got {len(known_ns)}.',
            },
        }

    if operator.gf_type == 'rational':
        return _verify_rational(operator, bar_dims, max_n)
    else:
        return _verify_algebraic(operator, bar_dims, max_n)


def _verify_rational(
    operator: KSTransportOperator,
    bar_dims: Dict[int, int],
    max_n: int,
) -> Dict[str, Any]:
    r"""Verify a rational GF via partial fractions (exact match expected)."""
    evals = operator.eigenvalues
    d = len(evals)
    known_ns = sorted(bar_dims.keys())

    # Set up the Vandermonde-type system
    ns_for_solve = known_ns[:d]
    A_mat = Matrix([
        [ev ** n for ev in evals]
        for n in ns_for_solve
    ])
    b_vec = Matrix([bar_dims[n] for n in ns_for_solve])

    try:
        c_vec = A_mat.solve(b_vec)
    except Exception:
        return {
            'consistent': False,
            'method': 'partial_fractions',
            'details': {'note': 'Vandermonde system is singular.'},
        }

    coeffs = list(c_vec)
    predictions = {}
    errors = {}
    consistent = True

    for n in range(1, max_n + 1):
        predicted = sum(c * ev ** n for c, ev in zip(coeffs, evals))
        predicted_simplified = simplify(predicted)
        predictions[n] = predicted_simplified

        if n in bar_dims:
            actual = bar_dims[n]
            if simplify(predicted_simplified - actual) != 0:
                consistent = False
                errors[n] = (predicted_simplified, actual)

    return {
        'consistent': consistent,
        'method': 'partial_fractions',
        'details': {
            'residue_coefficients': coeffs,
            'predictions': predictions,
            'errors': errors,
        },
    }


def _verify_algebraic(
    operator: KSTransportOperator,
    bar_dims: Dict[int, int],
    max_n: int,
) -> Dict[str, Any]:
    r"""Verify an algebraic GF via successive ratio convergence.

    For an algebraic GF with dominant singularity at x = 1/lambda_max
    (a square-root branch point), the asymptotics are:
        a_n ~ C * lambda_max^n * n^{-3/2}
    so the ratio a_{n+1}/a_n converges to lambda_max as:
        a_{n+1}/a_n = lambda_max * (1 - 3/(2n) + O(1/n^2))

    We verify that (1) ratios are increasing toward lambda_max, and
    (2) the last ratio is within the expected O(1/n) of lambda_max.
    """
    lam_max = max(operator.eigenvalues,
                  key=lambda ev: float(Abs(Neval(ev))))
    lam_max_float = float(Abs(Neval(lam_max)))

    known_ns = sorted(bar_dims.keys())
    consecutive_ratios = []

    for i in range(len(known_ns) - 1):
        n1, n2 = known_ns[i], known_ns[i + 1]
        if n2 == n1 + 1 and bar_dims[n1] > 0:
            ratio = bar_dims[n2] / bar_dims[n1]
            consecutive_ratios.append((n1, ratio))

    if len(consecutive_ratios) < 3:
        return {
            'consistent': None,
            'method': 'growth_rate',
            'details': {'note': 'Need at least 4 consecutive bar dims.'},
        }

    # Check: ratios should approach lambda_max from below
    # For n^{-3/2} correction, a_{n+1}/a_n ~ lambda_max * (1 - 3/(2n))
    # At n = last_n, expected ratio ~ lambda_max * (1 - 1.5/last_n)
    last_n, last_ratio = consecutive_ratios[-1]
    expected_ratio = lam_max_float * (1 - 1.5 / last_n)
    deviation = abs(last_ratio - expected_ratio) / lam_max_float

    # Also check monotone increase in the tail (last 5 ratios)
    tail = consecutive_ratios[-5:]
    monotone = all(tail[i][1] <= tail[i + 1][1] for i in range(len(tail) - 1))

    # Consistency: deviation < 5% and ratios monotonically increasing
    consistent = deviation < 0.05 and monotone

    return {
        'consistent': consistent,
        'method': 'growth_rate',
        'details': {
            'dominant_eigenvalue': lam_max,
            'dominant_eigenvalue_float': lam_max_float,
            'last_ratio': last_ratio,
            'expected_ratio_at_n': expected_ratio,
            'deviation': deviation,
            'monotone_tail': monotone,
            'consecutive_ratios': consecutive_ratios,
        },
    }


# =========================================================================
# 7. DS reduction analysis
# =========================================================================

def ds_reduction_analysis(N: int) -> Dict[str, Any]:
    r"""Analyse the Drinfeld-Sokolov reduction sl_N -> W_N at KS level.

    For sl_N -> W_N, one eigenvalue (the 'Lie' eigenvalue from the
    Cartan subalgebra contribution) is killed.  The surviving eigenvalues
    give the W_N bar growth rates.

    For sl_3 -> W_3:
        Killed: eigenvalue 8 (dominant for sl_3)
        Surviving: {(3+sqrt(13))/2, (3-sqrt(13))/2}
        W_3 dominant growth rate: (3+sqrt(13))/2 ~ 3.303

    Parameters
    ----------
    N : int
        sl_N rank parameter.

    Returns
    -------
    dict with keys:
        'parent': KSTransportOperator for sl_N
        'killed_eigenvalue': the Lie eigenvalue
        'surviving_eigenvalues': list
        'surviving_discriminant': polynomial
        'w_growth_rate': dominant growth rate of W_N
    """
    parent = ks_operator_slN(N)

    # The largest eigenvalue is the Lie eigenvalue (Cartan contribution)
    evals_abs = [(ev, float(Abs(Neval(ev)))) for ev in parent.eigenvalues]
    evals_abs.sort(key=lambda p: p[1], reverse=True)
    killed = evals_abs[0][0]
    surviving = [ev for ev in parent.eigenvalues
                 if simplify(ev - killed) != 0]

    surv_disc = expand(prod([1 - ev * x for ev in surviving]))
    surv_rates = [float(Abs(Neval(ev))) for ev in surviving]
    w_growth = max(surv_rates) if surv_rates else 0.0

    return {
        'parent': parent,
        'killed_eigenvalue': killed,
        'surviving_eigenvalues': surviving,
        'surviving_discriminant': surv_disc,
        'w_growth_rate': w_growth,
    }


# =========================================================================
# 8. Recurrence <-> eigenvalue conversion
# =========================================================================

def characteristic_polynomial_from_recurrence(
    recurrence_coeffs: List[Any],
) -> Any:
    r"""Convert a linear recurrence to its characteristic polynomial.

    If a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_d a_{n-d},
    the characteristic polynomial is
        lambda^d - c_1 lambda^{d-1} - c_2 lambda^{d-2} - ... - c_d.

    Parameters
    ----------
    recurrence_coeffs : list
        [c_1, c_2, ..., c_d] from the recurrence.

    Returns
    -------
    sympy Poly in ``lam``
    """
    d = len(recurrence_coeffs)
    poly_expr = lam ** d
    for i, c in enumerate(recurrence_coeffs):
        poly_expr -= c * lam ** (d - 1 - i)
    return Poly(expand(poly_expr), lam)


def eigenvalues_from_recurrence(recurrence_coeffs: List[Any]) -> List[Any]:
    r"""Extract eigenvalues (roots of char poly) from a linear recurrence.

    Parameters
    ----------
    recurrence_coeffs : list
        [c_1, c_2, ..., c_d] from a_n = c_1 a_{n-1} + ... + c_d a_{n-d}.

    Returns
    -------
    list of sympy expressions
        Roots of the characteristic polynomial.
    """
    char_p = characteristic_polynomial_from_recurrence(recurrence_coeffs)
    return solve(char_p.as_expr(), lam)


# =========================================================================
# 9. Internal verification routines
# =========================================================================

def _verify_sl2_eigenvalues() -> bool:
    r"""Verify sl_2 KS eigenvalues give correct exponential growth rate.

    The Riordan bar dims a_n = R(n+3) satisfy a_n ~ C * 3^n * n^{-3/2},
    so the ratio a_{n+1}/a_n converges to 3 as 3*(1 - 3/(2n)).

    We check: (1) ratios are monotonically increasing in the tail,
    (2) last ratio is within expected O(1/n) of 3.

    Returns True if the growth rate is consistent with dominant eigenvalue 3.
    """
    from .bar_gf_algebraicity import sl2_bar_dims

    known = sl2_bar_dims(20)
    ratios = [known[i + 1] / known[i] for i in range(len(known) - 1)]

    # Tail monotonicity (last 10)
    tail = ratios[-10:]
    if not all(tail[i] <= tail[i + 1] for i in range(len(tail) - 1)):
        return False

    # Last ratio vs expected: 3*(1 - 1.5/n) at n=19
    n = len(known) - 1
    expected = 3.0 * (1 - 1.5 / n)
    return abs(ratios[-1] - expected) / 3.0 < 0.03


def _verify_sl3_eigenvalues() -> bool:
    r"""Verify sl_3 KS eigenvalues reproduce bar dims via partial fractions.

    Since sl_3 has a rational bar GF, the partial fractions formula
    a_n = c_1 * 8^n + c_2 * phi_+^n + c_3 * phi_-^n (where
    phi_pm = (3 +/- sqrt(13))/2) should give EXACT bar dims.

    Also verifies the linear recurrence a_n = 11*a_{n-1} - 23*a_{n-2} - 8*a_{n-3}.

    Returns True if the first 10 dims match exactly.
    """
    from .bar_gf_algebraicity import sl3_bar_dims

    known = sl3_bar_dims(10)

    # Verify the recurrence first
    for i in range(3, len(known)):
        expected = 11 * known[i - 1] - 23 * known[i - 2] - 8 * known[i - 3]
        if expected != known[i]:
            return False

    # Verify partial fractions
    op = ks_operator_sl3()
    coeffs = partial_fractions_from_eigenvalues(
        op.eigenvalues, known[:3]
    )
    predicted = predict_bar_dims(op.eigenvalues, coeffs, max_n=10)
    return all(simplify(p - a) == 0 for p, a in zip(predicted, known))


def _verify_virasoro_growth_rate() -> bool:
    r"""Verify Virasoro bar dims have dominant growth rate 3.

    The Motzkin differences M(n+1) - M(n) grow as ~ C * 3^n * n^{-3/2},
    same exponential rate as sl_2.

    We check: (1) ratios are monotonically increasing in the tail,
    (2) last ratio is within expected O(1/n) of 3.

    Returns True if the growth rate is consistent with dominant eigenvalue 3.
    """
    from .bar_gf_algebraicity import virasoro_bar_dims

    known = virasoro_bar_dims(20)
    ratios = [known[i + 1] / known[i] for i in range(len(known) - 1)
              if known[i] > 0]

    # Tail monotonicity (last 10)
    tail = ratios[-10:]
    if not all(tail[i] <= tail[i + 1] for i in range(len(tail) - 1)):
        return False

    # Last ratio vs expected: 3*(1 - 1.5/n) at n=19
    n = len(known) - 1
    expected = 3.0 * (1 - 1.5 / n)
    return abs(ratios[-1] - expected) / 3.0 < 0.03


# =========================================================================
# 10. Summary and display
# =========================================================================

def ks_summary_table(max_N: int = 3) -> List[Dict[str, Any]]:
    r"""Summary table of KS operators for sl_2 through sl_{max_N} + Virasoro.

    Returns a list of dicts with keys:
        'algebra', 'rank', 'ks_dim', 'eigenvalues', 'dominant_rate',
        'gf_type', 'discriminant', 'ds_invariant_factor'

    Parameters
    ----------
    max_N : int
        Maximum N for sl_N.
    """
    rows = []

    for N in range(2, max_N + 1):
        try:
            op = ks_operator_slN(N)
        except NotImplementedError:
            continue
        rows.append({
            'algebra': op.algebra_name,
            'rank': op.rank,
            'ks_dim': op.ks_dimension,
            'eigenvalues': op.eigenvalues,
            'dominant_rate': op.dominant_growth_rate,
            'gf_type': op.gf_type,
            'discriminant': op.discriminant,
            'ds_invariant_factor': op.ds_invariant_factor,
        })

    vir = ks_operator_virasoro()
    rows.append({
        'algebra': vir.algebra_name,
        'rank': vir.rank,
        'ks_dim': vir.ks_dimension,
        'eigenvalues': vir.eigenvalues,
        'dominant_rate': vir.dominant_growth_rate,
        'gf_type': vir.gf_type,
        'discriminant': vir.discriminant,
        'ds_invariant_factor': vir.ds_invariant_factor,
    })

    return rows
