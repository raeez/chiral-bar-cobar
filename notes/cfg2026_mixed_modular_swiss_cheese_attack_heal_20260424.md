# CFG 2026 Mixed Modular Swiss-Cheese Attack-Heal Synthesis

Date: 2026-04-24.

Scope: 22-lens attack-heal swarm on what arguments are actually needed
to realize Costello--Francis--Gwilliam 2026 methods in the mixed modular
Swiss-cheese programme. The active concurrency cap was six.

Primary source boundary:
[Costello--Francis--Gwilliam, *Chern--Simons factorization algebras and knot
polynomials*, arXiv:2602.12412, 2026](https://arxiv.org/abs/2602.12412).

## Verdict

The swarm converged.

CFG 2026 supplies a real but narrow input: ordinary real three-dimensional
Chern--Simons theory on `R^3`, a complete filtered `E_3` factorization
algebra `A^lambda`, perfect modules obtained from finite-dimensional
Drinfeld--Jimbo representations, and framed-link factorization-homology
traces equal to Reshetikhin--Turaev link invariants.

The repository may honestly compare to CFG only after restricting to the
local topological shadow. The surviving local comparison is:

1. associated graded `C^*(g)`;
2. first-order shifted Poisson bracket on linear observables determined by
   the invariant pairing;
3. all-order comparison only after a chosen regularization/formality/
   associator package and a proof that the full formal deformation classes
   agree in `hbar H^3(g)[[hbar]]`.

CFG 2026 does not prove 6d hCS, CY3/Hall/BKM, K3/M5, modular-family base
change, Sugawara topologization, WRT surgery, arbitrary `A^!` Wilson lines,
or a two-colored Swiss-cheese line-defect realization.

## Swarm Topology

The 22 lenses were:

1. CFG primary-source extraction.
2. BV deformation and all-order classification.
3. Swiss-cheese operadic compatibility.
4. RT/framed-link trace normalization.
5. filtered Koszul/perfect-module bridge.
6. cross-volume consistency.
7. modular-family/log-DM base change.
8. 6d hCS and dimensional-reduction claims.
9. stratified factorization and line defects.
10. formal-disk stable core.
11. compute/test verification surface.
12. parameter conventions.
13. Vol II source-boundary citation audit.
14. honest theorem-stack architecture.
15. stratified 3/1 defect-operad architecture.
16. relative CFG/FGM base-change theorem.
17. perfect-module/dualisability bridge.
18. compute-heal test specification.
19. cross-volume propagation/referee.
20. primary-source expansion.
21. final convergence referee.
22. citation-key and wording hygiene.

No theorem files were edited in this pass. No builds or tests were run.

## Stable Claims

These survive attack:

1. Vol I `thm:cfg` is safe when it is read literally: CFG proves ordinary
   3d CS filtered `E_3`, perfect modules, and framed-link RT trace. Anchor:
   `chapters/theory/en_koszul_duality.tex:5126`.
2. The local comparison warning is correct: CFG does not prove the full
   ordered-bar shadow tower is RT. Anchor:
   `chapters/theory/en_koszul_duality.tex:5177`.
3. The honest local overlap is the topologized derived chiral center after a
   formal-disk/fiber restriction, not `B^ord(A)` and not `A^!`.
4. The first-order bracket match is plausible and supported by the local
   `sl_2` computations: associated graded `C^*(g)`, bracket determined by
   the invariant pairing, extended as a biderivation.
5. The mixed `SC^{ch,top}` layer is two-colored. It is not itself a
   one-colored `E_3` algebra and cannot carry CFG Wilson lines without an
   added stratified line-defect structure.

## Claims Destroyed Or Demoted

These cannot be promoted as written:

1. `thm:e3-identification` as an all-order natural isomorphism inferred from
   `dim H^3(g)=1`. One dimension gives one scalar per order, not equality of
   the formal series. Anchor: `chapters/theory/en_koszul_duality.tex:5348`.
2. `thm:chiral-e3-cfg` as a natural map from naive `Gamma(D,-)`. Ordinary
   global sections on the formal disk are not the required symmetric
   monoidal equivalence to vector spaces. Anchor:
   `chapters/theory/en_koszul_duality.tex:6963`.
3. CFG as a source for Sugawara or chain-level topologization. Anchor:
   `chapters/theory/topologization_chain_level_platonic.tex:72`.
4. Vol II `cfg_side_by_side.tex` as a 6d hCS/CY3/K3/M5/BKM theorem
   imported from CFG. Anchor:
   `/Users/raeez/chiral-bar-cobar-vol2/appendices/cfg_side_by_side.tex:44`.
5. Vol II `six_d_hcs_e3_chiral_avatar_platonic.tex` as CFG conducted on a
   six-dimensional target. Anchor:
   `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:92`.
6. `A^!_line`-modules as CFG trace labels without a perfect/dualizable
   subcategory. Anchor:
   `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:364`.
7. boundary annulus Hochschild trace as the CFG framed-link trace without a
   perfect line label and duality maps. Anchor:
   `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:4224`.
8. WRT surgery, closed 3-manifold state spaces, and root-of-unity MTC
   statements as CFG consequences.
9. compute tests labelled as CFG or factorization-homology trace when they
   only compute Jones/HOMFLYPT/RT via Markov traces.
10. Vol III 6d/5d hCS universal-trace surfaces when cited as direct CFG
    boundaries instead of conditional independent avatar theorems.

## The Required Theorem Stack

The correct realization is a stack of separate arguments.

| Layer | Status | Required argument |
|---|---:|---|
| CFG local bulk algebra | proved by CFG | Semisimple `g`, invariant pairing, CS on `R^3`, complete filtered BV observables, locally constant `E_3`. |
| formal-disk affine comparison | conditional | Define the fiber/de Rham-horizontal functor; compute associated graded `C^*(g)` and first-order invariant-pairing `P_3` bracket. |
| all-order filtered `E_3` comparison | missing | Choose regularization/formality/associator data and prove equality of the full class in `hbar H^3(g)[[hbar]]`. |
| topologized derived center | local/internal | Prove `[m,G]=partial_z` on the original complex, or restrict to transferred/cohomological models. |
| mixed modular Swiss-cheese skeleton | internal/local | Keep the two-colored skeleton distinct from the one-colored `E_3` CFG algebra. |
| stratified line-defect bridge | missing | Build a framed `3/1` stratified defect operad and perfect module trace labels. |
| log-DM modular-family extension | missing | Prove ordered log-FM compactification, six-functor base change, clutching, KZB boundary formal type, and averaging compatibility. |
| 6d hCS avatar | separate conditional | Prove renormalized BV, anomaly cancellation, and pushforward/compactification to a locally constant 3d shadow. |

Replacement theorem form:

For semisimple `g` with normalized invariant pairing and noncritical affine
level `k`, the formal-disk fiber of the topologized derived chiral center of
`V_k(g)` has associated graded `C^*(g)` and first-order `P_3` bracket matching
CFG's local filtered `E_3` algebra after a specified parameter convention.
An all-order equivalence is conditional on chosen regularization/formality/
associator data and equality of the complete deformation class in
`hbar H^3(g)[[hbar]]`. Extension to mixed modular Swiss-cheese families is
conditional on relative log-FM/KZB/six-functor/clutching/averaging theorems.
Framed-link traces agree with CFG/RT only for perfect CFG modules transported
through a proved line-defect comparison.

## Parameter Dictionary

No all-order comparison should be stated without this dictionary.

1. Fix a normalized invariant form `B_0` on `g`.
2. Bare affine level means `B_KM = k B_0`.
3. Shifted KZ denominator is `kappa_KZ = k + h^vee`.
4. KZ small parameter is `h_KZ = 1/(k + h^vee)`.
5. Drinfeld--Jimbo parameter: `q_DJ = exp(pi i h_KZ)`.
6. Jones variable used in many knot engines: `q_Jones = q_DJ^2`.
7. CFG deformation data: a classical invariant pairing plus all-order choices
   forming a torsor over `hbar_CFG H^3(g)[[hbar_CFG]]`.
8. Do not set `lambda_CFG = k + h^vee` without a renormalization theorem.
9. Collision and KZ `r`-matrices must be distinguished:
   `r_coll = k Omega_0 / z`, while `r_KZ = Omega_0 / ((k+h^vee)z)`.
10. Framed RT uses a ribbon twist `theta_V`; unframed Jones requires a
    writhe correction with a fixed crossing convention.

## Missing Stratified Defect Object

The needed operadic object is not the current two-colored
`SC^{ch,top}`. It is a framed stratified disk operad

```tex
O_def = C_* Disk^{fr,ch,top}_{3 superset 2 superset 1 superset 0}.
```

Local models:

```tex
(D^3; D^2_boundary; D^1_K; D^0_J)
```

with colors:

1. bulk `b`: CFG filtered `E_3` algebra `A^lambda`;
2. boundary/open `partial`: chiral/topological boundary algebra;
3. line `ell_V`: framed oriented one-stratum labelled by a perfect
   dualizable `A^lambda`-module `V`;
4. junction `j`: endpoint data carrying evaluation and coevaluation maps.

Required maps:

```tex
ev_V: V^vee tensor_{A^lambda} V -> 1,
coev_V: 1 -> V tensor_{A^lambda} V^vee.
```

The current `SC^{ch,top}` is only the two-color truncation, forgetting line
strata, endpoints, perfect labels, and ribbon closure.

## Relative Modular Input

The missing relative theorem should have the following form.

Let `S` be a log-smooth Deligne--Mumford stack with normal-crossing boundary,
for instance `Mbar_{g,n}^{log}`. Let `pi: C -> S` be the universal semistable
curve and let

```tex
j_n: Conf_n^ord(C/S) -> FM_n^ord(C/S)
```

be the ordered log-Fulton--MacPherson compactification, after any required
finite Kummer/log-etale ramification along collision and nodal divisors.

For a filtered cyclic logarithmic `SC^{ch,top}` algebra `A`, holonomic per
weight and with KZB/Gauss--Manin normal-crossing formal type on every
stable-graph boundary stratum, prove:

```tex
R pi_{n,*} j_{n,*}^ord B^ch(A)
  ~= int_{C/S}^{fact,ord} A
  ~= Bbar_log^{ord,mod}(A)
```

compatibly with log-etale base change, stable-graph clutching, Stokes-sector
KZB gluing, and the `Sigma_n` averaging map.

Proof obligations:

1. ordered compactification over the boundary, with Kummer/log-etale
   ramification control;
2. relative six-functor base change for `R pi_* j_* B^ord`;
3. factorization homology over families, not just fibers;
4. averaging versus boundary residues;
5. stable-graph clutching as a six-functor push-pull theorem;
6. KZB formal type and Stokes compatibility at the boundary;
7. curved derived/coderived comparison using bounded-filtered Positselski
   hypotheses;
8. distinction between local CFG `Disk_3/E_3` input and modular
   Swiss-cheese boundary transport.

Minimal falsifiers:

1. local model `u=x^2` at two-point collision: trace/averaging must commute
   with `Res(d log x)`;
2. genus one, two points: elliptic propagator near `q=0` must preserve the
   `E_2` completion and KZB residue under averaging and base change;
3. genus two, no markings: seven stable graphs must give codimension-two
   cancellation after clutching;
4. split boundary `H_1` in `Abar_2`: recompute the Kunneth base-change class;
5. class `C`: the beta-gamma tower must stabilize at `N=4`.

## Perfect-Module Gate

Ambient statement:

```tex
C_line ~= A^!_line-mod
```

may remain as a description of an ambient line category only if it is not used
as a CFG trace theorem.

CFG trace label:

```tex
V in Perf(A^lambda)
```

must be compact/perfect, dualizable, complete filtered, finite type, and
equipped with evaluation/coevaluation. In the affine lane it must come from a
finite-dimensional Drinfeld--Jimbo representation or be explicitly marked
outside CFG.

Proof obligations:

1. define the completed filtered `A^!_line`-module category;
2. prove compactness/perfectness by a finite-cell or bounded finite-rank
   resolution;
3. prove dualizability by evaluation/coevaluation and triangle identities;
4. construct the comparison functor to CFG `A^lambda`-modules;
5. match associated gradeds;
6. prove factorization-homology trace compatibility;
7. prove the Morita comparison for the boundary category.

## Compute Surface

Current compute oracles are useful but mostly non-CFG:

1. Jones/HOMFLYPT/RT arithmetic: legitimate Markov-trace oracles.
2. `sl_2` CE/Hochschild/topologization arithmetic: legitimate local
   consistency checks.
3. SC bar-cobar inversion tests: legitimate anti-conflation oracles for
   `A`, `B(A)`, `A^!`, and `Z^der_ch(A)`.
4. They do not instantiate CFG's complete filtered BV-CS `E_3` algebra,
   perfect Drinfeld--Jimbo module, framed link, and trace/coend object.

Rename or gate:

1. `factorization_trace_jones/colored/slN` should be `markov_trace_*` or
   marked `non_cfg_rt_oracle`.
2. `TestFactorizationTrace` should be `TestQuantumMarkovTraceNonCFG`.
3. `test_e3_cs_deformation_line_for_sl2` should be renamed as a non-CFG
   CE `H^3(sl_2)` check.
4. `CFGComparison` boolean fixtures in the Vicedo envelope engine should be
   claim-surface flags, not proof oracles.

Needed CFG fixtures:

1. `CompleteFilteredBVCSA`;
2. `PerfectDJModuleFixture`;
3. `FramedLinkFixture`;
4. `TraceCoendFixture`;
5. `CFGParameterDict`.

Negative tests should pass Jones/RT arithmetic while failing CFG gates when
BV-CS completion, perfect module, framing, or trace/coend data are absent.

## Cross-Volume Propagation

Safe or nearly safe:

1. Vol I `chapters/theory/en_koszul_duality.tex:5126`: literal CFG theorem.
2. Vol I `chapters/theory/en_koszul_duality.tex:5177`: warning that CFG is
   not the whole shadow tower.
3. Vol II `chapters/connections/spectral-braiding-core.tex:628`: ordinary
   semisimple 3d CS comparison, if kept scoped.
4. Vol II `chapters/connections/3d_gravity.tex:6444`: ordinary BV-CS `E_3`
   provenance, if not used for KM/DS topologization.
5. Vol III `chapters/theory/cy_to_chiral.tex:422`: safe CFG boundary remark.
6. Vol III `chapters/theory/en_factorization.tex:570`: safe guardrail that
   CFG is not the 6d source.

False source dependencies:

1. Vol I `chapters/theory/topologization_chain_level_platonic.tex:72`.
2. Vol II `appendices/cfg_side_by_side.tex:44`.
3. Vol II `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:70`.
4. Vol II `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:383`.
5. Vol II `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:588`.
6. Vol II `chapters/connections/spectral-braiding-core.tex:664` if used for
   WRT surgery.
7. Vol III `chapters/theory/en_factorization.tex:1346`.
8. Vol III `chapters/theory/en_factorization.tex:1837`.
9. Vol III `chapters/theory/en_factorization.tex:2804`.
10. Vol III `chapters/theory/phi_universal_trace_platonic.tex:1232`.

Compute mislabels:

1. Vol I `compute/lib/theorem_cs_knot_invariant_engine.py:218`.
2. Vol I `compute/tests/test_theorem_cs_knot_invariant_engine.py:510`.
3. Vol I `compute/lib/theorem_vicedo_envelope_engine.py:805`.
4. Vol III `compute/lib/cfg25_e1_chiral_lift.py:141`.
5. Vol III `compute/lib/e3_ce_quantum_toroidal.py:29`.

## External Source Map

Sources and what they can supply:

1. Ayala--Francis--Tanaka, stratified factorization homology:
   stratified spaces and 3/1 defect language; not chiral D-modules or BV
   renormalization. https://arxiv.org/abs/1409.0848
2. Ayala--Francis--Rozenblyum, factorization homology:
   higher-categorical coefficients; not explicit CS/hCS observables.
   https://arxiv.org/abs/1504.04007
3. Costello--Gwilliam, Factorization Algebras in QFT I/II:
   perturbative BV observables and quantum factorization algebras; not
   log-DM modular sewing or RT knot identification.
4. Costello--Li and Williams:
   holomorphic BV/hCS/BCOV anomaly machinery; not CFG filtered `E_3`.
   https://arxiv.org/abs/1905.09269
   https://arxiv.org/abs/1505.06703
   https://arxiv.org/abs/1809.02661
5. Beilinson--Drinfeld:
   chiral algebras, factorization on curves, chiral homology; not 3/1
   defects or renormalized hCS.
6. Mok and Gaitsgory--Rozenblyum:
   log-FM and derived-stack/six-functor ambient technology; not by themselves
   chiral-observable base change over `Mbar_{g,n}`.
7. Felder--Wieczerkowski and Calaque--Enriquez--Etingof:
   smooth elliptic KZB formalism; not nodal/log boundary type for the mixed
   Swiss-cheese problem.
8. Drinfeld and Etingof--Kazhdan:
   associators and quasi-Hopf quantization; not analytic hCS or log modular
   base change.
9. Lurie and Douglas--Schommer-Pries--Snyder:
   `E_n` modules and dualizability criteria; not the actual perfectness of
   the present VOA/chiral module categories.
10. Reshetikhin--Turaev and Ben-Zvi--Brochier--Jordan:
    RT link/3-manifold invariants and surface factorization homology; not
    the mixed modular Swiss-cheese realization.

No primary source currently supplies all of the mixed modular CFG bridge.

## Citation Hygiene

Canonical key recommendation: `CFG2026`.

Canonical metadata:

```tex
K. Costello, J. Francis, and O. Gwilliam,
\emph{Chern--Simons factorization algebras and knot polynomials},
arXiv:2602.12412, 2026.
```

Migration aliases only: `CFG25`, `CFG26`, `CFG2602`.

Legitimate sentence:

> Costello--Francis--Gwilliam prove, for ordinary real three-dimensional
> Chern--Simons theory, that BV quantization gives a locally constant
> filtered `E_3` factorization algebra and that its factorization-homology
> trace with perfect modules recovers Reshetikhin--Turaev link invariants.

Conditional comparison sentence:

> The CY3/6d hCS construction may be compared with CFG only after passing to
> the locally constant topological shadow; before that reduction, the
> Dolbeault/chiral CE object, Hall/BKM/DT comparison, compact-CY3 extension,
> and Sugawara topologization require separate hypotheses and proofs.

Forbidden pattern:

> CFG proves the 6d hCS `E_3` algebra, the hCS-to-Hall map, the BKM/Delta5
> trace, the quantum-toroidal output, or the Sugawara `Q`-exact
> topologization.

## First Repair Queue

1. Rewrite Vol II `appendices/cfg_side_by_side.tex` so CFG is not a 6d
   hCS/CY/K3/M5 source.
2. Rewrite Vol II `six_d_hcs_e3_chiral_avatar_platonic.tex` so CFG is not
   theorem support for 6d QME, 6d `E_3`, OPE, K3 x E, or BKM.
3. Remove CFG as Sugawara/topologization authority from Vol I
   `topologization_chain_level_platonic.tex`.
4. Tighten Vol I `en_koszul_duality.tex` so `thm:chiral-e3-cfg` is an
   internal comparison to CFG, not a theorem of CFG.
5. Separate CFG framed-link RT from WRT surgery in Vol II
   `spectral-braiding-core.tex`.
6. Audit Vol II `3d_gravity.tex` KM/DS topologization claims.
7. Replace CFG-as-6d-FH and CFG-surgery language in Vol III
   `en_factorization.tex`.
8. Rewrite Vol III `phi_universal_trace_platonic.tex` so CFG is a conditional
   companion, not a 5d/6d hCS boundary theorem.
9. Relabel Vol III `cfg25_e1_chiral_lift.py` and its tests from "works" to
   conditional/open where appropriate.
10. Fix the `epsilon_2=0` / `sigma_2=0` contradiction in Vol III
    `e3_ce_quantum_toroidal.py` and mark quantum-toroidal output as
    conjectural modelling.

## Stop Conditions

Do not promote any CFG-adjacent claim until the relevant gate is present:

1. parameter dictionary fixed;
2. formal-disk fiber functor proved;
3. full deformation series matched if all-order `E_3` equality is claimed;
4. perfect/dualizable module subcategory constructed;
5. stratified `3/1` defect operad defined if Wilson lines are used;
6. relative log-FM/KZB/six-functor/clutching/averaging theorem supplied for
   modular-family statements;
7. separate Costello--Gwilliam/Costello--Li/Williams hCS theorem supplied
   for 6d/5d claims;
8. compute evidence relabelled so Markov-trace arithmetic is not CFG proof.

