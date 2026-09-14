# Four-input native comparison

The new mathematical include is `research-candidates/bd_diagonal026/nonzero-level005/four-input-body.tex`. It depends on the exact preserved body `nonzero-level004/translated-source-body.tex`. The wrapper `four-input-source.tex` includes both bodies and their primary bibliography. New labels use `bdfour-`. No source or evidence file in 004 was changed.

## Exact construction

The untranslated four-input bar has twenty-four orders and five words per order: e, m1, m2, m3, d. Its differential includes bm1=-omega3 d and bm3=-omega1 d. The middle mixed word and the double-merged word are closed. The two contributions to b²e cancel by the odd coefficient wedge sign.

The translated source uses the differentiated products proved in the preserved first chapter. Its state translations, coefficient derivatives, and bar differential are explicit on every finite input jet. A triangular normal form identifies this source with O4 tensor_R D4, and specifies the exact cohomology effect of adjoining translations.

The graded native map uses each actual adjacent edge and the product square for the disjoint first and last pairs. That square maps to its four actual order vertices by (1-u)(1-v), u(1-v), (1-u)v, uv. Its coefficient ring has only the two corresponding pair inverses. Four weighted integrals define the double-pair images of e, m1, m3, and d. The middle mixed word has no square image.

The complete defect table treats coefficient degrees zero, one, two, and all higher degrees for every seed. Four displayed Stokes identities cancel the disjoint adjacent boundaries. Side endpoint regularity removes the unwanted four-current double-pair states. The remaining degree-one defects lie on triple and double-pair diagonals. Degree-two defects lie on the small diagonal, with two currents or vacuum.

The added source complex N has explicit regular-coefficient right differential modules:

- Degree -3: vacuum on a pair and one current at each remaining point, for all six pairs.
- Degree -2: vacuum on both blocks of each double pair; a current on a triple and at its singleton; vacuum and a quadratic current on the two blocks of each double pair, in both placements.
- Degree -1: vacuum and quadratic currents on the small diagonal.

The nonzero differential is pair to double-pair vacuum and triple to small-diagonal vacuum. Every module has its complete normal derivative carrier. Quadratic states have the free translation basis h_a corresponding to (lambda-mu)^(2a). The source is explicitly enlarged by this N. Minimality among all possible four-input added modules is not claimed.

With beta=QB-Bb, the source differential is (bx,beta x+Qn), and the native map is Bx+n. The entire target is the unextended V_k Chevalley–Cousin complex at the fixed nonzero level. All fifteen partition types and every global coefficient are included. The source, square construction, differential, and comparison are permutation-equivariant.

## Relative cohomology

The pair-to-double-pair map and triple-to-small-vacuum map are surjective. For complementary pairs ij|lm, put I_ij equal to the exact annihilator of the native double-pole generator. Then:

- H^-3(N) is the direct sum of D4/(I_ij I_lm) over the three complementary pair channels.
- H^-2(N) is the explicitly presented kernel of the four triple collision maps, plus the double-pair vacuum/quadratic modules.
- H^-1(N) is the small-diagonal quadratic-current module.

The source projection has cone N[1]. These formulas therefore compute its relative cohomology in degrees -4, -3, and -2. The ordinary cohomology change is given by the displayed kernel/cokernel exact sequences, with every connecting map specified on actual cycles by the defect table. No unproved surjectivity of the degree -4 or -3 connecting maps is used.

The degree -2 connecting map is surjective onto the small-diagonal quadratic module. Actual closed two-forms dq12 wedge dq34 divided by t12^(2a+2)t34^2, on the double-merged word, generate its successive translation summands. The first coefficient is 4k J² delta. The general coefficient is 2k(2a+2)/((2a)! 2^(2a)), in the stated staged orientation. Thus H^-1 of the source projection is an isomorphism.

The lowest original cohomology has the five explicit generators per order. Only its unmerged generator maps nontrivially under the first connecting map. Its coefficient is the product of the three adjacent differences. Their twenty-four cubics span a six-dimensional space and generate (x,y,z)(x(y-z),y(x-z)). They do not generate the full cubic ideal; they vanish on the four triple-diagonal lines. The exact connecting image retains this ideal and the Weyl relations.

## Deconcatenation boundary

For each fixed ordered sector, its matching 3+1 and 1+3 cuts agree with the ternary native source on their factorization open sets. The added-module maps are explicit: internal pair modules map to the ternary pair module tensored with the remaining current, and the internal triple maps to the ternary small-diagonal current module tensored with that current. Crossing partitions vanish on this open set.

These sector statements do not give a coproduct on all ordered words. For example, the ordered 123|4 cut of e4123 is zero, while the corresponding native unshuffle component is nonzero on distinct positions. This is an exact incompatibility of the two specified coproducts.

The 2+2 cut fails even in the single 1234 sector with the fixed binary extensions. Torsion forces the image of a new pair generator into N2 tensor P2. Its double-pair differential must land in N2 tensor N2. The chain equation then requires a binary P2 cycle whose separated image is the pure JJ insertion. But the image of all such cycles is JJ times the proper right ideal tD. This excludes a strict cut preserving the native images. Cross localization does not remove the internal pair diagonal or the obstruction.

This resolves the requested four-input cochain construction and gives exact deconcatenation obstructions. A compatible all-arity ordered bar coalgebra structure requires further source or coproduct changes.

## Verification and custody

Run from the assigned worktree:

```sh
/opt/homebrew/bin/python3 reports/research/bd_diagonal026/nonzero-level005/check_exact.py
python3 reports/research/bd_diagonal026/nonzero-level005/build.py
python3 reports/research/bd_diagonal026/nonzero-level005/freeze.py
```

The exact calculation verifies four square identities for sixty-four actual global forms, the nonzero disjoint bar product and zero curvature, the six-dimensional path ideal, forty-nine translated double-pole formulas, the first six quadratic translation generators, the four triple density signs, the double-pair density, and complementary collision cancellation for all twenty-four orders. It also verifies preservation of all forty-two files in the frozen 004 manifest. Finite bounds and dependency versions are recorded. The general claims use the written proofs, not finite numerical extrapolation. No proof assistant was used.

The primary definitions remain Beilinson–Drinfeld, Sections 3.1.1–3.1.2 and 3.4.11. The target carrier and factorization formula have exact equation locators in the bibliography. The build recorder freezes the full LaTeX input closure, including the immutable 004 source and canonical shared style.

The mathematical control requirement is gpt-6-astra with ultra reasoning. Matching metadata was reported verified for this resumed assignment; direct runtime metadata was not exposed locally.

Fresh independent review of the identical frozen source remains required. Acceptance of the source dependency and native integration are separate gates. No files were staged or committed, no central PDF was written, and no standalone PDF viewer was opened.
