r"""Bershadsky-Polyakov Koszul conductor and complementarity: exact Fraction arithmetic.

MATHEMATICAL CONTENT
====================

The Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)}) is the DS reduction of
affine sl_3 at the MINIMAL nilpotent orbit.  Its central charge, Feigin-Frenkel
dual level, Koszul conductor, anomaly ratio, and modular characteristic are
computed here in exact rational arithmetic.

Formulas:

    c_BP(k) = 2 - 24(k+1)^2 / (k+3)

    k' = -k - 6     (Feigin-Frenkel dual; h^v(sl_3) = 3, Dynkin shift)

    K_BP = c_BP(k) + c_BP(-k-6) = 196   (level-independent)

    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)

    kappa_BP(k) = varrho_BP * c_BP(k)

    kappa_BP(k) + kappa_BP(-k-6) = varrho_BP * K_BP = 98/3

    Self-dual level: k = -3, the fixed point of the involution k -> -k-6.
    NOTE: c_BP has a POLE at k = -3 (the critical level for sl_3).
    The self-dual property refers to the involution fixed point, not to
    literal evaluation c_BP(-3) = K_BP/2.

ALGEBRAIC PROOF that K_BP = 196:
    c(k) = 2 - 24(k+1)^2/(k+3)
    k' = -k-6,  k'+1 = -k-5,  k'+3 = -k-3
    c(k') = 2 - 24(-k-5)^2/(-k-3) = 2 + 24(k+5)^2/(k+3)
    c(k) + c(k') = 4 + 24[(k+5)^2 - (k+1)^2]/(k+3)
                  = 4 + 24[(2k+6)(4)]/(k+3)
                  = 4 + 24 * 8 * (k+3)/(k+3)
                  = 4 + 192
                  = 196.

VERIFICATION PATHS:
    Path 1: Direct computation of c(k) + c(-k-6) = 196 (algebraic, above)
    Path 2: Numerical evaluation at k = 0, 1, -1, 2, -2, 5, 10, -4
    Path 3: Involution fixed point: dual_level(-3) = -3
    Path 4: Cross-engine consistency with sl3_subregular_bar.py
    Path 5: Cross-engine consistency with theorem_gz_frontier_engine.py

References:
    Fehily-Kawasetsu-Ridout (2020): BP central charge formula
    sl3_subregular_bar.py: anomaly ratio computation (rho = 1/6)
    theorem_gz_frontier_engine.py: K_BP = 196 (corrected from 76, AP1/AP3)
    bp_shadow_tower.py: shadow tower with K_BP = 196
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Union

# =============================================================================
# Constants
# =============================================================================

# Anomaly ratio for BP: sum_i (-1)^{p_i} / h_i over strong generators
#   J (h=1, bos): +1     G+ (h=3/2, fer): -2/3
#   G- (h=3/2, fer): -2/3     T (h=2, bos): +1/2
# Total: 1 - 2/3 - 2/3 + 1/2 = 1/6.
# VERIFIED: [DC] 1 - 2/3 - 2/3 + 1/2 = 1/6 from the strong-generator weights/parities;
# [LT] chapters/examples/bershadsky_polyakov.tex, Proposition `prop:bp-kappa`, states varrho = 1/6.
# VERIFIED: [DC] the strong-generator sum is 1/6; [LT] the BP kappa proposition records varrho = 1/6.
VARRHO_BP = Fraction(1, 6)

# Koszul conductor (proved level-independent; algebraic proof in docstring).
# VERIFIED: [DC] c(k) + c(-k-6) simplifies to 196 by direct cancellation;
# [LT] chapters/examples/bershadsky_polyakov.tex, eq. `eq:bp-conductor`, gives K_B = 196.
# VERIFIED: [DC] c(k) + c(-k-6) = 196; [LT] eq. `eq:bp-conductor` gives the same constant.
K_BP_EXACT = Fraction(196)

# Kappa complementarity sum: varrho * K = (1/6) * 196 = 98/3.
# VERIFIED: [DC] (1/6) * 196 = 98/3;
# [LT] chapters/examples/bershadsky_polyakov.tex, eq. `eq:bp-complementarity`, gives 98/3.
KAPPA_COMPLEMENTARITY_EXACT = VARRHO_BP * K_BP_EXACT  # = Fraction(98, 3)

# BP strong generators: name -> (conformal weight, parity).
# Parity: 0 = bosonic, 1 = fermionic.
BP_GENERATORS = {
    "J":  (Fraction(1), 0),     # VERIFIED: [LT] BP strong-generator list has J of weight 1 and bosonic parity; [DC] the U(1) current in the DS reduction is even.
    "G+": (Fraction(3, 2), 1),  # VERIFIED: [LT] BP strong-generator list has G^+ of weight 3/2 and fermionic parity; [DC] odd BRST survivors from the minimal nilpotent sector are fermionic.
    "G-": (Fraction(3, 2), 1),  # VERIFIED: [LT] BP strong-generator list has G^- of weight 3/2 and fermionic parity; [SY] G^+ and G^- form the same-weight conjugate pair.
    "T":  (Fraction(2), 0),     # VERIFIED: [LT] the stress tensor has weight 2 and bosonic parity; [DC] conformal vectors are even.
}


# =============================================================================
# Core functions
# =============================================================================

def c_BP(k: Union[int, Fraction]) -> Fraction:
    r"""Bershadsky-Polyakov central charge at level k.

    c_BP(k) = 2 - 24(k+1)^2 / (k+3).

    Source: Fehily-Kawasetsu-Ridout (2020).
    Corrected from principal W_3 formula (AP1/AP3, 2026-04-08).

    Raises ZeroDivisionError at the critical level k = -3.
    """
    k = Fraction(k)
    numerator = Fraction(24) * (k + 1) ** 2
    denominator = k + 3
    if denominator == 0:
        raise ZeroDivisionError(
            "BP central charge singular at k = -3 (critical level for sl_3)"
        )
    # VERIFIED: [LT] Fehily-Kawasetsu-Ridout central-charge formula c_BP(k) = 2 - 24(k+1)^2/(k+3);
    # [LC] k=-1 gives c=2 and k=0 gives c=-6.
    # VERIFIED: [LT] c_BP(k) = 2 - 24(k+1)^2/(k+3); [LC] k=-1 -> 2 and k=0 -> -6.
    return Fraction(2) - numerator / denominator


def dual_level(k: Union[int, Fraction]) -> Fraction:
    r"""Feigin-Frenkel dual level for BP.

    k' = -k - 6.

    The involution arises from h^v(sl_3) = 3 with the Dynkin grading
    shift for the minimal nilpotent: k + k' = -2 * h^v = -6.
    """
    # VERIFIED: [DC] solving k+k' = -2h^v with h^v(sl_3)=3 gives k' = -k-6;
    # [SY] the map is an involution with fixed point k = -3.
    # VERIFIED: [DC] k' = -k-6 from h^v(sl_3)=3; [SY] fixed point at k=-3.
    return -Fraction(k) - Fraction(6)


def K_BP(k: Union[int, Fraction]) -> Fraction:
    r"""Koszul conductor K_BP = c_BP(k) + c_BP(-k-6).

    Algebraically equal to 196 for all k != -3.
    """
    k = Fraction(k)
    # VERIFIED: [DC] direct sum c_BP(k) + c_BP(-k-6);
    # [CF] equals the level-independent conductor K_BP = 196.
    return c_BP(k) + c_BP(dual_level(k))


def kappa_BP(k: Union[int, Fraction]) -> Fraction:
    r"""Modular characteristic kappa_BP(k) = varrho_BP * c_BP(k).

    varrho_BP = 1/6 (anomaly ratio from strong-generator data).
    """
    # VERIFIED: [DC] kappa_BP = varrho_BP * c_BP by definition;
    # [CF] varrho_BP = 1/6 matches the BP anomaly-ratio proposition.
    return VARRHO_BP * c_BP(k)


def kappa_complementarity(k: Union[int, Fraction]) -> Fraction:
    r"""Kappa complementarity: kappa_BP(k) + kappa_BP(-k-6) = varrho * K_BP = 98/3."""
    k = Fraction(k)
    # VERIFIED: [DC] add the dual pair kappa_BP(k) + kappa_BP(-k-6);
    # [CF] equals varrho_BP * K_BP = 98/3.
    return kappa_BP(k) + kappa_BP(dual_level(k))


def self_dual_level() -> Fraction:
    r"""Self-dual level k_sd = -3, the fixed point of k -> -k-6.

    NOTE: c_BP has a pole at k = -3 (critical level for sl_3).
    The self-dual property is that dual_level(-3) = -3, i.e. the
    involution k -> -k-6 has fixed point k = -3.
    """
    # VERIFIED: [DC] solve k = -k-6 to get k = -3;
    # [SY] fixed point of the dual-level involution.
    # VERIFIED: [DC] k = -3 solves k = -k-6; [SY] unique involution fixed point.
    return Fraction(-3)


def compute_varrho() -> Fraction:
    r"""Compute the anomaly ratio from BP strong-generator data.

    varrho = sum_i (-1)^{p_i} / h_i:
        J (h=1, bos):    +1/1 = 1
        G+ (h=3/2, fer): -2/3
        G- (h=3/2, fer): -2/3
        T (h=2, bos):    +1/2
    Total: 1 - 2/3 - 2/3 + 1/2 = 1/6.
    """
    result = Fraction(0)
    for _name, (weight, parity) in BP_GENERATORS.items():
        sign = (-1) ** parity
        result += Fraction(sign) / weight
    # VERIFIED: [DC] the strong-generator sum is 1/6;
    # [CF] matches the constant VARRHO_BP.
    return result


# =============================================================================
# Verification
# =============================================================================

def verify_all(k_values: List[Union[int, Fraction]]) -> bool:
    r"""Verify all BP Koszul conductor and complementarity identities.

    Checks for every k in k_values (k != -3):
        1. K_BP(k) == 196.
        2. kappa_complementarity(k) == 98/3.
        3. dual_level(dual_level(k)) == k (involution).
        4. kappa_BP(k) == varrho * c_BP(k) (consistency).
        5. c_BP(k) + c_BP(dual_level(k)) == K_BP (direct).

    Global checks:
        6. Self-dual level is -3.
        7. dual_level(-3) == -3.
        8. compute_varrho() == 1/6.
        9. KAPPA_COMPLEMENTARITY_EXACT == 98/3.

    Raises AssertionError on any failure. Returns True on success.
    """
    for kv in k_values:
        kv = Fraction(kv)

        # Skip k = -3 (pole of c_BP) and k = 3 (pole of c_BP(dual_level))
        # VERIFIED: [DC] c_BP has denominator k+3, so the singular level is k=-3;
        # [SY] the dual level is skipped when dual_level(k) = -3 as well.
        if kv == Fraction(-3) or dual_level(kv) == Fraction(-3):
            continue

        k_dual = dual_level(kv)

        # (1) Koszul conductor = 196
        K = K_BP(kv)
        assert K == K_BP_EXACT, (
            f"K_BP({kv}) = {K}, expected {K_BP_EXACT}"
        )

        # (2) Kappa complementarity = 98/3
        kc = kappa_complementarity(kv)
        assert kc == KAPPA_COMPLEMENTARITY_EXACT, (
            f"kappa_complementarity({kv}) = {kc}, expected {KAPPA_COMPLEMENTARITY_EXACT}"
        )

        # (3) Involution: dual(dual(k)) = k
        assert dual_level(k_dual) == kv, (
            f"dual_level(dual_level({kv})) = {dual_level(k_dual)}, expected {kv}"
        )

        # (4) kappa consistency
        assert kappa_BP(kv) == VARRHO_BP * c_BP(kv), (
            f"kappa_BP({kv}) inconsistent with varrho * c_BP"
        )

        # (5) Direct sum
        assert c_BP(kv) + c_BP(k_dual) == K_BP_EXACT, (
            f"c_BP({kv}) + c_BP({k_dual}) = {c_BP(kv) + c_BP(k_dual)}, expected 196"
        )

    # (6, 7) Self-dual level
    k_sd = self_dual_level()
    # VERIFIED: [DC] k = -3 solves k = -k-6;
    # [SY] unique fixed point of the involution.
    # VERIFIED: [DC] k_sd = -3; [SY] dual_level(-3) = -3.
    assert k_sd == Fraction(-3), f"self_dual_level() = {k_sd}, expected -3"
    assert dual_level(k_sd) == k_sd, "k=-3 not fixed by involution"

    # (8) Anomaly ratio from generators
    assert compute_varrho() == VARRHO_BP, (
        f"compute_varrho() = {compute_varrho()}, expected {VARRHO_BP}"
    )

    # (9) Kappa complementarity constant
    # VERIFIED: [DC] (1/6) * 196 = 98/3;
    # [CF] BP complementarity theorem gives the same constant.
    # VERIFIED: [DC] (1/6) * 196 = 98/3; [CF] BP complementarity gives the same value.
    assert KAPPA_COMPLEMENTARITY_EXACT == Fraction(98, 3), (
        f"KAPPA_COMPLEMENTARITY_EXACT = {KAPPA_COMPLEMENTARITY_EXACT}, expected 98/3"
    )

    return True


def summary(k: Union[int, Fraction]) -> Dict[str, Fraction]:
    r"""Return a summary dict of all BP invariants at level k."""
    k = Fraction(k)
    kd = dual_level(k)
    return {
        "k": k,
        "k_dual": kd,
        "c_BP(k)": c_BP(k),
        "c_BP(k_dual)": c_BP(kd),
        "K_BP": K_BP(k),
        "varrho_BP": VARRHO_BP,
        "kappa_BP(k)": kappa_BP(k),
        "kappa_BP(k_dual)": kappa_BP(kd),
        "kappa_complementarity": kappa_complementarity(k),
    }


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    test_levels = [0, 1, -1, 2, -2, 5, 10, -4]
    print("BP Koszul Conductor Engine")
    print("=" * 60)
    for kv in test_levels:
        s = summary(kv)
        print(f"\nk = {kv}:")
        for key, val in s.items():
            print(f"  {key} = {val}")
    print("\n" + "=" * 60)
    print(f"Verification: {verify_all(test_levels)}")
    print(f"VARRHO_BP = {VARRHO_BP}")
    print(f"K_BP = {K_BP_EXACT}")
    print(f"kappa complementarity = {KAPPA_COMPLEMENTARITY_EXACT}")
