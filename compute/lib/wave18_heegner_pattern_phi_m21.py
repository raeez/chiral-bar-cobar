"""
Multi-path verifier for the Heegner pattern of the K3 BV obstruction tower.

Theorem (Vol I bv_brst.tex, thm:bvbrst-heegner-all-order; Vol II twin):
    c_n = c_{phi_{-2,1}}(n) * [H_n]   in H^2(g_{Delta_5}, C), for n >= 1,
where phi_{-2,1}(tau, z) = theta_1(tau, z)^2 / eta(tau)^6 is the weight -2
index 1 weak Jacobi form, c_{phi_{-2,1}}(N) its Fourier coefficients
(supported on admissible discriminants N in {-1, 0, 3, 4, 7, 8, 11, ...},
i.e., N mod 4 in {0, 3}; equivalently, N mod 4 in {-1, 0}), and [H_n] the
Humbert divisor class of discriminant n on barM_{A_2}.

Admissibility residue theorem: c_n = 0 unless n mod 4 in {0, 3}
(Eichler--Zagier 1985 Theorem 9.3).

Leading values at admissible n (with normalisation c(-1) = -1):
    c_phi(3) = -8,  c_phi(4) = 12,  c_phi(7) = -39,  c_phi(8) = 56.

Primary sources:
    Bruinier 2002 Prop 5.1 (Heegner-Chern reciprocity on barM_{A_2}).
    Borcherds 1998 Theorem 10.1 (singular-theta lift, Phi_10).
    Eichler-Zagier 1985 Theorem 9.3 (admissibility), Table 1 (tabulation).
    Costello-Gaiotto-Paquette 2018 (twisted-holographic factorisation algebra).
    Gritsenko-Nikulin 1998 Theorem 2.1 (denominator identity for Phi_10).

This module computes c_{phi_{-2,1}}(N) directly from the infinite-product
form of phi_{-2,1}, independent of any table, and verifies the Wave 17.5
leading values c_3=-8, c_4=12, c_7=-39, c_8=56.
"""

from __future__ import annotations
from typing import Dict, Tuple
import sympy as sp


def compute_phi_m21_coefficients(q_max: int = 8) -> Dict[int, int]:
    """Return the map from discriminant N to the Fourier coefficient c_phi_{-2,1}(N).

    Uses the infinite-product form
        phi_{-2,1}(tau, z) = -(y - 2 + y^{-1}) *
            prod_{n>=1} (1 - q^n y)^2 (1 - q^n/y)^2 / (1 - q^n)^4,
    truncated at q^{q_max}. The coefficient c(n, r) depends only on the
    discriminant N = 4n - r^2, confirming the Eichler-Zagier Jacobi
    structure.

    Normalisation: c_phi_{-2,1}(-1) = -1 (from the prefactor).
    """
    q, y = sp.symbols("q y")
    y_clear = 2 * q_max

    pref = -(y - 2 + 1 / y)
    expr = sp.sympify(pref)

    for n in range(1, q_max + 1):
        num_term = sp.expand((1 - q**n * y) ** 2 * (1 - q**n / y) ** 2)
        # 1/(1 - q^n)^4 = sum_{k>=0} C(k+3, 3) q^{n k}
        den_inv_series = sum(
            sp.binomial(k + 3, 3) * q ** (n * k) for k in range((q_max // n) + 2)
        )
        expr = sp.expand(expr * num_term * den_inv_series)

        # Truncate q powers > q_max
        expr_trunc = 0
        for term in sp.Add.make_args(expr):
            q_pow = 0
            for f in sp.Mul.make_args(term):
                if f == q:
                    q_pow += 1
                elif f.is_Pow and f.args[0] == q:
                    q_pow += int(f.args[1])
            if q_pow <= q_max:
                expr_trunc += term
        expr = sp.expand(expr_trunc)

    # Extract coefficients c(n, r)
    coeffs_nr: Dict[Tuple[int, int], int] = {}
    for k in range(q_max + 1):
        ck = expr.coeff(q, k)
        ck_shifted = sp.expand(ck * y**y_clear)
        ck_poly = sp.Poly(ck_shifted, y)
        for monom, c_nr in ck_poly.as_dict().items():
            r = monom[0] - y_clear
            coeffs_nr[(k, r)] = int(c_nr)

    # Collapse to discriminant N
    coeffs_N: Dict[int, int] = {}
    for (k, r), c in coeffs_nr.items():
        N = 4 * k - r * r
        if N in coeffs_N:
            assert coeffs_N[N] == c, (
                f"Inconsistency at N = {N}: {coeffs_N[N]} vs {c} "
                f"(violates Jacobi form structure)"
            )
        else:
            coeffs_N[N] = c

    return coeffs_N


def verify_wave18_heegner_pattern(q_max: int = 8) -> Dict[str, object]:
    """Verify Wave 18 leading values and admissibility residue theorem.

    Returns a dict with:
      'coefficients': {N: c_phi(N)},
      'leading_values': {n: c_n for n in (3, 4, 7, 8)},
      'admissibility_test': {n: (is_admissible, c_phi(n)) for n in 1..12},
      'matches_wave17_5': bool,
    """
    coeffs = compute_phi_m21_coefficients(q_max=q_max)

    expected_wave17_5 = {3: -8, 4: 12, 7: -39, 8: 56}
    leading_values = {n: coeffs.get(n, 0) for n in (3, 4, 7, 8)}
    matches = all(leading_values[n] == expected_wave17_5[n] for n in (3, 4, 7, 8))

    admissibility = {}
    for n in range(1, 13):
        is_adm = (n % 4) in (0, 3)
        c = coeffs.get(n, 0)
        # Admissibility theorem: c_phi(N) = 0 unless N mod 4 in {0, 3}.
        if not is_adm:
            assert c == 0, f"Admissibility violated: c_phi({n}) = {c} with n%4 = {n%4}"
        admissibility[n] = (is_adm, c)

    return {
        "coefficients": coeffs,
        "leading_values": leading_values,
        "expected_wave17_5": expected_wave17_5,
        "admissibility_test": admissibility,
        "matches_wave17_5": matches,
    }


def asymptotic_bound(n: int, m: int = 1) -> float:
    """Ramanujan-Petersson asymptotic: |c_phi(N)| ~ exp(pi * sqrt(N/m))
    at index m = 1, N = n (Gritsenko 1999; Dabholkar-Murthy-Zagier 2012).
    Diverges super-polynomially; the BV obstruction tower is a formal
    hbar-series with divergent coefficients, converging analytically
    only after Lusztig specialisation hbar_qg^2 = -1/8.
    """
    import math

    return math.exp(math.pi * math.sqrt(n / m))


if __name__ == "__main__":
    result = verify_wave18_heegner_pattern(q_max=8)

    print("Wave 18 Heegner pattern verifier")
    print("=" * 70)
    print()
    print("Fourier coefficients c_phi_{-2,1}(N) at admissible N:")
    for N in sorted(result["coefficients"]):
        c = result["coefficients"][N]
        if c != 0:
            adm = "admissible" if (N % 4) in (0, 3) or N == -1 else "inadmissible"
            print(f"  c_phi({N:3d}) = {c:+6d}   ({adm})")

    print()
    print("Leading values at admissible orders (BV obstruction c_n):")
    for n in (3, 4, 7, 8):
        print(
            f"  c_{n} = c_phi({n}) = {result['leading_values'][n]:+4d}   "
            f"(expected {result['expected_wave17_5'][n]:+4d})"
        )

    print()
    print(f"Matches Wave 17.5 leading values: {result['matches_wave17_5']}")

    print()
    print("Asymptotic growth |c_phi(n)| ~ exp(pi * sqrt(n)):")
    for n in (10, 100, 1000):
        print(f"  n = {n:5d}: exp(pi * sqrt(n)) ~ {asymptotic_bound(n):.3e}")
