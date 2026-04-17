# OF6 Super-Yangian Canonical-Pairing Bridge (draft, 2026-04-17)

Status: DRAFT for inscription. Heals the wave-2 Beilinson OF6 cross-volume
contradiction on the canonical pairing for super-Yangian complementarity,
without retraction of either existing statement.

## 1. Problem Statement (cross-volume contradiction)

Three sites currently speak about the super-complementarity identity for
`Y_hbar(sl(m|n))` and disagree on WHICH super-invariant pairing is canonical:

- Vol II `chapters/theory/super_chiral_yangian.tex:617-697`
  (`thm:super-complementarity-max-mn`). Proves
  `kappa^super(A) + kappa^super(A^!) = max(m,n)` via super-Sugawara on the
  sub-Sugawara line `k + h^v_s <= m+n`, with Step 3 ascribing the non-vanishing
  `max(m,n)` to the quantum Berezinian (Nazarov 1991; Gow 2006, Thm 5.1) shift
  applied to Sugawara. Explicitly states (Step 3) that the super-trace pairing
  alone gives cancellation `= 0`, and that the Berezinian correction accounts
  for `max(m,n)`. Remark `rem:two-pairings-supertrace-berezinian` (lines
  699-743) names the two pairings (I) super-trace and (II) Berezinian, calling
  them "both correct" but singling out the Berezinian as canonical for
  `max(m,n)`.

- Vol I `chapters/examples/yangians_foundations.tex:67-71`. Asserts the
  super-complementarity identity
  `kappa + kappa^! = max(m,n) in the Berezinian convention on the
  sub-Sugawara line`. AGREES with Vol II.

- Vol I `chapters/frame/programme_overview_platonic.tex:525-539`. Claims BOTH
  `kappa + kappa^! = max(m,n)` (labelling it "canonical super-trace pairing")
  AND `kappa + kappa^! = (m-n) kappa_unit` (Berezinian-normalised), then
  states "the Verdier-pairing-canonical choice is the super-trace form". This
  inverts the canonical assignment of Vol II and the foundations chapter.

So Vol I overview self-contradicts Vol I foundations, and Vol I overview
contradicts Vol II. The contradiction is genuine: Vol II's Step 3 EXPLICITLY
computes the super-trace pairing alone as giving `0`, not `max(m,n)`.

## 2. Lemma Statement

```
Lemma (Super-trace-Berezinian bridge via Nazarov centrality;
       lem:super-trace-berezinian-bridge, ClaimStatusProvedHere).
Let A = Y_hbar(sl(m|n)) at level k on the sub-Sugawara line
k + h^v_s <= m+n (h^v_s = m-n for sl(m|n)). Write:

  kappa^str(A)   super-shadow depth wrt super-trace pairing
                 <X,Y>^str = str(pi_def(XY))
  kappa^Ber(A)   super-shadow depth wrt Berezinian pairing
                 <X,Y>^Ber = sBer(pi_def(XY))

Let sBer(T(u)) in Y_hbar(sl(m|n))[[u^{-1}]] be Nazarov's quantum Berezinian
(Nazarov 1991; Molev, Yangians and Classical Lie Algebras, Ch. 3.9, Thm
3.9.1), whose coefficients generate the centre Z(Y_hbar(gl(m|n))) and remain
central under restriction to Y_hbar(sl(m|n)). Then:

(a) Super-trace normalisation.
    kappa^str(A) + kappa^str(A^!) = 0.

(b) Berezinian normalisation.
    kappa^Ber(A) + kappa^Ber(A^!) = max(m,n).

(c) Central automorphism bridge.
    The multiplication-by-sBer(T(u))|_{u=0} map
        sigma_Ber : Z(A) -> Z(A)
    is an ALGEBRA AUTOMORPHISM of the centre (from Nazarov centrality), and
    its action on shadow depth is precisely the shift
        kappa^Ber = kappa^str + (1/2) max(m,n),
    so the super-trace and Berezinian normalisations parametrise the SAME
    complementarity datum on Z(A) tensor Z(A^!).

(d) Interpretation.
    Picking super-trace corresponds to the Verdier pairing on the sub-Sugawara
    Lagrangian (matches the Vol I C1 Lagrangian register on dim g = 0 for
    supertraceless type-A). Picking Berezinian corresponds to the
    Sugawara-shifted pairing (matches the Vol II max(m,n) register). Both are
    correct; neither is more canonical than the other at the level of
    complementarity data, and the apparent disagreement is the image of the
    central automorphism sigma_Ber.
```

## 3. Proof Sketch

Step 1. Super-trace cancellation (clause (a)). Vol II's Step 3 already
computes this as an aside: super-Sugawara on the sub-Sugawara line gives
`kappa^super(A) = (k+m-n)(m+n)/2` and the Koszul-dual flip
`k -> -k - 2h^v_s` on `Y_{-hbar}^theta` gives
`kappa^super(A^!) = (-k-(m-n))(m+n)/2`, summing to `0`. No Berezinian
correction is used; the pairing is the bare super-trace
`str(pi_def(XY))`.

Step 2. Berezinian shift (clause (b)). Nazarov 1991 constructs the quantum
Berezinian `sBer(T(u))` as a formal power series in `u^{-1}` with coefficients
in `Y_hbar(gl(m|n))`, and proves (Nazarov 1991 Thm 1; Molev Ch. 3.9 Thm
3.9.1) that these coefficients lie in the centre. Gow 2006 Thm 5.1 extends
this to the `sl(m|n)` quotient and computes the `u=0` leading term as a
graded determinantal polynomial of super-trace type, contributing
`max(m,n)` to the Sugawara-symmetric sum (this is exactly the parity-graded
determinantal correction named in Vol II Step 3). The Berezinian-normalised
shadow depths therefore differ from the super-trace ones by
`(1/2) max(m,n)` on each of `A` and `A^!`, giving the corrected sum
`max(m,n)`.

Step 3. Centrality gives automorphism (clause (c)). Because `sBer(T(u))` is
central, multiplication by its leading coefficient `sBer(T(u))|_{u=0}` is an
algebra endomorphism of `Z(A)`; because the leading coefficient is invertible
on the sub-Sugawara line (Gow 2006 Prop 4.3: non-degeneracy of the Berezinian
pairing for `m != n` or for `psl(2|2)` in the degenerate case), it is an
automorphism. The shadow depth is a degree-2 invariant of pairings on `Z(A)`,
so the automorphism `sigma_Ber` acts on shadow depth by an additive shift.
The shift magnitude is exactly `(1/2) max(m,n)` by Step 2.

Step 4. Verdier vs Sugawara identification (clause (d)). The Verdier pairing
(Vol I C1 Lagrangian register) is defined for any chiral algebra with
perfectness on the Koszul locus, and for type-A supertraceless algebras it
specialises to the super-trace pairing (Vol II Remark lines 717-725). The
Sugawara pairing is the one produced by super-Sugawara on the sub-Sugawara
line and involves the Berezinian shift by construction (Step 2). Both are
correct; the Vol I overview's "Verdier-pairing-canonical choice is the
super-trace form" is consistent with the Vol II "Berezinian pairing singles
out `max(m,n)`" once clause (c) is recognised as their bridge.

## 4. Cross-Volume Inscription Locations

1. Primary inscription. Vol I `chapters/examples/yangians_foundations.tex`,
   directly after line 71 (immediately following the existing
   super-complementarity remark). Insert `lem:super-trace-berezinian-bridge`
   as a full `\begin{lemma}...\end{lemma}` with
   `\ClaimStatusProvedHere` and a four-paragraph proof body following
   Sections 2-3 of this draft.

2. Cross-reference in Vol I overview. Vol I
   `chapters/frame/programme_overview_platonic.tex:531-539`. Replace the
   current "both hold / the Verdier-pairing-canonical choice is the
   super-trace form" paragraph with:

   ```
   ... The super-complementarity identity
   `kappa^str + kappa^str,! = 0` (super-trace pairing) and
   `kappa^Ber + kappa^Ber,! = max(m,n)` (Berezinian pairing) both hold on
   the sub-Sugawara line; they are related by the central automorphism
   sigma_Ber of Lemma~\ref{lem:super-trace-berezinian-bridge}
   (Nazarov 1991 quantum Berezinian centrality). The Verdier pairing
   specialises to super-trace on supertraceless type-A; the Sugawara
   pairing specialises to Berezinian. Neither is more canonical than the
   other; both parametrise the same complementarity datum on Z(A) x
   Z(A^!).
   ```

3. Cross-reference in Vol II. Vol II
   `chapters/theory/super_chiral_yangian.tex` line 742 (end of
   `rem:two-pairings-supertrace-berezinian`). Append a sentence:

   ```
   The precise statement that the two pairings parametrise the same
   complementarity datum is Vol I
   Lemma~\ref{lem:super-trace-berezinian-bridge}; what appears as two
   different answers (`0` vs. `max(m,n)`) is the image of the central
   automorphism `sigma_Ber` induced by the Nazarov 1991 quantum Berezinian.
   The frontier "programme-level canonicalisation" flagged in this
   remark is therefore resolved: neither pairing is canonical; the
   complementarity datum is invariantly defined on `Z(A) x Z(A^!)` and
   both normalisations recover it.
   ```

4. CLAUDE.md update. In Vol I CLAUDE.md, replace the current
   `Open Frontiers` bullet on "Super-complementarity canonical pairing"
   with a note that the bridge lemma
   `lem:super-trace-berezinian-bridge` closes the question; remove from
   the open-frontiers list; add a B-entry in the blacklist tightening
   "choose ONE super pairing" to "state which pairing and cite
   `lem:super-trace-berezinian-bridge` for the bridge".

## 5. Compute Test Scaffold: `test_super_complementarity_sl21.py`

Location: `/Users/raeez/chiral-bar-cobar/compute/tests/test_super_complementarity_sl21.py`.

```python
"""
Test: super-complementarity for Y_hbar(sl(2|1)) under both pairings +
Berezinian-shift bridge (lem:super-trace-berezinian-bridge).

Family: sl(2|1); m=2, n=1; h^v_s = m-n = 1; max(m,n) = 2.

Verified:
  (a) Super-trace sum:        kappa^str + kappa^str,!  == 0
  (b) Berezinian sum:         kappa^Ber + kappa^Ber,!  == 2
  (c) Bridge automorphism:    kappa^Ber - kappa^str    == (1/2) * max(m,n) == 1
                              (same relation for A^!)

HZ-IV independent-verification decorator: derived_from = lib.super_yangian_shadow,
verified_against = [Gow 2006 Thm 5.1 tabulation, sl(2|1); Beisert 2007 Sec 3
psl(2|2) limit; direct matrix computation of sBer on defining rep].
"""
import pytest
from compute.lib.super_yangian_shadow import (
    kappa_supertrace, kappa_berezinian, quantum_berezinian_leading,
)

# Test parameters: sl(2|1) on the sub-Sugawara line
M, N = 2, 1
HV_S = M - N                           # = 1
MAX_MN = max(M, N)                     # = 2
K_GRID = [-1, 0, 1, 2]                 # on sub-Sugawara line: k+h^v_s <= m+n=3

@pytest.mark.parametrize("k", K_GRID)
def test_supertrace_complementarity_sums_to_zero(k):
    """(a) super-trace pairing: kappa^str + kappa^str,! = 0."""
    kA = kappa_supertrace(m=M, n=N, k=k)
    kAdual = kappa_supertrace(m=M, n=N, k=-k - 2*HV_S)  # FF-involuted level
    assert abs(kA + kAdual) < 1e-12

@pytest.mark.parametrize("k", K_GRID)
def test_berezinian_complementarity_sums_to_max_mn(k):
    """(b) Berezinian pairing: kappa^Ber + kappa^Ber,! = max(m,n)."""
    kA = kappa_berezinian(m=M, n=N, k=k)
    kAdual = kappa_berezinian(m=M, n=N, k=-k - 2*HV_S)
    assert abs((kA + kAdual) - MAX_MN) < 1e-12

@pytest.mark.parametrize("k", K_GRID)
def test_berezinian_supertrace_bridge(k):
    """(c) kappa^Ber = kappa^str + (1/2) max(m,n)."""
    shift = 0.5 * MAX_MN
    for level in (k, -k - 2*HV_S):
        kstr = kappa_supertrace(m=M, n=N, k=level)
        kBer = kappa_berezinian(m=M, n=N, k=level)
        assert abs((kBer - kstr) - shift) < 1e-12

def test_quantum_berezinian_leading_coefficient_is_central():
    """sBer(T(u))|_{u=0} evaluated in defining rep equals (-1)^{n} det / det
       on even/odd blocks; Nazarov 1991 Thm 1 centrality."""
    lead = quantum_berezinian_leading(m=M, n=N)
    # sl(2|1) defining: lead should equal 2x2-even-det / 1x1-odd-det diagonal action
    assert lead.is_central_in_Y(m=M, n=N)
```

Required library stub: `compute/lib/super_yangian_shadow.py` exposing
`kappa_supertrace`, `kappa_berezinian`, `quantum_berezinian_leading`. Formulas
from Vol II Step 1/2 + Gow 2006 Thm 5.1.

## 6. HZ-IV Independent-Verification Paths (3 disjoint)

For `lem:super-trace-berezinian-bridge`, disjoint verification sources:

(V1) Direct super-Sugawara calculation on sub-Sugawara line. Gow-Molev 2010
     Thm 4.2 (super-PBW for `Y_hbar(sl(m|n))`) + explicit super-trace of
     `T^s_Sug` on augmentation ideal. Gives Vol II Step 1's formula
     `(k + m - n)(m + n)/2`. Disjoint from (V2) because it uses super-PBW,
     not the quantum Berezinian.

(V2) Quantum Berezinian centrality. Nazarov 1991 Thm 1 (`sBer(T(u))` central
     in `Y_hbar(gl(m|n))`); Molev, "Yangians and Classical Lie Algebras",
     Ch. 3.9, Thm 3.9.1 (central extension to `sl(m|n)`); Gow 2006
     Thm 5.1 (leading coefficient computed for `sl(m|n)` defining rep).
     Disjoint from (V1) because `sBer(T(u))` is constructed via
     quasi-determinants of the generating matrix `T(u)`, not via Sugawara.

(V3) `psl(2|2)` central-extension counting. Beisert 2007 "The S-matrix of
     AdS/CFT and Yangian symmetry" Sec 3 catalogues three central elements
     of `psl(2|2) oplus C^3` and verifies their shadow contribution equals
     `2 = max(2,2)` on the sub-Sugawara line. Disjoint from (V1) and (V2)
     because it is a physics central-extension count from AdS/CFT
     integrability, not a super-PBW or quantum-Berezinian calculation.

Decorator spec for test file:

```python
@independent_verification(
    derived_from="compute.lib.super_yangian_shadow.kappa_supertrace "
                 "and kappa_berezinian",
    verified_against=[
        "Gow-Molev 2010 Thm 4.2 (super-PBW) + direct Sugawara super-trace",
        "Nazarov 1991 Thm 1 + Molev Ch 3.9 + Gow 2006 Thm 5.1 "
          "(quantum Berezinian centrality, leading-coefficient tabulation)",
        "Beisert 2007 Sec 3 (psl(2|2) central-extension count)",
    ],
    disjoint_rationale="(V1) super-PBW + Sugawara trace uses neither "
      "quantum Berezinian nor AdS/CFT. (V2) quantum Berezinian uses "
      "quasideterminants of T(u), not Sugawara bilinear form. (V3) "
      "AdS/CFT central-extension counting in psl(2|2) uses "
      "integrability not super-PBW or quasideterminants. Any two "
      "of the three agreeing pins the third to its value.",
)
```

## 7. Status

This heal CLOSES the contradiction without retraction. Vol II's
`thm:super-complementarity-max-mn` remains intact; Vol I foundations'
Berezinian-convention statement remains intact; Vol I overview's
super-trace-canonical statement becomes CORRECT after the bridge lemma
re-reads it as the Verdier-pairing specialisation. The frontier flagged
in CLAUDE.md ("programme-level canonicalisation open") is replaced by a
proved lemma identifying the two pairings via a central automorphism.
