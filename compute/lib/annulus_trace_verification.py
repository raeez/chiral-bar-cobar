r"""Finite annulus-trace table helper for standard-family metadata.

This module is a ledger accessor for the schematic row used in old
annulus-trace sanity checks.  It does not build a Hochschild chain
complex, does not compute a differential, and does not prove Theorem H.
The table values are meaningful only after the manuscript's named
hypotheses have already supplied the input:

  * the \(H_H\) chiral Hochschild concentration package;
  * a specified Calabi-Yau trace/pairing that converts chains to
    cochains with the chosen degree shift;
  * the generic-parameter and completion assumptions for the family.

The ordinary Hochschild chain differential is \(b\).  The Connes
operator \(B\) belongs to cyclic, negative-cyclic, or periodic cyclic
homology; it is not part of the ordinary Hochschild differential.  The
``cyclic bar'' count below is only a finite cyclic-word orbit count for
tests of table shape.  It is not the vector-space dimension of the
completed Hochschild chain complex.

The normalized scalar returned by :func:`annulus_partition_function` is
the table entry for the identity trace after all of the above comparison
data have been supplied.  It is not topological Hochschild homology, not
a conformal annulus character, and not a chain-level computation.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
from typing import Dict, List, Optional, Tuple


# ======================================================================
#  Family data
# ======================================================================

# Generator data for each standard family.
# Each entry: (generator_weights, ope_max_order, description)
_FAMILY_GENERATORS = {
    "Heisenberg": {
        "weights": [1],
        "num_generators": 1,
        "description": "Single current a(z) of weight 1",
    },
    "Affine_sl2": {
        "weights": [1, 1, 1],
        "num_generators": 3,
        "description": "Currents e(z), f(z), h(z) of weight 1",
    },
    "Virasoro": {
        "weights": [2],
        "num_generators": 1,
        "description": "Stress tensor T(z) of weight 2",
    },
    "W3": {
        "weights": [2, 3],
        "num_generators": 2,
        "description": "T(z) weight 2, W(z) weight 3",
    },
}

FAMILIES = ("Heisenberg", "Affine_sl2", "Virasoro", "W3")

MODEL_SCOPE = {
    "status": "finite schematic table",
    "not_a_proof_of": ["Theorem H", "Calabi-Yau duality", "THH"],
    "ordinary_hochschild_differential": "b",
    "connes_operator": "cyclic/negative-cyclic enhancement only",
}


# ======================================================================
#  Hochschild homology dimensions (table entries under H_H + CY data)
# ======================================================================

def hochschild_homology_dimension(family: str, degree: int) -> int:
    r"""Schematic HH_n table entry for a generic standard-family row.

    The function records the old finite table after the \(H_H\) and
    Calabi-Yau comparison hypotheses have been supplied elsewhere.  It
    is not a chain-level calculation and must not be cited as
    independent evidence for concentration, affine derivation
    dimensions, or topological Hochschild homology.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    if degree < 0 or degree > 2:
        return 0

    # Finite table entry used by legacy tests under the model scope above.
    return 1


def hochschild_cohomology_dimension(family: str, degree: int) -> int:
    r"""Schematic HH^n table entry under the named \(H_H\) package."""
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    if degree < 0 or degree > 2:
        return 0

    return 1


# ======================================================================
#  Calabi-Yau duality verification
# ======================================================================

def calabi_yau_pairing_check(family: str) -> Dict[str, object]:
    """Check internal consistency of the finite table with a CY shift."""
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    checks = {}
    all_ok = True
    for n in range(3):
        hh_n = hochschild_homology_dimension(family, n)
        hh_2mn = hochschild_cohomology_dimension(family, 2 - n)
        match = (hh_n == hh_2mn)
        checks[n] = {
            "HH_n": hh_n,
            "HH^{2-n}": hh_2mn,
            "match": match,
        }
        if not match:
            all_ok = False

    return {
        "family": family,
        "degree_checks": checks,
        "calabi_yau_holds": all_ok,
    }


# ======================================================================
#  Cyclic bar complex dimensions
# ======================================================================

def _bar_complex_dimension(num_generators: int, degree: int,
                           weight_bound: int,
                           generator_weights: List[int]) -> int:
    """Dimension of the ordinary bar complex B_n(A) at degree n.

    The bar complex B_n(A) consists of elements a_0 [a_1 | ... | a_n]
    where each a_i is chosen from the generators (with repetition)
    and subject to weight constraints.

    At degree n with r generators, the dimension is:
      dim B_n = r^{n+1} * (number of weight-balanced lambda monomials)

    Weight balance: sum of input weights = output weight + lambda degree.
    But in the bar complex, the "output" is part of the tensor, so
    the weight constraint is simply that the total weight of the
    n+1 generators is at most weight_bound.
    """
    if degree < 0:
        return 0

    r = num_generators
    weights = generator_weights

    # Count (n+1)-tuples of generators with total weight <= weight_bound
    count = 0
    tuples = _enumerate_weight_tuples_bar(weights, degree + 1)
    for tw in tuples:
        total = sum(tw)
        if total <= weight_bound:
            count += 1

    return count


def _enumerate_weight_tuples_bar(weights: List[int],
                                 length: int) -> List[Tuple[int, ...]]:
    """Enumerate all tuples of weights of given length."""
    if length == 0:
        return [()]
    result = []
    for t in _enumerate_weight_tuples_bar(weights, length - 1):
        for w in weights:
            result.append(t + (w,))
    return result


def cyclic_bar_dimension(family: str, degree: int,
                         weight_bound: int) -> int:
    """Finite cyclic-word orbit count at degree n.

    This counts generator-weight words modulo cyclic rotation in a
    finite weight window.  It is a toy table-shape invariant, not the
    dimension of the completed Hochschild chain complex.

    For the ordinary word-orbit model:

      B^cyc_n(A) = B_n(A) / Z_{n+1}

    where Z_{n+1} is the cyclic group acting by rotating the tensor
    factors a_0, a_1, ..., a_n.

    The cyclic-word orbit count depends on the symmetry of
    the generators.  For generators of DISTINCT weights, there is no
    cyclic symmetry and dim B^cyc_n = dim B_n / (n+1).

    For generators of EQUAL weight (e.g., affine sl_2 with three
    weight-1 generators), some cyclic orbits have nontrivial stabilizer
    and the dimension is larger than the naive quotient.

    We compute the exact orbit count using Burnside's lemma:
      dim B^cyc_n = (1/(n+1)) * sum_{d | (n+1)} phi(d) * (# tuples fixed by rotation d)

    For simplicity and exact arithmetic, we use the weight-based counting.
    """
    if degree < 0:
        return 0

    data = _FAMILY_GENERATORS.get(family)
    if data is None:
        raise ValueError(f"Unknown family: {family}")

    r = data["num_generators"]
    weights = data["weights"]

    # Compute the bar complex dimension
    bar_dim = _bar_complex_dimension(r, degree, weight_bound, weights)

    # For the finite cyclic-word orbit count: use Burnside's lemma.
    # For (n+1)-tuples under Z_{n+1} rotation, the number of orbits is
    #   (1/(n+1)) * sum_{d | (n+1)} euler_phi(d) * N_d
    # where N_d = number of tuples with period dividing (n+1)/d.
    #
    # For simplicity with weight-constrained generators, we use the
    # exact Burnside count.
    n_plus_1 = degree + 1
    if n_plus_1 == 0:
        return 0

    # Burnside: count orbits of Z_{n+1} on weight-constrained tuples
    total_fixed = 0
    for d in range(1, n_plus_1 + 1):
        if n_plus_1 % d != 0:
            continue
        # Rotation by d positions: a tuple is fixed iff it has period d
        # Number of weight-constrained tuples with period dividing d:
        # these are tuples where the first d entries determine the rest
        # AND the total weight constraint is satisfied
        period = d
        fixed = _count_periodic_tuples(weights, n_plus_1, period,
                                       weight_bound)
        phi_d = _euler_phi(d)
        total_fixed += phi_d * fixed

    return total_fixed // n_plus_1


def _count_periodic_tuples(weights: List[int], length: int,
                           period: int, weight_bound: int) -> int:
    """Count tuples of given length that are periodic with given period.

    A tuple (a_0, ..., a_{n}) has period p if a_i = a_{i mod p} for all i,
    AND p divides length.

    Returns the number of such tuples with total weight <= weight_bound.
    """
    if length % period != 0:
        return 0

    repeats = length // period

    # Enumerate all tuples of length = period
    base_tuples = _enumerate_weight_tuples_bar(weights, period)
    count = 0
    for bt in base_tuples:
        total_weight = sum(bt) * repeats
        if total_weight <= weight_bound:
            count += 1

    return count


def _euler_phi(n: int) -> int:
    """Euler's totient function phi(n)."""
    if n <= 0:
        return 0
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


# ======================================================================
#  Annulus partition function
# ======================================================================

def annulus_partition_function(family: str) -> Fraction:
    """Normalized scalar identity-trace table entry.

    The value is the legacy finite-table normalization after the annulus
    trace comparison and CY trace datum have been supplied.  It is not
    a conformal annulus amplitude, not a spectral THH invariant, and not
    a computation of the completed chain complex.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    # Legacy normalized table value under MODEL_SCOPE.
    return Fraction(1)


# ======================================================================
#  Full Hochschild package
# ======================================================================

def hochschild_package(family: str) -> Dict[str, object]:
    """Finite table package for a standard family.

    Returns the stored HH_n/HH^n rows, their internal CY-shift check,
    and the normalized scalar annulus entry.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    hh_homology = {n: hochschild_homology_dimension(family, n) for n in range(3)}
    hh_cohomology = {n: hochschild_cohomology_dimension(family, n) for n in range(3)}
    cy = calabi_yau_pairing_check(family)
    z_ann = annulus_partition_function(family)

    return {
        "family": family,
        "HH_*": hh_homology,
        "HH^*": hh_cohomology,
        "calabi_yau": cy,
        "Z_ann": z_ann,
        "poincare_polynomial": [hh_cohomology[n] for n in range(3)],
    }


# ======================================================================
#  Cross-family comparisons
# ======================================================================

def cross_family_hh_comparison() -> Dict[str, Dict[int, int]]:
    """Compare the finite HH_n table rows across standard families.

    This is a table-shape comparison.  It is not a proof that the
    completed Hochschild chain complexes have equal dimensions.
    """
    return {
        family: {n: hochschild_homology_dimension(family, n) for n in range(3)}
        for family in FAMILIES
    }


def cy_duality_all_families() -> Dict[str, bool]:
    """Check CY duality for all families."""
    return {
        family: calabi_yau_pairing_check(family)["calabi_yau_holds"]
        for family in FAMILIES
    }


# ======================================================================
#  Cyclic homology (from the SBI sequence)
# ======================================================================

def cyclic_homology_dimension(family: str, degree: int) -> int:
    """Schematic HC_n table row produced from the finite HH row.

    If the finite HH row is supplied and the SBI sequence has the
    stated split form, one obtains the displayed toy pattern.  The
    function does not compute Connes' operator or a cyclic complex.

    The SBI (Connes) exact sequence:
      ... -> HH_n -> HC_n -> HC_{n-2} -> HH_{n-1} -> ...

    For the 3-term input table (concentrated in {0,1,2}):
      HC_0 = HH_0 = 1
      HC_1 = HH_1 = 1 (since HC_{-1} = 0)
      HC_2 = HH_2 + HC_0 = 1 + 1 = 2
        (the SBI sequence: 0 -> HH_2 -> HC_2 -> HC_0 -> 0 gives
         HC_2 = HH_2 + HC_0 = 2)
      HC_{2k} = k+1 for k >= 0 (by periodicity: HC_{2k} = HC_{2k-2} + 1)
      HC_{2k+1} = 1 for k >= 0 (odd cyclic homology stabilizes)

    NOTE: this is only the periodic pattern under a chosen S-operator.
    The actual computation depends on the completed cyclic complex.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    if degree < 0:
        return 0
    if degree % 2 == 0:
        return degree // 2 + 1
    else:
        return 1


def negative_cyclic_homology_dimension(family: str, degree: int) -> int:
    """Schematic HC^-_n table row.

    This is a placeholder finite pattern for legacy tests, not a
    computation of a completed negative-cyclic complex.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    if degree < 0 or degree > 1:
        return 0
    return 1


# ======================================================================
#  Parametric verification
# ======================================================================

def verify_hh_independence_of_parameters(family: str,
                                         param_values: List[Fraction]
                                         ) -> bool:
    """Check that this finite table ignores level/central-charge input.

    This is not mathematical evidence for parameter independence; the
    helper has no parameter in its data model.
    """
    base_dims = {n: hochschild_homology_dimension(family, n) for n in range(3)}

    for _ in param_values:
        # The table accessor is parameter-independent by construction.
        current_dims = {n: hochschild_homology_dimension(family, n) for n in range(3)}
        if current_dims != base_dims:
            return False

    return True


# ======================================================================
#  Euler characteristics
# ======================================================================

def hochschild_euler_characteristic(family: str) -> int:
    """Euler characteristic of the finite HH_* table row.

    For the stored row this is 1 - 1 + 1.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    return sum((-1)**n * hochschild_homology_dimension(family, n)
               for n in range(3))


def hochschild_total_dimension(family: str) -> int:
    """Total dimension of the finite HH_* table row.

    For the stored row this is 1 + 1 + 1.
    """
    if family not in _FAMILY_GENERATORS:
        raise ValueError(f"Unknown family: {family}")

    return sum(hochschild_homology_dimension(family, n) for n in range(3))
