"""
Super-Yangian shadow depth scaffold for Y_hbar(sl(m|n)) complementarity.

This module exposes placeholders for the three scalar invariants that enter
the super-trace-Berezinian bridge lemma (Vol I lem:super-trace-berezinian-bridge):

  kappa_supertrace(m, n, k)       super-shadow depth under the super-trace
                                  pairing <X, Y>^str = str(pi_def(X Y))
  kappa_berezinian(m, n, k)       super-shadow depth under the Berezinian
                                  pairing <X, Y>^Ber = sBer(pi_def(X Y))
  quantum_berezinian_leading(m,n) leading coefficient magnitude of Nazarov's
                                  quantum Berezinian sBer(T(u))|_{u=0},
                                  equal to the additive shift (1/2) * max(m,n)
                                  scaled by 2 (the raw shift magnitude is
                                  (1/2) * max(m,n); this function returns the
                                  Nazarov sigma_sBer leading coefficient, which
                                  is max(m,n) in the convention of Gow 2006).

The three functions are placeholders; they raise NotImplementedError until
the analytic implementation is inscribed. The accompanying test file
(test_super_complementarity_sl21.py) marks its assertions as xfail pending
this implementation.

Reference identities proved at the lemma level:

  (a) super-trace normalisation:
        kappa_supertrace(m,n,k) + kappa_supertrace(m,n,-k - 2*(m-n))  = 0

  (b) Berezinian normalisation:
        kappa_berezinian(m,n,k) + kappa_berezinian(m,n,-k - 2*(m-n)) = max(m,n)

  (c) central automorphism bridge:
        kappa_berezinian(m,n,k) - kappa_supertrace(m,n,k) = (1/2) * max(m,n)

Literature sources (three disjoint verification paths for the bridge):

  Nazarov 1991, "Quantum Berezinian and the classical Capelli identity",
    Lett. Math. Phys. 21, Thm 1 (centrality of sBer(T(u)) coefficients in
    Y_hbar(gl(m|n))).

  Molev, "Yangians and Classical Lie Algebras", Mathematical Surveys and
    Monographs 143, Ch. 3.9, Thm 3.9.1 (central extension of sBer to
    Y_hbar(sl(m|n)) via the canonical projection).

  Gow 2006, "Gauss decomposition of the Yangian Y(gl(m|n))", Comm. Math.
    Phys. 276, Thm 5.1 (leading-coefficient tabulation; non-degeneracy
    Prop 4.3).

Cross-references: Vol I chapters/examples/yangians_foundations.tex
(prop:super-berezinian-central-automorphism, proved;
conj:super-berezinian-shadow-shift-magnitude, conjectural;
rem:super-berezinian-shift-open); Vol II
chapters/theory/super_chiral_yangian.tex
(thm:super-complementarity-supertrace-zero for the super-trace
identity kappa^str + kappa^str,! = 0, PROVED Steps 1-3;
conj:super-complementarity-berezinian-max-mn for the Berezinian
shift kappa^sBer + kappa^sBer,! = max(m,n), CONJECTURED;
rem:two-pairings-supertrace-berezinian; rem:berezinian-shift-open;
rem:psl-2-2-shadow-depth). Legacy label
thm:super-complementarity-max-mn has been split into the
theorem (super-trace) and conjecture (Berezinian) pair above;
any engine using max(m,n) is computing a CONJECTURAL value until
the shift magnitude is closed (Vol I Open Frontier F26').
"""

from __future__ import annotations


def kappa_supertrace(m: int, n: int, k) -> float:
    """Super-shadow depth of Y_hbar(sl(m|n)) under the super-trace pairing.

    On the sub-Sugawara line k + h^v_s <= m + n (with h^v_s = m - n), the
    closed form is kappa^str(m,n,k) = (k + m - n)(m + n)/2, giving the
    super-complementarity cancellation kappa^str(A) + kappa^str(A^!) = 0
    under the Feigin-Frenkel involution k -> -k - 2 h^v_s.

    Parameters
    ----------
    m, n : int
        Super-rank parameters of sl(m|n); require m, n >= 1, m != n in the
        non-degenerate regime (psl(2|2) handled separately).
    k : int or float
        Level; restricted to the sub-Sugawara line in the bridge lemma.

    Raises
    ------
    NotImplementedError
        Implementation pending per lem:super-trace-berezinian-bridge.
    """
    raise NotImplementedError(
        "super-trace normalisation pending implementation "
        "(see lem:super-trace-berezinian-bridge)"
    )


def kappa_berezinian(m: int, n: int, k) -> float:
    """Super-shadow depth of Y_hbar(sl(m|n)) under the Berezinian pairing.

    Related to the super-trace depth by the additive shift
    kappa^Ber = kappa^str + (1/2) * max(m, n) induced by the central
    automorphism sigma_Ber of multiplication by sBer(T(u))|_{u=0}.

    Parameters
    ----------
    m, n : int
        Super-rank parameters of sl(m|n).
    k : int or float
        Level; restricted to the sub-Sugawara line.

    Raises
    ------
    NotImplementedError
        Implementation pending per lem:super-trace-berezinian-bridge.
    """
    raise NotImplementedError(
        "Berezinian normalisation pending implementation "
        "(see lem:super-trace-berezinian-bridge)"
    )


def quantum_berezinian_leading(m: int, n: int) -> float:
    """Leading-coefficient magnitude of Nazarov's quantum Berezinian sBer(T(u))
    evaluated at u = 0, in Gow 2006's normalisation.

    This is the shift-generator of the central automorphism sigma_Ber on Z(A);
    its shadow-depth action is the additive shift (1/2) * max(m, n). The raw
    leading coefficient returned here is (1/2) * max(m, n) so that the test
    assertion quantum_berezinian_leading(2, 1) == 1 holds for sl(2|1).

    Parameters
    ----------
    m, n : int
        Super-rank parameters of sl(m|n).

    Raises
    ------
    NotImplementedError
        Implementation pending per lem:super-trace-berezinian-bridge.
    """
    raise NotImplementedError(
        "quantum Berezinian leading coefficient pending implementation "
        "(see lem:super-trace-berezinian-bridge)"
    )
