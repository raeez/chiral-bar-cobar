#!/usr/bin/env python3
r"""
alpha_n_conductor_engine.py -- The W_N Koszul conductor complement alpha_N
and associated invariants in exact arithmetic.

THE MATHEMATICAL CONTENT:

For the principal W_N algebra at central charge c, the Koszul duality
W_N^! = W_N(c') with c' = alpha_N - c defines the conductor complement

    alpha_N = 2(N-1)(2N^2 + 2N + 1).

This is the total ghost central charge: the bc system at conformal weights
s = 2, 3, ..., N contributes c_bc(s) = 1 - 3(2s-1)^2 = -(6s^2 - 6s + 1)*2,
and alpha_N = -sum_{s=2}^{N} c_bc(s) = sum_{s=2}^{N} 2(6s^2 - 6s + 1).

Key invariants:
- Self-dual central charge: c* = alpha_N / 2  (the fixed point of c -> alpha_N - c).
- Koszul conductor: K(W_N) = kappa(W_N) + kappa(W_N^!) = (H_N - 1) * alpha_N,
  where H_N = sum_{j=1}^{N} 1/j is the N-th harmonic number.
  (CAUTION AP136: H_N - 1 != H_{N-1}. At N=2: H_2 - 1 = 1/2, H_1 = 1.)

Verification census:
    alpha_2 = 26    (Virasoro: c + c' = 26)
    alpha_3 = 100
    alpha_4 = 246
    alpha_5 = 488
    K(W_2) = 13     (matches Virasoro Koszul conductor)
    K(W_3) = 250/3
    K(W_4) = 533/2
    K(W_5) = 9394/15

CAUTION (AP1): kappa(W_N) = c * (H_N - 1), NOT c * H_{N-1}.
CAUTION (AP136): H_{N-1} != H_N - 1.  Evaluate at N=2 to distinguish.
CAUTION (C4): H_N = sum_{j=1}^{N} 1/j.  Upper limit N, NOT N-1.
CAUTION (C5): c_bc(lambda) = 1 - 3(2*lambda - 1)^2.  The ghost contribution
    at weight s is |c_bc(s)| = 2(6s^2 - 6s + 1).
"""

from fractions import Fraction


def alpha_N(N: int) -> Fraction:
    r"""W_N Koszul conductor complement: alpha_N = 2(N-1)(2N^2 + 2N + 1).

    This is the value c + c' for the W_N family, generalizing 26 for Virasoro.

    # VERIFIED: direct expansion + ghost decomposition sum [DC];
    #           N=2 -> 26 matches Virasoro [CF].
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    # VERIFIED: [DC] closed form equals the ghost sum sum_{s=2}^N 2(6s^2-6s+1);
    # [CF] N=2 gives 26, the Virasoro complement c+c'.
    # VERIFIED: [DC] alpha_N is the closed ghost-sum polynomial; [CF] N=2 reproduces 26.
    return Fraction(2 * (N - 1) * (2 * N**2 + 2 * N + 1))


def c_star(N: int) -> Fraction:
    r"""Self-dual central charge: c* = alpha_N / 2.

    The fixed point of the Koszul involution c -> alpha_N - c.
    At N=2: c* = 13 (Virasoro self-dual point, census C8).

    # VERIFIED: alpha_N(2)/2 = 13 [DC]; matches C8 [LT].
    """
    # VERIFIED: [DC] the involution fixed point solves c = alpha_N - c, hence c* = alpha_N/2;
    # [LC] N=2 gives the Virasoro self-dual point 13.
    # VERIFIED: [DC] c* = alpha_N/2 from c = alpha_N - c; [LC] N=2 -> 13.
    return alpha_N(N) / 2


def H_N(N: int) -> Fraction:
    r"""N-th harmonic number: H_N = sum_{j=1}^{N} 1/j.

    CAUTION (AP136, C19): upper limit is N, NOT N-1.
    H_1 = 1, H_2 = 3/2, H_3 = 11/6, H_4 = 25/12.

    # VERIFIED: H_2 = 3/2 [DC]; H_4 = 25/12 [DC].
    """
    if N < 1:
        raise ValueError(f"Harmonic number requires N >= 1, got {N}")
    # VERIFIED: [DC] H_N is the defining sum sum_{j=1}^N 1/j;
    # [LC] H_2 = 3/2 and H_4 = 25/12.
    # VERIFIED: [DC] H_N is the defining harmonic sum; [LC] H_2 = 3/2 and H_4 = 25/12.
    return sum(Fraction(1, j) for j in range(1, N + 1))


def K_WN(N: int) -> Fraction:
    r"""Koszul conductor of W_N: K(W_N) = (H_N - 1) * alpha_N.

    This equals kappa(W_N, c) + kappa(W_N, alpha_N - c) evaluated at
    generic c, using kappa(W_N) = c * (H_N - 1).

    K(W_N) = (H_N - 1) * alpha_N because:
      kappa(c) + kappa(c') = c*(H_N - 1) + (alpha_N - c)*(H_N - 1)
                            = alpha_N * (H_N - 1).

    CAUTION (AP136): H_N - 1 != H_{N-1}.
    At N=2: H_2 - 1 = 1/2, so K = 26 * 1/2 = 13.
    But H_1 = 1, so H_{N-1} would give 26 * 1 = 26 (WRONG).

    # VERIFIED: K(W_2) = 13 matches Virasoro [CF];
    #           K(W_3) = 250/3 [DC]; K(W_5) = 9394/15 [DC].
    """
    # VERIFIED: [DC] kappa(c)+kappa(alpha_N-c) cancels c and leaves alpha_N(H_N-1);
    # [CF] N=2 -> 13 and N=3 -> 250/3.
    # VERIFIED: [DC] K(W_N) = alpha_N(H_N-1); [CF] N=2 -> 13 and N=3 -> 250/3.
    return (H_N(N) - 1) * alpha_N(N)


def ghost_contribution(s: int) -> Fraction:
    r"""Ghost central charge magnitude at conformal weight s.

    |c_bc(s)| = 2(6s^2 - 6s + 1), the absolute value of the bc ghost
    central charge at weight s.  The bc formula is c_bc(s) = 1 - 3(2s-1)^2
    = -(6s^2 - 6s + 1)*2, so |c_bc(s)| = 2(6s^2 - 6s + 1).

    # VERIFIED: s=2 -> 2(24 - 12 + 1) = 26 [DC]; matches c_bc(2) = -26 [C5].
    """
    if s < 1:
        raise ValueError(f"Conformal weight must be >= 1, got {s}")
    # VERIFIED: [DC] |1 - 3(2s-1)^2| = 2(6s^2-6s+1) by direct expansion;
    # [CF] s=2 gives 26, cancelling c_bc(2) = -26.
    # VERIFIED: [DC] the expanded ghost formula is 2(6s^2-6s+1); [CF] s=2 -> 26.
    return Fraction(2 * (6 * s**2 - 6 * s + 1))


def ghost_decomposition(N: int) -> list:
    r"""Ghost decomposition of alpha_N into weight-by-weight contributions.

    Returns [|c_bc(2)|, |c_bc(3)|, ..., |c_bc(N)|] where each entry is
    2(6s^2 - 6s + 1) for s = 2, 3, ..., N.

    The sum equals alpha_N(N).

    # VERIFIED: sum for N=2 is 26 = alpha_2 [DC];
    #           sum for N=3 is 26 + 74 = 100 = alpha_3 [DC].
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    # VERIFIED: [DC] weights run exactly through s=2,...,N;
    # [LC] N=3 produces the verified list [26, 74].
    # VERIFIED: [DC] the list runs over weights 2,...,N; [LC] N=3 gives [26, 74].
    return [ghost_contribution(s) for s in range(2, N + 1)]


def alpha_N_from_ghosts(N: int) -> Fraction:
    r"""Compute alpha_N via ghost decomposition sum.

    alpha_N = sum_{s=2}^{N} 2(6s^2 - 6s + 1).

    This provides an independent computation path for verification.

    # VERIFIED: matches alpha_N(N) for N = 2..10 [DC].
    """
    # VERIFIED: [DC] summing the weight-by-weight ghost magnitudes reproduces alpha_N;
    # [CF] agrees with the closed form 2(N-1)(2N^2+2N+1).
    # VERIFIED: [DC] summing the ghost terms reproduces alpha_N; [CF] it matches the closed form.
    return sum(ghost_decomposition(N))


def kappa_WN(N: int, c: Fraction) -> Fraction:
    r"""kappa(W_N) at central charge c: kappa = c * (H_N - 1).

    CAUTION (C4, AP136): H_N - 1, NOT H_{N-1}.
    At N=2: kappa = c * (H_2 - 1) = c * 1/2 = c/2 (matches Virasoro, C2).

    # VERIFIED: N=2, c=26 -> 13 [DC]; matches C2 [LT].
    """
    # VERIFIED: [DC] kappa(W_N,c) = c(H_N-1) by definition;
    # [CF] N=2 reduces to the Virasoro formula c/2.
    # VERIFIED: [DC] kappa(W_N,c) = c(H_N-1); [CF] N=2 reduces to c/2.
    return Fraction(c) * (H_N(N) - 1)


def verify_all(max_N: int = 10) -> dict:
    """Run all internal consistency checks up to W_{max_N}.

    Returns a dict of check names -> bool (True = passed).
    """
    results = {}

    # Check alpha values
    expected_alpha = {
        2: 26,   # VERIFIED: [DC] 2(N-1)(2N^2+2N+1)|_{N=2} = 26; [CF] W_2 = Vir so c+c' = 26.
        3: 100,  # VERIFIED: [DC] 2(N-1)(2N^2+2N+1)|_{N=3} = 100; [CF] ghost sum 26 + 74 = 100.
        4: 246,  # VERIFIED: [DC] 2(N-1)(2N^2+2N+1)|_{N=4} = 246; [CF] ghost sum 26 + 74 + 146 = 246.
        5: 488,  # VERIFIED: [DC] 2(N-1)(2N^2+2N+1)|_{N=5} = 488; [CF] self-dual point is c = 244 = alpha_5/2.
    }
    for n, val in expected_alpha.items():
        results[f"alpha_{n}={val}"] = (alpha_N(n) == Fraction(val))

    # Check ghost decomposition
    for n in range(2, max_N + 1):
        results[f"ghost_sum_{n}"] = (alpha_N_from_ghosts(n) == alpha_N(n))

    # Check K values
    expected_K = {
        2: Fraction(13),       # VERIFIED: [DC] (3/2 - 1) * 26 = 13; [CF] matches the Virasoro conductor.
        3: Fraction(250, 3),   # VERIFIED: [DC] (11/6 - 1) * 100 = 250/3; [CF] kappa(W_3,c) = 5c/6.
        4: Fraction(533, 2),   # VERIFIED: [DC] (25/12 - 1) * 246 = 533/2; [CF] kappa(W_4,c) = 13c/12.
        5: Fraction(9394, 15), # VERIFIED: [DC] (137/60 - 1) * 488 = 9394/15; [CF] kappa(W_5,c) = 77c/60.
    }
    for n, val in expected_K.items():
        results[f"K_{n}={val}"] = (K_WN(n) == val)

    # Check c_star
    for n in range(2, max_N + 1):
        results[f"c_star_{n}"] = (c_star(n) == alpha_N(n) / 2)

    # Check W_2 = Virasoro consistency
    # VERIFIED: [DC] K(W_2) = (H_2-1)alpha_2 = (1/2)*26 = 13;
    # [CF] W_2 is Virasoro, whose conductor is 13.
    results["K_W2=13_Vir"] = (K_WN(2) == Fraction(13))
    # VERIFIED: [DC] kappa(W_2,26) = 26*(H_2-1) = 13;
    # [CF] kappa(Vir_26) = 26/2 = 13.
    results["kappa_W2_c26=13"] = (kappa_WN(2, Fraction(26)) == Fraction(13))

    return results


if __name__ == "__main__":
    print("alpha_N conductor engine -- verification run")
    print("=" * 55)

    for n in range(2, 8):
        print(f"  W_{n}: alpha={alpha_N(n)}, c*={c_star(n)}, "
              f"K={K_WN(n)}, ghosts={ghost_decomposition(n)}")

    print()
    checks = verify_all()
    passed = sum(v for v in checks.values())
    total = len(checks)
    print(f"Internal checks: {passed}/{total} passed")
    for name, ok in checks.items():
        if not ok:
            print(f"  FAILED: {name}")
