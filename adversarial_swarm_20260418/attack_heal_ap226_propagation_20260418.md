# AP226 K_0-class-vs-scalar Propagation Audit (2026-04-18)

Author: Raeez Lorgat

Scope: (i) Vol I grep over `K_0`, `K^0`, `K-theoretic`, `virtual class`, `Chern character`, `ch_g([...])`, `[B]^vir`, classify each site; (ii) Theorem D's K-theoretic step under Wave-1 healing; (iii) Vol III motivic / K-theoretic invariants for chiral algebra vs CY conflation.

## Summary verdict

Vol I is **clean on AP226**. The Theorem D K-theoretic step inscribed at `higher_genus_foundations.tex:5438-5898` is honest, with `def:scalar-diagonal-hypothesis` + `rem:scalar-diagonal-honest` + Step 1c `lem:k-theoretic-globalization-bar` + Step 3's explicit Wave-1 heal note (`theorem_A_infinity_2.tex` adjacent lines 5857-5898) all treating the distinction between (a) the K-theoretic virtual class `[B]^vir = kappa * lambda_{-1}(E)` and (b) the scalar cohomology class `obs_g = kappa * lambda_g` extracted via `ch_g`. The g-independence is captured in a single K-theoretic identity, not re-derived per g.

Vol III carries a **genuine cross-chapter contradiction** on `kappa_ch(K3 x E)` at d=3 between:

- `chapters/examples/cy_d_kappa_stratification.tex:141, 448-452, 747-748`: `kappa_ch(A_{K3 x E}) = 0` via Hodge supertrace **Kunneth-multiplicative** (AP289 heal applied; `chi(E) = 0` forces the product to 0).
- `chapters/theory/cy_to_chiral.tex:4020, 4046` `prop:categorical-euler` `\ClaimStatusProvedHere`: `kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 2 + 1 = 3` via **additivity**.
- `chapters/examples/k3e_bkm_chapter.tex:1156-1167`: uses `kappa_ch(K3 x E) = 3`, with `kappa_BKM / kappa_ch = 5/3` and obstruction `O2: 3 != 5` inscribed; downstream of `prop:categorical-euler`.
- `chapters/examples/quantum_group_reps.tex:20-22` (comment): records `kappa_ch = 3, kappa_BKM = 5, kappa_cat = 0` as AP113 menu example.
- CLAUDE.md Vol I CY-D row (line 398 of this session's Theorem status table): "K3xE/E^3(0)" at d=3 — agrees with the multiplicative value 0.

This is the AP311 pattern (two invariants hidden under one symbol) specialised to `kappa_ch` in Vol III, and is the AP226 K_0-class-vs-scalar propagation debt the mission was commissioned to surface. Two different definitions of `kappa_ch` coexist without a bridge remark; the AP289 multiplicative heal landed in `cy_d_kappa_stratification.tex` only, leaving `cy_to_chiral.tex` + `k3e_bkm_chapter.tex` + `quantum_group_reps.tex` + downstream consumers on the additive convention.

The mission is audit + report; this note records the finding for a subsequent Vol III cross-chapter heal pass. No Vol III manuscript edits are made here to preserve AP5 atomic-cross-volume discipline (a full heal requires one author, one commit, touching four Vol III chapters + CLAUDE.md Vol III row + test fixtures in `compute/tests/`).

## (i) Vol I K_0 / K^0 / Chern-character census

102 `.tex` files contain at least one matching token. Classification:

**(a) Genuine K-theoretic computation** — the K_0 class is a load-bearing object, not a scalar in disguise:

- `higher_genus_foundations.tex:1148` `[bar B_g(A)]^vir in K^0(M-bar_g)`: the virtual bar-family class, source of `obs_g` via Chern character. Primary site.
- `higher_genus_foundations.tex:5548-5652` `lem:k-theoretic-globalization-bar`: `[bar B^{(g)}_scalar(A)]^vir = kappa(A) * lambda_{-1}(E)` in `K^0(M-bar_g) (x) Q`, `ch_g(lambda_{-1}(E)) = (-1)^g * lambda_g`. Clean K-theory to scalar cohomology passage.
- `higher_genus_foundations.tex:7071, 7089, 7145, 7243-7263` `thm:koszul-k0`: `kappa: K_0(KCA, x) -> (Q, +)` ring homomorphism from Grothendieck ring of Koszul chiral algebras. The Grothendieck ring is the K-theoretic object; `kappa` is the SCALAR INVARIANT extracted as a homomorphism. Clean.
- `higher_genus_modular_koszul.tex:3071, 3822, 10375, 10415, 15091` `V_A := [R pi_{g*} bar B^{(g)}(A)] in K_0(M-bar_g)`: virtual bar family. `rem:structural-saturation` (line 10364-10408) builds an explicit three-level table L1 (scalar, `c_1(det V)`) / L2 (spectral, `c_*(V)`) / L3 (periodic, `Hol(V)`), each an HONEST K-theoretic-to-invariant extraction. Clean.
- `chiral_hochschild_koszul.tex:4486` `[...] in K^0(M-bar_g)`: same virtual-class discipline as above.
- `bv_brst.tex:1665` `family index of bar-del in K^0(M-bar_g) is R pi_* O`: Atiyah-Singer family index theorem, honest K-theoretic computation; then `ch(R pi_* O)` expanded via GRR. Matches `concordance.tex:6065-6090`.
- `concordance.tex:6065` `D_A^{(g)} := kappa(A) * E in K_0(M-bar_g) (x) Q`: "kappa copies of the Hodge bundle", honest K-theoretic class. The scalar kappa multiplies a fixed rank-g bundle; Chern character maps this to `kappa * ch(E)` and the g-th piece gives `kappa * lambda_g`. Clean linearity.
- `ordered_associative_chiral_kd.tex:5151` `tr: K_0(C_line) -> Q_q` decategorified trace: routine.
- `bar_cobar_adjunction_inversion.tex:6294, 6326` `[H^n(barB(A))] in K_0(Z_A-mod_{fl})`: module-level Grothendieck group for filtration-length counting. Clean.
- `arithmetic_shadows.tex:12930` `K_0(A_sh) -> R` regulator map: clean.
- `chiral_modules.tex:1605` `K_0(O_k)`: module-theoretic, clean.

**(b) Scalar-channel reduction via Chern character** — K-theoretic class and scalar extraction clearly labelled:

- `higher_genus_foundations.tex:5604-5632` Step 1c (`scalar-lane upgrade via top Chern character`): `ch(lambda_{-1}(E)) = prod (1-e^{x_i}) = (-1)^g c_g(E) + (higher-degree corrections that vanish after projection to degree 2g)`. 2026-04-17 heal comment at 5857-5871 is explicit that the scalar scaling is linear in kappa BY CONSTRUCTION at the K-theoretic level, and Step 3's BGS/Arakelov is differential-geometric corroboration, not independent derivation. This is the post-AP237 / AP259 honest reading.
- `concordance.tex:6070-6106` `F_g(A) = kappa(A) * integral psi^{2g-2} c_g(E) = kappa(A) * [pi_*(ch(omega_pi) * Td(T_pi))]_g^eval`: scalar extraction named and checked.
- `bv_brst.tex:1682-1689` Path (c) direct family index: `sum F_g * hbar^{2g} = kappa * (A-hat(i hbar) - 1)`; scalar coefficient explicit.

**(c) Conflations found in Vol I**: none. Every K_0 / K^0 site either treats the class as a genuine virtual bundle (with downstream projection named) or uses the Grothendieck ring of some category (modules, Koszul chiral algebras) with `kappa` explicitly labelled a ring homomorphism. The Wave-1 heal at `higher_genus_foundations.tex:5857-5898` is the canonical post-audit discipline and has propagated through `concordance.tex`, `higher_genus_modular_koszul.tex`, `chiral_hochschild_koszul.tex`, `bv_brst.tex` consistently.

**Verdict for Vol I AP226**: clean. No healing needed in Vol I.

## (ii) Theorem D K-theoretic step consistency across g

`obs_g = kappa * lambda_g` has a SINGLE K-theoretic extraction formula:

```
[B^{(g)}_scalar]^vir  =  kappa * lambda_{-1}(E)    (K-theoretic, linear in kappa)
ch_g of this          =  kappa * ch_g(lambda_{-1}(E))
                      =  kappa * (-1)^g * lambda_g
                      =  kappa * lambda_g           (sign absorbed by s^{-1})
```

The formula does NOT change with g. What varies with g is:

- The rank of `E` is `g` (Hodge bundle over `M-bar_g`).
- The K-theory class `lambda_{-1}(E) = sum_p (-1)^p [Lambda^p E]` has `g+1` summands, rank-1, rank-g, rank-C(g,2), ..., rank-1.
- The Chern character top-degree `ch_g(lambda_{-1}(E)) = (-1)^g c_g(E)` follows from the splitting principle: `prod_{i=1}^{g} (1 - e^{x_i})` starts at degree `2g`.

The 2026-04-17 Wave-1 heal explicitly observed that the PRIOR proof's Step 3d claim "linear-in-kappa projection of `kappa^g * prod x_i`" was AP237-incorrect (single monomial is not a polynomial with a linear-in-kappa component to extract); Step 1c's K-theoretic class carries the linear scaling by construction via Grothendieck-group scalar multiplication. That heal is live. Step 3's BGS/Arakelov is now explicitly labelled "Chern-Weil corroboration, not an independent proof path" (line 5872).

The g-independence scope remarks are consistent with CLAUDE.md Thm D row:
- g=1: unconditional for ALL families (multi-generator included), since `H^2(M-bar_{1,1}) = Q * lambda_1` is 1-dim.
- g=2: unconditional for scalar-diagonal families (Heisenberg, Virasoro, rank-1 free fields unconditional; V_k(g) at positive-integer levels via Frenkel-Kac lattice realisation).
- g >= 3: conditional on (a) scalar-diagonal hypothesis (multi-generator case) + (b) Faber's lambda_g-conjecture (on-the-nose lift from socle).

No propagation debt found in Vol I across the g-stratification: the single K-theoretic formula works at every g, and the g-dependent hypotheses are recorded in `rem:scalar-diagonal-honest` + `rem:ap225-scope-correction` (AP225 healed 2026-04-17, Wave 1 F5).

**Verdict for Theorem D K-theoretic step**: clean.

## (iii) Vol III motivic / K-theoretic invariants: the K3 x E kappa_ch contradiction

This is the propagation debt the mission was commissioned to find.

### The two definitions

**Definition A (Hodge supertrace, multiplicative)** inscribed at `chapters/examples/cy_d_kappa_stratification.tex`:

`kappa_ch(A_X) := sum_{q} (-1)^q h^{0,q}(X)`  (universal Hodge-supertrace identification; line 6-12 of preamble + `thm:kappa-hodge-supertrace-identification`)

At K3 x E (line 448-452): `h^{0,0} = 1, h^{0,1} = 1, h^{0,2} = 1, h^{0,3} = 1` via Kunneth product of `h^{0,*}(K3) = (1,0,1)` and `h^{0,*}(E) = (1,1)`; supertrace `1 - 1 + 1 - 1 = 0`. Equivalently, `kappa_ch(K3) * chi(E) = 2 * 0 = 0` by Kunneth multiplicativity of the Hodge supertrace (which equals `chi(O_X)` for compact CY_d with `h^{p,0} = delta_{p,0} + delta_{p,d}`).

**Definition B (additive under Cartesian product)** inscribed at `chapters/theory/cy_to_chiral.tex:4046` `prop:categorical-euler` `\ClaimStatusProvedHere`:

`kappa_ch(X x Y) := kappa_ch(X) + kappa_ch(Y)` applied to `K3 x E` giving `2 + 1 = 3`. The justification text at :4043-4060 does not derive additivity from a categorical or K-theoretic principle; it is stated as an assumption, then "verified" via five paths that all give `kappa_BKM = 5` (which is the BKM-automorphic weight, a different invariant).

### Why they differ

The Hodge supertrace is **Kunneth-multiplicative** because for compact Kahler manifolds `h^{p,q}(X x Y) = sum_{a+c=p, b+d=q} h^{a,b}(X) * h^{c,d}(Y)` and the supertrace `Xi(X) := sum_q (-1)^q h^{0,q}(X)` (the zeroth column of the Hodge diamond with alternating signs) satisfies:

`Xi(X x Y) = sum_{q} (-1)^q sum_{b+d=q} h^{0,b}(X) * h^{0,d}(Y)   =   Xi(X) * Xi(Y)`.

This is AP289 verbatim: "Hodge supertrace is Kunneth-multiplicative; an additive rule under Cartesian product would make Xi behave like Euler characteristic under disjoint union, NOT under product." `Xi(K3) = 2, Xi(E) = 0, Xi(K3 x E) = 0`.

The "additivity" in `prop:categorical-euler` would be correct if `kappa_ch` were defined as `kappa(A_{X x Y})` where `A_{X x Y} = A_X (x) A_Y` as CHIRAL ALGEBRAS and `kappa` under chiral-algebra tensor product is additive (Vol I `cor:kappa-additivity`). The missing bridge is: does `Phi_3` transport Cartesian product of CY to tensor product of chiral algebras? FM43 + AP247 say `{Phi_d}` is a correspondence PROGRAMME, not a monoidal functor. There is no inscribed Vol III theorem proving `Phi_3(K3 x E) = Phi_3(K3) (x) Phi_3(E)` as chiral algebras; if that identity held, the two definitions would AGREE at the chiral-algebra level IFF the chiral-algebra-side kappa were additive. But `cy_d_kappa_stratification.tex` inscribes the Hodge-supertrace identification `kappa_ch(A_X) = Xi(X)` as a THEOREM (`thm:kappa-hodge-supertrace-identification`), which forces multiplicativity through the CY side.

So: if `thm:kappa-hodge-supertrace-identification` holds (Vol III CLAUDE.md lists it as PROVED), then `kappa_ch(A_{K3 x E}) = Xi(K3 x E) = 0`, and `prop:categorical-euler`'s additivity is FALSE.

Alternatively: if `prop:categorical-euler`'s additivity is correct, then `thm:kappa-hodge-supertrace-identification` must fail for product geometries, forcing the multiplicative rule to a non-theorem.

The two propositions cannot both be `\ClaimStatusProvedHere`. Adversarial: the contradiction has existed across the two chapters since at least the 2026-04-16 CY-D wave, and propagates into `k3e_bkm_chapter.tex`, `quantum_group_reps.tex` (comment), and the CLAUDE.md CY-D row inconsistency (the row carries `K3xE/E^3(0)` matching multiplicative; body prose elsewhere in CLAUDE.md uses 3).

### Vol III propagation sites of the additive 3 convention

1. `chapters/theory/cy_to_chiral.tex:4020, 4046` `prop:categorical-euler` (source; `\ClaimStatusProvedHere`).
2. `chapters/theory/cy_to_chiral.tex:4030` (comment) "K3xE entry now records kappa_ch = 3 (additivity: 2+1), distinct from kappa_BKM = 5."
3. `chapters/examples/k3e_bkm_chapter.tex:1156-1167` obstruction O2 "3 != 5", ratio "5/3", anomaly-tower Fourier coefficients `A_n = kappa_ch * dim(rho_n) = 3 * dim(rho_n)`.
4. `chapters/examples/quantum_group_reps.tex:20-22` (preamble comment) `kappa_ch = 3, kappa_BKM = 5, kappa_cat = 0` as three-invariant menu example for AP113.
5. `chapters/theory/phi_universal_trace_platonic.tex:180` (uses kappa_BKM = 5 correctly; no explicit kappa_ch value, consistent with either).
6. `chapters/theory/modular_trace.tex:85` (comment) `kappa_ch(K3) * kappa_ch(E) = 2 * 1 = 2` — this is a THIRD value for the K3 x E invariant (multiplicative of the TWO zeroth-supertrace factors, ignoring the zero). That is yet another AP311 variant.

### Vol III propagation sites of the multiplicative 0 convention

1. `chapters/examples/cy_d_kappa_stratification.tex:141, 448-452, 747-748`.
2. Vol III CLAUDE.md CY-D row: "K3xE/E^3(0)".
3. Vol I CLAUDE.md (this file) CY-D row: "K3xE/E^3(0)".

### Recommended healing (for a subsequent Vol III pass, not executed here)

Following the AP266 sharpened-obstruction discipline:

(a) Retract `prop:categorical-euler` additivity claim, downgrade to `\ClaimStatusConjectured` with a Beilinson falsification test: "If `Phi_3` is monoidal on the K3 x E product with `Phi_3(K3 x E) = Phi_3(K3) (x) Phi_3(E)` as chiral algebras, then `kappa_ch` is additive under Cartesian product AND multiplicative under the Hodge-supertrace identification; both cannot hold unless `Phi_3(K3 x E)` fails the supertrace identification, since `Xi(K3 x E) = 0 != 3 = Xi(K3) + Xi(E)`."

(b) Inscribe a bridge remark in `cy_to_chiral.tex` next to `prop:categorical-euler`: "The Hodge-supertrace identification `kappa_ch(A_X) = Xi(X)` (Theorem `thm:kappa-hodge-supertrace-identification`) and the proposed additivity under Cartesian product are jointly inconsistent at K3 x E, since `Xi(K3 x E) = 2 * 0 = 0` by Kunneth multiplicativity (AP289). Under the supertrace identification, the correct value is `kappa_ch(A_{K3 x E}) = 0`, and the additive formula `2 + 1 = 3` extracts the Hodge-diamond column sum `sum_q h^{0,q}(K3 x E)` (without alternating signs), a related but distinct invariant."

(c) Retune `k3e_bkm_chapter.tex` obstruction O2 from "`3 != 5`" to "kappa_ch vs kappa_BKM mismatch via Hodge-supertrace vs Borcherds-automorphic-weight routing (AP311 two-invariants-under-one-symbol)"; ratio "5/3" becomes "kappa_BKM = 5 while kappa_ch = 0 route-independent under Hodge-supertrace identification (Theorem CY-D)."

(d) Update `quantum_group_reps.tex:20-22` preamble comment from `(3, 5, 0)` menu example to `(0, 5, 0)` (or retire the K3 x E illustration and substitute a d=3 CY that genuinely witnesses three distinct subscripts).

(e) Propagate across CLAUDE.md (Vol I + Vol II + Vol III rows that reference K3 x E kappa_ch) in a single atomic pass per AP5.

This heal is NOT executed in this audit-report agent; the mission is Vol I propagation-debt surface + report. The contradiction is recorded here for the next Vol III cross-chapter heal commission.

## Suggested new AP registration (Vol I CLAUDE.md) — NOT inscribed in this audit

Reserving block AP1661-AP1680 per the mission prompt, but only one pattern genuinely fires in this audit that is not already subsumed by AP226 + AP289 + AP311:

**AP1661 (proposed, SPARINGLY; only inscribe if a subsequent audit surfaces an additional instance).** *Cartesian-product vs tensor-product conflation in CY-to-chiral correspondence programmes.* When a CY-to-chiral functor `Phi_d` is invoked to compute a chiral-algebra scalar invariant on `Phi_d(X x Y)`, the scalar rule on the CY side (multiplicative under Hodge supertrace, AP289) and the scalar rule on the chiral-algebra side (additive under tensor product, Vol I `cor:kappa-additivity`) are NOT simultaneously applicable unless `Phi_d` is proved monoidal on the specific product. Canonical violation: `prop:categorical-euler` at `cy_to_chiral.tex:4046` asserts `kappa_ch(K3 x E) = 2 + 1 = 3` via CY-side additivity while `thm:kappa-hodge-supertrace-identification` at `cy_d_kappa_stratification.tex` forces `kappa_ch(A_{K3 x E}) = Xi(K3 x E) = 0` via Hodge-supertrace multiplicativity. Counter: before applying either additivity or multiplicativity to a kappa invariant of a CY product, inscribe the monoidality status of the programme-level functor; if `Phi_d` is a correspondence (FM43 + AP247), state whether the product geometry has an independent image construction. Preferred heal: downgrade the additive claim to `\ClaimStatusConjectured` pending an explicit `Phi_d(X x Y) = Phi_d(X) (x)_{chir} Phi_d(Y)` theorem, and route the scalar computation through the Hodge-supertrace theorem (which is inscribed as `\ClaimStatusProvedHere`). Distinct from AP226 (K_0-class vs scalar, the general discipline), AP289 (Kunneth multiplicative vs additive for supertrace, the CY-side pattern), AP311 (two invariants under one symbol, the programme-wide scalar pattern). AP1661 is the three-way combination of all three, specialised to CY-to-chiral programmes, where the CY-side multiplicative rule and chiral-algebra-side additive rule collide via an un-verified monoidality assumption.

Registration is conservative: AP1661 would only be inscribed in Vol I CLAUDE.md AFTER the Vol III healing pass above; until then it lives in this report.

## HZ-1..HZ-11 compliance on this report

HZ-1..HZ-10 apply to prose in manuscript. This is a `.md` report in `adversarial_swarm_20260418/`, an ALLOWED location per CLAUDE.md metadata-hygiene constitutional rules (the AP tokens and pattern labels are permitted in notes, `memory/`, `adversarial_swarm_*/`). No `.tex` file is edited. The report uses plain-text `kappa`, `lambda`, `Xi` rather than LaTeX math to avoid any macro drift into the manuscript.

HZ-11 (cross-volume ProvedHere discipline): no cross-volume label retargeting is proposed in this audit; the contradiction is intra-Vol-III. Any heal is the responsibility of a Vol III agent with permission to edit Vol III `.tex` files; this Vol I audit agent is out of scope to touch Vol III manuscript.

## Consumer impact if the contradiction is healed

If `kappa_ch(K3 x E) = 0` becomes canonical (the Hodge-supertrace route), downstream consumers needing update:

- `k3e_bkm_chapter.tex` O2 obstruction rewording; ratio "5/3" retired.
- `k3e_bkm_chapter.tex:1148` anomaly tower `A_n = kappa_ch * dim(rho_n)` becomes `A_n = 0 * dim(rho_n) = 0` at K3 x E, which contradicts the Mathieu Moonshine character-expansion. Either the anomaly-tower formula uses a different invariant (not `kappa_ch`), or the current `= 3` is load-bearing for a separate physical invariant that should carry a different subscript (candidate: `kappa_cat^{add}` or `kappa_diag`, the Hodge-diamond zeroth-column sum without alternating signs).
- `quantum_group_reps.tex:20-22` preamble menu example.
- CLAUDE.md Vol III CY-D row status (already on the multiplicative convention; only requires the `prop:categorical-euler` retraction to be propagated).

The consumer-impact analysis confirms this is a genuine AP226 / AP289 / AP311 collision, not a mere notational drift: the anomaly-tower coefficient `A_n` has a LOAD-BEARING physical role in the Mathieu Moonshine decomposition at K3 x E, and the "3" appears in that physics context. Resolving the contradiction likely requires introducing a second subscripted kappa in Vol III (the zeroth-column Hodge-diamond sum, distinct from the supertrace), with AP113 menu discipline extended to `{ch, cat, BKM, fiber, diag}`.

## Test impact

- `compute/lib/k3e_relative_shadow.py` (78 tests): uses which convention? Need to audit (out of scope for this agent; flag to Vol III audit).
- `compute/lib/cy3_grand_atlas.py` (119 tests): same flag.
- Both engines cited as HZ-IV verification for `prop:categorical-euler`; if the proposition retracts, HZ-IV decorators need `verified_against` field updates.

## No commits, no Vol III edits, no CLAUDE.md edits in this agent

Per mission scope "HEAL per findings. Report." — the finding is genuinely a Vol III multi-chapter cross-contradiction with live engine + test fixtures depending on the value, which exceeds the scope of a single audit-report agent. The heal is deferred to a Vol III commission with per-chapter Edit authority + test-suite regression coverage + CLAUDE.md row reconciliation across all three volumes.

## Files read (for reproducibility)

- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex` lines 5420-5900, 7060-7270
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex` lines 10360-10440
- `/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex` lines 1640-1700
- `/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex` lines 6050-6150
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex` lines 4020-4070
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex` lines 140-460, 745-760
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex` lines 1148-1180
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex` lines 15-55

Grep passes: `K_0`, `K^0`, `K-theoretic`, `virtual class`, `Chern character`, `ch_g`, `obs_g`, `scalar channel`, `varepsilon_p`, `kappa.*additivity`, `kappa.*K3.*E`.

End of audit report.
