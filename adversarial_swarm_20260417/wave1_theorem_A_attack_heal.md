# Wave-1 Adversarial Attack on Theorem A
## Modular Koszul Duality Programme, Volume I
## 2026-04-17, Beilinson-tradition adversarial audit

Targets: `chapters/theory/ftm_seven_fold_tfae_platonic.tex` (736 lines) and
`chapters/theory/theorem_A_infinity_2.tex` (1556 lines). Both read in full.
Cross-checks against `chapters/theory/chiral_koszul_pairs.tex` (filtered
comparison, PBW criterion, Kac-Moody Koszulness) and
`chapters/theory/higher_genus_modular_koszul.tex` (HS-sewing, hypothesis (c),
PBW propagation).

The status row in CLAUDE.md asserts Theorem A is "PROVED unconditional
(fixed curve + relative smooth + M-bar_{g,n} including boundary for standard
landscape)". The five proof-vehicle claims are:
(i) genus-0 seven-fold hub-and-spoke TFAE;
(ii) hypothesis-(c) base-change via BD holonomic + GR17 six-functor formalism;
(iii) Mok25 log-FM nodal sewing chain-level convergence at nodes;
(iv) Theorem A^{infty,2} R-twisted Sigma_n descent;
(v) PTVV / factorisation-homology alternative H01 upgraded.

After whole-file reading, only (i) and a restricted form of (iv) survive
unconditional inscription. Items (ii), (iii), (v) are partly phantom or
demoted in the actual .tex. The status-row "PROVED unconditional ... including
boundary" is overclaimed; the load-bearing modular-family steps are not
inscribed.

---

## Attack Findings

### F1. Phantom citation `rem:kac-moody-filtered-comparison` (CRITICAL)

The "non-tautology witness" of Spoke 4 in
`prop:class-L-witness` (FTM file, lines 606-630) cites
`Remark~\ref{rem:kac-moody-filtered-comparison}` as the load-bearing input
specifying *which* Kashiwara filtration on the vacuum module is used to
upgrade associated-graded Koszulity to filtered Koszulity for affine KM
on P^1. A grep across `chapters/` returns ZERO matches for the label. This
is AP190 (hidden import) and AP209 (missing lemma cited).

Consequence: clause (iii) of `prop:class-L-witness` ("the filtered-comparison
lemma is load-bearing") asserts a contingency on a non-existent remark. The
V_k(sl_2) witness for Spoke 4's non-tautology is therefore unsubstantiated at
the chiral level. The forward implication of Spoke 4 is unaffected (it goes
via the cone identification, which does exist as
`lem:twisted-product-cone-counit`); but the *reverse* direction's
non-tautology claim (`prop:no-tautology-at-g0`) loses its concrete witness.
The general filtered-comparison lemma `lem:filtered-comparison` (chiral_koszul_pairs.tex:348-374)
exists and is proved, but it requires "the filtration is exhaustive,
complete, and bounded below" -- a hypothesis that the Kashiwara filtration
on V_k(g) is supposed to satisfy, but the supposed verification is the
phantom remark.

### F2. Spoke 5 forward direction is tautological at g=0

`prop:ftm-spoke-bar-conc-pbw` (Spoke 5) claims bidirection
"bar concentration in weight 1" iff "PBW E_2-collapse". The forward direction
proof (FTM file, lines 334-340) reads: "bar-weight concentration ... forces
all PBW differentials d_r = 0 for r >= 2: a nonzero d_r with r >= 2 would
move weight and hence break concentration." This is unfolding of definitions:
PBW E_2-collapse is *defined* as d_r = 0 for r >= 2 acting on the weight
filtration, and "bar concentration in a single weight per bar degree" is
the assertion that the same filtration has E_infty supported in one weight.
The "would break concentration" argument is a one-line consequence of weight
preservation by d_1 plus the fact that any nonzero d_r raises filtration
weight. Calling this an "independent bidirection" inflates a definitional
identity to a theorem. Spoke 5 is the weakest of the six and should be
explicitly noted as a definitional reformulation, not a proof obligation.

### F3. Spoke 6 is parametrised but the seven-fold TFAE statement is not so qualified

`thm:ftm-seven-fold-tfae-via-hub-spoke` (FTM file, lines 165-191) states the
seven-fold TFAE for an arbitrary "augmented chiral algebra ... equipped with
a PBW filtration", with all seven conditions equivalent. Spoke 6 itself is
then proved only on the *class-G stratum*
(`prop:ftm-spoke-sc-pbw`, lines 370-388) and `rem:sc-formal-parametrised-scope`
(lines 390-403) explicitly states "the *unparametrised* bidirection ... is
false as stated" -- because class L, C, M algebras are Koszul but NOT
SC-formal. The theorem statement therefore advertises a seven-fold equivalence
that the body of the chapter immediately retracts. AP193 (biconditional, only
forward / restricted direction proved) and AP232 (duality-clause family-scope
overclaim).

The honest formulation: at g=0 there is a SIX-fold TFAE on the full Koszul
locus (Spokes 1-5 plus the hub) and a SEVEN-fold TFAE on the class-G stratum
(adding SC-formality). The "seven-fold TFAE" headline is at best a
class-G-conditional theorem.

### F4. Spoke 5 fails forward at g >= 1 outside class G; "extension" claim is reversed

`cor:TFAE-extends-to-genus-1-uniform-weight` (FTM file, lines 487-520) admits
that Spoke 5 "loses its forward implication at g >= 1 outside class G",
because d_fib^2 = kappa * omega_g produces a weight-2 cocycle whenever
kappa != 0. The corollary then claims Spokes 1-4 "persist at genus 1 ...
the uniform-weight scalar curvature kappa(A)*omega_g enters the bar
differential at fiberwise level but preserves the PBW filtration, so the
E_2-collapse equivalence lifts." But this is a forward-only persistence
(PBW E_2 collapse continues to characterise a distinguished property),
not a bidirection: the *content* of the bidirection at g >= 1 is what
"twisted tensor acyclic" or "counit qi" *means* on the universal curve,
which involves the BV/curved-A_inf machinery, not the flat g=0 bar-cobar.
The "lifts" claim is asserted, not proved; the corollary references no
chain-level theorem witnessing it. AP200 (transfer theorem gap: g=0 result
asserted to apply at g>=1 without proof).

### F5. Hypothesis (c) base-change citation is to a non-existent layer of GR17

The status row claims "hypothesis (c) base change proved via BD holonomic +
GR17 Vol II six-functor formalism on relative Ran prestack". The actual .tex
file `theorem_A_infinity_2.tex` cites `[Chapter~IV.5, Theorem~3.1.2]{GR17}`
for the (infty,2)-enhancement of the factorization model structure (lines 638,
1243, 1249) and `[Chapter~I.3]{GR17}` for stability/presentability (line 634).
Nowhere in the chapter is hypothesis (c) "base change on the relative Ran
prestack" stated as a theorem with a proof. The phrase
`relative Ran` does not appear in the FTM or A^{infty,2} chapters. Hypothesis
(c) of `thm:pbw-universal-semisimple` is "g is semisimple" (the Whitehead-input
hypothesis used for class-L universal PBW), not a base-change condition;
the status row appears to conflate two distinct hypothesis (c)'s.
AP191 (circular proof chain via mis-attributed citation) + AP-CY32
(reorganisation != bypass).

### F6. Mok25 log-FM nodal sewing: no chain-level theorem inscribed

A grep for `nodal sewing theorem`, `sewing.*nodes`, `chain-level at nodes`,
`node.*factorization` across all of `chapters/` returns ZERO matches. The
Mok25 log-FM compactification is invoked in the
`lem:R-twisted-descent` proof (theorem_A_infinity_2.tex:958-991) for the
*horizontal* extension of the local system L_R across the diagonal strata
of Conf^ord_n(X), which is on a single fixed curve, NOT the *modular*
nodal sewing on M-bar_{g,n}. The status-row claim that nodal sewing is
"chain-level at nodes" via "Francis-Gaitsgory factorization-gluing +
HS-sewing convergence" has no corresponding theorem in the .tex; HS-sewing
appears only in `higher_genus_modular_koszul.tex` (Tier 2, analytic
convergence on the Siegel upper half-space H_g, not on M-bar_{g,n}
boundary), and even there it is *analytic* convergence, not chain-level
algebraic gluing. AP190 (hidden import) at the modular-family level.

### F7. PTVV / H01 alternative is *not* upgraded to a proposition; it remains a conjecture

The status row claims "PTVV/factorization-homology alternative H01 upgraded
to proposition". The actual content of `theorem_A_infinity_2.tex` lists
PTVV only in `conj:lagrangian-koszul-converse` (line 1404), which is
explicitly a CONJECTURE for the *converse* direction, not an alternative
proof of Theorem A itself. No chapter contains a "PTVV alternative" proof
of Theorem A. AP149 (resolution propagation failure: status-row update
not reflected in .tex). The "genuinely independent (no Verdier-pair
hypothesis)" upgrade is inscribed for Theorem C in
`chapters/theory/c_strengthening.tex` (mentioned in CLAUDE.md status row
for Theorem C), NOT for Theorem A. The status-row conflation of
H01-for-A with the Theorem-C PTVV alternative is a confabulation.

### F8. R-twisted Sigma_n descent: pure braid -> Sigma_n extension is the AP-CY30 trap

`lem:R-twisted-descent` Step 1 (theorem_A_infinity_2.tex:953-956) asserts:
"The classical Yang-Baxter equation R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}
on codimension-2 loci ensures that the representation of the pure braid
group PB_n(X) extends to a representation of the symmetric group Sigma_n
on the boundary of a fundamental domain." This is exactly the AP-CY30 trap
("factored != solved": YBE does NOT imply ZTE). YBE on PB_n produces a
braid-group representation; extending to Sigma_n requires the additional
*unitarity* condition R(z)R^{op}(-z) = id (or equivalently R^2 = id at
coincident spectral parameters). The proof omits this hypothesis. For
the rational Yangian Y_hbar(g), unitarity holds; for the trigonometric
quantum group U_q(g-hat), unitarity holds at generic q; for the elliptic
case (Belavin), unitarity is convention-dependent. The lemma as stated is
therefore conditional on an unstated unitarity hypothesis on R(z), not on
YBE alone.

### F9. Theorem A^{infty,2} requires hypothesis (H3) explicitly

The chapter explicitly admits (line 86-94) that hypothesis (H3) (finite-dim
graded bar pieces) is restrictive: "the non-finitely-generated MC4-completion
regime fails (H3) and is therefore the sole genuinely open frontier
(Conjecture Pi 4)". The CLAUDE.md status row collapses this into "PROVED
unconditional ... finitely generated standard landscape unconditional",
which is correct *modulo* the qualifier; but the bare phrase "PROVED
unconditional" without scope is misleading. AP215 (preface advertising
stronger than proved). The honest summary: Theorem A^{infty,2} is proved
under (H1)+(H2)+(H3); the standard finitely generated landscape satisfies
all three; the unbounded-rank regime is open as Pi 4.

### F10. Step 2 of A^{infty,2} proof uses a Mittag-Leffler claim without verification

Step 2 (theorem_A_infinity_2.tex:824-844) asserts "convergence of the
spectral sequence to the unit morphism is the Mittag-Leffler property for
the bar-length filtration under conilpotent-completeness." Conilpotent-
completeness ensures lim^1 vanishes for the *coradical* filtration on
the codomain coalgebra, not directly for the bar-length filtration on
the bar of an algebra. The two filtrations are dual, but the
identification requires (H2) (augmentation-ideal completeness on the
algebra side) which is then used to invoke Positselski 2018. The chapter
gestures at this via the (H2) hypothesis but does not exhibit the Mittag-
Leffler argument explicitly. AP194 (curved complex with flat tools, here
in reverse: a coalgebra Mittag-Leffler argument is invoked via an algebra
hypothesis without bridging).

---

## Survivors

After the attack, the following content of the inscribed Theorem A holds
unconditionally:

(S1) **Hub-and-spoke at g=0 on the Koszul locus, six-fold TFAE.**
The bidirections Spokes 1-5 with the PBW E_2-collapse hub hold for any
augmented chiral algebra on a smooth genus-0 curve with a PBW filtration
satisfying exhaustion, completeness, and bounded-below. The proofs route
through `thm:fundamental-twisting-morphisms` (LV12 chiral analogue),
`thm:pbw-koszulness-criterion`, `lem:filtered-comparison`,
`lem:twisted-product-cone-counit`, and `thm:bar-concentration`. The
non-tautology of Spoke 4's reverse direction is supplied by
`lem:filtered-comparison` (which exists and is proved), even though
the Kac-Moody-specific witness in `prop:class-L-witness`(iii) is phantom
(F1).

(S2) **Theorem A^{infty,2} on the conilpotent-complete locus under
(H1)+(H2)+(H3).** The Koszul reflection K^2 ~ id is established as an
adjoint equivalence in Fact(X) under the star product, with the explicit
properad lift via Hackney-Robertson. The pole-free-point restriction
recovers LV12 verbatim. (H3) is satisfied throughout the finitely
generated standard landscape.

(S3) **R-twisted Sigma_n descent on the Conf^ord_n(X) top stratum,
under unitarity of R(z).** Step 2 of `lem:R-twisted-descent` (the
Grothendieck-fibre-type descent on the open configuration space) is
correct. The extension across diagonal strata via Mok25 nearby cycles
is plausible but not chain-level inscribed; the unitarity hypothesis on
R(z) needs to be made explicit (F8).

(S4) **Spoke 6 (SC-formality) as a class-G *characterisation*** (NOT a
class-G-restricted equivalence with the PBW hub). On the standard
landscape, SC-formality is equivalent to class-G membership; this is
`prop:sc-formal-iff-class-g`.

---

## Platonic Reconstitution

### Theorem A (Koszul Reflection, Beilinson-rectified scope)

Let X be a smooth quasi-projective curve over a field k of characteristic
zero. Let A be a factorization E_1-algebra on X satisfying:
- (H1) augmentation: A in Alg^{fact,aug}_X;
- (H2) augmentation-ideal completeness: A ~ lim_n A / bar A^n;
- (H3) finite-dim graded bar pieces: each conformal-weight space of
  Bbar^ch_X(A) is finite-dimensional.

Then the chiral bar and chiral cobar functors assemble into an adjoint
equivalence

  K = Bbar^ch_X : Alg^{fact,aug,comp}_X <-> CoAlg^{fact,conil,co}_X : K^{-1} = Omega^ch_X

of stable presentable (infty,1)-categories under the Francis star-product
ambient Fact(X). The equivalence satisfies:

(A1) **Adjoint equivalence on the conilpotent-complete locus.** Unit
eta_A : A -> Omega^ch_X Bbar^ch_X(A) and counit eps_A : Bbar^ch_X
Omega^ch_X(C) -> C are weak equivalences in the coderived
(infty,1)-category D^co.

(A2) **Chain-level involutivity K^2 ~ id on the Koszul locus Kosz(X).**
Both unit and counit are chain-level quasi-isomorphisms on Kosz(X), which
contains the entire finitely generated standard landscape (Heisenberg, all
affine Kac-Moody at non-critical levels, Virasoro at generic c, principal
W_N at generic Psi, lattice VOAs, betagamma, bc).

(A3) **Properad lift via Hackney-Robertson.** The adjoint equivalence
extends along Fact-Op(X) -> Fact-Prop(X), with bar and cobar as
graph-wise extensions; the (infty,2)-enhancement uses GR17 Chapter IV.5
Theorem 3.1.2.

(A4) **Pole-free-point restriction.** Pullback along {pt} -> Ran(X)
recovers LV12 Theorem 11.4.1 for the (Ass, Ass^!) Koszul pair, verbatim.

(A5) **R-twisted Sigma_n descent on Conf^ord_n(X), conditional on
unitarity of R(z).** For E_1-chiral A with classical R-matrix R(z)
satisfying YBE *and* R(z)R^{op}(-z) = id, the symmetric bar
Bbar^Sigma_n(A) is the L_R-twisted Sigma_n-coinvariant descent of
B^ord_n(A) on the Conf^ord_n(X) top stratum; extension to lower
diagonal strata is conditional on the inscribed Mok25 log-FM
nearby-cycle compatibility, which is currently proved on the
configuration space level only and NOT lifted to chain-level
factorization gluing on M-bar_{g,n}.

### Genus-0 hub-and-spoke (six-fold TFAE on Koszul locus, seven-fold
on class-G stratum)

For A as above with PBW filtration on the genus-0 fiber, the conditions

(i) chiral Koszul morphism;
(ii) counit qi;
(iii) unit weak equivalence;
(iv) twisted tensor acyclicity (both K^L_tau and K^R_tau);
(v) bar concentration in weight 1;
(vi) PBW E_2-collapse [HUB]

are TFAE on the full Koszul locus Kosz(X) by hub-and-spoke (five
bidirections to (vi); transitivity supplies the remaining ten). On the
class-G sub-stratum, condition

(vii) SC-formality

is added to the TFAE list as the seventh equivalent condition; for class
L, C, M, conditions (i)-(vi) hold but (vii) fails. The non-tautology of
the (iv) <-> (vi) bidirection is via `lem:filtered-comparison` (existing
and proved), independent of any Kac-Moody-specific witness.

### Genus-extension scope ledger

(g0-Span) Spokes 1-4 (the (i),(ii),(iii),(iv) <-> (vi) bidirections) extend
unconditionally to genus 1 *only on the uniform-weight lane*, and only as
*forward* persistence (PBW E_2-collapse continues to characterise these
properties on the universal curve over M-bar_{1,n}). Bidirection content
at g >= 1 requires curved A_infty / BV machinery and is NOT inscribed at
chain level in the FTM seven-fold chapter; it is the subject of MC5
(weight-completed; class M chain-level on direct-sum genuinely false).

(g0-Spoke5) (v) <-> (vi) at g >= 1 holds only in class G; outside class G
the forward implication "(v) => (vi)" specialises to "(v) => kappa(A) = 0",
which (on the standard landscape) forces class G.

(g0-Spoke6) (vii) <-> class-G persists at every genus on the class-G
stratum (Wick-contraction).

(M-bar) The full M-bar_{g,n} extension "including boundary" claimed in
the status row is NOT inscribed at chain level. The K-theoretic
filtration globalisation (Theorem D template, status row D entry) and
the PTVV alternative (status row entry, but not inscribed in the Theorem
A chapters) remain the planned vehicles; their inscription is OUTSTANDING.

### Proof skeleton (no circular routings)

Step 1 (adjunction in Fact(X)): Francis 2012 Section 4 plus the
universal property of free/cofree constructions; cite GR17 Chapter IV.5
Section 2.4 for the (infty,1) enhancement. Primitive anchor:
Francis-Gaitsgory star-product symmetric monoidal structure.

Step 2 (unit/counit equivalences on conilpotent-complete locus):
spectral sequence on bar-length filtration, exhaustion via (H2), each
graded piece is the classical LV12 Koszul complex over {pt}, then
star-product base-change exactness from GR17 Chapter IV.5 Section 1.3.
Convergence: Mittag-Leffler via (H2) on the algebra side, dualised via
(H1) augmentation. Primitive anchor: Positselski 2018 Theorem 9.1
(weakly curved bar-cobar Quillen equivalence).

Step 3 (properad lift): Hackney-Robertson 2019 Proposition 6.3
(transfer-stable model structure under symmetric monoidal left
adjoints). Primitive anchor: Hackney-Robertson, model-independent.

Step 4 (pole-free restriction): direct pullback identification with
LV12 Theorem 11.4.1. Primitive anchor: LV12.

Step 5 (R-twisted descent on Conf^ord top stratum, under unitarity):
classical Grothendieck fibre theory on the principal Sigma_n-torsor
Conf^ord_n(X) -> Conf_n(X). Primitive anchor: standard descent.

---

## Open Frontier Items

(OF1) **Inscribe modular-family extension to M-bar_{g,n} including
boundary.** The status-row "modular-family PROVED" sentence cites a
chain "BD holonomic + GR17 six-functor + Mok25 log FM + Francis-Gaitsgory
factorization-gluing + HS-sewing convergence" that is not assembled in
any chapter. Either (a) inscribe an explicit "modular-family Theorem A"
chapter that assembles the chain at chain level, or (b) demote the
status-row claim to "Genuinely open chain-level on M-bar_{g,n}; weight-
completed via MC5; analytic convergence via HS-sewing on H_g" -- which
is what the .tex actually supports.

(OF2) **Heal the phantom `rem:kac-moody-filtered-comparison`** (F1):
either inscribe the remark with the Kashiwara-filtration-on-vacuum-
module statement plus its verification (citing Kashiwara-Tanisaki or
analogous), or drop clause (iii) of `prop:class-L-witness` and rephrase
the V_k(sl_2) witness as "the filtered comparison lemma applies given
generic level k; the Kashiwara filtration verification is the standard
PBW-on-vacuum-module computation, see [reference]".

(OF3) **State unitarity hypothesis on R(z) in `lem:R-twisted-descent`**
(F8). Either restrict to unitary R-matrices (Yangian rational, U_q
trigonometric at generic q), or extend the lemma with an explicit
non-unitary discussion.

(OF4) **Demote the "seven-fold TFAE" headline to "six-fold TFAE on
Koszul locus + seventh on class-G stratum"** (F3). The current statement
of `thm:ftm-seven-fold-tfae-via-hub-spoke` advertises a class-restricted
equivalence as if it were universal. The class-G qualification belongs
in the theorem statement, not in a downstream remark.

(OF5) **Inscribe PTVV alternative for Theorem A** (F7), or remove it
from the status-row claim. The current status-row sentence
"PTVV/factorization-homology alternative H01 upgraded to proposition
... genuinely independent (no Verdier-pair hypothesis)" matches the
Theorem-C PTVV upgrade, not Theorem A. Cross-volume conflation; AP149
healing required.

(OF6) **Spoke 5 forward direction at g=0** (F2): mark explicitly as a
definitional reformulation, not a separate proof obligation. Reduces
the Spoke 5 bidirection's content to its reverse direction
(`thm:bar-concentration` + Spoke 1).

(OF7) **MC4-completion regime / Conjecture Pi 4** (the standing open
frontier explicitly inscribed in the chapter). Status: open by
construction, decorative for current applications.

---

## Verdict

The seven-fold TFAE at g=0 *survives the attack as a six-fold TFAE on the
full Koszul locus, augmented by a seventh equivalence on the class-G
stratum*. The hub-and-spoke architecture is correct; the "21-arrow
adversarial objection" is correctly diffused; Spokes 1-4 are genuinely
non-tautological via the existing `lem:filtered-comparison`. Theorem
A^{infty,2} on the conilpotent-complete locus under (H1)+(H2)+(H3) holds
as inscribed, with the proof via Francis-Gaitsgory + Hackney-Robertson +
Positselski + LV12.

The status-row overclaim "PROVED unconditional ... including boundary
... PTVV alternative upgraded" is NOT supported by the .tex. The
load-bearing modular-family extension to M-bar_{g,n} including the
boundary divisor is not inscribed; the cited chain (GR17 Vol II
six-functor + Mok25 nodal sewing + Francis-Gaitsgory factorization-
gluing + HS-sewing) is not assembled in any chapter; the PTVV
alternative belongs to Theorem C, not Theorem A. The honest summary is:

**Theorem A is proved on a smooth fixed curve at g=0 (six/seven-fold
TFAE) and at the (infty,2)-properad level on the conilpotent-complete
locus under (H1)+(H2)+(H3) (which is satisfied throughout the
finitely generated standard landscape). Genus-1 forward persistence
of Spokes 1-4 holds on the uniform-weight lane. The full M-bar_{g,n}
chain-level extension, the unitary R-matrix discipline in the
ordered-to-symmetric descent lemma, and the phantom Kac-Moody
filtered-comparison remark are all open inscription targets.**

This is a stronger and more durable statement than the current
status-row prose, because it is recoverable line-by-line from the
.tex without any phantom citations.

---
