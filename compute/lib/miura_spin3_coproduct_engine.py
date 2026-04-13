r"""Miura coproduct at spin 3 for W_{1+infinity}[Psi].

MATHEMATICAL CONTENT
====================

This module derives the spectral coproduct Delta_z(W) for the spin-3
generator W of W_{1+infinity}[Psi], extending the spin-2 result
Delta_z(T) = T.1 + 1.T + ((Psi-1)/Psi) J.J + z(1.J) from
w_infinity_ope_compat_spin2.py.

MIURA TRANSFORM
===============

The Miura transform for W_{1+infinity}[Psi] on a single free boson
J(z)J(w) ~ Psi/(z-w)^2 gives the relation between the eigenvalue
generators psi_n and the W-algebra field generators {J, T, W, ...}:

    psi_1 = J
    psi_2 = T + :J^2:/(2*Psi)
    psi_3 = W + (1/Psi)*:J*T: + (1/(6*Psi^2))*:J^3: + (1/(2*Psi))*J''

where :AB: denotes normal-ordered product and J'' = partial^2 J.

The INVERSION is:
    J = psi_1
    T = psi_2 - psi_1^2/(2*Psi)
    W = psi_3 - (1/Psi)*psi_1*psi_2 + psi_1^3/(3*Psi^2) - psi_1''/(2*Psi)

DRINFELD COPRODUCT
==================

The Drinfeld coproduct Delta_z(T(u)) = T(u).T(u-z) gives at spin 3:

    Delta_z(psi_3) = psi_3.1 + 1.psi_3 + psi_1.psi_2 + psi_2.psi_1
                   + z*(psi_1.psi_1 + 2*1.psi_2) + z^2*(1.psi_1)

MAIN RESULT
===========

Inverting the Miura transform, the coproduct on the spin-3 primary W is:

    Delta_z(W) = W.1 + 1.W
               + ((Psi-1)/Psi) * (J.T + T.J)
               + ((1-Psi)/(2*Psi^2)) * (J.:J^2: + :J^2:.J)
               + ((Psi-1)/Psi) * z * J.J
               + 2*z * 1.T
               + z^2 * 1.J

COEFFICIENTS IN THE W-FIELD BASIS:
    c_{J,T}     = (Psi-1)/Psi           [spin-1 x spin-2 primary cross-term]
    c_{T,J}     = (Psi-1)/Psi           [spin-2 x spin-1 primary cross-term]
    c_{J,:J^2:} = (1-Psi)/(2*Psi^2)     [spin-1 x composite cross-term]
    c_{:J^2:,J} = (1-Psi)/(2*Psi^2)     [composite x spin-1 cross-term]
    c_{J,J}^z   = (Psi-1)/Psi           [spectral: spin-1 x spin-1]
    c_{1,T}^z   = 2                      [spectral: identity x spin-2]
    c_{1,J}^{z^2} = 1                   [spectral: identity x spin-1]

VERIFICATION:
    Psi = 1 (free boson):     all (Psi-1)/Psi terms vanish, giving
        Delta_z(W) = W.1 + 1.W + 2z*1.T + z^2*1.J
    Psi -> inf (classical):   (Psi-1)/Psi -> 1, (1-Psi)/(2Psi^2) -> 0, giving
        Delta_z(W) = W.1 + 1.W + J.T + T.J + z*J.J + 2z*1.T + z^2*1.J
    z = 0:                    standard (non-spectral) coproduct:
        Delta_0(W) = W.1 + 1.W + ((Psi-1)/Psi)(J.T + T.J)
                   + ((1-Psi)/(2Psi^2))(J.:J^2: + :J^2:.J)
    Consistency:              the composite of all Miura + coproduct terms
                              reproduces Delta_z(psi_3) exactly.

ALTERNATIVE FORM (psi-basis substitution):
Using :J^2: = 2*Psi*(psi_2 - T), the J.T and J.:J^2: terms combine:
    (Psi-1)/Psi * J.T + (1-Psi)/(2*Psi^2) * J.:J^2:
    = (Psi-1)/Psi * J.T + (1-Psi)/Psi * J.(psi_2 - T)
    = (Psi-1)/Psi * J.T - (Psi-1)/Psi * J.psi_2 + (Psi-1)/Psi * J.T
    = (Psi-1)/Psi * (2*J.T - J.psi_2)

References:
    standalone/ordered_chiral_homology.tex, Theorem 3.24 (spin-2 case).
    Prochazka-Rapcak, arXiv:1711.11582 (Miura transform for W_{1+inf}).
    Tsymbaliuk, arXiv:1404.5240 (affine Yangian coproduct).
    w_infinity_ope_compat_spin2.py (spin-2 predecessor in this programme).
"""

from __future__ import annotations

from typing import Any, Dict, Tuple

from sympy import (
    Rational,
    Symbol,
    binomial,
    expand,
    factor,
    limit,
    oo,
    simplify,
    symbols,
)


# ============================================================================
# Symbolic setup
# ============================================================================

Psi_sym, z_sym = symbols('Psi z', commutative=True)


# ============================================================================
# 1. Drinfeld coproduct in the psi-basis
# ============================================================================

def delta_psi(n: int, z: Any = None) -> Dict[Tuple[int, int], Any]:
    r"""Compute Delta_z(psi_n) from the Drinfeld formula.

    Delta_z(psi_n) = psi_n . 1 + sum_{k=0}^{n-1} sum_{m=1}^{n-k}
                     binom(n-k-1, m-1) z^{n-k-m} psi_k . psi_m

    Returns {(left_index, right_index): coefficient}.
    """
    if z is None:
        z = z_sym
    result: Dict[Tuple[int, int], Any] = {}

    # Leading term: psi_n . 1
    result[(n, 0)] = Rational(1)

    for k in range(n):
        for m in range(1, n - k + 1):
            coeff = expand(binomial(n - k - 1, m - 1) * z**(n - k - m))
            if coeff != 0:
                key = (k, m)
                if key in result:
                    result[key] = expand(result[key] + coeff)
                else:
                    result[key] = coeff

    return {k: v for k, v in result.items() if v != 0}


# ============================================================================
# 2. Miura transform: psi_n <-> W-field basis
# ============================================================================

# The Miura relations for W_{1+inf}[Psi]:
#   psi_1 = J
#   psi_2 = T + :J^2:/(2*Psi)
#   psi_3 = W + (1/Psi)*:JT: + (1/(6*Psi^2))*:J^3: + (1/(2*Psi))*J''
#
# Inversion:
#   J = psi_1
#   T = psi_2 - :J^2:/(2*Psi)
#   W = psi_3 - (1/Psi)*:JT: - (1/(6*Psi^2))*:J^3: - (1/(2*Psi))*J''


def miura_psi2_to_W(Psi: Any = None) -> Dict[str, Any]:
    r"""Express psi_2 in the W-field basis.

    psi_2 = T + :J^2:/(2*Psi)

    Returns {field_label: coefficient}.
    """
    if Psi is None:
        Psi = Psi_sym
    return {
        "T": Rational(1),
        ":J^2:": 1 / (2 * Psi),
    }


def miura_psi3_to_W(Psi: Any = None) -> Dict[str, Any]:
    r"""Express psi_3 in the W-field basis.

    psi_3 = W + (1/Psi)*:JT: + (1/(6*Psi^2))*:J^3: + (1/(2*Psi))*J''

    Returns {field_label: coefficient}.
    """
    if Psi is None:
        Psi = Psi_sym
    return {
        "W": Rational(1),
        ":JT:": 1 / Psi,
        ":J^3:": 1 / (6 * Psi**2),
        "J''": 1 / (2 * Psi),
    }


def miura_W_from_psi(Psi: Any = None) -> Dict[str, Any]:
    r"""Express W in terms of psi-generators (inversion of Miura).

    W = psi_3 - (1/Psi)*:psi_1*psi_2: + psi_1^3/(3*Psi^2) - psi_1''/(2*Psi)

    Note: :psi_1*psi_2: = :J*(T + :J^2:/(2Psi)): = :JT: + :J^3:/(2Psi).
    So: W = psi_3 - (1/Psi)*(:JT: + :J^3:/(2Psi)) + :J^3:/(3Psi^2) - J''/(2Psi)
          = psi_3 - :JT:/Psi - :J^3:/(2Psi^2) + :J^3:/(3Psi^2) - J''/(2Psi)
          = psi_3 - :JT:/Psi - :J^3:/(6Psi^2) - J''/(2Psi)
    Consistent with Miura relation.

    Returns {generator_label: coefficient}.
    """
    if Psi is None:
        Psi = Psi_sym
    return {
        "psi_3": Rational(1),
        ":JT:": -1 / Psi,
        ":J^3:": -1 / (6 * Psi**2),
        "J''": -1 / (2 * Psi),
    }


# ============================================================================
# 3. Coproduct of composite fields
# ============================================================================

def delta_JT(Psi: Any = None, z: Any = None) -> Dict[Tuple[str, str], Any]:
    r"""Compute Delta_z(:JT:) from the vertex bialgebra property.

    Delta_z(:JT:) = :Delta_z(J) * Delta_z(T):

    where Delta_z(J) = J.1 + 1.J and
          Delta_z(T) = T.1 + 1.T + c*J.J + z*1.J with c = (Psi-1)/Psi.

    The product in the tensor vertex algebra is taken componentwise with
    normal ordering in each factor.
    """
    if Psi is None:
        Psi = Psi_sym
    if z is None:
        z = z_sym

    c = (Psi - 1) / Psi

    # Delta_z(J) = (J, 1) + (1, J)
    # Delta_z(T) = (T, 1) + (1, T) + c*(J, J) + z*(1, J)
    #
    # Product (left component * left component, right * right, normal ordered):
    result: Dict[Tuple[str, str], Any] = {}

    terms = [
        # (J,1) * (T,1) = (:JT:, 1)
        (":JT:", "1", Rational(1)),
        # (J,1) * (1,T) = (J, T)
        ("J", "T", Rational(1)),
        # (J,1) * (c*J, J) = (c*:J^2:, J)
        (":J^2:", "J", c),
        # (J,1) * (z*1, J) = (z*J, J)
        ("J", "J", z),
        # (1,J) * (T,1) = (T, J)
        ("T", "J", Rational(1)),
        # (1,J) * (1,T) = (1, :JT:)
        ("1", ":JT:", Rational(1)),
        # (1,J) * (c*J, J) = (c*J, :J^2:)
        ("J", ":J^2:", c),
        # (1,J) * (z*1, J) = (z, :J^2:)
        ("1", ":J^2:", z),
    ]

    for left, right, coeff in terms:
        key = (left, right)
        if key in result:
            result[key] = expand(result[key] + coeff)
        else:
            result[key] = expand(coeff)

    return {k: v for k, v in result.items() if v != 0}


def delta_J3(z: Any = None) -> Dict[Tuple[str, str], Any]:
    r"""Compute Delta_z(:J^3:) from the vertex bialgebra property.

    Delta_z(:J^3:) = :(J.1 + 1.J)^3: = :J^3:.1 + 3:J^2:.J + 3J.:J^2: + 1.:J^3:

    (The spectral parameter z does not appear because J is primitive:
    Delta_z(J) = J.1 + 1.J is z-independent.)
    """
    return {
        (":J^3:", "1"): Rational(1),
        (":J^2:", "J"): Rational(3),
        ("J", ":J^2:"): Rational(3),
        ("1", ":J^3:"): Rational(1),
    }


def delta_Jpp(z: Any = None) -> Dict[Tuple[str, str], Any]:
    r"""Compute Delta_z(J'') = partial^2 Delta_z(J) = J''.1 + 1.J''.

    The second derivative commutes with the coproduct; J is primitive.
    """
    return {
        ("J''", "1"): Rational(1),
        ("1", "J''"): Rational(1),
    }


# ============================================================================
# 4. Main result: Delta_z(W)
# ============================================================================

def delta_W(Psi: Any = None, z: Any = None) -> Dict[Tuple[str, str], Any]:
    r"""Compute Delta_z(W) by inverting the Miura transform.

    Delta_z(W) = Delta_z(psi_3)
               - (1/Psi)*Delta_z(:JT:)
               - (1/(6*Psi^2))*Delta_z(:J^3:)
               - (1/(2*Psi))*Delta_z(J'')

    where each term on the right is already computed in the W-field basis.

    Returns {(left_label, right_label): coefficient_as_function_of_Psi_and_z}.
    """
    if Psi is None:
        Psi = Psi_sym
    if z is None:
        z = z_sym

    result: Dict[Tuple[str, str], Any] = {}

    def _add(key: Tuple[str, str], val: Any) -> None:
        if key in result:
            result[key] = expand(result[key] + val)
        else:
            result[key] = expand(val)

    # -------------------------------------------------------------------
    # Term 1: Delta_z(psi_3) in the W-field basis
    # -------------------------------------------------------------------
    # Delta_z(psi_3) = psi_3.1 + 1.psi_3 + psi_1.psi_2 + psi_2.psi_1
    #                + z*(psi_1.psi_1 + 2*1.psi_2) + z^2*(1.psi_1)
    #
    # Substituting psi_1 = J, psi_2 = T + :J^2:/(2Psi),
    # psi_3 = W + :JT:/Psi + :J^3:/(6Psi^2) + J''/(2Psi):

    # psi_3 . 1
    _add(("W", "1"), Rational(1))
    _add((":JT:", "1"), 1 / Psi)
    _add((":J^3:", "1"), 1 / (6 * Psi**2))
    _add(("J''", "1"), 1 / (2 * Psi))

    # 1 . psi_3
    _add(("1", "W"), Rational(1))
    _add(("1", ":JT:"), 1 / Psi)
    _add(("1", ":J^3:"), 1 / (6 * Psi**2))
    _add(("1", "J''"), 1 / (2 * Psi))

    # psi_1 . psi_2 = J . (T + :J^2:/(2Psi))
    _add(("J", "T"), Rational(1))
    _add(("J", ":J^2:"), 1 / (2 * Psi))

    # psi_2 . psi_1 = (T + :J^2:/(2Psi)) . J
    _add(("T", "J"), Rational(1))
    _add((":J^2:", "J"), 1 / (2 * Psi))

    # z * psi_1 . psi_1 = z * J . J
    _add(("J", "J"), z)

    # 2z * 1 . psi_2 = 2z * (1.T + 1.:J^2:/(2Psi))
    _add(("1", "T"), 2 * z)
    _add(("1", ":J^2:"), z / Psi)

    # z^2 * 1 . psi_1 = z^2 * 1 . J
    _add(("1", "J"), z**2)

    # -------------------------------------------------------------------
    # Term 2: -(1/Psi) * Delta_z(:JT:)
    # -------------------------------------------------------------------
    djt = delta_JT(Psi, z)
    for key, val in djt.items():
        _add(key, expand(-val / Psi))

    # -------------------------------------------------------------------
    # Term 3: -(1/(6*Psi^2)) * Delta_z(:J^3:)
    # -------------------------------------------------------------------
    dj3 = delta_J3(z)
    for key, val in dj3.items():
        _add(key, expand(-val / (6 * Psi**2)))

    # -------------------------------------------------------------------
    # Term 4: -(1/(2*Psi)) * Delta_z(J'')
    # -------------------------------------------------------------------
    djpp = delta_Jpp(z)
    for key, val in djpp.items():
        _add(key, expand(-val / (2 * Psi)))

    # Clean up: remove zero terms, simplify
    return {k: simplify(v) for k, v in result.items() if simplify(v) != 0}


def delta_W_explicit(Psi: Any = None, z: Any = None) -> Dict[Tuple[str, str], Any]:
    r"""The analytically derived formula for Delta_z(W).

    This is the CLOSED-FORM result, not computed from components:

        Delta_z(W) = W.1 + 1.W
                   + ((Psi-1)/Psi) * (J.T + T.J)
                   + ((1-Psi)/(2*Psi^2)) * (J.:J^2: + :J^2:.J)
                   + ((Psi-1)/Psi) * z * J.J
                   + 2*z * 1.T
                   + z^2 * 1.J
    """
    if Psi is None:
        Psi = Psi_sym
    if z is None:
        z = z_sym

    c1 = (Psi - 1) / Psi
    c2 = (1 - Psi) / (2 * Psi**2)

    return {
        ("W", "1"): Rational(1),
        ("1", "W"): Rational(1),
        ("J", "T"): c1,
        ("T", "J"): c1,
        ("J", ":J^2:"): c2,
        (":J^2:", "J"): c2,
        ("J", "J"): c1 * z,
        ("1", "T"): 2 * z,
        ("1", "J"): z**2,
    }


# ============================================================================
# 5. Coefficient extraction
# ============================================================================

def coefficient_JT(Psi: Any = None) -> Any:
    """Return the coefficient of J tensor T in Delta_z(W)."""
    if Psi is None:
        Psi = Psi_sym
    return (Psi - 1) / Psi


def coefficient_TJ(Psi: Any = None) -> Any:
    """Return the coefficient of T tensor J in Delta_z(W)."""
    if Psi is None:
        Psi = Psi_sym
    return (Psi - 1) / Psi


def coefficient_J_Jsq(Psi: Any = None) -> Any:
    """Return the coefficient of J tensor :J^2: in Delta_z(W)."""
    if Psi is None:
        Psi = Psi_sym
    return (1 - Psi) / (2 * Psi**2)


def coefficient_Jsq_J(Psi: Any = None) -> Any:
    """Return the coefficient of :J^2: tensor J in Delta_z(W)."""
    if Psi is None:
        Psi = Psi_sym
    return (1 - Psi) / (2 * Psi**2)


def coefficient_JJ_z(Psi: Any = None) -> Any:
    """Return the coefficient of z * J tensor J in Delta_z(W)."""
    if Psi is None:
        Psi = Psi_sym
    return (Psi - 1) / Psi


def coefficient_1T_z() -> Any:
    """Return the coefficient of z * 1 tensor T in Delta_z(W)."""
    return Rational(2)


def coefficient_1J_z2() -> Any:
    """Return the coefficient of z^2 * 1 tensor J in Delta_z(W)."""
    return Rational(1)


# ============================================================================
# 6. Consistency verification: reconstruct Delta_z(psi_3)
# ============================================================================

def verify_psi3_reconstruction(Psi: Any = None, z: Any = None) -> Dict[str, Any]:
    r"""Verify that Delta_z(W) + corrections = Delta_z(psi_3).

    The Miura relation psi_3 = W + (1/Psi):JT: + (1/(6Psi^2)):J^3: + (1/(2Psi))J''
    implies:
        Delta_z(psi_3) = Delta_z(W) + (1/Psi)*Delta_z(:JT:)
                       + (1/(6Psi^2))*Delta_z(:J^3:) + (1/(2Psi))*Delta_z(J'')

    We verify this identity holds.
    """
    if Psi is None:
        Psi = Psi_sym
    if z is None:
        z = z_sym

    # LHS: Delta_z(psi_3) in psi-basis
    dpsi3 = delta_psi(3, z)

    # RHS: assemble from components
    dW = delta_W(Psi, z)
    djt = delta_JT(Psi, z)
    dj3 = delta_J3(z)
    djpp = delta_Jpp(z)

    # Convert LHS to W-field basis
    # psi_1 = J, psi_2 = T + :J^2:/(2Psi), psi_3 = W + ...
    psi_to_W: Dict[Tuple[str, str], Any] = {}

    def _add_psi(key: Tuple[str, str], val: Any) -> None:
        if key in psi_to_W:
            psi_to_W[key] = expand(psi_to_W[key] + val)
        else:
            psi_to_W[key] = expand(val)

    # Map each (left_psi_index, right_psi_index) to W-field basis
    psi2_fields = {"T": Rational(1), ":J^2:": 1 / (2 * Psi)}
    psi3_fields = {
        "W": Rational(1), ":JT:": 1 / Psi,
        ":J^3:": 1 / (6 * Psi**2), "J''": 1 / (2 * Psi),
    }

    for (l, r), coeff in dpsi3.items():
        # Map index to field labels
        left_fields = {0: {"1": Rational(1)}, 1: {"J": Rational(1)},
                       2: psi2_fields, 3: psi3_fields}
        right_fields = {0: {"1": Rational(1)}, 1: {"J": Rational(1)},
                        2: psi2_fields, 3: psi3_fields}

        for lf, lc in left_fields.get(l, {}).items():
            for rf, rc in right_fields.get(r, {}).items():
                _add_psi((lf, rf), expand(coeff * lc * rc))

    # RHS: Delta_z(W) + corrections
    rhs: Dict[Tuple[str, str], Any] = {}

    def _add_rhs(key: Tuple[str, str], val: Any) -> None:
        if key in rhs:
            rhs[key] = expand(rhs[key] + val)
        else:
            rhs[key] = expand(val)

    for key, val in dW.items():
        _add_rhs(key, val)
    for key, val in djt.items():
        _add_rhs(key, expand(val / Psi))
    for key, val in dj3.items():
        _add_rhs(key, expand(val / (6 * Psi**2)))
    for key, val in djpp.items():
        _add_rhs(key, expand(val / (2 * Psi)))

    # Compare
    all_keys = set(psi_to_W.keys()) | set(rhs.keys())
    mismatches = {}
    for key in all_keys:
        lhs_val = simplify(psi_to_W.get(key, 0))
        rhs_val = simplify(rhs.get(key, 0))
        diff = simplify(lhs_val - rhs_val)
        if diff != 0:
            mismatches[key] = {
                "lhs": lhs_val, "rhs": rhs_val, "diff": diff
            }

    return {
        "all_match": len(mismatches) == 0,
        "num_terms_lhs": len({k: v for k, v in psi_to_W.items() if simplify(v) != 0}),
        "num_terms_rhs": len({k: v for k, v in rhs.items() if simplify(v) != 0}),
        "mismatches": mismatches,
    }


# ============================================================================
# 7. Limiting cases
# ============================================================================

def delta_W_at_Psi(psi_val: Any, z: Any = None) -> Dict[Tuple[str, str], Any]:
    """Evaluate Delta_z(W) at a specific value of Psi."""
    if z is None:
        z = z_sym
    dw = delta_W_explicit(Psi_sym, z)
    return {k: simplify(v.subs(Psi_sym, psi_val))
            for k, v in dw.items()
            if simplify(v.subs(Psi_sym, psi_val)) != 0}


def delta_W_free_boson(z: Any = None) -> Dict[Tuple[str, str], Any]:
    """Delta_z(W) at Psi = 1 (free boson limit).

    At Psi = 1, all (Psi-1)/Psi cross-terms vanish:
        Delta_z(W) = W.1 + 1.W + 2z*1.T + z^2*1.J
    """
    return delta_W_at_Psi(Rational(1), z)


def delta_W_classical_limit(z: Any = None) -> Dict[Tuple[str, str], Any]:
    """Delta_z(W) in the classical limit Psi -> infinity.

    (Psi-1)/Psi -> 1, (1-Psi)/(2*Psi^2) -> 0:
        Delta_z(W) = W.1 + 1.W + J.T + T.J + z*J.J + 2z*1.T + z^2*1.J
    """
    if z is None:
        z = z_sym
    return {
        ("W", "1"): Rational(1),
        ("1", "W"): Rational(1),
        ("J", "T"): Rational(1),
        ("T", "J"): Rational(1),
        ("J", "J"): z,
        ("1", "T"): 2 * z,
        ("1", "J"): z**2,
    }


def verify_classical_limit(z: Any = None) -> bool:
    """Verify that lim_{Psi->inf} Delta_z(W) = classical formula."""
    if z is None:
        z = z_sym
    dw = delta_W_explicit(Psi_sym, z)
    classical = delta_W_classical_limit(z)

    all_keys = set(dw.keys()) | set(classical.keys())
    for key in all_keys:
        val = dw.get(key, 0)
        expected = classical.get(key, 0)
        lim_val = limit(val, Psi_sym, oo)
        if simplify(lim_val - expected) != 0:
            return False
    return True


# ============================================================================
# 8. Coassociativity partial check
# ============================================================================

def verify_counit_W(Psi: Any = None, z: Any = None) -> Dict[str, Any]:
    r"""Verify (eps . id)(Delta_z(W)) gives the correct result.

    The counit eps sends all generators to 0: eps(J) = eps(T) = eps(W) = 0,
    eps(:J^2:) = eps(:J^3:) = eps(:JT:) = eps(J'') = 0, eps(1) = 1.

    (eps . id)(Delta_z(W)) should give W + 2z*T + z^2*J.

    This is the W-projection of the counit applied to psi_3:
    (eps . id)(Delta_z(psi_3)) = psi_3 + 2z*psi_2 + z^2*psi_1
    and the W-part is W + 2z*T + z^2*J (the composite terms come from
    the Miura corrections to psi_3, psi_2, not from Delta_z(W)).
    """
    if Psi is None:
        Psi = Psi_sym
    if z is None:
        z = z_sym

    dw = delta_W_explicit(Psi, z)

    # Apply eps to left factor: only terms with left = "1" survive
    counit_result: Dict[str, Any] = {}
    for (left, right), coeff in dw.items():
        if left == "1":
            if right in counit_result:
                counit_result[right] = expand(counit_result[right] + coeff)
            else:
                counit_result[right] = expand(coeff)

    # Expected: (eps . id)(Delta_z(W)) = W + 2z*T + z^2*J
    # These are the terms where only the independent W-field generators
    # appear on the right, coming from the primitive and spectral parts.
    expected = {
        "W": Rational(1),
        "T": 2 * z,
        "J": z**2,
    }

    all_keys = set(counit_result.keys()) | set(expected.keys())
    mismatches = {}
    for key in all_keys:
        cr = simplify(counit_result.get(key, 0))
        ex = simplify(expected.get(key, 0))
        if simplify(cr - ex) != 0:
            mismatches[key] = {"computed": cr, "expected": ex}

    return {
        "all_match": len(mismatches) == 0,
        "counit_result": counit_result,
        "expected": expected,
        "mismatches": mismatches,
    }


def verify_counit_psi3(Psi: Any = None, z: Any = None) -> Dict[str, Any]:
    r"""Verify (eps . id)(Delta_z(psi_3)) in the W-field basis.

    (eps . id)(Delta_z(psi_3)) = psi_3 + 2z*psi_2 + z^2*psi_1
    In W-field basis:
    = W + :JT:/Psi + :J^3:/(6Psi^2) + J''/(2Psi) + 2z*(T + :J^2:/(2Psi)) + z^2*J

    This is the FULL counit, including Miura composite contributions from
    all three terms Delta_z(W), (1/Psi)*Delta_z(:JT:), etc.
    """
    if Psi is None:
        Psi = Psi_sym
    if z is None:
        z = z_sym

    # Assemble Delta_z(psi_3) = Delta_z(W) + corrections
    dW = delta_W_explicit(Psi, z)
    djt = delta_JT(Psi, z)
    dj3 = delta_J3(z)
    djpp = delta_Jpp(z)

    full: Dict[Tuple[str, str], Any] = {}

    def _add(key: Tuple[str, str], val: Any) -> None:
        if key in full:
            full[key] = expand(full[key] + val)
        else:
            full[key] = expand(val)

    for k, v in dW.items():
        _add(k, v)
    for k, v in djt.items():
        _add(k, expand(v / Psi))
    for k, v in dj3.items():
        _add(k, expand(v / (6 * Psi**2)))
    for k, v in djpp.items():
        _add(k, expand(v / (2 * Psi)))

    # Apply eps to left factor
    counit_result: Dict[str, Any] = {}
    for (left, right), coeff in full.items():
        if left == "1":
            if right in counit_result:
                counit_result[right] = expand(counit_result[right] + coeff)
            else:
                counit_result[right] = expand(coeff)

    # Expected:
    expected = {
        "W": Rational(1),
        ":JT:": 1 / Psi,
        ":J^3:": 1 / (6 * Psi**2),
        "J''": 1 / (2 * Psi),
        "T": 2 * z,
        ":J^2:": z / Psi,
        "J": z**2,
    }

    all_keys = set(counit_result.keys()) | set(expected.keys())
    mismatches = {}
    for key in all_keys:
        cr = simplify(counit_result.get(key, 0))
        ex = simplify(expected.get(key, 0))
        if simplify(cr - ex) != 0:
            mismatches[key] = {"computed": cr, "expected": ex}

    return {
        "all_match": len(mismatches) == 0,
        "counit_result": {k: str(v) for k, v in counit_result.items()},
        "expected": {k: str(v) for k, v in expected.items()},
        "mismatches": mismatches,
    }


# ============================================================================
# 9. Comparison with spin-2 result
# ============================================================================

def compare_with_spin2() -> Dict[str, Any]:
    r"""Compare structural features of Delta_z(T) and Delta_z(W).

    Spin 2: Delta_z(T) = T.1 + 1.T + ((Psi-1)/Psi)*J.J + z*1.J

    Spin 3: Delta_z(W) = W.1 + 1.W
                       + ((Psi-1)/Psi)*(J.T + T.J)
                       + ((1-Psi)/(2Psi^2))*(J.:J^2: + :J^2:.J)
                       + ((Psi-1)/Psi)*z*J.J + 2z*1.T + z^2*1.J

    Key structural observations:
    1. The spin-2 cross-term coefficient (Psi-1)/Psi appears at spin 3
       for BOTH the J.T/T.J terms AND the z*J.J spectral term.
    2. A NEW coefficient (1-Psi)/(2Psi^2) appears for the composite
       :J^2: cross-terms (this is -(Psi-1)/(2Psi^2)).
    3. The spectral z-polynomial has degree 2 (vs degree 1 at spin 2).
    4. The 1.T term has coefficient 2z (not z), matching binom(2,1) = 2.
    """
    return {
        "spin_2": {
            "cross_terms": {"J.J": "(Psi-1)/Psi"},
            "spectral_terms": {"1.J": "z"},
            "z_degree": 1,
        },
        "spin_3": {
            "cross_terms": {
                "J.T": "(Psi-1)/Psi",
                "T.J": "(Psi-1)/Psi",
                "J.:J^2:": "(1-Psi)/(2*Psi^2)",
                ":J^2:.J": "(1-Psi)/(2*Psi^2)",
            },
            "spectral_terms": {
                "J.J": "(Psi-1)/Psi * z",
                "1.T": "2*z",
                "1.J": "z^2",
            },
            "z_degree": 2,
        },
        "pattern": (
            "At spin s, the cross-terms involve fields of total weight s "
            "split as (a, s-a) for 1 <= a <= s-1. The spectral polynomial "
            "in z has degree s-1. The coefficient (Psi-1)/Psi appears "
            "universally on the primary cross-terms; composite corrections "
            "carry higher powers of 1/Psi."
        ),
    }


# ============================================================================
# 10. Master verification
# ============================================================================

def run_all() -> Dict[str, Any]:
    """Run the complete verification suite."""
    return {
        "psi3_reconstruction": verify_psi3_reconstruction(),
        "free_boson_limit": delta_W_free_boson(),
        "classical_limit_correct": verify_classical_limit(),
        "counit_W": verify_counit_W(),
        "counit_psi3": verify_counit_psi3(),
        "comparison_spin2": compare_with_spin2(),
        "explicit_formula": {
            k: str(v) for k, v in delta_W_explicit().items()
        },
    }


if __name__ == "__main__":
    results = run_all()

    print("=" * 70)
    print("W_{1+inf} Miura coproduct at spin 3: verification suite")
    print("=" * 70)

    print("\n1. psi_3 reconstruction (consistency):")
    r = results["psi3_reconstruction"]
    print(f"   All match: {r['all_match']}")
    if r["mismatches"]:
        for k, v in r["mismatches"].items():
            print(f"   MISMATCH at {k}: {v}")

    print("\n2. Free boson limit (Psi=1):")
    fb = results["free_boson_limit"]
    for k, v in fb.items():
        print(f"   {k}: {v}")

    print("\n3. Classical limit (Psi->inf):")
    print(f"   Correct: {results['classical_limit_correct']}")

    print("\n4. Counit verification (W only):")
    cu = results["counit_W"]
    print(f"   All match: {cu['all_match']}")
    if cu["mismatches"]:
        for k, v in cu["mismatches"].items():
            print(f"   MISMATCH at {k}: {v}")

    print("\n5. Counit verification (full psi_3):")
    cp = results["counit_psi3"]
    print(f"   All match: {cp['all_match']}")
    if cp["mismatches"]:
        for k, v in cp["mismatches"].items():
            print(f"   MISMATCH at {k}: {v}")

    print("\n6. Explicit formula for Delta_z(W):")
    for k, v in results["explicit_formula"].items():
        print(f"   {k}: {v}")

    all_pass = (
        r["all_match"]
        and results["classical_limit_correct"]
        and cu["all_match"]
        and cp["all_match"]
    )
    print(f"\nALL CHECKS PASS: {all_pass}")
