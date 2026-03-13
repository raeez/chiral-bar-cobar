# NEW MACHINERY — Tools That Don't Yet Exist

**Purpose**: For each research programme in PROGRAMMES.md, this file specifies exactly
what new mathematical tools, computational infrastructure, or theoretical frameworks
are required. Each entry identifies: what exists, what's missing, the first concrete
step, and what success looks like.

**Framing**: This work operates at the triple intersection of pure mathematics
(Serre/Grothendieck/BD standard), mathematical physics (Witten/Costello/Gaiotto standard),
and physics (Polyakov/Dirac standard). All three are equally weighted. The physics
conjectures are IN SCOPE. The gap between algebraic machinery and physical theories is
our gap to close.

**Design for Opus 4.6**: Each machinery item is structured as a self-contained unit
with explicit inputs, outputs, and verification criteria. This prevents scope creep
(the main failure mode) while enabling deep vertical strikes (the main strength).

**Dual Imperative**: Every tool below serves the most powerful theorem it can
reach. The discipline of specifying exact inputs, outputs, and verification
criteria is not conservatism — it is what makes ambitious targets credible.

**Last updated**: Session ~126 (Mar 9, 2026)

---

## Frontier Dependency Order

Use the machinery catalogue in the following order, not as a flat menu.
This is the machinery ledger for extending the proved modular Koszul core
to the larger modular homotopy-theory programme.

1. **Resolved entry theorem already in hand**:
   MC1 is no longer the live bottleneck for the standard finite-type
   interacting families.
2. **MC2 machinery complete**:
   All three MC2 packages are now resolved (`thm:mc2-full-resolution`):
   the intrinsic cyclic `\Defcyc(\cA)` model, the geometric
   completed tensor / clutching package, and the tautological-line
   support. The universal MC element `Theta_A` exists.
3. **Structural comparison machinery next**:
   then attack MC3 and MC4, especially the H-level comparison problems
   that remain after the standard M-level completions for
   `W_\\infty` and Yangian towers.
4. **Physics-facing machinery last**:
   MC5 depends on those prior layers and should not set the order of
   attack.

Auxiliary warning:
the periodicity flank remains weak.  Treat periodicity machinery as
containment and clarification work unless it is directly supporting a
proved structural statement such as the lcm/profile shadow or quantum
periodicity input.

Entry-surface warning:
keep the double entry frame explicit while using this catalogue.
Heisenberg remains the primary commutative/modular atom.  The Yangian
evaluation-locus Drinfeld-Kohno square is the secondary
braided/factorization atom.  Machinery that goes beyond the evaluation
locus must say so exactly; do not let category-`O` or dg-shifted
targets leak backward into the evaluation-locus theorem.

---

## M1. Derived Oper Identification (Programme I)

### What exists
- PBW spectral sequence for B-bar(g_{-h^v}) computing H^*(g; S^*(g[t^-1]))
- H^0 = Fun(Op) proved (thm:oper-bar-h0)
- H^1 = Omega^1(Op) proved (prop:oper-bar-h1)
- Feigin-Frenkel center z = Fun(Op) (PE, FG06)
- Oper space is formally smooth (FG06)

### What's missing
**Tool 1.1: Derived algebraic geometry interface for bar complexes.**
The bar complex B-bar(g_{-h^v}) is a cochain complex of vector spaces. The derived oper
space O(Op^dR(X)) is an object in derived algebraic geometry. The identification requires
a functor connecting these two worlds.

Specifically: for a formally smooth affine scheme Spec(R), the cotangent complex L_{R/k}
is R-free in degree 0. But the bar complex has cohomology in all degrees. The connection
is that B-bar should be quasi-isomorphic to the *Chevalley-Eilenberg complex* computing
Lie algebra cohomology of the pro-nilpotent radical of Op, which in turn computes the
de Rham cohomology of Op (because Op is formally smooth and pro-affine).

**Tool 1.2: Explicit PBW spectral sequence computation beyond E_1 for sl2.**
At E_1: H^p(sl2; S^q(sl2[t^-1])). The sl2-invariants of symmetric powers of the loop
algebra. For p = 0: S^q(sl2[t^-1])^{sl2} = the ring of sl2-invariant polynomials on the
arc space, which is the center z. For p = 1: derivations of z. For p = 2: this is the
unknown quantity. Need to compute H^2(sl2; S^*(sl2[t^-1])) explicitly.

### Status update (Mar 8, 2026)
- The genus-1 `\mathfrak{sl}_2` PBW verification surface is now consolidated in compute:
  `compute/lib/genus1_pbw_sl2.py` exposes tensor-power Casimir and PBW `d_1` diagnostics
  (`adjoint_casimir_on_tensor_power`, `bracket_d1_on_tensor_power`, rank/kernel helpers).
- The weight-3 MC1 checks now consume this shared API in
  `compute/tests/test_genus1_pbw_sl2.py`, removing duplicated local constructions.
- The same module now includes explicit `d_1` equivariance and Casimir-commutation
  residual diagnostics, with tests verifying these algebraic gates through tensor
  power `n=6`.
- These diagnostics are now mirrored in the genus-1 PBW theorem exposition
  (`higher_genus.tex`, Step 4 of `thm:pbw-genus1-km`) via explicit `n=3,4,5,6`
  Casimir/rank/equivariance data, so the manuscript argument and compute API
  remain synchronized.
- A dedicated profiler now exists
  (`compute/scripts/profile_genus1_pbw_sl2_scaling.py`) and records the runtime
  envelope through `n=6`; Casimir eigenspaces are the dominant scaling cost.
- The `n=7` frontier lane now has a full sparse/modular eigenspace path:
  latest single-prime extraction recovers the full spectrum with
  identical multiplicities on both modular backends, and default
  frontier runs now use the fast `weight_block` lane.
- The same modular lane now has an explicit backend strategy selector:
  `global` versus `weight_block` (ad(h)-weight decomposition), with
  default policy `CASIMIR_MODULAR_STRATEGY="auto"` selecting
  `weight_block` at `n>=7`.
  This backend now also prunes impossible weight/eigenvalue pairs in the
  finite-field rank loop (`|w|>j` for `\lambda_j=2j(j+1)`), reducing
  rank solves on `n=7`.  The default modular prime is now the smallest
  non-colliding frontier prime (`CASIMIR_MODULAR_PRIMES=(127,)`), so
  default `n=7` auto runs remain exact at the eigenspace level with
  lower practical runtime.
- The same frontier lane is now formalized behind a reusable staged API:
  `staged_frontier_diagnostics_on_tensor_power(...)` in
  `compute/lib/genus1_pbw_sl2.py`, which packages:
  core rank/kernel/invariant diagnostics, optional equivariance and
  Casimir-commutator gates, and optional eigenspace extraction
  (`auto`/`exact`/`exact_sparse`/`modular`/`theory`) with per-stage timings.
  The scaling profiler (`compute/scripts/profile_genus1_pbw_sl2_scaling.py`)
  now runs through this shared API, so staged frontier checks and full frontier
  checks use the same compute path.
- Casimir extraction policy is now explicit in the shared API:
  `CASIMIR_EXACT_CUTOFF = 6` with mode selector
  `casimir_method_for_tensor_power(power, method="auto")`.
  Default `auto` keeps exact eigenspaces through `n<=6` and switches to
  modular sparse extraction at `n>=7`, while `theory` remains available as a
  baseline/control mode.
  A `QQ`-exact sparse nullity backend (`exact_sparse`) was also benchmarked;
  it is substantially slower (`n=5`: ~`26.7s` vs exact ~`1.85s`,
  `n=6`: >`240s`), so default policy remains unchanged.
- A first MC2 compute scaffold now exists (`compute/lib/mc2_cyclic_linf.py`):
  finite coderivation dg-Lie identities, low-arity cyclic `L_\infty` brackets,
  and a first symbolic Maurer-Cartan solver pass (solutions `{0,1}`) with tests in
  `compute/tests/test_mc2_cyclic_linf.py`.
- The MC2 scaffold now includes a first bar-derived affine `\mathfrak{sl}_2`
  seed: generator-level simple-pole brackets and normalized double-pole pairing
  are extracted from `compute/lib/bar_complex.py` (`sl2_algebra()`), giving a
  non-toy dg-Lie / cyclic-checkpoint for Step 2.
- The same MC2 module now reaches first nontrivial Step 3 input:
  an `\eta`-valued cyclic `l_3` seed from the Killing cocycle
  `\phi(a,b,c)=\langle [a,b],c\rangle`, with mixed-parameter residual probe
  `l_3(xe,yh,zf)` and CE-closure/nontriviality checks in the test lane.
- MC2 now also has a shared transfer layer from generator seeds to the first
  higher bracket:
  `build_cyclic_l3_marker_extension_from_seed(...)` lifts any cyclic seed
  (`l_2` + pairing) to an `\eta`-valued Killing `l_3` channel, and
  `cyclic_ce_profile_from_cyclic_seed(...)` computes cyclic CE dimensions
  directly from the same seed data.  The specialized `sl_2`, `sl_3`, and
  `sp_4` `l_3` builders now route through this common path.
- The MC2 module now also includes a first Step-4 completion/clutching surrogate:
  genus-indexed completed tensor convolution as a `\widehat{\otimes}` proxy,
  boundary clutching projection via `l_2`, and an explicit boundary-factorized
  compatibility check (`6\omega + 22q\omega + 20q^2\omega` in the toy model),
  together with truncated completed-series MC residual checks.
  The same lane now verifies completed cyclicity for `l_2`/`l_3` on
  genus-indexed series and runs a first symbolic truncated completed-MC
  solve branch (for the toy ansatz with fixed `a_0=1`, forcing `a_1=a_2=0`).
  It now also includes a genus-stratified obstruction extractor
  (`O_g` from lower genera under zero genus-0 sector) and a recursive
  branchwise solver for the same ansatz class, including explicit
  inconsistent-branch detection (fixed `a_0=2` gives no solution branch).
  The same lane now also has multi-basis completed-MC solvers
  (truncated + recursive): on the toy basis `(\theta,\omega)`,
  fixing `\theta_0=1` forces `\theta_g=0` for `g>=1` while leaving
  `\omega_g` as explicit free completed coefficients.
  It now also includes a suspension-shifted symmetric
  `sl_2` `l_3` seed representative with nontrivial mixed MC channel
  (`\eta=-2xyz` on `(e,h,f)`) and explicit nonzero positive-genus
  obstruction outputs at genera `2` and `3` on
  `\alpha_1=e+h+f`.
  The same shifted-seed nontriviality lane now extends to
  `sl_3`, `sp_4`, and `g_2`: on `(e1,e2,f12)` the mixed residual channel is
  `\eta=xyz` for `sl_3`, `\eta=2xyz` for `sp_4`, and `\eta=3xyz` for `g_2`,
  with genus-3 obstruction outputs `\eta`, `2\eta`, and `3\eta`.
  The same lane now exposes a direct one-channel normalization profile:
  for `sl_2`, `sl_3`, `sp_4`, and `g_2`, the genus-3 `\eta` obstruction equals
  the mixed residual value at `(1,1,1)`, so the extracted normalization
  ratio is uniformly `1`.
  The same profile now has a symbolic scaling law:
  with `\alpha_1=t\sum b_i`, genus-2 obstruction terms scale as `t^2`
  and the genus-3 `\eta` channel is exactly
  `O_3^\eta(t)=t^3\,\eta(1,1,1)` in all four lanes.
  On the root-string channel `(e1,e2,f12)` for
  `sl_3/sp_4/g_2`, the same scaling data now satisfies the explicit
  signature law `O_2=t^2(e12+f1-m f2)`, `O_3^\eta=m t^3\eta`,
  equivalently `O_3^\eta=-t\,O_2^{f2}`, with `m=1,2,3`.
  The same signature law is now lifted to a symbolic one-parameter
  root-string family (`m` formal): the shifted obstruction identities
  are verified as polynomial identities in `(m,t)`, and the sampled
  specializations `m=1,2,3` coincide with the concrete
  `sl_3/sp_4/g_2` profiles exactly.
  The same root-string lane now also has a symbolic seed-packet lift
  with free parameters `(a,b,m)`:
  `[e1,e2]=a e12`, `[e2,f12]=b f1`, `[e1,f12]=-m f2`,
  `\langle e12,f12\rangle=m`.
  Its shifted profile is
  `O_2=t^2(a\,e12+b\,f1-m\,f2)`, `O_3^\eta=a m t^3\eta=-a t\,O_2^{f2}`;
  the genus-3 `\eta` obstruction is independent of the free `f1`
  packet coefficient `b`.
  The same packet law now has an explicit projector check:
  on shifted `sl_3/sp_4/g_2` and family samples `m=1,2,3`,
  extracting the visible low-arity packet
  (simple-pole `l_2` scales + root-string pairing scale) and
  rebuilding the packet seed reproduces
  `\eta(1,1,1)`, genus-2 `O_2`, and genus-3 `O_3^\eta`
  exactly.
  The same root-string packet now also has an inverse
  identifiability check: from obstruction data alone
  (`O_2^{e12}`, `O_2^{f1}`, `O_2^{f2}`, `O_3^\eta`) one recovers the
  packet coefficients `(a,b,m)` and the normalization
  `\eta(1,1,1)=a m`, with `\eta` independent of `b`.
  The same lane now has a canonical transfer round-trip check:
  extracting the packet from shifted seed data, inferring it from
  obstruction data, and reconstructing the packet profile return the
  same `O_2` and `O_3^\eta` channels on
  `sl_3/sp_4/g_2` and family samples `m=1,2,3`.
  The same transfer package now also recovers the first nontrivial
  higher-bracket channel directly: the reconstructed shifted seed
  reproduces the same mixed residual
  `l_3(xe1,ye2,zf12)=\eta(1,1,1)\,x y z`,
  with `\eta(1,1,1)=a m` inferred obstruction-side.
  The same obstruction-side recovery now also reconstructs the shifted
  root-string seed profile at channel level: the recovered seed reproduces the
  source coefficients in the visible channels
  `[e1,e2]\to e12`, `[e2,f12]\to f1`, `[e1,f12]\to f2`,
  `\langle e12,f12\rangle`, and `l_3(e1,e2,f12)\to\eta`.
  On the same visible channels, ordered seed-line support is now
  permutation-rigid in compute: only `(e1,e2,f12)` preserves the full
  `(e12,f1,f2,\eta)` support incidence, both on source seeds and on
  seeds reconstructed obstruction-side.
  The same lane now also realizes the incidence-orbit criterion in
  compute: the visible root-string permutation group realizes the same
  universal three-case orbit table on the tested lanes `m=1,2,3`, and
  the induced support orbits are singleton exactly on
  `(e12,f1,f2,\eta)`, with `e12` the unique normalization-nonzero
  genus-2 singleton.
  The same packet now yields a normalized invariant signature
  `(1,1,-1,1)` on visible incidence channels and normalized pairing
  profile `(e12,f12)/m=1`, `(f1,f12)/m=(f2,f12)/m=0`, uniformly on
  `sl_3/sp_4/g_2` and family `m=1,2,3`.
  Equivalently, the signed seed-character is now one canonical tuple
  `(1,1,-1,1)` together with the same normalization/support indicators
  across all tested lanes.
  It now also satisfies the full symbolic polynomial identities on the
  tested triples: `O_2(\alpha_1)=\frac12\,l_2(\alpha_1,\alpha_1)` and
  `O_3^\eta(\alpha_1)=\eta(x,y,z)=\frac16\,l_3^\eta(\alpha_1,\alpha_1,\alpha_1)`.
  The same shifted `\eta` channel is now explicitly aligned with
  cyclic CE uniqueness (`H^2_{cyc}=\mathbb{C}`) for `sl_2`, `sl_3`,
  `sp_4`, and `g_2`; the extracted coefficient
  `\eta(1,1,1)` also matches the seed Killing 3-cocycle normalization.
  The same genus-1-only ansatz now has explicit support truncation:
  obstructions are nonzero only at genera `2,3`, and vanish for all
  `g>=4` in these shifted arity-`<=3` lanes.
  These normalization/scaling/root-signature/polynomial/CE/support checks are now
  bundled as one executable shifted one-channel criterion package.
- The theorem surface now packages the former MC2 reduction as a
  resolved theorem package rather than a live frontier: the intrinsic
  cyclic `\Defcyc(\cA)` model, the geometric completed tensor /
  clutching realization, and the one-channel normalization input are
  assembled by the printed `MC2` theorems. The live frontier now begins
  with MC3 and MC4, with MC5 downstream.
- The theorem surface now also hardens that last package into a named
  criterion chain: first show via joint clutching restrictions and
  normalized trace that the surviving obstruction lies in the
  tautological line, then build the corresponding one-channel
  Verdier/Lagrangian plane, then lift it through the one-channel PTVV /
  anti-involution criterion on perfect projector subcomplexes, then
  realize that lift by explicit one-channel coderivation subcomplexes
  inside `\Defcyc(\cA)`, then reduce those subcomplexes further to
  finite low-bar-length seed data in
  `\operatorname{CoDer}^{\mathrm{cyc}}(\widehat{\barB}_X(\cA))[1]`,
  then compress that seed data to one distinguished degree-`2`
  cocycle plus finite bar-length-`<=3` correction packets and one
  finite pairing matrix from the minimal seed-packet criterion, then
  identify that packet with the visible low-arity simple-pole bracket
  sector, normalized double-pole pairing matrix, and Killing
  `l_3^\eta` sector, then reduce that visible packet further to a
  canonical transfer package on the one-channel seed spaces consisting
  of one cyclic seed, one shared generator-seed lift producing the
  Killing `l_3^\eta` sector, and one functorial normalization splitting
  off the one-channel cocycle line, then reduce that package further to
  the explicit root-string transfer law
  `O_2=t^2(a e12+b f1-m f2)`, `O_3^\eta=a m t^3\eta`,
  with obstruction-side recovery of `(a,b,m)` and the same
  coefficient-extraction normalization, then reduce that law further to
  a root-string chart forced on the one-channel seed spaces up to
  rescaling of the three seed lines, then reduce that chart statement
  further to intrinsic line detection by
  `l_{2,sp}`, `\beta^{dp}`, `\nu^{sp}`, and the support of
  `(O_2,O_3^\eta)`, then reduce that further to automorphism-rigidity
  of the one-channel support graph, then reduce that further to a
  finite stabilizer computation on the one-channel support graph, then
  reduce that further to a bounded incidence-matrix / orbit-count
  computation on the visible one-channel graph, then reduce that
  further to a universal three-case orbit table for
  `m=1,2,3` / `sl_3, sp_4, g_2`, then collapse that to direct
  lookup/identification against one canonical universal table, then
  collapse that further to the minimal invariant signature packet that
  forces that table, then collapse that further to the universal
  signed seed-character law recovering that packet, then collapse that
  further to the universal two-sign plus normalization-scalar law
  recovering that character, then collapse that further to the
  root-string parity sign plus normalization scalar, then collapse
  that further to the chart-normalized seed scalar, and
  then one normalized scalar comparison with `\kappa(\cA)` fixes the
  normalization.
- Immediate effect: extending MC1 checks to higher conformal weights is now a representation
  data task, not a new linear-algebra scaffolding task.

### First concrete step
```
TARGET: Compute H^2(B-bar(sl2_{-2})) and compare with Omega^2(Op_{PGL2}(D)).

INPUT: The sl2 bar complex at critical level k = -2 (kappa = 0, d^2 = 0).
       We have the bar differential from compute/lib/chiral_bar.py.

COMPUTATION:
1. The PBW filtration on B-bar^2 has associated graded
   gr B-bar^2 = Lambda^2(sl2) tensor S^*(sl2[t^-1]) + sl2 tensor S^*(sl2[t^-1]) + ...
2. The E_1 differential is the CE differential of sl2.
3. H^2(sl2; S^q) for small q can be computed by hand or machine.
4. The oper space for PGL2 is: Op = Spec(C[[t]][z2, z3, ...]) where z_n = Tr(del^n A).
   Its de Rham forms Omega^2 are generated by dz_i wedge dz_j.
5. COMPARE: dim H^2(B-bar^{(n)}(sl2_{-2})) vs dim Omega^2(Op)_n for small weight n.

VERIFICATION: If dims match for n = 2, 3, 4, the pattern is confirmed.
              If they don't match, the conjecture needs refinement.

TOOLS NEEDED: Extension of chiral_bar.py to handle critical-level specialization
              (set k = -2 in existing code). New module: oper_comparison.py.
```

### Success criterion
A proved theorem: H^2(B-bar(sl2_{-2})) = Omega^2(Op_{PGL2}(D)) as graded vector spaces,
with explicit isomorphism via the PBW spectral sequence. This would be the first result
in the derived Langlands direction from bar-cobar.

---

## M2. Root-of-Unity Bar Analysis (Programme II)

### What exists
- Bar complex for affine KM at generic level (chain groups, differentials, curvature)
- Finite-dimensionality at admissible levels (cor:bar-admissible-finiteness)
- Level-shifting Koszul duality g_k^! = g_{-k-2h^v}
- Classical quantum group theory at roots of unity (Lusztig, De Concini-Kac)

### What's missing
**Tool 2.1: Admissible-level bar complex specialization.**
At admissible k = -h^v + p/q, the curvature m_0 is non-zero but takes a special form:
kappa(g_k) = dim(g) * (k + h^v) / (2 * (dim g / rank g)) = dim(g) * p / (2q * (dim g / rank g)).
For rational p/q, this is rational. The bar complex should exhibit periodicity related to
the denominator q.

No existing code can compute the bar complex at a specific admissible level. The current
compute engine has bar complexes at *generic* level (level k is a symbol, not a number).
Specializing requires evaluating the structure constants at specific k and tracking the
resulting linear algebra over Q.

**Tool 2.2: CDG periodicity detection.**
A curved dg-module (M, d, h) with d^2 = h * id has a Z/2-graded structure (even/odd
with respect to the curvature). At roots of unity, we expect a longer periodicity:
B-bar^{n+2q} = B-bar^n as modules. Detecting this requires:
- Computing B-bar^n for enough consecutive n (at least 2q + 2)
- Checking isomorphism of modules (not just dimension matching)
- Tracking the CDG structure (curved differential + module structure)

**Tool 2.3: Quantum group comparison.**
The Lusztig small quantum group u_q(g) at q = e^{pi*i*p/q} has a known bar complex
(computed in the finite-dimensional algebra setting by Ginzburg-Kumar). We need a
comparison tool that:
- Computes Bar(u_q(sl2)) for small q (q^3 = 1, q^4 = 1, q^5 = 1)
- Computes B-bar(sl2_{-2+p/q}) at the same parameters
- Tests for quasi-isomorphism (or explicit chain map)

### First concrete step
```
TARGET: Compute B-bar(sl2_{-2+1/2}) through degree 6 over Q.

INPUT: sl2 OPE structure constants at k = -3/2 (simplest non-trivial admissible level).
       This is k = -h^v + p/q = -2 + 1/2, so p = 1, q = 2.
       The quantum group parameter is q_QG = e^{pi*i*2} = 1 (degenerate!).
       Better: k = -2 + 2/3, so p = 2, q = 3, q_QG = e^{pi*i*3/2}.

COMPUTATION:
1. Specialize the sl2 bar differential matrices (D21, D32, ...) at k = -4/3.
2. Compute homology over Q (exact arithmetic, no floating point).
3. Check: dim H^n(B-bar(sl2_{-4/3})) for n = 1, 2, 3, 4, 5, 6.
4. Separately: compute Ext groups for Rep^fd(U_q(sl2)) at q = e^{2*pi*i/3}.
5. Compare dimensions.

VERIFICATION: If dims match and exhibit period 2q = 6, the KL conjecture
              is confirmed at the simplest non-trivial admissible level.

TOOLS NEEDED: bar_admissible.py — specializes generic bar differential to Q-valued
              at specific rational level. quantum_group_bar.py — bar complex of
              Lusztig's u_q(sl2) for small roots of unity.
```

### Success criterion
A verified dimension match between B-bar(sl2_{-4/3}) and Bar(u_{q=e^{2pi*i/3}}(sl2))
through degree 6, with observed 6-periodicity. This would be first computational
evidence for the KL-from-bar-cobar conjecture.

---

## M3. Fusion Monoidality (Programme III)

### What exists
- Module bar-cobar functor Phi (thm:e1-module-koszul-duality)
- Chain-level modular functor with factorization (thm:chain-modular-functor)
- Heisenberg Fock module fusion: F_lambda boxtimes F_mu = F_{lambda+mu}
- Bar coalgebra coproduct from separating degeneration

### What's missing
**Tool 3.1: Explicit fusion product computation at chain level.**
The fusion product M1 boxtimes_A M2 is defined by coinvariants on a genus-0 curve with
3 punctures. At chain level, this involves:
- Taking the tensor product of B-bar(A, M1) and B-bar(A, M2) as bar complexes
- Applying the separating degeneration map (factorization of M-bar_{0,3})
- Computing the resulting coalgebra structure

For Heisenberg: F_lambda is the Fock module with momentum lambda. The fusion product
is addition of momenta. We need to verify that B-bar(H, F_{lambda+mu}) is quasi-isomorphic
to B-bar(H, F_lambda) tensor B-bar(H, F_mu) with coalgebra structure respected.

**Tool 3.2: Coalgebra coproduct from residues on M-bar_{0,4}.**
The coproduct Delta on the bar coalgebra comes from the boundary divisor Delta_{sep}
of M-bar_{0,4} (two copies of M-bar_{0,3} glued). The explicit map requires:
- The propagator on M-bar_{0,4} = P^1 (the cross-ratio coordinate z)
- Residues as z -> 0 (one degeneration channel) and z -> infinity (dual channel)
- These residues must define a coalgebra map (coassociative, compatible with differential)

### First concrete step
```
TARGET: Verify fusion monoidality for Heisenberg Fock modules F_1, F_1 -> F_2.

INPUT: Heisenberg at level kappa. F_lambda = C[a_{-1}, a_{-2}, ...] with
       a(z) ~ sum a_n z^{-n-1}. Fusion: F_1 boxtimes F_1 = F_2.

COMPUTATION:
1. Compute B-bar(H, F_1) through degree 3: the bar complex of Heisenberg
   with Fock module insertion at a marked point.
2. Compute B-bar(H, F_2) through degree 3.
3. Compute B-bar(H, F_1) tensor B-bar(H, F_1) as a chain complex.
4. Construct the comparison map from (3) to (2) using the separating
   degeneration residues on M-bar_{0,4}.
5. Check: is this a quasi-isomorphism? Is it a coalgebra map?

VERIFICATION: Quasi-isomorphism at degree 1, 2, 3.
              Coalgebra structure compatibility.

TOOLS NEEDED: fock_bar.py — bar complex with Fock module insertions.
              fusion_chain.py — chain-level fusion product from M-bar_{0,4} residues.
```

### Success criterion
A proved theorem for Heisenberg Fock modules: Phi(F_lambda boxtimes F_mu) = Phi(F_lambda)
tensor Phi(F_mu) as coalgebras. This would be the first verified case of fusion
monoidality at chain level.

---

## M4. E_2-Bar Complex (Programme IV)

### What exists
- E_1-bar complex = our chiral bar complex on curves (fully developed)
- E_2-operad = little 2-discs operad (well-known)
- Brieskorn algebra = H*(Conf_k(C)) (Arnold's theorem)
- Totaro's presentation for H*(C-bar_k(R^n)) (generalizes Arnold)
- Ayala-Francis NAP duality (infinity-categorical, not chain-level)

### What's missing
**Tool 4.1: E_2-bar complex definition.**
For an E_2-algebra A (an algebra over the little 2-discs operad), the bar complex
should be:
   B-bar_2(A) = bigoplus_n Gamma(C-bar_n(R^2), A^{boxtimes n} tensor Omega^*_log)

where Omega^*_log are logarithmic forms on the FM compactification of C_n(R^2).

The key difference from n = 1:
- Arnold generators w_{ij} = d log(z_i - z_j) are 1-forms (real codimension 1)
- For n = 2: the collision divisors have real codimension 2, so the propagator is a
  1-form (not 0-form). The linking sphere is S^1.
- The "residue" is now an integral over linking S^1, not an algebraic residue.

**Tool 4.2: E_2-OPE (factorization operations on surfaces).**
An E_2-algebra has binary operations parametrized by Conf_2(R^2) = R^2 \ {0},
not Conf_2(R^1) = R \ {0}. The "OPE" is not a Laurent expansion in one variable
but a configuration in the plane. The radial part gives the usual z^{-n} poles;
the angular part gives *new* structure not present in the chiral case.

**Tool 4.3: d^2 = 0 via Totaro relations.**
Arnold relations (w_{ij} wedge w_{jk} + w_{jk} wedge w_{ki} + w_{ki} wedge w_{ij} = 0)
are replaced by Totaro relations for H*(C-bar_k(R^2)):
   w_{ij}^2 = 0 (the 1-forms are nilpotent)
   w_{ij} w_{jk} + w_{jk} w_{ki} + w_{ki} w_{ij} = 0 (same cyclic relation)
but now w_{ij} are degree-1 classes (in R^2 they have cohomological degree 1),
so the signs are different.

### First concrete step
```
TARGET: Define and compute B-bar_2 for the free E_2-algebra on one generator.

INPUT: Free E_2-algebra on generator x of degree 0.
       This is the "E_2 tensor algebra" = bigoplus_n H_*(Conf_n(R^2)) tensor x^{tensor n}.

COMPUTATION:
1. Write down the Brieskorn presentation for H*(Conf_n(R^2)) for n = 2, 3, 4.
2. Define the E_2-bar differential using linking integrals.
3. For degree 2: B-bar^2 = H*(Conf_2(R^2)) tensor x^2 = H^1(S^1) tensor x^2.
   The differential d: B-bar^2 -> B-bar^1 should be the E_2-multiplication.
4. For degree 3: use Totaro relations to check d^2 = 0.
5. Compare with known E_2-Koszul duality: the Koszul dual of the free E_2-algebra
   on x is the free E_2-coalgebra on x[-1] (desuspension).

VERIFICATION: d^2 = 0 at degrees 2, 3. Cohomology matches E_2-Koszul dual.

TOOLS NEEDED: e2_bar.py — E_2 bar complex using Brieskorn algebra.
              totaro.py — Totaro relations for configuration space cohomology.
```

### Success criterion
A working E_2-bar complex for free algebras that reproduces known E_2-Koszul duality
results. This is the proof-of-concept for the n >= 2 programme.

---

## M5. Holomorphic-to-Real Propagator Comparison (Programme V)

### What exists
- Genus-0 weight systems match Bar-Natan (prop:vassiliev-genus0)
- Holomorphic propagator w_{ij} = d log(z_i - z_j) on C
- Kontsevich propagator w^K_{ij} = (1/2pi) d arg(t_i - t_j) on S^1
- Feynman transform identification (thm:prism-higher-genus)

### What's missing
**Tool 5.1: Restriction functor from C-bar_n(Sigma_g) to C_n(S^1).**
The key computation: embed S^1 -> Sigma_g (as a cycle) and restrict configuration
spaces. The holomorphic propagator on Sigma_g restricts to a real 0-form on S^1.
The question: does this restriction send bar complex cohomology to the Kontsevich
integral?

For genus 0: S^1 embeds in P^1 as the unit circle. The restriction
d log(z_i - z_j)|_{|z|=1} = d arg(z_i - z_j) + i * d log|z_i - z_j|
has real part = Kontsevich propagator (up to normalization) and imaginary part
= log of distance. The imaginary part integrates to zero on closed diagrams.

**Tool 5.2: Higher-genus propagator restriction.**
For genus g >= 1, the propagator is ω(z,w) = d_z log E(z,w) where E is the prime form.
On the real locus (if it exists), this restricts to a real propagator.
The question: does the real part of the genus-g propagator on the Schottky real locus
give the appropriate extension of the Kontsevich integral to surfaces?

### First concrete step
```
TARGET: Verify that restriction to S^1 of the genus-0 sl2 bar complex
        reproduces the first three Vassiliev invariants v_2, v_3, v_4.

INPUT: The genus-0 bar complex of sl2 at level k.
       Configuration spaces C_n(P^1) with S^1 = {|z| = 1} embedded.

COMPUTATION:
1. For n = 2 chords (degree 4 of Kontsevich integral):
   Integrate w_{12} w_{34} over C_4(S^1) (ordered configurations on the circle).
   Should give the coefficient of the trefoil knot in v_2.
2. For n = 3 chords (degree 6):
   Integrate products of w_{ij} over C_6(S^1).
   Compare with known v_3 values.
3. The sl2 weight system W_Gamma for each chord diagram Gamma contributes
   Tr(ad^{2n}) = known Casimir eigenvalues. Verify these match.

VERIFICATION: Agreement with tabulated Vassiliev invariants (Bar-Natan tables).

TOOLS NEEDED: circle_restriction.py — restricts FM propagator to S^1 configurations.
              vassiliev_tables.py — known Vassiliev invariant values for comparison.
```

### Success criterion
Numerical agreement of the restricted bar complex integrals with known Vassiliev
invariants for the trefoil and figure-eight knots, confirming the genus-0 comparison.

---

## M6. BRST-Bar Identification (Programme VI-a: Anomaly)

### What exists
- thm:anomaly-koszul: kappa-additivity, c = 26 criticality (PROVED)
- Bar complex differential = sum of OPE residues
- BRST differential = sum of ghost-matter OPE contractions
- Structural analogy: log forms ~ ghosts, Arnold relations ~ ghost algebra

### What's missing
**Tool 6.1: Explicit dg-algebra isomorphism B-bar^ch(A) -> C*_BRST(A tensor Diff(X)).**
The structural analogy between log forms and ghosts needs to be promoted to an explicit
chain map. The key identifications:
- Generator eta_{ij} = d log(z_i - z_j) <-> ghost field c(z_i) c(z_j)
- Arnold relation <-> ghost number conservation
- Bar curvature m_0 = kappa <-> BRST anomaly (c - 26)/12

This requires defining both sides precisely for the same algebra and constructing the map.

**Tool 6.2: Costello-Gwilliam perturbative QFT framework interface.**
At genus g >= 1, the BRST complex involves path integral measure contributions.
Costello's renormalization formalism (Costello, "Renormalization and Effective Field
Theory") provides the mathematical framework for perturbative BRST at higher genus.
The bar complex at genus g is defined via configuration spaces on Sigma_g.
The identification requires showing that Costello's counterterm expansion matches
the bar complex spectral sequence.

### First concrete step
```
TARGET: Construct explicit isomorphism for the bosonic string (A = Heisenberg^26).

INPUT: Heisenberg algebra H of rank 26 (26 free bosons).
       Ghost system: bc ghosts (c_ghost = -26, so c_total = 0).
       BRST complex: C*_BRST = H^26 tensor bc with Q_BRST = oint c(z)(T_matter + T_ghost/2).

COMPUTATION:
1. The bar complex B-bar(H^26 tensor bc) at genus 0.
   Generators: 26 bosonic + 2 ghost. Bar differential from OPE residues.
2. The BRST complex C*_BRST(H^26, bc) at genus 0.
   This is the semi-infinite cohomology complex.
3. Define the chain map Phi: B-bar -> C*_BRST by:
   - eta_{ij} |-> c_1 c_0 (the zero-modes of the ghost)
   - bar differential d_bar |-> [Q_BRST, -]
   - Show Phi d_bar = Q_BRST Phi
4. At genus 0: both sides compute the same thing (Feigin semi-infinite cohomology
   = bar complex cohomology). The map should be an explicit quasi-isomorphism.

VERIFICATION: Phi is a chain map. Phi induces isomorphism on H^0.
              kappa(H^26 tensor bc) = 0 iff c = 26 (already proved).

TOOLS NEEDED: brst_complex.py — explicit BRST differential for bosonic string.
              bar_brst_comparison.py — chain map construction and verification.
```

### Success criterion
An explicit chain map B-bar(H^26 tensor bc) -> C*_BRST at genus 0, proved to be a
quasi-isomorphism. This would upgrade conj:anomaly-physical to ProvedHere at genus 0.

---

## M7. Holomorphic-Topological Identification (Programme VI-b,c: AdS3, HCS, AGT)

### What exists
- Curved A-infinity on bar complex (thm:bar-ainfty-complete)
- Genus expansion (thm:genus-universality)
- Complementarity (thm:quantum-complementarity-main)
- Costello-Paquette conjecture relating curved Koszul duality to twisted SUGRA
- AGT: 4d partition functions = W-algebra conformal blocks (physics, established)

### What's missing
**Tool 7.1: Twisted supergravity observable algebra from bar complex.**
CP2020 conjectures B-bar(A) computes twisted SUGRA observables. To verify:
- Need the explicit algebra of observables of Costello-Li twisted SUGRA on AdS3
- This is a Costello-Gwilliam factorization algebra on the 3-manifold AdS3
- The claim: this factorization algebra, restricted to the boundary S^2, is B-bar(A)
- First test case: A = Kac-Moody at level k. Twisted SUGRA = Chern-Simons with
  gauge group G_C on AdS3. Boundary WZW observables should match B-bar(g_k).

**Tool 7.2: Holomorphic Chern-Simons operad.**
The chiral operad P_HCS from holomorphic Chern-Simons on a 3-fold Y with boundary X
should define, via its boundary restriction, a chiral algebra on X. This requires:
- Costello-Gwilliam perturbative quantization of HCS on Y
- Boundary operator algebra extraction
- Comparison with bar complex of the resulting chiral algebra

**Tool 7.3: AGT chain-level realization.**
The AGT correspondence (Nekrasov partition function = W-algebra conformal blocks)
should have a chain-level avatar:
- 4d instanton moduli space M_G = moduli of G-instantons on C^2
- Equivariant cohomology H*_T(M_G) = W-algebra module (Schiffmann-Vasserot)
- Bar complex should provide chain-level refinement:
  B-bar(W_k) should compute equivariant chains on M_G

### First concrete step
```
TARGET: Verify that B-bar(sl2_k) at genus 0 matches the Chern-Simons
        observable algebra on the solid torus (boundary = torus T^2).

INPUT: SL2 Chern-Simons at level k on the solid torus D^2 x S^1.
       Boundary theory: sl2 WZW on T^2.

COMPUTATION:
1. CS observable algebra on D^2 x S^1:
   The flat connections are representations of pi_1(D^2 x S^1) = Z in SL2.
   These are diagonal: A = diag(theta, -theta), parametrized by theta in [0, 2pi].
   Quantization: the space of states is H^0(M_flat, L^k) = chi_k(SL2) (characters).
2. Bar complex B-bar(sl2_k) at genus 0:
   H^0(B-bar) = sl2-coinvariants = center of U(sl2) / (level k relations).
   At positive integer k: finite-dimensional, dim = k+1 (integrable reps).
3. Compare: dim H^0(B-bar(sl2_k)) vs dim H^0(CS on solid torus) = k+1.

VERIFICATION: Dimension match for k = 1, 2, 3, 4.
              Structure match (ring isomorphism, not just dimensions).

TOOLS NEEDED: cs_observables.py — Chern-Simons observable algebras for simple cases.
              bar_cs_comparison.py — comparison functor.
```

### Success criterion
Proved ring isomorphism H^0(B-bar(sl2_k)) = H^0(CS(SL2, k)) for the solid torus.
This would be the first concrete verification of the bar-cobar / gauge theory
correspondence and would partially upgrade conj:ads-cft-bar.

---

## M7b. Factorization Drinfeld-Kohno Ladder (Programme II / VI-d interface)

### What exists
- chain-level DK shadows for affine and Yangian settings with
  `q \mapsto q^{-1}` / `R \mapsto R^{-1}`;
- an evaluation-locus factorization theorem in the Yangian chapter;
- the ordered-configuration / braid-reversal viewpoint already isolated
  in the finite RTT story; and
- theorematic standard-RTT completed M-level packages for the standard
  Yangian towers.

### What's missing
**Tool 7b.1: intrinsic ordered factorization category.**
Define the ordered factorization category on the evaluation locus with
interval-factorization descent, braid-monodromy compatibility, and the
correct Verdier-opposite involution.

**Tool 7b.2: factorization Kazhdan functor.**
Construct `KZ_fact` on that ordered category and prove compatibility
with ordered fusion, braid transport, and the bar-cobar involution.

**Tool 7b.3: extension beyond evaluation modules.**
Isolate the four exact extra inputs:
Yangian Koszulness or replacement resolution theory,
RTT-complete bar control,
generation by evaluation objects after completion,
and a Barr-Beck style reconstruction theorem.

**Tool 7b.4: dg-shifted Yangian comparison.**
After the factorization ladder is explicit, compare the resulting
ordered factorization target with the dg-shifted Yangian / line-operator
target at the intended H-level rather than collapsing them into one
premature slogan.

### First concrete step
```
TARGET: Rewrite the monolithic DK package as a staged theorem ladder.

LADDER:
1. DK-0: chain-level evaluation-locus shadow on standard evaluation objects;
2. DK-1: ordered factorization category on the evaluation locus;
3. DK-2: factorization Kazhdan functor KZ_fact;
4. DK-3: extension beyond evaluation modules using Koszul/generator/monadic input;
5. DK-4: full ordered E1-factorization equivalence;
6. DK-5: dg-shifted Yangian / line-operator comparison at the H-level target.

VERIFICATION:
- each rung states exact hypotheses and output;
- evaluation-locus results are not advertised as full category-O theorems;
- the dg-shifted comparison is kept visibly downstream of the ordered
  factorization lift.
```

### Success criterion
A staged DK programme in which the evaluation-locus theorem is the
first proved rung, the extension beyond evaluation modules is an exact
input list rather than a slogan, and the dg-shifted Yangian comparison
is fenced as its own downstream H-level target.

---

## M8. Infinite-Generator Koszul Duality (Programme VI-d: W-infinity, Higher-Spin)

### What exists
- Koszul duality for finitely-generated quadratic chiral algebras (complete theory)
- Bar complexes for all finite-generator algebras in Master Table
- Principal finite-type `W_N` higher-genus PBW / modular Koszul package theorematic at completed M-level
- Virasoro (1 generator), W_3 (2 generators), W_N (N-1 generators) computed
- Conjectured: Virasoro^! = W_infinity, W_N^! = Yangian Y(gl_N)
- The standard principal-stage `W_\infty` tower now has its theorematic
  standard-tower completed M-level bar-cobar package.
- The standard RTT Yangian tower now has its theorematic standard-RTT
  completed M-level bar-cobar package.
- Formal H-level comparison criteria are now proved: once a filtered
  target has the correct finite quotients, comparison with the
  corresponding standard tower is automatic.
- The remaining finite-stage identification problems are now reduced to
  explicit coefficient identities plus finite detection.

### What's missing
The live `W` gap is not finite-type principal `W_N`, and it is no
longer the bare existence of a completed bar construction.  The live
MC4 package is now exact:

1. build the filtered H-level targets beyond the theorematic standard
   towers;
2. prove the named mode identities on the finite quotients; and
3. close the finite-detection reductions that promote those identities
   from generator seeds or evaluation families to the full quotient
   package.

**Tool 8.1: `W_\infty` factorization target plus residue-coefficient package.**
The remaining `W_\infty` task is to construct a principal-stage
compatible factorization target whose finite quotients recover the
principal Drinfeld--Sokolov stages.  The completion scaffold is already
in place; what is missing is the actual higher-spin coefficient data
and its exact comparison with the finite-type stages.

Concretely, one needs:
- explicit higher-spin structure constants for the first finite-spin
  windows;
- extraction of the local residue/OPE coefficients
  `C^{res}_{s,t;u;m,n}(N)`;
- proof of the stagewise identities
  `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)`; and
- generator-seed detection plus translation closure so finitely many
  primary coefficients determine all descendants.

**Tool 8.2: Yangian one-loop kernel package.**
The remaining Yangian task is to construct the RTT-adapted filtered
target and identify its finite quotients with the theorematic RTT
stages by exact kernel comparison, not by a generic convergence slogan.

Concretely, one needs:
- extraction of the one-loop line-operator kernel coefficients
  `K^{line}_{a,b}(N)` from the rational formulas;
- comparison with the truncated RTT coefficients
  `K^{RTT}_{a,b}(N)`;
- compatibility with the standard evaluation-module formulas; and
- faithful-evaluation detection so vanishing of the defect family on
  tensor products of fundamental evaluation modules forces equality in
  the quotient.

**Tool 8.3: H-level comparison lift beyond the standard towers.**
After the finite quotients satisfy the exact coefficient identities, the
remaining comparison step is to build the filtered H-level targets whose
finite quotients recover those identified stages and then apply the
inverse-limit comparison theorem.  The frontier issue is therefore not
principal-stage bar data; it is the actual factorization / dg-shifted
realization carrying the already-identified finite quotients.

### First concrete step
```
TARGET: Verify the first nontrivial MC4 finite-detection identities on
        small principal stages.

INPUT:
1. Principal Drinfeld--Sokolov coefficients for the first finite
   `W_N` stages.
2. One-loop line-operator kernels for the first truncated RTT stages.

COMPUTATION:
1. On the `W_\infty` side, extract the generator-level residue
   coefficients `C^{res}_{s,t;u;0,n}(N)` for the first visible
   principal stages.
2. Compare those primary coefficients with the principal
   Drinfeld--Sokolov coefficients `C^{DS}_{s,t;u;0,n}(N)`.
3. Use translation closure to propagate the equality to descendant
   coefficients `C^{res}_{s,t;u;m,n}(N)`.
4. On the Yangian side, extract the first one-loop kernel coefficients
   `K^{line}_{a,b}(N)` and compare them with
   `K^{RTT}_{a,b}(N)`.
5. Test the Yangian defect family on tensor products of fundamental
   evaluation modules.

VERIFICATION:
- exact equality of the first visible `W_\infty` generator coefficients
  with the DS coefficients;
- exact equality of the first visible Yangian kernel coefficients with
  the truncated RTT coefficients;
- vanishing of the Yangian defect family on the chosen faithful
  evaluation family.

TOOLS NEEDED:
- `w_infinity_ope.py` upgraded from support scaffolding to explicit
  residue-coefficient extraction;
- a Yangian kernel-extraction module for the one-loop rational formulas;
- an evaluation-family verifier for the finite RTT quotients.
```

Status update (Mar 9, 2026): the old pro-nilpotent completion scaffold in
`compute/lib/pronilpotent_bar.py` is now supporting infrastructure rather than
the live MC4 bottleneck.  On the `W_\infty` side,
`compute/lib/w_infinity_ope.py` already provides a structural finite-spin
scaffold: exact stress-tensor action, truncated singular-support bounds, and
adjacent-merge maps compatible with the weight filtration, while
`compute/lib/w_infinity_support_complex.py` enumerates finite target sets and
support matrices at fixed weight.  What remains open is the actual
higher-spin coefficient extraction and the comparison with the principal
Drinfeld--Sokolov coefficients.  On the Yangian side, the missing compute
surface is now the one-loop kernel-extraction and faithful-evaluation
detection package, not a first completion theorem.

### Success criterion
An executable MC4 package in which:
1. the first visible `W_\infty` residue identities and Yangian kernel
   identities are checked exactly;
2. the finite-detection layers are implemented concretely on
   generator-level seeds and faithful evaluation families; and
3. the resulting finite quotients are ready to feed into the filtered
   H-level comparison targets beyond the already theorematic
   standard-tower M-level packages.

---

## M9. Computational Scale-Up (Programme IX)

### What exists
- Exact bar cohomology for 5 algebras with closed-form GFs (Heis, F_2, bc, sl2, Vir)
- Closed-form GF for betagamma (OEIS A025565)
- Partial data: sl3 (3 pts), W3 (4 pts), Y(sl2) (3 pts)
- Python compute engine with 1472 tests

### What's missing
**Tool 9.1: Sparse linear algebra for bar cohomology.**
The sl3 bar complex at degree 4 has chain groups of dimension 786432 (= 8^4 * 24^3 / 6,
roughly). The differential matrix D_{4->3} is 786432 x 24576. Computing its kernel and
image requires sparse linear algebra over Q (exact arithmetic).

Current Python (sympy) cannot handle this. Options:
- SageMath: Has sparse matrix rank computation over Q via linbox. Can handle 10^5 x 10^4.
- FLINT/Arb: C library for exact linear algebra. Much faster.
- Magma: Commercial, but has best-in-class sparse kernel computation.
- Reduction modulo primes: compute rank mod p for several primes p, reconstruct exact rank.
  Much faster than exact computation.

**Tool 9.2: Modular arithmetic approach.**
Instead of computing dim H^4(B-bar(sl3)) over Q, compute dim H^4 mod p for
p = 2, 3, 5, 7, 11, 13, ..., 97. If all give the same dimension, that dimension
is correct (with overwhelming probability). This reduces the problem to linear
algebra over F_p, which is vastly faster.

**Tool 9.3: Structure exploitation for W3.**
The W3 bar complex has non-KM structure: two generators T (weight 2) and W (weight 3)
with complicated quartic OPE W(z)W(w). The bar differential involves composite fields
(e.g., :TT: appears in W*W OPE). This requires tracking the full OPE including
composite field contributions, which the current code partially handles (w3_bar.py).

The degree-5 computation needs:
- All bar-5 elements (products of 5 generators from {T, W})
- The bar-4 to bar-5 and bar-5 to bar-4 differentials
- Chain groups: 2^5 = 32 generator-type combinations, times OS forms

### First concrete step
```
TARGET: Compute dim H^4(B-bar(sl3)) mod p for p = 2, 3, 5, 7, 11.

INPUT: sl3 structure constants (8 generators: H1, H2, E1-E3, F1-F3).
       Killing form kappa_{ab}. OPE poles (double + simple).

COMPUTATION:
1. Enumerate all bar-4 elements: 8^4 * |OS^4| generator-type combinations
   tensor Orlik-Solomon forms of degree 4.
   |OS^4| on 4 elements: need to compute from Arnold presentation.
2. Construct the differential matrix D_{4->3} over F_p.
   Each entry is a polynomial in k (level) evaluated mod p.
3. Compute rank(D_{4->3}) and rank(D_{5->4}) mod p.
4. dim H^4 = dim ker(D_{4->3}) - dim im(D_{5->4}) mod p.
5. If all 5 primes give the same answer, that's the answer.

VERIFICATION: Check consistency with dim H^3 = 204 (known).
              The Euler characteristic sum (-1)^n dim H^n should match
              the known alternating sum from the generating function.

TOOLS NEEDED: bar_modular.py — bar differential over F_p.
              sparse_rank.py — sparse matrix rank over F_p (using numpy or scipy).
              os_forms.py — Orlik-Solomon algebra generators and relations.
```

### Success criterion
dim H^4(B-bar(sl3)) computed and verified. This either confirms or refutes the
OEIS A030112 match (predicted: 1086) and provides the fourth data point needed
to conjecture the generating function.

---

## M10. Holographic Dictionary Formalization (Programme VI-b: AdS3/CFT2)

### What exists
- conj:ads-cft-bar: full conjecture statement (concordance.tex)
- Curved A-infinity bar complex models bulk gravity
- Curvature m_0 = kappa encodes cosmological constant
- Genus expansion = 1/N expansion
- Costello-Paquette framework for twisted supergravity

### What's missing
**Tool 10.1: Twisted supergravity algebra of observables.**
Costello-Li define twisted supergravity on a 3-manifold Y as a perturbative
field theory in the Costello-Gwilliam formalism. The algebra of observables is
a factorization algebra on Y. We need:
- The explicit factorization algebra for SL(2,C) CS on AdS3 = H^3
  (hyperbolic 3-space)
- Its restriction to the boundary S^2 = del(AdS3)
- Comparison with the bar complex of the boundary WZW/Virasoro

**Tool 10.2: Bulk-boundary map as bar-cobar adjunction unit.**
The unit of the bar-cobar adjunction eta: A -> Omega(B-bar(A)) is the
cobar-bar augmentation map. In the holographic context, this should be the
bulk-to-boundary map: given a boundary operator O in A, eta(O) is the
corresponding bulk field in Omega(B-bar(A)).

The counit epsilon: B-bar(Omega(C)) -> C is the boundary-to-bulk map:
given a bulk coalgebra element, epsilon extracts the boundary observable.

For this to be the holographic dictionary, need:
- The unit/counit maps to preserve the physical data (conformal dimensions,
  spins, correlation functions)
- The genus expansion to correspond to the 1/N expansion on the bulk side

**Tool 10.3: Central charge / cosmological constant dictionary.**
The identification kappa ~ c/2 ~ R_AdS^2 / ell_P^2 needs:
- R_AdS = radius of curvature of AdS3
- ell_P = Planck length
- For SL(2) CS at level k: R_AdS^2 / ell_P^2 = k (the CS level)
- Our kappa(sl2_k) = 3k/4
- So kappa = (3/4) * R_AdS^2 / ell_P^2

This gives a precise numerical dictionary, not just a proportionality.
Need to verify this against known AdS3/CFT2 results (BTZ black hole
entropy, etc.).

### First concrete step
```
TARGET: Verify the kappa / cosmological constant dictionary for BTZ black holes.

INPUT: BTZ black hole in AdS3 with R_AdS = sqrt(k * ell_P^2).
       Bekenstein-Hawking entropy S_BH = pi r_+ / (2 G_3).
       Brown-Henneaux: c = 3 R_AdS / (2 G_3).
       Cardy formula: S_CFT = (pi^2 / 3) c T = pi sqrt(c E / 6).

COMPUTATION:
1. Our genus-1 free energy: F_1 = kappa * lambda_1 = kappa / 24.
   For sl2_k: F_1 = k/32.
2. The CFT partition function at genus 1: Z = |eta(tau)|^{-2c}.
   The free energy = -log Z = c * (pi / 12) * Im(tau) + ...
3. At the BTZ saddle (tau = i * beta / (2pi R_AdS)):
   F_1^CFT = c / 24 * beta / R_AdS = (k * dim(g) / (k + h^v)) / 24 * beta / R_AdS
4. Our F_1 = kappa / 24 = 3k / (4 * 24) = k / 32.
5. Compare: CFT gives c/24 = (3k/(k+2))/24, we give k/32.
   At large k: c/24 ~ k/8, our kappa/24 = k/32.
   Ratio: 4/1. This factor should be dim(sl2)/rank(sl2) = 3/1 ... investigate.

VERIFICATION: Either the ratio is explained by a known factor (e.g., sigma(g)),
              or the dictionary needs refinement.

TOOLS NEEDED: btz_dictionary.py — BTZ thermodynamics from Chern-Simons level.
              genus1_comparison.py — compare F_1 with CFT partition function.
```

### Success criterion
A precise numerical dictionary between kappa and AdS3 radius, verified against
BTZ black hole entropy. This would turn part of conj:ads-cft-bar from speculation
to quantitative prediction.

---

## M11. W-Algebra Nilpotent Orbit Duality (Programme VIII-a)

### What exists
- Principal case proved: W^k(g)^! = W^{k'}(g) for principal f (thm:w-algebra-koszul-main)
- DS reduction commutes with bar complex (thm:ds-koszul-intertwine)
- Barbasch-Vogan duality for nilpotent orbits (classical, representation theory)
- Feigin-Frenkel duality k <-> -k-2h^v for principal f
- Type-A hook/subregular orbit scaffold implemented in
  `compute/lib/nonprincipal_ds_orbits.py`: partition transpose duality,
  orbit/centralizer dimension identities, frontier catalog, and an
  orbit-indexed non-principal level-shift data path. Full compute suite passes
  against this scaffold.
- The same module now also includes the first non-hook family scaffold:
  type-A two-row non-hook cases `(n-s,s)` (`s\ge 2`) with dual partition
  propagation, matrix/sl2-triple checks, and catalog-level verification.
- BV orbit-pair seed implementation added in `compute/lib/bv_duality.py`,
  including the first genuinely non-self-dual hook pair detector
  (`A_3`: `(3,1) \leftrightarrow (2,1,1)`).
- Non-principal DS seed reduction layer added in
  `compute/lib/nonprincipal_ds_reduction.py`: proved `sl_3` subregular
  Bershadsky--Polyakov seed (`(2,1)` self-dual orbit, `k'=-k-6`) plus hook
  seed records for the first non-self-dual case.

### What's missing
The live non-principal frontier is now packetized into three exact
tasks, not one undifferentiated conjectural mass.

**Packet 11.A: Paired non-principal DS seed transport/globalization.**
For non-principal nilpotent `f`, the DS reduction `W^k(g,f)=H^0_BRST(g_k,f)`
uses a non-standard BRST complex. The BRST charge `Q_f` depends on the
`\mathfrak{sl}_2`-triple containing `f`, and the reduction is more complex:
- The grading on g is by the eigenvalues of ad(h) where {e, h, f} is the sl2-triple
- The "good" grading may differ from the Dynkin grading
- The BRST complex has generators in degrees determined by the grading

Current status: the `sl_3` subregular seed and the first non-self-dual
hook pair already have explicit truncated seed complexes, survivor data,
and witness-level transport checks.

Need: extend those paired seed complexes and their transport maps beyond
the present hook/subregular theorematic seeds, and globalize agreement of
survivor brackets, cohomology profiles, and normalization data on dual
orbit pairs.

**Packet 11.B: Dual-orbit input.**
For a nilpotent orbit O in g, the BV dual orbit O^D in g (or g^L for non-simply-laced)
is defined by:
- Take the special piece containing O
- Take the "opposite" orbit in the Lusztig-Spaltenstein correspondence
- For simply-laced g: O^D is in g itself. For non-simply-laced: O^D is in g^L.

Current status: a seeded type-A BV database is already live, including
the first genuinely non-self-dual hook pair.

Need: extend the dual-orbit input beyond the current seeded type-A
catalog, including the component-group compatibilities needed by the
printed conjecture.

**Packet 11.C: Orbit-indexed non-principal level shift.**
For principal f, the dual level is k' = -k - 2h^v. For non-principal f, the
formula is expected to be:
   k' = -k - 2h^v + (something depending on f)
The "something" involves the Dynkin labels of f and the dual Coxeter number.

Current status: the level-shift scaffold is already orbit-indexed in
type A, with seeded non-hook corrections and verifier wiring.

Need: determine and verify the orbit-indexed rule `k'=k'(k,f)` beyond
the current seeded correction table and align it with the normalization
bridge used by the chapter-level statements.

Status update (Mar 8, 2026, twelfth pass): the level-shift scaffold is now
orbit-indexed (`nonprincipal_orbit_level_shift_type_a`) rather than a single
hook-only ansatz callsite, with an explicit correction-data hook keyed by
partitions. Seeded non-hook entries are now populated with nonzero
per-orbit corrections (for example `(4,2)` in type A), while the hook/subregular
anchors remain on `k'=-k-2n`; verifier wiring is now live for orbit-specific
correction propagation.

Status update (Mar 8, 2026, fourteenth pass): the same correction layer is now
seeded across the broader type-A non-principal catalog, not only the two-row
examples. The correction hook carries explicit non-hook anchors such as
`(3,3)` and `(3,2,1)`, together with a transpose-invariant seeded fallback on
the remaining non-principal range, and the orbit verifiers now run on the
general `general_nonprincipal` partition catalog as well.

Status update (Mar 7, 2026, second pass): the BP seed formulas currently encoded
in `nonprincipal_ds_reduction.py` produce a level-independent
`c(k)+c(k') = 76` for `k' = -k-6`, and the chapter-level consistency check has
been aligned to that value.

Status update (Mar 7, 2026, third pass): the follow-on scaffolds are now in
place:
- `compute/lib/nonprincipal_ds_normalization.py` encodes the raw/shifted BP
  convention bridge (including the shift-only map to the chapter target sum).
- `compute/lib/ds_reduction.py` records the first chain-level DS inputs for the
  `sl_3` subregular seed (`\mathfrak{sl}_2`-triple, positive grading profile,
  BRST ghost conformal weights).
This isolates the remaining open work to the genuine non-principal correction
term and the full BRST differential realization.

Status update (Mar 8, 2026): the DS chain scaffold is now explicit enough to
launch the BRST differential itself:
- `compute/lib/ds_reduction.py` now records the full subregular `sl_3`
  good-grading basis, the linear DS constraint data, and the target
  Bershadsky--Polyakov presentations.
- The constrained positive nilpotent is verified to be abelian in this seed,
  so the quadratic ghost term vanishes at the symbolic scaffold level.
What remains is no longer "what are the BRST inputs?" but "realize the
resulting BRST differential/cohomology and then move to the first genuinely
non-self-dual hook case."

Status update (Mar 8, 2026, second pass): the first BRST differential layer is
now explicit in compute:
- `compute/lib/ds_reduction.py` now builds a truncated subregular `sl_3`
  seed complex with differential `d = \chi \wedge -` and symbolic
  nilpotence checks (`d^2=0`).
- The same module now builds paired DS seed complexes for the first
  non-self-dual type-A hook pair (`A_3`: `(3,1)` and `(2,1,1)`), again with
  symbolic `d^2=0` verification on both source and target seeds.

Status update (Mar 8, 2026, third pass): the truncated BRST layer now carries
explicit cohomology extraction and specialization:
- `truncated_cohomology_dimensions` and `complex_is_acyclic` are now part of
  the DS scaffold API.
- The subregular specialization (`\chi=(1,0)`) is acyclic at the truncated
  level (`H^0=H^1=H^2=0`).
- Both first-hook-pair specializations (`(1,0)` / `(0,1)` assignments on
  source/target seeds) are acyclic at the same truncated level.

Status update (Mar 8, 2026, fourth pass): the non-principal DS scaffold is now
systematic at the hook/subregular family level:
- `compute/lib/nonprincipal_ds_reduction.py` now includes
  `nonprincipal_hook_seed` and `nonprincipal_hook_seed_catalog`, with explicit
  verification that orbit status tags and level shifts propagate from the
  orbit ledger into the DS seed ledger.
- The same module now carries a type-A hook constraint-count ansatz
  (`hook_constraint_count_ansatz_type_a`, pairwise form included) and
  verification checks, so generic seed sizing is no longer hard-coded; the
  current count rule is extracted from canonical hook `sl_2` triples via
  positive simple-root grades, with `sl_3` subregular anchored to the proved
  two-constraint seed.
- The orbit module now also exposes a concrete hook-pair profile ledger
  (`hook_orbit_pair_profile`, with catalog-level verification), so partition
  duality, orbit/centralizer dimensions, positive graded basis labels, and the
  simple-root count data used by the sizing ansatz are recorded in one place.
- `compute/lib/ds_reduction.py` now includes `hook_pair_ds_seed`,
  `hook_pair_specialized_complexes`, and `hook_pair_ds_seed_catalog`, extending
  the previous first-pair-only truncated complexes to all type-A hook cases up
  to a chosen cutoff.
- The DS pair catalog is now cross-checked against the DS seed catalog
  (`verify_hook_pair_seed_alignment`) so partition/dual-level data is validated
  across modules, not only within each module separately.
- Catalog-level checks now verify symbolic `d^2=0` and acyclic nonzero
  character specializations across the seeded hook/subregular family.

Status update (Mar 8, 2026, fifth pass): the `sl_3` subregular survivor sector
is now explicit:
- `compute/lib/ds_reduction.py` now includes a matrix realization of the
  subregular `sl_3` basis and an explicit `g^f`-based strong-generator
  candidate list.
- The surviving candidates are
  `J ~ H_2 + \frac{1}{2}H_1`, `G^+ ~ E_{23}`, `G^- ~ F_{13}`, `T ~ F_{12}`.
- Their `ad(h)`-grades are `0,-1,-1,-2`, so the induced DS conformal weights
  are exactly `1,\frac{3}{2},\frac{3}{2},2`, matching the
  Bershadsky--Polyakov strong presentation.
- The candidate matrices are verified to centralize `f = F_{12}` explicitly,
  so the subregular seed now has both the exact linear constraint sector and
  the correct surviving strong-field profile.
- The same module now also records the canonical splitting
  `\mathfrak{sl}_3 = [e,\mathfrak{sl}_3] \oplus \mathfrak{g}^f` and the
  induced projection to the strong fields. In particular,
  `H_2 \mapsto J`, `E_{23} \mapsto G^+`, `F_{13} \mapsto G^-`,
  `F_{12} \mapsto T`, while the chosen `[e,\mathfrak{sl}_3]` basis projects
  to zero.
- At the same linearized level, the projected survivor bracket is now
  explicit:
  `[J,G^+] = \frac{3}{2}G^+`, `[J,G^-] = -\frac{3}{2}G^-`,
  `[G^+,G^-] = T`, and `T` is central in the projected bracket.

Status update (Mar 8, 2026, sixth pass): the first genuinely non-self-dual
hook orbit is now concrete on the matrix side:
- `compute/lib/nonprincipal_ds_orbits.py` now includes standard Jordan
  nilpotent representatives for type-A partitions and hook cases, plus
  recovery of the partition from kernel dimensions of powers.
- The first non-self-dual pair (`A_3`: `(3,1)` and `(2,1,1)`) now has explicit
  nilpotent matrices in compute, not only partition labels.
- Matrix centralizer dimensions are now checked directly against the partition
  formula across the hook-family scaffold, so the orbit side of the frontier is
  no longer purely combinatorial.
- The same module now also constructs explicit traceless centralizer bases for
  that first non-self-dual pair, of sizes `5` and `9` respectively, exposing
  the first concrete asymmetry in the dual hook data beyond partition labels.
- Standard Jacobson--Morozov triples for that pair are now also fixed in code,
  with full `ad(h)` grading multiplicities on `\mathfrak{sl}_4`:
  source `(3,1)` gives `{4:1, 2:4, 0:5, -2:4, -4:1}`,
  target `(2,1,1)` gives `{2:1, 1:4, 0:5, -1:4, -2:1}`.
- The standard traceless basis is now also grouped explicitly by `ad(h)` grade,
  so the positive directions for the first hook pair are concrete labels:
  source positive basis `E13` in grade `4` and
  `E12,E14,E23,E43` in grade `2`;
  target positive basis `E12` in grade `2` and
  `E13,E14,E32,E42` in grade `1`.
- `compute/lib/ds_reduction.py` now feeds those actual five positive
  directions on each side into the linear hook-pair Koszul blocks, replacing
  the earlier placeholder two-constraint toy model for the first
  non-self-dual pair.
- The same DS scaffold now attaches the actual ghost conformal weights to
  those five directions:
  source has one grade-4 ghost and four grade-2 ghosts;
  target has one grade-2 ghost and four grade-1 ghosts.
- The first non-self-dual hook pair's truncated exterior BRST seed now uses
  those same five ghost directions as well, so the wedge and Koszul models are
  aligned for that frontier pair.

Status update (Mar 8, 2026, seventh pass): the first non-self-dual hook pair
now has an explicit reduced survivor sector:
- `compute/lib/nonprincipal_ds_orbits.py` now computes the homogeneous
  `\mathfrak{g}^f` basis for the first hook pair under the fixed
  Jacobson--Morozov triples.
- On the source `(3,1)` side, the surviving DS weights are
  `(1,2,2,2,3)`.
- On the target `(2,1,1)` side, the surviving DS weights are
  `(1,1,1,1,\frac{3}{2},\frac{3}{2},\frac{3}{2},\frac{3}{2},2)`.
- `compute/lib/ds_reduction.py` now exposes the induced reduced bracket on
  those survivor bases; in particular, the source has a nontrivial weight-2 to
  weight-3 bracket, while the target has a larger weight-0/weight-3/2 sector
  acting on the rest of the survivor algebra.
- Unlike the subregular `sl_3` seed, the first hook pair has non-abelian
  positive sectors on both sides:
  source brackets ` [E12,E23]=E13 ` and ` [E14,E43]=E13 `,
  target brackets ` [E13,E32]=E12 ` and ` [E14,E42]=E12 `.
  So the quadratic ghost term is now forced in the real BRST differential for
  this pair.
- `compute/lib/ds_reduction.py` now packages that data into explicit BRST
  blueprints for the first hook pair, with full standard-basis profiles on
  both sides and `quadratic_ghost_term_present = True`.
- The nonzero quadratic-ghost support is now explicit as well:
  source `c_{E12}c_{E23}b_{E13}` and `c_{E14}c_{E43}b_{E13}`,
  target `c_{E13}c_{E32}b_{E12}` and `c_{E14}c_{E42}b_{E12}`.
- The same module now builds the actual finite ghost-sector BRST complexes for
  that pair, not only wedge placeholders. These differentials include both the
  character term and the explicit quadratic `c c b` support, and both source
  and target complexes are verified to satisfy `d^2=0` and to be acyclic in
  all ghost degrees.
- Those source and target ghost complexes are now identified by an explicit
  canonical relabeling of the positive directions:
  `E13 <-> E12`, `E12 <-> E13`, `E23 <-> E32`, `E43 <-> E42`, with `E14`
  fixed. So the first non-self-dual hook pair now has a literal ghost-complex
  source/target matching at the seed level.
- Beyond the pure ghost sector, `compute/lib/ds_reduction.py` now builds mixed
  fixed constraint-degree BRST blocks on shifted currents `u_i`, `c`-ghosts,
  and `b`-ghosts. For the first hook pair these mixed blocks are verified
  through constraint degree `2`; on both source and target they satisfy
  `d^2=0` and have zero cohomology in every available BRST degree.
- The same canonical relabeling now matches those mixed `u-c-b` blocks as
  well, not only the pure ghost complexes. So the first hook pair has an
  explicit seed-level source/target identification on both the ghost sector and
  the first finite mixed current-plus-ghost truncations.
- Beyond the purely constraint-generated mixed differential, the same
  `u-c-b` blocks now also include the first nonlinear current/OPE correction:
  the `c \cdot \rho` action of the positive sector on the shifted currents and
  `b`-ghosts, derived directly from the explicit positive-sector brackets.
- For the first non-self-dual hook pair, that nonlinear current-action term is
  genuinely nonzero on the first positive constraint-degree block, but the
  resulting mixed blocks still satisfy `d^2=0`, remain acyclic through
  constraint degree `2`, and still match source-to-target under the same
  canonical relabeling.
- The next survivor-coupled layer is now also in compute: linear survivor
  degree is added on top of those nonlinear mixed blocks, and the positive
  sector acts on survivor variables through the induced quotient action
  `\mathfrak{g}/[e,\mathfrak{g}] \cong \mathfrak{g}^f`.
- For the first non-self-dual hook pair, that survivor-feedback term is
  genuinely nonzero (`6` source terms and `14` target terms), but the first
  tested survivor-coupled truncation (constraint degree `\le 1`, survivor
  degree `1`) is still square-zero and acyclic on both sides.
- With the exact-rank path now routed through `DomainMatrix`, the same
  survivor-coupled hook-pair truncation is also checked at survivor degree `2`:
  even there, both source and target remain square-zero and acyclic through
  constraint degree `1`. So higher survivor polynomial degree alone does not
  break the collapse.
- The self-dual `sl_3` subregular seed is now in that same mixed formalism:
  its mixed `u-c-b` blocks are built explicitly through constraint degree `3`,
  the quadratic ghost term stays absent, and every tested block is square-zero
  and acyclic. Since the constrained positive sector is abelian there, the new
  nonlinear current-action term vanishes, so this remains the control case for
  the nonlinear extension. The mixed-block picture now covers both the
  self-dual control case and the first genuinely non-self-dual hook pair.
- In the subregular control case, the survivor-feedback layer is also explicit:
  `c_{\alpha_1+\alpha_2}` sends `G^-` to `J` and `T` to `-G^+` in the reduced
  survivor sector, while the corresponding linear survivor-coupled truncation
  remains square-zero and acyclic through constraint degree `2`.
- The next frontier layer is now also in compute: the internal reduced-survivor
  CE sector coming from the closed `g^f` bracket itself. This adds survivor
  ghosts and the quadratic/action terms induced by the reduced bracket table.
  Here the story finally stops collapsing: the new internal survivor CE blocks
  are square-zero but not acyclic. Already at survivor polynomial degree `1`,
  the subregular `sl_3` block has cohomology
  `{0:1,1:2,2:2,3:2,4:1}`, while the first non-self-dual hook pair has source
  profile `{0:2,1:5,2:5,3:5,4:5,5:2}` and target profile
  `{0:1,1:2,2:2,3:2,4:2,5:3,6:2,7:0,8:1,9:1}`. The first linear `H^0`
  generators are also explicit: `T` in the subregular control case,
  `source_gm2_1` and `source_gm4_1` on the first hook source, and
  `target_gm2_1` on the first hook target.
- The first attempt to couple that internal survivor CE sector back to the
  positive-sector BRST layer is now also explicit, and it fails for a precise
  reason: the projected positive action on survivors is not a derivation of the
  reduced survivor bracket. Compute now records the derivation defects
  directly. In the subregular control case there are already `8` nonzero
  defects for `c_{\alpha_1+\alpha_2}`; for example,
  `\rho([G^+,G^-])-[\rho(G^+),G^-]-[G^+,\rho(G^-)] = \frac12 G^+`. For the
  first non-self-dual hook pair the source defects have counts
  `2,8,2,8` on the four active positive directions, while the target defects
  have count `26` on each active direction. Correspondingly, the naive
  semidirect coupled blocks fail `d^2=0` already at the first tested
  truncations.
- The subregular control case now goes one step further: compute records the
  discarded `[e,\mathfrak{g}]` witnesses for the positive action itself and the
  corresponding unreduced witness formula for every derivation defect. In
  particular, for `c_{\alpha_1+\alpha_2}` one has
  `[E_{13},G^-] = J + [e,\frac12 F_{12}]` and
  `[E_{13},J] = [e,-\frac32 E_{23}]`, and the defect tensor is recovered from
  the witness identity
  `D(a,b) = \operatorname{pr}(-[w(a),[e,b]] - [[e,a],w(b)])`. Because the
  active positive generator is itself `ad_e`-exact, the first transferred
  cubic BRST correction cancels the naive reduced survivor action entirely in
  this control case, and the corrected semidirect truncation restores
  `d^2=0`.
- The same first-order correction mechanism now also works on the first
  genuinely non-self-dual hook pair. Compute solves the derivation-coboundary
  equation independently for each active positive ghost on both source and
  target survivor sectors; in the first tested hook pair those correction terms
  cancel the naive reduced survivor action completely on both sides. As a
  result, the corrected source and target semidirect survivor blocks restore
  `d^2=0` at the same low truncation where the naive quotient-level coupling
  failed.
- The hook-pair story now also has the first explicit unreduced witness layer:
  compute decomposes the non-self-dual hook-pair survivor action into projected
  terms plus chosen `[e,\mathfrak{g}]` witness preimages, and the hook-pair
  derivation defects are now recovered from the same witness identity
  `D(a,b)=\operatorname{pr}(-[w(a),[e,b]]-[[e,a],w(b)])` that already governs
  the subregular control case. That upgrade is now carried through one step
  further: the first transferred correction itself is recorded as explicit
  witness data, not merely as a quotient-level solved coefficient vector. In
  particular, compute now packages each first-order correction term together
  with the exact constrained-current witness and the survivor-action lift that
  produce it, and the first hook pair’s corrected semidirect truncation still
  restores `d^2=0` after this witness-level repackaging.
- This witness-driven first transfer is no longer only a single-pair fact.
  Compute now verifies a low-rank hook catalog through `\mathfrak{sl}_7`
  (`A_2`/`A_6` hooks) where every constrained current is `ad_e`-exact and the
  first transferred correction cancels the reduced survivor action on both
  source and target sides.
- That propagation now extends one layer further at the first semidirect
  truncation: for every hook orientation through `\mathfrak{sl}_6`, the
  corrected semidirect survivor blocks at
  `(constraint\ degree, survivor\ degree, internal\ CE\ degree)=(0,1,1)`
  still satisfy `d^2=0`, and the corrected semidirect blocks now also match
  under transpose-dual swap through the same `\mathfrak{sl}_6` range.
- Beyond the checked `\mathfrak{sl}_6` semidirect range, the next hook rank is
  now also controlled in a sharper form: in `\mathfrak{sl}_7`, the
  first-transfer cancellation still holds for every hook orientation, and the
  corrected semidirect truncation is now verified for the full hook family at
  `(0,1,1)` by combining direct square-zero checks on the half-catalog
  `r=1,2,3` with transpose-dual symmetry checks on the nontrivial pairs
  `r=1,2`.
- The exact projector bottleneck that appeared at the next rank has now been
  removed too: compute no longer resolves survivor projections by repeated
  `LUsolve` in ambient `n^2` coordinates, but by cached inverses in the
  traceless standard-basis coordinate system. With that change in place,
  `\mathfrak{sl}_8` is now computationally reachable on the same hook track:
  the witness-driven first transfer cancels the reduced survivor action for
  every hook orientation `r=1,\dots,6`, and the corrected semidirect
  truncation at `(0,1,1)` is verified for the full hook family by direct
  square-zero checks on the half-catalog `r=1,2,3` together with dual-swap
  checks on the same three nontrivial pairs.
- That same optimized projection layer now carries one more full semidirect
  rank as well: `\mathfrak{sl}_9` has direct half-catalog square-zero checks
  on `r=1,2,3,4` and transpose-dual checks on the nontrivial pairs
  `r=1,2,3`, so the corrected semidirect truncation at `(0,1,1)` is now
  verified for the full hook family there too. The first-transfer layer is
  correspondingly open beyond that family boundary, with the extreme hook
  `r=1` already positive in `\mathfrak{sl}_9`.
- The same family argument now reaches one rank further again: in
  `\mathfrak{sl}_{10}`, the witness-driven first transfer cancels the reduced
  survivor action for every hook orientation `r=1,\dots,8`, and the corrected
  semidirect truncation at `(0,1,1)` is verified for the full hook family by
  square-zero checks on the half-catalog `r=1,2,3,4` together with
  transpose-dual checks on the nontrivial pairs `r=1,2,3`.
- The next rank is now open too. The apparent `\mathfrak{sl}_{11}` blocker was
  a basis-label alias in the standard traceless basis: `E_{1,11}` and
  `E_{11,1}` both collapsed to the same serialized key before the high-rank
  label format was made unambiguous. With that fixed, the witness-driven first
  transfer again cancels the reduced survivor action for every hook
  orientation `r=1,\dots,9`, and the corrected semidirect truncation at
  `(0,1,1)` is verified for the full hook family by square-zero checks on the
  half-catalog `r=1,2,3,4,5` together with transpose-dual checks on the
  nontrivial pairs `r=1,2,3,4`. The main scaling cost is now the dual-swap
  comparison rather than survivor projection.
- One rank beyond that family boundary is already sampled positively too:
  in `\mathfrak{sl}_{12}`, the extreme hook `r=1` has witness-driven
  first-transfer cancellation, corrected semidirect square-zero at `(0,1,1)`,
  and the corresponding transpose-dual comparison; the next interior hook
  `r=2` already has first-transfer cancellation and corrected semidirect
  square-zero at the same truncation as well. So the current unknown is no
  longer whether the next rank opens at all, but whether the full half-catalog
  sweep `r=1,\dots,5` can be pushed through at acceptable cost.
- That remaining `\mathfrak{sl}_{12}` gap is now closed too. With the
  semidirect relabeling check rewritten to compare relabeled block data rather
  than rebuilding full BRST matrices, the full half-catalog
  `r=1,2,3,4,5` now passes at `(0,1,1)`: every orientation has
  first-transfer cancellation and corrected semidirect square-zero, and the
  transpose-dual comparisons hold on the nontrivial pairs `r=1,2,3,4,5`.
  The live next-rank question has therefore moved on to `\mathfrak{sl}_{13}`.
- That next rank is now open too. Three projector-path optimizations were
  needed to reach the interior of the half-catalog: direct coordinate
  extraction in the standard traceless basis instead of repeated exact solves,
  one-pass pivot extraction for `[e,g]` rather than incremental rank tests,
  and sparse coordinate-column assembly with cached basis-index maps. With
  those changes in place, `\mathfrak{sl}_{13}` now satisfies the same
  truncation statement: the witness-driven first transfer is positive on the
  half-catalog `r=1,\dots,6`, corrected semidirect square-zero holds on the
  same half-catalog at `(0,1,1)`, and transpose-dual comparison holds on the
  nontrivial pairs `r=1,\dots,5`. The live family frontier is now
  `\mathfrak{sl}_{14}`.
- One step past that family boundary is already sampled positively: in
  `\mathfrak{sl}_{14}`, the full hook half-catalog `r=1,\dots,6` now satisfies
  witness-driven first-transfer cancellation, corrected semidirect
  square-zero at `(0,1,1)`, and transpose-dual comparison on the nontrivial
  pairs. The live family frontier has therefore moved on to
  `\mathfrak{sl}_{15}`.
- The next rank is already open at low depth too: in `\mathfrak{sl}_{15}`,
  the full hook half-catalog `r=1,\dots,7` now satisfies witness-driven
  first-transfer cancellation, corrected semidirect square-zero at `(0,1,1)`,
  and transpose-dual comparison on the nontrivial pairs. The live family
  frontier has therefore moved on to `\mathfrak{sl}_{16}`.
- The next rank is already open at low depth too: in `\mathfrak{sl}_{16}`,
  the full hook half-catalog `r=1,\dots,7` now satisfies witness-driven
  first-transfer cancellation, corrected semidirect square-zero at `(0,1,1)`,
  and transpose-dual comparison on the nontrivial pairs. The live family
  frontier has therefore moved on to `\mathfrak{sl}_{17}`.
- The next rank is already open at low depth too: in `\mathfrak{sl}_{17}`,
  the full hook half-catalog `r=1,\dots,8` now satisfies witness-driven
  first-transfer cancellation, corrected semidirect square-zero at `(0,1,1)`,
  and transpose-dual comparison on the nontrivial pairs. The live family
  frontier has therefore moved on to `\mathfrak{sl}_{18}`.
- One step beyond that written boundary is already open on the same compute
  track: in `\mathfrak{sl}_{18}`, the full hook half-catalog `r=1,\dots,8`
  now satisfies witness-driven first-transfer cancellation, corrected
  semidirect square-zero at `(0,1,1)`, and transpose-dual comparison on the
  nontrivial pairs. The written family boundary therefore moves on to
  `\mathfrak{sl}_{18}` and the live family frontier to `\mathfrak{sl}_{19}`.
- One step beyond that new written boundary is now fully closed as well: in
  `\mathfrak{sl}_{19}`, the full hook half-catalog `r=1,\dots,9` satisfies
  witness-driven first-transfer cancellation, corrected semidirect
  square-zero at `(0,1,1)`, and transpose-dual comparison on the nontrivial
  pairs. The written family boundary therefore moves on to
  `\mathfrak{sl}_{19}` and the live family frontier to `\mathfrak{sl}_{20}`.
- One step beyond that new written boundary is already open at the extreme
  hook: `\mathfrak{sl}_{20}, r=1` satisfies witness-driven first-transfer
  cancellation and corrected semidirect square-zero at `(0,1,1)`.
- The same mixed/nonlinear `u-c-b` machinery is now generalized from the first
  hook pair to all type-A hook pairs at the seed level: compute now exposes
  family APIs for constraints, positive-sector brackets, quadratic `c c b`
  support, and current-action terms with truncation controls.
- Family transpose-duality is now checked at block level too: mixed and
  nonlinear hook-pair blocks are compared under the dual swap
  `r \leftrightarrow n-r-1` via canonical side relabeling, and the catalog
  verifiers now run these checks systematically.
- Survivor scaffolds are no longer first-pair-only:
  `compute/lib/ds_reduction.py` now also exposes generic hook-pair survivor
  candidates and reduced-bracket tables, plus family-level survivor-action and
  survivor-coupled block builders. The same transpose-dual verification pass is
  now available for survivor-coupled blocks via a catalog checker on a
  tractable seeded range.
- This family block layer now also has non-hook coverage:
  type-A two-row non-hook partition pairs are wired into the same mixed,
  nonlinear, and survivor-coupled builders, and the corresponding canonical
  relabel/dual-swap verifiers now run on the seeded non-hook range; in the
  cheaper mixed/nonlinear sector that two-row range now reaches
  `\mathfrak{sl}_9`.
- The next non-hook family layer is now live too:
  the same partition-pair DS machinery now covers seeded general
  `general_nonprincipal` type-A partitions (for example `(3,2,1)`), with
  mixed/nonlinear/survivor-coupled block builders; for mixed and nonlinear
  blocks the general-family verification is now reduced by transpose symmetry,
  and the seeded range reaches size `9`. The same general
  survivor-coupled family-via-duality layer now also remains positive through
  size `12` in survivor degree `1` and through size `11` in survivor degree
  `2`.
- The same generic partition-pair path now also reaches the first transferred
  survivor correction on the seeded non-hook range: witness-level
  survivor-action lifts and constrained-current preimages are recorded for
  seeded two-row and `general_nonprincipal` partitions, the internal survivor
  CE sector is exposed on that same family path, and the corrected semidirect
  survivor blocks at truncation `(0,1,1)` now restore `d^2=0` with seeded
  two-row/general dual-swap catalog checks.
- That non-hook verification layer is now organized to scale: the seeded
  two-row corrected semidirect checks are bundled in one pass through
  `\mathfrak{sl}_8` at truncation `(0,1,1)`, and the same two-row
  family-via-duality check stays positive in survivor degree `2` through
  `\mathfrak{sl}_8`; the seeded
  `general_nonprincipal` corrected
  semidirect family is reduced by transpose symmetry and now reaches size
  `14` as a stable seeded bundle at the first corrected semidirect
  truncation `(0,1,1)`; this step uses a fixed row-minor solver for the
  reduced survivor-bracket layer in place of repeated tall exact solves and
  prunes semidirect branches that cannot contribute at internal CE cutoff
  `1`. The same
  general family-via-duality check remains positive in survivor degree `2`
  through size `11`.

### First concrete step
```
TARGET: strengthen the self-dual sl3-subregular/Bershadsky--Polyakov
        control case and then pass to the first genuinely non-self-dual
        hook pair in sl4.

INPUT: sl3 has two non-zero nilpotent orbits:
       - Regular (principal): dim 6, W-algebra = W_3 (2 generators T, W)
       - Subregular/minimal: dim 4, W-algebra = Bershadsky--Polyakov
         W^k(sl3,f_sub) with generators (J,G^+,G^-,T).
       The subregular orbit is self-dual under partition transpose.

COMPUTATION:
1. The subregular nilpotent in sl3 is e = E_{12} (a simple root vector).
   The sl2-triple: e = E_{12}, h = H_1, f = F_{12}.
2. DS reduction: W^k(sl3, f_sub) = H^0_BRST(sl3_k, f_sub).
   In the printed control case this is the Bershadsky--Polyakov algebra,
   so the immediate task is not to identify a new algebra but to verify
   the seed-level BRST package, the normalization bridge, and the
   self-dual transport profile on the same orbit.
3. In type A, BV duality is partition transpose. For sl3 the subregular
   partition (2,1) is self-transpose, so the subregular orbit is self-dual.
4. So the conjecture predicts a self-dual non-principal check:
   the BP/subregular seed must transport to itself with the correct
   orbit-indexed level shift and normalization profile. This is a
   sanity-check base case, not yet a genuinely new dual orbit pairing.
5. The first genuinely non-self-dual hook test in type A therefore begins at
   sl4, where (3,1)^t = (2,1,1).

VERIFICATION: First close the self-dual sl3-subregular control package
              (dual-orbit input, orbit-indexed level shift, paired seed
              transport). Then move to sl4 hook pairs and compare the
              two distinct dual-orbit reductions.

TOOLS NEEDED: ds_reduction.py — paired BRST seed complexes / transport.
              bv_duality.py — dual-orbit input package.
              nonprincipal_ds_orbits.py — orbit-indexed level-shift data.
              w_algebra_ope.py — OPE structure constants for W(g, f).
```

### Success criterion
A proved theorem for the first genuinely non-self-dual hook pair in type A
(starting with sl4): W^k(sl_n, f_{(n-1,1)}) and W^{k'}(sl_n, f_{(2,1^{n-2})})
form a Koszul dual pair with explicit level relation. The sl3-subregular case
remains the sanity-check base case for the same infrastructure.

---

## Summary: New Tools Required

| ID | Tool | Programme | Implementation | Priority |
|----|------|-----------|----------------|----------|
| M1 | Derived oper spectral sequence | I | Extend chiral_bar.py + new oper_comparison.py | HIGH |
| M2 | Admissible-level bar specialization | II | bar_admissible.py + quantum_group_bar.py | HIGH |
| M3 | Chain-level fusion product | III | fock_bar.py + fusion_chain.py | MEDIUM |
| M4 | E_2 bar complex | IV | e2_bar.py + totaro.py | LOW |
| M5 | Circle restriction of propagator | V | circle_restriction.py + vassiliev_tables.py | MEDIUM |
| M6 | BRST-bar chain map | VI-a | brst_complex.py + bar_brst_comparison.py | HIGH |
| M7 | CS observable algebra | VI-b | cs_observables.py + bar_cs_comparison.py | MEDIUM |
| M8 | Pro-nilpotent bar / W_infinity OPE | VI-d | w_infinity_ope.py + pronilpotent_bar.py | LOW |
| M9 | Sparse modular linear algebra | IX | bar_modular.py + sparse_rank.py | HIGH |
| M10 | BTZ dictionary | VI-b | btz_dictionary.py + genus1_comparison.py | MEDIUM |
| M11 | Non-principal three-packet transport | VIII-a | ds_reduction.py + bv_duality.py + nonprincipal_ds_orbits.py | MEDIUM |

### Priority justification
- HIGH = either (a) concrete computation yielding confirmable/refutable prediction,
  or (b) direct upgrade of conjectured claim to proved.
- MEDIUM = requires new framework but has clear entry point.
- LOW = requires substantial conceptual development before computation begins.

### Estimated new code
- ~15 new Python modules in compute/lib/
- ~15 new test files in compute/tests/
- ~3000 lines of new code total (not counting tests)
- All building on existing infrastructure (OPEAlgebra, ChainComplex, GradedVectorSpace)
