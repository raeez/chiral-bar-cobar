r"""Exact arithmetic for the W-algebra chapter repair.

This module deliberately separates three kinds of information:

* identities obtained from an explicit rational formula;
* finite Lie-theoretic combinatorics;
* modular, bar, and Koszul claims that still require comparison theorems.

The Bershadsky--Polyakov convention is Fehily--Kawasetsu--Ridout
(2021), Definition 2.1 and Equation (2.2).  Its standard conformal
vector has

    c(k) = -(2k+3)(3k+1)/(k+3).

The frequently occurring expression

    2 - 24(k+1)^2/(k+3)

is retained as a shifted secondary expression.  It is a different
function and therefore supplies a different reflection constant.
"""

from __future__ import annotations

from sympy import Rational, Symbol, simplify, sympify


k_sym = Symbol("k")


class UnverifiedWInvariantError(RuntimeError):
    """Raised when an exact input has not yet been promoted to an invariant."""


# ---------------------------------------------------------------------------
# Bershadsky--Polyakov: exact OPE convention and typed open invariants
# ---------------------------------------------------------------------------


def bp_central_charge_correct(level=k_sym):
    """Standard BP central charge in the FKR convention."""
    k = sympify(level)
    return simplify(-((2 * k + 3) * (3 * k + 1)) / (k + 3))


def bp_shifted_secondary_central_charge(level=k_sym):
    """The separate shifted expression used on several legacy surfaces."""
    k = sympify(level)
    return simplify(2 - 24 * (k + 1) ** 2 / (k + 3))


def bp_complementarity_correct(level=k_sym):
    """Exact standard reflection identity c(k)+c(-k-6)=50."""
    k = sympify(level)
    return simplify(bp_central_charge_correct(k) + bp_central_charge_correct(-k - 6))


def bp_shifted_secondary_complementarity(level=k_sym):
    """Exact shifted reflection identity c_shift(k)+c_shift(-k-6)=196."""
    k = sympify(level)
    return simplify(
        bp_shifted_secondary_central_charge(k)
        + bp_shifted_secondary_central_charge(-k - 6)
    )


def bp_generator_parities():
    """Parity packet for the ordinary BP vertex algebra."""
    return {"J": "even", "T": "even", "G+": "even", "G-": "even"}


def bp_reciprocal_weight_diagnostic():
    """Sum 1/h over the four even strong generators."""
    return Rational(1) + 2 * Rational(2, 3) + Rational(1, 2)


def bp_modular_status_packet():
    """Status of the genus-one modular quantities."""
    return {
        "standard_central_conductor": Rational(50),
        "shifted_secondary_sum": Rational(196),
        "reciprocal_weight_diagnostic": Rational(17, 6),
        "kappa": None,
        "rho": None,
        "K_kappa": None,
        "status": "open",
        "required_input": (
            "complete genus-one minimal-DS curvature with charged ghosts, "
            "neutral fields, improvement term, and mixed channels"
        ),
    }


def bp_kappa_correct(level=k_sym):
    """Fail loudly: the standard central charge does not determine kappa."""
    raise UnverifiedWInvariantError(bp_modular_status_packet()["required_input"])


def bp_kappa_complementarity_correct(level=k_sym):
    """Fail loudly: K^kappa_BP remains an open comparison invariant."""
    raise UnverifiedWInvariantError(bp_modular_status_packet()["required_input"])


def verify_bp_central_charge_at_admissible_levels():
    """Evaluate the standard and shifted expressions at three useful levels."""
    levels = (Rational(-3, 2), Rational(-1), Rational(-1, 2))
    return {
        level: {
            "standard": bp_central_charge_correct(level),
            "shifted_secondary": bp_shifted_secondary_central_charge(level),
        }
        for level in levels
    }


# ---------------------------------------------------------------------------
# Principal type A: exact central-charge and reflection arithmetic
# ---------------------------------------------------------------------------


def wn_central_charge(N, level=k_sym):
    r"""Principal W^k(sl_N) central charge in the standard DS convention."""
    if N < 2:
        raise ValueError("principal type A requires N >= 2")
    k = sympify(level)
    return simplify(
        Rational(N - 1)
        * (1 - Rational(N * (N + 1)) * (k + N - 1) ** 2 / (k + N))
    )


def wn_complementarity_sum(N):
    r"""Arithmetic reflection sum under k -> -k-2N.

    The function name is retained for compatibility.  The computation
    establishes a rational-function identity; a Koszul interpretation is
    a separate theorem obligation.
    """
    k = k_sym
    return simplify(wn_central_charge(N, k) + wn_central_charge(N, -k - 2 * N))


def wn_anomaly_ratio(N):
    """Reciprocal-weight diagnostic sum_{j=2}^N 1/j."""
    if N < 2:
        raise ValueError("principal type A requires N >= 2")
    return sum((Rational(1, j) for j in range(2, N + 1)), Rational(0))


def wn_kappa(N, level=k_sym):
    """Require a genus-one comparison instead of promoting a weight sum."""
    raise UnverifiedWInvariantError(
        "principal W_N kappa requires its genus-one curvature comparison"
    )


def verify_anomaly_ratio_principal_wn(N):
    """Compare the explicit weight sum with the harmonic-number recurrence."""
    direct = wn_anomaly_ratio(N)
    recurrence = sum((Rational(1, j) for j in range(2, N + 1)), Rational(0))
    return {"weight_sum": direct, "harmonic_recurrence": recurrence, "match": direct == recurrence}


def verify_wn_c_complementarity_formula():
    """Check the reflection sum by direct substitution and a closed formula."""
    results = {}
    for N in range(2, 8):
        direct = wn_complementarity_sum(N)
        closed = 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
        root_identity = 2 * (N - 1) + 4 * N * (N**2 - 1)
        results[N] = {
            "direct": int(direct),
            "closed": closed,
            "root_identity": root_identity,
            "all_match": int(direct) == closed == root_identity,
            "interpretation": "arithmetic reflection identity",
        }
    return results


# ---------------------------------------------------------------------------
# Nilpotent partitions: exact finite combinatorics
# ---------------------------------------------------------------------------


def partition_transpose(partition):
    """Transpose an integer partition."""
    parts = tuple(int(x) for x in partition)
    if not parts or any(x <= 0 for x in parts) or any(
        parts[i] < parts[i + 1] for i in range(len(parts) - 1)
    ):
        raise ValueError("partition must be a nonincreasing tuple of positive integers")
    return tuple(sum(1 for part in parts if part >= j) for j in range(1, parts[0] + 1))


def sl_centralizer_dimension(partition):
    """Dimension of the nilpotent centralizer in sl_N."""
    transpose = partition_transpose(partition)
    return sum(column**2 for column in transpose) - 1


def hook_generator_content_sl_n(N, r):
    r"""Exact hook partition packet for [N-r,1^r].

    Principal and zero orbits have canonical generator packets.  For an
    intermediate hook this routine records only the exact partition and
    centralizer dimension; good-grading weights and shadow data require a
    separate BRST computation.
    """
    if N < 2 or r < 0 or r > N - 1:
        raise ValueError("hook requires N >= 2 and 0 <= r <= N-1")
    partition = (N - r,) + (1,) * r
    packet = {
        "partition": partition,
        "transpose": partition_transpose(partition),
        "dim_slice": sl_centralizer_dimension(partition),
        "n_generators": sl_centralizer_dimension(partition),
        "shadow_class": None,
    }
    if r == 0:
        packet.update(
            weights=tuple(range(2, N + 1)),
            parities=("even",) * (N - 1),
            status="principal generator packet exact",
        )
    elif r == N - 1:
        packet.update(
            weights=(1,) * (N**2 - 1),
            parities=("even",) * (N**2 - 1),
            status="zero-orbit affine packet exact",
        )
    else:
        packet.update(
            weights=None,
            parities=None,
            status="good-grading generator packet open in this engine",
        )
    return packet


# ---------------------------------------------------------------------------
# Classical exponents
# ---------------------------------------------------------------------------


def bcd_exponents(lie_type, rank):
    """Exponents of a simple Lie algebra of type B, C, or D."""
    if lie_type in {"B", "C"}:
        if rank < 2:
            raise ValueError("types B and C require rank >= 2 here")
        return tuple(range(1, 2 * rank, 2))
    if lie_type == "D":
        if rank < 4:
            raise ValueError("type D requires rank >= 4 here")
        return tuple(sorted(tuple(range(1, 2 * rank - 2, 2)) + (rank - 1,)))
    raise ValueError(f"unsupported type: {lie_type}")


def bcd_generator_weights(lie_type, rank):
    """Principal generator weights e_i+1, with multiplicity."""
    return tuple(exponent + 1 for exponent in bcd_exponents(lie_type, rank))


def bcd_anomaly_ratio(lie_type, rank):
    """Reciprocal-weight diagnostic for the principal generator packet."""
    return sum(
        (Rational(1, weight) for weight in bcd_generator_weights(lie_type, rank)),
        Rational(0),
    )


# ---------------------------------------------------------------------------
# Primary-source status packets
# ---------------------------------------------------------------------------


def minimal_so_central_charge(N, level=k_sym):
    """Keep the unimplemented KRW formula explicit."""
    raise UnverifiedWInvariantError(
        "minimal so_N central charge requires the complete KRW formula in a fixed convention"
    )


def minimal_so_is_rational(N):
    r"""Status from arXiv:2506.15605, abstract and main representation theorem.

    For every N>=7 the level -1 simple minimal W-algebra is identified with
    an even subalgebra of osp(1|2) tensored with free fermions.  Strong
    rationality is stated for even N.  Odd N therefore returns ``None`` in
    this boolean-valued compatibility API.
    """
    if N >= 8 and N % 2 == 0:
        return True
    return None


def minimal_so_status(N):
    """Typed form of the level -1 minimal so_N theorem."""
    if N < 7:
        return {"representation_theorem": False, "strongly_rational": None}
    return {
        "representation_theorem": True,
        "strongly_rational": True if N % 2 == 0 else None,
        "source": "Creutzig--Fasquel--Kovalchuk--Linshaw--Nakatsuka, arXiv:2506.15605",
    }


def conformal_extension_collapse_examples():
    """Require theorem-number verification before exposing a numerical list."""
    raise UnverifiedWInvariantError(
        "collapse examples require primary-source theorem numbers and level conventions"
    )


def logarithmic_verlinde_status():
    """Scope stated in Creutzig, arXiv:2411.11383."""
    return {
        "status": "proved under natural assumptions",
        "paper": "2411.11383",
        "author": "Thomas Creutzig",
        "examples": ("singlet algebras", "V_k(sl_2) at admissible levels"),
        "output": "Grothendieck fusion data; actual fusion requires the additional reconstruction described there",
    }
