## Verdict

FAILS as a theorem-framing in the sharp form under audit.

PROVED: the live manuscript has independent theorem surfaces for bar-cobar reflection, Positselski, Theorem C, Theorem D, and Theorem H. The five-theorem core is explicitly listed in `CLAUDE.md:46`--`CLAUDE.md:50`. Theorem A has unit and counit data in `chapters/theory/theorem_A_infinity_2.tex:175`--`chapters/theory/theorem_A_infinity_2.tex:190`, and Theorem B has a Positselski surface in `chapters/theory/koszul_pair_structure.tex:1310`--`chapters/theory/koszul_pair_structure.tex:1328`.

FAILS: the two equations do not imply those theorem surfaces. `(CL-1)` supplies at most the ordered differential/flatness mechanism; it does not supply the adjunction, unit/counit equivalences, Positselski coderived machinery, PBW concentration, or Hochschild amplitude. `(CL-2)` is numerically false if `K(A)` is read as the scalar `\kappa(A)`: `\kappa(\mathrm{Vir}_c)=c/2`, `\kappa(V_k(\mathfrak g))=\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`, and `\kappa(\mathcal H_k)=k` are anchored in `CLAUDE.md:276`--`CLAUDE.md:280`, whereas the BRST ghost-charge formulas in the live conductor chapter give constants such as `K(\mathrm{Vir}_c)=26` and `K(\widehat{\mathfrak g}_k)=2\dim\mathfrak g` (`chapters/theory/kappa_conductor.tex:204`--`chapters/theory/kappa_conductor.tex:226`).

GAP: the Wave-14 Climax draft asserts that A, B, C, D, H are "sub-shadows" (`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:393`--`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:401`) and concludes that all five are corollaries (`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:506`--`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:510`), but it does not give the missing adjunction, coderived, PBW, or genus-obstruction derivations. The same draft admits universal BRST functoriality is open beyond standard cases (`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:472`--`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:478`).

KILL: the current Climax framing conflates three different objects: scalar `\kappa(A)`, central-charge conductor `K_c(A)=c(A)+c(A^!)`, and the universal ordered-to-symmetric conductor `K_\mathcal A=\mathrm{Av}_\mathcal A`. The latter is explicitly defined as averaging, not ghost charge, in `chapters/theory/universal_conductor_K_platonic.tex:42`--`chapters/theory/universal_conductor_K_platonic.tex:62`.

## (a) (CL-1) => Theorem A

Claim under audit: `d_bar = KZ^*(\nabla_Arnold)` implies the bar-cobar adjoint equivalence.

PROVED: `(CL-1)` can justify a differential once the KZ/Arnold pullback is already constructed. The live bar-cobar chapter says the ordered bar complex uses FM compactifications and Arnold relations, and that `d^2=0` follows from those relations (`chapters/theory/bar_cobar_adjunction_inversion.tex:2774`--`chapters/theory/bar_cobar_adjunction_inversion.tex:2782`; `chapters/theory/bar_cobar_adjunction_inversion.tex:4057`--`chapters/theory/bar_cobar_adjunction_inversion.tex:4066`). The Wave-14 draft likewise states that Arnold flatness pulls back to `d_bar^2=0` (`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:98`--`adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md:106`).

GAP: Theorem A is not just `d_bar^2=0`. It requires a symmetric-monoidal adjoint equivalence, with unit and counit quasi-isomorphisms. The live Theorem A surface states exactly that: `K\dashv K^{-1}`, unit `\eta_\mathcal A`, counit `\varepsilon_\mathcal C`, and chain-level quasi-isomorphisms for both (`chapters/theory/theorem_A_infinity_2.tex:175`--`chapters/theory/theorem_A_infinity_2.tex:190`). `(CL-1)` does not construct either natural transformation.

GAP: Chain-level equivalence requires explicit homotopical witnesses, not only flatness. The live chapter says the chain-level incarnation requires an explicit contracting homotopy `h` with `[d,h]=id-p` and Mittag-Leffler/pro-completion witnesses in class-M cases (`chapters/theory/bar_cobar_adjunction_inversion.tex:1683`--`chapters/theory/bar_cobar_adjunction_inversion.tex:1708`). `(CL-1)` gives no such `h`.

GAP: The `(infinity,1)` lane requires Lurie/Positselski/bar-cobar adjunction data. The proof of the unified reflection cites the abstract universal twisting adjunction, not Arnold/KZ alone (`chapters/theory/theorem_A_infinity_2.tex:203`--`chapters/theory/theorem_A_infinity_2.tex:205`).

Verdict: `(CL-1)` motivates one geometric input to Theorem A. It does not prove Theorem A.

## (b) (CL-2) => Theorem C

Claim under audit: `K(A)=-c_ghost(BRST(A))` implies `\kappa+\kappa^!` lands in `{0,8,13,250/3,98/3}`.

FAILS under the scalar reading. Theorem C is about `K^\kappa(A):=\kappa(A)+\kappa(A^!)`, not the BRST ghost conductor by itself. The live theorem defines `K^\kappa`, `\varrho`, and `K=c+c^!` separately (`chapters/theory/chiral_center_theorem.tex:2808`--`chapters/theory/chiral_center_theorem.tex:2818`). Its bridge is `K^\kappa=\varrho K` under the extra hypothesis `\varrho(A)=\varrho(A^!)` (`chapters/theory/chiral_center_theorem.tex:2815`--`chapters/theory/chiral_center_theorem.tex:2823`).

FAILS: the family assignments in the prompt are misindexed against the live theorem. The live table gives Heisenberg `0`, affine `0`, beta-gamma `0`, Virasoro `13`, principal `W_3` `250/3`, and BP `98/3` (`chapters/theory/chiral_center_theorem.tex:2835`--`chapters/theory/chiral_center_theorem.tex:2843`). Thus "affine, 13", "beta-gamma, 250/3", and "Virasoro, 98/3" are not the Vol I Theorem C assignments.

PROVED: Heisenberg complementarity as scalar kappa sum is `k+(-k)=0`, anchored in the proof of Theorem C (`chapters/theory/chiral_center_theorem.tex:2774`--`chapters/theory/chiral_center_theorem.tex:2780`) and in the live table (`chapters/theory/chiral_center_theorem.tex:2837`). But this uses Verdier/Koszul duality, not BRST ghost charge. A trivial Heisenberg BRST sector gives `-c_ghost=0`; that recovers the paired conductor, not the individual scalar `\kappa(\mathcal H_k)=k` from `CLAUDE.md:279`.

FAILS: affine scalar complementarity is `0`, not `13`. For `\mathfrak{sl}_2`, `\kappa(V_k(\mathfrak{sl}_2))=3(k+2)/4` follows from `CLAUDE.md:276`--`CLAUDE.md:277`. The Feigin-Frenkel involution sends it to `-\kappa`, so the sum is `0` (`chapters/theory/chiral_center_theorem.tex:2777`--`chapters/theory/chiral_center_theorem.tex:2780`; `chapters/theory/chiral_center_theorem.tex:2901`--`chapters/theory/chiral_center_theorem.tex:2908`). The adjoint `bc(1)` BRST conductor is instead `2\dim\mathfrak g`, giving `6` for `\mathfrak{sl}_2` (`chapters/theory/kappa_conductor.tex:204`--`chapters/theory/kappa_conductor.tex:214`).

FAILS: beta-gamma scalar complementarity is `0`, not `250/3`, in the live table (`chapters/theory/chiral_center_theorem.tex:2839`) and proof (`chapters/theory/chiral_center_theorem.tex:2910`--`chapters/theory/chiral_center_theorem.tex:2919`). The value `250/3` belongs to principal `W_3`, via `\varrho=5/6` and `K=100` (`chapters/theory/chiral_center_theorem.tex:2842`).

FAILS: Virasoro scalar complementarity is `13`, not `98/3`. The live proof gives `c/2+(26-c)/2=13` (`chapters/theory/chiral_center_theorem.tex:2781`--`chapters/theory/chiral_center_theorem.tex:2784`; `chapters/theory/chiral_center_theorem.tex:2921`--`chapters/theory/chiral_center_theorem.tex:2924`). The value `98/3` belongs to BP, not Virasoro (`chapters/theory/chiral_center_theorem.tex:2843`).

PROVED: the B-row `8` has live anchors as a Mukai-enhanced K3 witness, not a generic BRST ghost computation: `K^{\kappa_ch}=2c_+(\mathrm{Mukai}(K3))=8` (`chapters/examples/free_fields.tex:6051`--`chapters/examples/free_fields.tex:6054`; `chapters/theory/chiral_koszul_pairs.tex:7711`--`chapters/theory/chiral_koszul_pairs.tex:7717`).

Verdict: `(CL-2)` can be one input to the central-charge conductor `K`, but Theorem C requires the anomaly-ratio bridge and Verdier duality. It is not a corollary of `(CL-2)` alone.

## (c) Trinity K_E = K_c = K_g

Claim under audit: `K_E=K_c=K_g`.

NOT ANCHORED as currently proved. The live `kappa_conductor` chapter marks the Trinity theorem `\ClaimStatusProvedHere` and states the three definitions coincide (`chapters/theory/kappa_conductor.tex:71`--`chapters/theory/kappa_conductor.tex:80`). But the proof step `K_E=K_c` invokes "Borel--Weil--Bott on Ran" to turn an Euler character into a central-charge sum (`chapters/theory/kappa_conductor.tex:83`--`chapters/theory/kappa_conductor.tex:91`), with no primary theorem or internal theorem providing that exact transformation.

GAP: `K_c=K_g` is asserted by "additivity of the Virasoro central charge across BRST quasi-isomorphism" (`chapters/theory/kappa_conductor.tex:93`--`chapters/theory/kappa_conductor.tex:101`). Central charge is not a generic quasi-isomorphism invariant of cdgas without a specified conformal vector/energy-momentum compatibility. The missing input is a theorem that all allowed quasi-free BRST resolutions preserve the relevant Virasoro anomaly class.

FAILS as a universal notation: another live chapter says the "universal conductor" is not the scalar ghost conductor but the ordered-to-symmetric averaging morphism, explicitly replacing the retired scalar headline (`chapters/theory/universal_conductor_K_platonic.tex:4`--`chapters/theory/universal_conductor_K_platonic.tex:10`; `chapters/theory/universal_conductor_K_platonic.tex:42`--`chapters/theory/universal_conductor_K_platonic.tex:62`). Thus the symbol `K` is already overloaded.

GAP/OPEN: the Wave-14 conductor draft itself says the Vol III ghost face would be the ghost charge of a GKM BRST resolution "if a BRST resolution were known", and marks that open (`adversarial_swarm_20260416/wave14_reconstitute_kappa_conductor.md:440`--`adversarial_swarm_20260416/wave14_reconstitute_kappa_conductor.md:444`).

Verdict: at best, Trinity is a theorem requiring three independent proofs plus strict scope: Koszul-self-dual, BRST-resolvable, finite-type/regularity hypotheses, and a fixed convention for `K`. It is not a tautology and not established by the two Climax equations.

## (d) Virasoro BRST check

Claim under audit: `\kappa(\mathrm{Vir}_c)=c/2=-c_ghost(BRST(\mathrm{Vir}_c))`.

PROVED: `\kappa(\mathrm{Vir}_c)=c/2` is a canonical Vol I constant (`CLAUDE.md:278`).

PROVED: the standard fermionic `bc(\lambda)` central charge is `-2(6\lambda^2-6\lambda+1)`, and at `\lambda=2` it is `-26` (`chapters/theory/kappa_conductor.tex:60`--`chapters/theory/kappa_conductor.tex:65`). The live Virasoro conductor corollary computes the reparametrisation ghost contribution as `+26` for `K=-c_ghost` (`chapters/theory/kappa_conductor.tex:217`--`chapters/theory/kappa_conductor.tex:226`).

FAILS: `c/2=26` only at `c=52`. For generic `c`, `-c_ghost(BRST(\mathrm{Vir}_c))=26`, not `c/2`.

PROVED BUT DIFFERENT: Virasoro Theorem C is `\kappa+\kappa^!=13`, because `\mathrm{Vir}_c^!\simeq\mathrm{Vir}_{26-c}` and `c/2+(26-c)/2=13` (`chapters/theory/chiral_center_theorem.tex:2921`--`chapters/theory/chiral_center_theorem.tex:2924`). The ghost conductor `26` is a central-charge conductor, not scalar `\kappa`.

Verdict: `(CL-2)` is numerically false for Virasoro under the scalar kappa reading.

## (e) Affine sl_2 BRST check

Claim under audit: `\kappa(V_k(\mathfrak{sl}_2))=3(k+2)/4=-c_ghost(BRST(V_k(\mathfrak{sl}_2)))`.

PROVED: the affine scalar formula is `\kappa(V_k(\mathfrak g))=\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)` (`CLAUDE.md:276`--`CLAUDE.md:277`). For `\mathfrak{sl}_2`, `\dim=3` and `h^\vee=2`, so `\kappa=3(k+2)/4`.

PROVED: the live conductor chapter gives affine `K(\widehat{\mathfrak g}_k)=2\dim(\mathfrak g)` from one fermionic `bc(1)` ghost per Lie algebra direction (`chapters/theory/kappa_conductor.tex:204`--`chapters/theory/kappa_conductor.tex:214`). For `\mathfrak{sl}_2`, this is `6`.

FAILS: `3(k+2)/4=6` only at `k=6`. For generic level, `-c_ghost` is constant while scalar `\kappa` is level-dependent.

PROVED BUT DIFFERENT: affine scalar complementarity under `k\mapsto -k-2h^\vee` is `0`, not `6` or `13` (`chapters/theory/chiral_center_theorem.tex:2777`--`chapters/theory/chiral_center_theorem.tex:2780`; `chapters/theory/chiral_center_theorem.tex:2901`--`chapters/theory/chiral_center_theorem.tex:2908`).

Verdict: affine `sl_2` kills scalar `(CL-2)`.

## (f) Heisenberg BRST check

Claim under audit: `\kappa(\mathcal H_k)=k=-c_ghost(BRST(\mathcal H_k))`.

PROVED: the canonical scalar is `\kappa(\mathcal H_k)=k` (`CLAUDE.md:279`).

PROVED: the Wave-14 BRST draft describes Heisenberg as quasi-free with no ghosts and gives `K(\mathcal H_\kappa)=0` (`adversarial_swarm_20260416/wave14_brst_ghost_identity_chapter_draft.md:206`--`adversarial_swarm_20260416/wave14_brst_ghost_identity_chapter_draft.md:213`). That agrees with paired scalar complementarity `k+(-k)=0`, not with individual `k`.

FAILS/DRIFT: the inscribed `kappa_conductor` chapter now gives `K(\mathcal H_k)=-2` and `K^c=2` from a single spin-1 bosonic generator (`chapters/theory/kappa_conductor.tex:190`--`chapters/theory/kappa_conductor.tex:202`), which conflicts with both the Wave-14 draft and Theorem C's scalar `0` row. This is internal conductor-definition drift.

FAILS: no natural abelian BRST ghost complex gives `-c_ghost=k` for all levels. The level `k` is an OPE normalisation parameter, not a ghost spin/multiplicity.

Verdict: Heisenberg is the simplest counterexample to scalar `(CL-2)`.

## (g) (CL-2) => Theorem D

Claim under audit: `obs_g=\kappa\lambda_g` derives from `K(A)=-c_ghost(BRST(A))`.

GAP: Theorem D is a genus-obstruction theorem, not a ghost-charge theorem. The obstruction formula uses a genus expansion of the total bar differential and the equation `d_total^2=0`; the live proof defines `obs_g` from lower-genus differential components (`chapters/theory/higher_genus_foundations.tex:4961`--`chapters/theory/higher_genus_foundations.tex:4970`) and expands the differential in powers of `\hbar` (`chapters/theory/higher_genus_foundations.tex:4974`--`chapters/theory/higher_genus_foundations.tex:4999`).

GAP: The `\lambda_g` factor requires Hodge-bundle geometry. The live type-discipline lemma states `obs_g(\mathcal A)=\kappa(\mathcal A)\lambda_g` in `H^{2g}(\overline{\mathcal M}_g)` and identifies `\lambda_g=c_g(\mathbb E)` (`chapters/theory/clutching_uniqueness_platonic.tex:846`--`chapters/theory/clutching_uniqueness_platonic.tex:870`). Ghost charge alone does not produce this tautological class.

PROVED WITH EXTRA INPUTS: the live chapter records three independent verification paths at leading genera, beginning with a direct elliptic Arnold identity at `g=1` (`chapters/theory/clutching_uniqueness_platonic.tex:1282`--`chapters/theory/clutching_uniqueness_platonic.tex:1306`). Those paths are additional to `(CL-2)`.

FAILS as all-genera universal statement without scope. Concordance says all-genera scalar universality holds for uniform-weight generators, but for multi-weight families only the genus-1 identity is unconditional, and stronger all-genera scalar formulae fail because cross-channel corrections appear (`chapters/connections/concordance.tex:447`--`chapters/connections/concordance.tex:465`).

Additional inputs required: genus expansion of `d_total`; Arnold/KZB or elliptic Arnold identities; Hodge bundle and Faber-Pandharipande tautological class; uniform-weight hypothesis or correction terms; identification of the scalar curvature coefficient with `\kappa`; and a proof that the BRST conductor equals that scalar coefficient in the family.

Verdict: `(CL-2)` can at most identify a candidate coefficient after other machinery proves the obstruction class is scalar and Hodge. It does not imply Theorem D.

## Theorem B and H

Theorem B:

GAP/FAILS from `(CL-1)` alone. The live Positselski theorem is a coderived/contraderived equivalence for the chiral bar coalgebra (`chapters/theory/koszul_pair_structure.tex:1310`--`chapters/theory/koszul_pair_structure.tex:1328`). Its proof uses chiral comodule-contramodule correspondence and CDG coalgebra homological algebra (`chapters/theory/koszul_pair_structure.tex:1331`--`chapters/theory/koszul_pair_structure.tex:1338`). `(CL-1)` supplies neither coderived categories nor the comodule-contramodule equivalence.

GAP: bar-cobar inversion also requires the counit quasi-isomorphism and coacyclic cone statements. The live inversion theorem isolates strict Koszul and coderived off-Koszul lanes (`chapters/theory/bar_cobar_adjunction_inversion.tex:1992`--`chapters/theory/bar_cobar_adjunction_inversion.tex:2041`). Arnold flatness is not this theorem.

Theorem H:

FAILS from `(CL-1)+(CL-2)`. The live ordered Hochschild concentration theorem uses ordered FM compactifications and pure-braid Orlik-Solomon Koszulness, then averaging for the symmetric statement (`chapters/theory/chiral_hochschild_koszul.tex:1521`--`chapters/theory/chiral_hochschild_koszul.tex:1548`). That is PBW/Orlik-Solomon spectral sequence input, not a formal consequence of flatness or ghost charge.

PROVED: Virasoro and W-algebra examples have separate live Hochschild computations/concentration surfaces (`chapters/theory/hochschild_cohomology.tex:198`--`chapters/theory/hochschild_cohomology.tex:208`; `chapters/theory/hochschild_cohomology.tex:308`--`chapters/theory/hochschild_cohomology.tex:314`).

FAILS explicitly by live concordance: Arnold-Orlik-Solomon relations give `d^2=0`, but not cohomological concentration; PBW is indispensable (`chapters/connections/concordance.tex:7961`--`chapters/connections/concordance.tex:7976`).

Verdict: Theorem B and Theorem H are not corollaries of the Climax equations.

## Kill list

1. FAILS: scalar `(CL-2)` is false for Virasoro, affine `sl_2`, and Heisenberg. It must not be stated as `\kappa(A)=-c_ghost(BRST(A))`.

2. FAILS: the prompt's Theorem C family-value assignments are not the live Vol I assignments. Live Vol I: affine `0`, beta-gamma `0`, Virasoro `13`, `W_3` `250/3`, BP `98/3`, B-row `8` (`chapters/theory/chiral_center_theorem.tex:2835`--`chapters/theory/chiral_center_theorem.tex:2843`; `chapters/theory/chiral_center_theorem.tex:2858`--`chapters/theory/chiral_center_theorem.tex:2866`).

3. GAP: `(CL-1)` does not construct Theorem A's unit/counit equivalences. It controls differential flatness only.

4. GAP: `(CL-1)` does not imply Positselski. Coderived/contraderived machinery is an independent input.

5. FAILS: `(CL-1)+(CL-2)` do not imply Hochschild concentration. Live concordance explicitly says Arnold relations do not imply concentration.

6. GAP: The Trinity proof in `kappa_conductor.tex` is not anchored tightly enough for a load-bearing theorem. Its two core identifications need primary/literature-backed proofs or downgrading.

7. FAILS/DRIFT: `K` has incompatible meanings across live chapters: scalar ghost conductor in `kappa_conductor.tex`, ordered-to-symmetric averaging in `universal_conductor_K_platonic.tex`, and scalar `\kappa` in the Climax prompt.

8. GAP: The Wave-14 Climax draft is fuzzier than the sharp audit reconstruction. It asserts "sub-shadows" but does not derive A/B/C/D/H, and it admits universal BRST resolution/functoriality is open.

9. FAILS: Theorem D all-genera scalar universality is scoped; multi-weight all-genera statements have cross-channel corrections.

10. NOT ANCHORED: "any BRST-free-field resolution" gives the same ghost charge unless resolution-independence of conformal anomaly is proved with hypotheses.

## Rescue paths

1. Rescue `(CL-1)` as a foundational differential theorem, not the climax theorem: "The ordered bar differential is the Arnold/KZ pullback, hence `d_bar^2=0`; bar-cobar equivalence additionally requires the universal twisting adjunction plus unit/counit quasi-isomorphism witnesses."

2. Replace scalar `(CL-2)` by a scoped conductor identity:
   `K_c(A)=c(A)+c(A^!)=-c_ghost(BRST_pair(A,A^!))`
   on the BRST-resolvable, Koszul-self-dual, fixed-convention locus. Then derive scalar Theorem C only after adding `K^\kappa=\varrho K_c` and proving `\varrho(A)=\varrho(A^!)`.

3. Split notation:
   `\kappa(A)` = genus/obstruction scalar;
   `K^\kappa(A)=\kappa(A)+\kappa(A^!)`;
   `K_c(A)=c(A)+c(A^!)`;
   `K_g(A)=-c_ghost(BRST(A))`;
   `K_\mathcal A=\mathrm{Av}_\mathcal A` = ordered-to-symmetric conductor.

4. State Trinity as conditional:
   `K_E=K_c=K_g` only on a named subcategory with finite bar Euler pairing, fixed conformal vector, quasi-free BRST resolution, and a proved anomaly-invariance theorem.

5. Make the climax smaller and true:
   "The two Climax equations are compatibility bridges among existing theorems, not generators of them." A/B/H stay in the bar-cobar/PBW lane; C/D use conductor and Hodge geometry after separate hypotheses.

6. Falsifier to run next: a tiny symbolic check table with rows `Heis_k`, `Vir_c`, `V_k(sl_2)` comparing scalar `\kappa(A)` to `-c_ghost`; it should intentionally fail generically and thereby enforce the notation split before any inscription.
