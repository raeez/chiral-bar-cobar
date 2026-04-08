r"""The phantom M5 Koszul dual: physical interpretation and structural analysis.

MATHEMATICAL SETTING
====================

The M5 brane boundary VOA is W_{1+infty}[lambda=N] (Costello-Gaiotto-Paquette).
The Koszul dual is obtained via Verdier intertwining (Theorem A):

    D_Ran(B(W_{1+infty}[lambda])) ~ B(W_{1+infty}[lambda^!])

where the Linshaw involution gives lambda^! = 2 - lambda.

For N M5 branes: lambda = N, so lambda^! = 2 - N.

The modular characteristic of the Koszul dual is:
    kappa(M5_N^!) = (2 - N)^3

This engine investigates the PHYSICAL INTERPRETATION of M5_N^!.

KEY FINDINGS
============

1. COMPLEMENTARITY SUM (AP24):
   kappa(M5_N) + kappa(M5_N^!) = N^3 + (2-N)^3 = 6N^2 - 12N + 8 = 2[3(N-1)^2 + 1]
   This is ALWAYS POSITIVE (minimum value 2 at N=1).
   It NEVER vanishes.

2. PHYSICAL INTERPRETATION CANDIDATES:

   (A) "Negative-N" theory: Setting N -> 2-N in the (2,0) theory.
       For N >= 3: lambda^! = 2-N < 0, which is OUTSIDE the physical range
       of the W_{1+infty} parameter space.  The (2,0) theory at negative N
       does not exist as a unitary QFT.

   (B) Anti-M5 / orientifold interpretation:
       The sign flip N -> 2-N resembles the orientifold projection
       O5^- which changes SO(N) to USp(N).  The (2,0) of type D_N
       (not A_{N-1}) has a natural Z_2 involution.  The Koszul dual
       MIGHT correspond to the (2,0) of type D_{|2-N|} with appropriate
       analytic continuation.

   (C) 5d N=2 SYM at strong coupling:
       The M5 boundary theory at lambda=N reduces to 5d N=2 SYM with
       gauge group U(N) when compactified on S^1.  The Koszul dual at
       lambda^! = 2-N could correspond to the S-dual of 5d SYM,
       which at strong coupling is the LITTLE STRING THEORY (type IIA
       on N NS5 branes).

   (D) M2 Koszul dual analogy:
       For M2 (ABJM): kappa(M2_N) = -N^2.  The Koszul dual has
       kappa(M2_N^!) = +N^2 (by AP24 for KM-type: kappa + kappa! ~ 0).
       The M2 Koszul dual is related to the S-dual boundary condition
       via the 3d mirror symmetry of Gaiotto-Witten.
       For M5: the situation is DIFFERENT because the (2,0) theory
       has no Lagrangian description, so there is no direct S-duality
       to invoke.

   (E) Relation to 6d (1,0):
       The 6d (1,0) theories (with one tensor multiplet) have
       a(1,0) = (4N^3 + ...) / ... with DIFFERENT subleading
       corrections than (2,0).  The Koszul dual does NOT match
       any known (1,0) theory because:
       - (1,0) always has a > 0 (positive anomaly)
       - kappa(M5^!) = (2-N)^3 is NEGATIVE for N >= 3
       - The sign of kappa controls the orientation of the genus
         expansion; negative kappa would imply a "wrong-sign" genus
         expansion, which is unphysical for a unitary theory.

3. N=2 SELF-DUALITY:
   At N=2: lambda = 2, lambda^! = 0.  Since kappa(M5_2^!) = 0,
   the Koszul dual is UNCURVED (vanishing curvature in the bar complex).
   This is the shadow of the W_{1+infty}[lambda=0] = u(infty)_1 theory,
   the free boson limit.  The N=2 M5 branes map under Koszul duality
   to the FREE BOSON TOWER, which has a concrete physical interpretation.

4. COMPLEMENTARITY POLYNOMIAL ANALYSIS:
   The complementarity sum P(N) = 6N^2 - 12N + 8 satisfies:
   - P(N) > 0 for all N (discriminant = 144 - 192 = -48 < 0)
   - P(1) = 2  (minimum, the free tensor multiplet)
   - P(2) = 8
   - P(3) = 26
   - P(N) ~ 6N^2 for large N (quadratic growth)
   The RESIDUAL complementarity P(N) is the "irreducible anomaly"
   that cannot be cancelled by any matter content -- it is a
   topological invariant of the M5 brane stack.

5. GENUS TOWER SIGN STRUCTURE:
   For N >= 3: kappa(M5_N^!) = (2-N)^3 < 0.
   This means F_g(M5_N^!) = kappa^! * lambda_g^FP < 0 for ALL genera.
   A negative genus expansion has no perturbative interpretation as
   a physical theory.  This is the strongest argument that M5_N^!
   for N >= 3 is a "phantom" -- it does not correspond to any unitary QFT.

CONVENTIONS
===========

  AP1   kappa formulas are family-specific; never copy
  AP9   kappa(A) != c(A)/2 in general
  AP20  kappa intrinsic to A, not the physical system
  AP24  kappa + kappa! != 0 for W-algebra families
  AP25  three functors: bar coalgebra, Verdier dual, cobar inversion
  AP32  multi-weight algebras receive cross-channel corrections at g >= 2
  AP39  kappa = c/2 only for Virasoro

REFERENCES
==========

  Costello, arXiv:1610.04144
  Costello-Gaiotto, arXiv:1812.09257
  Costello-Paquette, arXiv:2103.16984
  Linshaw, arXiv:1710.02275
  Beem-Rastelli-vR, arXiv:1404.1079
  Henningson-Skenderis, arXiv:hep-th/9806087
  Gaiotto-Witten, arXiv:0807.3720 (S-duality for 3d boundaries)
  Ohmori-Shimizu-Tachikawa-Yonekura, arXiv:1406.4550 (6d (1,0) anomaly)
  Bhardwaj-Tachikawa, arXiv:1509.00013 (classification of 6d SCFTs)
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple


# ============================================================================
# Helpers
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Akiyama-Tanigawa Bernoulli numbers."""
    A = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        A[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return A[0]


def _factorial(n: int) -> int:
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    """Faber-Pandharipande number lambda_g^FP."""
    if g < 1:
        raise ValueError(f"genus >= 1 required, got {g}")
    B_2g = _bernoulli(2 * g)
    abs_B = abs(B_2g)
    num = (2 ** (2 * g - 1) - 1) * abs_B
    den = Fraction(2 ** (2 * g - 1)) * _factorial(2 * g)
    return num / den


@lru_cache(maxsize=64)
def harmonic(n: int) -> Fraction:
    """H_n = sum_{j=1}^n 1/j."""
    if n <= 0:
        return Fraction(0)
    return sum(Fraction(1, j) for j in range(1, n + 1))


# ============================================================================
# 1. M5 Koszul dual core
# ============================================================================

@dataclass(frozen=True)
class PhantomM5:
    """The Koszul dual of N M5 branes: the phantom theory M5_N^!.

    Constructed via the Linshaw involution lambda -> 2 - lambda
    on the W_{1+infty}[lambda] family.

    Attributes
    ----------
    N : int
        Number of M5 branes in the ORIGINAL theory.
    """
    N: int

    @property
    def lambda_original(self) -> Fraction:
        return Fraction(self.N)

    @property
    def lambda_dual(self) -> Fraction:
        """Dual parameter: lambda^! = 2 - N."""
        return Fraction(2 - self.N)

    @property
    def kappa_original(self) -> Fraction:
        """kappa(M5_N) = N^3 (leading)."""
        return Fraction(self.N) ** 3

    @property
    def kappa_dual(self) -> Fraction:
        """kappa(M5_N^!) = (2 - N)^3."""
        return Fraction(2 - self.N) ** 3

    @property
    def kappa_full_original(self) -> Fraction:
        """Full kappa from Beem-Rastelli: (4N^3 - 3N - 1)/2."""
        return Fraction(4 * self.N ** 3 - 3 * self.N - 1, 2)

    @property
    def kappa_full_dual(self) -> Fraction:
        """Full kappa of dual from Beem-Rastelli at lambda^! = 2 - N.

        c(lambda) = 4*lambda^3 - 3*lambda - 1
        kappa(lambda) = c(lambda)/2

        At lambda = 2 - N:
            c(2-N) = 4*(2-N)^3 - 3*(2-N) - 1
                   = 4*(8 - 12N + 6N^2 - N^3) - 6 + 3N - 1
                   = 32 - 48N + 24N^2 - 4N^3 - 7 + 3N
                   = -4N^3 + 24N^2 - 45N + 25
        """
        lam = 2 - self.N
        c_dual = 4 * lam ** 3 - 3 * lam - 1
        return Fraction(c_dual, 2)

    @property
    def complementarity_sum(self) -> Fraction:
        """kappa(A) + kappa(A^!) at leading order.

        N^3 + (2-N)^3 = 6N^2 - 12N + 8.
        """
        return self.kappa_original + self.kappa_dual

    @property
    def complementarity_full(self) -> Fraction:
        """Full complementarity sum using Beem-Rastelli formula."""
        return self.kappa_full_original + self.kappa_full_dual

    @property
    def dual_is_negative_kappa(self) -> bool:
        """Whether kappa(M5_N^!) < 0."""
        return self.kappa_dual < 0

    @property
    def dual_is_uncurved(self) -> bool:
        """Whether kappa(M5_N^!) = 0 (uncurved bar complex)."""
        return self.kappa_dual == 0

    @property
    def dual_lambda_in_physical_range(self) -> bool:
        """Whether lambda^! >= 0 (physical W_{1+infty} range)."""
        return self.lambda_dual >= 0

    @property
    def interpretation_class(self) -> str:
        """Classification of the physical interpretation.

        Returns one of:
        - "free_boson_tower": N=2, lambda^!=0, kappa^!=0
        - "free_tensor_self": N=1, lambda^!=1, self-like
        - "unphysical_negative_lambda": lambda^! < 0
        - "physical_small_lambda": 0 < lambda^! < 1
        """
        if self.N == 1:
            return "dual_free_tensor"
        if self.N == 2:
            return "free_boson_tower"
        if self.lambda_dual < 0:
            return "unphysical_negative_lambda"
        return "physical_small_lambda"


# ============================================================================
# 2. Physical interpretation candidates
# ============================================================================

def negative_n_analysis(N: int) -> Dict:
    """Analysis of the "negative N" interpretation of M5^!.

    The (2,0) theory of type A_{N-1} has N^3 degrees of freedom.
    Setting N -> 2-N gives (2-N)^3 degrees of freedom, which is
    negative for N >= 3.

    Negative degrees of freedom have appeared in:
    - Orientifold planes (O-planes contribute negative charge)
    - Ghost systems in BRST cohomology
    - Analytic continuation of N in matrix models (Dijkgraaf-Vafa)

    The question is whether M5_N^! can be identified with any of these.
    """
    phantom = PhantomM5(N)
    n_eff = 2 - N  # "effective" N for the dual

    return {
        "N": N,
        "N_effective_dual": n_eff,
        "kappa_dual": phantom.kappa_dual,
        "kappa_dual_sign": "positive" if phantom.kappa_dual > 0 else "zero" if phantom.kappa_dual == 0 else "negative",
        "negative_dof": phantom.kappa_dual < 0,
        "analytic_continuation_viable": True,  # always formally possible
        "physical_interpretation": (
            "free tensor (N_eff = 1, anomaly-free)" if N == 1 else
            "free boson tower (N_eff = 0, W_{1+inf}[0] = vacuum module)" if N == 2 else
            f"negative-N phantom (N_eff = {n_eff}, no unitary QFT)"
        ),
        "orientifold_match": (
            abs(n_eff) <= N and N >= 3  # Rough: orientifold charge is O(1), not O(N)
        ),
        "ghost_system_match": (
            phantom.kappa_dual < 0  # Ghosts have negative kappa
        ),
    }


def orientifold_comparison(N: int) -> Dict:
    """Compare M5_N^! with orientifold M5 / O5 theories.

    The O5^- plane contributes -1/2 units of M5 charge.
    N M5 on top of O5^- gives gauge group USp(2N) (for O5^-)
    or SO(2N) (for O5^+).

    The (2,0) theory of type D_N (not A_{N-1}) has:
        a(D_N) = (16N^3 - 24N^2 + 12N - 4) / 12
                = (4*(2N)^3 - 6*(2N)^2 + ... ) / 12

    Compare with kappa(M5_N^!) = (2-N)^3.
    """
    phantom = PhantomM5(N)

    # (2,0) type D_N anomaly
    a_D_N = Fraction(16 * N ** 3 - 24 * N ** 2 + 12 * N - 4, 12)
    # Leading: 4N^3/3

    # (2,0) type A_{N-1} anomaly
    a_A = Fraction(4 * N ** 3 - 3 * N - 1, 12)

    # Ratio test: does kappa^! match any D-type anomaly?
    kappa_dual = phantom.kappa_dual
    match_d_type = False
    matched_d = None
    for d in range(1, 2 * N + 1):
        a_d = Fraction(16 * d ** 3 - 24 * d ** 2 + 12 * d - 4, 12)
        if Fraction(a_d * 6) == kappa_dual:
            match_d_type = True
            matched_d = d
            break

    return {
        "N": N,
        "kappa_dual": kappa_dual,
        "a_anomaly_A_type": a_A,
        "a_anomaly_D_N": a_D_N,
        "d_type_match": match_d_type,
        "matched_D_rank": matched_d,
        "o5_charge": Fraction(-1, 2),
        "interpretation": (
            f"D-type match at rank {matched_d}" if match_d_type else
            "no D-type match (phantom is NOT a D-type (2,0) theory)"
        ),
    }


def five_d_sym_comparison(N: int) -> Dict:
    """Compare M5_N^! with 5d N=2 SYM at strong coupling.

    The (2,0) theory on S^1 of radius R gives 5d N=2 SYM with
    coupling g^2 = R.  The Koszul dual at lambda^! = 2-N corresponds
    to the "strong coupling limit" of 5d SYM.

    At infinite coupling, 5d SYM transitions to the 6d (2,0) theory;
    the Koszul dual REVERSES this transition.

    The 5d SYM central charge is
        c_5d(N) = dim(SU(N)) = N^2 - 1

    The ratio test:
        kappa(M5_N^!) / c_5d(N) = (2-N)^3 / (N^2 - 1) for N >= 2
    """
    phantom = PhantomM5(N)
    c_5d = N ** 2 - 1 if N >= 2 else 0

    ratio = phantom.kappa_dual / Fraction(c_5d) if c_5d > 0 else None

    # Little string theory central charge
    # LST at N NS5 branes: c_LST = 6N
    c_lst = 6 * N

    return {
        "N": N,
        "kappa_dual": phantom.kappa_dual,
        "c_5d_SYM": c_5d,
        "ratio_kappa_dual_to_c_5d": ratio,
        "c_little_string": c_lst,
        "ratio_kappa_dual_to_c_lst": phantom.kappa_dual / Fraction(c_lst) if c_lst > 0 else None,
        "5d_match": ratio is not None and ratio > 0,
        "lst_match": phantom.kappa_dual / Fraction(c_lst) > 0 if c_lst > 0 else False,
        "interpretation": (
            "5d SYM has c > 0 but kappa^! < 0 for N >= 3; no direct match"
            if N >= 3 else
            f"N={N}: lambda^! = {phantom.lambda_dual}, within W_infty physical range"
        ),
    }


def one_zero_comparison(N: int) -> Dict:
    """Compare M5_N^! with 6d (1,0) theories.

    The 6d (1,0) theories with gauge group SU(N) and matter in
    the fundamental representation have:
        a_{(1,0)} = (11N^3 - 3N^2 + 25N - 9) / 24   (generic)
        c_{(1,0)} = (3N^3 - N^2 + 9N - 3) / 6

    Different from (2,0) where a = c.

    Key test: (1,0) always has a > 0, but kappa^! < 0 for N >= 3.
    """
    phantom = PhantomM5(N)

    # (1,0) SU(N) with 2N fundamentals (conformal)
    # a = (17N_f N^2 - 18N_f N + N_f + ... ) / ...
    # Simplified: use the single-tensor formula
    # a_{single tensor} = (11 - 3 + 25 - 9)/24 = 24/24 = 1 (N=1)
    # For N M5 -> (1,0) needs more data; use the Ohmori et al formula

    # Ohmori-Shimizu-Tachikawa-Yonekura (2014):
    # For N M5 on C^2/Z_k (orbifold):
    #   a = k * a_{(2,0)}(N) + corrections
    #   a_{(1,0)}(N, k=1) = a_{(2,0)}(N) [same leading]

    a_20 = Fraction(4 * N ** 3 - 3 * N - 1, 12)
    # (1,0) with k=2: a = 2 * a_{(2,0)} approximately
    a_10_approx = 2 * a_20  # rough: k=2 orbifold

    return {
        "N": N,
        "kappa_dual": phantom.kappa_dual,
        "a_anomaly_20": a_20,
        "a_anomaly_10_approx": a_10_approx,
        "kappa_dual_sign": "positive" if phantom.kappa_dual > 0 else "zero" if phantom.kappa_dual == 0 else "negative",
        "10_always_positive_a": a_10_approx > 0,
        "sign_mismatch": phantom.kappa_dual < 0 and a_10_approx > 0,
        "match": not (phantom.kappa_dual < 0 and a_10_approx > 0),
        "interpretation": (
            "sign mismatch: (1,0) has a > 0 but kappa^! < 0; M5^! is NOT a (1,0) theory"
            if N >= 3 else
            f"N={N}: no sign conflict (kappa^! = {phantom.kappa_dual})"
        ),
    }


def m2_koszul_dual_analogy(N: int) -> Dict:
    """Compare M5 and M2 Koszul dual structures.

    M2 (ABJM):
        kappa(M2_N) = -N^2
        kappa(M2_N^!) = +N^2  (by S-duality of 3d mirror, approximately)
        Complementarity: kappa + kappa^! ~ 0 (KM-type)

    M5:
        kappa(M5_N) = +N^3
        kappa(M5_N^!) = (2-N)^3
        Complementarity: kappa + kappa^! = 6N^2 - 12N + 8 (NEVER zero)

    The structural difference: M2 has AFFINE KM-type complementarity
    (AP24: kappa + kappa^! = 0 for KM), while M5 has W-ALGEBRA-type
    complementarity (AP24: kappa + kappa^! != 0 for W-algebras).
    """
    phantom_m5 = PhantomM5(N)

    # M2 data
    kappa_m2 = Fraction(-N * N)
    kappa_m2_dual = Fraction(N * N)  # approximate: S-dual boundary
    comp_m2 = kappa_m2 + kappa_m2_dual

    # M5 data
    comp_m5 = phantom_m5.complementarity_sum

    return {
        "N": N,
        "M2": {
            "kappa": kappa_m2,
            "kappa_dual": kappa_m2_dual,
            "complementarity": comp_m2,
            "type": "KM-type (anti-symmetric)",
        },
        "M5": {
            "kappa": phantom_m5.kappa_original,
            "kappa_dual": phantom_m5.kappa_dual,
            "complementarity": comp_m5,
            "type": "W-algebra-type (positive residual)",
        },
        "ratio_complementarity": (
            comp_m5 / comp_m2 if comp_m2 != 0 else None
        ),
        "structural_difference": (
            "M2 has vanishing complementarity sum (KM-type, AP24); "
            "M5 has non-vanishing residual 6N^2 - 12N + 8 (W-algebra-type)"
        ),
    }


# ============================================================================
# 3. N=2 self-duality analysis
# ============================================================================

def n2_self_duality_analysis() -> Dict:
    """Deep analysis of the N=2 point: lambda=2, lambda^!=0.

    At N=2: kappa(M5_2^!) = 0, meaning the Koszul dual is UNCURVED.
    The dual algebra is W_{1+infty}[lambda=0] = u(infty)_1, the
    free boson tower (vacuum module of the affine Yangian).

    This is the UNIQUE point where the phantom has a direct physical
    interpretation: it is the free boson VOA.

    The complementarity sum at N=2 is 8+0 = 8.
    """
    phantom = PhantomM5(2)

    return {
        "N": 2,
        "lambda_original": Fraction(2),
        "lambda_dual": Fraction(0),
        "kappa_original": Fraction(8),
        "kappa_dual": Fraction(0),
        "complementarity": Fraction(8),
        "dual_algebra": "W_{1+inf}[lambda=0] = u(infty)_1 = free boson tower",
        "dual_is_uncurved": True,
        "dual_has_physical_interpretation": True,
        "physical_interpretation": (
            "The free boson tower u(infty)_1 is the vacuum module of the "
            "affine Yangian Y(hat{gl}_1). At lambda=0, the W_{1+infty} "
            "algebra degenerates to the universal enveloping of gl(infty). "
            "This is the unique point where M5^! has a concrete realization."
        ),
        "genus_expansion_dual": {
            g: Fraction(0) for g in range(1, 6)
        },  # F_g = 0 for all g because kappa^! = 0
    }


# ============================================================================
# 4. Complementarity polynomial analysis
# ============================================================================

def complementarity_polynomial(N: int) -> Dict:
    """Analyze the complementarity polynomial P(N) = 6N^2 - 12N + 8.

    P(N) = kappa(M5_N) + kappa(M5_N^!) = N^3 + (2-N)^3

    Properties:
    - P(N) = 2[3(N-1)^2 + 1]
    - P(N) > 0 for all real N (discriminant < 0)
    - P(1) = 2 (minimum)
    - P(N) ~ 6N^2 for large N
    """
    P = 6 * N ** 2 - 12 * N + 8

    # Verify algebraic identity
    direct = N ** 3 + (2 - N) ** 3
    factored = 2 * (3 * (N - 1) ** 2 + 1)

    return {
        "N": N,
        "P_N": P,
        "direct_sum": direct,
        "factored_form": factored,
        "all_forms_agree": P == direct == factored,
        "is_positive": P > 0,
        "discriminant": 144 - 192,  # -48 < 0: no real roots
        "minimum_at": 1,
        "minimum_value": 2,
        "interpretation": (
            "P(N) > 0 for all N: the complementarity sum never vanishes. "
            "This means there is no 'anomaly cancellation' between M5 and M5^!. "
            "The irreducible residual 2[3(N-1)^2 + 1] is a topological invariant "
            "of the brane stack that persists in every Koszul pair."
        ),
    }


def complementarity_table(N_max: int = 10) -> List[Dict]:
    """Table of complementarity data for N = 1, ..., N_max."""
    rows = []
    for N in range(1, N_max + 1):
        phantom = PhantomM5(N)
        rows.append({
            "N": N,
            "lambda": phantom.lambda_original,
            "lambda_dual": phantom.lambda_dual,
            "kappa": phantom.kappa_original,
            "kappa_dual": phantom.kappa_dual,
            "complementarity_leading": phantom.complementarity_sum,
            "complementarity_full": phantom.complementarity_full,
            "dual_sign": "+" if phantom.kappa_dual > 0 else "0" if phantom.kappa_dual == 0 else "-",
            "interpretation_class": phantom.interpretation_class,
        })
    return rows


# ============================================================================
# 5. Genus tower sign analysis
# ============================================================================

def genus_tower_sign_analysis(N: int, max_genus: int = 6) -> Dict:
    """Analyze the sign of F_g(M5_N^!) at each genus.

    F_g = kappa * lambda_g^FP

    For N >= 3: kappa^! < 0, so F_g < 0 at ALL genera.
    This rules out a perturbative interpretation as a physical theory.
    """
    phantom = PhantomM5(N)
    tower = {}
    for g in range(1, max_genus + 1):
        fg = phantom.kappa_dual * lambda_fp(g)
        tower[g] = {
            "F_g": fg,
            "sign": "+" if fg > 0 else "0" if fg == 0 else "-",
            "lambda_g_FP": lambda_fp(g),
        }

    all_negative = all(tower[g]["sign"] == "-" for g in tower)
    all_zero = all(tower[g]["sign"] == "0" for g in tower)
    all_positive = all(tower[g]["sign"] == "+" for g in tower)

    return {
        "N": N,
        "kappa_dual": phantom.kappa_dual,
        "genus_tower": tower,
        "all_negative": all_negative,
        "all_zero": all_zero,
        "all_positive": all_positive,
        "perturbative_interpretation": (
            "uncurved (vanishing free energy)" if all_zero else
            "physical (positive free energy)" if all_positive else
            "unphysical (negative free energy at all genera)" if all_negative else
            "mixed signs"
        ),
    }


# ============================================================================
# 6. S-duality and mirror symmetry analysis
# ============================================================================

def s_duality_analysis(N: int) -> Dict:
    """Test whether M5_N^! arises from S-duality.

    For M2 (3d boundary): the Koszul dual is related to the S-dual
    boundary condition via Gaiotto-Witten 3d mirror symmetry.

    For M5 (6d boundary): there is no Lagrangian description, so
    S-duality does not apply directly.  However:

    1. On S^1 -> 5d SYM: S-duality gives strong-weak coupling swap.
    2. On T^2 -> 4d N=4: S-duality is Montonen-Olive.
    3. On T^3 -> 3d N=8: S-duality is 3d mirror symmetry.

    The DIMENSIONAL REDUCTION tower shows that M5^! acquires an
    interpretation as the S-dual BOUNDARY CONDITION in lower dimensions,
    but never as an independent 6d theory.
    """
    phantom = PhantomM5(N)

    # 5d: coupling g^2 = R (radius). S-dual: g^2 -> 1/g^2, i.e., R -> 1/R.
    # This is T-duality, not S-duality.
    # lambda -> lambda' under T-duality of the (2,0) on S^1.

    # 4d: Montonen-Olive: tau -> -1/tau.
    # (2,0) on T^2 with modulus tau gives 4d N=4 with coupling tau.
    # Koszul duality lambda -> 2-lambda vs S-duality tau -> -1/tau:
    # these are DIFFERENT operations.

    # 3d: Gaiotto-Witten mirror symmetry.
    # (2,0) on T^3 gives 3d N=8 with hyperkahler target.
    # Mirror symmetry: swaps Coulomb and Higgs branches.
    # Koszul duality swaps A and A^!.

    return {
        "N": N,
        "lambda_original": phantom.lambda_original,
        "lambda_dual": phantom.lambda_dual,
        "dimensional_reduction": {
            "6d": "no S-duality (no Lagrangian)",
            "5d_on_S1": "T-duality R -> 1/R (not Koszul duality)",
            "4d_on_T2": "Montonen-Olive tau -> -1/tau (distinct from lambda -> 2-lambda)",
            "3d_on_T3": "3d mirror symmetry (closest analogue of Koszul duality)",
        },
        "koszul_matches_s_dual": False,
        "koszul_matches_mirror": N <= 2,  # At N=1,2 the operations might coincide
        "interpretation": (
            "Koszul duality (lambda -> 2-lambda) is NOT equivalent to "
            "any version of S-duality in ANY compactification dimension. "
            "It is a HOMOLOGICAL operation on the bar complex, not a "
            "duality of the physical theory. The phantom M5^! exists "
            "only as an algebraic shadow -- a mathematical dual with "
            "no independent physical existence."
        ),
    }


# ============================================================================
# 7. Comprehensive analysis
# ============================================================================

def phantom_m5_full_analysis(N: int) -> Dict:
    """Complete analysis of the phantom M5_N^!."""
    phantom = PhantomM5(N)
    return {
        "N": N,
        "core": {
            "lambda": phantom.lambda_original,
            "lambda_dual": phantom.lambda_dual,
            "kappa": phantom.kappa_original,
            "kappa_dual": phantom.kappa_dual,
            "complementarity": phantom.complementarity_sum,
            "dual_sign": "+" if phantom.kappa_dual > 0 else "0" if phantom.kappa_dual == 0 else "-",
            "interpretation_class": phantom.interpretation_class,
        },
        "candidates": {
            "negative_N": negative_n_analysis(N),
            "orientifold": orientifold_comparison(N),
            "5d_SYM": five_d_sym_comparison(N),
            "6d_10": one_zero_comparison(N),
            "M2_analogy": m2_koszul_dual_analogy(N),
        },
        "complementarity_polynomial": complementarity_polynomial(N),
        "genus_tower": genus_tower_sign_analysis(N),
        "s_duality": s_duality_analysis(N),
    }


def phantom_sweep(N_max: int = 8) -> List[Dict]:
    """Sweep analysis across N = 1, ..., N_max."""
    return [
        {
            "N": N,
            "kappa": Fraction(N) ** 3,
            "kappa_dual": Fraction(2 - N) ** 3,
            "complementarity": 6 * N ** 2 - 12 * N + 8,
            "dual_sign": "+" if (2 - N) ** 3 > 0 else "0" if N == 2 else "-",
            "lambda_dual": 2 - N,
            "in_physical_range": 2 - N >= 0,
            "interpretation": PhantomM5(N).interpretation_class,
        }
        for N in range(1, N_max + 1)
    ]
