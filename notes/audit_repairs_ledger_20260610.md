## 2026-06-18 -- Pass 574: Heisenberg two-point mixed-mode residue formula

Audit anchor: the remaining mixed-mode part of the ordered
residue-twisted acyclicity gap in the rank-one Heisenberg Theorem-H
lane.  Pass 573 proves every single-mode polynomial string.  The next
truthful upgrade is the exact finite-support mixed-mode formula, not a
promotion to full Fock-window acyclicity:
\[
  d_1([\alpha|u_{\mathbf q}]\otimes\eta_{12})
  =
  k\sum_{r:q_r>0} r q_r\,u_{\mathbf q-\mathbf e_r}.
\]

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: added
  `prop:heisenberg-two-point-mixed-mode-residue-formula`, a
  `\ClaimStatusProvedHere` proposition proving the exact
  finite-support mixed-mode residue formula for
  \(u_{\mathbf q}=\prod_r\alpha_{-r}^{q_r}\mathbf1\).  It also proves
  that a fixed non-vacuum monomial line injects into its image for
  \(k\neq0\).
- The proposition explicitly prevents a false upgrade: on the raw
  ungraded polynomial span the same formula is
  \(L_k=k\sum_{r\ge1}r\partial_{x_r}\), and
  \(L_k(x_2-2x_1)=0\).  Therefore full mixed-mode Fock-window
  acyclicity requires the actual graded residue-twisted/Koszul complex
  and finite-window homotopy data.
- `compute/lib/residue_twisted_heisenberg_engine.py`: added exact
  finite-support mixed-mode residue reports and a raw ungraded kernel
  witness evaluator.
- `compute/tests/test_residue_twisted_heisenberg_engine.py`: added
  regression coverage for the mixed-mode coefficient formula,
  vacuum/zero-level/bad-exponent edge cases, the raw-kernel witness,
  and the manuscript theorem surface.
- `compute/tests/test_external_review_harvest_completion_scope.py`:
  added Pass 574 to the global external-review harvest guard.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the
  D5/E/H Theorem-H rows and residual summary so mixed-mode formula is
  harvested while full mixed-mode Fock-window acyclicity remains
  source-level work.

Verification:

- `python3 -m py_compile
  compute/lib/residue_twisted_heisenberg_engine.py
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`: 24
  passed.
- `python3 scripts/generate_metadata.py` regenerated 4704 claims:
  `PH=1863 PE=450 CJ=349 H=31 CD=1745 O=2 DF=264 total=4704`,
  with 2313 proved claims in the theorem registry.
- `make phase0-index` passed with 2037 indexed nodes and the
  pre-existing open label `thm:hochschild-concentration-E1` still at 9
  references.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 283 passed.
- Status scans found
  `prop:heisenberg-two-point-mixed-mode-residue-formula` as
  `ProvedHere` in `metadata/claims.jsonl`,
  `metadata/theorem_registry.md`, `standalone/theorem_index.tex`, and
  `PHASE0_THEOREM_DEPENDENCY_INDEX.md`.
- `git diff --check` is clean for the touched tracked manuscript,
  metadata, theorem-index, and ledger surfaces; a trailing-whitespace
  scan is also clean for the untracked compute, matrix, and phase0
  files touched by this pass.

## 2026-06-18 -- Pass 573: Heisenberg two-point single-mode polynomial arbitrary-mode string

Audit anchor: the remaining single-mode part of the ordered
residue-twisted acyclicity gap in the rank-one Heisenberg Theorem-H
lane.  Pass 571 proved \(n=1\) for all powers, and Pass 572 proved all
modes for \(q=1\).  The same arbitrary-mode residue formula and
Heisenberg commutator prove the two-parameter family:
\[
  d_1^{(n)}([\alpha|\alpha_{-n}^{q}\mathbf1]\otimes\eta_{12})
  =\alpha_{(n)}\alpha_{-n}^{q}\mathbf1
  =q\,n\,k\,\alpha_{-n}^{q-1}\mathbf1 .
\]

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: added
  `prop:heisenberg-two-point-single-mode-polynomial-residue`, a
  `\ClaimStatusProvedHere` proposition proving that every two-point
  positive Arnold line in the single-mode polynomial string
  \(\C[\alpha_{-n}]\), \(n\geq1\), is contracted for \(q\geq1\) and
  \(k\neq0\).  The proof applies
  `eq:ordered-residue-arbitrary-mode` with \(m=n\) and computes
  \([\alpha_n,\alpha_{-n}^{q}]=qn k\alpha_{-n}^{q-1}\).
- The preceding Pass 571 and Pass 572 propositions now point to this
  two-parameter extension, so they no longer list same-mode higher
  powers as a residual gap.
- `compute/lib/residue_twisted_heisenberg_engine.py`: extended the
  exact rational checker to the single-mode polynomial
  arbitrary-mode family \(qnk\), with explicit no-promotion scope.
- `compute/tests/test_residue_twisted_heisenberg_engine.py`: added
  regression coverage for the \(qnk\) coefficient grid, the zero-level
  failure, positive-mode/power input guards, and the manuscript theorem
  surface.
- `compute/tests/test_external_review_harvest_completion_scope.py`:
  added Pass 573 to the global external-review harvest guard.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the
  D5/E/H Theorem-H rows and residual summary so single-mode polynomial
  strings are no longer listed as unharvested.

Verification:

- `python3 -m py_compile
  compute/lib/residue_twisted_heisenberg_engine.py
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`: 20
  passed.
- `python3 scripts/generate_metadata.py` regenerated 4703 claims:
  `PH=1862 PE=450 CJ=349 H=31 CD=1745 O=2 DF=264 total=4703`,
  with 2312 proved claims in the theorem registry.
- `make phase0-index` passed with 2036 indexed nodes and the
  pre-existing open label `thm:hochschild-concentration-E1` still at 9
  references.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 279 passed.
- Status scans found
  `prop:heisenberg-two-point-single-mode-polynomial-residue` as
  `ProvedHere` in `metadata/claims.jsonl`,
  `metadata/theorem_registry.md`, `standalone/theorem_index.tex`, and
  `PHASE0_THEOREM_DEPENDENCY_INDEX.md`.
- `git diff --check` is clean for the touched tracked manuscript,
  metadata, theorem-index, and ledger surfaces; a trailing-whitespace
  scan is also clean for the untracked compute, matrix, and phase0
  files touched by this pass.

## 2026-06-18 -- Pass 572: Heisenberg two-point single-oscillator arbitrary-mode string

Audit anchor: the remaining ordered residue-twisted acyclicity gap in
the rank-one Heisenberg Theorem-H lane, after Pass 571 proved only the
weight-one polynomial string.  The arbitrary-mode ordered residue
formula supplies the \(m=n\) contribution, and the Heisenberg mode
relation gives
\[
  d_1^{(n)}([\alpha|\alpha_{-n}\mathbf1]\otimes\eta_{12})
  =\alpha_{(n)}\alpha_{-n}\mathbf1
  =nk\,\mathbf1 .
\]

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: added
  `prop:heisenberg-two-point-single-oscillator-residue`, a
  `\ClaimStatusProvedHere` proposition proving that every two-point
  positive Arnold line with second input
  \(v_n=\alpha_{-n}\mathbf1\), \(n\geq1\), is contracted for
  \(k\neq0\).  The proof applies
  `eq:ordered-residue-arbitrary-mode` with \(m=n\) and computes
  \([\alpha_n,\alpha_{-n}]=nk\mathbf1\).
- `compute/lib/residue_twisted_heisenberg_engine.py`: extended the
  exact rational checker to the single-oscillator arbitrary-mode
  family \(nk\), with explicit no-promotion scope.
- `compute/tests/test_residue_twisted_heisenberg_engine.py`: added
  regression coverage for the \(nk\) coefficient family, the zero-level
  failure, the positive-mode input guard, and the manuscript theorem
  surface.
- `compute/tests/test_external_review_harvest_completion_scope.py`:
  added Pass 572 to the global external-review harvest guard.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the
  D5/E/H Theorem-H rows and residual summary so individual
  single-oscillator higher modes are no longer listed as unharvested.

Verification:

- `python3 -m py_compile
  compute/lib/residue_twisted_heisenberg_engine.py
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`: 17
  passed.
- `python3 scripts/generate_metadata.py` regenerated 4702 claims:
  `PH=1861 PE=450 CJ=349 H=31 CD=1745 O=2 DF=264 total=4702`,
  with 2311 proved claims in the theorem registry.
- `make phase0-index` passed with 2035 indexed nodes and the
  pre-existing open label `thm:hochschild-concentration-E1` still at 9
  references.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 276 passed.
- Status scans found
  `prop:heisenberg-two-point-single-oscillator-residue` as
  `ProvedHere` in `metadata/claims.jsonl`,
  `metadata/theorem_registry.md`, `standalone/theorem_index.tex`, and
  `PHASE0_THEOREM_DEPENDENCY_INDEX.md`.
- `git diff --check` is clean for the touched tracked manuscript,
  metadata, theorem-index, and ledger surfaces; a trailing-whitespace
  scan is also clean for the untracked compute, matrix, and phase0
  files touched by this pass.

## 2026-06-18 -- Pass 571: Heisenberg two-point weight-one polynomial string

Audit anchor: the remaining ordered residue-twisted acyclicity gap in
the rank-one Heisenberg Theorem-H lane.  Pass 569 proved only the
central-current summand \([\alpha|\alpha]\).  The same ordered residue
formula and the Heisenberg mode relation prove a larger family: for
\(u_q=\alpha_{-1}^{q}\mathbf1\),
\[
  d_1([\alpha|u_q]\otimes\eta_{12})
  =\alpha_{(1)}u_q=qk\,u_{q-1}.
\]

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: added
  `prop:heisenberg-two-point-weight-one-polynomial-residue`, a
  `\ClaimStatusProvedHere` proposition proving that every two-point
  positive Arnold line in the ordered weight-one polynomial string
  \(\C[\alpha_{-1}]\) is contracted for \(q\geq1\), \(k\neq0\).
  The proof computes
  \([\alpha_1,\alpha_{-1}^{q}]=qk\alpha_{-1}^{q-1}\) directly in the
  Heisenberg mode algebra.
- `compute/lib/residue_twisted_heisenberg_engine.py`: extended the
  exact rational checker from the single \(k\)-differential to the
  family \(qk\), with explicit no-promotion scope.
- `compute/tests/test_residue_twisted_heisenberg_engine.py`: added
  regression coverage for the \(qk\) coefficient family, the zero-level
  failure, the positive-power input guard, and the manuscript theorem
  surface.

Verification:

- `python3 -m py_compile
  compute/lib/residue_twisted_heisenberg_engine.py
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`: 14
  passed.
- `python3 scripts/generate_metadata.py` regenerated 4701 claims:
  `PH=1860 PE=450 CJ=349 H=31 CD=1745 O=2 DF=264 total=4701`,
  with 2310 proved claims in the theorem registry.
- `make phase0-index` passed with 2034 indexed nodes and the
  pre-existing open label `thm:hochschild-concentration-E1` still at 9
  references.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 273 passed.
- Status scans found
  `prop:heisenberg-two-point-weight-one-polynomial-residue` as
  `ProvedHere` in `metadata/claims.jsonl`,
  `metadata/theorem_registry.md`, `standalone/theorem_index.tex`, and
  `PHASE0_THEOREM_DEPENDENCY_INDEX.md`.
- `git diff --check` is clean for the touched manuscript, compute,
  test, ledger, matrix, and regenerated metadata/index files.

## 2026-06-18 -- Pass 570: Curved second-kind Heisenberg endpoint

Audit anchor: `lem:curved-dual-centre-heisenberg`, previously the
remaining completed second-kind convergence input in the rank-one
Heisenberg Theorem-H lane.  The rank-one curved dual has an explicit
oscillator normal form: in weight window \(N\), every positive mode is
a two-term Koszul--Clifford pair with coefficient \(-kn\), hence
contractible for \(k\neq0\).

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: retagged
  `lem:curved-dual-centre-heisenberg` as `\ClaimStatusProvedHere` and
  added the finite-window proof.  The completed second-kind complex is
  a finite tensor product of contractible oscillator pairs plus the
  vacuum line; transition maps are degreewise surjective, so no
  \(R^1\!\varprojlim\) correction appears.
- Updated the nearby Heisenberg finite-window certificate and Theorem-H
  exactness criterion: the curved second-kind degree-\(2\) endpoint is
  now supplied by the lemma; the remaining Heisenberg gates are ordered
  residue-twisted acyclicity and ordered-to-symmetric/PBW descent.
- `compute/lib/curved_second_kind_heisenberg_engine.py`: added an
  exact rational finite-window checker for the coefficients
  \(-kn\), positive-weight cohomology, and strict Mittag--Leffler
  status.
- `compute/tests/test_curved_second_kind_heisenberg_engine.py`,
  `compute/tests/test_heisenberg_curved_dual_scope.py`, and
  `compute/tests/test_theorem_h_hochschild_polynomial.py`: added or
  updated guards for the proved lemma and for the still-conditional
  full Theorem-H conclusion.

Verification:

- `python3 -m py_compile
  compute/lib/curved_second_kind_heisenberg_engine.py
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  244 passed.
- `python3 scripts/generate_metadata.py` regenerated 4700 claims:
  `PH=1859 PE=450 CJ=349 H=31 CD=1745 O=2 DF=264 total=4700`,
  with 2309 proved claims in the theorem registry.
- `make phase0-index` passed with 2033 indexed nodes and the
  pre-existing open label `thm:hochschild-concentration-E1` still at 9
  references.
- `pytest -q
  compute/tests/test_curved_second_kind_heisenberg_engine.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 268 passed.
- Fixed-string stale scans found no remaining `completed second-kind
  convergence obligation`, `residual obligation is convergence`, or
  `curved second-kind convergence obligation` on the touched Theorem-H
  surfaces.
- Status scans found `lem:curved-dual-centre-heisenberg` as
  `ProvedHere` in `metadata/claims.jsonl`,
  `metadata/theorem_registry.md`, `standalone/theorem_index.tex`, and
  `PHASE0_THEOREM_DEPENDENCY_INDEX.md`; remaining conditional hits are
  downstream claims that still depend on ordered acyclicity/descent,
  not stale lemma status.
- `git diff --check` is clean for the touched manuscript, compute,
  test, ledger, matrix, and regenerated metadata/index files.

## 2026-06-18 -- Pass 569: Two-point Heisenberg residue-twisted Arnold summand

Audit anchor: ordered residue-twisted acyclicity, the remaining
positive-Arnold part of the Theorem-H package.  The full conjecture is
still a source-level theorem, but the arity-\(2\) rank-one Heisenberg
central-current summand closes exactly: the positive
\(\operatorname{OS}(A_1)\) Arnold line maps by the nonzero Heisenberg
double-pole coefficient.

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: added
  `prop:heisenberg-two-point-residue-twisted-acyclicity`, a
  `\ClaimStatusProvedHere` proposition proving
  \(d_1([\alpha|\alpha]\otimes\eta_{12})
  =\alpha_{(1)}\alpha=k\mathbf1\) for \(k\neq0\).  Hence the
  two-point positive Arnold fibre line has \(H^1=0\).  The proposition
  explicitly excludes arbitrary Fock monomials, higher collision
  clusters, multi-strata, ordered-to-symmetric descent, and the curved
  second-kind endpoint.
- `compute/lib/residue_twisted_heisenberg_engine.py`: added an exact
  two-term rational check for the differential \(C^1\xrightarrow{k}C^0\).
  It reports rank, positive-fibre kernel dimension, degree-zero
  cokernel dimension, and a no-Theorem-H-promotion scope.
- `compute/tests/test_residue_twisted_heisenberg_engine.py`: added
  regression coverage for the nonzero-level acyclicity, the \(k=0\)
  failure, manuscript scope, and harvest-control entries.

Verification:

- `python3 -m py_compile
  compute/lib/residue_twisted_heisenberg_engine.py
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_external_review_harvest_completion_scope.py`: 9
  passed.
- `python3 scripts/generate_metadata.py` regenerated 4700 claims:
  `PH=1858 PE=450 CJ=349 H=31 CD=1746 O=2 DF=264 total=4700`,
  with 2308 proved claims in the theorem registry.
- `make phase0-index` passed with 2033 indexed nodes and the
  pre-existing open label `thm:hochschild-concentration-E1` still at 9
  references.
- `pytest -q
  compute/tests/test_residue_twisted_heisenberg_engine.py
  compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_H_hochschild_koszul.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 253 passed.
- Stale-status scans found the new proposition as `ProvedHere` in
  `metadata/claims.jsonl`, `metadata/theorem_registry.md`,
  `standalone/theorem_index.tex`, and
  `PHASE0_THEOREM_DEPENDENCY_INDEX.md`; no conditional metadata drift
  was found.  The only full-conjecture scan hit is the intended
  negative matrix sentence preserving the conjectural status of full
  ordered twisted-tensor acyclicity.
- `git diff --check` is clean for the touched manuscript, compute,
  test, ledger, matrix, and regenerated metadata/index files.

## 2026-06-18 -- Pass 568: Heisenberg finite-window ML certificate proved

Audit anchor: Theorem H non-vacuity and the rank-one Heisenberg
finite-window certificate.  Pass 459 had correctly fenced the
Heisenberg witness from the full Theorem-H package, but the proposition
still mixed two statuses: finite-window Fock combinatorics and
Mittag--Leffler finiteness are proved directly, while the low-degree
Hochschild endpoint still depends on ordered residue-twisted
acyclicity and curved second-kind convergence.

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: retagged
  `prop:heisenberg-theorem-h-window-certificate` as
  `\ClaimStatusProvedHere` after narrowing the statement to the
  finite-window partition basis, normalized bar-length bound, and
  degreewise Mittag--Leffler stabilization.  The proposition now
  explicitly does not compute the low-degree Hochschild witnesses or
  remove the two residual Theorem-H inputs.
- `compute/lib/kdh_certificate_engine.py`: added an exact rank-one
  Heisenberg finite-window combinatorial certificate:
  `partition_numbers_up_to`, `heisenberg_fock_window_dimension`, and
  `heisenberg_finite_window_report`.  The report records the exact
  partition counts, cumulative Fock-window dimension, normalized
  bar-length bound, and logical scope.
- `compute/tests/test_kdh_certificate_engine.py` and
  `compute/tests/test_theorem_h_hochschild_polynomial.py`: added
  regression coverage that checks the partition counts
  \(p(0),\ldots,p(6)=(1,1,2,3,5,7,11)\), the cumulative dimension
  \(\sum_{m\le6}p(m)=30\), the bar-length bound \(p\le N\), and the
  firewall that this is not ordered residue-twisted acyclicity,
  curved second-kind convergence, or a proof of Theorem~H.

Verification:

- `python3 -m py_compile
  compute/lib/kdh_certificate_engine.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `python3 scripts/generate_metadata.py` regenerated 4699 claims:
  `PH=1857 PE=450 CJ=349 H=31 CD=1746 O=2 DF=264 total=4699`,
  with 2307 proved claims in the theorem registry.
- `make phase0-index` passed with the pre-existing open label
  `thm:hochschild-concentration-E1` still at 9 references.
- `pytest -q
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_kdh_certificate_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_generate_metadata_parser.py`: 259 passed.
- Fixed-string stale scans found no remaining old Heisenberg
  finite-window title, conditional proposition metadata, low-degree
  cohomology clause inside the proved proposition, or promotion phrase
  saying the finite-window result proves Theorem~H.
- `git diff --check` is clean for the touched manuscript, compute,
  test, ledger, matrix, and regenerated metadata/index files.

## 2026-06-18 -- Pass 567: Vallette/GR17 ambient-transfer firewall

Audit anchor: Theorem A ambient package and the active
first-principles cache.  The repaired theorem surface already marked
the factorization ambient as conditional, but one proof paragraph, the
`GR17` bibliography note, and two cache rows still allowed a reader to
reconstruct the retired argument: apply Vallette's \(k\)-linear
Quillen equivalence directly in \(\Fact(X)\), or replace the missing
factorization model structure by a phantom GR17 IV.5 theorem.

Repairs:

- `chapters/theory/theorem_A_infinity_2.tex`: rewrote the Theorem A
  proof paragraph so Vallette's bar--cobar Quillen equivalence is used
  only on the \(k\)-linear pole-free operadic model.  Transport to the
  Ran factorization/properadic ambient is now explicitly the
  conditional \(H_{\Fact}(X)\) package plus Hackney--Robertson and
  Hinich machinery, not a published GR17 model-structure theorem.
- `standalone/references.bib`: corrected the `Francis2012` and `GR17`
  notes.  `Francis2012` is no longer presented as a category-valued
  factorization Morita source, and `GR17` is no longer described as
  proving a Chapter IV.5 factorization-sheaf model structure or
  \((\infty,2)\)-enhancement of the Francis star-product.
- `notes/first_principles_cache_comprehensive.md`: replaced the
  obsolete FM70/FM72 repair recommendations that cited GR17 IV.5 by
  the conditional \(H_{\Fact}(X)\) / properadic-transfer formulation.
- `compute/tests/test_factorization_ambient_citation_scope.py`: added
  regression coverage for the theorem paragraph, bibliography notes,
  and active cache rows.

Verification:

- `python3 -m py_compile
  compute/tests/test_factorization_ambient_citation_scope.py
  compute/tests/test_theorem_concordance_rectification_engine.py`
  passed.
- `pytest -q compute/tests/test_factorization_ambient_citation_scope.py`:
  4 passed.
- `pytest -q
  compute/tests/test_theorem_concordance_rectification_engine.py -k
  "fg_ambient_package_is_conditional_not_gr17_citation or
  morita_theorem_is_conditional_recognition_package"`: 2 passed.
- Fixed-string stale scans over the repaired theorem paragraph,
  bibliography note, and active cache found no remaining GR17 IV.5
  model-structure replacement phrase.

## 2026-06-18 -- Pass 566: Pointed-bar/conformal-block claim-surface sync

Audit anchor: claim-surface propagation for Pass 565.  After the
canonical pointed-bar/conformal-block bridge was retagged as a
comparison theorem, the generated theorem index, JSONL claim registry,
label index, dependency graph, proved-surface registry, and active audit
notes still had to be checked for old unconditional titles, statuses,
and line anchors.

Repairs:

- Regenerated metadata with `python3 scripts/generate_metadata.py`.
  The conditional comparison labels now appear in
  `standalone/theorem_index.tex`, `metadata/claims.jsonl`,
  `metadata/label_index.json`, and `metadata/dependency_graph.dot` with
  current line/node anchors; `metadata/theorem_registry.md` remains a
  proved-surface registry and therefore correctly excludes the five
  conditional labels while recording the updated conditional total.
- `notes/antipatterns_catalogue.md` and
  `notes/first_principles_cache_comprehensive.md`: replaced the old
  Vol-I bar-complex-identifies-conformal-blocks language by the
  pointed-bar/conformal-block comparison package.
- `compute/tests/test_conformal_block_bar_comparison_scope.py`:
  extended the regression guard so the theorem index, JSONL claims,
  label index, dependency graph, active notes, and proved-registry
  exclusion all fail on the retired unconditional titles, statuses, and
  node keys.

Verification:

- `python3 -m py_compile
  compute/tests/test_conformal_block_bar_comparison_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`
  passed.
- `pytest -q
  compute/tests/test_conformal_block_bar_comparison_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_determinant_anomaly_conformal_block_scope.py
  compute/tests/test_generate_metadata_parser.py`: 21 passed.

## 2026-06-18 -- Pass 565: Pointed bar versus conformal-block comparison gate

Audit anchor: review Witten/conformal-block gate and the hidden
dependency behind the earlier Verlinde ordered/TUY repair.  The
canonical `prop:conformal-blocks-bar` still claimed
\(\ClaimStatusProvedHere\) and said the bar complex computes conformal
blocks.  Its proof actually constructs derived coinvariants and then
uses an unstated comparison to classical TUY/Hitchin conformal blocks.

Repairs:

- `chapters/theory/chiral_modules.tex`: retagged
  `prop:conformal-blocks-bar` as conditional and renamed it as the
  pointed bar resolution/conformal-block comparison.  The statement now
  separates the proved bar-side derived coinvariant complex from the
  classical conformal-block target, which requires degreewise finite
  holonomic pointed bar terms, exactness above degree \(0\), and a
  TUY/Hitchin or equivalent finite-rank comparison theorem.  The KZB
  and Verlinde statements are now comparison-gated and include
  determinant-anomaly/projective-flatness language.
- `chapters/theory/configuration_spaces.tex`: retagged the punctured
  bar corollary as a punctured bar coinvariant/conformal-block
  comparison, not an unconditional recovery theorem.
- `chapters/examples/kac_moody.tex`: synced the Kac--Moody duplicate to
  the same comparison package and corrected the no-insertion Verlinde
  normalization from the quantum-dimension ratio expression to
  \(\sum_\lambda S_{0,\lambda}^{2-2g}\).  The genus-zero value is now
  \(Z_0=1\) by unitarity, and the false \(k\mapsto -k-4\) positive-level
  Verlinde-category statement is removed.
- `chapters/theory/theorem_C_refinements_platonic.tex`: narrowed the
  perfectness bridge so `prop:conformal-blocks-bar` is used only under
  its exactness and conformal-block comparison hypotheses.
- `compute/lib/conformal_blocks_bar_identification_engine.py` and
  `compute/tests/test_conformal_blocks_bar_identification_engine.py`:
  changed the compute-layer description to Verlinde dimensions and
  expected pointed-bar comparison targets, not proof that bar cohomology
  equals conformal blocks.
- `compute/tests/test_conformal_block_bar_comparison_scope.py`: added a
  regression guard for the conditional status/type signatures,
  comparison language, determinant anomaly gate, corrected Verlinde
  normalization, and retired raw bar/conformal-block phrases.

Verification:

- `python3 -m py_compile
  compute/tests/test_conformal_block_bar_comparison_scope.py
  compute/lib/conformal_blocks_bar_identification_engine.py
  compute/tests/test_conformal_blocks_bar_identification_engine.py`
  passed.
- `pytest -q
  compute/tests/test_conformal_block_bar_comparison_scope.py`: 4 passed.

## 2026-06-18 -- Pass 564: Verlinde recovery through ordered/TUY comparison

Audit anchor: review Witten/conformal-block gate and the expanded
ordered-to-symmetric correction queue.  Several theorem and first-reader
surfaces said that ordered chiral homology itself recovers Verlinde
conformal blocks.  That conflates the ordered chain model with the
TUY/Hitchin conformal-block sheaf.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex` and
  `standalone/ordered_chiral_homology.tex`: retagged
  `prop:verlinde-from-ordered` as conditional with the full type
  signature.  The statement now requires positive integral
  \(\widehat{\mathfrak{sl}}_2\) level, TUY/Hitchin finite-rank
  conformal-block sheaf, integrable-module truncation, KZB projectively
  flat connection, boundary sewing, determinant-anomaly matching, and
  the ordered-chain-to-TUY comparison morphism.  Handle and separating
  factorisation are TUY factorisation plus ordered sewing comparison,
  not raw ordered-bar factorisation.
- `standalone/e1_primacy_ordered_bar.tex` and
  `standalone/en_chiral_operadic_circle.tex`: propagated the same
  conditional type signature to the compact standalone Verlinde
  propositions.
- `chapters/frame/preface.tex`,
  `standalone/survey_modular_koszul_duality_v2.tex`, and
  `compute/lib/verlinde_ordered_engine.py`: replaced first-reader and
  compute-docstring recovery language by the ordered/TUY comparison
  lane.
- `compute/tests/test_determinant_anomaly_conformal_block_scope.py`:
  added a regression guard requiring the comparison package and
  forbidding the retired raw ordered-homology-to-conformal-block
  phrases.

Verification:

- `python3 -m py_compile
  compute/tests/test_determinant_anomaly_conformal_block_scope.py`
  passed.
- `pytest -q
  compute/tests/test_determinant_anomaly_conformal_block_scope.py`
  passed.

## 2026-06-18 -- Pass 563: Lossy descent kernel criterion

Audit anchor: expanded repair specification A8 and the ordered
chiral-homology standalone.  Proposition `prop:lossy-descent` said
the ordered-to-symmetric map is "surjective but not injective for
\(n\ge2\)" for every \(\Eone\)-chiral algebra.  That overstates the
claim: scalar abelian or otherwise trivial-isotypic windows can be
lossless in a fixed arity.

Repairs:

- `standalone/ordered_chiral_homology.tex`: replaced the universal
  non-injectivity assertion by the exact completed coinvariant kernel
  criterion.  The kernel is the completed relation subspace
  generated by \(\sigma c-c\), or in the \(R\)-twisted case by
  \(r\sigma\otimes c-r\otimes\sigma c\).  Non-injectivity is now
  asserted precisely when a nontrivial ordered \(\Sigma_n\)-isotypic
  or \(R\)-twisted component survives in the finite window.  The
  \(r\)-matrix, associator, and higher obstruction classes are
  witnesses when present, not universal axioms.
- `standalone/introduction_full_survey.tex`: changed the first-reader
  information-content paragraph to the same kernel criterion, matching
  the visible Heisenberg scalar exception.
- `compute/tests/test_ordered_symmetric_conductor_scope.py`: added a
  regression guard requiring the kernel criterion and blocking the
  retired universal non-injectivity phrasing.

Verification:

- `python3 -m py_compile
  compute/tests/test_ordered_symmetric_conductor_scope.py` passed.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py`:
  8 passed.

## 2026-06-18 -- Pass 562: Symmetric-power descent is finite direct image, not coarse-stack equivalence

Audit anchor: expanded repair specification A8/B3 and the ordered
chiral-homology standalone.  Proposition `prop:sym-descent` correctly
wanted Beilinson--Drinfeld symmetric descent, but its proof asserted
that \(\cD\)-modules on \([X^n/\Sigma_n]\) and on the coarse symmetric
power \(X^{(n)}\) have equivalent categories because \(\Sigma_n\) is
finite in characteristic zero.  Stabilizers along diagonals make that
too strong.

Repairs:

- `standalone/ordered_chiral_homology.tex`: retagged
  Proposition `prop:sym-descent` as \(\ClaimStatusConditional\) with a
  type signature.  The proof now keeps equivariant descent through the
  quotient stack, explicitly denies equivalence with arbitrary
  \(\cD\)-modules on the coarse symmetric power, and obtains the
  Beilinson--Drinfeld symmetric object as the Reynolds summand of the
  finite direct image \(\pi_{n,+}\cF_n^{\mathrm{ord}}\).  The
  diagonal/ramification issue is now handled by a regular-extension
  hypothesis.
- `compute/tests/test_ordered_symmetric_conductor_scope.py`: added a
  guard requiring the quotient-stack/coarse-symmetric-power distinction
  and blocking the retired coarse-category-equivalence and
  ramification-irrelevance phrases.

Verification:

- `python3 -m py_compile
  compute/tests/test_ordered_symmetric_conductor_scope.py` passed.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py`:
  7 passed.

## 2026-06-18 -- Pass 561: \(E_1\)-primacy averaging finite-window status

Audit anchor: expanded repair specification A8 and the universal
conductor theorem.  The canonical conductor chapter had the correct
finite-window \(R\)-twisted descent criterion, but the standalone
\(E_1\)-primacy exposition still carried a theorem titled
"\(\av_R\) is a surjective dg Lie morphism" without a claim-status
marker or type signature, and its proof spoke of "any section" of the
ribbon-forgetting quotient.

Repairs:

- `standalone/e1_primacy_ordered_bar.tex`: retied
  Theorem `thm:av-surjective` to the finite-window conductor package.
  It is now \(\ClaimStatusConditional\), with type signature
  \((\)Open quadrant, ordered-to-symmetric convolution presentation,
  Beilinson levels \(2\) and \(5\), finite-window chain section,
  strong-unitary \(R\)-twisted descent, completed Reynolds-kernel
  bracket ideal, and conductor coefficient multiplication\()\).  The
  section language now says a chosen finite-window chain section plus
  homotopy is required; without it the displayed average is only a
  linear projection.
- `compute/tests/test_ordered_symmetric_conductor_scope.py`: added a
  regression guard requiring the conditional status/type package and
  forbidding the retired "any section" and unqualified descent phrases.

Verification:

- `python3 -m py_compile
  compute/tests/test_ordered_symmetric_conductor_scope.py` passed.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py`:
  6 passed.

## 2026-06-18 -- Pass 560: Universal W-algebra critical PBW scope

Audit anchor: the external strengthening Theorem-H firewall and the
Pass 559 PBW critical/admissible correction.  The detailed
\(\mathcal W\)-algebra existence proposition still said the universal
\(\mathcal W^k(\mathfrak g,f_{\mathrm{prin}})\) is chirally Koszul at
every level.  That sentence made the conditional marker vacuous and hid
the critical Feigin--Frenkel centre/Sugawara--KZ boundary.

Repairs:

- `chapters/theory/existence_criteria.tex`: the table, scope remark,
  proposition, and proof now state the universal W-algebra result on
  the generic/non-critical principal \(\mathcal W\) lane.  Critical
  level is separated as the Feigin--Frenkel centre/Sugawara--KZ
  boundary, and admissible/simple quotient levels are sent to the
  null-vector obstruction test rather than inherited from PBW.
- `compute/tests/test_w_algebra_critical_pbw_scope.py`: added a
  source guard forbidding the retired every-level W-algebra Koszul
  phrases and requiring the generic/non-critical principal lane,
  critical boundary, finite-type/completed-dual, and Theorem-H/post-
  Verdier firewall language.

Verification:

- `python3 -m py_compile
  compute/tests/test_w_algebra_critical_pbw_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- `pytest -q compute/tests/test_w_algebra_critical_pbw_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py`: 20 passed.

## 2026-06-18 -- Pass 559: PBW universality critical/admissible firewall

Audit anchor: strengthening-PDF Theorem-H hypothesis firewall and the
critical/admissible off-locus warnings.  Several summaries still said
that PBW universality covers universal affine \(V_k(\mathfrak g)\) at
every level "including critical and admissible."  That phrasing hides
two different boundaries: critical level is the Feigin--Frenkel
centre/Sugawara/KZ degeneration surface, and admissibility is a
condition on simple quotient levels, not an extra universal-PBW theorem.

Repairs:

- `chapters/frame/preface.tex` and
  `chapters/frame/preface_sections5_9_draft.tex`: rewrote the scope
  paragraphs so PBW universality applies on the verified universal
  non-critical PBW/Koszul lane; critical and admissible levels are
  separately typed.
- `standalone/survey_modular_koszul_duality.tex`,
  `standalone/survey_modular_koszul_duality_v2.tex`, and
  `standalone/survey_track_a_compressed.tex`: replaced the same
  compact overclaim with the non-critical PBW/Koszul lane plus the
  Feigin--Frenkel centre/Sugawara degeneration boundary and
  simple-quotient admissibility gate.
- `notes/volume_I_platonic_reconstitution.md`: corrected the older
  reconstitution summary so critical affine and admissible simple
  quotient cases are not presented as settled by rationality,
  \(C_2\)-cofiniteness, or conilpotent completion alone.
- `compute/tests/test_simple_quotient_bar_scope.py`: now blocks the
  retired "including critical and admissible" and "Koszul at every
  level including critical" phrases on the live summary surfaces, and
  requires the non-critical PBW lane plus critical-boundary wording.

Verification:

- `pytest -q compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_langlands_fle_bridge_scope.py`: 16 passed.
- `pytest -q compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_langlands_fle_bridge_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_theorem_linshaw_rigidity_engine.py`: 65 passed.
- Multiline stale-phrase scan over the guarded live summaries found no
  remaining `including critical and admissible`, `Koszul at every level
  including critical`, or `critical and admissible)` forms.
- `git diff --check --` on the touched Pass 559 files passed.

## 2026-06-18 -- Pass 558: Linshaw--Qi admissible rigidity scope

Audit anchor: strengthening-PDF Theorem-H/admissible-level firewall and
the simple-quotient repairs from Passes 552--553.  The Linshaw--Qi
rigidity helper still promoted \(L_{-4/3}(\mathfrak{sl}_2)\) from
vertex-algebra deformation rigidity to a proved chiral-Hochschild /
Koszul row, citing the retired `rem:admissible-koszul-status`.

Repairs:

- `compute/lib/theorem_linshaw_rigidity_engine.py`: separated
  Linshaw--Qi's \(H^2_{1/2}\)-rigidity result from the chiral
  Hochschild and quotient-bar claims.  The
  \(L_{-4/3}(\mathfrak{sl}_2)\) row now records
  `huang_rigidity=True`, but `is_koszul=None`, `is_rigid=None`,
  `koszul_status="CONDITIONAL_QUOTIENT_BAR"`, and
  `chirhoch_status="CONDITIONAL_QUOTIENT_BAR"`.
- The same engine now names the missing package: quotient-bar spectral
  sequence, PBW/Shapovalov detection, finite-window exactness, strong
  convergence, and comparison from Huang \(H^2_{1/2}\) to chiral
  Hochschild \(H^2\).
- `compute/tests/test_theorem_linshaw_rigidity_engine.py`: updated the
  admissible \(-4/3\) tests so Linshaw--Qi rigidity remains proved, but
  Theorem-H/Koszulness status remains conditional.
- `compute/tests/test_simple_quotient_bar_scope.py`: added the Linshaw
  engine to the global simple-quotient compute-surface guard and
  requires the `CONDITIONAL_QUOTIENT_BAR` marker.

Verification:

- `python3 -m py_compile
  compute/lib/theorem_linshaw_rigidity_engine.py
  compute/tests/test_theorem_linshaw_rigidity_engine.py
  compute/tests/test_simple_quotient_bar_scope.py` passed.
- `pytest -q compute/tests/test_theorem_linshaw_rigidity_engine.py`: 44 passed.
- `pytest -q compute/tests/test_theorem_linshaw_rigidity_engine.py
  compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py`: 56 passed.
- `git diff --check -- compute/lib/theorem_linshaw_rigidity_engine.py
  compute/tests/test_theorem_linshaw_rigidity_engine.py
  compute/tests/test_simple_quotient_bar_scope.py` passed.

## 2026-06-18 -- Pass 557: External-review navigation placeholder guard

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`,
section "Fatal build and navigation errors."  The old rendered PDF had
large numbers of unresolved `??` references and placeholder theorem /
chapter / table references.  A full LaTeX reference build remains a
session-end build-surface task, but the live source should at least be
guarded against reintroducing literal placeholder forms.

Repairs:

- `compute/tests/test_external_review_harvest_completion_scope.py`: added
  a non-build regression guard over `main.tex`, `chapters/`,
  `appendices/`, and `standalone/` visible TeX.  It rejects literal `??`
  placeholders and the reviewed fatal forms `Theorem ??`,
  `Proposition ??`, `Chapter ??`, `Table ??`, `§??`, and
  `Vol II Remark ??`.
- The guard deliberately does not classify cross-volume references such
  as `Vol~II Remark~\ref{...}` as errors; those require the actual
  LaTeX/xr build surface, not a string check.

Verification:

- `python3 -m py_compile
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py`:
  5 passed.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_theorem_h_kdh_certificate_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py`: 28 passed.
- Targeted temporary-marker and Theorem-H overclaim scans over the touched
  guard, KDH checker, ledger, and matrix were clean.

## 2026-06-18 -- Pass 556: KDH finite-window certificate checker

Audit anchor: Pass 555 proved the abstract finite-window KDH contraction
certificate, but family-specific work still needed an exact way to check
the finite algebraic data before any infinite-tower claim is made.

Repairs:

- `compute/lib/kdh_certificate_engine.py`: added an exact rational
  finite-window checker for the algebraic part of
  Proposition `prop:theorem-h-finite-window-kdh-certificate`.  It checks
  \(d^2=0\), \(p^2=p\), \(dp=pd\), \(dh+hd=\mathrm{id}-p\), vanishing of
  \(p\) in degrees \(\geq3\), exact rank-nullity high-tail cohomology
  dimensions, and, for a tower prefix, transition maps that are cochain
  maps, degreewise surjective, and compatible with the projectors.
- `compute/tests/test_kdh_certificate_engine.py`: added tests for a
  valid contractible high-tail model, a valid two-window tower, exact
  rational matrix rank, exact rank-nullity cohomology dimensions, and
  failures for broken homotopy, nonzero high-tail projector, nonzero
  high-tail cohomology, and non-surjective transition.
- The engine and tests explicitly state their logical scope: they check
  finite-window algebra only.  They do not construct KDH windows for any
  family, do not prove an infinite tower, and do not prove Theorem~H.
- `notes/external_review_harvest_matrix_20260617.md`: recorded this
  checker under the Theorem-H source-work rows.

Verification:

- `python3 -m py_compile compute/lib/kdh_certificate_engine.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_theorem_h_kdh_certificate_scope.py` passed.
- `pytest -q compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_theorem_h_kdh_certificate_scope.py`: 13 passed.
- Targeted overclaim scan over the checker, checker tests, ledger, and
  matrix found no active phrases saying that the checker proves
  Theorem~H, constructs all family windows, or turns a finite prefix into
  an infinite tower proof.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_kdh_certificate_engine.py
  compute/tests/test_theorem_h_kdh_certificate_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py`: 27 passed.
- Matrix table-status guards found no `open`, `audit`, `partial`,
  `ongoing`, or unverified row; historical/explanatory uses
  of those words remain in the audit log.
- `git diff --check -- compute/lib/kdh_certificate_engine.py
  compute/tests/test_kdh_certificate_engine.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.

## 2026-06-18 -- Pass 555: Theorem-H finite-window KDH certificate

Audit anchor: source-level Theorem~H residual obligations in
`notes/external_review_harvest_matrix_20260617.md`: ordered
residue-twisted acyclicity, completion, and family finite-window
certificates.  The KDH obstruction surface already identified the exact
high-degree tail, but it did not yet provide a theorem-level bridge from
explicit finite-window chain contractions to completed KDH acyclicity.

Repairs:

- `chapters/theory/theorem_h_off_koszul_platonic.tex`: added
  Proposition `prop:theorem-h-finite-window-kdh-certificate`.  It proves
  the homological algebra certificate: if
  \(\mathrm{KD}_{\mathrm H}^\bullet(\cA)\cong\varprojlim_N K_N^\bullet\)
  is a strict inverse system of finite-dimensional KDH windows with
  surjective transition maps, and each window carries a projector
  \(p_N\) onto degrees \(\leq2\) plus a homotopy
  \(h_N\) satisfying \(d_Nh_N+h_Nd_N=\mathrm{id}-p_N\), then
  \(H^n(\mathrm{KD}_{\mathrm H}^\bullet(\cA))=0\) for \(n\geq3\).
  Under the depth-zero amplitude hypothesis this kills
  \(\ChirHoch^n(\cA)\) for \(n\geq3\).  The proof uses the finite-window
  homotopy identity and the Milnor exact sequence; the degree-3
  \(\varprojlim^1 H^2\) term vanishes by finite-dimensional
  Mittag--Leffler stabilization.
- The boundary firewall in the same chapter now names the certificate
  as sufficient for the high-degree tail, while stating that the
  family-specific KDH windows and transition maps still have to be
  constructed.
- `chapters/connections/concordance.tex`: the controlling Theorem~H row
  now records the certificate as a family-specific input, not a formal
  consequence of rationality or \(C_2\)-cofiniteness.
- `compute/tests/test_theorem_h_kdh_certificate_scope.py`: added a
  regression guard for the theorem statement, concordance sync, and
  ledger/matrix record.
- `notes/external_review_harvest_matrix_20260617.md`: recorded this
  pass under the D5 and Theorem-H/Hochschild residual-source-work rows.

Verification:

- `python3 -m py_compile compute/tests/test_theorem_h_kdh_certificate_scope.py
  scripts/generate_metadata.py` passed.
- `pytest -q compute/tests/test_theorem_h_kdh_certificate_scope.py`: 3 passed.
- `python3 scripts/generate_metadata.py` passed and regenerated
  `metadata/claims.jsonl`, `metadata/census.json`,
  `metadata/dependency_graph.dot`, `metadata/label_index.json`,
  `metadata/theorem_registry.md`, and `standalone/theorem_index.tex`;
  the new proposition appears in the registry as
  `prop:theorem-h-finite-window-kdh-certificate`.
- `pytest -q compute/tests/test_theorem_h_kdh_certificate_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py
  compute/tests/test_generate_metadata_parser.py`: 21 passed.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_theorem_h_kdh_certificate_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py
  compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_w_orbit_duality_scope.py`: 27 passed.
- Targeted overclaim scan found no active occurrences of the forbidden
  phrases saying that finite-window tables, rationality, or
  \(C_2\)-cofiniteness prove Theorem~H for a family.
- `git diff --check --` on the touched Theorem-H, concordance, guard,
  ledger, matrix, and regenerated metadata/index files passed.
- No full LaTeX build was run in this pass.

## 2026-06-18 -- Pass 554: BP scalar-conductor compute scope

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
the review H free-field/W/DS/AGT gate, B5 Gaiotto boundary/bulk
separation, and the Pass 531 W-orbit scope repair.  The BP conductor
engine and its tests still presented the exact identity
\(c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=196\) in theorem-level
language.  The identity is correct scalar arithmetic, but it does not
prove BP same-family Koszul duality, non-principal DS/bar transport,
bar-cobar inversion, or Theorem~H.

Repairs:

- `compute/lib/bp_koszul_conductor_engine.py`: retagged as a
  scalar-conductor diagnostic engine.  The header now states that the
  central-charge companion, kappa complementarity, self-dual level, and
  anomaly-ratio identities are scalar checks only.  Interpreting
  \(k'=-k-6\) as the actual Verdier/Koszul branch now explicitly
  requires the subregular DS/bar transport hypothesis.
- `compute/tests/test_bp_koszul_conductor_engine.py`: changed
  theorem-level test rhetoric to scalar-diagnostic rhetoric.  The
  independent-verification block now describes a scalar polynomial
  identity in \(\mathbb Q(k)\), not a proof of BP same-family duality.
- `compute/tests/test_w_orbit_duality_scope.py`: extended the W-orbit
  scope guard so the BP scalar-conductor layer cannot regress into a
  theorem-level duality, non-principal DS/bar, bar-cobar, or Theorem-H
  proof surface.
- `compute/tests/test_external_review_harvest_completion_scope.py`: the
  external-review completion guard now requires the Pass 554 matrix
  entry.
- `notes/external_review_harvest_matrix_20260617.md`: recorded this
  pass under the theorem-status and free-field/W rows.

Verification:

- `python3 -m py_compile
  compute/lib/bp_koszul_conductor_engine.py
  compute/tests/test_bp_koszul_conductor_engine.py
  compute/tests/test_w_orbit_duality_scope.py` passed.
- `pytest -q compute/tests/test_bp_koszul_conductor_engine.py
  compute/tests/test_w_orbit_duality_scope.py`: 78 passed.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_bp_koszul_conductor_engine.py
  compute/tests/test_w_orbit_duality_scope.py`: 82 passed.
- Targeted stale-phrase scan over the BP scalar-conductor engine,
  scalar-diagnostic test, and W-orbit guard found no active occurrences
  of the retired theorem-level BP duality / Theorem-H proof phrases.
- `git diff --check --
  compute/lib/bp_koszul_conductor_engine.py
  compute/tests/test_bp_koszul_conductor_engine.py
  compute/tests/test_w_orbit_duality_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 553: Admissible simple-quotient theorem-surface sync

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
D5 / Theorem-H admissible off-locus scope, A1 / theorem-status
firewall, and the Pass 552 simple-quotient diagnostic repair.  Pass 552
fenced the legacy `bar_cohomology_simple_quotient_engine.py` helper as
finite evidence, but live theorem-facing text still promoted
\(L_k(\mathfrak{sl}_2)\) admissible simple quotients to a settled
Koszul theorem and several compute surfaces still used the same proved /
unconditional language.

Repairs:

- `chapters/theory/chiral_koszul_pairs.tex`: the admissible
  simple-quotient remark no longer says rank-one admissible Koszulness
  is settled.  It now states the finite Shapovalov/character evidence
  and names the missing package: quotient bar spectral sequence,
  PBW/Shapovalov detection of higher differentials, finite-window
  exactness, and strong convergence.  The rank-one statement is not an
  input to Theorem~H or bar-cobar inversion until that package is
  supplied.
- `chapters/examples/kac_moody.tex`,
  `chapters/connections/concordance.tex`,
  `chapters/theory/theorem_h_off_koszul_platonic.tex`, and the preface
  surfaces now agree with the same status: rationality and
  \(C_2\)-cofiniteness are finiteness inputs, not Koszulness criteria,
  and the rank-one lane is conditional/evidence rather than proved.
- Standalone mirrors
  `standalone/koszulness_fourteen_characterizations.tex`,
  `standalone/survey_track_a_compressed.tex`,
  `standalone/survey_modular_koszul_duality.tex`,
  `standalone/survey_modular_koszul_duality_v2.tex`,
  `standalone/programme_summary.tex`, and
  `standalone/programme_summary_sections9_14.tex` received the same
  repair, including removal of the false "bar functor preserves
  surjections, hence concentration transfers" argument.
- Compute surfaces were retagged: `theorem_admissible_koszul_sl3_engine.py`
  treats rank-one admissible \(sl_2\) as finite evidence/conditional;
  `vertex_algebra_extensions_engine.py` returns `None` rather than
  `True` for the simple-quotient Koszul verdict; and
  `theorem_universal_chiral_genus_extension_engine.py` no longer admits
  admissible simple quotients into the proved genus-extension tier.
- The related admissible \(sl_3\) Li-bar engines
  `admissible_sl3_d1_rank_engine.py` and
  `admissible_sl3_d1_poisson_engine.py` are now model diagnostics, not
  theorem-level proofs of simple-quotient Koszulness.  Their
  q\(\leq2\) outputs are `conditional-model`, and the q\(\geq3\)
  Poisson obstruction is finite-model evidence unless the quotient-bar
  comparison/convergence package is supplied.
- Historical audit notes that repeated the old rank-one claim now carry
  superseded-status text.
- `compute/tests/test_simple_quotient_bar_scope.py` now guards the live
  TeX, standalone, and compute status surfaces against reintroducing
  the retired theorem phrases.

Verification:

- `python3 -m py_compile
  compute/tests/test_simple_quotient_bar_scope.py
  compute/lib/theorem_admissible_koszul_sl3_engine.py
  compute/tests/test_theorem_admissible_koszul_sl3_engine.py
  compute/lib/vertex_algebra_extensions_engine.py
  compute/tests/test_vertex_algebra_extensions.py
  compute/lib/theorem_universal_chiral_genus_extension_engine.py
  compute/tests/test_theorem_universal_chiral_genus_extension_engine.py
  compute/lib/admissible_sl3_d1_rank_engine.py
  compute/tests/test_admissible_sl3_d1_rank_engine.py
  compute/lib/admissible_sl3_d1_poisson_engine.py
  compute/tests/test_admissible_sl3_d1_poisson_engine.py` passed.
- `pytest -q compute/tests/test_simple_quotient_bar_scope.py`: 6 passed.
- `pytest -q
  compute/tests/test_theorem_admissible_koszul_sl3_engine.py
  compute/tests/test_vertex_algebra_extensions.py
  compute/tests/test_theorem_universal_chiral_genus_extension_engine.py
  compute/tests/test_admissible_sl3_d1_rank_engine.py
  compute/tests/test_admissible_sl3_d1_poisson_engine.py`: 422 passed.
- `pytest -q compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py`: 20 passed.
- Targeted retired-phrase scan over the repaired admissible
  simple-quotient TeX, standalone, compute, and audit surfaces found no
  active occurrences of the old settled/proved/unconditional slogans.
- `git diff --check --` on the touched Pass 553 files passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 552: Simple-quotient sl2 bar diagnostic scope

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
A1 / theorem-status firewall, D5 / Theorem-H admissible/off-locus
scope, and B3 / Hochschild-bar object discipline.  The legacy
`bar_cohomology_simple_quotient_engine.py` presented a finite
Shapovalov/character helper as if it computed
\(H^\bullet(B(L_k(\mathfrak{sl}_2)))\) and proved all admissible
\(\mathfrak{sl}_2\) simple quotients Koszul.  Inspection showed the
opposite scope: `bar_cohom_dim` returned the universal
\(V_k(\mathfrak{sl}_2)\) bar-cohomology model, while `quotient_dim`
above the Shapovalov budget returned the Verma dimension as an
upper-bound placeholder.  The helper is useful finite evidence, but it
does not prove the quotient bar spectral sequence for all admissible
levels.

Repairs:

- `compute/lib/bar_cohomology_simple_quotient_engine.py`: retagged the
  module as a finite Shapovalov/character diagnostic.  The header now
  names the exact missing proof obligation: quotient bar spectral
  sequence, PBW/Shapovalov detection, finite-window exactness, and
  strong convergence.
- Added `MODEL_SCOPE` with `not_proof_all_admissible=True`,
  `uses_universal_cohomology_model=True`, and
  `uses_verma_upper_bound_above_shapovalov_budget=True`.
- `SimpleQuotientBarResult` now carries the same scope metadata at
  runtime.  The legacy `is_koszul` flag is explicitly the verdict of
  the finite/universal model, not a theorem-status proof flag.
- `koszulness_structural_analysis` now returns `verdict_scope`,
  `not_proof_all_admissible`, `cohomology_model`, and
  `missing_proof_obligation`.  Its prose no longer says the engine
  proves all admissible \(\mathfrak{sl}_2\) levels.
- `compute/tests/test_bar_cohomology_simple_quotient_engine.py`:
  changed theorem/proof rhetoric to finite diagnostic rhetoric and
  added assertions for the new non-proof metadata.
- `compute/tests/test_simple_quotient_bar_scope.py`: added a source and
  runtime guard against reintroducing the old unconditional/simple-
  quotient theorem phrases.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the D5
  and H/free-field/admissible rows with this compute-surface repair.

Verification:

- `python3 -m py_compile
  compute/lib/bar_cohomology_simple_quotient_engine.py
  compute/tests/test_bar_cohomology_simple_quotient_engine.py
  compute/tests/test_simple_quotient_bar_scope.py` passed.
- `pytest -q compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_bar_cohomology_simple_quotient_engine.py`: 119 passed.
- `pytest -q compute/tests/test_simple_quotient_bar_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`: 18 passed.
- Retired-phrase scan over the engine and legacy test found no active
  occurrences of the old unconditional/simple-quotient theorem slogans
  outside the new guard's forbidden-string list.
- Matrix scan found no `open`/`audit`/`partial`/`ongoing` table statuses
  and confirmed the Pass 552 matrix and ledger records.
- `git diff --check --
  compute/lib/bar_cohomology_simple_quotient_engine.py
  compute/tests/test_bar_cohomology_simple_quotient_engine.py
  compute/tests/test_simple_quotient_bar_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 551: FLE critical-level reflection scope

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
C3 / Feigin--Frenkel language and D5 / Theorem-H critical-level scope.
The legacy `theorem_langlands_fle_bridge_engine.py` still presented a
finite critical-level table as a "six independent methods" verification
of the Langlands/FLE bridge, and it described the fixed point of
\(k\mapsto -k-2h^\vee\) as if the Koszul dual algebra were the algebra
itself.  That is the exact C3 failure mode: the critical-level reflection
is a scalar/reflected-level check, while the Feigin--Frenkel centre,
chiral Koszul dual object, bar-cobar inverse, derived centre, and
categorical FLE are separate objects/statements.

Repairs:

- `compute/lib/theorem_langlands_fle_bridge_engine.py`: retagged the
  module as a finite critical-level consistency suite for the
  cohomological shadow \(H^\bullet(B(V_{\mathrm{crit}}(\mathfrak g)))
  \simeq \Omega^\bullet(\mathrm{Op}_{\mathfrak g^\vee}(D))\).  The
  header now states that it does not prove the categorical FLE and does
  not identify critical centres, chiral Koszul duals, bar-cobar inverses,
  or derived chiral centres.
- The old "Feigin--Frenkel involution/self-duality" method is now the
  critical-level reflection fixed-point check.  Its scope is explicitly
  level-reflection only: not strict Koszul self-duality, not KSDual
  membership, and not self-complementarity.
- `FLEBridgeResult` and `ff_involution_analysis` now expose runtime
  metadata:
  `finite critical-level consistency checks; not a proof of the
  categorical FLE`, `level reflection fixed point only; not strict Koszul
  self-duality`, `not_koszul_self_dual=True`, and
  `critical_not_koszul=True`.
- `critical_vs_generic_comparison` now says generic-level Koszulness is
  conditional on the named PBW/chiral-Koszul/finite-type/completion
  package rather than automatic for every non-critical level.
- `compute/tests/test_theorem_langlands_fle_bridge_engine.py`: changed
  the test rhetoric from proof/complete-bridge wording to finite
  cohomological-shadow consistency checks and added assertions for the
  new scope metadata.
- `compute/tests/test_langlands_fle_bridge_scope.py`: added a source and
  runtime guard against the retired proof/self-duality/genericity
  phrases and against future ledger/matrix drift.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the C3
  and D5 rows with this compute-surface repair.

Verification:

- `python3 -m py_compile
  compute/lib/theorem_langlands_fle_bridge_engine.py
  compute/tests/test_theorem_langlands_fle_bridge_engine.py
  compute/tests/test_langlands_fle_bridge_scope.py` passed.
- `pytest -q compute/tests/test_langlands_fle_bridge_scope.py
  compute/tests/test_theorem_langlands_fle_bridge_engine.py
  compute/tests/test_theorem_fle_critical_level_engine.py
  compute/tests/test_feigin_frenkel_reflection_scope.py`: 169 passed.
- `pytest -q compute/tests/test_langlands_fle_bridge_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_factorization_homology_shadow_scope.py
  compute/tests/test_annulus_trace_model_scope.py`: 13 passed.
- Retired-phrase scan over the engine and legacy bridge test found no
  active occurrences of the old proof/self-duality/genericity claims
  outside the new guard's forbidden-string list.
- Matrix scan found no `open`/`audit`/`partial`/`ongoing` table statuses
  and confirmed the Pass 551 matrix and ledger records.
- `git diff --check -- compute/lib/theorem_langlands_fle_bridge_engine.py
  compute/tests/test_theorem_langlands_fle_bridge_engine.py
  compute/tests/test_langlands_fle_bridge_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 550: Topological shadow scope for explicit factorization homology

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
B3 / Gelfand gate and B5 / open--closed slot separation.  A live compute
surface, `factorization_homology_explicit_engine.py`, still presented
selected Verlinde/WRT/Drinfeld-center numbers as "actual" raw
factorization-homology computations.  The most dangerous statements were
that \(T^2\times I\) factorization homology equals a Drinfeld center and
that a punctured sphere output is equivalently a module over the chiral
derived center.  Those statements are correct only after changing the
input to a topologized modular tensor category or supplying a
Swiss-cheese/OCA comparison; they are not statements about raw chiral
factorization homology.

Repairs:

- `compute/lib/factorization_homology_explicit_engine.py`: retagged the
  module as a finite topological-shadow table.  It now states that it is
  not a chain-level computation of raw chiral factorization homology and
  does not identify critical centers, chiral derived centers, Drinfeld
  centers, or bar cohomology.
- The \(T^2\times I\) Drinfeld-center function now explicitly has input
  type "modular tensor category supplied by CS/WRT topologization" and
  output type "global dimension of \(Z(C)\)"; return metadata records
  `topologized MTC/WRT shadow only`, `not_raw_chiral_factorization_homology`,
  and `not_chiral_derived_center`.
- The punctured-sphere helper now returns the boundary \(A\)-bimodule
  structure and says any chiral derived-center action requires a separate
  Swiss-cheese/OCA comparison datum; locality alone no longer supplies an
  equivalent \(Z^{\mathrm{der}}_{\mathrm{ch}}\)-module statement.
- `compute/tests/test_factorization_homology_explicit_engine.py`: changed
  the test description and Drinfeld-center class from equality rhetoric
  to topologized MTC/WRT shadow rhetoric, and asserts the new `MODEL_SCOPE`
  and return metadata.
- `compute/tests/test_factorization_homology_shadow_scope.py`: added a
  source-level guard for the old phrases and for this ledger/matrix
  record.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the B3 and
  K/open--closed rows with this compute-surface scope repair.

Verification:

- `python3 -m py_compile
  compute/lib/factorization_homology_explicit_engine.py
  compute/tests/test_factorization_homology_explicit_engine.py
  compute/tests/test_factorization_homology_shadow_scope.py` passed.
- `pytest -q compute/tests/test_factorization_homology_shadow_scope.py
  compute/tests/test_factorization_homology_explicit_engine.py`: 51 passed.
- `pytest -q compute/tests/test_factorization_homology_shadow_scope.py
  compute/tests/test_factorization_homology_explicit_engine.py
  compute/tests/test_annulus_trace_model_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  58 passed.
- `git diff --check -- compute/lib/factorization_homology_explicit_engine.py
  compute/tests/test_factorization_homology_explicit_engine.py
  compute/tests/test_factorization_homology_shadow_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- Matrix scan confirmed the Pass 549/550 records and found no
  `open`/`audit`/`partial`/`ongoing` table statuses.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 549: Annulus Hochschild chain-model firewall

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
B3 / Gelfand gate.  The review instruction says to keep chiral
Hochschild, algebraic Hochschild, topological Hochschild, Lie
cohomology, Gelfand--Fuchs cohomology, critical centers, derived
centers, Drinfeld centers, and bar cohomology in typed comparison
slots.  The open/closed annulus theorem already separated the slots, but
its proof still used a loose "two-sided bar equals cyclic word" step, and
the legacy compute helper still read as if it verified literal
Hochschild dimensions and a topological annulus partition function.

Repairs:

- `chapters/connections/thqg_open_closed_realization.tex`: rewrote the
  annulus trace proof's Step 4.  The derived tensor product
  \(A_b\otimes_{A_b^e}^{\mathbf L}A_b\) is now computed by the standard
  \(A_b^e\)-free bar resolution of the diagonal, then by tensoring over
  \(A_b^e\) to obtain the ordinary Hochschild chain complex.  The
  cyclic-object notation \(B^{\mathrm{cyc}}\) is explicitly not a naive
  cyclic coinvariant quotient of an ordered bar complex, and Connes'
  operator is restricted to the cyclic/negative-cyclic refinement rather
  than the ordinary Hochschild differential.
- `compute/lib/annulus_trace_verification.py`: retagged the module as a
  finite annulus-trace table helper.  It now says that it does not build
  a Hochschild complex, compute a differential, prove Theorem~H, prove
  Calabi--Yau duality, or compute THH.  The normalized scalar value
  remains as legacy table metadata only after the \(H_H\), completion,
  genericity, and CY trace data have been supplied elsewhere.
- `compute/tests/test_annulus_trace_verification.py`: changed the legacy
  tests from theorem-verification rhetoric to table-shape regression
  tests and added an assertion for the helper's `MODEL_SCOPE` metadata.
- `compute/audit/compute_chirhoch_complete_sweep.md`: changed the old
  `AUDITED (clean)` row for `annulus_trace_verification.py` to
  `AUDITED + FENCED`.
- `compute/tests/test_annulus_trace_model_scope.py`: added a B3 guard
  that checks the manuscript chain model, the compute helper scope, the
  retired `b+B` ordinary-Hochschild wording, and the ledger/matrix record.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the B3
  and E/Hochschild rows with this annulus-trace table/chain-model pass.

Verification:

- `python3 -m py_compile compute/lib/annulus_trace_verification.py
  compute/tests/test_annulus_trace_verification.py
  compute/tests/test_annulus_trace_model_scope.py` passed.
- `pytest -q compute/tests/test_annulus_trace_model_scope.py
  compute/tests/test_annulus_trace_verification.py`: 80 passed.
- `pytest -q compute/tests/test_annulus_trace_model_scope.py
  compute/tests/test_annulus_trace_verification.py
  compute/tests/test_three_hochschild_unification.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  93 passed.
- `git diff --check -- chapters/connections/thqg_open_closed_realization.tex
  compute/lib/annulus_trace_verification.py
  compute/tests/test_annulus_trace_verification.py
  compute/tests/test_annulus_trace_model_scope.py
  compute/audit/compute_chirhoch_complete_sweep.md
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- Matrix status scan found no `open`/`audit`/`partial`/`ongoing` table
  statuses.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 548: Y-algebra Gaiotto gate

Audit anchor: `expanded_expert_repair_specification_main36 (1).md`,
B5 / Gaiotto gate: no class-S, corner-VOA, or \(Y\)-algebra claim
without \(\Omega\)-background parameters, boundary labels, and a named
comparison package.  This pass also harvests the D2/D3 firewall
consequence from Pass 547: a parameter-reflected companion is not
bar--cobar inversion and is not a strict Koszul dual without an
independent Verdier/formality comparison.

Repairs:

- `chapters/examples/y_algebras.tex`: inserted the chapter-level
  Gaiotto--Rap\v{c}\'ak junction datum before the theorem table:
  \(Y_{N_1,N_2,N_3}[\Psi]\) is used with fixed
  \(\Omega\)-background parameters and
  \(\mathrm{GL}(N_1),\mathrm{GL}(N_2),\mathrm{GL}(N_3)\) boundary
  labels; algebraic BRST/truncation, chiral Koszul, and physical
  bulk/boundary claims are separate lanes unless a named comparison
  package is supplied.
- Retagged `thm:y-central-charge` as a conditional truncation-lane
  scalar, not an unqualified physical VOA central-charge theorem.  The
  proof now explains why the \(Y_{0,0,N}\) discrepancy is a
  normalisation/decoupled-\(U(1)\) issue rather than a proved physical
  central-charge formula.
- Retagged `prop:y-koszul-dual` as a conditional Verdier/BRST
  comparison.  The proposition now assumes \(H_Y^\vee\): fixed
  junction/\(\Omega\)/boundary data, PBW chiral Koszulness, convergence
  of the Verdier-dual completed bar construction, and a BRST/DS
  comparison identifying the Verdier output with the parameter-reflected
  corner VOA.  It states \(K_X(Y[\Psi])=\mathbb D_{\Ran}\bar B_X(Y[\Psi])
  \simeq Y[-\Psi]\), and explicitly requires a further
  formality/minimal-model comparison before a strict \(Y[\Psi]^!\) may
  be named.
- Removed the \(Y\)-chapter drift phrases that called
  \(\Psi\mapsto-\Psi\) the Feigin--Frenkel involution on \(\Psi\), made
  it Verdier duality by itself, or treated the self-dual point as an
  unconditional Koszul-duality fixed point.
- Tightened the opening five-theorem table from a "verification" table
  to a status table: bar--cobar inversion, \(Y\)-channel
  complementarity, and channel-by-channel \(\kappa\) are all marked
  conditional on their stated generic/PBW/comparison packages instead
  of being displayed as unqualified proved rows.
- `chapters/examples/w_algebras_deep.tex`: changed the \(Y\)-algebra
  duality-compatibility remark from "Feigin--Frenkel duality" / "FF-dual"
  language to the parameter-reflected BRST companion and conditional
  Verdier/BRST comparison lane.
- `compute/tests/test_y_algebras_gaiotto_gate_scope.py`: added a live
  guard for the junction datum, conditional dual comparison, truncation
  central-charge scope, table/remark propagation, the
  `w_algebras_deep` \(Y\)-section, and this matrix/ledger record.
- `notes/external_review_harvest_matrix_20260617.md`: upgraded the B5
  Gaiotto-gate row and residual summary with this \(Y\)-algebra pass.

Verification:

- `python3 -m py_compile
  compute/tests/test_y_algebras_gaiotto_gate_scope.py
  compute/tests/test_y_algebras_scalar_typing.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- `pytest -q compute/tests/test_y_algebras_gaiotto_gate_scope.py
  compute/tests/test_y_algebras_scalar_typing.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  11 passed.
- `pytest -q compute/tests/test_y_algebras_gaiotto_gate_scope.py
  compute/tests/test_y_algebras_scalar_typing.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_feigin_frenkel_reflection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  21 passed.
- `git diff --check -- chapters/examples/y_algebras.tex
  chapters/examples/w_algebras_deep.tex
  compute/tests/test_y_algebras_gaiotto_gate_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 547: No Koszul dual from the bar--cobar counit

Audit anchor: `chiral1 Research Paper Strengthening.pdf`,
bar--cobar/Verdier items 275--280: define the Verdier-dualized
homotopy dual separately from reconstruction, do not call the strict
dual unless formality is supplied, and add a theorem-level statement
that \(\Omega B(A)\not\simeq A^!\) unless a separate self-duality
theorem is provided.

Repairs:

- `chapters/theory/theorem_A_infinity_2.tex`: added
  `cor:no-dual-from-barcobar-counit`, titled `No Koszul dual from the
  bar--cobar counit`.  The corollary states that the counit gives
  \[
    R_X(\cA)=\Omegach_X\Bbarch_X(\cA)\xrightarrow{\sim}\cA
  \]
  on the Koszul locus, while the homotopy Koszul dual lives on the
  Verdier branch
  \[
    K_X(\cA)=\mathbb D_{\Ran}\Bbarch_X(\cA)\simeq\cA^!_\infty.
  \]
- The only permitted comparison
  \(\Omegach_X\Bbarch_X(\cA)\simeq\cA^!_\infty\) is the composite of
  the reconstruction counit with an independently supplied
  self-duality equivalence
  \(\sigma_\cA\colon\cA\xrightarrow{\sim}\cA^!_\infty\).
- The corollary also fences the strict dual: replacing
  \(\cA^!_\infty\) by a strict \(\cA^!\) requires a separate
  formality/minimal-model comparison \(\cA^!_\infty\simeq\cA^!\).
  Without these extra data, \(\Omegach_X\Bbarch_X(\cA)\simeq\cA^!\)
  is not a theorem of bar--cobar adjunction.
- `compute/tests/test_theorem_a_reconstruction_duality_firewall_scope.py`:
  added a guard for the new corollary, the self-duality-equivalence
  requirement, the strict-dual/formality requirement, and the separation
  of \(R_X\) from \(K_X\).
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass 547
  under the Theorem A / bar-cobar / Positselski row and residual
  harvest summary.

Verification:

- `python3 -m py_compile
  compute/tests/test_theorem_a_reconstruction_duality_firewall_scope.py
  compute/tests/test_theorem_ab_spine_ambient_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- `pytest -q compute/tests/test_theorem_a_reconstruction_duality_firewall_scope.py
  compute/tests/test_theorem_ab_spine_ambient_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  12 passed.
- `pytest -q compute/tests/test_theorem_a_reconstruction_duality_firewall_scope.py
  compute/tests/test_theorem_ab_spine_ambient_scope.py
  compute/tests/test_theorem_B_scope.py
  compute/tests/test_factorization_ambient_citation_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  24 passed.
- `git diff --check -- chapters/theory/theorem_A_infinity_2.tex
  compute/tests/test_theorem_a_reconstruction_duality_firewall_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 546: Ordered bar differential base-change naturality

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, ordered bar
items 238--239: prove \(d_B\) is natural under \'{e}tale maps of
curves, and prove smooth-base-change naturality under holonomic
finiteness.

Repairs:

- `chapters/theory/bar_construction.tex`: added
  `cor:ordered-bar-differential-base-change`.  For an \'{e}tale map
  \(u\colon Y\to X\), the induced map
  \(u_n\colon\FM_n(Y)\to\FM_n(X)\) gives
  \[
    \Phi_{u,n}\colon
    u_n^*\mathbb B^{\ord}_{X,n}(\cA)
    \xrightarrow{\sim}
    \mathbb B^{\ord}_{Y,n}(u^*\cA),
  \]
  and the corollary proves
  \[
    \Phi_{u,n}u_n^*d_\cA=d_{u^*\cA}\Phi_{u,n},\quad
    \Phi_{u,n}u_n^*d_{\mathrm{dR}}=d_{\mathrm{dR}}\Phi_{u,n},\quad
    \Phi_{u,n}u_n^*d_{\mathrm{res}}^X
    =d_{\mathrm{res}}^Y\Phi_{u,n}.
  \]
  Hence \(\Phi_{u,n}u_n^*d_B^X=d_B^Y\Phi_{u,n}\).
- The proof identifies \(u_n^{-1}(D^X_{ij})=D^Y_{ij}\), uses
  `prop:bar-residue-coordinate-independence` to prove
  \(u_n^*\operatorname{Res}_{D^X_{ij}}
    =\operatorname{Res}_{D^Y_{ij}}u_n^*\), and checks that the chiral
  product pulls back from \(\mu_{\cA}\) to \(\mu_{u^*\cA}\), so OPE
  mode projections commute with pullback.
- The same corollary adds the smooth-family statement only under the
  correct finite-window hypotheses: smooth proper curve family,
  relative FM stages, holonomic finite bar windows, and proper-support
  de~Rham direct-image base change.  Without those hypotheses the
  statement stops at the aritywise pullback identity before relative
  de~Rham pushforward.
- `compute/tests/test_ordered_bar_base_change_naturality_scope.py`:
  added a regression guard for the \'{e}tale pullback equations, the
  residue-pullback identity, chiral-product pullback, and the
  holonomic/proper-support smooth-base-change gate.
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass 546
  under the ordered chiral bar construction row and residual harvest
  summary.

Verification:

- `python3 -m py_compile
  compute/tests/test_ordered_bar_base_change_naturality_scope.py
  compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- `pytest -q compute/tests/test_ordered_bar_base_change_naturality_scope.py
  compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  17 passed.
- `pytest -q compute/tests/test_ordered_bar_base_change_naturality_scope.py
  compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`:
  269 passed.
- `git diff --check -- chapters/theory/bar_construction.tex
  compute/tests/test_ordered_bar_base_change_naturality_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 545: BD chiral operation and full OPE-mode bar residue

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, ordered bar
items 240--243: compare the ordered OPE residue with the
Beilinson--Drinfeld chiral operation, prove that the OPE residue is the
BD chiral operation on the Fulton--MacPherson boundary, prove that no
higher poles are lost, and give the arbitrary \(m\)-mode contribution.

Repairs:

- `chapters/theory/bar_construction.tex`: strengthened
  `thm:residue-formula` and
  `thm:bd-ope-residue-full-poles` (`BD chiral operation and full OPE
  residue`).  The theorem surface now displays the coefficient identity
  \[
    \operatorname{pr}_m\mu_{\mathrm{BD}}(a,b)=a_{(m)}b
  \]
  on the formal neighbourhood of the pairwise diagonal, with
  \(\mu_{\mathrm{BD}}\colon j_*j^*(\cA\boxtimes\cA)\to\Delta_!\cA\)
  named as the BD chiral operation.
- The arbitrary-mode residue formula
  `eq:ordered-residue-arbitrary-mode` is now explicitly tied to
  \(\operatorname{pr}_m\mu_{\mathrm{BD}}\): the Poincare residue removes
  only the logarithmic normal form, while the OPE-mode projection
  selects the pole order \(m+1\).  Thus higher poles are part of
  \(d_{\mathrm{res}}\), not artefacts lost by the bar construction.
- The BD comparison cites BD Sections 3.3--3.4 and keeps the type
  boundary honest: the ordered statement is before coinvariants, while
  `cor:bd-ope-symmetric-ran-differential` remains conditional on the
  ordered-to-symmetric descent criterion.
- The theorem now distinguishes the bar-residue statement from the
  polar connection kernel: the logarithmic form supplies the normal
  orientation and does not multiply the OPE pole by a second propagator
  pole.
- `compute/tests/test_bar_ope_mode_bd_comparison_scope.py`: added a
  regression guard for the arbitrary-mode formula, the
  \(\operatorname{pr}_m\mu_{\mathrm{BD}}\) coefficient identity, full
  pole retention, the no-second-propagator-pole boundary, and the
  conditional symmetric BD descent statement.
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass 545
  under the ordered chiral bar construction row and residual harvest
  summary.

Verification:

- `python3 -m py_compile
  compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- `pytest -q compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  13 passed.
- `pytest -q compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`:
  265 passed.
- `git diff --check -- chapters/theory/bar_construction.tex
  compute/tests/test_bar_ope_mode_bd_comparison_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 544: Coordinate independence of \(d_{\mathrm{res}}\)

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, ordered bar
items 235--237: prove local coordinate independence of \(d_B\), prove
the coordinate-change correction, and state when a stress tensor is
required for the Virasoro cocycle.

Repairs:

- `chapters/theory/bar_construction.tex`: added
  `prop:bar-residue-coordinate-independence`.  For an étale coordinate
  change \(w=f(z)\) near \(D_{ij}\), with \(u=z_i-z_j\) and
  \(v=w_i-w_j\), the proof writes \(v=u\,g\) with \(g\) invertible
  along \(D_{ij}\), hence
  \[
    d\log v=d\log u+d\log g
  \]
  and \(d\log g\) is regular along the collision divisor.
- The proposition proves
  \[
    \operatorname{Res}_{D_{ij}}\bigl(\alpha\wedge
    d\log(w_i-w_j)\bigr)
    =
    \operatorname{Res}_{D_{ij}}\bigl(\alpha\wedge
    d\log(z_i-z_j)\bigr)
  \]
  for simple-pole logarithmic forms \(\alpha\), with the same
  determinant-line sign convention.  Therefore the collision-residue
  summand \(d_{\mathrm{res}}\) of the ordered bar differential is
  independent of the affine/formal coordinate representative.
- The same proposition fences the stronger projective connection
  statement: the Schwarzian/Virasoro cocycle is asserted only when a
  conformal stress tensor \(T\) with central charge \(c\) is part of
  the structure.  Without that datum only \(\mathcal D\)-module
  coordinate naturality and residue invariance are asserted.
- `compute/tests/test_collision_form_local_global_scope.py`: added a
  guard for the theorem label, the \(v=u\,g\) factorisation, regularity
  of \(d\log g\), equality of residues, independence of
  \(d_{\mathrm{res}}\), and the no-stress-tensor/no-Virasoro-cocycle
  boundary.
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass
  544 under the local/global \(d\log\) and ordered-bar construction
  rows.

Verification:

- Label scan confirmed `app:signs-shifts` exists in `main.tex`.
- `python3 -m py_compile
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- Token scan over `prop:bar-residue-coordinate-independence` confirmed
  the theorem label, `\ClaimStatusProvedHere`, \(v=u\,g\),
  \(d\log v=d\log u+d\log g\), regularity along \(D_{ij}\),
  \(d_{\mathrm{res}}\), and the no-Virasoro-cocycle boundary.
- `pytest -q compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  9 passed.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 261 passed.
- `git diff --check -- chapters/theory/bar_construction.tex
  compute/tests/test_collision_form_local_global_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 543: Degree-two conductor kernel as ordered \(r\)-matrix data

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, ordered
averaging items 78--80 and kernel items 222--224: remove informal
``information loss'' language unless the kernel is characterized,
identify \(\ker(\operatorname{av})\) in degree two as ordered
\(r\)-matrix data, and state exactly what is known in higher arity for
braid/associator data.

Repairs:

- `chapters/theory/universal_conductor_K_platonic.tex`: added
  `thm:uc-degree-two-rmatrix-kernel`.  In a finite window,
  \[
    \ker(K_{\cA,2}^{\mathrm{ch}})
    =
    \ker(\mathrm{Re}_2)
    =
    \operatorname{im}\!\left(\frac{1-s}{2}\right),
    \qquad s=(12).
  \]
- On arity-two residue-generated windows, the kernel is now identified
  with the completed span of the anti-invariant ordered
  \(r\)-matrix components
  \[
    r_{\cA,\alpha}^{-}(z)
    =
    \frac12\bigl(r_{\cA,\alpha}(z)
      -s\cdot r_{\cA,\alpha}(z)\bigr).
  \]
  The symmetric shadow keeps only \(\mathrm{Re}_2(r_{\cA,\alpha})\).
- For \(n\ge3\), the theorem identifies the kernel components
  \(\beta^-=(1-\mathrm{Re}_n)\beta\) of ordered braid,
  KZ-associator, Yangian, or surface-braid coefficients.  These
  components generate the whole kernel only under the explicit
  finite-window generation hypothesis; without it, no exhaustion claim
  is made.
- `compute/tests/test_ordered_symmetric_conductor_scope.py`: added a
  guard for the theorem label, the \(\operatorname{im}((1-s)/2)\)
  formula, the anti-invariant \(r\)-matrix component, and the
  higher-arity non-overclaim generation clause.
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass
  543 under the ordered-to-symmetric/conductor-kernel row.

Verification:

- `python3 -m py_compile
  compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- Token scan over `thm:uc-degree-two-rmatrix-kernel` confirmed the
  theorem label, `\ClaimStatusProvedHere`,
  \(\operatorname{im}((1-s)/2)\), \(r_{\cA,\alpha}^{-}(z)\),
  \(\beta^-=(1-\mathrm{Re}_n)\beta\), and the higher-arity
  generation caveat.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  9 passed.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 260 passed.
- `git diff --check -- chapters/theory/universal_conductor_K_platonic.tex
  compute/tests/test_ordered_symmetric_conductor_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 542: Finite-window \(R\)-twisted descent theorem

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, ordered
averaging items 69--76: prove continuity of Reynolds/coinvariant
descent, define \(R\)-twisted coinvariants explicitly, prove
preservation of the bar differential and convolution bracket, and
state exactly when averaging is a dg Lie morphism rather than a linear
projection.

Repairs:

- `chapters/theory/universal_conductor_K_platonic.tex`: strengthened
  the conductor hypothesis package \(\mathbf H_{\mathrm{uc}}\) by
  adding the missing shuffle-compatible coefficient multiplication
  \[
    \mu_{m,n}\colon
    \operatorname{Ind}_{\Sigma_m\times\Sigma_n}^{\Sigma_{m+n}}
    (R_m\otimes R_n)\to R_{m+n}.
  \]
  This is the datum needed for a tensor-product \(R\)-twisted bracket
  to land in the chosen arity-\((m+n)\) symmetric target.
- Added `thm:uc-r-twisted-dg-lie-descent`.  In a finite window it
  defines
  \[
    B^{\Sigma,R}_{X,n}(\cA;\mathcal W)
    =
    \varprojlim_N
    \bigl(R_n\otimes_{\mathbb Q[\Sigma_n]} C_n/F^NC_n\bigr),
  \]
  proves that the bar differential descends exactly under
  \(R\)-twisted equivariance, proves that the convolution bracket
  descends after the coefficient multiplication maps are supplied, and
  records that without these hypotheses the formula is only a linear
  shadow projection.
- The theorem also isolates the untwisted Reynolds criterion:
  the Reynolds representative is a dg Lie morphism precisely when the
  Reynolds kernel is closed under the relevant ordered brackets.
- Updated the proof of `thm:uc-universal-conductor` to cite the new
  finite-window theorem before invoking the older \(R\)-descent
  corollaries.
- `compute/tests/test_ordered_symmetric_conductor_scope.py`: added a
  guard requiring the new theorem, the explicit coinvariant complex,
  differential descent, bracket descent, coefficient-multiplication
  caveat, Reynolds representative, and linear-shadow warning.
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass
  542 under the A8 ordered-to-symmetric/R-twisted descent item.

Verification:

- `python3 -m py_compile
  compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- Token scan over `thm:uc-r-twisted-dg-lie-descent` confirmed the
  theorem label, `\ClaimStatusProvedHere`, the explicit
  \(R_n\otimes_{\mathbb Q[\Sigma_n]}C_n/F^NC_n\) coinvariant
  complex, averaging/differential descent, convolution bracket, and
  linear-shadow warning.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  8 passed.
- `pytest -q compute/tests/test_ordered_symmetric_conductor_scope.py
  compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 259 passed.
- `git diff --check -- chapters/theory/universal_conductor_K_platonic.tex
  compute/tests/test_ordered_symmetric_conductor_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 541: Empty-boundary FM obstruction vanishing

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, log-FM
items 164--165: state the exact relation to ordinary FM when
\(D=\emptyset\), and prove that log-FM reduces to ordinary FM in that
case.  Pass 539 made the global log-FM package an obstruction-vanishing
problem; this pass proves the first positive base case of that
obstruction problem.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: added
  `thm:empty-boundary-logfm-obstructions-vanish`.  In the
  \(D=\emptyset\), fixed smooth-curve finite window with
  \(d_{\mathrm{sew}}=d_{\mathrm{pf}}=\hbar\Delta=0\), the global
  log-FM obstruction complex restricts to the ordinary
  Fulton--MacPherson tree-cooperad obstruction complex.
- Proved that the degree-zero generator
  \(\Delta_{\log}^{(0)}\) is the ordinary FM collision cocomposition
  \(\Delta_T^{\mathrm{FM}}\), hence extends to a strict dg cooperad
  map out of the Boardman--Vogt tree resolution.
- Concluded
  \[
    [\mathfrak o_q^{\log\mathrm{FM}}(\mathcal W_{\mathrm{sm}})]=0
    \qquad (q\ge1)
  \]
  and the decorated analogues vanish on ordinary collision
  \(\mathrm{Ch}_\infty\) operations.
- The theorem explicitly does not assert vanishing for stable-node,
  relative-boundary, Mok-crossing, planted-forest, or
  non-separating-handle windows; those remain the genuine relative
  log-FM obstruction problem.
- `compute/tests/test_harvest_type_signature_logfm_cluster.py`: added
  a regression guard for the positive smooth-core vanishing theorem and
  its non-overclaim boundary.
- `notes/external_review_harvest_matrix_20260617.md`: recorded Pass
  541 as a proved smooth-core upgrade under the log-FM block.

Verification:

- `python3 -m py_compile
  compute/tests/test_harvest_type_signature_logfm_cluster.py
  compute/tests/test_external_review_harvest_completion_scope.py` passed.
- Token scan over `thm:empty-boundary-logfm-obstructions-vanish`
  confirmed the theorem label, `\ClaimStatusProvedHere`,
  \(D=\emptyset\), \(\mathcal W_{\mathrm{sm}}\), the truncation
  \(d_{\mathrm{sew}}=d_{\mathrm{pf}}=\hbar\Delta=0\), and the
  non-overclaim sentence.
- `pytest -q compute/tests/test_harvest_type_signature_logfm_cluster.py
  compute/tests/test_external_review_harvest_completion_scope.py`:
  8 passed.
- `pytest -q compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 255 passed.
- `git diff --check -- chapters/theory/higher_genus_modular_koszul.tex
  compute/tests/test_harvest_type_signature_logfm_cluster.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 540: External-input harvest completion status hardening

Audit anchor: all three external input files named in the chat, now
copied into the repository as
`materials/raw/2026-06-05-chiral1-research-paper-strengthening.pdf`,
`materials/raw/2026-06-17-chiral-bar-cobar-manuscript-review-and-improvement.pdf`,
and
`materials/raw/2026-06-17-expanded-expert-repair-specification-main36.md`
with hashes recorded in `references/source-provenance.md`.

Repairs:

- `notes/external_review_harvest_matrix_20260617.md`: removed the
  ambiguous `partial` and `ongoing` table statuses from the harvest
  control surface.  Rows now distinguish harvested corrections from
  residual source-level theorem/proof obligations; residual frontier
  work is not counted as an unharvested external-review correction.
- `compute/tests/test_external_review_harvest_completion_scope.py`:
  hardened the completion guard so a table status containing `open`,
  `audit`, `partial`, or `ongoing` fails the targeted harvest suite.
- The fatal-weakness block now points to the completed status gates
  and to Pass 539's log-FM obstruction complex as the truthful source
  target left after harvesting the review advice.

Verification:

- `python3 -m py_compile
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py` passed.
- Matrix status scan over table rows passed: no status cell contains
  `open`, `audit`, `partial`, or `ongoing`.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 7 passed.
- `pytest -q compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 254 passed.
- `git diff --check -- notes/external_review_harvest_matrix_20260617.md
  notes/audit_repairs_ledger_20260610.md
  compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py
  chapters/theory/higher_genus_modular_koszul.tex
  chapters/connections/concordance.tex` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 539: Log-FM global coherence obstruction complex

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, fatal
weakness 1 and block B: the log-FM cooperad is the hidden keystone, and
Mok's strata/degeneration formula do not by themselves supply global
Gysin residues, proper pushforwards, automorphism normalisations,
Boardman--Vogt coherences, or chiral-operation compatibility.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: added the
  finite-window global log-FM coherence obstruction complex
  \(\mathfrak E_{\log\mathrm{FM}}^\bullet(\mathcal W)\), built from
  the Hom complex
  \[
    \operatorname{Hom}\bigl(
      C_\bullet(W\mathsf{Gr}^{\mathrm{st}}_{\mathcal W}),
      \operatorname{CoEnd}(\cC^{\log\mathrm{FM},\mathcal W}_{\mathrm{mod}})
    \bigr).
  \]
- Identified the first obstruction classes:
  \(\mathfrak o_1\) is the chain-map defect of the generator formula,
  \(\mathfrak o_2\) is the codimension-two global
  target-identification defect left after local determinant signs
  cancel, and \(\mathfrak o_3\) is the Boardman--Vogt pentagon defect.
- Added `thm:logfm-obstruction-criterion`: in each finite window,
  the signed log-FM residue-pushforward package \((\mathrm{LF}1)--
  (\mathrm{LF}6)\) exists iff these obstruction classes and their
  decorated chiral-operation analogues vanish; the completed package
  then requires compatible choices in a strict Mittag--Leffler tower.
- Updated the log-FM modular convolution well-definedness criterion so
  the old conditional package is now equivalent, windowwise, to a
  named obstruction-vanishing problem.
- `compute/tests/test_harvest_type_signature_logfm_cluster.py`: added
  a guard for the obstruction complex, first obstruction meanings, and
  the LF1--LF6 equivalence.

Verification:

- `python3 -m py_compile compute/tests/test_harvest_type_signature_logfm_cluster.py`
  passed.
- `pytest -q compute/tests/test_harvest_type_signature_logfm_cluster.py`:
  3 passed.
- `pytest -q compute/tests/test_external_review_harvest_completion_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 7 passed.
- `git diff --check -- chapters/theory/higher_genus_modular_koszul.tex
  compute/tests/test_harvest_type_signature_logfm_cluster.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md
  chapters/connections/concordance.tex` passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 538: External-review final harvest guard and local \(d\log\) notation patch

Audit anchor: the local/global \(d\log\) correction in
`Chiral-Bar-Cobar Manuscript Review and Improvement.pdf` and
`expanded_expert_repair_specification_main36 (1).md` A4/B2: the
coordinate expression \(\dlog(z_i-z_j)\) is only an affine/formal
collision-screen representative of the logarithmic normal form, not a
global curve form.

Repairs:

- `appendices/notation_index.tex`: retuned the entry for \(\eta_{ij}\)
  from a bare FM propagator formula to the logarithmic normal form along
  \(D_{ij}\), represented by \(\dlog(z_i-z_j)\) only on affine/formal
  collision screens and replaced globally by coordinate-change,
  KZB, or prime-form data.
- `appendices/signs_and_shifts.tex`: added the local-normal-coordinate
  hypothesis to the residue-orientation lemma, so the displayed residue
  formula is explicitly a local representative calculation.
- `chapters/connections/arithmetic_shadows.tex`: removed a surviving
  literal \(d_{\mathrm{bar}}=\mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})\)
  summary and replaced it by the typed KZ--Arnold
  bar-superconnection plus Fulton--MacPherson boundary-residue
  realization.
- `chapters/connections/bv_brst.tex`: split the BV/bar comparison,
  ordered-bar differential, and KZ--Arnold connection into their typed
  roles; the connection contributes to the bar operator only after
  boundary-residue realization.
- `chapters/connections/feynman_connection.tex`: retyped the
  Heisenberg Feynman-rule realisation as the output of the
  KZ--Arnold bar-superconnection after Fulton--MacPherson
  boundary-residue realization.
- Removed the same retired formula from six additional live
  cross-reference surfaces:
  `chapters/theory/higher_genus_modular_koszul.tex`,
  `chapters/connections/genus1_seven_faces.tex`,
  `chapters/connections/feynman_diagrams.tex`,
  `chapters/connections/holographic_datum_master.tex`,
  `chapters/theory/algebraic_foundations.tex`, and
  `chapters/theory/higher_genus_foundations.tex`.
- `compute/tests/test_collision_form_local_global_scope.py`: extended
  the existing local/global guard to the notation and signs appendices.
- `compute/tests/test_external_review_harvest_completion_scope.py`:
  added a final external-review harvest guard checking that the matrix
  has no open/audit table rows and that live TeX surfaces avoid the
  exact retired slogans and symbolic drift patterns from the input
  reviews.

Verification:

- `python3 -m py_compile compute/tests/test_external_review_harvest_completion_scope.py compute/tests/test_collision_form_local_global_scope.py compute/tests/test_kz_arnold_superconnection_scope.py compute/tests/test_arnold_borcherds_nilpotence_scope.py`
  passed.
- `pytest -q compute/tests/test_collision_form_local_global_scope.py compute/tests/test_kz_arnold_superconnection_scope.py compute/tests/test_arnold_borcherds_nilpotence_scope.py compute/tests/test_external_review_harvest_completion_scope.py compute/tests/test_heisenberg_curved_dual_scope.py compute/tests/test_theorem_h_hochschild_polynomial.py compute/tests/test_theorem_h_engine_status_scope.py`:
  251 passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 537: Heisenberg curved-dual manuscript propagation

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
object-firewall warning and `expanded_expert_repair_specification_main36
(1).md` A3/A6: keep the Koszul dual object, scalar shadow, and
level-flipped Heisenberg algebra distinct; replace Arnold-alone
nilpotence rhetoric by the operator-valued Borcherds/OPE coefficient
identity together with Arnold form cancellation.

Repairs:

- Propagated the Heisenberg convention through live manuscript and
  standalone surfaces: for \(k\neq0\),
  \[
    \cH_k^!\simeq
    (\mathrm{Sym}^{\mathrm{ch}}(V^*[1]),m_0=-k\omega),
  \]
  the curved second-kind branch.  The uncurved
  \(\mathrm{Sym}^{\mathrm{ch}}(V^*)\) is now only an associated-graded
  or \(k=0\) shadow on the repaired surfaces.
- Removed object-level identifications \(\cH_k^!=\cH_{-k}\) from the
  Hochschild and holographic lanes.  The level-flipped algebra is now
  described as scalar-shadow/open-colour comparison data with the same
  scalar \(\kappa=-k\), not as the Koszul-dual object.
- Repaired Heisenberg nilpotence summaries in
  `chapters/frame/heisenberg_frame.tex`: \(d^2=0\) is attributed to
  the central Borcherds coefficient identity plus Arnold logarithmic
  form cancellation, not to Arnold alone.
- Extended `compute/tests/test_heisenberg_curved_dual_scope.py` with a
  live manuscript scan over `chapters/`, `appendices/`, and
  `standalone/` for the exact drift phrases.

Verification:

- `python3 -m py_compile compute/tests/test_heisenberg_curved_dual_scope.py`
  passed.
- `pytest -q compute/tests/test_heisenberg_curved_dual_scope.py`:
  9 passed.
- Focused locator over live manuscript roots for the exact high-risk
  phrases (`H_k^! = Sym`, `\cH_k^!=\cH_{-k}`, `Arnold alone`,
  `Koszul self-identification`) returned clean, except for the intended
  forbidden literal inside the regression test before the locator was
  narrowed to manuscript roots.
- `git diff --check` over the repaired file set passed.
- No full LaTeX build or metadata regeneration was run in this pass.

## 2026-06-18 -- Pass 536: Theorem H KDH obstruction equivalence surfaced

Audit anchor: `chiral1 Research Paper Strengthening.pdf`, Theorem-H
items 338--339 and 384: define
\(\mathrm{KD}_{\mathrm H}^{\bullet}(\cA)\), prove that Theorem~H
high-degree concentration is equivalent to acyclicity of the
positive-depth obstruction package, and identify
\(\ChirHoch^n(\cA)\) with \(H^n(\mathrm{KD}_{\mathrm H}^{\bullet}(\cA))\)
for \(n\ge4\).  Target false pattern: Theorem~H presented as a formal
bar--cobar consequence or as a bare amplitude statement without the
obstruction complex that measures the missing positive-depth
collision data.

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: the live theorem
  lane already contained the definitional package
  `def:theorem-h-collision-depth-package` and the conditional
  proposition `prop:theorem-h-kdh-criterion`.  This pass integrates
  that criterion into the main polynomial-growth clause of Theorem~H:
  the concentration statement now explicitly says that, under
  Proposition~\ref{prop:theorem-h-kdh-criterion}, the terminal
  positive-depth obstruction package
  \[
    \mathfrak{o}^{\ge3}_{\mathrm H,\infty}(\cA)
    =
    \mathfrak{o}_{\mathrm H}^{3}(\cA)
    \oplus
    \bigoplus_{n\ge4}
      H^n(\mathrm{KD}_{\mathrm H}^{\bullet}(\cA))
  \]
  vanishes.
- The proof of the growth clause now cites
  `prop:theorem-h-kdh-criterion` and records the exact long-sequence
  content: the degree-three obstruction is the cokernel of
  \(\partial_{\mathrm H}^{3}\colon H^2(Q_{\mathrm H})\to
  H^3(\mathrm{KD}_{\mathrm H}^{\bullet})\), while for every \(n\ge4\)
  one has
  \[
    \ChirHoch^n(\cA)\cong
    H^n(\mathrm{KD}_{\mathrm H}^{\bullet}(\cA)).
  \]
- `compute/tests/test_theorem_h_hochschild_polynomial.py`: strengthened
  the KDH guard so it checks the definition of the positive-depth
  complex, the quotient \(Q_{\mathrm H}\), the boundary map, the
  terminal obstruction package, the proposition's high-degree
  equivalence, and the main Theorem~H growth clause's citation of the
  KDH criterion.

Verification:

- `python3 -m py_compile compute/tests/test_theorem_h_hochschild_polynomial.py`:
  clean.
- `pytest -q compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_h_engine_status_scope.py`: 231 passed.
- Fixed-string scans confirm that
  `prop:theorem-h-kdh-criterion`,
  \(\mathfrak{o}^{\ge3}_{\mathrm H,\infty}\), and
  \(H^n(\mathrm{KD}_{\mathrm H}^{\bullet}(\cA))\) occur both in the
  theorem surface and in the guard.
- `git diff --check -- chapters/theory/chiral_hochschild_koszul.tex
  compute/tests/test_theorem_h_hochschild_polynomial.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-18 -- Pass 535: Cross-volume Heisenberg dual object firewall

Audit anchor: the external-review object-firewall warning applied
globally to the Heisenberg row.  Pass 534 repaired the local
bosonisation sentence; this pass propagates the same mathematics
through live Vol~I/II/III compute and test surfaces.  Target false
patterns: payloads or prose saying \(H_k^!=\mathrm{Sym}^{\mathrm{ch}}(V^*)\)
as an uncurved object, identifying \(H_k^!\) with \(H_{-k}\), or using
the rank-one Heisenberg as an object-level Koszul self-dual example.

Repairs:

- Vol~I compute/test surfaces now label the Heisenberg companion as the
  curved second-kind `Sym^ch(V*[1])` branch with scalar
  \(\kappa(H_k^!)=-k\).  This includes the cross-algebra registry,
  invariant-machine payloads, genus-two/three complementarity engines,
  Theorem-twisted-holography diagnostics, GLZ/quadratic-dual prose,
  kappa-stratification tests, and the archived verified-formula label.
  Legitimate non-Heisenberg uses of uncurved `Sym^ch(V*)`, such as the
  fermion dual, remain untouched.
- Vol~II holographic, bulk-boundary, modular-obstruction, YM synthesis,
  and deep bridge payloads now distinguish the curved chiral dual from
  the \(H_{-k}\) open-colour / scalar-shadow row.
- Vol~III CY and holography surfaces now replace object-level
  \(H_1^!=H_1\) or \(H_1^!=H_{-1}\) language by the curved dual branch.
  The \(Y^+\) / omega-background fixed-parameter statements are retained
  only as parameter-level self-duality; they no longer imply
  Heisenberg object-level Koszul self-duality.  The
  `c3_koszul_data` self-duality flag is corrected to `False`, and the
  hyperkahler conductor example now uses \(K_{H_1}=0\), not \(2\).
- `compute/tests/test_heisenberg_curved_dual_cross_volume_scope.py`
  adds a cross-volume guard over the repaired live surfaces.  It
  forbids the old uncurved-object and \(H_{\pm k}\)-identification
  strings, requires the curved branch wording, and checks the corrected
  Vol~III `is_self_dual=False`, \(\kappa_{H_1^!}=-1\), and
  \(K_{H_1}=0\) surfaces when the sibling repositories are present.

Verification:

- `python3 -m py_compile` on the touched Vol~I/II/III Python files:
  clean.
- Vol~I targeted tests:
  `pytest -q compute/tests/test_heisenberg_curved_dual_cross_volume_scope.py
  compute/tests/test_heisenberg_curved_dual_scope.py
  compute/tests/test_invariant_machine.py`: 116 passed.
- Vol~II targeted tests:
  `pytest -q compute/tests/test_bulk_boundary_duality_engine.py
  compute/tests/test_holographic_ht_engine.py`: 139 passed.
- Vol~III targeted tests:
  `pytest -q compute/tests/test_e1_koszul_three_families.py
  compute/tests/test_drinfeld_center_heisenberg_bulk.py
  compute/tests/test_string_field_theory_e1_cy3.py
  compute/tests/test_e3_koszul_heisenberg.py
  compute/tests/test_e2_bar.py`: 354 passed.
- Vol~III hyperkahler changed methods:
  `pytest -q compute/tests/test_hyperkahler_anchored_fixed_point.py::TestZFunctorialityKoszulReflectionsIV::test_Z_functoriality_at_canonical_chiral_algebras
  compute/tests/test_hyperkahler_anchored_fixed_point.py::TestSupertraceTrinityCentreCollapseIV::test_supertrace_equals_kappa_conductor_at_canonical_examples`:
  2 passed.
- Broad scans across live Vol~I/II/III compute and test surfaces find
  no residual Heisenberg-specific `H_k^! = Sym^ch(V*)`,
  `H_1^! = Sym^ch(V*)`, `H_k^! = H_{-k}`, or `H_1^! = H_1` surfaces
  outside regression-test forbidden literals and explicit
  associated-graded/uncurved-shadow warnings.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 534: Bosonization remark keeps Heisenberg curved dual

Audit anchor: external-review Heisenberg/Koszul-dual warning that
\(\mathfrak H_k^!\) at \(k\neq0\) must be the curved second-kind
branch, not the uncurved commutative \(\mathrm{Sym}^{\mathrm{ch}}(V^*)\)
with product-type centre. Target false pattern: a local bosonization
comparison still saying the Heisenberg algebra has uncurved
\(\mathrm{Sym}^{\mathrm{ch}}(V^*)\) as its Koszul dual.

Repairs:

- `chapters/theory/chiral_hochschild_koszul.tex`: in the
  boson--fermion correspondence remark, replaced the stale sentence
  \(\mathcal H_\kappa^!\simeq\mathrm{Sym}^{ch}(V^*)\) by the typed
  statement: for \(\kappa\neq0\), the dual is the curved second-kind
  \(\mathrm{Sym}^{\mathrm{ch}}(V^*[1])\) branch with
  \(m_0=-\kappa\omega\); the uncurved symmetric algebra is only the
  \(k=0\) or associated-graded shadow. The reason bosonization is not
  Koszul duality is still the generator-count mismatch: the
  Heisenberg dual branch has one generator, while the fermion has two.
- `compute/tests/test_heisenberg_curved_dual_scope.py`: extended the
  existing curved-dual guard to cover the bosonization comparison and
  forbid the old uncurved-dual sentence.

Verification:

- `pytest -q compute/tests/test_heisenberg_curved_dual_scope.py`:
  7 passed.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 533: Chiral Hochschild indexing guard harvested

Audit anchor: raw Theorem-H repair item for
`koszul_pair_structure.tex`, where the normalized Hochschild cochain
complex had previously been susceptible to an off-by-one convention:
degree \(0\) must be \(M\), \(\delta_0\) must be the chiral adjoint
map whose image gives inner derivations, and the geometric
Fulton--MacPherson model must use \(n\) normalized inputs plus two
extra marked points, hence \(\overline C_{n+2}(X)\).

Repairs:

- The live TeX already carried the corrected convention:
  `thm:chiral-hochschild-complex` displays
  \(0\to M\to \operatorname{Hom}_{\mathcal D_X}(\overline{\mathcal A},M)\),
  writes \((\delta_0m)(a)\) as the left-right chiral adjoint action,
  indexes \((\delta_n f)(a_1,\ldots,a_{n+1})\) with
  \(\sum_{i=1}^n(-1)^i\), and states
  \(H^1=\mathrm{Der}/\mathrm{Inn}\) with inner derivations coming from
  \(\delta_0(M)\).
- The live `thm:geometric-chiral-hochschild` already uses
  \(\overline C_{n+2}(X)\), explains that the two extra marked points
  are output/evaluation points, and says the comparison computes
  \(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\), not \(\cA^!\).
- `compute/tests/test_koszul_pair_hochschild_indexing_scope.py` now
  guards those repaired surfaces and excludes the old
  \(\overline C_{n+1}\), zero-input-as-\(\overline{\mathcal A}\), and
  \(a_0,\ldots,a_{n+1}\) differential conventions inside the affected
  theorem blocks.

Verification:

- `pytest -q compute/tests/test_koszul_pair_hochschild_indexing_scope.py`:
  2 passed.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 532: Theorem-H compute proof-language scoped

Audit anchor: external-review Theorem-H finding that the compute layer
and tests still presented finite lookup tables and witness triples as
mathematical verification of the full Hochschild concentration theorem.
Target false pattern: hard-coded or finite-window rows saying they
``verify'' Theorem~H, or that the W/Virasoro polynomial-ring lane is
``refuted by Theorem~H'' without carrying the \(H_H\) package and the
missing residue-twisted acyclicity/completion gates.

Repairs:

- `compute/lib/theorem_h_hochschild_polynomial.py`: retitled the
  module as a conditional Theorem-H status table. The public
  `verify_theorem_h*` names are retained for API compatibility, but the
  docstrings now say they are internal \(H_H\)-row consistency checks,
  not chain-level proofs of Theorem~H. The W-algebra polynomial-ring
  model is described as a different Gelfand--Fuchs lane outside the
  \(H_H\) table, not as something proved false by an unconditional
  Theorem~H proof.
- `compute/lib/chiral_hochschild_engine.py`: changed the engine header
  and W-algebra compatibility surface to conditional \(H_H\)-table
  language. The engine records Betti vectors and OPE normalization
  metadata; it is explicitly not a chain model for the full derived
  centre.
- `compute/tests/test_theorem_h_hochschild_polynomial.py`: rewrote the
  header and W/Virasoro/W_N test docstrings so the tests check finite
  \(H_H\)-table consistency and do not assert generic-family proof,
  generic W_N Koszulness, or unconditional amplitude.
- `compute/tests/test_theorem_H_hochschild_koszul.py`: downgraded the
  old "independent verification" prose to finite \(H_H\) witness checks
  and engine sanity anchors. The file now states that these triples do
  not prove the chiral bar comparison, residue-twisted
  Orlik--Solomon/Koszul-complex input, or collision-depth support
  degeneration.
- `compute/tests/test_theorem_h_engine_status_scope.py`: added guards
  excluding the repaired overclaim phrases across both Theorem-H compute
  engines and both test modules, and requiring the finite-table /
  \(H_H\)-conditional replacement language.

Verification:

- `python3 -m py_compile compute/lib/theorem_h_hochschild_polynomial.py
  compute/lib/chiral_hochschild_engine.py
  compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_H_hochschild_koszul.py`: clean.
- `pytest -q compute/tests/test_theorem_h_engine_status_scope.py
  compute/tests/test_theorem_h_hochschild_polynomial.py
  compute/tests/test_theorem_H_hochschild_koszul.py`: 232 passed.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 531: W-orbit compute evidence scoped

Audit anchor: red-team finding for `thm:w-algebra-koszul-main` and
the live compute surface around `conj:w-orbit-duality`. Target false
pattern: compute headers saying they verify the W-orbit conjecture, the
BP seed described as proved, and a principal \(W_N\) central-charge
implementation whose code omitted the \((k+N-1)^2\) factor even though
the local docstring and TeX formula contained it.

Repairs:

- `compute/lib/w_orbit_duality.py`: rewrote the module header as finite
  evidence and consistency checks. It now says explicitly that the
  module does not prove `conj:w-orbit-duality`, identifies
  `thm:w-algebra-koszul-main` as conditional principal characteristic
  transport, and identifies `conj:bp-duality` as a conjecture with
  conductor evidence only.
- The same module now fixes `wn_central_charge(n,k)` to implement
  \(c(W_N,k)=(N-1)-N(N^2-1)(k+N-1)^2/(k+N)\), restoring the
  Virasoro/\(W_3\) specializations and the Freudenthal--de~Vries
  complementarity constants \(K_2=26\), \(K_3=100\), \(K_4=246\),
  \(K_5=488\).
- The same module now describes `WOrbitDualityVerification` and
  `verify_orbit_duality_type_a` as finite check/evidence packets rather
  than full conjecture verification.
- `compute/tests/test_w_orbit_duality.py`: rewrote the test header to
  finite-evidence language, removed "Full type-A verification" and
  "Verified complementarity table" wording, and replaced the stale
  `prop:bp-duality` proved reference with `conj:bp-duality` evidence
  language.
- `compute/tests/test_w_orbit_duality_scope.py`: added guards tying the
  compute wording to the TeX theorem surface: principal W transport is
  conditional, non-principal W-orbit duality is conjectural, and the
  compute layer is evidence only.

Verification:

- `pytest -q compute/tests/test_w_orbit_duality_scope.py
  compute/tests/test_w_orbit_duality.py`: 138 passed.
- `git diff --check -- compute/lib/w_orbit_duality.py
  compute/tests/test_w_orbit_duality.py
  compute/tests/test_w_orbit_duality_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 530: Editorial status-census remarks scoped

Audit anchor: red-team findings for
`rem:conjecture-attack-strategies` and
`rem:constitution-status-updates`. Target false pattern: a census
remark with no explicit status tag being treated as a proved theorem
surface because it cites conjectural packets.

Repairs:

- `chapters/connections/editorial_constitution.tex`: retitled
  `rem:conjecture-attack-strategies` with
  `\ClaimStatusConditional` and added an opening firewall. The remark
  is now explicitly a status census and search-strategy surface: it
  records proved subloci, finite computational evidence, and live
  conjectures, but promotes none of the listed conjectures to theorems.
- The same file now retitles `rem:constitution-status-updates` with
  `\ClaimStatusConditional` and says it is a conditional
  status-census surface, not a new proof of any referenced conjectural
  or conditional input.
- The MC3 folding reference in `rem:constitution-status-updates` now
  cites `Remark~\ref{rem:mc3-type-b-folding}`, not a proposition, and
  scopes the folding route to prefundamental Clebsch--Gordan closure
  for types \(B_n\) and \(C_n\), not the completed/coderived DK package.
- `compute/tests/test_editorial_constitution_status_census_scope.py`:
  added guards for both census remarks and the ledger/matrix record.

Verification:

- `pytest -q compute/tests/test_editorial_constitution_status_census_scope.py
  compute/tests/test_editorial_constitution_mc5_scope.py
  compute/tests/test_feynman_disk_local_scope.py
  compute/tests/test_mc5_disk_local.py`: 21 passed.
- `git diff --check -- chapters/connections/editorial_constitution.tex
  compute/tests/test_editorial_constitution_status_census_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 529: Disk-local ternary comparison scoped

Audit anchor: red-team findings for
`prop:compactified-ternary-two-channel` and the external-review
Kontsevich/FM gate. Target false pattern: a proved logarithmic
\(\bP^1\) residue lemma presented as if it verified the conjectural
disk-local perturbative/FM comparison.

Repairs:

- `chapters/connections/feynman_diagrams.tex`: retitled
  `prop:compactified-ternary-two-channel` as a two-channel reduction
  for a compactified logarithmic ternary packet. The proposition remains
  `\ClaimStatusProvedHere`, but only for the pure logarithmic
  \(\bP^1\) residue argument after two logarithmic forms have already
  been constructed with matching boundary-channel and orientation
  conventions.
- The proposition now explicitly says it does not construct the
  perturbative ternary form, does not compare it with the bar form, and
  does not prove
  Conjecture~\ref{conj:v1-disk-local-perturbative-fm}.
- The adjacent application remark now applies the proposition only
  conditionally, after the compactified perturbative and bar logarithmic
  forms have been constructed with the stated pole and orientation
  conventions; it reduces three residue equalities to two but does not
  supply the compactification/Stokes upgrade.
- `chapters/connections/editorial_constitution.tex`: the MC5 route
  summary and H7 gap now describe
  Proposition~\ref{prop:compactified-ternary-two-channel} as a
  logarithmic residue reduction, not as a proof of the disk-local
  perturbative/FM comparison.
- `compute/lib/mc5_disk_local.py` and
  `compute/tests/test_mc5_disk_local.py`: their headers now record
  finite symbolic C2/C3 evidence for selected families, not verification
  of the conjecture.
- `compute/tests/test_feynman_disk_local_scope.py`: added guards for
  the proposition, application remark, editorial route, compute headers,
  and this ledger/matrix entry.

Verification:

- `pytest -q compute/tests/test_feynman_disk_local_scope.py
  compute/tests/test_mc5_disk_local.py`: 16 passed.
- `pytest -q compute/tests/test_editorial_constitution_mc5_scope.py
  compute/tests/test_feynman_disk_local_scope.py
  compute/tests/test_mc5_disk_local.py`: 18 passed.
- `git diff --check -- chapters/connections/feynman_diagrams.tex
  chapters/connections/editorial_constitution.tex
  compute/lib/mc5_disk_local.py compute/tests/test_mc5_disk_local.py
  compute/tests/test_feynman_disk_local_scope.py
  notes/audit_repairs_ledger_20260610.md
  notes/external_review_harvest_matrix_20260617.md`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 528: Standard-tower MC5 closure fenced as conditional packaging

Audit anchor: review theorem-status firewall and the red-team finding
that the standard-tower MC5 reduction/closure surface had depended on
the conjectural DK/KL package. Target false pattern: a conditional
corollary whose title and last line still read as if the MC5 packet
closed unconditionally.

Repairs:

- `chapters/connections/editorial_constitution.tex`: retitled
  `cor:standard-tower-mc5-closure` as "Conditional standard-tower MC5
  closure under DK/KL and BV/BRST packages."
- The corollary conclusion now says that, conditional on the four named
  packages, there is no further infinite-tower algebraic obstruction
  beyond the genuswise BV/BRST/bar comparison already imported in
  assumption~(iv).
- The statement explicitly says it is not an unconditional closure
  theorem: the hypotheses include
  Conjecture~\ref{conj:master-dk-kl}, the standard-tower reduction
  Conjecture~\ref{conj:standard-tower-mc5-reduction}, and the
  BV/BRST/bar comparison package.
- The proof now concludes only the conditional package statement,
  rather than saying "Hence the standard-tower MC5 packet closes."
- `compute/tests/test_editorial_constitution_mc5_scope.py`: added a
  guard requiring the closure corollary to remain conditional and the
  standard-tower reduction to remain conjectural.

Verification:

- `pytest -q compute/tests/test_editorial_constitution_mc5_scope.py`: 2
  passed.
- `pytest -q compute/tests/test_theorem_open_closed_rectification_engine.py`:
  54 passed.
- `git diff --check -- chapters/connections/editorial_constitution.tex
  compute/tests/test_editorial_constitution_mc5_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 527: \(c=13\) self-duality scoped to scalar and rational-shadow surfaces

Audit anchor: external review object firewall and Feigin--Frenkel /
Koszul-dual language discipline. Target false pattern: treating the
Virasoro scalar fixed point \(c=13=26-13\) as an automatic
vertex-algebra, ordered-bar-complex, or all-degree Drinfeld-double
self-equivalence.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: retitled
  `prop:c13-full-self-duality` as "Scalar and rational shadow fixed
  point at \(c=13\)" and added a type signature. The statement now
  names \(\iota_{\mathrm{Vir}}(c)=26-c\), rationality/compatibility of
  \(S_r(\operatorname{Vir}_c)\), and the checked residue-trace
  computation through \(r\leq7\).
- The proposition now has an explicit bar-complex firewall: the scalar
  equality \(13=26-13\) does not construct an isomorphism of ordered bar
  complexes, vertex algebras, or chiral Koszul dual objects. Such an
  identification requires a separate Virasoro Koszul-equivalence
  package.
- The Drinfeld-double scope remark and all-degree RTF conjecture now
  separate: proved rational-shadow fixed point, proved checked-range
  RTF vanishing, and conjectural all-degree RTF / Drinfeld-double
  self-duality.
- `rem:c13-holographic-significance` now says "unique scalar
  self-dual point" and "rational-shadow and checked trace
  self-duality"; it no longer says the boundary theory and its dual are
  identical or that RTF vanishes for all test functions.
- `chapters/connections/concordance.tex`: synchronized the \(c=13\)
  concordance paragraph and table to the same scalar/rational-shadow
  scope.
- `standalone/theorem_index.tex`: updated the stale theorem title
  string for `prop:c13-full-self-duality`.
- `compute/tests/test_theorem_shadow_depth_gkw_engine.py` and
  `compute/tests/test_theorem_arithmetic_rectification_engine.py`:
  updated stale docstrings that called the full tower self-dual.
- `compute/tests/test_c13_self_duality_scope.py`: added a guard for the
  manuscript theorem, holographic remark, Drinfeld-double scope remark,
  concordance, and theorem index.

Verification:

- `pytest -q compute/tests/test_c13_self_duality_scope.py
  compute/tests/test_conductor_cross_channel_scope.py
  compute/tests/test_shadow_channel_cross_channel_scope.py
  compute/tests/test_theorem_shadow_depth_gkw_engine.py::TestAdversarial::test_virasoro_c13_still_class_m
  compute/tests/test_theorem_arithmetic_rectification_engine.py::TestAnomalyCancellation::test_h04_c13_self_duality`:
  12 passed.
- Final combined targeted suite for Passes 525--527:
  `pytest -q compute/tests/test_shadow_channel_cross_channel_scope.py
  compute/tests/test_shadow_channel_decomposition.py
  compute/tests/test_genus2_multichannel.py
  compute/tests/test_koszulness_vii_multiweight.py
  compute/tests/test_scalar_full_coefficient_typing.py
  compute/tests/test_conductor_cross_channel_scope.py
  compute/tests/test_feigin_frenkel_reflection_scope.py
  compute/tests/test_c13_self_duality_scope.py
  compute/tests/test_theorem_shadow_depth_gkw_engine.py::TestAdversarial::test_virasoro_c13_still_class_m
  compute/tests/test_theorem_arithmetic_rectification_engine.py::TestAnomalyCancellation::test_h04_c13_self_duality`:
  311 passed.
- `git diff --check -- chapters/theory/higher_genus_modular_koszul.tex
  chapters/connections/concordance.tex
  compute/tests/test_c13_self_duality_scope.py
  compute/tests/test_theorem_shadow_depth_gkw_engine.py
  compute/tests/test_theorem_arithmetic_rectification_engine.py
  standalone/theorem_index.tex`: clean.

No full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 526: Scalar conductor no longer kills cross-channel terms

Audit anchor: expanded repair specification D3/D4 and the review
warning that conductor identities are lane-specific until a theorem
identifies them. Target false pattern: a theorem-facing conductor
paragraph saying the all-weight cross-channel correction is controlled
by \(\kappa+\kappa'\) and vanishes identically when the scalar
conductor is zero.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: changed the
  finite scalar tau theorem's multi-weight remainder from stale
  \(\Delta F_g^{\mathrm{cross}}\) notation to the chapter-standard
  \(\delta F_g^{\mathrm{cross}}\).
- `prop:koszul-conductor-wn` and the type-\(A\) DS tower remark now
  call \(k\mapsto-k-2h^\vee\) the critical-level reflection
  \(\iota_{\mathrm{crit}}\), with Feigin--Frenkel \(W\)-duality named
  only as the surrounding comparison lane, not as the bare level map.
- `prop:koszul-conductor-anomaly-vanishing`: replaced the false
  implication "scalar conductor zero implies
  \(\delta F_g^{\mathrm{cross}}=0\)" by the correct firewall:
  \(\kappa(\cA)+\kappa(\cA^!)\) is a scalar anomaly diagnostic for the
  diagonal complementarity lane.  Mixed stable-graph contributions must
  be computed or separately proved zero via single-channel structure,
  free-field/lattice factorisation, or \(H_{\mathrm{SCD}}\).
  The full coefficient is restated as
  \(F_g=F_g^{\mathrm{diag}}+\delta F_g^{\mathrm{cross}}\), with
  \(F_g^{\mathrm{diag}}=\kappa\lambda_g^{\mathrm{FP}}\), so the bare
  Faber--Pandharipande scalar formula is not used for the full
  coefficient.
- `compute/tests/test_conductor_cross_channel_scope.py`: added a
  focused guard for the \(\delta/\Delta\) notation, conductor
  scalar-scope language, and critical-level-reflection terminology in
  these windows.

Verification:

- `pytest -q compute/tests/test_conductor_cross_channel_scope.py
  compute/tests/test_shadow_channel_cross_channel_scope.py
  compute/tests/test_feigin_frenkel_reflection_scope.py`: 10 passed.
- `pytest -q compute/tests/test_scalar_full_coefficient_typing.py`: 3
  passed after the full coefficient was rewritten through
  \(F_g^{\mathrm{diag}}\).
- Fixed-string scans found no remaining
  `\Delta F_g^{\mathrm{cross}}`, no `controlled by
  $\kappa + \kappa'$`, and no `vanishes identically when` in the
  scanned theorem surfaces.
- `git diff --check -- chapters/theory/higher_genus_modular_koszul.tex
  compute/tests/test_conductor_cross_channel_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 525: Shadow-channel decoupling scoped to strict diagonal lane

Audit anchor: expanded repair specification D4 and the review warning
that the formal genus tower is
\[
F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}
+\delta F_g^{\mathrm{cross}}(\cA),
\]
with the first term only the scalar diagonal/uniform-weight projection.
Target false pattern: a shadow-channel theorem and compute oracle
treating abelian primary brackets as enough to split an arbitrary
multi-channel obstruction tower into independent one-channel factors.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: retitled
  `thm:shadow-channel-decomposition` as a strict shadow-channel
  decomposition theorem and added its type signature:
  Open quadrant, completed shadow/modular convolution presentation,
  Beilinson level~5, and hypothesis package \(H_{\mathrm{SCD}}\).
- The theorem now requires strict orthogonal idempotent channel
  splitting, vanishing mixed Gerstenhaber and transferred higher
  brackets, diagonal pairing/propagator, no mixed stable-graph weights,
  and strict Mittag--Leffler completion.  Outside that package the
  theorem explicitly states
  \[
  \Theta_\cA=\sum_i\kappa_i\Theta_{\eta_i}
  +\Theta_\cA^{\mathrm{mix}},
  \]
  with scalar trace \(\delta F_g^{\mathrm{cross}}(\cA)\).
- `cor:shadow-cauchy-schwarz` is now only a strict diagonal scalar
  diagnostic.  The equality condition is corrected: the upper bound is
  saturated iff at most one scalar channel trace is nonzero, while
  \(\rho=1/r\) occurs iff all channel traces are equal.  The corollary
  no longer claims to be the full genus-\(2\) complementarity formula
  when \(\delta F_2^{\mathrm{cross}}\) is present.
- Downstream multi-weight and \(\beta\gamma\) references no longer cite
  the old theorem as an arbitrary multi-channel decomposition source;
  they point to the scalar diagonal projection / cross-channel graph
  construction or to the relevant bootstrap rigidity surface.
- `compute/lib/shadow_channel_decomposition.py`: retyped the module as
  a strict diagonal diagnostic engine, added an explicit
  `strict_channel_decoupled` gate, and stopped treating abelian primary
  OPE vanishing as sufficient for channel independence.
- `compute/tests/test_shadow_channel_decomposition.py`: updated the
  behaviour checks so abelian multi-channel data is independent only
  when \(H_{\mathrm{SCD}}\) is supplied.
- `compute/tests/test_shadow_channel_cross_channel_scope.py`: added a
  focused guard blocking the retired unconditional tensor-product and
  abelian-implies-decoupled surfaces.

Verification:

- `pytest -q compute/tests/test_shadow_channel_cross_channel_scope.py
  compute/tests/test_shadow_channel_decomposition.py`: 40 passed.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 524: Determinant-line anomaly and conformal-block scope repaired

Audit anchor: expanded repair specification B4/B7 and the review's
Polyakov/Witten gate: determinant-line formulation, anomaly accounting,
and conformal blocks as actual comparison objects rather than hidden
consequences of formal OPE data. Target false pattern: a theorem
assigning \(c_1(L_\cA)=\kappa(\cA)\lambda\) and then calling the
induced determinant-line connection flat; adjacent prose saying the
formal-disk OPE determines conformal blocks on all Riemann surfaces.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: added a type
  signature to `thm:primitive-flat-descent`.
- `chapters/theory/higher_genus_modular_koszul.tex`: added a type
  signature to `thm:conformal-block-reconstruction`, and replaced the
  false flat-determinant-line sentence by Chern--Weil anomaly
  accounting:
  \[
  [F_{\nabla^{\det}_\cA}/(2\pi i)] = \kappa(\cA)\lambda.
  \]
  The determinant line is now an anomaly line connection; flatness is
  only projectivised or after cancelling the scalar Hodge curvature.
- The integrable affine conformal-block paragraph now requires the
  Tsuchiya--Ueno--Yamada/Hitchin comparison package: integrable
  weights, finite-rank conformal-block sheaf, projective KZ/Hitchin
  connection, and determinant-line anomaly matching.
- `thm:deformation-quantization-ope` now has a type signature and ends
  with the correct scope: formal-disk OPE data determines the bar-side
  perturbative log-FM genus expansion in the completed modular
  convolution algebra, not analytic conformal blocks on all Riemann
  surfaces without the separate comparison package.
- `compute/tests/test_determinant_anomaly_conformal_block_scope.py`:
  added a focused guard blocking the retired flat determinant-line and
  OPE-determines-all-conformal-blocks surfaces.

Verification:

- `pytest -q compute/tests/test_determinant_anomaly_conformal_block_scope.py
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: 4 passed.
- `git diff --check -- chapters/theory/higher_genus_modular_koszul.tex
  compute/tests/test_determinant_anomaly_conformal_block_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 523: Log-FM modular cluster type signatures harvested

Audit anchor: expanded repair specification A1/E and Strengthening PDF
line items 81--170 plus 901--1000. Target false pattern: central
conditional modular/log-FM theorems carrying status labels but not
stating the type signature and hypothesis package at the theorem
surface.

Repairs:

- `chapters/theory/higher_genus_modular_koszul.tex`: added explicit
  type signatures to the perturbative modular MC theorem, universal
  modular deformation functor, modular propagator theorem, log-FM
  modular cocomposition theorem, finite-rank spectral reduction
  theorem, and primitive-to-global reconstruction theorem.
- The log-FM modular cocomposition theorem now states the Open
  quadrant, logarithmic FM chain-coefficient/homotopy modular cooperad
  presentation, Beilinson levels \(2\) and \(5\), Mok geometry, local
  Gysin/sign/nested-cocomposition inputs, finite
  groupoid/Reynolds normalisation, and the global signed log-FM
  residue-pushforward package \((\mathrm{LF}1)--(\mathrm{LF}6)\).
- `compute/tests/test_harvest_type_signature_logfm_cluster.py`: added a
  focused guard requiring these theorem labels to carry nearby
  `Type signature:` and `hypothesis package:` text, and requiring the
  log-FM cocomposition theorem to name the global signed package.

Verification:

- `pytest -q compute/tests/test_harvest_type_signature_logfm_cluster.py`:
  2 passed.
- `git diff --check -- chapters/theory/higher_genus_modular_koszul.tex
  compute/tests/test_harvest_type_signature_logfm_cluster.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 522: Residual Feigin--Frenkel/Koszul-dual conflations removed

Audit anchor: expanded repair specification C3 and review
Feigin--Frenkel language item.  Target false pattern: copy-forward and
landscape surfaces still calling the level map
\(k\mapsto -k-2h^\vee\) the Feigin--Frenkel involution/Koszul duality
instead of the critical-level reflection, or treating
Feigin--Frenkel \(W\)-duality as the chiral Koszul dual object.

Repairs:

- `standalone/introduction_full_survey.tex`: changed the Kac--Moody
  table row from "Feigin--Frenkel = Koszul duality" to
  "critical-level reflection distinct from the chiral Koszul dual" and
  renamed the theorem/index language from Feigin--Frenkel involution to
  critical-level reflection.
- `chapters/examples/landscape_census.tex`: changed scalar conductor
  and affine-census passages from Feigin--Frenkel involution/Koszul
  dual wording to critical-level reflected companion level, explicitly
  saying it is not the chiral Koszul dual object.
- `chapters/theory/infinite_fingerprint_classification.tex`: changed
  the \(W\)-algebra coset slot and critical fixed-point proof so
  Feigin--Frenkel duality is a critical-level reflected comparison
  lane, not an identification with either \(W\)-algebra's chiral
  Koszul dual object.
- `compute/tests/test_feigin_frenkel_reflection_scope.py`: extended
  the terminology guard to these surfaces.
- `notes/external_review_harvest_matrix_20260617.md`: C3 now records
  this residual object-firewall harvest in addition to pass 498.

Verification:

- `pytest -q compute/tests/test_feigin_frenkel_reflection_scope.py`: 4
  passed.
- Fixed-string scans over the repaired surfaces found no remaining
  "Feigin--Frenkel = Koszul duality", no "Feigin--Frenkel Koszul dual
  sends", no "on the Koszul dual side this is Feigin--Frenkel
  duality", and no newly guarded Feigin--Frenkel-involution wording.
- `git diff --check` clean for the files touched in pass 522.

---

## 2026-06-17 -- Pass 521: Residual local/global \(d\log\) surfaces repaired

Audit anchor: expanded repair specification A4 and review local/global
\(d\log\) item.  Target false pattern: active theorem and standalone
surfaces still treating \(d\log(z_i-z_j)\) as a global form or global
integral kernel on \(\FM_n(X)\), \(\mathrm{Conf}_n(X)\), or
\(\mathbb P^1\), instead of as the affine/formal representative of a
logarithmic normal form along the collision diagonal.

Repairs:

- `chapters/theory/quantum_corrections.tex`: changed the genus-\(0\)
  quantum-correction surface so Arnold flatness uses logarithmic normal
  forms represented by \(d\log(z_i-z_j)\) only on affine/formal
  collision screens.
- `chapters/theory/cobar_construction.tex`: changed the
  categorical-logarithm paragraph so the integral kernel is the
  logarithmic normal form \(\eta_{ij}\), with \(d\log(z_i-z_j)\) only
  its affine/formal representative and projective/positive-genus
  replacement data named.
- `chapters/frame/guide_to_main_results.tex`,
  `chapters/frame/preface_section1_v2.tex`,
  `chapters/frame/preface_section1_draft.tex`,
  `standalone/survey_track_a_compressed.tex`,
  `standalone/survey_modular_koszul_duality.tex`, and
  `standalone/survey_modular_koszul_duality_v2.tex`: removed
  copy-forward global-kernel phrasing and replaced it with the local
  normal-form / affine-screen representative / projective-period
  replacement distinction.
- `compute/tests/test_collision_form_local_global_scope.py`: extended
  the local/global guard to these repaired surfaces.
- `notes/external_review_harvest_matrix_20260617.md`: A4 now records
  this residual local/global harvest in addition to pass 493.

Verification:

- `pytest -q compute/tests/test_collision_form_local_global_scope.py`: 2
  passed.
- Fixed-string scans over `chapters`, `standalone`, and `appendices`
  found no remaining retired phrases from this pass, including
  "The logarithmic form \(\eta_{ij}=d\log(z_i-z_j)\) is the integral
  kernel", "The categorical logarithm
  \(\eta_{ij}=d\log(z_i-z_j)\)", and the old
  "\(\eta_{12}=d\log(z_1-z_2)\) is globally defined on
  \(\mathbb P^1\)" sentence.
- `git diff --check` clean for the files touched in pass 521.

---

## 2026-06-17 -- Pass 520: KZ--Arnold equality residuals typed as superconnection realisations

Audit anchor: expanded repair specification A5 and review KZ identity
item.  Target false pattern: residual summaries using
\(d_{\mathrm{bar}}=\KZ^*(\nabla_{\mathrm{Arnold}})\) as a literal
global equality between a chain differential and a connection, instead
of the finite-window bar-superconnection statement followed by
Fulton--MacPherson boundary/residue realisation.

Repairs:

- `chapters/theory/e1_modular_koszul.tex`: changed the Climax-Theorem
  summary so it identifies the genus-\(0\) affine/tangent
  finite-window collision part of the bar differential with the
  residue realisation of the KZ--Arnold bar superconnection.
- `chapters/theory/theorem_B_scope_platonic.tex`: rewrote the
  monodromy-filtration proof.  It now uses the finite KZ-window
  superconnection for the residue component and separately names the
  \(\Gamma_n\)-equivariance of internal and logarithmic-form
  components.
- `chapters/theory/chiral_koszul_pairs.tex`: removed the displayed old
  shorthand \(\dbar=\KZ^*(\nabla_{\Arn})\) from the theorem-facing
  remark and replaced it by the finite-window superconnection plus
  FM-residue reading.
- `chapters/theory/mc5_class_m_chain_level_platonic.tex`: replaced
  "chiral bar differential with the pullback" by the collision-part /
  residue-realised superconnection wording.
- `compute/tests/test_kz_arnold_superconnection_scope.py`: extended
  the guard to these four surfaces.
- `notes/external_review_harvest_matrix_20260617.md`: A5 now records
  the residual KZ equality harvest in addition to pass 492.

Verification:

- `pytest -q compute/tests/test_kz_arnold_superconnection_scope.py`: 2
  passed.
- Fixed-string scans over active theorem surfaces found no remaining
  `d_{\mathrm{bar}} = \mathrm{KZ}^{*}(\nabla_{\mathrm{Arnold}})`, no
  remaining displayed `\dbar = \KZ^*(\nabla_{\Arn})`, no remaining
  "bar differential as \(\mathrm{KZ}^*(\nabla^{\mathrm{Arnold}})\)",
  and no remaining "KZ-window chiral bar differential with the
  pullback" phrase.
- `git diff --check` clean for the files touched in pass 520.

---

## 2026-06-17 -- Pass 519: Borcherds coefficient wording on nilpotence surfaces

Audit anchor: expanded repair specification A6 and review nilpotence
item.  Target false pattern: residual shorthand
``Borcherds/Jacobi'' on bar-square surfaces, which can be read as
ordinary Jacobi replacing the Borcherds OPE coefficient identity.

Repairs:

- `appendices/arnold_relations.tex`: changed the affine bar-square
  proof, corollary, and triple-residue theorem from
  ``Borcherds/Jacobi'' wording to the sharper Borcherds coefficient
  identity.  The theorem statement still records that this reduces to
  Jacobi only in the purely Lie bracket screen.
- `chapters/theory/configuration_spaces.tex`: changed the configuration
  summary and scalar/operator distinction to require the Borcherds
  coefficient identity on OPE coefficients, not a Jacobi shorthand.
- `compute/tests/test_arnold_borcherds_nilpotence_scope.py`: updated
  the nilpotence guard to require the sharper wording and to reject
  ``Borcherds/Jacobi'' on the active nilpotence surfaces.
- `notes/external_review_harvest_matrix_20260617.md`: A6 now records
  the residual wording harvest in addition to pass 494.

Verification:

- `pytest -q compute/tests/test_arnold_borcherds_nilpotence_scope.py`: 3
  passed.
- Fixed-string scan over `appendices/arnold_relations.tex` and
  `chapters/theory/configuration_spaces.tex` found no remaining
  `Borcherds/Jacobi`.
- `git diff --check` clean for the files touched in pass 519.

---

## 2026-06-17 -- Pass 518: Yetter--Drinfeld Brown seed corrected

Audit anchor: Strengthening PDF arithmetic items 895--897
\textup{(}define the Yetter--Drinfeld/Schauenburg bracket, compute
\(\delta^{(n)}\) for claimed \(n\), and do not mix the arithmetic
bracket with the chiral bar differential without a comparison
map\textup{)}, together with the associator target-cocycle items
778--780.  Target false pattern: stale or shifted Brown--Padovan seeds
on the active \(\delta^{(n)}\) and \(\phi^{(n)}\) arithmetic target
surfaces.

Repairs:

- `chapters/connections/arithmetic_shadows.tex`: corrected the
  high-weight Yetter--Drinfeld Schauenburg theorem
  `thm:YD-delta-13-16` and its proof from the false seed
  \((d_3,d_4,d_5)=(1,1,1)\) to the Brown--Padovan seed
  \((d_3,d_4,d_5)=(1,1,2)\).  The displayed values
  \((d_{13},d_{14},d_{15},d_{16})=(16,21,28,37)\) and the products
  \(C_{n-1}d_n\) were already the values forced by the corrected
  recurrence.
- `chapters/frame/preface.tex`: corrected the
  \(\phi^{(n)}\)-target summary from the shifted seed
  \((d_1,d_2,d_3)=(1,0,1)\) to the unshifted Brown seed
  \((d_0,d_1,d_2)=(1,0,1)\), matching the compute modules and the
  arithmetic chapter.
- `compute/tests/test_yetter_drinfeld_brown_seed_scope.py`: regression
  guard added to recompute \(d_{13},\ldots,d_{16}\), the Catalan
  products, and the \(\lfloor n/2\rfloor+1\) weights; it also blocks
  the stale \((1,1,1)\) seed and the shifted preface seed.
- `notes/external_review_harvest_matrix_20260617.md`: arithmetic block
  L now records the Yetter--Drinfeld/Schauenburg seed repair.

Verification:

- `pytest -q compute/tests/test_yetter_drinfeld_brown_seed_scope.py`: 4
  passed.
- Fixed-string scans over active manuscript surfaces found no remaining
  stale high-weight seed `$(d_3, d_4, d_5) = (1, 1, 1)$` and no
  remaining shifted preface seed `$(d_1,d_2,d_3)=(1,0,1)$`.
- `git diff --check` clean for the files touched in pass 518.

---

## 2026-06-17 -- Pass 517: EK quantization signature firewall

Audit anchor: expanded repair specification B1 and Strengthening PDF
Hall/Yangian/EK items.  Target false pattern: invoking
Etingof--Kazhdan quantization as a bare theorem name without the
source Lie bialgebra, completion topology, associator, and
QUE/quasi-Hopf target.

Repairs:

- `chapters/examples/deformation_quantization.tex`: the data firewall
  now says EK quantization requires a source Lie bialgebra
  \((\mathfrak g,\delta)\), completed/pro-nilpotent topology,
  Drinfeld associator, and target QUE/quasi-Hopf category; the
  Lusztig-specialisation remark likewise keeps the formal
  \(\hbar\)-adic theorem separate from the root-of-unity point.
- `chapters/theory/ordered_associative_chiral_kd.tex`,
  `chapters/theory/e1_modular_koszul.tex`,
  `chapters/theory/derived_langlands.tex`,
  `chapters/theory/bar_construction.tex`,
  `chapters/theory/virasoro_motivic_purity_all_r_platonic.tex`,
  `chapters/theory/motivic_shadow_full_class_m_platonic.tex`, and
  `chapters/connections/master_concordance.tex`: EK invocations now
  carry the source/topology/associator/target signature instead of
  functioning as untyped shorthand.
- `standalone/e1_primacy_ordered_bar.tex` and
  `standalone/N3_e1_primacy.tex`: standalone copy-forward surfaces
  now carry the same EK signature.
- `compute/tests/test_ek_quantization_signature_scope.py`: regression
  guard added for the EK signature discipline.
- `notes/external_review_harvest_matrix_20260617.md`: B1 row now
  records this harvested EK-signature correction.

Verification:

- `pytest -q compute/tests/test_ek_quantization_signature_scope.py`: 4
  passed.
- Fixed-string scans over `chapters`, `standalone`, `appendices`,
  `notes`, and `metadata` found no remaining
  `gives the same torsor for quantisation choices of a fixed Lie
  bialgebra`, no remaining bare
  `Etingof--Kazhdan quantization datum has been supplied.  The
  pentagon`, and no remaining
  `Etingof--Kazhdan quantisation theorem~\cite{EK96}.`.
- `git diff --check` clean for the files touched in pass 517.

---

## 2026-06-17 -- Pass 516: Siegel--Borcherds target-cocycle scope

Audit anchor: Strengthening PDF items 778--780 and 886--899, plus the
existing `sieg_borcherds_associator_scope` engine guard.  Target false
pattern: treating scalar Siegel/Borcherds target data or an
order-\(\hbar^3\) pentagon calculation as an all-order compact Hall
associator.

Repairs:

- `chapters/theory/hochschild_cohomology.tex`: rewrote the
  \( \widetilde\Phi^{\mathrm{Sieg\text{-}Bor}}_\hbar \) lane as a
  supplied first-order Siegel--Borcherds target cocycle classified by
  \([\chi_3]\).  The theorem, proof, six-path remark, corollary, and
  seven-path comparison now explicitly say that no all-order Hall
  associator is constructed without non-scalar Hall source data and an
  all-order pentagon proof.
- `chapters/theory/nilpotent_completion.tex`,
  `chapters/theory/theorem_B_scope_platonic.tex`,
  `chapters/connections/bv_brst.tex`,
  `chapters/theory/e1_modular_koszul.tex`,
  `chapters/examples/yangians_drinfeld_kohno.tex`,
  `chapters/theory/infinite_fingerprint_classification.tex`, and
  `chapters/theory/motivic_shadow_tower.tex`: replaced residual old
  carrier language by target-cocycle language with the
  order-\(\hbar^3\) / all-order-Hall-associator split.
- `compute/tests/test_sieg_borcherds_target_cocycle_scope.py`:
  regression guard added for the target-cocycle wording and retired
  associator phrases.
- `notes/external_review_harvest_matrix_20260617.md`: block J now
  records this harvested associator-scope correction.

Verification:

- `pytest -q compute/tests/test_sieg_borcherds_target_cocycle_scope.py
  compute/tests/test_hdelta5_hall_bkm_recognition_gates.py
  compute/tests/test_cy_bkm_algebra_engine.py -k 'sieg_borcherds_associator
  or hdelta5 or target_cocycle_scope or hall_bkm_recognition'`: 20
  passed, 147 deselected.
- Fixed-string scans over `chapters`, `standalone`, `appendices`,
  `notes`, and `metadata` found no remaining retired all-order
  Hall-associator phrases or the old D1--D5 promotion phrase.
- `git diff --check` clean for the files touched in pass 516.

---

## 2026-06-17 -- Pass 515: GRT/associator scope firewall harvested

Audit anchor: external review warning on K3/BKM/Hall/GRT claims and
Strengthening PDF items on formality torsors, associator dependence,
and scalar target data.  Target false pattern: upgrading the standard
Drinfeld associator torsor, or a finite scalar shadow, into
GRT-triviality of categorical modular data.

Repairs:

- `chapters/theory/ordered_associative_chiral_kd.tex`: narrowed
  `rem:chiral-qg-grt1-torsor` to the verified
  \(\mathfrak{sl}_2\)/affine bar-side \(H^0\) shadow.  General
  simple-\(\mathfrak g\) associator-independence is now a comparison
  hypothesis, and the remark explicitly excludes categorical modular
  data, Drinfeld centres, line categories, and root-of-unity BKM
  \(S\)-matrices.
- `chapters/connections/arithmetic_shadows.tex`: sharpened
  `thm:grt-1-S-matrix-trivial` so the finite \(130\times130\)
  scalar \(S\)-matrix invariance is conditional on its displayed
  factorisation and factorwise-invariance package, with no
  categorical modular-data consequence.
- `standalone/e1_primacy_ordered_bar.tex`,
  `standalone/en_chiral_operadic_circle.tex`,
  `standalone/ordered_chiral_homology.tex`, and
  `standalone/seven_faces.tex`: removed copy-forward overclaims that
  made associator-independence automatic for all simple types or
  declared unconditional \(H^0\) GRT-rigidity.
- `notes/antipatterns_catalogue.md`: synced the chiral-QG summary to
  the actual conditional theorem status and the narrowed
  associator-torsor scope.
- `compute/tests/test_grt_associator_scope.py`: regression guard added
  for the GRT/associator firewall.
- `notes/external_review_harvest_matrix_20260617.md`: B2 and L rows now
  record the harvested GRT-scope correction.

Verification:

- `pytest -q compute/tests/test_grt_associator_scope.py`: 5 passed.
- Fixed-string scans over `chapters`, `standalone`, `notes`,
  `appendices`, and `metadata` found no remaining
  `extended structurally to all simple`, no remaining
  `the $\GRT_1$ action on the $\Pthree$ bracket is trivial for simple`,
  no remaining `the GRT$_1$ action on modular data is trivial.`, and no
  remaining unconditional `$H^0$: any two associators` GRT-rigidity
  phrase.
- `git diff --check` clean for the files touched in pass 515.

---

## 2026-06-17 -- Pass 514: Saito--Kurokawa packet separated from \(\Delta_5\)

Audit anchor: Strengthening PDF block L / arithmetic and modular
forms.  Target false pattern: using a fictitious
Saito--Kurokawa lift of \(\Delta_5\) to evaluate a central
\(L\)-value, instead of separating the Borcherds--Gritsenko
denominator \(\Delta_5\) from the Saito--Kurokawa square
\(\Delta_{10}=\Delta_5^2\).

Repairs:

- `chapters/theory/hochschild_cohomology.tex`: rewrote Path~(SE-C) so
  \(\Delta_5\) is the Borcherds--Gritsenko denominator with character,
  not a standard Saito--Kurokawa lift.  The Saito--Kurokawa packet is
  now explicitly \(\Delta_{10}=\Delta_5^2=\mathrm{SK}(f_{18})\) with
  \(f_{18}=E_6\Delta\).  The old central-\(L\)-value period evaluation
  through \(\mathrm{SK}(\Delta_5)\) is removed and replaced by a
  conditional square-root/character compatibility check.
- `compute/tests/test_saito_kurokawa_delta5_scope.py`: regression guard
  added for the \(\Delta_5\) versus \(\Delta_{10}\) distinction.
- `notes/external_review_harvest_matrix_20260617.md`: arithmetic block
  L now records this local harvested correction while preserving the
  remaining arithmetic programme as source-level frontier work.

Verification:

- `pytest -q compute/tests/test_saito_kurokawa_delta5_scope.py
  compute/tests/test_genus2_bocherer_deep_engine.py
  compute/tests/test_sk_surface_polarization.py`: 205 passed.
- Fixed-string scans over `chapters`, `standalone`, `appendices`,
  `notes`, and `metadata` found no remaining
  `SK(\Delta_5)`, no remaining
  `L(1/2,\mathrm{SK}(\Delta_5))`, and no remaining
  `Saito--Kurokawa lift~$\mathrm{SK}(\Delta_5)$`.

---

## 2026-06-17 -- Pass 513: Theorem A/B master rows synced to ambient-qualified bar--cobar

Audit anchor: external-review A2 and Strengthening PDF block D.  Target
false pattern: compact theorem rows presenting Theorem~A as an
ambient-free \(K^2\simeq\mathrm{id}\) assertion and Theorem~B as a
bare Koszul-locus counit, suppressing the weak adjunction,
Verdier--Ran intertwining, class-\(\mathsf M\) raw failure, and
completed/coderived Positselski replacement.

Repairs:

- `CLAUDE.md`: Theorem~A now separates weak bar--cobar adjunction in
  the weight-completed/pro-conilpotent Francis--Gaitsgory ambient,
  Verdier--Ran intertwining, and \(K^2\simeq\mathrm{id}\) only on
  \(\mathrm{Kosz}(X)\), with the corresponding augmentation,
  completion, finite-bar-piece, holonomic Ran, and PBW/Koszul
  acyclicity inputs.
- `CLAUDE.md`: Theorem~B now separates strict counit inversion on the
  Koszul locus from the class-\(\mathsf M\) raw direct-sum failure and
  the weight-completed coderived Positselski theorem, including
  diagonal Ext, completed/pro/\(J\)-adic, strict ML, and Milnor inputs.
- `compute/tests/test_theorem_ab_spine_ambient_scope.py`: regression
  guard added for the A/B master rows.
- `notes/external_review_harvest_matrix_20260617.md`: A2, D2, and
  Strengthening block D now record the theorem-spine propagation, and
  the residual-work section no longer lists compact A/B/C/D/H theorem
  spine consolidation as outstanding.

Verification:

- `pytest -q compute/tests/test_theorem_ab_spine_ambient_scope.py
  compute/tests/test_theorem_A_bar_cobar_isomorphism.py
  compute/tests/test_theorem_thm_a_bl_rectification_engine.py
  compute/tests/test_bar_cobar_bottleneck_iv.py`: 103 passed.
- `pytest -q compute/tests/test_theorem_concordance_rectification_engine.py
  -k 'fg_ambient_package or completed_chiral_positselski or
  positselski or ambient_split or ambient_sensitive'`: 2 passed, 167
  deselected.
- `pytest -q compute/tests/test_theorem_ab_spine_ambient_scope.py
  compute/tests/test_theorem_c_three_tier_scope.py
  compute/tests/test_theorem_d_spine_scope.py
  compute/tests/test_theorem_h_spine_package_scope.py`: 17 passed.
- Fixed-string scans found no remaining old compact Theorem~A or
  Theorem~B rows in `CLAUDE.md`, and no stale theorem-spine residual
  wording in the harvest matrix.

---

## 2026-06-17 -- Pass 512: Theorem C master row synced to C0/C1/C2

Audit anchor: Strengthening PDF block F and theorem-spine
consolidation after Pass 507.  Target false pattern: the master
five-theorem row presenting Theorem~C only as the scalar Verdier sum
\(K^\kappa=\kappa+\kappa^!\), thereby hiding the C0/C1/C2 separation
and letting the scalar ceiling masquerade as the shifted-symplectic C2
upgrade.

Repairs:

- `CLAUDE.md`: Theorem~C in the five-theorem table now states C0 flat
  fibre-centre comparison, C1 Verdier eigenspace / perfect-pairing
  complementarity, and the scalar ceiling as the trace shadow rather
  than C2.  The hypothesis package names C0, C1, and C2 separately and
  keeps the algebra-level Verdier sum distinct from
  \(\mathcal N(A_b)\).
- `compute/tests/test_theorem_c_three_tier_scope.py`: extended the
  existing Theorem~C guard to include the CLAUDE.md master row and to
  reject the retired scalar-only row.
- `notes/external_review_harvest_matrix_20260617.md`: block F now
  records the theorem-spine synchronization.

Verification:

- `pytest -q compute/tests/test_theorem_c_three_tier_scope.py
  compute/tests/test_scalar_full_coefficient_typing.py
  compute/tests/test_master_bourbaki_scope.py`: 12 passed.
- Fixed-string scan found no remaining scalar-only Theorem~C row
  `**C** | $K^\kappa(A_b) = \kappa(A_b) +
  \kappa^!_{\mathrm{alg}}(A_b)$ in family-stratum ceiling` in
  `CLAUDE.md`.

---

## 2026-06-17 -- Pass 511: Theorem H theorem-spine \(H_H\) package synced

Audit anchor: external-review D5 / strengthening block E.  Target false
pattern: Hochschild amplitude as an unconditional theorem, or as a
bare \(H_3\)-wall statement, rather than the full \(H_H\)-conditional
derived-centre claim.

Repairs:

- `CLAUDE.md`: the KSDual architecture sentence and five-theorem spine
  row for Theorem~H now state the
  \(\mathrm{ChirHoch}^\bullet \subset \{0,1,2\}\) result only under
  \(H_H\). The row lists the PBW, finite-type/perfect, genericity,
  \(E_\infty\)-completion, strict Mittag--Leffler, localized
  residue-twisted bar concentration, and completed/pro/\(J\)-adic
  Class~M hypotheses, and excludes critical/admissible/logarithmic
  off-loci unless their own spectral sequence and completion packages
  are supplied.
- `standalone/five_theorems_modular_koszul.tex`: the abstract and both
  KSDual synthesis paragraphs now use \(H_H\), not a bare \(H_3\)
  package; the deformation-theoretic paragraph now says
  \(\ChirHoch^3=0\) only on the full \(H_H\) surface.
- `notes/external_review_harvest_matrix_20260617.md`: D5 / block E now
  records the theorem-spine synchronization.
- `compute/tests/test_theorem_h_spine_package_scope.py`: regression
  guard added against the retired unconditional / \(H_3\)-only wording.

Verification:

- `pytest -q compute/tests/test_theorem_h_spine_package_scope.py
  compute/tests/test_theorem_h_engine_status_scope.py`: 9 passed.
- `pytest -q compute/tests/test_chirhoch_dimension_engine.py
  compute/tests/test_theorem_H_hochschild_koszul.py
  compute/tests/test_chiral_hochschild_engine.py`: 225 passed.
- Fixed-string scans found no remaining active
  `only under its $H_3$ package`, no remaining active
  `Theorem H remains conditional on its $H_3$ package`, and no
  remaining active unconditional
  `Theorem~H proves $\ChirHoch^3 = 0$: the deformation theory is
  unobstructed` on the repaired theorem-spine surfaces.

No full LaTeX build or metadata regeneration was run in this pass.

---

## 2026-06-17 -- Pass 510: Theorem D theorem-spine table, part map, and concordance synced

Audit anchor: theorem-spine consolidation after the local Theorem~D
repair. Target false pattern: compact core maps still presenting
Theorem~D as the bare formula
\(\mathrm{obs}_g=\kappa\lambda_g\), and a concordance paragraph calling
the \(\hat A\)-genus expression the first Chern class of a bundle.

Repairs:

- `CLAUDE.md`: changed the five-theorem table row for Theorem~D so it
  states the three-surface split: \(\mathrm{obs}_1=\kappa\lambda_1\)
  universally, \(\mathrm{obs}_g=\kappa\lambda_g\) on the
  scalar-diagonal uniform-weight lane, and all-weight free energy with
  \(\delta F_g^{\mathrm{cross}}\). The hypothesis package now names
  the curved chain equation \(m_1^2=[m_0,-]\), period-corrected
  \(D_g^2=0\), scalar trace, and uniform/multi-weight graph package.
- `chapters/theory/introduction.tex`: changed the Part~V map row from
  bare Theorem~D formula to genus-one universal, scalar-diagonal
  uniform-weight all-genera, and cross-channel off-lane wording.
- `chapters/connections/concordance.tex`: changed the Theorem~D
  integrability paragraph so the pure tautological class is explicitly
  for uniform-weight scalar-diagonal algebras, and so the
  \(\hat A\)-genus expression is the scalar characteristic-class trace
  of the period-corrected family, not a first Chern class and not the
  bundle itself.
- `compute/tests/test_theorem_d_spine_scope.py`: added guards for the
  spine table, part map, and concordance paragraph.
- `notes/external_review_harvest_matrix_20260617.md`: updated the
  Theorem~D row to include this theorem-spine pass.

Verification:

- `pytest -q compute/tests/test_theorem_d_spine_scope.py`: 4 passed.
- `pytest -q compute/tests/test_theorem_d_curved_scalar_scope.py
  compute/tests/test_scalar_full_coefficient_typing.py
  compute/tests/test_modular_bar.py
  compute/tests/test_curved_ainfty_bar_complex.py
  compute/tests/test_bottleneck_bar_cobar_curved.py
  compute/tests/test_master_bourbaki_scope.py`: 183 passed.
- Fixed-string scans found no remaining active
  `The $\hat{A}$-genus is the \emph{first Chern class}` in the
  concordance paragraph and no remaining bare Part~V
  `Theorem D $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$` row in the
  introduction map.

No full LaTeX build or metadata regeneration was run in this pass.

---

## 2026-06-17 -- Pass 509: algebraic modular QME shell separated from all-loop physical QME

Audit anchor: Strengthening PDF block K and the review's Costello gate:
CME/PVA, all-loop QME, boundary VOA, and \(E_3\)-lift are distinct
statements. Target false pattern: a compact BV theorem saying "the QME
is the Maurer--Cartan equation in the modular convolution algebra"
without naming that statement as the algebraic modular QME shell rather
than a physical all-loop analytic QME.

Repairs:

- `chapters/theory/koszul_pair_structure.tex`: changed the theorem
  item from "quantum master equation" to "algebraic modular QME shell"
  and stated that it is a finite-window identity in the completed
  modular convolution algebra, not an all-loop analytic QME for a
  physical factorization algebra.
- `chapters/theory/koszul_pair_structure.tex`: changed the proof so
  the Maurer--Cartan equation is explicitly the algebraic modular QME
  shell. A physical all-loop QME now requires local observables,
  propagator, renormalization scale, counterterms, analytic SDR, and
  anomaly-cancellation data.
- `compute/tests/test_physics_qme_cme_scope.py`: added guards for the
  new QME wording and for the existing BV/BRST finite-type PVA gate
  separating the classical PVA/CME theorem from all-loop QME.
- `notes/external_review_harvest_matrix_20260617.md`: marked the
  physics/open-closed row as applied for local physics-surface harvest,
  while preserving full QME and CS/WZW physical constructions as
  source-level frontier work.

Verification:

- `pytest -q compute/tests/test_physics_qme_cme_scope.py`: 4 passed.
- `pytest -q compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_physics_horizon.py`: 197 passed.
- Fixed-string scan found no remaining active
  `The QME is the Maurer--Cartan equation in the modular convolution
  algebra` phrase in `chapters/theory/koszul_pair_structure.tex`.

No full LaTeX build or metadata regeneration was run in this pass.

---

## 2026-06-17 -- Pass 508: Theorem D summary surfaces scoped to curved chain, scalar shadow, and total differential

Audit anchor: review block on positive-genus curvature and Strengthening
PDF block G, "Theorem D / modular tower". Target false pattern: compact
Theorem~D surfaces still advertising global single-number genus
universality, instead of separating the raw curved chain equation
\(m_1^2=[m_0,-]\), the scalar diagonal shadow
\([m_0]\mapsto\kappa(\cA)\lambda_g\), the period-corrected total
square-zero differential \(D_g\), and the multi-weight
\(\delta F_g^{\mathrm{cross}}\) correction.

Repairs:

- `standalone/five_theorems_modular_koszul.tex`: retitled the Theorem~D
  statement as scalar modular characteristic plus cross-channel
  correction. The type surface now states that the positive-genus
  fibrewise operator is curved, \(m_1^2=[m_0,-]\); only its scalar
  diagonal shadow gives \(\kappa(\cA)\lambda_g\); and only the
  period-corrected total modular differential \(D_g\) is square-zero.
- `standalone/five_theorems_modular_koszul.tex`: changed the genus-1
  clause so \(d_{\mathrm{fib}}^2=\kappa\omega_1\) is explicitly the
  scalar diagonal projection of the curved fibre equation, and changed
  front summary language from global genus universality to the
  uniform-weight scalar lane plus \(\delta F_g^{\mathrm{cross}}\) off
  that lane.
- `standalone/programme_summary.tex` and
  `standalone/programme_summary_sections2_4.tex`: replaced the old
  "no matter how complicated the OPE structure, the genus tower is
  controlled by a single number" sentence by the scoped statement that
  the single-number control holds after scalar diagonal projection on
  the uniform-weight lane, while off that lane the full free energy
  includes \(\delta F_g^{\mathrm{cross}}\).
- `compute/tests/test_theorem_d_curved_scalar_scope.py`: added guards
  for the curved-chain/scalar-shadow/total-differential split and for
  the retired global single-number language.
- `notes/external_review_harvest_matrix_20260617.md`: marked the
  Theorem~D / modular-tower row as applied for local theorem-surface
  harvest, while recording that genus-two KZB and all multi-weight
  closed forms remain source-level frontier work.

Verification:

- `pytest -q compute/tests/test_theorem_d_curved_scalar_scope.py`: 4
  passed.
- `pytest -q compute/tests/test_scalar_full_coefficient_typing.py
  compute/tests/test_modular_bar.py
  compute/tests/test_curved_ainfty_bar_complex.py
  compute/tests/test_bottleneck_bar_cobar_curved.py`: 175 passed.
- Fixed-string scans found no remaining active instances of the retired
  Theorem~D global-universality title or the old "no matter how
  complicated the OPE structure" single-number sentence in the three
  repaired summary files.

No full LaTeX build or metadata regeneration was run in this pass.

---

## 2026-06-17 -- Pass 507: Theorem C summary surfaces synced to C0/C1/C2

Audit anchor: Strengthening PDF block H, "Theorem C, derived centre,
symplectic complementarity", especially items 553--600. Target false
pattern: compact theorem summaries still presenting Theorem~C as a
single unconditional Lagrangian statement, treating the scalar identity
as the C2 shifted-symplectic clause, or using a fixed
\((-1)\)-shifted pairing on \(\mathbf C_g\) instead of the
Verdier-pairing degree \(-(3g-3)\) with a separate C2
BV/shifted-symplectic package.

Repairs:

- `standalone/programme_summary.tex` and
  `standalone/programme_summary_sections2_4.tex`: rewrote the compact
  Theorem~C statement as a three-tier theorem. C0 is the strict flat
  fibre-centre comparison; C1 is the represented Verdier eigenspace
  decomposition with perfectness and nondegenerate anti-invariant
  pairing; C2 is the conditional shifted-symplectic/BV upgrade. The
  scalar identity \(F_g=\kappa\lambda_g^{\mathrm{FP}}\) is now the
  uniform-weight trace shadow of C1 together with Theorem~D, not C2.
- `standalone/five_theorems_modular_koszul.tex`: retitled the Theorem~C
  statement as three-tier complementarity, expanded the type signature
  to name C0/C1/C2 and their hypotheses, and changed the Lagrangian and
  shifted-symplectic clauses so the scalar conductor cannot substitute
  for the C2 package.
- `compute/tests/test_theorem_c_three_tier_scope.py`: added guards for
  the three summary surfaces, requiring the C0/C1/C2 split and blocking
  the retired "C1 unconditional", fixed \((-1)\)-shifted pairing, and
  "scalar identity is C2" language.
- `notes/external_review_harvest_matrix_20260617.md`: marked the
  Theorem~C / derived-centre row as applied for local theorem-surface
  harvest, while recording that explicit derived-centre computations
  and full BV/shifted-symplectic constructions remain source-level
  witness work.

Verification:

- `pytest -q compute/tests/test_theorem_c_three_tier_scope.py`: 4
  passed.
- `pytest -q compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_scalar_full_coefficient_typing.py
  compute/tests/test_master_bourbaki_scope.py`: 24 passed.
- Fixed-string scans found no remaining active instances of
  `The eigenspace decomposition (C1) is unconditional` or
  `are Lagrangian for the $(-1)$-shifted symplectic pairing` in the
  three repaired summary files.

No full LaTeX build or metadata regeneration was run in this pass.

---

## 2026-06-17 -- Pass 506: ordered chiral bar sign and completion surface closed

Audit anchor: Strengthening PDF block C, "Ordered chiral bar
construction". Target false pattern: a theorem-facing definition giving
the precise ordered bar differential later in the chapter while an
older schematic block still used free placeholder signs
\(\epsilon_i\) and \(\sigma_{ij}\), blurred full pairwise
Fulton--MacPherson faces with the consecutive-block \(\chirAss\)
quotient, and did not name the finite-output/product-completion gate at
the point where the differential was introduced.

Repairs:

- `chapters/theory/bar_construction.tex`: replaced the duplicate
  schematic three-component differential block by the desuspended
  ordered formulas for \(d_{\cA}\), \(d_{\mathrm{dR}}\), and
  \(d_{\mathrm{res}}\), with the exact adjacent residue sign
  \((-1)^{\sum_{q<i}(|a_q|-1)+|a_i|}\).
- `chapters/theory/bar_construction.tex`: added the full-FM
  non-adjacent face rule as conjugation by the order-preserving shuffle
  plus Fulton--MacPherson boundary-orientation parity, and explicitly
  separated it from the consecutive-block \(\chirAss\) quotient.
- `chapters/theory/bar_construction.tex`: tied the local identities to
  Proposition~\(\ref{prop:ordered-bar-local-differential-identities}\)
  and the finite-output/product-completion hypotheses to
  Theorem~\(\ref{thm:ordered-bar-complete-conilpotent-functor}\).
- `chapters/theory/bar_construction.tex`: sharpened the nilpotence
  remark so residue-residue cancellation requires Borcherds/OPE modes,
  Arnold logarithmic-form relations, and the signed residue-orientation
  package; pure mode Jacobi alone is not presented as sufficient.
- `chapters/theory/bar_construction.tex`: updated the
  Loday--Vallette/geometric sign translation table so it no longer
  points to the retired \(\epsilon_i\) placeholder.
- `compute/tests/test_ordered_bar_sign_completion_scope.py`: added
  regression guards for the precise desuspension signs, full-FM versus
  \(\chirAss\) scope, completion hypotheses, and retired placeholder
  sign phrases.
- `notes/external_review_harvest_matrix_20260617.md`: marked the
  ordered chiral bar construction row as applied for local harvest,
  while preserving the caveat that theorem-spine consolidation remains
  nonlocal work.

Verification:

- `pytest -q compute/tests/test_ordered_bar_sign_completion_scope.py`:
  5 passed.
- `pytest -q compute/tests/test_bar_cobar_chain_maps.py
  compute/tests/test_bar_complex_core.py
  compute/tests/test_ordered_symmetric_conductor_scope.py`: 468 passed.
- `pytest -q compute/tests/test_bar_graph_complex_bridge.py
  compute/tests/test_ordered_bar_descent_engine.py`: 160 passed.
- Fixed-string scans found no remaining active instances of the retired
  placeholder phrases
  `epsilon_i = \sum`, `sigma_{ij} is a sign determined by`, or
  `Sign: $(-1)^{\epsilon_i}$` in `chapters/theory/bar_construction.tex`.

No full LaTeX build or metadata regeneration was run in this pass.

---

## 2026-06-17 -- Pass 505: W/DS/AGT scope firewall and rectangular \(\mathfrak{sl}_4,(2,2)\) KRW correction

Audit anchor: external review W/DS/AGT corridor and the expanded repair
specification's warning that DS reduction is a filtered functor on
primitive triples, not equality of all structures. Target false
patterns: using AGT as a proof of Koszul duality; treating
non-principal DS reduction as automatically commuting with bar--cobar
or Verdier duality; stating Bershadsky--Polyakov same-family duality
without the subregular DS--bar transport package; and retaining the
stale \(\mathfrak{sl}_4,(2,2)\) rectangular conductor \(14/70\)
instead of the KRW scalar conductor \(110/550\).

Repairs:

- `chapters/examples/genus_expansions.tex`: replaced the unqualified
  "DS reduction preserves both the discriminant and \(\kappa\)" sentence
  by a principal-lane statement requiring DS--bar exchange and scalar
  normalization, with non-principal reductions routed through the
  subregular DS--bar transport package.
- `chapters/examples/w_algebras.tex`: rewrote the AGT conjecture,
  scope remark, theorem type signature, proof, and S-duality remark so
  AGT is external comparison evidence only. The theorem now explicitly
  requires \(H_{\mathrm{AGT-shadow}}\), MC5 sewing, principal DS--bar
  exchange, scalar normalization, and finite-window/completion data; it
  says AGT is not a proof of Koszul duality or DS--bar commutation.
- `standalone/survey_track_a_compressed.tex` and
  `standalone/koszulness_fourteen_characterizations.tex`: split
  Bershadsky--Polyakov proved strictness/OPE-bar witnesses from the
  conditional same-family companion and level-shifted duality, which now
  require subregular DS--bar transport and Verdier exchange.
- `chapters/connections/subregular_hook_frontier.tex`: corrected the
  rectangular \((2,2)\subset\mathfrak{sl}_4\) scalar lane to
  \(c(k)=15k/(k+4)-12k-8\),
  \(c(k)+c(k^\vee)=110\), and
  \(\kappa(k)+\kappa(k^\vee)=550\). The paragraph now distinguishes the
  proved KRW scalar complementarity from the still-conditional
  categorical DS--KD commutation.
- `compute/lib/hook_type_w_duality.py`,
  `compute/lib/theorem_transport_transpose_sl4_engine.py`, and the
  corresponding tests: synchronized the \((2,2)\) KRW formula and
  removed stale \(14/70\), \(7k-16\), and \(7-48/(k+4)\) branches.
- `compute/tests/test_nonprincipal_ds_agt_scope.py`: added regression
  guards for AGT-as-comparison, DS-as-filtered-functor, BP conditional
  same-family duality, and the \((2,2)\) \(110/550\) scalar lane.

Verification:

- `pytest -q compute/tests/test_nonprincipal_ds_agt_scope.py
  compute/tests/test_ds_kd_red_team.py`: 66 passed.
- `pytest -q compute/tests/test_theorem_transport_transpose_sl4_engine.py`:
  69 passed.
- `pytest -q compute/tests/test_theorem_ds_koszul_hook_engine.py
  compute/tests/test_ds_bar_commutation.py
  compute/tests/test_ds_kd_red_team.py
  compute/tests/test_agt_shadow_correspondence.py
  compute/tests/test_bershadsky_polyakov_bar.py
  compute/tests/test_nonprincipal_ds_agt_scope.py
  compute/tests/test_hook_type_w_duality.py
  compute/tests/test_non_principal_beyond_hook_engine.py
  compute/tests/test_theorem_creutzig_w_landscape_engine.py
  compute/tests/test_theorem_butson_inverse_reduction_engine.py
  compute/tests/test_theorem_transport_transpose_sl4_engine.py`:
  680 passed, 2 deselected.
- Fixed-string scans over `chapters`, `standalone`, `compute`, and
  `notes` found no remaining active \(c+c^\vee=14\),
  \(\kappa+\kappa^\vee=70\), \(7k-16\), or \(7-48/(k+4)\)
  rectangular \((2,2)\) claims outside forbidden-string guards.

No full LaTeX build or metadata regeneration was run in this pass.

---

## [theorem-H/H-1] fatal / false / conf=high

FALSE CLAIM AUDITED: Shelton--Yuzvinsky Koszulness was alleged to
contract the positive part of the Arnold algebra itself, and this
alleged contraction was then transported through \(\sigma\) to kill
all positive-degree Arnold classes on the \(E_1\)-page as the sole
mechanism of `thm:hochschild-concentration-E1`.

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:1457-1532 (lem:chiral-homotopy-transport), 1154-1219 (prop:fm-tower-collapse Step 3), 1663-1693 (proof of thm:hochschild-concentration-E1)

EVIDENCE: OS(A_{m-1}) = H^*(FM_m(C);R) is the cohomology ring of the configuration space: its natural differential is zero and its positive part is nonzero — the same proposition (line 1046-1049) quotes the Poincaré polynomial ∏_{j=1}^{m-1}(1+jt), which I reverified (m=2 gives 1+t, so OS^{≥1} ⊇ C·ω_12 ≠ 0). A homotopy with dh+hd = id−π_0 would force OS^{≥1} acyclic, i.e. H^{≥1}(FM_m(C)) = 0, contradicting the quoted polynomial. What Koszulness of an algebra R actually provides is a contracting homotopy of the Koszul complex R⊗(R^!)^∨, never of R itself; Shelton–Yuzvinsky 1997 proves OS algebras of supersolvable arrangements are Koszul algebras and contains no such homotopy. The transport computation (lines 1558-1570) requires d_bar = σ(d⊗id_{A^⊗m})σ^{-1}, a differential never touching the algebra factors — false for any bar differential, whose residue terms multiply algebra slots and change m. The 'tensor decomposition' B̄^ord(A)|_{FM_m} ≃ OS(A_{m-1})⊗A^{⊗m} with the differential acting on the OS factor alone is asserted ('represent σ by this chain isomorphism', line 1484), not proved, and σ from lem:chiral-quadratic-koszul is an operadic chain map of a different type (P^! → T^c(s^{-1}P̄)^∨), not a decomposition of the algebra-level bar complex. Remark rem:sigma-inverse-chain-level (1605-1632) concedes σ^{-1} may not exist and retreats to 'the weaker cohomology-level statement' that d_1 annihilates positive Arnold classes — but that weaker statement is exactly what the false homotopy was supposed to prove, so it is asserted, not established.

REPAIR: (1) Excise the false homotopy at all four sites: prop:fm-tower-collapse statement (iii) and proof Step 3 (lines 1052-1084, 1145-1219), lem:chiral-homotopy-transport (1457-1603), proof of thm:hochschild-concentration-E1 (1663-1693), and rem:fm-collapse-nontrivial (2028-2052). Replace 'SY furnishes a contracting homotopy of OS^{>=1}' with the true statement: SY furnishes Koszulness of OS(A_{m-1}), i.e. contractibility of the Koszul complex OS (x) OS^pd (Priddy), never of OS itself. (2) State the honest open lemma: at each collision stratum, the E_1-term is a residue-twisted tensor complex (OS(A_{m-1}) (x) coefficient system, d_1 = OPE-residue twist); positive-fibre-degree acyclicity must be proved from PBW-Koszulness of gr_F A coupled to OS-Koszulness via the twisting cochain — this is thm:bar-concentration localized at the stratum. (3) Rewrite Step 3 of prop:fm-tower-collapse to route through thm:bar-concentration (the file already proves PBW => associated graded = classical Koszul complex, acyclic in positive degrees); keep the proposition \ClaimStatusConditional but delete the 'without invoking bar concentration' claims and rewrite rem:pbw-parallel-consequences (the two collapses are not parallel; FM-tower collapse consumes bar concentration). (4) Downgrade thm:hochschild-concentration-E1 — whose entire content is the ordered E_1-page independence claim — to \ClaimStatusConjectured, naming the ordered twisted-tensor acyclicity lemma (ordered analogue of bar concentration over the pure-braid OS stratum) as the open obligation; cor:hochschild-averaging-symmetric inherits this conditionality, and downstream consumers (prop:chirhoch-sharp-hilbert, prop:smooth-formal-moduli-standard, lem:totalization-amplitude, the comparison at lines 2940-2948) are re-pointed at the bar-concentration route, under which the symmetric concentration ChirHoch^n = 0 for n not in {0,1,2} survives conditionally. (5) Replace the question-begging closing sentence of rem:sigma-inverse-chain-level (1624-1631) with the named obligation: d_1-annihilation of positive Arnold classes is equivalent to positive-fibre-degree acyclicity of the residue-twisted complex, which SY Koszulness of OS alone does not imply.

---

## 2026-06-17 -- Pass 499: \(\beta\gamma\) residue split into raw OPE, pole-valued \(r_{\mathrm{coll}}\), and contact transport

Audit anchor: external review item C2 and the second-pass
object-specific correction in `Chiral-Bar-Cobar Manuscript Review and
Improvement.pdf`. Target false pattern: saying "the \(\beta\gamma\)
binary collision residue is zero" without specifying that only the
pole-valued \(r_{\mathrm{coll}}\) vanishes after \(d\log\)-absorption,
while the raw OPE contraction and regular contact operator remain
nonzero.

Repairs:

- `chapters/connections/genus1_seven_faces.tex`: replaced the
  unqualified genus-one statement "the binary collision residue is
  zero" by the three-slot statement: the genus-zero and genus-one
  pole-valued collision \(r\)-matrices vanish, the raw ordered OPE
  contraction \(\beta(z)\gamma(w)\sim(z-w)^{-1}\) is nonzero, and
  \(\Theta_{\beta\gamma}^{\mathrm{ord}}
  =\beta\otimes\gamma-\gamma\otimes\beta\) remains the nonzero
  class-\(C\) contact datum.
- `chapters/examples/free_fields.tex`: added the raw OPE clause before
  the displayed \(r^{\mathrm{coll}}_{\beta\gamma}(z)=0\) statement and
  changed the free-field table row from bare \(r(z)=0\) to
  "pole-valued \(r_{\mathrm{coll}}=0\) after \(d\log\)-absorption;
  raw OPE contraction nonzero".
- `standalone/seven_faces.tex`: synchronized the seven-face summary:
  GZ26 Hamiltonians see zero pole-valued \(r_{\mathrm{coll}}\), not a
  zero raw \(\beta\gamma\) OPE; regular contact transport is the
  surviving ordered datum.
- `compute/tests/test_betagamma_residue_scope.py`: added a regression
  guard for the raw-OPE / pole-valued-\(r_{\mathrm{coll}}\) / regular
  contact distinction across the canonical beta-gamma chapter, the
  free-field summary, the genus-one seven-face surface, the ordered
  associative appendix, and the standalone seven-face summary.

Verification:

- `pytest -q compute/tests/test_betagamma_residue_scope.py`: 4 passed.
- `pytest -q compute/tests/test_betagamma_residue_scope.py compute/tests/test_bv_bar_class_c_engine.py`:
  111 passed.
- Fixed-string / scoped regex scans over `chapters`, `standalone`,
  `appendices`, and `compute/tests` found no remaining checked
  beta-gamma claim that says the raw OPE contraction vanishes or that
  the unqualified binary collision residue is zero. Remaining
  `r(z)=0` hits are free-fermion Gaussian data or explicitly
  pole-valued \(bc\) / \(r_{\mathrm{coll}}\) statements.
- `git diff --check --` on the touched files: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 500: DDYBE theorem/evidence firewall harvested from external review

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
item 12 and `expanded_expert_repair_specification_main36 (1).md`
C4. Target false pattern: the genus-\(2\) face-model DDYBE chapter
mixing an exact degeneration theorem with finite-window generic
\(\Omega\) numerical residuals, and retaining stale prose about
engine labels that now resolve in the main higher-genus chapter.

Repairs:

- `chapters/theory/genus_2_ddybe_platonic.tex`: split the former
  "Face-model DDYBE, scope-restricted" theorem into
  Theorem~\(\ref{thm:g2-face-model-bypass-scope-restricted}\), now
  only the exact diagonal/separating degeneration to the genus-\(1\)
  Felder DYBE and tagged `\ClaimStatusProvedHere`, and
  Proposition~\(\ref{prop:g2-generic-ddybe-finite-window-evidence}\),
  tagged `\ClaimStatusNumericalEvidence`, for the finite-window
  generic-\(\Omega\) residual checks at `relative < 1e-4`.
- Kept the full generic-\(\Omega\) system
  `eq:ddybe`--`eq:ddybe-coupling` on
  `conj:g2-ddybe` with `\ClaimStatusConjectured`, and kept the
  non-separating \(\Omega_{12}\) fixed-nonzero boundary as a frontier
  target in `rem:g2-nonseparating-untested`.
- Rewrote the engine-label remark: `prop:g2-nonsep-degen` and
  `prop:g2-sep-degen` are now declared in
  `higher_genus_modular_koszul.tex`; the local chapter records their
  exact local anchors instead of repeating the stale "not declared"
  warning.
- `compute/tests/test_genus_2_ddybe_platonic.py`: changed the
  independent-verification decorator for generic \(\Omega\) from the
  exact theorem label to
  `prop:g2-generic-ddybe-finite-window-evidence`, added guards that
  prevent generic numerical residuals from being reabsorbed into the
  exact theorem, and added a guard that the engine-label remark remains
  current.
- `standalone/theorem_index.tex`: synced the local DDYBE theorem title
  and inserted the new numerical-evidence proposition entry. Metadata
  was not globally regenerated.

Verification:

- `pytest -q compute/tests/test_genus_2_ddybe_platonic.py`: 11 passed.
- `pytest -q compute/tests/test_face_model_ddybe_engine.py
  compute/tests/test_genus2_ddybe_engine.py`: 47 passed.
- Fixed-string scans found no remaining local DDYBE instances of the
  old "Face-model DDYBE, scope-restricted" theorem title, no stale
  `not declared in` claim in the DDYBE chapter, and no generic-\(\Omega\)
  verification-table reference to theorem part (ii).
- `git diff --check -- chapters/theory/genus_2_ddybe_platonic.tex
  compute/tests/test_genus_2_ddybe_platonic.py
  standalone/theorem_index.tex`: clean.

No full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 503: Polyakov/BRST criticality gate harvested from external review

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
Polyakov/Witten gate and
`expanded_expert_repair_specification_main36 (1).md` B4/B7. Target
false pattern: treating the shadow obstruction tower, the
half-central-charge scalar, or the bar-cobar counit as a proof of
Polyakov's path integral or of string criticality without the
determinant line, ghost complex, BRST current, and anomaly-cancellation
equation.

Repairs:

- `chapters/frame/preface.tex`: rewrote the Polyakov correspondence as
  an anomaly-accounting dictionary.  The text now says that a
  string-critical claim requires a determinant line, the \(bc\)-ghost
  complex, a BRST current \(Q\), and \(Q^2=0\).  The critical dimension
  is now the BRST condition
  \(c_{\mathrm{matter}}+c_{\mathrm{ghost}}=0\), not the KSDual fixed
  point; the ghost system is an external BRST resolution, not
  \(\cA^!\) by the bar-cobar counit alone.
- `chapters/frame/preface_sections5_9_draft.tex`: synchronized the
  same correction in the draft preface fragment.
- `standalone/survey_modular_koszul_duality.tex` and
  `standalone/survey_modular_koszul_duality_v2.tex`: changed the
  Polyakov--bar-cobar dictionary from a claimed proof of the worldsheet
  functional integral to a comparison dictionary requiring
  determinant-line and BRST data.
- `standalone/introduction_full_survey.tex`: removed the claim that
  the bosonic critical dimension follows from scalar Koszul duality
  alone.  Scalar duality now gives the half-central-charge shadow;
  string criticality additionally requires the ghost sector and BRST
  nilpotence.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: extended
  the existing physics-surface guard to require the determinant-line /
  BRST / ghost-resolution language and forbid the retired
  path-integral and scalar-criticality phrases.

Verification:

- `pytest -q compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  17 passed.
- `pytest -q compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_q_hbar_convention_bridge_scope.py`: 20 passed.
- Fixed-string scans over `chapters/frame`, `standalone`,
  `chapters/connections`, `chapters/theory`, and `appendices` found no
  remaining targeted phrases claiming that the shadow tower "proves
  Polyakov", that criticality follows from scalar Koszul duality alone,
  or that the bar complex computes Polyakov's path integral.
- `git diff --check --` on all touched files in this pass: clean.

The CS/WZW side remains conditional where it appears: the KL/DK
Chern--Simons framing convention is guarded by pass 501, and
`chapters/connections/bv_brst.tex` states the WZW BRST/bar comparison
as genus-\(0\) conditional with the all-genera statement conjectural.

---

## 2026-06-17 -- Pass 504: residual Yangian additive-\(\hbar\) convention split from KL/DK exponent parameters

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
item 13 and `expanded_expert_repair_specification_main36 (1).md` B1.
Target false pattern: using bare \(\hbar\) simultaneously for the
additive Yangian parameter and for the exponent parameter entering
KL/DK \(q\)-conventions.

Repairs:

- `standalone/drinfeld_kohno_bridge.tex`: in the
  Yangian/quantum-loop comparison square, replaced bare
  \(q_Y=e^\hbar\), \(Y_\hbar\), and
  \(\hbar=\pi i/(k+h^\vee)\) overlap-zone statements by the explicit
  additive Yangian parameter \(\hbar_Y\).  The text now writes
  \(q_Y=\exp(\hbar_Y)\) and
  \(\hbar_Y:=\pi i/(k+h^\vee)\), keeping this parameter distinct from
  the KL/DK reference parameter \(\hbar_{\mathrm{ref}}\).
- `chapters/examples/yangians_drinfeld_kohno.tex`: synchronized the
  included Yangian/DK comparison square with
  \(Y_{\hbar_Y}\), \(Y_{-\hbar_Y}\), and
  \(q_Y=\exp(\hbar_Y)\), and added an explicit reference that
  \(\hbar_Y\) is the additive Yangian parameter, distinct from the
  KL/DK convention bridge.
- `compute/tests/test_q_hbar_convention_bridge_scope.py`: extended the
  q-convention regression guard to cover additive Yangian
  overlap zones in both the standalone and included Yangian/DK
  chapters.

Verification:

- `pytest -q compute/tests/test_q_hbar_convention_bridge_scope.py`: 4
  passed.
- Fixed-string scans over the theorem-facing q/Yangian overlap files
  found no remaining `q_DK = exp(pi i...)`, `q_Y=e^\hbar`, or bare
  `\hbar = \pi i/(k+h^\vee)` pattern.
- `git diff --check -- standalone/genus1_seven_faces.tex
  standalone/drinfeld_kohno_bridge.tex
  chapters/examples/yangians_drinfeld_kohno.tex
  compute/tests/test_q_hbar_convention_bridge_scope.py`: clean.

No full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 501: KL/DK \(q\)-parameter bridge repaired on theorem-facing standalone surfaces

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
item 13 and `expanded_expert_repair_specification_main36 (1).md`
B1. Target false pattern: calling the half-monodromy parameter
\(\exp(\pi i/(k+h^\vee))\) the Drinfeld--Kohno parameter, and using
bare \(\hbar\) in a way that hides the distinction between
\(q_{\mathrm{KL}}\) and \(q_{\mathrm{DK}}\).

Repairs:

- `standalone/genus1_seven_faces.tex`: changed the abstract,
  Verlinde proposition, and quantum-group remark so the half-braid
  parameter is
  \(q_{\mathrm{KL}}=\exp(\pi i/(k+h^\vee))\), while the full pure-braid
  Drinfeld--Kohno parameter is
  \(q_{\mathrm{DK}}=q_{\mathrm{KL}}^2
  =\exp(2\pi i/(k+h^\vee))\).  The old statement that
  \(q_{\mathrm{DK}}=\exp(\pi i/(k+h^\vee))\), with full-cycle factor
  \(q_{\mathrm{DK}}^2\), was removed.
- `standalone/drinfeld_kohno_bridge.tex`: replaced the local shorthand
  \(q_{\mathrm{KL}}=e^{\hbar}\), \(\hbar=\pi i/(k+h^\vee)\), by the
  canonical reference parameter
  \(q_{\mathrm{KL}}=\exp(\pi i\hbar_{\mathrm{ref}})\),
  \(\hbar_{\mathrm{ref}}=(k+h^\vee)^{-1}\), matching
  `appendices/q_convention_bridge_appendix.tex`.
- `compute/tests/test_q_hbar_convention_bridge_scope.py`: added
  regression guards for the appendix convention, the genus-one
  standalone half/full monodromy split, and the Drinfeld--Kohno
  standalone reference-\(\hbar\) wording.

Verification:

- `pytest -q compute/tests/test_q_hbar_convention_bridge_scope.py`: 3
  passed.
- Fixed-string scans over
  `standalone/genus1_seven_faces.tex`,
  `standalone/drinfeld_kohno_bridge.tex`,
  `chapters/connections/genus1_seven_faces.tex`, and
  `chapters/examples/yangians_drinfeld_kohno.tex` found no remaining
  `q_{\mathrm{DK}}=\exp(\pi i...)` or
  `q_{\mathrm{DK}}=e^{\pi i...}` pattern.
- `git diff --check -- standalone/genus1_seven_faces.tex
  standalone/drinfeld_kohno_bridge.tex
  compute/tests/test_q_hbar_convention_bridge_scope.py`: clean.

The broader Yangian/BV additive-\(\hbar\) convention sweep remains open;
this pass repairs the sharp KL/DK half/full misidentification.

---

## 2026-06-17 -- Pass 502: K3/BKM/Hall recognition target conditionality propagated through included Vol I surfaces

Audit anchor: `Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
item 14, `expanded_expert_repair_specification_main36 (1).md` C5,
and the Strengthening PDF \(H_\Delta\) / K3 / Hall / BKM block.
Target false pattern: using scalar denominator identities,
finite-window Yangian computations, or automorphic target data as if
they constructed the compact Hall--Drinfeld object
\(\mathbf H_{\Delta_5}\).

Repairs:

- `chapters/examples/w_algebras.tex`: changed the BKM \(W\)-algebra,
  Schiffmann--Vasserot coproduct, and Miura-transform passages so
  they speak of the conditional target
  \(\mathbf H_{\Delta_5}^{\mathrm{tgt}}\) after the compact
  Hall/CoHA source, Hopf pairing, PBW/no-extra-relations theorem,
  parity/comparison data, and Mittag--Leffler inverse limit are
  supplied.
- `chapters/examples/yangians_foundations.tex` and
  `chapters/examples/yangians_computations.tex`: changed the K3
  fourth taxon from an asserted Hall--Drinfeld double to a conditional
  recognition target.  Finite RTT/Yangian data are now explicitly
  finite-window shadows, not a construction of the K3 object.
- `chapters/examples/yangians_drinfeld_kohno.tex`: changed the
  Siegel-KZB braid representation and horizontal-section object to
  target statements on
  \((\mathbf H_{\Delta_5}^{\mathrm{tgt}})^{\otimes n}\), conditional
  on the Hall source, PBW, comparison maps, and KZB connection.
- `chapters/examples/genus_expansions.tex`: made the genus-\(2\)
  Siegel trace a conditional target package on
  \(\overline{\mathcal A}_2\), not a consequence of the
  bar--cobar counit.
- `chapters/examples/bar_complex_tables.tex`: removed the false
  inference that the Gritsenko--Nikulin denominator cancellation
  proves vacuum-sector bar acyclicity.  It is now a target
  Euler-characteristic cancellation; actual Hall bar acyclicity
  requires the source/comparison package.
- `chapters/examples/lattice_foundations.tex`: changed the
  "universal functor" evaluation equalities to a conditional
  automorphic-product recognition dictionary using target arrows
  \(\leadsto\) and \(\mathbf H^{\mathrm{tgt}}\).
- `chapters/examples/symmetric_orbifolds.tex` and
  `chapters/examples/exceptional_yangian_koszul_duality_platonic.tex`:
  changed the K3 Siegel character and exceptional-Yangian K3 row to
  target statements under the same Hall/CoHA, PBW, comparison, and
  inverse-limit gates.
- `chapters/frame/open_beilinson_tower_platonic.tex` and
  `chapters/frame/preface.tex`: downgraded residual front-matter
  assertions about Selmer deformations, Kontsevich formality, sibling
  functors, and the pentagon coboundary tower to conditional target
  packages.  Scalar and automorphic data no longer construct the
  compact Hall object by themselves.
- `compute/tests/test_hdelta5_hall_bkm_recognition_gates.py`: extended
  the regression guard from frame/Vol~III surfaces to the included
  Vol~I example chapters above, checking both required conditional
  language and retired overclaim fragments.

Verification:

- `pytest -q compute/tests/test_hdelta5_hall_bkm_recognition_gates.py`:
  9 passed.
- Fixed-string scans over included `chapters/frame`,
  `chapters/examples`, `appendices`, and `standalone` surfaces found no
  remaining targeted phrases asserting vacuum bar acyclicity from the
  denominator identity, target-free \(\mathbf H_{\Delta_5}\) Hall-double
  equality, universal-\(\Psi\) equality, unconditional
  \(H_{\Delta_5}\) Kontsevich-formality off divisors, or integrable
  \(H_{\Delta_5}\)-module status.
- `git diff --check --` on all touched files in this pass: clean.

No full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 498: Feigin--Frenkel terminology split from the critical-level reflection

Audit anchor: external review item C3 / expert gate warning that
\(k\mapsto-k-2h^\vee\) must not be called the whole
Feigin--Frenkel duality theorem. Target false pattern: presenting the
affine level reflection as "the Feigin--Frenkel involution" and then
identifying it with chiral Koszul / Verdier duality on configuration
spaces.

Repairs:

- `chapters/connections/concordance.tex`: rewrote the Feigin--Frenkel
  comparison table and key remark. The scalar/current-presentation map
  is now the critical-level reflection
  \(\iota_{\mathrm{crit}}(k)=-k-2h^\vee\). The text separates three
  objects: the reflected affine scalar companion, the actual chiral
  Koszul dual obtained via Verdier-dual bar plus chiral CE, and the
  Feigin--Frenkel centre theorem at the fixed critical level.
- `chapters/frame/preface.tex`, `chapters/frame/preface_sections2_4_draft.tex`,
  and `chapters/theory/introduction.tex`: first-reader surfaces now
  state central-charge complementarity using
  \(\iota_{\mathrm{crit}}\), not an untyped "Feigin--Frenkel
  involution"; the preface title is now "Feigin--Frenkel centre and
  the critical-level reflection".
- `chapters/theory/poincare_duality_quantum.tex` and
  `chapters/examples/kac_moody.tex`: local examples and the
  \(\kappa\)-anti-symmetry proposition now say critical-level
  reflection. Kac--Moody text explicitly says Verdier duality acts on
  the bar coalgebra and then passes through the chiral CE dual; it is
  not the bare level relabelling.
- `standalone/five_theorems_modular_koszul.tex`,
  `standalone/survey_modular_koszul_duality_v2.tex`, and
  `standalone/survey_track_a_compressed.tex`: synchronized standalone
  summary copies so the same distinction is visible outside the main
  volume path.
- `compute/tests/test_feigin_frenkel_reflection_scope.py`: added a
  regression guard retiring the stale phrases "The Feigin--Frenkel
  involution" for the level map and "is Koszul duality on
  configuration spaces" on the guarded first-reader surfaces.
- `compute/tests/test_standard_family_certification_surfaces.py`:
  updated the Kac--Moody anchor from "Feigin--Frenkel level
  involution" to "critical-level reflection" and corrected a stale
  landscape-table string to the live "Critical affine boundary"
  wording.

Verification:

- `pytest -q compute/tests/test_feigin_frenkel_reflection_scope.py compute/tests/test_standard_family_certification_surfaces.py`:
  9 passed.
- Fixed-string scans over the guarded first-reader surfaces found no
  remaining occurrences of `The Feigin--Frenkel involution` or `is
  Koszul duality on configuration spaces`.
- `git diff --check --` on the touched files: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 497: External expert-review advice folded into Theorem B and KSDual scope

Audit anchor: `/Users/raeez/Downloads/expanded_expert_repair_specification_main36 (1).md`
and `/Users/raeez/Desktop/Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`.
Target false patterns: (i) treating positive-genus curvature as the
raw scalar identity \(h^{(g)}=\kappa\omega_g\) on the Theorem B
co/contra surface, and (ii) saying that KSDual automatically makes
Theorem A an equivalence and Theorem H exact without the finite-type
curved/Koszul-complete/\(H_3\) packages.

Repairs:

- `chapters/theory/theorem_B_scope_platonic.tex`: changed the setup
  from the fibrewise scalar slogan \(h^{(g)}=\kappa\omega_g\) to the
  raw CDG identity \(d^{(g)2}=h^{(g)}\ast(-)\), the transferred
  curved \(A_\infty\) identity
  \(m_1^{(g)2}(a)=[m_0^{(g)},a]_{m_2}\), and the scalar diagonal
  projection
  \(\operatorname{tr}_{\mathrm{diag}}(m_0^{(g)})=\kappa(\cA)\omega_g\).
  The square-zero object is now explicitly the period-corrected total
  modular differential.
- `appendices/type_system.tex`: scoped KSDual as the
  \(\mathbb Z/2\)-fixed locus computed in the finite-type curved
  Verdier--Koszul ambient. Theorem A now restricts to a unit/counit
  equivalence only under the Koszul-complete package; Theorem H
  exactness is tied to its \(H_3\) package; scalar anti-diagonal sums
  are orbit data, not KSDual membership criteria.
- `standalone/five_theorems_modular_koszul.tex`: synchronized the
  KSDual summary so the five-theorem first-reader surface no longer
  presents \(K=0\), \(c=13\), or the five-archetype label as automatic
  fixed-locus theorem data.
- `compute/tests/test_theorem_B_scope.py` and the local KSDual guard
  `compute/tests/test_master_ksdual_scope.py`: added regression checks
  for the curvature/projection split and for the package-scoped KSDual
  exactness language.

Verification:

- `pytest -q compute/tests/test_theorem_B_scope.py compute/tests/test_master_ksdual_scope.py compute/tests/test_positive_genus_curvature_projection_scope.py`:
  17 passed.
- Fixed-string scans over the patched KSDual and Theorem B surfaces
  found no remaining live occurrences of the retired unscoped phrases
  `h^{(g)} = \kappa \cdot \omega_g`, `where Theorem~A is an
  equivalence`, `Theorem~H is exact in $\{0, 1, 2\}$`, or
  `Self-dual points include`.
- `git diff --check --` on the touched files: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 496: Ordered-to-symmetric averaging typed as \(L_R\)-twisted conductor descent

Audit anchor: expanded repair specification A8 and the external review's
ordered/symmetric conductor recommendation. Target false pattern:
presenting ordered-to-symmetric averaging as a naive
\(\Sigma_n\)-average that simply "kills" \(R\)-matrix/Yangian data,
instead of a typed descent theorem with hypotheses and a formal kernel.

Repairs:

- `chapters/theory/universal_conductor_K_platonic.tex`: made
  conductor eligibility the explicit package
  \(\mathbf H_{\mathrm{uc}}(\cA)\): conilpotent completion, equivariant
  ordered differential/bracket, QYBE, strong unitarity
  \(R^{21}(-z)R^{12}(z)=\id\), regular-singular
  Fulton--MacPherson extension of \(L_R\), and compatibility of nearby
  cycles with chiral collision products. Added the chain-level
  \(L_R\)-twisted derived completed coinvariant target and defined the
  ordered information-loss conductor as the homotopy fibre.
- `chapters/frame/guide_to_main_results.tex`,
  `chapters/frame/preface.tex`, `chapters/theory/introduction.tex`,
  `chapters/theory/bar_cobar_adjunction_curved.tex`, and
  `chapters/theory/bar_construction.tex`: replaced naive first-reader
  averaging language by the universal-conductor descent; retained the
  Reynolds average only as the untwisted characteristic-zero
  representative.
- `standalone/introduction_full_survey.tex`,
  `standalone/programme_summary.tex`,
  `standalone/programme_summary_section1.tex`,
  `standalone/survey_modular_koszul_duality.tex`,
  `standalone/e1_primacy_ordered_bar.tex`,
  `standalone/five_theorems_modular_koszul.tex`, and
  `standalone/koszulness_fourteen_characterizations.tex`: synchronized
  the standalone summary surfaces so the missing ordered data live in
  the formal conductor fibre, not in metaphorical "discarded" data.
- `compute/tests/test_ordered_symmetric_conductor_scope.py`: added a
  regression guard for the A8 hypothesis package, the formal conductor
  fibre, and retired phrases such as "kills/discards the \(R\)-matrix"
  in first-reader surfaces.

Verification:

- `pytest compute/tests/test_ordered_symmetric_conductor_scope.py`: 3
  passed.
- `pytest compute/tests/test_ordered_bar_descent_engine.py`: 76 passed.
- Fixed-string scans over `chapters/frame`, `chapters/theory`,
  `standalone`, and `appendices` found no remaining first-reader
  occurrences of the retired "kills/discards the \(R\)-matrix" or
  "general averaging is the plain \(\Sigma_n\)-projection" phrasing.
- `git diff --check --` on the touched files: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 495: Positive-genus curvature scoped as curved CDG plus scalar projection

Audit anchor: review/spec A7 and D4 from
`expanded_expert_repair_specification_main36 (1).md` and
`Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`. Target false
pattern: treating \(d_{\mathrm{fib}}^2=\kappa(\cA)\omega_g\) or
\(\kappa(\cA)\lambda_g\) as a raw chain/operator identity rather than
as a scalar diagonal / uniform-weight Hodge projection of the curved
\(A_\infty\)/CDG package.

Repairs:

- `chapters/theory/higher_genus_foundations.tex`: retargeted the
  canonical higher-genus convention and the chain-level curvature
  proposition. The raw statement is now
  \(m_1^{(g)\,2}(a)=m_2(m_0^{(g)},a)-m_2(a,m_0^{(g)})
  =[m_0^{(g)},a]\); \(\kappa(\cA)\omega_g\) appears only after
  scalar diagonal projection, and \(\kappa(\cA)\lambda_g\) only after
  the Hodge/Chern--Weil projection.
- `chapters/theory/bar_cobar_adjunction_curved.tex`: rewrote the
  curved gravity dictionary so \(D_g\) is the period-corrected
  square-zero total differential and the scalar Hodge coefficient is a
  projection of \(m_0^{(g)}\), not a raw square of \(\dfib\).
- `chapters/frame/preface.tex`, `chapters/theory/introduction.tex`,
  and `chapters/frame/guide_to_main_results.tex`: synchronized the
  public theorem-facing Theorem~D summaries and roadmap lines with the
  chain/scalar/total split.
- `chapters/connections/thqg_open_closed_realization.tex`,
  `appendices/homotopy_transfer.tex`, and
  `chapters/connections/concordance.tex`: repaired the physics bridge,
  HTT transfer statement, and concordance remarks so they refer to
  the curved identity and scalar/Hodge projections separately.
- Standalone mirrors
  `standalone/survey_modular_koszul_duality_v2.tex`,
  `standalone/programme_summary.tex`,
  `standalone/programme_summary_section1.tex`,
  `standalone/survey_track_a_compressed.tex`, and
  `standalone/five_theorems_modular_koszul.tex` now carry the same
  projected-curvature wording.
- Added `compute/tests/test_positive_genus_curvature_projection_scope.py`
  to block the retired raw scalar-square phrasing on the repaired
  surfaces and require the chain/scalar/period-corrected total layers.

Verification:

- `pytest compute/tests/test_positive_genus_curvature_projection_scope.py
  compute/tests/test_higher_genus_curved_scope.py
  compute/tests/test_arnold_borcherds_nilpotence_scope.py`: 7 passed.
- Targeted fixed-string scan over the repaired surfaces leaves only the
  intentional convention-warning line that defines
  `\dfib^{\,2}=\kappa\omega_g` as scalar-projection shorthand.
- `git diff --check --` the repaired files and new guard: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## [theorem-H/H-2] fatal / false / conf=high

CLAIM: the old affine witness identified first chiral Hochschild
cohomology with the adjoint g at generic non-critical level, realised by
adjoint-action derivations (witness table; prop:chirhoch1-affine-km;
old affine sl_2 vector; restated inside thm:mr-H).  This claim is now
repaired by the zero-mode quotient firewall.

LOCATION: chapters/theory/chiral_center_theorem.tex:2168-2239 and 2018-2044; chapters/theory/chiral_hochschild_koszul.tex:1728-1731, 1398-1424; chapters/connections/master_reconstruction.tex:297-298

EVIDENCE: The chapter's own inner-derivation operator is the zero mode: line 7125 of chiral_hochschild_koszul.tex says 'The chiral computation uses a different inner-derivation operator, namely the vertex-algebra zero mode a_(0)'. For V_k(g), (J^a)_(0)J^b = f^{ab}_c J^c is precisely the adjoint action, so the adjoint cochains are coboundaries of the 0-cochains J^a ∈ A — inner by the manuscript's own convention. The proof of prop:chirhoch1-affine-km exhibits the adjoint maps as cocycles ('the cochains J^a ↦ εφ^a for φ ∈ g form exactly one copy of the adjoint g-module'), kills everything else as boundaries, and never quotients the adjoint summand by the inner coboundaries; the honest weight-0 quotient is Der(g)∩so(κ)/ad(g) = 0 for simple g. The supporting 'three-term Koszul resolution 0→A⊗g^*⊗A→A⊗g⊗A→A⊗A→A→0' (line 2200-2207) is not a resolution of the diagonal bimodule: the manuscript's own computation (chiral_koszul_pairs.tex:1496-1517) gives dim(A^i)_2 = 5 for affine sl_2 at weight 3, which I reverified by direct CE computation (ranks 3 and 1, H^2 = (9−1)−3 = 5), so the dual coalgebra has nonzero pieces in bar degree ≥ 2 and the diagonal resolution cannot terminate after three terms; relatedly, prop:derived-center-explicit(ii)'s claim that 'the bar cohomology is concentrated in bar degree 1 (chiral Koszulness)' contradicts that 5. The proof of cor:chirhoch-affine-sl2 (line 1416-1424) additionally conflates Ext^1_{V_k}(C,C) (= the generating space g, the Koszul-dual side A^!) with ChirHoch^1 = Ext^1_{A^e}(A,A), violating the repo's own five-object firewall.

REPAIR: (1) Recompute ChirHoch^1(V_k(g)) in the chapter's stated convention (ChirHoch^1 = Der/Inn with Inn = {a_(0)}, chiral_hochschild_koszul.tex:7113-7125, 3555-3560, 8614-8617) with the inner quotient performed. Weight-0 cocycles: D(J^a) = M^a_b J^b requires M in Der(g) ∩ so(κ) = ad(g) for simple g (verified by sympy: 3-parameter for sl_2); these equal the inner derivations (φ_a J^a)_(0) since (J^b)_(0)J^a = f^{ba}_c J^c (OPE residue). Constant-shift cochains J^a ↦ v^a·1 are cocycles only for v ∈ z(g) = 0. So the weight-0 answer is 0, mirroring HH^1(U(g)) = H^1(g,U(g)) = 0 (Whitehead + local finiteness); state the all-weight vanishing only after an honest positive-weight computation or name it as an explicit proof obligation. (2) Propagate: witness-table row chiral_hochschild_koszul.tex:1728-1731 (dim 0; 'adjoint derivations inner via current zero modes; level external'); rewrite observation (i) of rem:chirhoch-derivation-types — the simple-pole-innerness dichotomy (line 3598) applies to class L exactly as to βγ/bc/fermion, making the Heisenberg the unique simple-pole-free survivor; cor:chirhoch-affine-sl2 old affine vector → (1,0,1) and rem:sl2-chirhoch-dim5 total corrected to 2, deleting the sl_3/sl_4/E_8 growth sentence; fix line 7174; prop:smooth-formal-moduli-standard's V_k(g) case becomes a reduced point and the 'inner-gauge orbits' family argument is deleted (an inner-gauge orbit is by definition a trivial deformation family); excise the clause from thm:mr-H (master_reconstruction.tex:297-298); fix compute/lib/chiral_hochschild_engine.py::_km_derivation_analysis (weight-0: total dim g, inner dim g, outer 0 — currently hardcodes inner_derivations=0 while _betagamma/_bc set inner=1 for the identical zero-mode mechanism) and its tests. (3) Repair the two supporting defects inside this scope: (a) in prop:derived-center-explicit(ii) (chiral_center_theorem.tex:2035-2039) replace 'bar cohomology concentrated in bar degree 1 (chiral Koszulness)' with the actual Koszulness of thm:bar-concentration — concentration in bar-differential degree q = 0 with (A^i)_p ≠ 0 in all bar degrees p, e.g. dim(A^i)_2 = 5 at weight 3 (chiral_koszul_pairs.tex:1504-1509, re-verified: ranks 3 and 1, (9−1)−3 = 5); (b) delete the three-term diagonal Koszul resolution (chiral_center_theorem.tex:2092-2094, 2200-2207) — the diagonal resolution has terms A⊗(A^i_p)^∨⊗A for every p with (A^i)_p ≠ 0, and CE cohomology of g⊗t^{-1}C[t^{-1}] is nonzero in arbitrarily high degrees, so degree-≥3 vanishing and the ChirHoch^2 = C computation cannot be sourced from resolution length; re-derive concentration (if at all) from the FM-tower collapse of thm:main-koszul-hoch and flag the weakened ChirHoch^2 support to its own finding; (c) in cor:chirhoch-affine-sl2's proof delete 'Ext^1_{V_k(sl_2)}(C,C) = sl_2' as Hochschild input — that group is the Koszul-dual generating space (A^i)_1 (bar-degree-1 cohomology, the A^! side), not ChirHoch^1 = Ext^1 over the chiral enveloping/bimodule structure, per the five-object firewall. (4) If a nonzero affine H^1 is intended under the engine docstring's undefined 'chiral OPE deformation complex' (no inner quotient), define that complex once at Definition level and apply it uniformly to every row — noting this would resurrect the βγ/bc rescaling and fermion classes and destroy the table's internal logic — and rename the invariant so it is not conflated with the Der/Inn ChirHoch^1 used everywhere else (per H-6).

---

## [theorem-H/H-3] fatal / status-inflation / conf=high

CLAIM: the old engine advertised its sl_N adjoint prequotient arithmetic
as a verification of Theorem H's affine dimension package per the repo's
3-path rule.

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:1778-1781; compute/lib/chiral_hochschild_engine.py:415-465, 496-531, 855-901; compute/tests/test_theorem_H_hochschild_koszul.py:251-379

EVIDENCE: The engine computed nothing: center_dimension() ended in 'return 1'; center_dimension_koszul_dual() was 'return 1'; _km_derivation_analysis returned outer_derivations = lie_dim with the literal table {'current_algebra_derivations': d, 'level_deformation': 0} and inner_derivations=0; WAlgebraHochschild.dim_n returned 1 for n∈{0,2} else 0. The advertised N=10 check was only the arithmetic identity 10²−1=99 about dim sl_10, not a cohomology computation. inner_derivations=0 for KM is false in the manuscript's own convention (the zero modes (J^a)_(0) are nonzero inner derivations, line 7125). The tests asserted hardcoded tuples equal themselves, with 'paths' like sl2_dim1_via_whitehead == dim_simple_lie_algebra('sl_2'), which returns 3 by construction. No path computed a differential, a cocycle space, or a quotient.

REPAIR: (1) chapters/theory/chiral_hochschild_koszul.tex:1778-1781 — delete the two sentences, or replace with the honest statement: the breakdown is *recorded* in compute/lib/chiral_hochschild_engine.py as a ledger instantiating Proposition prop:chirhoch1-affine-km (itself \ClaimStatusConditional); the only computation on that code path is dim sl_N = N^2-1 as prequotient metadata, and a chain-level verification of the dimension package is an open compute obligation. Never use 'verified'/'confirms' for the old prequotient helper, whose expected and computed values are the same arithmetic N^2-1 transcribed twice. (2) Same file, ~line 1813 (proof of prop:smooth-formal-moduli-standard): change 'verified in the chiral-Hochschild engine for W_N at N=3,…,10' to 'recorded in the chiral-Hochschild engine' — WAlgebraHochschild.dim_n and _wN_derivation_analysis are constant functions of N (and the test range is N=2..8), so the N-range conveys spurious verification strength. (3) Retag rem:chirhoch-derivation-types (line 1696) from \ClaimStatusComputed to match the Conditional status of its source proposition, restoring it only when item (4) lands. (4) Add the one genuine path the auditor proposes, patterned on the repo's existing computational precedent ordered_chirhoch_arity4_derham_engine.py (which builds an actual complex and computes ranks): a finite-weight-window sympy engine for H_k and V_k(sl_2) (weight <= 3-4) enumerating weight-graded 1-cochains on generators, imposing lambda-bracket Leibniz through BOTH the double-pole central term and the simple-pole f^{ab}_c term, quotienting by zero-mode coboundaries a_(0) (which for KM include the adjoint action), reporting dim ker/im per window. Critically, write it to report rather than confirm: the explicit cochain D_X(J^a) = X^a|0> offered by prop:gerstenhaber-sl2-bracket fails the cocycle condition for simple g (f^{ab}_c X^c != 0), and the adjoint candidates are inner under the manuscript's own zero-mode convention, so the honest computation may falsify the naive nonzero affine-H1 convention — in which case prop:chirhoch1-affine-km must name the completed/curve-level ambient in which its Koszul-resolution Ext yields g, or be healed. (5) Fix the engine's data model: _km_derivation_analysis records inner_derivations=0, but in the manuscript's convention (lines 7118/7125/7174) the zero modes (J^a)_(0) are nonzero inner derivations (dim >= dim g); either correct the field or rename the DerivationAnalysis fields so they stop claiming to be dim Der(A)/dim Inn(A) — the docstring already disavows that reading.

---

## [theorem-H/H-5] major / false / conf=high

CLAIM: thm:chiral-hochschild-complex (ProvedHere): the displayed normalized cochain complex 0→Hom(A,M)→Hom(A^⊗2,M)→… with δ_n f = Y(a_0,f(…)) + Σ_{i=1}^n (−1)^i f(…,Y(a_i,a_{i+1}),…) + (−1)^{n+1} Y(f(…),a_{n+1}) computes RHom_{A^e}(A,M)

LOCATION: chapters/theory/koszul_pair_structure.tex:488-510

EVIDENCE: As displayed the differential does not square to zero: the internal sum runs i=1..n, omitting the i=0 face f(Y(a_0,a_1),…). Direct check in the associative shadow with their n=0,1 formulas: δ_0f(a,b) = af(b) − f(a)b; δ_1g(a,b,c) = ag(b,c) − g(a,bc) + g(a,b)c; then δ_1δ_0 f(a,b,c) = ab·f(c) − a·f(bc) ≠ 0. Also the complex omits the degree-0 term Hom(k,M)=M of Hom_{A^e}(Bar_•(A),M), which is exactly the term whose image kills inner derivations — the plausible mechanical origin of finding H-2's never-quotiented adjoint classes. A theorem tagged ProvedHere whose displayed object is not a complex is status-inflated regardless of the fixability.

REPAIR: In koszul_pair_structure.tex, thm:chiral-hochschild-complex (lines 488-510): (1) Re-index the cochain spaces to the standard convention C^n = Hom_{D_X}(Abar^{(x)n}, M) for n >= 0, with C^0 = Hom_{A^e}(A (x) A, M) = M, and display the complex as 0 -> M -> Hom_{D_X}(Abar, M) -> Hom_{D_X}(Abar^{(x)2}, M) -> ... (Abar = ker epsilon, per the normalized convention already stated at lines 403-404). (2) Keep the displayed differential formula verbatim but 1-index the arguments, with f of arity n: (delta_n f)(a_1,...,a_{n+1}) = Y(a_1, f(a_2,...,a_{n+1})) + sum_{i=1}^{n} (-1)^i f(a_1,...,Y(a_i,a_{i+1}),...,a_{n+1}) + (-1)^{n+1} Y(f(a_1,...,a_n), a_{n+1}); in degree 0, (delta_0 m)(a) = Y(a,m) - Y(m,a), the chiral adjoint map whose image is the inner derivations. (Equivalently, if 0-indexed labels a_0..a_{n+1} are retained for arity-(n+1) cochains, the internal sum must run i=0..n with signs (-1)^{i+1} and the last face must carry (-1)^n; appending the i=0 face with sign +1 alone does NOT restore delta^2 = 0.) (3) Amend the proof to record Hom_{A^e}(A (x) Abar^{(x)n} (x) A, M) = Hom_{D_X}(Abar^{(x)n}, M), the two outer faces giving the first and last terms and the n internal faces the middle sum, with degree 0 = Hom_{A^e}(A (x) A, M) = M. (4) Record the restored degree placement -- H^0 = M^A (centre for M = A), H^1 = Der/Inn (the M-term's image is exactly the inner/adjoint classes), H^2 = infinitesimal deformations -- matching def:chiral-hochschild-complex (n inputs in degree n) and the Vir witness ChirHoch^0 = C, ChirHoch^2 = C.Theta. (5) Fix the same off-by-one in the companion thm:geometric-chiral-hochschild (lines 514-531): its degree-n term Gamma(C-bar_{n+1}(X), Hom(A^{boxtimes(n+1)}, A) (x) Omega^n_log) must be reconciled with def:chiral-hochschild-complex's degree-n term on C-bar_{n+2}(X) (n inputs + output + evaluation point). (6) Propagate the inner-derivation quotient at H^1 to the witness tables (scope of H-6).

---

## [theorem-H/H-6] major / type-error / conf=high

CLAIM: Consistent degree conventions across witnesses: the Heisenberg level tangent k↦k+ε is a degree-1 class ('the single outer derivation encoding the level deformation', dim ChirHoch^1(H_k)=1) while the Virasoro central-charge tangent c↦c+ε is a degree-2 class (dim ChirHoch^1(Vir_c)=0, Θ ∈ ChirHoch^2)

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:1358-1396, 1719-1737; chapters/theory/chiral_center_theorem.tex:1992-2070; compute/lib/chiral_hochschild_engine.py:534-561, 652-679

EVIDENCE: Both classes deform the binary OPE coefficient of the unique generator (k/(z−w)² vs (c/2)/(z−w)⁴): structurally identical product deformations. No single grading convention places one in degree 1 and the other in degree 2; the chapter does both. A genuine outer degree-1 class for H_k exists — the shift derivation D(J)=1, outer since b_(0)J = const forces |b|=0 and 1_(0)=0 — but the manuscript misidentifies its H^1 class as the level deformation (the scaling derivation D(J)=J fails the derivation identity on J_(1)J = k|0⟩: LHS 0, RHS 2k|0⟩, so the level direction is not a derivation at all). The engine encodes the same contradiction: heisenberg derivation_types={'level_deformation': 1} vs virasoro 'that parameter is a deformation class in degree 2'.

REPAIR: Adopt-by-propagation, not by fiat: the chapter already declares and correctly applies the standard convention (ChirHoch^1 = Der/Inn, ChirHoch^2 = binary product deformations "in the unshifted Gerstenhaber convention") in comp:boson-hochschild (chiral_hochschild_koszul.tex:3541-3569) and the explicit boson example (7111-7174). Propagate those computations into the five inconsistent sites. Concretely: (1) In cor:chirhoch-heisenberg (1358-1374), rem:heisenberg-family-vs-fixed-fiber (1376-1387), the Heisenberg row + observation (i) of rem:chirhoch-derivation-types (1719-1755), prop:derived-center-explicit(i) (chiral_center_theorem.tex:1992-2016), and _heisenberg_derivation_analysis (engine 534-561): name the ChirHoch^1 witness as the shift derivation D(alpha)=1 (alpha -> alpha + eps*1; outer since a_(0)alpha = 1 forces wt(a)=0 and 1_(0)=0), the class lines 3560/7122 already exhibit; delete every identification of the level tangent with a derivation (D(alpha)=alpha fails the derivation identity on alpha_(1)alpha = k|0>: 0 vs 2k|0>); set engine derivation_types={'shift_derivation': 1, 'level_deformation': 0} and fix the false docstring claim that rescaling generates the derivation space. (2) Place the level tangent k -> k+eps in degree 2 AND record its exactness at k != 0: it equals d(N/2k) for the rescaling 1-cochain N(alpha)=alpha, witnessing H_{k+eps} iso H_k via alpha -> (1+eps/2k)alpha; correspondingly repair the degree-2 paragraphs at 3562-3568 and 7148-7154 ("ChirHoch^2 = C.[k]"): if dim ChirHoch^2 = 1 via the Koszul-duality route Z(A^!)^vee, its generator is the dual-vacuum eta of prop:derived-center-explicit(i), not the level class. Invert observation (i): free rescaling makes the Heisenberg level GAUGE-TRIVIAL, while the affine level is a nontrivial degree-2 direction (no rescaling absorbs it against the simple-pole term); that is the honest G/L asymmetry. (3) Re-derive the BV/Gerstenhaber package of chiral_center_theorem.tex:2583-2680 (xi_k^2 = k*eta, Delta(xi_k)=1, [xi_k,eta]=-eta) for the corrected degree-1 witness; the relation xi^2 = k*eta loses its justification once xi_k leaves degree 1. (4) Rebuild prop:smooth-formal-moduli-standard (1784-1840) and the archetype table (1842-1878) with the tangent space to chiral-product formal moduli = ChirHoch^2 (MC elements of the shifted deformation dgla), not ChirHoch^1 (degree-1 classes are infinitesimal automorphisms): the "MC family k -> k+eps" is gauge-constant in moduli; the V_k(g) "inner-gauge orbits of J^a" are gauge directions contributing zero moduli; and dim M(Vir_c)=0 contradicts the chapter's own nontrivial Theta-family c -> c+eps (a genuinely 1-dimensional product-moduli direction since Theta is not exact: only v = beta*T has the right weight and the induced 2*beta*T term in the (1)-slot forces beta=0). Recompute the table per family, deciding triviality (exactness) of each degree-2 class. (5) The Virasoro triple (1,0,1) and the KM engine entry level_deformation: 0 stand unchanged; the Heisenberg dims (1,1,1) survive in degrees 0,1 with the shift witness, while degree 2 requires the honest eta-vs-[k] re-derivation above.

---

## [theorem-H/H-7] major / false / conf=high

CLAIM: Heisenberg witness package: dim ChirHoch^2(H_k) = 1 because ChirHoch^2 ≅ Z(H_k^!)^∨⊗ω_X with H_k^! = Sym^ch(V^*) and Z(Sym^ch(V^*)) = C; sharp Hilbert series eq:chirhoch-sharp-hilbert has t²-column HS_{Z(A^!)}(q)

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:1293-1330 (prop:chirhoch-sharp-hilbert), 1358-1396 (cor:chirhoch-heisenberg); chapters/theory/chiral_center_theorem.tex:1992-2016; compute/lib/chiral_hochschild_engine.py:445-465

EVIDENCE: The centre of a commutative chiral/vertex algebra is the whole algebra (all non-negative products vanish), so Z(Sym^ch(V^*)) = Sym^ch(V^*) is infinite-dimensional, with q-character of product type, not 1. Hence by the chapter's own formula ChirHoch^2(H_k) ≅ Z(H_k^!)^∨⊗ω_X would be infinite-dimensional, contradicting the recorded dim = 1; equivalently the asserted input 'Z(H_k^!) = C' (proof of cor:chirhoch-heisenberg, line 1393-1395; engine docstring 'A! = Sym^ch(V*), center = C → dim = 1') is false for the stated dual. The companion proof in prop:derived-center-explicit(i) manufactures the answer from a 'three-term resolution 0→A⊗V^*⊗A→A⊗V⊗A→A⊗A→A→0 ... of the polynomial vertex algebra on one generator' — but a free polynomial algebra on one generator has a two-term diagonal Koszul resolution (no relation term), so the displayed resolution is fabricated to produce HH^2 = C.

REPAIR: Keep the triple (1,1,1) — it has an independent direct OPE witness (comp:boson-hochschild, chiral_hochschild_koszul.tex:3541-3569: regular-OPE centre of H_k itself, the outer derivation D(alpha)=1 from the no-simple-pole zero mode, the level-deformation 2-cocycle) — but repair the Koszul-duality route by making the curvature load-bearing, as the chapter itself half-records at line 3602: (a) In cor:chirhoch-heisenberg and its proof (chiral_hochschild_koszul.tex:1358-1396), replace "Z(H_k^!) = Z(Sym^ch(V^*)) = C" with the curved dual H_k^! = (Sym^ch(V^*[1]), m_0 = -k·omega) ≅ CE(h-hat_{-k}); note H_k is non-augmented for k≠0 (a_{(1)}a = k·1 admits no augmentation), so its bar/Koszul dual is necessarily curved, and the uncurved commutative Sym^ch(V^*) has Z equal to itself with product-type q-character. Inscribe a lemma that the degree-0 cohomology of the completed second-kind Hochschild complex of the curved dual is C for k≠0 (nondegenerate curvature, Clifford-type collapse) — currently this is only asserted without proof in ex:heisenberg-curved-specialization (2661-2673). (b) In prop:chirhoch-sharp-hilbert (1293-1330), add the hypothesis that A^! is an honest uncurved chiral algebra with the stated centre (excluding non-augmented A such as H_k at k≠0 from the literal statement), or define the t^2-column as the curved second-kind centre when A is non-augmented; as written, the t^2-column applied to a commutative dual is the full q-character of the dual itself — exactly the mechanism by which the critical-level Feigin-Frenkel divergence appears, per the chapter's own remarks. (c) In prop:derived-center-explicit(i) (chiral_center_theorem.tex:2074-2099), delete the displayed three-term resolution: for a free polynomial algebra on one generator the associative Koszul diagonal resolution is two-term (Lambda^2 V = 0) and gives HH^2 = 0; replace it with the curved/chiral resolution whose third slot is the level-curvature line (the nonhomogeneous relation a_{(1)}a = k·1) together with the curve-level omega_X twist of the FM collapse, or route degree 2 through the level-deformation cocycle of comp:boson-hochschild. (d) In compute/lib/chiral_hochschild_engine.py:445-465, correct the docstring to "A! = (Sym^ch(V*[1]), m_0 = -k·omega) ≅ CE(h-hat_{-k}); curved second-kind centre = C at k≠0; the uncurved commutative Sym^ch(V*) has Z = itself (infinite-dimensional, finite per weight)". (e) Reconcile lines 3494 and 3536 ("a commutative chiral algebra", no curvature) with line 3602 (curvature m_0 = -k·omega): the curvature must appear at every occurrence of H_k^! at k≠0; the uncurved commutative algebra is only the k=0/associated-graded shadow. The auditor's finite-window alternative is a weaker stopgap; the curved-dual repair is the correct one and matches the manuscript's own ex:heisenberg-curved-specialization.

---

## [theorem-H/H-8] major / unproven-as-stated / conf=high

CLAIM: Shift and indexing bookkeeping: E_2^{r,p}(p) ≅ Ext^r_{D_X}((A^!)_p, ω_X) concentrated in row s=p; 'the geometric Verdier shift [p+2] ... and the totalization shift [−p] ... combine to the constant shift [2]'; per-bar-degree summands CH^{p,•}[−p] then have amplitude [0,2] independently of p

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:632-732 (lem:hochschild-shift-computation), 734-763 (lem:totalization-amplitude hypothesis); chapters/theory/higher_genus_foundations.tex:3061-3074 (rem:hochschild-shift-origin)

EVIDENCE: Three mutually inconsistent indexings are used for the same collapse: lem:hochschild-shift-computation puts the survivors in the row s=p with r the Ext degree; its own proof puts them at the single deepest filtration level (full collision, codimension p+1), i.e. one column, with the Ext degree varying; rem:hochschild-shift-origin says they lie 'on the diagonal p=q'. With E_2 in row s=p, the abutment satisfies H^m(CH^{p,•}) ≅ Ext^{m−p}, nonzero for m ∈ [p, p+2]; under the manuscript's cohomological conventions (CLAUDE.md: |d|=+1, s^{-1} lowers degree, so H^n(C[−p]) = H^{n−p}(C)) the shifted summand CH^{p,•}[−p] then has cohomology in [2p, 2p+2], not [0,2] — so the hypothesis of lem:totalization-amplitude is not delivered by the shift lemma as written; it works only under the opposite shift convention, never fixed. Adding the Verdier label [p+2] (which relates the A-side to the A^!-side in the duality, not the amplitude of CH^{p,•}(A)) to the totalization label [−p] is symbol arithmetic, not a degree computation.

REPAIR: Keep the auditor's repair direction but do not introduce a new convention: the manuscript already fixes one (rem:shift-notation, appendices/signs_and_shifts.tex: V[n]^k = V^{k+n}, with a Warning that opposite-convention shift indices must be negated); cite it at def:bigraded-hochschild. Then: (1) Perform once the honest degree count the chapter skips: fix the normalization of omega_{C_{p+2}(X)} (sheaf vs dualizing complex), and compute the internal degree at which the deepest-stratum survivor of prop:fm-tower-collapse(iv) sits — Kashiwara offset for the codimension-(p+1) full-collision embedding plus the fiber form-degree p of the weight-p bar strand plus the base D_X-Ext degree r in [0,2]. This determines the true offset delta(p) (= p if the row claim s=p survives the count, p+1 otherwise) and reconciles statement (i) with its deepest-stratum proof mechanism: restate (i) as concentration in the single deepest-stratum column with abutment H^m(CH^{p,bullet}) iso Ext^{m-delta(p)}_{D_X}((A^!)_p, omega_X). (2) Replace the twist [-p] by [+delta(p)] in def:bigraded-hochschild (higher_genus_foundations.tex:3052) and at every use site (chiral_hochschild_koszul.tex lines 671, 747, 755, 776, 788, 797, 805, 855, 1244, 2168, 2274), so that under the declared convention H^k(CH^{p,bullet}[delta(p)]) = H^{k+delta(p)}(CH^{p,bullet}) iso Ext^k, giving each summand amplitude [0,2] by computation; verify d_bar has degree +1 in the regraded total degree. (3) Rewrite lemma (iii): delete '(p+2)-p=2'; state instead (a) the per-summand anchoring isomorphism above, and (b) the constant [2] in RHH(A) iso RHom(RHH(A^!), omega_X[2]) as base-curve Verdier/Serre duality (2 = 2 dim_C X; holonomic D_X-Ext on a proper curve has amplitude [0,2]), with the configuration-space shift p+2 shown to cancel inside the collapse (fiber pairing against the bar strand) in the same count — noting that in the duality the regrading enters both sides of RHom (as -p and +p), so a constant [2] is not obtainable as (p+2)+(-p). (4) Correct rem:hochschild-shift-origin ('diagonal p=q') and the transport sentences in rem:theorem-H-filter-exactness and thm:main-koszul-hoch to the corrected indexing. (5) lem:totalization-amplitude needs only its citation and E_1 line updated (E_1^{p,q} = H^{p+q+delta(p)}(CH^{p,bullet}) iso Ext^{p+q}); its amplitude-transport logic stands as the auditor said.

---

## [theorem-H/H-9] major / unproven-as-stated / conf=high

CLAIM: E_2-degeneration of the collision-depth spectral sequence: 'the same strata carry pure mixed Hodge structures, and Deligne strictness forbids a nonzero weight-changing differential beyond E_2'; FM-formality (Kontsevich) ensures no higher chain-level corrections — with coefficients A^{⊠(p+2)} for A = V_k(g), Vir_c, etc.

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:709-718, 1250-1255 (Step 7 of prop:fm-tower-collapse)

EVIDENCE: Purity/strictness arguments apply to complexes of mixed Hodge modules; the coefficients here are chiral-algebra D-modules (V_k(g) is an inductive limit of infinite-rank induced D-modules), which are neither coherent nor holonomic and carry no MHM structure, so 'pure MHS on the strata' has no defined meaning for the actual E_1 page. Kontsevich/FM formality (prop:en-formality) concerns constant real coefficients on the local fibres; it does not control differentials in a spectral sequence with non-constant infinite-rank D-module coefficients coupled by OPE residues. Both degeneration arguments are category errors as applied; degeneration may still hold but requires a finite-window holonomic reduction first, which is nowhere performed at this step.

REPAIR: In both places replace the formality/purity justification by the support (lattice) argument, which needs no Hodge theory and no holonomicity. (1) lem:hochschild-shift-computation, lines 709-718: replace the paragraph "The higher differentials vanish for either of two standard reasons. ... Thus E_2(p)=E_infty(p)." with: "Higher differentials vanish for support reasons: by (i) the E_2-page is concentrated in the single row s=p, and d_m: E_m^{r,s} -> E_m^{r+m,s-m+1} changes s by m-1>=1 for m>=2, so every d_m with m>=2 has zero source or zero target. Since the collision-depth filtration at fixed p is finite, E_2(p)=E_infty(p)." (2) prop:fm-tower-collapse Step 7, lines 1250-1255: replace by the same argument quoting eq:fm-tower-surviving (E_2^{r,s}(p)=0 for s!=p, established in Steps 3-5 via localized residue-twisted bar concentration), noting the degeneration inherits exactly the conditional scope of that concentration (Koszul locus), with no additional hypothesis. (3) If the Hodge-theoretic remark is retained at all, demote it explicitly to a constant-coefficient consistency check: H^k(FM_m(C);Q) is pure Tate of weight 2k, which explains degeneration of the analogous constant-coefficient Cohen-Taylor/Leray spectral sequence; it is not an argument here, because the chiral coefficient D-modules (ind-induced, characteristic variety T*X, non-holonomic at every finite conformal-weight window) underlie no mixed Hodge module, so Deligne strictness does not apply -- and prop:en-formality, being an operad-level constant-coefficient statement supplying no strict maps on prescribed complexes, does not constrain coefficient-coupled differentials. Do NOT adopt the auditor's first repair branch (prove MHM/weight structure on finite windows where coefficients are "O-coherent hence holonomic"): finite-window pieces of induced chiral-algebra D-modules are never O-coherent or holonomic, so no MHM structure exists at any window; the finite-window + Mittag-Leffler + holonomic-perfectness hypotheses already stated in thm:main-koszul-hoch stay where they belong (Ext identification, amplitude, duality), not in the degeneration step.

---

## [theorem-H/H-10] major / unproven-as-stated / conf=high

CLAIM: Averaging step (attack d): cor:hochschild-averaging-symmetric — av: g^{E_1} → g^{mod} preserves the {0,1,2} envelope; 'The E_∞-chiral hypothesis provides a Σ_n-equivariant null-homotopy of the ordered Hochschild complex in ordered degrees ≥ 3 at the level of cochains'; ChirHoch^n(A) = (ChirHoch^{ord,n}(A))_{Σ_n}

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:1880-1923; chapters/connections/master_reconstruction.tex:315-325

EVIDENCE: The cochain-level equivariant null-homotopy is asserted in a single parenthesis ('the PBW filtration is Σ_n-stable by construction, and its commutative-chiral associated graded carries the standard Koszul homotopy equivariantly') with no construction and no passage from gr to the filtered complex. If the symmetric complex is literally the Σ-coinvariants of the ordered one (as the final equation ChirHoch^n = (ChirHoch^{ord,n})_{Σ_n} and lem:chirhoch-descent's (−)_{Σ,Δ} presuppose), then char-0 exactness of coinvariants alone yields the corollary and the E_∞ hypothesis does no work; if it is not literally coinvariants (the BD/Ran-space symmetric theory), the final equation is unproven — the identification of the symmetric ChirHoch with ordered coinvariants is exactly the conditional, unconstructed descent comparison of H-4. Either way the proof as written does not establish what the E_∞ hypothesis is claimed to be essential for, and thm:mr-H's proof body repeats the envelope-preservation as a citation of this corollary.

REPAIR: Reject the auditor's first repair branch (the "two lines from char-0 exactness" proof is unsound: degreewise varying-group coinvariants do not commute with cohomology — explicit counterexample — and by prop:r-matrix-descent-vol1/cor:pole-free-descent the plain Sigma-action is not even by chain maps on the singular-OPE landscape). Repair instead: (1) State, as a named conditional proposition (the Hochschild-level analogue of prop:r-matrix-descent-vol1), the comparison between the intrinsic symmetric chiral Hochschild complex of def:chiral-hochschild-complex and the strong-unitary R-twisted Sigma_n-descent of the ordered complex, with hypothesis package YBE + strong unitarity R_12(z)R_21(-z)=id + the descent datum, recording that it reduces to plain Reynolds/coinvariant descent exactly on the pole-free commutative-chiral locus — in particular on gr_PBW(A) under E_infinity-completion, not on A itself. (2) Rewrite the proof of cor:hochschild-averaging-symmetric in the spectral-sequence lane that rem:sigma-inverse-chain-level says is available: the PBW/collision filtration is Sigma-stable; its associated graded is commutative-chiral, where the descent is plain coinvariants (cor:pole-free-descent) and localized residue-twisted bar concentration gives the symmetric E_1-page vanishing in fibre degrees >= 1; symmetric concentration in degrees >= 3 follows by convergence of the symmetric collision spectral sequence under the Mittag-Leffler/completeness conditions of rem:theorem-H-filter-exactness, which must be added explicitly to the corollary's hypothesis package. Delete the claim of a cochain-level null-homotopy on the un-graded ordered complex and delete (or restate as the gr-level statement actually proved) the equation ChirHoch^n(A) = (ChirHoch^{ord,n}(A))_{Sigma_n}. (3) In thm:mr-H (chapters/connections/master_reconstruction.tex:301-325), add the named ordered-to-symmetric descent comparison to the hypothesis package H_H rather than citing the averaging corollary as discharged. (4) Keep rem:hochschild-averaging-scope but ground "essential" in the actual mechanism: E_infinity-completion is what makes the associated graded pole-free so the R-twist trivialises on gr; without it neither a plain Sigma-action nor a Reynolds average exists on any page, and only the ordered bound survives (conj:hochschild-concentration-E1-only stands as stated).

---

## [theorem-H/H-11] major / vacuous / conf=high

CLAIM: Vacuousness of the hypothesis package (attack c): some nontrivial example satisfies the full Theorem-H package — PBW chiral Koszul + diagonal Hochschild complexes 'perfect in the holonomic D_X-module derived category' + finite-dimensional graded realizations + genericity + E_∞-completion + strict Mittag–Leffler — end to end

LOCATION: chapters/theory/chiral_hochschild_koszul.tex:2212-2277 (thm:main-koszul-hoch hypotheses), 1358-1455 (witness corollaries, all ClaimStatusConditional), 2142-2210 (rem:theorem-H-filter-exactness)

EVIDENCE: No witness is verified against the package: every example corollary (Heisenberg, affine sl_2, Virasoro, sharp Hilbert) and every link of the proof chain (shift lemma, totalization, fm-tower-collapse, quadratic transfer, homotopy transport, descent, main theorem, polynomial growth, averaging) carries ClaimStatusConditional; the only ProvedHere links (thm:hochschild-bar-cobar, thm:chiral-hochschild-differential) discharge their key steps in one sentence ('On the PBW Koszul locus the associated graded is the quadratic Koszul resolution, so the augmentation is a quasi-isomorphism'). Perfectness in the holonomic derived category is never checked for any example, and for V_k(g) the diagonal complex is built from non-holonomic infinite-rank D-modules, so the hypothesis can only be meant through the finite-window reduction, which is itself only sketched; rem:theorem-H-filter-exactness moreover lists as an 'exactness criterion' that 'positive Arnold fibre classes must be killed by the Shelton–Yuzvinsky homotopy' — i.e. the package quietly includes the conclusion of the broken mechanism (H-1) among its hypotheses, making the theorem true-by-hypothesis on its advertised locus.

REPAIR: Inscribe a package-assembly proposition for the Heisenberg pair (H_k, Sym^ch(V*)), k != 0, near the witness corollaries of chiral_hochschild_koszul.tex: (i) PBW flatness and chiral Koszulness — already ProvedHere (ex:heisenberg-koszul-pair, thm:km-chiral-koszul), which also discharges the E_infty-completion hypothesis since cor:hochschild-averaging-symmetric defines it as the same flat-PBW condition; (ii) NEW: in each finite conformal-weight window N, both diagonal chiral Hochschild complexes (for H_k and Sym^ch(V*)) are bounded complexes of O_X-coherent, hence holonomic, D_X-modules with finite-dimensional graded realizations — bar length is bounded by N because every generator has conformal weight >= 1 — so window perfectness in the holonomic derived category holds; (iii) NEW: the window tower has finite-dimensional terms in each degree, so the inverse system of cohomologies satisfies Mittag-Leffler automatically (decreasing images in finite-dimensional spaces stabilize), giving lambda^1_n(H_k) = 0; (iv) genericity k != 0. Cross-check the assembled window cohomology against the independent direct computation ex:HH-heisenberg-complete / cor:chirhoch-heisenberg (1,1,1), and add a compute/ test that computes a low-weight window cohomology matrix directly rather than hardcoding the table. Simultaneously rectify rem:theorem-H-filter-exactness: replace "On the generic PBW finite-type lanes these four terms vanish by the preceding lemmas" with per-criterion attribution — Arnold-killing: lem:chiral-homotopy-transport / thm:hochschild-concentration-E1 (Conditional); d_{r>=2}-vanishing: prop:fm-tower-collapse Step 7 (Conditional); lambda^1_n and perfectness cone: discharged for the Heisenberg by the new proposition, open for the other archetypes. Align theorem_h_hochschild_polynomial.py status fields ('PROVED') with the tex Conditional tags. Upgrade cor:chirhoch-heisenberg off Conditional only when the assembly proposition closes; if it does not close, adopt the auditor's fallback and state explicitly that the Theorem-H locus is not yet shown to contain any of the five archetypes.

---

## [foundations-master/A-1] fatal / misattributed / conf=high

CLAIM: thm:mr-morita (ClaimStatusProvedHere): 'Lurie's Morita theorem in the factorization context (Francis--Gaitsgory, [S4.2]{Francis2012}; promoted to (infinity,2) by [Chapter IV.5]{GR17})' proves that C^op -> A_b-mod^fact is an equivalence of factorization (infinity,1)-categories

LOCATION: chapters/connections/master_reconstruction.tex:213-241

EVIDENCE: Verified against the sources: FG12 (arXiv:1103.5803, TOC fetched) Section 4.2 is 'Coalgebras vs. ind-nilpotent coalgebras in the pro-nilpotent case' inside Section 4 'Koszul duality in nilpotent tensor infinity-categories'; the paper concerns factorization ALGEBRAS (abstract: 'We prove the equivalence of higher-dimensional chiral and factorization algebras... as a chiral form of Koszul duality') and contains no Morita theory and no factorization categories beyond a passing remark in 1.1.1. GR17 Chapter IV.5 (nLab TOC) is 'Infinitesimal differential geometry' in Part IV 'Formal Geometry'; GR17 contains no factorization-category material at all. Additionally hypothesis package H_0 (lines 229-233) is type-inconsistent: 'C^op is small, idempotent complete, and dualizable in the Lurie symmetric-monoidal infinity-cat of factorization presentable stable categories' - a presentable stable category is never small, and compact generation is a property of presentable categories. A theorem tagged ProvedHere whose entire proof is two citations that verifiably do not contain the result is status inflation of the worst kind.

REPAIR: In chapters/connections/master_reconstruction.tex:213-241: (i) Retag thm:mr-morita from \ClaimStatusProvedHere to \ClaimStatusConditional, aligning with its four sibling reconstruction theorems. (ii) Rewrite the proof in two layers. Pointwise layer (citable): for a presentable stable ∞-category with compact generator b, Hom(b,−): C → RMod_{End(b)} is an equivalence — cite Lurie, Higher Algebra, Theorem 7.1.2.1 (Schwede–Shipley recognition) and Schwede–Shipley 2003. Factorization layer (the actual content, currently unproved): state as the explicit named residual of H_0 a "factorization-Morita assembly" hypothesis — b carries a factorization-unit (vacuum) structure over Ran(X,D,τ) making End(b) a factorization algebra; b is a compact generator on each finite Ran stratum; the stratumwise Schwede–Shipley equivalences are natural and satisfy Beck–Chevalley over the disjoint-union arrows, assembling to an equivalence of factorization categories C^op ≃ A_b-mod^fact. If a framework citation is wanted, cite Raskin "Chiral categories" for factorization categories — not FG12. (iii) Delete \cite[§4.2]{Francis2012} (Koszul duality for coalgebras in pro-nilpotent tensor ∞-categories — unrelated) and \cite[Chapter IV.5]{GR17} (infinitesimal differential geometry — unrelated); drop the "(∞,2)-promotion" claim entirely (no (∞,2) factorization Morita theorem exists in GR17). (iv) Fix H_0 to be type-consistent and aligned with conv:master-reconstruction-tower: "C^op is a compactly generated presentable stable factorization category on (X,D,τ) (equivalently Ind of a small idempotent-complete stable factorization category); b is a compact generator carrying the factorization-unit structure" — delete "small", delete the phantom "Morita-generating in the sense of Francis–Gaitsgory", and delete the false closing sentence "Compact generation, idempotent completion, and dualizability are exactly the hypotheses needed" (idempotent completeness is automatic, dualizability is implied by compact generation in Pr^L_st). (v) No change needed in thm:mr-master (already Conditional) or the master_concordance row (already "presentable + compact generator"); both become consistent once H_0 is repaired.

---

## [foundations-master/A-2] fatal / vacuous / conf=high

CLAIM: Level 0 of the open Beilinson tower: 'C^op is a factorization dg-category on (X,D,tau) in the Francis--Gaitsgory sense, equipped with its Verdier-symmetric monoidal structure on Ran(X,D,tau)' is the primitive object from which the chart algebra A_b = End_C(b) is derived

LOCATION: chapters/connections/master_reconstruction.tex:86-92 (def:mr-open-datum slot 4); cf. chapters/examples/yangians_drinfeld_kohno.tex:527-549

EVIDENCE: (1) No definition of 'factorization dg-category on (X,D,tau)' exists anywhere in the repo (exhaustive grep over chapters/ and appendices/): the only definition resembling one is def:e1-factorization-category (yangians_drinfeld_kohno.tex:527), which takes an E1-chiral algebra A as INPUT ('For an E1-chiral algebra A on a curve X, the E1-factorization category Fact_E1(A) consists of: Objects: A-modules on ordered configuration spaces...') with no descent data, no D-module structure, no Weiss/Ran gluing axioms. (2) 'Ran(X,D,tau)' occurs exactly twice in the corpus (master_reconstruction.tex:88, vertical_equivalence_level_0.tex:52) and is never constructed; the Ran space actually defined (configuration_spaces.tex:5556, def:ran-space-complete) is the plain Ran(M) of a topological space with no divisor or tangential structure. (3) 'Verdier-symmetric monoidal structure' is never defined (4 grep hits, all usages). (4) FG12 does not define factorization categories (verified TOC; that notion is Raskin's unpublished 'Chiral categories'). (5) For none of the five archetypes G/L/C/M/B is a category C^op with vacuum b exhibited such that End(b) returns the algebra: Part I (fourier_seed.tex, algebraic_foundations.tex) starts every computation from the OPE of a given chiral algebra. The only available instantiation is C^op := A-mod, b := A, End(A) = A, which makes the Morita theorem a tautology and level 0 decorative.

REPAIR: Three-part repair, using the corpus's own Vol II material rather than inventing Raskin-style machinery from scratch (refines the auditor's option (a); option (b) is unnecessary and would violate the repo's MA-2 constitution). (1) DEFINE THE NOTION IN VOL I: in def:mr-open-datum slot 4 (master_reconstruction.tex:86-88) and vertical_equivalence_level_0.tex:49-54, delete "in the Francis--Gaitsgory sense, equipped with its Verdier-symmetric monoidal structure on Ran(X,D,tau)" and restate, in Vol I Part I, the Vol II definition def:oc-factorization-category (chiral-bar-cobar-vol2/chapters/theory/foundations.tex:1020): a constructible dg-cosheaf of dg-categories on the mixed Ran space Ran^oc(X,D,tau) with factorization equivalences, holomorphic locality, boundary local constancy, local SC^{ch,top} model, and clutching compatibility -- together with the mixed-Ran construction (Vol II def:bordified-curve, def:mixed-config), so Vol I is self-complete. Cite FG12 only for the D-empty closed sector (factorization algebras); add a bibliography entry for Raskin, "Chiral categories" (unpublished notes), as the source for category-valued factorization objects; delete "Verdier-symmetric monoidal" everywhere or define it at first use. Replace the dangling phantom anchor subsec:thqg-open-sector-factorization-category (main.tex:2809) with a real subsection containing this definition. (2) FIX THE MORITA THEOREM: in thm:mr-morita (master_reconstruction.tex:213-241), excise the citations [FG12 \S4.2] and [GR17 Chapter IV.5]; restate the theorem as: stratumwise on Ran^oc, reconstruction from a compact generator is Lurie HA \S4.8 / Schwede--Shipley Morita theory; compatibility of the Morita equivalence with the factorization cosheaf structure (so that C^op = A_b-mod^fact as factorization categories and End(b) inherits the chiral structure on (X,D,tau)) is a named clause of hypothesis package H_0, currently discharged only stratumwise; retag \ClaimStatusConditional. (3) POPULATE LEVEL 0 WITH ONE WITNESS AND NAME THE CIRCULARITY: import into Vol I the Vol II benchmark def:benchmark-Cop-sl2 (archetype L: C_op(V_k(sl_2)) on (P^1,{0,infty},tau), generating objects the Weyl modules, End of the vacuum module = V_k(sl_2)), stating explicitly that every witness currently available is constructed from its chart algebra, so the primitivity of C^op over A_b is an architectural normalisation (a Morita-invariance statement) proved only up to the factorization-Morita clause of H_0; record this caveat in conv:master-primitive-datum (master_concordance.tex:94-101) and in the genus_complete/holographic chapters that repeat the slogan "C^op is the primitive open object".

---

## [foundations-master/A-3] major / misattributed / conf=high

CLAIM: prop:fg-ambient-properties (ClaimStatusProvedElsewhere): 'Fact(X) is stable, presentable, symmetric monoidal at the (infinity,2)-level', with proof-by-references: 'passing to factorization algebras preserves both properties ([Chapter IV.5, S1.3]{GR17}). Symmetric monoidal structure under star is [S4.2]{Francis2012}; units are [S4.3]{Francis2012}. The (infinity,2)-enhancement is [Chapter IV.5, Theorem 3.1.2]{GR17}'

LOCATION: chapters/theory/theorem_A_infinity_2.tex:1325-1342; same citation pattern at lines 223, 2278 ('in place of Val16') and in the proof of thm:koszul-reflection at 396-415

EVIDENCE: GR17 IV.5 is 'Infinitesimal differential geometry' (Lie algebroids, infinitesimal neighborhoods) - GR17 contains no factorization algebras anywhere, so 'IV.5 S1.3' and 'IV.5 Theorem 3.1.2' cannot contain factorization-ambient statements; the (infinity,2) material in GR17 is Appendix Part A. FG12's symmetric monoidal structures on D(Ran X) are Section 2.2 ('Symmetric monoidal structures on D(Ran X)'), not 4.2; 4.3 is 'The case of Lie algebras', not units. This proposition is the ambient pillar invoked by the proof of Theorem A (thm:koszul-reflection) for its (infinity,2)-promotion, so the citation rot is load-bearing: the proposition is ProvedElsewhere with an 'elsewhere' that does not exist.

REPAIR: Re-source prop:fg-ambient-properties (theorem_A_infinity_2.tex:1325-1343) clause by clause, with honest claim-status splits: (1) stability/presentability of D(Ran X): FG12 S2.1 (D(Ran X) as a limit of D(X^I) along !-pullbacks) plus GR17 Vol I Chapter I.1 (DGCat_cont closed under limits) -- not 'GR17 IV.5 S1.3'; (2) the star and chiral symmetric monoidal structures: FG12 S2.2 ('Symmetric monoidal structures on D(Ran X)') with explicit description in S2.3, stating that these live on D(Ran X) and that the induced monoidal structure on Fact(X) itself is a separate statement sourced from Raskin 'Chiral categories' (categorical/unital level) or BD04 S3.4; (3) units: NOT FG12 (whose commutative coalgebras and chiral structure are non-unital) -- cite Raskin 'Chiral categories' for unital factorization, and delete the garbled 'two units coincide after sheafification' clause or prove it; (4) the (infinity,2)-enhancement: no published source exists -- downgrade from ClaimStatusProvedElsewhere to ClaimStatusProvedHere with an actual proof (e.g. via the Hackney-Robertson properadic machinery already in the chapter, GR17's general (infinity,2)-toolkit being only Vol I Appendix A.1-A.3) or to ClaimStatusConjectured with the proof obligation named. Then purge the phantom 'GR17 Chapter IV.5' citations repo-wide: theorem_A_infinity_2.tex lines 223, 403, 1264, 1338-1342, 1560, 1777, 2246, 2278, 2475; bar_cobar_adjunction_curved.tex 6520, 6550, 6648; chiral_koszul_pairs.tex 5540, 6925; master_reconstruction.tex 239. Where the intended content is the (infinity,1) bar-cobar equivalence in the chiral setting, the real source is FG12 S3.3-3.4 (Koszul duality functors; turning Koszul duality into an equivalence) + S4.1 (pro-nilpotence) + Theorems 5.1.x/5.2.x (labels t:Koszul, t:factorization; stated for the Lie/Com pair, so the chirAss-operad form still needs the abstract S3.3-3.4 machinery plus an in-manuscript argument). Where the intended content is a 'model structure on factorization coalgebras', delete the attribution entirely -- no such theorem exists in any published source (GR17 is model-independent; Val16 is over a field) -- and rewrite rem:ainf2-heal-72: its 'replacement' of Val16 by GR17 IV.5 Theorem 3.1.2 must itself be retracted, either restoring Val16 with its field hypothesis explicit at the pole-free point, or restating the step infinity-categorically via FG12 S4 where no model structure is needed. Also fix the rem:ainf2-hziv machinery list item 'Gaitsgory-Rozenblyum factorization infinity-category and model structure' and the phantom cite[Proposition 3.1]{Francis2012} at line 1562 (the twisting-morphism dictionary is FG12 S3.3, items numbered x.y.z). Finally, re-audit the downstream uses: thm:koszul-reflection's (infinity,2)-promotion and the L2 lane now rest on whatever status the rebuilt proposition carries, so their ClaimStatus tags must be made consistent (Conditional until the (infinity,2)-enhancement is proved in-manuscript).

---

## [foundations-master/A-4] major / false / conf=high

CLAIM: prop:fourier-genus1-propagator: eta^(1)_ij = dlog theta1(z_i - z_j | tau) + (2 pi i/Im tau) Im(z_i - z_j) dzbar_i, with proof asserting 'The correction term ... compensates this monodromy, making eta^(1)_ij single-valued'

LOCATION: chapters/theory/fourier_seed.tex:117-179; second inconsistent variant at chapters/theory/configuration_spaces.tex:4022-4028

EVIDENCE: Numerically verified (mpmath, 30 digits): dlog theta1 has B-cycle monodromy -2 pi i (du) where du = dz_i - dz_j, i.e. the deficit lives on the basis form dz_i - dz_j; the manuscript's correction changes by +2 pi i dzbar_i under z_i -> z_i + tau, which lives on dzbar_i and cannot cancel a deficit on dz_i - dz_j. The correct doubly periodic propagator is [d/du log theta1(u) + 2 pi i Im(u)/Im(tau)](dz_i - dz_j) (verified to machine precision to have zero monodromy under u -> u+1 and u -> u+tau). The correction must be of type (1,0) with a non-holomorphic coefficient, not a (0,1)-form; the manuscript's form is also not antisymmetric under i <-> j. configuration_spaces.tex:4025 gives a SECOND, different formula: dlog theta1((z_i-z_j)/(2 pi i); tau) + (pi/Im tau) d(conj(z_i - z_j)) - whose correction is translation-invariant (zero monodromy, so cancels nothing) and whose theta-argument rescaling (z_i-z_j)/(2 pi i) is incompatible with the lattice Z + tau Z. The downstream cohomological statement [A^(1)_123] = 2 pi i [omega_tau] (Arnold failure = Arakelov class) plausibly survives with the corrected propagator, but both explicit formulas as printed are wrong and mutually inconsistent.

REPAIR: Replace all THREE occurrences (not two) with the single convention eta^(1)_ij = [partial_u log theta1(u|tau) + 2 pi i Im(u)/Im(tau)]|_{u = z_i - z_j} (dz_i - dz_j), i.e. coefficient g^(1)(u) — doubly periodic, odd, simple pole of residue 1 at u = 0 (the standard Brown-Levin / eMZV g^(1) and the (1,0)-part of the one-loop string Green function) — times du_ij = dz_i - dz_j, restoring eta^(1)_ji = eta^(1)_ij in line with the genus-0 convention. Site (a) chapters/theory/fourier_seed.tex:123-127: replace the display; rewrite the proof's first paragraph (lines 150-160) to say the B-cycle deficit is -2 pi i (dz_i - dz_j), a (1,0)-form, so the compensator must be the (1,0)-form 2 pi i [Im(z_i-z_j)/Im tau] (dz_i - dz_j) with non-holomorphic coefficient — a (0,1)-form cannot cancel a (1,0) deficit; keep the Arakelov paragraph and record d eta^(1)_ij = 2 pi i (delta_{D_ij} - q_ij^* omega_tau), q_ij(z) = z_i - z_j, which yields [A^(1)_123] = 2 pi i [omega_tau] unchanged. Site (b) chapters/theory/higher_genus_foundations.tex:3247-3252: same replacement in the genus-1 display of def:higher-genus-log-forms; in the proof of thm:arnold-higher-genus at 3357-3363, replace the dzbar_i term by the corrected (1,0) term, delete 'with residue one on the diagonal' for the correction (the residue comes from the theta quotient; the correction is regular), and fix 'Its dbar is the normalized volume form' to: the dbar of its coefficient wedged with du equals -2 pi i times the unit-mass volume form omega_tau pulled back along the difference map. Site (c) chapters/theory/configuration_spaces.tex:4022-4028: replace the display with the same formula with theta-argument z_i - z_j itself (no /(2 pi i) rescaling — the section's lattice is Lambda_tau = Z + tau Z, line 3990) and correction 2 pi i [Im(z_i - z_j)/Im tau] d(z_i - z_j); amend the trailing sentences of prop:elliptic-arnold-relations (lines 4048-4052): the non-holomorphic piece is a (1,0)-form with real-analytic coefficient, and the (1,1) period term in the cyclic wedge arises from dbar of that coefficient via d eta^(1) = 2 pi i (delta_Delta - omega_tau), not from a '(pi/Im tau) dzbar' regularization. Optionally, per the repo's 3-path discipline, add a compute test (mpmath) checking double periodicity of g^(1) under u -> u+1 and u -> u+tau, residue 1 at u = 0, and the smooth part of d eta equal to -2 pi i omega_tau.

---

## [foundations-master/A-5] major / unproven-as-stated / conf=high

CLAIM: thm:modular-mc-clutching: the proof derives the boxed equation d Theta + (1/2)[Theta,Theta]^oc + hbar Delta_clutch(Theta) = 0 from Stokes' theorem on the bordered FM compactification, assembling '0 = int_{partial sigma} omega = (Type I+II+III) + Type IV(a) + Type IV(b)'

LOCATION: chapters/theory/configuration_spaces.tex:3171-3464, esp. 3351-3359 vs 3426-3451

EVIDENCE: The proof's own parenthetical concedes the Type IV faces do not exist on the stated domain: '(Note: the Type IV faces arise from the genus-graded modular structure of the bar differential: they record nodal degenerations of the underlying curve, not collisions of marked points on a fixed curve. The fixed-curve Stokes argument on C-bar^oc_{k,m} produces Types I--III; the Type IV contribution enters through the moduli variation encoded in the genus summation ... and the modular operad algebra structure)' (3351-3359). Yet the Assembly step (3426-3451) writes 0 = int_{partial sigma} omega = (I+II+III) + IV(a) + IV(b) for sigma a chain in the FIXED-curve compactification C-bar^oc_{k,m}(X,D,tau), summing over boundary faces that are absent from partial sigma. The bracket and clutching terms are therefore imported from thm:bar-modular-operad, not derived by the Stokes argument the proof presents. The theorem is honestly tagged Conditional, but the proof body misrepresents its own logic, and this is the central Maurer-Cartan equation of the framing (CLAUDE.md's 'one equation').

REPAIR: Restructure the proof of thm:modular-mc-clutching (configuration_spaces.tex:3220-3464) as a two-source derivation, and delete the false assembly identity. (a) Replace the Assembly step (3426-3451): remove eq:stokes-assembly's claim that 0 = int_{partial sigma} omega = (I+II+III)+IV(a)+IV(b) follows from Stokes on C-bar^oc_{k,m}. State instead: (Source 1, geometric) the fixed-curve Stokes/residue argument on C-bar^oc_{k,m}(X,D,tau) — whose codimension-one boundary consists of Types I-III only (cite rem:comparison-classical-fm) — realizes the within-genus terms (d_int + d_bdy + d_mix)Theta as face integrals; (Source 2, algebraic) the boxed equation is the component expansion of (D^oc_A)^2 = 0 for the genus-completed open-closed differential D^oc_A = d_0 + Theta_A, where the separating-edge part of the Getzler-Kapranov decomposition eq:gk-decomposition gives (1/2)[Theta,Theta]^oc and the non-separating part gives hbar Delta_clutch(Theta), exactly parallel to thm:mc2-bar-intrinsic(i) and cor:recovery-bar-intrinsic. The square-zero property is thm:bar-modular-operad(iii) in the closed sector (ProvedHere, via the partial^2 = 0 stratification of Mbar_{g,n}); its open-closed extension (the FCom^oc-algebra structure invoked in def:modular-twisting-morphism-oc) is a named hypothesis of the Conditional status. The Type IV(a)/(b) labels refer to genuine boundary divisors only of the relative bordered FM compactification over Mbar_{g,r} (cite thm:normal-crossings-preservation), not of the fixed-curve space. (b) Rewrite the section opening 2867-2877, which repeats the overstatement that 'the MC element and the equation itself follow from Stokes' theorem on the four-type boundary'. (c) Scope prop:four-type-boundary / constr:bordered-fm: state eq:boundary-four-types as the decomposition for the relative family over Mbar_{g,r}, with the fixed-curve boundary being Types I-III (the proposition's Type IV paragraph and rem:comparison-classical-fm already say this); remove D_Gamma^nod from the fixed-curve blowup list eq:bordered-fm-result or qualify it as the relative case. (d) Retain ClaimStatusConditional, and name the outstanding geometric proof obligation explicitly: constructing the relative open-closed bordered FM compactification over Mbar_{g,r} and proving the moduli-direction closedness (or controlled non-closedness) of the amplitude form, which is what a single unified Stokes derivation of all four types would require. (e) Close the unclosed parenthesis of the '(Note: ...' parenthetical at 3351-3359.

---

## [foundations-master/A-6] major / false / conf=high

CLAIM: thm:mr-bourbaki (Master Reconstruction as Bourbaki structure): '(3) the typical structure is recovered from any one of its five projections via the corresponding reconstruction theorem; (4) the structure is rigid ... an endomorphism inducing the identity on any one level is the identity on every level'

LOCATION: chapters/connections/master_reconstruction.tex:817-858

EVIDENCE: (4) Counterexample to rigidity: the automorphism alpha -> -alpha of the Heisenberg chart algebra H_k (an admissible morphism of OpenDatum: it fixes the vacuum and stress tensor T = (1/2):aa:, intertwines Theta by naturality and Tr by invariance of the character) induces the identity on level 5 - the scalars (kappa, Z, F_g) are invariants, so EVERY automorphism induces the identity there - but is not the identity on level 1 (acts by -1 on A_b) or level 4 (Fock(lambda) -> Fock(-lambda)). The proof's mechanism ('an endomorphism ... acting as the identity at any level acts as the identity on the universal MC element') has no content at level 5: scalars do not detect Theta. (3) From level 3 no reconstruction theorem exists even conditionally: thm:mr-H is a CONCENTRATION statement ('F_2 on the Koszul locus has image concentrated in {0,1,2}' per M1, lines 435-436), not a recovery of level <= 2 data; and the derived centre is a Morita invariant, so it cannot determine the chart algebra beyond Morita class - the manuscript's own five-object firewall (rem:mr-five-objects) forbids the identification that recovery from level 3 would require.

REPAIR: In thm:mr-bourbaki (master_reconstruction.tex:817-858): (a) Replace clause (3) by the proven recovery pattern: the datum is recovered from its level-1 projection (Morita, thm:mr-morita, given b) or its level-2 projection (cobar inversion K^2 ~ id on Kosz, thm:mr-A); the descending reconstructions 5->4 (thm:mr-modular, up to Morita equivalence of the line category, and consuming the trace-plus-clutching system, which strictly exceeds the bare scalar tuple (kappa, Z, F_g)) and 4->3 (thm:mr-drinfeld-double, under H_4) terminate at level 3; 1->3 (thm:mr-H) is formation-with-concentration, not reconstruction. State the missing 3->2 link as a named open reconstruction problem: the derived centre is chart-independent (slot (7) of def:mr-open-datum), so the level-3 projection determines A_b at most up to Morita class. (b) Replace clause (4) by: rigidity holds from levels 0, 1, 2 — an endomorphism inducing the identity on C^op (fixing b), on A_b, or on B(A_b) is the identity at every level (downward functoriality; at level 2, corestriction of B(phi) = T^c(s^{-1} phibar) to the cogenerator piece gives phibar = id, hence phi = id). Levels 3, 4, 5 are non-faithful: every admissible endomorphism intertwines Theta and Tr by clause (2), hence induces the identity on the level-5 scalars; witnesses on KSDual: alpha -> -alpha on H_k (identity at level 5, -1 at level 1, Fock(lambda) -> Fock(-lambda) at level 4) and Aut(V_{Lambda_24}); level-4 rigidity holds at most up to inner (Skolem-Noether) ambiguity; cite lem:master-scalar-non-faithfulness and the heterotic c=16 witness thm:master-scalar-nonfaithful-witness-c16 (V_{E8+E8} vs V_{D16+}: equal (c, chi, F_g on curve moduli), non-isomorphic), which refutes level-5 recovery outright. (c) In the proof, delete the appeal to M2 for rigidity-from-any-level: M2 states that Theta_C projects onto each level, not that a level-n identity action lifts to the identity on Theta_C; the MC mechanism is faithful only at levels 1-2 where the binary collision residue lives. (d) Rewrite the closing sentence as: well-defined, recoverable from its chart-side projections (levels 0-2) with conditional descending reconstructions 5->4->3, and rigid from levels 0-2.

---

## [foundations-master/A-7] major / false / conf=high

CLAIM: KSDual layer: def:mr-ksdual defines KSDual = {A in Kosz : sigma(A) ~ A} with sigma: A -> A^!; rem:mr-ksdual-witnesses lists 'Heisenberg H_k with curved Sym^ch(V*): kappa+kappa^! = 0' and 'beta-gamma_lambda with bc_lambda: kappa+kappa^! = 0' as KSDual witnesses; thm:mr-ksdual claims on KSDual 'Hochschild concentration is exact in {0,1,2}' and 'the five-archetype dichotomy stabilises'

LOCATION: chapters/connections/master_reconstruction.tex:514-609; contradicted by chapters/connections/master_concordance.tex:2197-2253 and chapters/theory/fourier_seed.tex:396-405

EVIDENCE: Three documented internal contradictions. (i) The witnesses are sigma-ORBIT PAIRS, not fixed points: sigma(beta-gamma) = bc != beta-gamma, and master_concordance's own table (rem:ksdual-fixed-points-bucket) says class C 'beta-gamma_lambda <-> bc_lambda: cousin family - no intrinsic fixed point'. The witness criterion used (kappa + kappa^! = 0) contradicts the definition's own consequence five lines earlier ('On A_b in KSDual, kappa(A_b)+kappa(A_b^!) collapse to TWICE THE SELF-DUAL CEILING' = 2 kappa(A_b)): for H_k these give 0 vs 2k, consistent only at the degenerate k = 0 (the trivial algebra, per the concordance: 'the rank-one vacuum Heisenberg H_0 is the trivial chiral algebra'). (ii) The concordance's G-row 'level shift k -> -k' contradicts fourier_seed rem:fourier-heisenberg-not-selfdual: 'H_k^! = (Sym^ch(V*), m0 = -k omega), NOT H_{-k} ... not a Heisenberg algebra' - the scalar kappa-flip is being mistaken for an algebra-level involution, the repo's own MA-1 pattern (shadow = object); sigma does not even preserve the uncurved category, so the Z/2-action needs the curved ambient to typecheck, which def:mr-ksdual does not name, and the lead-in assertion 'A^{!!} ~ A on the standard landscape' (line 515-516) is bare prose. (iii) The unique class-L fixed point is the critical level k = -h^v, where the concordance itself says 'Theorem H is excluded at this point' and N(L) = 2(k+h^v) = 0 - so thm:mr-ksdual(i) (exact concentration on KSDual) is false there if critical is in Kosz, vacuous if not. Net effect: KSDual-with-all-claimed-properties = {trivial algebra, Vir_{c=13}, W3/BP at imaginary shifted level k+3 = +-2i, V_Lambda24, Mukai-K3}; the 'five-archetype dichotomy stabilises on KSDual' slogan has no nondegenerate G witness, no L witness, no C witness at all.

REPAIR: Four edits to /Users/raeez/chiral-bar-cobar/chapters/connections/master_reconstruction.tex:514-609. (1) Definition: replace the bare lead-in 'A^{!!} ~ A on the standard landscape' with the finite-type statement, citing the finite-type Koszul involutivity theorem (thm:universal-defect-construction, poincare_duality_quantum.tex:285-287) and naming the finite-type hypothesis. In def:mr-ksdual, name the ambient so sigma typechecks: sigma: A -> A^! lands in the curved weight-completed finite-type category (prop:fourier-five-duality-objects), and KSDual := {A in Kosz : A^! is again augmented uncurved and A^! ~ A in Kosz} — equivalently the Z/2-fixed locus computed in the curved ambient and intersected with Kosz. (2) Witness remark: delete the H_k and beta-gamma/bc bullets as KSDual witnesses and delete kappa+kappa^! = 0 as a membership criterion (it is the constant Verdier-sum of the whole G/L/C sigma-orbit families — the anti-diagonal kappa^! = -kappa — meeting the fixed-point diagonal kappa^! = kappa only at the degenerate kappa = 0; the fixed-point value is 2*kappa, per def:mr-ksdual's own consequence). Re-inscribe those two items as sigma-ORBIT pairs whose KSDual intersection is: G only at the degenerate vacuum k = 0 (scalar-level fixed point; algebra-level sigma-fixedness not established, since H_k^! is the curved Sym^ch(V*), rem:fourier-heisenberg-not-selfdual), C empty (cousin family, rem:ksdual-fixed-points-bucket). (3) Import the concordance fixed-point table CONTENT (G: k=0 degenerate; L: k=-h^v critical, excluded by H_3; C: none; M: c=13, 50, 98 with the real-vs-complex level caveat; B: Mukai-self-dual) but explicitly qualified as the scalar kappa-involution fixed locus, citing poincare_duality_quantum.tex:313-336 that the Feigin-Frenkel shift and Koszul duality are distinct operations whose scalar agreement does not identify the algebras; assert algebra-level sigma-fixedness only where inscribed (V_Lambda24 lattice self-duality, Mukai-K3 B-row) and for the M fixed points only along the analytically continued family as the existing closing paragraph already does. (4) Theorem thm:mr-ksdual: add the scope sentence that H_3's genericity hypothesis excludes the critical-level point, hence KSDual meets archetype L in the empty set under the theorem's own hypotheses; restate (ii) honestly — on the admissible locus the surviving archetypes are M (c=13 in the weight-completed ambient; W3/BP on the analytic family), B, and the lattice point, with G only at the degenerate vacuum — and rectify the 'five-archetype dichotomy stabilises' framing here and in the corresponding CLAUDE.md/KSDual slogans to 'the archetype label is rigid on KSDual, whose nondegenerate points realise only the M and B archetypes'.

---

## [foundations-master/A-8] major / status-inflation / conf=high

CLAIM: Status of the corollary layer: cor:mr-B 'ProvedHere on Koszul locus', cor:mr-C 'ProvedHere on Koszul locus', cor:mr-D 'ProvedHere', cor:mr-H 'ProvedHere'; and the prose layer asserts 'The Master Reconstruction Theorem ... subsumes Theorems A through H as corollaries' in the indicative

LOCATION: chapters/connections/master_reconstruction.tex:749-805; chapters/theory/introduction.tex:2178-2180; FRONTIER.md:26-28; chapters/connections/master_concordance.tex:209-215

EVIDENCE: cor:mr-H (line 795-797, ProvedHere) states the same concentration claim as thm:mr-H (line 281-283), which is tagged ClaimStatusConditional 500 lines earlier in the SAME FILE with a six-condition hypothesis package (PBW, perfectness, genericity, E-infinity completion, strict Mittag-Leffler). cor:mr-D (line 779-781, ProvedHere) rests on thm:genus-universality, tagged ClaimStatusConditional at higher_genus_foundations.tex:7340. cor:mr-B (line 749-752, ProvedHere) rests on thm:bar-cobar-inversion-qi, tagged ClaimStatusConditional at bar_cobar_adjunction_inversion.tex:1724. Meanwhile the chapter abstract (lines 52-56), the introduction, FRONTIER.md, and the concordance all state 'Theorems A, B, C, D, H are corollaries' / 'subsumes Theorems A through H as corollaries' with no conditional qualifier. The theorem layer's Conditional discipline is real; the corollary and prose layers leak it away.

REPAIR: (1) cor:mr-H (master_reconstruction.tex:795-796): retag \ClaimStatusConditional, matching thm:mr-H (line 283), thm:main-koszul-hoch, and cor:hochschild-averaging-symmetric; its scope phrase "on the Koszul / PBW locus" claims strictly less than package H_3 (which adds perfectness, genericity, E_infinity-completion, strict Mittag-Leffler), and thm:mr-H states that on the bare PBW locus only the Koszul-defect complex is obtained. (2) cor:mr-B (lines 749-751): retag \ClaimStatusConditional, or split explicitly: ProvedHere on the genus-0 strict FTM surface and for class M in the weight-completed/pro-conilpotent ambient; the all-genera Koszul-locus inversion is conditional on the modular pre-Koszul package MK1-MK3 of thm:higher-genus-inversion (ClaimStatusConditional, higher_genus_complementarity.tex:4927), with locus membership proved for the standard landscape by thm:pbw-allgenera-*. (3) cor:mr-D: KEEP ProvedHere but expand the qualifier to "on the uniform-weight scalar-diagonal lane (Definition def:scalar-diagonal-hypothesis, Proposition prop:scalar-obstruction-hodge-euler)" -- do NOT downgrade to a g=1 sub-statement as the auditor proposed: the lane identity is ProvedHere for all g>=1 via the GRR/Chern-Weil route. Separately fix the slip "lambda_g in H^2(Mbar_{g,n})" to H^{2g} (lambda_g is the top Chern class of the rank-g Hodge bundle). (4) cor:mr-C: no retag needed; the corollary claims only the C0/C1 family-stratum scalar reading, which is the proved scope; optionally add "(scalar C0/C1 reading; the C2 shifted-symplectic/BV upgrade remains conditional on the BV package)". (5) Prose layer (introduction.tex:2178-2180, FRONTIER.md:28-29, master_concordance.tex:214-215, and the chapter abstract lines 54-56): append one clause, e.g. "subsumes Theorems A through H as corollaries, each scoped by its hypothesis package (H_1, H_3, H_4, H_5)" -- the structural subsumption claim is legitimate (the MRT itself is tagged Conditional), but the packages must stay visible at the summary layer per the repo's own suppress-no-hypothesis rule.

---

## REGION theorem-H: core_claim_survives=no

Theorem H does not survive as proven mathematics; it should be a conjecture with one named missing lemma. The unique mechanism claimed to force concentration — a 'Shelton–Yuzvinsky contracting homotopy' h_m on the Orlik–Solomon algebra satisfying dh_m+h_md=id−π_0 — is mathematically false as stated: OS(A_{m-1})=H^*(FM_m(C)) has zero differential and nonzero positive-degree cohomology (Poincaré polynomial ∏(1+jt), quoted in the same proposition and reverified here), so no such homotopy exists; Koszulness of an algebra contracts its Koszul complex OS⊗(OS^!)^∨, never OS itself. The transport lemma further treats the chiral bar differential as σ(d⊗id_{A^⊗m})σ^{-1}, i.e. never touching the algebra slots, which is false for any bar differential. Second, the concentration is proved (to the extent it is) for the bigraded object RHom_D(A^{⊠(p+2)},ω)[−p] — a Verdier-dual-of-bar object whose [−p] regrading manufactures the amplitude — while the deformation-theoretic ChirHoch=Ext_{A^e}(A,A) (the object carrying the MC-moduli, witness, and derived-centre-=-bulk interpretations) has its own grading in which no concentration is established and in whose ordinary-algebra shadow concentration is false (HH of Koszul algebras is generically unbounded); the bridge (lem:chirhoch-descent) asserts the HH^*≅(HH_*)^∨-type identification in one unconstructed sentence. Third, the old flagship affine adjoint-H1 witness counts coboundaries as cohomology: by the chapter's own inner-derivation operator (the zero mode a_(0), line 7125), the adjoint cochains are inner via (J^a)_(0), and the proof never quotients by them; the claimed three-term diagonal Koszul resolution contradicts the manuscript's own (correct, here recomputed) dim(A^i)_2=5 for affine sl_2. Fourth, the 'verified by the chiral Hochschild engine for N=2..10' claims are hardcoded lookup tables (return 1; return dim g; inner_derivations=0), so the repo's 3-path verification rule is satisfied only notionally. Fifth, no advertised example is verified against the full hypothesis package (PBW+perfectness+genericity+E_∞-completion+strict ML): every witness corollary is tagged Conditional, and the Heisenberg witness data is internally contradictory (dim ChirHoch^2=1 vs ChirHoch^2≅Z(Sym^ch(V^*))^∨⊗ω with Z of a commutative chiral algebra infinite-dimensional). The statement itself is not refuted — no ChirHoch^3≠0 counterexample is exhibited, the SS bookkeeping is locally sound given its hypotheses, the register discipline (chiral vs THH vs categorical) is maintained at the label level, and the critical-level exclusion is consistently enforced — but the proof, the witnesses, and the verification apparatus all fail, and the honest repair is a downgrade to conjecture pending a twisted-Koszul-complex acyclicity lemma on the E_1 page plus corrected witness computations.

---

## REGION foundations-master: core_claim_survives=yes-with-repairs

The Part-I genus-0 chain-level mathematics is largely sound: the Arnold relation proof is correct (verified by direct computation), the manuscript honestly acknowledges that the Arnold relation fails at genus >= 1 (contrary to what CLAUDE.md's slogan suggests), the scalar tables (kappa complementarity K^kappa(Vir)=13, N(A) witness values, kappa(V_Lambda24)=24) are internally consistent, and the modular convolution dGLA and MC element Theta are constructed rather than postulated. The framing layer above it does not survive as stated. Level 0 of the tower is a phrase, not a definition: 'factorization dg-category on (X,D,tau) in the Francis-Gaitsgory sense' names a notion FG12 does not contain, 'Ran(X,D,tau)' and 'Verdier-symmetric monoidal structure' are never constructed, and no archetype ever has C^op and a vacuum b exhibited - the only factorization-category definition in the book takes the chiral algebra as input, making level 0 derived from level 1. The Morita anchor thm:mr-morita is tagged ProvedHere with a one-sentence proof citing FG12 Section 4.2 ('Coalgebras vs. ind-nilpotent coalgebras in the pro-nilpotent case') and GR17 Chapter IV.5 ('Infinitesimal differential geometry') - both verified against the actual sources to contain nothing of the kind - and its hypothesis package is internally type-inconsistent (small + presentable + compact generator). The same fabricated-looking 'GR17 IV.5, Theorem 3.1.2' citation props up the (infinity,2)-ambient of Theorem A. The Bourbaki form of the Master Reconstruction is false as stated (the -1 automorphism of the Heisenberg chart kills rigidity at level 5; the derived centre is a Morita invariant so level-3 recovery is impossible in principle), the KSDual witness list contradicts both its own definition and the master concordance's fixed-point table, the explicit genus-1 propagator formulas in two foundation files are wrong (numerically verified failure of double-periodicity) and mutually inconsistent, and the corollary layer of the climax chapter systematically upgrades Conditional engines to ProvedHere. The honest repaired object - a level-1-to-5 conditional comparison schema with A/B/C/D/H as constituents rather than corollaries, KSDual a thin set of isolated (partly complex) points, and corrected citations - is genuinely present in the underlying chapters, but it is substantially weaker than the advertised five-level reconstruction tower with a Bourbaki-rigid primitive datum.

---

## 2026-06-17 -- Pass 478: AP34 closed-sector action versus bulk-sector images

Audit anchor: continuation of AP25/AP34 cleanup from
`/Users/raeez/Desktop/corrections/chiral1 Research Paper Strengthening.pdf`,
with target false pattern "derived centre / Swiss-cheese action = physical
bulk before OCA."

Repairs:

- `standalone/survey_modular_koszul_duality.tex`: replaced the claim that the
  Swiss-cheese structure maps the holomorphic bulk algebra to the
  $E_2$-algebra by the typed statement that it maps the algebraic
  closed-sector actor there; the Quillen equivalence is now scoped to the
  algebraic closed-sector comparison surface, and the physical-bulk reading is
  explicitly gated by the open--closed comparison datum.
- `standalone/survey_modular_koszul_duality_v2.tex`: replaced both occurrences
  of "image is the bulk sector of a 3d gauge theory" by "OCA image is the
  physical bulk sector of a 3d gauge theory."
- `standalone/cy_quantum_groups_6d_hcs.tex`: replaced the statement that the
  $\Ethree$-action is on "the bulk algebra (the derived center)" by the typed
  statement that it is on the algebraic closed-sector actor
  $\Zder(A_\cC)$; the physical-bulk interpretation now requires the OCA/HT
  comparison datum.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added a focused
  guard for these three surfaces, forbidding the retired physical-bulk
  identifications and requiring the OCA/HT gates.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  12 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 534 passed.
- `git diff --check -- standalone/survey_modular_koszul_duality.tex
  standalone/survey_modular_koszul_duality_v2.tex
  standalone/cy_quantum_groups_6d_hcs.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Literal stale-string scan over the touched manuscript sources found no
  remaining `holomorphic bulk algebra`, `image is the bulk sector of a 3d gauge
  theory`, or `bulk algebra (the derived center)` occurrences outside the
  guard's forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 492: KZ--Arnold equality typed as bar superconnection plus residue realization

Audit anchor: user-supplied review artifacts
`/Users/raeez/Downloads/expanded_expert_repair_specification_main36 (1).md`
and `/Users/raeez/Desktop/Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`,
especially the warning that the slogan
\(d_B=\KZ^*(\nabla_{\mathrm{Arnold}})\) is type-wrong unless read as a
finite-window superconnection whose Fulton--MacPherson boundary
residue realization is the ordered bar differential.

Repairs:

- `chapters/frame/preface.tex`: replaced the boxed G2 identity by the
  finite-window bar superconnection
  \[
  \nabla^{B,0}_{\cA,V,n}
  =d_\cA+d_{\mathrm{dR}}
  -\sum_{i<j}\widetilde\rho_{\cA,V,n}(t_{ij})\eta_{ij}
  =\mathrm{KZ}_{\cA,V,n}^*(\nabla_{\mathrm{Arnold}})
  \]
  and explicitly stated that the ordered bar differential is the
  FM-boundary residue realization, not the connection itself.
- `chapters/theory/introduction.tex`: changed the front-facing climax
  paragraph from "bar differential = pulled-back KZ--Arnold
  connection" to the finite-window superconnection statement; the
  chapter roadmap row now describes the residue-realized
  superconnection rather than a literal differential/connection
  equality.
- `chapters/theory/bar_construction.tex`: repaired both the chapter
  opening and the dedicated KZ--Arnold remark so they state
  superconnection pullback followed by FM-boundary/residue
  realization. The old equality is now named only as shorthand for
  this typed construction.
- `chapters/theory/climax_theorem.tex`: changed the chapter title and
  main theorem from a literal equality theorem to a conditional
  genus-zero finite-window theorem. The theorem now names the current
  window \(V\), the action
  \(\rho_{A,V,n}\colon\mathfrak t_n\to\End(V^{\otimes n})\), the bar
  superconnection, and the FM-residue realization. The ghost statement
  is scoped to the canonical standard-family BRST witness surface.
  The genus-one and genus-\(g\) conjectures now use the same
  superconnection/residue-realization type.
- `chapters/theory/chiral_climax_platonic.tex`: changed the opening
  and Definition~\ref{eq:climax-equation-G2} from
  \(\dbar=\KZ^*(\nabla_{\Arn})\) to the typed finite-window
  superconnection, with the bar differential obtained by residue
  realization.
- `compute/tests/test_kz_arnold_superconnection_scope.py`: added a
  focused guard over the preface, introduction, bar-construction, and
  climax surfaces. It blocks the retired literal equality phrases and
  requires the superconnection/residue-realization language.

Verification:

- `pytest compute/tests/test_kz_arnold_superconnection_scope.py`: 2
  passed.
- `pytest compute/tests/test_bar_construction_scalar_typing.py
  compute/tests/test_kz_shadow_connection.py`: 91 passed, with the
  existing six `ComplexWarning` notices from
  `compute/lib/kz_shadow_connection.py`.
- Fixed-string scan over the repaired surfaces for the retired literal
  equality / pulled-back-differential slogans: clean.
- `git diff --check -- chapters/frame/preface.tex
  chapters/theory/introduction.tex chapters/theory/bar_construction.tex
  chapters/theory/climax_theorem.tex
  chapters/theory/chiral_climax_platonic.tex
  compute/tests/test_kz_arnold_superconnection_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 493: Collision logarithmic form local/global scope repaired

Audit anchor: user-supplied review artifacts
`/Users/raeez/Downloads/expanded_expert_repair_specification_main36 (1).md`
and `/Users/raeez/Desktop/Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`,
especially the warning that the affine Arnold form
\(d\log(z_i-z_j)\) is a coordinate representative on an
affine/formal genus-zero collision screen, not a globally defined
coordinate-difference form on an arbitrary curve.

Repairs:

- `chapters/frame/preface.tex`: scoped the boxed \(G2\) form
  \(\eta_{ij}=d\log(z_i-z_j)\) to an affine coordinate chart/formal
  tangent screen and stated that the global object is a logarithmic
  normal form along the diagonal with coordinate-change cocycle. The
  higher-genus replacements are named as KZB/theta or prime-form
  representatives.
- `chapters/theory/introduction.tex`: changed the opening and roadmap
  claims from a global coordinate propagator to a logarithmic normal
  form along each diagonal, represented by \(d\log(z_i-z_j)\) only on
  the affine/formal genus-zero nilpotence screen. Positive genus is now
  routed through prime-form/KZB representatives and the
  Virasoro/projective-connection datum.
- `chapters/theory/configuration_spaces.tex`: retitled the Arnold form
  surface as the affine/formal representative of the logarithmic normal
  form, and changed the bar differential sentence to "FM-residue
  realization" of the connection image. The higher-genus summary now
  separates genus-zero affine/formal representatives, projective-linear
  gluing on \(\mathbb P^1\), elliptic KZB/theta propagators, and
  prime-form representatives.
- `chapters/theory/bar_construction.tex`: changed the chapter opening,
  OPE paragraph, and nilpotence discussion so the singular kernel is
  the logarithmic normal form, locally represented by \(d\log\) only on
  the affine/formal genus-zero screen; global curve data is recorded by
  the coordinate-change cocycle.
- `chapters/theory/climax_theorem.tex` and
  `chapters/theory/chiral_climax_platonic.tex`: changed the Arnold
  form paragraphs so the coordinate difference is not treated as a
  global function on arbitrary curves, and named KZB/theta or prime-form
  representatives as the positive-genus replacements.
- `compute/tests/test_collision_form_local_global_scope.py`: added a
  focused regression guard over these six surfaces, forbidding the
  retired globalizing \(d\log(z_i-z_j)\) slogans and requiring the
  local-representative/global-replacement language.

Verification:

- `pytest compute/tests/test_collision_form_local_global_scope.py
  compute/tests/test_genus_normalization_surfaces.py
  compute/tests/test_elliptic_propagator_normalization.py`: 10 passed.
- Fixed-string scan over the touched manuscript surfaces found the
  retired globalizing slogans only inside the guard's forbidden-fragment
  assertions.
- `git diff --check -- chapters/frame/preface.tex
  chapters/theory/introduction.tex chapters/theory/configuration_spaces.tex
  chapters/theory/bar_construction.tex chapters/theory/climax_theorem.tex
  chapters/theory/chiral_climax_platonic.tex
  compute/tests/test_collision_form_local_global_scope.py
  notes/audit_repairs_ledger_20260610.md`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 494: Arnold--Borcherds nilpotence and same-pair residue scope

Audit anchor: user-supplied review artifacts
`/Users/raeez/Downloads/expanded_expert_repair_specification_main36 (1).md`
and `/Users/raeez/Desktop/Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`,
especially the warnings that \(d_{\bar B}^{2}=0\) is not proved by
Arnold alone, and that repeating a same-diagonal residue vanishes
because the first Poincar\'e residue removes the unique logarithmic
normal factor, not merely "for degree reasons."

Repairs:

- `chapters/frame/preface.tex`,
  `chapters/frame/preface_section1_v2.tex`, and
  `chapters/frame/preface_section1_draft.tex`: replaced the same-pair
  degree-count slogan by the normal-crossings residue statement: after
  the first Poincar\'e residue along \(D_{ij}\), there is no second
  normal direction for the same diagonal; the desuspension sign records
  only ordered-bar orientation.
- `chapters/theory/introduction.tex`: changed the selection-principle
  proof sketch so shared-index triple collisions consume two separate
  inputs: Arnold cancels the logarithmic two-form coefficients, while
  Borcherds cancels the OPE-mode coefficients. The Heisenberg example
  now says the coefficient side is central/vacuum, not that Arnold alone
  supplies the algebraic input.
- `appendices/arnold_relations.tex`: retitled and rescoped the affine
  bar-square theorem as "Arnold forms plus Borcherds coefficients." The
  fixed-triple theorem is now explicitly a scalar-form Arnold
  equivalence; operator-valued chiral bar nilpotence additionally
  requires the Borcherds/Jacobi coefficient identity.
- `chapters/theory/configuration_spaces.tex`: separated scalar
  Orlik--Solomon residue nilpotence from operator-valued chiral bar
  nilpotence. The higher-genus proposition title now reads "affine
  Arnold scalar presentation," and the positive-genus paragraph no
  longer says an Arnold-only relation computes the closed pairwise
  contribution.
- `chapters/theory/chiral_climax_platonic.tex`: changed the
  triple-collision chiral CYBE proof so Arnold supplies the form
  relation and the infinitesimal braid relation is named as the
  simple-pole coefficient projection of Borcherds. The disjoint-pair
  case is no longer called an Arnold property.
- `standalone/programme_summary.tex`,
  `standalone/programme_summary_section1.tex`,
  `standalone/five_theorems_modular_koszul.tex`,
  `standalone/survey_track_a_compressed.tex`,
  `standalone/survey_modular_koszul_duality.tex`,
  `standalone/survey_modular_koszul_duality_v2.tex`, and
  `standalone/introduction_full_survey.tex`: propagated the same-pair
  residue-exact wording and the Arnold--Borcherds split into the
  duplicate summary surfaces.
- `standalone/theorem_index.tex`, `metadata/theorem_registry.md`,
  `metadata/claims.jsonl`, and `metadata/dependency_graph.dot`: synced
  the changed theorem/proposition/corollary titles without regenerating
  metadata.
- `compute/tests/test_arnold_borcherds_nilpotence_scope.py`: added a
  focused regression guard forbidding the retired degree-reason,
  Arnold-only, and disjoint-pair-Arnold slogans, and requiring the
  residue-exact plus Arnold--Borcherds language.

Verification:

- `pytest compute/tests/test_arnold_borcherds_nilpotence_scope.py
  compute/tests/test_kz_arnold_superconnection_scope.py
  compute/tests/test_collision_form_local_global_scope.py`: 6 passed.
- Fixed-string scan over touched manuscript, standalone, metadata, and
  guard surfaces found the retired slogans only inside the guard's
  forbidden-fragment assertions.
- `git diff --check -- chapters/frame/preface.tex
  chapters/frame/preface_section1_v2.tex
  chapters/frame/preface_section1_draft.tex chapters/theory/introduction.tex
  chapters/theory/configuration_spaces.tex
  chapters/theory/chiral_climax_platonic.tex appendices/arnold_relations.tex
  standalone/programme_summary.tex standalone/programme_summary_section1.tex
  standalone/five_theorems_modular_koszul.tex
  standalone/survey_track_a_compressed.tex
  standalone/survey_modular_koszul_duality.tex
  standalone/survey_modular_koszul_duality_v2.tex
  standalone/introduction_full_survey.tex standalone/theorem_index.tex
  metadata/theorem_registry.md metadata/claims.jsonl
  metadata/dependency_graph.dot
  compute/tests/test_arnold_borcherds_nilpotence_scope.py
  notes/audit_repairs_ledger_20260610.md`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 491: Theorem H example-table affine quotient synced with \(H_H\)

Audit anchor: user-supplied review artifacts
`/Users/raeez/Downloads/expanded_expert_repair_specification_main36 (1).md`
and `/Users/raeez/Desktop/Chiral-Bar-Cobar Manuscript Review and Improvement.pdf`
were ingested as advisory evidence, not authority. The verified live
obligation was their Theorem~H warning: the \([0,2]\) chiral
Hochschild concentration is only on the named \(H_H\) package, and
affine Kac--Moody degree-one adjoint zero modes are prequotient
metadata, not quotient-level \(\ChirHoch^1\).

Repairs:

- `chapters/examples/y_algebras.tex`,
  `chapters/examples/n2_superconformal.tex`, and
  `chapters/examples/level1_bridge.tex`: changed example-table
  Theorem~H rows to \(H_H\)-conditional amplitude statements.
- `chapters/connections/holographic_codes_koszul.tex`: changed the
  K7 row to \(H_H\)-conditional curve-level \(\ChirHoch\) amplitude.
- `chapters/frame/preface.tex`: changed the affine family summary so
  \(\operatorname{ChirHoch}^1(V_k(\fg))=0\) after the zero-mode inner
  quotient, \(P_{V_k(\fg)}(t)=1+t^2\), and the adjoint \(\fg\) is
  the zero-mode derivation prequotient / bar-dual generator count.
- `standalone/en_chiral_operadic_circle.tex`: repaired the affine
  example, class-L proof sentence, and comparison table to the same
  quotient convention.
- `standalone/five_theorems_modular_koszul.tex`,
  `standalone/programme_summary.tex`,
  `standalone/programme_summary_sections2_4.tex`, and
  `standalone/survey_modular_koszul_duality_v2.tex`: removed stale
  summary claims
  \(\ChirHoch^1(V_k(\fg))\cong\fg\),
  \(P(t)=1+\dim(\fg)t+t^2\), and total dimension
  \(\dim(\fg)+2\); replaced them by the \(H_H\)-conditional
  quotient profile \(P_{V_k(\fg)}(t)=1+t^2\) with adjoint
  prequotient metadata.
- `compute/tests/test_theorem_h_engine_status_scope.py`: extended the
  guard to include the example, preface, holographic-code, and
  standalone summary surfaces; added forbidden fragments for the
  retired affine quotient profile.

Verification:

- `pytest compute/tests/test_theorem_h_engine_status_scope.py`: 5
  passed.
- Regex scan for retired affine quotient fragments found only an
  unrelated \(\kappa\)-formula occurrence and the guard's own
  forbidden-fragment assertions:
  `rg -n '\\ChirHoch\^1\(V_k\(\\fg\)\).*\\cong.*\\fg|dim\(\\fg\).*\+ 2|1 \+ \\dim\(\\fg\).*t \+ t\^2' chapters standalone appendices compute`.
- `git diff --check -- chapters/examples/y_algebras.tex
  chapters/examples/n2_superconformal.tex chapters/examples/level1_bridge.tex
  standalone/en_chiral_operadic_circle.tex
  chapters/connections/holographic_codes_koszul.tex chapters/frame/preface.tex
  standalone/five_theorems_modular_koszul.tex standalone/programme_summary.tex
  standalone/programme_summary_sections2_4.tex
  standalone/survey_modular_koszul_duality_v2.tex
  compute/tests/test_theorem_h_engine_status_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 479: Derived-centre objects are not bulk algebras

Audit anchor: AP25/AP34 continuation. Target false pattern:
derived-centre, conductor, or boundary-recovery language being stated as
physical bulk algebra before the OCA/HT comparison is present.

Repairs:

- `standalone/survey_modular_koszul_duality_v2.tex` and
  `standalone/survey_track_b_compressed.tex`: replaced the heading
  "Bulk = derived centre" by "Closed sector = derived centre" and
  rewrote the Swiss-cheese sentence so it maps the algebraic
  closed-sector actor to the $E_2$-algebra; holomorphic physical-bulk
  identification now requires the open--closed comparison datum.
- `chapters/theory/universal_conductor_K_platonic.tex`: changed
  `\DerZ(\cA)` from "a bulk algebra built from chiral Hochschild
  cochains" to the algebraic closed-sector Hochschild cochain algebra.
- `chapters/theory/en_koszul_duality.tex`: changed the homotopy-invariant
  application from deformation functors of the bulk algebra to deformation
  functors of the algebraic closed-sector object.
- `chapters/examples/yangians_drinfeld_kohno.tex`: changed the
  boundary/line bridge wording so `\beta_{\mathrm{der}}` recovers the
  algebraic closed-sector object from the boundary algebra, not a bulk
  algebra.
- `chapters/frame/preface.tex`: changed the Volume II summary so the
  derived centre has OCA image in the bulk algebra on constructed
  comparison lanes, rather than being identified with the bulk algebra by
  definition.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added
  visible-TeX guards for these surfaces.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  13 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 535 passed.
- `git diff --check -- standalone/survey_modular_koszul_duality_v2.tex
  standalone/survey_track_b_compressed.tex
  chapters/theory/universal_conductor_K_platonic.tex
  chapters/theory/en_koszul_duality.tex
  chapters/examples/yangians_drinfeld_kohno.tex
  chapters/frame/preface.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scans over the touched manuscript sources found the retired
  forms only inside the guard's forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 480: Holographic Datum BBL triangle retuned to closed sector

Audit anchor: AP25/AP34 continuation. Target false pattern: the standalone
`holographic_datum.tex` defined the BBL triangle by naming the chiral
derived centre itself as "Bulk" and introducing `\cA_{\mathrm{bulk}}`.

Repairs:

- `standalone/holographic_datum.tex`: renamed the local section to the
  closed-sector--boundary--line triangle. The physical BBL diagram is now
  described as a comparison reading that requires the open--closed comparison
  datum.
- Replaced the definition's "Bulk" vertex by the algebraic closed-sector
  vertex, with notation `\cA_{\mathrm{cl}}` and a local OCA gate for any
  physical bulk interpretation.
- Replaced boundary-to-bulk and bulk-to-lines edge language by
  boundary-to-closed-sector and closed-sector-to-lines language.
- Retuned the Heisenberg, Kac--Moody, and Virasoro examples so their middle
  vertex is the closed sector, not a physical bulk.
- Removed the stale `eq:bulk` label and "closed-string derived centre" wording.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added a
  visible-TeX guard for the standalone, forbidding the old "Bulk: derived
  centre", `\cA_{\mathrm{bulk}}`, `eq:bulk`, and old BBL edge phrases.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  13 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 535 passed.
- `git diff --check -- standalone/holographic_datum.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scans found no manuscript occurrences of
  `bulk--boundary--line triangle is recovered`, `boundary-to-bulk trace`,
  `bulk-to-lines edge`, `\cA_{\mathrm{bulk}}`, or `eq:bulk`; the remaining
  occurrences are the guard's forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 481: BBL outline and index surfaces gated by OCA

Audit anchor: AP25/AP34 continuation. Target false pattern: outline and
index surfaces still naming a bulk/boundary/line triangle or bulk
reconstruction when the hand-written theorem surface is only the algebraic
closed-sector/boundary/line triangle before OCA.

Repairs:

- `chapters/theory/introduction.tex`: changed the Volume II table and closing
  outlook item from "bulk/boundary/line triangle" to the
  closed-sector/boundary/line triangle, with physical BBL language only after
  OCA. Also typed the Swiss-cheese entry as the derived closed-sector pair.
- `standalone/programme_summary_sections9_14.tex`: changed the abstract so
  Sections 11--12 package the closed-sector/boundary/line algebraic triangle;
  physical BBL language is explicitly OCA-gated.
- `chapters/connections/thqg_introduction_supplement_body.tex`: changed the
  Volume II guide to say it supplies physical comparison data for the
  closed-sector/boundary/line algebraic triangle; physical BBL reading
  requires the open--closed comparison datum.
- `chapters/connections/genus_complete.tex`: changed the index entry from
  `bulk-boundary correspondence!derived center` to `closed sector!from
  boundary`.
- `chapters/theory/higher_genus_modular_koszul.tex`: changed the index entry
  from `derived centre!bulk reconstruction` to `derived centre!open--closed
  comparison`.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added guards
  for these outline/index surfaces. Generated `standalone/theorem_index.tex`
  was not edited; it should be refreshed only when metadata regeneration is
  explicitly in scope.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  14 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 536 passed.
- `git diff --check -- chapters/theory/introduction.tex
  standalone/programme_summary_sections9_14.tex
  chapters/connections/thqg_introduction_supplement_body.tex
  chapters/connections/genus_complete.tex
  chapters/theory/higher_genus_modular_koszul.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scans over the touched hand-written sources found the retired
  phrases only inside the guard's forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 482: Seven-entry package closes the bulk-algebra leak

Audit anchor: AP25/AP34 continuation. Target false pattern: the
seven-entry holographic datum and genus-complete package still listing the
derived-centre entry as a bulk algebra rather than an algebraic closed-sector
object.

Repairs:

- `chapters/connections/thqg_introduction_supplement.tex`: changed the
  seven-entry list from "The bulk algebra" to "The algebraic closed-sector
  object"; a physical bulk algebra is now stated to be supplied only by the
  additional open--closed comparison datum.
- `chapters/connections/genus_complete.tex`: changed the holographic modular
  Koszul datum package from "bulk algebra" to "algebraic closed-sector object"
  in the complete ingredient list.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: extended the
  outline/index guard to cover both phrases.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  14 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 536 passed.
- `git diff --check -- chapters/connections/thqg_introduction_supplement.tex
  chapters/connections/genus_complete.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scans found the retired package wording only inside the guard's
  forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 483: Landau--Ginzburg HKR bulk wording gated

Audit anchor: AP25/AP34 continuation. Target false pattern: the
Landau--Ginzburg example named the HKR closed-sector algebra as the bulk
algebra before mentioning the open/closed comparison.

Repairs:

- `chapters/examples/deformation_quantization.tex`: changed the
  Landau--Ginzburg paragraph so functions on the derived critical locus are
  the algebraic closed-sector algebra; the physical-bulk reading now requires
  the Landau--Ginzburg open/closed comparison.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added a guard
  for the Landau--Ginzburg wording.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  15 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 537 passed.
- `git diff --check -- chapters/examples/deformation_quantization.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scan found the retired Landau--Ginzburg bulk-algebra phrase
  only inside the guard's forbidden-fragment assertion.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 484: Bulk-operator labels retuned to closed sector

Audit anchor: AP25/AP34 continuation. Target false pattern: closed colour or
derived-centre action labelled as bulk operators/action before the OCA or
BV/BRST comparison is supplied.

Repairs:

- `standalone/holographic_datum.tex`: changed the old SC-pair sentence from
  "bulk acting on boundary" to algebraic closed sector acting on the boundary,
  with physical bulk action requiring the open--closed comparison datum.
- `standalone/programme_summary.tex` and
  `standalone/programme_summary_sections5_8.tex`: changed the closed-colour
  table row from "Bulk operators" to "Closed-sector operators."
- `chapters/theory/poincare_duality_quantum.tex`: changed the diagram label
  from "bulk action" to "closed-sector action," changed "Intrinsic bulk
  operators" to "Intrinsic closed-sector operators," and changed the prose from
  boundary-to-intrinsic-bulk to boundary-to-intrinsic-closed-sector.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added guards
  for these operator/action labels.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  16 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 538 passed.
- `git diff --check -- standalone/holographic_datum.tex
  standalone/programme_summary.tex
  standalone/programme_summary_sections5_8.tex
  chapters/theory/poincare_duality_quantum.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scans found the retired operator/action labels only inside the
  guard's forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 485: Vol II companion BBL references made OCA-gated

Audit anchor: AP25/AP34 continuation. Target false pattern: cross-volume
companion prose referring to the HT bulk-boundary-line triangle without
naming the closed-sector comparison surface or the Vol~II open--closed
comparison gate.

Repairs:

- `chapters/connections/bv_brst.tex`: changed the four-loop, five-loop, and
  Heegner-pattern Vol~II companion references from the HT
  bulk-boundary-line triangle to the
  `\mathsf{SC}^{\mathrm{ch,top}}` HT closed-sector/boundary/line comparison
  triangle, with physical BBL interpretation/readings explicitly through the
  Vol~II open--closed comparison.
- `chapters/connections/feynman_diagrams.tex`: changed the Vol~II leg of the
  cross-volume triangle to the HT
  `\mathsf{SC}^{\mathrm{ch,top}}` closed-sector/boundary/line comparison
  triangle, with physical BBL interpretation only after the Vol~II
  open--closed comparison.
- `compute/tests/test_physics_open_closed_bridge_surfaces.py`: added guards
  for these cross-volume companion phrases.

Verification:

- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  16 passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py
  compute/tests/test_twisted_holography_engine.py
  compute/tests/test_abjm_holographic_datum.py
  compute/tests/test_m5_brane_shadow_engine.py
  compute/tests/test_theorem_burns_f2_engine.py
  compute/tests/test_physics_horizon.py`: 538 passed.
- `git diff --check -- chapters/connections/bv_brst.tex
  chapters/connections/feynman_diagrams.tex
  compute/tests/test_physics_open_closed_bridge_surfaces.py`: clean.
- Stale-string scans found the retired `bulk-boundary-line triangle` forms
  only inside the guard's forbidden-fragment assertions.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 486: Factorization ambient citations routed through \(H_{\Fact}\)

Audit anchor: A-3 / Theorem A ambient-citation rot. Target false pattern:
downstream bar--cobar and chiral-pair arguments still citing a phantom
`GR17 Chapter IV.5, Theorem 3.1.2` or a
Francis--Gaitsgory--Rozenblyum model structure as the source of the chiral
factorization model-structure lift.

Repairs:

- `chapters/theory/bar_cobar_adjunction_curved.tex`: kept
  Vallette/Loday--Vallette as the pointwise chain-operadic input, but changed
  the chiral lift to depend on the conditional factorization ambient package
  \(H_{\Fact}(X)\) of Proposition~\ref{prop:fg-ambient-properties}. The text
  now explicitly says no published GR17 model theorem is used for this lift.
- `chapters/theory/bar_cobar_adjunction_curved.tex`: changed the
  rectification corollary so the chiral version uses \(H_{\Fact}(X)\); without
  that package the result is only the chain-operadic rectification statement.
- `chapters/theory/chiral_koszul_pairs.tex`: changed the Verdier/Ran duality
  argument and the LV-transfer verification so they use the chosen
  factorization/Ran enhancement satisfying \(H_{\Fact}(X)\), not
  \(\mathcal D\)-modules with a non-existent ordinary chiral tensor bifunctor
  and not a GR17 model-structure theorem.
- `compute/tests/test_factorization_ambient_citation_scope.py`: added guards
  for the rebuilt ambient package and downstream citation surfaces.

Verification:

- `pytest compute/tests/test_factorization_ambient_citation_scope.py`: 3
  passed.
- `pytest compute/tests/test_factorization_ambient_citation_scope.py
  compute/tests/test_theorem_concordance_rectification_engine.py
  compute/tests/test_theorem_A_infinity_2.py`: 179 passed.
- `git diff --check -- chapters/theory/bar_cobar_adjunction_curved.tex
  chapters/theory/chiral_koszul_pairs.tex
  compute/tests/test_factorization_ambient_citation_scope.py`: clean.
- Fixed-string scans over hand-written TeX found no remaining
  `\cite[Chapter~IV.5`, `Theorem~3.1.2`, `GR17 transfer`,
  `GR17 model-categorical localisation`, or
  `Francis--Gaitsgory--Rozenblyum model structure` source claims. The only
  remaining `GR17 IV.5` mention on the repaired source surface is the negative
  statement in `theorem_A_infinity_2.tex` that no such published theorem is
  being used.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 487: Standalone genus-1 propagator mirror normalized

Audit anchor: genus-1 elliptic propagator normalization. Target false
pattern: an Arakelov correction written as an antiholomorphic
`d\bar z` term rather than as a real-analytic coefficient multiplying
the same `(1,0)` differential as the theta quotient.

Repairs:

- `standalone/chiral_chern_weil.tex`: replaced the old genus-1 formula
  `d\log\vartheta_1(z_1-z_2|\tau)
  +2\pi i\,\im(z_1-z_2)/\im(\tau)\,d\bar z_1` by the normalized
  elliptic Cauchy kernel
  \[
  \left[
  \partial_u\log\vartheta_1(u|\tau)
  +2\pi i\,\frac{\im u}{\im\tau}
  \right]_{u=z_1-z_2}(dz_1-dz_2).
  \]
  The accompanying prose now states that the correction is a
  real-analytic coefficient in a `(1,0)` form whose `+2\pi i` shift
  cancels the theta quotient's `-2\pi i` B-cycle shift.
- `compute/tests/test_elliptic_propagator_normalization.py`: added the
  standalone Chiral--Chern--Weil surface to the live-file guard and
  blocked the retired `d\bar z_1` compensator from returning.

Verification:

- `pytest compute/tests/test_elliptic_propagator_normalization.py`: 5
  passed.
- Fixed-string scans over `chapters/`, `standalone/`, `appendices/`,
  and `compute/` found the retired
  `d(\overline{z_i - z_j})`, `z_i - z_j}{2\pi i`, and
  `\im(z_1-z_2)/\im(\tau)\,d\bar z_1` variants only inside the
  guard's forbidden-fragment assertions.
- `git diff --check -- standalone/chiral_chern_weil.tex
  compute/tests/test_elliptic_propagator_normalization.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 488: Theorem H summary surfaces made \(H_H\)-conditional

Audit anchor: Theorem H status discipline. Target false pattern:
compact introductions and standalone summaries replacing the full
Theorem~H hypothesis package by the phrase "on the Koszul locus," or
calling the chiral Hochschild amplitude item a proved consequence on
that smaller locus.

Repairs:

- `chapters/theory/introduction.tex`: changed both Theorem~H overview
  entries and the chapter-map row so the amplitude/Hilbert-polynomial
  claim is stated under \(H_H\): PBW chiral Koszul,
  finite-type/perfect, generic, \(E_\infty\)-completed, strict
  Mittag--Leffler, and localized bar-concentration. The meta-theorem
  status paragraph now calls item~(viii) \(H_H\)-conditional rather
  than a consequence merely on the Koszul locus.
- `standalone/programme_summary.tex` and
  `standalone/programme_summary_sections2_4.tex`: changed the
  Koszulness meta-theorem statement so item~(viii) is a one-way
  consequence under \(H_H\), and changed the list item to
  "Under \(H_H\), \(\mathrm{ChirHoch}^*(\mathcal A)\) has amplitude
  \([0,2]\)."
- `standalone/survey_modular_koszul_duality_v2.tex`,
  `standalone/introduction_full_survey.tex`,
  `standalone/N1_koszul_meta.tex`, and
  `standalone/survey_track_a_compressed.tex`: replaced the compact
  "one-way chiral Hochschild consequence on the Koszul locus" and
  unconditional table-row forms by \(H_H\)-conditional wording.
- `chapters/connections/thqg_introduction_supplement_body.tex`: changed
  the cross-volume introduction list item so Theorem~H amplitude and
  Koszul-dual Hochschild duality are explicitly under \(H_H\).
- `chapters/connections/concordance.tex`: changed the projection table
  and the Koszulness-characterisation section from "proved consequence
  on the Koszul locus" to "\(H_H\)-conditional chiral Hochschild
  consequence," with the PBW/generic/perfect/completed
  strict-Mittag--Leffler and localized bar-concentration inputs named.
- `compute/tests/test_theorem_h_engine_status_scope.py`: extended the
  Theorem~H status guard to cover these summary surfaces and block the
  retired "one-way chiral Hochschild consequence on the Koszul locus,"
  "proved one-way consequence on the Koszul locus," and compact
  unconditional Theorem~H amplitude phrases.

Verification:

- `pytest compute/tests/test_theorem_h_engine_status_scope.py`: 5
  passed.
- Fixed-string scans over `chapters/`, `standalone/`, `appendices/`,
  and `compute/` found the retired Theorem~H summary phrases only
  inside the guard's forbidden-fragment assertions.
- `git diff --check -- chapters/theory/introduction.tex
  standalone/programme_summary.tex
  standalone/programme_summary_sections2_4.tex
  standalone/survey_modular_koszul_duality_v2.tex
  chapters/connections/thqg_introduction_supplement_body.tex
  standalone/introduction_full_survey.tex chapters/connections/concordance.tex
  standalone/N1_koszul_meta.tex standalone/survey_track_a_compressed.tex
  compute/tests/test_theorem_h_engine_status_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 489: Front-matter Theorem H surfaces carry \(H_H\)

Audit anchor: continuation of Theorem~H status discipline. Target false
pattern: front-matter and standalone theorem summaries still presenting
Theorem~H as bare concentration on the Koszul or generic
Koszul/PBW locus, without the full \(H_H\) package.

Repairs:

- `standalone/five_theorems_modular_koszul.tex`: retitled the theorem
  statement as \(H_H\)-conditional chiral Hochschild concentration,
  replaced the phrase "bulk in the Beilinson tower" by the algebraic
  closed-sector object, and expanded the hypothesis package to PBW
  chiral Koszulness, finite-type/perfect diagonal Hochschild
  complexes, genericity, \(E_\infty\)-chiral PBW completion, strict
  Mittag--Leffler passage, and localized residue-twisted bar
  concentration. The three-Hochschild-theories warning now says the
  \([0,2]\) amplitude is under \(H_H\).
- `chapters/frame/open_beilinson_tower_platonic.tex`: changed the
  Theorem~H paragraph and Bulk-level summary from "on the Koszul
  locus" to \(H_H\)-conditional concentration, naming the package.
- `chapters/frame/guide_to_main_results.tex`: changed the theorem
  guide from "Koszul/generic surface with \(E_\infty\)-chiral PBW
  completion" to \(H_H\), and expanded the proof-source sentence to
  include finite-type/perfectness, strict Mittag--Leffler passage, and
  localized bar-concentration.
- `chapters/connections/master_concordance.tex`: changed the
  Theorem~H row from generic Koszul/PBW locus to \(H_H\), with the
  package named before the amplitude claim.
- `chapters/theory/introduction.tex`: changed the Part~III map row so
  Theorem~H is \(H_H\)-conditional Hochschild concentration.
- `standalone/survey_modular_koszul_duality_v2.tex`: changed the
  Swiss-cheese datum paragraph from physical bulk wording to algebraic
  closed-sector colour plus an open--closed comparison gate, and
  changed the \(E_\infty\)-input Theorem~H sentence to require \(H_H\).
- `compute/tests/test_theorem_h_engine_status_scope.py`: extended the
  summary-surface guard to include these front-matter files and block
  the retired theorem-title, generic-Koszul/PBW, and
  Koszul-locus-concentration phrases.

Verification:

- `pytest compute/tests/test_theorem_h_engine_status_scope.py`: 5
  passed.
- `pytest compute/tests/test_physics_open_closed_bridge_surfaces.py`:
  16 passed.
- Fixed-string scans found the retired front-matter Theorem~H phrases
  only inside the guard's forbidden-fragment assertions.
- `git diff --check -- standalone/five_theorems_modular_koszul.tex
  chapters/frame/open_beilinson_tower_platonic.tex
  chapters/frame/guide_to_main_results.tex
  chapters/connections/master_concordance.tex chapters/theory/introduction.tex
  standalone/survey_modular_koszul_duality_v2.tex
  compute/tests/test_theorem_h_engine_status_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.

---

## 2026-06-17 -- Pass 490: Theorem H proof-source drift removed from theorem-facing summaries

Audit anchor: Theorem~H proof-source discipline. Target false pattern:
front-matter and climax summaries saying Theorem~H is verified or
extracted "via Shelton--Yuzvinsky" or from "Shelton--Yuzvinsky
Koszulity of the Arnold cohomology," which wrongly promotes a
Koszul-complex fibre input to the whole \(H_H\) mechanism.

Repairs:

- `chapters/frame/preface.tex`: changed the five-theorem summary so
  Theorem~H is on the \(H_H\) surface. The verification-path sentence
  now states the theorem-level mechanism as the \(H_H\) finite-window
  collision-depth collapse: localized residue-twisted bar
  concentration, Arnold--Priddy/Shelton--Yuzvinsky Koszul-complex
  acyclicity as fibre input, and ordered-to-symmetric averaging.
  Feigin--Fuchs, Whitehead, and finite-window certificates are named
  as family checks, not replacements for \(H_H\).
- `standalone/five_theorems_modular_koszul.tex`: rewrote the
  Step~3 circularity paragraph so Shelton--Yuzvinsky/Priddy supplies
  only Koszul-complex acyclicity of the braid-arrangement
  Orlik--Solomon fibre. The text now explicitly says it does not
  contract Arnold cohomology itself and does not by itself prove
  Hochschild concentration. The \(E_1\)-variant paragraph now requires
  the ordered \(H_H^{E_1}\) analogue, including residue-twisted
  acyclicity.
- `chapters/theory/chiral_climax_platonic.tex`: changed the
  projection summary so Theorem~H is extracted from the full
  \(H_H\) package, with Arnold--Priddy/Shelton--Yuzvinsky
  Koszul-complex acyclicity named only as the fibre input.
- `compute/tests/test_theorem_h_engine_status_scope.py`: extended the
  summary guard to include the preface and climax surfaces, and to
  block the retired proof-source phrases.

Verification:

- `pytest compute/tests/test_theorem_h_engine_status_scope.py`: 5
  passed.
- Fixed-string scans over `chapters/`, `standalone/`, `appendices/`,
  and `compute/` found the retired proof-source phrases only inside
  the guard's forbidden-fragment assertions.
- `git diff --check -- chapters/frame/preface.tex
  standalone/five_theorems_modular_koszul.tex
  chapters/theory/chiral_climax_platonic.tex
  compute/tests/test_theorem_h_engine_status_scope.py`: clean.

No metadata regeneration or full LaTeX build was run in this pass.
