r"""Principal W-algebra Koszul conductors for all simple Lie algebras: exact Fraction arithmetic.

MATHEMATICAL CONTENT
====================

For a simple Lie algebra g with rank r, dimension d, and dual Coxeter number h^v,
the principal W-algebra W(g, k) has Fateev-Lukyanov central charge:

    c(g, k) = r - d * h^v * (k + h^v - 1)^2 / (k + h^v)

The Feigin-Frenkel dual level is k' = -k - 2*h^v, and the complementarity sum:

    alpha(g) = c(g, k) + c(g, k')

is level-independent (k cancels algebraically).

ALGEBRAIC PROOF of k-independence:
    Let h = h^v.  Write K = k + h, so k' + h = -k - h, and
    c(k)  = r - d*h*(K - 1)^2 / K
    c(k') = r - d*h*(-K - 1)^2 / (-K) = r + d*h*(K + 1)^2 / K
    alpha = 2r + d*h*[(K+1)^2 - (K-1)^2] / K
          = 2r + d*h*[4K] / K
          = 2r + 4*d*h.

So alpha(g) = 2*rank(g) + 4*dim(g)*h^v(g) for ALL simple g.

The anomaly ratio for the principal W-algebra W(g) is:

    varrho(g) = sum_{i=1}^{rank(g)} 1 / s_i

where s_i = m_i + 1 are the conformal spins (m_i the exponents of g).
All generators of a principal W-algebra are bosonic.

For sl_N: spins = {2, 3, ..., N}, so varrho = H_N - 1 = sum_{j=2}^{N} 1/j.
This recovers kappa(W_N) = c * (H_N - 1) from CLAUDE.md C4.

The Koszul conductor is:

    K(W(g)) = kappa(W(g), k) + kappa(W(g), k') = varrho(g) * alpha(g)

PRINCIPAL RESULTS:
    alpha(E_8) = 2*8 + 4*248*30 = 16 + 29760 = 29776
    varrho(E_8) = 1/2 + 1/8 + 1/12 + 1/14 + 1/18 + 1/20 + 1/24 + 1/30 = 121/126
    K(W(E_8)) = (121/126) * 29776 = 1801448/63

CROSS-CHECKS:
    alpha(A_1) = 2 + 12 = 14?  No: 2*1 + 4*3*2 = 2 + 24 = 26.  Correct.
    K(Vir) = (1/2) * 26 = 13.  Matches CLAUDE.md C8/C18.
    alpha(A_2) = 2*2 + 4*8*3 = 4 + 96 = 100.  Correct.
    K(W_3) = (5/6) * 100 = 250/3.  Matches CLAUDE.md C18.

VERIFICATION PATHS:
    Path 1: Algebraic cancellation of k in alpha (proof above).
    Path 2: Numerical evaluation at k = 1, 2, 5, 17, -1, 1/3, 100.
    Path 3: Cross-family: A_1 -> K(Vir) = 13, A_2 -> K(W_3) = 250/3.
    Path 4: Closed-form formula alpha = 2r + 4dh matches all families.
    Path 5: Exponent tables from Bourbaki Lie Groups Ch. IV-VI, Table V.

References:
    Fateev-Lukyanov (1988): central charge formula for principal W-algebras.
    Feigin-Frenkel (1992): dual level k' = -k - 2h^v.
    Bourbaki, Lie Groups Ch. IV-VI: exponents of simple Lie algebras.
    CLAUDE.md C4, C8, C18, C20: kappa and Koszul conductor formulas.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Tuple


# =============================================================================
# Lie algebra data: (rank, dimension, dual Coxeter number)
# =============================================================================

LIE_ALGEBRA_DATA: Dict[str, Tuple[int, int, int]] = {
    # A_n = sl_{n+1}
    'A1': (1, 3, 2),
    'A2': (2, 8, 3),
    'A3': (3, 15, 4),
    'A4': (4, 24, 5),
    'A5': (5, 35, 6),
    'A6': (6, 48, 7),
    'A7': (7, 63, 8),
    'A8': (8, 80, 9),
    # B_n = so_{2n+1}
    'B2': (2, 10, 3),
    'B3': (3, 21, 5),
    'B4': (4, 36, 7),
    'B5': (5, 55, 9),
    'B6': (6, 78, 11),
    'B7': (7, 105, 13),
    'B8': (8, 136, 15),
    # C_n = sp_{2n}
    'C2': (2, 10, 3),  # C_2 = B_2 as Lie algebras (same dim/hv but different exponents)
    'C3': (3, 21, 4),
    'C4': (4, 36, 5),
    'C5': (5, 55, 6),
    'C6': (6, 78, 7),
    'C7': (7, 105, 8),
    'C8': (8, 136, 9),
    # D_n = so_{2n}
    'D4': (4, 28, 6),
    'D5': (5, 45, 8),
    'D6': (6, 66, 10),
    'D7': (7, 91, 12),
    'D8': (8, 120, 14),
    # Exceptional
    'E6': (6, 78, 12),
    'E7': (7, 133, 18),
    'E8': (8, 248, 30),
    'F4': (4, 52, 9),
    'G2': (2, 14, 4),
}


# =============================================================================
# Exponents of simple Lie algebras (Bourbaki convention)
# =============================================================================

def exponents_of(name: str) -> List[int]:
    """Return the exponents of the simple Lie algebra g.

    Source: Bourbaki, Lie Groups and Lie Algebras, Ch. IV-VI, Table V.
    """
    if name.startswith('A'):
        n = int(name[1:])
        return list(range(1, n + 1))
    elif name.startswith('B'):
        n = int(name[1:])
        return list(range(1, 2 * n, 2))
    elif name.startswith('C'):
        n = int(name[1:])
        return list(range(1, 2 * n, 2))
    elif name.startswith('D'):
        n = int(name[1:])
        # Exponents: 1, 3, 5, ..., 2n-3, n-1
        return sorted(list(range(1, 2 * n - 2, 2)) + [n - 1])
    elif name == 'E6':
        return [1, 4, 5, 7, 8, 11]
    elif name == 'E7':
        return [1, 5, 7, 9, 11, 13, 17]
    elif name == 'E8':
        return [1, 7, 11, 13, 17, 19, 23, 29]
    elif name == 'F4':
        return [1, 5, 7, 11]
    elif name == 'G2':
        return [1, 5]
    else:
        raise ValueError(f"Unknown Lie algebra: {name}")


def spins_of(name: str) -> List[int]:
    """Conformal spins of generators of the principal W-algebra W(g).

    Spin = exponent + 1.
    """
    return [e + 1 for e in exponents_of(name)]


# =============================================================================
# Core functions: exact Fraction arithmetic
# =============================================================================

def central_charge(rank: int, dim: int, hv: int, k: Fraction) -> Fraction:
    """Fateev-Lukyanov central charge c(g, k) for the principal W-algebra.

    c(g, k) = rank - dim * h^v * (k + h^v - 1)^2 / (k + h^v)
    """
    k = Fraction(k)
    return Fraction(rank) - Fraction(dim * hv) * (k + hv - 1) ** 2 / (k + hv)


def dual_level(k: Fraction, hv: int) -> Fraction:
    """Feigin-Frenkel dual level: k' = -k - 2*h^v."""
    return -Fraction(k) - 2 * hv


def alpha_closed_form(rank: int, dim: int, hv: int) -> Fraction:
    """Closed-form complementarity sum: alpha = 2*rank + 4*dim*h^v.

    This is the k-independent value of c(k) + c(k').
    """
    return Fraction(2 * rank + 4 * dim * hv)


def alpha_numerical(rank: int, dim: int, hv: int, k: Fraction) -> Fraction:
    """Compute alpha = c(k) + c(k') at a specific k value."""
    kp = dual_level(k, hv)
    return central_charge(rank, dim, hv, k) + central_charge(rank, dim, hv, kp)


def verify_k_independence(rank: int, dim: int, hv: int,
                          test_levels: List[Fraction] = None) -> bool:
    """Verify that alpha(k) is constant across multiple k values."""
    if test_levels is None:
        test_levels = [Fraction(1), Fraction(2), Fraction(5), Fraction(17),
                       Fraction(-1), Fraction(1, 3), Fraction(100),
                       Fraction(7, 11), Fraction(-hv + 1)]
    expected = alpha_closed_form(rank, dim, hv)
    return all(alpha_numerical(rank, dim, hv, k) == expected for k in test_levels)


def harmonic(n: int) -> Fraction:
    """Harmonic number H_n = sum_{j=1}^{n} 1/j.

    H_1 = 1, H_2 = 3/2, H_3 = 11/6, ...
    """
    return sum(Fraction(1, j) for j in range(1, n + 1))


def varrho(name: str) -> Fraction:
    """Anomaly ratio for the principal W-algebra W(g).

    varrho(g) = sum_{i=1}^{rank(g)} 1/s_i
    where s_i are the conformal spins (= exponents + 1).

    For sl_N (type A_{N-1}): varrho = H_N - 1 = sum_{j=2}^{N} 1/j.
    """
    return sum(Fraction(1, s) for s in spins_of(name))


def kappa(name: str, k: Fraction) -> Fraction:
    """kappa(W(g), k) = varrho(g) * c(g, k)."""
    rank, dim, hv = LIE_ALGEBRA_DATA[name]
    return varrho(name) * central_charge(rank, dim, hv, k)


def koszul_conductor(name: str) -> Fraction:
    """Koszul conductor K(W(g)) = varrho(g) * alpha(g).

    Level-independent; equals kappa(k) + kappa(k').
    """
    rank, dim, hv = LIE_ALGEBRA_DATA[name]
    return varrho(name) * alpha_closed_form(rank, dim, hv)


def self_dual_level(hv: int) -> Fraction:
    """Fixed point of k -> -k - 2*h^v: k_sd = -h^v."""
    return Fraction(-hv)


# =============================================================================
# Precomputed constants for E_8
# =============================================================================

# E_8 exponents: 1, 7, 11, 13, 17, 19, 23, 29
# E_8 spins: 2, 8, 12, 14, 18, 20, 24, 30
# Source: Bourbaki Lie Groups Ch. IV-VI, Table V.
E8_EXPONENTS = [1, 7, 11, 13, 17, 19, 23, 29]
E8_SPINS = [2, 8, 12, 14, 18, 20, 24, 30]

# alpha(E_8) = 2*8 + 4*248*30 = 16 + 29760 = 29776
# VERIFIED: [DC] closed-form 2r + 4dh = 2*8 + 4*248*30 = 29776;
# [DC] numerical evaluation at k=1: c(1) + c(-61) = 29776;
# [CF] same formula gives alpha(A1)=26 (Vir), alpha(A2)=100 (W_3).
ALPHA_E8 = Fraction(29776)

# varrho(E_8) = 1/2 + 1/8 + 1/12 + 1/14 + 1/18 + 1/20 + 1/24 + 1/30 = 121/126
# VERIFIED: [DC] direct sum of reciprocals of spins;
# [CF] for A-type, varrho = H_N - 1, matches CLAUDE.md C4 formula.
VARRHO_E8 = Fraction(121, 126)

# K(W(E_8)) = varrho(E_8) * alpha(E_8) = (121/126) * 29776 = 3602896/126 = 1801448/63
# VERIFIED: [DC] (121/126)*29776 = 121*29776/126 = 3602896/126 = 1801448/63;
# [CF] A1: (1/2)*26=13=K(Vir); A2: (5/6)*100=250/3=K(W_3). Both match CLAUDE.md C18.
K_E8 = Fraction(1801448, 63)


# =============================================================================
# Summary and verification
# =============================================================================

def summary() -> Dict[str, Dict[str, Fraction]]:
    """Compute alpha, varrho, K for all Lie algebras in the database."""
    results = {}
    for name, (rank, dim, hv) in sorted(LIE_ALGEBRA_DATA.items()):
        a = alpha_closed_form(rank, dim, hv)
        v = varrho(name)
        K = v * a
        results[name] = {
            'rank': rank,
            'dim': dim,
            'hv': hv,
            'spins': spins_of(name),
            'alpha': a,
            'varrho': v,
            'K': K,
            'k_independent': verify_k_independence(rank, dim, hv),
        }
    return results


def verify_all() -> bool:
    """Run all internal consistency checks."""
    checks = []

    # 1. alpha(A1) = 26
    checks.append(alpha_closed_form(1, 3, 2) == Fraction(26))

    # 2. K(Vir) = 13
    checks.append(koszul_conductor('A1') == Fraction(13))

    # 3. alpha(A2) = 100
    checks.append(alpha_closed_form(2, 8, 3) == Fraction(100))

    # 4. K(W_3) = 250/3
    checks.append(koszul_conductor('A2') == Fraction(250, 3))

    # 5. alpha(E8) = 29776
    checks.append(alpha_closed_form(8, 248, 30) == ALPHA_E8)

    # 6. varrho(E8) = 121/126
    checks.append(varrho('E8') == VARRHO_E8)

    # 7. K(E8) = 1801448/63
    checks.append(koszul_conductor('E8') == K_E8)

    # 8. k-independence for all families
    for name, (rank, dim, hv) in LIE_ALGEBRA_DATA.items():
        checks.append(verify_k_independence(rank, dim, hv))

    # 9. Closed-form matches numerical for all
    for name, (rank, dim, hv) in LIE_ALGEBRA_DATA.items():
        checks.append(
            alpha_numerical(rank, dim, hv, Fraction(1))
            == alpha_closed_form(rank, dim, hv)
        )

    # 10. A-type varrho = H_N - 1
    for n in range(1, 9):
        name = f'A{n}'
        if name in LIE_ALGEBRA_DATA:
            N = n + 1  # sl_{n+1} has W_N = W_{n+1}
            checks.append(varrho(name) == harmonic(N) - 1)

    return all(checks)


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    print("Principal W-algebra Koszul Conductors")
    print("=" * 80)
    print()

    # Closed-form derivation
    print("CLOSED-FORM: alpha(g) = 2*rank + 4*dim*h^v")
    print()

    # Table
    fmt = "{:<6} {:>4} {:>5} {:>4} {:<32} {:>12} {:>8} {:>15}  {}"
    print(fmt.format("Name", "rank", "dim", "h^v", "spins", "varrho", "alpha",
                      "K", "k-indep?"))
    print("-" * 110)

    results = summary()
    for name in ['A1', 'A2', 'A3', 'A4', 'B2', 'B3', 'C3', 'D4',
                  'E6', 'E7', 'E8', 'F4', 'G2']:
        r = results[name]
        print(fmt.format(
            name, r['rank'], r['dim'], r['hv'],
            str(r['spins']), str(r['varrho']), str(r['alpha']),
            str(r['K']), "YES" if r['k_independent'] else "FAIL"))

    print()
    print(f"E_8 RESULT:")
    print(f"  alpha(E_8) = {ALPHA_E8}")
    print(f"  varrho(E_8) = {VARRHO_E8} = {float(VARRHO_E8):.10f}")
    print(f"  K(W(E_8)) = {K_E8} = {float(K_E8):.6f}")
    print()

    # Cross-checks
    print("CROSS-CHECKS:")
    print(f"  K(Vir) = K(W(A1)) = {koszul_conductor('A1')} [expected: 13]")
    print(f"  K(W_3) = K(W(A2)) = {koszul_conductor('A2')} [expected: 250/3]")
    print(f"  K_BP from CLAUDE.md C20 = 196 (Bershadsky-Polyakov, NON-principal)")
    print()

    # Verification
    ok = verify_all()
    print(f"ALL INTERNAL CHECKS: {'PASS' if ok else 'FAIL'}")
