# Wave-1 Attack-and-Heal on Theorem A (v2)
## 2026-04-18, Beilinson-tradition audit (second pass)
## Target: chapters/theory/theorem_A_infinity_2.tex (1596 lines at entry)

## Provenance

This note continues the 2026-04-17 Wave-1 audit inscribed at
`adversarial_swarm_20260417/wave1_theorem_A_attack_heal.md`. The prior audit
surfaced ten findings (F1-F10) and seven open frontiers (OF1-OF7). Since that
inscription:

- F1 phantom `rem:kac-moody-filtered-comparison` HEALED (label now inscribed at
  `ftm_seven_fold_tfae_platonic.tex:675`).
- OF1 modular-family scope PARTIALLY HEALED via
  `rem:A-infinity-2-modular-family-scope` at `theorem_A_infinity_2.tex:891`.
- F8 unitarity hypothesis on R(z): UNHEALED at entry.
- F10 Mittag-Leffler Step 2: UNHEALED at entry.
- OF5 PTVV-lane scope clarification: UNHEALED at entry.

The present note records the second-pass attack, the surviving core, and the
three targeted heals inscribed in this session.

## Attack ledger (second-pass findings)

- **F11 (HIGH, scope hypothesis missing).** `lem:R-twisted-descent` (Step 1,
  formerly line 988-994) asserts that classical YBE alone suffices to extend
  the pure-braid representation `PB_n` to a symmetric-group representation
  `Sigma_n`. Extension along the quotient map `PB_n -> Sigma_n` requires the
  relation `s_i^2 = id`, which at the monodromy level reads
  `R(z) R^{op}(-z) = id` (unitarity). YBE is a codimension-2 braid relation;
  unitarity is a codimension-0 involution relation; the two are independent.
  Category: AP7 (universal quantifier without type/convention restriction)
  + AP-CY30 (factored != solved).

- **F12 (MEDIUM, proof step with implicit-bridge hypothesis).** Step 2 of the
  main theorem proof (line 824-844 at entry) invokes Mittag-Leffler for the
  bar-length filtration under (H2) conilpotent-completeness. The argument is
  correct but elides the bridge: conilpotent-completeness on the coalgebra
  side controls the coradical filtration on the codomain, not the bar-length
  filtration on the domain. Bridging the two filtrations along the bar-cobar
  adjunction uses (H2) augmentation-ideal-completeness on the algebra side.
  The proof references (H2) but the ML argument needs to be exhibited.
  Category: AP194 (complex-with-flat-tools, reverse direction).

- **F13 (MEDIUM, cross-volume metadata drift).** The CLAUDE.md theorem-status
  table previously advertised a "PTVV alternative for Theorem A", with
  language matching the Theorem-C PTVV refinement (`chapters/theory/
  theorem_C_refinements_platonic.tex`, T9). The Wave-1 audit item OF5
  correctly diagnosed this as a cross-volume conflation: PTVV is a
  Theorem-C lane, not a Theorem-A lane. The Theorem-A chapter's HZ-IV
  decorator package lists three genuine alternative verification sources
  (Francis's chiral Deligne conjecture, Lurie HA Section 5.5, and
  Hackney-Robertson model-independence); no PTVV. Category: AP149
  (resolution propagation failure).

## Surviving core

Theorem A is an involutive symmetry `K^2 ~ id` that computes the chiral
duality invariant through two orthogonal dimensions: the Koszul locus (where
involutivity is chain-level) and the conilpotent-complete ambient (where
involutivity is coderived). The bar `K = Bbar^ch_X` and the cobar
`K^{-1} = Omega^ch_X` are coordinates; the invariant is the reflection
symmetry `K^2 ~ id`. Each of the eight prior parallel statements is a
coordinate-level reading of the one symmetry; each of the fourteen downstream
corollaries is a pullback along a restriction, a truncation, or a
sub-infty-2-specialisation.

The fixed-smooth-curve X scope is unconditional under (H1)+(H2)+(H3). The
R-twisted Sigma_n descent on Conf^ord_n(X) holds under the additional
unitarity hypothesis on R(z); the modular-family extension to
Mbar_{g,n} including boundary requires two uninscribed ingredients
(Francis-Gaitsgory six-functor base-change, Mok25 log-FM nodal sewing at
chain level) and is therefore CONDITIONAL.

## Heals inscribed this session

- **H11 (F8 unitarity):** SCOPE-RESTRICTED. `lem:R-twisted-descent` now
  carries two labelled hypotheses (R1) YBE and (R2) unitarity
  `R(z) R^{op}(-z) = id`. Step 1 of the proof explicitly invokes (R2) for
  the descent `PB_n -> Sigma_n`. A new scope remark
  `rem:R-descent-unitarity-scope` records which families satisfy (R2):
  rational Yangian Y_hbar(g) always, trigonometric U_q(g-hat) at generic q,
  Heisenberg/free-field trivial-R automatic, elliptic Belavin/Felder
  convention-dependent. Status tag unchanged (ClaimStatusProvedHere) since
  the lemma is unconditional on the rational + generic-trigonometric locus
  that exhausts the programme's concrete E_1-chiral witnesses. The correction
  is explicit hypothesis inscription, not a downgrade.

- **H12 (F10 Mittag-Leffler):** OBSTRUCTION-SHARPENED. New remark
  `rem:A-inf-2-ml-step-2` inscribes the Mittag-Leffler bridge: the bar-length
  filtration and the coradical filtration are varprojlim-dual under (H2),
  and (H3) finite-dim graded bar pieces ensures surjectivity of stage maps
  in every cohomological degree. When (H3) fails (Pi 4 regime), the
  obstruction is a varprojlim^1-class in H^{bullet+1}(Bbar^ch_X(A)); vanishing
  of this class is the precise chain-level obstruction to extending Theorem
  A^{infty,2} beyond (H3). This follows the AP266 sharpened-obstruction
  healing pattern: the deep-math extension to non-(H3) is not forced; the
  obstruction is given an explicit cohomological name, and the frontier item
  Conjecture Pi 4 is now quantitatively characterised as "the varprojlim^1
  obstruction class vanishes".

- **H13 (F13/OF5 PTVV scope):** DISAMBIGUATED. New remark
  `rem:A-inf-2-ptvv-scope` clarifies that PTVV is a Theorem-C lane and does
  not provide an alternative proof of Theorem A. The three genuine
  alternative verification sources for Theorem A (Francis's chiral Deligne,
  Lurie HA Section 5.5, Hackney-Robertson model-independence) are unchanged
  and installed as HZ-IV decorators. The PTVV inscription for Theorem C
  remains at `chapters/theory/theorem_C_refinements_platonic.tex`
  `thm:C-PTVV-alternative`; cross-volume programme metadata referring to a
  `PTVV-for-A alternative` should be read as a Theorem-C reference.

## Open frontier items carried forward

- (OF1) Modular-family extension to Mbar_{g,n} including boundary. Status
  unchanged from Wave-1: CONDITIONAL on Francis-Gaitsgory six-functor
  base-change and Mok25 log-FM nodal sewing at chain level; neither is
  inscribed in Vol I. `rem:A-infinity-2-modular-family-scope` records the
  honest ledger.
- (OF2) Kac-Moody filtered comparison HEALED (label inscribed since Wave-1).
- (OF3) Unitarity hypothesis HEALED this session (see H11).
- (OF4) Six-fold-vs-seven-fold TFAE discipline: FTM chapter already carries
  the honest split (six-fold Koszul-locus + seventh class-G); CLAUDE.md
  status row reflects this correctly. No action this session.
- (OF5) PTVV scope HEALED this session (see H13).
- (OF6) Spoke 5 forward-direction definitional reformulation: no action this
  session; FTM chapter carries the honest reading at g=0.
- (OF7) Pi 4 MC4-completion regime: sharpened this session (see H12) via
  the explicit varprojlim^1 obstruction class.

## Files touched

- `chapters/theory/theorem_A_infinity_2.tex` (inscription site; three edits:
  unitarity hypothesis into `lem:R-twisted-descent`, Step 1 proof update,
  three new scope remarks).

## Commit plan

No commit in this run per user's instruction. A follow-up commit authored by
Raeez Lorgat should include:

- the three heals above on `theorem_A_infinity_2.tex`;
- this note at `adversarial_swarm_20260418/wave1_theorem_A_attack_heal_v2.md`.

Cross-volume propagation: AP5 check completed. Vol II sites that cite
`lem:R-twisted-descent` do so by reference only (preface and factorization
chapters); the unitarity hypothesis propagates via the label. No atomic
rename is required (label stable; hypotheses added inline as (R1)/(R2)).
Vol III carries no references to the R-twisted descent lemma.

CLAUDE.md theorem-status row for Theorem A remains accurate: it already
records the fixed-curve unconditional scope and the modular-family
CONDITIONAL scope; the three heals tighten the chapter inscription without
changing the programme-level status.
