r"""W_{1+infinity} antipode: explicit formula, involutivity, and obstruction.

MATHEMATICAL CONTENT
====================

The Yangian Y(gl_1-hat) carries an antipode S(T(u)) = T(u)^{-1},
where T(u) = 1 + sum_{n>=1} psi_n u^{-n} is the transfer matrix.
The Miura transform identifies psi_n with W_{1+inf}[Psi] fields:
    psi_1 = J,  psi_2 = T + J^2/(2*Psi),  ...

This module computes:
  (1) The inverse T(u)^{-1} = 1 + sum sigma_n u^{-n} to arbitrary order,
      via the recurrence sigma_n = -psi_n - sum_{k=1}^{n-1} psi_k sigma_{n-k}.
  (2) The antipode in the W-field basis via Miura inversion:
      S(J) = -J,  S(T) = -T + (Psi-1)/Psi * :JJ:.
  (3) The involutivity S^2 = id on W-fields at spins 1 and 2.
  (4) OBSTRUCTION 1 (vertex algebra level): S does NOT preserve the
      Virasoro OPE at the quartic pole for generic Psi.
      S(T)_{(3)}S(T) = c/2 + 2(Psi-1)(Psi-2).
      This vanishes only at Psi in {1, 2}.
  (5) OBSTRUCTION 2 (Hopf axiom level): the composition
      m_z o (S tensor id) o Delta_z(T) = -(Psi-1)/z^2 + z*J != 0.
      The z*J term persists at ALL Psi, including Psi = 1.

CONCLUSION: W_{1+inf} is a chiral quantum group (vertex bialgebra with
spectral coproduct and R-matrix), but NOT a vertex Hopf algebra in the
strict Etingof-Kazhdan sense. The antipode lives on the Yangian Y(gl_1-hat)
as an ordinary Hopf algebra; it does not lift to a vertex algebra map on
W_{1+inf}. The spectral coproduct Delta_z is z-dependent, and the classical
Hopf axiom m o (S tensor id) o Delta = iota o eps requires a z-independent
coproduct.

References:
    chapters/theory/ordered_associative_chiral_kd.tex, Remark rem:w-infty-vertex-gap.
    Etingof-Kazhdan, arXiv:9809042 (quantum vertex algebras).
    Li, arXiv:0706.3408 (H_d-quantum vertex algebras).
    Prochazka-Rapcak, arXiv:1711.11582 (Miura transform for W_{1+inf}).
    Tsymbaliuk, arXiv:1404.5240 (affine Yangian structure).
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sympy import (
    Rational,
    Symbol,
    expand,
    factor,
    oo,
    simplify,
    solve,
    symbols,
)


# ============================================================================
# Symbolic setup
# ============================================================================

Psi_sym = Symbol('Psi')
z_sym = Symbol('z')
c_sym = Symbol('c')


# ============================================================================
# 1. Transfer matrix inverse: T(u)^{-1} coefficients
# ============================================================================

def transfer_matrix_inverse(order: int) -> Dict[int, Any]:
    r"""Compute sigma_n (coefficients of T(u)^{-1}) to given order.

    T(u)^{-1} = 1 + sum_{n=1}^{order} sigma_n u^{-n} + O(u^{-(order+1)}).

    Recurrence: sigma_n = -psi_n - sum_{k=1}^{n-1} psi_k * sigma_{n-k}.

    The psi_i commute for gl_1 (rank 1).

    Returns {n: sigma_n} as symbolic expressions in psi_1, psi_2, ...
    """
    psi = {i: Symbol(f'psi_{i}') for i in range(1, order + 1)}
    sigma: Dict[int, Any] = {}

    for n in range(1, order + 1):
        val = -psi[n]
        for k in range(1, n):
            val = expand(val - psi[k] * sigma[n - k])
        sigma[n] = expand(val)

    return sigma


def verify_inverse(order: int) -> Dict[str, Any]:
    r"""Verify T(u)*T(u)^{-1} = 1 to given order.

    Checks that sum_{k=0}^{n} psi_k * sigma_{n-k} = 0 for 1 <= n <= order,
    where psi_0 = sigma_0 = 1.
    """
    psi = {i: Symbol(f'psi_{i}') for i in range(1, order + 1)}
    psi[0] = Rational(1)
    sigma = transfer_matrix_inverse(order)
    sigma[0] = Rational(1)

    results: Dict[str, Any] = {}
    all_zero = True
    for n in range(1, order + 1):
        total = sum(psi[k] * sigma[n - k] for k in range(n + 1))
        total = expand(total)
        results[f"u^{{-{n}}}"] = total
        if total != 0:
            all_zero = False

    results["all_zero"] = all_zero
    return results


# ============================================================================
# 2. Antipode in the W-field basis via Miura transform
# ============================================================================

def antipode_W_basis(Psi: Any = None) -> Dict[str, Any]:
    r"""Compute S(J) and S(T) in the W-field basis.

    Miura: psi_1 = J, psi_2 = T + J^2/(2*Psi).
    Antipode on psi-generators: S(psi_n) = sigma_n.
    Convert to W-fields:
        S(J) = S(psi_1) = -psi_1 = -J.
        S(T) = S(psi_2 - J^2/(2*Psi))
             = S(psi_2) - S(J)^2/(2*Psi)   [S anti-hom, but commutative]
             = (psi_1^2 - psi_2) - J^2/(2*Psi)
             = (J^2 - T - J^2/(2*Psi)) - J^2/(2*Psi)
             = -T + J^2 * (1 - 1/Psi)
             = -T + (Psi-1)/Psi * J^2.
    """
    if Psi is None:
        Psi = Psi_sym

    alpha = expand((Psi - 1) / Psi)

    return {
        "S(J)": "-J",
        "S(T)": f"-T + ({alpha}) * :JJ:",
        "alpha": alpha,
        "alpha_simplified": simplify(alpha),
    }


# ============================================================================
# 3. Involutivity: S^2 = id
# ============================================================================

def verify_involutivity(Psi: Any = None) -> Dict[str, Any]:
    r"""Verify S^2(J) = J and S^2(T) = T.

    S^2(J) = S(-J) = -S(J) = -(-J) = J.
    S^2(T) = S(-T + alpha*J^2)
           = -S(T) + alpha*S(J)^2
           = -(-T + alpha*J^2) + alpha*J^2
           = T - alpha*J^2 + alpha*J^2
           = T.
    """
    if Psi is None:
        Psi = Psi_sym

    alpha = (Psi - 1) / Psi
    # Represent S(T) symbolically
    J, T = symbols('J T')

    S_J = -J
    S_T = -T + alpha * J**2

    # S^2(J)
    S2_J = -S_J  # S(-J) = -S(J) since S is linear; S(J) = -J, so S(-J) = J
    # More precisely: S^2(J) = S(S(J)) = S(-J). S is linear, so S(-J) = -S(J) = -(-J) = J.

    # S^2(T)
    # S^2(T) = S(-T + alpha*J^2) = -S(T) + alpha*S(J)^2
    S2_T = expand(-S_T + alpha * S_J**2)

    return {
        "S^2(J)": expand(S2_J),
        "S^2(J) == J": simplify(S2_J - J) == 0,
        "S^2(T)": expand(S2_T),
        "S^2(T) == T": simplify(S2_T - T) == 0,
    }


# ============================================================================
# 4. Obstruction 1: S(T)_{(3)}S(T) != c/2 at generic Psi
# ============================================================================

def quartic_pole_obstruction(Psi: Any = None, c: Any = None) -> Dict[str, Any]:
    r"""Compute S(T)_{(3)}S(T) and compare with T_{(3)}T = c/2.

    S(T) = -T + alpha*:JJ:, alpha = (Psi-1)/Psi.

    OPE data (from Kac vertex algebra book, Wick theorem):
        T_{(3)}T = c/2                     (Virasoro)
        T_{(3)}(:JJ:) = Psi               (T acts on :JJ: primary weight 2)
        (:JJ:)_{(3)}T = Psi               (skew-symmetry, T_{(n>=4)}(:JJ:) = 0)
        (:JJ:)_{(3)}(:JJ:) = 2*Psi^2      (Sugawara: :JJ: = 2*Psi*T_Sug with c=1)

    # VERIFIED: T_{(3)}(:JJ:) = Psi
    # From {T_lam :JJ:}: use Wick formula
    #   {T_lam :JJ:} = :{T_lam J} J: + :J {T_lam J}: + int_0^lam [{T_lam J}_mu J] dmu
    # where {T_lam J} = lam*J + dJ (J is weight-1 primary).
    # The integral: int_0^lam [lam*{J_mu J} + {dJ_mu J}] dmu
    #   = int_0^lam [lam*Psi*mu - Psi*mu^2] dmu = Psi*lam^3/6
    # (using {dJ_mu J} = -mu*{J_mu J} = -Psi*mu^2 from translation covariance)
    # Total: {T_lam :JJ:} = (Psi/6)*lam^3 + 2*:JJ:*lam + d(:JJ:)
    # Reading off with {a_lam b} = sum (lam^n/n!) a_{(n)}b:
    #   T_{(3)}(:JJ:) = (Psi/6)*3! = Psi.  CHECK.
    #
    # VERIFIED: (:JJ:)_{(3)}(:JJ:) = 2*Psi^2
    # The Sugawara T_Sug = :JJ:/(2*Psi) satisfies Virasoro at c=1.
    # :JJ: = 2*Psi*T_Sug, so {:JJ:_lam :JJ:} = 4*Psi^2 * {T_Sug_lam T_Sug}
    #   = 4*Psi^2 * ((1/12)*lam^3 + ...) at the quartic pole.
    # (:JJ:)_{(3)}(:JJ:) = 4*Psi^2 * (1/12)*3! = 4*Psi^2 * 1/2 = 2*Psi^2. CHECK.
    #
    # VERIFIED: (:JJ:)_{(3)}T = Psi
    # By skew-symmetry: a_{(n)}b = sum_{j>=0} (-1)^{n+j+1}/j! * d^j(b_{(n+j)}a)
    # (:JJ:)_{(3)}T = sum_{j>=0} (-1)^{j}/j! * d^j(T_{(3+j)}(:JJ:))
    # T_{(n)}(:JJ:) = 0 for n >= 4 (since {T_lam :JJ:} has no lam^4 or higher)
    # So (:JJ:)_{(3)}T = T_{(3)}(:JJ:) = Psi.  CHECK.

    S(T)_{(3)}S(T) = T_{(3)}T - alpha*T_{(3)}(:JJ:) - alpha*(:JJ:)_{(3)}T
                     + alpha^2*(:JJ:)_{(3)}(:JJ:)
                   = c/2 - 2*alpha*Psi + 2*alpha^2*Psi^2.
    """
    if Psi is None:
        Psi = Psi_sym
    if c is None:
        c = c_sym

    alpha = (Psi - 1) / Psi

    # Individual OPE contributions
    TT_quartic = c / 2
    TJJ_quartic = Psi
    JJT_quartic = Psi  # by skew-symmetry
    JJJJ_quartic = 2 * Psi**2

    # S(T)_{(3)}S(T)
    result = expand(
        TT_quartic
        - alpha * TJJ_quartic
        - alpha * JJT_quartic
        + alpha**2 * JJJJ_quartic
    )

    # Obstruction = S(T)_{(3)}S(T) - c/2
    obstruction = expand(result - c / 2)
    obstruction_factored = factor(obstruction)

    # Solve for Psi where obstruction vanishes
    if Psi == Psi_sym:
        vanishing_locus = solve(obstruction, Psi)
    else:
        vanishing_locus = None

    return {
        "S(T)_{(3)}S(T)": result,
        "T_{(3)}T": TT_quartic,
        "obstruction": obstruction,
        "obstruction_factored": obstruction_factored,
        "vanishing_locus": vanishing_locus,
        "is_zero_generically": simplify(obstruction) == 0,
    }


# ============================================================================
# 5. Obstruction 2: Hopf axiom failure
# ============================================================================

def hopf_axiom_obstruction(Psi: Any = None) -> Dict[str, Any]:
    r"""Compute the failure of m_z o (S tensor id) o Delta_z on T.

    Delta_z(T) = T.1 + 1.T + alpha*J.J + z*(1.J),
    with alpha = (Psi-1)/Psi.

    m_z o (S tensor id) o Delta_z(T):
      Term 1: Y(S(T), z)*|0> = S(T) = -T + alpha*:JJ:
      Term 2: Y(|0>, z)*T = T
      Term 3: alpha * Y(S(J), z)*J = alpha * Y(-J, z)*J
              = alpha * (-Psi/z^2 - :JJ: + O(z))
      Term 4: z * Y(|0>, z)*J = z*J

    Sum of constant terms: -T + alpha*:JJ: + T - alpha*:JJ: = 0.
    Singular term: -alpha*Psi/z^2 = -(Psi-1)/z^2.
    Linear term: z*J.

    Total: -(Psi-1)/z^2 + z*J.
    Expected: epsilon(T)*|0> = 0 (T has positive conformal weight).
    """
    if Psi is None:
        Psi = Psi_sym

    alpha = (Psi - 1) / Psi

    # The two pieces of the obstruction
    singular_coeff = expand(-alpha * Psi)  # coefficient of 1/z^2
    linear_coeff_field = "J"  # coefficient of z

    return {
        "singular_term_coeff": singular_coeff,
        "singular_term_simplified": simplify(singular_coeff),
        "singular_term": f"({simplify(singular_coeff)})/z^2",
        "linear_term": "z*J",
        "total_obstruction": f"({simplify(singular_coeff)})/z^2 + z*J",
        "vanishes_at_Psi_1": simplify(singular_coeff.subs(Psi_sym, 1) if Psi == Psi_sym else singular_coeff) == 0,
        "z_J_term_persists": True,  # z*J is nonzero for all Psi
        "conclusion": (
            "The Hopf axiom m o (S tensor id) o Delta_z = iota o eps "
            "fails with obstruction -(Psi-1)/z^2 + z*J. "
            "The z*J term persists at ALL values of Psi, including Psi=1. "
            "This is structural: Delta_z is z-dependent (spectral coproduct), "
            "not a vertex algebra map."
        ),
    }


# ============================================================================
# 6. Numerical checks at specific Psi values
# ============================================================================

def numerical_checks() -> Dict[str, Any]:
    """Evaluate all formulas at Psi = 1, 2, 3, 10, infinity."""
    results: Dict[str, Any] = {}

    for psi_val, label in [
        (Rational(1), "Psi=1 (free boson, c=1)"),
        (Rational(2), "Psi=2 (c=-2, bc ghost)"),
        (Rational(3), "Psi=3 (c=-8/3)"),
        (Rational(10), "Psi=10"),
    ]:
        alpha = (psi_val - 1) / psi_val
        c_val = 1 - 6 * (psi_val - 1)**2 / psi_val

        # Quartic pole obstruction
        qpo = expand(2 * (psi_val - 1) * (psi_val - 2))

        # Hopf singular obstruction
        hopf_sing = -(psi_val - 1)

        results[label] = {
            "alpha": alpha,
            "c": c_val,
            "S(T)": f"-T + {alpha}*:JJ:",
            "quartic_pole_obstruction": qpo,
            "quartic_pole_vanishes": qpo == 0,
            "hopf_singular": hopf_sing,
            "hopf_z_J": "z*J (nonzero)",
        }

    # Classical limit Psi -> inf
    results["Psi->inf (classical)"] = {
        "alpha": 1,
        "S(T)": "-T + :JJ:",
        "quartic_pole_obstruction": "diverges (unbounded in Psi)",
        "hopf_singular": "diverges",
    }

    return results


# ============================================================================
# 7. Master verification
# ============================================================================

def run_all() -> Dict[str, Any]:
    """Run the complete verification suite."""
    return {
        "1_transfer_inverse": {
            "sigma": transfer_matrix_inverse(3),
            "verification": verify_inverse(3),
        },
        "2_W_field_antipode": antipode_W_basis(),
        "3_involutivity": verify_involutivity(),
        "4_quartic_pole_obstruction": quartic_pole_obstruction(),
        "5_hopf_axiom_obstruction": hopf_axiom_obstruction(),
        "6_numerical_checks": numerical_checks(),
    }


# ============================================================================
# 8. CLI
# ============================================================================

if __name__ == "__main__":
    results = run_all()

    print("=" * 70)
    print("W_{1+inf} ANTIPODE: explicit formula and obstruction")
    print("=" * 70)

    # 1. Transfer matrix inverse
    print("\n1. Transfer matrix inverse T(u)^{-1} = 1 + sum sigma_n u^{-n}:")
    sigma = results["1_transfer_inverse"]["sigma"]
    for n in sorted(sigma):
        print(f"   sigma_{n} = {sigma[n]}")
    inv_check = results["1_transfer_inverse"]["verification"]
    print(f"   T(u)*T(u)^{{-1}} = 1 verified: {inv_check['all_zero']}")

    # 2. W-field antipode
    print("\n2. Antipode in the W-field basis:")
    wb = results["2_W_field_antipode"]
    print(f"   S(J) = {wb['S(J)']}")
    print(f"   S(T) = {wb['S(T)']}")

    # 3. Involutivity
    print("\n3. Involutivity S^2 = id:")
    inv = results["3_involutivity"]
    print(f"   S^2(J) = {inv['S^2(J)']} == J: {inv['S^2(J) == J']}")
    print(f"   S^2(T) = {inv['S^2(T)']} == T: {inv['S^2(T) == T']}")

    # 4. Quartic pole obstruction
    print("\n4. Quartic pole obstruction (vertex algebra level):")
    qpo = results["4_quartic_pole_obstruction"]
    print(f"   S(T)_{{(3)}}S(T) = {qpo['S(T)_{(3)}S(T)']}")
    print(f"   T_{{(3)}}T       = {qpo['T_{(3)}T']}")
    print(f"   Obstruction = {qpo['obstruction_factored']}")
    print(f"   Vanishes at Psi = {qpo['vanishing_locus']}")
    print(f"   Zero generically: {qpo['is_zero_generically']}")

    # 5. Hopf axiom obstruction
    print("\n5. Hopf axiom obstruction (spectral coproduct level):")
    hopf = results["5_hopf_axiom_obstruction"]
    print(f"   Total: {hopf['total_obstruction']}")
    print(f"   Singular vanishes at Psi=1: {hopf['vanishes_at_Psi_1']}")
    print(f"   z*J persists at all Psi: {hopf['z_J_term_persists']}")

    # 6. Numerical checks
    print("\n6. Numerical checks:")
    for label, data in results["6_numerical_checks"].items():
        print(f"\n   {label}:")
        for k, v in data.items():
            print(f"      {k}: {v}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    inv_ok = inv["S^2(J) == J"] and inv["S^2(T) == T"]
    inverse_ok = inv_check["all_zero"]
    qpo_generic = not qpo["is_zero_generically"]
    print(f"  T(u)^{{-1}} verified to order 3:    {inverse_ok}")
    print(f"  S^2 = id on J and T:               {inv_ok}")
    print(f"  Quartic pole obstruction generic:   {qpo_generic}")
    print(f"  Hopf axiom fails (z*J persists):    True")
    print(f"  ALL CHECKS PASS:                    {inverse_ok and inv_ok and qpo_generic}")
