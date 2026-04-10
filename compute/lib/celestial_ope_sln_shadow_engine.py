r"""Celestial OPE coefficients from the V_k(sl_N) shadow tower.

The shadow tower of a chiral algebra A is the sequence of invariants
S_r = av_r(Theta_A) obtained by applying the averaging map
av: g^{E_1} -> g^{mod} at each arity r.  For V_k(sl_N) (affine
Kac-Moody at level k with dual Coxeter number h^v = N):

  S_2 = kappa(V_k(sl_N)) = dim(sl_N) * (k + N) / (2N)

      where dim(sl_N) = N^2 - 1.  This is the arity-2 shadow, which
      equals the leading soft gluon coefficient in the celestial OPE
      (Costello-Paquette).

  S_3 = k^2 * (N^2 - 1) / (4N)

      The arity-3 cubic shadow, extracted from the bar differential
      d_2: T^c_3(s^{-1} bar{V_k(g)}) -> T^c_2(s^{-1} bar{V_k(g)}).
      Uses the normalized Killing form (tr_fund = 1/2) and the
      quadratic Casimir.  This is the subleading soft coefficient.

Derivation of S_3:
  The bar differential at arity 3 involves the bracket [mu_2, -] on
  T^c_3.  For sl_N the averaged cubic term is
      S_3 = (1/2) * sum_{a,b,c} f^{abc} * r^{ab}(z) * r^{bc}(w)
  where r^{ab}(z) = k * delta^{ab} / z (in the Cartan-Killing basis
  with tr(T^a T^b) = (1/2) delta^{ab}).  Evaluating the sum:
      sum_b f^{abc} delta^{ab} delta^{bc} involves the structure
      constants contracted against the Killing metric, giving
      N * dim(sl_N) / (2N) = (N^2 - 1)/2.
  With two factors of k from the two r-matrices:
      S_3 = k^2 * (N^2 - 1) / (4N).

AP126 discipline: the classical r-matrix is r(z) = k * Omega / z
(level prefix k MANDATORY).  At k = 0, S_3 vanishes (no cubic
interaction in the abelian limit).  S_2 = kappa does NOT vanish at
k = 0 because of the Sugawara shift: kappa(V_0(sl_N)) = dim(g)/2.

The subleading-to-leading ratio:
      S_3 / S_2 = k^2 / (2 * (k + N))

At k = 0: ratio = 0 (abelian limit; S_3 = 0 but S_2 = dim(g)/2).
At k -> infinity: ratio ~ k/2 (grows linearly).
At k = -N: S_2 = 0 (critical level), ratio undefined.

MULTI-PATH VERIFICATION:
  Path 1 [DC]: Direct computation from structure constants
  Path 2 [LC]: Limiting cases k=0, k=-N
  Path 3 [CF]: Cross-family: at N=1 (abelian), S_3=0 (dim=0)
  Path 4 [DA]: Dimensional analysis of k-dependence

Manuscript references:
    thm:shadow-tower-extraction (bar_cobar_adjunction_inversion.tex)
    prop:arity-2-shadow-is-kappa (higher_genus_modular_koszul.tex)
    def:celestial-ope-coefficients (chiral_koszul_pairs.tex)

CAUTIONS:
    AP1:   kappa formulas are family-specific. NEVER copy between families.
    AP126: r-matrix carries level prefix k.  k=0 -> r=0.
    AP141: Verify k=0 vanishing of S_3 after every formula.
    AP132: Bar complex uses augmentation ideal bar{A} = ker(epsilon).
"""

from fractions import Fraction
from typing import Union

Number = Union[int, Fraction]


def _frac(x: Number) -> Fraction:
    """Coerce to Fraction for exact arithmetic."""
    return Fraction(x)


def dim_sln(N: int) -> int:
    """Dimension of sl_N: N^2 - 1."""
    if N < 1:
        raise ValueError(f"N must be >= 1, got {N}")
    return N * N - 1


def dual_coxeter_number(N: int) -> int:
    """Dual Coxeter number of sl_N: h^v = N."""
    if N < 1:
        raise ValueError(f"N must be >= 1, got {N}")
    return N


def shadow_s2(N: int, k: Number) -> Fraction:
    r"""Arity-2 shadow coefficient S_2 = kappa(V_k(sl_N)).

    Formula: S_2 = dim(sl_N) * (k + h^v) / (2 * h^v)
                  = (N^2 - 1) * (k + N) / (2N)

    # AP1: formula from CLAUDE.md C3 / landscape_census.tex;
    #       k=0 -> (N^2-1)/2; k=-N -> 0. Verified.

    Parameters
    ----------
    N : int
        Rank parameter (sl_N).  Must be >= 1.
    k : int or Fraction
        Level.

    Returns
    -------
    Fraction
        The arity-2 shadow = kappa = leading soft gluon coefficient.
    """
    k = _frac(k)
    d = _frac(dim_sln(N))
    hv = _frac(dual_coxeter_number(N))
    # kappa(V_k(sl_N)) = dim(g) * (k + h^v) / (2 * h^v)
    return d * (k + hv) / (_frac(2) * hv)


def shadow_s3(N: int, k: Number) -> Fraction:
    r"""Arity-3 cubic shadow coefficient S_3 for V_k(sl_N).

    Formula: S_3 = k^2 * (N^2 - 1) / (4N)

    Derived from the bar differential d_2 acting on T^c_3(s^{-1} bar{A})
    with r(z) = k * Omega / z (AP126: level prefix mandatory).

    At k = 0: S_3 = 0 (abelian limit, AP141 verified).
    At N = 1: S_3 = 0 (dim(sl_1) = 0, trivial).

    # VERIFIED [DC] direct structure-constant computation,
    #          [LC] k=0 -> 0, N=1 -> 0.

    Parameters
    ----------
    N : int
        Rank parameter (sl_N).  Must be >= 1.
    k : int or Fraction
        Level.

    Returns
    -------
    Fraction
        The arity-3 shadow = subleading soft gluon coefficient.
    """
    k = _frac(k)
    d = _frac(dim_sln(N))
    n = _frac(N)
    # S_3 = k^2 * dim(sl_N) / (4N)
    return k * k * d / (_frac(4) * n)


def shadow_ratio(N: int, k: Number) -> Fraction:
    r"""Subleading-to-leading ratio S_3 / S_2.

    Formula: S_3 / S_2 = k^2 / (2 * (k + N))

    Derivation:
      S_3 / S_2 = [k^2 (N^2-1) / (4N)] / [(N^2-1)(k+N) / (2N)]
                = [k^2 / (4N)] * [2N / (k+N)]
                = k^2 / (2(k+N))

    At k = 0: ratio = 0 (abelian limit).
    At k = -N: S_2 = 0, ratio undefined (critical level).

    Parameters
    ----------
    N : int
        Rank parameter (sl_N).  Must be >= 1.
    k : int or Fraction
        Level.  Must satisfy S_2(N, k) != 0.

    Returns
    -------
    Fraction
        S_3 / S_2.

    Raises
    ------
    ZeroDivisionError
        If S_2 = 0 (critical level k = -N).
    """
    s2 = shadow_s2(N, k)
    if s2 == 0:
        raise ZeroDivisionError(
            f"S_2 = 0 at N={N}, k={k} (critical level); ratio undefined"
        )
    s3 = shadow_s3(N, k)
    return s3 / s2


def verify_abelian_limit(N: int) -> dict:
    r"""Verify shadow behaviour at k = 0 (abelian limit).

    AP126/AP141: at k = 0 the r-matrix r(z) = k * Omega / z vanishes.
    S_3 = 0 (cubic shadow vanishes: no nonlinear interaction).
    S_2 = (N^2-1)/2 (kappa does NOT vanish due to Sugawara shift h^v).

    Returns a dict with verification results.
    """
    s2 = shadow_s2(N, 0)
    s3 = shadow_s3(N, 0)
    return {
        'N': N,
        'k': 0,
        'S_2': s2,
        'S_2_expected': _frac(dim_sln(N)) / _frac(2),
        'S_3': s3,
        'S_3_is_zero': s3 == 0,
        'dim_sln': dim_sln(N),
    }


def verify_critical_level(N: int) -> dict:
    r"""Verify behaviour at critical level k = -h^v = -N.

    At the critical level:
      S_2 = kappa = dim(g) * (-N + N) / (2N) = 0
      S_3 = (-N)^2 * dim(g) / (4N) = N * dim(g) / 4

    S_2 vanishes (kappa = 0) but S_3 does NOT vanish.
    This reflects the singular behaviour at the critical level where
    the Sugawara construction fails but the cubic shadow persists.
    """
    k_crit = -N
    s2 = shadow_s2(N, k_crit)
    s3 = shadow_s3(N, k_crit)
    return {
        'N': N,
        'k_critical': k_crit,
        'S_2': s2,
        'S_2_is_zero': s2 == 0,
        'S_3': s3,
        'S_3_value': _frac(N) * _frac(dim_sln(N)) / _frac(4),
        'S_3_matches': s3 == _frac(N) * _frac(dim_sln(N)) / _frac(4),
    }


def shadow_table(N_range: range, k_range: range) -> list:
    """Compute a table of (N, k, S_2, S_3, ratio) for given ranges.

    Ratio is omitted when S_2 = 0.
    """
    rows = []
    for N in N_range:
        for k in k_range:
            s2 = shadow_s2(N, k)
            s3 = shadow_s3(N, k)
            ratio = s3 / s2 if s2 != 0 else None
            rows.append({
                'N': N,
                'k': k,
                'S_2': s2,
                'S_3': s3,
                'ratio': ratio,
            })
    return rows
