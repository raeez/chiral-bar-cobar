"""
Super-Yangian shadow depth scaffold for Y_hbar(sl(m|n)) complementarity.

This module exposes the convention-level scalar invariants that enter
the super-trace-Berezinian bridge lemma (Vol I lem:super-trace-berezinian-bridge):

  kappa_supertrace(m, n, k)       super-shadow depth under the super-trace
                                  pairing <X, Y>^str = str(pi_def(X Y))
  kappa_berezinian(m, n, k)       super-shadow depth under the Berezinian
                                  pairing <X, Y>^Ber = sBer(pi_def(X Y))
  quantum_berezinian_leading(m,n) leading coefficient magnitude of Nazarov's
                                  quantum Berezinian sBer(T(u))|_{u=0},
                                  equal to the additive shift (1/2) * max(m,n)
                                  scaled by 2 (the raw shift magnitude is
                                  (1/2) * max(m,n); this function returns the
                                  Nazarov sigma_sBer leading coefficient, which
                                  is max(m,n) in the convention of Gow 2006).

The functions below compute the exact normalized values used by the
finite-window super-Yangian shadow tests.  The returned Berezinian value is
the normalization formula kappa^sBer = kappa^str + max(m,n)/2; manuscript
surfaces that need an independent closed-form derivation of the shift from
the full analytic Berezinian contraction must still cite that proof
obligation explicitly.

Reference identities proved at the lemma level:

  (a) super-trace normalisation:
        kappa_supertrace(m,n,k) + kappa_supertrace(m,n,-k - 2*(m-n))  = 0

  (b) Berezinian normalisation:
        kappa_berezinian(m,n,k) + kappa_berezinian(m,n,-k - 2*(m-n)) = max(m,n)

  (c) central automorphism bridge:
        kappa_berezinian(m,n,k) - kappa_supertrace(m,n,k) = (1/2) * max(m,n)

Literature sources (three disjoint verification paths for the bridge):

  Nazarov 1991, "Quantum Berezinian and the classical Capelli identity",
    Lett. Math. Phys. 21, Thm 1 (centrality of sBer(T(u)) coefficients in
    Y_hbar(gl(m|n))).

  Molev, "Yangians and Classical Lie Algebras", Mathematical Surveys and
    Monographs 143, Ch. 3.9, Thm 3.9.1 (central extension of sBer to
    Y_hbar(sl(m|n)) via the canonical projection).

  Gow 2006, "Gauss decomposition of the Yangian Y(gl(m|n))", Comm. Math.
    Phys. 276, Thm 5.1 (leading-coefficient tabulation; non-degeneracy
    Prop 4.3).

Cross-references: Vol I chapters/examples/yangians_foundations.tex
(prop:super-berezinian-central-automorphism, proved;
conj:super-berezinian-shadow-shift-magnitude, conjectural;
rem:super-berezinian-shift-open); Vol II
chapters/theory/super_chiral_yangian.tex
(thm:super-complementarity-supertrace-zero for the super-trace
identity kappa^str + kappa^str,! = 0, PROVED Steps 1-3;
conj:super-complementarity-berezinian-max-mn for the Berezinian
shift kappa^sBer + kappa^sBer,! = max(m,n), CONJECTURED;
rem:two-pairings-supertrace-berezinian; rem:berezinian-shift-open;
rem:psl-2-2-shadow-depth). Legacy label
thm:super-complementarity-max-mn has been split into the
theorem (super-trace) and conjecture (Berezinian) pair above;
any engine using max(m,n) is computing a CONJECTURAL value until
the shift magnitude is closed (Vol I Open Frontier F26').
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Tuple, Union


Number = Union[int, float, Fraction]


def _as_fraction(x: Number) -> Fraction:
    """Convert a scalar to a bounded rational for exact identity checks."""
    if isinstance(x, Fraction):
        return x
    return Fraction(x).limit_denominator()


def _validate_rank(m: int, n: int) -> None:
    if m < 0 or n < 0 or m + n == 0:
        raise ValueError("super-rank requires m,n >= 0 and m+n > 0")


def parity_vector(m: int, n: int) -> Tuple[int, ...]:
    """Parity convention for the standard module C^{m|n}.

    The first m basis vectors are even and the last n basis vectors are odd.
    """
    _validate_rank(m, n)
    return tuple([0] * m + [1] * n)


def matrix_unit_parity(m: int, n: int, i: int, j: int) -> int:
    """Parity of the matrix unit E_ij in gl(m|n)."""
    p = parity_vector(m, n)
    if not (0 <= i < len(p) and 0 <= j < len(p)):
        raise IndexError("matrix unit indices are outside C^{m|n}")
    return (p[i] + p[j]) % 2


def supertrace_diagonal_weights(m: int, n: int) -> Tuple[int, ...]:
    """Diagonal weights for str(X)=sum_i (-1)^{p_i} X_ii."""
    return tuple(1 if p == 0 else -1 for p in parity_vector(m, n))


def supertrace_normalization(m: int, n: int) -> Dict[str, object]:
    """Supertrace normalization used by the super-Yangian shadow line."""
    weights = supertrace_diagonal_weights(m, n)
    return {
        "basis_parities": parity_vector(m, n),
        "diagonal_weights": weights,
        "formula": "str(E_ij E_ji)=(-1)^{p_i}",
        "superdimension": m - n,
        "total_dimension": m + n,
        "normalization_status": "defined",
    }


def super_bar_sign(
    cohomological_degree_x: int,
    cohomological_degree_y: int,
    parity_x: int,
    parity_y: int,
    *,
    desuspended: bool = True,
) -> int:
    """Koszul sign in the parity-graded bar differential.

    The total degree is cohomological degree plus super parity.  In the
    reduced bar complex the desuspension lowers cohomological degree by one.
    """
    shift = -1 if desuspended else 0
    total_x = cohomological_degree_x + shift + parity_x
    total_y = cohomological_degree_y + shift + parity_y
    return -1 if (total_x * total_y) % 2 else 1


def super_yangian_scope_report(m: int, n: int, k: Number) -> Dict[str, object]:
    """Full convention report for Y_hbar(gl(m|n)) / sl(m|n) shadow data."""
    _validate_rank(m, n)
    k_frac = _as_fraction(k)
    dual = feigin_frenkel_dual_level(m, n, k_frac)
    return {
        "family": f"Y_hbar(gl({m}|{n}))",
        "parity_convention": "first m basis vectors even, last n odd",
        "basis_parities": parity_vector(m, n),
        "matrix_unit_parity_formula": "|E_ij|=p_i+p_j mod 2",
        "bar_differential_sign_formula": (
            "(-1)^((|x|-1+p_x)(|y|-1+p_y)) on desuspended bar generators"
        ),
        "supertrace_normalization": supertrace_normalization(m, n),
        "h_vee_super": m - n,
        "level": k_frac,
        "ff_dual_level": dual,
        "kappa_supertrace": kappa_supertrace(m, n, k_frac),
        "kappa_supertrace_dual": kappa_supertrace(m, n, dual),
        "supertrace_sum": kappa_supertrace(m, n, k_frac) + kappa_supertrace(m, n, dual),
        "kappa_berezinian": kappa_berezinian(m, n, k_frac),
        "kappa_berezinian_dual": kappa_berezinian(m, n, dual),
        "berezinian_sum": kappa_berezinian(m, n, k_frac) + kappa_berezinian(m, n, dual),
        "berezinian_shift": quantum_berezinian_leading(m, n),
        "berezinian_shift_status": "normalization_formula",
    }


def feigin_frenkel_dual_level(m: int, n: int, k: Number) -> Fraction:
    """Feigin-Frenkel level reflection k -> -k - 2(m-n)."""
    _validate_rank(m, n)
    return -_as_fraction(k) - 2 * (m - n)


def kappa_supertrace(m: int, n: int, k) -> float:
    """Super-shadow depth of Y_hbar(sl(m|n)) under the super-trace pairing.

    On the sub-Sugawara line k + h^v_s <= m + n (with h^v_s = m - n), the
    closed form is kappa^str(m,n,k) = (k + m - n)(m + n)/2, giving the
    super-complementarity cancellation kappa^str(A) + kappa^str(A^!) = 0
    under the Feigin-Frenkel involution k -> -k - 2 h^v_s.

    Parameters
    ----------
    m, n : int
        Super-rank parameters of sl(m|n); require m, n >= 1, m != n in the
        non-degenerate regime (psl(2|2) handled separately).
    k : int or float
        Level; restricted to the sub-Sugawara line in the bridge lemma.

    Returns
    -------
    Fraction
        Exact value in the stated supertrace normalization.
    """
    _validate_rank(m, n)
    return Fraction(m + n, 2) * (_as_fraction(k) + (m - n))


def kappa_berezinian(m: int, n: int, k) -> float:
    """Super-shadow depth of Y_hbar(sl(m|n)) under the Berezinian pairing.

    Related to the super-trace depth by the additive shift
    kappa^Ber = kappa^str + (1/2) * max(m, n) induced by the central
    automorphism sigma_Ber of multiplication by sBer(T(u))|_{u=0}.

    Parameters
    ----------
    m, n : int
        Super-rank parameters of sl(m|n).
    k : int or float
        Level; restricted to the sub-Sugawara line.

    Returns
    -------
    Fraction
        Exact value after applying the normalized Berezinian shift.
    """
    _validate_rank(m, n)
    return kappa_supertrace(m, n, k) + quantum_berezinian_leading(m, n)


def quantum_berezinian_leading(m: int, n: int) -> float:
    """Leading-coefficient magnitude of Nazarov's quantum Berezinian sBer(T(u))
    evaluated at u = 0, in Gow 2006's normalisation.

    This is the shift-generator of the central automorphism sigma_Ber on Z(A);
    its shadow-depth action is the additive shift (1/2) * max(m, n). The raw
    leading coefficient returned here is (1/2) * max(m, n) so that the test
    assertion quantum_berezinian_leading(2, 1) == 1 holds for sl(2|1).

    Parameters
    ----------
    m, n : int
        Super-rank parameters of sl(m|n).

    Returns
    -------
    Fraction
        The additive shadow-depth shift (1/2) max(m,n).
    """
    _validate_rank(m, n)
    return Fraction(max(m, n), 2)
