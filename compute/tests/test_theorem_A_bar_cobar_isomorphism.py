"""
Independent verification decorator for Theorem A
(\\label{thm:bar-cobar-isomorphism-main}).

Theorem A (geometric bar-cobar duality) asserts that for a chiral Koszul
pair (A, C, tau, F_bullet) on a smooth curve X, the canonical unit
    C -> B_X(A)
is a weak equivalence of conilpotent complete factorization coalgebras on
Ran(X), and the canonical counit
    Omega_X(C) -> A
is a quasi-isomorphism of factorization algebras on X.

Derivation source (the manuscript's proof path):
  - Koszul-Moore twisting-morphism adjunction (Loday-Vallette 2012 Ch.11)
    adapted to the chiral/factorization setting;
  - BD-sheaf filtered comparison on the chiral Koszul pair;
  - Mok 2025 logarithmic Fulton-MacPherson compactification for nodal
    gluing.

Independent verification sources (disjoint from the derivation path):
  - Lurie *Higher Algebra* (HA) Section 5.2 inf-categorical bar-cobar
    adjunction, presented as a nerve-realization duality between augmented
    E_1-algebras and coaugmented E_1-coalgebras. HA is category-theoretic
    and makes no reference to BD factorization sheaves, to twisting
    morphisms, or to the explicit chiral Koszul pair; its input is the
    stable monoidal infinity-category structure on ModR.
  - PTVV 2013 (arXiv:1111.3209): 1-shifted symplectic structure on
    RMap(M_bar_g, BG_A) combined with Costello-Gwilliam factorization
    homology provides a Lagrangian-correspondence route to the same
    bar-cobar identification at genus 0 / over a fixed curve, via
    derived-symplectic geometry. The derivation uses neither twisting
    morphisms nor the BD filtered comparison.

This test registers the independent-verification relationship and checks
the registry entry it installs. The anchor comparison itself (Heisenberg
frame inversion vs BD genus-0 acyclicity) is NOT yet implemented as a
computation anywhere in compute/lib; the test skips with that obligation
named rather than asserting an uncomputed agreement.
"""

from __future__ import annotations

import pytest

from compute.lib.independent_verification import (
    entries_for,
    independent_verification,
)


@independent_verification(
    claim="thm:bar-cobar-isomorphism-main",
    derived_from=[
        "Loday-Vallette 2012 twisting-morphism bar-cobar adjunction "
        "(Ch. 11) adapted to chiral setting",
        "BD-sheaf filtered comparison on chiral Koszul pair "
        "(Beilinson-Drinfeld 2004)",
        "Mok 2025 logarithmic Fulton-MacPherson nodal gluing",
    ],
    verified_against=[
        "Lurie HA Section 5.2 infinity-categorical bar-cobar "
        "nerve-realization adjunction",
        "PTVV 2013 arXiv:1111.3209 1-shifted symplectic structure on "
        "RMap(Mbar_g, BG_A) via factorization homology (Costello-Gwilliam)",
    ],
    disjoint_rationale=(
        "The derivation uses Loday-Vallette twisting morphisms and BD "
        "factorization sheaves -- both are explicit operadic/sheaf-level "
        "machinery on Ran(X). Lurie HA's bar-cobar adjunction is purely "
        "infinity-categorical (nerve and realization between presentable "
        "stable E_1-algebra/coalgebra categories) and makes no use of "
        "twisting morphisms, BD sheaves, or log FM. PTVV's shifted-"
        "symplectic / factorization-homology route uses derived-symplectic "
        "geometry on mapping stacks and Costello-Gwilliam factorization "
        "homology; neither pipeline references twisting morphisms or the "
        "chiral Koszul-pair filtration. The three source sets are "
        "disjoint as machinery."
    ),
)
def test_theorem_A_bar_cobar_isomorphism_independent_structure():
    """Registry consistency plus an explicit open computational obligation.

    The only content this harness genuinely computes is the
    independent-verification registry relationship installed by the
    decorator (source disjointness, module scan). That is asserted below.

    The mathematical anchor comparison itself -- Heisenberg frame
    inversion (Section 'frame-inversion' of chiral_koszul_pairs.tex)
    against BD genus-0 acyclicity (thm:BD-genus-zero) -- has no
    implemented computation in compute/lib: no engine exposes a
    frame-inversion witness or a BD-acyclicity witness that could be
    compared. The obligation is recorded as a skip so it stays visible
    instead of silently passing.
    """
    entries = entries_for("thm:bar-cobar-isomorphism-main")
    assert entries, (
        "decorator failed to register the IV relationship for "
        "thm:bar-cobar-isomorphism-main"
    )
    assert all(not e.is_tautological() for e in entries), (
        "IV registry entry for thm:bar-cobar-isomorphism-main is "
        "tautological (derivation and verification sources overlap)"
    )
    assert all(not e.manuscript_read_paths for e in entries), (
        "this module must not read manuscript .tex files at runtime"
    )
    pytest.skip(
        "obligation: chain-level anchor comparison (Heisenberg frame "
        "inversion vs BD genus-0 acyclicity) not yet implemented as a "
        "computation; only the IV registry relationship is verified here"
    )
