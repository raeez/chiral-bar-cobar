# Cross-Volume Proof Audit Report

Date: 2026-07-05

Scope: `/Users/raeez/chiral-bar-cobar`,
`/Users/raeez/chiral-bar-cobar-vol2`,
`/Users/raeez/calabi-yau-quantum-groups`.

This audit scanned the active TeX theorem surface reachable from each
`main.tex`, plus the wider repository theorem surface for duplicate-label
drift. It does not certify every theorem. It identifies where
certification fails or remains impossible without a bounded proof
reconstruction.

## Audit Artifacts

- `scripts/proof_surface_audit.py` -- reproducible syntactic
  proof-surface audit.
- `notes/proof_audit_20260705/claims.csv` -- 21,529 theorem-like
  environments scanned.
- `notes/proof_audit_20260705/findings.csv` -- mechanical failure
  candidates.
- `notes/proof_audit_20260705/summary.json` -- machine summary.
- `notes/proof_audit_20260705/REPORT.md` -- generated summary.
- `notes/proof_audit_20260705/END_TO_END_REPORT.md` -- this human triage
  report.
- `notes/proof_audit_20260705/ACTIVE_REPAIR_QUEUE.md` -- ordered repair
  queue.

## Summary Counts

Active theorem-like environments scanned: 17,768.

Active proof-bearing environments without claim status:

| Volume | Count | Breakdown |
|---|---:|---|
| Vol I | 224 | 211 computations, 7 corollaries, 6 verifications |
| Vol II | 751 | 270 theorems, 242 propositions, 89 corollaries, 110 computations, 25 lemmas, 9 maintheorems, 6 verifications |
| Vol III | 1,745 | 825 theorems, 703 propositions, 145 corollaries, 58 lemmas, 14 computations |

Other mechanical findings:

| Code | Count |
|---|---:|
| `PROVED_WITHOUT_PROOF_ENV` | 227 |
| `PROVED_DEPENDS_ON_NON_PROVED` | 219 |
| `PROVED_HAS_UNRESOLVED_REF` | 122 |
| `ACTIVE_LABEL_STATUS_CONFLICT` | 0 |
| `ARCHIVAL_LABEL_STATUS_CONFLICT` | 147 |

## Confirmed Repairs

The active duplicate-label/status conflict gate is closed. The first
recursive scan found 37 active conflicts; the current scan finds 0.

Repaired clusters include:

- `bv_brst`: Vol II genus-zero BRST/bar statements now carry the
  conditional status and explicit PBW, filtration, associated-graded
  comparison, and lifting-obstruction hypotheses.
- `bv_brst`: Vol II class-C BV/bar text no longer proves harmonic
  decoupling by bidegree; it is conditional on the missing boundary
  residue and free-field trace factorisation statements.
- `feynman_diagrams`: Vol II duplicate theorem surfaces now carry
  matching statuses, and Vol I `prop:m04-standard-log-basis` has the
  corrected sign \(B=b\).
- Cross-volume label collisions were repaired for `eq:ks-product`,
  `prop:cross-channel-no-closed-form`, `rem:y-algebra-depth-classification`,
  Vol III's ordinary Hochschild brace formula, and Vol III's
  quantum-group `r`-matrix remark.
- Missing external/definitional/heuristic status tags were added to the
  remaining active duplicate surfaces.

## Confirmed Failures

### F1. Vol III Is Not Certifiable From Its Claim Surface

Vol III has 1,745 active proof-bearing theorem/proposition/lemma/
corollary/computation environments with no `\ClaimStatus...` macro. Its
active theorem surface is therefore not auditable by the same standard as
Vol I. This is not a refutation of every Vol III theorem, but it is a
certification failure.

The audit scanner now sees six active Vol III status-bearing surfaces:
one `ProvedHere`, two `ProvedElsewhere`, and three `Definitional`.
The Vol III metadata generator indexes only three of those, so the
metadata layer itself remains incomplete.

### F2. Vol II Has a Large Untagged Proof Surface

Vol II has 751 active proof-bearing environments with no claim-status
macro. The largest risk is in theorem/proposition environments, not just
computations. Until these are tagged and tied to bounded proof bodies or
external theorem citations, Vol II cannot serve as a certified
cross-volume support for Vol I.

### F3. Some `ProvedHere` Statements Have No Bounded Proof Body

After allowing intervening remarks/conventions/definitions and
"Proof of Theorem X" blocks, 227 `ProvedHere` claims still have no
detected proof body. Some may be chapter-distributed arguments, but that
is itself a proof-surface failure unless the proof is explicitly bounded
and tied to the claim.

Confirmed inspected examples:

- Vol I `chapters/examples/yangians_foundations.tex:4460`,
  `thm:felder-R-half-braiding`.
Repaired in this pass:

- Vol I `chapters/connections/master_reconstruction.tex:953`,
  `cor:mr-C`, was downgraded to conditional and supplied with the
  bounded derivation from Theorem C, Theorem D, and the scalar
  complementarity tables.
- Vol I `chapters/connections/master_reconstruction.tex:971`,
  `cor:mr-D`, now has a bounded proof from the scalar-diagonal
  hypothesis and scalar obstruction proposition.
- Vol II `chapters/connections/log_ht_monodromy_core.tex:59`,
  `thm:synthesis`, was downgraded to conditional and supplied with
  proof-obligation routing; its nonessential downstream KZB reference
  was retargeted to the proved affine monodromy theorem.

### F4. Independent Verification Coverage Fails

`make verify-independence` fails in Vol I and Vol II.

Vol I:

- `ProvedHere` labels found: 1,855.
- Independent verification coverage: 118 labels, 6.4%.
- Without independent verification: 1,737.
- Orphan independent-verification decorators: 32.

Vol II:

- `ProvedHere` labels found: 955.
- Independent verification coverage: 116 labels, 12.1%.
- Without independent verification: 839.
- Orphan independent-verification decorators: 84.
- 104 test modules failed to import during the audit, mainly missing
  `pytest` / `sympy`.

This does not refute the mathematics. It refutes any claim that the
proved surface is presently independently verified.

### F5. Dependency Failures Remain

The script found 219 `ProvedHere` claims referencing non-proved,
unmarked, conjectural, conditional, heuristic, or missing labels. This
class contains false positives because some references occur negatively.

Inspected false positive:

- Vol I `chapters/connections/feynman_diagrams.tex:522`,
  `prop:compactified-ternary-two-channel`, references a conjecture only
  to say it does not prove that conjecture. Its actual proof is the
  residue theorem on `\mathbb P^1`; this statement is locally sound.

The class remains serious. It is the exact queue where dependency audit
must proceed by hand.

### F6. Unresolved References Remain Inside Proved Claims

There are 122 `ProvedHere` claims with unresolved references:

- Vol I: 26.
- Vol II: 96.

Each must be repaired, removed as a dependency, or used as evidence for a
status downgrade.

### F7. Forbidden-Slogan Regex Hits Were Mostly Negations

The script found 9 forbidden-collapse candidates. Manual inspection of
the checked cases shows deliberate negations or scoped distinctions, not
confirmed failures:

- Vol I `rem:walg-deep-2` says there is no equality
  `CoHA = W_{1+\infty}`.
- Vol II `rem:hall-borcherds-as-C5-to-C6` says the BPS partition
  function is not the gravity path integral.
- Vol III `prop:qgf-coha-y-plus-winfty-chain` states the allowed chain
  `CoHA(C^3)=Y^+ -> Y -> End(W-vac)`.

Conclusion: no confirmed forbidden-slogan failure from the inspected
regex hits. The regex should remain a suspect generator, not an arbiter.

## Compute / Test Verification

Passed:

- Vol I targeted census checks:
  `python3 -m pytest compute/tests/test_landscape_census_scalar_typing.py compute/tests/test_landscape_census_verification.py -q`
  Result: 131 passed.
- Vol III direct Hodge-supertrace smoke check for `E`, `K3`, `K3xE`,
  `E^2`, and the quintic: all expected values matched `chi_O`.

Failed / unavailable:

- Vol I `make verify-independence`: failed as above.
- Vol II `make verify-independence`: failed as above.
- Vol II and Vol III full pytest surfaces are not presently runnable in
  this shell because required Python dependencies are missing.

Incomplete:

- Vol I `make test` was started and interrupted after 929.30 seconds.
  Partial result before interruption: 6,648 passed, 8 skipped, 937
  deselected. This is not a completed pass.

## Mathematical Assessment

The project has real proof islands and a real immune system. The
five-object firewall, type-signature discipline, kappa census tests, and
explicit red-team ledgers are structurally correct ways to converge.

The project as a whole is not presently certifiable as a proved
mathematical corpus. The failure is not mainly that the central ideas are
hopeless; the failure is that the theorem surface is much larger than the
verified proof surface.

The active duplicate-label/status conflict gate is now closed. The
remaining blockers are:

1. Vol III has no working claim-status registry over active theorem
   surfaces.
2. Vol II has hundreds of unmarked proof-bearing statements.
3. Many `ProvedHere` claims lack bounded proof bodies.
4. Independent-verification coverage is below 13% in Vol I and Vol II.
5. Proved-here dependency and unresolved-reference queues remain open.

## Required Repair Order

1. Install Vol III claim-status coverage and tag every active
   proof-bearing theorem surface.
2. Tag the 751 unmarked active Vol II proof-bearing statements.
3. For each `PROVED_WITHOUT_PROOF_ENV`, either attach a bounded proof,
   point to the exact theorem proving it, or downgrade the status.
4. Triage `PROVED_DEPENDS_ON_NON_PROVED` manually, marking negative
   references as false positives and real dependencies as failures.
5. Repair the 122 unresolved references inside `ProvedHere` statements.
6. Re-run `make verify-independence` until orphan decorators are zero and
   coverage is honest.
7. Only then begin theorem-by-theorem mathematical proof reconstruction.
