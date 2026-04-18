# CY-C pentagon stratification: attack-and-heal audit (2026-04-18)

Target: Vol III CY-C pentagon `{3, 12, 24}` stratification, post-`cade61c` state.

Mission: verify the `cade61c` commit's heal actually propagated from κ_ch to ρ^{R_i}
across all inscription sites, audit the five intertwiners, R_2 source-branch
orientation, Hodge-supertrace κ_ch = 0 for K3 × E, and surface any residual
AP300 / AP290 / AP312 / AP289 drift.

Author: Raeez Lorgat. No AI attribution.


## Executive verdict

The pentagon STRUCTURE is sound. The `cade61c` heal installed ρ^{R_i} as the
stratification invariant at the load-bearing theorem
`thm:kappa-stratification-CY-C` and in the main pentagon construction in
`cy_c_six_routes_generator_level_platonic.tex`. Five named intertwiners
β_{13}, β_{34}, β_{45}, β_{56}, β_{61} are inscribed with explicit stratification
types (injection / surjection / isomorphism) and explicit construction prose.
R_2 is consistently pinned as a source (produces BKM Lie superalgebra, not a
chiral algebra) with auxiliary arrow β_{23} at character level only.

The heal is INCOMPLETE. Three classes of residual drift remain:

1. **AP300 same-file retracted-mechanism drift** inside
   `cy_c_six_routes_convergence.tex`: the theorem
   `thm:kappa-stratification-CY-C` correctly says κ_ch = 0 (Hodge supertrace,
   route-independent) and ρ^{R_i} ∈ {3, 12, 24} (generator rank, route-dependent).
   The SAME FILE contains `prop:kappa-spectrum-k3-healed` (lines 468–492) which
   writes `κ_ch^{R_1}(S) = 2`, `κ_ch^{R_3}(S) = 24`, `κ_ch^{R_5}(S) = 2` —
   exactly the category error the Wave `cade61c` heal retracted at
   `rem:rho-vs-kappa-ch-disambiguation` (line 447–456, which explicitly says
   "Writing κ_ch^{R_i} ∈ {3, 12, 24} confuses a purely algebraic invariant
   (ρ^{R_i}) with the Hodge-supertrace (κ_ch = 0)"). The section-opening prose
   at line 404 and the concluding remark at line 513 repeat the retracted
   framing.

2. **AP312 three-way cross-file scalar-value contradiction** for
   κ_ch(K3 × E):
   - Value **0** (Hodge supertrace, Künneth-multiplicative, χ(O_{K3×E}) =
     χ(O_{K3}) · χ(O_E) = 2 · 0 = 0): `cy_c_six_routes_convergence.tex:411`,
     `cy_c_six_routes_generator_level_platonic.tex:65`,
     `quantum_group_reps.tex:932`.
   - Value **3** via additivity κ_ch(K3) + κ_ch(E) = 2 + 1 = 3:
     `k3e_cy3_programme.tex:333, 983, 1825, 3052`; `k3e_bkm_chapter.tex:980,
     1137, 1250, 1352`; `k3_chiral_algebra.tex:241, 449, 506, 541`;
     `quantum_group_reps.tex:1115`.
   Canonical κ_ch (per CLAUDE.md B90 and `thm:kappa-hodge-supertrace-identification`)
   is the Hodge supertrace = 0. The "κ_ch = 3" sites silently redefine κ_ch
   as complex dimension / de Rham primitive rank (which IS additive under
   products). No cross-file bridge remark exists; the two conventions
   collide route-for-route with the pentagon-stratification claim.

3. **AP289 Künneth-multiplicative vs additive** contamination: several sites
   assert "κ_ch is additive under CY products" (e.g.
   `k3e_cy3_programme.tex:333`, `k3_chiral_algebra.tex:506`,
   `test_cy_c_six_routes.py:138`). Additivity holds for complex dimension
   dim_C, NOT for the Hodge supertrace Σ (-1)^q h^{0,q}. The theorem
   `thm:kappa-hodge-supertrace-identification` forces multiplicativity; the
   "additivity of κ_ch" framing is a holdover from the pre-`cade61c` convention
   and is geometrically wrong under the healed definition.

Additionally the "N=1 coincidence" narrative `κ_BKM = κ_ch(K3) + κ_ch(K3×E) =
2 + 3 = 5` appears verbatim at `k3e_cy3_programme.tex:1824`,
`k3_chiral_algebra.tex:512`, `k3e_bkm_chapter.tex:1137–1140`, and
`test_cy_c_six_routes.py:393`. CLAUDE.md B88 + the status-table CY-D row
retracted this as confabulation 2026-04-17 (the correct value κ_BKM(Φ_1) = 5
comes from Gritsenko Δ_5 weight-5 paramodular form, not from a decomposition).
AP149 resolution-propagation failure: the retraction did not land on Vol III
manuscript sites.


## Detailed findings

### (i) Pentagon inscription locus

Three files carry the pentagon machinery:

- `chapters/examples/cy_c_six_routes_convergence.tex` (1536 lines) — scalar
  convergence, α_{ij} pairwise bridges, κ-stratification theorem.
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex` (526 lines) —
  generator-level upgrade, pentagon β_{ij}, colimit identification.
- `chapters/examples/cy_c_pentagon_hypothesis_closures_platonic.tex` (577
  lines) — four hypothesis closures (H1 Costello-Li; H2 threefold Kummer;
  H3 half-twist orbifold; H4 HKR-Borcherds).

Cross-referenced: `quantum_group_reps.tex:922–936` has a pentagon
stratification remark; `k3_yangian_chapter.tex`, `k3e_cy3_programme.tex`,
`k3_chiral_algebra.tex`, `k3e_bkm_chapter.tex` use κ_ch values that contradict
the pentagon heal.


### (ii) ρ^{R_i} discipline at the load-bearing theorem

`thm:kappa-stratification-CY-C` (`cy_c_six_routes_convergence.tex:406–426`) is
the pentagon-healing theorem. Its statement and proof are clean:
- (i) κ_ch(X) = Σ (-1)^q h^{0,q}(X) = 0 route-independent (verified Künneth
  h^{0,q}(K3 × E) = (1,1,1,1) → alternating sum 0).
- (ii) κ_cat(X) = χ(O_X) = 0 manifold invariant (verified χ(O_{K3×E}) =
  χ(O_{K3}) · χ(O_E) = 2 · 0 = 0).
- (iii) κ_fiber(X) = 24.
- (iv) ρ^{R_i}(X) route-dependent: {3, 12, 24}.
- (v) κ_BKM(X) = 5, attached to R_2 only.

The main pentagon theorem
`thm:cy-c-six-routes-generator-level-convergence` at
`cy_c_six_routes_generator_level_platonic.tex:281` correctly uses ρ^{R_i}
throughout (three strata `{A_X^{R_1}, A_X^{R_5}, A_X^{R_6}} at ρ = 3`,
`{A_X^{R_4}} at ρ = 12`, `{A_X^{R_3}} at ρ = 24`).

Verdict: at the load-bearing theorem sites the heal landed correctly.


### (iii) Residual AP300 in `cy_c_six_routes_convergence.tex`

Four sites in the same file that hosts `rem:rho-vs-kappa-ch-disambiguation`
still write κ_ch^{R_i} as a route-dependent invariant taking values
{2, 2, 24}:

- **Line 64** (chapter overview, preface-level prose): "CY-C is not the
  statement that κ_ch^{R_i}(X) = κ_ch^{R_j}(X) for all pairs. The modular
  characteristic depends on the route." The framing admits κ_ch^{R_i}
  exists as a route-dependent quantity — contradicting the retraction 340
  lines below.

- **Line 404** (section opener for `thm:kappa-stratification-CY-C`): "The
  modular characteristic κ_ch^{R_i}(X) is a priori a function of the route."
  The theorem itself then proves κ_ch is route-INDEPENDENT equal to 0 and
  ρ^{R_i} is the route-dependent invariant. The section opener phrases the
  question as if the theorem's conclusion were open.

- **Lines 475–479** (`prop:kappa-spectrum-k3-healed`, inscribed as
  ClaimStatusProvedHere). Verbatim:
  ```
  (iii) κ_ch^{R_5}(S) = 2 (sigma-model central charge: c = 6, bar
        coefficient 2).
  (iv)  κ_ch^{R_1}(S) = χ(O_S) = 2 (CY-to-chiral correspondence Φ_2).
  (v)   κ_ch^{R_3}(S) = 24 (lattice-VOA rank: Mukai lattice rank 24).
  ```
  Same category error as the retracted naive pentagon: assigning
  `κ_ch^{R_i}` values of 2, 2, 24 on K3. Under the healed definition
  κ_ch(K3) = χ(O_{K3}) = 2 is route-independent. The three route-dependent
  values are: c(R_5)/2 = 3 for sigma-model (but the central-charge
  convention was already flagged AP290 elsewhere), ρ^{R_1}(K3) = 2 (de Rham
  primitive rank at d=2), ρ^{R_3}(K3) = 24 (Mukai lattice rank). So the
  PROP is tracking ρ^{R_i} and central-charge mixed under the
  κ_ch^{R_i} letter.

- **Line 513** (concluding remark): "the algebraization invariant
  κ_ch^{R_i} is route-dependent with four distinct values". Direct
  contradiction of `thm:kappa-stratification-CY-C`(i,iv).

This is AP300: `ClaimStatusProvedHere` proposition
`prop:kappa-spectrum-k3-healed` + framing prose use a mechanism that
`rem:rho-vs-kappa-ch-disambiguation` (earlier in the same file) explicitly
retracts. Paired AP290 (κ-subscript type-swap: ρ formula assigned to κ_ch).


### (iv) Three-way cross-file contradiction (AP312)

**κ_ch(K3 × E) = 0** sites (Hodge supertrace convention):
- `cy_c_six_routes_convergence.tex:411` (the healed theorem).
- `cy_c_six_routes_generator_level_platonic.tex:65`.
- `quantum_group_reps.tex:932` ("κ_ch(K3 × E) = χ^Hodge(K3) · χ^Hodge(E) =
  2 · 0 = 0").

**κ_ch(K3 × E) = 3** sites (complex dimension / de Rham primitive rank
convention, additive under products):
- `k3e_cy3_programme.tex:333–334`: "Additivity. κ_ch(K3 × E) = κ_ch(K3) +
  κ_ch(E) = 2 + 1 = 3 = dim_C(K3 × E)".
- `k3e_cy3_programme.tex:983, 1824–1827, 3052`.
- `k3e_bkm_chapter.tex:980, 1137–1140, 1250, 1352`.
- `k3_chiral_algebra.tex:241, 449, 506, 541`.
- `quantum_group_reps.tex:1115`.

Neither convention is wrong in isolation; they are DIFFERENT INVARIANTS both
sailing under the κ_ch letter:

- Definition A: κ_ch(X) = Σ_q (-1)^q h^{0,q}(X) = χ(O_X). Künneth-MULTIPLICATIVE.
  K3: 2. E: 0. K3 × E: 0.
- Definition B: κ_ch(X) = dim_C X (or "primitive generator count"). ADDITIVE
  under products. K3: 2. E: 1. K3 × E: 3.

CLAUDE.md B90 + `thm:kappa-hodge-supertrace-identification` make Definition A
canonical. The `k3e_cy3_programme` + `k3e_bkm_chapter` + `k3_chiral_algebra`
sites use Definition B and write κ_ch.

**AP289 Künneth-multiplicative vs additive**: the "additivity of κ_ch"
prose is DIRECTLY the failure pattern AP289 catches (Hodge supertrace is
Künneth-multiplicative, not additive under products). At K3 × E the two
conventions happen to disagree (0 vs 3); at K3 × K3 they would give 4 vs
4 (coincidence); at E × E they give 0 vs 2 (disagree). The product-convention
collision is observable.


### (v) Test-file AP288 label-disjoint / computation-identical

`compute/tests/test_cy_c_six_routes.py:130–157`:
```
spectrum = {
  ...
  ("kappa_ch_R4", "K3xE"): F(12),
  ("kappa_ch_R3", "K3xE"): F(24),
}
...
def test_kappa_ch_additive_under_products_R1(self):
    """kappa_ch^{R1}(K3) + kappa_ch^{R1}(E) = 2 + 1 = 3 = kappa_ch^{R1}(K3 x E)."""
```

The variable names carry κ_ch but the values are the ρ^{R_i} generator ranks
(12, 24) on R_4, R_3; and on R_1 the value 3 is dim_C X = ρ^{R_1}. Under the
healed ρ vs κ_ch disambiguation, these test lines should rename to ρ^{R_i}
or be annotated as testing ρ under a legacy label. AP290 κ-subscript
type-swap at the test layer.

Line 393 of the same test file self-admits "AP-CY37: kappa_BKM = kappa_ch +
chi(O_S) is a coincidence for N=1." Under the retracted "N=1 coincidence"
narrative (CLAUDE.md 2026-04-17 CY-D row, B88), this decomposition is
confabulation: κ_BKM(Φ_1) = 5 via Gritsenko Δ_5, with no decomposition
κ_BKM = κ_ch + χ(O_S) = 3 + 2 valid at any N. The test inscription preserves
the retracted narrative.


### (vi) AP149 propagation failure on "N=1 coincidence"

Verbatim "κ_BKM = κ_ch(K3) + κ_ch(K3×E) = 2 + 3 = 5" appears at:
- `k3e_cy3_programme.tex:1824–1827, 1856`.
- `k3_chiral_algebra.tex:512`.
- `k3e_bkm_chapter.tex:1137–1140`.
- `test_cy_c_six_routes.py:393`.

CLAUDE.md CY-D row says "naive decomposition κ_BKM = κ_ch + χ(O_fiber) holds
at NO N (already fails at N=1: 5 ≠ 0); the prior 'N=1 coincidence' narrative
is retracted as confabulation (HEAL 2026-04-17)." The retraction is visible
in CLAUDE.md but did not propagate to the Vol III manuscript.


### (vii) Five intertwiners: explicitness audit

All five pentagon arrows are inscribed with explicit construction prose, not
merely existentially:

- β_{13}: K3 elliptic genus 2φ_{0,1} decomposes Mukai-lattice Fock space into
  rank-3 primitive part + 21 secondary rank, rank-3 identified with
  Φ_3(D^b(Coh(X))) via HKR (`cy_c_six_routes_generator_level_platonic.tex:192–
  198`).
- β_{34}: Z/2-orbifold Mayer-Vietoris count 8 + 16 = 24 → 12 via
  `kummer_excision_verification.py`; closed by
  `thm:h2-threefold-kummer-lift` (H2 hypothesis closure).
- β_{45}: half-twist from ρ=12 BPS ring to ρ=3 primitive sector; closed by
  `thm:h3-half-twist-orbifold-identification`.
- β_{56}: Costello-Li holomorphic-twist compactification; closed by
  `thm:h1-costello-li-chain-level-factorisation`.
- β_{61}: Costello-Li / Φ_3 identification, closed by
  `thm:h4-hkr-borcherds-functorial-lift`.

Verdict: no AP241 (advertised-but-not-inscribed) violation on the
intertwiners themselves. The four hypothesis closures H1–H4 are inscribed
in `cy_c_pentagon_hypothesis_closures_platonic.tex` with ClaimStatusProvedHere
tags; their own audit is out of scope for this attack but was not challenged
by the present pass.


### (viii) R_2 source branch orientation

Consistent throughout:

- `cy_c_six_routes_generator_level_platonic.tex:56`: "R_2 is a source not a
  node".
- `cy_c_six_routes_generator_level_platonic.tex:134`: "R_2 does not produce
  a chiral algebra: it produces the Lie superalgebra g_BKM".
- β_{23}: A_X^{R_2, char} ↪ A_X^{R_3} at character level only (line 154).
- `quantum_group_reps.tex:928`: "R_2 as the source branch".

R_2 source orientation carries no AP288 or AP263 ambiguity: the Lie
superalgebra status is a proved negative (R_2 produces g_BKM which is not
a chiral algebra; any "chiral algebra" associated with R_2 would be its
vacuum representation's VOA, which is R_3). The five-node pentagon is
literally five nodes, not six-minus-one by convention.


### (ix) Hodge supertrace verification

Mission statement's sketch: χ(O_E) = 0 via g(E) = 1, χ(O_{K3×E}) =
χ(O_{K3}) · χ(O_E) = 2 · 0 = 0. Verification:

E elliptic curve: h^{0,0}(E) = 1, h^{0,1}(E) = g(E) = 1 ⇒ χ(O_E) = 1 - 1 = 0. ✓

K3: h^{0,0} = 1, h^{0,1} = 0, h^{0,2} = 1 ⇒ χ(O_{K3}) = 1 - 0 + 1 = 2. ✓

K3 × E via Künneth h^{0,q}(K3 × E) = Σ_{a+b=q} h^{0,a}(K3) · h^{0,b}(E):
- q = 0: 1·1 = 1.
- q = 1: 1·1 + 0·1 = 1.
- q = 2: 1·0 + 0·1 + 1·1 = 1 (h^{0,2}(E) = 0).
- q = 3: 0·0 + 1·1 + 0·0 = 1 (h^{0,3}(K3) = 0, h^{0,3}(E) = 0).

Alternating sum 1 - 1 + 1 - 1 = 0. ✓

χ(O_{K3×E}) = 2 · 0 = 0. ✓

The healed theorem `thm:kappa-stratification-CY-C`(i,ii) is numerically
correct. The "κ_ch(K3 × E) = 3" sites are using a DIFFERENT definition of
κ_ch (complex dimension additivity), not a wrong computation under the
healed definition.


## Heal plan

Three tiers of rectification, in priority order:

### Tier 1: Same-file AP300 repair in `cy_c_six_routes_convergence.tex`

(a) `prop:kappa-spectrum-k3-healed` at line 468: rename clauses (iii,iv,v)
from κ_ch^{R_i} to ρ^{R_i} or restate with explicit convention split. Two
honest options:
   - **Option A** (rename to ρ): clauses (iii) ρ^{R_5}(K3) = 2, (iv)
     ρ^{R_1}(K3) = 2 (with κ_ch(K3) = χ(O_K3) = 2 as a separate manifold
     remark), (v) ρ^{R_3}(K3) = 24. Matches Main theorem at line 406.
   - **Option B** (introduce "κ_ch, naive" with an explicit scope-remark that
     this is NOT the Hodge supertrace but a legacy label for ρ). Technically
     valid but AP234/AP311 letter-collision risk.
   Recommend Option A.

(b) Line 64 chapter overview and line 404 section opener: rephrase "the
modular characteristic κ_ch^{R_i} depends on the route" to "the generator
rank ρ^{R_i} depends on the route; κ_ch is route-independent" to match
the theorem's conclusion.

(c) Line 513 concluding remark: rewrite "the algebraization invariant
κ_ch^{R_i} is route-dependent with four distinct values" → "the
algebraization invariant ρ^{R_i} is route-dependent with three distinct
values {3, 12, 24}; κ_ch = 0 is route-independent."

### Tier 2: Cross-file AP312 propagation on κ_ch(K3 × E) = 0 vs 3

Two honest options:

- **Option A** (rename κ_ch → ρ at the "3" sites): at
  `k3e_cy3_programme.tex:333, 983, 1825, 3052`; `k3e_bkm_chapter.tex:980,
  1137, 1250, 1352`; `k3_chiral_algebra.tex:241, 449, 506, 541`;
  `quantum_group_reps.tex:1115`, replace κ_ch(K3 × E) = 3 with
  ρ^{R_1}(K3 × E) = dim_C(K3 × E) = 3, or κ_fiber^{dim}(K3 × E) = 3, with
  a convention-bridge remark. Preserves the "3 is the chiral invariant
  tracked by each programme chapter" intuition without letter-collision.

- **Option B** (introduce two subscripts κ_ch^{Hodge} and κ_ch^{dim}):
  more explicit but expands the κ_{...} registry further and violates the
  HZ-7 closed subscript set `{ch, cat, BKM, fiber}`. Not recommended.

Option A aligns with CLAUDE.md CY-D B90 (the stratification is GENERATOR
RANK ρ^{R_i}, orthogonal to κ_ch).

### Tier 3: "N=1 coincidence" retraction propagation (AP149)

At `k3e_cy3_programme.tex:1824–1827, 1856`, `k3_chiral_algebra.tex:512`,
`k3e_bkm_chapter.tex:1137–1140`, `test_cy_c_six_routes.py:393`:

Replace `κ_BKM = κ_ch(K3) + κ_ch(K3 × E) = 2 + 3 = 5` with a plain remark
that κ_BKM(Φ_1) = 5 via Gritsenko 1999 Δ_5 weight-5 paramodular form of
level 1 (matching CLAUDE.md CY-D healed entry). Explicit note that the
decomposition `κ_BKM = κ_ch + χ(O_fiber)` is NOT an identity at any N
(fails at N=1 where 5 ≠ 0 + 2, fails at N ≥ 2 by Borcherds weight formula),
per B88.

### Tier 4: Test file AP288/AP290 relabeling

`test_cy_c_six_routes.py`:
- Lines 131–132: rename `kappa_ch_R3`, `kappa_ch_R4` spectrum keys to
  `rho_R3`, `rho_R4`.
- Lines 138–146: rename `test_kappa_ch_additive_under_products_R1` →
  `test_rho_R1_additive_under_products` with docstring naming the
  invariant as generator rank (dim_C X additive under products).
- Lines 148–157: rename `test_kappa_ch_not_additive_for_kappa_cat` →
  `test_kappa_ch_multiplicative_via_Kunneth`; the test body is correct
  (κ_cat = χ(O_X) Künneth-multiplicative) but the test NAME mischaracterises
  the comparison.
- Lines 390–410: retract the "N=1 coincidence" test (AP-CY37) per
  Tier-3 above. Replace with a test that κ_BKM(Φ_1) = 5 via a Δ_5 Fourier
  coefficient engine, consistent with CLAUDE.md CY-D B90.


## Sharpened-obstruction frontier (AP266 style)

Beyond the letter-collision and propagation cleanup, the pentagon heal
leaves one honest mathematical frontier: the isomorphism
`G(K3 × E) = colim(Pentagon)` in `prop:cy-c-pentagon-colimit` is stated
conditional on the four hypotheses H1–H4 in
`cy_c_pentagon_hypothesis_closures_platonic.tex`. The heal commit `cade61c`
did not touch those hypothesis closures. Each is itself
`ClaimStatusProvedHere`, but independent audit of H1 (Costello-Li
chain-level factorization at d=3) would surface:

- Whether the BV-chain-level factorization claim is genuinely proved
  cohain-level or only cohomologically (AP258 cohomological-vs-chain-level
  status drift).
- Whether the cited Costello-Gwilliam Vol 2 Ch 2 result IS about the
  CY_3 hCS theory at chain level or only at the factorization algebra level
  on R^6, with the curve-restriction bridge AP249 cited but not inscribed.

These are follow-up frontier items. For the present audit, the pentagon
heal propagation is the primary deliverable.


## Worktree patch (AP316)

This audit was performed by direct read on the main-repo paths, not in a
worktree. No patch file needed. All edits described in Heal Plan Tiers
1–4 are one-shot find-and-replace operations that can be performed in the
main working tree without concurrency risk.

Patch summary for implementation:

```
# Tier 1: cy_c_six_routes_convergence.tex
sed -i '' 's/\\kappa_{\\mathrm{ch}}^{R_\([0-9]\)}/\\rho^{R_\1}/g' \
  chapters/examples/cy_c_six_routes_convergence.tex
# then rewrite the narrative prose at lines 64, 404, 513 by hand (prose edits
# are not safe under sed).
# plus inscribe rem:kappa-ch-vs-rho-stratification naming the convention split.

# Tier 2: cross-file κ_ch(K3 × E) = 3 → ρ^{R_1}(K3 × E) = 3
grep -l 'kappa_{\\mathrm{ch}}(K3 \\times E)' chapters/examples/*.tex \
  | xargs # manual review of each site; Option A rename

# Tier 3: Retract N=1 coincidence
# grep for literal '2 + 3 = 5' and replace with Gritsenko Δ_5 remark.

# Tier 4: Test rename in compute/tests/test_cy_c_six_routes.py
```

Every edit above is within Vol III. No Vol I or Vol II propagation required
because the residue lives in the CY-C chapter cluster and its test file.
CLAUDE.md references to "CY-C pentagon κ_ch stratification {3,12,24} →
CATEGORY ERROR" (B89/B90) remain accurate post-heal.


## Anti-patterns registered (AP981–AP1000 pool)

**AP983 (Retracted-convention residue in ClaimStatusProvedHere proposition,
same file as the retraction remark).** A chapter inscribes `rem:...` that
explicitly labels a mechanism or convention as a category error; the same
chapter contains a ClaimStatusProvedHere proposition that uses precisely
that retracted mechanism. Stronger than AP300 (lemma-vs-retraction drift in
same file) because the consumer is a ClaimStatusProvedHere proposition with
its own proof body, not an intermediate lemma. Canonical violation this audit:
`cy_c_six_routes_convergence.tex` carries `rem:rho-vs-kappa-ch-disambiguation`
(line 447) retracting "writing κ_ch^{R_i} ∈ {3, 12, 24} confuses ρ^{R_i} with
Hodge supertrace"; 21 lines later `prop:kappa-spectrum-k3-healed` (line 468,
ClaimStatusProvedHere) writes exactly `κ_ch^{R_5}(S) = 2`, `κ_ch^{R_1}(S) =
2`, `κ_ch^{R_3}(S) = 24`. Counter: before accepting any
ClaimStatusProvedHere proposition, grep the enclosing file for
`\begin{remark}[.*retract\|.*category error\|.*confuses\|.*disambiguation]`
and cross-check the proposition's mechanism against every retraction
remark in the file. Healing: retag proposition and rename clauses to the
newly-canonical invariant. This is the AP300 specialisation for the case
where the downstream consumer is not an intermediate lemma but a
`ClaimStatusProvedHere` proposition — a more detection-resistant failure
mode because the proposition appears "published" to cursory reading.

**AP984 (Convention-split under single letter κ_ch: Hodge supertrace vs
complex dimension).** Two genuinely different invariants carried under the
κ_ch letter coexist across the manuscript without a bridge remark: (A)
Σ_q (-1)^q h^{0,q}(X) Künneth-multiplicative, (B) dim_C X additive under
products. At K3 × E the two disagree (0 vs 3). CLAUDE.md B90 pins (A) as
canonical. Sibling to AP234 (K-letter Trinity vs scalar-complementarity).
Counter: every κ_ch occurrence across Vol III must name the convention in
the enclosing remark, and cross-file bridge remark pins the canonical form.
Healing: rename (B)-convention occurrences to ρ^{R_i} or κ_fiber^{dim} per
HZ-7 closed subscript set; refuse bare κ_ch where the value is derived via
additivity under products.


## File paths

Audit loci:

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_six_routes_convergence.tex` —
  theorem, residual AP300 at lines 64, 404, 468–492, 513.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_six_routes_generator_level_platonic.tex` —
  pentagon structure (clean).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_pentagon_hypothesis_closures_platonic.tex` —
  hypothesis closures (out of scope).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex` —
  AP312 κ_ch = 3 drift (lines 333, 983, 1824, 3052).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex` —
  AP312 + AP149 N=1 coincidence (lines 980, 1137, 1250).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_algebra.tex` —
  AP312 + AP149 (lines 241, 449, 506, 512, 541).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex` —
  partial (line 932 correct, line 1115 drift).
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_cy_c_six_routes.py` —
  AP288/AP290 test relabeling needed (lines 130–157, 390–410).
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_cy_c_six_routes_generator_level.py` —
  not audited in this pass; secondary sweep recommended.

CLAUDE.md of Vol I does not carry a CY-C pentagon status row directly; the
B89/B90 entries and the CY-D row with the Hodge-supertrace identification
remain accurate post-heal. No Vol I edits required.
