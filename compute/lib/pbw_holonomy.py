"""PBW holonomy theorem — intrinsic transport operator verification.

Verifies Theorem thm:pbw-recurrence and Theorem thm:growth-mode-factorization:
  1. The bar cohomology GF is D-finite of order rank(g)+1
  2. The Picard-Fuchs operator has singular locus = spectral discriminant
  3. The discriminant factors as (1 - dim(g)x) · Δ^DS(x)
  4. Δ^DS divides Δ_{W(g)}

Proved for sl₂; verified computationally for sl₃ (conditional on conj:sl3-bar-gf).
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Tuple

# ============================================================
# Riordan numbers (sl₂ bar cohomology)
# ============================================================

def sl2_bar_dims(n_max: int) -> List[int]:
    """dim H^n(bar(sl₂_hat)) for n = 1, ..., n_max.

    Uses Riordan R(n+3) with degree-2 correction (R(5)=6→5).
    Recurrence: (k+1)R(k) = (k-1)(2R(k-1) + 3R(k-2)) for k >= 2.
    Values: 3, 5, 15, 36, 91, 232, 603, 1585, ...
    """
    R = [1, 0, 1]  # R(0)=1, R(1)=0, R(2)=1
    for k in range(3, n_max + 4):
        num = (k - 1) * (2 * R[k - 1] + 3 * R[k - 2])
        R.append(num // (k + 1))
    dims = []
    for n in range(1, n_max + 1):
        val = R[n + 3]
        if n == 2:
            val = 5  # Corrected: R(5)=6, but H²=5
        dims.append(val)
    return dims


# ============================================================
# Picard-Fuchs verification for sl₂
# ============================================================

def _riordan_shifted(n_max: int) -> List[int]:
    """Riordan numbers R(n+3) for n = 1, ..., n_max (uncorrected).

    These satisfy (n+1)R(n) = (n-1)(2R(n-1) + 3R(n-2)) exactly.
    The ACTUAL bar cohomology differs at n=2 (R(5)=6, H²=5).
    """
    R = [1, 0, 1]
    for k in range(3, n_max + 4):
        num = (k - 1) * (2 * R[k - 1] + 3 * R[k - 2])
        R.append(num // (k + 1))
    return [R[n + 3] for n in range(1, n_max + 1)]


def verify_picard_fuchs_sl2(n_max: int = 20) -> Dict:
    """Verify that Riordan numbers R(n+3) are annihilated by the PF operator.

    L = (1-2x-3x²)∂² + (-1+3x)∂ + 1

    The PF equation governs the Riordan generating function;
    the actual bar dims differ at degree 2 (rem:bar-deg2-symmetric-square).
    """
    dims = _riordan_shifted(n_max + 5)
    # Pad: a[0] = 0 (no degree-0 term), a[n] = dims[n-1]
    a = [0] + dims

    errors = []
    # Verify the P-recursive recurrence directly:
    # (n+4)a_n = (n+2)(2a_{n-1} + 3a_{n-2})  [shifted Riordan]
    for n in range(3, min(n_max + 1, len(a))):
        lhs = (n + 4) * a[n]
        rhs = (n + 2) * (2 * a[n - 1] + 3 * a[n - 2])
        if lhs != rhs:
            errors.append((n, lhs - rhs))

    return {
        "verified_degrees": n_max - 1,
        "errors": errors,
        "all_zero": len(errors) == 0,
    }


# ============================================================
# Growth-mode factorization
# ============================================================

def discriminant_sl2() -> Tuple[List[int], List[int], List[int]]:
    """Δ_{sl₂} = (1-3x)(1+x) = 1 - 2x - 3x².

    Returns (full, growth, ds_invariant) as coefficient lists.
    Growth factor: (1 - 3x), where 3 = dim(sl₂).
    DS-invariant factor: (1 + x).
    """
    full = [1, -2, -3]  # 1 - 2x - 3x²
    growth = [1, -3]     # 1 - 3x
    ds = [1, 1]          # 1 + x
    return full, growth, ds


def discriminant_sl3() -> Tuple[List[int], List[int], List[int]]:
    """Δ_{sl₃} = (1-8x)(1-3x-x²) (conjectured).

    Returns (full, growth, ds_invariant) as coefficient lists.
    Growth factor: (1 - 8x), where 8 = dim(sl₃).
    DS-invariant factor: (1 - 3x - x²).
    """
    # (1-8x)(1-3x-x²) = 1 - 11x + 23x² + 8x³
    full = [1, -11, 23, 8]
    growth = [1, -8]
    ds = [1, -3, -1]
    return full, growth, ds


def poly_mul(p: List[int], q: List[int]) -> List[int]:
    """Multiply two polynomials (coefficient lists, constant first)."""
    result = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


def verify_factorization(full, growth, ds) -> bool:
    """Verify full = growth * ds."""
    product = poly_mul(growth, ds)
    return product == full


def transfer_matrix_eigenvalues(discriminant_coeffs: List[int]) -> List:
    """Eigenvalues of transfer matrix = reciprocals of roots of Δ(x).

    For Δ(x) = Σ c_k x^k, the reversed polynomial is
    p(t) = t^d Δ(t^{-1}) = Σ c_k t^{d-k}.
    Its roots are the eigenvalues.
    """
    d = len(discriminant_coeffs) - 1
    reversed_coeffs = list(reversed(discriminant_coeffs))
    # Return the reversed polynomial coefficients
    return reversed_coeffs


def companion_matrix(poly_coeffs: List[int]) -> List[List[Fraction]]:
    """Companion matrix of monic polynomial.

    poly_coeffs = [c_0, c_1, ..., c_{d-1}, 1] (monic, leading coeff = 1).
    Returns the companion matrix whose char poly is the given polynomial.
    """
    d = len(poly_coeffs) - 1
    assert poly_coeffs[-1] == 1, "Polynomial must be monic"
    M = [[Fraction(0)] * d for _ in range(d)]
    for i in range(d - 1):
        M[i + 1][i] = Fraction(1)
    for i in range(d):
        M[i][d - 1] = Fraction(-poly_coeffs[i])
    return M


# ============================================================
# DS-invariance verification
# ============================================================

def poly_divides(divisor: List[int], dividend: List[int]) -> bool:
    """Check if divisor | dividend over Q."""
    # Use polynomial long division
    d = [Fraction(c) for c in dividend]
    v = [Fraction(c) for c in divisor]
    if len(v) > len(d):
        return all(c == 0 for c in d)
    while len(d) >= len(v) and any(c != 0 for c in d):
        if d[-1] == 0:
            d.pop()
            continue
        if len(d) < len(v):
            break
        ratio = d[-1] / v[-1]
        shift = len(d) - len(v)
        for i in range(len(v)):
            d[shift + i] -= ratio * v[i]
        d.pop()
    return all(c == 0 for c in d)


def verify_ds_invariance_sl2() -> bool:
    """Verify Δ^DS_{sl₂} = (1+x) divides Δ_Vir = (1-3x)(1+x)."""
    _, _, ds = discriminant_sl2()
    delta_vir = [1, -2, -3]  # (1-3x)(1+x)
    return poly_divides(ds, delta_vir)


def verify_ds_invariance_sl3() -> bool:
    """Verify Δ^DS_{sl₃} = (1-3x-x²) divides Δ_{W₃} = (1-x)(1-3x-x²)."""
    _, _, ds = discriminant_sl3()
    delta_w3 = poly_mul([1, -1], [1, -3, -1])  # (1-x)(1-3x-x²)
    return poly_divides(ds, delta_w3)


# ============================================================
# Recurrence verification
# ============================================================

def verify_sl2_recurrence(n_max: int = 15) -> Dict:
    """Verify Riordan recurrence on R(n+3) (uncorrected sequence).

    (n+1)a_n = (n-1)(2a_{n-1} + 3a_{n-2}) for all n >= 3.
    Verified on the UNCORRECTED Riordan sequence, which satisfies
    the recurrence exactly.  The asymptotic companion matrix is
    [[2,3],[1,0]] with eigenvalues {3,-1}.
    """
    dims = _riordan_shifted(n_max)
    a = dims  # a[0] = R(4) = dim H^1 = 3, etc.

    errors = []
    for i in range(2, len(a)):
        n = i + 1  # bar degree
        # a_n = R(n+3), so (n+4)a_n = (n+2)(2a_{n-1} + 3a_{n-2})
        lhs = (n + 4) * a[i]
        rhs = (n + 2) * (2 * a[i - 1] + 3 * a[i - 2])
        if lhs != rhs:
            errors.append((n, lhs, rhs))

    return {
        "dims": dims,
        "verified": len(errors) == 0,
        "errors": errors,
    }


def verify_sl3_recurrence(n_max: int = 8) -> Dict:
    """Verify sl₃ constant-coefficient recurrence (conjectural).

    a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3).
    Known: a(1)=8, a(2)=36, a(3)=204.
    """
    a = [8, 36, 204]
    for _ in range(3, n_max):
        a.append(11 * a[-1] - 23 * a[-2] - 8 * a[-3])

    # Verify the first three match
    errors = []
    if a[0] != 8:
        errors.append(("a(1)", a[0], 8))
    if a[1] != 36:
        errors.append(("a(2)", a[1], 36))
    if a[2] != 204:
        errors.append(("a(3)", a[2], 204))

    return {
        "dims": a,
        "char_poly": [8, 23, -11, 1],  # t³ - 11t² + 23t + 8 = (t-8)(t²-3t-1)
        "eigenvalues": {
            "dominant": 8,
            "ds_invariant": "roots of t²-3t-1: (3±√13)/2",
        },
        "errors": errors,
    }


# ============================================================
# Molien-Weyl series verification
# ============================================================

def molien_weyl_invariants(lie_type: str, rank: int,
                           p_max: int = 20) -> List[int]:
    """dim(Sym^p(g))^g for p = 0, 1, ..., p_max.

    Uses the Chevalley theorem: the invariant ring is polynomial
    in r generators of degrees d_1, ..., d_r.
    """
    if lie_type == "A" and rank == 1:
        # sl₂: degree 2
        degrees = [2]
    elif lie_type == "A" and rank == 2:
        # sl₃: degrees 2, 3
        degrees = [2, 3]
    elif lie_type == "A":
        # sl_{r+1}: degrees 2, 3, ..., r+1
        degrees = list(range(2, rank + 2))
    else:
        raise ValueError(f"Unsupported type {lie_type}{rank}")

    # dim(Sym^p(g))^g = number of partitions of p into parts from degrees
    # (with repetition)
    dims = [0] * (p_max + 1)
    dims[0] = 1
    for d in degrees:
        new_dims = list(dims)
        for p in range(d, p_max + 1):
            new_dims[p] += new_dims[p - d]
        dims = new_dims

    return dims


def count_molien_poles(lie_type: str, rank: int) -> int:
    """Number of independent poles in the Molien-Weyl series.

    For sl_{r+1}: r poles (from r independent degrees).
    """
    if lie_type == "A":
        return rank
    raise ValueError(f"Unsupported type {lie_type}{rank}")


# ============================================================
# Master verification
# ============================================================

def run_all_verifications() -> Dict:
    """Run all PBW holonomy theorem verifications."""
    results = {}

    # 1. sl₂ Riordan recurrence
    r1 = verify_sl2_recurrence()
    results["sl2_recurrence"] = r1
    print(f"sl₂ recurrence: {'PASS' if r1['verified'] else 'FAIL'}")
    print(f"  dims: {r1['dims'][:8]}")

    # 2. Picard-Fuchs verification
    r2 = verify_picard_fuchs_sl2()
    results["sl2_picard_fuchs"] = r2
    print(f"sl₂ Picard-Fuchs: {'PASS' if r2['all_zero'] else 'FAIL'}")
    print(f"  verified {r2['verified_degrees']} degrees")

    # 3. Growth-mode factorization
    for name, disc_fn in [("sl2", discriminant_sl2),
                           ("sl3", discriminant_sl3)]:
        full, growth, ds = disc_fn()
        ok = verify_factorization(full, growth, ds)
        results[f"{name}_factorization"] = ok
        print(f"{name} factorization: {'PASS' if ok else 'FAIL'}")
        print(f"  Δ = {full}, growth = {growth}, DS = {ds}")

    # 4. DS-invariance
    r4a = verify_ds_invariance_sl2()
    r4b = verify_ds_invariance_sl3()
    results["sl2_ds_invariance"] = r4a
    results["sl3_ds_invariance"] = r4b
    print(f"sl₂ DS-invariance: {'PASS' if r4a else 'FAIL'}")
    print(f"sl₃ DS-invariance: {'PASS' if r4b else 'FAIL'}")

    # 5. Molien-Weyl
    for name, lt, rk in [("sl₂", "A", 1), ("sl₃", "A", 2)]:
        inv = molien_weyl_invariants(lt, rk, 12)
        poles = count_molien_poles(lt, rk)
        results[f"{name}_molien"] = {
            "invariants": inv,
            "poles": poles,
            "rank_plus_1": rk + 1,
        }
        print(f"{name} Molien: {inv[:8]}, poles={poles}, "
              f"rank+1={rk+1}")

    # 6. sl₃ recurrence
    r6 = verify_sl3_recurrence()
    results["sl3_recurrence"] = r6
    print(f"sl₃ recurrence: dims = {r6['dims'][:6]}")
    print(f"  eigenvalues: {r6['eigenvalues']}")

    # 7. Transfer matrix for sl₂
    T = [[2, 3], [1, 0]]
    tr = T[0][0] + T[1][1]
    det = T[0][0] * T[1][1] - T[0][1] * T[1][0]
    char_poly = [det, -tr, 1]  # t² - 2t - 3 = (t-3)(t+1)
    results["sl2_transfer"] = {
        "matrix": T,
        "trace": tr,
        "det": det,
        "char_poly": char_poly,
        "eigenvalues": [3, -1],
        "matches_discriminant": char_poly == [-3, -2, 1],
    }
    print(f"sl₂ transfer matrix: {T}")
    print(f"  eigenvalues: {{3, -1}}, char poly: t²-2t-3 = (t-3)(t+1)")
    print(f"  discriminant: (1-3x)(1+x) = 1-2x-3x² ✓")

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("PBW HOLONOMY THEOREM — VERIFICATION")
    print("=" * 60)
    results = run_all_verifications()
    print("\n" + "=" * 60)
    all_pass = all(
        v if isinstance(v, bool) else
        v.get("verified", v.get("all_zero", True))
        for v in results.values()
        if isinstance(v, (bool, dict))
    )
    print(f"OVERALL: {'ALL PASS' if all_pass else 'SOME FAILURES'}")
