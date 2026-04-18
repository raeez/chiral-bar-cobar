# Wave 3 (2026-04-18) — CY-C Pentagon attack-and-heal

Target: Wave-12 B90 heal of CY-C pentagon {3, 12, 24} stratification from `κ_ch^{R_i}` to `ρ^{R_i}`
(generator-lattice rank). CLAUDE.md B89/B90 + AP289 + AP290 discipline.

## 1. Attack ledger

### Core inscription (STRONG — no attack)

- **Home chapter inscription is correct**: `chapters/examples/cy_c_six_routes_generator_level_platonic.tex`
  (526 lines) + `chapters/examples/cy_c_pentagon_hypothesis_closures_platonic.tex` (578 lines). Both
  declare `\providecommand{\kch}{\kappa_{\mathrm{ch}}}% Hodge supertrace (route-independent, = 0 for
  K3 x E)` and `\providecommand{\rhoR}{\rho}% generator-lattice rank (route-dependent)`. The pentagon
  is explicitly inscribed with five intertwiners
  (`β_13, β_34, β_45, β_56, β_61`), R_2 as automorphic source (not a pentagon node via
  `β_{23}: A_X^{R_2,char} ↪ A_X^{R_3}` at character level only), and generator-rank stratification
  {3, 12, 24}. `cor:six-way-isomorphism-falsified` (line 210) and
  `prop:beta-13-not-isomorphism-counter-example` (line 379) explicitly reject the naive six-way
  isomorphism. `rem:rho-vs-kappa-ch-disambiguation` in the companion chapter (line 447) correctly
  states that "$\kappa_{\mathrm{ch}}^{R_i} \in \{3, 12, 24\}$ confuses a purely algebraic invariant
  ($\rho^{R_i}$) with the Hodge-supertrace ($\kappa_{\mathrm{ch}} = 0$)".
- **Four hypothesis closures (H1-H4)** inscribed as named theorems (Costello-Li chain-level,
  threefold Kummer Mayer-Vietoris, half-twist orbifold, HKR-Borcherds functorial lift), each with
  HZ-IV disjoint-verification blocks. Upgrade `thm:cy-c-pentagon-convergence-unconditional`
  (ClaimStatusProvedHere, line 478) closes four prior conditional hypotheses.
- **Test file structure is sound**:
  `compute/tests/test_cy_c_six_routes_generator_level.py` tests five ProvedHere claims against five
  disjoint-source buckets (Maulik-Okounkov, Huybrechts Chow motive, Kummer Mayer-Vietoris,
  kappa_bkm_universal, Niemeier classification).

### Finding F1 — AP290 κ_ch ↔ ρ type-swap persists in `cy_c_six_routes_convergence.tex`
(Severity: HIGH; category: AP290 type-swap + AP149 propagation failure)

The sister chapter `chapters/examples/cy_c_six_routes_convergence.tex` (scalar-level companion to
the pentagon) carries the heal inconsistently:
- Line 414 (`thm:kappa-stratification-CY-C` part (i)): correctly states `κ_ch(X) = Σ (-1)^q
  h^{0,q}(X) = 0` route-independent.
- Line 414 part (iv): correctly defines the route-dependent invariant as `ρ^{R_i}`, stratifying
  {3, 12, 24}.
- Line 64 (`rem:cy-c-exclusions`): STALE — writes `κ_{\mathrm{ch}}^{R_i}(X) = κ_{\mathrm{ch}}^{R_j}(X)`
  as the thing CY-C is NOT; should read `ρ^{R_i}(X) = ρ^{R_j}(X)`.
- Line 460 (`rem:kappa-k3e-never-bare`): STALE — writes "$\kappa_{\mathrm{ch}}^{R_i}$ for the
  algebraization invariant with explicit route (values $3, 12, 24$ depending on $i$)". This is the
  exact AP290 type-swap the chapter elsewhere retracts.
- Line 513 (Concluding remarks): STALE — "the algebraization invariant $\kappa_{\mathrm{ch}}^{R_i}$
  is route-dependent with four distinct values". Recommits the error the chapter's own
  disambiguation remark corrects at line 447.

### Finding F2 — AP5/AP149 propagation failure: κ_ch(K3×E) = 3 persists across 30+ sites
(Severity: HIGH; category: AP5 cross-chapter propagation + AP289 Künneth-multiplicative)

Grep `\kappa_{\mathrm{ch}}.*=\s*3` returns 30+ hits in Vol III under the stale additive semantics
`κ_ch(K3×E) = κ_ch(K3) + κ_ch(E) = 2 + 1 = 3` (AP289 violation: Hodge supertrace is Künneth
MULTIPLICATIVE, not additive). Sites:
- **`main.tex:446`** (`κ_ch(K3 × E) = 3`).
- **`main.tex:496`** (κ•-spectrum: `{κ_cat = 0, κ_ch = 3, κ_BKM = 5, κ_fiber = 24}`).
- **`main.tex:903`** (`κ_ch = 3` under `dim_C` brace).
- **`chapters/frame/preface.tex:120, 545, 869, 988`** (four independent hits, including climax
  prose at 545: `$\kappa_{\mathrm{ch}} = 3$ is constant around the cycle`).
- **`chapters/examples/quantum_group_reps.tex:550`** (spectrum recital).
- **`chapters/examples/k3e_cy3_programme.tex:983, 1317, 1667, 1690, 1776, 2987, 3044, 3085`** (eight
  hits in the K3×E flagship chapter; line 983 explicitly carries the AP289 violation
  `κ_ch = 3 = κ_ch(K3) + κ_ch(E) = 2 + 1`).
- `working_notes.tex` (15+ hits — lower priority; session-ledger scope).
- `notes/physics_topological_strings.tex:972`, `notes/theory_denominator_bar_euler.tex:758`
  (notes/ ledger, AP288 scope).

The correct Wave-12 value is `κ_ch(K3×E) = 0` via Hodge supertrace $Ξ(X) = \sum_q (-1)^q h^{0,q}(X)$,
with $h^{0,q}(K3 × E) = (1,1,1,1)$ giving $1-1+1-1 = 0$. The "= 3" sites match the naive
`dim_C(X) = 3` interpretation, which is the GENERATOR RANK $\rho^{R_1}$ of $\Phi_3$, not $\kappa_{\mathrm{ch}}$.

### Finding F3 — Test file uses stale variable names κ_CH_PENTAGON / κ_CH_STRATA for ρ values
(Severity: MODERATE; category: AP277 vacuous decorator variant + AP290)

`compute/tests/test_cy_c_six_routes_generator_level.py:52-66` declares:
```
KAPPA_CH_PENTAGON = { "R1": F(3), "R3": F(24), "R4": F(12), "R5": F(3), "R6": F(3) }
KAPPA_CH_STRATA  = { F(3): {"R1","R5","R6"}, F(12): {"R4"}, F(24): {"R3"} }
```
Test methods named `test_beta_13_injection_preserves_kappa_3` etc. The VALUES are correct
(they are the ρ values); the NAMES carry κ_ch semantics. Line 558: `KAPPA_BKM_K3E not in
chiral_algebra_invariant  # 5 not in {3, 12, 24}` — the assertion compares κ_BKM (5) against ρ
values {3,12,24}, labelled as "chiral_algebra_invariant"; the inequality holds but the prose is
confused (κ_BKM and ρ are different invariant species, not the same invariant at different values).
HZ-IV decorator `derived_from` / `verified_against` prose still names "kappa_ch" as the
stratification invariant (lines 146-162, 202-217, 272-287). AP290 type-swap at the code/prose
layer even though the `.tex` heal is correct.

### Finding F4 — Internal proof-body inconsistency at `cy_c_six_routes_generator_level_platonic.tex:220-221`
(Severity: LOW; category: proof-prose naming drift)

`cor:six-way-isomorphism-falsified` proof (line 220-221): "$\rhoR$ is a bar-complex invariant of
the chiral algebra (Vol~I Thm~H amplitude concentration), hence isomorphism-invariant." The
invariance attribution to "Vol~I Thm~H amplitude concentration" is incorrect: Thm H concentrates
ChirHoch^* of A in degrees {0,1,2} (sharp Hilbert series), it does NOT guarantee generator-rank
invariance. Generator-rank invariance follows from ρ being defined on the degree-0 strong
generators of A, which are preserved by chiral-algebra isomorphism by construction. Minor
attribution drift; the conclusion is correct but the citation is phantom.

### Finding F5 — HZ-IV non-disjoint dependency risk at pentagon-convergence-unconditional
(Severity: MODERATE; category: AP243)

The upgrade theorem (line 478) at `cy_c_pentagon_hypothesis_closures_platonic.tex:570-575`
verifies against "the Francis-Gaitsgory (∞,2)-adjoint framework (Vol I Theorem A^{∞,2})".
But Vol I `theorem_A_infinity_2.tex` is itself CONDITIONAL on (a) Francis-Gaitsgory GR17
six-functor base-change and (b) Mok25 logarithmic factorization-gluing (CLAUDE.md Theorem A row,
AP249). Using a CONDITIONAL Vol I theorem as the disjoint verification of the pentagon-convergence
unconditional-upgrade creates a dependency where the "upgrade from ProvedHereConditional to
ProvedHere" relies on a theorem that is itself CONDITIONAL. The
colimit-universal-property verification still earns its keep (Lurie colimit preservation for
symmetric-monoidal ∞-cats is internal to the ∞-categorical machinery), but the HZ-IV prose
advertising Vol I Theorem A^{∞,2} as "disjoint verification" is drift. Either (i) restrict
verification to Lurie's in-framework universal property (genuinely internal and unconditional), or
(ii) tag the upgrade `\ClaimStatusConditional` on Vol I Theorem A^{∞,2} modular-family extension.

## 2. Surviving core (Drinfeld-voice)

The pentagon is a five-node diagram of five intertwiners
$R_1 \xhookrightarrow{\beta_{13}} R_3 \twoheadrightarrow^{\beta_{34}} R_4 \twoheadrightarrow^{\beta_{45}} R_5
\xrightarrow[\sim]{\beta_{56}} R_6 \xrightarrow[\sim]{\beta_{61}} R_1$ stratified into three types
(one injection, two surjections, two isomorphisms) by the generator-lattice rank $\rho^{R_i} \in
\{3, 12, 24\}$; the Hodge-supertrace invariant $\kappa_{\mathrm{ch}}(K3 \times E) = \sum_q (-1)^q
h^{0,q} = 1-1+1-1 = 0$ is Künneth-MULTIPLICATIVE (Ξ(K3)·Ξ(E) = 2·0 = 0), route-independent, and
does NOT stratify the pentagon. $R_2$ (Borcherds BKM superalgebra) enters as an automorphic-source
branch $\beta_{23}: A_X^{R_2,\mathrm{char}} \hookrightarrow A_X^{R_3}$ at character level only, not
as a pentagon node. The quantum vertex chiral group $G(K3 \times E)$ is the colimit of the pentagon
(Proposition~cy-c-pentagon-colimit), and the prior "six routes converge isomorphically" formulation
is falsified by the ρ-stratification. Four previously-conditional hypotheses (Costello-Li
chain-level, threefold Kummer Mayer-Vietoris, half-twist orbifold, HKR-Borcherds functorial lift)
are closed as named theorems H1-H4, upgrading the convergence theorem from ProvedHereConditional
to ProvedHere (modulo F5 scope).

## 3. Heal plan (per-finding, status-tagged)

| # | Finding | Heal | Status |
|---|---------|------|--------|
| F1 | Three residual AP290 type-swaps in `cy_c_six_routes_convergence.tex` (L64, L460, L513) | Rewrite `\kappa_{\mathrm{ch}}^{R_i}` → `\rho^{R_i}` in these three prose sites; add explicit cross-reference to `rem:rho-vs-kappa-ch-disambiguation` | Heal scoped; deferrable to standalone editing pass |
| F2 | 30+ consumer sites with `κ_ch(K3×E) = 3` | AP5/AP149 propagation pass: replace `κ_ch = 3` → `ρ^{R_1} = 3 (algebraic), κ_ch = 0 (Hodge supertrace)` at each of: `main.tex:446, 496, 903`; `preface.tex:120, 545, 869, 988`; `quantum_group_reps.tex:550`; `k3e_cy3_programme.tex` ×8; `introduction.tex:832`. Notes/ sites can be annotated with top-of-file "HISTORICAL — pre-Wave-12 semantics" banner per AP288 | Load-bearing; multi-file propagation pass required |
| F3 | Test file variable names / HZ-IV prose use stale `KAPPA_CH` semantics | Global rename `KAPPA_CH_PENTAGON → RHO_PENTAGON`; `KAPPA_CH_STRATA → RHO_STRATA`; rewrite HZ-IV prose to name "generator-lattice rank ρ"; keep test ASSERTION values unchanged | Mechanical; single-file |
| F4 | `cor:six-way-isomorphism-falsified` proof attributes ρ-invariance to Vol I Thm H | Replace "Vol I Thm H amplitude concentration" with "isomorphism-invariance of the degree-0 strong-generator rank of the chiral algebra" (direct, no Vol I citation needed) | Minor prose fix |
| F5 | Pentagon-convergence-unconditional HZ-IV cites Vol I Thm A^{∞,2} which is itself conditional | Restrict disjoint verification to "Lurie symmetric-monoidal colimit-preservation (internal, unconditional)" OR tag upgrade `\ClaimStatusConditional` on Vol I Thm A^{∞,2} modular-family extension (AP249) | Scope-restriction; single-site |

AP266 sharpening opportunity (bonus): the "R_2 is source, not node" retraction can be sharpened
by inscribing the explicit cohomology class obstructing R_2 from being a pentagon node:
$[R_2 \to R_i]$ for $i \ne 3$ would require a Lie-superalgebra-to-chiral-algebra functor that
does not exist (R_2's output $\mathfrak{g}_{\Delta_5}$ is a Lie superalgebra, no chiral-algebra
structure), giving $\mathrm{Obs}_{R_2\text{-as-node}} \in \mathrm{Hom}(\text{LieSAlg}, \text{ChirAlg}) = 0$.

## 4. Commit plan

NO COMMITS this session. Attack-heal note only. Future session inscription order:
1. F1 (3 sites, single-file, no cross-volume propagation) — 1 atomic edit.
2. F4 (1 prose fix in proof body) — 1 atomic edit.
3. F5 (scope-restriction of HZ-IV verification prose) — 1 atomic edit.
4. F3 (test file rename + HZ-IV prose rewrite) — 1 atomic edit, then `make test`.
5. F2 propagation (30+ sites across 4 files + 2 climax files) — ONE atomic AP5 commit, preceded
   by fresh grep census, with PE-5 template applied at each edit site (HZ-7 Vol III κ-subscript
   discipline mandatory). Verify `main.tex` and `preface.tex` build cleanly before committing.

Per CONSTITUTIONAL TRUST WARNING and HZ-IV discipline: ALL commits authored by Raeez Lorgat ONLY.

## 5. Cache entries (to append to `notes/first_principles_cache_comprehensive.md`)

- **Pattern 246 (AP289 Künneth-multiplicative on Hodge supertrace).** Confusion trigger: any
  `κ_ch(X × Y) = κ_ch(X) + κ_ch(Y)` on CY products. Correct: Hodge supertrace
  $\Xi(X×Y) = \Xi(X) \cdot \Xi(Y)$ (multiplicative). Canonical value: $\kappa_{\mathrm{ch}}(K3 \times E)
  = \Xi(K3) \cdot \Xi(E) = 2 \cdot 0 = 0$, NOT $2+1 = 3$. The additive-reading "3" is
  $\rho^{R_1}(K3 \times E) = \dim_{\mathbb{C}}(K3 \times E)$ = generator rank of $\Phi_3$, a
  DIFFERENT invariant. Source: thm:kappa-stratification-CY-C (i) at
  `cy_c_six_routes_convergence.tex:411`; Vol I B89/B90.
- **Pattern 247 (AP290 κ/ρ type-swap at K3×E).** Confusion trigger: any `\kappa_{\mathrm{ch}}^{R_i}
  \in \{3, 12, 24\}` expression. Correct: the pentagon stratifies the GENERATOR-LATTICE RANK
  $\rho^{R_i}$, NOT the Hodge-supertrace $\kappa_{\mathrm{ch}}$. Grep trigger:
  `\kappa_\{\\?mathrm\{ch\}\}\^\{R_\d`. Cross-check: is the invariant defined as the number of
  strong generators of the chiral algebra? (→ ρ) or as the Hodge alternating sum $\sum_q (-1)^q
  h^{0,q}$? (→ κ_ch). Canonical values at K3×E: ρ ∈ {3,12,24} (route-dependent algebraic);
  κ_ch = 0 (route-independent Hodge supertrace).
