# Dual collision coefficient repair

Candidate 002 repairs the sole blocking finding against candidate 001. It remains unaccepted until renewed review. The original 001 manifest, frozen source, PDF, and renders remain unchanged.

Only `platonic/chapters/ordered_native_collision.tex` changes among the manuscript files. Its former three-line dual-collision assertion is replaced by an explicit construction and proof. The geometric coefficient map, state merger, bar/RHom arguments, cobar proof, and Ran boundary are unchanged. Automatic theorem numbering updates the downstream reference in the rendered internal-bar chapter.

For B=Lδ_p^*C_I, the proof first extends the pulled-back bar to C_J:

    γ_p,w : C_J ⊗_B^L Lδ_p^*Q_I(w) → Q_J(w).

Transposition over C_J gives the corrected map

    Hom_C_J(Q_J(w), C_J)
      → C_J ⊗_B^L Lδ_p^*Hom_C_I(Q_I(w), C_I).

The bar component in a fixed weight is finite semifree. The dual comparison therefore follows from evaluation on a shifted free module and a finite filtration. The proof identifies the transpose by precomposition, verifies the differential and connection, and uses the coalgebra equation to prove compatibility with convolution. The completed target takes the degreewise product after extension of each weight. For nested ordered surjections, E_q E_p identifies with E_qp and d_qp^vee=E_q(d_p^vee) d_q^vee.

The binary coefficient example proves why extension is necessary. For B=C²→C by the first projection, B-linearity forces any reverse linear map into the first idempotent summand. It cannot preserve the unit (1,1). After extension the weight-zero target is C and the dual map preserves its unit.

## Verification

Commands run from the worktree:

```sh
/opt/homebrew/bin/python3 reports/research/MINING-2026-09-13/repair-002/check_dual_collision.py
TEXINPUTS=/Users/raeez/latex-template: make platonic
git diff --check
```

Python 3.14.6 reports all targeted checks passing: 171 dual-differential basis checks, 16 nested transpose checks, 569 convolution basis pairs through weight four, 25 idempotent samples, and the scalar-extended unit. The proof, rather than these finite checks, establishes the general derived comparison. The unrelated 001 calculation suite was not repeated.

The default build produces 603 pages with no LaTeX errors, undefined references, or undefined citations. The corrected construction occupies physical pages 49–50. Its unchanged cobar and Ran consumers occur on pages 51–52; the internal-bar reference appears on page 53. Pages 49–54 were rendered from the new PDF into this directory and visually inspected. No clipping, overlap, missing notation, or manuscript-firewall text was found. The inherited optional-citation advisory remains; no box warning occurs in the new chapter.

The old files named `final-page-049/050/051.png` are stale 001 intermediates and remain preserved. The old `verified-page-049/050/051.png` match 001. The images under `repair-002/render/page-049.png` through `page-054.png` belong to 002. No old image was overwritten.

Inherited whole-volume metadata defects and the missing rendered bibliography URLs remain separate obligations. No whole-volume acceptance is claimed. Full Ran descent, punctured-scale comparison, and realization of the omega-weighted state algebra remain outside this bounded repair.

## Evidence and custody

The complete fresh reviewer return was read and preserved under `materials/raw/` with its exact hash. It blocks 001 only for the missing dual coefficient extension; its supporting findings are not promoted to whole-volume acceptance. The current mining ledger adds M21 and retains the former dispositions.

The newly received stopped-session route has 671 records and SHA-256 `a617a8e2ed2d53f5e037a9ce9d3d440e07906c6ebd6ada16cb8184f47fae40f3`. Its complete JSON is preserved under this repair's raw directory. It remains discovery material pending semantic consumption; it supplies no premise of this repair.

No source bytes outside the assigned worktree were written. No stage, commit, push, or publication occurred. Required controls remain gpt-6-astra/ultra; independently observed runtime metadata is unavailable and unverified.
