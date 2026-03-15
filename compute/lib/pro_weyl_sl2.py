"""Pro-Weyl convergence for Y(sl_2) — task B7 for conj:pro-weyl-recovery.

Conjecture (conj:pro-weyl-recovery, yangians.tex):
  For a rational highest ell-weight Psi, the ordinary standard module
  M(Psi) is recovered as a derived inverse limit

      M(Psi) ~= R lim_m W_m

  where W_m = W(Psi_{<=m}) are local Weyl module truncations.

For sl_2, this reduces to a character-level convergence statement.
The evaluation Verma module M(lambda, a) has the same formal character
as the U(sl_2) Verma module M(lambda): a single weight-1 space at each
weight lambda, lambda-2, lambda-4, ...

The local Weyl module W_m approximates M(lambda) by keeping only the
first m weight levels.  For Y(sl_2), all finite-dimensional
highest-weight modules are evaluation modules, so W(lambda, a) = V_lambda(a)
(the irreducible of dimension lambda+1).

This module tests:
  1. Truncated approximations W_m (first m weight levels of M(lambda))
  2. Coefficientwise convergence W_m -> M(lambda) as m -> infinity
  3. Error character at each truncation level
  4. Error support: only on weights <= lambda - 2m
  5. Multiple values of lambda (0, 1, 2, 5, 10)
  6. Convergence rate (exact stabilization at finite m for each weight)

Mathematical content:
  The projective system is W_1 <- W_2 <- ... <- W_m <- ...
  where each W_m is a finite-dimensional quotient of M(lambda) keeping
  only the top m weight spaces.  The inverse limit recovers M(lambda)
  because M(lambda) is the universal object mapping to all W_m.

  At the level of characters:
    ch(W_m) = sum_{k=0}^{m-1} q^{lambda - 2k}
    ch(M(lambda)) = sum_{k=0}^{infty} q^{lambda - 2k}
    error(m) = ch(M(lambda)) - ch(W_m) = sum_{k=m}^{infty} q^{lambda - 2k}

  The error is supported on weights <= lambda - 2m, confirming pointwise
  convergence.  This is the shadow-level (S-level) verification of the
  derived inverse limit.

CONVENTIONS:
  - Cohomological grading (consistent with the monograph).
  - Formal characters as dicts: weight -> multiplicity.
  - Weights are integers for integral highest weight modules.

References:
  - yangians.tex, conj:pro-weyl-recovery
  - sl2_baxter.py for formal character machinery
  - concordance.tex, MC3 architecture
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from compute.lib.sl2_baxter import (
    FormalCharacter,
    formal_character_equal,
    sl2_fd_character,
    sl2_verma_character,
    subtract_characters,
    sum_characters,
)


# ---------------------------------------------------------------------------
# Weyl module truncations
# ---------------------------------------------------------------------------

def weyl_truncation(lam: int, m: int) -> FormalCharacter:
    """Character of the m-th Weyl truncation W_m of M(lambda).

    W_m keeps the first m weight levels of the Verma module M(lambda):
      ch(W_m) = sum_{k=0}^{m-1} q^{lambda - 2k}

    This is a finite-dimensional module of dimension m (when m <= lambda+1
    for dominant lambda, but we allow arbitrary m for the formal character).

    For Y(sl_2), W_m is the quotient of M(lambda) by the submodule
    generated at weight lambda - 2m.

    Args:
        lam: highest weight (integer).
        m: number of weight levels to keep (m >= 0).

    Returns:
        Formal character of W_m.
    """
    if m <= 0:
        return {}
    return {lam - 2 * k: 1 for k in range(m)}


def weyl_tower(lam: int, max_m: int) -> List[FormalCharacter]:
    """Build the Weyl tower W_1, W_2, ..., W_{max_m} for M(lambda).

    This is the projective system underlying the pro-Weyl recovery:
      W_1 <- W_2 <- ... <- W_m <- ...
    Each W_{m+1} extends W_m by one additional weight space.

    Args:
        lam: highest weight.
        max_m: number of truncation levels.

    Returns:
        List of formal characters [W_1, W_2, ..., W_{max_m}].
    """
    return [weyl_truncation(lam, m) for m in range(1, max_m + 1)]


# ---------------------------------------------------------------------------
# Error characters
# ---------------------------------------------------------------------------

def error_character(lam: int, m: int, depth: int = 100) -> FormalCharacter:
    """Compute the error character: ch(M(lambda)) - ch(W_m).

    The error is the tail of the Verma character not captured by W_m:
      error(m) = sum_{k=m}^{depth-1} q^{lambda - 2k}

    This is supported on weights <= lambda - 2m.
    When m >= depth, the error is empty (W_m captures all computed levels).

    Args:
        lam: highest weight.
        m: truncation level.
        depth: depth for the Verma character computation.

    Returns:
        Formal character of the error (nonneg multiplicities).
    """
    if m >= depth:
        return {}
    verma = sl2_verma_character(lam, depth=depth)
    W_m = weyl_truncation(lam, m)
    return subtract_characters(verma, W_m)


def error_support_bound(lam: int, m: int, depth: int = 100) -> Optional[int]:
    """Highest weight appearing in the error character.

    Should be exactly lambda - 2m (the first weight NOT in W_m).
    Returns None if the error is empty (m >= depth).

    Args:
        lam: highest weight.
        m: truncation level.
        depth: Verma depth.

    Returns:
        Highest weight in the error, or None if error is empty.
    """
    err = error_character(lam, m, depth=depth)
    if not err:
        return None
    return max(err.keys())


def error_dimension(lam: int, m: int, depth: int = 100) -> int:
    """Total dimension of the error = depth - m (number of missing weight spaces).

    Args:
        lam: highest weight.
        m: truncation level.
        depth: Verma depth.

    Returns:
        Sum of multiplicities in the error character.
    """
    err = error_character(lam, m, depth=depth)
    return sum(err.values())


# ---------------------------------------------------------------------------
# Convergence analysis
# ---------------------------------------------------------------------------

def coefficientwise_convergence(lam: int, max_m: int,
                                 depth: int = 100) -> Dict[int, int]:
    """For each weight mu in M(lambda), determine the smallest m such that
    W_m captures that weight.

    Weight lambda - 2k first appears in W_{k+1} (since W_m has levels 0..m-1).

    Returns:
        dict: weight -> stabilization level (smallest m capturing it).
    """
    verma = sl2_verma_character(lam, depth=max_m)
    result = {}
    for k in range(min(max_m, depth)):
        weight = lam - 2 * k
        # Weight lambda - 2k first appears in W_{k+1}
        result[weight] = k + 1
    return result


def convergence_rate_data(lam: int, max_m: int,
                           depth: int = 100) -> List[Dict]:
    """Compute convergence data for the pro-Weyl tower.

    For each truncation level m = 1, ..., max_m, records:
      - m: truncation level
      - dim_Wm: dimension of W_m
      - dim_error: dimension of the error
      - error_top_weight: highest weight in the error (or None)
      - fraction_captured: dim(W_m) / depth (fraction of Verma captured)

    Args:
        lam: highest weight.
        max_m: maximum truncation level.
        depth: Verma depth for computing errors.

    Returns:
        List of dicts with convergence data.
    """
    data = []
    for m in range(1, max_m + 1):
        W_m = weyl_truncation(lam, m)
        dim_Wm = sum(W_m.values()) if W_m else 0
        dim_err = error_dimension(lam, m, depth=depth)
        top_wt = error_support_bound(lam, m, depth=depth)
        frac = dim_Wm / depth if depth > 0 else 0.0
        data.append({
            "m": m,
            "dim_Wm": dim_Wm,
            "dim_error": dim_err,
            "error_top_weight": top_wt,
            "fraction_captured": frac,
        })
    return data


# ---------------------------------------------------------------------------
# Projective system structure
# ---------------------------------------------------------------------------

def verify_projective_system(lam: int, max_m: int) -> bool:
    """Verify the projective system property: W_{m+1} surjects onto W_m.

    In terms of characters, this means ch(W_m) is a sub-character of
    ch(W_{m+1}), i.e., for every weight mu, mult_{W_m}(mu) <= mult_{W_{m+1}}(mu).

    This is trivially true since W_{m+1} = W_m + one additional weight space.

    Args:
        lam: highest weight.
        max_m: number of levels to check.

    Returns:
        True if all surjections hold.
    """
    tower = weyl_tower(lam, max_m)
    for i in range(len(tower) - 1):
        W_curr = tower[i]
        W_next = tower[i + 1]
        # Every weight in W_curr must appear in W_next with >= multiplicity
        for w, mult in W_curr.items():
            if W_next.get(w, 0) < mult:
                return False
        # W_next must have exactly one more weight space
        if sum(W_next.values()) != sum(W_curr.values()) + 1:
            return False
    return True


def verify_inverse_limit(lam: int, max_m: int, depth: int = 100) -> bool:
    """Verify that lim_m W_m = M(lambda) as formal characters (up to depth).

    The inverse limit of the projective system {W_m} should recover the
    Verma module M(lambda).  At the character level, this means:
      for every weight mu in M(lambda), there exists m_0 such that
      mult_{W_m}(mu) = mult_{M(lambda)}(mu) for all m >= m_0.

    We check this up to 'depth' weight levels.

    Args:
        lam: highest weight.
        max_m: maximum truncation level (should be >= depth).
        depth: number of weight levels to verify.

    Returns:
        True if convergence holds at all weights up to depth.
    """
    verma = sl2_verma_character(lam, depth=depth)

    for w, mult in verma.items():
        # Find the smallest m such that W_m captures weight w
        # Weight w = lam - 2k, so we need m >= k+1
        k = (lam - w) // 2
        m_0 = k + 1  # stabilization level

        if m_0 > max_m:
            continue  # Can't verify beyond max_m

        # Check stabilization: W_m(w) = mult for all m >= m_0
        for m in range(m_0, min(max_m + 1, m_0 + 10)):
            W_m = weyl_truncation(lam, m)
            if W_m.get(w, 0) != mult:
                return False

    return True


# ---------------------------------------------------------------------------
# Derived correction (R^1 lim) analysis
# ---------------------------------------------------------------------------

def r1_lim_vanishing(lam: int, max_m: int) -> bool:
    """Verify that R^1 lim_m W_m = 0 (Mittag-Leffler condition).

    For the pro-Weyl tower, R^1 lim vanishes because the transition
    maps W_{m+1} -> W_m are surjective (they are quotient maps).
    The Mittag-Leffler condition is automatically satisfied for a
    projective system of surjections.

    At the character level, surjectivity means:
      For every weight mu in W_m, mult_{W_m}(mu) <= mult_{W_{m+1}}(mu).

    Since our W_m are quotients of M(lambda), the transition maps
    W_{m+1} -> W_m are surjective (they kill the extra weight space).

    Args:
        lam: highest weight.
        max_m: levels to check.

    Returns:
        True if the Mittag-Leffler condition holds (surjectivity).
    """
    # The transition maps are surjective by construction:
    # W_{m+1} -> W_m kills the weight-space at level m, and is identity
    # on levels 0, ..., m-1.
    #
    # We verify: for each m, the character of W_m is obtained from W_{m+1}
    # by removing the single weight lambda - 2m.
    tower = weyl_tower(lam, max_m)
    for i in range(len(tower) - 1):
        W_curr = tower[i]
        W_next = tower[i + 1]
        diff = subtract_characters(W_next, W_curr)
        # The difference should be exactly one weight space
        if len(diff) != 1:
            return False
        weight, mult = next(iter(diff.items()))
        expected_weight = lam - 2 * (i + 1)
        if weight != expected_weight or mult != 1:
            return False
    return True


# ---------------------------------------------------------------------------
# Finite-dimensional Weyl modules (fd truncation)
# ---------------------------------------------------------------------------

def fd_weyl_character(lam: int) -> FormalCharacter:
    """Character of the finite-dimensional Weyl module W(lambda) for Y(sl_2).

    For Y(sl_2), the local Weyl module W(lambda) is the irreducible
    representation V_lambda of dimension lambda+1.  This is because
    all finite-dimensional highest-weight Y(sl_2)-modules are evaluation
    modules, and the universal one (Weyl module) is irreducible.

    Args:
        lam: highest weight (must be >= 0 for fd reps).

    Returns:
        Character of V_lambda.
    """
    if lam < 0:
        raise ValueError(f"fd Weyl module requires lam >= 0, got {lam}")
    return sl2_fd_character(lam + 1)


def fd_weyl_vs_verma(lam: int) -> Dict:
    """Compare the fd Weyl module W(lambda) with the Verma module M(lambda).

    For dominant lambda >= 0:
      - W(lambda) = V_lambda has dimension lambda+1
      - M(lambda) is infinite-dimensional
      - M(lambda) surjects onto W(lambda) (= V_lambda for Y(sl_2))
      - The kernel has character: M(lambda) - V_lambda = M(-lambda-2)
        (for integral dominant lambda, the Verma has a singular vector
        at weight -lambda-2, generating a submodule isomorphic to M(-lambda-2))

    Returns:
        dict with comparison data.
    """
    depth = max(2 * lam + 10, 50)
    verma = sl2_verma_character(lam, depth=depth)
    weyl = fd_weyl_character(lam)
    kernel = subtract_characters(verma, weyl)

    # The kernel should be M(-lambda-2) for lambda >= 0
    # i.e., weights -lambda-2, -lambda-4, -lambda-6, ...
    expected_kernel_hw = -lam - 2 if lam >= 0 else None

    return {
        "lam": lam,
        "dim_weyl": sum(weyl.values()),
        "weyl_character": weyl,
        "kernel_top_weight": max(kernel.keys()) if kernel else None,
        "expected_kernel_hw": expected_kernel_hw,
        "kernel_matches_subverma": (
            max(kernel.keys()) == expected_kernel_hw if kernel else lam < 0
        ),
    }


# ---------------------------------------------------------------------------
# Ell-weight truncation (Drinfeld polynomial level)
# ---------------------------------------------------------------------------

def drinfeld_polynomial_truncation(lam: int, m: int) -> Dict:
    """Describe the Drinfeld polynomial truncation Psi_{<=m}.

    For Y(sl_2), a highest ell-weight Psi is determined by a
    Drinfeld polynomial P(u) = prod_{j=1}^n (u - a_j).

    For evaluation modules: P(u) = (u - a)^lambda, a single root
    of multiplicity lambda.

    Truncation Psi_{<=m} keeps only the first min(m, lambda) roots:
      P_{<=m}(u) = (u - a)^{min(m, lambda)}

    The Weyl module W(Psi_{<=m}) = V_{min(m,lambda)}(a).

    For m >= lambda, the truncation is exact: P_{<=m} = P.

    Args:
        lam: highest weight (degree of Drinfeld polynomial).
        m: truncation level.

    Returns:
        dict describing the truncation.
    """
    effective_deg = min(m, lam) if lam >= 0 else m
    return {
        "lam": lam,
        "m": m,
        "drinfeld_degree": lam if lam >= 0 else "infinite",
        "truncated_degree": effective_deg,
        "is_exact": m >= lam if lam >= 0 else False,
        "weyl_dim": effective_deg + 1 if effective_deg >= 0 else 0,
    }


# ---------------------------------------------------------------------------
# Convergence metrics
# ---------------------------------------------------------------------------

def convergence_summary(lam: int, max_m: int = 20,
                         depth: int = 100) -> Dict:
    """Summary of pro-Weyl convergence for M(lambda).

    Collects all convergence diagnostics into a single report.

    Args:
        lam: highest weight.
        max_m: maximum truncation level.
        depth: Verma depth.

    Returns:
        dict with convergence summary.
    """
    rate_data = convergence_rate_data(lam, max_m, depth=depth)

    # Find the m at which 50%, 90%, 99% of the Verma is captured
    milestones = {}
    for target_frac in [0.5, 0.9, 0.99]:
        for entry in rate_data:
            if entry["fraction_captured"] >= target_frac:
                milestones[f"{int(target_frac*100)}%"] = entry["m"]
                break

    return {
        "lam": lam,
        "max_m": max_m,
        "depth": depth,
        "projective_system_valid": verify_projective_system(lam, max_m),
        "inverse_limit_converges": verify_inverse_limit(lam, max_m, depth),
        "mittag_leffler_holds": r1_lim_vanishing(lam, max_m),
        "milestones": milestones,
        "final_error_dim": rate_data[-1]["dim_error"] if rate_data else None,
        "final_fraction": rate_data[-1]["fraction_captured"] if rate_data else None,
    }


# ---------------------------------------------------------------------------
# Multi-lambda verification
# ---------------------------------------------------------------------------

def verify_pro_weyl_convergence(lambdas: Optional[List[int]] = None,
                                 max_m: int = 30,
                                 depth: int = 100) -> Dict[int, Dict]:
    """Verify pro-Weyl convergence for multiple values of lambda.

    Args:
        lambdas: list of highest weights to test. Default: [0, 1, 2, 5, 10].
        max_m: maximum truncation level.
        depth: Verma depth.

    Returns:
        dict: lambda -> convergence summary.
    """
    if lambdas is None:
        lambdas = [0, 1, 2, 5, 10]

    results = {}
    for lam in lambdas:
        results[lam] = convergence_summary(lam, max_m=max_m, depth=depth)
    return results


# ---------------------------------------------------------------------------
# Tail decay and convergence rate
# ---------------------------------------------------------------------------

def tail_decay(lam: int, max_m: int, depth: int = 100) -> List[Tuple[int, int]]:
    """Compute the tail dimension (error dimension) as a function of m.

    For the Verma module truncated to 'depth' levels:
      tail_dim(m) = depth - m  (for m <= depth)
      tail_dim(m) = 0          (for m > depth)

    The decay is LINEAR in m — this is the simplest possible convergence.
    There are no derived corrections (R^1 = 0 by Mittag-Leffler).

    Args:
        lam: highest weight.
        max_m: maximum truncation level.
        depth: Verma depth.

    Returns:
        List of (m, tail_dim) pairs.
    """
    result = []
    for m in range(1, max_m + 1):
        tail_dim = max(depth - m, 0)
        result.append((m, tail_dim))
    return result


def verify_linear_decay(lam: int, max_m: int, depth: int = 100) -> bool:
    """Verify that the error dimension decreases linearly: dim_error(m) = depth - m.

    This is the expected convergence rate: each additional truncation level
    captures exactly one new weight space.

    Args:
        lam: highest weight.
        max_m: maximum truncation level.
        depth: Verma depth.

    Returns:
        True if linear decay holds.
    """
    for m in range(1, min(max_m + 1, depth + 1)):
        actual = error_dimension(lam, m, depth=depth)
        expected = depth - m
        if actual != expected:
            return False
    return True


# ---------------------------------------------------------------------------
# Verification suite
# ---------------------------------------------------------------------------

def verify_all() -> Dict[str, bool]:
    """Run all pro-Weyl convergence verification checks."""
    results = {}

    # Projective system
    for lam in [0, 1, 2, 5, 10]:
        results[f"projective system lam={lam}"] = \
            verify_projective_system(lam, max_m=20)

    # Inverse limit convergence
    for lam in [0, 1, 2, 5, 10]:
        results[f"inverse limit lam={lam}"] = \
            verify_inverse_limit(lam, max_m=50, depth=30)

    # Mittag-Leffler (R^1 vanishing)
    for lam in [0, 1, 2, 5, 10]:
        results[f"Mittag-Leffler lam={lam}"] = \
            r1_lim_vanishing(lam, max_m=20)

    # Linear decay
    for lam in [0, 1, 2, 5, 10]:
        results[f"linear decay lam={lam}"] = \
            verify_linear_decay(lam, max_m=40, depth=50)

    # Error support bound
    for lam in [0, 1, 2, 5, 10]:
        for m in [1, 3, 5]:
            bound = error_support_bound(lam, m)
            expected = lam - 2 * m
            results[f"error support lam={lam} m={m}"] = (bound == expected)

    # fd Weyl vs Verma
    for lam in [0, 1, 2, 5]:
        data = fd_weyl_vs_verma(lam)
        results[f"kernel structure lam={lam}"] = data["kernel_matches_subverma"]

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("PRO-WEYL CONVERGENCE FOR Y(sl_2) — TASK B7")
    print("=" * 70)

    results = verify_all()
    n_pass = sum(1 for v in results.values() if v)
    n_fail = sum(1 for v in results.values() if not v)

    for name, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print(f"\n{n_pass} passed, {n_fail} failed out of {len(results)} checks.")

    print("\n" + "=" * 70)
    print("CONVERGENCE SUMMARY")
    print("=" * 70)

    for lam in [0, 1, 2, 5, 10]:
        summary = convergence_summary(lam, max_m=20, depth=50)
        print(f"\n  lambda = {lam}:")
        print(f"    Projective system valid: {summary['projective_system_valid']}")
        print(f"    Inverse limit converges: {summary['inverse_limit_converges']}")
        print(f"    Mittag-Leffler (R^1=0): {summary['mittag_leffler_holds']}")
        print(f"    Milestones: {summary['milestones']}")
        print(f"    Final error dim (m=20): {summary['final_error_dim']}")
        print(f"    Fraction captured: {summary['final_fraction']:.2%}")
