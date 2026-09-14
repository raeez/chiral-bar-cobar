# Subregular affine reduction: candidate006

The new source constructs a strict unital quasi-isomorphism from the full subregular sl3 W-algebra into its affine–ghost differential vertex algebra. This candidate requires fresh independent review. The whole native book and the original reflected Koszul comparison remain unaccepted.

## Frozen mathematical targets

The source manifest is `source-manifest.json`, SHA-256 `d116f3c5208ac9e1b7437b391b8cbc011b33e2ff02a1a3a4e72ef1798a990f00`. It binds 87 source files, with seven additions or changes against candidate004. The new mathematical body is `cbc/chapters/theory/subregular_ds.tex`, SHA-256 `e7ba05abec42d37ed47cae9346bc09b0289ff1837ed68756bb3019315cbe8da0`. The aggregate diff is `7854b89c3da5484f22676708d6077c64848b7847062d47627435b7c59d49716a`.

The first target is over R=C[k], on the universal affine vacuum algebra of sl3 tensor two charged free-fermion pairs. The character uses f=−E21 and the integral good grading x=diag(2,−1,−1)/3. The differential is the zero mode of q=:(E12−1)c1:+:E13 c2:. All cohomological degrees, parity, normal ordering, modes, and residue signs are stated.

The closed generators are J, U, P, V. The proof gives an ordered tensor decomposition of complexes, an explicit contraction of the constraint pairs, and a bounded-below filtration that contracts two further ghost pairs. These constructions prove a PBW basis and cohomology concentrated in degree zero. The inclusion is a strict unital vertex map. Every specialization, including k=−3, is covered by the same polynomial proof. A reverse strict unital degree-preserving vertex map is obstructed by b_i(0)c_i=1.

The second target localizes at k+3. The fields G+=U, G−=−V, and T=(P+3:JJ:/4−3∂J/2)/(k+3) satisfy the full universal Bershadsky–Polyakov products. All four strong generators are even. The proof includes the exact stress homotopy

    (k+3)(Lfull−T−∂J/2)=D(:b1E21:+:b2E31:).

The conformal formula is excluded at k=−3. No native consumer edited here asserts a conformal vector there.

The third target constructs the full meromorphic binary collision on an affine coordinate chart. The map preserves all vertex modes, the vacuum, both differential-operator connections, and the collision mapping cone. Its finite iterates are compatible. No completed bar or other-curve descent is inferred.

## Deciding corrections

The weight-one current has coefficient (2k+3)/3. The charged cubic coefficient is (k+1)(2k+3), and the Virasoro quartic coefficient is c/2, with c=−(2k+3)(3k+1)/(k+3). All three vanish at k=−3/2. At k=−1/2 they equal 2/3, 1, 1/5. Vanishing scalar terms do not make the full collision zero.

For reflected parameters k and −k−6, the conformal charges sum to 50. They agree only when (k+3)^2=−4. This is a conformal obstruction, not a construction or disproof of every possible curved Koszul equivalence.

The connected framework and deep-example passages now use the actual four-generator reduction and binary products. The hierarchy example gives the correct PBW vacuum series. The local orbit table distinguishes the zero orbit from the minimal nonzero orbit. The original reflected subregular comparison remains explicitly stated, with its missing cross-level map identified.

## Preservation and source evidence

All 85 candidate004 source hashes matched their recorded manifest before copying. The source and final manifest hashes match the handoff. No candidate005 directory was present in the assigned worktree. Candidate004 and all earlier candidates remain read-only.

All prior complete proof bodies are retained. The sole change to an imported prior proof is a line break in the projective-line field-convention display. The affine sl2 proof, relative comparison, Virasoro operator proof, elliptic propagator, finite BV proof, and other imported bodies remain byte-identical to candidate004. No accepted PDF is replaced.

The complete old F1–F8 and R1–R3 reviews are copied into `prior-rejections/`, together with the candidate004 integration findings. `prior-rejection-custody.json` binds each copy to its source hash. These reviews are evidence to check, not accepted mathematical premises. `rejection-disposition.md` records the current boundary for every group.

Primary PDFs and extracted text are retained in `primary/`. Kac–Wakimoto, arXiv math-ph/0304011v2, section 1 and Theorem 4.1, specify the reduction conventions and the structural comparison. Arakawa, arXiv1005.0185v4, section 2, page 2, gives the universal Bershadsky–Polyakov products. The local proof and exact mode calculation independently reconstruct the decisive identities. `primary-sources.json` records the source hashes and locators.

## Reproduction and limits

Run from the assigned worktree:

    /opt/homebrew/bin/python3 reports/research/cbc_native026/candidate006/check_modes.py
    python3 reports/research/cbc_native026/candidate006/build.py subregular
    python3 reports/research/cbc_native026/candidate006/build.py proof
    python3 reports/research/cbc_native026/candidate006/build.py native

The exact calculation uses Python 3.14.6 and SymPy 1.14.0. Its 347 checks consist of 300 generator or vacuum sanity checks and 47 composite identities. The latter include all four closed fields, every displayed singular product, and the exact stress homotopy. These identities are finite symbolic calculations. The general cohomology theorem rests on the written contraction and filtration proof.

An early mode-ordering implementation recursed on equal even modes. Allowing direct insertion for those commuting equal modes corrected the implementation. An initial identification G−=V gave the opposite charged OPE. The exact product fixes G−=−V. Neither failure is evidence against the polynomial reduction theorem. Both routes are recorded here to preserve their scope.

Builds run from the owned source directories, with output directories under this report tree. They require stable auxiliary hashes. The final build records, input closure, render binding, and evidence manifest specify the exact artifacts. Complete standalone render inspection and selected native-page inspection do not certify the remaining native book.

The original reflected W/Koszul comparison, arbitrary module comparison, completed totalizations, second differential, nodal clutching, chiral cyclic/BV/CG identification, and arbitrary-genus insertion amplitudes remain outside this proved result. Several inherited native consumers still assert stronger claims and prevent whole-book acceptance.

No staging, commit, push, central PDF write, or external PDF opening is authorized or performed. No child assignment was made. The required mathematical controls are gpt-6-astra and ultra effort. Independently observed runtime metadata is unavailable, so those controls remain unverified.

The first source freeze is preserved under `frozen-source001/`. Its native differential display collided with the equation number. The successor changes only that display layout. `source-manifest-001.json` and `freeze001-custody.json` preserve the prior boundary.
