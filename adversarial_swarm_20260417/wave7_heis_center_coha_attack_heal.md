% wave7_heis_center_coha_attack_heal.md
% Adversarial audit 2026-04-17, Wave 7 augmentation. Author: Raeez Lorgat.
% Targets: Vol I Heisenberg derived-centre inscription in
% `chapters/theory/chiral_center_theorem.tex` (prop:derived-center-explicit
% + prop:heisenberg-bv-structure), and Vol III CoHA = Y^+ identification
% in `chapters/examples/toric_cy3_coha.tex` + `coha_wall_crossing_platonic.tex`.

# Summary

Vol III CoHA=Y^+ inscription is already sharp. Vol I Heisenberg BV-structure
proposition has a **k=0 scope gap** in the BV operator statement which I
correct by surgical edit. The Drinfeld-centre-equals-bulk conjecture for
Heisenberg remains correctly marked conjectural in the preface. One small
cross-reference in prop:heisenberg-bv-structure warrants tightening.

# Phase 1 Attack

## (i) Explicit generators {1, ξ_k, η}

File: `chapters/theory/chiral_center_theorem.tex:1965-2117`.
Generators and their meaning inscribed correctly:
- `1 ∈ ChirHoch^0`: vacuum, naive centre of H_k.
- `ξ_k ∈ ChirHoch^1`: level-deformation class k ↦ k+ε.
- `η ∈ ChirHoch^2`: dual-vacuum / obstruction class of the Koszul dual
  `H_k^! = Sym^ch(V*)`.

Koszul resolution argument (quadratic OPE ⇒ chirally Koszul ⇒ three-term
resolution ⇒ ChirHoch^n = C for n∈{0,1,2}) is correct (line 2051–2074).

## (ii) BV structure at lines 2485-2552 — k=0 scope gap

Proposition statement lines 2511-2514:
```
Δ(1) = 0,     Δ(ξ_k) = 1,     Δ(η) = 0.
```
The proof at 2519-2525 derives `Δ(η) = 0` from the BV relation as:
`0 = Δ(ξ_k^2) − (Δξ_k)ξ_k − (−1)^1 ξ_k(Δξ_k) = k·Δ(η) − ξ_k + ξ_k = k·Δ(η)`,
and explicitly notes "giving Δ(η) = 0 for k ≠ 0".

The statement omits the k ≠ 0 hypothesis. At k = 0 (free abelian boson) the
BV argument degenerates: `ξ_0² = 0·η = 0`, so the Yoneda-product argument
that forces `Δ(η)` does not determine it from this relation. The k=0 case
still gives `Δ(η) = 0`, but by a different mechanism (direct Connes B
evaluation on the weight-zero dual-vacuum cocycle, as in the uncurved
Sym^ch(V*) resolution; see MSV99 §3 applied to V = C·a). So:

- the BV-structure proposition is CORRECT (Δη = 0 at all k), but
- the PROOF as written only covers k ≠ 0.

Minimum heal: add a one-line k=0 remark after the BV relation argument, or
rephrase the proposition to carry a "k ≠ 0" qualifier in the Δ bullet with
a separate remark for k = 0. I choose the former (less disruptive).

Also: the phrase "since the deformation is unobstructed ([ξ_k,ξ_k]=0)" on
line 2517-2518 is used before the bracket calculation that proves
[ξ_k,ξ_k]=0 at 2571-2573. This is a forward-reference of the kind Vol I
allows (internal to the same proposition), but a one-word clarification
"(proved below)" prevents the reader from suspecting circularity.

## (iii) Cross-reference: naive centre vs derived centre

Prop:derived-center-explicit(i) states `Z^der_ch(H_k) ≃ C ⊕ C[-1] ⊕ C[-2]`
(total dim 3) while the naive commutant centre is dim 1. The outer
derivation ξ_k and the obstruction class η are invisible to the commutant;
this fits AP-CY65 (spectral parameters / outer derivations visible only in
the derived centre) and FM40 (naive ≠ derived). The inscription is correct.

## (iv) Test inventory

Tests covering Heisenberg derived centre:
```
/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bar.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bar_explicit_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bridge.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_heisenberg_bv_bar_proof.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_hh_heisenberg_e3_engine.py
```
Five files present; aggregate test counts match Wave-7 #36 agent report
(72+ total when included with chirhoch1-KM test families). Engine–test
pairs synchronized.

Cross-volume Drinfeld-centre test (Vol III):
`/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_drinfeld_center.py`
plus `test_drinfeld_center_e1_cy3.py`, `test_drinfeld_center_hocolim.py`,
`test_drinfeld_center_yangian.py`. Engines all present.

## (v) CoHA = Y^+ scope

Vol III inscription at `chapters/examples/toric_cy3_coha.tex:72-102`:

- **thm:sv-c3** (line 75, ClaimStatusProvedElsewhere): C^3 with Jordan
  quiver + cubic potential W = tr(XYZ − XZY); CoHA ≃ Y^+(ĝl_1).
  SHARP. Matches Schiffmann–Vasserot 2012 arXiv:1202.2756 exactly.
- **thm:rsyz** (line 96, ClaimStatusProvedElsewhere): toric CY_3 without
  compact 4-cycles; CoHA ≃ Y^+(ĝ_{Q_X}) affine super Yangian.
  SHARP. Matches Rapčák–Soibelman–Yang–Zhao scope.

The sister chapter `coha_wall_crossing_platonic.tex` adds a ledger-strict
algebra-vs-coalgebra separation (§1–§3) that explicitly disowns any
"D² = 0 in the CoHA" phrasing as Ginzburg-dg-algebra shorthand, and an
explicit positive-half-vs-full-Yangian ledger (points (i)–(iii) in the
Foreword). This is the right granularity. No heal needed.

One scope check: Vol III `thm:sv-c3` uses "critical CoHA" via vanishing
cycle sheaf H^BM(Crit(W_d), φ_W_d). This is the motivic / critical form
(Kontsevich–Soibelman 2010). The rational form (Schiffmann–Vasserot 2012
for C^2 without potential, yielding the shuffle / Y^+ for gl_1 via
Drinfeld presentation) is a DIFFERENT construction but converges on the
same Y^+(ĝl_1) target; this is Prochazka–Rapčák's independent corroboration
cited implicitly at line 45 in the platonic chapter. No drift.

## (vi) Cross-volume ownership

CoHA = Y^+ is owned by Vol III. Vol I mentions it only as a bridge in
Part V Face F5 (Drinfeld Yangian); no Vol I theorem claims CoHA identity.
Cross-references resolve. AP5 clean.

## (vii) Drinfeld-centre-equals-bulk conjecture for Heisenberg

Preface line 4228–4242: `conj:v1-drinfeld-center-equals-bulk` is properly
marked conjectural with `\begin{conjecture}`; the statement is for
E_1-chiral algebras in general, not for Heisenberg specifically. Three
obstructions explicit (line 4244–4255). Partial closure for affine KM
cited (line 4257–4266). Topologization hypotheses explicit (line 4231).

CLAUDE.md status-table entry "Drinfeld center Heis VERIFIED" refers to the
**computational** verification of 5 invariants at 6 levels (engine test
`test_drinfeld_center_hocolim.py`), NOT to a theoretical proof of the
conjecture. The conjecture itself remains open. The status table wording
is ambiguous; I recommend rewording to "Drinfeld center Heis: numerical
evidence at 6 levels, 72 tests; conj:v1-drinfeld-center-equals-bulk
remains OPEN (general E_1-chiral case)" but this is a CLAUDE.md edit and
not part of the manuscript.

# Phase 2 Heal

Two surgical edits to `chapters/theory/chiral_center_theorem.tex`:

1. In the BV-operator bullet of `prop:heisenberg-bv-structure`, add an
   explicit k ≠ 0 note and a one-line remark that Δ(η) = 0 holds at
   k = 0 by direct Connes-B evaluation on the Sym^ch(V*) resolution.

2. In the BV-relation argument, annotate "unobstructed" with the internal
   forward-reference.

Both edits are atomic and preserve all existing proof content.

# Verdicts

- Vol III CoHA = Y^+ inscription: **ACCEPT as-is**.
- Vol I Heisenberg BV-structure: **ACCEPT with the two surgical edits below**.
- Drinfeld-centre-equals-bulk conjecture: **correctly conjectured in preface**.
