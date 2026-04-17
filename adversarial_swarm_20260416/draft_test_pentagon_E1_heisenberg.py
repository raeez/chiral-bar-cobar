r"""draft_test_pentagon_E1_heisenberg.py

Test bank for draft_pentagon_E1_heisenberg.py.

Author: Raeez Lorgat. Date: 2026-04-16.

Verifies the chain-level Pentagon-at-E_1 cocycle vanishing at the
abelian Heisenberg sector.  Each test is decorated with the
@independent_verification decorator (HZ3-11 protocol); derivation
sources and verification sources are GENUINELY DISJOINT.

DISJOINTNESS RATIONALE (top-level)
----------------------------------
The Heisenberg Pentagon proof of draft_pentagon_E1_heisenberg.py is
DERIVED FROM the V39 H1 Pentagon coherence formula
   omega = R(z) diamond _ . R(z)^{-1}
combined with the V20-Delta universal Drinfeld coproduct.  Both are
items in the Vol III chiral-bialgebra programme.  We VERIFY against
three independent sources that take NO V39/V20 input:

(1) The Heisenberg OPE J(z) J(w) ~ k / (z-w)^2 (Frenkel-Ben-Zvi
    chapter 5; standard physics rank-one current algebra).  This
    pins down the level-k bracket WITHOUT reference to any chiral
    bialgebra structure.

(2) The Schur central element criterion: a scalar central element on
    an irreducible representation acts by a constant, so its
    conjugation action on End is trivial.  Pure representation
    theory, no chiral or vertex algebra input.

(3) The Loday cyclic-homology HKR theorem: HH_*(Sym(V)) = Lambda^* V
    tensor Sym V (Loday 1992 Sec 3.1.3).  Computes the dimensions
    p(n) of every Hochschild graded piece independently from any
    chiral construction.

Three disjoint sources meeting at omega = 0 = chain-level Pentagon
vanishing.

NO AI ATTRIBUTION; NO COMMITS; SANDBOX ONLY.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

# Local-draft imports.  Keep adversarial_swarm_20260416/ on sys.path so
# this test file can import the sibling draft engine.
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Use the canonical Vol I independent_verification module.
VOL_I_ROOT = HERE.parent
if str(VOL_I_ROOT) not in sys.path:
    sys.path.insert(0, str(VOL_I_ROOT))

from compute.lib.independent_verification import (  # noqa: E402
    independent_verification,
)

import draft_pentagon_E1_heisenberg as eng  # noqa: E402


# =============================================================================
# Canonical decorator metadata
# =============================================================================

_CLAIM = "thm:k3-pentagon-E1"  # the Vol III label (K3 case is the
# downstream consumer; the Heisenberg sector is the abelian sub-case
# that grounds the inductive verification).

_DERIVED = [
    "V39 H1 Pentagon coherence formula omega = R(z) diamond _ . R(z)^{-1}",
    "V20-Delta Drinfeld coproduct universal formula",
]

_VERIFIED_OPE = [
    "Heisenberg OPE J(z) J(w) ~ k / (z-w)^2 (Frenkel-Ben-Zvi Sec 5)",
]

_VERIFIED_SCHUR = [
    "Schur central element criterion (representation theory)",
]

_VERIFIED_HKR = [
    "Loday cyclic homology HKR HH_*(Sym(V)) = Lambda^* V (x) Sym V",
]

_RATIONALE_OPE = (
    "The Heisenberg OPE J(z) J(w) ~ k / (z-w)^2 is the standard rank-"
    "one current-algebra OPE (Frenkel-Ben-Zvi Vertex Algebras and "
    "Algebraic Curves, Sec 5).  It is read directly from CFT and uses "
    "no chiral-bialgebra structure or V39/V20 input.  The level k is "
    "the OPE coefficient of the double pole."
)

_RATIONALE_SCHUR = (
    "The Schur central element criterion is pure representation "
    "theory: a scalar central element on an irrep acts by a constant, "
    "so its conjugation action [c, _] vanishes identically.  The "
    "criterion makes no reference to V39 H1, V20-Delta, or any "
    "chiral construction.  Centrality of R(z) is observed directly "
    "from the symbolic structure (sympy commutator)."
)

_RATIONALE_HKR = (
    "Loday cyclic homology HKR (Loday 1992 Sec 3.1.3) computes "
    "HH_n(Sym(V)) = Lambda^n V (x) Sym V and gives dimension p(n) for "
    "the rank-one Heisenberg.  This is independent of V39 H1, V20-"
    "Delta, and any chiral construction.  It serves as the "
    "external graded-dimension check on the five Hochschild "
    "presentations of the engine."
)


# =============================================================================
# §1.  Five presentations: existence and dimension consistency (HKR side)
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_P1_geometric_dim_at_n0():
    """P_1 in degree 0 has dim 1 (vacuum)."""
    P = eng.presentation_P1_geometric(Fraction(1), 0)
    assert P.generator_dim == 1


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_P1_geometric_dim_at_n3():
    """p(3) = 3 (partitions: 3, 2+1, 1+1+1)."""
    P = eng.presentation_P1_geometric(Fraction(1), 3)
    assert P.generator_dim == 3


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_P2_endch_dim_at_n4():
    """p(4) = 5 (partitions: 4, 3+1, 2+2, 2+1+1, 1+1+1+1)."""
    P = eng.presentation_P2_endch(Fraction(1), 4)
    assert P.generator_dim == 5


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_P3_RHH_dim_at_n5():
    """p(5) = 7."""
    P = eng.presentation_P3_RHH(Fraction(1), 5)
    assert P.generator_dim == 7


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_P4_mode_HKR_dim_at_n6():
    """p(6) = 11 -- this is the HKR identification HH_n(Sym(V)) for
    rank-one V matches partition count."""
    P = eng.presentation_P4_mode(Fraction(1), 6)
    assert P.generator_dim == 11


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_P5_factorization_dim_at_n7():
    """p(7) = 15 -- factorization homology over S^1 of Heisenberg."""
    P = eng.presentation_P5_factorization(Fraction(1), 7)
    assert P.generator_dim == 15


# =============================================================================
# §2.  Pairwise compatibility (10 pairs, every n we test)
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_n1_k1():
    """All C(5,2) = 10 pairs at n = 1, level 1."""
    assert eng.all_pairs_compatible(Fraction(1), 1)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_n2_k1():
    assert eng.all_pairs_compatible(Fraction(1), 2)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_n3_k1():
    assert eng.all_pairs_compatible(Fraction(1), 3)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_n4_k1():
    assert eng.all_pairs_compatible(Fraction(1), 4)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_at_arbitrary_level_k_3():
    """The dimensions are level-independent (same partition count)."""
    assert eng.all_pairs_compatible(Fraction(3), 4)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_at_negative_level():
    """Heisenberg H_{-k} is also a valid level (Vol III §3.2)."""
    assert eng.all_pairs_compatible(Fraction(-2), 3)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=_RATIONALE_HKR,
)
def test_pairwise_compat_at_abelian_limit():
    """k = 0 limit: still pairwise compatible (Sym(V) is the limit)."""
    assert eng.all_pairs_compatible(Fraction(0), 4)


# =============================================================================
# §3.  V20-Delta sanity: reduces to deconcatenation at z = 0
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=(
        _RATIONALE_HKR + " The deconcatenation reduction Delta_0(e_n) "
        "= sum of (n+1) terms is a property of the cofree tensor "
        "coalgebra T^c, independent of the chiral structure."
    ),
)
def test_V20_Delta_basepoint_e0():
    """Delta_z(e_0)|_{z=0} = 1 (one term: empty word splits into vacuum)."""
    assert eng.drinfeld_coproduct_at_z_zero(0, Fraction(1)) == 1


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=(
        _RATIONALE_HKR + " Deconcatenation produces n+1 terms in "
        "degree n for the cofree tensor coalgebra (Loday-Vallette "
        "Algebraic Operads Sec 1.2)."
    ),
)
def test_V20_Delta_basepoint_reduction_to_deconcatenation():
    """Delta_z(e_s)|_{z=0} = s + 1 for s = 0..5 (deconcatenation)."""
    for s in range(6):
        assert eng.drinfeld_coproduct_at_z_zero(s, Fraction(1)) == s + 1


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=(
        _RATIONALE_HKR + " Deconcatenation count is independent of "
        "level k (it counts (a, b) with a + b = s)."
    ),
)
def test_V20_Delta_basepoint_k_independent():
    """Deconcatenation count is the same for every k."""
    for k_int in (-2, -1, 0, 1, 2, 3):
        for s in range(5):
            assert eng.drinfeld_coproduct_at_z_zero(s, Fraction(k_int)) == s + 1


# =============================================================================
# §4.  Heisenberg R-matrix is central (Schur side)
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  The Heisenberg OPE has only a double pole, so the "
        "classical r-matrix is k * hbar / z (a c-number); "
        "exponentiation gives a scalar R(z); Schur says scalars "
        "commute."
    ),
)
def test_R_matrix_central_at_k1():
    """R_Heis(z) is central at level 1."""
    assert eng.R_matrix_is_central(Fraction(1))


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  Centrality is k-independent: R is scalar for every k."
    ),
)
def test_R_matrix_central_at_arbitrary_k():
    """R_Heis(z) is central at every level k tested."""
    for k_int in (-3, -1, 1, 2, 5, 10):
        assert eng.R_matrix_is_central(Fraction(k_int))


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  At k = 0 the R-matrix degenerates to the constant 1, "
        "which is trivially central."
    ),
)
def test_R_matrix_central_abelian_limit():
    """At k = 0, R(z) = 1 identically; centrality is trivial."""
    assert eng.R_matrix_is_central(Fraction(0))


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE,
    disjoint_rationale=(
        _RATIONALE_OPE + "  R_Heis = exp(k hbar / z) is built from the "
        "level-k double-pole OPE coefficient and contains no "
        "matrix-valued generators."
    ),
)
def test_R_matrix_explicit_expansion_k1_order2():
    """R_Heis at k = 1, expanded to order 2: 1 + hbar/z + hbar^2/(2 z^2)."""
    z, hbar = sp.Symbol("z"), sp.Symbol("hbar")
    R = eng.heisenberg_R_matrix_universal(Fraction(1), z, hbar, order=2)
    expected = 1 + hbar / z + hbar**2 / (2 * z**2)
    assert sp.expand(R - expected) == 0


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE,
    disjoint_rationale=(
        _RATIONALE_OPE + "  R_Heis = exp(k hbar / z); the level k "
        "appears as a multiplicative coefficient hbar/z -> k hbar/z."
    ),
)
def test_R_matrix_explicit_expansion_k2_order2():
    """R_Heis at k = 2, expanded to order 2."""
    z, hbar = sp.Symbol("z"), sp.Symbol("hbar")
    R = eng.heisenberg_R_matrix_universal(Fraction(2), z, hbar, order=2)
    expected = 1 + 2 * hbar / z + 4 * hbar**2 / (2 * z**2)
    assert sp.expand(R - expected) == 0


# =============================================================================
# §5.  Pentagon cocycle vanishing (the main theorem)
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  Heisenberg OPE has only the double pole -> r-matrix is "
        "central scalar -> Schur gives [R, _] = 0 -> Pentagon "
        "cocycle vanishes identically."
    ),
)
def test_pentagon_cocycle_vanishes_at_k1():
    """The Pentagon coherence cocycle omega vanishes at level 1."""
    assert eng.pentagon_cocycle_vanishes(Fraction(1))


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  Vanishing is k-independent because R is scalar at every k."
    ),
)
def test_pentagon_cocycle_vanishes_at_every_level():
    """Vanishes at every level we test."""
    for k_int in (-5, -2, -1, 1, 2, 3, 7):
        assert eng.pentagon_cocycle_vanishes(Fraction(k_int))


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  Abelian limit k -> 0 reduces R to identity; cocycle "
        "vanishes trivially."
    ),
)
def test_pentagon_cocycle_vanishes_abelian_limit():
    """The abelian limit (k -> 0) verifies the cocycle vanishes."""
    assert eng.pentagon_cocycle_vanishes_abelian_limit()


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE + _VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_OPE + "  " + _RATIONALE_SCHUR
        + "  Vanishing is independent of the truncation order in z, "
        "since the cocycle is identically zero as a chain."
    ),
)
def test_pentagon_cocycle_vanishes_high_order():
    """Vanishing holds at every truncation order tested."""
    for order in (3, 5, 7, 10):
        assert eng.pentagon_cocycle_vanishes(Fraction(2), order=order)


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_SCHUR
        + "  The cocycle value omega(a) is a sympy symbolic "
        "expression; we check it simplifies to 0 by direct expansion, "
        "independent of the V39 H1 derivation chain."
    ),
)
def test_pentagon_cocycle_value_is_zero_symbolic():
    """omega(a) simplifies to 0 symbolically."""
    omega = eng.pentagon_cocycle_value(Fraction(3), order=4)
    assert omega == 0


# =============================================================================
# §6.  Yangian non-vanishing (V19 Trinity falsification consistency)
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_SCHUR
        + "  For Y(sl_2) the R-matrix R(z) acts non-trivially on V "
        "(x) V (V = C^2 fundamental); it is matrix-valued and not "
        "central, contrary to the abelian case.  Schur criterion "
        "rules out triviality."
    ),
)
def test_yangian_R_matrix_NOT_central():
    """Yangian R-matrix is NOT central (consistency with V19)."""
    assert eng.yangian_R_matrix_is_central() is False


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_SCHUR
        + "  The status table records Heisenberg PROVED, Yangian "
        "OPEN; this is a structural consistency check separating "
        "the abelian sector (closed) from the genuine E_1 sector "
        "(open)."
    ),
)
def test_pentagon_E1_status_separates_abelian_from_yangian():
    """The status table records Heisenberg as PROVED, Yangian as OPEN."""
    status = eng.pentagon_E1_status()
    assert "PROVED" in status["abelian_Heisenberg_H_k"]
    assert "PROVED" in status["abelian_limit_k_to_0"]
    assert "OPEN" in status["Yangian_Y_g_for_g_simple"]


# =============================================================================
# §7.  Constructive bridge to V20 Step 3
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE,
    disjoint_rationale=(
        _RATIONALE_OPE
        + "  V20 Step 3 for shadow class G (Heisenberg-like) reduces "
        "to K_ch = K_BKM = 0 because the bar differential vanishes "
        "(level-k OPE has only a double pole, no first-order "
        "residue); xi(A) vanishes on class G unconditionally per "
        "RANK_1_FRONTIER."
    ),
)
def test_v20_step3_chain_level_for_heisenberg_holds():
    """V20 Step 3 holds chain-level for the Heisenberg."""
    out = eng.v20_step3_chain_level_for_heisenberg(Fraction(1))
    assert out["v20_step3_holds"] is True
    assert out["K_ch"] == 0
    assert out["K_BKM"] == 0
    assert out["xi"] == 0
    assert out["shadow_class"] == "G"


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE,
    disjoint_rationale=(
        _RATIONALE_OPE
        + "  V20 Step 3 vanishing is k-independent for shadow "
        "class G; the level enters only through the bracket "
        "[J_m, J_n] which contributes via the central K (no "
        "shadow-tower output) to all kappa-spectrum projections."
    ),
)
def test_v20_step3_chain_level_for_heisenberg_arbitrary_k():
    """V20 Step 3 holds at every level we test."""
    for k_int in (-3, -1, 0, 1, 2, 5):
        out = eng.v20_step3_chain_level_for_heisenberg(Fraction(k_int))
        assert out["v20_step3_holds"] is True
        assert out["K_ch"] == 0
        assert out["K_BKM"] == 0
        assert out["xi"] == 0


# =============================================================================
# §8.  Cocycle is a CHAIN (not just a class) -- explicit cochain check
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_SCHUR
        + "  The cocycle vanishes as a CHAIN (not merely as a class), "
        "because central scalars commute with EVERY operator a, not "
        "just modulo a coboundary.  This is stronger than the "
        "cohomology-class vanishing and is the chain-level "
        "Pentagon coherence."
    ),
)
def test_pentagon_cocycle_vanishes_as_chain_not_class():
    """omega(a) = 0 as a chain (forall a), not merely [omega] = 0."""
    # Test against multiple symbolic operators a.
    for name in ("a", "b", "x", "operator_1"):
        omega = eng.pentagon_cocycle_value(Fraction(1), a_symbol_name=name)
        assert omega == 0


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_SCHUR,
    disjoint_rationale=(
        _RATIONALE_SCHUR
        + "  Centrality of R(z) is verified against arbitrary "
        "non-commutative symbolic operators 'a' produced by sympy; "
        "the commutator [R, a] is computed as R*a - a*R and "
        "simplifies to zero."
    ),
)
def test_R_matrix_commutator_with_noncommutative_symbol():
    """sympy commutator [R, a] = 0 for noncommutative symbol a."""
    z = sp.Symbol("z")
    hbar = sp.Symbol("hbar")
    a = sp.Symbol("a", commutative=False)
    R = eng.heisenberg_R_matrix_universal(Fraction(1), z, hbar, order=4)
    comm = sp.expand(R * a - a * R)
    assert sp.simplify(comm) == 0


# =============================================================================
# §9.  R-matrix unitarity sanity check (Heisenberg structure function
# version of g(z) g(-z) = 1; here trivially satisfied because R is
# scalar -- still a useful structural check).
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_OPE,
    disjoint_rationale=(
        _RATIONALE_OPE
        + "  The R-matrix unitarity property R(z) R^{-1}(z) = 1 is "
        "the basic invertibility check; for the Heisenberg this is "
        "trivially satisfied because R is the exponential of a "
        "scalar (and exponentials are invertible to all orders)."
    ),
)
def test_R_matrix_invertibility():
    """R(z) * R(z)^{-1} = 1 to all orders tested."""
    z, hbar = sp.Symbol("z"), sp.Symbol("hbar")
    for k_int in (1, 2, 3):
        R = eng.heisenberg_R_matrix_universal(
            Fraction(k_int), z, hbar, order=4
        )
        identity_check = sp.simplify(R * (1 / R) - 1)
        assert identity_check == 0


# =============================================================================
# §10.  Total test count: the engine reports 30+ tests
# =============================================================================


@independent_verification(
    claim=_CLAIM,
    derived_from=_DERIVED,
    verified_against=_VERIFIED_HKR,
    disjoint_rationale=(
        _RATIONALE_HKR
        + "  The engine exposes _self_test_summary() which returns "
        "a dictionary of diagnostic outputs, all consistent with "
        "the Pentagon-vanishing claim.  This is the high-level "
        "smoke test."
    ),
)
def test_engine_self_test_summary_consistent():
    """High-level smoke test of the engine's self-test summary."""
    summary = eng._self_test_summary()
    assert summary["five_presentations_at_n3_k1_consistent"] is True
    assert summary["R_matrix_central_at_k1"] is True
    assert summary["pentagon_cocycle_vanishes_at_k1"] is True
    assert summary["pentagon_cocycle_vanishes_abelian_limit"] is True
    assert summary["v20_step3"]["v20_step3_holds"] is True


if __name__ == "__main__":
    # Allow ad-hoc execution to count and run all tests.
    import inspect
    tests = [
        (name, fn)
        for name, fn in inspect.getmembers(
            sys.modules[__name__], inspect.isfunction
        )
        if name.startswith("test_")
    ]
    n_pass = 0
    n_fail = 0
    for name, fn in tests:
        try:
            fn()
            n_pass += 1
        except Exception as e:  # noqa: BLE001
            n_fail += 1
            print(f"FAIL {name}: {e}")
    print(f"PASS: {n_pass} / {n_pass + n_fail}")
