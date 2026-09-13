# Native ordered collision candidate

This candidate constructs ordered diagonal maps on finite powers of a smooth separated finite-type complex curve. It proves their compatibility with free horizontal state words, relative ordered bars, and positive-weight cobar reconstruction. It is not independently accepted.

The source is `platonic/chapters/ordered_native_collision.tex`. The existing ordered chapter includes it before its internal ordered bar and contains an explicit consumer comparison. The two new primary citations are in `platonic/references.bib`.

## Mathematical result

For a surjection p:I→J and a total order on each fibre, lexicographic expansion defines an actual map Y_J→Y_I over the collision diagonal δ_p:X^J→X^I. The map restricts the Thom-Sullivan coefficient family to expanded block-order faces before pulling back coordinates. No forbidden within-fibre denominator is specialized to zero. The induced map δ_p^dagger C_I^r→C_J^r is a map of commutative algebra objects in right differential modules, with the explicitly unshifted pointwise convention. The chain rule is ∂_Z_j κ(c)=κ(Σ_{p(i)=j}∂_z_i c). Nested maps compose by concatenating fibre orders.

The horizontal free-state algebra is C_I⊗T(u_i). The state merger sends u_i to u_p(i) and preserves actual noncommutative composite words. Its first nontrivial ordered bar square is

    α b[u_1|u_2|u_3] = [u_a²|u_b] - [u_a|u_a u_b] = b α[u_1|u_2|u_3].

The map also sends ω_13 and ω_23 to ω_ab, and sends ω_12 to zero when 1 and 2 merge with fixed internal order. The zero is obtained by face restriction before coordinate substitution.

The binary derived coefficient fibre is C×C. Its two projections are distinct collision restrictions. Replacing the coefficient algebra by its cohomology instead gives a dual-number fibre, proving relative nonformality. This is an algebra calculation, with the complete bounded flat proof in the source.

The bar differential and relative RHom interpretation include the leading-face sign, contraction, semifree argument and convolution lifts. The cobar proof includes the gap-sign exponent and a finite filtration in each weight. Completed reconstruction targets the completed free-state algebra. It does not silently map a formal word series to the uncompleted tensor algebra.

## Exact boundaries

- The finite-power order family is not Cartesian for the usual Ran transitions: its binary collision fibre map is C²→C. A full factorization/Ran comparison remains an additional construction.
- The recovered multiplication a_i a_j=ω_ij b_ij remains valid as a dg coefficient algebra. With all state generators horizontal, it fails the differential-module Leibniz identity. Its derivative is -dq_ij/(z_i-z_j)² b_ij, which is nonzero on an adjacent-exchange edge. No identification of that algebra with the free horizontal state algebra is claimed.
- Punctured-scale expansion, supported residue, chiral-convolution multiplication, and an arbitrary physical state system require their own comparison maps.
- The coefficient-relative RHom is in dg coefficient modules. It is not the derived Hom of horizontal sections.

## Recovery custody

`mining-dispositions.json` has twenty statement dispositions. “Integrated” means implemented in this candidate, not accepted. It preserves forty-eight source occurrences with forty-two distinct hashes, including rejected and intermediate source versions. Eighty-eight relevant public intermediate records are preserved with exact session lines and record hashes. Analysis-channel messages and private reasoning were not selected.

Additional matched returns and public exposures remain explicitly pending. No claim of complete semantic reading of all preserved bytes is made. The current proof consumes complete load-bearing arguments from the retained collision/bar sources, the exact original C ranges recorded in the ledger, the live manuscript, primary sources, and new calculations. No archived program was executed.

The four explicitly stopped historical reading artifacts named by `semantic_wave_reconcile` were searched for the specific order-chart, ordered-collision, merged-state and Thom-Sullivan terms. Those searches had no matches. They are not treated as completed native-collision evidence.

## Verification

Base: clean principal `develop` at `cb6e88263f4bb75ef5c1d9db911f61ca5d3d4d9c`. Worktree: `frontier-mine-vol1-20260913`. Branch: `repair/frontier-mine-vol1-20260913`. No stage, commit, push, publication, shared-checkout write, or template change occurred.

Run from the worktree:

```sh
/opt/homebrew/bin/python3 reports/research/MINING-2026-09-13/calculations/check_collisions.py
TEXINPUTS=/Users/raeez/latex-template: make platonic
git diff --check
```

Python 3.14.6 and SymPy 1.14.0 give all exact checks passing. The calculation checks 17,009 overlap pairs, 33,921 nested compositions, 633 fibre partitions, 254 bar-square parity cases, 3,279 merged-state bar words, three rational connection identities, and 3,110 cobar-square/counit cases. The formulas are tested through the finite ranges named in `calculations/results.json`; the manuscript supplies their general proofs.

The first invocation through the worktree's `/usr/bin/python3` failed because SymPy was unavailable. The explicit Homebrew Python invocation above resolves that environment mismatch. This failure was not suppressed or counted as passing.

The actual default integrated build produces `out/platonic.pdf`, 603 pages. Final logs report no LaTeX errors, undefined references, or undefined citations. The new chapter has one `amsrefs` advisory about optional citation syntax and no overfull or underfull box warning. Inherited warnings remain elsewhere in the full volume. The existing template symlink remains unchanged; the explicit TEXINPUTS path resolves its shared target from the deeper worktree.

Physical pages 45–51 contain the complete new chapter. Pages 53–54 show its immediate consumer, and pages 601–602 contain the added bibliography entries. These pages were visually inspected. The final page breaks keep the cobar statement together and the Ran boundary section on its own page. The added prose has no project-management or closed-repository references.

This regional check is not a whole-book firewall or mathematical verdict. Inherited PDF metadata still includes “integrated monograph,” a literal title spacing token, and unrelated Igusa subject/keywords. The existing front matter and unmodified claims need their own review. The candidate PDF is a working artifact and must not replace an accepted release.

Required research controls: gpt-6-astra with ultra reasoning. The task requests those controls; independently observed runtime metadata is unavailable and therefore unverified.

## Integration interfaces

The separate CBC source owner confirmed the same suspension convention: |s|=-1 and b2(sa⊗sb)=(-1)^|a|s(ab). Its determinant-line calculation remains separately owned. This candidate does not alter the two-color forest source or infer its mixed coefficient identities.

Shared copies of `Volume_I_Ordered_Chiral_Geometry.tex` in the other book repositories require semantic integration by the main owner. Their baseline byte identity is not acceptance. The detailed reconstruction does not consume the new coefficient object, so it has not been edited.

`candidate-manifest.json` freezes every owned changed file, the three source changes, the PDF, the aggregate source patch, and selected build dependencies. Its hashes, rather than the mutable worktree paths alone, identify the independent-review candidate.
