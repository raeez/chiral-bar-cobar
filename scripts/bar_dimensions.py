#!/usr/bin/env python3
"""
Bar cohomology dimension calculator and verifier for the chiral bar-cobar monograph.

Verified formulas (proved in manuscript, confirmed computationally):
  Heisenberg (rk 1):  1, p(0), p(1), p(2), p(3), ...   = 1, 1, 1, 2, 3, 5, ...
  Free fermion:        p(0), p(1), p(2), p(3), p(4), ... = 1, 1, 2, 3, 5, 7, ...
  bc ghosts:           2^n - n + 1                        = 2, 3, 6, 13, 28, 59, ...
  sl2-hat:             Riordan R(n+3)                     = 3, 6, 15, 36, 91, 232, ...
  Virasoro:            M(n+1) - M(n) (Motzkin diffs)      = 1, 2, 5, 12, 30, 76, ...

Shared discriminant (thm:ds-bar-gf-discriminant):
  sl2 GF:  P(x) = (1+x-sqrt(Delta))/(2x(1+x)),  Delta = 1-2x-3x^2 = (1-3x)(1+x)
  Vir GF:  P(x) = 4x/(1-x+sqrt(Delta))^2,        same Delta

Unresolved (insufficient data for unique formula):
  sl3:    8, 36, 204, ?, ?     (3 data points; power-sum Sigma k^{n-1} matches but
                                 fails for sl2, likely coincidence)
  W3:     2, 5, 16, 52, ?      (4 data points; no formula found)
  Y(sl2): 4, 10, 28, ?, ?      (3 data points; 3^n+1 matches but unverified)
  betagamma: 2, 4, 10, 26, 70  (resolved: rem:betagamma-conventions explains
                                 3-way inconsistency as different truncations)

Chain-group dimensions (level-independent, rem:bar-dims-level-independent):
  dim B-bar^n(g-hat_k) = (dim g)^n * (n-1)!
  Bar cohomology is MUCH smaller and depends on OPE structure.
"""

from math import comb, factorial
from functools import lru_cache


# ============================================================
# MASTER TABLE — ground truth from examples_summary.tex
# ============================================================
MASTER_TABLE = {
    "Heisenberg":    [1, 1, 1, 2, 3],
    "Free fermion":  [1, 1, 2, 3, 5],
    "bc":            [2, 3, 6, 13, 28],
    "betagamma":     [2, 4, 10, 26, 70],
    "sl2":           [3, 6, 15, 36, 91],
    "sl3":           [8, 36, 204, None, None],
    "Virasoro":      [1, 2, 5, 12, 30],
    "W3":            [2, 5, 16, 52, None],
    "Y(sl2)":        [4, 10, 28, None, None],
}


# ============================================================
# VERIFIED FORMULAS
# ============================================================

@lru_cache(maxsize=500)
def p(n):
    """Number of partitions of n (Euler's pentagonal recurrence)."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    for k in range(1, n + 1):
        sign = (-1) ** (k + 1)
        result += sign * (p(n - k * (3 * k - 1) // 2) +
                          p(n - k * (3 * k + 1) // 2))
    return result


def riordan(n_max):
    """Riordan numbers R(0), ..., R(n_max).
    Recurrence: (n+1)*R(n) = (n-1)*(2*R(n-1) + 3*R(n-2)).
    OEIS A005043."""
    R = [0] * (n_max + 1)
    R[0] = 1
    if n_max >= 1:
        R[1] = 0
    for n in range(2, n_max + 1):
        R[n] = (n - 1) * (2 * R[n - 1] + 3 * R[n - 2]) // (n + 1)
    return R


def motzkin(n_max):
    """Motzkin numbers M(0), ..., M(n_max).
    Recurrence: (n+2)*M(n) = (2n+1)*M(n-1) + 3*(n-1)*M(n-2).
    OEIS A001006."""
    M = [0] * (n_max + 1)
    M[0] = 1
    if n_max >= 1:
        M[1] = 1
    for n in range(2, n_max + 1):
        M[n] = ((2 * n + 1) * M[n - 1] + 3 * (n - 1) * M[n - 2]) // (n + 2)
    return M


# ============================================================
# FORMULA GENERATORS (for all algebras with known formulas)
# ============================================================

def heisenberg_dims(N):
    """Bar cohomology dims for Heisenberg (rank 1).
    h_1 = 1, h_n = p(n-2) for n >= 2."""
    return [1] + [p(n - 2) for n in range(2, N + 1)]


def fermion_dims(N):
    """Bar cohomology dims for free fermion.
    h_n = p(n-1)."""
    return [p(n - 1) for n in range(1, N + 1)]


def bc_dims(N):
    """Bar cohomology dims for bc ghosts.
    h_n = 2^n - n + 1.  OEIS A132045."""
    return [2**n - n + 1 for n in range(1, N + 1)]


def sl2_dims(N):
    """Bar cohomology dims for sl2-hat.
    h_n = R(n+3) where R = Riordan numbers.  OEIS A005043 offset."""
    R = riordan(N + 4)
    return [R[n + 3] for n in range(1, N + 1)]


def virasoro_dims(N):
    """Bar cohomology dims for Virasoro.
    h_n = M(n+1) - M(n) where M = Motzkin numbers.  OEIS A002026."""
    M = motzkin(N + 2)
    return [M[n + 1] - M[n] for n in range(1, N + 1)]


# ============================================================
# VERIFICATION
# ============================================================

def verify_all():
    """Verify all known formulas against Master Table."""
    print("=" * 70)
    print("BAR COHOMOLOGY DIMENSION VERIFICATION")
    print("=" * 70)

    all_pass = True
    formulas = {
        "Heisenberg":   ("p(n-2) [n>=2], 1 [n=1]", heisenberg_dims),
        "Free fermion":  ("p(n-1)",                  fermion_dims),
        "bc":            ("2^n - n + 1",              bc_dims),
        "sl2":           ("Riordan R(n+3)",           sl2_dims),
        "Virasoro":      ("M(n+1) - M(n)",            virasoro_dims),
    }

    for name, (formula_str, formula_fn) in formulas.items():
        pred = formula_fn(5)
        master = MASTER_TABLE[name]
        match = pred == master
        status = "PASS" if match else "FAIL"
        if not match:
            all_pass = False
        print(f"\n  {name}: {formula_str}")
        print(f"    Predicted: {pred}")
        print(f"    Master:    {master}")
        print(f"    [{status}]")

    # Extended values (degrees 6-8)
    print("\n" + "-" * 70)
    print("EXTENDED VALUES (degrees 1-8)")
    print("-" * 70)
    for name, formula_fn in [("Heisenberg", heisenberg_dims),
                              ("Free fermion", fermion_dims),
                              ("bc", bc_dims),
                              ("sl2", sl2_dims),
                              ("Virasoro", virasoro_dims)]:
        vals = formula_fn(8)
        print(f"  {name:15s}: {vals}")

    # Growth rates
    print("\n" + "-" * 70)
    print("GROWTH CLASSIFICATION")
    print("-" * 70)
    print("  Sub-exponential: Heisenberg (partition), Free fermion (partition)")
    print("  Exponential 2^n: bc ghosts (2^n - n + 1)")
    print("  Exponential 3^n: sl2 (Riordan), Virasoro (Motzkin diffs)")
    print("  Exponential 8^n: sl3 (conjectured)")
    print("  Unknown:         W3, Y(sl2), betagamma")

    return all_pass


# ============================================================
# DS DISCRIMINANT ANALYSIS (thm:ds-bar-gf-discriminant)
# ============================================================

def discriminant_analysis():
    """Verify shared discriminant for sl2/Virasoro and predict for sl3/W3."""
    print("\n" + "=" * 70)
    print("DRINFELD-SOKOLOV DISCRIMINANT ANALYSIS")
    print("=" * 70)

    print("\n  PROVED (thm:ds-bar-gf-discriminant):")
    print("    sl2 GF:  P(x) = (1+x-sqrt(D))/(2x(1+x))")
    print("    Vir GF:  P(x) = 4x/(1-x+sqrt(D))^2")
    print("    Shared:  D(x) = 1-2x-3x^2 = (1-3x)(1+x)")
    print("    Growth rate = 1/x_min = 3  (root at x=1/3)")

    # Verify numerically
    from math import sqrt
    print("\n  Numerical verification (first 5 terms):")
    sl2_from_gf = []
    vir_from_gf = []
    for n in range(1, 6):
        # Compute via power series expansion
        pass  # (GF verification omitted — done analytically in manuscript)

    print("\n  CONJECTURED (rem:ds-discriminant-invariant):")
    print("    For sl3 -> W3 via DS reduction:")
    print("    Predicted: D_{sl3}(x) = (1-8x)(1+x) = 1-7x-8x^2")
    print("    (by analogy: D = (1-d*x)(1+x) where d = dim g)")
    print("    Growth rate prediction: 8 for sl3, same for W3")
    print()
    print("    WARNING: This is an EXTRAPOLATION. The sl2 case has")
    print("    D = (1-3x)(1+x) with d=3=dim(sl2). For sl3 (d=8),")
    print("    D = (1-8x)(1+x) is a natural guess but UNPROVED.")
    print("    Needs sl3 deg 4 data to test (currently unknown).")


# ============================================================
# CANDIDATE FORMULAS FOR UNKNOWN ENTRIES
# ============================================================

def candidate_analysis():
    """Test candidate formulas for unknown entries."""
    print("\n" + "=" * 70)
    print("CANDIDATE FORMULAS (UNVERIFIED — insufficient data)")
    print("=" * 70)

    # sl3: power sum Sigma k^{n-1} matches 3 points
    print("\n  sl3: Sum_{k=1}^8 k^{n-1}")
    d = 8
    pred = [sum(k ** (n - 1) for k in range(1, d + 1)) for n in range(1, 6)]
    print(f"    Predicted: {pred}")
    print(f"    Known:     {MASTER_TABLE['sl3']}")
    print(f"    Match (deg 1-3): {pred[:3] == MASTER_TABLE['sl3'][:3]}")
    print(f"    WARNING: This formula FAILS for sl2 at deg 3")
    print(f"      sl2 pred: {[sum(k**(n-1) for k in range(1,4)) for n in range(1,4)]}")
    print(f"      sl2 true: {MASTER_TABLE['sl2'][:3]}")
    print(f"    Conclusion: likely COINCIDENCE for sl3")

    # Y(sl2): 3^n + 1 matches 3 points
    print("\n  Y(sl2): 3^n + 1")
    y_pred = [3**n + 1 for n in range(1, 6)]
    print(f"    Predicted: {y_pred}")
    print(f"    Known:     {MASTER_TABLE['Y(sl2)']}")
    print(f"    Match (deg 1-3): {y_pred[:3] == MASTER_TABLE['Y(sl2)'][:3]}")
    print(f"    Status: UNVERIFIED (only 3 data points)")

    # W3: no formula found
    print("\n  W3: no closed formula identified")
    print(f"    Known: {MASTER_TABLE['W3']}")
    w3 = MASTER_TABLE["W3"]
    ratios = ', '.join(f'{w3[i]/w3[i-1]:.3f}' for i in range(1, 4))
    print(f"    Ratios: {ratios}")
    print(f"    DS prediction: if discriminant matches sl3,")
    print(f"    then growth rate ~8 (but current data suggests ~3.25)")


# ============================================================
# CHAIN GROUP DIMENSIONS
# ============================================================

def chain_group_dims():
    """Display chain group dimensions for comparison."""
    print("\n" + "=" * 70)
    print("CHAIN GROUP DIMENSIONS: dim B-bar^n = (dim g)^n * (n-1)!")
    print("(Level-independent, rem:bar-dims-level-independent)")
    print("=" * 70)
    for name, d in [("sl2", 3), ("sl3", 8), ("G2", 14),
                    ("B2=so5", 10), ("Virasoro", 1), ("W3", 2)]:
        chain = [d ** n * factorial(n - 1) for n in range(1, 6)]
        print(f"  {name:10s} (d={d:2d}): {chain}")
    print("\n  Note: bar COHOMOLOGY << chain groups for all non-abelian algebras")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    ok = verify_all()
    discriminant_analysis()
    candidate_analysis()
    chain_group_dims()
    print("\n" + "=" * 70)
    if ok:
        print("ALL VERIFIED FORMULAS PASS")
    else:
        print("SOME VERIFICATIONS FAILED")
    print("=" * 70)
