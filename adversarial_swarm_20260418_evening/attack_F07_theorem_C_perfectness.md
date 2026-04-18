# F07 Attack: Theorem C perfectness and derived-center bypasses

Repo surface audited: Vol I only, with live source priority over metacognitive status notes.

Local source availability note:
- Live bibliography entries exist for `GR17`, `TUY89`, `Francis2013`, and `Arakawa2016RationalAdmissible` in `bibliography/references.tex`.
- No local PDF/text copy of Hinich, TUY, Arakawa 2016, or GR17 was found in the workspace.
- The live theorem file cites `Hinich2001`, but the live bibliography has no `\bibitem{Hinich2001}`.

Compute cross-checks run:
- `pytest -q compute/tests/test_dmod_filtration_ss.py -k 'gap_sl2_positive_int or gap_sl2_generic'` -> `2 passed`
- `pytest -q compute/tests/test_holographic_dmod_purity.py -k 'conformal_blocks_dim_sl2_k1_4pt'` -> `1 passed`
- `pytest -q compute/tests/test_conformal_blocks_genus_engine.py -k 'genus1_equals_num_reps and A and 1 and 1'` -> `7 passed`

## 1. T1 vs T2

### T1 is now honestly conjectural, but its source anchoring is sloppy
- `conj:derived-center-koszul-equivalence` is explicitly a conjecture at `chapters/theory/theorem_C_refinements_platonic.tex:123-129`.
- The bypass-failure remark is explicitly inscribed at `chapters/theory/theorem_C_refinements_platonic.tex:160-179`.
- So the *status* downgrade is real, not just narrative.

### T2 is narrower than the old Wave-14/AGENTS/FRONTIER story, but the narrowed proof is still not clean
- The live proposition is `prop:perfectness-standard-landscape` at `chapters/theory/theorem_C_refinements_platonic.tex:234-312`.
- The live source restricts the unconditional lane to:
  - Heisenberg.
  - Affine KM at positive integer level.
  - Affine KM at boundary admissible level.
- Generic non-critical affine KM is explicitly conjectural at `chapters/theory/theorem_C_refinements_platonic.tex:314-333`.
- Class M boundary perfectness is explicitly conjectural at `chapters/theory/theorem_C_refinements_platonic.tex:335-349`.

### Internal drift remains live
- The paragraph just above the proposition still says “affine Kac--Moody at non-critical level cases are proved unconditionally” at `chapters/theory/theorem_C_refinements_platonic.tex:226-229`. That overstates the actual proposition.
- The theorem index still summarizes the proposition as “unconditional for Heisenberg and affine KM non-critical” at `standalone/theorem_index.tex:2375-2376`.
- `AGENTS.md:614` and `FRONTIER.md:23` still preserve the old unconditional-family narrative.

Conclusion for section 1:
- T1 has been genuinely downgraded.
- T2 has been narrowed in source, but the narrowed proof still contains unresolved gaps.
- Reverse drift persists on the live metadata surface.

## 2. HINICH/FG BYPASS AUDIT

### What is actually inscribed
At `chapters/theory/theorem_C_refinements_platonic.tex:164-179`, the manuscript claims:
- Hinich gives a chain-level `E_2` model for each brace dg algebra separately, but not the comparison zig-zag between `Z^{der}_{ch}(A)` and `Z^{der}_{ch}(A^!)`.
- “Francis--Gaitsgory” / `GR17` gives a six-functor Ran-space ambient useful for the chiral base, not the Koszul-dual derived-center comparison.
- Therefore neither route removes the Deligne-Tamarkin dependence.

### Audit result on the citations themselves
- `Hinich2001` is cited at `theorem_C_refinements_platonic.tex:166`, but the live bibliography has no such key. The only Hinich entries are `HS87`, `HS93`, and `Hin97` at `bibliography/references.tex:736-743`.
- `GR17` is not Francis-Gaitsgory. In the live bibliography it is Gaitsgory-Rozenblyum, *A Study in Derived Algebraic Geometry*, at `bibliography/references.tex:649-650`.
- So the live text gets the *logical shape* of the bypass failure right, but the bibliographic presentation is unstable:
  - Hinich source unresolved.
  - GR17 source misnamed.

### Does the failure claim survive anyway?
Yes, in the weak sense relevant here.
- A rectification theorem for brace dg algebras can upgrade each side to an `E_2` model, but that does not itself manufacture a quasi-isomorphism between two unrelated brace algebras. The remark’s logic is sound.
- A Gaitsgory-Rozenblyum six-functor / Ran formalism can improve the factorization ambient, but that is ambient infrastructure, not an equivalence theorem for derived centers across Koszul-dual pairs. The remark’s logic is again sound.

### Stronger attack: the supposed PTVV/derived-stack bypass also fails as an independence claim
- `prop:ptvv-lagrangian` is marked `ClaimStatusProvedHere`, but its proof imports Theorem C itself:
  - shifted form uses Verdier pairing at `chapters/theory/higher_genus_complementarity.tex:2219-2222`;
  - Lagrangian clause uses `C_g = Q_g(A) \oplus Q_g(A^!)` from `thm:quantum-complementarity-main` at `chapters/theory/higher_genus_complementarity.tex:2240-2245`.
- The repair is acknowledged in `thm:C-PTVV-alternative`, which downgrades clause (iii) to conjectural and states that only clauses (i)-(ii) are independent at `chapters/theory/theorem_C_refinements_platonic.tex:432-476`.

Conclusion for section 2:
- The manuscript does inscribe that the Hinich and GR17 bypasses fail.
- That inscription is not fully source-clean: undefined Hinich cite, misnamed `GR17`.
- The failure is therefore “inscribed but bibliographically defective,” not mere narrative.

## 3. TUY PERFECTNESS CHECK

### What `lem:perfectness-criterion` actually requires
`lem:perfectness-criterion` requires total finite-dimensional flat fiber cohomology:
- `\dim H^n(\bar B^{(g)}_{flat}(A)|_\Sigma) < \infty` for all `n`, at `chapters/theory/higher_genus_complementarity.tex:331-336`.
- After the spectral-sequence collapse, the only surviving issue is total finiteness of degree-0 fiber cohomology, at `higher_genus_complementarity.tex:359-385`.

### What `prop:perfectness-standard-landscape` actually proves
The proposition quietly weakens the language from total fiber cohomology to “finite-weight fiber finiteness”:
- see `chapters/theory/theorem_C_refinements_platonic.tex:242-246`.
- For the integer-level affine KM lane, the proof ends with “The bar cohomology at each fiber is finite dimensional at each conformal weight” at `theorem_C_refinements_platonic.tex:266-267` and “each of finite graded dimension at each conformal weight” at `:301-303`.

This is not the same statement as `lem:perfectness-criterion`.

### What TUY actually buys on the live record
TUY, as cited in the proposition and in the bibliography (`TUY89` at `bibliography/references.tex:1326-1327`), supports:
- finite-rank conformal blocks on stable pointed curves;
- sewing/factorization through a finite sum over integrable channels.

That is good evidence for finite-dimensional *conformal blocks*. But the theorem needing proof is finite-dimensional fiber cohomology of the strict flat bar complex.

### The missing bridge
The clean bridge is available elsewhere in the repo but is not used in the T2 proof:
- `prop:conformal-blocks-bar` identifies conformal blocks with `H^0` of the bar complex at `chapters/theory/chiral_modules.tex:541-554`.
- Combined with `lem:perfectness-criterion`, which already gives degree-0 concentration at `higher_genus_complementarity.tex:359-380`, this would let TUY finite rank imply the required total finiteness of the only surviving cohomology group.

But `prop:perfectness-standard-landscape` does not cite or insert that bridge. As written, it proves only weightwise finiteness, not the exact hypothesis it claims to discharge.

### Level-1 witness: what the local compute surface confirms
The local compute layer supports finite-rank conformal blocks on the integrable `\widehat{\mathfrak{sl}}_2` lane:
- `compute/tests/test_holographic_dmod_purity.py` verifies that the 4-point block at level 1 has dimension 2.
- `compute/tests/test_conformal_blocks_genus_engine.py` verifies genus-1 block dimension equals the number of integrable simples; for type `A_1`, level 1 this gives 2.
- `compute/tests/test_vertex_algebra_extensions.py:1186-1193` gives a character-level cross-check for `L_1(sl_2)` by matching Weyl-Kac coefficients with the lattice/Fock partition formula `\sum_n p(h-n^2)`.

This is enough to witness finite-dimensional conformal blocks and finite weight multiplicities at level 1.
It is **not** by itself a proof of perfectness of the flat relative bar family over `\overline{\mathcal M}_g`.

Conclusion for section 3:
- TUY does not, on the current written proof, deliver T2 in the form required by `lem:perfectness-criterion`.
- A plausible repair exists: explicitly route TUY finite-rank conformal blocks through `prop:conformal-blocks-bar` and the degree-0 concentration lemma.
- Until that repair is written, the integer/admissible “unconditional” lane is not fully secured on the inscribed proof surface.

## 4. GENERIC-LEVEL OBSTRUCTION

### What the live conjecture says
`conj:perfectness-boundary-km-generic` at `chapters/theory/theorem_C_refinements_platonic.tex:314-333` is honest about the unresolved point:
- Kac-Kazhdan gives finite-length composition at each conformal weight on smooth fibers.
- What is missing is propagation to the nodal stratum without TUY/Arakawa finite-conformal-block input.

### What the rest of the repo says
- `chapters/theory/ftm_seven_fold_tfae_platonic.tex:694-705` records only “finiteness-at-each-weight” from Kac-Kazhdan/Shapovalov on the generic lane.
- `compute/tests/test_dmod_filtration_ss.py` distinguishes the positive-integer lane from the generic lane:
  - `test_gap_sl2_positive_int` passes with “no gap”.
  - `test_gap_sl2_generic` passes with “gap present”.

The generic obstruction on the current record is therefore not “Jordan blocks in the Shapovalov form” in any final sense. The more precise obstruction is:
- Kac-Kazhdan/Shapovalov controls fixed-weight local algebra.
- It does **not** by itself produce a stable-curve / nodal-sewing theorem for the fiber bar complex.
- Hence it does not upgrade smooth-fiber weightwise control to family perfectness on `\overline{\mathcal M}_g`.

### Is the generic case close?
Not on the present inscribed evidence.
- The repo has evidence that Kac-Kazhdan is necessary input.
- The repo does not have an inscribed theorem replacing TUY/Arakawa on the generic non-critical boundary lane.
- So the honest statement is: generic non-critical affine KM remains open here and needs more than Kac-Kazhdan. It needs a genuine nodal/family finiteness theorem.

## 5. VERDICT

- T1: honest conjecture on the live theorem surface. The failure of the Hinich and GR17 bypasses is actually inscribed, but the bibliography is defective: `Hinich2001` is undefined and `GR17` is Gaitsgory-Rozenblyum, not Francis-Gaitsgory.
- T2: narrowed scope is inscribed, but the proof still overreaches. TUY and Arakawa give a credible route to finite-rank conformal blocks; they do not, as currently used in `prop:perfectness-standard-landscape`, discharge the exact total-finiteness hypothesis of `lem:perfectness-criterion`.
- Generic non-critical affine KM is still genuinely conjectural. Kac-Kazhdan only gives smooth-fiber, weightwise control; the nodal/family step is missing.
- C2 remains conditional on more than coderived `BV=bar`: it also needs the conditional BV bracket theorem, the conditional BV Verdier comparison, nondegeneracy, Kontsevich-Pridham, and the bar-chart transport lemma.
- AP271 reverse drift is real: the live theorem index, AGENTS, and FRONTIER still advertise generic affine KM non-critical as unconditional when the source theorem file does not.

VERDICT: Wave-14 overclaim has been partly healed for Theorem C, but F07 still lands a serious hit: T1 is only conjectural, T2's narrowed integer/admissible lane is not fully proved as written, generic non-critical KM remains open, and the metadata surface still drifts back toward the false unconditional story.
