# Active Repair Queue

Date: 2026-07-05

This queue is the operational answer to the proof audit. It excludes
inactive archival drift from the first pass. Archival drift remains real
cleanup, but active theorem-surface truth comes first.

## Gate 0: Audit Surface

- Status: done.
- Artifact: `scripts/proof_surface_audit.py`.
- Current active theorem-like count: 17,768.
- Current active duplicate-label status conflicts: 0.
- Current archival duplicate-label status conflicts: 147.

## Gate 1: Active Duplicate-Label Conflicts

- Status: closed on 2026-07-05.
- Starting count after the first recursive active-file scan: 37.
- Current count: 0.

Resolved clusters:

1. `bv_brst` conditional/proved drift:
   - Vol II genus-zero BRST/bar statements were downgraded from
     `\ClaimStatusProvedHere` to `\ClaimStatusConditional`.
   - `thm:brst-bar-genus0` now states the PBW, complete/exhaustive
     filtration, associated-graded comparison, and filtered
     lifting-obstruction hypotheses.
   - The class-C BV/bar paragraph in Vol II is now conditional on
     harmonic decoupling rather than a proof of the conjecture.

2. `feynman_diagrams` proved/unmarked drift:
   - Vol II now carries matching statuses for the active duplicate
     labels.
   - Vol I `prop:m04-standard-log-basis` had a real sign error fixed:
     \(d\log(1-t)=dt/(t-1)\), so the coefficient is \(B=b\), not
     \(B=-b\).

3. Arithmetic/CY product drift:
   - Vol III's unrelated wall-crossing product label was renamed from
     `eq:ks-product` to `eq:ks-wall-product`.

4. Boundary holography Vol II/Vol III drift:
   - Vol III `thm:typed-boundary-holographic-realisation` is now tagged
     `\ClaimStatusProvedHere`.

5. Operadic and higher-genus complexity drift:
   - Vol II `thm:operadic-complexity` is now conditional on the Vol I
     shadow-formality comparison hypotheses.
   - Vol II's genus-2-to-4 no-closed-form result was relabelled
     `prop:cross-channel-truncated-no-closed-form`, avoiding collision
     with Vol I's conditional infinite generating-function statement.

6. Same-volume Vol I duplicate status drift:
   - The summary occurrence in `w_algebras_deep.tex` was relabelled
     `rem:y-algebra-depth-classification-deep-summary`; the proof-bearing
     label remains in `y_algebras.tex`.

7. Remaining moderate synchronization:
   - Missing heuristic/conditional/proved-elsewhere/definitional status
     tags were added for SFT/bar, loop-genus, Feigin--Frenkel, Weiss
     cover, coacyclic/coderived, KL/Finkelberg, Swiss-cheese, and modular
     homotopy type surfaces.
   - Vol III's ordinary Hochschild brace equation was relabelled
     `eq:hoch-brace-explicit`, since Vol I's `eq:brace-explicit` is the
     chiral brace formula.
   - Vol III's quantum-group `r`-matrix remark was relabelled
     `rem:three-r-matrices-qg`, since Vol I's label names a different
     three-way distinction.

## Gate 2: Untagged Active Proof Surface

Rule: no active theorem/proposition/lemma/corollary/computation/
verification remains unmarked.

Current counts:

- Vol I: 224 active unmarked proof-bearing surfaces
  (211 computations, 7 corollaries, 6 verifications).
- Vol II: 751 active unmarked proof-bearing surfaces
  (270 theorems, 242 propositions, 89 corollaries, 110 computations,
  25 lemmas, 9 maintheorems, 6 verifications).
- Vol III: 1,745 active unmarked proof-bearing surfaces
  (825 theorems, 703 propositions, 145 corollaries, 58 lemmas,
  14 computations).

Priority:

1. Vol III top-level theorem/proposition surfaces, because Vol III still
   has no comprehensive claim-status registry.
2. Vol II theorem/proposition surfaces, because Vol I repeatedly cites
   Vol II for vertical equivalences.
3. Vol I unmarked computations and verifications, because these often
   carry numerical constants.

## Gate 3: `ProvedHere` Without Bounded Proof

Rule: a `ProvedHere` claim must have a bounded proof body or a precise
pointer to the theorem/proposition whose proof proves it.

Current mechanical count: 227.

- Vol I: 105.
- Vol II: 122.

Remaining confirmed failure from manual inspection:

- Vol I `chapters/examples/yangians_foundations.tex:4460`,
  `thm:felder-R-half-braiding`.

Repaired in this pass:

- Vol I `chapters/connections/master_reconstruction.tex:953`,
  `cor:mr-C`, was downgraded from `ProvedHere on Koszul locus` to
  `Conditional` and given a bounded derivation from
  `thm:quantum-complementarity-main`, `thm:modular-characteristic`, and
  the complementarity scalar table.
- Vol I `chapters/connections/master_reconstruction.tex:971`,
  `cor:mr-D`, was given a bounded proof from
  `def:scalar-diagonal-hypothesis`,
  `prop:scalar-obstruction-hodge-euler`, and
  `thm:modular-characteristic`.
- Vol II `chapters/connections/log_ht_monodromy_core.tex:59`,
  `thm:synthesis`, was downgraded to `Conditional` and supplied with
  explicit proof-obligation routing. The one downstream self-contained
  KZB computation was retargeted from a nonessential `thm:synthesis`
  reference to `thm:affine-monodromy-identification`.

Known false positives:

- Vol I `thm:single-fermion-boson-duality` has a proof after an
  intervening remark.
- Vol I `thm:chiral-quantization` has a proof after an intervening
  remark.
- Vol I `thm:universal-kac-moody-koszul` has a proof after a proof
  subsection heading.

## Gate 4: Dependency Triage

Rule: each `ProvedHere` claim depending on a non-proved label is either a
false positive by negative/reference-only use, or a real proof failure.

Current count: 219.

- Vol I: 80.
- Vol II: 139.

Known false positive:

- Vol I `chapters/connections/feynman_diagrams.tex:522`,
  `prop:compactified-ternary-two-channel`, references
  `conj:v1-disk-local-perturbative-fm` only negatively.

## Gate 5: Unresolved References Inside Proved Claims

Current count: 122.

- Vol I: 26.
- Vol II: 96.

Rule: every `ProvedHere` statement with an unresolved reference must
either repair the reference, remove the dependency, or downgrade the
claim.

## Gate 6: Independent Verification

Rule: `make verify-independence` must become an honest gate, not a
decorative count.

Current state from this audit session:

- Vol I: failed; 6.4% independent-verification coverage.
- Vol II: failed; 12.1% independent-verification coverage; 104 test
  modules failed to import.

## Stop Condition

The repair pass stops only when every active claim has one of:

- bounded proof in the tree,
- exact external theorem citation,
- computation rerun in this session or explicitly marked previously
  computed,
- downgraded epistemic status,
- explicit open obligation.
